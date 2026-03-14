# Standards and Regulatory References — Breach Investigation Forensics

## Primary Legislation

### GDPR Article 33(3)(a) — Investigation Obligation
- Art. 33(3)(a) requires notification to include the nature of the breach, categories and numbers of data subjects and records affected. This inherently mandates an investigation to determine these facts.
- Art. 33(4) allows phased notification, acknowledging that investigations take time but requiring information to be provided "without undue further delay."

### GDPR Article 33(5) — Documentation Obligation
- Controllers must document "the facts relating to the personal data breach, its effects and the remedial action taken." This requires a documented investigation with findings.
- The documentation must "enable the supervisory authority to verify compliance."

### GDPR Article 5(2) — Accountability
- The controller must be able to demonstrate compliance with GDPR principles. Forensic investigation documentation serves as accountability evidence for Art. 32 (security measures) and Art. 33/34 (notification) compliance.

## Forensic Standards

### ISO/IEC 27037:2012 — Guidelines for Identification, Collection, Acquisition and Preservation of Digital Evidence
- Provides principles for handling digital evidence: relevance, reliability, sufficiency, and auditability.
- Section 5: First responder activities — identification and collection of potential digital evidence.
- Section 6: Competence requirements for digital evidence handling personnel.
- Section 7: Evidence handling procedures for digital devices, networks, and mobile equipment.

### ISO/IEC 27041:2015 — Guidance on Assuring Suitability and Adequacy of Incident Investigative Method
- Provides guidance on validating investigation methods to ensure they are fit for purpose.
- Section 6: Method validation requirements including error rate assessment.

### ISO/IEC 27042:2015 — Guidelines for the Analysis and Interpretation of Digital Evidence
- Section 5: Analysis process — initial analysis, subsequent analysis, and interpretation.
- Section 6: Use of tools — validation of forensic tools and documentation of tool limitations.
- Section 7: Reporting — requirements for forensic investigation reports.

### ISO/IEC 27043:2015 — Incident Investigation Principles and Processes
- Defines the investigation process classes: readiness, initialization, acquisitive, and investigative.
- Provides the overarching framework within which ISO 27037, 27041, and 27042 operate.

### NIST SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response
- Section 3: Data collection — volatile and non-volatile data, evidence integrity.
- Section 4: Examination — extracting relevant information from collected data.
- Section 5: Analysis — drawing conclusions from examined data.
- Section 6: Reporting — documenting findings and methodology.

### NIST SP 800-61r3 — Computer Security Incident Handling Guide (2024)
- Section 3.2: Detection and analysis — signs of incidents, documentation.
- Section 3.3: Containment, eradication, and recovery.
- Section 3.4: Post-incident activity — lessons learned, evidence retention.

## Regulatory Guidance

### EDPB Guidelines 9/2022 — Investigation and Scope Determination
- Section 2.4: Controllers have a short period to investigate whether a breach has occurred, but this should not unduly delay notification.
- Section 3.1: The risk assessment depends on investigation findings — scope, data types, and exposure duration.
- Section 5: Phased notification is permitted when investigation is ongoing, but available information must be provided immediately.

### ENISA — Recommendations for Technical Investigation of Security Incidents (2023)
- Provides guidance on forensic investigation procedures specifically in the context of personal data breach notification requirements.
- Recommends maintaining pre-prepared forensic toolkits and trained personnel to minimize investigation delays.

### ICO (UK) — Data Security Incident Management Guidance
- Expects controllers to "assess the scope and severity of the breach" through "a thorough investigation."
- The ICO may request investigation documentation during enforcement proceedings.

## Legal Considerations for Forensic Evidence

### Legal Privilege
- In Germany, communications between the DPO and external legal counsel for the purpose of obtaining legal advice may be privileged (Anwaltsprivileg). Forensic reports prepared at the direction of external counsel for litigation purposes may be covered by litigation privilege.
- Forensic reports prepared for regulatory notification purposes (Art. 33 compliance) are generally not privileged and may be disclosed to supervisory authorities.
- Stellar Payments Group maintains two investigation tracks: a privileged track directed by external counsel (Freshfields) and a non-privileged track for regulatory compliance.

### Admissibility of Digital Evidence
- Digital evidence must meet the standards of the applicable jurisdiction for court admissibility.
- In Germany, the Zivilprozessordnung (ZPO) §371 governs electronic evidence. Chain of custody and hash verification are critical for admissibility.
- The EU Regulation on Electronic Evidence (proposed) may harmonize standards across member states.

### Employee Rights
- Investigation of employee devices or accounts must comply with the Bundesdatenschutzgesetz (BDSG) §26 (employee data processing), Works Council co-determination rights under the Betriebsverfassungsgesetz (BetrVG) §87(1)(6), and proportionality requirements.

## Tool References

| Tool | Version | Purpose | Validation |
|------|---------|---------|-----------|
| Splunk Enterprise Security | 7.3 | Log correlation and timeline analysis | NIST CFTT validated |
| ELK Stack (Elasticsearch 8.x) | 8.12 | Large-volume log search and visualization | Open-source, community-validated |
| Wireshark | 4.2 | Network packet analysis | NIST CFTT validated |
| Volatility 3 | 3.0 | Memory forensics analysis | Widely used in forensic community |
| FTK Imager | 4.7 | Forensic disk image acquisition | NIST CFTT validated |
| Autopsy | 4.21 | Disk forensics and file recovery | NIST CFTT validated |
| Plaso/log2timeline | 20240301 | Super-timeline creation | Open-source, community-validated |
| YARA | 4.5 | Malware signature scanning | Widely used, VirusTotal integration |
| Chainsaw | 2.9 | Windows event log rapid triage | Open-source, Sigma-compatible |
| CrowdStrike Falcon Forensics | 7.x | Endpoint forensic data collection | Commercial, vendor-validated |
