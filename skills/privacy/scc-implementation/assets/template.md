# Standard Contractual Clauses — Implementation Record Template

## Transfer Identification

| Field | Value |
|-------|-------|
| Transfer Reference | SCC-2025-APAC-001 |
| Date of Assessment | 15 March 2025 |
| Assessed By | Elisa Brandt, Head of Data Protection, Athena Global Logistics GmbH |
| SCC Version | Commission Implementing Decision (EU) 2021/914 of 4 June 2021 |

## Module Selection Record

| Criterion | Assessment |
|-----------|-----------|
| Data Exporter Identity | Athena Global Logistics GmbH (Berlin, Germany) |
| Data Exporter Role | Controller — determines purposes and means of processing shipment data for European operations |
| Data Importer Identity | TransPacific Freight Solutions Ltd (Hong Kong SAR) |
| Data Importer Role | Processor — processes shipment data on documented instructions from Athena Global Logistics for regional freight consolidation and customs clearance |
| Selected Module | Module 2: Controller to Processor (C2P) |
| Rationale | The importer does not independently determine the purposes of processing; all processing is performed on behalf of and under the instructions of the exporter pursuant to the freight forwarding services agreement dated 1 January 2025 |

## Annex I.A — Parties Checklist

| Required Field | Completed | Content Summary |
|---------------|-----------|-----------------|
| Exporter legal name and address | Yes | Athena Global Logistics GmbH, Friedrichstrasse 112, 10117 Berlin |
| Exporter contact person | Yes | Elisa Brandt, elisa.brandt@athenalogistics.eu |
| Exporter activities | Yes | International freight forwarding, customs brokerage, warehouse management |
| Exporter role designation | Yes | Controller |
| Importer legal name and address | Yes | TransPacific Freight Solutions Ltd, 88 Harbour Road, Wan Chai, Hong Kong SAR |
| Importer contact person | Yes | James Leung, j.leung@transpacificfreight.hk |
| Importer activities | Yes | Regional freight consolidation, last-mile delivery, customs clearance |
| Importer role designation | Yes | Processor |

## Annex I.B — Transfer Description Checklist

| Required Field | Completed | Content Summary |
|---------------|-----------|-----------------|
| Data subject categories | Yes | Shipping customers, employees of customer companies, customs brokers, warehouse workers |
| Personal data categories | Yes | Full name, business email, phone, company name, shipping address, customs ID numbers, consignment references |
| Sensitive data | Yes | None transferred |
| Transfer frequency | Yes | Continuous real-time API; daily batch at 02:00 UTC |
| Processing nature | Yes | Storage, retrieval, customs documentation, delivery tracking, exception reporting |
| Transfer purpose | Yes | Freight forwarding contract fulfilment — regional customs clearance and delivery |
| Retention period | Yes | 36 months from shipment completion |

## Annex I.C — Supervisory Authority

| Field | Value |
|-------|-------|
| Competent SA | Berliner Beauftragte fuer Datenschutz und Informationsfreiheit (BlnBDI) |
| Basis for Selection | SA of the EU Member State in which the data exporter is established (Clause 13) |

## Annex II — Technical and Organisational Measures Checklist

| Measure | Documented | Last Verified |
|---------|-----------|--------------|
| Encryption in transit (TLS 1.3 / SFTP AES-256) | Yes | 10 March 2025 |
| Encryption at rest (AES-256) | Yes | 10 March 2025 |
| Access control (RBAC + MFA) | Yes | 10 March 2025 |
| Data minimisation (field stripping, masking) | Yes | 10 March 2025 |
| Logging and monitoring (SIEM, 12-month retention) | Yes | 10 March 2025 |
| Incident response (24-hour SLA) | Yes | 10 March 2025 |
| Physical security (ISO 27001 DC) | Yes | 10 March 2025 |
| Business continuity (RPO 4h / RTO 8h) | Yes | 10 March 2025 |
| Staff measures (training, background checks) | Yes | 10 March 2025 |
| Sub-processor management (due diligence, audit) | Yes | 10 March 2025 |

## Annex III — Sub-Processor Authorisation Record

| Sub-Processor | Country | Activity | Authorisation Type | SCC Executed |
|--------------|---------|----------|--------------------|-------------|
| CloudVault Asia Pte Ltd | Singapore | Cloud hosting | General authorisation with notification | Module 3, 15 March 2025 |
| Pinnacle Data Services Co Ltd | Thailand | Data entry for customs docs | Specific authorisation | Module 3, 22 January 2025 |

## Clause 14 — Transfer Impact Assessment Cross-Reference

| Field | Value |
|-------|-------|
| TIA Reference Number | TIA-2025-HK-001 |
| TIA Completion Date | 10 March 2025 |
| Destination Country | Hong Kong SAR, China |
| Key Laws Assessed | Hong Kong Personal Data (Privacy) Ordinance (Cap. 486); PRC National Security Law as applied in HKSAR; Interception of Communications and Surveillance Ordinance (Cap. 589) |
| TIA Conclusion | Transfer may proceed with supplementary measures; identified risk of access under NSL assessed as low probability for freight logistics data |
| Supplementary Measures Applied | End-to-end TLS 1.3 encryption; data segmentation restricting HKSAR staff access to logistics data only; contractual transparency obligation for government requests |

## Execution Record

| Field | Value |
|-------|-------|
| Execution Date | 15 March 2025 |
| Exporter Signatory | Elisa Brandt, Head of Data Protection |
| Importer Signatory | James Leung, Chief Privacy Officer |
| Governing Law (Clause 17) | Law of the Federal Republic of Germany |
| Forum and Jurisdiction (Clause 18) | Courts of Berlin, Germany |
| Next Review Date | 15 March 2026 |

## Ongoing Compliance Actions

| Action | Frequency | Next Due |
|--------|-----------|----------|
| Annual SCC review | Annual | 15 March 2026 |
| TIA reassessment | Annual or upon material legal change | 10 March 2026 |
| Sub-processor audit | Annual | 15 March 2026 |
| Annex II measures verification | Annual | 10 March 2026 |
| Data subject request procedure test | Semi-annual | 15 September 2025 |
