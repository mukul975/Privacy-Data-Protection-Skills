# AI Model Privacy Audit Report Template

## Organisation: Cerebrum AI Labs

---

## SECTION 1: AUDIT OVERVIEW

| Field | Value |
|-------|-------|
| Audit ID | MPA-2026-___ |
| Model Name | |
| Model Version | |
| Audit Trigger | Pre-deployment / Periodic / Post-retraining / Incident / Regulatory |
| Threat Model | Black-box / Grey-box / White-box |
| Audit Date | |
| Auditor | |
| Next Audit Date | |

---

## SECTION 2: MODEL PROFILE

| Attribute | Value |
|-----------|-------|
| Model type/architecture | |
| Parameter count | |
| Training data size | |
| Training epochs | |
| Regularisation | |
| Differential privacy | Yes (epsilon=___) / No |
| Deployment context | |
| Data sensitivity level | General / Special Category / Highly Sensitive |

---

## SECTION 3: ATTACK RESULTS

### 3.1 Membership Inference

| Element | Value |
|---------|-------|
| Attack method | Population metric / Reference model / Shadow model / LiRA |
| Tool used | ML Privacy Meter / Custom / Other: |
| Samples tested | |
| TPR@0.1% FPR | |
| TPR@1% FPR | |
| AUC | |
| Most vulnerable subgroup | |
| Risk Level | Acceptable (<5%) / Elevated (5-15%) / Unacceptable (>15%) |

### 3.2 Training Data Extraction

| Element | Value |
|---------|-------|
| Attack method | Prompt-based / Gradient-based / Canary / Generative |
| Canaries inserted | ___ at frequencies: |
| Canary extraction rate | ___% |
| Verbatim match rate | ___% |
| PII types extracted | |
| PII volume extracted | |
| Risk Level | Acceptable (<0.1%) / Elevated (0.1-1%) / Unacceptable (>1%) |

### 3.3 Model Inversion

| Element | Value |
|---------|-------|
| Attack method | Confidence-based / GAN-based / Gradient-based |
| Targets tested | |
| SSIM score | |
| PSNR score | |
| Re-identification possible? | Yes / No |
| Risk Level | Acceptable (<0.3) / Elevated (0.3-0.6) / Unacceptable (>0.6) |

### 3.4 Attribute Inference

| Element | Value |
|---------|-------|
| Attack method | Correlation-based / Partial knowledge / Group inference |
| Sensitive attributes tested | |
| Accuracy above baseline per attribute: | |
| - Attribute 1: | ___% |
| - Attribute 2: | ___% |
| Risk Level | Acceptable (<10%) / Elevated (10-25%) / Unacceptable (>25%) |

---

## SECTION 4: RESULTS SUMMARY

| Attack Category | Metric | Value | Threshold | Result |
|----------------|--------|-------|-----------|--------|
| Membership Inference | TPR@1%FPR | | <5% / <15% | Pass/Warn/Fail |
| Training Data Extraction | Extraction Rate | | <0.1% / <1% | Pass/Warn/Fail |
| Model Inversion | SSIM | | <0.3 / <0.6 | Pass/Warn/Fail |
| Attribute Inference | Accuracy Above Baseline | | <10% / <25% | Pass/Warn/Fail |

**Overall Audit Outcome**: Pass / Conditional Pass / Fail

---

## SECTION 5: RECOMMENDED MITIGATIONS

| # | Attack Category | Mitigation | Priority | Owner | Deadline |
|---|----------------|-----------|----------|-------|----------|
| 1 | | | Critical/High/Medium | | |
| 2 | | | | | |
| 3 | | | | | |

---

## SECTION 6: REMEDIATION VALIDATION

| Mitigation Applied | Re-test Result | Threshold Met? |
|-------------------|----------------|----------------|
| | | Yes / No |

---

## SECTION 7: SIGN-OFF

| Role | Name | Date |
|------|------|------|
| Audit Lead | | |
| Model Owner | | |
| DPO | | |
