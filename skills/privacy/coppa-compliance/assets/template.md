# COPPA Compliance Audit Report

## Audit Information

| Field | Value |
|-------|-------|
| **Audit Date** | 2026-03-14 |
| **Operator** | BrightPath Learning Inc. |
| **Operator Address** | 200 Education Lane, Amsterdam, 1012 AB, Netherlands |
| **US Agent** | BrightPath US LLC, 500 Learning Way, San Francisco, CA 94105 |
| **Auditor** | Dr. Sarah Chen, Chief Privacy Officer |
| **Service** | BrightPath Educational Gaming Platform (iOS, Android, Web) |
| **Target Audience** | Children aged 5-15 |
| **Safe Harbor** | kidSAFE Seal Program (active, renewed 2025-11-01) |
| **Scope** | Full COPPA compliance audit — annual review |

## Audit Results

### Notice Requirements (Section 312.4)

| # | Item | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 1 | Online privacy notice posted prominently | 312.4(b) | PASS | Link on home page footer and each data collection screen |
| 2 | Operator identification in notice | 312.4(b)(1) | PASS | Full name, address, email, phone for BrightPath Learning and US agent |
| 3 | Information collected described | 312.4(b)(2) | PASS | All data types listed with collection methods |
| 4 | Use of information described | 312.4(b)(3) | PASS | Educational purposes and service improvement described |
| 5 | Third-party disclosure described | 312.4(b)(4) | PASS | AWS (hosting) and SendGrid (notifications) named |
| 6 | Parental rights described | 312.4(b)(5) | PASS | Review, delete, refuse rights with instructions |
| 7 | Direct notice to parent | 312.4(c) | PASS | Email with full disclosure sent before collection |

### Consent Requirements (Section 312.5)

| # | Item | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 8 | Verifiable parental consent | 312.5(a) | PASS | Consent obtained before any data collection |
| 9 | Consent method appropriate | 312.5(b) | PASS | Credit card micro-transaction (USD 0.50, refunded) |
| 10 | Neutral age screen | FTC guidance | PASS | "Enter your date of birth" with scrollable picker |

### Parental Access (Section 312.6)

| # | Item | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 11 | Parent can review data | 312.6(a) | PASS | Parental dashboard shows all collected data |
| 12 | Parent can delete data | 312.6(a) | PASS | One-click deletion from dashboard |
| 13 | Parent can refuse collection | 312.6(a) | PASS | Per-purpose withdrawal toggles on dashboard |

### Data Minimisation (Section 312.7)

| # | Item | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 14 | No excess data conditioning | 312.7 | PASS | Core features accessible without optional data |

### Security (Section 312.8)

| # | Item | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 15 | Reasonable security | 312.8 | PASS | AES-256 at rest, TLS 1.3 in transit, RBAC, annual pentest |

### Data Retention (Section 312.10)

| # | Item | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 16 | Retention limited | 312.10 | PASS | Academic year + 30 days for learning data; 90 days for logs |
| 17 | Secure deletion | 312.10 | PASS | Automated deletion with verification; backup purge within 30 days |

### Safe Harbor (Section 312.11)

| # | Item | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 18 | Safe harbor membership | 312.11 | PASS | kidSAFE Seal active; annual compliance review completed |

## Summary

| Metric | Value |
|--------|-------|
| **Total Items** | 18 |
| **Passed** | 18 |
| **Failed** | 0 |
| **Not Applicable** | 0 |
| **Compliance Rate** | 100% |

## Recommendations

### Recommendation 1: Prepare for Proposed Rule Amendments

**Description**: The FTC's December 2023 NPRM proposes requiring separate opt-in consent for targeted advertising and enhanced data security requirements. While BrightPath does not serve advertising, the enhanced security and retention provisions may apply.

**Action**: Review proposed rule amendments when finalized and update compliance program accordingly.

**Owner**: Legal Team

**Timeline**: Within 90 days of final rule publication

### Recommendation 2: Expand Consent Methods

**Description**: Currently only credit card micro-transaction is offered. Adding digital identity verification or Open Banking verification would improve accessibility for unbanked families.

**Action**: Evaluate integration with PRIVO's consent management platform for additional methods.

**Owner**: Engineering Team

**Timeline**: Q3 2026

## Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| CPO | Dr. Sarah Chen | 2026-03-14 | [Signed] |
| US Legal Counsel | James Rodriguez | 2026-03-14 | [Signed] |
| Engineering Lead | Aisha Patel | 2026-03-14 | [Signed] |

## Next Audit

**Scheduled Date**: 2027-03-14 (Annual cadence)

**Interim Reviews**: Quarterly privacy notice review; semi-annual consent flow testing.
