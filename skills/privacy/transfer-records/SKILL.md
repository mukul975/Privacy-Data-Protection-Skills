---
name: managing-transfer-records-documentation
description: >-
  Guides maintenance of cross-border transfer registers, audit trails, and
  compliance documentation under GDPR Art. 30 and Art. 46, EDPB record-keeping
  guidance, and supervisory authority expectations. Keywords: transfer register,
  audit trail, Art. 30, Art. 46, documentation, compliance records.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cross-border-transfers
  tags: "transfer-register, audit-trail, art-30, art-46, documentation, compliance-records"
---

# Managing Transfer Records and Documentation

## Overview

Maintaining comprehensive transfer records and documentation is a foundational obligation under the GDPR and a practical necessity for demonstrating compliance with cross-border data transfer requirements. Articles 5(2) and 24 impose a general accountability obligation, while Article 30 mandates specific records of processing activities — including details of international transfers. Beyond these baseline requirements, each transfer mechanism (SCCs, BCRs, adequacy reliance, derogations) carries its own documentation expectations. This skill provides a structured approach to building, maintaining, and auditing transfer records across all mechanisms.

## Transfer Register: Core Fields

### Mandatory Fields per Transfer Entry

Every cross-border transfer must be documented with the following information:

| Field | Description | Legal Basis |
|-------|-------------|-------------|
| Transfer ID | Unique identifier for the transfer entry | Internal governance |
| Data Exporter | Identity and contact details of the transferring entity | Art. 30(1)(a) |
| Data Importer | Identity and contact details of the receiving entity | Art. 30(1)(a) |
| Exporter Country | Country from which data is transferred | Art. 30(1)(e) |
| Importer Country | Destination country or international organisation | Art. 30(1)(e) |
| Categories of Data Subjects | Types of individuals whose data is transferred | Art. 30(1)(c) |
| Categories of Personal Data | Types of personal data transferred | Art. 30(1)(c) |
| Special Category Data | Whether Art. 9 special categories are included | Art. 9(1), Art. 30(1)(c) |
| Purpose of Transfer | Business and legal purpose for the transfer | Art. 30(1)(b) |
| Legal Basis for Processing | Lawful basis under Art. 6 (and Art. 9 if applicable) | Art. 30(1)(b) |
| Transfer Mechanism | The Chapter V mechanism relied upon | Art. 30(1)(e), Art. 46 |
| Mechanism Reference | SCC execution date, BCR approval reference, adequacy decision reference, etc. | Art. 46 |
| TIA Reference | Reference to the Transfer Impact Assessment (if applicable) | EDPB Rec. 01/2020 |
| Supplementary Measures | Technical, contractual, and organisational measures applied | EDPB Rec. 01/2020 |
| Data Retention Period | How long transferred data will be retained by the importer | Art. 30(1)(f) |
| Review Date | Next scheduled review date for the transfer | Accountability (Art. 5(2)) |
| Status | Active, Under Review, Suspended, Terminated | Internal governance |
| Risk Rating | Overall risk assessment (Low, Medium, High, Critical) | Accountability (Art. 5(2)) |

### Extended Fields for Specific Mechanisms

**For SCC-based transfers:**

| Field | Description |
|-------|-------------|
| SCC Module | Module 1 (C2C), 2 (C2P), 3 (P2P), or 4 (P2C) |
| SCC Execution Date | Date the SCCs were signed by both parties |
| SCC Annex I Completed | Whether the transfer description annex is completed |
| SCC Annex II Completed | Whether the technical/organisational measures annex is completed |
| SCC Annex III Completed | Whether the sub-processor list is completed (Modules 2/3) |
| Clause 7 Docking | Whether a docking clause has been used for additional parties |

**For BCR-based transfers:**

| Field | Description |
|-------|-------------|
| BCR Approval Authority | Lead supervisory authority that approved the BCRs |
| BCR Approval Date | Date of BCR approval |
| BCR Version | Current version of the BCRs |
| Entity Coverage | Whether the specific entities are listed in the BCR member list |
| BCR Audit Date | Date of last BCR compliance audit |

**For adequacy-based transfers:**

| Field | Description |
|-------|-------------|
| Adequacy Decision Reference | EC decision number and date |
| Adequacy Scope | Full or partial adequacy; any sector/type limitations |
| Adequacy Review Date | Date of next EC review of the adequacy decision |
| Monitoring Status | Whether developments in the destination country are being tracked |

**For Art. 49 derogation-based transfers:**

| Field | Description |
|-------|-------------|
| Derogation Relied Upon | Specific Art. 49 paragraph |
| Necessity Assessment | Documentation of why the transfer is strictly necessary |
| Frequency | Whether the transfer is occasional or repetitive |
| DPA Notification | Whether the supervisory authority has been informed (Art. 49(1)(2)) |

## Audit Trail Requirements

### What Must Be Logged

The audit trail for transfer records must capture:

| Event Type | Details to Log | Retention |
|------------|---------------|-----------|
| Transfer Created | Creator identity, creation date, all initial field values | Life of transfer + 5 years |
| Transfer Modified | Modifier identity, modification date, field changed, old value, new value | Life of transfer + 5 years |
| Mechanism Changed | Old mechanism, new mechanism, reason for change, approver | Life of transfer + 5 years |
| TIA Completed/Updated | TIA reference, assessment date, outcome, assessor | Life of transfer + 5 years |
| Review Conducted | Reviewer identity, review date, outcome, next review date | Life of transfer + 5 years |
| Transfer Suspended | Suspension date, reason, authoriser | Life of transfer + 5 years |
| Transfer Terminated | Termination date, reason, data return/deletion confirmation | Life of transfer + 5 years |
| Document Attached | Document type, filename, upload date, uploader | Life of transfer + 5 years |
| SA Inquiry Received | Inquiry reference, SA identity, date, scope | Life of transfer + 10 years |

### Audit Trail Integrity

- Each audit log entry must be immutable once created
- Entries must include a timestamp (UTC) and authenticated user identity
- The audit trail must be protected against tampering (hash chains, write-once storage, or equivalent)
- Access to the audit trail must be restricted to authorised personnel (DPO, privacy counsel, internal audit)

## Documentation Packages by Mechanism

### SCC Documentation Package

A complete SCC documentation package for each transfer includes:

1. **Executed SCCs** — Signed copy with all Annexes (I, II, III where applicable)
2. **Transfer Impact Assessment** — Completed TIA per EDPB 6-step methodology
3. **Supplementary measures record** — List of technical, contractual, and organisational measures with effectiveness assessment
4. **Due diligence record** — Evidence of importer assessment (questionnaire responses, certifications, audit reports)
5. **Annex review log** — Record of periodic reviews and updates to Annex content
6. **Sub-processor management** — Current sub-processor list, notification records, objection process documentation

### BCR Documentation Package

1. **Approved BCR text** — Current version with all amendments
2. **BCR member list** — All entities bound by the BCRs with accession dates
3. **Compliance audit reports** — Internal and external audit reports
4. **Training records** — Evidence of BCR training for relevant personnel
5. **Complaint handling log** — Records of data subject complaints and resolutions
6. **Update log** — Record of all BCR amendments with approval dates

### Adequacy Documentation Package

1. **Adequacy decision reference** — Link to the relevant EC decision
2. **Scope assessment** — Documentation confirming the transfer falls within the adequacy scope
3. **Monitoring log** — Evidence of monitoring developments in the destination country
4. **Contingency plan** — Plan for transitioning to alternative mechanisms if adequacy is revoked

### Art. 49 Derogation Documentation Package

1. **Derogation assessment** — Written analysis of why the specific derogation applies
2. **Necessity analysis** — Documentation of why no alternative mechanism is available
3. **Data subject information** — Evidence that data subjects were informed per Art. 49(1)(e) where applicable
4. **DPA notification** — Copy of any notification to the supervisory authority under Art. 49(1)(2)
5. **Transfer log** — Detailed log of each individual transfer (for occasional transfers)

## Supervisory Authority Expectations

### Information to Produce on Request

Supervisory authorities expect organisations to produce the following within a reasonable timeframe (typically 2-4 weeks):

1. Complete transfer register covering all international transfers
2. Transfer mechanism documentation for any specific transfer
3. TIA documentation for transfers to non-adequate countries
4. Evidence of periodic reviews and updates
5. Audit trail for any specific transfer entry
6. Sub-processor chains for processor-based transfers
7. Records of any transfer suspensions or terminations and the reasons

### Common SA Findings

| Finding | Description | Remediation |
|---------|-------------|-------------|
| Incomplete register | Missing transfers or incomplete fields | Conduct full inventory; populate all mandatory fields |
| Stale TIAs | TIAs not updated after significant legal developments | Establish TIA review triggers and periodic review schedule |
| Missing execution dates | SCCs without documented execution dates | Obtain signed copies with dates; implement document management |
| No review schedule | No evidence of periodic transfer reviews | Establish annual review cycle; document in governance framework |
| Inadequate audit trail | Changes to transfer records not tracked | Implement audit logging; migrate to system with built-in audit trail |
| Missing sub-processor records | Incomplete or outdated sub-processor lists | Audit sub-processor chains; update SCC Annex III |

## Review and Governance Cycle

### Annual Review Cycle

| Quarter | Activity |
|---------|----------|
| Q1 | Full transfer register review: verify all active transfers, close terminated transfers, update mechanism status |
| Q2 | TIA refresh: reassess all transfers to non-adequate countries against current legal developments |
| Q3 | Mechanism review: verify SCC execution dates, BCR compliance, adequacy decision status, derogation continuing necessity |
| Q4 | Governance review: assess documentation completeness, audit trail integrity, SA readiness, update policies |

### Trigger-Based Reviews

In addition to the annual cycle, reviews must be triggered by:

- Change in destination country legislation or enforcement practice
- CJEU judgment affecting transfer mechanisms (e.g., Schrems-type ruling)
- EC adequacy decision adopted, amended, or revoked
- EDPB guidance or recommendation affecting transfer documentation
- Organisational change (new entity, acquisition, divestiture)
- Data breach involving transferred data
- Supervisory authority inquiry or investigation

## Athena Global Logistics — Transfer Register Example

### Active Transfers (Extract)

| Transfer ID | Exporter | Importer | Dest Country | Mechanism | TIA Ref | Review Date | Status |
|------------|----------|----------|-------------|-----------|---------|------------|--------|
| ATH-INT-001 | Athena GmbH (DE) | TransPacific Ltd (HK) | Hong Kong | SCCs Module 2 | TIA-2024-003 | 2025-06-30 | Active |
| ATH-INT-002 | Athena GmbH (DE) | CloudVault Pte Ltd (SG) | Singapore | SCCs Module 3 | TIA-2024-005 | 2025-06-30 | Active |
| ATH-INT-003 | Athena GmbH (DE) | Athena Japan KK (JP) | Japan | EU Adequacy (2019/419) | N/A | 2025-12-31 | Active |
| ATH-INT-004 | Athena GmbH (DE) | Athena India Pvt Ltd (IN) | India | SCCs Module 1 | TIA-2024-008 | 2025-06-30 | Active |
| ATH-INT-005 | Athena GmbH (DE) | Pinnacle TH (TH) | Thailand | SCCs Module 3 | TIA-2024-010 | 2025-06-30 | Active |
| ATH-INT-006 | Athena GmbH (DE) | Athena US Inc (US) | United States | DPF + SCCs fallback | TIA-2024-012 | 2025-06-30 | Active |

### Governance Framework

- **Transfer Register Owner**: Elisa Brandt, Group DPO
- **Review Frequency**: Quarterly (full register), plus trigger-based
- **Audit Trail System**: GRC platform with immutable logging
- **SA Response SLA**: Complete documentation package within 10 business days of request
- **Escalation Path**: DPO → Head of Legal → Chief Privacy Officer → Board Privacy Committee
