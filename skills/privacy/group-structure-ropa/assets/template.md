# Group RoPA Entity Register — Helix Biotech Holdings SE

**Group Name**: Helix Biotech Holdings SE
**Group DPO**: Dr. Elena Voss, dpo@helix-biotech.eu
**Last Updated**: [YYYY-MM-DD]

---

## Entity Inventory

| # | Entity Legal Name | Country | Registration | Role | DPO / Privacy Lead | Lead SA | RoPA Status |
|---|------------------|---------|-------------|------|-------------------|---------|-------------|
| 1 | Helix Biotech Holdings SE | Netherlands | KvK 12345678 | Controller (minimal) | Dr. Elena Voss | AP Netherlands | Current |
| 2 | Helix Biotech Solutions GmbH | Germany | HRB 267891 | Controller + Processor | Dr. Elena Voss | BayLDA | Current |
| 3 | Helix Biotech Solutions Ltd | United Kingdom | Co. 87654321 | Controller | James Walker | ICO | Current |
| 4 | Helix Biotech Solutions Inc. | United States | DE Corp. 54321 | Controller + Processor | Sarah Chen | N/A (no federal DPA) | Current |
| 5 | Helix Shared Services B.V. | Netherlands | KvK 11223344 | Controller + Processor | Dr. Elena Voss | AP Netherlands | Current |
| 6 | Helix Biotech Diagnostics S.A.S. | France | RCS Paris 556677 | Controller | Pierre Laurent | CNIL | Integration in progress |

---

## Intra-Group Data Flow Register

| # | Source Entity | Destination Entity | Data Type | Relationship | DPA/JCA Reference | Transfer Mechanism |
|---|-------------|-------------------|-----------|-------------|-------------------|--------------------|
| 1 | GmbH | Shared Services B.V. | Employee payroll data | Controller-to-Processor | DPA-IG-2024-SSC-DE-001 | Intra-EEA (no mechanism needed) |
| 2 | Ltd | Shared Services B.V. | Employee payroll data | Controller-to-Processor | DPA-IG-2024-SSC-UK-002 | UK adequacy decision |
| 3 | Inc. | GmbH | Pharmacovigilance reports | Processor-to-Controller | DPA-IG-2024-PV-US-001 | EU SCCs Module 4 |
| 4 | GmbH | Ltd | Clinical trial data | Joint Controllers | JCA-2024-CT-001 | UK adequacy decision |
| 5 | GmbH | Inc. | Employee directory | Controller-to-Controller | LIA-2024-DIR-001 | BCR-HELIX-2024-001 |

---

## Intra-Group Agreement Register

| # | Agreement Type | Reference | Parties | Executed | Expiry | Status |
|---|---------------|-----------|---------|----------|--------|--------|
| 1 | Art. 28 DPA | DPA-IG-2024-SSC-DE-001 | GmbH (controller) — Shared Services B.V. (processor) | 2024-01-15 | 2027-01-14 | Active |
| 2 | Art. 28 DPA | DPA-IG-2024-SSC-UK-002 | Ltd (controller) — Shared Services B.V. (processor) | 2024-02-01 | 2027-01-31 | Active |
| 3 | Art. 26 JCA | JCA-2024-CT-001 | GmbH + Ltd (joint controllers for multi-country trials) | 2024-03-01 | Indefinite (term of clinical programme) | Active |
| 4 | BCR-C | BCR-HELIX-2024-001 | All group entities (controller transfers) | 2024-06-01 | Approved by BfDI | Active |

---

## Entity-Level RoPA Summary

### Helix Biotech Solutions GmbH (Germany)

| Record ID | Processing Activity | Data Subjects | Special Category | DPIA |
|-----------|---------------------|---------------|-----------------|------|
| DE-RPA-001 | Employee payroll | Employees | Church tax (religion) | No |
| DE-RPA-002 | Clinical trial data management | Trial participants | Health, genetic | Yes (DPIA-2024-ONC-04) |
| DE-RPA-003 | Website analytics | Website visitors | None | No |
| DE-RPA-004 | Customer CRM | B2B customers | None | No |
| DE-RPA-005 | Pharmacovigilance | Patients, HCPs | Health | Yes (DPIA-2024-PV-001) |

*[Repeat for each entity]*

---

*This register provides the group consolidated view. Each entity maintains its own Art. 30 records independently. This document does not substitute for entity-level RoPA obligations.*
