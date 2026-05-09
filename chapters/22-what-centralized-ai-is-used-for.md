# Chapter 22
## What Centralized AI Is Used For — and What Warp Refuses

> *There are some human functions for which it is inappropriate to substitute computer systems no matter how technically accomplished.*
>
> — Joseph Weizenbaum, *Computer Power and Human Reason: From Judgment to Calculation* (1976)

In 1976, the MIT computer scientist Joseph Weizenbaum — who had, a decade earlier, written ELIZA, the program that demonstrated how readily humans would attribute understanding to systems that had none — published *Computer Power and Human Reason*, a book that became one of the foundational moral critiques of computing's applications. Weizenbaum's argument was not that computers could not, in principle, perform any function. It was that *some functions, by virtue of what they require of human beings, ought not to be performed by machines* — and that the technical capacity to substitute computation for judgment did not, by itself, constitute a license to do so.[^1]

This chapter is the chapter the comparison-of-architectures has been building toward. It names, plainly and from public record, what *centralized* synthetic-intelligence services are now being used for. It describes the structural impossibility of opting out as an individual user of those systems. And it explains the architectural mechanism by which Warp *refuses*, by design, to participate in those uses, including some applications that the user themselves might be tempted to authorize but that the architecture, on the Foundation's behalf, will not enable.

This is the chapter where the word *Moral* in *Moral AI* (Chapter 9) becomes operational. The architecture is not morally neutral. It is built with deliberate refusals.

---

### The Dual-Use Problem

A general-purpose computational capability is, by definition, dual-use. The same matrix multiplication that summarizes a doctor's notes also targets a building. The same retrieval pipeline that answers a student's homework question also profiles a population. The same model that drafts a wedding toast also drafts political propaganda. The dual-use problem is not specific to synthetic intelligence; it is the standing problem of every transformative technology in modern history, from the steam engine to nuclear physics to the Internet itself.

What is different about synthetic intelligence is the *operator's* position in the dual-use problem. In most prior dual-use technologies, the technology was sold as a tool — and the buyer's use of the tool was, ethically, the buyer's responsibility. The chemical company that sold fertilizer was not, in any direct sense, complicit in the buyer's decision to use it for explosives. The chip manufacturer that sold semiconductors was not, in any direct sense, complicit in the buyer's decision to use them in weapons systems.

Synthetic intelligence at hyperscale is different because the *operator continues to operate* the technology after the user has acquired access to it. Every query passes through the operator's pipeline. Every output is produced by the operator's model. The relationship is not buyer-seller-after-purchase; it is *renter-and-operator-throughout*. The operator's contracts, policies, and practices govern, in real time, what the technology is being used for and by whom.

This is the dual-use problem with the operator as continuous co-participant. *And the operator's incentives, as Chapter 2 demonstrated, are increasingly aligned with use cases that ordinary users have not consented to and would not, if asked clearly, consent to.*

---

### Documented Uses

The following are matters of public record, drawn from corporate announcements, investigative journalism, and government contracting databases. The names are named because they are parties to public contracts; the structural argument is not against the named parties but against the arrangement they collectively constitute.

**Military and defense applications.** In December 2022, the United States Department of Defense awarded the Joint Warfighting Cloud Capability (JWCC) contract — valued at $9 billion — to Amazon Web Services, Microsoft Azure, Google, and Oracle. The JWCC contract gives Defense access to commercial cloud services across all classification levels (unclassified, secret, top secret), including AI and machine-learning capabilities provided by these operators' synthetic-intelligence services. A successor contract is in procurement as of early 2026.[^2]

**OpenAI's policy change.** On or about January 10, 2024, OpenAI quietly modified its usage policy to remove the explicit prohibition on "military and warfare" use that had previously been part of the company's published terms. OpenAI subsequently confirmed work with the U.S. Department of Defense, including DARPA-funded cybersecurity work and broader engagement with national-security agencies. The change was first reported by *The Intercept* and confirmed across multiple business and policy publications.[^3]

**Anthropic, Palantir, and AWS partnership.** In November 2024, Anthropic announced a partnership with Palantir Technologies and Amazon Web Services to deliver Claude family models into U.S. intelligence and defense agency deployments via Palantir's AI Platform. Anthropic has subsequently developed "Claude Gov" — custom variants of its models built for national-security customers — and was awarded a $200 million Department of Defense contract for "prototyping frontier AI capabilities that advance U.S. national security." A 2026 dispute over the scope of unrestricted military use produced a notable counterexample: Anthropic's CEO publicly refused certain Pentagon requests on stated ethical grounds, and the contract was terminated by mutual incompatibility. The episode is structurally illuminating in both directions — that the AI labs are now major military contractors, and that the labs themselves sometimes attempt to draw lines that the contracting customer rejects.[^4]

**Surveillance and law-enforcement integrations.** Multiple commercial synthetic-intelligence services are now integrated, directly or via reseller and integrator partnerships, with federal, state, and local law-enforcement systems. The integrations include investigative-document review, transcript analysis, predictive analytics, and population-scale content moderation. Specific deployments are typically not publicly disclosed in detail; the existence of the deployments is a matter of public record through contracting databases and reseller announcements.

**Content moderation at scale.** Major platforms operate synthetic-intelligence-driven content moderation across billions of users, with the moderation policies set by the platform operator and enforced at scale on user-generated content. The moderation is, by structural necessity, opaque to the affected users — who learn of moderation decisions only after they are made, with appeal mechanisms that are themselves typically AI-mediated.

**Behavioral targeting.** Synthetic-intelligence systems are now central inputs to advertising, recommendation, and behavioral-engagement systems across the Internet's largest platforms. The targeting is invisible to most users; the synthetic-intelligence component is rarely advertised to the targets.

These uses are not hypothetical. They are the documented current applications of the synthetic-intelligence services the major operators provide. *Every user of every hyperscale synthetic-intelligence service is, by virtue of using the service, providing revenue and (in some cases) training data and (in all cases) operational scale to the operators that are pursuing these contracts.*

This is not a moral accusation against the user. The user is not, in any individual sense, responsible for the operator's contracts. The structural fact, however, is that *the user's monthly subscription is part of the operator's revenue base that funds the operator's pursuit of these other contracts*. The user is supporting, financially if not morally, an operator whose other activities the user may not endorse.

---

### The Structural Impossibility of Opting Out

A user who wishes to use synthetic-intelligence capability while not supporting the operator's other applications faces, in the hyperscale architecture, an essentially impossible problem.

The user can read the operator's published policies and choose operators whose stated commitments most closely align with the user's preferences. *This does not work*, because the operators' published policies are revisable (as OpenAI's January 2024 change demonstrated), and because the operator's position regarding any particular customer's use is determined by the operator's contract with that customer, not by the operator's published consumer policy.

The user can avoid specific products that have been publicly tied to specific applications. *This also does not work*, because the underlying capability is shared across the operator's product lines. The same models, the same data centers, the same engineering teams, and the same operational infrastructure serve consumer subscriptions, enterprise contracts, and government deployments. A user paying $20 per month for a consumer chat product is supporting the operator's overall capability stack, including the portions sold separately to military and intelligence customers.

The user can ask the operator detailed questions about how their queries are processed, which models are used, what training corpora are involved, whether their data feeds capabilities the user does not wish to support. *This does not produce reliable answers*, because the operator's commercial sensitivity around contracting customers prevents detailed disclosure, and because the operator's internal processes are not, in any case, observable from the user's side.

The structural conclusion is that *a user of any hyperscale synthetic-intelligence service is, in operational terms, a participant in the operator's full activity portfolio*, with no architectural or contractual mechanism available to the user that would limit their participation to only the activities the user endorses. The opt-out the user ostensibly has is the binary choice to use the service or not — a choice that, given the dependence many users have developed on these services, is functionally not an opt-out at all.

This is the dual-use problem at hyperscale, with the user as unwilling participant in the operator's other arrangements.

---

### Warp's Structural Prevention

The Warp architecture refuses participation in these arrangements through three structural mechanisms.

**The first is custody.** A Cell's data is on the Cell's owner's hardware, under the owner's keys. There is no operator-side aggregation that could be sold to a defense contractor, fed into a surveillance system, or repurposed for behavioral targeting — because there is no operator-side aggregation. The data the operator does not have, the operator cannot misuse.

**The second is invocation control.** A Cell's capability invocations are governed by the owner's policy, evaluated before any external call leaves the Cell. A Cell can be configured to refuse to invoke specific providers, refuse to handle specific categories of query, refuse to participate in specific kinds of federation. The architecture enforces these refusals at the protocol level. *A Cell that has been configured to refuse military-aligned providers will not invoke them, regardless of how the query is phrased.*

**The third is the Foundation's deliberate refusal.** The Webspinner Foundation, as steward of the architecture, has chosen not to build certain features into the reference implementations. Some examples:

- The reference Capability Bus does not implement integrations with major surveillance platforms. Building such integrations would be a separate effort by parties willing to do so, and the Foundation does not produce the tooling that would make those integrations easy.
- The reference Loom does not include behavioral-targeting components, advertising-channel integrations, or population-scale analytics. The Loom is for the user's interaction with their Cell, not for the Cell's analysis of the user.
- The reference WRAG implementation does not include population-scale aggregation across federated peers. WRAG retrievals are scoped to the querying Cell's authorized federations and do not produce cross-population behavioral profiles as a side effect.
- The reference Compute Farm does not implement integrations with autonomous-weapons targeting systems, with mass-surveillance correlation engines, or with the operational platforms of defense contractors known to be assembling such systems.

These are not hypothetical refusals. They are concrete decisions the Foundation has made about what the reference architecture will and will not include. A third party could, of course, build integrations along these lines — the architecture is open source — but they would be doing so over the Foundation's stated objection, with the Foundation's tooling actively designed not to make their work easier, and with any Cells participating in such integrations doing so by their owners' explicit configuration rather than by default.

**The negative features of Warp are part of what Warp is.**

---

### What This Means in Practice

For a user, the architectural refusal translates to specific operational properties.

A Cell does not, by default, federate with operators whose primary business models depend on uses the Foundation has refused to support. A Cell does not, by default, advertise its capabilities into federations that include such operators. A Cell's user can opt into broader federation if they wish, but the default is the more restrictive arrangement.

A user's BYOK invocations to commercial frontier providers go to the providers the user has chosen. The user can blocklist providers whose other contracts the user finds incompatible with their values. The user's queries reach the chosen provider only, with the minimum-necessary content; the user is not, by virtue of using their Cell, contributing revenue or operational scale to providers they have not chosen.

A user's data does not leave the Cell except where the user has authorized it. *No automatic flow exists* by which the user's content could be aggregated, sold, repurposed, or surveilled by a party the user has not explicitly engaged with. The data the operator does not have, the operator cannot misuse — and there is no operator.

For a small business, a community organization, or a professional practice operating a Sovereign Cell, the architectural refusal translates to a posture they can communicate to their own constituents: *"Our synthetic-intelligence work does not contribute to military, surveillance, or behavioral-targeting systems, because the architecture we use does not connect to those systems. Here is the audit trail that demonstrates the claim."* This is a posture that no operator-mediated arrangement can credibly offer, because the operator-mediated arrangement does, by structural necessity, contribute to the operator's other activities.

---

### A Difficult Honesty

I want to close, as the comparison chapters have closed, with what this argument does *not* claim.

It does not claim that every defense, intelligence, or law-enforcement use of synthetic intelligence is wrong. The Foundation does not take this position. Many such uses are, by reasonable judgment, legitimate functions of legitimate states acting within reasonable constraints. The architectural refusal Warp implements is not a claim that the underlying applications are universally illegitimate; it is a claim that *the architecture should not be the means by which ordinary users are conscripted into supporting them without their consent*.

It does not claim that operators currently providing these services are evil. The Foundation does not take this position either. The operators are, in the main, run by people making decisions within the constraints of competitive pressure, regulatory expectation, and shareholder obligation. The structural problem is the architecture, not the people.

It does not claim that Warp is a complete answer to the problems described. Warp is one architectural choice. The legitimacy of state surveillance, the constraints on autonomous weapons, the proper limits of behavioral targeting — these are political questions that the architecture cannot resolve, only refuse to participate in. The political work remains to be done, and Warp is not, in itself, a substitute for it.

What the chapter does claim is that *users who do not wish to participate in these arrangements should have an architectural alternative that lets them work with synthetic intelligence without doing so*. Until now, no such alternative has been available at the level of capability ordinary users need. Warp is the alternative. The negative features — what Warp will not do — are part of what the architecture sells, and they are the part the Foundation considers most important.

---

### Closing Part IV

This chapter closes Part IV.

Part IV has compared the two architectures across the four operational dimensions: cost, environmental footprint, privacy posture, and capability and quality. It has named, in this final chapter, the moral comparison that the operational comparisons enable.

The verdict, across all five comparisons, is that Warp is the better architecture for users — better in cost, better in environmental footprint, better in privacy, capability-equivalent or better in quality for the bulk of useful work, and structurally aligned with the user's interest in not contributing to applications they have not endorsed.

Part V — the final part of the book — turns from comparison to invitation. It is the part that asks the reader, having understood the trap and the alternative, what their own response will be. The architecture is built. The work that follows is the work of populating it.

---

## Endnotes

[^1]: Joseph Weizenbaum, *Computer Power and Human Reason: From Judgment to Calculation* (W. H. Freeman, 1976). Weizenbaum was the creator of the ELIZA program (1964–1966), an early natural-language interaction demonstration whose unintended popularity (users genuinely confiding in the program's simple pattern-matching) shaped Weizenbaum's later philosophical work. *Computer Power and Human Reason* is among the foundational texts of computing-ethics literature; its argument that some functions ought not to be substituted by computational systems regardless of technical capacity remains a touchstone in the field.

[^2]: U.S. Department of Defense, Joint Warfighting Cloud Capability (JWCC) contract awards (December 2022). FedScoop, "Pentagon awards AWS, Google, Microsoft and Oracle spots on Joint Warfighting Cloud Capability solicitation" (December 8, 2022). https://fedscoop.com/pentagon-awards-aws-google-microsoft-and-oracle-spots-on-joint-warfighting-cloud-capability-solicitation/. Microsoft, "Microsoft continues commitment to US Department of Defense with JWCC selection" (December 8, 2022). https://blogs.microsoft.com/blog/2022/12/08/microsoft-continues-commitment-to-us-department-of-defense-with-jwcc-selection/. Microsoft federal-services overview: https://learn.microsoft.com/en-us/compliance/us-government/gov-jwcc. Subsequent expansion: TechCrunch, "Pentagon inks deals with Nvidia, Microsoft, and AWS to deploy AI on classified networks" (May 2026).

[^3]: Sam Biddle, "OpenAI Quietly Deletes Ban on Using ChatGPT for 'Military and Warfare,'" *The Intercept* (January 12, 2024). https://theintercept.com/2024/01/12/open-ai-military-ban-chatgpt/. CNBC, "OpenAI quietly removes ban on military use of its AI tools" (January 16, 2024). https://www.cnbc.com/2024/01/16/openai-quietly-removes-ban-on-military-use-of-its-ai-tools.html. TechCrunch, "OpenAI changes policy to allow military applications" (January 12, 2024). https://techcrunch.com/2024/01/12/openai-changes-policy-to-allow-military-applications/. OpenAI's subsequent confirmation of DoD/DARPA work via the company's published statements and the Anna Makanju remarks at the World Economic Forum, January 2024.

[^4]: Palantir Investor Relations, "Anthropic and Palantir Partner to Bring Claude AI Models to AWS for U.S. Government Intelligence and Defense Operations" (November 2024). https://investors.palantir.com/news-details/2024/Anthropic-and-Palantir-Partner-to-Bring-Claude-AI-Models-to-AWS-for-U.S.-Government-Intelligence-and-Defense-Operations/. TechCrunch, "Anthropic teams up with Palantir and AWS to sell AI to defense customers" (November 7, 2024). https://techcrunch.com/2024/11/07/anthropic-teams-up-with-palantir-and-aws-to-sell-its-ai-to-defense-customers/. Anthropic, "Anthropic awarded $200M DOD agreement for AI capabilities" (2025). https://www.anthropic.com/news/anthropic-and-the-department-of-defense-to-advance-responsible-ai-in-defense-operations. The 2026 dispute is documented in *Euronews*, "Why AI company Anthropic and the US are at a standoff over a military contract" (February 2026), and the Wikipedia overview "Anthropic–United States Department of Defense dispute," with the EFF analysis at https://www.eff.org/deeplinks/2026/03/anthropic-dod-conflict-privacy-protections-shouldnt-depend-decisions-few-powerful providing the strongest framing of the structural lesson.
