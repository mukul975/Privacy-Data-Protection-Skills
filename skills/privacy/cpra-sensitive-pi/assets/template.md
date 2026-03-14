# Sensitive Personal Information Processing Register

## Organization Information

| Field | Value |
|-------|-------|
| **Organization** | Liberty Commerce Inc. |
| **Register Date** | 2026-03-14 |
| **Maintained By** | Privacy Operations Team |
| **Review Cadence** | Quarterly |
| **Last Review** | 2026-01-15 |

## Sensitive PI Categories Collected

| Category | §1798.140(ae) | Collected | Purpose | Retention | Sold/Shared |
|----------|---------------|-----------|---------|-----------|-------------|
| Government IDs (SSN) | (ae)(1) | Yes | Tax reporting for marketplace sellers | Duration of seller account + 7 years | No |
| Government IDs (DL) | (ae)(1) | Yes | Age verification for restricted products | Verification event + 30 days | No |
| Account credentials | (ae)(2) | Yes | Authentication, transaction authorization | Duration of account | No |
| Precise geolocation | (ae)(3) | Yes | Delivery tracking, store finder | 30 days | No |
| Racial/ethnic origin | (ae)(4) | Yes (optional survey) | Aggregate diversity reporting | 90 days (aggregated and anonymized) | No |
| Religious beliefs | (ae)(5) | No | N/A | N/A | N/A |
| Union membership | (ae)(6) | Employees only | Payroll (dues deduction) | Employment + 7 years | No |
| Private communications | (ae)(7) | No (intended recipient) | N/A | N/A | N/A |
| Genetic data | (ae)(8) | No | N/A | N/A | N/A |
| Biometric data | (ae)(9) | No (device-side only) | N/A | N/A | N/A |
| Health information | (ae)(10) | Inferred from purchases | Product recall notifications | Transaction retention period | No |
| Sex life/orientation | (ae)(11) | No | N/A | N/A | N/A |

## Purpose Restriction Matrix (Post-Limit Request)

| Sensitive PI Category | Pre-Limit Uses | Post-Limit Permitted Uses | Post-Limit Blocked Uses |
|----------------------|----------------|--------------------------|------------------------|
| Precise geolocation | Delivery tracking, store finder, local inventory, targeted ads | Delivery tracking, active store finder request | Targeted advertising, location-based marketing |
| Account credentials | Authentication, transaction processing, fraud detection, profile enrichment | Authentication, transaction processing, fraud detection | Profile enrichment, cross-referencing |
| Government IDs | Tax reporting, age verification | Tax reporting (SSN), age verification (DL) | Any other purpose |
| Racial/ethnic origin | Aggregate diversity reporting, customer segmentation | None — delete within 30 days | All processing |
| Health information (inferred) | Product recommendations, recall notifications | Product recall notifications | Product recommendations, behavioral profiling |

## Limit Request Metrics

| Quarter | Requests Received | Processed Within 15 Business Days | Average Processing Time |
|---------|-------------------|-----------------------------------|------------------------|
| Q1 2025 | 312 | 312 (100%) | 0.5 days |
| Q2 2025 | 287 | 287 (100%) | 0.3 days |
| Q3 2025 | 401 | 401 (100%) | 0.4 days |
| Q4 2025 | 456 | 456 (100%) | 0.2 days |

## Technical Controls

| Control | Description | Status |
|---------|-------------|--------|
| Purpose-based access control | Sensitive PI database fields restricted by purpose code | Active |
| Limit flag enforcement | Consumer limit status checked before any sensitive PI processing | Active |
| Geolocation suppression | Advertising tag manager blocks geolocation data for limited consumers | Active |
| Credential isolation | Payment credentials processed exclusively via PCI-compliant service provider | Active |
| Survey data auto-deletion | Racial/ethnic survey responses auto-deleted 30 days after limit request | Active |
| Audit logging | All sensitive PI access events logged with purpose justification | Active |

## Sign-Off

| Role | Name | Date |
|------|------|------|
| CPO | Sarah Mitchell | 2026-03-14 |
| DPO | Robert Kim | 2026-03-14 |
| CISO | Angela Torres | 2026-03-14 |
