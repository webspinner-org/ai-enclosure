# Chapter 13
## The Capability Bus

> *Be conservative in what you do, be liberal in what you accept from others.*
>
> — Jon Postel, *Transmission Control Protocol*, RFC 793 (September 1981)

In September 1981, Jon Postel finalized the Transmission Control Protocol — the "TCP" of TCP/IP — in RFC 793. Buried in the document, in the discussion of how implementations should handle malformed or unexpected input, was a single sentence that has become known as the *robustness principle*. *Be conservative in what you do, be liberal in what you accept from others.* The principle was a piece of practical engineering wisdom: a network of independent implementations, each written by different parties at different times under different assumptions, will only interoperate at scale if every implementation is generous about variance in its peers' behavior while staying disciplined in its own.[^1]

The Capability Bus of the Warp architecture is governed by Postel's principle. It is the messaging fabric over which Cells advertise capabilities, route requests, and return responses. Like the Internet protocols that inspired it, the Capability Bus is built on the assumption that the population of Cells participating in any given conversation is heterogeneous, evolving, partly trusted, partly unknown — and that the protocol must therefore be tolerant of variance, strict about its own contracts, and robust against the failure modes of imperfect peers.

This chapter describes what the Capability Bus is, how it works, and why it allows Cells to cooperate without becoming centralized.

---

### Pub/Sub and Capability-Based Routing

The Capability Bus is, at the architectural level, a *publish-subscribe* messaging fabric. Cells publish *capability advertisements* describing what services they offer, and Cells subscribe to *capability invocations* describing what services they wish to consume. Messages flow between publisher and subscriber, with the routing fabric matching invocations to advertisers without either party needing to know the others ahead of time.

The pub/sub pattern is well-established in distributed systems. The Foundation has not invented it. The reference implementation of the Capability Bus draws on the patterns proven by NATS, Apache Kafka, RabbitMQ, MQTT, and the broader event-streaming ecosystem, with adaptations specific to the Warp use case.

The key adaptation is *capability-based routing*. In a conventional pub/sub system, messages are routed by *topic* — a string identifier that publishers and subscribers agree on out of band. In the Capability Bus, messages are routed by *capability descriptor* — a structured representation of the service being offered or requested, including the service's interface, the data types involved, the sensitivity classification, the quality of service, and the policy constraints under which the capability may be invoked.

A capability advertisement might look, schematically, like:

> *"This Cell offers document-summarization service. Input: text up to 50,000 words. Output: structured summary up to 1,000 words. Sensitivity: accepts up to Personal classification. Latency: typically under 30 seconds. Cost: free for federated peers under the family-trust contract; pay-per-call for general callers. Available: 24/7. Authentication: signed invocation under a recognized peer key."*

A capability invocation might look:

> *"Caller seeks document-summarization service for the attached input. Sensitivity classification: Personal. Required latency: under 60 seconds. Caller's signature attached. Caller's authorization: family-trust contract token attached."*

The Capability Bus matches the invocation to the advertisement by checking that the invocation's requirements fall within the advertiser's offered terms, that the caller's authorization satisfies the advertiser's authentication requirements, and that the sensitivity classification is within the advertiser's accepted range. *No central registry decides this matching*; the matching is done by the bus protocol itself, with each participating Cell evaluating the messages addressed to it according to local policy.

Capability-based routing has several properties that conventional topic-based routing does not.

- **Self-describing.** A Cell encountering a capability advertisement for the first time has, in the advertisement itself, all the information needed to invoke it correctly. There is no out-of-band specification to retrieve.
- **Policy-aware.** Sensitivity classifications, authorization requirements, and quality-of-service constraints are first-class fields in the advertisement and the invocation, rather than ad-hoc conventions.
- **Federated by design.** Capability advertisements can include the federation contracts under which they are offered, which means a Cell can advertise different capability terms to different classes of peers (family, business associates, community members, the general public) within the same protocol.

---

### How Messages Move

The Capability Bus does not, in the Warp architecture, run as a centralized service. There is no Webspinner-operated bus server through which all Cell traffic flows. The bus is a *protocol implemented by every Cell*, and the messages move directly from publisher to subscriber by whatever underlying transport the participants have agreed on.

In practice, several transport patterns coexist:

**Local-network transport.** When two Cells on the same local network — a household, a small office, a community center — communicate, the messages flow over the local network directly, with no Internet-side hop required. This is the lowest-latency case and the most privacy-preserving (the messages do not leave the premises).

**Direct-Internet transport.** When two Cells on the Internet wish to communicate and have established a federation contract, the bus messages flow as authenticated and signed exchanges directly between them, typically over standard TLS-over-TCP or QUIC, with the protocol envelope wrapping the capability invocation and response. NAT-traversal techniques (similar to those used by WebRTC and contemporary peer-to-peer protocols) allow Cells behind residential routers to reach each other.

**Relay transport.** For Cells whose network conditions prevent direct connection, or for asynchronous patterns where the recipient is offline at the moment of sending, lightweight relay nodes can buffer messages until the recipient retrieves them. The relays operate the relay protocol but cannot read the contents of relayed messages, which are end-to-end encrypted to the recipient's identity. Relays are operated by community Cells, by partner organizations, or by the Foundation's reference relay implementation; users can choose which relays to use, or none.

**Multicast advertisement.** Capability advertisements that are intended for a broad audience — public services offered to the open federation — can be distributed via a gossip-protocol mechanism similar to those used in BitTorrent's DHT and modern peer-to-peer systems. The mechanism is opt-in; Cells that wish to advertise publicly do so, while Cells that wish to remain unannounced simply don't.

Each transport pattern has different latency, privacy, and reliability characteristics, and the Capability Bus protocol abstracts over them: a capability invocation is the same shape regardless of which transport carries it.

---

### Worker Subscription Patterns

Within a Cell, the Capability Bus also serves as the *internal* messaging fabric. The Loom, the Weaver, and the Grimoire communicate with each other over the bus, using the same capability descriptors and invocation envelopes that govern external federation. This unification is deliberate. It means that the same audit and policy machinery that governs which external providers may be invoked also governs which internal components may invoke each other, with the same evidence trail.

It also enables an important pattern: *worker scaling*. A Cell that wishes to handle more concurrent inference workload than a single Weaver can sustain can run multiple Weavers, each subscribed to the inference capability descriptor, with the bus distributing inference requests across the available workers. Adding capacity to a Cell becomes a matter of starting another Weaver process; removing capacity is a matter of stopping one. The user does not have to reconfigure routing; the bus handles the matching.

Worker subscription extends beyond inference. A Cell with multiple Grimoire instances (perhaps one for current work, one for archived materials, one for federated read-only mirrors) can have each instance advertise its retrieval capability with appropriate scope, and the Weaver selects the right Grimoire based on the query's metadata. A Cell with multiple Loom front-ends (a chat interface, a programmatic API, a voice interface) can have each subscribe to user-interaction events with appropriate authorization scopes.

This is the *horizontal scaling* property of the Capability Bus, and it is the property that makes the Cell a real architecture rather than a single-machine appliance. *A Cell is not one process. A Cell is a collection of processes that have agreed, via the bus, to play the roles of one Cell.* The collection can grow or shrink as the user's needs change.

---

### Horizontal Scaling Without Central Coordination

The most important architectural property of the Capability Bus is the negative one. *There is no central coordinator.* The bus protocol does not require a registry that all Cells consult. It does not require a global naming service that resolves capability identifiers. It does not require a transaction coordinator that sequences invocations. It does not require any single party to be running, online, or trustworthy.

This is not a minor design choice. It is the property that distinguishes the Warp federation from every centralized cooperation pattern of the modern Internet.

Consider what happens when the Foundation, in a hypothetical adversarial future, decides to introduce mandatory routing through a Foundation-operated central server. The architecture, as currently specified, has no place for such a server. Cells would have to be modified to recognize and use the server, the protocol would have to be updated, and any Cell that refused the update would continue to operate as before, federating with other refusing Cells over the original protocol. *The Foundation cannot retroactively centralize the bus.*

Consider what happens when a malicious actor wishes to monitor or disrupt the bus. There is no central traffic point to surveil. There is no central authority to compromise. There are point-to-point cryptographically authenticated exchanges between consenting Cells, with traffic patterns that resemble the long tail of contemporary Internet activity rather than concentrated platform flows.

Consider what happens when a country wishes to restrict synthetic-intelligence cooperation across its borders. The Capability Bus has no jurisdictional dependence — it is a protocol, not a service. Restrictions can be applied to Internet traffic in the conventional way, but the bus has no central choke point that a regulator can target without affecting the underlying TLS/QUIC traffic that the modern Internet runs on.

These properties are not accidental. They are the operating consequences of the choice to build the bus as a protocol rather than a platform. *The cost of this choice is that the Foundation cannot offer some of the conveniences a centralized operator could offer*: centralized search across all public capabilities, centralized analytics on bus traffic, centralized policy enforcement across the network. The Foundation has chosen to forgo these conveniences. The reasons are the same reasons the chapters before this one have given.

---

### The Robustness Principle in Practice

To return to Postel's principle: how does the Capability Bus, in practice, embody the discipline of *be conservative in what you do, be liberal in what you accept from others*?

*Conservative in what you do.* When a Cell publishes a capability advertisement, the advertisement uses only the canonical fields, the canonical encodings, the canonical sensitivity classifications. The Cell does not invent its own fields or take liberties with the protocol. When a Cell signs an invocation, the signature is over exactly the canonical message, in exactly the canonical form. Future versions of the protocol can extend the schema; current versions adhere to it.

*Liberal in what you accept.* When a Cell receives a capability invocation, it tolerates extra fields it does not recognize (skipping them or passing them through), tolerates encoding variations within reason, tolerates timing variations within stated bounds, tolerates the small frictions of an evolving network. The Cell rejects messages that fail to authenticate, fail to authorize, or violate the Cell's own policy — but it does not reject messages merely because they look slightly different from what the Cell itself would have produced.

The cumulative effect, when the principle is followed across a population of independently-implemented Cells, is a network that *works*. Cells written by different communities, in different languages, at different times, with different priorities can interoperate at the protocol level. The federation is real because the protocol is robust.

This is the engineering wisdom that built the Internet. The Foundation has chosen to apply it to synthetic intelligence because it is the wisdom most likely to keep the Warp federation honest about its decentralization. *The Internet did not become centralized because its protocols required centralization. It became centralized because its participants accepted, over time, the conveniences that centralized operators offered.* The Capability Bus is built on the explicit understanding that the Foundation must, at the protocol level, refuse those conveniences. The price of decentralized federation is the work of doing it the hard way.

It is worth doing the hard way. The next chapter describes the Compute Farm, which is what happens when the Capability Bus is asked to manage not only routing but also where, exactly, the inference work runs.

---

## Endnotes

[^1]: Jon Postel, ed., "Transmission Control Protocol — DARPA Internet Program — Protocol Specification," RFC 793, USC/Information Sciences Institute (September 1981), §2.10. Online: https://datatracker.ietf.org/doc/html/rfc793. The robustness principle was reiterated and formalized in RFC 1122, "Requirements for Internet Hosts — Communication Layers" (R. Braden, ed., October 1989), and has been the subject of considerable debate in subsequent decades — particularly the question of whether liberal acceptance creates security risks that ought to be balanced against the interoperability benefits. The Foundation's view is that for protocols intended to enable cross-community federation among independently implemented peers, the principle remains correct, with security mediated by the cryptographic-authentication and capability-scope mechanisms that the protocol itself enforces.
