---
name: implementing-standard-contractual-clauses
description: >-
  Guides implementation of EU Standard Contractual Clauses under Commission Decision
  2021/914 across all four modules (C2C, C2P, P2P, P2C). Covers clause-by-clause
  completion, Annex I-III drafting, and SCC module selection. Keywords: SCCs, standard
  contractual clauses, module selection, data transfers, Annex completion.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cross-border-transfers
  tags: "sccs, standard-contractual-clauses, cross-border-transfers, gdpr-article-46, data-export"
---

# Implementing Standard Contractual Clauses

## Overview

Commission Implementing Decision (EU) 2021/914 of 4 June 2021 introduced modernised Standard Contractual Clauses (SCCs) for the transfer of personal data to third countries under Regulation (EU) 2016/679. These SCCs replaced the prior sets adopted under Directive 95/46/EC and became the mandatory instrument from 27 December 2022. The modular architecture allows parties to select the appropriate clause set based on their roles in the transfer relationship.

## Module Selection Decision Framework

### Module 1: Controller to Controller (C2C)

**When to use**: The data exporter is a controller and the data importer independently determines the purposes and means of processing the imported data as a separate controller.

**Typical scenarios at Athena Global Logistics**:
- Sharing shipment tracking data with overseas partner logistics firms that independently process that data for their own route optimisation
- Providing employee data to a foreign group entity that acts as an independent controller for local employment law compliance
- Transferring customer data to an overseas insurance partner that underwrites cargo policies under its own controllership

**Key Module 1 clauses**:
- Clause 8.1 — Data protection safeguards: The data importer must process data only for the specific purposes described in Annex I, with an independent legal basis under the importer's applicable law
- Clause 8.2 — Purpose limitation: The importer shall not process data for purposes incompatible with those for which the data was transferred
- Clause 8.3 — Transparency: The importer must provide data subjects with a copy of the clauses and Annex I information upon request
- Clause 8.4 — Accuracy: Both parties must take reasonable steps to ensure data is accurate and up to date
- Clause 8.5 — Duration and erasure: Data processed only for the duration specified in Annex II; erasure or return upon termination

### Module 2: Controller to Processor (C2P)

**When to use**: The data exporter is a controller and the data importer processes data on behalf of the exporter as a processor.

**Typical scenarios at Athena Global Logistics**:
- Engaging a cloud infrastructure provider headquartered in a third country to host the transport management system
- Using an overseas payroll processing bureau to calculate salaries for locally-hired staff
- Contracting a third-country call centre to handle customer service inquiries on behalf of the company

**Key Module 2 clauses**:
- Clause 8.1 — Instructions: The processor shall process data only on documented instructions from the controller as specified in Annex II
- Clause 8.2 — Purpose limitation: Processing solely for the specific purposes set out in Annex I
- Clause 8.3 — Transparency: Controller must inform data subjects of the transfer and identity of the importer
- Clause 8.5 — Sub-processing: Sub-processors only with prior specific or general written authorisation; same data protection obligations imposed by contract
- Clause 8.6 — International onward transfers: Sub-processor transfers require the same level of protection
- Clause 8.8 — Security: Technical and organisational measures as described in Annex II
- Clause 8.9 — Documentation and compliance: Processor must maintain records and allow audits

### Module 3: Processor to Processor (P2P)

**When to use**: The data exporter is a processor (acting on behalf of an EU controller) and the data importer is a sub-processor.

**Typical scenarios at Athena Global Logistics**:
- The company acts as a data processor for a European shipping consortium and sub-contracts warehousing data management to a third-country sub-processor
- A managed IT services provider contracted by the company further sub-processes personal data with an offshore development centre

**Key Module 3 clauses**:
- Clause 8.1 — Instructions: Sub-processor processes only under the chain of instructions ultimately originating from the controller
- Clause 8.5 — Onward sub-processing: Further sub-processing only with prior specific or general written authorisation from the controller (obtained through the initial processor)
- Clause 8.8 — Security measures: Annex II security measures apply equivalently
- Clause 8.9 — Documentation and compliance: Full audit chain maintained back to the controller

### Module 4: Processor to Controller (P2C)

**When to use**: The data exporter is a processor and the data importer is the controller whose data is being returned or transferred.

**Typical scenarios at Athena Global Logistics**:
- Returning processed analytics results to a non-EU client controller who originally provided the raw shipment data
- A European cloud processor returning personal data to its non-EU controller client upon contract termination

**Key Module 4 clauses**:
- Clause 8.1 — The importer shall process data in compliance with its obligations under the GDPR (where applicable) or equivalent standards
- Clause 8.2 — Purpose limitation and transparency obligations on the importer as controller

## Module Selection Decision Tree

```
START: Identify the role of the data EXPORTER (EU-based party)
  |
  ├── Exporter is a CONTROLLER
  |     |
  |     ├── Importer determines its OWN purposes → MODULE 1 (C2C)
  |     |
  |     └── Importer processes ON BEHALF of exporter → MODULE 2 (C2P)
  |
  └── Exporter is a PROCESSOR
        |
        ├── Importer is a SUB-PROCESSOR → MODULE 3 (P2P)
        |
        └── Importer is the CONTROLLER (data return) → MODULE 4 (P2C)
```

## Annex I: List of Parties and Transfer Details

### Section A — List of Parties

| Field | Data Exporter | Data Importer |
|-------|--------------|---------------|
| Name | Athena Global Logistics GmbH | TransPacific Freight Solutions Ltd |
| Address | Friedrichstrasse 112, 10117 Berlin, Germany | 88 Harbour Road, Wan Chai, Hong Kong SAR |
| Contact person | Elisa Brandt, Head of Data Protection | James Leung, Chief Privacy Officer |
| Activities relevant to transfer | International freight forwarding, customs brokerage, warehouse management for European operations | Regional freight consolidation, last-mile delivery coordination, customs clearance for Asia-Pacific operations |
| Role | Controller | Processor (Module 2) |

### Section B — Description of Transfer

| Element | Detail |
|---------|--------|
| Categories of data subjects | Shipping customers (consignors and consignees), employees of customer companies, customs brokers, warehouse workers |
| Categories of personal data | Full name, business email, business phone number, company name, shipping address, customs identification numbers, consignment reference numbers, delivery scheduling preferences |
| Sensitive data | None transferred under this agreement |
| Frequency of transfer | Continuous real-time transfer via API integration; batch file transfer daily at 02:00 UTC |
| Nature of processing | Storage, retrieval, matching of consignment records, generation of customs documentation, delivery status tracking, exception reporting |
| Purpose of transfer | Fulfilment of freight forwarding contracts requiring regional processing of shipment data for customs clearance and last-mile delivery in Asia-Pacific jurisdictions |
| Retention period | 36 months from completion of the relevant shipment, after which data is securely deleted in accordance with Annex III procedures |

### Section C — Competent Supervisory Authority

The competent supervisory authority is the **Berliner Beauftragte für Datenschutz und Informationsfreiheit (BlnBDI)**, identified in accordance with Clause 13 as the supervisory authority of the Member State in which the data exporter is established.

## Annex II: Technical and Organisational Measures

| Measure Category | Specific Measures Implemented |
|-----------------|------------------------------|
| Encryption of data in transit | TLS 1.3 for all API communications; SFTP with AES-256 encryption for batch transfers |
| Encryption of data at rest | AES-256 encryption on all database storage volumes; encrypted backup tapes with separate key management |
| Access control | Role-based access control (RBAC) with least-privilege principle; multi-factor authentication for all administrative access; quarterly access reviews |
| Data minimisation | API payloads stripped of fields not required for the specific processing purpose; data masking applied to non-essential personal identifiers in development and testing environments |
| Logging and monitoring | Centralised SIEM with 12-month log retention; real-time alerting on anomalous access patterns; daily log review by security operations centre |
| Incident response | Documented incident response plan with 24-hour initial assessment SLA; notification to data exporter within 48 hours of confirmed breach; annual tabletop exercises |
| Physical security | ISO 27001-certified data centres; biometric access controls; 24/7 CCTV surveillance; clean desk policy in processing areas |
| Business continuity | RPO of 4 hours and RTO of 8 hours; geographically separated disaster recovery site; annual DR testing with documented results |
| Staff measures | Mandatory data protection training upon onboarding and annually thereafter; background checks for all staff with access to personal data; confidentiality agreements |
| Sub-processor management | Due diligence assessment before engagement; contractual flow-down of equivalent security obligations; annual audit of sub-processor compliance |

## Annex III: List of Sub-Processors

| Sub-Processor | Location | Processing Activity | Safeguard Mechanism |
|--------------|----------|-------------------|-------------------|
| CloudVault Asia Pte Ltd | Singapore | Cloud infrastructure hosting for the regional freight management platform | SCCs Module 3 (P2P) executed 15 March 2025 |
| Pinnacle Data Services Co Ltd | Bangkok, Thailand | Data entry and validation for customs documentation | SCCs Module 3 (P2P) executed 22 January 2025 |

## Clause-by-Clause Implementation Checklist

### Section I — General Clauses (All Modules)

| Clause | Subject | Implementation Action |
|--------|---------|----------------------|
| Clause 1 | Purpose and scope | Confirm selected module is recorded in the preamble; verify parties have initialled the correct module |
| Clause 2 | Effect and invariability | Verify no modifications to the standard text; confirm any additional safeguards are in a separate addendum, not in the SCC body |
| Clause 3 | Third-party beneficiaries | Confirm data subjects can enforce Clauses 1-3, 8, 9, 12, 15-17 as third-party beneficiaries |
| Clause 4 | Interpretation | Confirm interpretation aligned with GDPR; terms have the same meaning as in the Regulation |
| Clause 5 | Hierarchy | Verify that in case of contradiction, the SCCs prevail over other contractual arrangements |
| Clause 6 | Description of transfer | Verify Annex I.B is complete with all required elements |
| Clause 7 | Docking clause | Determine if additional parties will accede; if so, prepare Annex I.A amendment procedure |

### Section II — Obligations of the Parties

| Clause | Subject | Implementation Action |
|--------|---------|----------------------|
| Clause 8 | Data protection safeguards | Module-specific; verify all sub-clauses completed per selected module |
| Clause 9 | Use of sub-processors | Module 2/3: Document prior authorisation mechanism (specific or general); maintain sub-processor list; establish notification procedure for changes |
| Clause 10 | Data subject rights | Establish procedure for the importer to handle data subject requests; define response timelines (within 30 days per GDPR Art. 12(3)) |
| Clause 11 | Redress | Confirm independent dispute resolution body identified; verify importer will accept jurisdiction of competent courts |
| Clause 12 | Liability | Confirm liability allocation between parties; verify insurance or financial capacity to meet potential claims |

### Section III — Local Laws and Government Access

| Clause | Subject | Implementation Action |
|--------|---------|----------------------|
| Clause 14 | Local laws affecting compliance | Document the Transfer Impact Assessment results; identify specific laws in the importer's jurisdiction that may impinge on SCC protections |
| Clause 15 | Government access obligations | Importer must notify exporter of government access requests (unless legally prohibited); importer must challenge disproportionate requests; importer must provide transparency report |

### Section IV — Final Provisions

| Clause | Subject | Implementation Action |
|--------|---------|----------------------|
| Clause 16 | Non-compliance and termination | Establish escalation procedure: notification → 30-day cure period → suspension → termination; data return or deletion upon termination |
| Clause 17 | Governing law | Select law of the EU Member State of the exporter (Germany, for Athena Global Logistics) |
| Clause 18 | Choice of forum and jurisdiction | Select courts of the EU Member State of the exporter (Berlin, Germany) |

## SCC Execution and Record-Keeping

1. **Version control**: Maintain a register of all executed SCCs with version numbers, execution dates, parties, and selected modules.
2. **Periodic review**: Review all executed SCCs at least annually or upon any material change in processing, importer jurisdiction law, or sub-processor arrangements.
3. **Regulatory updates**: Monitor EDPB guidance and European Commission updates for any revision to the SCC instrument or supplementary guidance.
4. **Integration with TIA**: Each SCC must reference the corresponding Transfer Impact Assessment documenting the assessment of the importer's jurisdiction under Clause 14.
5. **Supervisory authority cooperation**: Maintain readiness to provide all SCC documentation to the competent supervisory authority upon request under Art. 46(2)(c) and Art. 58(1).
