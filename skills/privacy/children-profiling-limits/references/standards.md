# Standards and Regulatory References — Children's Profiling Limits

## Primary Legislation

### GDPR Article 4(4) — Definition of Profiling

"'Profiling' means any form of automated processing of personal data consisting of the use of personal data to evaluate certain personal aspects relating to a natural person, in particular to analyse or predict aspects concerning that natural person's performance at work, economic situation, health, personal preferences, interests, reliability, behaviour, location or movements."

### GDPR Article 22 — Automated Individual Decision-Making, Including Profiling

- **Art. 22(1)**: "The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her."
- **Art. 22(2)**: Exceptions: (a) necessary for entering into/performing a contract; (b) authorised by law; (c) based on explicit consent.
- **Art. 22(3)**: Where exceptions apply, suitable measures must be in place to safeguard rights and freedoms, including human intervention.
- **Art. 22(4)**: Decisions under Art. 22(2) must not be based on special category data (Art. 9) unless Art. 9(2)(a) or (g) applies.

### GDPR Recital 71 — Children and Profiling

"In order to ensure fair and transparent processing in respect of the data subject [...] the controller should use appropriate mathematical or statistical procedures for the profiling, implement technical and organisational measures appropriate to ensure, in particular, that factors which result in inaccuracies in personal data are corrected and the risk of errors is minimised [...] in a manner that prevents, inter alia, discriminatory effects on natural persons on the basis of racial or ethnic origin, political opinion, religion or beliefs, trade union membership, genetic or health status or sexual orientation, or that result in measures having such an effect. Automated decision-making and profiling based on special categories of personal data should be allowed only under specific conditions. **In any case, such processing should be subject to suitable safeguards, which should include specific information to the data subject and the right to obtain human intervention, to express his or her point of view, to obtain an explanation of the decision reached after such assessment and to challenge the decision. Such measure should not concern a child.**"

### EU Digital Services Act — Article 28(2)

"Providers of online platforms shall not present advertisements on their interface based on profiling as defined in Article 4, point (4), of Regulation (EU) 2016/679, using personal data of the recipient of the service when they are aware with reasonable certainty that the recipient of the service is a minor."

### UK AADC Standard 12 — Profiling

"Switch options which use profiling off by default (unless you can demonstrate a compelling reason for profiling to be on by default, taking account of the best interests of the child). Only allow profiling if you have appropriate measures in place to protect the child from any harmful effects (including but not limited to feeding the child content that is detrimental to their health or wellbeing)."

### UK AADC Standard 5 — Detrimental Use of Data

"Do not use children's personal data in ways that have been shown to be detrimental to their wellbeing, or that go against industry codes of practice, other regulatory provisions or Government advice."

### UK AADC Standard 13 — Nudge Techniques

"Do not use nudge techniques to lead or encourage children to provide unnecessary personal data or weaken or turn off their privacy protections."

### COPPA — Persistent Identifiers for Behavioural Advertising

- 16 CFR 312.2: Persistent identifiers constitute "personal information" when used for purposes beyond support for internal operations.
- Using persistent identifiers to serve targeted advertising to children requires verifiable parental consent.
- The 2013 amendments expanded the scope to capture behavioural advertising targeting of children.

## EDPB Guidance

### EDPB Guidelines on Automated Individual Decision-Making and Profiling (WP251rev.01, Adopted 3 October 2017, Revised 6 February 2018)

- **Section IV.B**: Profiling of children — "In general, organisations should not rely solely on automated decision-making (including profiling) to make decisions about children because: they may be less able to understand the implications of their actions; they may be less able to make informed decisions about the processing; and such decisions may have lifelong consequences."
- **Paragraph 71**: The EDPB interprets Recital 71's statement "such measure should not concern a child" as a strong presumption against profiling of children for decisions with legal or significant effects.
- **Paragraph 72**: Controllers relying on Art. 22(2) exceptions for children must demonstrate that the exception is strictly necessary and that additional safeguards are in place beyond those required for adults.

### EDPB Guidelines 05/2020 on Consent

- Paragraph 133-135: Consent for profiling of children must be parental consent (under Art. 8) and must be specific to the profiling purpose.

## National Guidance

### ICO AADC Standard 12 — Detailed Guidance

The ICO specifies:
- **Default off**: All profiling features must be switched off by default for child users. This includes recommendation algorithms, content personalisation based on behaviour, and any form of user categorisation.
- **Compelling reason exception**: The controller must demonstrate that profiling is in the child's best interests, not merely commercially beneficial. Educational adaptive learning may qualify; advertising targeting does not.
- **Protective measures**: Where profiling is enabled, the controller must implement: content diversity to prevent filter bubbles, time limits on algorithmic feeds, mental health safeguards, and human review capability.
- **Annual impact assessment**: Controllers must conduct annual assessments of the impact of profiling on children's wellbeing.

### CNIL Guidance on Profiling and Targeted Advertising (2022)

- CNIL has stated that behavioural advertising targeting children is "extremely difficult to justify" under GDPR.
- Controllers must not use dark patterns or nudge techniques to obtain consent for profiling.
- CNIL recommends contextual advertising (based on page content, not user profile) as the alternative for services with child users.

## DSA Implementation

### European Commission Guidelines on DSA Article 28 (2023)

- "Minor" defined as any person under 18.
- "Aware with reasonable certainty" includes: age declared by user, age inferred from content engagement, age estimated by technology, or age known from other sources.
- The prohibition covers: behavioural advertising, retargeting, lookalike audiences based on minors' data, and any ad targeting using personal data profiles of minors.
- Contextual advertising (based on page content, not user profile) is not prohibited.

## Enforcement Decisions

- **TikTok (DPC Ireland, 2023)**: EUR 345 million. TikTok's "For You" algorithmic feed profiled children to serve content without adequate safeguards. Default public profiles exposed children's content. Violated Art. 5(1)(a), 5(1)(c), 12, 13, 24, and 25.
- **Instagram/Meta (DPC Ireland, 2022)**: EUR 405 million. Instagram failed to restrict profiling of children on business accounts with public-by-default settings. Violated Art. 5(1)(c), 12, 13, 24, 25, and 35.
- **YouTube/Google (FTC, 2019)**: USD 170 million. Google used persistent identifiers (cookies) to track children's viewing behaviour on child-directed channels for behavioural advertising.
- **TikTok (CNIL, 2022)**: EUR 5 million. Cookie consent mechanism made it difficult for users, including children, to refuse tracking — facilitating profiling without genuine consent.
- **Epic Games (FTC, 2022)**: USD 275 million. Design patterns manipulated children into in-app purchases, constituting a form of commercial exploitation through profiling.

## Research

### UK Children's Commissioner Report — "Who Knows What About Me?" (2018)

- Found that by age 13, the average UK child has had 72 million data points collected about them by online services.
- Data includes browsing behaviour, location history, social connections, and purchasing patterns.
- Recommended strict limits on profiling of children and prohibition of behavioural advertising to under-18s.

### 5Rights Foundation — "Pathways: How Digital Design Puts Children at Risk" (2021)

- Documented how recommendation algorithms expose children to harmful content including self-harm, eating disorders, and extreme content.
- Found that profiling-based recommendations can create content "rabbit holes" within minutes of account creation.
- Recommended algorithmic impact assessments mandatory for services accessed by children.
