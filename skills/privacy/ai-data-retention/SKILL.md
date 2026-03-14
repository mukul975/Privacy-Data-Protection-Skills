---
name: ai-data-retention
description: >-
  Managing data retention and deletion for AI/ML systems including training datasets,
  model weights, inference logs, and derived data. Covers GDPR storage limitation,
  right to erasure impact on trained models, and machine unlearning approaches.
  Keywords: AI data retention, model deletion, machine unlearning, storage limitation.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "ai-data-retention, machine-unlearning, storage-limitation, model-deletion, training-data"
---

# AI/ML Data Retention and Deletion

## Overview

AI systems create unique data retention challenges. Training data, model weights, inference logs, embeddings, and derived features all contain or reflect personal data, but their lifecycle and deletion requirements differ significantly from traditional database records. GDPR Article 5(1)(e) requires that personal data be kept no longer than necessary for the purposes of processing, and Article 17 grants data subjects the right to erasure. For AI systems, satisfying these requirements requires addressing whether personal data can be extracted from trained models (memorization risk), how to handle erasure requests when data is embedded in model weights, and what retention periods apply to different AI data categories. Cerebrum AI Labs must establish clear retention policies for each category of AI-related data.

## AI Data Categories and Retention

### Data Lifecycle in ML Systems

```
Raw Data → Preprocessed Data → Training Data → Model Weights → Inference Logs → Derived Insights
  │              │                    │               │               │                │
  │              │                    │               │               │                │
  ▼              ▼                    ▼               ▼               ▼                ▼
Retention    Retention           Retention      Retention       Retention         Retention
Policy A     Policy B            Policy C       Policy D        Policy E          Policy F
```

### Retention Schedule for Cerebrum AI Labs

| Data Category | Description | Retention Period | Legal Basis | Deletion Method |
|--------------|-------------|-----------------|-------------|-----------------|
| Raw training data | Original customer support transcripts, application forms | 24 months from collection | Art. 6(1)(f) legitimate interest | Secure deletion from storage |
| Preprocessed training data | Cleaned, tokenized, feature-engineered datasets | Until model retraining + 6 months | Art. 6(1)(f) legitimate interest | Secure deletion |
| Training data labels | Human-annotated labels for supervised learning | Same as preprocessed data | Art. 6(1)(f) legitimate interest | Secure deletion |
| Model weights | Trained neural network parameters | Duration of model deployment + 12 months archive | Art. 6(1)(f) legitimate interest | Model deletion or retraining without subject data |
| Model evaluation data | Test sets, validation sets, benchmark results | Same as model weights | Art. 6(1)(f) legitimate interest | Secure deletion |
| Inference logs | Individual predictions, input/output pairs | 90 days (operational) or 6 months (audit) | Art. 6(1)(f) legitimate interest | Automated purge |
| Embeddings/vectors | Vector representations of personal data | Same as source data or 12 months | Art. 6(1)(f) legitimate interest | Delete from vector database |
| Aggregated metrics | Model performance statistics (no individual data) | Indefinite | Art. 6(1)(f) legitimate interest | N/A — not personal data |
| Feature importance logs | Which features influenced predictions | 12 months | Art. 6(1)(f) legitimate interest | Secure deletion |
| Data subject consent records | Consent for AI processing | Duration of processing + statute of limitations (6 years) | Art. 7(1) demonstrating consent | Archive then delete |

## Right to Erasure and Trained Models

### The Machine Unlearning Challenge

When a data subject exercises their right to erasure under GDPR Article 17, Cerebrum AI Labs must consider whether the individual's personal data persists in:

1. **Training datasets** — Can be deleted directly
2. **Model weights** — Data is not stored explicitly but may be memorized by the model
3. **Inference logs** — Can be deleted directly
4. **Embeddings** — Can be deleted from vector databases
5. **Derived features** — May need recalculation without the subject's data

### Memorization Risk Assessment

| Model Type | Memorization Risk | Mitigation |
|-----------|-------------------|------------|
| Large language models (LLMs) | High — can reproduce training data verbatim | Differential privacy, deduplication, canary testing |
| Classification models | Low — learn decision boundaries, not individual records | Standard deletion of training data sufficient |
| Recommendation models | Medium — collaborative filtering can reveal preferences | Remove user vectors, retrain periodically |
| Embedding models | Medium — vector representations encode personal characteristics | Delete user embeddings, regenerate if needed |
| Generative models (images, text) | High — can generate content resembling specific individuals | Differential privacy, output filtering, periodic retraining |

### Erasure Response Process for Cerebrum AI Labs

| Step | Action | Timeline |
|------|--------|----------|
| 1 | Receive and validate erasure request | Day 0 |
| 2 | Search all AI data stores for subject's data | Days 1-3 |
| 3 | Delete from raw and preprocessed training datasets | Days 3-5 |
| 4 | Delete from inference logs and embeddings | Days 3-5 |
| 5 | Assess memorization risk for affected models | Days 5-10 |
| 6 | If memorization risk is low: document assessment, no model change needed | Day 10 |
| 7 | If memorization risk is high: schedule model retraining without subject's data | Within 30 days |
| 8 | Confirm deletion to data subject | Within 30 days (Art. 12(3)) |

### Machine Unlearning Approaches

| Approach | Description | Effectiveness | Cost |
|----------|-------------|---------------|------|
| Full retraining | Retrain model from scratch without the subject's data | Complete removal | Very high (GPU cost, time) |
| SISA (Sharded, Isolated, Sliced, Aggregated) training | Train on data shards; retrain only affected shard | Good — equivalent to full retraining for shard | Medium |
| Gradient-based unlearning | Apply gradient ascent on the subject's data to reverse learning | Approximate — may not fully remove influence | Low |
| Fine-tuning with forget set | Fine-tune model to reduce memorization of specific data | Approximate | Low-medium |
| Model replacement | Replace with newer model trained without the data | Complete removal | Scheduled with retraining cycle |

**Cerebrum AI Labs Policy:**
- For classification models: delete training data; schedule model retraining in next quarterly cycle
- For LLMs and generative models: delete training data; assess memorization with extraction attacks; retrain if memorization detected
- For recommendation models: delete user vectors and interactions; incremental model update

## Automated Retention Enforcement

### Retention Automation for Cerebrum AI Labs

| Data Store | Technology | Automated Retention |
|-----------|------------|-------------------|
| Training data (S3/GCS) | Object lifecycle policies | Auto-delete after 24 months |
| Preprocessed data (data lake) | Apache Iceberg time-travel expiry | Auto-expire snapshots after retention period |
| Model registry (MLflow) | Custom retention script | Archive models 12 months after decommission |
| Inference logs (Elasticsearch) | Index Lifecycle Management (ILM) | Hot: 7 days → Warm: 83 days → Delete: 90 days |
| Vector database (Pinecone/Weaviate) | TTL on vectors | Auto-expire after 12 months |
| Consent records (PostgreSQL) | pg_cron scheduled deletion | Delete 6 years after consent withdrawal |

## Key Legal References

- **GDPR Article 5(1)(e)** — Storage limitation: personal data kept no longer than necessary
- **GDPR Article 17** — Right to erasure ("right to be forgotten")
- **GDPR Article 17(3)** — Exceptions to erasure (archiving in public interest, legal claims)
- **GDPR Recital 39** — Storage periods should be limited to a strict minimum
- **EU AI Act Article 10(5)** — Training data retention for high-risk AI systems
- **EDPB Guidelines 05/2020 on Consent** — Consent records retention requirements
- **ICO Guidance on AI and Data Protection (2023)** — Practical approach to AI data retention
- **Bourtoule et al., "Machine Unlearning" (2021)** — SISA training approach for efficient unlearning
- **Cao and Yang, "Towards Making Systems Forget with Machine Unlearning" (IEEE S&P 2015)** — Foundational machine unlearning paper
