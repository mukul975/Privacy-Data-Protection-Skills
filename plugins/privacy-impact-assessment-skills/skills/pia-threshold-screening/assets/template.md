# PIA Threshold Screening Report

## Processing Activity Details

| Field | Value |
|-------|-------|
| Activity Name | Patient Genomic Profiling Platform |
| Controller | QuantumLeap Health Technologies |
| Screening Date | 2026-03-14 |
| Screened By | Dr. Elena Vasquez, DPO |
| RoPA Reference | ROPA-QLH-2026-047 |
| Business Unit | Precision Medicine Division |

## Processing Description

QuantumLeap Health Technologies proposes deploying a machine learning-based genomic profiling platform across its 12 partner hospital networks. The platform ingests whole genome sequencing (WGS) data, electronic health records (EHR), lifestyle questionnaire responses, and environmental exposure datasets to generate personalised health risk scores and treatment pathway recommendations. The system will process data for approximately 450,000 patients in the initial rollout phase, with projected scaling to 2 million patients within 36 months.

---

## Phase 1: Mandatory DPIA Triggers (Art. 35(3))

### Art. 35(3)(a) -- Systematic Profiling with Legal/Significant Effects

| Element | Assessment |
|---------|-----------|
| Systematic and extensive evaluation? | **Yes** -- Continuous genomic risk scoring across entire patient cohort with periodic re-evaluation as new research data becomes available |
| Based on automated processing/profiling? | **Yes** -- ML models generate risk scores and treatment recommendations without manual clinician intervention at the scoring stage |
| Legal or similarly significant effects? | **Yes** -- Risk scores directly influence treatment pathway selection, clinical trial eligibility, and are shared with insurance partners for coverage determinations |

**Result: MANDATORY TRIGGER MET**

### Art. 35(3)(b) -- Large-Scale Special Category Processing

| Element | Assessment |
|---------|-----------|
| Special category or criminal data? | **Yes** -- Genetic data (Art. 9(1)), health data (Art. 9(1)) |
| Large scale? | **Yes** -- 450,000+ patients across 12 hospital networks in Germany, Austria, and Switzerland |

**Result: MANDATORY TRIGGER MET**

### Art. 35(3)(c) -- Large-Scale Public Area Monitoring

| Element | Assessment |
|---------|-----------|
| Systematic monitoring? | No -- Processing involves clinical data analysis, not observation/surveillance |
| Publicly accessible area? | No -- Hospital clinical information systems are restricted-access environments |
| Large scale? | N/A |

**Result: NOT MET**

---

## Phase 2: National Supervisory Authority Blacklist Check

### BfDI / DSK (Germany)

| Field | Value |
|-------|-------|
| List Consulted | Datenschutzkonferenz Muss-Liste (2018, updated 2023) |
| Match Found | **Yes** |
| Matched Entry | Category 8: "Processing of genetic data or biometric data for the purpose of uniquely identifying a natural person" |
| Additional Match | Category 3: "Extensive processing of personal data for profiling purposes that has effects on natural persons" |

### DSB (Austria)

| Field | Value |
|-------|-------|
| List Consulted | DSFA-Verordnung (DSFA-V), BGBl. II Nr. 278/2018 |
| Match Found | **Yes** |
| Matched Entry | Section 2(3): Large-scale processing of genetic or biometric data |

---

## Phase 3: WP248rev.01 Nine-Criteria Assessment

| # | Criterion | Status | Rationale |
|---|-----------|--------|-----------|
| 1 | Evaluation or scoring | **Met** | Genomic risk scoring evaluates patient predispositions for 200+ conditions, generating composite health risk indices |
| 2 | Automated decision-making with legal/similar effect | **Met** | Automated treatment pathway recommendations directly influence clinical decisions; insurance coverage implications constitute similarly significant effects |
| 3 | Systematic monitoring | Not Met | Platform performs analytical processing of stored data, not real-time monitoring or surveillance |
| 4 | Sensitive data or highly personal data | **Met** | Genetic data and health data are explicitly special category under Art. 9(1); genomic data is among the most sensitive personal data categories |
| 5 | Data processed on a large scale | **Met** | 450,000+ patients, 12 hospital networks, 3 countries (DACH region), processing WGS data (approx. 100GB per patient) |
| 6 | Matching or combining datasets | **Met** | Platform combines WGS data, EHR records, lifestyle questionnaire data, environmental exposure databases, and published genomic research datasets |
| 7 | Vulnerable data subjects | **Met** | Patients receiving clinical care are in a position of imbalance relative to the healthcare provider; many are in acute treatment |
| 8 | Innovative use or new technology | **Met** | Novel ML-based genomic interpretation models; federated learning architecture across hospital networks; proprietary variant classification algorithms |
| 9 | Preventing exercise of a right | Not Met | Patients can decline genomic profiling and continue receiving standard-of-care treatment without penalty |

**Criteria Met: 7 of 9** | Borderline: 0 | Threshold: 2

---

## Screening Outcome

| Field | Value |
|-------|-------|
| **Decision** | **DPIA MANDATORY** |
| Primary Trigger | Art. 35(3)(a): Systematic profiling with significant effects AND Art. 35(3)(b): Large-scale special category processing |
| Supporting Factors | National blacklist match (BfDI Category 8, DSB Section 2(3)); 7 of 9 WP248 criteria met |
| DPO Review | Completed -- Dr. Elena Vasquez confirms DPIA mandatory |
| Prior Consultation Risk | **High** -- Art. 36 prior consultation with BfDI may be required if residual risk cannot be sufficiently mitigated |

## Next Steps

| Action | Responsible | Deadline |
|--------|-------------|----------|
| Initiate full DPIA under Art. 35(7) | DPO Office | 2026-03-21 |
| Assign DPIA lead assessor | Head of Privacy Engineering | 2026-03-18 |
| Register in DPIA portfolio (ref: DPIA-QLH-2026-012) | Privacy Operations | 2026-03-15 |
| Engage external genomics ethics reviewer | Chief Medical Officer | 2026-04-01 |
| Prepare Art. 36 prior consultation package | DPO Office | 2026-05-15 |
| Notify joint controllers (partner hospitals) of DPIA requirement | Legal Department | 2026-03-25 |

## Sign-Off

| Role | Name | Date | Decision |
|------|------|------|----------|
| DPO | Dr. Elena Vasquez | 2026-03-14 | DPIA Required -- approved for full assessment |
| CISO | Marcus Reinhardt | 2026-03-14 | Acknowledged -- security team to support DPIA |
| Head of Precision Medicine | Prof. Dr. Annika Berger | 2026-03-14 | Acknowledged -- project timeline adjusted |
