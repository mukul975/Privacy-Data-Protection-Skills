---
name: texas-tdpsa-compliance
description: >-
  Texas Data Privacy and Security Act (TDPSA) compliance. No revenue
  threshold applies to all businesses. Covers data broker registration
  requirements, biometric identifier provisions under CUBI, consumer
  rights, AG enforcement, and 30-day cure period. Effective July 1, 2024.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "tdpsa, texas-privacy, data-broker, biometric, no-revenue-threshold"
---

# Texas Data Privacy and Security Act (TDPSA)

## Overview

The Texas Data Privacy and Security Act (TDPSA), codified as Tex. Bus. & Com. Code §541.001 through §541.203, was signed into law on June 18, 2023 (HB 4), and became effective July 1, 2024. Texas is the largest state by population to enact comprehensive consumer privacy legislation and is notable for having **no revenue threshold** for applicability — the TDPSA applies to any person that conducts business in Texas or produces products or services consumed by Texas residents, regardless of company size.

The TDPSA also interacts with the existing Texas Capture or Use of Biometric Identifier Act (CUBI), Tex. Bus. & Com. Code §503.001, which provides separate biometric data protections.

## Applicability (§541.002)

The TDPSA applies to a person that:
1. Conducts business in Texas or produces a product or service consumed by Texas residents
2. Processes or engages in the sale of personal data
3. Is **not** a small business as defined by the U.S. Small Business Administration (SBA)

**Key feature: No revenue or consumer count threshold.** Unlike California ($25M revenue), Virginia (100,000 consumers), or Colorado (100,000 consumers), the TDPSA applies broadly to any non-small business processing personal data of Texas residents.

**Small business exemption:** Small businesses as defined by SBA size standards are exempt from most provisions but are NOT exempt from the prohibition on selling sensitive data without consent (§541.107(b)).

**Additional exemptions (§541.003):**
- State agencies and political subdivisions
- Financial institutions subject to GLBA (entity-level)
- Covered entities and business associates under HIPAA (entity-level)
- Nonprofit organizations
- Institutions of higher education
- Electric utilities (ERCOT-related)

**Liberty Commerce Inc. Assessment:**
Liberty Commerce Inc. is not an SBA-defined small business (annual revenue: $48M, 320 employees). It conducts business in Texas and processes personal data of Texas residents. The TDPSA applies.

## Consumer Rights (§541.051)

### Five Consumer Rights

1. **Right to Access** (§541.051(1)): Confirm processing and access personal data
2. **Right to Correct** (§541.051(2)): Correct inaccuracies
3. **Right to Delete** (§541.051(3)): Delete personal data
4. **Right to Portability** (§541.051(4)): Obtain data in portable, readily usable format
5. **Right to Opt Out** (§541.051(5)): Opt out of:
   - Targeted advertising
   - Sale of personal data
   - Profiling in furtherance of decisions producing legal or similarly significant effects

### Response Requirements (§541.055)
- Respond within 45 days
- Extension: up to 45 additional days with notice
- At least one free response per 12 months per right
- Appeal process: respond within 60 days

## Sensitive Data (§541.001(29), §541.101(b)(5))

### Categories
1. Racial or ethnic origin
2. Religious beliefs
3. Mental or physical health diagnosis
4. Sexual orientation
5. Citizenship or immigration status
6. Genetic or biometric data processed for identification
7. Personal data of a known child
8. Precise geolocation data

### Consent Requirements
Processing sensitive data requires **opt-in consent**. For small businesses: selling sensitive data without consent is prohibited regardless of SBA size.

## Data Broker Provisions (§541.201-§541.203)

The TDPSA includes specific data broker requirements:

### Definition (§541.201)
A "data broker" is a business entity whose principal source of revenue is derived from collecting, processing, or transferring personal data the entity did not directly collect from consumers.

### Registration Requirement (§541.202)
Data brokers must register with the Texas Secretary of State and pay a registration fee. Registration must include:
- Legal name and primary business address
- Contact information for privacy inquiries
- Description of data collection practices
- Whether the broker has experienced a data breach in the preceding 3 years

### Consumer Rights for Data Brokers (§541.203)
Data brokers must provide:
- Clear and conspicuous disclosure that they are a data broker
- A mechanism for consumers to opt out of data collection
- Instructions for submitting access and deletion requests

**Liberty Commerce Inc. Assessment:**
Liberty Commerce Inc. is not a data broker — its principal revenue derives from e-commerce, not from collecting/processing/transferring personal data. The data broker provisions do not apply.

## Biometric Data: CUBI Interaction

### Texas Capture or Use of Biometric Identifier Act (CUBI) — Tex. Bus. & Com. Code §503.001

CUBI, enacted in 2009, provides additional protections for biometric identifiers:
- Defines biometric identifier: retina or iris scan, fingerprint, voiceprint, record of hand or face geometry
- Requires informed consent before capture
- Prohibits sale, lease, or disclosure without consent
- Requires reasonable care in storage, transmission, and protection
- Requires destruction within a reasonable time (when purpose fulfilled or within 3 years of last interaction)
- No private right of action — AG enforcement only
- Penalties: Up to $25,000 per violation

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. does not capture biometric identifiers from Texas consumers. Device-side biometric authentication (Face ID, fingerprint) processes locally and does not transmit biometric data to Liberty Commerce Inc. servers.

## Controller Obligations (§541.101)

1. **Purpose limitation** (§541.101(a)(1)): Limit processing to adequate, relevant, and reasonably necessary purposes
2. **Data minimization** (§541.101(a)(2)): Do not process beyond what is reasonably necessary
3. **Data security** (§541.101(a)(3)): Appropriate technical and organizational measures
4. **Non-discrimination** (§541.101(a)(4)): No processing in violation of antidiscrimination laws
5. **Sensitive data consent** (§541.101(b)(5)): Obtain consent before processing

### Privacy Notice (§541.101(b))
Must include:
- Categories of personal data processed
- Purposes for processing
- Consumer rights exercise instructions
- Categories shared with third parties
- Categories of third parties
- Contact information

### Data Protection Assessments (§541.103)
Required for:
- Targeted advertising
- Sale of personal data
- Profiling with legal or significant effects
- Sensitive data processing
- High-risk processing activities

## Enforcement (§541.151-§541.155)

### Attorney General Authority
- Exclusive enforcement — no private right of action (except CUBI has AG enforcement only)
- May investigate and bring action under the Deceptive Trade Practices — Consumer Protection Act (Tex. Bus. & Com. Code §17.41 et seq.)

### 30-Day Cure Period (§541.154)
- AG must provide 30-day written notice of alleged violation
- If cured within 30 days and express written statement of cure provided: AG may not bring action
- **Unlike CPRA:** Cure period is permanent, not sunsetting

### Penalties
- Civil penalties up to $7,500 per violation
- Injunctive relief
- Reasonable attorney fees and investigation costs

## Key Regulatory References

- Tex. Bus. & Com. Code §541.001-§541.203 (TDPSA)
- Tex. Bus. & Com. Code §503.001 (CUBI — biometric identifiers)
- Tex. Bus. & Com. Code §17.41 et seq. (DTPA — enforcement framework)
- SBA Size Standards (13 CFR §121.201) — small business determination
- Texas Secretary of State — Data broker registration
