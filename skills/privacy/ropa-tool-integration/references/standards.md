# Standards and Regulatory References — RoPA Tool Integration

## Primary Legislation

### GDPR Article 30(3) — Electronic Records

- **Art. 30(3)**: Records shall be in writing, including in electronic form. This provision explicitly authorises and implicitly encourages electronic RoPA management, which is the foundation for tool-based approaches.
- **Art. 30(4)**: Records must be made available to the supervisory authority on request. Electronic systems with export capabilities facilitate timely compliance with supervisory authority requests.

### GDPR Article 24 — Accountability

- **Art. 24(1)**: Controllers must implement appropriate technical and organisational measures to ensure and demonstrate compliance. Purpose-built privacy management platforms provide stronger accountability evidence than manual spreadsheet processes, including audit trails, approval workflows, and version history.

### GDPR Article 25 — Data Protection by Design

- **Art. 25(1)**: Applies to the tools and systems used for privacy management themselves. The privacy management platform must be selected and configured with data protection by design principles, including access controls, encryption, and data minimisation within the platform.

## Regulatory Guidance

### EDPB Guidance

- **EDPB Position Paper on Art. 30 (2018)**: While not prescribing specific tools, the EDPB emphasised that records should be "maintained" (ongoing process) and "made available" (accessibility), both of which are better served by dedicated platforms than static documents.

### National Supervisory Authority Positions

- **CNIL (France)**: Provides its RoPA template in machine-readable formats (CSV, JSON) specifically to facilitate import into privacy management tools. The CNIL has also published a free open-source RoPA tool for smaller organisations.
- **AEPD (Spain)**: Publishes the "Facilita RGPD" tool, a free web-based RoPA generator for SMEs, demonstrating supervisory authority endorsement of tool-based approaches.
- **ICO (United Kingdom)**: The ICO's accountability framework guidance specifically references the use of data mapping tools and privacy management software as indicators of mature accountability practices.

## ISO/IEC Standards

- **ISO/IEC 27701:2019**: Section 7.2.8 (Records related to processing PII) — the PIMS standard supports tool-based record management and integration with the organisation's ISMS.
- **ISO/IEC 27001:2022**: Clause 7.5 (Documented information) — establishes requirements for document control that apply to RoPA tools: creation, updating, version control, access control, storage, retention, and disposition.

## Platform-Specific Certifications

When selecting a RoPA management platform, verify:

| Certification | Relevance |
|--------------|-----------|
| ISO 27001:2022 | Platform provider maintains an ISMS covering the hosted service |
| SOC 2 Type II | Independent audit of security controls (security, availability, processing integrity, confidentiality, privacy) |
| CSA STAR | Cloud-specific security assessment |
| GDPR Art. 28 DPA | Platform provider has executed an Art. 28 DPA for processing RoPA data |
| EU data residency | Platform stores RoPA data within the EEA |
