# Standards and Regulatory References — AI Training Data Lawfulness

## Primary Legislation

### GDPR — Lawful Basis Provisions

- **Art. 5(1)(a)**: Lawfulness, fairness, transparency — personal data must be processed lawfully, fairly, and in a transparent manner.
- **Art. 5(1)(b)**: Purpose limitation — data collected for specified, explicit, legitimate purposes and not further processed incompatibly.
- **Art. 5(1)(c)**: Data minimisation — adequate, relevant, and limited to what is necessary.
- **Art. 5(1)(e)**: Storage limitation — kept no longer than necessary for the purposes.
- **Art. 6(1)**: Lawfulness of processing — at least one basis must apply: (a) consent, (b) contract, (c) legal obligation, (d) vital interests, (e) public interest, (f) legitimate interests.
- **Art. 6(4)**: Compatibility assessment for further processing — considers link between purposes, context, nature of data, consequences, safeguards.
- **Art. 7**: Conditions for consent — demonstrable, distinguishable, withdrawable, freely given.
- **Art. 9**: Processing of special categories — prohibited unless Art. 9(2) exception applies.
- **Art. 13-14**: Information to be provided to data subjects — must include purposes, lawful basis, legitimate interests pursued.
- **Art. 21**: Right to object — applies to processing based on Art. 6(1)(e) or (f), including profiling.

### EU AI Act (Regulation (EU) 2024/1689)

- **Art. 10**: Data and data governance — training, validation, and testing data sets must be subject to appropriate data governance and management practices. Data sets must be relevant, sufficiently representative, and to the best extent possible, free of errors and complete.
- **Art. 10(5)**: Allows processing of special category data (Art. 9 GDPR) for bias detection and correction in high-risk AI systems, subject to safeguards.
- **Recital 45**: Clarifies that AI Act data governance requirements are without prejudice to GDPR — lawful basis still required for personal data processing.

### Directive (EU) 2019/790 — Copyright in the Digital Single Market

- **Art. 3**: Text and data mining for scientific research — permits reproduction and extraction for TDM by research organisations and cultural heritage institutions.
- **Art. 4**: General TDM exception — permits TDM where rightholders have not reserved their rights. Note: this addresses copyright, not data protection — GDPR obligations persist independently.

## EDPB and DPA Guidance

### EDPB Guidelines 04/2025 — Processing Personal Data Through AI Models

Core provisions on lawful basis:
- AI model training constitutes processing of personal data when training data contains personal data.
- The controller must identify and document a lawful basis under Art. 6(1) for the training processing operation specifically.
- Legitimate interest requires documented three-part balancing test with heightened scrutiny for large-scale training.
- Web scraping for AI training faces a high bar under legitimate interest — reasonable expectations of data subjects weigh against.
- Consent for AI training must be specific to the training purpose — general terms of service consent is insufficient.
- Purpose limitation applies: training data collected for one purpose cannot be freely repurposed for different AI training without assessment.
- The controller must be able to demonstrate compliance (accountability, Art. 5(2)).

### EDPB Report on ChatGPT Taskforce (2024)

Coordinated enforcement findings:
- OpenAI's initial reliance on contractual necessity (Art. 6(1)(b)) for training was rejected by multiple DPAs.
- Legitimate interest (Art. 6(1)(f)) may be available but requires comprehensive balancing test documentation.
- Consent (Art. 6(1)(a)) is available for specific training uses where obtained validly.
- The accuracy principle (Art. 5(1)(d)) applies to AI model outputs about identifiable persons.
- Right to erasure challenges acknowledged — but controller must demonstrate good faith effort.

### CNIL — AI Action Plan: Recommendations on Training Data (2024)

- Recommends legitimate interest as primary basis for AI training on first-party data with strong safeguards.
- Web scraping: emphasises that public availability does not constitute implicit consent or eliminate GDPR obligations.
- Recommends PII detection and removal from training data as a minimum safeguard.
- Recommends pseudonymisation of training data where feasible.
- Acknowledges that re-consent for existing data used in AI training may be impractical — alternative safeguards expected.

### ICO — Generative AI First Call for Evidence Response (2024)

- Legitimate interest for AI training must account for the reasonable expectations of individuals.
- Purpose limitation assessment required when repurposing existing data for AI training.
- Recommends transparency as a key safeguard — data subjects must be informed about AI training use.
- Risk-based approach: higher-risk AI training requires stronger lawful basis justification.

### Garante (Italy) — OpenAI Measures (2023-2024)

- Ordered identification of lawful basis for all training data categories.
- Required publication of clear privacy information about AI training use.
- Mandated opt-out mechanism for Italian data subjects.
- Required age verification to prevent children's data from entering AI training pipelines.

### Datatilsynet (Norway) — Meta AI Training Decision (2023)

- Temporary ban on processing Norwegian user data for Meta AI training.
- Finding: legitimate interest balancing test was not adequately documented.
- Finding: data subjects were not effectively informed about AI training use.
- Finding: opt-out mechanism was insufficient — too difficult for average users.

## Academic and Industry Standards

### OECD AI Principles (2019, Updated 2024)

- Principle 1.2: AI systems should respect the rule of law, human rights, democratic values, including privacy.
- Principle 1.4: Transparency and responsible disclosure regarding AI systems.
- Principle 2.3: Calls for AI actors to apply risk management and responsible business conduct.

### ISO/IEC 42001:2023 — AI Management System

- Section 6.1.4: Requires identification and assessment of AI risks including privacy risks.
- Section 8.4: Data management requirements for AI systems, including data quality and provenance.
- Annex B: AI risk sources and impacts including privacy impacts from training data.

### Partnership on AI — Responsible Practices for Synthetic Media

- Guidelines on training data sourcing and consent for generative AI.
- Recommends documentation of training data provenance and licensing.

## Enforcement Decisions

- **Garante v. OpenAI (Provvedimento 9870832, 2023)**: Temporary processing ban. No identified lawful basis for ChatGPT training data. Required: identify Art. 6(1) basis, implement transparency, age verification, opt-out.
- **CNIL v. Clearview AI (SAN-2022-019, 2022)**: EUR 20M fine. Scraping public photos for facial recognition training without lawful basis or transparency.
- **Datatilsynet v. Meta (2023)**: Temporary injunction on AI training using Norwegian user data — inadequate legitimate interest documentation.
- **DPC v. Meta (2024)**: Regulatory intervention causing Meta to pause EU AI training — legitimate interest basis under challenge.
- **AEPD v. LaLiga (2019)**: EUR 250K fine for using mobile app microphone access (not AI training per se, but established precedent that innovative technology use requires explicit lawful basis beyond general terms of service).
- **Hamburg DPA v. Clearview AI (2023)**: Order to delete German residents' biometric data from AI training database — no lawful basis for biometric data processing.
