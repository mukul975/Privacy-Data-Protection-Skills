# ISO 31700 Gap Assessment Report Template

## Assessment Information

| Item | Value |
|------|-------|
| Organization | Prism Data Systems AG |
| Assessment Scope | All consumer-facing products and services |
| Assessment Date | 2026-03-14 |
| Assessor | Dr. Lukas Meier (DPO), Thomas Richter (Privacy Engineering Lead) |
| Standard | ISO 31700-1:2023 |
| Target Certification Date | 2026-Q4 |

## Executive Summary

Prism Data Systems AG has achieved an overall average maturity score of 3.4 out of 5.0 across all 30 ISO 31700 requirements. Six requirements currently score below the certification threshold of Level 3, with one critical gap in physical media disposal (Requirement 27). The Design phase shows the highest maturity (3.8 average), followed by Production (3.5) and Disposal (2.7).

A focused remediation program targeting the six gap areas is estimated to require 4 months of effort, enabling certification readiness by Q3 2026 with a target certification audit in Q4 2026.

## Scoring Summary

| Phase | Avg Score | Requirements | Gaps | Critical |
|-------|-----------|-------------|------|----------|
| Design (Req. 1-16) | 3.8/5 | 16 | 2 | 0 |
| Production (Req. 17-24) | 3.5/5 | 8 | 1 | 0 |
| Disposal (Req. 25-30) | 2.7/5 | 6 | 3 | 1 |
| **Overall** | **3.4/5** | **30** | **6** | **1** |

## Detailed Scoring Matrix

### Design Phase

| Req | Title | Score | Status | Evidence |
|-----|-------|-------|--------|----------|
| 1 | Designing privacy controls | 4/5 | PASS | Privacy preference center in all products |
| 2 | Privacy notice and consent | 4/5 | PASS | Layered notices; granular consent |
| 3 | Consumer PII collection | 4/5 | PASS | API allowlist validation |
| 4 | Creating and managing consumer PII | 4/5 | PASS | Automated lifecycle management |
| 5 | Consumer PII use limitation | 4/5 | PASS | Purpose registry with OPA enforcement |
| 6 | Consumer PII disclosure to third parties | 3/5 | PASS | DPA with all processors |
| 7 | Consumer PII quality | 3/5 | PASS | Self-service editing; validation |
| 8 | Consumer PII security | 4/5 | PASS | Field-level encryption; SOC 2 Type II |
| 9 | Consumer PII retention | 4/5 | PASS | Automated retention enforcement |
| 10 | Organizational commitment | 4/5 | PASS | DPO appointed; board reporting |
| 11 | Privacy risk assessment | 4/5 | PASS | DPIA + LINDDUN threat modeling |
| 12 | Designing PII processing rights | 4/5 | PASS | Self-service DSAR portal |
| 13 | Designing ergonomic privacy controls | 3/5 | PASS | WCAG 2.1 AA; usability tested |
| 14 | Designing privacy for vulnerable consumers | 2/5 | **GAP** | Age verification only; no elderly design review |
| 15 | Supply chain management | 3/5 | PASS | Privacy in procurement; annual audits |
| 16 | Designing for disposal | 2/5 | **GAP** | IoT firmware lacks data wipe |

### Production Phase

| Req | Title | Score | Status | Evidence |
|-----|-------|-------|--------|----------|
| 17 | Privacy awareness and training | 4/5 | PASS | Annual training; role-specific modules |
| 18 | Privacy operations | 4/5 | PASS | Operations handbook; monitoring |
| 19 | Privacy breach management | 4/5 | PASS | IRP; 72-hour notification; tabletop exercises |
| 20 | Communication with consumers | 3/5 | PASS | Privacy inbox; FAQ; DPO contact |
| 21 | Third-party management | 3/5 | PASS | Processor register; DPA review |
| 22 | Consumer PII use | 4/5 | PASS | OPA enforcement in production |
| 23 | Managing privacy inquiries | 3/5 | PASS | 25-day DSAR response average |
| 24 | Privacy performance monitoring | 2/5 | **GAP** | No formal KPIs or dashboard |

### Disposal Phase

| Req | Title | Score | Status | Evidence |
|-----|-------|-------|--------|----------|
| 25 | End-of-life PII management | 2/5 | **GAP** | No formal end-of-life process |
| 26 | Consumer notification of disposal | 3/5 | PASS | Account closure email |
| 27 | PII disposal | 1/5 | **CRITICAL GAP** | Physical media disposal unverified |
| 28 | Data portability at end of life | 3/5 | PASS | JSON/CSV export before closure |
| 29 | Supply chain disposal | 2/5 | **GAP** | No verification of supplier deletion |
| 30 | Disposal documentation | 3/5 | PASS | Deletion logs maintained |

## Remediation Roadmap

| Priority | Req | Severity | Remediation | Owner | Target | Est. Effort |
|----------|-----|----------|-------------|-------|--------|------------|
| 1 | 27 | CRITICAL | NIST SP 800-88 media sanitization with certificates | IT Operations | 2026-05-01 | 3 weeks |
| 2 | 25 | MAJOR | End-of-life procedures per product line | Product Management | 2026-05-15 | 2 weeks |
| 3 | 29 | MAJOR | Disposal audit clause in contracts; verification | Procurement | 2026-06-01 | 3 weeks |
| 4 | 14 | MAJOR | Vulnerable consumer design review stage gate | UX Engineering | 2026-06-15 | 4 weeks |
| 5 | 16 | MAJOR | IoT firmware data wipe functionality | Firmware Engineering | 2026-07-01 | 6 weeks |
| 6 | 24 | MAJOR | Privacy KPIs and monitoring dashboard | Privacy Engineering | 2026-06-01 | 3 weeks |

## Approval

| Role | Name | Decision | Date |
|------|------|----------|------|
| DPO | Dr. Lukas Meier | Approved remediation plan | 2026-03-14 |
| CTO | Anna Kowalski | Budget approved | 2026-03-14 |
| CEO | Hans Brunner | Certification target approved | 2026-03-14 |
