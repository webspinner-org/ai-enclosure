# CLAUDE.md — Canon for AI Enclosure

This file is the single source of truth for the *AI Enclosure* book project.
**Read this in full before any writing or editing work in this repository.**

---

## Title (Locked)

- **Title:** AI Enclosure
- **Subtitle:** Why Sovereign Intelligence Demands Warp Speed
- **Author:** John D. Marx, Founder, The Webspinner Foundation

The "AI" in the title is deliberate — it meets readers where they are. The body of the book uses **SI** (Synthetic Intelligence) instead.

---

## The Thesis (One Sentence)

> Warp is Moral AI: synthetic intelligence that you own, that you can inspect, that cannot be repurposed without your consent, and whose environmental and economic costs are bounded by your own choices rather than imposed by a centralized operator.

---

## Terminology Rules (Strict)

These are non-negotiable. Drift here is the most common failure mode.

| Use | Don't Use | Notes |
|-----|-----------|-------|
| Synthetic Intelligence (SI) | Artificial Intelligence (AI) | "AI" permitted in title only. Body text uses SI. |
| Sovereign Intelligence | Sovereign AI | Names both human and synthetic sovereignty; avoids the nationalist capture of "Sovereign AI." |
| Warp | the Webspinner architecture | Capitalize as proper noun. |
| Cell | tenant, instance, server | The privacy/capability boundary unit. |
| Loom | front-end, UI tier | Front-end role within a Cell. |
| Weaver | inference server, AI tier | Orchestration/AI role within a Cell. |
| Grimoire | database, storage tier | Data role within a Cell. |
| WRAG | RAG, retrieval | Webspinner Retrieval-Augmented Grounding. |
| BYOK | bring-your-own-key | Bring Your Own Key. |
| Hyperscale AI / Hyperscalers | Big AI, frontier labs | What Warp opposes. |
| The Webspinner Foundation | Webspinner LLC, Webspinner Cloud | Use Foundation framing for moral/movement claims. |

---

## The Four Pillars of Warp

1. **Green SI** — environmental sustainability through Apple Silicon idle economics, federated compute, and edge offload.
2. **Confidential SI** — privacy through federated retrieval, BYOK, and Cell isolation.
3. **Sovereign SI** — user ownership: the right to inspect, modify, refuse, and disconnect.
4. **Moral AI** — the ethical outcome: SI that cannot be conscripted into purposes the user does not consent to.

The **Value Triangle** (lower cost, greater speed, better quality) is the proof that these pillars are not tradeoffs.

---

## Voice and Tone

- **Authority:** Inventor's voice. The author lived through the PC revolution, built on it, and is making the parallel argument for Synthetic Intelligence.
- **Stakes:** Alarmist where the stakes are real. The "largest single threat" framing in the Note on Terminology is intentional and stays.
- **Discipline:** Technical claims need backing. Architectural arguments need real numbers.
- **Cadence:** PC-era parallels welcome. First-person used sparingly, mostly in the Foreword.
- **Register:** Thoughtful general reader. Not academic. Not technologist-only.

---

## The Antagonist Frame

Hyperscale AI is the structural antagonist of the book — not any specific company, not specific people. The argument is about *concentration*, not *malice*. Critique the structure, the incentives, and the consequences. Avoid attacks on individuals.

---

## Do-Not-Drift List

Things we have decided NOT to do, regardless of reader or reviewer pressure:

- Do not soften the moral language to be more palatable to enterprise readers.
- Do not call SI "AI" in the body of the book.
- Do not frame Warp as a product pitch. It is an architecture and a movement.
- Do not retreat from the four-pillar structure. Sovereign SI and Moral AI are the strongest pillars, not the most marketable — keep them prominent.
- Do not treat sovereignty as a technical feature. It is a moral imperative.
- Do not let the Value Triangle dilute the moral case. It is the proof, not the argument.
- Do not adopt corporate AI-industry euphemisms ("alignment," "responsible AI," "guardrails") as load-bearing terms. Critique them where relevant; do not borrow them.

---

## Working Process

- One chapter per file in `chapters/`, named `NN-slug.md` (e.g., `03-the-privacy-collapse.md`).
- All decisions go in `DECISIONS.md` with dates. Append-only.
- Open threads go in `OPEN_QUESTIONS.md`. Promote to DECISIONS.md when settled.
- Read `OUTLINE.md` for the current chapter map.
- Commit early and often. Per-chapter commits with meaningful messages.

---

## Operational Reminders

- The Pro Max subscription is the auth path for Claude Code in this repo. The `ANTHROPIC_API_KEY` environment variable must remain unset to avoid auth conflict.
- The repo is on the M5 Max MacBook Pro (Spindle).
- The book is the deliverable. The repo is the working surface. Treat the repo as if it might one day be made public.
