# Health Data Processing DPIA Report

## Reference: DPIA-QLH-2026-0016

| Field | Value |
|-------|-------|
| Organisation | QuantumLeap Health Technologies |
| Processing | Phase III Clinical Trial QT-CARDIO-301 Data Processing |
| Art. 9(2) Exemption | Art. 9(2)(j) — Scientific research with Art. 89(1) safeguards |
| Date | 2026-03-14 |
| DPO | Dr. Elena Vasquez, CIPP/E, CIPM |
| Principal Investigator | Prof. Dr. Maria Santos, Charite Berlin |

---

## Health Data Categories

| Category | Elements | Sensitivity |
|----------|----------|------------|
| Direct health data | ECG readings, cardiac biomarkers (troponin, BNP), adverse event reports, vital signs | Very High |
| Genetic data | Pharmacogenomic CYP450 enzyme panel (CYP2D6, CYP3A4, CYP2C19) | Maximum |
| Clinical trial data | Randomisation group, dosing records, efficacy endpoints, concomitant medications | Very High |

## Art. 9(2)(j) Exemption Validation

| Condition | Status |
|-----------|--------|
| Necessary for scientific research purposes | Met — Phase III clinical trial is scientific research |
| Art. 89(1) safeguards: data minimisation | Met — only protocol-specified data collected |
| Art. 89(1) safeguards: pseudonymisation | Met — participants identified by subject number only; re-identification key held by PI at clinical site |
| EU or Member State law basis | Met — BDSG Section 27 authorises health data processing for scientific research with appropriate safeguards |

## Risk Assessment Summary

| Risk | Level | Mitigation | Residual |
|------|-------|------------|---------|
| Participant re-identification from genetic data | High | Pseudonymisation; genetic data stored separately from clinical data; access restricted to pharmacogenomics team only | Medium |
| Breach exposing clinical trial participant health data | Very High | AES-256 encryption; segregated trial database; SOC 2 certified hosting; 72-hour breach response | Medium |
| Discriminatory use of pharmacogenomic data | High | Genetic data used solely for dosing optimisation; contractual prohibition on insurance/employment use; automatic deletion after trial analysis | Low |

## Approvals

| Role | Name | Date |
|------|------|------|
| DPO | Dr. Elena Vasquez | 2026-03-14 |
| Principal Investigator | Prof. Dr. Maria Santos | 2026-03-14 |
| Head of Clinical Operations | Dr. Lisa Bergmann | 2026-03-15 |
| Ethics Committee Approval | Charite Ethics Committee ref EC-2026-0147 | 2026-02-28 |
