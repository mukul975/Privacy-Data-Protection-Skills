---
name: vcdpa-compliance
description: >-
  Virginia Consumer Data Protection Act (VCDPA) compliance implementation.
  Covers 5 consumer rights, controller obligations, processor requirements,
  opt-in for sensitive data, data protection impact assessments, AG
  enforcement, and cure period provisions. Effective January 1, 2023.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "vcdpa, virginia-privacy, consumer-rights, dpia, ag-enforcement"
---

# Virginia Consumer Data Protection Act (VCDPA)

## Overview

The Virginia Consumer Data Protection Act (VCDPA), codified as Va. Code §59.1-575 through §59.1-585, was signed into law on March 2, 2021, and became effective on January 1, 2023. Virginia was the second state to enact comprehensive consumer privacy legislation after California. The VCDPA follows the controller-processor model used in the GDPR rather than the business-service provider framework of the CCPA.

The VCDPA is enforced exclusively by the Virginia Attorney General — there is no private right of action and no dedicated privacy enforcement agency. The AG must provide a 30-day cure period before initiating enforcement action under §59.1-584.

## Applicability (§59.1-576)

The VCDPA applies to persons that conduct business in Virginia or produce products or services targeted to Virginia residents AND:

1. During a calendar year, control or process personal data of at least 100,000 Virginia consumers; OR
2. Control or process personal data of at least 25,000 Virginia consumers AND derive over 50% of gross revenue from the sale of personal data.

**Exemptions (§59.1-576(B)):**
- Virginia governmental entities
- Financial institutions subject to GLBA (Title V of Gramm-Leach-Bliley Act, 15 U.S.C. §6801 et seq.)
- Covered entities and business associates under HIPAA (42 U.S.C. §1320d et seq.)
- Nonprofit organizations
- Institutions of higher education
- Data subject to GLBA, HIPAA, FERPA, FCRA, DPPA, or Farm Credit Act

**Liberty Commerce Inc. Assessment:**
Liberty Commerce Inc. processes personal data of approximately 145,000 Virginia consumers through its e-commerce platform. It meets threshold (1) and is subject to the VCDPA.

## Five Consumer Rights (§59.1-577)

### 1. Right to Access (§59.1-577(A)(1))

Consumers have the right to confirm whether a controller is processing their personal data and to access such personal data.

**Liberty Commerce Inc. Implementation:**
Consumers access their data profile through the privacy portal at privacy.libertycommerce.com/virginia. The system generates a comprehensive data access report including all categories of personal data processed, sources, purposes, and any third-party recipients.

### 2. Right to Correct (§59.1-577(A)(2))

Consumers have the right to correct inaccuracies in their personal data, taking into account the nature of the personal data and the purposes of the processing.

### 3. Right to Delete (§59.1-577(A)(3))

Consumers have the right to delete personal data provided by or obtained about the consumer.

**Liberty Commerce Inc. Implementation:**
Deletion requests propagate to all processors within 30 days. Retained data for legal compliance is documented with specific legal basis.

### 4. Right to Data Portability (§59.1-577(A)(4))

Consumers have the right to obtain a copy of their personal data previously provided to the controller in a portable and, to the extent technically feasible, readily usable format that allows the consumer to transmit the data to another controller without hindrance.

### 5. Right to Opt Out (§59.1-577(A)(5))

Consumers have the right to opt out of:
- **Targeted advertising** — displaying advertisements to a consumer based on personal data obtained from the consumer's activities across nonaffiliated websites, applications, or online services
- **Sale of personal data** — exchange of personal data for monetary consideration
- **Profiling** — in furtherance of decisions that produce legal or similarly significant effects concerning the consumer

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. provides a unified opt-out mechanism on its Virginia privacy page. Consumers can opt out of each category independently. GPC signals are recognized and honored as opt-out of targeted advertising and sale, consistent with multi-state compliance.

## Sensitive Data Processing (§59.1-578(A)(5))

The VCDPA requires **opt-in consent** before processing sensitive data. This is a stricter standard than CCPA/CPRA (which allows collection without consent but provides a limit right).

### Sensitive Data Categories (§59.1-575)
1. Personal data revealing racial or ethnic origin
2. Religious beliefs
3. Mental or physical health diagnosis
4. Sexual orientation
5. Citizenship or immigration status
6. Genetic or biometric data processed for identification
7. Personal data collected from a known child
8. Precise geolocation data (within 1,750 feet / 533 meters)

**Key difference from CPRA:** VCDPA requires prior consent; CPRA permits collection with a post-collection limit right.

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. obtains opt-in consent before processing sensitive data from Virginia consumers. The consent mechanism presents each sensitive data category separately with clear affirmative action (unticked checkbox). Consent records include: consumer ID, category, consent text version, timestamp, and mechanism.

## Controller Obligations (§59.1-578)

### Data Minimization (§59.1-578(A)(1))
Limit collection to what is adequate, relevant, and reasonably necessary in relation to the purposes.

### Purpose Limitation (§59.1-578(A)(2))
Do not process personal data for purposes not reasonably necessary to or compatible with the disclosed purposes.

### Security (§59.1-578(A)(3))
Establish, implement, and maintain reasonable administrative, technical, and physical data security practices appropriate to the volume and nature of the personal data at issue.

### Non-Discrimination (§59.1-578(A)(4))
Do not process personal data in violation of state and federal antidiscrimination laws.

### Consent for Sensitive Data (§59.1-578(A)(5))
Obtain consent before processing sensitive data.

### Privacy Notice (§59.1-578(B))
Provide a reasonably accessible, clear, and meaningful privacy notice that includes:
- Categories of personal data processed
- Purpose for processing
- How consumers may exercise their rights (including appeal)
- Categories of personal data shared with third parties
- Categories of third parties with whom data is shared
- Contact information for the controller

### Response Timeline (§59.1-578(C))
- Respond within 45 days of receipt
- Extension: Up to 45 additional days (90 total) with notice to consumer

## Data Protection Impact Assessments (§59.1-580)

Controllers must conduct and document DPIAs for processing activities that present a heightened risk of harm to consumers. Required for:

1. **Targeted advertising** processing
2. **Sale of personal data**
3. **Profiling** where it presents a reasonably foreseeable risk of:
   - Unfair or deceptive treatment or unlawful disparate impact
   - Financial, physical, or reputational injury
   - Physical intrusion or surveillance creating offense to a reasonable person
   - Other substantial injury
4. **Sensitive data** processing
5. **Any processing activity** involving personal data that presents a heightened risk of harm

### DPIA Content Requirements
- Identify and weigh the benefits from the processing against potential risks
- Consider use of de-identified data
- Factor in the reasonable expectations of consumers
- Consider the context of processing and the relationship between controller and consumer

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. has completed DPIAs for:
- Targeted advertising program (AdReach Network partnership)
- Marketplace seller data sale to analytics partners
- Consumer credit scoring for buy-now-pay-later feature
- Precise geolocation processing for delivery optimization
- Sensitive data processing (optional diversity surveys)

Each DPIA is reviewed annually and upon material changes. DPIAs are retained for five years.

## Processor Requirements (§59.1-579)

Processing must be governed by a contract between the controller and processor that includes:
- Instructions for processing data
- Nature and purpose of processing
- Type of data subject to processing and duration
- Rights and obligations of both parties
- Requirement that the processor ensure persons processing data are subject to a duty of confidentiality
- Requirement to delete or return all personal data at controller's direction upon end of services
- Requirement to make available information to demonstrate compliance (upon reasonable request)
- Requirement to allow and cooperate with reasonable assessments by the controller or the controller's designated assessor
- Requirement that the processor engage sub-processors only pursuant to a written contract with obligations no less protective than the controller-processor contract

## Enforcement (§59.1-584)

### Attorney General Authority
- Exclusive enforcement authority under the VCDPA
- May investigate potential violations
- May issue civil investigative demands (CIDs)
- Must provide 30-day written notice of alleged violations before bringing action

### 30-Day Cure Period
- Controller or processor has 30 days after receiving AG notice to cure the alleged violation
- If cured: AG may not bring action for that violation
- If not cured: AG may bring action under the Virginia Consumer Protection Act (§59.1-196 et seq.)

### Penalties
- Civil penalties up to $7,500 per violation
- Reasonable expenses including attorney fees
- Injunctive relief

## Key Regulatory References

- Va. Code §59.1-575 — Definitions
- Va. Code §59.1-576 — Applicability and exemptions
- Va. Code §59.1-577 — Consumer rights
- Va. Code §59.1-578 — Controller obligations
- Va. Code §59.1-579 — Processor requirements
- Va. Code §59.1-580 — Data protection impact assessments
- Va. Code §59.1-581 — De-identified data
- Va. Code §59.1-582 — Limitations
- Va. Code §59.1-583 — Consumer rights request procedures
- Va. Code §59.1-584 — Enforcement, 30-day cure period
- Va. Code §59.1-585 — Relation to other laws
