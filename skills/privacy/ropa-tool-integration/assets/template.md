# RoPA Tool Integration Assessment — Helix Biotech Solutions GmbH

**Assessment Date**: 2025-01-15
**Assessed By**: Dr. Elena Voss, Data Protection Officer
**Current RoPA Management Method**: Microsoft Excel (multiple workbooks across departments)

---

## Current State Assessment

### Existing RoPA Inventory

| Metric | Value |
|--------|-------|
| Total processing activities recorded | 47 |
| Controller records (Art. 30(1)) | 38 |
| Processor records (Art. 30(2)) | 9 |
| Entities covered | 3 (GmbH, Ltd, Shared Services B.V.) |
| Processing owners | 14 assigned owners |
| Current storage format | Excel workbooks on SharePoint |
| Last full review date | 2024-09-20 |
| Average completeness score | 72.4% |

### Pain Points with Current Approach

- [x] Manual updates are error-prone and frequently delayed
- [x] No automated staleness detection or review reminders
- [x] Version history is incomplete or non-existent
- [x] No audit trail for changes
- [x] Cannot generate supervisory authority-formatted exports
- [x] No integration with IT change management
- [x] No integration with vendor management
- [x] Multiple spreadsheets across departments with inconsistencies
- [x] Cannot support multi-entity group structure
- [x] Reporting and dashboards require manual effort

---

## Platform Requirements

### Functional Requirements

| Requirement | Priority | Notes |
|-------------|----------|-------|
| Full Art. 30(1) field support (all 7 fields) | Must have | All 7 mandatory controller fields |
| Full Art. 30(2) field support (all 4 fields) | Must have | 9 processor records to migrate |
| Multi-entity support | Must have | 6 entities (including pending Diagnostics S.A.S. acquisition) |
| Approval workflows | Must have | DPO and processing owner dual approval |
| Version control with audit trail | Must have | BayLDA previously requested change history |
| Automated review reminders | Must have | Currently no reminders leading to 34% staleness |
| Supervisory authority export templates | Should have | BfDI, CNIL, ICO (3 SAs across group) |
| DPIA module linkage | Should have | 6 active DPIAs require cross-referencing |
| Vendor/processor management linkage | Should have | 23 external processors under DPA |
| Data discovery/automated population | Nice to have | For post-acquisition discovery |
| Custom fields | Should have | Clinical trial-specific fields needed |
| Multi-language support | Must have | German, English, French (Diagnostics S.A.S.) |

### Integration Requirements

| System | Integration Type | Priority |
|--------|-----------------|----------|
| Azure AD via Okta (SSO + org sync) | SAML 2.0 + SCIM | Must have |
| ServiceNow (IT change mgmt) | Webhook on change request closure | Should have |
| SAP Ariba (vendor management) | API sync for new vendor onboarding | Should have |
| Collibra Data Catalog | API for data lineage enrichment | Nice to have |
| Archer GRC platform | Export for quarterly risk reporting | Nice to have |

### Technical Requirements

| Requirement | Specification |
|-------------|--------------|
| Hosting model | SaaS (EU-hosted) or hybrid with on-premises option |
| Data residency | EU (EEA) required — Frankfurt (eu-central-1) or Amsterdam preferred |
| Encryption at rest | AES-256 minimum |
| API availability | REST API with OAuth 2.0 |
| Uptime SLA | 99.9% minimum |
| Backup and recovery | Daily backups, RPO < 24h, RTO < 4h |
| Security certifications | ISO 27001 and SOC 2 Type II required |

---

## Platform Evaluation Scorecard

| Criterion | Weight | OneTrust | TrustArc | Collibra | DataGrail |
|-----------|--------|----------|----------|----------|-----------|
| Art. 30 field coverage | 20% | 5/5 | 4/5 | 4/5 | 3/5 |
| Multi-entity support | 10% | 5/5 | 4/5 | 5/5 | 3/5 |
| API capability | 15% | 5/5 | 3/5 | 5/5 | 4/5 |
| Workflow automation | 15% | 5/5 | 4/5 | 3/5 | 3/5 |
| Integration ecosystem | 10% | 5/5 | 3/5 | 4/5 | 4/5 |
| SA template support | 10% | 5/5 | 4/5 | 2/5 | 2/5 |
| Ease of use | 10% | 3/5 | 4/5 | 3/5 | 4/5 |
| Total cost (3-year) | 10% | 2/5 | 3/5 | 2/5 | 4/5 |
| **Weighted Total** | **100%** | **4.45/5** | **3.65/5** | **3.55/5** | **3.35/5** |

---

## Migration Plan

| Phase | Duration | Key Activities |
|-------|----------|---------------|
| 1. Contract and setup | 2 weeks | DPA execution with OneTrust, tenant provisioning (EU-hosted), SSO via Okta |
| 2. Configuration | 4 weeks | Custom fields for clinical trials, BfDI/CNIL/ICO export templates, approval workflows |
| 3. Integration | 3 weeks | Okta SCIM sync, ServiceNow webhook, SAP Ariba vendor feed |
| 4. Data migration | 2 weeks | CSV export from 6 Excel workbooks, import to OneTrust, field mapping validation |
| 5. Testing | 2 weeks | UAT with DPO office (3 users) and 5 processing owners from HR, Clinical, IT, Finance, Sales |
| 6. Training | 1 week | DPO office admin training (8 hours), processing owner self-service training (2 hours) |
| 7. Go-live | 1 week | Production cutover, Excel workbooks archived to SharePoint read-only, monitoring |

---

## Decision

**Selected Platform**: OneTrust Privacy Management
**Decision Date**: 2025-02-10
**Approved By**: Dr. Martin Keller, Chief Financial Officer
**Budget Approved**: EUR 142,000 (3-year SaaS license + implementation services)
**Target Go-Live Date**: 2025-06-15
