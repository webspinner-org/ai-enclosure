# Chapter 4
## The Lessons of Computing History

> *Information wants to be free, because the cost of getting it out is getting lower and lower all the time. Information wants to be expensive, because it's so valuable. The right information in the right place just changes your life. So you have these two fighting against each other.*
>
> — Stewart Brand, in conversation with Steve Wozniak, Hackers Conference, 1984

In November 1984, in a cluster of cabins on the California coast at Fort Cronkhite, about 150 of the people who had built the personal computer convened the first Hackers Conference. Steve Wozniak was there. Lee Felsenstein was there. *Whole Earth Catalog* veterans of the previous decade were there, and a young documentary observer named Steven Levy who would write a book that took its title from the gathering. At one point during the proceedings, the writer and futurist Stewart Brand made a remark to Wozniak that Levy paraphrased into seven words: *Information wants to be free.*

What Brand actually said was longer and more honest. He said information wanted to be free *and* it wanted to be expensive. The first because the cost of distribution was collapsing. The second because the right information in the right place changed lives. Brand was naming a tension, not asserting a slogan. The tension is the one this book is also about.[^1]

That gathering at Fort Cronkhite in 1984 took place at a particular moment in computing history. It is worth understanding that moment, because the moment we are now in resembles it more than any commentator I trust seems to admit.

---

### The Mainframe Era and Its Priesthood

For roughly thirty years, from the late 1950s through the late 1970s, the dominant fact about computing was that the computer was big, expensive, scarce, centrally administered, and accessed at the discretion of an institution.

The institution might be a university, a government laboratory, a Fortune 500 company, a hospital, or a bank. The computer lived in a glass-walled room — what the mainframe community called the "computer room," or, more elaborately, the "data processing center" — climate-controlled, raised-floor, white-tile, attended by professionals in white coats whose job was as much priestly as technical. Users — the people who wanted to compute something — did not enter the room. They submitted jobs on punch cards or, in the era of timesharing, sat at terminals connected to the mainframe over short cables or leased lines. They received output on paper or on a screen they did not own, processed by a machine they did not own, governed by an operating system whose source code they were not permitted to see, on a schedule administered by people whose priorities were not theirs.

This is the world I came up in. I worked the night shift on a Burroughs B-1900 at Cook Children's Hospital in Fort Worth in 1982, at the age of twenty. The image I retain most clearly from those years is not of any particular computation but of the line of nurses, doctors, accountants, and administrators outside the door of the computer room, waiting for a printout, waiting for a batch run to finish, waiting for permission to compute. The mainframe priesthood I belonged to in those years did not see itself as a priesthood. It saw itself as competent professionals doing demanding technical work. It was both. The priesthood and the competence were not opposed.

The economic logic of the mainframe era was straightforward. The hardware was expensive enough that no individual could own it. The expertise to operate it was specialized enough that no individual could replace its operators. The software was complex enough that no individual could write it. *Therefore the computer was institutional, and the right to compute was something institutions granted.* Every premise in that argument was true at the time. The premises would not remain true.

IBM was the dominant institution within this institutional logic. By the late 1960s, IBM held a substantial majority of the world's general-purpose computer market, and the United States Department of Justice had filed an antitrust suit alleging illegal monopolization. The suit, filed in January 1969, would consume thirteen years of litigation, generate testimony from more than nine hundred and fifty witnesses, and ultimately be withdrawn in January 1982 by Assistant Attorney General William Baxter on the grounds that it was "without merit." The withdrawal came at almost the exact moment that the personal computer was, on its own, making the question moot.[^2]

The mainframe priesthood was not broken by the Justice Department. It was made irrelevant by a development none of the litigators had anticipated.

---

### The PC Revolution and What It Democratized

Seven years before the antitrust case was withdrawn, on March 5, 1975, in the rain, in the double-wide garage of a man named Gordon French in Menlo Park, California, thirty people held the first meeting of what would come to be called the Homebrew Computer Club. Lee Felsenstein moderated subsequent meetings. The club had no dues, no commercial activity, and a stated mission of helping ordinary people own and operate computers.[^3]

Two of the attendees, a few meetings in, were a young Steve Wozniak and a younger Steve Jobs. Wozniak demonstrated, in those meetings, the design that would become the Apple I. He distributed the schematics, in keeping with the Homebrew norm of shared design. The norm of shared design, as it turned out, was the difference. The Homebrew Computer Club was not a venue for promoting a product. It was a venue in which the assumption of institutional ownership of computing was being collectively, deliberately, and joyfully refused.

The decade that followed dissolved the mainframe priesthood. The Apple II (1977), the IBM PC (1981), the Apple Macintosh (1984), Microsoft Windows (1985), and the long tail of cloning, kit-building, and software entrepreneurship that surrounded them moved computation out of the glass-walled room and onto the desks of ordinary people. By the time the Justice Department concluded that its case against IBM was "without merit," the case had also become *moot*. IBM still made mainframes. IBM still made money on mainframes. But the question of who controlled computation had been answered by the market — and the market had answered, *not IBM*.

What did the PC revolution democratize, exactly?

It democratized:

- **Ownership of the hardware.** The user owned the computer outright. It was not rented, leased, time-shared, or borrowed. The user could resell it, modify it, take it apart, refuse to upgrade it, and pass it down to children.
- **Control of the software.** The user chose what to run. The user could install software written by strangers, by friends, by hobbyists, or by themselves. The user could modify software, in the limit. There was no central authority dictating what the computer was permitted to do.
- **The right to compute privately.** What the user did on the machine was, by default, the user's business. Files lived on the user's disk. Documents stayed on the user's desk. The keystroke logger of the timesharing mainframe — which had recorded every command the user issued, for billing — had no analog on the personal machine.
- **The right to build for ordinary people.** Anyone with a PC, a compiler, and a willingness to learn could write software for the same machine that the largest corporation owned. The asymmetry that had defined the mainframe era — that the institution had access to power the individual could not match — was, for a time, broken.

The PC era was not a utopia. It had its own pathologies — the Microsoft monopoly on operating systems being the most consequential — and these would themselves provoke antitrust action that culminated in the 2001 ruling and settlement. But the broad arc of the era was, on balance, democratizing. Computational power flowed outward, from a handful of institutional centers to hundreds of millions of individual users.

I lived through this. I founded a PC company in 1986, the year I married Louisa. I built a fourth-generation language called CGL that generated C and Unix applications. I built a company on top of CGL called Open Systems Group that, in 1996, was ranked #127 on the Inc. 500. I am not a disinterested observer of the PC era. I am one of the people who used it as a livelihood and watched it change a sector — software development for small and medium businesses — that the mainframe era had treated as an afterthought.

What I learned, in those years, is that the institutional logic that had seemed inevitable in 1965 was not, in fact, inevitable. The premises had changed. *The technology had changed underneath the politics.* And the people who had assumed the politics were inevitable were the slowest, in the end, to notice.

---

### The Web's Flattening of Distribution

The PC democratized the production of computation. The Web, beginning with Tim Berners-Lee's proposal at CERN in 1989 and the public release of NCSA Mosaic in 1993, democratized its *distribution*.

Before the Web, software reached users through a small number of channels: shrink-wrapped retail at companies like Egghead and CompUSA, mail-order catalogs, magazine cover disks, bulletin-board systems, the rare Internet FTP archive. Each channel had gatekeepers. Each gatekeeper had preferences. The cost of getting a piece of software to a million users, even after the PC made the user side trivially accessible, was substantial enough that the publishers' decisions were a meaningful constraint on what got built.

The Web removed the publisher constraint, almost overnight, for almost every category of digital content. Anyone with a web server — and within a few years, anyone with an HTML editor and a hosting account — could publish to a global audience. The cost of distribution, which had been the centralizing force keeping power inside the publishing industry, fell so close to zero that the publishing industry, in many sectors, never recovered.

What followed was extraordinarily generative. The Linux operating system. The Apache web server. PHP, MySQL, Python, Ruby, JavaScript, Node, Git. Wikipedia. Stack Overflow. GitHub. The vast and ongoing flowering of free and open-source software that, by 2025, ran a substantial fraction of the world's compute infrastructure — including, ironically, the very hyperscaler data centers this book has been criticizing.

It is important to acknowledge that the Web also produced new concentrations. The same low-cost-distribution dynamic that put a website within reach of any teenager produced, within fifteen years, a small number of platforms — Google, Facebook, Amazon, Apple, and a handful of others — that re-aggregated the distribution power the Web had decentralized. The pattern of *centralized, then distributed, then re-centralized at a higher layer* became the master pattern of the early twenty-first century Internet.

That pattern matters to this book. It is the pattern most likely to repeat with synthetic intelligence — except that the re-centralization is no longer at a *higher* layer. It is at the level of cognition itself.

---

### The Pattern: Centralized → Distributed → Cooperative

Step back and look at the arc.

- **1955–1975 — Centralized.** Computation lives in institutions. The user is a supplicant.
- **1975–1995 — Distributed.** Computation lives on personal hardware. The user is a sovereign.
- **1995–2015 — Re-centralized at a higher layer.** Personal computation persists, but value, attention, and control flow back into a small number of platforms. The user is a sovereign of their device and a tenant of the platforms that mediate their lives through it.
- **2015–present — Hyperscale.** A new class of computational capability — first deep learning, now large language models and other generative systems — is so capital-intensive that it can only be produced by entities operating at the scale of the largest platforms or larger. The pattern of mainframe-era institutional logic is reasserting itself, in a new form, at a new layer.

Each transition between phases looked, at the time, like a permanent reorganization. *Of course* the mainframe priesthood would always run computing. *Of course* the personal computer would always sit at the center of the user's life. *Of course* the platforms would always intermediate distribution. None of these turned out to be permanent. None of the present hyperscaler arrangements will be permanent either.

But — and this is the unhappy lesson — the *next* phase was never automatic. The PC revolution required the Homebrew Computer Club. The Web required Tim Berners-Lee's deliberate decision to release HTTP into the public domain rather than license it. The free software movement required Richard Stallman, the GNU project, and twenty years of unfunded labor. *The democratizing transitions in the history of computing have, every single time, required someone to refuse the current arrangement and build the next one.*

The next phase is the one this book is about. I want to give it a name now, because it has been implicit through Part I and the pillar chapters that follow will make it explicit.

The next phase is *cooperative*.

It is not a return to personal computing as it existed in 1985 — the synthetic intelligence layer is too capital-intensive for any one person to operate alone, and the data and compute requirements of useful synthetic intelligence will continue to grow. It is also not a continuation of hyperscale, in which a handful of operators provide everything for everyone on terms the users cannot read. It is a third thing. It is a federation of users, families, small businesses, communities, and cooperatives, each operating their own Cell, each owning their own data and their own keys, each cooperating with others to share compute when they have surplus and borrow compute when they need it, each grounded in their own knowledge and their own values, each able to invoke frontier capability when they choose to, on their own terms.

That is what this book proposes. That is what Warp is for.

---

### Why SI Is at the Same Inflection Point Now

There are five reasons to believe the present moment is structurally analogous to the period from roughly 1973 to 1977 — the years between when personal computing first became technically possible and when the Homebrew Computer Club made it culturally inevitable.

1. **The hardware required to do useful work has become accessible to individuals.** A modern Apple Silicon laptop, a single mid-tier NVIDIA GPU in a desktop, or a small Mac Studio is now sufficient to run open-weight models that would have qualified as state-of-the-art two years ago. The technology to be useful at the personal level *exists*. This was the precondition for the PC revolution. It is the precondition for the next.

2. **Open-weight models of meaningful capability are widely available.** Meta's Llama series, Mistral's models, the DeepSeek family, the Qwen family, and dozens of others are released to the public on permissive or near-permissive licenses. The ground floor of synthetic intelligence is no longer proprietary. It will not become proprietary again unless the broader culture allows it.

3. **The orchestration problem is the actual problem.** The hard part of building a useful synthetic intelligence is not, anymore, the model. It is the connective tissue — the retrieval, the routing, the memory, the integration with the user's data and tools, the policy enforcement, the cost management. This is exactly the problem that distributed cooperative architectures are good at, and that hyperscalers are not particularly better at than anyone else.

4. **The hyperscale path's costs are becoming legible.** Chapters 1, 2, and 3 have made the case that the environmental, economic, and privacy costs of the centralized path are not merely inconvenient — they are structural and accelerating. The window in which a sufficient number of users will accept those costs uncritically is closing.

5. **A generation of builders is ready.** The hobbyists, the open-source community, the privacy-aware developers, the small-business operators, the families that grew up online, the teachers, the librarians, the engineers who have grown tired of the platforms — all of these populations are not only available, they are restive. They are looking for the architecture. They have been looking for it for at least three years.

What is missing is the architecture itself, articulated clearly enough to build against.

The architecture is called Warp. The next chapter introduces it.

---

### A Note on Hope

The history I have just summarized is, for the most part, an encouraging history. The mainframe priesthood was outflanked. The platforms have not yet been outflanked, but the pattern has happened twice and it can happen again. The technology is on our side. The users are on our side. The economics are tilting our way faster than the incumbents seem to have noticed.

I am sixty-four. I have been wrong about many things in my life. About the broad arc of computing — that it tends, when builders refuse the current arrangement, toward broader access, lower cost, and greater human dignity — I do not believe I have been wrong.

The work that follows this chapter is the work of building the next arrangement. It will not happen on its own. *It never has*. It will happen because a sufficient number of us decide, deliberately, to make it happen.

That is the lesson of computing history. It is not a guarantee. It is an invitation.

---

## Endnotes

[^1]: Stewart Brand, remarks at the first Hackers Conference, Fort Cronkhite, California, November 1984, in conversation with Steve Wozniak. The conversation was filmed; Brand's actual phrasing differs slightly from the popular paraphrase that became "information wants to be free" — including the qualifier "almost" and the both-sides framing. See "Information wants to be free" (Wikipedia) for the full quotation and provenance: https://en.wikipedia.org/wiki/Information_wants_to_be_free. Steven Levy's *Hackers: Heroes of the Computer Revolution* (Doubleday, 1984; updated edition O'Reilly, 2010) is the canonical narrative of the era.

[^2]: *United States v. International Business Machines Corp.*, S.D.N.Y. Civ. No. 69-200 (filed January 17, 1969; trial began May 19, 1975; case withdrawn January 8, 1982). Department of Justice Antitrust Division, "United States' Memorandum on the 1969 Case." https://www.justice.gov/atr/case-document/united-states-memorandum-1969-case. Stanford CS course material on IBM regulation: https://cs.stanford.edu/people/eroberts/cs181/projects/corporate-monopolies/government_ibm.html. The "without merit" characterization is from Assistant Attorney General William F. Baxter's January 8, 1982 statement.

[^3]: "Homebrew Computer Club" (Wikipedia), drawing on contemporary accounts: https://en.wikipedia.org/wiki/Homebrew_Computer_Club. The club met from March 5, 1975 through December 1986. Founders Gordon French and Fred Moore convened the first meeting at French's Menlo Park garage; Lee Felsenstein moderated subsequent meetings. The first newsletter was published March 15, 1975 and continued for 21 issues through December 1977. Steven Levy, *Hackers* (cited in note 1), provides the canonical narrative.
