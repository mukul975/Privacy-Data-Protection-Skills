# Standards and Regulatory References — Children's Profiling Limits

## Primary Legislation

### GDPR Article 4(4) — Definition of Profiling

"'Profiling' means any form of automated processing of personal data consisting of the use of personal data to evaluate certain personal aspects relating to a natural person, in particular to analyse or predict aspects concerning that natural person's performance at work, economic situation, health, personal preferences, interests, reliability, behaviour, location or movements."

### GDPR Article 22 — Automated Individual Decision-Making

- **Art. 22(1)**: "The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her."
- **Art. 22(2)**: Exceptions: (a) necessary for contract; (b) authorised by law; (c) explicit consent with suitable safeguards.
- **Art. 22(3)**: In the cases of Art. 22(2)(a) and (c), the controller must implement suitable measures to safeguard the data subject's rights and freedoms and legitimate interests, at least the right to obtain human intervention, to express their point of view, and to contest the decision.
- **Art. 22(4)**: Decisions in Art. 22(2) shall not be based on special categories of data in Art. 9(1) unless Art. 9(2)(a) or (g) applies.

### GDPR Recital 71 — Children and Automated Decisions

"In order to ensure fair and transparent processing in respect of the data subject [...] the controller should use appropriate mathematical or statistical procedures for the profiling, implement technical and organisational measures appropriate to ensure, in particular, that factors which result in inaccuracies in personal data are corrected and the risk of errors is minimised [...] Such measure should not concern a child."

### EU Digital Services Act — Article 28(2)

"Providers of online platforms shall not present advertisements on their interface based on profiling as defined in Article 4, point (4), of Regulation (EU) 2016/679, using personal data of the recipient of the service when they are aware with reasonable certainty that the recipient of the service is a minor."

### UK AADC Standard 5 — Detrimental Use of Data

"Do not use children's personal data in ways that have been shown to be detrimental to their wellbeing, or that go against industry codes of practice, other regulatory provisions or Government advice."

### UK AADC Standard 7 — Default Settings

"Settings must be 'high privacy' by default (unless you can demonstrate a compelling reason for a different default, taking account of the best interests of the child)."

### UK AADC Standard 12 — Profiling

"Switch options which use profiling off by default (unless you can demonstrate a compelling reason for profiling to be on by default, taking account of the best interests of the child). Only allow profiling if you have appropriate measures in place to protect the child from any harmful effects (including but not limited to feeding the child content that is detrimental to their health or wellbeing)."

### UK AADC Standard 13 — Nudge Techniques

"Do not use nudge techniques to lead or encourage children to provide unnecessary personal data or weaken or turn off their privacy protections."

### COPPA — Persistent Identifiers and Behavioural Advertising

- **16 CFR 312.2**: Persistent identifiers that can recognise a user over time and across different websites constitute "personal information" under COPPA.
- Using persistent identifiers to serve behavioural advertising to children requires verifiable parental consent.
- **Support for internal operations exception**: Contextual advertising, frequency capping, and security are permitted without consent; behavioural targeting is NOT.

## Regulatory Guidance

### EDPB Guidelines on Automated Individual Decision-Making and Profiling (WP251rev.01, Adopted 6 February 2018)

- **Section IV.B**: "As a general rule, [...] the controller should not rely on the exceptions in Article 22(2) to justify profiling concerning a child."
- **Paragraph 29**: "The GDPR emphasises that children merit specific protection and this is especially relevant where children's data is used for profiling, particularly for marketing purposes."
- **Paragraph 75**: Suitable safeguards for automated decisions must include: transparency about the logic involved, human intervention, the right to express a point of view, and the right to contest the decision.

### ICO Guidance on Profiling and Children (AADC Interpretation)

The ICO clarifies that "profiling" in AADC Standard 12 includes:
- Recommendation algorithms that use personal data about the child's preferences or behaviour
- Personalisation engines that adapt content based on interaction history
- Engagement optimisation algorithms designed to maximise time on platform
- Advertising targeting systems that use personal data for ad selection

The ICO does NOT consider the following to be "profiling" under the AADC:
- Content-based filtering (recommendations based on the content characteristics, not the user)
- Age-based content filtering (using age to exclude inappropriate content)
- Contextual advertising (ads based on page content, not user profile)
- Aggregate analytics (anonymised, group-level analysis with no individual evaluation)

### European Commission Communication on Better Internet for Kids (BIK+, 2022)

- Recommends that digital services providers limit profiling of children.
- Calls for industry codes of conduct addressing algorithmic amplification of harmful content to children.
- Supports age-appropriate design standards including profiling restrictions.

## Enforcement Decisions

- **TikTok (DPC Ireland, 2023)**: EUR 345 million fine. The DPC found that TikTok's "For You" algorithmic recommendation system profiled children to serve content, without adequate safeguards against harmful content amplification. The DPC specifically addressed the profiling of children under GDPR Art. 5(1)(a), 5(1)(c), and Art. 25.
- **Instagram/Meta (DPC Ireland, 2022)**: EUR 405 million fine. Meta failed to restrict profiling and public exposure of children's data, including allowing children aged 13-17 to operate business accounts that were profiled for commercial purposes.
- **Google/YouTube (FTC, 2019)**: USD 170 million. Google used persistent identifiers to track children's viewing behaviour across child-directed YouTube channels and served behaviourally targeted advertising based on those profiles.
- **TikTok (CNIL, 2022)**: EUR 5 million. CNIL found that TikTok made it difficult for users (including children) to refuse tracking cookies that enable profiling, constituting a nudge technique.
- **Epic Games/Fortnite (FTC, 2022)**: USD 275 million for dark patterns and design choices that exploited children, including engagement-maximising features designed around profiling.

## Research and Evidence

### UK Parliament — Impact of Social Media on Young People's Mental Health (2019)

- Evidence that algorithmic recommendation systems can amplify harmful content exposure for children.
- Social media platforms' engagement-optimisation profiling was identified as a contributing factor in children's mental health deterioration.
- Recommended legislative restrictions on profiling of children.

### EU Joint Research Centre — Impact of Recommender Systems on Children (2022)

- Found that recommendation algorithms on major platforms can create "filter bubbles" and content rabbit holes for children.
- Children's developmental stage makes them more susceptible to algorithmic influence than adults.
- Recommended content diversity injection, time limits, and age-appropriate recommendation safeguards.

### Surgeon General's Advisory on Social Media and Youth Mental Health (US, 2023)

- Highlighted the role of algorithmic content curation in exacerbating mental health risks for children.
- Recommended that platforms disable engagement-maximising features for children under 18.
- Called for transparency about algorithmic systems affecting children.
