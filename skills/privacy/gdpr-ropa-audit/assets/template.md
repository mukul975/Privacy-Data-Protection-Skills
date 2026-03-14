# RoPA Audit Report — Nexus Technologies GmbH

**Audit Date**: 2026-01-20
**Audit Lead**: Dr. Katharina Weiss, Data Protection Officer
**Audit Scope**: Full organisational RoPA covering 47 processing activities across 8 business units
**Audit Period**: Q4 2025 — Q1 2026
**Report Classification**: Confidential — Internal Use Only

---

## Executive Summary

This audit assessed 47 processing activity records maintained by Nexus Technologies GmbH against GDPR Article 30(1) controller requirements. The review identified 12 findings across 9 processing activities, comprising 2 Critical, 5 Major, and 5 Minor findings. Immediate remediation is required for Critical findings within 30 days.

---

## Audit Scope and Methodology

| Parameter | Detail |
|-----------|--------|
| Organisation | Nexus Technologies GmbH, Friedrichstraße 108, 10117 Berlin, Germany |
| Registration | HRB 182734 B, Amtsgericht Charlottenburg |
| DPO | Dr. Katharina Weiss, dpo@nexus-tech.eu, +49 30 2345 6789 |
| Total RoPA entries audited | 47 (43 controller, 4 processor) |
| Sample interviews conducted | 10 (21% of entries) |
| Audit standard | GDPR Art. 30(1)(a)-(g) and Art. 30(2)(a)-(d) |

---

## Summary of Findings

| Severity | Count | Remediation Deadline |
|----------|-------|---------------------|
| Critical | 2 | 2026-02-19 |
| Major | 5 | 2026-03-21 |
| Minor | 5 | 2026-04-20 |
| **Total** | **12** | |

---

## Detailed Findings

### Finding 1 — Critical

| Attribute | Detail |
|-----------|--------|
| Record ID | RPA-023 |
| Processing Activity | Customer behavioural analytics for product recommendation engine |
| Business Unit | Digital Marketing |
| Field | Art. 30(1)(f) — Retention Periods |
| Issue | Retention period field is empty. No time limit or deletion criteria specified for behavioural tracking data comprising browsing history, click patterns, and purchase predictions. |
| Regulatory Risk | Non-compliance with Art. 5(1)(e) storage limitation principle and Art. 30(1)(f) documentation requirement. |
| Remediation | Marketing team to define and document retention period for behavioural data. Recommended: 24 months from last interaction, with automated deletion via the CDP platform. |
| Owner | Stefan Richter, Head of Digital Marketing |
| Deadline | 2026-02-19 |

### Finding 2 — Critical

| Attribute | Detail |
|-----------|--------|
| Record ID | RPA-041 |
| Processing Activity | Employee health screening data processing |
| Business Unit | Human Resources |
| Field | Art. 30(1)(b) — Purposes / Art. 9 — Special Categories |
| Issue | Processing of health data (Art. 9(1) special category) recorded with purpose "HR operations" — insufficiently specific. No explicit Art. 9(2) condition documented. |
| Regulatory Risk | Processing special category data without documented lawful basis under Art. 9(2) and with vague purpose violating Art. 5(1)(b). |
| Remediation | HR to specify purpose as "occupational health assessments under employment law obligation per Section 3 ArbSchG" and document Art. 9(2)(b) employment law condition. |
| Owner | Maria Fischer, HR Director |
| Deadline | 2026-02-19 |

### Finding 3 — Major

| Attribute | Detail |
|-----------|--------|
| Record ID | RPA-007 |
| Processing Activity | Cloud-based CRM system (Salesforce) |
| Business Unit | Sales |
| Field | Art. 30(1)(e) — International Transfers |
| Issue | Record states "data processed in Salesforce EU data centre" but Salesforce support access from the United States is not documented. No Transfer Impact Assessment for US remote access. |
| Regulatory Risk | Undocumented international transfer without documented safeguard mechanism, contrary to Art. 30(1)(e) and Chapter V requirements. |
| Remediation | Document US support access as an international transfer. Reference the EU-US Data Privacy Framework adequacy decision (July 2023) as the transfer mechanism, confirming Salesforce Inc. is listed on the Data Privacy Framework List. |
| Owner | Thomas Braun, Sales Operations Manager |
| Deadline | 2026-03-21 |

### Finding 4 — Major

| Attribute | Detail |
|-----------|--------|
| Record ID | RPA-012 |
| Processing Activity | Supplier onboarding and due diligence |
| Business Unit | Procurement |
| Field | Art. 30(1)(d) — Categories of Recipients |
| Issue | Recipient field lists "third-party due diligence provider" without identifying the specific processor (Refinitiv World-Check) or confirming an Art. 28 DPA is in place. |
| Regulatory Risk | Incomplete recipient documentation; potential undocumented processor relationship. |
| Remediation | Procurement to update record with "Refinitiv (LSEG), Art. 28 DPA executed 2024-03-15, ref: DPA-2024-RF-001" and add to vendor register. |
| Owner | Claudia Lehmann, Procurement Lead |
| Deadline | 2026-03-21 |

### Finding 5 — Major

| Attribute | Detail |
|-----------|--------|
| Record ID | RPA-015 |
| Processing Activity | CCTV surveillance of office premises |
| Business Unit | Facilities |
| Field | Art. 30(1)(g) — Security Measures |
| Issue | Security measures field states "cameras are secured" with no further detail on access controls, footage encryption, or viewing authorisation procedures. |
| Regulatory Risk | Insufficient description of technical and organisational measures contrary to Art. 30(1)(g) read with Art. 32. |
| Remediation | Facilities team to update with: "AES-256 encrypted storage on on-premises NVR, role-based access restricted to Facilities Manager and Security Lead, 30-day automated overwrite, access logged and audited quarterly." |
| Owner | Andreas Koch, Facilities Manager |
| Deadline | 2026-03-21 |

### Finding 6 — Major

| Attribute | Detail |
|-----------|--------|
| Record ID | RPA-029 |
| Processing Activity | Employee performance reviews |
| Business Unit | Human Resources |
| Field | Art. 30(1)(c) — Categories of Data Subjects |
| Issue | Record lists "employees" but omits contingent workers (contractors, temporary staff) who are also subject to performance review processes. |
| Regulatory Risk | Incomplete data subject categorisation resulting in inaccurate RoPA. |
| Remediation | HR to add "contractors" and "temporary agency workers" to data subject categories and verify privacy notices have been provided to these groups. |
| Owner | Maria Fischer, HR Director |
| Deadline | 2026-03-21 |

### Finding 7 — Major

| Attribute | Detail |
|-----------|--------|
| Record ID | RPA-034 |
| Processing Activity | Website analytics via Google Analytics 4 |
| Business Unit | Digital Marketing |
| Field | Art. 30(1)(b) — Purposes |
| Issue | Purpose recorded as "website analytics" without specifying the legitimate interest relied upon or documenting the LIA. |
| Regulatory Risk | Vague purpose description failing Art. 5(1)(b) specificity requirement. |
| Remediation | Update purpose to "Analysis of aggregate website visitor behaviour to optimise user experience and conversion rates, relying on legitimate interest (Art. 6(1)(f)) per LIA ref: LIA-2025-GA4-001." |
| Owner | Stefan Richter, Head of Digital Marketing |
| Deadline | 2026-03-21 |

### Finding 8 — Minor

| Attribute | Detail |
|-----------|--------|
| Record ID | RPA-003 |
| Processing Activity | Finance — accounts payable processing |
| Business Unit | Finance |
| Field | Art. 30(1)(a) — Controller Identity |
| Issue | DPO contact email listed as previous DPO's personal email (j.schmidt@nexus-tech.eu) rather than the functional mailbox (dpo@nexus-tech.eu). |
| Remediation | Update DPO email to dpo@nexus-tech.eu across all records. |
| Owner | Dr. Katharina Weiss, DPO |
| Deadline | 2026-04-20 |

### Finding 9 — Minor

| Attribute | Detail |
|-----------|--------|
| Record ID | RPA-019 |
| Processing Activity | Customer support ticket management |
| Business Unit | Customer Success |
| Field | last_reviewed_date |
| Issue | Record last reviewed on 2024-08-10 — 529 days ago, exceeding the 365-day review threshold. |
| Remediation | Customer Success team to review and re-validate all fields in this record. |
| Owner | Lisa Hartmann, Customer Success Manager |
| Deadline | 2026-04-20 |

### Finding 10 — Minor

| Attribute | Detail |
|-----------|--------|
| Record ID | RPA-031 |
| Processing Activity | Business travel booking |
| Business Unit | Administration |
| Field | Art. 30(1)(f) — Retention Periods |
| Issue | Retention period stated as "per company policy" without specifying the actual duration. Policy reference: POL-RET-004 specifies 10 years, but this should be explicit in the RoPA entry. |
| Remediation | Update retention field to "10 years from date of travel per tax documentation requirements (Section 147 AO), ref: POL-RET-004." |
| Owner | Sabine Krüger, Office Manager |
| Deadline | 2026-04-20 |

### Finding 11 — Minor

| Attribute | Detail |
|-----------|--------|
| Record ID | RPA-038 |
| Processing Activity | Recruitment applicant tracking |
| Business Unit | Human Resources |
| Field | Consistency |
| Issue | Retention period correctly states "6 months from application decision per AGG requirements" but the ATS system is configured for 12-month retention. System configuration does not match documented retention. |
| Remediation | Align ATS system configuration with documented 6-month retention period, or update RoPA if 12-month retention is justified and documented. |
| Owner | Maria Fischer, HR Director |
| Deadline | 2026-04-20 |

### Finding 12 — Minor

| Attribute | Detail |
|-----------|--------|
| Record ID | Multiple (RPA-002, RPA-005, RPA-014) |
| Processing Activity | Various |
| Business Unit | Various |
| Field | Formatting |
| Issue | Three records use inconsistent date formats for retention periods (DD/MM/YYYY vs YYYY-MM-DD). |
| Remediation | Standardise all date references to ISO 8601 (YYYY-MM-DD) format per the RoPA governance procedure. |
| Owner | DPO Office |
| Deadline | 2026-04-20 |

---

## Recommendations

1. Implement automated quarterly RoPA staleness checks using the validation script to flag records exceeding their review date.
2. Conduct a targeted review of all processing activities involving special category data (Art. 9) to verify explicit Art. 9(2) conditions are documented.
3. Integrate RoPA validation into the change management process so that new systems or changes to existing processing trigger a RoPA update.
4. Standardise the DPO contact to the functional mailbox (dpo@nexus-tech.eu) across all records to prevent future staleness on personnel changes.
5. Schedule the next full RoPA audit for Q1 2027.

---

**Prepared by**: Dr. Katharina Weiss, DPO, Nexus Technologies GmbH
**Reviewed by**: Internal Audit Committee
**Distribution**: DPO, CFO, Data Protection Steering Committee, affected business unit heads
