# Chapter 1
## The Hyperscale Trap

> *It is wholly a confusion of ideas to suppose that the economical use of fuel is equivalent to a diminished consumption. The very contrary is the truth.*
>
> — William Stanley Jevons, *The Coal Question* (1865)

In 1865, a British economist named William Stanley Jevons published a book called *The Coal Question*. It made a counterintuitive argument: that the steady improvement of steam-engine efficiency, far from reducing Britain's appetite for coal, was actually accelerating it. Each new generation of engine burned coal more efficiently than the last — and Britain's total coal consumption climbed faster than ever. Efficiency was creating demand faster than it was saving fuel. The principle Jevons described is now called the *Jevons paradox*, and it is the trap inside the trap of hyperscale Synthetic Intelligence.[^1]

This chapter is about the trap. Not a metaphorical trap. A measurable, concrete, accelerating trap, with utility bills attached.

---

### The Buildout

The numbers are difficult to absorb on first reading. They get easier when you sit with them, and harder when you understand them.

In 2024, the world's data centers consumed approximately 415 terawatt-hours of electricity — about 1.5 percent of all electricity generated on the planet. That is the *current* figure, before the wave of new SI infrastructure now being commissioned reaches full operation. According to the International Energy Agency's *Energy and AI* analysis, global data center electricity consumption is projected to more than double by 2030, reaching roughly 945 TWh — close to 3 percent of total global electricity. The driver is overwhelmingly SI: power consumption in "accelerated servers" — the GPU-laden machines that train and run modern Synthetic Intelligence — is projected to grow at thirty percent per year through the rest of this decade, more than three times the rate of conventional servers.[^2]

The capital flowing into this buildout has reached a scale with no real precedent in the history of computing. The five largest hyperscalers — Amazon, Microsoft, Google, Meta, and Oracle — collectively spent approximately $443 billion on capital expenditure in 2025, a 73 percent increase over their 2024 total. For 2026, the projected figure is $602 billion, a 36 percent year-over-year increase, with each of the four largest expected to exceed $100 billion individually. Roughly three-quarters of this capital is now devoted to SI.[^3]

It is being spent — let me say this plainly — to build factories that produce sentences.

Goldman Sachs projects that hyperscaler capex from 2025 through 2027 will reach $1.15 trillion, more than double the amount spent in the preceding three years. To finance the gap between rising SI capex and internal cash flow, hyperscalers raised $108 billion in debt during 2025 alone, and industry analysts project an additional $1.5 trillion in debt issuance over the coming years.[^4]

The Stargate Project — a joint venture announced on January 21, 2025 by OpenAI, SoftBank, Oracle, and the investment firm MGX — alone proposes $500 billion of new American SI infrastructure by 2029, with ten gigawatts of dedicated power capacity. By late September 2025, the project had announced commitments approaching seven gigawatts of capacity and over $400 billion of investment, with sites spanning Texas, New Mexico, Ohio, and other states.[^5]

These are not figures from speculative pitch decks. These are commitments already underway, already breaking ground.

---

### The Grid

A buildout of this magnitude does not arrive without cost to the places that have to carry it. The clearest case study in the United States is Northern Virginia.

Loudoun County, Virginia, contains what the industry quietly calls Data Center Alley — the largest concentration of data center capacity on the planet. As of 2025, the county had 199 operating data centers and 117 more in development. Dominion Energy, the regional utility, has announced a $50.1 billion capital plan for transmission lines, substations, and generation between 2025 and 2029, in significant part to keep up with data center demand. Dominion projects that peak power demand from Virginia data centers could reach 13.3 gigawatts by 2038, nearly a fivefold increase from approximately 2.8 gigawatts in 2022.[^6]

The cost of this infrastructure does not stay inside the data center industry. Dominion has filed for a 14 percent residential rate increase for 2026, citing data center growth as a primary driver. Loudoun County residents are now in active legal opposition to the proposed Golden-to-Mars 500-kilovolt transmission line that would run through their neighborhoods to feed the next wave of facilities. The Virginia legislature has begun debating whether to create a separate utility rate class for data centers — a bureaucratic way of acknowledging what every grandmother in Loudoun already understands: that the residential ratepayer is, today, subsidizing the SI industry.[^7]

In Pennsylvania, the trajectory is starker. In September 2024, Constellation Energy announced that it would *restart* the Three Mile Island nuclear plant — closed since 2019 — under a twenty-year power purchase agreement with Microsoft, which will take all 835 megawatts of the restored unit's output for its data centers. Restart cost: $1.6 billion, with an additional $1 billion federal loan approved in 2025. The plant has been renamed the Crane Clean Energy Center, but the older name will not soon leave the public memory: Three Mile Island was the site of the worst civilian nuclear accident in American history. We are now restarting it because a single American technology company has computational requirements that cannot otherwise be met.[^8]

Across the Atlantic, the pattern repeats and intensifies. Ireland — a small country whose generous corporate tax regime made it an early data center destination — saw data center electricity consumption rise from 5 percent of national grid demand in 2015 to approximately 22 percent in 2024. Projections suggest it could pass 30 percent in the next decade. In 2021, the Irish state effectively imposed a moratorium on new grid connections for data centers; in December 2025, the moratorium was lifted only on the condition that new data centers source 80 percent of their demand from additional Irish renewables and provide dispatchable generation back to the grid in shortage events. Twenty-two percent of national electricity, in a country of five million people, is now spent on the operation of facilities largely owned by foreign corporations and used to provide services largely consumed elsewhere.[^9]

There is a phrase we should retire, and the Irish case is the place to retire it. The phrase is *the cloud*. There is no cloud. There are buildings full of machines, on land owned by someone, drawing power from a grid that someone else paid to build, in a community whose air, water, and electricity are now in part dedicated to processing the queries of strangers.

---

### The Water

The thirst of the centralized SI architecture is harder to see than its hunger for electricity, but it is no less real.

In 2023, Pengfei Li, Jianyi Yang, Mohammad Islam, and Shaolei Ren, then at the University of California, Riverside and the University of Texas at Arlington, published a paper called "Making AI Less 'Thirsty,'" the most careful public accounting we have of synthetic intelligence's water footprint. The paper estimates that training the GPT-3 model in Microsoft's American data centers directly evaporated approximately 700,000 liters of clean freshwater — approximately the water consumed in manufacturing 370 BMW automobiles. Inference is no smaller a problem. The running of trained models to answer queries happens billions of times a day across hyperscale services, and the cumulative draw is captured better at the global level than the per-query level. Ren and his colleagues project that global SI water withdrawals could reach 4.2 to 6.6 billion cubic meters per year by 2027 — between the total annual water withdrawal of Denmark and roughly half of the United Kingdom's.[^10]

This is, again, *additional* water demand, on top of every existing industrial, agricultural, and municipal call on a freshwater system that is already, in much of the world, in deficit.

The geographic distribution of this demand makes it worse. The data centers built in Arizona, Texas, Nevada, and northern Spain — chosen for their cheap land, business-friendly zoning, and proximity to high-voltage transmission — are also disproportionately located in regions of severe water stress. Cooling towers in Phoenix evaporate water that the Colorado River basin cannot easily spare. The hyperscaler water-disclosure reports, when published, are typically a year or two old and aggregate hundreds of facilities into a single global number — which means the local cost in any given watershed is consistently understated.

This is the part of the buildout that the industry would prefer the public not focus on. There is no political constituency for "data centers should be allowed to evaporate the Colorado River." So the conversation is structurally avoided.

---

### The Carbon Ledger

Energy and water are inputs. The output, in carbon terms, is the metric that has begun to embarrass even the hyperscalers themselves.

Microsoft, which has positioned itself for a decade as the most environmentally serious of the major American technology companies, published in May 2024 a sustainability report disclosing that its overall emissions across Scopes 1, 2, and 3 had risen 29.1 percent over its 2020 baseline. Direct operational emissions (Scopes 1 and 2) had actually fallen 6.3 percent. The damage was in Scope 3 — the supply-chain emissions associated with capital goods (servers, GPUs, building materials) and purchased services — which had risen 30.9 percent over the same period. The company itself attributed the increase to the construction of new data centers and the embodied carbon of the building materials and hardware required to support its investments in AI.[^11]

Microsoft is not unique. Every hyperscaler with an honest carbon disclosure has reported a similar trajectory. The sustainability targets these companies set in 2020 — net-zero by 2030, carbon-negative shortly thereafter — have been revised, deferred, or quietly reframed. The reason is not corporate hypocrisy, though there is some of that. The reason is structural. You cannot build, in five years, a generation of data centers requiring on the order of one hundred new gigawatts of dedicated capacity, and simultaneously decarbonize. The grid does not yet contain that much new clean energy, the supply chain does not produce GPUs without embodied carbon, and the timelines do not match.

This is the nature of the trap: the centralized, hyperscale path requires building so much capacity, so quickly, in so many regions, that the environmental commitments of the very companies making the investments cannot survive contact with the engineering reality. The companies' climate teams know this. The companies' investor-relations teams are beginning to acknowledge it. The companies' marketing teams are still discussing "AI for climate" without irony.

---

### The Jevons Inheritance

Here is where Jevons returns.

The standard reply, when one raises the environmental cost of hyperscale SI, is that the technology will become more efficient. This is true. Per-FLOP energy consumption is improving year over year. Per-query inference cost is falling. New chip architectures, more efficient cooling, better workload scheduling — all of these are real and ongoing advances.

And none of them save us, for the reason Jevons identified in 1865.

When the unit cost of a useful capability falls, demand for that capability rises. When inference becomes cheaper, more applications use inference. When training becomes cheaper, more models are trained. When models become more capable, more domains are addressed. The history of every transformative technology, from steam engines to internal combustion to the Internet itself, is the history of efficiency gains being eaten by demand growth — what the energy economist calls *rebound* and what every engineer in this field, in private, calls *the obvious thing*.

The IEA's projection of a doubling of data center electricity by 2030 is not despite the efficiency gains. It already incorporates them. It is the *post-efficiency* trajectory. Whatever the chips and cooling systems gain in efficiency, demand growth eats.

This is not a problem efficiency can solve. It is a problem efficiency, by itself, *creates*.

---

### Why Centralized SI Is Structurally Unsustainable

Let me state the chapter's thesis directly.

The hyperscale architecture for Synthetic Intelligence is not unsustainable because the engineers are careless or the executives are venal. It is unsustainable because *centralization itself is the problem*. To deliver synthetic intelligence as a rented service, at planetary scale, from a small number of operator-owned facilities, you must:

1. **Concentrate compute** in regions with available transmission capacity, available cooling water, available political acceptance, and available cheap land. Such regions are scarce, and they overlap badly with regions of water and grid stress.
2. **Build for peak load**, because rented services must promise capacity. The result is data centers that run, on average, well below their nameplate capacity but draw their full carbon and water cost from the moment they are commissioned.
3. **Bear the embodied carbon** of every GPU and switch and cooling system in the supply chain — much of it manufactured in regions whose own grids are dominated by coal.
4. **Charge users a margin** sufficient to amortize the capital, which in turn requires aggressive utilization, which in turn requires aggressive marketing, which in turn drives demand growth, which in turn re-triggers the cycle.

Every one of these features is intrinsic to the architectural choice of *centralized, rented, large-batch synthetic intelligence delivered from operator-owned data centers.* Change any one of them, and the unit economics fail. Refuse to make the choice, and the curve bends.

The Webspinner Foundation argues, and this book will argue, that the curve must bend.

There is an alternative. It was sketched in the Foreword. It is the subject of every chapter that follows. But before we describe what to build instead, we must finish describing the trap that has been built — because the second-largest barrier to escaping it, after the financial incentives of those inside it, is the conviction (repeated daily by parties who profit from the conviction) that there is no alternative.

There is.

---

## Endnotes

[^1]: William Stanley Jevons, *The Coal Question: An Enquiry Concerning the Progress of the Nation, and the Probable Exhaustion of Our Coal-Mines* (London: Macmillan, 1865), Chapter VII, "Of the Economy of Fuel." The "Jevons paradox" was named in modern economics literature in the late twentieth century; the underlying argument is Jevons's. Full text via the Library of Economics and Liberty.

[^2]: International Energy Agency, *Energy and AI* (Paris: IEA, 2025), and IEA, *Electricity 2024: Analysis and Forecast to 2026* (Paris: IEA, 2024).

[^3]: CreditSights, *Technology: Hyperscaler Capex 2026 Estimates* (December 2025); MUFG Americas, *AI Chart Weekly: Financing the AI Supercycle* (December 19, 2025); Dell'Oro Group, "Hyperscaler AI Deployments Lift Data Center Capex to Record Highs in 2Q 2025" (2025).

[^4]: Goldman Sachs Research, "Why AI Companies May Invest More than $500 Billion in 2026" (2025); CreditSights and MUFG analyses cited in note 3.

[^5]: OpenAI, "Announcing The Stargate Project" (January 21, 2025); OpenAI, "OpenAI, Oracle, and SoftBank expand Stargate with five new AI data center sites" (September 24, 2025); CNBC, "OpenAI's first data center in $500 billion Stargate project is open in Texas, with sites coming in New Mexico and Ohio" (September 23, 2025).

[^6]: Dominion Energy, *2025–2029 Capital Plan* (filings with the Virginia State Corporation Commission, 2024–2025); Loudoun County, Virginia, *Data Center Capital of the World: A Strategy for a Changing Paradigm* (2025); Virginia Mercury, "Loudoun residents take fight against high-voltage power lines for Data Center Alley to SCC" (December 16, 2025).

[^7]: Virginia Mercury, "Loudoun County neighbors fight proposed Dominion transmission lines for Data Center Alley" (August 14, 2025); VPM News, "In the world's data center hotbed, how close is too close, and who should pay?" (May 7, 2025); Data Center Dynamics, "Dominion Energy admits it can't meet data center power demands in Virginia."

[^8]: Constellation Energy, "Constellation to Launch Crane Clean Energy Center" (September 20, 2024); NPR, "Three Mile Island nuclear plant will reopen to power Microsoft data centers" (September 20, 2024); CNBC, "Trump administration backs Three Mile Island nuclear restart with $1 billion loan to Constellation" (November 18, 2025); Data Center Dynamics, "Three Mile Island nuclear power plant to return as Microsoft signs 20-year, 835MW AI data center PPA."

[^9]: Bloomberg, "Ireland Ends Moratorium on New Power Links to Data Centers" (December 12, 2025); Commission for Regulation of Utilities (Ireland), *Large Energy User Connection Policy Decision Paper*, CRU2025236 (December 2025); IIEA, *Data Centres in Ireland: The State of Play* (2024).

[^10]: Pengfei Li, Jianyi Yang, Mohammad A. Islam, and Shaolei Ren, "Making AI Less 'Thirsty': Uncovering and Addressing the Secret Water Footprint of AI Models," arXiv:2304.03271 (April 2023, revised); published version in *Communications of the ACM* (2025); UC Riverside News, "AI programs consume large volumes of scarce water" (April 28, 2023).

[^11]: Microsoft, *2024 Environmental Sustainability Report* (May 2024). The figures cited — 29.1 percent overall increase, 6.3 percent decrease in Scope 1+2, 30.9 percent increase in Scope 3, all relative to the FY2020 baseline — are from Microsoft's own report covering FY2023, as summarized on the company's official issues blog (https://blogs.microsoft.com/on-the-issues/2024/05/15/microsoft-environmental-sustainability-report-2024/). Note: a 23.4 percent figure circulates in popular coverage; this appears to come from a later reporting cycle and should not be conflated with the FY2023-vs-FY2020 figures used here. See also Microsoft, *2025 Environmental Sustainability Report* (May 2025); Data Center Dynamics, "Microsoft emissions up 23% since 2020, company blames AI data centers."
