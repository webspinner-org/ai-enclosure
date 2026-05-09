# Chapter 12
## WRAG — Webspinner Retrieval-Augmented Grounding

> *Consider a future device for individual use, which is a sort of mechanized private file and library... A memex is a device in which an individual stores all his books, records, and communications, and which is mechanized so that it may be consulted with exceeding speed and flexibility.*
>
> — Vannevar Bush, "As We May Think," *The Atlantic* (July 1945)

In July 1945, in the closing weeks of the Second World War, Vannevar Bush — the engineer who had run American wartime research from the Office of Scientific Research and Development — published an essay in *The Atlantic* titled "As We May Think." The essay imagined a postwar device he called the *memex*: a personal information system in which an individual could store the books, records, correspondence, and accumulated knowledge of a working life, indexed not by the rigid taxonomies of the librarian but by *associations* — links between ideas the way the human mind itself moves between them.[^1]

The memex was never built in the form Bush imagined. The technology of 1945 could not yet support it, and the technology of subsequent decades took different paths — first databases, then hypertext, then the World Wide Web, then search engines, then personal cloud storage. But the *concept* — that an individual ought to have a personal mechanized memory, organized for their own retrieval, governed by their own associations — has remained one of the unfinished projects of the computing era.

WRAG — the *Webspinner Retrieval-Augmented Grounding* protocol — is the Foundation's contribution to finishing it. WRAG is what happens when retrieval-augmented generation (the now-standard pattern of grounding language-model output in retrieved context) meets the Cell architecture (in which the corpus retrieved from is the user's own Grimoire, governed by the user's own keys, federated only with the user's authorization). The result is a personal memex with synthetic-intelligence reasoning attached — Bush's vision finally tractable, eighty years late.

This chapter describes the protocol.

---

### Grounding vs. Generation

The first and most important thing to understand about WRAG is the philosophical distinction between *grounding* and *generation*.

A standard large language model, in its native operation, *generates*. Given a prompt, it produces a continuation by drawing on the patterns it has absorbed during training. The continuation is, in some sense, the model's best guess at what should follow the prompt, based on a vast statistical compression of the training corpus. The continuation is *plausible* with respect to the training distribution. It is not necessarily *true* with respect to any particular fact, source, or context the model was not specifically trained on.

This is the well-known *hallucination* problem. A purely generative model, asked about a specific document, a specific person, or a specific event, will frequently produce a confident-sounding answer that bears no specific relationship to the actual document, person, or event in question. The output sounds right. It is not, in any verifiable sense, sourced.

*Grounding* is the discipline of constraining the model's output to *identifiable* source material. In a grounded system, the model is given, alongside the user's query, the relevant retrieved passages from a corpus the system has access to. The model is instructed — by prompt design, by fine-tuning, by output-validation — to base its response on those passages, to cite them where appropriate, to acknowledge when the retrieved material does not address the query, and to refuse to fabricate beyond what the sources support.

Grounding does not eliminate hallucination — no current technique fully does — but it dramatically reduces it. More importantly, grounding *makes hallucination detectable*. A grounded response that does not match its cited sources is an obvious failure that the user (or the Cell's audit pipeline) can catch. A purely generative response has no comparable check.

WRAG is a grounding protocol. It is built on the assumption that *the model the Cell uses is, in its native operation, a generator* — a useful generator, often an excellent generator, but a generator nonetheless — and that turning a generator into a reliable assistant requires *attaching it to a corpus the user controls* and *constraining its output to the materials the corpus provides.*

This is, in a sense, the deepest design choice of the Warp architecture. *We do not ask the model to know the user. We ask the model to reason about what the Grimoire has retrieved.* The Grimoire is the seat of the user's accumulated knowledge. The model is a reasoner the user has temporarily invited to work with that knowledge. The two roles are kept distinct, and the architecture maintains the distinction.

---

### The Retrieval Pipeline

A WRAG-enabled Cell processes a user query through a pipeline whose stages are worth naming explicitly.

**Stage 1: Query Understanding.** The Loom passes the user's query to the Weaver. The Weaver performs an initial light analysis to determine what kind of query this is — does it require retrieval at all (some queries, like "draft a poem about autumn," may not), and if so, what kind of corpus is relevant. A query about the user's medical records, a query about their work documents, a query about a specific federation peer's shared knowledge base, and a query about today's news headlines all route differently. The Weaver tags the query with a sensitivity classification (Chapter 7) and a corpus scope.

**Stage 2: Retrieval.** Based on the corpus scope, the Weaver issues retrieval requests against the Grimoire (for the user's own corpus) and against any federated Grimoires the query has been authorized to reach. Retrieval is, in the typical case, a hybrid of *semantic* retrieval (vector similarity against pre-computed embeddings of the corpus) and *lexical* retrieval (keyword matching, where appropriate). The Foundation's reference Grimoire implementation supports both, with the specific weights tunable by the Cell's owner.

**Stage 3: Re-ranking.** The retrieved passages are re-ranked by relevance to the query, using a smaller fast model that can quickly score the retrieved candidates. Re-ranking is critical because vector retrieval, while fast, is not always precise; a re-ranking pass with a more discriminating model produces materially better top-k results.

**Stage 4: Context Assembly.** The top-ranked passages are assembled into a structured context that will be passed to the answering model. The assembly preserves the source of each passage — the document, the timestamp, the author, the federation source if applicable — so that the answering model can cite, and so that the Cell's audit logs can trace each output to its inputs. Context-window management decides how much of the retrieved material can fit alongside the user's query.

**Stage 5: Inference.** The assembled context, the user's query, and the Cell's prompt template (which includes the grounding instructions) are passed to the model — local, federated, or BYOK frontier, as the sensitivity rules permit. The model produces a response.

**Stage 6: Grounding Verification.** The response is checked against the retrieved context. Citations are validated. Specific factual claims that purport to be grounded in the retrieved material are spot-checked. Where the response includes content that does not appear to be supported by the retrieved context, the response is either re-prompted with stronger grounding constraints or returned to the user with a flag noting the potential ungrounded segment.

**Stage 7: Response Delivery.** The verified response is delivered to the Loom and shown to the user. The full retrieval-and-grounding trace — what was retrieved, what was used, what was cited — is logged in the Grimoire under the user's audit-log policy. The user can inspect the trace at any time.

This pipeline is more elaborate than the typical naïve RAG implementation. It is also closer to what reliable, production-grade synthetic intelligence work actually requires. The Foundation has chosen to bake the elaboration into the architecture rather than leave it as an exercise for individual deployers, on the principle that the *default* behavior of a Warp Cell ought to be the *correct* behavior.

---

### Federated Retrieval in Practice

The retrieval pipeline above describes the case of querying the user's own Grimoire. The federated case is similar in structure but has important distinctions worth describing.

When a query's corpus scope includes federated peers, the Weaver issues retrieval requests to those peers — *not* by replicating the peers' corpora locally, but by invoking the peers' retrieval capabilities via the Capability Bus (Chapter 13). The peer's Cell performs the retrieval against its own Grimoire, returns the relevant passages (or pointers to them), and the calling Weaver assembles the federated results alongside its own local retrieval into the context that goes to the answering model.

Several properties of federated retrieval are worth emphasizing:

- **The peer's corpus does not leave the peer's Grimoire.** Only the relevant passages, retrieved against the calling Cell's query, traverse the federation boundary. The full corpus stays put.
- **The peer has the right to refuse.** Federated retrieval is a capability the peer Cell offers, on the peer's terms, with capability-scoped credentials. A peer can refuse a particular query, refuse a particular caller, refuse a particular topic, or revoke access at any time.
- **Privileged passages can be marked.** A peer Cell offering federated retrieval can mark certain materials as available only to certain capability scopes — public documents to general callers, sensitive materials to vetted callers, restricted materials never federated. The peer's owner controls the granularity.
- **The federation is auditable on both sides.** Both the calling Cell and the peer Cell log the federation activity. A community Cell that offers federated retrieval to its members has a complete record of what was queried, by whom, when — visible to both the community and the individual querier.

The cumulative effect is that a Warp user, operating their own Cell, has access to *the union of corpora they have been authorized to query*, via federation, without any of those corpora living in a centralized index controlled by an operator. The aggregation problem of Chapter 3 — that hyperscale services concentrate everyone's data in a single operator's logs — does not exist in the federated retrieval model, because there is no central operator, no central log, and no central corpus.

---

### Why Standard RAG Isn't Enough

The general technique of retrieval-augmented generation is not novel to Warp. The pattern has been deployed in commercial settings since at least 2020 and has become a standard component of enterprise synthetic-intelligence offerings. Why does the Foundation argue that *standard* RAG is insufficient and that WRAG specifically is required?

The answer has three parts.

First, *standard RAG runs in the operator's data center*. The user's corpus, in the standard pattern, is ingested into the operator's infrastructure, indexed by the operator's pipeline, retrieved by the operator's retrieval system, and used by the operator's models. Every privacy issue Chapter 3 enumerated applies to the standard RAG corpus as much as to the standard prompt. The corpus is in the operator's custody. The retrievals are in the operator's logs. The decisions about how the corpus is indexed and retrieved are the operator's decisions, not the user's.

WRAG runs in the user's Cell. The corpus stays in the user's Grimoire. The retrievals are local. The indexing is the user's choice. The corpus does not enter the operator's facility, period.

Second, *standard RAG is single-corpus*. The user has one corpus, in one place, governed by one access policy, queryable as one resource. WRAG is *federated by design*. The user's corpus, the user's family's corpus, the user's small business's corpus, the user's community's corpus, and any other corpora the user has been authorized to federate with are all queryable as a structured collection, with the appropriate scopes and restrictions enforced at each boundary. This is what *real* knowledge work looks like — drawing from one's own materials, one's collaborators' materials, one's institutional materials, one's publicly available references — and it is what the architecture supports.

Third, *standard RAG often skips grounding verification*. Many production RAG systems assemble the retrieved context, pass it to the model, and return whatever the model produces, with no automated check that the response is actually grounded in the retrieved material. The ungrounded portions slip through, and the user (or, worse, downstream users of the user's output) cannot tell which portions came from sources and which were generated. WRAG bakes grounding verification into the pipeline as a default, with the verification stage itself being inspectable from the audit log.

These three differences — *user-side corpus, federated by design, verification-required* — are not minor. They are the difference between "a retrieval system that happens to work for synthetic intelligence" and "a synthetic intelligence system designed for the user's sovereign use."

---

### What WRAG Enables

To make the abstract concrete, here are several patterns of work that WRAG enables and that hyperscale RAG does not, in the same form.

**The personal research assistant.** A working professional with twenty years of accumulated documents — papers they have read, notes they have taken, drafts they have produced, correspondence they have exchanged — ingests this corpus into their Grimoire. WRAG turns the corpus into a queryable knowledge base their synthetic intelligence can reason against. The professional can ask questions like "what did I think about this when I encountered it three years ago" and receive a grounded answer, citing their own past notes.

**The small-firm institutional memory.** A law firm, medical practice, or design studio aggregates its institutional corpus — case files, treatment notes, project archives — into the firm's Sovereign Cell. Each professional in the firm queries against the institutional memory under role-based federation. New employees come up to speed by querying the firm's history; departing employees take their personal corpora with them while leaving the institution's intact.

**The community knowledge base.** A neighborhood association, a religious congregation, a school district maintains a community Cell whose Grimoire holds the community's shared materials — documents of record, reference materials, accumulated wisdom from elders and long-tenured members. Community members query this knowledge base from their personal Cells, with the community's own access rules governing what is available to whom.

**The cross-organizational research federation.** Several independent research groups working on related topics establish a federation of Cells that share specific corpora — published papers, anonymized datasets, methodological notes. Members of each group query across the federation under their own affiliations, with each group retaining control over what it contributes and to whom.

**The cross-time-and-context personal assistant.** Each member of a household has personal materials in their own Cell, plus selective access to the household's shared corpus (calendars, household documents, financial materials of the family). Queries that involve "household-and-mine" context are routed through both Grimoires, with each enforcing its own privacy rules.

These patterns are not exotic. They are the kinds of work that ordinary professionals, small organizations, and communities do every day — and that the hyperscale architecture has, until now, required them to either give up doing well or give up doing privately.

---

### Where WRAG Falls Short

I want to close, as the previous chapters have, with an honest accounting of what WRAG does not solve.

WRAG does not eliminate hallucination. Even with verification, models occasionally produce ungrounded content; the verification stage catches most of it but not all. WRAG reduces the rate and surface-area of hallucination, but the user is still expected to verify output for high-stakes decisions.

WRAG depends on the quality of the user's corpus. A Grimoire full of low-quality, contradictory, or out-of-date materials produces low-quality, contradictory, or out-of-date answers. Garbage in, garbage out, as always. The Foundation's guidance and the reference Grimoire tooling include provisions for corpus hygiene — provenance tracking, deprecation flags, contradiction detection — but the *content* of the corpus is the user's responsibility.

WRAG cannot substitute for capability the model does not have. A small local model with WRAG over the user's corpus is, for many tasks, better than a frontier model without that grounding — but for tasks that require frontier-scale reasoning capability that the small model genuinely lacks, the user can and should invoke a frontier model under BYOK, with the WRAG retrieval producing the prompt context. WRAG composes with frontier invocation; it does not replace it.

WRAG inherits the privacy properties of the Grimoire. If the Grimoire is on hardware whose physical security has been compromised, or if the Grimoire's encryption keys have been revealed, no protocol can recover what the underlying custody has lost. WRAG is part of a defense-in-depth architecture; it is not the whole defense.

These limitations are the honest residual. They are dramatically smaller than the limitations of the alternatives. They are the limits within which the architecture works, and they are the limits the user must work within when operating the architecture.

The next chapter describes the Capability Bus — the messaging fabric that lets all of these federated WRAG queries actually traverse Cell boundaries.

---

## Endnotes

[^1]: Vannevar Bush, "As We May Think," *The Atlantic Monthly*, July 1945. https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/. The essay was written in the closing months of the Second World War, during which Bush directed the Office of Scientific Research and Development. The memex idea — a personal mechanized library and association engine — has been a touchstone for personal-computing visionaries from Doug Engelbart and Ted Nelson onward. For the lineage: Engelbart's 1962 SRI paper "Augmenting Human Intellect: A Conceptual Framework" and Nelson's 1965 "Complex information processing: a file structure for the complex, the changing and the indeterminate" are the canonical follow-ons.
