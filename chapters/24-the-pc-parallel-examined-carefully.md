# Chapter 24
## The PC Parallel, Examined Carefully

> *Those who cannot remember the past are condemned to repeat it.*
>
> — George Santayana, *The Life of Reason*, Volume I: *Reason in Common Sense* (1905)

In 1905, the philosopher George Santayana published the first volume of his five-volume *The Life of Reason*, in which he made the observation that has, in the century since, become one of the most-quoted sentences in English-language thought. *Those who cannot remember the past are condemned to repeat it.* Santayana's point was specific: that civilizations which fail to absorb the practical lessons of their predecessors are doomed to discover those lessons again, the hard way, in their own time and at their own cost.[^1]

Chapter 4 of this book made the case that the present synthetic-intelligence moment resembles the period from roughly 1973 to 1977 — the years between when personal computing first became technically possible and when the Homebrew Computer Club, the early kit computers, and the broader hobbyist movement made the PC's democratization culturally inevitable. This chapter returns to the comparison with more care, because the comparison is doing real work in the argument of the book and needs to survive the attention it has been drawing.

I will examine, in turn, what the PC actually accomplished against the mainframe priesthood; what the catalysts of that transition were; what is genuinely parallel about the present moment and what is not; and what lessons the PC era's incomplete victories offer for the work of synthetic-intelligence democratization. The conclusion is mixed. The parallels are real and useful; the disanalogies are also real and instructive. *We are not living through 1977 again.* We are living through a moment with structural similarities to 1977 that, taken seriously, do meaningful work in shaping what we should build.

---

### What the PC Actually Accomplished

The standard popular history of the personal-computer revolution presents it as a story of liberation: ordinary people gained access to computing power that had previously been confined to institutions, and the world was transformed. This is not wrong. It is also, when examined carefully, incomplete.

What the PC actually accomplished, in the period from roughly 1975 to 1995, was the following:

**It moved the production of computation from institutional spaces to personal spaces.** A user could, by 1985, do on a desk what had previously required a glass-walled room. The hardware was theirs. The software was theirs. The data was theirs. The right to compute was no longer something granted by an institution; it was something the user exercised on their own behalf.

**It moved the gatekeeping of access from operators to markets.** A user no longer had to wait for an operator to grant computing access; they had only to purchase a machine. Markets are not the same thing as democracy, but the shift from operator-gatekeeping to market-gatekeeping was a meaningful expansion of access for many populations who had previously been excluded.

**It enabled a generation of new applications and new businesses that could not have existed under mainframe economics.** Word processing, spreadsheets, desktop publishing, small-business accounting, home databases, hobbyist programming, the early bulletin-board services, the entire ecosystem of shareware and freeware — these arose because the cost of access had fallen by orders of magnitude.

**It produced a generation of builders.** The hobbyists, students, small-business owners, and engineers who came up using personal computers did not, in general, return to the mainframe assumption that computing was an institutional good. They built their own things. They expected access. They taught their children to expect access.

These were not small accomplishments. They were the foundations of the second half of the twentieth century's computing era and of the Internet that followed.

---

### What the PC Did Not Accomplish

It is also worth naming what the PC did not accomplish, because the disanalogies matter.

**It did not eliminate institutional concentration.** The mainframe priesthood was outflanked, but it was replaced, over the next twenty years, by a different priesthood — the platform priesthood of the Internet's largest operators. Microsoft's operating-system monopoly, Apple's app-store control, Google's search dominance, Facebook's social-graph leverage, Amazon's e-commerce position, and the broader pattern of platform centralization were the *next* concentration, arising on top of the personal computer's distributed substrate. The PC made the platforms possible; the platforms then re-aggregated the power the PC had distributed.

**It did not eliminate inequality of access.** The personal computer was, throughout its first two decades, a technology of the relatively wealthy. The libraries, schools, and community programs that brought PC access to broader populations did meaningful work, but the PC did not arrive simultaneously in every community, and the gaps it produced (the "digital divide" of the 1990s and early 2000s) compounded into inequalities of opportunity that persist.

**It did not democratize the production of computing infrastructure.** The end users gained the means to compute; the people who *built* the means to compute remained a relatively small population, working for a small number of large firms. The chips, the operating systems, the major application platforms continued to be the work of a few large institutions, even as the user population grew to billions.

**It did not preserve the distributed substrate it created.** The Internet, beginning as a genuinely decentralized system on top of personal computers, was over the following decades increasingly mediated by centralized platforms — to the point that, by the 2010s, the average user's access to the Internet was, in practical terms, mediated by perhaps half a dozen platforms whose policies shaped what the user could see and do.

These limitations are not failures of the PC revolution; they are the bounds of what a single architectural choice can accomplish. *No one architectural shift produces final liberation.* The PC accomplished what it accomplished and bequeathed the next generation a more democratized substrate — on top of which the platforms then built their next layer of concentration.

This is the historical pattern. We should expect Warp's accomplishments to be similarly bounded.

---

### The Catalysts of the PC Transition

What actually catalyzed the PC's emergence from hobbyist curiosity to mainstream tool? Five forces were operative, and the same five forces are at work now.

**The cost curve of the underlying technology.** Moore's Law in the 1970s, the falling cost of memory, the integration of CPU functions onto single silicon dies — these brought the cost of useful computation down to the level where individuals could afford it. Without the underlying cost reduction, no architectural choice would have democratized computing; the technology had to be cheap enough.

**A pre-existing community of builders.** The Homebrew Computer Club did not emerge from nowhere. It emerged from a community of electronics hobbyists, ham radio operators, model railroaders, and amateur engineers who had been building electronic things for decades. The community had skills, social patterns, and shared expectations about what builders did with new technology.

**A clear ideological alternative to the institutional default.** Ted Nelson's *Computer Lib* (1974), Lee Felsenstein's writings on community memory, the broader counterculture's distrust of institutional authority, and the early free-software movement's commitments all provided an *intellectual frame* in which personal computing was the right thing to do, not just the new thing to do. Without the ideological frame, the PC era might have produced cheaper mainframes.

**Cheap distribution channels.** Computer hobbyist magazines, mail-order catalogs, the *Whole Earth Catalog*, early computer stores, and (later) the network of small dealers and value-added resellers gave the PC ecosystem the distribution it needed. The mainframe priesthood had its own distribution (institutional sales forces); the PC needed a different one and built it.

**A founding generation that refused the alternative.** Steve Wozniak refused to keep the Apple I designs proprietary. Bill Gates and Paul Allen built MS-DOS for the IBM PC on terms that allowed the operating system to escape IBM's control. The early Linux developers, Apache developers, and the broader free-software community produced infrastructure that no proprietary actor could withhold. The founders of the PC era *chose*, repeatedly, the more distributed option when the more centralized option was available.

These five forces operated together. No one of them was sufficient. Together, they produced a transition whose pace and reach surprised most contemporaries and that, in retrospect, looks inevitable only because we know how it ended.

---

### Parallels at Present

Each of the five forces operating in the PC era has, now, a structural parallel in synthetic intelligence.

**The cost curve.** The hardware cost of running useful synthetic-intelligence inference has fallen by orders of magnitude in the last five years. Apple Silicon, NVIDIA's consumer-grade GPUs, and the broader trend toward AI accelerators in PC and mobile platforms have brought the cost of capable inference into reach for ordinary users. The trajectory is continuing.

**A pre-existing community of builders.** The open-source software community, the hobbyist machine-learning community, the local-LLM enthusiasts running models on Mac Studios and dedicated PCs, the academic researchers working on smaller models, and the broader engineering community frustrated with platform constraints — these populations exist, are growing, and have skills, social patterns, and shared expectations comparable to the Homebrew era's community.

**A clear ideological alternative.** The free-software movement, the privacy-rights community, the cypherpunk tradition Chapter 7's epigraph drew on, the contemporary platform-skepticism literature, and the broader cultural exhaustion with extractive consumer technology all provide an intellectual frame in which user-owned synthetic intelligence is the right thing to do. The frame exists. It is, at present, less consolidated than the equivalent frame in 1975 was — but it is real and growing.

**Distribution channels.** GitHub, Hugging Face, the open-source release patterns of the major model providers, the proliferation of local-AI tooling on technical blogs and developer YouTube, and the broader infrastructure of open-source distribution provide what the PC ecosystem needed and now serves as the substrate for community-driven adoption.

**A founding generation that refuses.** The Foundation is one. There are others — Mozilla, the Free Software Foundation, the Internet Archive, the various community-broadband projects, and the steadily growing cohort of small businesses and community organizations that have rejected platform dependence in favor of self-hosted alternatives. The cohort exists. The cohort is growing. The cohort has not yet produced an architecture for synthetic intelligence at the scale the PC era produced for general-purpose computing — *which is what this book is for*.

The five forces are operative. The alignment is not as complete as it was in 1975, but the alignment is real, and the trajectory of the underlying technology and culture is in the direction the alignment requires.

---

### What Is Different This Time

It would be dishonest to leave the comparison without acknowledging the disanalogies. There are at least four.

**The capital intensity is genuinely different.** A 1976 personal computer cost a few thousand dollars, in 1976 dollars; the Apple I sold for $666.66. A 2026 frontier-model training run costs hundreds of millions to billions of dollars. The user does not need to fund frontier training to participate in synthetic intelligence — that is the whole point of the BYOK pattern — but the *capability frontier itself* requires capital that no individual hobbyist can match. This is materially different from the PC era, in which a sufficiently determined hobbyist could approach the state of the art on their own.

**The training-data dependency is genuinely different.** The PC ran software that any sufficiently skilled programmer could write. A synthetic-intelligence system runs models trained on corpora that no individual can assemble — and the open-weight ecosystem's continued availability depends on the major labs' continued willingness to release weights. The current moment includes a small number of deliberate open-weight commitments from major actors (Meta most prominently); the long-term trajectory of open-weight releases is, as of 2026, an active area of policy and commercial uncertainty.

**The state-actor interest is genuinely different.** The PC era largely escaped serious state attention until it was already entrenched. Synthetic intelligence has, from its inception as a public technology, been a subject of intense state attention — for national-security reasons, for economic-competitiveness reasons, for surveillance reasons, and for regulatory reasons. State-level interventions to consolidate or restrict synthetic intelligence are likely throughout the period in which Warp is being adopted. This was not a comparable factor in the PC era.

**The user-experience expectation is genuinely different.** The 1976 user was excited to type at a CP/M prompt for the privilege of using a computer. The 2026 user expects, reasonably, the polished, integrated, mobile, low-friction experience that platforms have spent twenty years cultivating. Warp must not only deliver on its architectural commitments but do so with a user experience that does not feel like a regression from the platforms' offerings. This is a substantial engineering and design challenge that the PC era's analog did not face.

These differences mean that the PC parallel is *useful but not exact*. The strategy that worked in 1977 is not literally the strategy that will work now. The lesson is that *the same forces are operative but in altered form*, and the work of democratizing synthetic intelligence will require strategy adapted to its particular conditions.

---

### What Is Substantively the Same

That said, three things are substantively the same.

**The technology is at an inflection point.** What was technically impossible at the user-level five years ago is technically practical now; what is impractical now will be routine in five years. The inflection-point dynamic of 1973–1977 is operative now in synthetic intelligence.

**The institutional priesthood is identifiable, and its structural interests are diagnosable.** The hyperscale operators, like the mainframe vendors of 1975, are pursuing the strategies that follow from their architectural position. They are predictable. The work of routing around them is the same kind of work the Homebrew Computer Club did against IBM, even though the specific tactics differ.

**The decision is whether the next generation accepts the institutional default.** As in 1975, the question is whether a sufficient community of builders refuses the customary arrangement and builds the next one. The community exists. The architecture is described. The question is whether the work is done.

---

### What the Lesson Says

I have said elsewhere in this book that I lived through the PC revolution. I did. I helped found a PC company in 1986; I built the architecture and the business that the personal-computer market enabled. The lesson I take from the PC era is not that the personal computer's transition was easy or that it would have happened without deliberate effort. *The lesson is that the transition required builders who refused, and that the builders' refusal was, in the end, sufficient against an institutional default that had every appearance of being permanent.*

The institutional defaults in 2026 also have every appearance of being permanent. They are not. They are subject to the same forces that ended the mainframe era and, before that, the proprietary-computer era of the 1950s. The technology is at an inflection point. The community of builders is in place. The ideological alternative is articulated. The distribution channels exist. *What is missing is the architecture and the founding generation's refusal.*

The architecture is described in this book. The refusal is the reader's to participate in.

The next chapter describes the role of the Webspinner Foundation in this work — what we are trying to do, what we are not trying to do, and why a small organization can, at this particular moment, play the role this moment requires.

---

## Endnotes

[^1]: George Santayana, *The Life of Reason: Or, the Phases of Human Progress*, Volume I: *Reason in Common Sense* (Charles Scribner's Sons, 1905). The "those who cannot remember the past" passage appears in Chapter XII ("Flux and Constancy in Human Nature"). Available via Project Gutenberg: https://www.gutenberg.org/files/15000/15000-h/15000-h.htm. Santayana's broader corpus on philosophy, aesthetics, and ethics — *The Sense of Beauty* (1896), *Scepticism and Animal Faith* (1923), and the *Realms of Being* tetralogy (1927–1940) — extends his thought across multiple domains; the *Life of Reason* volumes remain the most-cited single work.
