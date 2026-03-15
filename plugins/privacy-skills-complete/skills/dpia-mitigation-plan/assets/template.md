# DPIA Mitigation Plan

## Plan Details

| Field | Value |
|-------|-------|
| DPIA Reference | DPIA-QLH-2026-012 |
| Processing Activity | Patient Genomic Profiling Platform |
| Controller | QuantumLeap Health Technologies |
| Plan Date | 2026-03-14 |
| Plan Owner | Dr. Elena Vasquez, DPO |
| Risk Appetite | Score 6 or below (Medium) |
| Total Budget | EUR 310,000 |

---

## Risk Summary (Inherent vs Residual)

| Risk ID | Description | Inherent Score | Inherent Level | Residual Score | Residual Level | Reduction | Within Appetite |
|---------|-------------|---------------|----------------|---------------|----------------|-----------|-----------------|
| R1 | Unauthorised access to genomic datasets | 12 | Very High | 4 | Medium | 8 pts | Yes |
| R2 | Algorithmic bias in genomic risk scores | 12 | Very High | 4 | Medium | 8 pts | Yes |
| R3 | Purpose creep by insurance partners | 6 | Medium | 3 | Low | 3 pts | Yes |
| R4 | Platform unavailability during treatment | 6 | Medium | 3 | Low | 3 pts | Yes |
| R5 | Re-identification via research linkage | 8 | High | 4 | Medium | 4 pts | Yes |

---

## Mitigation Measures

### M1: Genomic Data Encryption

| Field | Value |
|-------|-------|
| Description | AES-256 encryption at rest for all genomic data stores (PostgreSQL TDE, S3 SSE-KMS); TLS 1.3 for all data in transit including inter-service communication |
| Type | Technical |
| Addresses | R1 (Unauthorised access) |
| Effect | Reduces likelihood by 1 level |
| Owner | Marcus Reinhardt, CISO |
| Budget | EUR 45,000 |
| Timeline | 2026-01-15 to 2026-03-01 |
| Status | **Verified** |
| Verification | Penetration test by Cure53 (Report ref: CURE53-QLH-2026-003) |
| Result | Passed: no unencrypted data exposure found; all endpoints enforce TLS 1.3 minimum |

### M2: Privileged Access Management

| Field | Value |
|-------|-------|
| Description | Role-based access control with mandatory MFA; CyberArk PAM for all administrative and genomic data access; session recording for privileged operations |
| Type | Technical |
| Addresses | R1 (Unauthorised access) |
| Effect | Reduces likelihood by 1 level |
| Owner | IT Security Lead |
| Budget | EUR 35,000 |
| Timeline | 2026-02-01 to 2026-03-15 |
| Status | **Implemented** (verification pending) |
| Verification | Access control audit scheduled for 2026-04-01 |

### M3: Algorithmic Bias Audit Programme

| Field | Value |
|-------|-------|
| Description | Systematic bias testing using validation cohorts spanning 12 ethnic groups with minimum 5,000 samples each; demographic parity, equalised odds, and calibration metrics evaluated for each genomic risk model |
| Type | Technical |
| Addresses | R2 (Algorithmic bias) |
| Effect | Reduces likelihood by 1 level |
| Owner | Head of AI Research |
| Budget | EUR 80,000 |
| Timeline | 2026-03-01 to 2026-06-30 |
| Status | **In Progress** -- cohort recruitment at 67% (8/12 groups at minimum sample) |
| Verification | Statistical bias metrics: demographic parity difference below 0.1, equalised odds difference below 0.1 |

### M4: Clinical Review Board Oversight

| Field | Value |
|-------|-------|
| Description | Independent clinical review board reviews all treatment pathway recommendations classified as high-impact (oncology, rare disease, pharmacogenomics); mandatory human-in-the-loop for confidence scores below 85% |
| Type | Organisational |
| Addresses | R2 (Algorithmic bias) |
| Effect | Reduces likelihood by 1 level |
| Owner | Chief Medical Officer, Prof. Dr. Annika Berger |
| Budget | EUR 25,000 (annual board compensation) |
| Timeline | 2026-04-01 to 2026-05-15 |
| Status | **Approved** -- board members nominated; terms of reference drafted |
| Verification | Board meeting minutes; override rate tracking (target: reviewed 100% of high-impact recommendations) |

### M5: Insurance Partner Data Processing Agreements

| Field | Value |
|-------|-------|
| Description | Art. 28 DPA with all insurance partners restricting data use to coverage eligibility assessment only; explicit GenDG Section 18 compliance clause prohibiting use for underwriting, premium calculation, or coverage exclusion |
| Type | Organisational |
| Addresses | R3 (Purpose creep) |
| Effect | Reduces likelihood by 1 level |
| Owner | Legal Counsel, Dr. Katrin Neumann |
| Budget | EUR 15,000 |
| Timeline | 2026-01-01 to 2026-02-28 |
| Status | **Verified** |
| Verification | Legal review of executed DPA terms against Art. 28(3) requirements |
| Result | DPA executed with all 3 insurance partners (AOK Bayern, Techniker Krankenkasse, Allianz Private Health); GenDG clause included and countersigned |

### M6: Multi-Region Infrastructure Resilience

| Field | Value |
|-------|-------|
| Description | Active-passive multi-region deployment (primary: Frankfurt eu-central-1, secondary: Dublin eu-west-1) with automated DNS failover; immutable backup strategy with 4-hour RPO |
| Type | Technical |
| Addresses | R4 (Platform unavailability) |
| Effect | Reduces likelihood by 1 level |
| Owner | Infrastructure Lead |
| Budget | EUR 60,000 (annual infrastructure cost) |
| Timeline | 2025-11-01 to 2026-02-01 |
| Status | **Verified** |
| Verification | Failover drill conducted 2026-02-15 with clinical operations team |
| Result | RTO measured at 47 seconds; RPO measured at 3.8 hours; all clinical endpoints restored within SLA |

### M7: Clinical Fallback Protocols

| Field | Value |
|-------|-------|
| Description | Documented manual treatment pathway selection protocols for use when genomic platform is unavailable; locally cached last-known risk profiles at each hospital; clinician training completed |
| Type | Organisational |
| Addresses | R4 (Platform unavailability) |
| Effect | Reduces likelihood by 1 level |
| Owner | Clinical Operations Director |
| Budget | EUR 10,000 |
| Timeline | 2026-01-15 to 2026-03-01 |
| Status | **Implemented** (verification pending) |
| Verification | Tabletop exercise with clinical staff at 3 pilot hospitals; scheduled for 2026-04-10 |

### M8: Differential Privacy for Research Exports

| Field | Value |
|-------|-------|
| Description | Differential privacy mechanism (epsilon=1.0, delta=1e-5) applied to all research data exports; privacy budget tracking per dataset; automatic export blocking when budget exhausted |
| Type | Technical |
| Addresses | R5 (Re-identification) |
| Effect | Reduces likelihood by 1 level |
| Owner | Privacy Engineering Team |
| Budget | EUR 40,000 |
| Timeline | 2026-04-01 to 2026-07-31 |
| Status | **Approved** -- design specification complete; development sprint planned |
| Verification | Privacy budget verification; re-identification attack simulation (k-anonymity check k>=50) |

---

## Implementation Dashboard

| Status | Count | Budget |
|--------|-------|--------|
| Verified | 3 (M1, M5, M6) | EUR 120,000 |
| Implemented | 2 (M2, M7) | EUR 45,000 |
| In Progress | 1 (M3) | EUR 80,000 |
| Approved | 2 (M4, M8) | EUR 65,000 |
| **Total** | **8** | **EUR 310,000** |

---

## Art. 36 Prior Consultation Assessment

| Field | Value |
|-------|-------|
| Prior Consultation Required | **No** |
| Rationale | All residual risks reduced to Medium (score 4) or Low (score 3) through implemented and planned mitigation measures, within the organisational risk appetite threshold of 6 |
| Condition | Prior consultation assessment contingent on M3 (bias audit) and M8 (differential privacy) achieving target effectiveness. If verification fails, residual risks R2 and R5 may require re-assessment |
| Monitoring | Quarterly re-assessment of residual risk levels; next review: 2026-06-30 |

---

## Sign-Off

| Role | Name | Date | Decision |
|------|------|------|----------|
| DPO | Dr. Elena Vasquez | 2026-03-14 | Mitigation plan approved; residual risk within appetite |
| CISO | Marcus Reinhardt | 2026-03-14 | Technical measures on track; M2 verification prioritised |
| CFO | Thomas Weiss | 2026-03-14 | Budget EUR 310,000 approved under privacy programme allocation |
| CMO | Prof. Dr. Annika Berger | 2026-03-14 | Clinical review board establishment approved |
