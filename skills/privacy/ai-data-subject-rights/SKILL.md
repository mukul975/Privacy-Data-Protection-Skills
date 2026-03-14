---
name: ai-data-subject-rights
description: >-
  Implements data subject rights mechanisms for AI systems including right to
  explanation of AI decisions, contestation procedures, human review, model
  output correction, and training data access. Covers GDPR Arts. 15-22 and
  AI Act Art. 86. Keywords: data subject rights, AI explanation, contestation,
  human review, training data access, model correction.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "data-subject-rights, ai-explanation, contestation, human-review, training-data-access, model-correction"
---

# Data Subject Rights for AI Systems

## Overview

AI systems create unique challenges for data subject rights exercise. Traditional rights mechanisms designed for structured databases do not map directly to ML model architectures where personal data is encoded in model weights, reproduced in model outputs, or used in opaque decision processes. This skill provides the framework for implementing each GDPR right (Arts. 15-22) and the AI Act Art. 86 right to explanation in the context of AI processing, addressing both training-time and inference-time rights.

## Rights Framework for AI

### Right of Access (Art. 15)

| AI Context | Obligation | Implementation |
|-----------|-----------|----------------|
| Training data contribution | Confirm whether data subject's data was in training set; provide copy if feasible | Training data catalogue indexed by data subject identifier; membership query |
| AI inference inputs | Provide data used as input to AI decision | Log inference inputs with data subject linkage |
| AI inference outputs | Provide AI decision/score/classification affecting data subject | Decision logging with data subject ID |
| Logic explanation | Art. 15(1)(h): meaningful information about logic of automated decisions | SHAP/LIME explanation on request or system-level explanation |
| Training data source | Art. 14(2)(f): source of data if not collected from data subject | Training data provenance documentation |

**Technical Challenges**:
- Identifying specific records in massive training datasets
- Determining if a data subject's data is in the training set without running membership inference
- Providing meaningful logic explanation for complex models

### Right to Rectification (Art. 16)

| AI Context | Obligation | Implementation |
|-----------|-----------|----------------|
| Training data correction | Correct inaccurate data in training dataset | Update training data; assess if model retraining needed |
| Model output correction | Correct inaccurate AI outputs about a data subject | Output correction mechanism; flag in decision system |
| Inference input correction | Correct data used as inference input | Update input data; re-run inference |

**Technical Challenge**: Correcting training data may require model retraining to propagate the correction. For deployed models, correction may need model update or retraining pipeline.

### Right to Erasure (Art. 17)

| AI Context | Obligation | Implementation |
|-----------|-----------|----------------|
| Training data deletion | Delete data subject's data from training dataset | Remove from training data; assess model impact |
| Model unlearning | Remove influence of deleted data from trained model | Machine unlearning technique or full retraining |
| Inference logs | Delete inference inputs and outputs linked to data subject | Purge from decision logs |
| Model outputs | Delete generated content about the data subject | Content removal mechanism |

**Technical Challenge**: True erasure from a trained model requires either verified machine unlearning or complete model retraining. The EDPB acknowledges this challenge but expects controllers to demonstrate good faith effort and use best available techniques.

### Right to Restriction (Art. 18)

| AI Context | Obligation |
|-----------|-----------|
| Contested accuracy | Restrict processing while accuracy of training data or AI output is verified |
| Unlawful processing | Restrict rather than delete if data subject requests |
| During objection assessment | Restrict while controller assesses whether legitimate grounds override |

**Implementation**: Quarantine data subject's data from training pipeline and inference pipeline during restriction period.

### Right to Data Portability (Art. 20)

| AI Context | Obligation |
|-----------|-----------|
| Training data contribution | Provide data subject's training data contribution in structured, machine-readable format |
| AI-generated profile | If AI has created a profile, provide in portable format |
| Inference history | Provide history of AI decisions affecting data subject |

### Right to Object (Art. 21)

| AI Context | Obligation |
|-----------|-----------|
| AI training objection | If training is based on legitimate interest (Art. 6(1)(f)), data subject can object |
| Profiling objection | Object to AI profiling including inference of characteristics |
| Direct marketing | Absolute right to object to AI-driven direct marketing profiling |

**Upon objection**: Controller must cease processing unless compelling legitimate grounds override. For AI training: remove data from training pipeline and assess model impact.

### Rights Relating to Automated Decisions (Art. 22)

| Right | Implementation |
|-------|---------------|
| Right not to be subject | Opt-out from solely automated AI decisions with legal/significant effects |
| Right to human intervention | Qualified human reviewer with authority to override AI |
| Right to express views | Mechanism for data subject to provide additional context |
| Right to contest | Formal contestation with independent review |
| Right to explanation | AI Act Art. 86 + GDPR Recital 71: clear explanation of AI's role in the decision |

### AI Act Art. 86 — Right to Explanation

For high-risk AI systems, affected persons have the right to:
- Clear and meaningful explanations of the role of the AI system in the decision-making procedure
- The main elements of the decision taken
- This right is without prejudice to GDPR data subject rights

## Operational Implementation

### Rights Request Triage for AI

```
Data subject rights request received
│
├─ Identify if AI processing is involved
│  ├─ Was AI used in any decision affecting the data subject?
│  ├─ Is the data subject's data in any training dataset?
│  └─ Has AI generated any content about the data subject?
│
├─ Determine applicable AI-specific rights
│  ├─ Access: training data, inference records, logic explanation
│  ├─ Rectification: training data or output correction
│  ├─ Erasure: training data deletion, model unlearning
│  ├─ Restriction: quarantine from AI pipeline
│  ├─ Objection: cease AI training on their data
│  └─ Automated decision: explanation, human review, contestation
│
├─ Route to appropriate team
│  ├─ Standard rights: data protection team
│  ├─ AI-specific: data protection + ML engineering team
│  └─ Contestation: independent review panel
│
└─ Process within Art. 12 timeframe (one month, extendable by two)
```

### Response Timeframes

| Request Type | Standard | Extended | Justification for Extension |
|-------------|----------|----------|---------------------------|
| Access (standard) | 1 month | 3 months | Complex, voluminous |
| Access (AI logic) | 1 month | 3 months | Requires technical explanation generation |
| Rectification | 1 month | 3 months | May require model retraining |
| Erasure | 1 month | 3 months | Machine unlearning complexity |
| Explanation (Art. 86) | Without undue delay | — | Time-critical for affected persons |
| Contestation | 30 days | 90 days | Requires independent review |

## Enforcement Precedents

- **Austrian DPA v. CRIF (2023)**: Violation of Art. 15(1)(h) — credit scoring system failed to provide meaningful information about automated decision logic upon access request.
- **Garante v. OpenAI (2023)**: Required mechanism for data subjects to request correction of inaccurate AI outputs and to object to AI training on their data.
- **Dutch DPA guidance (2024)**: Right to erasure includes obligation to address erasure from AI training data, even if technically challenging.
- **EDPB ChatGPT Taskforce (2024)**: Controllers must demonstrate capability to address rights requests affecting training data — technical difficulty does not exempt.

## Integration Points

- **ai-automated-decisions**: Contestation and human review mechanisms
- **ai-transparency-reqs**: Logic explanation fulfils transparency obligations
- **ai-data-retention**: Erasure rights intersect with retention and unlearning
- **ai-training-lawfulness**: Objection right applies to legitimate interest-based training
