# Chapter 17
## Privacy by Design

> *Security is a process, not a product.*
>
> — Bruce Schneier, *Crypto-Gram* (May 1999), restated as the central thesis of *Secrets and Lies: Digital Security in a Networked World* (2000)

In May 1999, the cryptographer and security writer Bruce Schneier published an essay in his monthly *Crypto-Gram* newsletter that began with one of the most-quoted sentences of his career. *Security is a process, not a product.* The argument that followed was a corrective to the technology industry's persistent tendency to treat security as a checklist of features that could be bolted onto a product, rather than as the discipline of designing, operating, and continually re-evaluating systems whose threat models change as fast as the systems themselves.[^1]

Privacy is the same kind of discipline. The four pillars of Warp — Green, Confidential, Sovereign, Moral — describe what the architecture is *for*. The five rights — to own, inspect, modify, refuse, disconnect — describe what the architecture *delivers*. This chapter describes what the architecture *defends against* and, with equal honesty, *what it does not*. Privacy by Design is not a label. It is the discipline of naming the threat model openly, acknowledging the residual risks, and being honest with users about what the architecture can promise and what it cannot.

This is the chapter where the Foundation owes the reader the candor that the marketing departments of hyperscale providers are structurally incapable of offering.

---

### The Four Threat Surfaces

The Cell architecture, viewed from a security and privacy perspective, has four distinct surfaces at which adversaries can attempt to compromise the user's interests. Each surface has its own threat model, its own defenses, and its own residual risks.

**Surface 1: The user's hardware.** The Cell runs on hardware the user owns. If the hardware is compromised — by malware, by a stolen device, by a hostile party with physical access, by a supply-chain attack on the device itself before delivery — then the architecture's protections operate against an adversary who already has substantial leverage. The architecture mitigates this with hardware-backed key storage (Apple's Secure Enclave, the TPM on PC platforms, dedicated HSMs on enterprise equipment) and with full-disk encryption of the Grimoire. It does not eliminate the threat. *A user whose laptop has been compromised at the kernel level is, in security terms, in trouble that no architecture can fully repair.*

**Surface 2: The Cell's network.** The Cell communicates with the user's Loom over local network connections, with peer Cells over federation transports, and with model providers under BYOK over the public Internet. Each of these transport paths is a potential surface for attack — passive eavesdropping, active man-in-the-middle, traffic analysis, denial of service. The architecture mitigates with mandatory TLS or QUIC for all external traffic, with end-to-end signing of all bus messages, and with the Capability Bus's authenticated routing. *A determined nation-state adversary with substantial network position remains capable of traffic-pattern analysis even when the contents are encrypted*, and the architecture does not pretend otherwise.

**Surface 3: Federated peers.** A federation contract grants a peer Cell certain capabilities to invoke services on the user's Cell or to receive services from it. The peer is, by virtue of the contract, partly trusted within the scope of the contract. If the peer Cell is compromised, or if its owner is acting in bad faith, the consequences can include leakage of whatever data the user has authorized the peer to receive. The architecture mitigates with capability scoping (the peer gets only what was specifically granted), with revocability (the user can terminate the contract at any time), and with audit logs (the user can see what the peer has been doing under the contract). *The architecture cannot make a bad-faith peer good*; it can only limit the scope of harm and make detection tractable.

**Surface 4: BYOK provider relationships.** When the user invokes a frontier model under BYOK, the prompt and response cross from the user's Cell to the provider's facility and back. The provider sees the prompt content, the prompt content may be retained according to the provider's terms with the user, and the provider's compliance with those terms is the user's contractual lever, not the architecture's. The architecture mitigates by sensitivity-aware routing (the user can prevent specific classes of query from leaving the Cell at all), by contract selection (the user chooses providers with terms acceptable to them), and by minimal-prompt assembly (the user's full corpus does not go to the provider — only the relevant retrieved passages required to answer the query). *The architecture cannot make a hostile provider trustworthy*; it can only minimize what reaches the provider in the first place.

These four surfaces are the entirety of the Cell's exposure. Each is named because each requires its own defensive discipline, and each carries its own residual risks.

---

### Defenses Layer by Layer

For each of the four surfaces, the architecture provides defenses at multiple layers. The pattern follows the classical "defense in depth" doctrine of computer security: no single defense is treated as sufficient; each is one layer in a stack designed to survive the failure of any individual component.

For **Surface 1 (Hardware)**:
- *Hardware-backed key storage* protects the Cell's identity even against software-only compromise.
- *Full-disk encryption* of the Grimoire protects data at rest from physical-access compromise of a stolen device.
- *Process isolation* between Loom, Weaver, and Grimoire ensures that compromise of one tier does not directly grant access to the others' working state.
- *Audit logging* gives the user post-hoc visibility into actions on the device, with the logs themselves protected by the same encryption as the Grimoire.

For **Surface 2 (Network)**:
- *End-to-end encryption* on all bus messages, with keys derived from the participating Cells' identities, ensures that intermediaries (relay nodes, network operators, ISPs) cannot read message contents.
- *Mutual authentication* on every federation invocation prevents impersonation attacks.
- *Replay protection* using nonces and signed timestamps prevents captured messages from being re-played by an adversary.
- *Onion-routed transport* options for users with strong anonymity requirements (the Foundation's reference implementation supports Tor and equivalent protocols where the user wishes).

For **Surface 3 (Federated Peers)**:
- *Capability scoping* limits what any individual federation contract grants.
- *Audit logging* on both sides of every federated interaction provides bilateral verification of what was exchanged.
- *Revocability* lets the user terminate any federation at any time.
- *Reputation tracking* (in the Cell's local records, optional and user-controlled) helps the user identify peers whose behavior has been unreliable.

For **Surface 4 (BYOK Providers)**:
- *Provider selection* lets the user choose providers with terms compatible with the user's privacy posture.
- *Sensitivity-aware routing* ensures only queries the user has authorized to leave the Cell go to external providers.
- *Minimal-prompt assembly* sends only the retrieved context required for the specific query, not the user's full corpus.
- *Provider blocklists* let the user permanently exclude providers they consider unacceptable.
- *Zero-data-retention contracts* (offered by some providers, opt-in by the user) reduce what the provider keeps after the inference completes.

These defenses are layered, not stacked. Each layer addresses a specific class of failure; the combination provides robustness against the realistic combinations of adversary capability and adversary intent that a Cell will encounter.

---

### Honest Residual Risks

I want to name, as plainly as possible, the categories of risk that the Warp architecture *does not* eliminate. The list is the price of architectural honesty.

**User-side compromise.** A user whose own device is compromised — by sophisticated malware, by physical theft of an unlocked device, by social-engineering attacks against the user themselves — is operating against an adversary who is, in some meaningful sense, inside the user's perimeter. The architecture's hardware-backed key storage and audit logging raise the bar but do not make the device invulnerable. Users with elevated threat models (journalists, activists, professionals handling exceptionally sensitive matters) should adopt operational practices appropriate to their threat — separate devices for separate work, hardware-token authentication, careful physical security — that the architecture's reference tooling supports but does not enforce.

**Side-channel attacks.** Modern hardware has known side channels — timing, power, electromagnetic emanation, cache-line behavior — through which information can leak in ways that bypass the explicit cryptographic protections. Mitigations exist for the major classes of side channel and the reference implementations apply them, but a determined and well-resourced adversary with physical proximity to the device may extract information through paths the architecture cannot fully close.

**Configuration errors.** A Cell whose owner has misconfigured the sensitivity rules, the federation contracts, or the provider blocklists will leak or refuse incorrectly until the misconfiguration is corrected. The reference Loom provides configuration tools designed for ordinary users, and the audit log surfaces unexpected behavior, but the user remains responsible for configuration. *We are not making the case that the user has no responsibility. We are making the case that the user should have the means to discharge that responsibility.*

**Federation peer compromise.** A peer Cell that the user has federated with may, after the fact, be compromised or its owner may turn adversarial. The data the user has authorized the peer to receive is, in that case, subject to whatever fate the peer's security has met. The architecture limits the scope (capability scoping) and provides exit (revocation), but it cannot retroactively undo what the peer was authorized to do before the compromise.

**BYOK provider compliance.** A model provider whose terms forbid retention can violate the terms, lose data to a breach, or be compelled by legal process to disclose content. The user's contractual remedies are the user's contractual remedies; the architecture cannot enforce on the provider's side.

**Hardware supply chain.** A user whose hardware was compromised before delivery — at the manufacturer, in transit, by a hostile party with access to the supply chain — is operating against an adversary whose position is, again, inside the user's perimeter. The architecture's mitigations apply only to the extent that the hardware is actually trustworthy at the layers below the operating system.

**Quantum computing risk.** The cryptographic primitives currently used by the architecture are believed secure against classical adversaries but are, in the long run, vulnerable to sufficiently capable quantum computers. The Foundation's roadmap includes migration to post-quantum cryptographic primitives as standardization matures (NIST's PQC selection process is ongoing as of this writing); the architecture is designed to support cryptographic agility, but the migration is future work.

**Human error.** Users will, on occasion, share things they did not intend to share, federate with parties they should not have, run queries they should not have run, and configure policies that did not produce the behavior they wanted. The architecture provides revocability, audit, and reasonable defaults; it does not eliminate human error, and we should not pretend that any architecture can.

These are the honest residual risks. They are smaller, in aggregate, than the residual risks of the hyperscale alternative — which include all of the above plus the operator-side risks the Cell architecture eliminates entirely. The point is not that Warp is a perfect privacy architecture. The point is that Warp's residual risks are *the residual risks of running a personal computer in a connected world*, while the hyperscale architecture's risks are those plus *the additional risks of trusting a remote operator with the user's interior life.*

---

### What This Lets You Promise Users

A small business operating a Sovereign Cell can, in good faith, make the following commitments to the people whose data passes through the Cell:

- Your data is on our hardware, in our office, under our keys.
- We do not share your data with third parties except where you have specifically authorized us to (under BYOK, with the providers you have approved, under their published terms).
- Our internal use of your data is auditable, and the audit logs are available to you on request.
- Our use of your data does not contribute to training third-party models.
- If you ask us to delete your data, we delete it from the Grimoire, with the deletion verifiable from the audit log.
- If we go out of business, your data goes with us — we do not have an arrangement with a successor operator that retains it.
- If we are compelled by legal process to disclose your data, we are the named party, and we will notify you to the extent the law permits.

These are commitments that a business operating on hyperscale infrastructure cannot make in good faith, because the hyperscale infrastructure does not actually support them at the architectural level. The business operating on Warp can.

For an individual user, the commitments simplify further:

- Your synthetic intelligence runs on your machine.
- Your conversations with it are between you and your machine.
- Your data is in your custody.
- If you decide to stop, nothing of yours is left behind on someone else's infrastructure.

These are the promises the architecture makes possible. They are not absolute — the residual risks above continue to apply — but they are the strongest privacy posture currently available, and they are stronger than what any operator-mediated alternative can offer.

---

### What This Does Not Let You Promise

A Cell's owner, however careful, should not promise users:

- That their hardware is invulnerable. Hardware can be compromised.
- That federation peers will never be compromised. Peers are people, and people are sometimes compromised.
- That BYOK providers will perfectly honor their terms. Compliance failures happen.
- That sophisticated nation-state adversaries cannot reach them. Some adversaries are sufficiently resourced that no architecture available to ordinary citizens can defend against them.
- That the user's own configuration will always be correct. Configuration is the user's responsibility.

The Foundation's view is that *honest acknowledgment of these limits is itself a form of privacy*. A user who knows what the architecture protects against and what it does not can take appropriate compensating measures — using a separate, more constrained Cell for the most sensitive work, using hardware tokens for authentication, using onion-routed transports for queries that warrant the latency cost, declining BYOK invocation for content that should never leave the Cell.

A user who has been told by an operator that their privacy is "fully protected" — without the operator's specifying against whom and under what assumptions — has been told a marketing claim. The architecture exists to replace marketing claims with operational properties.

---

### Closing Part III

This chapter closes Part III of the book.

Part I described the trap: hyperscale's environmental, capital, and privacy unsustainability, and the historical pattern of escape. Part II described the architecture: Warp itself, the four pillars, and the Value Triangle. Part III has described the architecture in technical detail: Cells, WRAG, the Capability Bus, the Compute Farm, BYOK, the Architecture of Sovereignty, and now Privacy by Design.

The architecture is now described, at the level of detail that lets engineers build, lets policy readers evaluate, and lets ordinary readers verify the claims of the previous chapters against an actual buildable specification. What remains is to compare what we have built against what the alternative offers — Part IV — and to make the affirmative case for the broader movement of which Warp is a part — Part V.

The trap and the architecture are now both on the page. What follows is the comparison, and then the call.

---

## Endnotes

[^1]: Bruce Schneier, "Why Cryptography Is Harder Than It Looks," *Crypto-Gram* (May 15, 1999), available in the Schneier *Crypto-Gram* archive at https://www.schneier.com/crypto-gram/. The essay's "security is a process" thesis was elaborated in book-length form as Bruce Schneier, *Secrets and Lies: Digital Security in a Networked World* (Wiley, 2000), which remains a touchstone of the practitioner literature on systems-level security thinking. The Privacy by Design framework most directly relevant to this chapter's title is Ann Cavoukian, *Privacy by Design: The 7 Foundational Principles* (Information & Privacy Commissioner of Ontario, 2009), available at https://www.ipc.on.ca/wp-content/uploads/Resources/7foundationalprinciples.pdf — which articulates the principle that privacy must be embedded into design, default settings, and full lifecycle, rather than treated as a compliance checklist applied after the fact.
