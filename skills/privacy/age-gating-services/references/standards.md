# Standards and Regulatory References — Age-Gating Services

## Primary Legislation

### GDPR Article 8 — Conditions Applicable to Child's Consent

- **Art. 8(1)**: Requires parental consent for children below the applicable national age threshold (13-16) when consent is the lawful basis for information society services.
- **Art. 8(2)**: Controller must make reasonable efforts to verify age, taking into consideration available technology.

### UK Online Safety Act 2023

- **Section 11(3)**: Providers must use "proportionate systems or processes" to prevent children from encountering primary priority content harmful to children.
- **Section 12(2)-(3)**: Safety duties protecting children include implementing age verification and age estimation where proportionate.
- **Section 37(2)**: Age verification means any measure designed to verify the age of a user. Age estimation means any measure designed to estimate the age or age range of a user.
- **Schedules 6-7**: Lists of primary priority and priority content harmful to children that triggers age-gating obligations.

### EU Digital Services Act — Article 28

- **Art. 28(1)**: Online platforms accessible to minors must implement appropriate measures for child safety.
- **Art. 28(2)**: Platforms must not present advertisements based on profiling using personal data of minors.

### COPPA — 16 CFR Part 312

- **Section 312.2**: Defines "child" as under 13. Services directed to children or with actual knowledge of child users must comply.
- **Section 312.5(c)**: Exceptions to parental consent, including the provision that operators of general audience sites must implement age screens before collecting personal information from children.

### UK Gambling Act 2005

- **Section 46**: Offence for a person under 18 to gamble.
- **Section 47**: Offence to invite, cause or permit a child or young person to gamble.
- Remote gambling operators must implement age verification before gambling services are accessible.

### Audiovisual Media Services Directive (AVMSD) — Directive (EU) 2018/1808

- **Article 6a(1)**: Video-sharing platform providers must take appropriate measures to protect minors from content which may impair their development.
- **Article 28b(1)**: Measures may include age verification systems.

## Regulatory Guidance

### ICO Age Assurance Opinion (2021, Updated 2023)

- Age assurance is mandatory for services likely to be accessed by children.
- Self-declaration age gates must use neutral design that does not reveal the threshold.
- The level of assurance required is proportionate to the risk of the processing.
- Non-neutral age gates (e.g., "Are you 13 or older?") are a compliance risk factor.

### FTC COPPA Guidance on Age Screens

- Age screens must not "encourage the child to enter a false age."
- Non-neutral age gates can establish actual knowledge that the operator is collecting from children.
- The FTC treats a non-neutral age gate that children routinely circumvent as evidence that the operator has actual knowledge of child users (Musical.ly/TikTok enforcement, 2019).

### Ofcom Codes of Practice (UK Online Safety Act, 2024)

- Age verification recommended as "highly effective" for preventing children's access to pornographic content.
- Age estimation recommended as proportionate for broader content categories.
- Service providers must assess the effectiveness of their age-gating measures and demonstrate they work.
- Ofcom expects providers to monitor circumvention rates and improve measures over time.

### CNIL Recommendations on Age Verification (2024)

- Age verification systems must comply with GDPR data minimisation.
- "Double-blind" architecture preferred: identity provider and content provider separated.
- Self-declaration alone is insufficient for age-restricted content.
- CNIL has certified technical solutions for age verification of adult content.

## Technical Standards

### PAS 1296:2018 — Online Age Checking (BSI/DCMS)

- British Standards Institute Published Application Specification for online age checking.
- Defines age verification (definitive check) and age estimation (probabilistic check).
- Specifies accuracy requirements, data protection safeguards, and testing methodologies.
- Recommends that age checking providers publish accuracy data.

### IEEE 2089.1-2024 — Age-Appropriate Digital Services Framework

- Section 6: Age assurance implementation guidance.
- Covers neutral age prompts, circumvention prevention, and re-verification triggers.
- Recommends risk-based approach to selecting age-gating mechanisms.

## Enforcement Decisions

- **Musical.ly/TikTok (FTC, 2019)**: USD 5.7 million. FTC found that Musical.ly's age gate was non-neutral (asked "How old are you?" with the threshold displayed), making it easy for children to circumvent. FTC treated this as evidence of actual knowledge.
- **Epic Games/Fortnite (FTC, 2022)**: USD 275 million. FTC found that Epic's age gate was ineffective and that Epic had actual knowledge of collecting from children despite the age gate.
- **TikTok (ICO, 2023)**: GBP 12.7 million. ICO found that TikTok's age-gating was insufficient to prevent children under 13 from creating accounts.
- **Various pornographic website operators (CNIL/Ofcom, 2023-2024)**: Multiple enforcement actions for failing to implement effective age verification, relying solely on self-declaration checkboxes.

## Research

### Ofcom Online Nation Report (2023)

- 33% of UK children aged 8-17 have social media profiles despite being below the platform's stated minimum age.
- 16% of 3-4 year olds have their own profiles on social media.
- Self-declaration age gates are the most commonly circumvented measure.

### Thorn Digital Defenders Report (2022)

- Survey of 1,000 US children found that 45% of children under 13 were able to bypass age gates on social media platforms.
- Children reported learning circumvention techniques from siblings, friends, and online tutorials.
- Recommended that platforms implement multiple layers of age assurance rather than relying on a single gate.
