# Chapter 2
## The Concentration Problem

> *Freedom of the press is guaranteed only to those who own one.*
>
> — A. J. Liebling, *The New Yorker*, May 14, 1960

In the spring of 1960, the journalist A. J. Liebling sat through several days of a publishers' convention, watching newspaper owners congratulate themselves on the vigor of their industry. He was unimpressed. The newspaper owners were a small and shrinking group, increasingly indistinguishable from the political and commercial interests they purported to cover, and Liebling — who had spent thirty years inside the trade — knew exactly what their consolidation meant for the rest of us. In a parenthetical aside that has long outlived its surrounding article, he summarized the situation in eleven words. *Freedom of the press is guaranteed only to those who own one.*[^1]

What Liebling saw in 1960 about the newspaper press, this chapter will argue is now true about the synthetic press — about the machines that increasingly mediate, generate, and curate the words ordinary people read, write, and reason with. To paraphrase him for the present moment: *the freedom to think with synthetic intelligence is guaranteed only to those who own one.*

Today, almost no one does.

---

### The Economics of Frontier Model Training

To understand the concentration problem, you first have to understand what it costs to train a frontier model.

A "frontier" model, in the loose industry usage of 2025, is one of the small handful of synthetic intelligences operating at or near the leading edge of capability — the GPT-4-class, Claude-3-class, Gemini-Ultra-class systems that the major labs introduce, replace, and quietly retire on a roughly annual cadence. Estimates of the actual training cost of these models vary widely, in part because the labs disclose very little, and in part because the question of what to count is genuinely hard. Do you count only the compute cycles consumed during the final training run? The development cycles preceding it? The salaries of the researchers? The amortized cost of the GPU cluster itself? Different conventions yield different numbers.

Even the conservative numbers are staggering. The most thorough academic accounting available, by Ben Cottier, Robi Rahman, and colleagues at Epoch AI, places the largest publicly identified training runs to date in the tens to low hundreds of millions of dollars in compute costs alone — with broader estimates that include hardware amortization, staff, and energy reaching well into the hundreds of millions for a single model. Their longitudinal analysis finds that the cost of the most compute-intensive training runs has grown by roughly 2.4x per year, every year, since 2016 — a doubling time of approximately ten months.[^2]

Where does this trajectory lead? It is not necessary to speculate. The CEO of Anthropic, Dario Amodei — one of the small number of people on the planet making these decisions in 2025 — has said publicly that frontier developers are likely to spend close to *one billion dollars* on a single training run in the near term, with multiple ten-billion-dollar runs anticipated within roughly two years. That is not the all-in cost of a lab. That is the cost of a single training of a single model.[^3]

If the curve extends, the cost of training the leading model will exceed a billion dollars by 2027 and ten billion by the late 2020s. By the middle of the next decade — within the working life of a young engineer reading this paragraph — only entities with the financial profile of a mid-sized nation will be able to train at the frontier.[^4]

This is not what the personal computer revolution looked like. This is what the *mainframe* era looked like, only larger.

---

### Who Can Afford to Build SI Today

If a frontier model costs hundreds of millions of dollars to train today and is on track to cost ten billion within a few years, the question of *who* can afford to build SI is no longer rhetorical. It has a very short answer.

In 2024, by Stanford's count, nearly ninety percent of the notable new AI models in the world were produced by industry, up from sixty percent in 2023. Academia, which had been the principal source of novel architectures for the better part of three decades, had been priced out within a single year. The same Stanford analysis finds that the training compute used for top models doubles every five months, training data every eight months, and power consumption annually. No university in the world is in a position to keep up with that pace. Hardly any government is, either.[^5]

In practice, the entities that *are* in a position to keep up form a list short enough to fit on a coaster:

- **The American hyperscalers** — Microsoft, Google, Amazon, and Meta — directly, or through equity-and-credits partnerships with affiliated labs.
- **OpenAI**, financed primarily by Microsoft and an expanding consortium of cloud and chip partners.
- **Anthropic**, financed primarily by Amazon and Google.
- **xAI**, financed primarily by Elon Musk's other companies and a recent capital round of comparable scale.
- **The major Chinese platforms** — Alibaba, Tencent, Baidu, ByteDance, and a small number of state-affiliated labs.
- **A handful of well-funded national or quasi-national efforts** in France, the UAE, the United Kingdom, and India.

That is the list. Roughly a dozen organizations, in three or four jurisdictions, with the capital and the compute to operate at the frontier of a technology we are repeatedly told will reshape every aspect of human life.

It is an instructive exercise to ask the same question about any other generationally significant technology in modern memory and observe how the lists compare. The number of entities in the world capable of producing a competitive automobile in 2025 is in the hundreds. The number capable of producing a competitive smartphone is in the dozens. The number capable of producing a competitive operating system is in the high single digits. The number capable of producing a competitive frontier synthetic intelligence is *smaller than the number of countries in the European Union.*

This is not a market. This is something else.

---

### The Capital Moat and Its Consequences

The standard reply, when one observes this concentration, is that *of course* synthetic intelligence is expensive to build today, and *of course* very few entities can afford to build it, but *the cost will come down* and *the field will democratize itself in due course.*

There are reasons to doubt this reply. The principal one is that the actors at the top of the present concentration are not waiting for the field to democratize. They are actively building what economists call a *capital moat* — a set of structural advantages, accumulating year over year, that make it progressively harder for new entrants to compete on the dimensions that matter.

The capital moat in synthetic intelligence has at least four layers, each of which has thickened materially in the last two years:

1. **Compute access.** Frontier training requires tens of thousands of high-end accelerators wired together with specialized interconnect, in a single coherent cluster, drawing tens of megawatts of power. The supply of such hardware is constrained at every level — by the foundry that fabricates the chips (TSMC, primarily), by the small number of designs that meet the requirement (NVIDIA's, principally), and by the small number of operators with the data centers to host them. New entrants cannot simply *buy* this capacity. Existing players, with multi-year purchase commitments, allocate it.

2. **Talent.** The number of researchers in the world capable of leading a frontier training run is, by best industry estimates, in the low thousands. The major labs have spent the last five years systematically acquiring this population at compensation levels — multi-million-dollar packages for senior researchers, with the most sought-after individuals reportedly receiving substantially more — that effectively close the position to non-incumbents. A university that wishes to train its own students for this work must do so in the knowledge that the most capable will be hired into the incumbents within months of graduation.

3. **Data.** Frontier training requires not only more data than any prior class of model, but also data of progressively higher quality, increasingly curated to the model's intended capabilities. Incumbents have spent the last three years buying or licensing exclusive access to large portions of the world's news archives, code repositories, scientific publications, and proprietary corpora. The data freely scraped from the open web in 2020 is no longer sufficient — and it is, in many cases, no longer freely scrapeable.

4. **Distribution.** The path from a trained model to a paying customer runs primarily through a small number of cloud platforms and operating systems. Microsoft's Azure-OpenAI integration, Amazon's Bedrock-Anthropic integration, and Google's Vertex-Gemini integration are not neutral marketplaces; they are vertically aligned distribution channels in which the cloud provider's preferred model is the default, the only first-class citizen, and frequently the only option that an enterprise procurement department will actually approve.

The Federal Trade Commission, in a Section 6(b) staff report issued in January 2025 after a year-long study, identified each of these layers and concluded that the partnerships among the cloud-service providers and the leading model labs gave the cloud providers the ability "to create lock-in, deprive start-ups of key AI inputs, and reveal sensitive information that can undermine fair competition." The cumulative financial investment in the partnerships studied — Microsoft–OpenAI, Amazon–Anthropic, and Google–Anthropic — exceeded twenty billion dollars at the time of the report, before the full Stargate commitments and subsequent capital flows.[^6]

Senators Elizabeth Warren and Ron Wyden, in a parallel inquiry, made the antitrust framing explicit: the same handful of cloud platforms that dominated the previous decade of Internet infrastructure are now positioned to dominate the synthetic intelligence layer above it, with the practical consequence of foreclosing competition before it can begin.[^7]

Whether the present American political system will act on these findings is a separate question. The structural diagnosis is not in serious dispute.

---

### Power Flowing to the Few

Concentrations of capability create concentrations of power. This is a sociological observation, not a moral one.

When a small number of entities control the generation of a transformative technology, they accumulate, over time, several distinct forms of leverage that have nothing directly to do with the technology itself. They become the principal employers of the talent associated with the field, which gives them an outsized voice in what gets researched. They become the principal funders of academic work in the field, which gives them an outsized voice in what gets published. They become the principal sources of revenue for journalists, regulators, conferences, and trade associations covering the field, which gives them an outsized voice in what gets covered, what gets regulated, and what gets discussed at all. They become the principal lobbying interests on legislation that affects the field, which gives them an outsized voice in what becomes law.

None of these dynamics is unique to synthetic intelligence. All of them have been observed, repeatedly, in industries from petroleum to telecommunications to pharmaceuticals. What is unique to synthetic intelligence is the scope of what the technology *does*. A petroleum concentration determines who profits from gasoline. A telecommunications concentration determines who profits from telephony. A synthetic intelligence concentration determines, increasingly, who profits from cognition itself — from the production, summarization, retrieval, and curation of the words and reasoning by which most people, for most of their working lives, think.

This is the part of the problem that I find hardest to write about, because it is the part most easily dismissed as alarmist. I am going to write it anyway. *To control synthetic intelligence at the level the present concentration controls it is to be in a position to shape, at scale, what people read, what people are told, what people are informed, and — over time — what people believe.* The major labs do not yet exercise this power overtly. There are reasons to think most of them have no current intention of exercising it overtly. But the power exists, and concentrations of power, in the historical record, are not customarily left unexercised.

This is not a forecast about the people currently running these companies. It is a forecast about the structural position they occupy. The structural position is the problem.

---

### The Historical Pattern: Every Centralization Eventually Breaks

There is a consoling thought worth holding briefly, because it is partly true.

Every previous concentration of comparable scope has, eventually, broken. Standard Oil concentrated American petroleum refining to such a degree that the Supreme Court ordered it dissolved in 1911. AT&T concentrated American telecommunications to such a degree that it was broken into Regional Bell Operating Companies in 1984. IBM concentrated mainframe computing to such a degree that the Department of Justice pursued it for thirteen years, from 1969 until 1982 — after which the rise of the personal computer rendered the concentration largely moot, with little further legal help required. Microsoft concentrated personal-computer operating systems to such a degree that it lost a major antitrust case in 2001 and entered into a consent decree that constrained its conduct for years afterward.

In each case, the concentration ended. In each case, what came next was, by most measures, broader, more competitive, and more useful to ordinary people than what preceded.

The consoling thought is that the same will happen to the present concentration. There is some truth in this. Concentrations are unstable. They are also, when their structural advantages are large enough, *very durable* before they break. AT&T's American telephone monopoly lasted almost seventy years. Standard Oil's controlling position in American refining lasted about three decades. Microsoft's desktop operating-system dominance has, in functional terms, lasted into its fifth decade. *On the timescale at which concentrations break, several human generations live and die under their terms.*

The reader who hopes that the synthetic intelligence concentration will simply democratize itself, the way personal computing did, is hoping for a particular historical pattern to repeat. I share the hope. I do not believe we should rely on it.

The personal computer did not democratize itself. It was democratized — actively, deliberately, against the wishes of the priesthood that profited from the prior arrangement, by builders who refused to accept the prior arrangement as legitimate. The hobbyists won not because the technology decided, on its own, to leave the glass-walled rooms. They won because they walked into the glass-walled rooms, took what they needed, and built something else.

That is the pattern this book proposes to repeat.

---

### What This Means

The Hyperscale Trap (Chapter 1) was an environmental and economic critique. The Concentration Problem is a political one. Both are downstream of the same architectural choice — the choice to deliver synthetic intelligence as a rented service, from a small number of operator-owned facilities, financed by a small number of capital pools, accountable to a small number of shareholders.

Change the architectural choice, and both problems weaken at once.

The chapters that follow describe what the alternative architecture is, what it costs, what it can and cannot do, and how to begin building it now — not after the next antitrust case, not after the next election, not after the next round of policy. *Now.* While the window is open. While the curve can still bend.

The window will not stay open indefinitely. Liebling's parenthetical — that freedom of the press is guaranteed only to those who own one — was, when he wrote it, already a description of an arrangement that had taken almost a century to consolidate, and that would in the decades to follow prove very difficult to reverse. We are at the equivalent of about 1880 in the synthetic press. The consolidation is well underway. It is not yet complete.

That fact is the entire reason this book exists.

---

## Endnotes

[^1]: A. J. Liebling, "The Wayward Press: Do You Belong in Journalism?" *The New Yorker*, May 14, 1960, pages 105–109. The quotation is a parenthetical aside in a longer piece reporting on a publishers' convention. See also the Quote Investigator account of the line's provenance, which traces thematically similar formulations earlier but credits Liebling with the canonical version: https://quoteinvestigator.com/2015/05/21/free-press/.

[^2]: Ben Cottier, Robi Rahman, et al., "The Rising Costs of Training Frontier AI Models," arXiv:2405.21015 (May 2024, revised). The 2.4x-per-year cost growth figure (90% confidence interval 2.0x to 2.9x) and the methodology for distinguishing compute-only cost from broader development cost are both from this paper. Epoch AI maintains an updated dataset of frontier-training estimates: https://epochai.org.

[^3]: Dario Amodei, public remarks on the trajectory of frontier training costs (multiple venues, 2024–2025), as summarized in *Fortune*, "Why the cost of training AI could soon become too much to bear" (April 4, 2024) and subsequent industry coverage. Amodei has stated that frontier training runs are likely to approach $1 billion in the near term and that multiple $10 billion training runs are anticipated within roughly two years.

[^4]: Cottier, Rahman, et al. (cited in note 2), with extrapolation; *Fortune* coverage cited in note 3; PYMNTS, "AI Cheat Sheet: Large Language Foundation Model Training Costs" (2025).

[^5]: Stanford Institute for Human-Centered AI (HAI), *Artificial Intelligence Index Report 2025* (Stanford University, 2025). https://hai.stanford.edu/ai-index/2025-ai-index-report. The figures cited — industry's roughly 90 percent share of notable models in 2024 (versus 60 percent in 2023), the 5-month doubling of training compute, the 8-month doubling of dataset size, and the annual doubling of training power consumption — are drawn from the report's Research and Development and Technical Performance sections.

[^6]: U.S. Federal Trade Commission, *Partnerships Between Cloud Service Providers and AI Developers: FTC Staff Report on AI Partnerships and Investments Section 6(b) Study* (January 2025). https://www.ftc.gov/system/files/ftc_gov/pdf/p246201_aipartnerships6breport_redacted.pdf. FTC press release, "FTC Issues Staff Report on AI Partnerships & Investments Study" (January 2025). https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-issues-staff-report-ai-partnerships-investments-study. Quoted language is from the Commission Chair's accompanying statement on the report.

[^7]: Office of Senator Elizabeth Warren, "Warren, Wyden Launch Investigation into Google, Microsoft Partnerships with AI Developers Anthropic, OpenAI" (2024). https://www.warren.senate.gov/news/press-releases/warren-wyden-launch-investigation-into-google-microsoft-partnerships-with-ai-developers-anthropic-openai
