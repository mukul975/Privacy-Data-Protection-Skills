# RoPA Tool Integration Assessment — Helix Biotech Solutions GmbH

**Assessment Date**: [YYYY-MM-DD]
**Assessed By**: [Name, Title]
**Current RoPA Management Method**: [Spreadsheet / OneTrust / TrustArc / Other]

---

## Current State Assessment

### Existing RoPA Inventory

| Metric | Value |
|--------|-------|
| Total processing activities recorded | [Number] |
| Controller records (Art. 30(1)) | [Number] |
| Processor records (Art. 30(2)) | [Number] |
| Entities covered | [Number of legal entities] |
| Processing owners | [Number of assigned owners] |
| Current storage format | [Spreadsheet / Document / Platform] |
| Last full review date | [YYYY-MM-DD] |
| Average completeness score | [Percentage] |

### Pain Points with Current Approach

- [ ] Manual updates are error-prone and frequently delayed
- [ ] No automated staleness detection or review reminders
- [ ] Version history is incomplete or non-existent
- [ ] No audit trail for changes
- [ ] Cannot generate supervisory authority-formatted exports
- [ ] No integration with IT change management
- [ ] No integration with vendor management
- [ ] Multiple spreadsheets across departments with inconsistencies
- [ ] Cannot support multi-entity group structure
- [ ] Reporting and dashboards require manual effort
- [ ] Other: [specify]

---

## Platform Requirements

### Functional Requirements

| Requirement | Priority | Notes |
|-------------|----------|-------|
| Full Art. 30(1) field support (all 7 fields) | Must have | |
| Full Art. 30(2) field support (all 4 fields) | Must have | |
| Multi-entity support | [Must/Should/Nice] | [Number of entities] |
| Approval workflows | Must have | |
| Version control with audit trail | Must have | |
| Automated review reminders | Must have | |
| Supervisory authority export templates | Should have | [Which SAs: CNIL, ICO, BfDI] |
| DPIA module linkage | Should have | |
| Vendor/processor management linkage | Should have | |
| Data discovery/automated population | Nice to have | |
| Custom fields | Should have | |
| Multi-language support | [Must/Should/Nice] | [Languages needed] |

### Integration Requirements

| System | Integration Type | Priority |
|--------|-----------------|----------|
| Azure AD / Okta (SSO + org sync) | SAML/OIDC + SCIM | Must have |
| ServiceNow / Jira (IT change mgmt) | Webhook / API | Should have |
| Vendor management system | API sync | Should have |
| Data catalog (Collibra / Alation) | API sync | Nice to have |
| GRC platform | API / export | Nice to have |

### Technical Requirements

| Requirement | Specification |
|-------------|--------------|
| Hosting model | [ ] SaaS [ ] On-premises [ ] Hybrid |
| Data residency | EU (EEA) required |
| Encryption at rest | AES-256 minimum |
| API availability | REST API with OAuth 2.0 or API key |
| Uptime SLA | 99.9% minimum |
| Backup and recovery | Daily backups, RPO < 24h, RTO < 4h |
| Security certifications | ISO 27001, SOC 2 Type II required |

---

## Platform Evaluation Scorecard

| Criterion | Weight | OneTrust | TrustArc | Collibra | DataGrail |
|-----------|--------|----------|----------|----------|-----------|
| Art. 30 field coverage | 20% | /5 | /5 | /5 | /5 |
| Multi-entity support | 10% | /5 | /5 | /5 | /5 |
| API capability | 15% | /5 | /5 | /5 | /5 |
| Workflow automation | 15% | /5 | /5 | /5 | /5 |
| Integration ecosystem | 10% | /5 | /5 | /5 | /5 |
| SA template support | 10% | /5 | /5 | /5 | /5 |
| Ease of use | 10% | /5 | /5 | /5 | /5 |
| Total cost (3-year) | 10% | /5 | /5 | /5 | /5 |
| **Weighted Total** | **100%** | **/5** | **/5** | **/5** | **/5** |

---

## Migration Plan

| Phase | Duration | Key Activities |
|-------|----------|---------------|
| 1. Contract and setup | 2 weeks | DPA execution, tenant provisioning, SSO configuration |
| 2. Configuration | 4 weeks | Custom fields, templates, workflows, SA templates |
| 3. Integration | 3 weeks | AD sync, ServiceNow webhook, vendor management link |
| 4. Data migration | 2 weeks | CSV export from spreadsheet, import, validation |
| 5. Testing | 2 weeks | UAT with DPO office and 5 processing owners |
| 6. Training | 1 week | DPO office training (admin), processing owner training (basic) |
| 7. Go-live | 1 week | Production cutover, spreadsheet decommission |

---

## Decision

**Selected Platform**: [___]
**Decision Date**: [YYYY-MM-DD]
**Approved By**: [Name, Title]
**Budget Approved**: [Amount]
**Target Go-Live Date**: [YYYY-MM-DD]
