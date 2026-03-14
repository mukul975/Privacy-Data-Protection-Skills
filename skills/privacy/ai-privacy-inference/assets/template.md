# AI Inference Privacy Assessment — Template

## Organisation: Cerebrum AI Labs
## Assessment Reference: INF-PRIV-2026-___
## Date: ____-__-__
## Assessor: ________________
## DPO Reviewer: ________________

---

## 1. AI System Identification

| Field | Value |
|-------|-------|
| System ID | |
| System Name | |
| Version | |
| System Owner | |
| Inference Description | |

## 2. Inference Classification

| Field | Value |
|-------|-------|
| Inference Type | Observed / Derived / Inferred / Aggregated |
| Data Subjects | |
| Estimated Volume | |
| Input Features | |
| Output Format | |

## 3. Profiling Level Assessment

| Question | Answer | Notes |
|----------|--------|-------|
| Does the system evaluate personal aspects of individuals? | Yes / No | |
| Does the inference feed a decision about an individual? | Yes / No | |
| Is a human meaningfully involved in the decision? | Yes / No | |
| Does the decision produce legal or similarly significant effects? | Yes / No | |

**Profiling Level**: Profiling Only / Profiling with Human Decision / Solely Automated Decision

## 4. Art. 22 Assessment (If Solely Automated)

| Question | Answer | Evidence |
|----------|--------|----------|
| Which Art. 22(2) exception applies? | Contract / Law / Explicit Consent / None | |
| Is human intervention available? | Yes / No | |
| Can data subjects express their point of view? | Yes / No | |
| Is there a contestation mechanism? | Yes / No | |
| Are individual explanations available? | Yes / No | |
| Explanation method | SHAP / LIME / Other: _______ | |
| Contestation SLA | ___ business days | |

## 5. Special Category Risk Assessment

| Feature | Correlated Art. 9 Characteristic | Correlation Strength | Mitigation |
|---------|--------------------------------|---------------------|------------|
| | | High / Medium / Low | |
| | | High / Medium / Low | |
| | | High / Medium / Low | |

**Special Category Risk Level**: None / Proxy (Low) / Proxy (High) / Direct Art. 9 Inference

**If Art. 9 risk identified, Art. 9(2) condition**: ________________________

## 6. Accuracy Assessment

| Metric | Overall | Group 1: ___ | Group 2: ___ | Group 3: ___ |
|--------|---------|-------------|-------------|-------------|
| Precision | | | | |
| Recall | | | | |
| F1 Score | | | | |
| Disparate Impact Ratio | N/A | | | |

**Four-Fifths Rule**: PASS / FAIL (lowest group ratio: ____)

**Confidence Threshold**: Inferences below ___% confidence require human review

**Staleness Policy**: Inferences regenerated every ___ days

## 7. Transparency Measures

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Privacy notice discloses profiling | Complete / Pending | |
| Logic described (Art. 13(2)(f)) | Complete / Pending | |
| Significance and consequences disclosed | Complete / Pending | |
| AI Act Art. 52 transparency met | Complete / Pending / N/A | |

## 8. Data Subject Rights Implementation

| Right | Process Documented | Tested | SLA |
|-------|-------------------|--------|-----|
| Access (Art. 15) | Yes / No | Yes / No | ___ days |
| Rectification (Art. 16) | Yes / No | Yes / No | ___ days |
| Objection (Art. 21) | Yes / No | Yes / No | ___ days |
| Contestation (Art. 22(3)) | Yes / No | Yes / No | ___ days |
| Explanation | Yes / No | Yes / No | ___ days |

## 9. Retention and Governance

| Data Type | Retention Period | Automated Deletion |
|-----------|-----------------|-------------------|
| Inference outputs | ___ days | Yes / No |
| Input data used for inference | ___ days | Yes / No |
| Explanation logs | ___ days | Yes / No |
| Audit trail | ___ months | Yes / No |

## 10. DPIA and Lawful Basis

| Field | Value |
|-------|-------|
| Lawful Basis | Art. 6(1)(_): ________________ |
| LIA Reference (if Art. 6(1)(f)) | |
| DPIA Reference | |
| DPIA Outcome | |

## 11. Risk Summary

| Risk | Severity | Likelihood | Mitigation | Residual Risk |
|------|----------|------------|------------|--------------|
| Inaccurate inference causing harm | | | | |
| Art. 9 proxy discrimination | | | | |
| Over-reliance on automated output | | | | |
| Inference scope creep beyond purpose | | | | |

## Sign-Off

| Role | Name | Approval | Date |
|------|------|----------|------|
| ML Engineering Lead | | Approved / Blocked | |
| Data Protection Officer | | Approved / Blocked | |
| Responsible AI Lead | | Approved / Blocked | |

---

*Assessment conducted per Cerebrum AI Labs AI Governance Policy AGP-2025-v2.0, GDPR Art. 22, and EDPB Guidelines WP 251 rev.01.*
