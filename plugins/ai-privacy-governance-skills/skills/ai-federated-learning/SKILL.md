---
name: ai-federated-learning
description: >-
  Implements federated learning architecture patterns for GDPR compliance.
  Covers secure aggregation protocols, differential privacy integration,
  communication protocols, and privacy-by-design distributed ML training.
  Keywords: federated learning, distributed training, secure aggregation,
  differential privacy, privacy-preserving ML.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "federated-learning, secure-aggregation, differential-privacy, distributed-ml, privacy-preserving, gdpr"
---

# Federated Learning for GDPR Compliance

## Overview

Federated learning (FL) is a distributed machine learning approach that trains models across multiple data holders without centralising personal data. Instead of collecting training data into a central repository, federated learning sends the model to the data, computes local updates on each participant's device or server, and aggregates only model updates (gradients or weights) at a central coordinator. This architecture directly addresses GDPR data minimisation (Art. 5(1)(c)) and data protection by design (Art. 25) principles by eliminating the need to transfer and centralise personal data for AI training. However, federated learning is not a privacy silver bullet — it introduces its own privacy risks that must be managed through complementary techniques.

## Federated Learning Architecture Patterns

### Pattern 1: Cross-Device Federated Learning

**Use case**: Training on data from millions of user devices (smartphones, tablets, IoT).

| Component | Description |
|-----------|-------------|
| Participants | End-user devices (smartphones, tablets, wearables) |
| Scale | Thousands to millions of participants |
| Data | Small per-device, large aggregate (e.g., keyboard predictions, health metrics) |
| Coordination | Central server selects participants per round, distributes model, aggregates updates |
| Communication | Compressed gradient updates over mobile networks |
| Privacy risk | Individual gradient updates may leak information about device data |

**GDPR Analysis**:
- Data minimisation: personal data never leaves the device — strong compliance
- Controller role: platform operator is controller; device owners are not processors
- Lawful basis: consent or legitimate interest for on-device processing
- International transfers: no personal data transfer if aggregation is privacy-preserving
- Right to erasure: device can be excluded from future rounds; model unlearning may be needed

### Pattern 2: Cross-Silo Federated Learning

**Use case**: Training across organisational boundaries (hospitals, banks, subsidiaries).

| Component | Description |
|-----------|-------------|
| Participants | Organisational data silos (hospitals, branches, partner companies) |
| Scale | 2 to 100 participants |
| Data | Large per-silo, structured (e.g., medical records, financial transactions) |
| Coordination | Trusted aggregator or peer-to-peer protocol |
| Communication | Model updates over secure channels between organisations |
| Privacy risk | Gradient updates may reveal institutional data patterns |

**GDPR Analysis**:
- Joint controller determination: participants and aggregator may be joint controllers (Art. 26) — requires joint controller agreement
- Data processing agreements: if aggregator is a processor, Art. 28 DPA required
- Data minimisation: personal data stays within each silo — strong compliance
- International transfers: if silos are in different jurisdictions, gradient transfer legality depends on privacy guarantees
- Lawful basis: each silo needs independent lawful basis for local training; aggregation needs separate basis

### Pattern 3: Vertical Federated Learning

**Use case**: Different organisations hold different features for the same individuals.

| Component | Description |
|-----------|-------------|
| Participants | Organisations with complementary data (bank + retailer sharing customer features) |
| Scale | 2 to 10 participants |
| Data | Different features for overlapping individuals |
| Coordination | Secure multi-party computation for feature combination |
| Communication | Encrypted intermediate representations |
| Privacy risk | Feature linkage may reveal individual attributes across parties |

**GDPR Analysis**:
- Joint controller: participants are likely joint controllers — each processes personal data for a common purpose
- Purpose limitation: combined training purpose must be compatible with each party's original collection purpose
- Data subject notification: data subjects must be informed about cross-organisation federated training
- Consent: may be required for combining data across organisations

## Secure Aggregation Protocols

### Protocol 1: Masking-Based Secure Aggregation

Participants mask their local updates with pairwise random masks that cancel out upon aggregation. The aggregator receives the sum without seeing individual updates.

| Property | Value |
|----------|-------|
| Privacy guarantee | Individual updates not visible to aggregator or other participants |
| Computational cost | O(n^2) pairwise key agreement, O(n) masking per round |
| Communication cost | 2x baseline (masks + masked updates) |
| Dropout tolerance | Handles participant dropout if sufficient participants remain |
| Collusion resistance | Secure against aggregator + up to t-1 participant collusion |

### Protocol 2: Homomorphic Encryption Aggregation

Participants encrypt their updates with a homomorphic encryption scheme. The aggregator computes the sum on encrypted data without decryption.

| Property | Value |
|----------|-------|
| Privacy guarantee | Computationally secure — updates encrypted throughout |
| Computational cost | 100-1000x overhead for encryption/decryption operations |
| Communication cost | 2-10x baseline (ciphertext expansion) |
| Dropout tolerance | Excellent — encrypted updates can be summed independently |
| Collusion resistance | Secure against aggregator (does not hold decryption key) |

### Protocol 3: Trusted Execution Environment (TEE)

Aggregation occurs within a hardware-protected enclave (Intel SGX, ARM TrustZone). Participants send updates to the TEE, which performs aggregation in isolated memory.

| Property | Value |
|----------|-------|
| Privacy guarantee | Hardware-based isolation — aggregator cannot inspect updates |
| Computational cost | Near-native (small overhead for enclave transitions) |
| Communication cost | Baseline (no encryption expansion for enclave-to-enclave) |
| Dropout tolerance | Excellent |
| Collusion resistance | Depends on hardware trust model; vulnerable to side-channel attacks |

## Differential Privacy Integration

### Local Differential Privacy (LDP)

Each participant adds noise to their gradient update before sending to the aggregator:

- **Mechanism**: Gaussian noise calibrated to sensitivity and privacy budget (epsilon, delta)
- **Guarantee**: Individual update is differentially private — aggregator cannot infer specific data points
- **Trade-off**: Higher noise reduces model accuracy; need more participants to compensate
- **Recommended epsilon**: 1-10 per round, with privacy accounting across rounds

### Central Differential Privacy (CDP)

The aggregator adds noise to the aggregated update before applying to the global model:

- **Mechanism**: Gaussian noise added to the sum of clipped gradients
- **Guarantee**: Global model is differentially private with respect to any single participant's data
- **Trade-off**: Less noise needed than LDP for same accuracy (noise averages out); requires trusted aggregator
- **Recommended epsilon**: 1-8 total privacy budget

### Privacy Budget Management

| Parameter | Description | Guidance |
|-----------|-------------|----------|
| Epsilon (ε) | Privacy loss parameter — lower is more private | ε ≤ 1: strong privacy; ε ≤ 8: moderate; ε > 10: weak |
| Delta (δ) | Probability of privacy failure | δ < 1/N where N is dataset size |
| Rounds (T) | Number of federated training rounds | Privacy degrades with rounds — use composition theorems |
| Clip norm (C) | Maximum gradient norm per participant | Balance between privacy (lower C) and convergence (higher C) |
| Noise multiplier (σ) | Ratio of noise to sensitivity | Determined by ε, δ, C, and composition method |

## GDPR Compliance Assessment for Federated Learning

### Data Protection by Design (Art. 25) Alignment

| GDPR Principle | FL Implementation | Compliance Status |
|----------------|-------------------|-------------------|
| Data minimisation (Art. 5(1)(c)) | Personal data stays local — only model updates transmitted | Strong compliance |
| Purpose limitation (Art. 5(1)(b)) | Local processing for specified training purpose | Requires per-participant purpose documentation |
| Storage limitation (Art. 5(1)(e)) | No central training data repository — data retained locally per participant's policy | Compliance depends on participant retention |
| Integrity and confidentiality (Art. 5(1)(f)) | Secure aggregation protects update confidentiality | Strong with SA + DP |
| Accuracy (Art. 5(1)(d)) | Model accuracy may differ from centralised training | Monitor and document accuracy trade-offs |

### Remaining GDPR Challenges

1. **Gradient leakage**: Model updates can leak training data even without transmitting raw data — secure aggregation and DP mitigate but do not eliminate
2. **Model memorization**: The aggregated model may still memorize individual records — privacy auditing required post-training
3. **Right to erasure**: Removing a participant's contribution from the trained model is challenging — machine unlearning or retraining required
4. **Controller/processor determination**: Complex multi-party FL architectures require clear role delineation
5. **Lawful basis**: Each participant needs independent lawful basis; the aggregator needs basis for processing updates
6. **Transparency**: Data subjects must be informed about federated learning participation

## Implementation Considerations

### Communication Efficiency

| Technique | Description | Privacy Impact |
|-----------|-------------|---------------|
| Gradient compression | Quantise or sparsify gradients before transmission | May interact with DP noise — careful calibration needed |
| Federated averaging (FedAvg) | Multiple local SGD steps before communication | Reduces communication rounds; may increase per-round privacy cost |
| Gradient selection | Send only top-k gradient components | Leaks which components are most significant — privacy concern |

### Participant Selection

| Strategy | Description | Privacy Consideration |
|----------|-------------|----------------------|
| Random selection | Uniformly random participant sampling per round | Fair representation; privacy amplification through subsampling |
| Availability-based | Select participants with sufficient resources | May bias toward certain participant profiles |
| Contribution-based | Select participants whose data improves model most | Reveals information about data distribution — privacy risk |

## Enforcement Relevance

While no enforcement action has specifically addressed federated learning, the technology is directly relevant to:

- **CNIL AI recommendations (2024)**: Identified federated learning as a recommended privacy-enhancing technology for AI training
- **EDPB Guidelines 04/2025**: Mentioned distributed training as a data minimisation measure for AI systems
- **Garante v. OpenAI (2023)**: Centralised data collection was a key compliance issue — federated alternatives could have mitigated
- **AI Act Art. 10**: Data governance for training data — FL enables data governance while maintaining data locality

## Integration Points

- **ai-dpia**: FL architecture reduces data centralisation risk in DPIA assessment
- **ai-training-lawfulness**: FL may simplify lawful basis by keeping data local
- **ai-model-privacy-audit**: Federated models require distributed privacy auditing
- **ai-privacy-inference**: FL complements confidential computing for inference privacy
- **ai-data-retention**: Data locality in FL simplifies retention compliance
