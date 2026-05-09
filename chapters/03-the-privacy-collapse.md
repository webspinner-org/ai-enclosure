# Chapter 3
## The Privacy Collapse

> *They conferred, as against the Government, the right to be let alone — the most comprehensive of rights, and the right most valued by civilized men.*
>
> — Justice Louis D. Brandeis, dissenting in *Olmstead v. United States*, 277 U.S. 438 (1928)

In 1928, the Supreme Court of the United States ruled, by a vote of five to four, that wiretapping a telephone line did not violate the Fourth Amendment because no physical entry of the suspect's premises had occurred. Justice Louis Brandeis dissented. His dissent in *Olmstead v. United States* is one of the great minority opinions in American jurisprudence. It made the case, decades before the Court would adopt it as majority doctrine, that the right to privacy is not a derivative of property law but a foundational human right — what Brandeis called "the right to be let alone, the most comprehensive of rights and the right most valued by civilized men."[^1]

The Court would eventually agree with him. By 1967, in *Katz v. United States*, the rule of *Olmstead* was overturned. Brandeis's dissent had become the law.

I open this chapter with that history because the technology of 2026 has produced a privacy crisis that *Olmstead* did not anticipate and that *Katz* does not solve. The wiretap of 1928 captured a single conversation between two specific persons. The synthetic intelligence of today captures, processes, and re-renders the conversations, the writings, the search histories, the medical records, the legal correspondence, and the unguarded interior monologues of essentially every literate person on the planet who has ever used the open Internet. There is no analogy in twentieth-century privacy law for what hyperscale Synthetic Intelligence has already done — and is doing now, in the moment you are reading this paragraph.

This chapter describes that collapse and the impossibility of retrofitting a remedy. The chapters that follow describe what an architecture designed for privacy from the foundation would look like. It is called Confidential SI, it is one of the four pillars of Warp, and the relevant chapters are 7 (the principle), 11 (the Cell as the privacy boundary), 15 (BYOK as the user's root of trust), and 17 (the full threat model and defenses).

The promise comes after the diagnosis. The diagnosis comes now.

---

### Where Your Data Actually Goes

When you submit a prompt to a hyperscale Synthetic Intelligence service, the popular imagination pictures something like a conversation with a particularly well-read assistant. The reality is closer to the following.

Your prompt — the text of your question, your code, your private worry, your medical query, your draft contract, your unfiltered diary entry, whatever it happened to be — is transmitted as a packet across the public Internet to the service's edge. From there it is forwarded to the service's API gateway, then to the load balancer, then to the inference cluster, where it is tokenized and presented to the model along with whatever system prompt the operator has prepended to it. The model produces a response. The response is returned to you.

That is the part the user sees. The parts the user does not see are these:

- **Logs.** The text of the prompt, the text of the response, and the metadata of the session (timestamp, IP address, account identifier, device fingerprint, geographic location, conversation ID) are written to the service's logs. These logs are retained, by default, for a period defined by the service's terms — frequently thirty days, sometimes much longer, sometimes indefinitely. They are accessible to the operator's employees with appropriate credentials, to any third party the operator chooses to share them with under their privacy policy, and — under court order — to law enforcement.
- **Training pipelines.** Unless the user has opted out (a feature whose existence and accessibility varies wildly across services), the content of the conversation may be added to the corpus used to fine-tune future versions of the model. The user's prompt becomes part of the model's training data. The user's words, paraphrased, may be returned someday to a different user.
- **Safety review.** Conversations flagged as potentially harmful, abusive, or commercially sensitive may be routed to human reviewers, frequently contractors located in jurisdictions different from the user's. The reviewers see the prompt, the response, and the surrounding context.
- **Cross-service integration.** In the case of services delivered through cloud platforms — Azure, AWS, Google Cloud — the conversation may be processed by ancillary services (logging, billing, security analytics, abuse detection) operated by the cloud provider, each of which has its own retention and access policies.
- **Preservation orders.** In May 2025, in connection with the *New York Times v. OpenAI* litigation, a federal magistrate judge issued an order requiring OpenAI to retain *all ChatGPT conversation logs* from the relevant period — affecting more than 400 million users worldwide. OpenAI objected. The order was upheld in June 2025.[^2]

That last point bears restating, because it has not been adequately absorbed by the public. *Every conversation that hundreds of millions of people had with a leading commercial Synthetic Intelligence service is now under court-ordered preservation in a copyright lawsuit.* Not because those users were parties to the lawsuit. Not because they consented. Because the operator was the defendant, and the operator's conversation logs are evidence.

This is the reality of where your data goes. It does not stay between you and the synthetic intelligence. There is no "between you and the synthetic intelligence." There is you, the operator, the operator's employees, the operator's contractors, the operator's cloud partners, the operator's training pipelines, the operator's logs, and any party who can compel disclosure of any of those — which is to say, eventually, almost anyone with a subpoena.

---

### Training Data Appropriation

The privacy collapse is not only a question of where the conversations go after they happen. It is also a question of where the training data came from in the first place.

Every frontier model in service today was trained on a corpus that includes, among other things: the contents of large portions of the open web; archives of news, magazine, and academic publications; books, both copyrighted and out-of-copyright; code repositories, public and (in some cases) private; transcripts of audio and video; social media posts; and proprietary corpora purchased or licensed from data brokers and publishers. The composition of these corpora is generally not disclosed in detail. The degree of consent obtained from the original authors is, in most cases, none.

This appropriation is now being litigated, on multiple continents, simultaneously.

The most consequential of these cases is *The New York Times Company v. Microsoft Corporation and OpenAI*, filed in the Southern District of New York in December 2023. The Times alleges that OpenAI and Microsoft trained ChatGPT on millions of copyrighted Times articles without permission, that the resulting model is capable of reproducing substantial passages of Times work near-verbatim on demand, and that the consequence is direct competitive harm to the Times's subscription business. OpenAI's defense rests primarily on the doctrine of fair use, arguing that machine training is a transformative analytical use that does not substitute for the original. In April 2025, Judge Sidney Stein narrowed the Times's claims but allowed the central copyright infringement allegation to proceed to the merits. The case is, as of this writing, the most closely watched intellectual-property litigation in the United States in a generation.[^3]

It is not the only one. Authors, illustrators, photographers, music publishers, news organizations, software developers, and Getty Images have filed comparable suits against OpenAI, Microsoft, Anthropic, Google, Meta, Stability AI, and others. The legal questions are genuinely unsettled. The factual question — *did the labs train on this material* — is, in case after case, conceded.

The privacy implications of this appropriation reach beyond copyright. The same scraping practices that captured copyrighted articles also captured: personal blogs, public-facing social media, court records that included sensitive personal information, leaked databases that had no business being indexed, medical case studies, legal filings, school records, and the millions of small private moments that ordinary people have left in publicly accessible corners of the Internet without consenting to the use that has been made of them.

In December 2024, the Italian data protection authority (Garante per la protezione dei dati personali) imposed a €15 million fine on OpenAI — the first GDPR penalty against a generative AI provider — finding that OpenAI had processed personal data scraped from the Internet without a lawful basis under Article 6 of the GDPR, that ChatGPT's age-verification mechanism was inadequate, and that OpenAI had failed to comply with the GDPR's 72-hour breach-notification requirement following a March 2023 data exposure. The Garante had previously, in March 2023, ordered ChatGPT temporarily suspended in Italy until OpenAI brought the service into nominal compliance.[^4]

The fine is small relative to OpenAI's revenue. The precedent is not. The Italian authority found, formally and on the record, that the principal commercial Synthetic Intelligence service in the world had been processing the personal data of millions of Europeans without legal basis, for years, and had no straightforward way to identify whose data it had processed or to expunge it on request.

The next time you see an industry executive describe the corpus of a model as "publicly available data," remember that finding. *Publicly available* is not the same as *lawfully usable* in a regulated jurisdiction, and the leading providers have been, in effect, betting that the regulators of the world would not be able to keep up.

---

### The Aggregation Problem

There is a deeper privacy problem that neither retention policies nor copyright remedies address. It is a problem the privacy literature calls *aggregation*.

The aggregation problem is the observation that information which is, individually, not sensitive — your zip code, your job title, your approximate age, your stated political party, your reading habits, the medical condition you researched last March, the legal question you asked your assistant in October, the names of your three children — becomes, in combination, dramatically more sensitive than any one piece of it. A profile assembled from a dozen non-private signals is often more revealing than any private one of them would have been.

A frontier Synthetic Intelligence service operating at hyperscale, with hundreds of millions of users, with access to the prompts and responses of those users across long periods, with the capacity to retrieve and re-render any of that content on demand, is the most powerful aggregation engine ever built. It is more powerful than the credit bureaus. It is more powerful than the ad-tech industry. It is more powerful, in raw informational reach, than any state intelligence apparatus has ever had at its disposal in peacetime.

I want to be clear about what I am claiming. I am not claiming that the major labs are *exercising* the aggregation power they possess. As far as the public record shows, they are mostly not. I am claiming that the aggregation power *exists*, and that it exists by virtue of the architectural choice to centralize the conversations of hundreds of millions of people in the operator's data centers.

The principal mitigation the industry offers to this problem is the promise of strong internal controls on access — the assurance that only authorized employees, under appropriate review, may query the logs. This mitigation is exactly as strong as the access-control system it depends on. It is also exactly as durable as the corporate policies behind it, which can be changed by a future board, a future regulator, a future intelligence agency with a national security letter, or a future business model that finds the data more valuable than the policy.

This is the structural fact: *as long as the conversations are in the operator's hands, the user's privacy depends on the operator's discipline.* No promise the operator makes can change that fact, because the operator cannot promise on behalf of the operator's successors, the operator's regulators, or the operator's adversaries.

---

### A Recent Cautionary Tale: Microsoft Recall

In the spring of 2024, Microsoft announced a new feature called *Recall*. Bundled with the new generation of "Copilot+ PCs," Recall would take periodic screenshots of everything a Windows user did on their computer, run optical character recognition over the screenshots, and store the resulting text in a searchable local database. The marketing positioned this as photographic memory for the personal computer. The security community noticed immediately that what Microsoft had built was, in effect, a self-administered surveillance camera.

Within days of the public preview, security researcher Kevin Beaumont demonstrated that Recall's database was unencrypted (relying only on standard BitLocker disk encryption, which would not protect against an info-stealing malware running in the user's session), captured credit card numbers and passwords by default, and was scheduled to be enabled by default on millions of new machines. The backlash was immediate and bipartisan. Microsoft delayed the feature, pushed it back from June to October to December, made it opt-in, encrypted the database, added biometric gating, and excluded sensitive fields from capture by default.[^5]

The Recall episode is instructive for two reasons. First, it shows that the industry's instincts on privacy, at the largest scale, are still unreliable. A company that has spent twenty years rebuilding its security reputation, with a multi-billion-dollar internal security organization, shipped — for default-on installation on millions of machines — a feature that captured the most sensitive content on the device into an unencrypted database. Second, it shows that public scrutiny still works, when applied early and loudly. Recall in its current form is a much better feature than the one initially announced, because the security community refused to let the original ship.

The cautionary lesson, however, is sobering. The Synthetic Intelligence layer of the modern operating system is being designed by parties who, even when their reputations are at stake, get the privacy fundamentals wrong on the first attempt. The default settings on the next generation of Synthetic Intelligence features will be set by them, in their interests, on their schedules. The reader who relies on those defaults is taking a serious bet on the discipline of the operator.

---

### The Regulatory Lag

The European Union has tried to write legislation for this problem. The result is the EU AI Act, which entered into force in August 2024, with most of its substantive provisions phasing in across 2025, 2026, and 2027. The Act distinguishes "general-purpose AI models" from sector-specific uses, imposes transparency and risk-management obligations on the largest providers, and requires disclosure of training-data summaries.

The Act is, as of this writing, the most ambitious attempt by any jurisdiction to govern frontier Synthetic Intelligence. It is also already, in important respects, behind the technology. The Act's transparency requirements are weaker than its drafters intended; the carve-outs for "open" models are large enough to drive a hyperscaler through; the enforcement infrastructure is being built in real time against an industry that ships a new generation of models every six months. The General Data Protection Regulation, on which much of European Union privacy law rests, was adopted in 2016 — before any of the technology this chapter describes existed.

In the United States, federal privacy legislation has not been enacted. State-level privacy laws, of which California's CCPA and CPRA are the leading examples, were not designed with synthetic intelligence in mind. The Federal Trade Commission has used its existing authority creatively, including in the Section 6(b) inquiry into hyperscaler-lab partnerships described in Chapter 2, but the FTC's authority is structural and competition-focused, not privacy-focused. Sectoral laws — HIPAA for medical data, FERPA for educational records, GLBA for financial data — apply in their domains but were written long before machine training was a concern.

The pattern, across jurisdictions, is consistent. *Privacy law is, almost without exception, behind the technology by years.* It is enforced selectively, against actors who are politically convenient, with penalties small relative to the revenue of the offenders. The Italian €15 million fine, while precedent-setting, is approximately what OpenAI generates in a few hours of revenue at 2025 levels.

The lag is not the regulators' fault. Regulators move at the speed of democratic deliberation, which is the correct speed for democratic deliberation. The lag is structural — a property of the difference between the speed at which a hyperscale service can be deployed (months) and the speed at which legislation can be drafted, debated, enacted, and enforced (years to decades).

A privacy regime that depends on regulators catching up is a privacy regime that depends on a race regulators cannot win.

---

### Why Privacy Can't Be Retrofitted

The hardest fact about the current Synthetic Intelligence privacy collapse is the one most resistant to remedy: *privacy cannot be retrofitted into a system that was not designed for it.*

This is not an argument from preference. It is an argument from architecture.

Consider what a privacy retrofit would have to accomplish. It would have to:

1. **Identify all data already used to train existing models** — the corpora of GPT-4, Claude 3, Gemini 2, and their successors — and assess each piece for lawful basis under the privacy regime of the user's jurisdiction.
2. **Honor deletion requests** for data that should not have been included, given that deletion requests under the GDPR's Article 17 ("right to erasure") cannot, on present technology, be fully satisfied: removing a specific person's data from a trained model requires retraining the model, which costs hundreds of millions of dollars and takes months. No frontier provider performs full retraining in response to deletion requests, and the technical research on "machine unlearning" remains in its infancy.
3. **Prevent inadvertent disclosure** through model outputs, given that frontier models have been demonstrated to reproduce copyrighted text, personal information, and private data verbatim under appropriate prompting.
4. **Constrain log access** durably across changes of ownership, business model, regulatory environment, and personnel — none of which the operator can guarantee to an individual user.
5. **Provide cryptographic assurances** that the user's data is not being processed in ways the user has not authorized, when the user has, by the architecture, given up custody of the data to a remote operator.

No combination of privacy policies, terms of service, encryption-at-rest, audit logs, or compliance certifications can satisfy these requirements when the underlying architecture is *centralized rented inference from operator-owned facilities trained on operator-curated corpora.* Each remedy addresses one symptom. None addresses the cause.

The cause is the architectural choice to put the user's data in the operator's facility, under the operator's control, processed by the operator's pipeline, retained on the operator's terms.

---

### The Promise, in Brief

The Webspinner Foundation's answer to this collapse is not a stronger privacy policy. It is a different architecture.

In the architecture proposed by this book — described in detail in the chapters that follow — the structural facts are inverted:

- Your data lives in **your Cell**, on hardware you control, under cryptographic identity you own. The operator is no longer in custody of it. (Chapter 11.)
- Inference is **grounded in your own corpus** through Webspinner Retrieval-Augmented Grounding (WRAG), so the model does not need to have memorized your private knowledge to answer questions about it. (Chapter 12.)
- When a frontier model is invoked, it is invoked under **Bring-Your-Own-Key (BYOK)** — your contractual relationship with the model provider, with you as the root of trust, with sensitivity-aware routing that decides what may leave your Cell at all. (Chapter 15.)
- The architecture itself, **not the operator's policy**, prevents your conversations from accumulating in someone else's logs, your data from feeding someone else's training, or your prompts from being retrieved under court order against a service you do not even use. (Chapters 7 and 17.)

These are not promises about future restraint by the parties currently in control. They are properties of a system in which those parties are not in control of your data in the first place.

The structural choice is the remedy. Nothing else can be.

---

That is the diagnosis of the privacy collapse. The next chapter — the last in Part I — looks at what computing history has to teach us about how to escape diagnoses of this severity. The history is not encouraging. It is also not without precedent.

We have escaped one of these traps before.

---

## Endnotes

[^1]: *Olmstead v. United States*, 277 U.S. 438 (1928), Brandeis, J., dissenting. The full passage: "The makers of our Constitution undertook to secure conditions favorable to the pursuit of happiness. They recognized the significance of man's spiritual nature, of his feelings, and of his intellect. They knew that only a part of the pain, pleasure and satisfactions of life are to be found in material things. They sought to protect Americans in their beliefs, their thoughts, their emotions and their sensations. They conferred, as against the Government, the right to be let alone — the most comprehensive of rights, and the right most valued by civilized men. To protect that right, every unjustifiable intrusion by the Government upon the privacy of the individual, whatever the means employed, must be deemed a violation of the Fourth Amendment." The dissent was vindicated by *Katz v. United States*, 389 U.S. 347 (1967). Full text via Justia: https://supreme.justia.com/cases/federal/us/277/438/

[^2]: NPR, "Judge allows 'New York Times' copyright case against OpenAI to go forward" (March 26, 2025); Nelson Mullins, "From Copyright Case to AI Data Crisis: How The New York Times v. OpenAI Reshapes Companies' Data Governance and eDiscovery Strategy" (2025); OpenAI, "How we're responding to The New York Times' data demands in order to protect user privacy" (2025). The 400-million-user preservation order was issued by Magistrate Judge Ona T. Wang in May 2025 and affirmed by District Judge Sidney Stein in June 2025.

[^3]: *The New York Times Company v. Microsoft Corporation, OpenAI, Inc., et al.*, S.D.N.Y. Case No. 1:23-cv-11195 (filed December 27, 2023); Memorandum Opinion and Order on motion to dismiss, April 4, 2025 (Stein, D.J.). https://www.nysd.uscourts.gov/sites/default/files/2025-04/yf%2023cv11195%20OpenAI%20MTD%20opinion%20april%204%202025.pdf. Harvard Law Review, "NYT v. OpenAI: The Times's About-Face" (April 2024). https://harvardlawreview.org/blog/2024/04/nyt-v-openai-the-timess-about-face/

[^4]: Garante per la protezione dei dati personali (Italian Data Protection Authority), provvedimento (decision) of December 2024 imposing the €15 million fine on OpenAI for GDPR violations. The Hacker News, "Italy Fines OpenAI €15 Million for ChatGPT GDPR Data Privacy Violations" (December 2024); Lewis Silkin, "OpenAI faces €15 million fine as the Italian Garante strikes again" (January 14, 2025); Cross-Border Data Forum, "Generative AI and GDPR Enforcement in Europe: A Lot of Noise, One Fine, Zero Survivors" (2024). For the original March 2023 ban: Data Protection Report, "Italian Garante bans Chat GPT from processing personal data of Italian data subjects" (April 2023).

[^5]: Kevin Beaumont, "Microsoft Recall on Copilot+ PC: testing the security and privacy implications," DoublePulsar (June 2024). https://doublepulsar.com/microsoft-recall-on-copilot-pc-testing-the-security-and-privacy-implications-ddb296093b6c. CBC News, "Microsoft delays adding Recall screenshot feature to Windows over privacy concerns" (June 2024). https://www.cbc.ca/news/business/microsoft-ai-recall-feature-delayed-controversy-1.7235455. *Windows Recall* Wikipedia article for chronology of delays and the eventual security redesign: https://en.wikipedia.org/wiki/Windows_Recall.
