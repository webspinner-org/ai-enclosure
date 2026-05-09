# Chapter 19
## Environmental Footprints Compared

> *A thing is right when it tends to preserve the integrity, stability, and beauty of the biotic community. It is wrong when it tends otherwise.*
>
> — Aldo Leopold, *A Sand County Almanac* (1949)

In 1949, the year after Aldo Leopold's death, his essay collection *A Sand County Almanac* was published. The book closed with an essay called "The Land Ethic," in which Leopold articulated what would become the foundational principle of modern ecological ethics: that questions about how we use the natural world are properly judged not against narrow human convenience but against the *integrity, stability, and beauty of the biotic community* in which human use occurs.[^1]

This chapter compares the environmental footprints of the hyperscale and Warp architectures, judged against the standard Leopold proposed. The previous chapters of this book have made claims about both. This chapter assembles them into the side-by-side comparison the reader is owed.

I will argue, on the evidence the previous chapters have laid down, that the comparison is not close. Across every environmental dimension that admits of measurement — per-query energy, idle-state energy, embodied carbon, and the scaling behavior of each — Warp's footprint is materially smaller than hyperscale's, and the gap widens at scale rather than narrowing.

---

### Per-Query Energy

Per Chapter 6, a hyperscale H100 in production cluster context consumes approximately 1,000–1,500 watts at the wall, with PUE multipliers raising the grid-side draw to that range or above. Working through the published tokens-per-watt benchmarks yields approximately 2–4 kilowatt-hours of grid-side energy per million output tokens at H100-class hardware in mainstream hyperscale facilities. Newer hardware (B200 and successors in the most efficient facilities) brings this down by a factor of two to four under generous assumptions.

A modern Apple Silicon laptop generating the same million tokens consumes approximately 0.4–0.5 kilowatt-hours of wall-power, with no PUE multiplier, on residential or commercial electrical service the user is already paying for.

The per-query comparison, even with the most favorable assumptions for the hyperscale side, runs roughly 4× to 10× in Warp's favor for the workloads where local inference is sufficient. For workloads that genuinely require frontier capability and are invoked under BYOK, the energy cost equals the hyperscale energy cost (because it *is* the hyperscale energy cost), but the user is invoking the frontier provider only for the workloads that truly require it — typically ten to thirty percent of total inference. The blended footprint, across a typical user's workload mix, is dominated by the local-inference cost.

The cumulative effect is that a user running a Warp Cell consumes, on the user's electricity bill, between half a kilowatt-hour and a few kilowatt-hours per month of synthetic-intelligence-attributable energy. The comparable hyperscale subscription contributes, on the operator's electricity bill, between five and twenty-five kilowatt-hours per month per user — a difference of roughly an order of magnitude.

The order of magnitude is not anomalous. It is the expected consequence of moving inference off centralized infrastructure with PUE overhead, GPU oversubscription, and continuous load and onto user-owned hardware running on residential power on the user's existing HVAC.

---

### Idle-State Energy

The deeper comparison, the one Chapter 6 introduced and this chapter makes explicit, is the *idle-state* energy comparison.

A hyperscale data center has effectively no meaningful idle state. The operator has signed take-or-pay arrangements with regional utilities for tens to hundreds of megawatts of continuous power. The cooling infrastructure runs continuously. The thousands of GPUs in the facility consume substantial baseline power even when not actively serving inference, because the operating systems, the tensor frameworks, and the platform services are all running continuously. The data center *cannot* save energy by running fewer queries; the energy cost is paid whether queries are served or not.

A user-owned Cell, by contrast, has a meaningful idle state. The user's laptop draws eight to twelve watts at idle and forty to sixty watts under inference load. The *delta* — the additional power required to do useful synthetic-intelligence work on a machine that was going to be on anyway — is paid only when work is being done. When the user is not actively using the Cell, the Cell's energy cost approaches zero (or, in the case of a Cold-tier Cell with wake-on-demand, exactly zero until a federated invocation arrives).

The implication for the architecture's environmental scaling is profound. *In hyperscale, the data center's energy bill is set by capacity; in Warp, the federation's energy bill is set by use.* A federation of a million Cells with light average use draws approximately the energy of those Cells' light average use. A hyperscale data center serving the same workload draws approximately its provisioned capacity, regardless of the actual utilization.

This is the structural reason the hyperscale architecture scales environmentally worse than Warp does. The bigger the operator gets, the more capacity it must provision and the more continuous baseline energy it draws. The bigger the federation gets, the more capacity it has — but the energy cost is borne by the users in proportion to their actual use, not in proportion to the capacity sitting idle.

---

### Embodied Carbon

The environmental footprint of a computing infrastructure is not just the electricity it draws. It includes the *embodied* carbon of the hardware: the emissions associated with manufacturing the silicon, the boards, the cooling equipment, the building, the supporting infrastructure.

Per the published estimates cited in Chapter 6 (NVIDIA's own product carbon footprint disclosures and the academic literature on GPU lifecycle emissions): each H100 GPU has an embodied carbon footprint of roughly 164 kg CO2e for the silicon and supporting components, before deployment. Multiplied across the tens of thousands of GPUs in a single hyperscale cluster, the embodied carbon at deployment is in the multi-thousand-tonne range. Add the embodied carbon of the building, the cooling infrastructure, and the supporting servers and networking, and a single hyperscale data center represents on the order of tens of thousands of tonnes CO2e in embodied carbon at the moment of commissioning, before serving its first query.

A user-owned laptop has its own embodied carbon — a modern MacBook Pro is in the range of 200–400 kg CO2e for manufacturing, depending on configuration. Per user, this is comparable in order of magnitude to one user's allocated share of a hyperscale facility's embodied carbon, but with one critical difference: *the laptop is being used for many things, not just synthetic intelligence.* Only the marginal share of the laptop's embodied carbon attributable to synthetic-intelligence work is properly charged to the architecture; the rest is charged to the laptop's other uses (work, communication, entertainment, content creation), which the user would have a laptop for anyway.

The embodied-carbon comparison, properly amortized, runs strongly in Warp's favor. The user's existing laptop adds zero new embodied carbon to the synthetic-intelligence footprint. A hyperscale facility's GPUs are manufactured *specifically* for synthetic-intelligence workloads, and their embodied carbon is properly charged to that use case in full.

For a user who buys *new* hardware specifically for their Cell — a higher-end Mac, a desktop with a discrete GPU — the new hardware's embodied carbon does count, but per the GPU lifecycle literature, the use-phase emissions over the hardware's useful life dominate the embodied portion (typically 70–80% use, 20–30% embodied), and the use-phase emissions, on user-owned hardware, are dramatically lower than the equivalent hyperscale.

---

### Water

Per Chapter 1's citation of the Ren et al. work on AI water footprint: training the GPT-3 model required approximately 700,000 liters of clean freshwater for cooling-tower evaporation; global synthetic-intelligence water withdrawals are projected to reach 4.2–6.6 billion cubic meters per year by 2027; and the geographic distribution of hyperscale data centers in water-stressed regions (Arizona, Texas, Spain) makes the local impact disproportionate to the global figure.

The Warp architecture has no analogous water cost at the user-side. A laptop or desktop running on existing residential or commercial HVAC adds nothing to the user's water draw. The HVAC the user is running for human comfort is the HVAC that cools the inference work; no cooling-tower evaporation is required.

For BYOK invocations to frontier models, the user's share of the provider's water use is the same as the equivalent hyperscale account — proportional to actual frontier-model use, which is typically a small fraction of total workload. The federation does not, in itself, add water demand.

The water comparison is the least equivocal of the four environmental comparisons in this chapter. The hyperscale architecture has a meaningful water cost in stressed regions; Warp has effectively none.

---

### Scaling Behavior

The deepest difference between the architectures' environmental profiles is how they scale.

A hyperscale architecture serving N users scales its environmental footprint roughly proportionally to N. More users require more capacity; more capacity requires more buildings, more GPUs, more cooling, more water, more grid draw. Marginal-cost economics impose a scaling lower bound: the operator cannot serve more users without consuming more environmental resources, because each new user adds to the provisioned capacity the operator must build.

A Warp federation serving N users scales its environmental footprint roughly proportionally to *N's actual usage*, with the per-user marginal environmental cost being whatever electricity the user's hardware draws when actually running inference. Idle users add nothing. Light-use users add little. Heavy-use users add proportionally to their use. The federation's aggregate footprint is *bounded by aggregate usage*, not by aggregate capacity.

For any given level of useful work performed across the synthetic-intelligence ecosystem, the Warp architecture performs the work with a smaller environmental footprint than the hyperscale architecture, and the gap widens as the user base grows.

This is, in environmental terms, the Jevons-paradox response Chapter 1 anticipated. The rebound effect — that efficiency gains drive demand growth — operates in both architectures, but in the hyperscale case the rebound is paid by the data center's expansion, while in the Warp case the rebound is paid by the user's marginal electricity. The user's marginal electricity is typically a tiny fraction of what the data center's marginal expansion costs, in environmental terms.

---

### What This Comparison Does Not Say

This comparison does not say that Warp has no environmental cost. It does. Every kilowatt-hour the user's laptop draws for inference is a real kilowatt-hour from a real grid that includes some non-renewable generation. Every laptop the user owns has embodied carbon. The user's existing electricity may be sourced from a grid less clean than the hyperscaler's preferred-utility contracts.

This comparison does not say that all hyperscale data-center work should cease. There are workloads — frontier-model training, very-large-batch synchronous serving, certain research uses — for which centralized facilities are genuinely required, and the Warp architecture preserves the user's ability to invoke them under BYOK on the user's terms.

This comparison does not say that Warp will always be the more environmentally efficient option. As open-weight models continue to improve, as Apple Silicon's per-watt efficiency continues to climb, as cooperative compute matures, the gap will widen — but the comparison is sensitive to the underlying technology, which is evolving.

What this comparison does say is that the *current* environmental case for Warp is strong by every measure, that the gap is structural rather than incidental, and that the gap is likely to widen rather than narrow on the trajectory of the technology.

The next chapter compares the privacy postures of the two architectures.

---

## Endnotes

[^1]: Aldo Leopold, *A Sand County Almanac and Sketches Here and There* (Oxford University Press, 1949). The "Land Ethic" essay closes the volume; the "integrity, stability, and beauty of the biotic community" passage is the canonical formulation of Leopold's ecological ethics and is among the most cited lines in twentieth-century environmental writing. The book was published posthumously, having been completed shortly before Leopold's death in April 1948 fighting a grass fire on a neighbor's property in Wisconsin. Online text via various archives; the Aldo Leopold Foundation maintains the canonical primary-source reference: https://www.aldoleopold.org.
