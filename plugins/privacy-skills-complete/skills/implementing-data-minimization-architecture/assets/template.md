# Data Minimization Assessment Template

## Processing Activity Details

| Item | Value |
|------|-------|
| Processing Activity Name | Customer Onboarding Data Collection |
| Controller | Prism Data Systems AG |
| Purpose | Account creation, identity verification, contractual fulfillment |
| Lawful Basis | Article 6(1)(b) — Performance of a contract |
| Date of Assessment | 2026-03-14 |
| Assessor | Data Protection Office, Prism Data Systems AG |
| Review Date | 2026-06-14 (quarterly) |

## Field-Level Minimization Assessment

### Field: email

| Criterion | Score (0-2) | Justification |
|-----------|-------------|---------------|
| Necessity | 2 | Required for account authentication and transactional notifications |
| Proportionality | 2 | No less identifying alternative can fulfill authentication requirement |
| Aggregation potential | 2 | Cannot be meaningfully aggregated for core purpose |
| Pseudonymization feasibility | 1 | Can be pseudonymized in analytics pipelines but not in transactional context |
| Temporal scope | 2 | Required for duration of account lifecycle |
| Access scope | 1 | Support and authentication services require access |
| **Total** | **10** | **RETAIN WITH SAFEGUARDS** |

**Technical controls applied:**
- Field-level AES-256-GCM encryption at rest (DEK: DEK-email-v003)
- Dynamic masking for support agents (m***@domain.ch)
- Pseudonymized via HMAC-SHA256 before analytics pipeline ingestion
- Access logged with 90-day audit trail retention

### Field: date_of_birth

| Criterion | Score (0-2) | Justification |
|-----------|-------------|---------------|
| Necessity | 1 | Needed only for initial age verification; full date not required ongoing |
| Proportionality | 0 | Age bracket (18+/under 18) sufficient after initial verification |
| Aggregation potential | 0 | Can be generalized to age bracket immediately after verification |
| Pseudonymization feasibility | 0 | Can be pseudonymized or replaced with boolean age flag |
| Temporal scope | 0 | Not needed beyond initial verification transaction |
| Access scope | 0 | No role requires ongoing access to raw value |
| **Total** | **1** | **ELIMINATE or AGGREGATE** |

**Remediation action:**
- Convert to boolean `is_age_verified: true` after initial verification
- Delete raw date_of_birth within 24 hours of successful verification
- Store only the verification timestamp and result, not the input value

### Field: ip_address

| Criterion | Score (0-2) | Justification |
|-----------|-------------|---------------|
| Necessity | 2 | Required for fraud detection and geographic access restrictions |
| Proportionality | 1 | Truncated IP (first three octets) sufficient for geographic analysis; full IP needed for fraud |
| Aggregation potential | 1 | Can be truncated for geographic analysis but full address needed for fraud correlation |
| Pseudonymization feasibility | 0 | Can be pseudonymized after fraud detection window expires |
| Temporal scope | 1 | Required for 7-day fraud detection window; pseudonymize after |
| Access scope | 1 | Security operations and fraud team only |
| **Total** | **6** | **PROTECT** |

**Technical controls applied:**
- Full IP retained for 7 days in fraud detection pipeline with restricted access
- After 7 days, automatically truncated to /24 subnet for geographic analytics
- After 90 days, pseudonymized via HMAC-SHA256 with quarterly key rotation
- Dynamic masking applied for all non-security roles

## Assessment Summary

| Outcome | Count | Fields |
|---------|-------|--------|
| Eliminate/Aggregate | 1 | date_of_birth |
| Protect (mask/encrypt) | 1 | ip_address |
| Retain with safeguards | 1 | email |

## Approval

| Role | Name | Date | Decision |
|------|------|------|----------|
| Data Protection Officer | Dr. Lukas Meier | 2026-03-14 | Approved with conditions |
| Data Architecture Lead | Anna Kowalski | 2026-03-14 | Approved |
| Security Operations Lead | Thomas Richter | 2026-03-14 | Approved |

**Conditions:**
1. date_of_birth deletion automation must be deployed before the onboarding service goes live
2. IP address truncation pipeline must be verified in staging environment within two weeks
3. Quarterly re-assessment scheduled for 2026-06-14
