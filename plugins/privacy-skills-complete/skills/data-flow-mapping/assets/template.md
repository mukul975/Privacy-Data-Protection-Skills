# International Data Flow Mapping — Inventory Template

## Organisation

| Field | Value |
|-------|-------|
| Organisation | Athena Global Logistics GmbH |
| Mapping Date | March 2025 |
| Mapped By | Elisa Brandt, Head of Data Protection |
| Scope | Group-wide (all subsidiaries and third-party processors) |

## System Inventory

| System | Vendor | Hosting Location | Data Categories | System Owner |
|--------|--------|-----------------|-----------------|-------------|
| SAP S/4HANA | SAP SE | Frankfurt DC (on-premise) | Employee, customer, supplier, financial | IT Operations |
| CargoWise One | WiseTech Global | Sydney (SaaS) | Customer shipment, consignee, customs | Freight Operations |
| Salesforce | Salesforce Inc | Frankfurt (SaaS EU DC) | Customer contacts, sales pipeline | Sales |
| Workday | Workday Inc | Dublin (SaaS EU DC) | Employee HR, payroll, benefits | Human Resources |
| Microsoft 365 | Microsoft Corp | EU DC (SaaS) | Employee email, files, contacts | IT Operations |
| Fleetio | Fleetio Inc | Atlanta, US (SaaS) | Driver names, licences, GPS | Fleet Management |
| Custom Portal | Internal | Frankfurt DC | Customer logins, shipment tracking | IT Development |

## Data Flow Register

| Flow ID | Source | Source Country | Destination | Dest Country | Data Categories | Mechanism | TIA Ref | Status |
|---------|--------|---------------|-------------|-------------|----------------|-----------|---------|--------|
| DF-001 | SAP | Germany | Athena HK | Hong Kong SAR | Customer data | SCCs Mod 1 | TIA-2025-HK-001 | Compliant |
| DF-002 | CargoWise | Australia | Athena GmbH | Germany | Shipment data | Inbound; no Ch.V | N/A | N/A |
| DF-003 | Workday | Ireland | Workday US backup | United States | Employee HR | EU-US DPF | N/A (adequacy) | Compliant |
| DF-004 | Fleetio | Germany | Fleetio Inc | United States | Driver data | None | None | GAP — Critical |
| DF-005 | SAP | Germany | Athena India | India | Employee payroll | SCCs Mod 1 | None | GAP — TIA missing |
| DF-006 | Portal | Germany | TransPacific | Hong Kong SAR | Customer data | SCCs Mod 2 | TIA-2025-HK-001 | Compliant |
| DF-007 | M365 | EU | Microsoft US | United States | Employee email | EU-US DPF | N/A (adequacy) | Compliant |
| DF-008 | M365 | EU | Microsoft SG | Singapore | Employee email | SCCs | TIA-2025-SG-001 | Compliant |

## Gap Analysis Summary

| Gap ID | Flow | Issue | Severity | Remediation | Owner | Target Date |
|--------|------|-------|----------|-------------|-------|-------------|
| GAP-001 | DF-004 | No transfer mechanism for Fleetio (US) | Critical | Verify Fleetio DPF certification or execute SCCs Module 2 | DPO Office | 15 April 2025 |
| GAP-002 | DF-005 | SCCs in place but TIA not documented for India transfer | High | Complete TIA-2025-IN-001 | Privacy Counsel | 30 April 2025 |

## Third-Party Recipients Summary

| Recipient | Country | Role | Flows | Mechanism | Contract |
|-----------|---------|------|-------|-----------|----------|
| TransPacific Freight Solutions Ltd | Hong Kong SAR | Processor | DF-006 | SCCs Mod 2 | DPA-2025-001 |
| Athena Logistics (HK) Ltd | Hong Kong SAR | Controller (intra-group) | DF-001 | SCCs Mod 1 | IGA-2024-001 |
| Athena Freight Services India Pvt Ltd | India | Controller (intra-group) | DF-005 | SCCs Mod 1 | IGA-2024-005 |
| Workday Inc | US (backup) | Processor | DF-003 | EU-US DPF | DPA-WD-2024-001 |
| Fleetio Inc | United States | Processor | DF-004 | None (GAP) | DPA-FL-2024-003 |
| Microsoft Corporation | US, Singapore | Processor | DF-007, DF-008 | DPF (US), SCCs (SG) | DPA-MS-2024-001 |

## Data Flow Visualisation Summary

| Destination Region | Flow Count | Adequate | Non-Adequate | Gaps |
|-------------------|------------|----------|-------------|------|
| Asia-Pacific (HK, SG, AU, IN) | 4 | 0 | 4 | 1 (TIA missing) |
| North America (US) | 3 | 2 (DPF) | 1 | 1 (no mechanism) |
| Europe (DE, IE) | Internal only | N/A | N/A | 0 |

## Next Steps

| Action | Timeline |
|--------|----------|
| Remediate GAP-001 (Fleetio mechanism) | By 15 April 2025 |
| Complete TIA for India transfer (GAP-002) | By 30 April 2025 |
| Annual full inventory review | March 2026 |
| Quarterly flow register review | June 2025 |
