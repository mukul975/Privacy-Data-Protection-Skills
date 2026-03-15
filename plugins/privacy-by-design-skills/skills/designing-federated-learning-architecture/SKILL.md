---
name: designing-federated-learning-architecture
description: >-
  Architecture guide for GDPR-compliant federated learning systems. Covers horizontal
  and vertical FL, aggregation strategies (FedAvg, FedProx), communication efficiency,
  secure aggregation, and differential privacy integration. Includes privacy guarantees
  analysis and deployment patterns for cross-organizational ML without data sharing.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-by-design
  tags: "federated-learning, fedavg, secure-aggregation, distributed-ml, privacy-preserving-ml"
---

# Designing Federated Learning Architecture

## Overview

Federated Learning (FL) enables multiple parties to collaboratively train a machine learning model without sharing their raw data. Each participant trains a local model on their own data and shares only model updates (gradients or parameters) with a central aggregator. The aggregated model benefits from all participants' data without any single party accessing another's dataset.

FL directly supports GDPR Article 5(1)(c) data minimization (only model updates are shared, not personal data), Article 25(1) data protection by design (privacy is built into the architecture), and can reduce the need for cross-border data transfers under Chapter V (data stays in its jurisdiction of origin).

## FL Architectures

### Horizontal Federated Learning

Participants share the same feature space but have different data samples. Each participant has a complete record for their subjects but covers different subjects.

```
┌──────────────────────────────────────────────────────────────┐
│                    Central Aggregator                          │
│               (aggregates model updates only)                 │
│                                                                │
│  Global Model = Aggregate(Local_1, Local_2, ..., Local_K)    │
└─────────────┬──────────────┬──────────────┬──────────────────┘
              │              │              │
    ┌─────────▼────┐ ┌──────▼──────┐ ┌────▼──────────┐
    │ Hospital A   │ │ Hospital B  │ │ Hospital C    │
    │ 5,000 pts    │ │ 8,000 pts   │ │ 3,000 pts     │
    │ Same features│ │ Same features│ │ Same features │
    │ Train locally│ │ Train locally│ │ Train locally │
    └──────────────┘ └─────────────┘ └───────────────┘
```

**Use case:** Multiple hospitals training a diagnostic model; each hospital has complete patient records but different patients.

### Vertical Federated Learning

Participants share the same data subjects but have different features. Features are distributed across participants.

```
┌──────────────────────────────────────────────────────────────┐
│                    Coordination Server                         │
│         (aligns features without exposing raw data)           │
└─────────────┬──────────────┬──────────────┬──────────────────┘
              │              │              │
    ┌─────────▼────┐ ┌──────▼──────┐ ┌────▼──────────┐
    │ Bank         │ │ Insurer     │ │ Retailer      │
    │ Financial    │ │ Claims      │ │ Purchase      │
    │ features     │ │ features    │ │ features      │
    │ Same users   │ │ Same users  │ │ Same users    │
    └──────────────┘ └─────────────┘ └───────────────┘
```

**Use case:** Credit scoring where a bank has financial data, an insurer has claims history, and a retailer has purchase behavior — all for overlapping customers.

## Aggregation Strategies

### FedAvg (Federated Averaging)

The foundational FL algorithm (McMahan et al., 2017). Each participant trains for multiple local epochs, then the aggregator averages the model weights proportional to each participant's dataset size.

```
For each communication round t:
  1. Server sends global model w_t to selected participants
  2. Each participant k trains locally for E epochs on their data:
     w_k = LocalSGD(w_t, data_k, E epochs, learning_rate η)
  3. Server aggregates:
     w_{t+1} = Σ (n_k / n) * w_k
     where n_k = participant k's sample count, n = total samples
```

| Parameter | Recommended Range | Impact |
|-----------|------------------|--------|
| Local epochs (E) | 1-5 | More epochs = less communication, but higher divergence risk |
| Participation rate | 10-100% per round | Higher = better convergence, more communication |
| Learning rate (η) | 0.01-0.1 | Standard SGD tuning applies |
| Communication rounds | 50-500 | Depends on data heterogeneity and model complexity |

### FedProx (Federated Proximal)

Extension of FedAvg for heterogeneous settings. Adds a proximal term to the local objective to limit how far local models drift from the global model. Suitable when participants have non-IID (non-independently and identically distributed) data.

```
Local objective for participant k:
  minimize F_k(w) + (μ/2) * ||w - w_t||^2

  where μ controls the strength of the proximal regularization
```

| Scenario | FedAvg Performance | FedProx Performance | Recommendation |
|----------|-------------------|--------------------|--------------:|
| IID data across participants | Good | Good | FedAvg (simpler) |
| Mild non-IID (label skew) | Moderate | Good | FedProx (μ=0.01) |
| Severe non-IID (feature shift) | Poor | Moderate | FedProx (μ=0.1) + larger participation |
| Participants with varying compute | Unstable | Stable | FedProx (handles partial work) |

## Privacy Guarantees

### Threat Model

| Threat | Description | Mitigation |
|--------|-------------|------------|
| Gradient inversion | Adversary reconstructs training data from shared gradients | Secure aggregation + differential privacy |
| Membership inference | Adversary determines if a specific record was in training data | Differential privacy |
| Model inversion | Adversary recovers sensitive features from the trained model | Differential privacy + access control on model |
| Free-rider attack | Participant contributes noise instead of genuine updates | Contribution verification (FoolsGold, RFFL) |
| Poisoning attack | Malicious participant corrupts the global model | Byzantine-robust aggregation (Krum, trimmed mean) |

### Secure Aggregation

Secure aggregation ensures the server sees only the sum of all participants' updates, not individual updates. Implemented using:

1. **Pairwise masking** (Bonawitz et al., 2017) — Each pair of participants generates a shared random mask. Masks cancel out in the sum, but individual updates remain hidden.
2. **Threshold secret sharing** — Each participant secret-shares their update; the server reconstructs only the aggregate.
3. **Homomorphic encryption** — Participants encrypt updates; server aggregates ciphertexts.

### Differential Privacy in FL

Adding calibrated noise to model updates before sharing provides a formal privacy guarantee:

```
DP-FedAvg:
  1. Each participant clips gradients: ||g_k|| ≤ C (sensitivity bounding)
  2. Each participant adds Gaussian noise: g_k' = g_k + N(0, σ²·C²·I)
  3. Server aggregates noised updates: g_agg = (1/K) Σ g_k'
  4. Privacy accounting: track cumulative (ε, δ) via Rényi DP composition
```

**Privacy budget for Prism Data Systems AG FL deployment:**

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Clipping norm (C) | 1.0 | Standard for gradient clipping in DP-SGD |
| Noise multiplier (σ) | 1.1 | Provides (ε=3, δ=1e-5) per training run with 500 rounds |
| Target epsilon (ε) | 3.0 | Moderate privacy for non-special-category data |
| Target delta (δ) | 1e-5 | Standard for n ≈ 316,000 total records |
| Composition method | Rényi DP | Tighter composition bounds than basic composition |

## Communication Efficiency

| Technique | Compression Ratio | Accuracy Impact | Description |
|-----------|------------------|-----------------|-------------|
| Gradient quantization | 8-32x | Minimal | Reduce gradient precision from 32-bit to 8-bit or lower |
| Top-k sparsification | 10-100x | Moderate | Transmit only the k largest gradient components |
| Federated dropout | 2-10x | Minimal | Each participant trains a random submodel |
| Gradient compression (SignSGD) | 32x | Moderate | Transmit only the sign of each gradient component |
| Model distillation | Variable | Moderate | Participants share soft predictions instead of gradients |

## Implementation Workflow

1. **Define the ML task** — Specify the model architecture, training objective, and evaluation metrics.

2. **Assess data distribution** — Evaluate the degree of non-IID across participants. This determines the aggregation strategy (FedAvg for IID, FedProx for non-IID).

3. **Select privacy mechanisms** — Choose secure aggregation for gradient confidentiality and differential privacy for formal guarantees. Set epsilon budget.

4. **Configure communication** — Select gradient compression technique based on bandwidth constraints. Set the communication round budget.

5. **Implement local training** — Deploy the local training pipeline at each participant. Implement gradient clipping and noise injection for DP.

6. **Deploy aggregation server** — Deploy the central aggregator with secure aggregation protocol. Implement Byzantine-robust aggregation if untrusted participants exist.

7. **Monitor and evaluate** — Track model convergence, per-participant contribution quality, privacy budget consumption, and communication overhead.

## Key Regulatory References

- GDPR Article 5(1)(c) — Data minimization (only model updates shared)
- GDPR Article 25(1) — Data protection by design
- GDPR Article 26 — Joint controller arrangements (FL consortium governance)
- GDPR Chapter V — Cross-border transfers (FL reduces transfer need)
- GDPR Article 35 — DPIA for FL involving special category data
- EDPB Guidelines 4/2019 on Article 25 Data Protection by Design and by Default
