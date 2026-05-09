# Foreword

I started programming at sixteen. By twenty I was working the night shift on a Burroughs B-1900 at Cook Children's Hospital in Fort Worth, and that was when I first understood that computing was a priesthood and I wanted in.

The machine took up most of a room. It had its own climate. A small society of operators tended it in white shirts and quiet voices, the way you would tend an altar. I was the boy who got to feed it overnight — to watch the magnetic-tape spools turn and the line printer chatter out the day's reckoning. I loved it. I also noticed something that would shape more than forty years of my life: the people who depended on the machine were not the people who controlled it. The doctors, the nurses, the parents pacing the corridors with sick children — they trusted the machine because they had no choice. They could not see inside it. They could not question it. They could not own it.

I went to TCU and studied technology and philosophy, which struck most people as an odd combination and struck me as the only one. By the time I graduated, the priesthood I had glimpsed in Fort Worth was already cracking. The personal computer had arrived, and it arrived with an argument: that the power locked inside those climate-controlled rooms could be set free. That a hospital night-shift operator, or a small business in a rented strip-mall office, or a teacher, or a poet, did not have to ask permission to compute.

I joined that argument. In 1986 I helped found a PC company. From there I built CGL — a fourth-generation language that generated C and Unix applications — and on top of CGL I built Open Systems Group. In 1996, *Inc.* magazine ranked us number 127 on the Inc. 500. We were not the largest player in that revolution, not by a long way. But we were *in* it. We watched it happen. We helped it happen. The mainframe priesthood did not surrender; it was outflanked, by cheap commodity hardware, by open standards, and by a generation of builders who refused to accept that real computing required real institutions.

That is a story I have told in fragments many times. I am telling it once more now, in a book that is not about the past — because what I learned during those years is the only reason I can see clearly what is happening today.

---

After Open Systems Group closed, I was semi-retired in the way a builder is ever semi-retired, which is to say, restlessly. I went to Trinity School for Ministry. I had carried, since well before the PC years, a quiet sense that there was a calling on my life I had not yet answered. Seminary was my attempt at the answer.

A year into the program, I checked myself into the Hippocrates Health Institute and got sober. I was there for six weeks. When I came home I made love to my wife — Louisa, whom I had married on September 27, 1986. She had been a year behind me at TCU, and her parents had wanted her diploma in hand before any wedding — a way, I came later to suspect, of being quietly sure the relationship would stick. It has. By the time of my homecoming from Hippocrates we had been married twenty years, and she had carried our two daughters into the world a decade earlier. I had not understood, in all the time before, that a long habit of alcohol had quietly made me sterile. Louisa had not understood that she had not yet passed the age where a third child was possible. We were both, as it turned out, wrong. Our son arrived nine months later, a surprise from a Higher Power who, I have learned, is fond of surprises and fonder still of jokes.

I finished the degree. I have a Master of Arts in Religion from Trinity, and I have nothing but gratitude for what those years taught me. But the call I had gone there to answer turned out to be a different call than I had expected. The empty nest I had walked into seminary anticipating was, instead, a full house with a newborn boy at the center of it. Slowly, then unmistakably, the message clarified: *I was being called to be a father — not, at least not yet, a Father.* That distinction, lower case to upper, is one of the better jokes my Higher Power has ever played on me. I grin about it most days. I am grinning now.

That was nineteen years ago. My three children — the two daughters who came when they were supposed to, and the son who came when he was not supposed to — have been the central joy of the life my wife and I have built. Everything else, including this book, has been arranged around them.

I tell that story here, in the foreword to a book about synthetic intelligence, because the calling I went to seminary to answer did not go away when I left. It clarified. The call was not to a pulpit. The call was to use what I knew, in the years I have left, to help defend something the next generation will badly need defended. Nineteen years from the conception of the calling to the publication of this book is, by any measure, a long incubation. It is also exactly the right length of time, because the question this book asks could not have been asked any sooner. The technology was not yet here. The danger was not yet here. The full circle had not yet closed.

The Japanese have a word — *ikigai* — for the thing that is your reason for being. I believe I have arrived at mine. This book is the first artifact of it.

---

Here is what I see, with the eyes of someone who watched the last great inflection point happen:

The pattern is repeating. A new priesthood has built itself, in a new generation of climate-controlled rooms — bigger now, drawing power on the scale of small nations, drinking water in regions that cannot afford to spare it. The machines inside those rooms are far more capable than the B-1900 was. They are also, in a way the B-1900 was not, *consequential*. They are beginning to mediate the information, the work, and the reasoning of the people who do not control them. The doctors, the nurses, the parents, the teachers, the poets. Everyone outside the priesthood. Which is to say: nearly everyone.

We have been here before. We know how this goes if it is left to go on its own. The priesthood does not surrender voluntarily. It is outflanked, or it is not outflanked, and the difference between those two outcomes determines what kind of century this becomes.

This is the second great act of democratization in computing, and it is more urgent than the first. The first was about productivity — about who could compute, and at what cost. This one is about cognition. About who gets to think with what tools. About whose mind is augmented, on whose terms, with whose data, in service of whose ends. To leave that question to a small handful of entities accountable only to capital is, I will argue in the chapters that follow, the largest single threat to human sovereignty in our lifetimes.

I do not say that lightly. I am not a man given to apocalyptic framing. I lived through the first revolution and I know that technology does not, on its own, doom us; people and structures do. But the structure now consolidating around hyperscale Synthetic Intelligence is the wrong structure. It is centralized where it should be cooperative. It is opaque where it should be inspectable. It is rented where it should be owned. It is, in a phrase, *enclosing* a commons that has not yet finished being born.

Hence the title of this book: *AI Enclosure*. The historical analogy is deliberate. In an earlier century, the great commons of England were fenced off and converted into private property, and the people who had lived on them for generations were dispossessed of a way of life. Something analogous is being attempted now with the cognitive commons — with the data that is ours, the language that is ours, the means of synthetic thought that ought to be ours. It is being fenced. It is being converted. And most of us, like most of the dispossessed in the original Enclosures, do not yet understand that it is happening.

This book is my warning that it is happening, and my argument for what to build instead.

---

What I propose is called Warp.

Warp is an architecture for sovereign Synthetic Intelligence — SI that you own, that you can inspect, that you can modify, that you can refuse, and that you can disconnect. It is built from things called Cells, which are the fundamental privacy and capability boundaries of the system. Cells contain three roles called Loom, Weaver, and Grimoire. The vocabulary is borrowed from weaving, on purpose, because what we do when we orchestrate intelligence is closer to weaving than to magic. Threads are real. The Loom is real. The cloth is something the weaver makes, deliberately, and answers for.

I will define those terms properly in the chapters that follow, and I will defend the architecture on environmental, economic, technical, and moral grounds. The book is organized around four pillars — Green SI, Confidential SI, Sovereign SI, and Moral AI — and a Value Triangle that demonstrates the pillars are not in tension with cost, speed, or quality but rather constitute the proof of all three.

You do not need to be a technologist to follow the argument. You do need to be willing to take the question of *who owns the synthetic mind* as seriously as the previous generation took the question of who owned the personal computer. The previous generation answered well enough that you are reading this on a device that belongs to you, in software whose lineage runs through the rebellion against the mainframe priesthood. We owe the next generation an answer at least that good.

---

The Webspinner Foundation, which I founded and which is the steward of the work this book describes, is best understood as a movement that happens to ship software. Webspinner LLC builds the technology. Webspinner Cloud will run a managed version of it for those who want one. The Foundation exists to make sure that neither of those entities, nor any successor to them, ever becomes the priesthood we are trying to outflank. The Foundation is the conscience of the architecture. The book you are holding is its first public statement.

This is not a business book. It is not a technical manual, though there is technical substance in it where technical substance is required. It is a manifesto from someone who has built before, is building now, and is asking the reader to build alongside.

The case it makes is technical, economic, environmental, and moral. Those four arguments reinforce one another. Pull on any one of them and the others tighten. That is by design.

---

A last word, before the argument begins.

I am sixty-four. Old enough to have seen this pattern once before, and not too old to fight it again. I have been a hospital night-shift operator, a builder of compilers, the founder of a small company that made the Inc. 500, a seminary student, a sober man, the surprised father of an unexpected son, and now an old hand at a new revolution. I have been wrong about many things in my life. I do not believe I am wrong about this one.

The first revolution put the power of computation on the desks of ordinary people. The second revolution will put the power of synthetic intelligence in the hands of ordinary people — or it will fail to, and a small number of entities will hold that power on terms the rest of us cannot read, written by parties we cannot reach, for purposes we did not authorize.

I would prefer the first outcome. I have spent my life preferring the first outcome. This book is my best attempt to make it more likely.

Warp is the architecture. Warp speed is the pace.

The work begins on the next page.

— John D. Marx
   Founder, The Webspinner Foundation
