---
name: group-structure-ropa
description: >-
  Manages RoPA for complex multi-entity corporate groups including entity-level
  versus group-level records, intra-group transfer documentation, and shared
  processing coordination. Activate for group RoPA, multi-entity, corporate
  group, intra-group transfers, subsidiary records, holding company.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: records-of-processing
  tags: "gdpr, ropa, corporate-group, multi-entity, intra-group-transfers, subsidiary, holding"
---

# Group Structure RoPA

## Overview

GDPR Art. 30 applies to each controller and each processor individually. In a corporate group comprising a holding company, operating subsidiaries, shared service centres, and joint ventures, each entity that independently determines purposes and means of processing must maintain its own Art. 30(1) records. Entities acting as processors for group companies must maintain Art. 30(2) records. This skill addresses the complexities of group-level RoPA management including entity hierarchy, intra-group data flows, shared processing activities, and consolidated governance.

## Corporate Group Structure — Helix Biotech Solutions

```
Helix Biotech Holdings SE (Netherlands — Holding)
├── Helix Biotech Solutions GmbH (Germany — Primary Operating Entity)
│   ├── Controller for: own employees, clinical trials, marketing
│   └── Processor for: group shared services (see below)
├── Helix Biotech Solutions Ltd (United Kingdom — UK Subsidiary)
│   ├── Controller for: own employees, UK customer data, UK clinical sites
│   └── Joint controller with GmbH for: multi-country clinical trials
├── Helix Biotech Solutions Inc. (United States — US Subsidiary)
│   ├── Controller for: own employees, US customer data
│   └── Processor for: global pharmacovigilance data processing (under GmbH instruction)
├── Helix Shared Services B.V. (Netherlands — Shared Service Centre)
│   ├── Processor for: group-wide IT infrastructure, payroll processing
│   └── Controller for: own employees only
└── Helix Biotech Diagnostics S.A.S. (France — Acquired Entity)
    ├── Controller for: own employees, diagnostic service customers
    └── Integration pending — separate RoPA maintained
```

## Entity-Level vs Group-Level Records

### Entity-Level RoPA (Required)

Each legal entity must maintain its own RoPA containing processing activities for which it is controller or processor. This is a legal obligation that cannot be satisfied by a group-level record alone.

| Entity | Controller RoPA (Art. 30(1)) | Processor RoPA (Art. 30(2)) |
|--------|------------------------------|------------------------------|
| Helix Biotech Holdings SE | Minimal — shareholder data, board member data | None |
| Helix Biotech Solutions GmbH | Full — all German processing activities | Yes — shared services provided to group |
| Helix Biotech Solutions Ltd | Full — all UK processing activities | None |
| Helix Biotech Solutions Inc. | Full — all US processing activities | Yes — pharmacovigilance processing for GmbH |
| Helix Shared Services B.V. | Minimal — own employee data only | Yes — IT, HR, and finance processing for all group entities |
| Helix Biotech Diagnostics S.A.S. | Full — all French processing activities | None |

### Group-Level Consolidated View (Recommended)

In addition to entity-level records, maintain a consolidated group view that:

1. Aggregates all entity-level RoPA entries into a single searchable register.
2. Highlights intra-group data flows and transfer arrangements.
3. Identifies shared processing activities and joint controller arrangements.
4. Supports group-level reporting to the board and supervisory authorities.
5. Enables gap analysis across entities (e.g., one entity has incomplete records).

The consolidated view is not a legal substitute for entity-level records but serves governance and oversight purposes.

## Intra-Group Data Flows

### Controller-to-Controller Transfers

When one group entity transfers personal data to another group entity and each determines its own purpose for the processing, this is a controller-to-controller transfer requiring:

- **Legal basis**: Art. 6(1) lawful basis for the disclosure (typically Art. 6(1)(f) legitimate interest with intra-group LIA)
- **Transfer mechanism**: If the receiving entity is outside the EEA, an appropriate Chapter V safeguard (SCCs, BCRs, adequacy decision)
- **RoPA documentation**: Both entities must record the transfer in their respective RoPAs — the disclosing entity as a recipient under Art. 30(1)(d), the receiving entity as data source documentation

**Example:**

Helix Biotech Solutions GmbH (Germany) shares employee directory data with Helix Biotech Solutions Inc. (US) for internal communications.

| Aspect | GmbH (Disclosing Controller) | Inc. (Receiving Controller) |
|--------|------------------------------|------------------------------|
| Purpose | Enable employee collaboration across group | Maintain employee directory for US operations |
| Lawful basis | Art. 6(1)(f) — legitimate interest (Recital 48: intra-group transfers) | Art. 6(1)(f) — legitimate interest |
| RoPA field | Art. 30(1)(d): Recipient = Helix Biotech Solutions Inc.; Art. 30(1)(e): US transfer | Art. 30(1)(c): Data source = Helix Biotech Solutions GmbH |
| Transfer mechanism | EU-US Data Privacy Framework (if Inc. is DPF-listed) OR EU SCCs Module 1 (controller-to-controller) | — |
| LIA reference | LIA-2024-DIR-001 | LIA-2024-DIR-002 |

### Controller-to-Processor Transfers (Intra-Group)

When a group shared service centre processes data on behalf of another group entity, the relationship is controller-to-processor even though both entities are in the same corporate group:

- **Art. 28 DPA required**: An intra-group DPA is required between the controller entity and the processor entity, even within the same group.
- **RoPA documentation**: The controller entity records the shared service centre as a processor in Art. 30(1)(d). The shared service centre records the controller entity in its Art. 30(2)(a) processor records.

**Example:**

Helix Shared Services B.V. (Netherlands) processes payroll for all group entities.

| Controller Entity | DPA Reference | Processing Categories | Data Categories |
|------------------|---------------|----------------------|-----------------|
| Helix Biotech Solutions GmbH | DPA-IG-2024-SSC-DE-001 | Payroll calculation, tax reporting, social security reporting | Employee names, tax IDs, bank accounts, salaries |
| Helix Biotech Solutions Ltd | DPA-IG-2024-SSC-UK-002 | Payroll calculation, HMRC reporting, pension contributions | Employee names, NI numbers, bank accounts, salaries |
| Helix Biotech Solutions Inc. | DPA-IG-2024-SSC-US-003 | Payroll calculation, IRS reporting, benefits administration | Employee names, SSNs, bank accounts, salaries |

### Joint Controller Arrangements (Art. 26)

When two or more group entities jointly determine the purposes and means of processing, they are joint controllers under Art. 26:

- **Art. 26 arrangement required**: Formal arrangement determining respective responsibilities.
- **RoPA documentation**: Each joint controller records the arrangement in Art. 30(1)(a) with cross-reference to the Art. 26 arrangement.

**Example:**

Helix Biotech Solutions GmbH and Helix Biotech Solutions Ltd jointly conduct multi-country clinical trials and jointly determine the trial protocol, data collection methods, and analysis purposes.

| Aspect | GmbH | Ltd |
|--------|------|-----|
| Art. 26 arrangement | JCA-2024-CT-001 | JCA-2024-CT-001 |
| Responsibilities | Trial sponsor, EMA reporting, EU site management | UK site management, MHRA reporting |
| Contact point for data subjects | GmbH (as designated under Art. 26(1)) | GmbH (as designated) |
| RoPA Art. 30(1)(a) | Joint controller: Helix Biotech Solutions Ltd, ref: JCA-2024-CT-001 | Joint controller: Helix Biotech Solutions GmbH, ref: JCA-2024-CT-001 |

## Binding Corporate Rules (BCRs) and Group RoPA

If the group has approved BCRs under Art. 47, the RoPA transfer fields (Art. 30(1)(e)) should reference the BCRs as the transfer mechanism for intra-group transfers:

| Transfer | Mechanism | Reference |
|----------|-----------|-----------|
| GmbH to Ltd (UK) | UK adequacy decision (28 June 2021, extended) | N/A (adequacy) |
| GmbH to Inc. (US) | BCR-C ref: BCR-HELIX-2024-001 (approved by BfDI as lead SA) | BCR-HELIX-2024-001 |
| GmbH to S.A.S. (France) | Intra-EEA — no transfer mechanism required | N/A |
| Shared Services B.V. to Inc. (US) | BCR-P ref: BCR-HELIX-2024-002 (processor BCRs) | BCR-HELIX-2024-002 |

## Group RoPA Governance Model

### Centralised Governance with Local Execution

| Role | Scope | Responsible Entity |
|------|-------|-------------------|
| Group DPO | Overall RoPA governance, consolidated reporting, group-level standards | Helix Biotech Holdings SE (Dr. Elena Voss) |
| Entity Privacy Lead | Entity-level RoPA creation and maintenance | Each subsidiary |
| Shared Services Privacy Lead | Processor RoPA for all shared services | Helix Shared Services B.V. |
| Group Privacy Analyst | Consolidated view management, cross-entity gap analysis | Holdings SE |

### Governance Workflow

1. **Entity-level creation**: Each entity's privacy lead creates and maintains entity-level RoPA entries following group standards.
2. **Group template**: All entities use the same RoPA template and field definitions to ensure consistency.
3. **Centralised aggregation**: Entity-level records are aggregated into the group consolidated view quarterly.
4. **Cross-entity review**: Group DPO reviews the consolidated view for intra-group transfer completeness, joint controller arrangement consistency, and entity-level gap identification.
5. **Board reporting**: Group DPO presents consolidated RoPA metrics to the Holdings SE board annually.

### Post-Acquisition Integration

When a new entity is acquired (e.g., Helix Biotech Diagnostics S.A.S.):

1. **Immediate (Day 1)**: Identify the acquired entity's existing RoPA and assess its format, completeness, and quality.
2. **30 days**: Conduct a gap analysis against the group RoPA template and identify intra-group data flows that will be established.
3. **60 days**: Migrate the acquired entity's RoPA to the group template format.
4. **90 days**: Establish intra-group DPAs for shared services and document intra-group transfers in both entities' RoPAs.
5. **6 months**: Full integration into the group consolidated view and ongoing governance cycle.

## Common Group Structure Pitfalls

1. **Assuming a single group RoPA satisfies all entities**: Each legal entity must have its own records. A group-level consolidated view does not replace entity-level obligations.

2. **Missing intra-group DPAs**: The GDPR does not exempt intra-group processing from the Art. 28 DPA requirement. A holding company providing IT services to subsidiaries must have DPAs in place.

3. **Undocumented intra-group transfers**: Data flows between group entities (shared directories, consolidated HR systems, group-wide analytics) are transfers that must be recorded in Art. 30(1)(d) and (e).

4. **Inconsistent entity identification**: Using trade names instead of legal entity names across different entities' RoPAs creates confusion during supervisory authority inspections.

5. **Missing joint controller arrangements**: When two group entities jointly determine processing purposes (e.g., a global marketing campaign managed by two subsidiaries), an Art. 26 arrangement is required but frequently overlooked within corporate groups.

6. **One-stop-shop confusion**: The lead supervisory authority under Art. 56 is determined by the location of the main establishment, not by where most processing occurs. Group RoPA must clearly identify each entity's establishment and the lead SA for cross-border processing.
