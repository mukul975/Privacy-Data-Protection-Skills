# Standards and Regulatory References — Backup Retention and Erasure

## Primary Legislation

### GDPR (Regulation (EU) 2016/679)
- **Article 17(1)** — Right to erasure: "without undue delay" — acknowledged as requiring longer for backups
- **Article 5(1)(e)** — Storage limitation: applies to backup copies
- **Article 5(1)(f)** — Integrity and confidentiality: backup encryption and access controls
- **Article 25** — Data protection by design: backup retention aligned with retention schedule at design stage
- **Article 32(1)(c)** — Ability to restore availability and access to personal data in timely manner (business continuity)
- **Article 32(1)(d)** — Regular testing of effectiveness of technical and organisational measures
- **Recital 66** — Right to be forgotten in the online environment (extends to backup copies)

### UK Data Protection Act 2018
- **Section 47** — Right to erasure (law enforcement processing) — same backup considerations apply
- **Section 40** — Security principle — backup integrity requirements

## Regulatory Guidance

### ICO (UK Information Commissioner's Office)
- **Right to erasure guidance** — "Put beyond use" concept for data in backup systems: data should not be actively used while awaiting deletion through backup rotation
- **ICO guidance on security** — Backup systems as a security measure; retention alignment requirement

### EDPB (European Data Protection Board)
- **Guidelines on the right to erasure** — Acknowledgement that backup deletion may require extended timeframe aligned with backup rotation
- **Guidelines 01/2020 on processing of personal data in the context of connected vehicles** — Practical example of backup erasure considerations (IoT context)

### Article 29 Working Party
- **WP250 rev.01 — Guidelines on the right to data portability** — Interaction between portability and backup systems

## Technical Standards
- **ISO/IEC 27001:2022 Annex A Control A.8.13** — Information backup: backup policies including retention periods
- **ISO/IEC 27001:2022 Annex A Control A.8.10** — Information deletion: applies to backup media
- **ISO/IEC 27002:2022 Section 8.13** — Information backup guidance including retention alignment
- **NIST SP 800-34 Rev. 1** — Contingency Planning Guide: backup strategy and retention
- **NIST SP 800-88 Rev. 1** — Media sanitization: applicable to backup media destruction
- **ISO 22301:2019** — Business continuity management: backup requirements that must be balanced with retention obligations
