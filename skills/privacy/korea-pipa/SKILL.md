---
name: korea-pipa
description: >-
  Guides compliance with South Korea's Personal Information Protection Act (PIPA,
  개인정보 보호법). Covers pseudonymisation framework, notification requirements,
  PIPC enforcement, consent standards, and cross-border transfer rules under the
  2023 amendments. Keywords: PIPA, Korea data protection, PIPC, pseudonymisation,
  consent, cross-border transfers.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: global-privacy-regulations
  tags: "pipa, korea-data-protection, pipc, pseudonymisation, cross-border-transfers"
---

# South Korea PIPA Compliance

## Overview

The Personal Information Protection Act (PIPA, 개인정보 보호법) is South Korea's comprehensive data protection law, originally enacted on 29 September 2011 (Act No. 10465) and significantly amended in 2020 (effective 5 August 2020) and 2023 (effective 15 September 2023). The Personal Information Protection Commission (PIPC, 개인정보보호위원회) is the independent supervisory authority with centralised enforcement jurisdiction since the 2020 amendments consolidated regulatory authority from multiple agencies.

South Korea received an adequacy decision from the European Commission on 17 December 2021, recognising PIPA as providing an adequate level of data protection for GDPR transfer purposes.

## Scope and Definitions

### Personal Information (Art. 2(1))
Information relating to a living individual that identifies or can identify the individual through the information alone or in combination with other information that can be easily used. Includes:
- Name, resident registration number, image
- Information that individually does not identify but can identify when combined with other easily accessible information

### Pseudonymised Information (Art. 2(1-2), introduced 2020)
Personal information processed by partially deleting or replacing to make it impossible to identify a specific individual without the use of additional information. Pseudonymised information may be processed for statistical purposes, scientific research, and preservation of records in the public interest without consent (Art. 28-2).

### Sensitive Information (Art. 23)
- Ideology, beliefs, membership of trade unions or political parties
- Political opinions, health information, sex life
- Genetic information, criminal record information
- Biometric information used for identification
- Race and ethnic origin (added by 2023 amendments)

## Consent Framework

### General Consent Requirements

| Requirement | PIPA Provision | Detail |
|-------------|---------------|--------|
| Informed consent | Art. 15(2) | Must disclose: purpose, items collected, retention period, right to refuse and consequences |
| Separate consent | Art. 22(1) | Consent for processing beyond the purpose must be separated from other consent items |
| Clear distinction | Art. 22(1) | Important content must be clearly displayed (larger font, colour, bold) |
| Opt-in for marketing | Art. 22(2) | Marketing purpose collection requires separate opt-in consent |
| Refusal right | Art. 22(5) | Data handler must not refuse service due to refusal of consent for non-essential information |
| Minor consent | Art. 22(6) | For children under 14, consent from legal representative required |

### Consent for Sensitive Information (Art. 23)
Processing sensitive information requires the data subject's separate explicit consent or a specific legal basis. The consent must clearly indicate the sensitive categories being processed.

### 2023 Amendment: Consent Alternatives (Art. 15(1))

The 2023 amendments introduced additional lawful processing bases beyond consent:

| Basis | Article | Description |
|-------|---------|-------------|
| Consent | Art. 15(1)(1) | Data subject's consent obtained per Art. 22 |
| Legal obligation | Art. 15(1)(2) | Special provisions in laws or compliance with legal obligations |
| Public institution duty | Art. 15(1)(3) | Necessary for public institutions to perform statutory duties |
| Contract performance | Art. 15(1)(4) | Necessary for contract with data subject |
| Legitimate interest | Art. 15(1)(6) | Necessary for legitimate interest of the data handler, where substantially related to the purpose and within the data subject's reasonable expectations (added 2023) |
| Urgent necessity | Art. 15(1)(5) | Urgently necessary for life, body, or property of the data subject or third party |

**Legitimate interest (Art. 15(1)(6)) requirements**:
- Reasonably related to the interest of the data handler
- Substantially related to the original collection purpose
- Within the reasonable expectations of the data subject
- Data handler must document the legitimate interest assessment
- The PIPC may issue further guidance on the scope and application

## Pseudonymisation Framework (Arts. 28-2 to 28-7)

### Permitted Uses of Pseudonymised Information (Art. 28-2)
Pseudonymised information may be processed without consent for:
1. Statistical purposes
2. Scientific research (including industrial research)
3. Preservation of records in the public interest

### Combination of Pseudonymised Information (Art. 28-3)
- Combination of pseudonymised information held by different data handlers must be performed by an entity designated by the PIPC
- The designated entity must apply additional pseudonymisation or anonymisation before providing the combined data to the requesting handler
- The combination must receive prior PIPC approval

### Safety Measures for Pseudonymised Information (Art. 28-4)
| Measure | Requirement |
|---------|-------------|
| Separation of additional information | Additional information enabling re-identification must be stored and managed separately |
| Technical safeguards | Encryption or equivalent protection for additional information |
| Access restrictions | Designation of authorised personnel; access logging |
| Prohibition on re-identification | Prohibited from using pseudonymised information to re-identify individuals; if re-identification occurs accidentally, immediate destruction or cessation of processing required |

### Zenith Global Enterprises Pseudonymisation Register

| Data Set | Purpose | Pseudonymisation Method | Additional Information Storage | PIPC Compliance |
|----------|---------|------------------------|-------------------------------|-----------------|
| Customer shipping patterns | Statistical analysis of route optimisation | k-anonymity (k=5) with generalisation of location data | Key mapping table stored in HSM, separate from analytics environment | Compliant |
| Employee performance metrics | Industrial research on workforce productivity | Tokenisation of employee identifiers | Token-identifier mapping in isolated database with MFA access | Compliant |
| Logistics volume trends | Public interest statistical reporting | Aggregation to postal code level with suppression of groups < 10 | No additional information retained (anonymised output) | Not applicable (anonymised) |

## Cross-Border Transfer Rules

### Transfer Mechanisms (Art. 28-8, as amended 2023)

The 2023 amendments significantly reformed cross-border transfer provisions:

| Mechanism | Article | Detail |
|-----------|---------|--------|
| Consent | Art. 28-8(1)(1) | Data subject's consent with disclosure of: recipient, destination country, transfer purpose, PI items, right to refuse and consequences |
| Contract necessity | Art. 28-8(1)(2) | Transfer necessary for contract with data subject |
| Adequacy recognition | Art. 28-8(1)(3) | Transfer to a country or international organisation recognised by the PIPC as having adequate protection |
| Standard contractual clauses | Art. 28-8(1)(4) | PIPC-approved standard contractual clauses between the parties |
| BCR equivalent | Art. 28-8(1)(4) | PIPC-approved data protection rules within a corporate group |
| PIPC certification | Art. 28-8(1)(5) | Recipient certified by a PIPC-designated certification body |

### PIPC Adequacy Recognitions
As of March 2026, the PIPC has recognised:
- European Union / EEA (reciprocal with EU adequacy decision of December 2021)
- United Kingdom (recognised 2022)

### Notification Requirements for Cross-Border Transfer (Art. 28-8(3))
The data handler must notify the data subject of:
- The recipient's identity
- The destination country
- The items of personal information transferred
- The purpose of transfer
- The retention and use period
- The right to refuse and consequences of refusal

**Zenith Global Enterprises Cross-Border Transfer Register**:

| Transfer ID | Flow | Destination | Mechanism | Notification | Status |
|------------|------|-------------|-----------|-------------|--------|
| CBT-KR-001 | Customer data → EU HQ | Germany (EU) | Adequacy recognition | Privacy notice updated | Active |
| CBT-KR-002 | Employee data → Regional HR | Singapore | Standard contractual clauses | Employee notice provided | Active |
| CBT-KR-003 | Logistics data → APAC ops | Japan | Consent (Art. 28-8(1)(1)) | Consent collected | Active |
| CBT-KR-004 | Payment data → Treasury | United Kingdom | Adequacy recognition | Privacy notice updated | Active |

## PIPC Enforcement

### Administrative Penalties

| Sanction Type | PIPA Provision | Detail |
|---------------|---------------|--------|
| Corrective orders | Art. 64 | Orders to cease violations, take corrective measures, or implement safeguards |
| Administrative fines (과태료) | Art. 75 | Up to KRW 50 million for procedural violations |
| Penalty surcharges (과징금) | Art. 64-2 | Up to 3% of related revenue (increased from prior cap by 2023 amendments) |
| Criminal penalties | Art. 71-73 | Imprisonment up to 5 years or fine up to KRW 50 million for serious violations |
| Public naming | Art. 64(4) | Public disclosure of violators |

### Notable PIPC Enforcement Actions

**Meta Platforms (September 2022)**:
- Fine: KRW 30.8 billion (approximately USD 22 million)
- Violations: Collecting and using sensitive information (political views, sexual orientation, religious beliefs) without proper consent from approximately 3.3 million Korean Facebook users
- Significance: Demonstrated PIPC willingness to impose significant fines on global technology companies

**Kakao (2023)**:
- Fine: KRW 15.1 billion
- Violations: Collection and use of personal information beyond consented purposes in advertising services
- Significance: Largest enforcement action against a domestic technology company

**Scatter Lab (2021)**:
- Fine: KRW 103 million
- Violations: AI chatbot (Lee Luda) trained on personal conversations without consent
- Significance: Established PIPC precedent for AI training data compliance under PIPA

## Data Subject Rights

| Right | Article | Response Deadline | Implementation |
|-------|---------|-------------------|----------------|
| Right to access | Art. 35 | 10 days | Self-service portal in Korean |
| Right to correction/deletion | Art. 36 | 10 days | Correction through customer portal; deletion workflow with legal hold check |
| Right to suspension | Art. 37 | 10 days | Processing suspension within 10 days of request |
| Right to notification | Art. 34 | Without delay | Breach notification to affected individuals |
| Right to data portability | Art. 35-2 (2023) | Per PIPC regulation | Structured export (implementation timeline per PIPC guidance) |
| Right regarding automated decisions | Art. 37-2 (2023) | Per PIPC regulation | Right to explanation and refusal of automated decisions |

## Breach Notification (Art. 34)

| Element | Requirement |
|---------|-------------|
| Individual notification | Without delay upon discovery of breach |
| PIPC notification | Within 72 hours of discovery for breaches affecting 1,000+ individuals |
| Content | Facts of breach, items of PI leaked, countermeasures, grievance procedures |
| Large-scale breach | 10,000+ individuals: additional reporting to PIPC and public notification through the website |
| Investigation cooperation | Cooperate fully with PIPC investigation |

## Compliance Programme

| Component | Detail |
|-----------|--------|
| Internal management plan | Documented plan per Art. 29 and Enforcement Decree Art. 30 |
| Chief Privacy Officer (CPO) | Designated officer meeting PIPA qualifications (Art. 31) |
| Annual training | PIPA compliance training for all Korean employees |
| Technical safeguards | Encryption of resident registration numbers and sensitive data (Art. 24-2) |
| Data destruction | Destruction within 5 days of retention period expiry (Art. 21) |
| Privacy impact assessment | Required for public institutions; recommended for private sector for large-scale processing |
