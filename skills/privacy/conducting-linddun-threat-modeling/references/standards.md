# LINDDUN Threat Modeling Standards and References

## LINDDUN Methodology

### Original Framework (2011)
Deng, M., Wuyts, K., Scandariato, R., Preneel, B., & Joosen, W. "A privacy threat analysis framework: supporting the elicitation and fulfillment of privacy requirements." Requirements Engineering, 16(1), 3-32. Introduced the LINDDUN framework with seven privacy threat categories mapped to privacy properties.

### LINDDUN GO (Lightweight Version)
Wuyts, K. & Joosen, W. "LINDDUN GO: A Lightweight Approach to Privacy Threat Modeling." Simplified version using threat type cards for rapid privacy threat identification in agile environments. Available at linddun.org.

### Official Resources
The LINDDUN methodology, threat tree catalogs, and case studies are maintained at linddun.org by the DistriNet research group at KU Leuven (Belgium).

## Privacy Properties Mapped to LINDDUN

| LINDDUN Category | Privacy Property | Opposite (Threat) |
|------------------|-----------------|-------------------|
| Linking | Unlinkability | Linkability |
| Identifying | Anonymity / Pseudonymity | Identifiability |
| Non-repudiation | Plausible deniability | Non-repudiation |
| Detecting | Undetectability / Unobservability | Detectability |
| Data Disclosure | Confidentiality | Disclosure |
| Unawareness | Content awareness | Unawareness |
| Non-compliance | Policy and consent compliance | Non-compliance |

## Relationship to STRIDE

| STRIDE Category | Focus | LINDDUN Category | Focus |
|----------------|-------|-------------------|-------|
| Spoofing | Authentication | Identifying | Anonymity |
| Tampering | Integrity | Non-compliance | Policy adherence |
| Repudiation | Non-repudiation | Non-repudiation | Plausible deniability |
| Information disclosure | Confidentiality | Data Disclosure | Data confidentiality |
| Denial of service | Availability | (Not directly mapped) | |
| Elevation of privilege | Authorization | Detecting | Undetectability |

## GDPR Regulatory Basis

### Article 25 — Data Protection by Design
LINDDUN directly supports Article 25 by providing a systematic methodology for identifying privacy risks at the design stage and selecting appropriate technical measures.

### Article 35 — Data Protection Impact Assessment
LINDDUN can serve as the risk identification methodology within a DPIA. The threat trees provide structured elicitation of privacy risks, and the risk scoring supports the DPIA's risk assessment.

### Article 32 — Security of Processing
While LINDDUN focuses on privacy threats, several categories (Data Disclosure, Non-compliance) overlap with security requirements under Article 32.

## Supporting Standards

### ISO/IEC 27005:2022 — Information Security Risk Management
Provides a general framework for risk assessment that LINDDUN specializes for privacy threats. The risk scoring methodology (likelihood x impact) is compatible with ISO 27005.

### NIST Privacy Framework v1.0
NIST's privacy framework identifies functions (Identify, Govern, Control, Communicate, Protect) that map to LINDDUN mitigation categories.
