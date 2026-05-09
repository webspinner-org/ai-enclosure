# agents/

Automation agents for the *AI Enclosure* manuscript.

---

## `illustrate.py`

Generates the book's illustrations from `ILLUSTRATIONS.md` using OpenAI's image API (`gpt-image-1` by default; `dall-e-3` is supported as a fallback).

### One-time setup

On modern macOS the system Python (Homebrew or otherwise) refuses `pip install` outside a virtualenv ([PEP 668](https://peps.python.org/pep-0668/)). The project ships a local `.venv/` for that reason.

```bash
# from the repo root, one time only:
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

# every shell session that will run the agent:
export OPENAI_API_KEY=sk-...
```

You can either run the script through the venv's Python directly (`.venv/bin/python agents/illustrate.py ...`) or activate the venv first (`source .venv/bin/activate`) and then call `python agents/illustrate.py ...`. The examples below show the direct-path form because it's robust against forgetting to activate.

`.venv/` and `requirements.txt` are at the repo root; the venv is gitignored, the requirements file is tracked.

### Common commands

```bash
# See every illustration the manifest knows about
.venv/bin/python agents/illustrate.py --list

# Print the prompts that would be sent, without calling the API
.venv/bin/python agents/illustrate.py --dry-run

# Generate just the cover (or any single slug from --list)
.venv/bin/python agents/illustrate.py --only cover

# Generate everything that isn't already on disk
.venv/bin/python agents/illustrate.py

# Regenerate something that already exists
.venv/bin/python agents/illustrate.py --only cover --force

# Generate at higher quality (more expensive)
.venv/bin/python agents/illustrate.py --quality high

# Use the older DALL·E 3 model instead of gpt-image-1
.venv/bin/python agents/illustrate.py --model dall-e-3
```

If you've activated the venv (`source .venv/bin/activate`), drop the `.venv/bin/` prefix and just say `python`.

### What it does

1. Reads `ILLUSTRATIONS.md` from the repo root.
2. For each entry in the script's `MANIFEST`, finds the matching heading in the markdown and extracts the `> ...` blockquote that follows as the image prompt.
3. Calls `client.images.generate(...)` with the prompt and the size specified for that illustration.
4. Decodes the returned base64 image and writes it to `ai-images/<slug>.png`.
5. Skips illustrations whose output file already exists, unless `--force` is passed.
6. Prints a summary at the end with counts for generated / skipped / failed.

### Cost guidance (gpt-image-1, May 2026 pricing)

| Quality | 1024×1024 | 1024×1536 / 1536×1024 | All 33 illustrations (mixed) |
|---|---|---|---|
| `low` | ~$0.011 | ~$0.016 | ~$0.45 |
| `medium` *(default)* | ~$0.042 | ~$0.063 | ~$1.80 |
| `high` | ~$0.167 | ~$0.250 | ~$7.00 |

The agent tells you the size and quality on each line before the API call, so you can stop early if you're surprised.

### Idempotency and recovery

- Every output filename is a deterministic slug. Re-running the script after an interruption resumes where it left off.
- If a generation fails (rate limit, content policy refusal, network error), the script logs the failure and continues to the next illustration. At the end it prints a list of failed slugs you can re-run with `--only`.
- Generated images are gitignored by default (see `.gitignore`). Move chosen images out of `ai-images/` and into a tracked location (or remove the gitignore entry) when you're ready to commit final artwork.

### Modifying the manifest

The list of illustrations to generate lives in the `MANIFEST` constant near the top of `illustrate.py`. Each entry is `(slug, heading_pattern, size)`. To add a new illustration:

1. Add a new section to `ILLUSTRATIONS.md` with a heading and a `> ...` blockquote prompt.
2. Add a new tuple to `MANIFEST` whose `heading_pattern` is a substring search that uniquely identifies the new section's heading.
3. Run `python agents/illustrate.py --only <slug>` to generate it.

### Caveats

- `gpt-image-1` may require organization verification on some accounts before access is granted. If you see `400` errors with permission-related messages, complete verification at https://platform.openai.com.
- Image models will mangle text in images. The Reference Architecture diagram is best rendered in a vector tool (Excalidraw / Figma / Draw.io) using the structured spec in `ILLUSTRATIONS.md`. The image-generation prompt for that diagram is provided as an aesthetic frontispiece, not as a label-precise diagram.
- Content-policy refusals happen occasionally. If a refusal is unjust, simplify the prompt's most evocative language and try again with `--force`.
