---
name: ai-deployment-checklist
description: >-
  Pre-deployment privacy compliance checklist for AI/ML systems covering DPIA
  completion, lawful basis verification, transparency notices, human oversight
  mechanisms, bias testing, and post-deployment monitoring setup. Keywords:
  AI deployment, privacy checklist, go-live, model deployment, compliance gate.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "ai-deployment, privacy-checklist, compliance-gate, model-release, pre-deployment"
---

# AI System Pre-Deployment Privacy Checklist

## Overview

Deploying an AI system that processes personal data requires verification of privacy compliance across multiple dimensions before the system goes live. This checklist serves as a compliance gate in the Cerebrum AI Labs ML deployment pipeline. No AI system may be deployed to production until all mandatory items are verified and signed off by the Data Protection Officer (DPO). The checklist is structured around GDPR requirements, the EU AI Act obligations (for high-risk systems), and internal governance standards.

## Pre-Deployment Compliance Gate

### Gate 1: Legal Basis and DPIA

| Check | Requirement | Status | Evidence |
|-------|-------------|--------|----------|
| Lawful basis documented | Art. 6(1) basis identified and recorded for all personal data processing | Required | LIA or consent records |
| Special categories assessed | Art. 9 data identified; explicit consent or Art. 9(2) exception documented | Required | Data classification report |
| DPIA completed | Art. 35 DPIA completed for high-risk processing (profiling, systematic monitoring, large-scale special categories) | Required if applicable | DPIA document signed by DPO |
| DPIA risks mitigated | All high/critical risks from DPIA have documented mitigations | Required | Risk treatment plan |
| Prior consultation | Art. 36 consultation with supervisory authority if residual risk remains high | Required if applicable | Consultation record |
| Legitimate interest assessment | If relying on Art. 6(1)(f), LIA balancing test completed | Required if LI basis | LIA document |

### Gate 2: Transparency and Information

| Check | Requirement | Status | Evidence |
|-------|-------------|--------|----------|
| Privacy notice updated | Art. 13-14 information includes AI processing details | Required | Updated privacy notice |
| Logic described | "Meaningful information about the logic involved" documented for data subjects | Required for automated decisions | Explanation document |
| Significance disclosed | Envisaged consequences of AI processing disclosed | Required for automated decisions | Privacy notice section |
| Profiling disclosed | If system profiles individuals, this is disclosed in privacy notice | Required if profiling | Privacy notice section |
| AI Act transparency | Art. 52 transparency obligations met (if applicable): inform that they are interacting with AI | Required for AI Act | User interface disclosure |

### Gate 3: Data Subject Rights

| Check | Requirement | Status | Evidence |
|-------|-------------|--------|----------|
| Access process defined | Process for responding to access requests for AI data (inputs, outputs, profiles) | Required | Documented SOP |
| Explanation mechanism | Individual explanations can be generated on request | Required for Art. 22 | Technical capability verified |
| Human intervention available | Art. 22(3) human review process established | Required for solely automated decisions | Process document + trained staff |
| Contestation channel | Data subjects can contest AI decisions and have them reviewed | Required for Art. 22 | Appeal process document |
| Rectification process | Process for correcting AI input data and regenerating outputs | Required | Documented SOP |
| Erasure process | Process for deleting data from training sets, inference logs, embeddings | Required | Documented SOP |

### Gate 4: Data Quality and Bias

| Check | Requirement | Status | Evidence |
|-------|-------------|--------|----------|
| Training data documented | Data sources, size, collection method, preprocessing documented | Required | Data card / dataset documentation |
| Bias testing completed | Model tested for bias across protected attributes (gender, race, age, disability) | Required | Bias test report |
| Fairness metrics acceptable | Disparate impact ratio >0.8 (four-fifths rule) or equivalent metric within acceptable range | Required | Fairness metrics report |
| Data quality verified | Training data completeness, accuracy, representativeness verified | Required | Data quality report |
| Art. 9 data removed or justified | Special category data either removed or lawful basis documented | Required | Data classification report |

### Gate 5: Security and Technical Controls

| Check | Requirement | Status | Evidence |
|-------|-------------|--------|----------|
| Data encryption at rest | Training data and model weights encrypted (AES-256 or equivalent) | Required | Security configuration |
| Data encryption in transit | All API endpoints use TLS 1.2+ | Required | SSL certificate |
| Access controls | Role-based access to model, training data, and inference logs | Required | IAM policy |
| Audit logging | All model invocations logged with timestamp, input hash, output, user | Required | Logging configuration |
| Adversarial robustness | Model tested against common adversarial attacks relevant to its domain | Recommended | Security test report |
| Model versioning | Model versioned in registry with rollback capability | Required | MLflow / model registry |

### Gate 6: Monitoring and Governance

| Check | Requirement | Status | Evidence |
|-------|-------------|--------|----------|
| Performance monitoring | Dashboard tracking accuracy, latency, error rates in production | Required | Monitoring setup |
| Drift detection | Data drift and concept drift detection implemented | Required | Drift monitoring configuration |
| Bias monitoring | Post-deployment bias metrics tracked continuously | Required | Fairness monitoring dashboard |
| Incident response | Process for handling AI-related privacy incidents (e.g., discriminatory output, data leak) | Required | Incident response plan |
| Retraining schedule | Defined schedule for model retraining with fresh data | Required | Retraining plan |
| Retention enforcement | Automated deletion of inference logs and training data per retention schedule | Required | Retention policy + automation |

### Gate 7: EU AI Act (High-Risk Systems Only)

| Check | Requirement | Status | Evidence |
|-------|-------------|--------|----------|
| Risk classification | System classified per Annex III | Required | Classification document |
| Technical documentation | Annex IV documentation complete | Required | Tech doc package |
| Risk management system | Art. 9 continuous risk management implemented | Required | Risk register + process |
| Conformity assessment | Internal or third-party conformity assessment completed | Required | Assessment report |
| EU Declaration of Conformity | Art. 47 declaration prepared | Required | Signed declaration |
| EU database registration | Art. 49 registration completed | Required | Registration confirmation |

## Sign-Off

| Role | Name | Approval | Date |
|------|------|----------|------|
| ML Engineering Lead | | [ ] Approved / [ ] Blocked | |
| Data Protection Officer | | [ ] Approved / [ ] Blocked | |
| Information Security Officer | | [ ] Approved / [ ] Blocked | |
| Product Owner | | [ ] Approved / [ ] Blocked | |
| Legal Counsel | | [ ] Approved / [ ] Blocked (high-risk only) | |

## Key Legal References

- **GDPR Articles 5, 6, 9** — Data processing principles, lawful basis, special categories
- **GDPR Article 22** — Automated individual decision-making safeguards
- **GDPR Article 25** — Data protection by design and by default
- **GDPR Article 35** — Data Protection Impact Assessment
- **EU AI Act Articles 9-15** — High-risk AI system requirements
- **EU AI Act Article 52** — Transparency obligations for certain AI systems
- **EDPB Guidelines on Automated Decision-Making (WP 251 rev.01)** — Art. 22 interpretation
- **ISO/IEC 42001:2023** — AI management system standard
