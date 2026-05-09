# Chapter 11
## Cells — The Building Block

> *Each pattern describes a problem which occurs over and over again in our environment, and then describes the core of the solution to that problem, in such a way that you can use this solution a million times over, without ever doing it the same way twice.*
>
> — Christopher Alexander et al., *A Pattern Language* (1977)

In 1977, the architect Christopher Alexander and his colleagues at the Center for Environmental Structure at Berkeley published *A Pattern Language: Towns, Buildings, Construction* — a 1,200-page catalog of 253 architectural patterns, ranging from city-scale ("Independent Regions") to door-handle-scale ("A Place to Wait"). The book proposed that good architecture is not a series of one-off creative gestures but the disciplined composition of recurring patterns, each pattern naming a problem and offering the core of a solution that can be adapted to a million local circumstances without ever repeating itself exactly.[^1]

The Cell is the foundational pattern of the Warp architecture. This chapter describes the pattern in technical detail — the three roles, why those particular boundaries, how Cells compose into larger structures, and how Cells federate with one another. The chapter is, by Alexander's standards, *one pattern.* Subsequent chapters describe the patterns that compose with it: WRAG (Chapter 12), the Capability Bus (Chapter 13), the Compute Farm (Chapter 14), BYOK (Chapter 15), the Architecture of Sovereignty (Chapter 16), and Privacy by Design (Chapter 17).

Each pattern describes a problem and offers the core of a solution. The Cell's problem is: *how do we deploy synthetic intelligence under a single owner's control, in a way that can compose with other deployments without surrendering that control?* The Cell's solution is the substance of this chapter.

---

### The Three Roles

A Cell has three roles, each implemented by software running within the Cell's hardware boundary: the **Loom**, the **Weaver**, and the **Grimoire**.

**The Loom** is the front-end role. It is the surface through which the user — or, in some configurations, other software acting on the user's behalf — interacts with the Cell. The reference Loom implementation is a local web application served on the user's local network, available to any browser, supporting the standard interactive patterns of synthetic-intelligence work: chat, document review, configuration of Cell behavior, audit-log inspection, sensitivity-rule editing, federation management, BYOK key administration, and the various task-specific surfaces a particular user has reason to want.

The Loom is designed to be replaceable. A user who prefers a terminal interface can run a terminal Loom against the same Cell. A small business that wants a domain-specific user experience can build a custom Loom that calls the Cell's standardized internal interfaces. A community that prefers a voice interface, a chat-platform integration, or a mobile-app surface can build accordingly. *The Loom is the Cell's mouth and ears. It is not the Cell's mind.*

**The Weaver** is the inference and orchestration role. It is the component that decides what to do with each query: which model to invoke, what context to retrieve, which sensitivity policy applies, whether external providers may be called and which, how to assemble the prompt, how to parse and return the response, how to log the interaction. The Weaver is the most computationally substantial of the three roles in a typical Cell, because it holds the model weights for local inference and runs the tensor computations that produce responses.

The Weaver's design is dictated by two constraints. The first is that it must be efficient enough on consumer hardware to make local inference practical — which, given the rapid evolution of inference frameworks (llama.cpp, MLX, vLLM, TGI, and others) and the steady improvement of open-weight models, is increasingly tractable on Apple Silicon and modern PC hardware. The second is that it must be *policy-correct* by construction: it must not be possible for a query to bypass the Cell's sensitivity rules or for a remote provider to be invoked without the appropriate BYOK contract. The Weaver is therefore designed as a strict enforcement boundary, with policy evaluation occurring before any external call and with the policy state visible and auditable from the Loom.

**The Grimoire** is the data role. It holds the Cell's persistent state — the user's documents and corpora, conversation history, vector embeddings, federation contracts, capability advertisements, audit logs, and the keys and certificates that compose the Cell's cryptographic identity. The Grimoire's design draws on a long tradition of personal-database systems (from the personal information manager of the 1980s through to the modern note-taking systems and personal knowledge bases) but extends them with the embedding and retrieval primitives required for grounded synthetic-intelligence work, which Chapter 12 describes in detail.

The Grimoire is, in the legal sense, the user's records. It is what a court order that wished to compel disclosure of the user's interactions would have to reach — and reaching it would, by the Cell's architecture, require the procedural protections that apply to compelled disclosure of personal records, not the procedural framework that applies to subpoenaing a hyperscaler.

---

### Why These Boundaries

The three-role decomposition is not arbitrary. It encodes three distinct trust and policy boundaries that, in the Cell's threat model, must be separately enforceable.

The Loom is the *attack surface* boundary. Anything reaching the Cell from the outside world reaches the Loom first. By isolating the user-facing surface from the inference and storage tiers, the Cell ensures that a compromised Loom (a malicious browser extension, a phishing page, a hostile script) does not, in itself, compromise the Weaver's policy enforcement or the Grimoire's stored data. A defender can replace the Loom without replacing the Cell.

The Weaver is the *policy enforcement* boundary. All decisions about what is and is not permitted — which providers are invoked, which models run locally, which queries are permitted to leave the Cell, which capabilities are advertised to peers — happen in the Weaver. The Weaver is where the Cell's owner's preferences become operational behavior. By concentrating policy enforcement in a single architectural role, the Cell makes the policy itself reviewable, auditable, and modifiable without the user having to trace decisions through multiple components.

The Grimoire is the *data custody* boundary. Persistent data lives only in the Grimoire. The Loom and the Weaver, between sessions, hold no persistent user state of consequence. A Grimoire that is encrypted at rest, with keys held by the user, is a unit of data that can be physically moved (to another machine, another hard drive, another jurisdiction) without losing the user's records. A Grimoire that is kept in regular backup is a Cell that can be restored after hardware failure without renegotiating any contracts.

The separation of these three roles is what enables the Cell's *defense in depth*: a compromise of any one role does not, by itself, compromise the others. A user can replace the Loom, replace the Weaver's underlying model, restore the Grimoire from backup, all without breaking the Cell's identity or its federation contracts. The roles are designed to be independently maintainable, which means the Cell as a whole is robust against partial failure in a way that a monolithic deployment is not.

---

### Cell Composition Options

Cells come in several sizes, suited to different scales of use. The Foundation has identified four reference compositions, with the understanding that any owner can compose a Cell however the owner pleases — the compositions below are recommended starting points, not architectural constraints.

**Single-Box Cell.** The simplest configuration. All three roles run on a single machine, typically a modern Apple Silicon laptop or desktop. Suitable for an individual user with ordinary needs: a working professional, a student, a writer, a small operation that does not require continuous availability. Capital cost: the price of a laptop the user likely already owns. Operating cost: residential electricity. Limitations: the Cell is unavailable when the laptop is off; storage capacity is the laptop's storage capacity; inference performance is the laptop's inference performance.

**Multi-Box Cell.** The Loom remains on the user's interactive device (a laptop, a tablet, a phone), but the Weaver and Grimoire move to a more powerful or always-on machine on the user's network — a Mac Studio, a desktop with a discrete GPU, a small home server. Suitable for users who want their Cell available continuously, who run heavier inference workloads, or who maintain a substantial Grimoire that benefits from dedicated storage. Capital cost: laptop plus desktop or server. Operating cost: continuous electricity for the always-on machine, typically in the range of fifty to two hundred watts depending on hardware. Limitations: the user is responsible for the always-on machine's reliability and updates.

**Sovereign Cell.** A configuration intended for users with serious privacy, scale, or compliance requirements: small businesses, professional practices (law, medicine, accounting), community organizations with sensitive data, journalists, activists, or any user whose threat model justifies dedicated infrastructure. Typically includes redundant storage, a more substantial inference rig (multiple GPUs or a higher-end Apple Silicon configuration), continuous backup, and possibly a dedicated network configuration. May include physical security — locked rack, controlled access, surveillance — appropriate to the user's threat model. Capital cost: a few thousand dollars and up. Operating cost: meaningful but bounded. Limitations: requires more administrative attention than a Single-Box Cell, though the Foundation's reference Sovereign Cell tooling is designed to minimize this.

**Managed Cell.** A configuration in which the user owns the Cell's identity, data, and policies, but the underlying hardware is hosted and operated by a third party — the Webspinner Foundation, a partner cooperative, a community-trust hosting provider, or a commercial managed-Cell service. The user retains the keys; the host operates the metal. Suitable for users who want the architectural benefits of Sovereign SI without the operational burden of running their own hardware. The trust model is different from the user-hosted compositions and is addressed in detail in Chapter 17, but the essential property — that the user, not the host, holds the keys to the data — is preserved.

These four compositions are recommendations. A user with unusual needs can compose differently, and the architecture is designed to accommodate. What matters is that the role boundaries are preserved and the keys are in the user's hands.

---

### Inter-Cell Federation

A Cell on its own is sufficient for most personal work. The architecture's broader value emerges when Cells *cooperate*.

Federation, in the Warp vocabulary, is the controlled and capability-scoped sharing of services between Cells. It is opt-in, peer-to-peer, and revocable. The mechanics are described in technical detail in Chapter 13 (the Capability Bus); this section describes the patterns at the level of intent.

**Family federation.** A household runs one or more Cells — perhaps one Cell per adult, plus a shared Cell for household administration. The Cells federate selectively: each adult can grant their Cell read access to a household calendar held in the shared Cell; the children's Cells (where the family has chosen to give children their own Cells) can be configured to query family-approved educational corpora. The federation is defined by the family's own preferences and managed by whichever family member is comfortable with the configuration interface.

**Small-business federation.** A law firm, a medical practice, a small consultancy runs a Sovereign Cell as the firm's primary infrastructure. Each professional in the firm runs a personal Cell that federates with the firm Cell for shared corpus access (case files, client records, knowledge bases) under role-based capability grants. When a professional leaves the firm, their personal Cell's federation contract is revoked; their personal data goes with them, the firm's data stays.

**Community federation.** A neighborhood, a religious congregation, a school district, a small nonprofit operates a community Cell that federates with the personal Cells of its members. The community Cell offers shared retrieval (a community knowledge base), shared compute (for members whose own hardware is insufficient for occasional heavier workloads), and a shared trust model (federated authentication, capability advertisements vetted by the community's administrators). Members participate by choice; non-members are not adversely affected by the community's choices.

**Cooperative federation.** A federation of independent professionals, businesses, or community organizations chooses to share specific capabilities — a shared scientific corpus, a shared legal-research index, a shared compute pool for periodic heavy workloads. The federation is governed by a contract among the participants, with capability scopes negotiated up front and with each participant retaining the right to exit.

**Public federation.** Some capabilities are useful to make publicly available: a translation service offered by a multilingual Cell, a publicly accessible knowledge corpus (a library's catalog, an institution's open-access archive), a publicly available document-summarization service. Public federation is just federation with broad capability scopes; the Cell offering the public capability is making a deliberate choice to extend the capability widely.

The common pattern across all five federation types is that *every relationship is the explicit, capability-scoped, revocable arrangement of identifiable counterparties.* No central operator brokers the arrangements. No platform extracts a margin from the cooperation. No party other than the participating Cells has visibility into the federation's traffic.

This is a fundamentally different cooperative model from the platform-mediated cooperation of the modern Internet, in which every "share" of every resource has been re-routed through an intermediary that profits from the transaction. *Warp's federation is direct.* The Cells that wish to cooperate cooperate. The Cells that do not wish to cooperate do not. The Foundation provides the protocol and the reference implementations; the Foundation does not stand in the middle of the relationships.

---

### Identity and Trust

Each Cell has a cryptographic identity — a long-lived asymmetric keypair that identifies the Cell to peers, signs the Cell's capability advertisements, authenticates the Cell's federation contracts, and enables cryptographic verification of any signed message originating from the Cell. The identity is generated at Cell setup and held in the Grimoire under hardware-protected key storage where the Cell's hardware supports it (Apple's Secure Enclave, hardware security modules on dedicated equipment, TPMs on PC platforms).

When a Cell wants to invoke a capability provided by another Cell, the invocation is signed by the calling Cell's identity, the caller's authorization to invoke the capability is verifiable from the receiving Cell's records, and the response is signed by the receiving Cell. *Trust is a property of identifiable, signed, capability-scoped messages.* There is no implicit trust, no platform-issued tokens, no operator-mediated authentication.

A Cell that loses its identity — through hardware failure, key compromise, or the owner's deliberate action — can be replaced. The replacement is a new Cell, with a new identity, and the federation contracts must be renegotiated with peers. This is, by design, a friction the architecture imposes: it ensures that a stolen or compromised Cell does not, by itself, gain access to the previous Cell's federations. The friction is the price of cryptographic isolation, and it is the price the Foundation considers worth paying.

For most users, the friction will be invisible. Cells are not typically lost. Federations are typically stable. The cryptographic underpinnings work, by design, to be inconspicuous when nothing has gone wrong.

---

### What Makes the Cell Different

A reader who has come this far might reasonably ask: how does the Cell differ from the contemporary patterns of "self-hosted" or "edge" or "personal" computing that have been advocated for years without producing a transformation comparable to what this book is proposing?

The differences are three.

First, the Cell is *integrated*. A typical self-hosted setup is a heterogeneous collection of services — a personal web server, a personal database, a personal file store, a personal mail server, perhaps a personal search index — each with its own configuration, threat model, maintenance burden, and failure mode. The Cell is one coherent unit with three role boundaries and a single management surface. The user does not have to be a sysadmin to operate it.

Second, the Cell is *federated*, not isolated. Self-hosted systems historically have been islands; their owner gives up the network effects of platform participation in exchange for sovereignty. The Cell offers federation as a first-class architectural primitive, which means that the network effects can be reconstituted *without* the platform — among Cells whose owners have chosen to cooperate, on terms the owners control.

Third, the Cell is *purpose-specific*. It is for synthetic intelligence. The architecture's choices — the Loom/Weaver/Grimoire decomposition, the WRAG retrieval pattern, the BYOK contract pattern, the sensitivity-aware routing — are tuned to the specific demands of running synthetic-intelligence workloads under the user's sovereignty. A general-purpose self-hosted server, retrofitted for synthetic intelligence, would not arrive at these choices on its own.

The Cell is, in short, *what self-hosting looks like when it is designed deliberately for the synthetic-intelligence era*, with all of the architectural lessons of the previous twenty years of platform cooperation and platform extraction taken into account.

---

The next chapter describes WRAG, the retrieval-augmented grounding pattern that connects the Weaver to the Grimoire and to federated peers. WRAG is the protocol by which the Cell becomes more than the sum of its parts.

---

## Endnotes

[^1]: Christopher Alexander, Sara Ishikawa, Murray Silverstein, with Max Jacobson, Ingrid Fiksdahl-King, and Shlomo Angel, *A Pattern Language: Towns, Buildings, Construction* (Oxford University Press, 1977). The opening characterization of a "pattern" appears in the book's introduction and is reiterated in the companion volume *The Timeless Way of Building* (Oxford University Press, 1979). The pattern-language idea has been independently influential in software engineering since the Gang of Four's *Design Patterns* (Addison-Wesley, 1994) and was a direct inspiration for the wiki and for many subsequent collaborative knowledge-management systems.
