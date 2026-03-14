# Regulatory Standards — Building Consent Record-Keeping

## Primary Regulations

### GDPR — Regulation (EU) 2016/679

- **Article 7(1)**: "Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to the processing of personal data." This is the foundational requirement for consent record-keeping.
- **Article 7(2)**: Requires that the consent request was presented in a manner clearly distinguishable from other matters, in an intelligible and easily accessible form, using clear and plain language. Records must include the consent text version to prove compliance.
- **Article 5(1)(a)**: Lawfulness, fairness, and transparency — records demonstrate lawful processing.
- **Article 5(2)**: Accountability principle — "The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1." Consent records are a primary mechanism for demonstrating accountability.
- **Article 24(1)**: The controller shall implement appropriate measures to ensure and demonstrate that processing is performed in accordance with the GDPR. This includes maintaining consent evidence.
- **Article 30**: Records of processing activities. Consent records complement Article 30 records by providing granular evidence of the lawful basis for each processing activity.

### Kantara Initiative Consent Receipt Specification v1.1

Published by the Kantara Initiative (a trust framework operator recognized by multiple governments), this specification defines:
- A JSON-based format for machine-readable consent receipts
- Required fields: version, jurisdiction, timestamp, collection method, receipt ID, PII principal ID, PII controllers, policy URL, services, purposes
- Optional fields: public key for receipt verification, sensitive data indicators, special categories
- The specification is designed to be interoperable across jurisdictions (GDPR, CCPA, LGPD, PIPA)
- Version 1.1.0 (latest) aligns with ISO/IEC 29184:2020 requirements

### ISO/IEC 29184:2020 — Online Privacy Notices and Consent

International standard specifying:
- Controls and consent record elements for online services
- Requirements for consent timestamps, versioning, and audit trails
- Guidance on consent receipt formats and content
- Interoperability with privacy frameworks across jurisdictions

## Supervisory Authority Guidance

### EDPB Guidelines 05/2020 on Consent

- **Paragraphs 89-93**: The burden of proof is on the controller. If challenged, the controller must be able to produce evidence that consent was obtained.
- **Paragraphs 94-98**: Evidence should include: who consented, when they consented, what they were told at the time, how they consented, and whether they subsequently withdrew consent.
- **Paragraphs 99-102**: The consent mechanism itself must be designed to create evidence. Logging UI interactions (clicks, toggles) alongside consent text versions creates robust evidence.
- **Paragraphs 103-107**: Re-consent obligations when consent text changes. Records must track version transitions.

### ICO Guidance on Consent Record-Keeping (UK)

The UK Information Commissioner's Office recommends:
- Keep records of when and how consent was obtained from each individual
- Keep a copy of the information provided to the individual at the time
- Keep records of the specific consent statement signed or ticked
- Implement regular audits to verify record completeness
- Maintain records for the duration of the processing plus a reasonable period for potential complaints (ICO suggests 6 years aligned with UK limitation period)

### Belgian DPA Decision 21/2022

The Belgian Data Protection Authority fined IAB Europe EUR 250,000 (February 2022) for TCF consent management deficiencies, partly because consent records within the TC String framework were insufficient to demonstrate valid consent under Article 7(1). This case underscored the importance of maintaining detailed consent records beyond what encoded strings can capture.
