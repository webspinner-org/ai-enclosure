# Chapter 14
## The Compute Farm — Cold, Warm, Hot

> *Volunteer computing harnesses idle computing power on millions of PCs to benefit science and other public-interest projects.*
>
> — David P. Anderson, "BOINC: A System for Public-Resource Computing and Storage" (2004)

In 1999, the SETI@home project at the University of California, Berkeley, released a screensaver. The screensaver downloaded small batches of radio-telescope data, analyzed the data for narrowband signals on the user's idle CPU, and reported the results back to a central coordination server. Within two years, SETI@home was running on more than three million home computers, collectively contributing more compute capacity to the search for extraterrestrial intelligence than any of the supercomputers of its era. The project's lead developer, David Anderson, generalized the platform into BOINC — the Berkeley Open Infrastructure for Network Computing — which now hosts dozens of public-interest scientific projects and remains, decades later, the canonical demonstration that the world's largest pool of underutilized compute capacity is the pool sitting on user-owned desks.[^1]

The Compute Farm of the Warp architecture inherits BOINC's central insight. *The hardware that ordinary users already own, when its idle capacity is intelligently aggregated and scheduled, constitutes a computing resource at hyperscale magnitudes — at residential operating cost.* Where BOINC's coordination was centralized (a project server distributed work units to volunteer machines), the Warp Compute Farm is federated (Cells negotiate work directly with one another), and where BOINC's workloads were specific scientific projects, the Compute Farm runs the open-ended workload of synthetic-intelligence inference. The substrate of underutilized consumer hardware, however, is the same substrate.

This chapter describes how the Compute Farm operates: how it categorizes Cell capacity into Cold, Warm, and Hot tiers; how it schedules work across those tiers under wake-on-demand economics; and how it uses speculative model spinning and predictive load shaping to deliver hyperscale-class responsiveness from distributed user-owned hardware.

---

### The Apple Silicon Advantage at Idle

Chapter 6 made the case that Apple Silicon is, watt for watt, materially efficient at synthetic-intelligence inference. The Compute Farm extends that case in the following way: *Apple Silicon is exceptionally efficient at idle, which means the marginal cost of waking up to do useful work is very small.*

A modern M-series MacBook Pro draws roughly eight to twelve watts at idle. The same machine, under inference load, draws forty to sixty watts. The *delta* — the additional power required to do useful synthetic-intelligence work on a machine that was going to be on anyway — is about thirty to fifty watts, sustained only as long as the inference work is being done. When the work completes, the machine returns to its idle state.

This is a fundamentally different thermal and economic profile than a hyperscale GPU server, which draws roughly its full operating power continuously regardless of whether useful work is being done at any given second. The hyperscale operator pays for the full thermal envelope twenty-four hours a day; the user with a laptop pays the *idle* envelope continuously and the *delta* envelope only when work is being done. The marginal cost structure of a Warp Cell is, in this sense, *the marginal cost structure of additional inference work on hardware that was already on*.

For the user themselves, this means that running their personal Cell adds, in dollar terms, perhaps a few cents per day to their electricity bill. For the federation, this means that the *aggregate* compute pool available to the network — when many Cells make their idle capacity available to one another under federation contracts — is genuinely large, and growing every time another user joins.

---

### Cold, Warm, Hot

The Compute Farm classifies a Cell's available compute capacity into three tiers, named for the latency at which the capacity can be brought to bear on a workload.

**Cold capacity** is the capacity of a Cell whose primary host is currently sleeping or fully off. Cold capacity is, in latency terms, slow to mobilize — typically tens of seconds, occasionally minutes, depending on the host hardware and the wake mechanism. Cold capacity is appropriate for *batch* workloads: long inference tasks, document corpus processing, training fine-tunes, large-scale retrieval indexing. The user can set their Cell's policy to permit cold-capacity participation in federation work, with the understanding that the cost of waking the host (a few additional watt-seconds of inrush plus the latency of boot or wake) is amortized across the work being done.

**Warm capacity** is the capacity of a Cell whose primary host is awake and idle, with the Cell's processes running and ready to accept work, but with no active workload at the moment. Warm capacity is fast to mobilize — typically under a second from the receipt of a federated invocation to the start of work. Warm capacity is appropriate for *interactive* workloads from federated peers: a family member's question that the user's Cell can answer faster than the family member's own Cell, a community member's query that benefits from the Cell's specialized model, a small-business client's request that the firm's Cell can handle from its institutional Grimoire.

**Hot capacity** is the capacity of a Cell currently running a workload, with available headroom for additional concurrent work. Hot capacity has effectively zero mobilization latency, because the work begins immediately on top of an already-running process. Hot capacity is appropriate for *sustained* workloads: a Cell serving multiple federated peers in parallel, a community Cell handling many simultaneous queries, a small-business Cell sustaining a daily working tempo.

The Compute Farm's scheduling logic — implemented in the Weaver of each Cell, with capability-scoped negotiation over the Capability Bus — matches incoming workloads to the most appropriate tier of capacity available among the Cells in the federation. A query that needs an answer in under a second is routed to a peer with hot or warm capacity. A bulk overnight task is routed to a peer with cold capacity that can be woken on the user's preferred schedule. The match is made by the bus protocol, with each participating Cell evaluating each potential work assignment against its own policy and its own current state.

The user does not, in the typical case, need to think about any of this. The user submits queries to their own Loom; the Weaver decides whether to handle the query locally or federate it; if federated, the Weaver selects the appropriate peer based on capability scope, sensitivity rules, and capacity tier; the response comes back through the same path. *The capacity tiering is an internal detail of the federation*, not a knob the user has to turn for ordinary work.

---

### Wake-on-Demand Economics

The Cold tier is interesting because it is the tier that breaks the most assumptions about cooperative compute.

Conventional cooperative-computing systems (BOINC and its successors) require the user to leave their machine on continuously. The user is volunteering not just compute but also the electricity required to keep the machine awake during otherwise-idle periods. This is a meaningful contribution but a bounded one — most users will not leave a desktop machine running twenty-four hours a day for a federation they are not directly using.

The Cold tier solves this with *wake-on-demand*. A Cell whose host hardware supports Wake-on-LAN (most desktops, many laptops in their docked configurations) or Wake-on-Network (Apple Silicon Macs in standard sleep) can advertise Cold capacity to the federation. When a federated workload is matched to that Cell, the Capability Bus's transport layer issues a wake packet, the host wakes, the Cell processes the work, and the host returns to sleep when the work is complete and the wake-keepalive interval elapses.

The economic significance is straightforward. The user has agreed, by participating in the Cold tier of federation, to make their hardware available *only when needed*, and the cost to the user is *only the marginal energy of the wake-and-work cycle*. The user is not paying to keep the hardware running continuously; the hardware is mostly off, and only briefly on when the federation has work for it.

For the federation, this means that the Cold tier represents a vast pool of latent capacity that is, on a marginal basis, very cheap to mobilize. A federation of a hundred Cells, with each member's Cold tier available for an average of an hour per day of federated work (because the federation's aggregate workload is rarely large enough to require more), has effectively a hundred Cell-hours per day of distributed compute available — the equivalent of a small but meaningful continuous compute pool, at a fraction of the energy cost of running that pool centrally.

The wake-on-demand pattern is not, by itself, an architecture. It is a *technique* the Compute Farm uses, alongside the more conventional warm-and-hot patterns, to extract useful capacity from a substrate that would otherwise be wasted.

---

### Speculative Model Spinning

The next technique the Compute Farm uses is *speculative model spinning* — the practice of pre-loading specific models onto specific Cells in anticipation of the workloads that are likely to require them.

A Cell's Weaver, in its native configuration, has one or a small number of models loaded into memory. Loading a new model — pulling the weights from disk, allocating GPU memory, initializing the inference framework — takes between several seconds (for small models) and a minute or two (for larger ones). For a single user with stable workload patterns, loading is a one-time cost paid at startup.

For a federation handling diverse workloads, model loading can become a bottleneck. A community Cell that needs to handle inference for a code-review query (best served by a code-specialized model), a medical-summary query (best served by a medical-fine-tuned model), and a translation query (best served by a multilingual model) cannot, in general, hold all three models in memory simultaneously on a single host. Switching between them imposes latency.

Speculative model spinning addresses this by *predicting* which models will be needed when, on which Cells, and pre-loading them ahead of need. The prediction draws on:

- **Historical workload patterns.** A Cell that has handled medical queries every weekday morning for the last six months is likely to handle one this morning.
- **Federation-level load shaping.** When a peer Cell signals that it expects a surge of code-review queries, neighboring Cells with code-specialized capacity can pre-spin those models.
- **Capacity availability.** A Cell with substantial unified-memory headroom can speculatively hold multiple models loaded; a Cell with constrained memory holds only its primary model and takes the loading cost when other models are needed.

Speculative loading costs energy — a model held in memory consumes some inference-ready power even when idle. The Compute Farm's scheduling logic balances the energy cost of speculative loading against the latency cost of on-demand loading, with the user's own policy preferences (favor latency, favor energy) shaping the balance.

The cumulative effect is that a federation of Cells, with intelligent model placement, can serve diverse workloads at *response times approaching those of a single hyperscale facility holding many models on hot standby* — without requiring any single Cell to provision all the models, all the time.

---

### Predictive Load Shaping

The companion to speculative model spinning is *predictive load shaping*: anticipating the workload patterns of the federation and arranging the Cells' capacity accordingly.

For a typical small-business federation — a law firm, a medical practice, a design studio — the workload pattern is heavily diurnal. Queries spike during working hours; the federation is largely quiet overnight and on weekends. Predictive load shaping recognizes this pattern and arranges Cells to be in their Hot or Warm tiers during the predicted peak, and to drop to Cold tier (with wake-on-demand) during predicted troughs.

For a community federation — a neighborhood association, a school district — the pattern may be different. School districts spike in midday and early evening when students are working on assignments; neighborhood associations spike in early evening when residents are home and engaged.

For a research federation, the pattern may include scheduled batch work (corpus indexing, fine-tune training) during otherwise-quiet periods, with the batch work itself shapeable to fit available capacity.

The Compute Farm's load-shaping logic reads the federation's recent history, applies straightforward time-series forecasting, and adjusts each Cell's tier transitions accordingly. The forecasting is local to each federation — no central coordinator is required — and the federation's members can review and adjust the predictions through the Loom interface of any participating Cell.

This is the kind of operational work that hyperscale operators do for their data centers, with teams of capacity engineers and proprietary scheduling systems. The Foundation's contribution is to make the same kind of capacity engineering tractable *at federation scale*, with reference implementations that any community can adopt.

---

### What Distributes Without Centralizing

The Compute Farm is, in summary, the architectural mechanism that allows the Warp federation to deliver computational responsiveness comparable to centralized hyperscale, from a substrate of distributed user-owned hardware, without ever centralizing the substrate itself.

The components are:

- **Cold/Warm/Hot capacity tiers** that match workload urgency to mobilization latency.
- **Wake-on-demand economics** that allow Cells to participate in federation without paying the cost of continuous availability.
- **Speculative model spinning** that pre-positions inference capability where it will be needed.
- **Predictive load shaping** that anticipates demand and arranges capacity accordingly.

None of these components requires a central operator. Each is implemented as a protocol behavior within the Capability Bus and the Cells participating in it. A federation that grows from ten Cells to ten thousand operates the same protocols at the same per-Cell cost; the protocols scale because they were designed not to require a central choke point in the first place.

This is what *cooperative* compute looks like, in the sense Chapter 4 named the next phase of computing history. It is not the personal computer of 1985, alone on a desk, doing only what its owner could fit on it. It is also not the hyperscale cloud, with everyone's work in a few operators' facilities. It is *a federation of personal computers*, doing collectively what no one of them could do alone, with each owner retaining control over their own contribution and their own consumption.

The next chapter describes BYOK — the contractual mechanism by which Cells invoke frontier capability when frontier capability is what's needed, on the user's terms, from the user's own account.

---

## Endnotes

[^1]: David P. Anderson, "BOINC: A System for Public-Resource Computing and Storage," *Proceedings of the 5th IEEE/ACM International Workshop on Grid Computing* (November 2004). https://boinc.berkeley.edu/boinc.pdf. The earlier SETI@home work is documented in: David P. Anderson, Jeff Cobb, Eric Korpela, Matt Lebofsky, and Dan Werthimer, "SETI@home: An Experiment in Public-Resource Computing," *Communications of the ACM*, vol. 45, no. 11 (November 2002), pp. 56–61. https://dl.acm.org/doi/10.1145/581571.581573. As of the early 2010s, BOINC-managed projects collectively delivered exaflop-class compute capacity from volunteer hardware, comparable to the largest supercomputers of the era.
