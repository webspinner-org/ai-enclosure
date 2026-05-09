# Chapter 18
## Cost Architectures Compared

> *Costs do not exist to be calculated. Costs exist to be reduced.*
>
> — Peter F. Drucker, *Managing for Results* (1964)

In 1964, the management theorist Peter Drucker published *Managing for Results*, in which he made what he called the central economic observation about modern enterprises: that the executives of large organizations spent enormous energy *measuring* their costs while spending almost no energy on the structural choices that produced those costs in the first place. The accounting departments were sophisticated. The architectural choices that had committed the organization to those costs in the first place were, in most cases, almost unexamined. *Costs do not exist to be calculated. Costs exist to be reduced.*[^1]

Part IV of this book — the four chapters that follow this one and the controversial one that closes the part — compares Warp and hyperscale across the four dimensions where the comparison is operationally meaningful: cost, environmental footprint, privacy posture, and capability. This chapter is the first comparison: the cost architectures themselves, side by side, with attention to where the curves cross and what the marginal-cost-per-user comparison actually says.

The previous chapters of this book have made cost claims in passing. This chapter assembles them, makes the comparison rigorous, and lands where the math leads. *The hyperscale architecture is more expensive than Warp for the user, in steady state, by margins large enough to constitute the dominant fact about the comparison.*

---

### Hyperscale Unit Economics

The hyperscale operator's cost structure has been built up across the chapters of Part I. Let me consolidate it.

A hyperscale data center capable of frontier inference work costs, in 2025–2026 dollars, between several hundred million and several billion dollars to build, depending on size, location, and power configuration. The four largest American hyperscalers spent collectively approximately $443 billion on capital expenditure in 2025 and are projected to spend approximately $602 billion in 2026, with roughly three-quarters of that capital flowing to synthetic-intelligence infrastructure. The Stargate Project alone proposes $500 billion of new infrastructure by 2029, with ten gigawatts of dedicated power capacity. (Chapters 1 and 2 cite these figures to their primary sources.)

The cost structure at the data-center level has the following components, in roughly the order of magnitude they contribute to total cost:

- **Capital cost of the hardware**, dominated by GPUs and accelerators, with NVIDIA H100/H200/B200-class units costing on the order of $25,000–$45,000 each at fleet pricing, deployed in clusters of tens of thousands at a single facility.
- **Capital cost of the building**, including the shell, the cooling infrastructure, the on-site power distribution, and the redundant systems that allow continuous operation.
- **Operational cost of electricity**, at hundreds of megawatts continuous load per facility, with annual electricity bills running into the hundreds of millions of dollars per facility at industrial rates.
- **Operational cost of water**, for evaporative cooling, with the per-facility consumption of clean freshwater running into the millions of liters per day.
- **Operational cost of personnel**, including the data-center operations staff, the security staff, the facilities staff, and the substantial software-engineering and research-and-development organizations that maintain the underlying services.
- **Cost of capital**, including the interest on the substantial debt the major operators have raised to finance the expansion ($108 billion of new debt issued by hyperscalers in 2025 alone, with industry projections of $1.5 trillion in further issuance).
- **Margin** sufficient to amortize all of the above, satisfy shareholder return requirements, fund the next round of expansion, and pay for the regulatory, lobbying, marketing, and administrative overhead the operator carries.

Distributed across the operator's user base, this cost structure resolves to a price the user sees as their monthly subscription, the per-token API fee, the enterprise contract minimum, or some combination. The arithmetic of how the operator's costs translate to the user's price involves the operator's gross margin, which (per Chapter 15) is in the range of 40–70 percent for consumer-tier services — meaning the user pays roughly 1.7× to 3.3× what the underlying inference actually costs the operator to produce.

For an individual user with active synthetic-intelligence needs, the bill is, in 2026, somewhere between $20 and $200 per month for the personal tier, with enterprise tiers in the hundreds to low thousands per seat per month. *This is the cost the user pays. It is not the cost of the work.*

---

### Warp Unit Economics

The Warp user's cost structure looks fundamentally different. There is no large up-front infrastructure investment to amortize — because the user's hardware is already paid for and is being used for purposes other than synthetic intelligence anyway. There is no operator margin — because there is no operator. There is no debt-service cost — because the architecture has no operator debt. There is no marketing cost — because there is no operator marketing.

The Warp user's cost structure is:

- **Marginal electricity** for inference. Per Chapter 6, this works out to approximately 0.4–0.5 kWh per million output tokens on representative Apple Silicon hardware, or a few cents per million tokens at typical residential electricity rates. For a heavy user generating, say, fifty million tokens per month, the marginal electricity cost is on the order of one to three dollars per month.
- **Optional capital** if the user chooses to augment their setup. A user happy with their existing laptop pays nothing additional. A user who buys a Mac Studio or builds a desktop with a discrete GPU spends a few thousand dollars one-time, amortized across several years of use, plus a small ongoing electricity cost for the always-on machine.
- **BYOK provider charges** when the user invokes a frontier model. Per Chapter 15, BYOK pricing is between thirty and fifty percent of comparable hyperscale subscription pricing for equivalent capability. For a user who invokes frontier models for, say, ten percent of their workload (with the rest handled locally), the BYOK component might be five to twenty dollars per month at typical use intensities.
- **Optional managed-Cell hosting**, if the user chooses to run their Cell on hosted hardware. Pricing varies by host but is typically in the range of $10–$50 per month for personal use, far below hyperscale subscription pricing for comparable functionality.
- **Time spent on configuration and maintenance**. Not a cash cost, but a real one. The reference Cell tooling minimizes this; ordinary users report a few hours of initial setup and approximately monthly attention thereafter.

For an individual user with the same workload that would run them $50–$100 per month on a hyperscale subscription, a Warp Cell with sensible BYOK invocation typically runs $5–$25 per month, with the remaining cost being electricity and amortized hardware that the user was paying anyway.

The cost ratio is, in steady state, roughly 4:1 to 10:1 in the user's favor. *The user gets the same work done for between ten and twenty-five percent of what the hyperscale arrangement would have cost.*

---

### Where the Curves Cross

It is fair to ask whether there are workload regimes where the cost comparison goes the other way. The honest answer is yes, and they are worth naming.

**Very-high-throughput sustained inference.** A user generating, say, one billion tokens per day — a software service that is using synthetic intelligence as its core engine, not a working professional using it as a tool — exceeds the throughput of practical Apple Silicon configurations. Such a user can run a multi-Cell federation, can buy higher-end hardware, or can simply buy substantial BYOK capacity. The cost crossover happens at workload levels that very few individual users approach but that some specialized commercial deployments do reach.

**Frontier-model-only workloads.** A user whose work *requires* the frontier model — research at the state of the art, certain very-long-context tasks, multimodal work that the open-weight ecosystem does not yet match — invokes the frontier provider for nearly every query. Such a user gets little benefit from local inference and is, in effect, running a Cell as a thin wrapper around BYOK calls. The cost is dominated by the provider's per-token pricing, with the architecture providing privacy and contractual benefits but minimal cost reduction over a direct provider account.

**Very-light-use users.** A user who uses synthetic intelligence very lightly — a few queries per week — pays the hyperscale subscription almost entirely as overhead, with low actual usage. For such a user, BYOK with a Cell might pay only a few cents per month, but the user has to bear the operational overhead of running a Cell at all. For *very* light use, the operational overhead may exceed the cost savings, and the cost case for Warp is weaker (though the privacy and sovereignty cases, of course, remain).

**Users without existing capable hardware.** A user whose only computer is a Chromebook or an older laptop without sufficient memory for local inference must either buy hardware or rely heavily on BYOK and managed Cells. The capital cost of suitable hardware is real, even when amortized; users without capable hardware see a smaller cost advantage in the short term, though the long-term picture remains favorable.

For the *typical* working user with a modern laptop and moderate-to-heavy synthetic-intelligence needs, the cost crossover does not happen at any realistic workload. Warp is cheaper at the workloads users actually run.

---

### The Marginal-Cost-Per-User Insight

Here is the deepest cost difference between the architectures, the one that explains why the comparison cannot be closed by hyperscalers without changing their architecture.

In the hyperscale architecture, the operator's *marginal cost of adding a new user* is non-zero. Each new user adds incremental load to the data center, requires incremental compute capacity, requires incremental storage, requires incremental support staff, requires incremental infrastructure provisioning, and (over time) requires incremental data-center expansion. The operator's per-user cost has a hard floor — the marginal cost of provisioning that user — beneath which the operator's pricing cannot fall without losing money on each customer.

In the Warp architecture, the *federation's* marginal cost of adding a new user is approximately zero. The new user brings their own hardware, their own electricity, their own contributions to the federated compute pool. The federation does not need to provision capacity for the new user; the new user provisions their own. The federation's aggregate capacity grows with each user joining, rather than needing to be expanded by an operator's capital plan to accommodate them.

This is the deep economic insight of the architecture. *The marginal cost per user is the user's own hardware and electricity, which the user pays directly*; the federation has no operator to extract margin from each marginal user. The hyperscale architecture, by contrast, must always have an operator pricing the marginal cost above the marginal cost-of-service or losing money — and the operator's margin is the user's premium.

Aggregate this across a hundred million users. At hyperscale unit economics with average pricing of, say, $50 per month, the aggregate market is $60 billion per year flowing to operators. At Warp unit economics, the aggregate cost is the aggregate electricity (a few dollars per user per year) plus the aggregate BYOK spend (a fraction of the hyperscale equivalent), with the difference — perhaps $40 billion per year — staying with users instead of becoming operator revenue.

That difference is the wealth-redistribution consequence of the architectural choice. It is the consequence the hyperscale operators understand most clearly and are, by virtue of their business model, structurally incapable of allowing.

---

### What the Cost Comparison Does Not Say

I want to close, as the previous chapters have, with what the comparison does not show.

The cost comparison does not say that hyperscale operators are dishonest. They are not. Their cost structure is what it is; their pricing reflects the structure; their margins are typical of capital-intensive businesses. The comparison says that *the architecture* is expensive, not that the operators are gouging.

The cost comparison does not say that Warp is free. It is not. The user is paying — for hardware, for electricity, for BYOK invocations, for the time of configuration. The comparison says that the user is paying *less*, in cash terms, for the work the user actually wants done.

The cost comparison does not, by itself, settle the question of which architecture is preferable. A user who values the conveniences of operator-mediated service may rationally pay the hyperscale premium for those conveniences. A user who values privacy, sovereignty, environmental impact, or moral standing may rationally pay extra for Warp even where the cost case favors hyperscale. *Cost is one of four comparisons in Part IV, not the entire comparison.*

What the cost comparison does say is that *the cost case for Warp does not cost the user the other cases*. The four pillars of Warp — Green, Confidential, Sovereign, Moral — are not luxuries the user is being asked to pay extra for. They are *consequences* of an architecture that is, also, cheaper. The Value Triangle of Chapter 10 was the conceptual statement of this; this chapter is the cost arithmetic that confirms it.

The next chapter does the same comparison for environmental footprint.

---

## Endnotes

[^1]: Peter F. Drucker, *Managing for Results: Economic Tasks and Risk-Taking Decisions* (Harper & Row, 1964; reissued by HarperCollins, 1986). The "costs do not exist to be calculated" formulation is among the most cited in Drucker's corpus and is the through-line of the book's argument about cost-effectiveness as a property of the firm's *structure*, not its accounting. Drucker's broader work on management — including *The Effective Executive* (Harper & Row, 1967) and *The Practice of Management* (Harper & Row, 1954) — extends the argument across the executive's principal decisions. The connection to the architectural argument of this book is direct: cost in computing, like cost in any enterprise, is a property of structural choice, not of measurement.
