---
name: data-flow-mapping
description: >-
  Guides systematic mapping of international personal data flows across an
  organisation. Covers system-by-system inventory methodology, third-party
  identification, transfer mechanism assignment, gap analysis, and data flow
  visualisation. Keywords: data flow mapping, international transfers, data
  inventory, transfer register, cross-border data flows.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cross-border-transfers
  tags: "data-flow-mapping, international-transfers, data-inventory, transfer-register, gap-analysis"
---

# Mapping International Data Flows

## Overview

A comprehensive international data flow map is the foundational prerequisite for any cross-border transfer compliance programme. GDPR Article 30 requires controllers and processors to document transfers to third countries or international organisations. Beyond regulatory compliance, a data flow inventory enables identification of unprotected transfers, assignment of appropriate transfer mechanisms, and ongoing monitoring of data movement across jurisdictions. This skill provides a structured methodology for conducting a system-by-system data flow inventory, identifying all third-party recipients, assigning transfer mechanisms, and performing gap analysis.

## Data Flow Inventory Methodology

### Phase 1: System Inventory

Identify every information system, application, and service that processes personal data within the organisation.

**System categories at Athena Global Logistics**:

| Category | Systems | Personal Data Processed |
|----------|---------|----------------------|
| Enterprise Resource Planning | SAP S/4HANA (hosted Frankfurt DC) | Employee data, customer data, supplier data, financial data |
| Transport Management | CargoWise One (SaaS, hosted Sydney) | Customer shipment data, consignee data, customs broker contacts |
| Customer Relationship Management | Salesforce (SaaS, hosted Frankfurt) | Customer contacts, communication history, sales pipeline |
| Human Resources | Workday (SaaS, hosted Dublin) | Employee personal data, payroll, benefits, performance, recruitment |
| Email and Collaboration | Microsoft 365 (SaaS, hosted EU DC) | Employee communications, contacts, calendar, file storage |
| Warehouse Management | Manhattan Associates (hosted Frankfurt DC) | Warehouse worker IDs, shift schedules, access logs |
| Fleet Management | Fleetio (SaaS, hosted US) | Driver names, licence numbers, GPS tracking data, vehicle assignments |
| Customer Portal | Custom web application (hosted Frankfurt DC) | Customer login credentials, shipment tracking, document uploads |
| Analytics Platform | Snowflake (SaaS, hosted Frankfurt) | Aggregated operational data, pseudonymised customer analytics |
| IT Service Management | ServiceNow (SaaS, hosted Amsterdam) | Employee IT tickets, contact details, device assignments |

### Phase 2: Data Flow Identification

For each system, trace every flow of personal data that crosses a national border.

**Data flow tracing methodology**:

1. **Inbound flows**: Where does personal data enter the system from? (user input, API integrations, file imports, email)
2. **Internal processing**: Where is data stored and processed? (primary data centre, disaster recovery site, development/test environments)
3. **Outbound flows**: Where does personal data leave the system to? (third-party integrations, data exports, email transmissions, backup replication)
4. **Sub-processor chains**: For SaaS systems, identify the provider's sub-processors and their locations.
5. **Support access**: Identify any remote support arrangements where third-country support staff may access personal data.

**Athena Global Logistics example data flow register (excerpt)**:

| Flow ID | Source System | Source Location | Destination | Destination Country | Data Categories | Legal Basis for Processing | Transfer Mechanism |
|---------|-------------|----------------|-------------|--------------------|-----------------|--------------------------|--------------------|
| DF-001 | SAP S/4HANA | Frankfurt, DE | Athena Logistics (HK) Ltd — local SAP instance | Hong Kong SAR | Customer names, addresses, consignment data | Art. 6(1)(b) contract | SCCs Module 1 |
| DF-002 | CargoWise One | Sydney, AU | Athena Global Logistics GmbH — API pull | Australia | Shipment status, consignee details | Art. 6(1)(b) contract | EU adequacy decision (implied — no decision for AU; SCCs Module 2 required) |
| DF-003 | Workday | Dublin, IE | Workday Inc sub-processor (US backup DC) | United States | Employee HR data | Art. 6(1)(b) employment contract | EU-US DPF + SCCs backup |
| DF-004 | Fleetio | Atlanta, US | N/A (primary processing in US) | United States | Driver names, licence numbers, GPS data | Art. 6(1)(f) legitimate interest | EU-US DPF (verify certification) |
| DF-005 | SAP S/4HANA | Frankfurt, DE | Athena Freight Services India — SFTP batch | India | Employee data (payroll, benefits) | Art. 6(1)(b) employment contract | SCCs Module 1 |
| DF-006 | Custom portal | Frankfurt, DE | TransPacific Freight Solutions — API | Hong Kong SAR | Customer shipment data | Art. 6(1)(b) contract | SCCs Module 2 |
| DF-007 | Microsoft 365 | EU DC | Microsoft Corp sub-processors (global) | Multiple (US, SG, IE) | Employee emails, files | Art. 6(1)(b) contract | EU-US DPF (US); SCCs (SG) |

### Phase 3: Third-Party Identification

Catalogue all third parties (processors, sub-processors, joint controllers, independent controllers) that receive personal data through international transfers.

| Third Party | Role | Country | Data Received | Purpose | Contract Reference |
|------------|------|---------|--------------|---------|-------------------|
| TransPacific Freight Solutions Ltd | Processor | Hong Kong SAR | Customer shipment data | Freight consolidation and customs clearance | DPA-2025-001 |
| CloudVault Asia Pte Ltd | Sub-processor (of TransPacific) | Singapore | Customer shipment data (hosting) | Cloud infrastructure | Sub-processor agreement via TransPacific |
| Pinnacle Data Services Co Ltd | Sub-processor (of TransPacific) | Thailand | Customs documentation data | Data entry and validation | Sub-processor agreement via TransPacific |
| Athena Freight Services India Pvt Ltd | Controller (intra-group) | India | Employee HR data | Local employment administration | Intra-group DPA-2024-005 |
| Workday Inc | Processor | Ireland (primary), US (backup) | Employee HR data | HRIS platform | DPA-WD-2024-001 |
| Fleetio Inc | Processor | United States | Driver data | Fleet management | DPA-FL-2024-003 |
| Microsoft Corporation | Processor | EU, US, Singapore | Employee email and files | Email and collaboration | DPA-MS-2024-001 |

### Phase 4: Transfer Mechanism Assignment

For each identified international data flow, assign the appropriate transfer mechanism:

```
For each flow:
  1. Check: Does the destination have an EU adequacy decision?
     → YES: Record "Adequacy Decision" as mechanism. Done.
     → NO: Continue.
  2. Check: Is the importer DPF-certified (for US transfers)?
     → YES: Record "EU-US DPF" as mechanism. Recommend SCCs as backup.
     → NO: Continue.
  3. Check: Are SCCs in place between the parties?
     → YES: Record "SCCs Module X" as mechanism. Verify TIA completed.
     → NO: Continue.
  4. Check: Are BCRs in place covering the transfer?
     → YES: Record "BCRs" as mechanism. Verify scope covers the data.
     → NO: Continue.
  5. Check: Does an Art. 49 derogation apply?
     → YES: Record "Art. 49(1)(x)" as mechanism. Document justification.
     → NO: FLAG AS UNPROTECTED TRANSFER — immediate action required.
```

### Phase 5: Gap Analysis

Identify transfers that lack a valid transfer mechanism:

| Gap Type | Description | Priority | Remediation |
|----------|-----------|----------|-------------|
| No mechanism | Transfer occurring without any Art. 45/46/49 basis | Critical | Suspend transfer or execute SCCs within 30 days |
| Expired mechanism | SCCs based on superseded 2010/2021 versions; DPF certification expired | High | Renew mechanism within 60 days |
| Missing TIA | SCCs in place but no documented TIA | High | Complete TIA within 30 days |
| Incomplete documentation | Mechanism exists but Annex fields are incomplete | Medium | Complete documentation within 60 days |
| Sub-processor gap | Importer uses sub-processors not covered by SCCs | High | Extend SCC coverage or require importer to execute Module 3 SCCs |
| Undiscovered flow | Data flow identified during mapping that was not previously known | High | Assess, assign mechanism, and document within 30 days |

## Data Flow Visualisation

### Visualisation Approaches

1. **Geo-map visualisation**: Plot data flows on a world map with colour-coded lines:
   - Green: Transfer covered by adequacy decision
   - Blue: Transfer covered by SCCs/BCRs with completed TIA
   - Yellow: Transfer covered by mechanism but TIA pending or in review
   - Red: Transfer lacking valid mechanism — immediate action required

2. **System-centric diagram**: For each major system, draw a diagram showing all inbound and outbound data flows with destination countries and mechanisms.

3. **Third-party relationship map**: Network diagram showing the organisation at the centre with all third parties and data flows radiating outward, grouped by jurisdiction.

4. **Transfer register dashboard**: Tabular view with filtering by mechanism type, destination country, risk level, and review status.

## Ongoing Maintenance

1. **Trigger-based updates**: Re-map data flows upon: new system implementation, new vendor onboarding, corporate restructuring, new country operations, new data categories.
2. **Periodic review**: Full data flow inventory review at least annually.
3. **Automated discovery**: Implement network monitoring and data loss prevention (DLP) tools to detect undocumented cross-border data flows.
4. **Integration with RoPA**: Data flow map feeds directly into the Art. 30 Records of Processing Activities.
5. **Integration with vendor register**: Third-party data recipients map feeds into the vendor management and DPA tracking system.
