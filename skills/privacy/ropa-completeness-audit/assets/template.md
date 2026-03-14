# RoPA Completeness Audit Report — Helix Biotech Solutions GmbH

**Audit Date**: 2025-01-20
**Audit Lead**: Dr. Elena Voss, Data Protection Officer
**SA Template Used**: BfDI (primary), CNIL (for Diagnostics S.A.S. entity)
**Scope**: Full organisational RoPA — all departments, GmbH entity
**Records Audited**: 38

---

## Executive Summary

| Metric | Score |
|--------|-------|
| **Overall Completeness** | 78.3% |
| Tier 1 — Art. 30 Mandatory | 89.2% |
| Tier 2 — SA Extended Fields | 71.5% |
| Tier 3 — Quality Assessment | 66.8% |
| **Rating** | Good |
| **Previous Audit Score** | 72.1% (Date: 2024-07-15) |
| **Trend** | Improved (+6.2 percentage points) |

---

## Gap Summary

| Severity | Count | Remediation Deadline |
|----------|-------|---------------------|
| Critical (missing mandatory field) | 3 | 30 days (by 2025-02-19) |
| Major (incomplete or vague field) | 11 | 60 days (by 2025-03-21) |
| Enhancement (SA recommended field) | 17 | Next annual review (2025-09-20) |
| **Total** | **31** | |

---

## Score Distribution by Department

| Department | Entries | Avg Score | Rating | Critical Gaps |
|-----------|---------|-----------|--------|---------------|
| Human Resources | 6 | 88% | Good | 0 |
| Clinical Operations | 8 | 82% | Good | 1 |
| Digital Marketing | 5 | 64% | Poor | 1 |
| Finance | 7 | 81% | Good | 0 |
| IT | 6 | 77% | Acceptable | 0 |
| Sales | 4 | 72% | Acceptable | 1 |
| Facilities | 2 | 69% | Acceptable | 0 |

---

## Critical Findings (Immediate Remediation Required)

### Finding 1: RPA-2024-CRM-003 — Salesforce Customer CRM

| Attribute | Detail |
|-----------|--------|
| Field | Art. 30(1)(e) — International transfers |
| Classification | Missing |
| SA Expectation | BfDI requires documentation of all transfers to third countries with safeguard mechanism |
| Current State | Field is blank |
| Gap Description | Salesforce processes data on EU servers but metadata replication to US servers is undocumented. Transfer to Salesforce Inc. (US) must be recorded with EU-US DPF or SCCs reference |
| Remediation Action | Document Salesforce US transfer with DPF certification reference and TIA |
| Owner | Katarina Mueller, Sales Director |
| Deadline | 2025-02-19 |

### Finding 2: RPA-2024-MKT-005 — Google Analytics 4

| Attribute | Detail |
|-----------|--------|
| Field | Art. 30(1)(b) — Purposes and Art. 30(1)(f) — Retention |
| Classification | Incomplete |
| SA Expectation | BfDI requires specific purpose statements (not generic "analytics") and documented retention periods |
| Current State | Purpose listed as "Website analytics." Retention period field is blank. |
| Gap Description | Purpose statement is too generic to assess proportionality. GA4 data retention setting (2 months vs 14 months) is not documented. |
| Remediation Action | Specify purposes (e.g., "Measuring website traffic volume, page popularity, and user journey to optimise content and detect technical errors"). Document GA4 retention setting and server-side deletion schedule. |
| Owner | Lisa Becker, Digital Marketing Manager |
| Deadline | 2025-02-19 |

### Finding 3: RPA-2024-SAL-002 — Trade Show Lead Capture

| Attribute | Detail |
|-----------|--------|
| Field | Art. 30(1)(c) — Data categories |
| Classification | Missing |
| SA Expectation | BfDI requires explicit listing of all personal data categories processed |
| Current State | Data categories field contains only "Contact details" |
| Gap Description | Badge scanning at trade shows captures name, company, job title, email, phone, and potentially dietary preferences (special category if indicating religious beliefs). All categories must be individually listed. |
| Remediation Action | Enumerate all data fields captured by badge scanner and lead capture forms. Assess whether dietary preference data constitutes special category data under Art. 9(1). |
| Owner | Stefan Weber, Sales Operations Manager |
| Deadline | 2025-02-19 |

---

## Remediation Tracker

| Gap ID | Record | Field | Severity | Owner | Deadline | Status |
|--------|--------|-------|----------|-------|----------|--------|
| GAP-001 | RPA-2024-CRM-003 | Art. 30(1)(e) transfers | Critical | K. Mueller | 2025-02-19 | Open |
| GAP-002 | RPA-2024-MKT-005 | Art. 30(1)(b) purpose, (f) retention | Critical | L. Becker | 2025-02-19 | Open |
| GAP-003 | RPA-2024-SAL-002 | Art. 30(1)(c) data categories | Critical | S. Weber | 2025-02-19 | Open |
| GAP-004 | RPA-2024-HR-001 | Art. 30(1)(d) internal recipients | Major | J. Richter | 2025-03-21 | Open |
| GAP-005 | RPA-2024-CT-002 | Art. 30(1)(g) security measures — specificity | Major | Dr. F. Hartmann | 2025-03-21 | Open |
| GAP-006 | RPA-2024-FIN-003 | Art. 30(1)(f) retention — AO reference missing | Major | T. Fischer | 2025-03-21 | Open |
| GAP-007 | RPA-2024-IT-004 | Art. 30(1)(d) processor DPA reference | Major | M. Steiner | 2025-03-21 | Open |
| GAP-008 | RPA-2024-MKT-002 | Art. 30(1)(b) lawful basis specificity | Major | L. Becker | 2025-03-21 | Open |
| GAP-009 | RPA-2024-HR-006 | Art. 30(1)(e) UK transfer mechanism | Major | J. Richter | 2025-03-21 | Open |
| GAP-010 | RPA-2024-CT-004 | Art. 30(1)(c) data subject categories | Major | Dr. F. Hartmann | 2025-03-21 | Open |
| GAP-011 | RPA-2024-FIN-005 | Art. 30(1)(g) backup testing evidence | Major | T. Fischer | 2025-03-21 | Open |
| GAP-012 | RPA-2024-SAL-001 | Art. 30(1)(d) Salesforce sub-processors | Major | K. Mueller | 2025-03-21 | Open |
| GAP-013 | RPA-2024-IT-002 | Art. 30(1)(f) retention specificity | Major | M. Steiner | 2025-03-21 | Open |
| GAP-014 | RPA-2024-FAC-001 | Art. 30(1)(g) CCTV signage documentation | Major | P. Braun | 2025-03-21 | Open |

---

## Recommendations

1. **Salesforce transfer documentation**: Immediately document all international transfers associated with Salesforce CRM, including sub-processor transfers. Obtain Salesforce Inc. DPF certification reference and complete a Transfer Impact Assessment.
2. **Marketing department training**: Schedule dedicated RoPA training for Digital Marketing team — lowest departmental score (64%) driven by vague purpose statements and missing retention periods across all 5 records.
3. **Automated completeness scanning**: Implement quarterly automated completeness scans using the process.py audit script to detect gaps between annual audits. Target: zero critical gaps at any point.
4. **Retention period standardisation**: Create a master retention schedule document linked from all RoPA entries. Several departments reference retention periods inconsistently or without legal basis citations.

---

## Next Audit

| Parameter | Value |
|-----------|-------|
| Next full audit | 2025-07-20 |
| Next automated scan | 2025-04-20 |
| 30-day critical remediation check | 2025-02-19 |
| 60-day major remediation check | 2025-03-21 |

---

**Prepared by**: Dr. Elena Voss, DPO
**Distribution**: DPO, Data Protection Steering Committee, affected processing owners
