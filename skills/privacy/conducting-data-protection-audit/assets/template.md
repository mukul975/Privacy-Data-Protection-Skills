# Data Protection Audit Report — Nexus Technologies GmbH

**Audit Date**: 2026-01-20 to 2026-02-14
**Lead Auditor**: Dr. Katharina Weiss, DPO
**Audit Scope**: Full organisational GDPR compliance across all eight domains
**Classification**: Confidential — Internal Use Only

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Overall Compliance Score | 74.5% |
| Overall Maturity Level | Managed |
| Total Control Points Assessed | 55 |
| Effective Controls | 38 (69%) |
| Partially Effective Controls | 11 (20%) |
| Ineffective Controls | 4 (7%) |
| Not Implemented Controls | 2 (4%) |
| Total Findings | 17 |
| Critical Findings | 2 |
| Major Findings | 6 |
| Minor Findings | 9 |

Nexus Technologies GmbH has achieved a Managed maturity level with an overall compliance score of 74.5%. Core governance and accountability structures are in place, but targeted improvements are needed in processor management, privacy by design integration, and DPIA coverage.

---

## Domain Scores

| Domain | GDPR Reference | Score | Maturity |
|--------|---------------|-------|----------|
| Data Protection Principles | Art. 5 | 81.0% | Managed |
| Accountability and Governance | Art. 24, 5(2) | 85.7% | Managed |
| Privacy by Design and Default | Art. 25 | 55.6% | Defined |
| Processor Management | Art. 28 | 66.7% | Defined |
| Records of Processing | Art. 30 | 80.0% | Managed |
| Security of Processing | Art. 32 | 83.3% | Managed |
| Data Protection Impact Assessments | Art. 35 | 71.4% | Managed |
| Data Protection Officer | Art. 37-39 | 88.9% | Managed |

---

## Critical Findings

### F-001: No Privacy by Design Integration in SDLC

| Attribute | Detail |
|-----------|--------|
| Domain | Privacy by Design and Default |
| Control | 3.1 — Privacy requirements integrated into SDLC |
| GDPR Reference | Art. 25(1) |
| Rating | Not Implemented |
| Finding | The software development lifecycle does not include any privacy review gates, privacy requirements specification, or DPO consultation checkpoints. Three new applications were deployed in the past 12 months without privacy assessment at the design stage. |
| Risk | Non-compliant with Art. 25(1) obligation to implement data protection principles at the time of determination of means. New systems may process personal data without appropriate safeguards. |
| Remediation | Integrate privacy review gates at requirements, design, and pre-deployment stages. Create a privacy requirements checklist for all new projects. Train development leads on privacy by design principles. |
| Owner | Jan Mueller, CTO |
| Deadline | 2026-03-16 |

### F-002: Processor DPAs Missing Art. 28(3) Mandatory Clauses

| Attribute | Detail |
|-----------|--------|
| Domain | Processor Management |
| Control | 4.2 — Art. 28(3) DPAs in place with all processors |
| GDPR Reference | Art. 28(3) |
| Rating | Not Implemented |
| Finding | Of 23 active processor relationships, 4 processors (Mailjet SAS, Cloudinary Ltd, Intercom Inc, Amplitude Inc) operate under general terms of service that do not contain all eight Art. 28(3) mandatory elements. Specifically, sub-processor notification (Art. 28(2)), audit rights (Art. 28(3)(h)), and data return/deletion obligations (Art. 28(3)(g)) are absent. |
| Risk | Processing by these four processors lacks the contractual safeguards required by Art. 28(3). Supervisory authorities have issued fines for DPA deficiencies (Berlin DPA fine against Deutsche Wohnen SE). |
| Remediation | Issue DPA addenda to all four processors within 30 days using the organisation's standard DPA template incorporating all Art. 28(3) clauses. If processors refuse, evaluate alternative providers. |
| Owner | Claudia Lehmann, Procurement Lead |
| Deadline | 2026-03-16 |

---

## Major Findings

### F-003: Incomplete DPIA Coverage

| Attribute | Detail |
|-----------|--------|
| Control | 7.2 — DPIAs conducted before high-risk processing |
| GDPR Reference | Art. 35(1) |
| Rating | Partially Effective |
| Finding | Two processing activities identified as high-risk (employee monitoring via endpoint DLP software, customer credit scoring) do not have completed DPIAs. |
| Owner | Dr. Katharina Weiss, DPO |
| Deadline | 2026-04-16 |

### F-004: Processor Due Diligence Not Periodic

| Attribute | Detail |
|-----------|--------|
| Control | 4.3 — Processor due diligence conducted periodically |
| GDPR Reference | Art. 28(1) |
| Rating | Partially Effective |
| Finding | Initial due diligence is conducted for new processors, but no periodic reassessment programme exists. 8 of 23 processors have not been reassessed since initial onboarding (oldest: 2021). |
| Owner | Claudia Lehmann, Procurement Lead |
| Deadline | 2026-04-16 |

### F-005: Default Settings Not Privacy-Oriented

| Attribute | Detail |
|-----------|--------|
| Control | 3.3 — Default settings ensure only necessary data is processed |
| GDPR Reference | Art. 25(2) |
| Rating | Ineffective |
| Finding | The customer account registration form collects phone number, date of birth, and gender as mandatory fields despite these not being necessary for account creation or service delivery. Default marketing preferences are set to opt-in. |
| Owner | Stefan Richter, Head of Digital Marketing |
| Deadline | 2026-04-16 |

### F-006: Retention Schedule Not Enforced

| Attribute | Detail |
|-----------|--------|
| Control | 1.5 — Retention periods defined with deletion procedures |
| GDPR Reference | Art. 5(1)(e) |
| Rating | Partially Effective |
| Finding | A retention schedule exists but automated deletion is implemented for only 12 of 47 processing activities. Manual deletion relies on annual reviews that have been delayed in 3 business units. |
| Owner | Dr. Katharina Weiss, DPO |
| Deadline | 2026-04-16 |

### F-007: Data Subject Rights Procedures Not Tested

| Attribute | Detail |
|-----------|--------|
| Control | 2.5 — Documented procedures for GDPR obligations |
| GDPR Reference | Art. 24(1) |
| Rating | Partially Effective |
| Finding | DSAR and breach notification procedures exist but have never been tested through simulation exercises. Staff in customer service (first point of contact for DSARs) were unable to describe the correct escalation path during interviews. |
| Owner | Maria Fischer, HR Director (training) |
| Deadline | 2026-04-16 |

### F-008: Sub-Processor Notification Gaps

| Attribute | Detail |
|-----------|--------|
| Control | 4.4 — Sub-processor authorisation and notification |
| GDPR Reference | Art. 28(2)-(4) |
| Rating | Partially Effective |
| Finding | General written authorisation model is used for most processors, but 3 processors do not provide sub-processor change notifications. The organisation has no monitoring mechanism to detect sub-processor changes. |
| Owner | Claudia Lehmann, Procurement Lead |
| Deadline | 2026-04-16 |

---

## Recommendations

1. **Immediate priority**: Establish Art. 25 privacy by design SDLC integration with mandatory DPO review before any new system deployment.
2. **30-day priority**: Execute DPA addenda for the four non-compliant processors or initiate vendor replacement evaluation.
3. **60-day priority**: Complete DPIAs for employee monitoring and credit scoring processing activities.
4. **90-day priority**: Implement automated retention enforcement across all processing activities using the data lifecycle management platform.
5. **Quarterly**: Conduct tabletop exercises for DSAR and breach notification procedures.
6. **Annual**: Implement periodic processor reassessment programme with risk-based frequency (high-risk: annual, standard: biennial).

---

**Next Audit**: Q1 2027 (full scope) with interim follow-up on critical and major findings in Q3 2026.

**Prepared by**: Dr. Katharina Weiss, DPO
**Distribution**: Board of Directors, CTO, CISO, General Counsel, Head of Procurement, Data Protection Steering Committee
