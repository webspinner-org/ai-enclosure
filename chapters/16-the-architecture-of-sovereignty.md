# Chapter 16
## The Architecture of Sovereignty

> *Code is law.*
>
> — Lawrence Lessig, *Code: Version 2.0* (2006), restating the central thesis of the original *Code and Other Laws of Cyberspace* (1999)

In 1999, Lawrence Lessig published *Code and Other Laws of Cyberspace*, the book that gave a generation of policy thinkers and engineers the vocabulary for the relationship between software and authority. Lessig's central observation was simple and consequential: in the digital era, the actual rules that govern what users can and cannot do are increasingly the rules built into the *code* — into the architecture of the systems users interact with — rather than the rules expressed in legislation. *Code is law.* If the code says you cannot do X, then for almost all practical purposes, you cannot do X, regardless of what the law of your jurisdiction says about the matter. Conversely, if the code makes it trivial to do Y, then Y will happen at scale, regardless of how the law condemns it.[^1]

Chapter 8 named *Sovereign SI* as the third pillar of Warp and articulated the five rights of an SI sovereign: to own, to inspect, to modify, to refuse, to disconnect. This chapter describes how those five rights are implemented in *code* — that is, in the actual architecture of the Cell, the Capability Bus, the BYOK pipeline, and the Foundation's reference implementations. *The point of this chapter is to demonstrate that the rights are not aspirational policy. They are properties of the architecture, enforceable because they are built in.*

The Foundation could publish a Bill of User Rights tomorrow. We have, in effect, just done that, in Chapter 8. A Bill of Rights without an architecture to enforce it is precisely the kind of contractual sovereignty that Chapter 8 argued against. The architecture of this chapter is what gives the Bill of Rights its teeth.

---

### Cell Ownership Models

The Cell, as Chapter 11 specified, has a single principal owner. The architecture supports several ownership models, each appropriate to a different scale and use case. Naming them precisely matters because the legal posture of each is meaningfully different.

**User-owned Cell.** A Cell whose owner is a single natural person, typically running on hardware the person bought, in a location the person controls (their home, their office, their personal device). The Cell is, in property terms, the user's personal property; the data resident in it is in the user's personal custody under whatever privacy law applies to personal records in their jurisdiction. The user-owned Cell is the canonical example for individual users and is the recommended composition for most personal use.

**Family-owned Cell.** A Cell whose owner is a household — typically with one adult member designated as the legal principal but with shared use among family members under household policy. The legal posture is the same as a user-owned Cell, with the family's internal sharing arrangements being a matter of household norm rather than additional legal structure. This composition is appropriate for households that want a shared institutional memory without setting up a formal organizational structure.

**Small-business-owned Cell.** A Cell whose owner is a legal business entity — a sole proprietorship, an LLC, a partnership, a small corporation. The data in the Cell is the business's records; the legal protections that apply to business records (work-product privilege, attorney-client privilege where applicable, accountant-client privilege, professional confidentiality) extend to the Cell. This composition is appropriate for professional practices, small consultancies, design studios, and similar small organizations.

**Community-owned Cell.** A Cell whose owner is a community organization — a cooperative, a nonprofit, a religious congregation, a neighborhood association, a school district. The Cell's governance is the community's governance; the data in the Cell is collectively owned according to the community's bylaws and norms. This composition is appropriate for community institutions whose members benefit from shared synthetic-intelligence capabilities while remaining outside the platform model.

**Sovereign-enterprise Cell.** A Cell whose owner is a larger organization — a corporation, a government agency, a substantial nonprofit — with sufficient resources to operate dedicated infrastructure and sufficient threat model to require it. The composition typically includes redundant hardware, formal access control, integration with the organization's existing identity and authentication systems, and audit-and-compliance reporting suited to the organization's regulatory environment. This composition is appropriate for organizations whose data sensitivity, regulatory exposure, or scale require the architectural commitments of a Cell at enterprise scope.

**Managed Cell.** A Cell whose owner remains the user (or family, business, community) but whose hardware is operated by a third party — the Webspinner Foundation, a partner cooperative, a community trust, or a commercial managed-Cell provider. The user retains the keys to the data and the cryptographic identity; the host operates the hardware. The legal posture is more complex than user-hosted compositions and is the subject of Chapter 17's threat-model discussion, but the essential property — that the user, not the host, holds the keys — is preserved by the architecture's design.

These six compositions cover the practical range of users the architecture serves. A Cell can be migrated between compositions as the owner's needs change (a user-owned Cell can become a small-business-owned Cell when the user incorporates; a family Cell can become a managed Cell when the family decides to outsource the hardware). The data and identity migrate with the ownership.

---

### Cryptographic Identity and Worker Attestation

The architectural foundation of the five rights is the cryptographic identity system. Every Cell has a long-lived asymmetric keypair that constitutes its identity to the federation. Within a Cell, every running process — every Loom, every Weaver, every Grimoire instance — has its own subordinate keypair, derived from or signed by the Cell's identity, which authenticates the process to other components of the same Cell.

The cryptographic primitives are conventional: standard public-key cryptography (Ed25519 or P-256 signatures, X25519 key agreement, AES-GCM or ChaCha20-Poly1305 for symmetric encryption, the standard cipher suites that govern modern TLS). The Foundation has chosen standard cryptography because the Foundation has no business inventing cryptography; the strength of the architecture comes from the *use* of well-attested primitives, not from novel ones.

What the architecture does add is *worker attestation* — the discipline that any process claiming to be a Cell component must, on receipt of an internal-bus invocation, produce a cryptographically valid signature chain proving that it is the process the Cell's policy says it should be. A rogue process injected into the Cell — say, by malware running in the same user account — cannot, without the Cell's identity key, produce a valid attestation, and therefore cannot impersonate a legitimate Cell component to the bus.

Where the underlying hardware supports it, the Cell's identity key is held in hardware-protected key storage: Apple's Secure Enclave on Apple Silicon, the TPM 2.0 on PCs that have it, an HSM on dedicated equipment, or equivalent on other platforms. Hardware-backed key storage means the key cannot be extracted by software-only attacks, which substantially raises the bar for compromising a Cell's identity.

For Managed Cells, where the host operates the hardware, the user's own key is held in a key store the user controls — typically on a hardware token (a YubiKey, a Trezor, or equivalent) that the user holds personally. The host has the data (encrypted at rest); the user has the keys. The architecture is structured so that the host *cannot* read the data without the user's key, and the user can revoke the host's access at any time by withdrawing the key.

---

### The Right to Inspect: Open Code, Open Weights, Auditable Bus Traffic

The right to inspect is implemented through three architectural commitments.

**Open code.** Every reference implementation of every Cell tier is released under open-source licenses approved by the Open Source Initiative — typically Apache 2.0 for the Foundation's reference work, with contributing projects free to choose other OSI-approved licenses where appropriate. The Foundation does not maintain proprietary code in any role of the architecture. Users (or their hired developers, or the broader community) can read the source, build their own binaries from it, audit its behavior, and contribute corrections.

**Open weights, where models are open.** The Cell architecture makes no commitment to operate only on open-weight models — the BYOK pattern explicitly permits invocation of closed-weight frontier models from commercial providers — but the architecture does insist that *which* model is being invoked, on each query, is visible to the user. A query routed to GPT-4 or Claude or Gemini under BYOK is logged as such; a query handled by the local Llama model is logged as such. The user knows what computed their answer.

**Auditable bus traffic.** Every Capability Bus message in or out of the user's Cell is logged in the user's audit log, with the message's signed envelope, its capability descriptor, its sensitivity classification, its source or destination peer, and whatever response was returned. The user can review this log at any time through the Loom. There is no shadow channel through which messages travel without leaving an audit trace; if the user sees no such message in the log, the message did not occur.

These three commitments together constitute *the user's ability to know how their Cell is behaving*. A user who chooses to exercise the right of inspection can do so as deeply as their interest and skill permit; a user who chooses to trust the Foundation's reference implementations and the audit log's summary view can do that. *The architecture does not require the user to be a security professional. It does require that the option to inspect, when the user wants it, is real.*

---

### The Right to Modify: Forkable Cells, Swappable Components, No Lock-In

The right to modify is implemented through three architectural commitments.

**Standardized interfaces.** Every interface between Cell components is documented as a public protocol. The interface between Loom and Weaver is documented; the interface between Weaver and Grimoire is documented; the Capability Bus protocol is documented; the WRAG retrieval protocol is documented. A user (or a third-party developer) who wishes to replace any component can do so by implementing the interface, with the rest of the Cell continuing to interoperate.

**Forkable reference implementations.** The Foundation's reference implementations are released under licenses that explicitly permit forking. A user, a community, or a commercial entity can take the reference Loom, modify it, and run their own variant. The modified variant continues to interoperate with other Cells running the reference Loom (and any other forks), because the interoperation is at the protocol level, not at the implementation level.

**No vendor lock-in.** The Foundation does not maintain proprietary cloud services, proprietary data formats, or proprietary protocols that any implementation must use to interoperate. The data in a Grimoire is in standard formats (with documented schemas and migration paths); the configuration in a Cell is in standard formats; the federation contracts are in standard formats. A user can, at any time, export their Cell's state and re-import it into a different implementation of the architecture, with the architecture's standardization ensuring that the new implementation reads what the old one wrote.

These commitments are what distinguish *standardized at the interface level* from *locked-in at the implementation level*. The Foundation invests in the reference implementations because the reference implementations are useful — they reduce the friction of getting started, they incorporate best practices, they receive ongoing security review — but the Foundation refuses to make the reference implementations *required*.

---

### The Right to Refuse: Capability-Level Opt-Outs, Provider Blocklists, Sensitivity Gates

The right to refuse is implemented at three layers.

**Capability-level opt-outs.** The Cell's configuration includes an explicit list of capabilities it will *not* offer and capabilities it will *not* invoke. A Cell can be configured to refuse, for example, to handle queries about specified topics, to invoke models from specified providers, to engage in federation contracts of specified scope, to participate in capability advertisements above specified sensitivity tiers. The opt-outs are enforced in the Weaver before any external call.

**Provider blocklists.** A user with strong preferences about which model providers are acceptable can maintain a blocklist — a set of providers whose services will not be invoked under any circumstance, regardless of the routing policy that might otherwise have selected them. A user who, for example, has decided that a particular operator's defense contracting is incompatible with the user's values can blocklist that operator and the architecture will respect the blocklist on every query, with the user's audit log reflecting the routing decisions.

**Sensitivity gates.** As described in Chapter 7, the user defines sensitivity classifications for queries (Public, Personal, Confidential, Privileged, or whatever the user prefers) and routing rules for each. A Cell that has been configured to handle Privileged queries only locally cannot be persuaded by a clever prompt-engineering attack to escalate a Privileged query to an external provider; the gating happens before the prompt is even fully assembled.

The combination of these three layers is what gives the user *operational refusal* — not just the abstract right to refuse, but the architectural mechanism by which the refusal is enforced. The user does not have to monitor each query to ensure compliance with their preferences; the preferences are encoded into the Cell's policy, evaluated automatically on each query, with the audit log providing post-hoc verification.

---

### The Right to Disconnect: Data Export, Federation Exit, No Captive State

The right to disconnect is implemented through three architectural commitments that, taken together, ensure no part of the user's Cell is held hostage by any external party.

**Data export.** The Grimoire supports complete, well-documented export of the user's data in standard formats. The user can, at any time, request a full export — documents, conversation history, vector embeddings, audit logs, configuration — that is portable to a different Cell, a different host, or simply to local archival storage outside the Cell entirely. The export is the user's; nothing is retained on the Foundation's side or any host's side after the export is complete.

**Federation exit.** Federation contracts the user has entered into are revocable by the user at any time. Capability advertisements published to peers can be withdrawn. Capability invocations the user has authorized for peers can be cancelled. After exit, the user's data does not flow to the former federation peers, and the former federation peers' data does not flow to the user. *The exit is clean*, in the sense that no residual entanglement remains.

**No captive state.** The Foundation, as steward of the architecture, does not operate any service that retains state on the user's behalf. There is no Foundation account that the user must keep; there is no central registry the user is bound to; there is no proprietary cloud the user must continue to pay for. A user who wishes to stop using Warp entirely can do so by shutting down their Cell; nothing of theirs remains on Foundation infrastructure, because nothing of theirs was on Foundation infrastructure in the first place.

The right to disconnect is what makes the other rights credible. A right to inspect that comes with no exit option is hostage-taking with extra steps. A right to modify that requires staying within a particular ecosystem is a managed concession. A right to refuse that does not include the right to leave is not a right at all. *The architecture's commitment to clean exit is what guarantees the other architectural commitments are real.*

---

### Architecture as Sovereignty

Lessig's argument was that code, in the digital era, has become the principal source of governance — and that those who write the code are, by virtue of writing it, exercising a kind of sovereign authority over the lives the code touches. *The Foundation's response to that argument is that the code, in this case, is being written deliberately to give that sovereign authority back to the user.*

This is not a small claim. Most software in the modern era is written, deliberately or by neglect, in ways that accumulate authority on the operator's side — through default opt-ins, through proprietary protocols, through dark patterns, through cloud-side state, through update mechanisms that change behavior without user consent. The Warp architecture has been written, deliberately, in the opposite direction. Each architectural choice has been evaluated against the question *does this give the user more sovereignty, or less?* — and the choices that diminish sovereignty have been refused, even when those choices would have made the system more convenient, more profitable, or easier to maintain.

This is a discipline. It is a discipline that requires the Foundation to forgo some of the conveniences a less-disciplined operator could offer. The discipline is the architectural expression of the moral case Chapter 9 made. *Sovereignty is not given. It is built in, deliberately, by people who refuse to accept the alternative.*

The next chapter — Privacy by Design — extends the architectural argument to the threat model, naming explicitly what the architecture protects against and what it does not, and what the user's part of the bargain is.

---

## Endnotes

[^1]: Lawrence Lessig, *Code and Other Laws of Cyberspace* (Basic Books, 1999); revised and updated as *Code: Version 2.0* (Basic Books, 2006). The phrase "code is law" is the book's central organizing argument, made repeatedly throughout both editions. *Code: Version 2.0* is published under a Creative Commons license and is freely available online: http://codev2.cc. Lessig's broader corpus on the relationship between technology, law, and culture — including *The Future of Ideas* (Random House, 2001) and *Free Culture* (Penguin, 2004) — extends the argument and is among the most influential bodies of work in contemporary technology policy.
