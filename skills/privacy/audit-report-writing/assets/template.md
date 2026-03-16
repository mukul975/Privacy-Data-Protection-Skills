# Privacy Audit Report

## Cover Page

| Field | Value |
|-------|-------|
| Report Title | Privacy Compliance Audit Report — DSAR Processing |
| Report ID | AUDIT-RPT-2026-Q1-001 |
| Classification | Confidential |
| Audit Period | 1 January 2026 – 28 February 2026 |
| Fieldwork Dates | 3 March 2026 – 10 March 2026 |
| Report Date | 25 March 2026 |
| Lead Auditor | Maria Chen, CIPP/E, CISA |
| Audit Team | Maria Chen, James Okoro, Priya Sharma |
| Distribution | CPO, DPO, Internal Audit Director, Head of Data Governance |

## Executive Summary

This report presents the results of the Q1 2026 privacy compliance audit of the Data Subject Access Request (DSAR) processing function at Zenith Global Enterprises.

### Overall Opinion: Needs Improvement

The DSAR process is broadly established but exhibits material control weaknesses in deadline tracking and identity verification that require prompt remediation.

### Findings Summary

| Severity | Count |
|----------|-------|
| Critical | 0 |
| High | 2 |
| Medium | 3 |
| Low | 1 |
| Observations | 2 |
| **Total** | **8** |

### Key Issues Requiring Immediate Attention

1. **AUDIT-2026-001 (High)**: 30% of sampled DSARs exceeded the one-month statutory deadline
2. **AUDIT-2026-002 (High)**: Identity verification inconsistently applied across business units

## Audit Scope and Objectives

| Element | Detail |
|---------|--------|
| Objective | Assess compliance of the DSAR process with GDPR Articles 12-23 and internal policy DP-POL-005 |
| Scope | All DSARs received between 1 Jan 2026 and 28 Feb 2026 across EU operations |
| Exclusions | Employee DSARs (covered by separate HR audit); third-party processor DSARs |
| Population | 247 DSARs received during the audit period |
| Sample Size | 50 DSARs (stratified random sampling by business unit) |

## Methodology

| Technique | Application |
|-----------|------------|
| Document Review | DSAR policy, procedures, training materials |
| Data Analysis | Response time analysis across full population (247 DSARs) |
| Sample Testing | Detailed review of 50 DSARs for completeness, accuracy, timeliness |
| Interviews | DPO, DSAR Coordinator, 3 Business Unit Privacy Champions |
| System Walkthrough | DSAR tracking system (OneTrust) configuration and workflow |

## Findings

### AUDIT-2026-001: DSAR Response Deadline Exceedances

| Element | Detail |
|---------|--------|
| Severity | High |
| Condition | 15 of 50 sampled DSARs (30%) exceeded the one-month response deadline under GDPR Article 12(3). Average overdue period: 12 days. |
| Criteria | GDPR Article 12(3): response within one month, extendable by two further months for complex requests with notification to data subject |
| Cause | Manual triage process with no automated deadline tracking; no escalation workflow at day 20 |
| Effect | Regulatory risk (supervisory authority complaint); reputational harm; potential fine |
| Recommendation | Implement automated deadline tracking in OneTrust with escalation alerts at day 20 and day 25; assign deputy responder for absence coverage |
| Evidence | ANA-005: Response time analysis; DOC-023: DSAR log extract |

### AUDIT-2026-002: Inconsistent Identity Verification

| Element | Detail |
|---------|--------|
| Severity | High |
| Condition | 3 of 4 business units do not follow the identity verification procedure in DP-PROC-012. Marketing unit accepted DSARs via unverified email. |
| Criteria | GDPR Article 12(6): controller may request additional information to confirm identity; DP-PROC-012 Section 4.2 |
| Cause | Procedure not cascaded to all business units; no mandatory verification step in OneTrust workflow |
| Effect | Risk of unauthorised disclosure of personal data to impersonators |
| Recommendation | Add mandatory identity verification step in OneTrust workflow; conduct targeted training for Marketing unit; quarterly spot-check compliance |
| Evidence | INT-002: Interview with Marketing Privacy Champion; OBS-003: OneTrust workflow screenshot |

### AUDIT-2026-003: Incomplete Exemption Documentation

| Element | Detail |
|---------|--------|
| Severity | Medium |
| Condition | 4 of 7 DSARs where exemptions were applied lacked documented justification for the exemption |
| Criteria | GDPR Articles 12(4), 15(4); DP-PROC-012 Section 5.1 requires written justification for any exemption |
| Cause | Free-text justification field in OneTrust not marked as mandatory |
| Effect | Inability to demonstrate lawful basis for refusal if challenged by data subject or supervisory authority |
| Recommendation | Make exemption justification field mandatory in OneTrust; provide exemption decision template with pre-approved justification categories |
| Evidence | DOC-031: Exemption log; OBS-005: OneTrust configuration screenshot |

## Management Response

| Finding ID | Response | Action Plan | Owner | Target Date |
|-----------|----------|------------|-------|------------|
| AUDIT-2026-001 | Accepted | Implement automated tracking and escalation in OneTrust | DSAR Coordinator | 30 April 2026 |
| AUDIT-2026-002 | Accepted | Workflow update and training programme | DPO | 15 April 2026 |
| AUDIT-2026-003 | Accepted | OneTrust field configuration change | Privacy Engineering Lead | 10 April 2026 |

## Appendices

### Appendix A: Evidence Register

| Evidence ID | Type | Description | Date |
|------------|------|-------------|------|
| DOC-023 | Documentary | DSAR log extract, Jan-Feb 2026 | 5 Mar 2026 |
| ANA-005 | Analytical | Response time statistical analysis | 7 Mar 2026 |
| INT-002 | Testimonial | Interview with Marketing Privacy Champion | 6 Mar 2026 |
| OBS-003 | Observational | OneTrust workflow configuration screenshot | 8 Mar 2026 |
| OBS-005 | Observational | OneTrust exemption field screenshot | 8 Mar 2026 |
| DOC-031 | Documentary | Exemption decision log | 5 Mar 2026 |

### Appendix B: Distribution Record

| Recipient | Version | Date Issued |
|-----------|---------|------------|
| Chief Privacy Officer | Full Report | 25 Mar 2026 |
| DPO | Full Report | 25 Mar 2026 |
| Internal Audit Director | Full Report | 25 Mar 2026 |
| Board Audit Committee | Executive Summary | 25 Mar 2026 |
