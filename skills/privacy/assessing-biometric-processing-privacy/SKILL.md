---
name: assessing-biometric-processing-privacy
description: >-
  Guides DPIA for biometric processing systems including facial recognition,
  fingerprint, voice, iris, and gait analysis. Covers Art. 9 special category
  requirements, Art. 35(3)(b) mandatory DPIA triggers for large-scale biometric
  processing, and EDPB Guidelines 3/2019 on video surveillance. Keywords:
  biometric, facial recognition, fingerprint, DPIA, Art. 9, special category,
  EDPB Guidelines 3/2019.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "biometric, facial-recognition, fingerprint, dpia, art-9, special-category"
---

# Assessing Biometric Processing Privacy

## Overview

Biometric data is classified as a special category of personal data under GDPR Art. 9(1) when processed for the purpose of uniquely identifying a natural person. Processing biometric data on a large scale triggers a mandatory DPIA under Art. 35(3)(b). This skill provides a comprehensive DPIA methodology for biometric systems including facial recognition, fingerprint identification, voice recognition, iris scanning, vein pattern analysis, and behavioural biometrics (gait, typing patterns, signature dynamics).

## Legal Framework for Biometric Data

### GDPR Definition — Art. 4(14)

"'Biometric data' means personal data resulting from specific technical processing relating to the physical, physiological or behavioural characteristics of a natural person, which allow or confirm the unique identification of that natural person, such as facial images or dactyloscopic data."

### Art. 9(1) — Prohibition on Processing Special Categories

Processing of biometric data for the purpose of uniquely identifying a natural person is prohibited unless one of the Art. 9(2) exemptions applies.

**Critical distinction**: Art. 9 only applies when biometric data is processed "for the purpose of uniquely identifying" a person. A photograph used for illustration purposes is not Art. 9 data; the same photograph processed through facial recognition software to identify the person is Art. 9 data.

### Art. 9(2) Exemptions Applicable to Biometric Processing

| Exemption | Reference | Application to Biometrics |
|-----------|-----------|--------------------------|
| Explicit consent | Art. 9(2)(a) | Employee consent often not freely given due to power imbalance (WP29 Opinion 2/2017). Consumer biometric consent must meet Art. 7 standards. |
| Employment, social security, social protection law | Art. 9(2)(b) | Member State law may authorise biometric processing in the employment context (e.g., biometric access control for high-security areas). |
| Vital interests | Art. 9(2)(c) | Limited to emergency situations where biometric identification is needed to protect someone's life. |
| Substantial public interest | Art. 9(2)(g) | Member State law basis required. May apply to law enforcement biometrics where authorised by specific legislation. |
| Health or social care | Art. 9(2)(h) | Biometric patient identification in healthcare settings. |
| Public health | Art. 9(2)(i) | Biometric contact tracing during health emergencies (subject to proportionality). |
| Archiving, scientific research, statistics | Art. 9(2)(j) | Biometric research (e.g., medical imaging analysis) with Art. 89(1) safeguards. |

### Art. 35(3)(b) — Mandatory DPIA Trigger

Processing on a large scale of special categories of data referred to in Art. 9(1), including biometric data processed for unique identification, requires a DPIA. "Large scale" factors per WP248rev.01:
- Number of data subjects (in absolute terms or as a proportion of the relevant population)
- Volume of data and/or range of data items
- Duration or permanence of the processing
- Geographic scope

### EDPB Guidelines 3/2019 on Video Surveillance

Key provisions relevant to facial recognition CCTV:
- Facial recognition in public spaces generally constitutes systematic monitoring of publicly accessible areas (Art. 35(3)(c)) in addition to large-scale biometric processing (Art. 35(3)(b)).
- Facial recognition for access control is less intrusive than identification in public spaces but still requires DPIA.
- Purpose limitation: biometric templates created for access control must not be repurposed for attendance monitoring or performance management.
- Storage limitation: biometric templates should be stored on a device controlled by the data subject (e.g., access card) rather than a central database where possible.

## Biometric System Types and Risk Assessment

### Verification (1:1 Matching)

One-to-one comparison of a live biometric sample against a stored template for the claimed identity. Used for access control, device unlock, payment authentication.

| Risk Factor | Assessment |
|-------------|-----------|
| Data subjects | Defined, enrolled individuals |
| Volume of data | Limited to enrolled population |
| Proportionality | Generally more proportionate than identification |
| Storage recommendation | Template stored on user's device or card (decentralised) |
| Art. 35(3)(b) trigger | Depends on scale of enrolled population |

### Identification (1:N Matching)

One-to-many comparison of a live biometric sample against a database of templates to determine identity. Used for law enforcement, border control, surveillance.

| Risk Factor | Assessment |
|-------------|-----------|
| Data subjects | Potentially unlimited (all persons in the capture area) |
| Volume of data | Can be very large (entire population databases) |
| Proportionality | Highly intrusive; requires strong justification |
| Storage recommendation | Centralised database is typically required for 1:N matching |
| Art. 35(3)(b) trigger | Almost always triggered |

### Categorisation

Classification of individuals into groups based on biometric characteristics (age, gender, ethnicity, emotion) without uniquely identifying them. Used for analytics, targeted advertising, audience measurement.

| Risk Factor | Assessment |
|-------------|-----------|
| Art. 9 applicability | May not fall under Art. 9 if not used for unique identification, but still high risk |
| AI Act classification | Emotion recognition in workplace/education prohibited (Art. 5(1)(f)) |
| Discrimination risk | Categorisation by race, ethnicity, or emotion raises equality law concerns |

## DPIA Content for Biometric Systems

### Systematic Description

For biometric systems, the Art. 35(7)(a) systematic description must include:

| Element | Required Detail |
|---------|----------------|
| Biometric modality | Facial, fingerprint, iris, voice, vein, gait, or multi-modal |
| Processing mode | Verification (1:1) or identification (1:N) or categorisation |
| Capture environment | Controlled (sensor/scanner) or uncontrolled (CCTV, ambient camera) |
| Template storage | Centralised database, decentralised (user device/card), or encrypted enclave |
| Template format | Proprietary template, ISO 19794 standard, or raw biometric data |
| Matching algorithm | Vendor algorithm (specify), open-source algorithm, or custom development |
| Accuracy metrics | False Acceptance Rate (FAR), False Rejection Rate (FRR), Equal Error Rate (EER) |
| Liveness detection | Anti-spoofing measures (presentation attack detection) |
| Fallback mechanism | Alternative identification method when biometric fails |
| Retention period | Template retention, raw biometric data retention, audit log retention |

### Necessity and Proportionality for Biometric Processing

The proportionality assessment for biometric systems must be rigorous because biometric data:
- Is permanent (unlike passwords, biometric characteristics cannot be changed if compromised)
- Is uniquely identifying (biometric data is inherently linked to the individual)
- Creates heightened risk of function creep (biometric templates can be repurposed)
- Has disproportionate impact if breached (biometric data cannot be reissued)

| Proportionality Question | Assessment Standard |
|--------------------------|-------------------|
| Is biometric processing necessary, or can a non-biometric alternative achieve the same purpose? | Badge/card access, PIN, password, or multi-factor authentication without biometrics |
| Is the biometric modality the least intrusive option? | Fingerprint is generally less intrusive than facial recognition; on-device verification less intrusive than centralised identification |
| Is the scale of biometric processing proportionate? | Processing all persons in an area (identification) is less proportionate than processing enrolled volunteers (verification) |
| Is the retention of biometric data minimised? | On-card template storage preferred over centralised database; raw biometric images should not be retained after template extraction |

## Risk Register for Biometric DPIA

### Common Biometric Processing Risks

| Risk ID | Risk | Likelihood | Severity | Typical Level |
|---------|------|-----------|----------|--------------|
| BIO-R1 | Biometric data breach — templates or raw data exposed to unauthorised parties | Possible | Maximum | Very High |
| BIO-R2 | Function creep — biometric data collected for access control repurposed for surveillance or attendance monitoring | Likely | Significant | High |
| BIO-R3 | Discriminatory accuracy — facial recognition performs worse on certain demographic groups (skin colour, age, gender) | Likely | Significant | High |
| BIO-R4 | False rejection denying legitimate access — disabled individuals, elderly, or those with skin conditions experience higher rejection rates | Possible | Significant | High |
| BIO-R5 | Spoofing or presentation attacks — fraudulent biometric samples (photos, masks, artificial fingerprints) bypass security | Possible | Significant | High |
| BIO-R6 | Chilling effect — knowledge of biometric surveillance alters behaviour in public or workplace spaces | Likely | Limited | High |
| BIO-R7 | Irreversibility — unlike passwords, compromised biometric data cannot be changed or reissued | Almost certain | Maximum | Very High |
| BIO-R8 | Third-party capture — biometric data of non-enrolled individuals incidentally captured by the system | Likely | Limited | High |

## Mitigation Measures for Biometric Processing

| Measure | Type | Risk Addressed |
|---------|------|---------------|
| On-device or on-card template storage (no centralised database) | Technical (DPbD) | BIO-R1, BIO-R7 |
| Template protection: cancellable biometrics or biometric encryption (BioHashing, fuzzy vault) | Technical | BIO-R1, BIO-R7 |
| Liveness detection / presentation attack detection (ISO 30107 compliance) | Technical | BIO-R5 |
| Purpose limitation enforcement through technical access controls | Technical + Organisational | BIO-R2 |
| Demographic accuracy testing across skin colour, age, gender groups (NIST FRVT benchmarks) | Technical | BIO-R3 |
| Non-biometric fallback mechanism (PIN, card, helpdesk override) | Organisational | BIO-R4 |
| Signage and transparency notices in capture areas | Organisational (Transparency) | BIO-R6, BIO-R8 |
| Automatic deletion of raw biometric images after template extraction | Technical (Data minimisation) | BIO-R1 |
| Regular penetration testing of biometric system | Technical (Security) | BIO-R5 |

## Enforcement Precedents

- **CNIL vs Clearview AI (2022)**: EUR 20 million fine for mass collection of facial images from internet for biometric identification database without consent, transparency, or DPIA.
- **ICO vs Clearview AI (2022)**: GBP 7.5 million fine for same biometric processing; enforcement notice ordering deletion of UK residents' biometric data.
- **Swedish DPA vs Skelleftea Municipality (2019)**: SEK 200,000 fine for school using facial recognition for student attendance tracking. Consent relied upon was not freely given due to power imbalance. Less intrusive alternatives were available.
- **ICO vs Serco Leisure (2022)**: Enforcement notice for requiring employees to use facial recognition for time and attendance at leisure centres. No DPIA conducted; no less intrusive alternative offered.
- **CNIL vs Clearview AI (2023)**: EUR 5.2 million additional penalty for non-compliance with the 2022 order, demonstrating the consequences of continued biometric processing in violation of enforcement.
- **French Conseil d'Etat vs Presto (2020)**: Upheld CNIL enforcement against biometric time-and-attendance system for employees; found that fingerprint scanning for attendance was disproportionate when badge systems were available.
- **Italian Garante vs P&G (Gillette) (2022)**: Enforcement action against automated age estimation system using facial analysis in retail stores without DPIA and without valid consent.
