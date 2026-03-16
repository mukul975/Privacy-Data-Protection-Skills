# Regulatory Standards — Delaware DPPA

## Primary Legislation

### Delaware Personal Data Privacy Act — 6 Del. C. §§12D-101 through 12D-111

Enacted: September 11, 2023 (HB 154). Effective: January 1, 2025.

- **§12D-101**: Short title
- **§12D-102**: Definitions (consumer, controller, processor, personal data, sensitive data, sale, targeted advertising, profiling, dark pattern, consent, precise geolocation)
- **§12D-103**: Applicability thresholds (35,000 consumers OR 10,000 + 20% revenue)
- **§12D-104**: Exemptions (entity-level and data-level)
- **§12D-105**: Controller duties (minimization, security, consent for sensitive data, DPIAs, minor protections, privacy notice)
- **§12D-106**: Consumer rights (access, correct, delete, portability, opt-out, appeal)
- **§12D-107**: Processor obligations and contract requirements
- **§12D-108**: De-identified and pseudonymous data provisions
- **§12D-109**: Limitations on applicability and construction
- **§12D-110**: Enforcement by Delaware AG, civil penalties up to $10,000 per violation
- **§12D-111**: Effective date and universal opt-out phase-in (January 1, 2026)

## Key Definitions (§12D-102)

### Consumer (§12D-102(8))
A natural person who is a Delaware resident acting only in an individual or household context. Does not include a person acting in a commercial or employment context.

### Personal Data (§12D-102(18))
Any information that is linked or reasonably linkable to an identified or identifiable natural person. Does not include de-identified data, aggregate data, or publicly available information.

### Sensitive Data (§12D-102(24))
Personal data revealing:
- Racial or ethnic origin
- Religious beliefs
- Mental or physical health condition or diagnosis
- Sex life or sexual orientation
- Citizenship or immigration status (unique to Delaware among early-enacted state laws)
- Genetic data
- Biometric data processed for identification
- Personal data of a known child under 13
- Precise geolocation data (within 1,750 feet)

### Consent (§12D-102(6))
A clear affirmative act signifying a consumer's freely given, specific, informed, and unambiguous agreement. Does not include:
- Acceptance of general terms of use
- Hovering over, muting, pausing, or closing content
- Agreement obtained through dark patterns

### Sale (§12D-102(23))
Exchange of personal data for monetary or other valuable consideration by the controller to a third party. Does not include:
- Disclosure to a processor
- Disclosure to an affiliate
- Disclosure as part of a merger/acquisition/bankruptcy
- Disclosure the consumer intentionally made public
- Disclosure to a third party at consumer direction

## Universal Opt-Out Mechanism Standards

### Global Privacy Control (GPC) Technical Specification
The GPC signal (Sec-GPC HTTP header) is the primary mechanism expected to satisfy the universal opt-out requirement. The specification requires:
- A `Sec-GPC: 1` HTTP header sent by the user agent
- The signal represents the user's intent to opt out of the sale of personal data and targeted advertising
- Controllers must not require additional action from the consumer after signal detection
- Absence of the signal must not be interpreted as consent to sell

### AG Guidance on Universal Opt-Out (Expected 2025-2026)
The Delaware AG is expected to issue guidance clarifying acceptable universal opt-out mechanisms, potentially referencing the Colorado AG rules on universal opt-out (4 CCR 904-3, Rule 5.11) as a model.

## Data Protection Assessment Standards

### DPPA Assessment Requirements (§12D-105(b))
Assessments must:
- Identify and weigh benefits of processing to controller, consumer, and public
- Identify and weigh potential risks of processing to consumer rights
- Factor in the use of de-identification and security safeguards
- Consider the reasonable expectations of the consumer
- Consider the context of the processing

### NIST Privacy Framework v1.0
The NIST Privacy Framework provides a voluntary tool for identifying and managing privacy risk. Core functions relevant to DPPA DPIA:
- **Identify-P**: Inventory processing activities, data elements, and purposes
- **Govern-P**: Establish policies for risk tolerance and assessment methodology
- **Control-P**: Implement data processing management controls
- **Communicate-P**: Provide transparency mechanisms to individuals
- **Protect-P**: Data protection safeguards aligned with processing risk

### ISO/IEC 27701:2019 — Privacy Information Management System
Extension to ISO 27001/27002 for privacy management. Relevant controls:
- **A.7.2.1**: Purpose identification and documentation
- **A.7.2.2**: Lawful basis identification
- **A.7.2.5**: Privacy impact assessment
- **A.7.2.8**: Records of processing

### ISO/IEC 29134:2017 — Privacy Impact Assessment Guidelines
Provides methodology for conducting PIAs:
- Threshold analysis to determine PIA necessity
- Systematic description of processing operations
- Assessment of necessity and proportionality
- Risk identification and evaluation
- Risk treatment measures

## Cross-Reference: Federal and Other State Laws

### FTC Act Section 5 — Unfair or Deceptive Practices
The FTC's enforcement of unfair and deceptive practices provides a federal baseline. Delaware's dark pattern prohibition aligns with FTC standards articulated in "Bringing Dark Patterns to Light" (September 2022).

### COPPA (15 U.S.C. §§6501-6506)
The DPPA incorporates COPPA standards for verifiable parental consent when processing data of known children under 13. COPPA Rule (16 CFR Part 312) defines acceptable verification methods.

### Colorado Privacy Act Rules (4 CCR 904-3)
Colorado AG rules provide useful implementation guidance for:
- Universal opt-out mechanism technical requirements (Rule 5.11)
- Data protection assessment methodology (Rule 8)
- Consent standards and dark pattern avoidance (Rule 4)

### Connecticut CTDPA (Conn. Gen. Stat. §42-515 through §42-525)
Similar structure to Delaware; useful for comparison on:
- Dark pattern definition and prohibition
- Universal opt-out implementation timeline
- Minor protections framework
