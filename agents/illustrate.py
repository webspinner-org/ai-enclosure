#!/usr/bin/env python3
"""
agents/illustrate.py — Generate book illustrations from ILLUSTRATIONS.md
using OpenAI's gpt-image-1 model.

Setup:
    pip install openai
    export OPENAI_API_KEY=sk-...

Usage:
    python agents/illustrate.py --list             # show all illustrations and exit
    python agents/illustrate.py --dry-run          # print prompts without calling the API
    python agents/illustrate.py --only cover       # generate just one
    python agents/illustrate.py                    # generate every illustration not yet on disk
    python agents/illustrate.py --force            # regenerate even existing files
    python agents/illustrate.py --quality high     # high quality (more expensive)

Output:
    Images are written to ai-images/<slug>.png at the repo root.
    Files that already exist are skipped unless --force is passed.

Cost note (May 2026 pricing for gpt-image-1):
    Quality 'low'    ≈ $0.011–0.016 per image
    Quality 'medium' ≈ $0.042–0.063 per image
    Quality 'high'   ≈ $0.167–0.250 per image
    The full manuscript is 33 illustrations. Budget accordingly.
"""

from __future__ import annotations

import argparse
import base64
import os
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Manifest of illustrations.
#
# Each entry is (slug, heading_pattern, size).
#
# - slug:            output filename (ai-images/<slug>.png) and CLI selector.
# - heading_pattern: a substring search within ILLUSTRATIONS.md. The first
#                    match in document order is used; the FIRST `> ...`
#                    blockquote after that match becomes the prompt.
# - size:            "1024x1024" (square), "1024x1536" (portrait),
#                    or "1536x1024" (landscape).
# ---------------------------------------------------------------------------

MANIFEST: list[tuple[str, str, str]] = [
    # Cover (two concepts; both generated)
    ("cover",                              "## Cover",                                            "1024x1536"),
    ("cover-alt",                          "**Alternative cover concept",                         "1024x1536"),

    # Front matter
    ("front-author-note",                  "### A Note on Authorship",                            "1024x1024"),
    ("front-foreword",                     "### Foreword",                                        "1024x1024"),
    ("front-terminology",                  "### A Note on Terminology",                           "1024x1024"),

    # Part I — The Why
    ("ch-01-hyperscale-trap",              "### Chapter 1 — The Hyperscale Trap",                "1536x1024"),
    ("ch-02-concentration",                "### Chapter 2 — The Concentration Problem",          "1536x1024"),
    ("ch-03-privacy-collapse",             "### Chapter 3 — The Privacy Collapse",               "1536x1024"),
    ("ch-04-lessons",                      "### Chapter 4 — The Lessons of Computing History",   "1536x1024"),

    # Interlude
    ("interlude-treasure-fleets",          "## Interlude — The Treasure Fleets",                  "1536x1024"),

    # Part II — The What
    ("ch-05-defining-warp",                "### Chapter 5 — Defining Warp",                       "1024x1024"),
    ("ch-06-green-si",                     "### Chapter 6 — Green SI",                            "1536x1024"),
    ("ch-07-confidential-si",              "### Chapter 7 — Confidential SI",                     "1024x1024"),
    ("ch-08-sovereign-si",                 "### Chapter 8 — Sovereign SI",                        "1024x1024"),
    ("ch-09-moral-ai",                     "### Chapter 9 — Moral AI",                            "1024x1024"),
    ("ch-10-value-triangle",               "### Chapter 10 — The Value Triangle",                 "1024x1024"),

    # Part III — The How
    ("ch-11-cells",                        "### Chapter 11 — Cells",                              "1024x1024"),
    ("ch-12-wrag",                         "### Chapter 12 — WRAG",                               "1536x1024"),
    ("ch-13-capability-bus",               "### Chapter 13 — The Capability Bus",                 "1536x1024"),
    ("ch-14-compute-farm",                 "### Chapter 14 — The Compute Farm",                   "1536x1024"),
    ("ch-15-byok",                         "### Chapter 15 — BYOK",                               "1024x1024"),
    ("ch-16-architecture-of-sovereignty",  "### Chapter 16 — The Architecture of Sovereignty",    "1024x1024"),
    ("ch-17-privacy-by-design",            "### Chapter 17 — Privacy by Design",                  "1536x1024"),

    # Part IV — The Versus
    ("ch-18-cost-compared",                "### Chapter 18 — Cost Architectures Compared",        "1536x1024"),
    ("ch-19-environmental-compared",       "### Chapter 19 — Environmental Footprints Compared",  "1536x1024"),
    ("ch-20-privacy-compared",             "### Chapter 20 — Privacy Postures Compared",          "1536x1024"),
    ("ch-21-capability-compared",          "### Chapter 21 — Capability and Quality Compared",    "1024x1024"),
    ("ch-22-refused-uses",                 "### Chapter 22 — What Centralized AI Is Used For",    "1536x1024"),

    # Part V — The Mission
    ("ch-23-democratization",              "### Chapter 23 — What Democratization Actually Means","1536x1024"),
    ("ch-24-pc-parallel",                  "### Chapter 24 — The PC Parallel",                    "1536x1024"),
    ("ch-25-webspinners-role",             "### Chapter 25 — Webspinner's Role",                  "1024x1024"),
    ("ch-26-cooperative-ethic",            "### Chapter 26 — The Cooperative Ethic",              "1536x1024"),
    ("ch-27-path-forward",                 "### Chapter 27 — The Path Forward",                   "1536x1024"),

    # WARP Reference Architecture diagram (image-generation variant only;
    # the structured spec is meant for vector-tool rendering, not for an
    # image model)
    ("warp-reference-architecture",        "### 2. Image-Generation Prompt",                      "1536x1024"),
]


REPO_ROOT = Path(__file__).resolve().parent.parent
ILLUSTRATIONS_FILE = REPO_ROOT / "ILLUSTRATIONS.md"
OUTPUT_DIR = REPO_ROOT / "ai-images"


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------

def extract_prompt(markdown: str, heading_pattern: str) -> str:
    """Find heading_pattern in markdown; return the next blockquote as one string.

    A "blockquote" is the run of consecutive lines starting with `> ` (and
    `>`-only lines that mark blank paragraphs inside the block) immediately
    following the heading. Lines between the heading and the start of the
    blockquote are skipped — there is typically a blank line plus, in some
    sections, a `**Prompt:**` marker.
    """
    idx = markdown.find(heading_pattern)
    if idx == -1:
        raise ValueError(f"heading not found: {heading_pattern!r}")

    rest = markdown[idx:]
    lines = rest.split("\n")

    prompt_lines: list[str] = []
    in_block = False
    # Skip the heading line itself
    for line in lines[1:]:
        if line.startswith("> "):
            prompt_lines.append(line[2:])
            in_block = True
        elif line.strip() == ">":
            prompt_lines.append("")
            in_block = True
        elif in_block:
            # First non-`>` line after we've started accumulating ends the block
            break
        # else: pre-blockquote text (like "**Prompt:**" or blank line); skip

    if not prompt_lines:
        raise ValueError(f"no `> ...` blockquote found after heading {heading_pattern!r}")

    return "\n".join(prompt_lines).strip()


# ---------------------------------------------------------------------------
# Image generation
# ---------------------------------------------------------------------------

def write_image_from_response(response, out_path: Path) -> None:
    """Save the first image from an OpenAI image-generation response to disk.

    gpt-image-1 returns base64. dall-e-3 may return either b64 or a URL.
    We handle both for portability.
    """
    datum = response.data[0]
    b64 = getattr(datum, "b64_json", None)
    if b64:
        out_path.write_bytes(base64.b64decode(b64))
        return
    url = getattr(datum, "url", None)
    if url:
        import urllib.request
        urllib.request.urlretrieve(url, out_path)
        return
    raise RuntimeError("response contained neither b64_json nor url")


def generate_one(client, slug: str, prompt: str, size: str,
                 model: str, quality: str, out_path: Path) -> None:
    """Call the OpenAI image API for a single illustration."""
    kwargs = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "n": 1,
    }
    # gpt-image-1 supports quality; dall-e-3 supports a different quality field
    if model == "gpt-image-1":
        kwargs["quality"] = quality  # low | medium | high | auto
    elif model == "dall-e-3":
        # dall-e-3 quality is "standard" or "hd"
        kwargs["quality"] = "hd" if quality in ("high", "auto") else "standard"

    response = client.images.generate(**kwargs)
    write_image_from_response(response, out_path)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate book illustrations from ILLUSTRATIONS.md.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--list", action="store_true",
                        help="list all illustrations and exit")
    parser.add_argument("--only", type=str, metavar="SLUG",
                        help="generate only the named slug (use --list to see them)")
    parser.add_argument("--dry-run", action="store_true",
                        help="print prompts without calling the API")
    parser.add_argument("--force", action="store_true",
                        help="regenerate even if output file already exists")
    parser.add_argument("--quality", default="medium",
                        choices=["low", "medium", "high", "auto"],
                        help="image quality (default: medium)")
    parser.add_argument("--model", default="gpt-image-1",
                        help="OpenAI image model (default: gpt-image-1)")
    parser.add_argument("--sleep", type=float, default=1.0,
                        help="seconds to sleep between API calls (default: 1.0)")
    args = parser.parse_args()

    # Load the manifest's source markdown
    if not ILLUSTRATIONS_FILE.exists():
        print(f"ERROR: {ILLUSTRATIONS_FILE} not found", file=sys.stderr)
        return 1
    markdown = ILLUSTRATIONS_FILE.read_text(encoding="utf-8")

    # --list
    if args.list:
        print(f"{'SLUG':<40} {'SIZE':<12} HEADING")
        print("-" * 100)
        for slug, heading, size in MANIFEST:
            print(f"{slug:<40} {size:<12} {heading}")
        print(f"\n{len(MANIFEST)} illustrations total.")
        return 0

    # Filter
    work = MANIFEST
    if args.only:
        work = [m for m in MANIFEST if m[0] == args.only]
        if not work:
            print(f"ERROR: slug not found: {args.only!r}", file=sys.stderr)
            print("Run with --list to see available slugs.", file=sys.stderr)
            return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # --dry-run
    if args.dry_run:
        for slug, heading, size in work:
            print(f"\n=== {slug}  ({size}) ===")
            try:
                prompt = extract_prompt(markdown, heading)
                print(prompt)
            except ValueError as e:
                print(f"ERROR: {e}")
        return 0

    # Real run — needs API key
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable is not set.", file=sys.stderr)
        print("Set it with: export OPENAI_API_KEY=sk-...", file=sys.stderr)
        return 1

    try:
        from openai import OpenAI
    except ImportError:
        print("ERROR: openai package not installed.", file=sys.stderr)
        print("Install it with: pip install openai", file=sys.stderr)
        return 1

    client = OpenAI()  # picks up OPENAI_API_KEY automatically

    total = len(work)
    succeeded: list[str] = []
    skipped: list[str] = []
    failed: list[tuple[str, str]] = []

    for i, (slug, heading, size) in enumerate(work, start=1):
        out_path = OUTPUT_DIR / f"{slug}.png"

        if out_path.exists() and not args.force:
            print(f"[{i}/{total}] {slug}: skipped (exists; --force to regenerate)")
            skipped.append(slug)
            continue

        try:
            prompt = extract_prompt(markdown, heading)
        except ValueError as e:
            print(f"[{i}/{total}] {slug}: SKIP — {e}", file=sys.stderr)
            failed.append((slug, str(e)))
            continue

        print(f"[{i}/{total}] {slug} ({size}, {args.quality}): generating...", flush=True)
        try:
            generate_one(
                client=client,
                slug=slug,
                prompt=prompt,
                size=size,
                model=args.model,
                quality=args.quality,
                out_path=out_path,
            )
            print(f"           → {out_path.relative_to(REPO_ROOT)}")
            succeeded.append(slug)
        except Exception as e:  # noqa: BLE001 — we want to keep going on any error
            print(f"           ✗ FAILED: {type(e).__name__}: {e}", file=sys.stderr)
            failed.append((slug, f"{type(e).__name__}: {e}"))

        # Light pacing between calls
        if i < total:
            time.sleep(args.sleep)

    # Summary
    print()
    print(f"Summary: {len(succeeded)} generated, {len(skipped)} skipped, {len(failed)} failed.")
    if failed:
        print("\nFailures:")
        for slug, err in failed:
            print(f"  {slug}: {err}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
