---
name: delaware-dppa
description: >-
  Delaware Personal Data Privacy Act (DPPA) compliance implementation.
  Covers consumer rights (access, correct, delete, portability, opt-out),
  controller obligations, processor requirements, sensitive data consent,
  universal opt-out recognition, DPIA requirements, and AG enforcement.
  Effective January 1, 2025, with no revenue threshold for applicability.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "delaware-dppa, delaware-privacy, consumer-rights, sensitive-data, universal-opt-out"
---

# Delaware Personal Data Privacy Act (DPPA)

## Overview

The Delaware Personal Data Privacy Act (DPPA), codified as Title 6, Chapter 12D of the Delaware Code (6 Del. C. §§12D-101 through 12D-111), was signed into law by Governor John Carney on September 11, 2023 (HB 154). The DPPA became effective on January 1, 2025. Delaware is notable for having the lowest applicability threshold of any comprehensive US state privacy law — requiring only that a controller process the personal data of 35,000 Delaware consumers (with no revenue-from-sale threshold) — making it the broadest in scope of the state privacy laws enacted through 2023.

Key distinguishing features of the DPPA:
- **Lowest consumer threshold**: 35,000 consumers (no revenue alternative needed)
- **No cure period**: Unlike many states, the DPPA provides no mandatory cure period; the AG has discretion
- **Broad sensitive data definition**: Includes immigration/citizenship status
- **Universal opt-out recognition**: Required from January 1, 2026
- **Minor protections**: Heightened requirements for known child data processing (under 18)
- **Targeted advertising consent for minors**: Explicit opt-in required for consumers known to be 13-17

## Applicability (§12D-103)

The DPPA applies to persons that conduct business in Delaware or produce products or services targeted to Delaware residents AND during the preceding calendar year either:

1. Controlled or processed personal data of at least **35,000 Delaware consumers** (excluding data processed solely to complete a payment transaction); OR
2. Controlled or processed personal data of at least **10,000 Delaware consumers** AND derived more than **20% of gross revenue** from the sale of personal data.

### Exemptions (§12D-104)

**Entity-level exemptions:**
- State and local government bodies
- Financial institutions subject to GLBA (entity-level)
- HIPAA covered entities and business associates (entity-level)
- Nonprofit organizations
- Institutions of higher education
- National securities exchanges and registered entities under SEC

**Data-level exemptions:**
- HIPAA-governed health data
- GLBA-governed financial data
- FCRA-governed credit data
- FERPA-governed education records
- DPPA (federal) driver data
- Data governed by the Farm Credit Act
- Clinical trial and research data (with conditions)
- Employment data (processed in employment context)
- Business contact data used in B2B context

**Liberty Commerce Inc. Assessment:**
Liberty Commerce Inc. processes personal data of approximately 52,000 Delaware consumers. With 12% of advertising revenue attributable to data sale activities, Liberty Commerce Inc. exceeds threshold (1) and treats itself as fully subject to the DPPA.

## Consumer Rights (§12D-106)

### Six Consumer Rights

1. **Right to Access** (§12D-106(a)(1)): Confirm whether a controller is processing personal data and access that data
2. **Right to Correct** (§12D-106(a)(2)): Correct inaccuracies in personal data
3. **Right to Delete** (§12D-106(a)(3)): Delete personal data provided by or obtained about the consumer
4. **Right to Portability** (§12D-106(a)(4)): Obtain personal data in a portable, readily usable format
5. **Right to Opt Out** (§12D-106(a)(5)): Opt out of:
   - Targeted advertising
   - Sale of personal data
   - Profiling in furtherance of decisions producing legal or similarly significant effects
6. **Right to Appeal** (§12D-106(f)): Appeal any refusal to take action on a rights request within a reasonable period after receiving the refusal

### Response Requirements

| Parameter | Requirement |
|-----------|-------------|
| Response deadline | 45 days from receipt |
| Extension | One additional 45-day extension with notice and reason |
| Denial requirements | Inform consumer of appeal right |
| Appeal response | 60 days; must inform consumer of right to contact AG |
| Cost | Free; no charge for first request per 12 months |
| Verification | Reasonable authentication; cannot require account creation |

### Universal Opt-Out Mechanism (§12D-106(a)(5)(c))

Effective **January 1, 2026**, controllers must recognize universal opt-out preference signals (such as Global Privacy Control). The signal must be treated as a valid opt-out of sale and targeted advertising. Controllers must not interpret the absence of a signal as consent.

## Controller Obligations (§12D-105)

### Privacy Notice Requirements

Controllers must provide a reasonably accessible, clear privacy notice that includes:
- Categories of personal data processed
- Purpose of processing
- How consumers can exercise their rights
- Categories of personal data shared with third parties
- Categories of third parties with whom data is shared
- Active email address or online mechanism for contacting the controller

### Data Minimization

Controllers must limit collection to what is adequate, relevant, and reasonably necessary for the disclosed purpose.

### Security

Controllers must establish, implement, and maintain reasonable administrative, technical, and physical data security practices appropriate to the volume and nature of the personal data at issue.

### Consent for Sensitive Data (§12D-105(a)(4))

Processing of sensitive data requires the consumer's consent. Sensitive data under the DPPA includes:
- Racial or ethnic origin
- Religious beliefs
- Mental or physical health diagnosis
- Sexual orientation
- Citizenship or immigration status
- Genetic or biometric data processed to identify an individual
- Personal data of a known child (under 13)
- Precise geolocation data (within 1,750 feet)

### Minors (§12D-105(a)(5))

- **Under 13**: Must obtain verifiable parental consent (COPPA standards apply)
- **13 to 17**: Must not process data for targeted advertising or sale without opt-in consent from the consumer known to be between 13 and 17

### Data Protection Assessments (§12D-105(b))

Controllers must conduct and document DPIAs for processing activities that present a heightened risk of harm, including:
- Targeted advertising
- Sale of personal data
- Profiling presenting reasonably foreseeable risk of unfair or deceptive treatment, financial/physical/reputational injury, or intrusion on solitude
- Processing sensitive data
- Processing personal data of minors for non-service purposes

## Processor Obligations (§12D-107)

Processors must:
- Adhere to controller instructions
- Assist with consumer rights requests
- Provide information for DPIAs upon request
- Engage sub-processors only with controller authorization and under written contract
- Delete or return personal data at controller direction after service completion
- Make available information for the controller to conduct assessments

Processing contracts must include:
- Instructions for processing
- Nature and purpose of processing
- Data types and consumer categories
- Duration of processing
- Rights and obligations of both parties
- Requirement for sub-processor agreements
- Confidentiality requirements

## Enforcement (§12D-110)

- **Enforcer**: Delaware Department of Justice (Attorney General)
- **Cure period**: None mandated (AG has discretion to allow opportunity to cure)
- **Civil penalties**: Up to $10,000 per violation
- **No private right of action**
- **AG investigative powers**: CID authority, subpoena power, and ability to bring action in Chancery Court

## Comparison With Peer State Laws

| Feature | Delaware DPPA | Connecticut CTDPA | Colorado CPA | Virginia VCDPA |
|---------|--------------|-------------------|--------------|----------------|
| Consumer threshold | 35,000 | 100,000 | 100,000 | 100,000 |
| Revenue alternative | 10,000 + 20% | 25,000 + 25% | 25,000 + revenue | 25,000 + 50% |
| Cure period | None (AG discretion) | 60 days (until Dec 2024) | 60 days (until Jan 2025) | 30 days (until Jan 2025) |
| Universal opt-out | Jan 1, 2026 | Jan 1, 2025 | Jul 1, 2024 | Not required |
| Immigration data sensitive | Yes | No | No | No |
| Minor age threshold | Under 18 | Under 16 | Under 13 | Under 13 |
| Penalty per violation | $10,000 | $5,000 | $20,000 | $7,500 |
