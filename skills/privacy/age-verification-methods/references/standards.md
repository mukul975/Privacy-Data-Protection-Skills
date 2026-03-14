# Standards and Regulatory References — Age Verification Methods

## Primary Legislation

### GDPR Article 8(2) — Verification Obligation

"The controller shall make reasonable efforts to verify in such cases that consent is given or authorised by the holder of parental responsibility over the child, taking into consideration available technology."

### UK Online Safety Act 2023

- **Section 11(3)**: Providers of regulated user-to-user services must use proportionate systems or processes designed to prevent children from encountering primary priority content harmful to children.
- **Section 37**: Age verification and age estimation — Ofcom may recommend age verification as a measure in codes of practice.
- **Section 231**: Definitions including "age assurance," "age verification," and "age estimation."

### EU Digital Services Act (Regulation (EU) 2022/2065) — Article 28

- **Art. 28(1)**: Providers of online platforms accessible to minors shall put in place appropriate and proportionate measures to ensure a high level of privacy, safety, and security of minors on their service.
- **Art. 28(2)**: Prohibits targeted advertising based on profiling using personal data of minors.

### France — Loi SREN (Loi visant a securiser et reguler l'espace numerique, 2024)

- Requires age verification for pornographic websites.
- CNIL approved a reference system requiring "double-blind" architecture: the identity verification provider cannot know which site the user accesses; the content provider cannot identify the user.
- Certified technical solutions must verify age without identifying the user to the content provider.

### EU eIDAS 2.0 Regulation (Regulation (EU) 2024/1183, amending Regulation (EU) No 910/2014)

- Mandates EU Digital Identity Wallets available to all EU citizens by 2026.
- Supports selective attribute disclosure: users can prove they are over a specific age without revealing full identity or date of birth.
- Establishes trust framework for qualified trust service providers offering identity attribute attestation.

## Regulatory Guidance

### ICO Opinion: Guidance for Age Assurance (November 2021, Updated 2023)

Key positions:
- Age assurance is not optional — services likely to be accessed by children must take steps to recognise child users.
- The level of certainty required is proportionate to the risk: higher risks to children require more robust age assurance.
- Self-declaration alone is insufficient for medium and high-risk services.
- Facial age estimation that processes on-device, does not store images, and does not identify the user can be proportionate.
- The ICO endorses a "layered" approach: self-declaration as first filter, with escalation to more robust methods as risk increases.

### ICO-OAIC Joint Audit of Yoti Age Estimation (2022)

- Joint audit by the UK Information Commissioner and the Australian Information Commissioner.
- Assessed Yoti's facial age estimation technology for accuracy and data protection compliance.
- Findings: Mean Absolute Error of 1.52 years for 13-17 age group; images processed on-device; no images stored server-side.
- Conclusion: Technology meets data protection requirements when implemented with appropriate safeguards.
- Recommendations: continued improvement of accuracy across demographic groups; regular bias audits.

### Ofcom Age Verification Guidance (UK Online Safety Act Implementation, 2024)

- Ofcom's codes of practice for the Online Safety Act specify age verification as a "highly effective" measure for preventing children's access to pornographic content.
- For other harmful content: age estimation technologies recommended as proportionate measures.
- Ofcom endorses the use of Open Banking, digital identity, mobile network operator verification, and facial age estimation.

### CNIL Age Verification Reference System (2024)

- CNIL published a reference system for age verification of users accessing adult content.
- Requires "double-blind" architecture separating identity verification from content access.
- The identity provider attests age without disclosing identity to the content provider.
- The content provider knows the user is over 18 but cannot identify them.
- Certified technical solutions must comply with GDPR data minimisation and purpose limitation.

## Technical Standards

### ISO/IEC 27566 — Age Assurance Systems (Under Development)

- Working draft standard from ISO/IEC JTC 1/SC 27.
- Covers age verification, age estimation, and age inference methods.
- Addresses accuracy requirements, privacy protection, accessibility, bias mitigation, and interoperability.
- Expected to provide a certification framework for age assurance providers.

### IEEE 2089.1-2024 — Age-Appropriate Digital Services Framework

- Published standard providing a framework for implementing age-appropriate design in digital services.
- Section 6 addresses age assurance: methods, accuracy requirements, and privacy-preserving implementation.
- Recommends risk-based approach to selecting age assurance methods.

### ETSI TS 119 461 — Policy and Security Requirements for Trust Service Components Providing Identity Proofing

- Specifies requirements for electronic identity verification services.
- Applicable to age verification services that use identity documents for age confirmation.
- Defines assurance levels for identity proofing aligned with eIDAS.

### UK Digital Identity and Attributes Trust Framework (DIATF)

- Published by the Department for Science, Innovation and Technology (DSIT).
- Provides a certification framework for digital identity and attribute service providers.
- Age verification providers can be certified under the DIATF to provide trusted age attributes.
- Certified providers must meet specific accuracy, privacy, security, and accessibility requirements.

### ICAO Doc 9303 — Machine Readable Travel Documents

- Specifies the format and security features of machine-readable passports and ID cards.
- Part 10: Logical Data Structure for storage of biometrics on contactless ICs (NFC chips).
- Relevant to document-based age verification systems that read passport NFC chips.

## Research and Evidence

### Ofcom Online Nation Report (2023)

- Found that 33% of UK children aged 8-17 have social media profiles despite being below the platform's stated minimum age.
- 16% of 3-4 year olds and 38% of 5-7 year olds have their own profiles on social media platforms.
- Evidence that self-declaration age gates are widely circumvented by children.

### 5Rights Foundation — "But How Do They Know It Is a Child?" (2021)

- Research report on age assurance methods and their effectiveness.
- Concluded that no single method is perfect; layered approaches are most effective.
- Identified facial age estimation as the most promising proportionate method for general use.
- Noted accessibility concerns with document-based methods (children and adults without ID).

### European Commission Study on Age Verification (2022)

- Comparative study of age verification methods across EU Member States.
- Found significant variation in approach and limited deployment of robust age verification.
- Recommended the EU Digital Identity Wallet as the preferred long-term solution for age verification.
