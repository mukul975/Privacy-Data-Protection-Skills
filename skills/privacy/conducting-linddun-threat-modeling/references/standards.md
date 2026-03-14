# LINDDUN Standards and References

## Methodology Foundation

### Original LINDDUN Paper (2011)
Deng, M., Wuyts, K., Scandariato, R., Preneel, B., & Joosen, W. "A privacy threat analysis framework: supporting the elicitation and fulfillment of privacy requirements." Requirements Engineering, 16(1), 3-32. Introduced the LINDDUN methodology with seven privacy threat categories derived from privacy properties.

### LINDDUN GO (2020)
Wuyts, K., & Joosen, W. "LINDDUN GO: A Lightweight Approach to Privacy Threat Modeling." Streamlined version of LINDDUN using card-based elicitation for agile development teams. Suitable for rapid assessments and workshops.

### LINDDUN PRO (2022)
Full systematic methodology with comprehensive threat tree catalogs, detailed DFD analysis, and formal risk assessment. Suitable for complex systems and high-risk processing activities.

## Privacy Properties

The seven LINDDUN categories map to established privacy properties:

| LINDDUN Category | Privacy Property | Definition Source |
|-----------------|-----------------|-------------------|
| Linking | Unlinkability | ISO/IEC 15408 (Common Criteria) |
| Identifying | Anonymity, Pseudonymity | Pfitzmann & Hansen terminology (2010) |
| Non-repudiation | Plausible deniability | Pfitzmann & Hansen terminology |
| Detecting | Undetectability, Unobservability | Pfitzmann & Hansen terminology |
| Data Disclosure | Confidentiality | ISO/IEC 27001 |
| Unawareness | Transparency, Intervenability | GDPR Articles 12-14 |
| Non-compliance | Compliance | GDPR Article 5, ISO/IEC 27701 |

## GDPR Integration

### Article 25(1) — Data Protection by Design
LINDDUN serves as a systematic methodology for identifying privacy risks during the design phase, directly implementing the Article 25(1) requirement to consider privacy "at the time of the determination of the means for processing."

### Article 35 — DPIA
LINDDUN provides a structured risk identification methodology suitable for the "systematic description of the envisaged processing operations and the purposes" (Article 35(7)(a)) and "assessment of the risks to the rights and freedoms of data subjects" (Article 35(7)(c)).

### EDPB Guidelines 4/2019
Identifies threat modeling as a recommended approach for implementing data protection by design. LINDDUN is explicitly suitable for the privacy risk assessment required under these guidelines.

## Related Methodologies

### STRIDE (Microsoft)
Security-focused threat modeling framework. LINDDUN complements STRIDE by addressing privacy-specific threats not covered by security analysis.

### PASTA (Process for Attack Simulation and Threat Analysis)
Risk-centric threat modeling methodology. Can be combined with LINDDUN for comprehensive security and privacy threat assessment.

### NIST Privacy Framework
Provides a high-level privacy risk management framework. LINDDUN operationalizes the "Identify" and "Govern" functions at the technical architecture level.
