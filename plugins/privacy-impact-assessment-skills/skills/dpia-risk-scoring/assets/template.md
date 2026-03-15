# DPIA Risk Scoring Report

## Assessment Details

| Field | Value |
|-------|-------|
| Assessment ID | DPIA-QLH-2026-012-RISK |
| Processing Activity | Patient Genomic Profiling Platform |
| Controller | QuantumLeap Health Technologies |
| Assessment Date | 2026-03-14 |
| Assessor | Dr. Elena Vasquez, DPO |
| Risk Appetite Threshold | Score 6 (Medium) |
| DPIA Reference | DPIA-QLH-2026-012 |

---

## Risk Register

### R1: Unauthorised Access to Genomic Datasets

| Field | Value |
|-------|-------|
| Description | Unauthorised access to genomic datasets enabling re-identification of patients and disclosure of genetic predispositions |
| Rights Category | Loss of confidentiality |
| Risk Source | External attacker exploiting application vulnerabilities; insider threat from authorised users exceeding access scope |
| Inherent Severity | 4 (Maximum) -- Genomic data disclosure is irreversible; genetic predispositions cannot be changed |
| Inherent Likelihood | 3 (Significant) -- Healthcare sector is heavily targeted; genomic data has high black-market value |
| **Inherent Risk** | **12 (Very High)** |

**Mitigation Measures:**

| Measure | Type | Status | Reduction |
|---------|------|--------|-----------|
| AES-256 encryption at rest for all genomic data stores; TLS 1.3 for all data in transit | Technical | Implemented | -1 |
| Role-based access control with MFA and privileged access management (CyberArk) | Technical | Implemented | -1 |
| Quarterly penetration testing by certified third party (Cure53) | Technical | Implemented | -0 |
| Data Loss Prevention (DLP) rules blocking bulk genomic data exports | Technical | Planned | -0 |

| Residual Severity | Residual Likelihood | **Residual Risk** |
|-------------------|--------------------|--------------------|
| 4 (Maximum) | 1 (Negligible) | **4 (Medium)** |

**Within Appetite: Yes**

---

### R2: Algorithmic Bias in Genomic Risk Scores

| Field | Value |
|-------|-------|
| Description | ML models produce biased risk scores for under-represented ethnic groups, leading to discriminatory treatment recommendations |
| Rights Category | Discrimination |
| Risk Source | Training data bias (overrepresentation of European-descent cohorts); model architecture limitations |
| Inherent Severity | 4 (Maximum) -- Biased treatment recommendations could lead to physical harm or denial of effective care |
| Inherent Likelihood | 3 (Significant) -- Known issue in genomics: 78% of GWAS participants are of European descent (Nature Genetics, 2023) |
| **Inherent Risk** | **12 (Very High)** |

**Mitigation Measures:**

| Measure | Type | Status | Reduction |
|---------|------|--------|-----------|
| Bias audit using validation cohorts spanning 12 ethnic groups with minimum 5,000 samples each | Technical | Planned | -1 |
| Clinical review board oversight for all high-impact treatment pathway recommendations | Organisational | Planned | -1 |
| Mandatory human-in-the-loop for any recommendation with confidence score below 85% | Organisational | Planned | -0 |

| Residual Severity | Residual Likelihood | **Residual Risk** |
|-------------------|--------------------|--------------------|
| 4 (Maximum) | 1 (Negligible) | **4 (Medium)** |

**Within Appetite: Yes**

---

### R3: Purpose Creep by Insurance Partners

| Field | Value |
|-------|-------|
| Description | Insurance partner organisations use shared genomic risk scores beyond the agreed coverage assessment purpose for underwriting exclusions or premium adjustments |
| Rights Category | Loss of purpose limitation |
| Risk Source | Data recipient contractual non-compliance; ambiguous data sharing terms |
| Inherent Severity | 3 (Significant) -- Could lead to insurance discrimination based on genetic predispositions |
| Inherent Likelihood | 2 (Limited) -- Regulated sector with existing contractual controls |
| **Inherent Risk** | **6 (Medium)** |

**Mitigation Measures:**

| Measure | Type | Status | Reduction |
|---------|------|--------|-----------|
| Art. 28 DPA with insurance partners strictly limiting purpose to coverage eligibility assessment | Organisational | Implemented | -1 |
| Technical controls: aggregated risk categories shared instead of raw scores; no individual genomic data transferred | Technical | Implemented | -0 |

| Residual Severity | Residual Likelihood | **Residual Risk** |
|-------------------|--------------------|--------------------|
| 3 (Significant) | 1 (Negligible) | **3 (Low)** |

**Within Appetite: Yes**

---

### R4: Platform Unavailability During Critical Treatment

| Field | Value |
|-------|-------|
| Description | Genomic profiling platform unavailable during critical clinical decision-making due to system failure or ransomware attack |
| Rights Category | Loss of availability |
| Risk Source | Infrastructure failure; ransomware targeting healthcare systems |
| Inherent Severity | 3 (Significant) -- Clinicians unable to access genomic insights for treatment decisions |
| Inherent Likelihood | 2 (Limited) -- Cloud infrastructure provides baseline resilience |
| **Inherent Risk** | **6 (Medium)** |

**Mitigation Measures:**

| Measure | Type | Status | Reduction |
|---------|------|--------|-----------|
| Multi-region deployment (Frankfurt, Dublin) with automated failover under 60 seconds | Technical | Implemented | -1 |
| Clinical fallback protocols: manual treatment pathway selection using last-known risk profiles (cached locally at each hospital) | Organisational | Implemented | -1 |
| Immutable backup strategy with 4-hour RPO and 1-hour RTO | Technical | Implemented | -0 |

| Residual Severity | Residual Likelihood | **Residual Risk** |
|-------------------|--------------------|--------------------|
| 3 (Significant) | 1 (Negligible) | **3 (Low)** |

**Within Appetite: Yes**

---

### R5: Re-identification via Research Database Linkage

| Field | Value |
|-------|-------|
| Description | Patients re-identified by linking pseudonymised genomic research exports with public genealogy databases or published GWAS datasets |
| Rights Category | Identity theft or fraud |
| Risk Source | Research data consumers; publicly available genetic databases (e.g., GEDmatch incidents) |
| Inherent Severity | 4 (Maximum) -- Full re-identification enables disclosure of all genetic predispositions |
| Inherent Likelihood | 2 (Limited) -- Requires sophisticated linkage attack and access to reference datasets |
| **Inherent Risk** | **8 (High)** |

**Mitigation Measures:**

| Measure | Type | Status | Reduction |
|---------|------|--------|-----------|
| Differential privacy (epsilon=1.0) applied to all research data exports | Technical | Planned | -1 |
| k-anonymity (k=50) requirement for any aggregated research dataset | Technical | Planned | -0 |

| Residual Severity | Residual Likelihood | **Residual Risk** |
|-------------------|--------------------|--------------------|
| 4 (Maximum) | 1 (Negligible) | **4 (Medium)** |

**Within Appetite: Yes**

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Risks Assessed | 5 |
| Inherent Very High | 2 (R1, R2) |
| Inherent High | 1 (R5) |
| Inherent Medium | 2 (R3, R4) |
| Residual Very High | 0 |
| Residual High | 0 |
| Residual Medium | 3 (R1, R2, R5) |
| Residual Low | 2 (R3, R4) |
| Average Risk Reduction | 5.6 points |
| All Risks Within Appetite | Yes |

## Art. 36 Prior Consultation Assessment

| Field | Value |
|-------|-------|
| Prior Consultation Required | **No** |
| Rationale | All residual risks reduced to Medium or Low through planned and implemented mitigation measures. No residual risk at High or Very High level. |
| Monitoring | Quarterly risk re-assessment required; bias audit results to be reviewed after initial 6-month operational period |

## Sign-Off

| Role | Name | Date | Decision |
|------|------|------|----------|
| DPO | Dr. Elena Vasquez | 2026-03-14 | Residual risk within appetite; proceed with planned mitigations |
| CISO | Marcus Reinhardt | 2026-03-14 | Technical measures validated; penetration testing scheduled |
| Head of Precision Medicine | Prof. Dr. Annika Berger | 2026-03-14 | Bias audit cohort recruitment underway |
