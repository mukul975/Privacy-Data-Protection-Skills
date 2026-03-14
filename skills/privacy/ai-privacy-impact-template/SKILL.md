---
name: ai-privacy-impact-template
description: >-
  Provides combined DPIA and AI Act conformity assessment template with
  integrated risk scoring matrix. Covers GDPR Art. 35 DPIA elements, AI Act
  high-risk system requirements, mitigation measures, and human oversight
  assessment. Keywords: DPIA template, conformity assessment, risk scoring,
  AI Act, combined assessment, high-risk AI.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "dpia-template, conformity-assessment, risk-scoring, ai-act, combined-assessment, high-risk"
---

# Combined DPIA and AI Act Conformity Assessment Template

## Overview

High-risk AI systems under the EU AI Act must undergo both a GDPR Art. 35 DPIA and an AI Act conformity assessment. Rather than conducting these as separate exercises, this skill provides an integrated template that satisfies both frameworks simultaneously. The combined assessment ensures consistency between GDPR privacy risk analysis and AI Act safety and fundamental rights evaluation, reduces duplication, and provides a single risk scoring matrix covering both regulatory dimensions. Art. 26(9) AI Act explicitly requires deployers to use DPIA results when fulfilling AI Act obligations.

## Combined Risk Scoring Matrix

### Risk Dimensions

| Dimension | Source | Weight |
|-----------|--------|--------|
| Privacy risk to data subjects | GDPR Art. 35(7)(c) | 30% |
| Fundamental rights impact | EU AI Act Art. 9(2)(a) | 25% |
| Accuracy and reliability risk | EU AI Act Art. 15 | 20% |
| Transparency and explainability gap | GDPR Art. 13(2)(f) + AI Act Art. 13 | 15% |
| Human oversight adequacy | GDPR Art. 22 + AI Act Art. 14 | 10% |

### Scoring Scale (Per Dimension)

| Score | Level | Description |
|-------|-------|-------------|
| 1 | Minimal | Risk negligible; controls effective |
| 2 | Low | Minor risk; standard controls sufficient |
| 3 | Medium | Moderate risk; enhanced controls needed |
| 4 | High | Significant risk; intensive mitigation required |
| 5 | Critical | Severe risk; may require processing suspension |

### Overall Risk Classification

| Weighted Score | Classification | Action Required |
|---------------|---------------|-----------------|
| 1.0-1.5 | Low | Standard monitoring |
| 1.6-2.5 | Medium | Enhanced monitoring and periodic review |
| 2.6-3.5 | High | Active mitigation and DPO/Board oversight |
| 3.6-4.5 | Very High | Art. 36 prior consultation; deployment hold pending mitigation |
| 4.6-5.0 | Critical | Do not deploy; fundamental redesign required |

## GDPR DPIA Requirements (Art. 35(7))

| Element | Reference | Combined Assessment Section |
|---------|-----------|---------------------------|
| Systematic description of processing | Art. 35(7)(a) | Section 2: AI System Description |
| Necessity and proportionality | Art. 35(7)(b) | Section 3: Necessity Assessment |
| Risk assessment | Art. 35(7)(c) | Section 5: Combined Risk Register |
| Mitigation measures | Art. 35(7)(d) | Section 6: Mitigation Measures |

## AI Act Conformity Assessment Requirements

For high-risk AI systems (Annex III), the conformity assessment per Art. 43 requires:

| Element | Reference | Combined Assessment Section |
|---------|-----------|---------------------------|
| Risk management system | Art. 9 | Section 5: Combined Risk Register |
| Data governance | Art. 10 | Section 2: Training Data Governance |
| Technical documentation | Art. 11 | Full combined assessment document |
| Record-keeping | Art. 12 | Section 7: Monitoring and Logging |
| Transparency | Art. 13 | Section 4: Transparency Assessment |
| Human oversight | Art. 14 | Section 4: Human Oversight |
| Accuracy, robustness, cybersecurity | Art. 15 | Section 5: Technical Risk Assessment |
| Quality management system | Art. 17 | Section 8: Quality Management |

## Mitigation Measures Framework

### Technical Measures

| Measure | GDPR Relevance | AI Act Relevance | Priority |
|---------|---------------|------------------|----------|
| Differential privacy | Training data protection | Robustness (Art. 15) | High for sensitive data |
| Model output perturbation | Model inversion protection | Accuracy trade-off (Art. 15) | Medium |
| Fairness constraints | Non-discrimination (Art. 5(1)(a)) | Bias prevention (Art. 10) | High for high-risk |
| Explainability tools (SHAP/LIME) | Art. 13(2)(f) logic explanation | Interpretability (Art. 13) | High |
| Input/output PII filtering | Data minimisation (Art. 5(1)(c)) | Accuracy (Art. 15) | High for generative AI |
| Encryption (rest/transit) | Security (Art. 32) | Cybersecurity (Art. 15) | Standard |
| Access controls (RBAC) | Security (Art. 32) | Cybersecurity (Art. 15) | Standard |
| Anomaly detection | Breach detection (Art. 33) | Robustness (Art. 15) | Medium |

### Organisational Measures

| Measure | GDPR Relevance | AI Act Relevance |
|---------|---------------|------------------|
| AI ethics review board | Accountability (Art. 5(2)) | Quality management (Art. 17) |
| Model cards | Transparency (Art. 13-14) | Technical documentation (Art. 11) |
| Regular bias audits | Fairness (Art. 5(1)(a)) | Bias monitoring (Art. 10) |
| Incident response for AI | Breach notification (Art. 33-34) | Post-market monitoring (Art. 72) |
| Staff training on AI risks | Accountability | Human oversight (Art. 14) |
| Documentation and record-keeping | Accountability (Art. 5(2)) | Record-keeping (Art. 12) |

## Enforcement Relevance

- **AI Act Art. 26(9)**: Deployers of high-risk AI shall use GDPR Art. 35 DPIA information when fulfilling AI Act obligations — the combined assessment implements this requirement.
- **AI Act Art. 43**: Conformity assessment procedures for high-risk AI systems.
- **GDPR Art. 35**: DPIA requirements — the combined template satisfies all Art. 35(7) elements.

## Integration Points

- **ai-dpia**: Combined template extends the AI DPIA methodology
- **ai-act-high-risk-docs**: Conformity assessment documentation aligns with high-risk requirements
- **ai-bias-special-category**: Bias assessment results feed into combined risk register
- **ai-automated-decisions**: Human oversight assessment integrates Art. 22 and Art. 14 requirements
