# Chapter 6
## Green SI — The Environmental Pillar

> *Small-scale operations, no matter how numerous, are always less likely to be harmful to the natural environment than large-scale ones, simply because their individual force is small in relation to the recuperative forces of nature.*
>
> — E. F. Schumacher, *Small Is Beautiful: Economics as if People Mattered* (1973)

The first pillar of Warp is environmental.

Chapter 1 made the case that hyperscale Synthetic Intelligence is, in its centralized form, structurally unsustainable: that it consumes industrial-scale electricity, evaporates clean water in regions that cannot spare it, accumulates embodied carbon in supply chains the operators do not control, and grows in all of these dimensions faster than efficiency improvements can offset. *Green SI* — the environmental pillar of Warp — is the architecture's structural answer to that diagnosis.

The argument of this chapter has three parts. The first is that the hardware most users already own is, watt for watt, materially more efficient at synthetic-intelligence work than the data-center hardware that hyperscalers have spent the last three years installing. The second is that distributed cooperative compute, layered on top of that hardware, can do most of the work the hyperscalers are doing today, with most of the responsiveness, at most of the quality, at a fraction of the environmental cost. The third is that this is not an aspirational claim. The hardware exists, the models exist, the math has been done. What is missing is the architectural commitment to organize around it.

E. F. Schumacher made the general case for small-scale operations against large-scale ones in 1973 — that small operations, by virtue of their bounded individual force, fall within the recuperative range of the natural systems they affect. Industrial-scale extraction does not. The argument generalizes to electricity. A million households running synthetic intelligence on hardware they already own draws on a million existing connections to the grid, distributed across a million regional substations, on patterns of consumption the grid was built to handle. A handful of hyperscale data centers consuming the equivalent power, concentrated in five or six counties, in the form of multi-hundred-megawatt step-loads, *was not*.

This chapter walks through the numbers.

---

### Apple Silicon's Idle-Cost Economics

The single most important hardware fact for Green SI is one that is rarely discussed in the popular coverage of synthetic intelligence: *the consumer hardware that almost every developer, designer, and small-business owner already owns is now competent inference hardware for substantial classes of useful synthetic-intelligence work.*

I am writing this chapter on a MacBook Pro with an M-series Apple Silicon chip. The same machine, when I direct it to, runs a quantized open-weight language model locally — typically generating thirty to forty tokens per second on a Llama-class 30-to-70-billion-parameter model, fast enough to be conversational, accurate enough to be useful for the bulk of my drafting and research workflow. While doing this, the laptop draws roughly fifty watts at the wall. When I am not running inference, it returns to a near-idle state and draws perhaps eight to twelve watts. The energy I use to produce useful synthetic-intelligence output, on this machine, is the energy I am already paying for to keep the machine on.[^1]

The economic-environmental significance of this fact takes a moment to absorb.

A hyperscale H100 GPU — the workhorse training and inference accelerator of 2024 and 2025 — has a thermal design power of 700 watts. When the cost of the surrounding server, networking, cooling, and data-center infrastructure is included, *each H100 in a production cluster effectively consumes between 1,000 and 1,500 watts at the wall.* The H200 and B200 successors have improved tokens-per-watt at the GPU level, but the surrounding infrastructure costs are similar.[^2]

Even before considering tokens-per-watt at the silicon level, the contrast in what the *grid* sees is severe. A hyperscale data center is, from the grid's perspective, a multi-hundred-megawatt continuous load that runs at high utilization regardless of whether useful work is being done at any given second, because the operator has signed a take-or-pay arrangement with the regional utility and is paying for the capacity whether it is drawn or not. Your laptop is a fifty-watt intermittent load that draws power only when you are actually using it.

This is what is meant by *idle-cost economics*. The hyperscale model has *no* meaningful idle state. Every hour the data center exists, it is consuming approximately the same amount of electricity, regardless of whether any user is requesting any service. The Apple Silicon model is the opposite: when you are not using your laptop for inference, your laptop is drawing nearly no power for inference. The cost of synthetic intelligence, in the Warp architecture, scales with the work being done — not with the capacity being held in reserve.

Add to this the second fact, which Apple has been quietly working toward for five years: the unified memory architecture of Apple Silicon shares a single pool of high-bandwidth memory between CPU, GPU, and Neural Engine. A modern M3 Ultra or M4 Max can address 128 to 192 gigabytes of unified memory at hundreds of gigabytes per second of bandwidth, sufficient to load and run models that, on a discrete-GPU PC, would require a server-class graphics card costing many times the price of the laptop. The unified-memory design is *more efficient* than the discrete-GPU design for inference of large models, because the cost of moving tensors between system memory and GPU memory — a cost that dominates many inference workloads on PC architectures — has been engineered out.[^3]

The cumulative effect, when you account for hardware power draw, data-center overhead, idle-state behavior, and the unified-memory architecture, is that the hardware in your hand is in the same neighborhood of energy efficiency as the hardware in a hyperscale data center for many useful inference workloads — and in some cases, on a per-token-per-watt basis, *better*. The Webspinner Foundation's internal modeling places the cumulative environmental advantage of distributed Apple-Silicon-class inference, against the centralized hyperscale path, in the range of approximately 8 to 10 times for representative workloads, once data-center PUE, idle-state behavior, and embodied-carbon amortization are included. The exact multiplier depends on assumptions; the order of magnitude does not.[^4]

I want to be careful here. This is not a claim that consumer hardware will replace hyperscale GPUs for *all* workloads, and it is not a claim that an M-series Mac is a frontier-model training rig. It is not. The claim is narrower and more important: *for the inference workloads that account for the majority of useful day-to-day synthetic-intelligence work, the consumer hardware is sufficient, and it consumes dramatically less energy than the centralized alternative.*

---

### Cooperative Compute and Edge Offload

The second component of the Green SI argument is what happens when many user-owned Cells cooperate.

A single Cell, running on a single laptop, is sufficient for one user's day-to-day work. A Cell augmented with a desktop or a Mac Studio is sufficient for a small business. A small federation of Cells — three or four households on the same street, a dozen members of a small cooperative, a school district with a Cell per classroom — can pool their otherwise-idle compute capacity to handle workloads that exceed any single Cell's resources, while still keeping the work entirely within their own infrastructure.

This is not a novel pattern. The model of cooperative compute is what the SETI@home project demonstrated in 1999, what the BOINC platform has been running for two decades, and what every blockchain network proves out (in a different and much less efficient way) every minute of every day. Capacity that sits idle on user-owned hardware can be aggregated, scheduled, and applied to common work without requiring a central operator to own the underlying infrastructure.

For synthetic intelligence specifically, three patterns of cooperative compute are operationally relevant:

1. **Federated retrieval.** A Cell's Grimoire holds the user's own corpus. When the user asks a question, retrieval against their own corpus happens locally. When the question would benefit from corpora the user does not hold — a community library's catalog, a partner organization's shared research, a publicly available knowledge base — the Cell federates the retrieval request to the relevant remote Cell, which answers from its own Grimoire and returns only the result. The full corpus does not move. Only the relevant fragments move. This is exponentially less data-intensive than the hyperscale model, in which every query is, in effect, evaluated against the hyperscaler's globally aggregated corpus.

2. **Cooperative inference.** When a user's question is too large for their own Cell to answer well — a long document summarization, a complex multi-step reasoning task, a multi-modal query — the Cell can route part of the work to a peer Cell with surplus capacity, with the peer's owner's permission, under capability-scoped credentials. The cost to the peer is the marginal energy of running the inference on hardware that was, on average, otherwise idle. The cost to the network is a tiny fraction of the equivalent hyperscale call.

3. **Edge offload to community-operated capacity.** Some Cells, by design, are cooperatives. A community-operated Cell, hosted by a library, a school, a religious institution, or a small commercial operator, can serve as a local capacity buffer for households whose individual hardware is not always sufficient. The community Cell is governed by its community, paid for by its community, and used by its community. It is not Microsoft, Google, or Amazon. It does not need to be.

The cumulative effect of these three patterns is that the marginal energy cost of an additional user joining the Warp network is, in most cases, *the energy that user's own hardware was already drawing.* This is not the case in the hyperscale model, where the marginal user requires the operator to provision additional capacity in a data center, with all of the embodied carbon, water, cooling, and grid-impact costs that follow.

A network in which marginal cost approaches the energy already being consumed by user-owned hardware is, in environmental terms, a fundamentally different kind of network than one in which marginal cost requires new industrial infrastructure.

---

### Real Numbers: kWh per Million Tokens

Let me put a few specific numbers on the page, with the appropriate caveats.

A hyperscale H100 in a production cluster, by available analyst benchmarks at the end of 2025, generates roughly $0.09 per million output tokens on a representative open-weight model under standard inference frameworks. Working backward through the published tokens-per-watt and PUE figures, this corresponds to approximately *2 to 4 kilowatt-hours of grid-side energy per million tokens served*, depending on the model, the batch size, and the data center's PUE. The newest hardware (B200 and successors, in the better data centers) brings this number down by an additional factor of two to four — the upper bound of which we will be generous with and grant to the hyperscalers for this calculation.[^5]

A modern Apple Silicon laptop, running a quantized 30-to-70-billion-parameter model at typical conversational throughput, generates roughly 30 to 40 output tokens per second at 50 watts of system draw. At those rates, *one million output tokens corresponds to approximately seven to nine hours of inference, at a total cost of roughly 0.4 to 0.5 kilowatt-hours.* No PUE multiplier applies, because the laptop is on the user's existing electrical service in their home or office, where the cooling cost is whatever HVAC the user was already running.[^6]

The comparison, taken at face value, suggests that a user generating a million tokens of inference on their own laptop consumes between 4 and 10 times less grid-side energy than the equivalent inference performed in a hyperscale data center. This is roughly consistent with the 8–10× advantage that the Foundation's modeling has anchored on for representative workloads.

Three caveats are essential:

- These numbers are *average-case representative*, not worst-case. There exist workloads — frontier-model invocation, very-large-batch synchronous serving, training — for which the hyperscale path retains a substantial efficiency advantage at the hardware level. The Warp architecture explicitly preserves the user's ability to invoke frontier hyperscale capability under BYOK contract for those cases (Chapter 15). What it does *not* require is that ordinary day-to-day inference run there.
- The numbers do not include embodied carbon. Embodied carbon is roughly 20 to 30 percent of the lifecycle environmental footprint of a GPU in a data center. The corresponding number for a consumer laptop is similar in proportion, but lower in absolute terms, because the laptop is built once and used for many things; only the marginal portion attributable to inference work is properly charged to inference.
- The numbers depend on the user actually doing useful work with their hardware. A laptop running an idle Cell that is rarely queried is not, environmentally, an improvement over a hyperscale account that is rarely queried. The advantage materializes when the architecture is used.

The takeaway, with all caveats, is that the order of magnitude is real. For the bulk of useful synthetic-intelligence work, distributed user-owned inference is *between half an order and a full order of magnitude* less energy-intensive than hyperscale inference. Multiplied across a billion users, the difference is the difference between a sustainable computing future and the trap described in Chapter 1.

---

### Grid Implications and Community Impact

The most underappreciated consequence of distributed compute, environmentally, is what it does not do to the grid.

Northern Virginia, as Chapter 1 detailed, is now under measurable strain from data-center demand. Dominion Energy is filing for fourteen-percent residential rate increases. Loudoun County residents are in court to stop transmission lines. Three Mile Island has been brought back from the dead specifically to power Microsoft data centers. Ireland has been forced to impose, lift, and re-condition a moratorium on new data-center grid connections. None of this would be necessary if the inference workloads could be distributed across the existing residential and commercial electrical infrastructure that those same regions already have.

The Warp architecture, at scale, has the following grid effects:

- **No new step-loads.** The grid does not see a new hundred-megawatt continuous load demanded by a single counterparty. It sees a million ten-watt increases distributed across a million existing connections, well within normal residential and commercial load patterns.
- **No new transmission lines.** Distributed compute does not require new high-voltage transmission corridors carved through neighborhoods. It uses the wires that are already there.
- **No new data-center water draw.** A laptop or desktop on existing HVAC adds nothing to a region's water demand. A hyperscale data center demands cooling-tower evaporation in the millions of liters per facility per day.
- **No revival of retired generation.** The grid does not need Three Mile Island, the Bowie coal plant, or any other shuttered facility to be brought back online to serve user-owned inference. The inference is already running on existing power.

There is a community dimension here that deserves naming. The hyperscale path, by concentrating compute in a small number of host counties, concentrates the *costs* of compute on a small number of host communities. The benefits accrue to a global user base; the burdens accrue to the residents of Loudoun, Ashburn, Manassas, Mesa, Phoenix, Dublin, and a handful of others. This is not, by the standards of any equitable framework I am aware of, a defensible distribution.

The Warp path puts the costs and benefits on the same household. The user who runs a Cell pays for the energy their Cell consumes, on their own utility bill, with full visibility into what they are paying for. They are not asking residents of Loudoun County to subsidize their work. The economic flow and the environmental flow run, here, in the same direction. That is what *sovereignty*, in environmental terms, looks like.

---

### A Note on the Frontier

I want to be clear about one final thing, because the rest of the book will return to it.

The architecture this chapter describes does *not* eliminate the need for frontier-scale compute. There remain workloads — training the next generation of models, serving extremely large synchronous user populations, running multi-modal models with parameter counts that no consumer hardware can hold — for which centralized facilities, with their associated environmental costs, are genuinely required.

The Foundation's position is not that frontier compute should not exist. It is that frontier compute should be a *resource that users invoke when they need it, on terms they negotiate, with full understanding of the environmental cost.* That is the BYOK pattern of Chapter 15, and it is structurally different from the present arrangement, in which all inference — frontier and ordinary — is consolidated at the same data centers, on the same operator's terms, billed and accounted for in the same opaque way.

A user who runs ninety-five percent of their inference on their own Cell, and invokes a frontier model for the remaining five percent under a deliberate BYOK contract, has structurally bent the environmental curve relative to a user who runs a hundred percent of their inference through a hyperscale account. Multiplied across a hundred million users, the bend is the difference.

That bend is the affirmative environmental case for Warp. The next pillar — Confidential SI — bends a different curve.

---

## Endnotes

[^1]: System power figures for Apple Silicon under inference load are aggregated from independent benchmarks: Markus Schall, "Mac with M3 Ultra against RTX 5090: Efficiency instead of watts" (2025); the *llama.cpp* community's M-series performance discussion (GitHub: ggml-org/llama.cpp, Discussion #4167); ModelPiper, "Local LLM Benchmarks on Apple Silicon: Token Speed Across M1 to M4" (2025); and the *Intelligence per Watt* preprint (arXiv:2511.07885, 2025). M3 Max system power under inference load is consistently reported in the 40–80 W range; idle is in the 8–12 W range; throughput on quantized 30–70 B-parameter models is in the 30–40 tokens-per-second range for typical conversational use.

[^2]: NVIDIA H100 product brief (NVIDIA, March 2024); H100 vs H200 vs B200 comparison (Introl Blog, 2025); SemiAnalysis, "H100 vs GB200 NVL72 Training Benchmarks" (2025); empirically calibrated H100 node power models (arXiv:2506.14551, 2025). H100 GPU TDP is 700 W; full-cluster power draw including server overhead and cooling is reported between 1,000 and 1,500 W per GPU depending on configuration. The H200 retains 700 W TDP while improving memory bandwidth from 3.35 to 4.8 TB/s, which is the source of its better tokens-per-watt at the silicon level.

[^3]: Apple Silicon unified memory architecture details from Apple's developer documentation and Scalastic, "Apple Silicon vs NVIDIA CUDA: AI Comparison 2025, Benchmarks, Advantages and Limitations" (2025). Compute Market, "Mac Mini M4 for AI 2026 — LLM Benchmarks & Review" (2026); Will It Run AI, "Apple Silicon for AI: M4 vs M3 vs M2 Comparison (2026)." The unified-memory advantage is most pronounced on inference workloads of large models that approach or exceed discrete-GPU VRAM capacity.

[^4]: The 8–10× cumulative environmental-advantage figure is the Webspinner Foundation's own modeling estimate for representative workloads, taking into account: (a) raw tokens-per-watt at the hardware level; (b) data-center PUE multiplier (averaging 1.5 across the global fleet, 1.09 in the most efficient hyperscale facilities, per Statista 2025 and Google's published 2024 fleet figure); (c) data-center idle-state behavior (full-capacity provisioning regardless of utilization); (d) embodied-carbon amortization across the lifecycle. The Foundation's working spreadsheet is available on request and will be published with the next architecture release. Independent academic modeling on related questions includes "Towards Carbon-efficient LLM Life Cycle" (HotCarbon, 2024) and the *Intelligence per Watt* preprint (arXiv:2511.07885, 2025).

[^5]: Inference cost benchmarks from Spheron, "Token Factory on GPU Cloud: Maximize Tokens per Watt for AI Inference Revenue (2026 Guide)"; Epoch AI, "How much energy does ChatGPT use?"; SemiAnalysis InferenceX benchmarks (April 2026), reporting H100 at approximately $0.09 per million tokens for GPT-OSS-120B under vLLM and B200 at approximately $0.02 per million tokens under TensorRT-LLM. Energy estimates derived from these by dividing by representative regional commercial-electricity tariffs ($0.08–$0.15 per kWh) and adjusting for typical hyperscale PUE.

[^6]: Apple Silicon energy estimate: at 30–40 tokens per second sustained at 50 W system draw, 1,000,000 tokens requires 25,000–33,000 seconds of inference (~7–9 hours), consuming 0.35–0.46 kWh of wall-power. No PUE multiplier applies, as the laptop is on existing residential or commercial service. Throughput and power figures cross-checked against the same benchmark sources cited in note 1.
