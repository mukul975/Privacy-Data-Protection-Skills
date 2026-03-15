---
name: ai-data-retention
description: >-
  Manages AI model retention and machine unlearning requirements. Covers
  training data deletion verification, model versioning for compliance,
  machine unlearning techniques (SISA, gradient-based), and retraining
  triggers. Keywords: AI retention, machine unlearning, model versioning,
  training data deletion, retraining, storage limitation.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "ai-retention, machine-unlearning, model-versioning, training-data-deletion, retraining, storage-limitation"
---

# AI Model Retention and Unlearning

## Overview

GDPR Art. 5(1)(e) storage limitation requires that personal data be kept no longer than necessary for the processing purpose. For AI systems, this creates complex retention challenges: training data used to build a model may no longer be needed once training is complete, but the model itself encodes information about the training data. Machine unlearning — the process of removing the influence of specific data from a trained model — is an emerging field that addresses the gap between deleting training data and eliminating its influence from model parameters. This skill provides retention policies, deletion verification methods, and machine unlearning techniques for AI compliance.

## AI Data Retention Categories

| Data Category | Description | Retention Consideration |
|---------------|-------------|----------------------|
| Raw training data | Original personal data used for model training | Delete after training unless retraining justifies retention |
| Processed training data | Cleaned, augmented, feature-engineered data | Same as raw — delete when training purpose exhausted |
| Validation/test data | Data used for model evaluation | Retain for model audit and comparison; pseudonymise |
| Model weights/parameters | Trained model artefacts encoding training data information | Retain while model is deployed; delete on decommission |
| Inference logs | Inputs and outputs of model predictions | Retention based on purpose (audit, debugging, rights exercise) |
| Model metadata | Training configuration, hyperparameters, provenance | Retain for compliance documentation; low privacy risk |
| Embedding vectors | Dense representations derived from personal data | May contain personal data — apply retention policy |

## Retention Policy Framework

### Training Data Retention Decision Tree

```
Training data category identified
│
├─ Is the data still needed for model retraining?
│  ├─ YES → Retain with documented justification and review date
│  └─ NO → Continue
│
├─ Is the data needed for model validation or audit?
│  ├─ YES → Retain in pseudonymised form with access controls
│  └─ NO → Continue
│
├─ Is the data needed for data subject rights exercise?
│  ├─ YES → Retain for rights exercise period, then delete
│  └─ NO → Continue
│
├─ Is there a legal obligation to retain?
│  ├─ YES → Retain per legal requirement
│  └─ NO → DELETE the training data
│
└─ After deletion: assess model for residual data encoding
```

### Model Lifecycle Retention

| Phase | Retention Rule |
|-------|---------------|
| Development | Training data retained during active development |
| Deployment | Training data deleted unless retraining is planned within defined period |
| Operation | Inference logs retained per purpose (30 days debug, 1 year audit) |
| Retraining | New training data collected; old data deleted post-training |
| Decommission | All model artefacts, training data, and logs deleted; retain only compliance documentation |

## Machine Unlearning Techniques

### Exact Unlearning

**Full retraining**: Retrain the model from scratch on the dataset minus deleted records.

| Property | Value |
|----------|-------|
| Guarantee | Complete — model has no knowledge of deleted data |
| Cost | Very high — full training cost for each deletion request |
| Feasibility | Impractical for large models or frequent deletion requests |
| When to use | Small models, infrequent requests, high-sensitivity data |

### SISA (Sharded, Isolated, Sliced, Aggregated) Training

Train model on sharded data partitions. To unlearn, retrain only the affected shard.

| Property | Value |
|----------|-------|
| Guarantee | Exact within the affected shard |
| Cost | 1/k of full retraining (k = number of shards) |
| Feasibility | Requires SISA architecture from the start |
| Trade-off | Model accuracy may decrease with fewer shards contributing |

### Approximate Unlearning

#### Gradient-Based Unlearning
Apply gradient ascent on the data to be forgotten, then fine-tune on remaining data.

| Property | Value |
|----------|-------|
| Guarantee | Approximate — statistically similar to retrained model |
| Cost | Low — few gradient steps |
| Feasibility | Works for most differentiable models |
| Verification | Requires membership inference testing to verify |

#### Influence Function-Based Unlearning
Use influence functions to estimate the effect of removing data and adjust model accordingly.

| Property | Value |
|----------|-------|
| Guarantee | Approximate — first-order approximation |
| Cost | Medium — requires Hessian computation |
| Feasibility | Best for smaller models or linear models |

### Unlearning Verification

After applying unlearning, verify effectiveness:

1. **Membership inference test**: Run MI attack on unlearned records — should classify as non-members
2. **Output comparison**: Compare model outputs with and without the unlearned data
3. **Canary test**: If canary records were included, verify they are no longer extractable
4. **Statistical test**: Compare model to one retrained from scratch on the same data minus deleted records

## Model Versioning for Compliance

### Version Control Requirements

| Element | Documentation |
|---------|---------------|
| Model version ID | Unique identifier (e.g., model-v2.3.1-20260314) |
| Training data snapshot | Hash of training dataset used for this version |
| Training date | When training was executed |
| Data deletions applied | Which data subject deletions are reflected in this version |
| Unlearning applied | Any approximate unlearning applied since last full retraining |
| Privacy properties | DP epsilon, MI test results for this version |
| Deployment dates | When deployed and when retired |

### Retraining Triggers

| Trigger | Action |
|---------|--------|
| Accumulated deletion requests exceed threshold | Full retraining on updated dataset |
| Scheduled periodic retraining | Incorporate all pending deletions |
| Privacy audit reveals unacceptable leakage | Retrain with enhanced privacy measures |
| Model performance degradation | Retrain with current data (post-deletions) |
| Regulatory change | Assess if retraining needed for compliance |

## Enforcement Relevance

- **EDPB Guidelines 04/2025**: Training data retention must be justified; deletion of training data does not automatically eliminate GDPR obligations for the model if it encodes personal data.
- **Garante v. OpenAI (2023)**: Required mechanism for data deletion from training data; acknowledged technical challenges but expected good faith effort.
- **EDPB ChatGPT Taskforce (2024)**: Controllers must demonstrate capability to address erasure requests affecting training data.

## Integration Points

- **ai-data-subject-rights**: Erasure rights implementation requires unlearning
- **ai-dpia**: Retention and deletion capability assessed in DPIA
- **ai-model-privacy-audit**: Audit verifies deletion effectiveness
- **ai-training-lawfulness**: Retention justification part of lawful basis assessment
