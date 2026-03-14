# CNIL Cookie Compliance Audit Report

## Audit Information

| Field | Value |
|-------|-------|
| **Organization** | CloudVault SaaS Inc. |
| **Website** | cloudvault-saas.eu |
| **Audit Date** | 2026-03-14 |
| **Auditor** | Marta Kowalski, DPO |
| **CNIL Reference** | Deliberation No. 2020-091 |

## Cookie Inventory

### Essential Cookies (No Consent Required)

| Name | Purpose | Duration | First Party |
|------|---------|----------|-------------|
| cv_session | Session management | Session | Yes |
| cv_csrf | CSRF protection | Session | Yes |
| cv_lb | Load balancer affinity | Session | Yes |
| cv_lang | Language preference | 365 days | Yes |
| cv_consent | Cookie consent choices | 180 days | Yes |

### Non-Essential Cookies (Consent Required)

| Name | Purpose | Category | Duration | Third Party |
|------|---------|----------|----------|-------------|
| _ga | Audience measurement | Analytics | 390 days | Google LLC |
| _gid | Session distinction | Analytics | 1 day | Google LLC |

## CNIL Compliance Checklist

| # | Requirement | Reference | Status |
|---|-----------|-----------|--------|
| 1 | "Refuse All" on first layer | Section 2.1 | PASS |
| 2 | Equal button size | Section 2.1 | PASS — both 200x44px |
| 3 | Equal button color | Section 2.1 | PASS — both #2563EB |
| 4 | Equal font treatment | Section 2.1 | PASS — both 16px bold |
| 5 | No cookie wall | Section 2.2 | PASS — banner does not block |
| 6 | 6-month reconsent | Section 2.3 | PASS — 180-day cycle |
| 7 | Essential cookies documented | Section 3 | PASS |
| 8 | Third parties named | Section 2.4 | PASS — Google LLC listed |
| 9 | Purposes described | Section 2.4 | PASS |
| 10 | No pre-consent tracking | Art. 5(3) | PASS — no scripts before choice |

**Result: 10/10 — FULLY COMPLIANT**

## Sign-Off

| Role | Name | Date |
|------|------|------|
| DPO | Marta Kowalski | 2026-03-14 |
| Engineering Lead | James Park | 2026-03-14 |
