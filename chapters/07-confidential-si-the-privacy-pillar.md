# Chapter 7
## Confidential SI — The Privacy Pillar

> *Privacy is the power to selectively reveal oneself to the world.*
>
> — Eric Hughes, *A Cypherpunk's Manifesto* (March 9, 1993)

In March of 1993, on a mailing list of cryptographers, software engineers, and the politically restless, a Berkeley mathematician named Eric Hughes posted what would come to be called *A Cypherpunk's Manifesto*. The manifesto opens with a definition of privacy that has aged better than most of the technology that surrounded its writing. *Privacy is the power to selectively reveal oneself to the world.* Hughes was careful, in the lines that follow, to distinguish privacy from secrecy. A secret is something one does not want anyone to know. *Privacy* is something one wants some people to know in some contexts and not others — the choice of revelation, made by the person revealing.[^1]

That distinction is the philosophical foundation of this chapter. Privacy is not the absence of information about you. It is your *power* to govern what is known, by whom, on what occasions, for what purposes. The hyperscale Synthetic Intelligence architecture, as Chapter 3 argued, has structurally removed that power. The user submitting a prompt to a hyperscale service is not selectively revealing themselves to a synthetic intelligence. They are, by the architecture, surrendering custody of their query, their context, their history, and their working interior life to an operator they cannot inspect and a chain of downstream parties they cannot enumerate.

*Confidential SI* — the second pillar of Warp — is the architectural answer to that surrender. It is built on four primitives, each of which restores a portion of the power Hughes identified as the substance of privacy. Together, they re-establish the user as the principal who decides what is known and by whom.

This chapter describes those four primitives. Chapter 11 returns to the Cell as the unit of isolation in technical detail. Chapter 12 returns to WRAG as the federated retrieval mechanism. Chapter 15 returns to BYOK as the user's contractual root of trust. Chapter 17 returns to the full threat model and the residual risks the architecture does not eliminate. This chapter is the principle. The chapters that follow are the practice.

---

### The Federated Retrieval Primitive

The first primitive is *federated retrieval*.

Recall, from Chapter 3, the structural problem with the hyperscale path. When a user asks a hyperscale model a question that depends on private context — about their own documents, their own history, their own correspondence — the model can only answer well if it has access to that context. Hyperscale services solve the access problem by ingesting the user's data into the operator's facility, where it joins the operator's logs, the operator's training corpora, the operator's safety pipelines, and any preservation orders the operator's litigation has accumulated. The data goes *to* the model.

Federated retrieval inverts the direction.

In the Warp architecture, the user's data lives in the *Grimoire* of the user's own Cell. When a question is asked, the Weaver of the Cell first performs retrieval against the Grimoire — finding the relevant documents, conversation history, and contextual material from the user's own corpus. That retrieved material is then assembled into a prompt and presented to the model. The model can be a small local model running entirely on the user's own hardware (in which case nothing leaves the Cell), a peer Cell's specialized model running under federation contract (in which case only the retrieved material relevant to the query crosses the boundary), or a frontier model invoked under BYOK (in which case the relevant prompt material is sent under the user's own contractual relationship with the provider, not the operator's).

The key technical claim is that *the model does not need to have memorized the user's data to answer questions about it*. Retrieval-augmented generation, as a technique, is not new. The Warp architecture's contribution is to make retrieval *federated* — to insist, by design, that retrieval occurs against corpora the user owns or has explicitly federated with, rather than against an operator-curated index of everyone's data — and to enforce this at the architectural level.

Webspinner Retrieval-Augmented Grounding (WRAG), the subject of Chapter 12, is the protocol family that implements this primitive. It includes the embedding pipeline that lives in the Grimoire, the federation envelope that allows a query to traverse Cell boundaries under capability-scoped credentials, and the grounding mechanism that ensures the model's output is anchored in identifiable retrieved material rather than generated from the model's general training. The combined effect is that the model becomes a *reasoner* over the user's own knowledge, rather than a generator drawing on whatever it happens to remember from its training.

Two privacy consequences follow.

First, the user's data is not surrendered to the model provider. It is held in the user's Grimoire, retrieved when needed, presented as prompt material, and discarded from the model's working context when the inference completes. There is no accumulation. There is no persistent record on the operator's side beyond the immediate inference call. There is no training pipeline that absorbs the user's words.

Second, the *content of the user's corpus* — the medical records, the legal correspondence, the family photographs, the private journals, the proprietary business documents — never leaves the Cell at all unless the user has, by capability-scoped policy, explicitly authorized it. Even when frontier capability is invoked, only the *minimum necessary* prompt material crosses the Cell boundary. The Grimoire stays put.

This is not a privacy policy. It is a property of the architecture.

---

### Bring-Your-Own-Key as a Privacy Mechanism

The second primitive is *BYOK* — Bring Your Own Key — and it is widely misunderstood as a billing mechanism. It is, more importantly, a privacy mechanism.

In the standard hyperscale arrangement, the user's relationship with the model provider is mediated by the operator. The user pays a monthly fee to the operator. The operator pays the model provider. The conversations flow through the operator's pipeline. The contractual relationship that determines what the model provider may do with the user's data is the *operator's* contract with the provider, not the user's.

This is a substantively different legal posture than the user typically realizes. When the operator's contract with the provider permits training, the user's data may be used for training, regardless of what the operator's privacy policy says to the user. When the operator's contract permits aggregation, the user's data may be aggregated. When the provider issues a subpoena to the operator for the operator's records, the user is rarely a notified party. The user is the source of the data and the bearer of the privacy interest, but the user is not the contractual principal.

BYOK changes this. Under BYOK, when a Cell needs to invoke a frontier model — Claude, GPT, Gemini, or another commercial offering — the Cell uses the user's own API key, issued under the user's own account, governed by the user's own contractual relationship with the provider. The contract terms are the user's contract terms. The data-processing addenda are the user's data-processing addenda. The user pays the provider directly, on their own bill. There is no operator in the middle.

The privacy consequences are substantial:

- The user's contract with the provider, not the operator's, governs what may be done with the prompts and responses.
- The user can choose providers based on the privacy terms they offer (zero-data-retention agreements, regional processing restrictions, no-training clauses), rather than being limited to whatever terms the operator has negotiated for its enterprise tier.
- The user is the notified party for any subpoena, breach disclosure, or material change in the provider's policies.
- The user can revoke their key at any time, terminating future use without renegotiating with an intermediary.
- The user can rotate keys across providers — using one for routine work, another for sensitive queries, a third for tasks that should never touch a particular jurisdiction — based on their own sensitivity classifications.

BYOK is, in short, the mechanism by which the user becomes the *legal principal* in their own synthetic-intelligence relationships, rather than the third-party beneficiary of someone else's. It is the contractual analog of owning the laptop instead of leasing time on a mainframe.

---

### Cell-Level Isolation

The third primitive is *Cell-level isolation*.

A Cell is, by definition, the unit of privacy and capability boundary in the Warp architecture (Chapter 5). The hardware boundary is the boundary of the Cell. Data flows out of the Cell only by deliberate, owner-authorized action — encoded in policy, enforced by the Weaver, audited locally.

Cell-level isolation has technical and legal dimensions worth distinguishing.

The technical dimension is straightforward. The Cell's three tiers — Loom, Weaver, Grimoire — communicate over local interfaces. The Cell's boundary with the outside world is mediated by a single, narrow set of egress points: capability invocations to peer Cells under federation, model invocations under BYOK, and the user's interactive Loom sessions. Each egress is signed, logged locally, and policy-checked before transmission. There is no implicit data sharing. There is no telemetry pipeline phoning home. There is no remote diagnostic channel that bypasses the user's policy. *What leaves the Cell is what the user has authorized to leave the Cell*, and the burden is on the architecture to enforce that, not on the user to trust that an operator will behave.

The legal dimension is the one less commonly discussed. Because the Cell is owned by an identifiable principal — a person, a household, a small business, a community group — and because the data resident in the Cell is in the principal's custody, the legal framework that applies is the one that governs the principal's own property and records. A subpoena directed at hyperscale conversation logs reaches the operator's records. A subpoena for the contents of a user's Cell would, like a subpoena for any other personal record system, require service on the user, with whatever procedural protections the user's jurisdiction extends to personal records. The user is, again, the principal.

This matters more than it first appears. Most twentieth-century privacy law was built on the assumption that personal records lived in personal possession — a desk drawer, a filing cabinet, a home computer. The Fourth Amendment, the GDPR's controller/processor distinction, the doctor-patient and attorney-client privileges, the protections for journalistic source materials, the constitutional protections against compelled testimony — all of these are calibrated to a world in which the records are in the hands of the person whose records they are. Cell-level isolation restores the user to the position those legal frameworks were written to protect. *It does not require new law. It restores the user to the position the existing law already covered.*

---

### Sensitivity-Aware Routing

The fourth primitive is *sensitivity-aware routing*.

Not all queries have the same privacy stakes. A request to summarize today's news headlines is, in privacy terms, materially different from a request to draft a confidential medical opinion. The hyperscale architecture, in practice, treats all queries identically: every prompt flows through the same operator-controlled pipeline, with the same retention rules, the same eligibility for safety review, the same exposure to preservation orders and subpoenas. The user does not have a knob to set sensitivity, beyond the binary choice of whether to use the service at all.

The Warp architecture exposes the knob.

Within each Cell, the owner defines sensitivity classifications and their corresponding routing rules. A typical configuration might look like:

- **Public** — queries about general knowledge, public news, ordinary arithmetic, code in public repositories. Eligible for routing to any model provider, including the cheapest available. May be cached and reused across sessions. May be logged in the Cell's standard logs.
- **Personal** — queries involving the user's personal context (calendar, contacts, ordinary correspondence, household management). Permitted to invoke frontier models under BYOK with zero-retention terms. Must not be sent to providers without zero-retention terms in force. Cell-side logs are encrypted at rest.
- **Confidential** — queries involving client matters, medical material, financial detail, draft legal documents. May be processed only by local models running entirely within the Cell. May not invoke any external provider. Cell-side logs are encrypted with a key the user must specifically authorize to read.
- **Privileged** — queries involving attorney-client communication, religious confession, journalistic source protection, or other categories of communication for which jurisdictional law extends special protection. May be processed only by local models, and additionally subject to integrity-of-storage requirements that survive certain classes of compromise.

These classifications are the user's. The categories I have listed are illustrative; a Cell may define more, fewer, or differently named. What matters architecturally is that each query carries a sensitivity tag *before* the Weaver dispatches it, and the Weaver enforces the routing rules associated with the tag *before* any external invocation. A Confidential-class query that the Cell is configured to handle locally cannot be silently re-routed to an external provider, because the routing decision is made before egress and is auditable from the Cell's own logs.

The combination of Cell-level isolation and sensitivity-aware routing means that the user can use a single Cell, with a single working interface, for the full range of their synthetic-intelligence work — and the same architecture that conveniences the user with cheap external inference for their public queries can, simultaneously and without contradiction, refuse to let any sensitive material near an external provider.

This is not a feature. It is a routing primitive. It is to data flow what TCP is to packet flow: an architectural mechanism, not a policy preference.

---

### The Headline Promise

Combining the four primitives — federated retrieval, BYOK, Cell-level isolation, sensitivity-aware routing — the headline privacy promise of the Warp architecture is clean enough to state in one sentence.

*The user's data does not enter someone else's custody unless the user has, by deliberate policy, authorized it to do so for a specific purpose.*

That is the promise. It is the structural answer to every threat Chapter 3 enumerated:

- *Where does my data go?* It stays in your Cell. Cellular boundary is the boundary.
- *Will my conversations be used to train future models?* Not unless you authorize it for a specific provider, under a specific contract, that you signed.
- *What happens if the operator is sued?* You are not the operator's customer in a contractual sense; the operator does not have your conversations to produce.
- *What if the operator changes its policies?* Operator policies, in the conventional sense, do not govern your data, because your data is in your Cell. The Foundation can change the Warp specification, but the specification governs new deployments; existing Cells continue to operate under the rules they were configured with.
- *What if a future government compels disclosure?* Then the legal framework that applies is the framework that applies to your personal records, with whatever procedural protections your jurisdiction provides for them. The architecture restores the user to the legal position that the existing privacy law was written to protect.
- *What about the aggregation problem?* The aggregation engine of hyperscale — the centralized accumulation of hundreds of millions of users' conversations in a single operator's logs — does not exist in the Warp architecture, because there is no central operator and no central log. Aggregation, if it occurs, occurs only across the user's own Cell, by the user's own choice, for the user's own purposes.

The honest residual risks — what Cell-level isolation does *not* protect against — are the subject of Chapter 17. They include compromise of the user's own hardware, mishandling of capability-scoped federation, side-channel attacks on the Cell's network, and the inevitable category of risks that come from human error in policy configuration. Confidential SI is not a guarantee. It is a structural improvement of multiple orders of magnitude over the present arrangement, and it is the strongest privacy posture the Foundation knows how to design.

---

### What This Pillar Does for the Reader

If you are a doctor in private practice, Confidential SI means your patient records do not have to live on a hyperscaler's servers to benefit from synthetic-intelligence assistance.

If you are an attorney, Confidential SI means your privileged communications, your work product, and your client confidences do not have to be entrusted to a third-party operator whose subpoena exposure you cannot control.

If you are a journalist, Confidential SI means your source materials do not have to be deposited with an operator whose preservation orders can be served, whose compliance team can be subpoenaed, and whose internal reviewers can be compelled.

If you are a small-business owner, Confidential SI means your customer relationships, your financial records, and your trade secrets stay on hardware you own, governed by contracts you signed, processed by capability-scoped models you have authorized.

If you are a parent, Confidential SI means the queries your family asks of synthetic intelligence — the schoolwork help, the medical questions, the relationship struggles, the small private moments that ordinary families have always handled at home — stay at home, where the law and the architecture and your own custody can all keep them.

If you are an ordinary person who has, until now, been told that synthetic intelligence requires you to surrender these things in order to have access to it, Confidential SI is the answer. *It does not.* The architecture has been designed to give you access to the technology without that surrender.

The next pillar — Sovereign SI — extends the privacy argument into the deeper question of what it means to *own* a synthetic intelligence at all.

---

## Endnotes

[^1]: Eric Hughes, *A Cypherpunk's Manifesto* (March 9, 1993). The original posting circulated on the cypherpunks mailing list and is now hosted in multiple archives. Canonical text via activism.net: https://www.activism.net/cypherpunk/manifesto.html. Nakamoto Institute archive (plain-text): https://nakamotoinstitute.org/static/docs/cypherpunk-manifesto.txt. The opening passage in full reads: "Privacy is necessary for an open society in the electronic age. Privacy is not secrecy. A private matter is something one doesn't want the whole world to know, but a secret matter is something one doesn't want anybody to know. Privacy is the power to selectively reveal oneself to the world." Hughes' insistence on the *positive* definition of privacy — as the capacity to govern revelation — anchors this chapter's framing.
