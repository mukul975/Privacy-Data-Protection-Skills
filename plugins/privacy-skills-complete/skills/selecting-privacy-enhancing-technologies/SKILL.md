---
name: selecting-privacy-enhancing-technologies
description: >-
  Comprehensive PET selection guide covering differential privacy, homomorphic
  encryption, secure multi-party computation, federated learning, zero-knowledge
  proofs, and trusted execution environments. Includes use-case matching matrix,
  performance comparison, and GDPR alignment assessment for each technology.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-by-design
  tags: "pet-selection, homomorphic-encryption, federated-learning, zero-knowledge-proofs, secure-computation"
---

# Selecting Privacy-Enhancing Technologies

## Overview

Privacy-Enhancing Technologies (PETs) are technical measures that protect personal data during collection, processing, storage, and sharing. The GDPR does not prescribe specific technologies but requires "appropriate technical measures" (Article 25(1), Article 32(1)) to implement data protection principles. The European Commission's February 2025 communication on PETs and the ENISA 2023 report on engineering privacy by design with PETs provide regulatory context for PET adoption.

Selecting the right PET depends on the processing scenario, data sensitivity, computational requirements, and the specific privacy property needed (confidentiality, anonymity, unlinkability, or transparency).

## PET Taxonomy

### 1. Differential Privacy (DP)

**Privacy property:** Statistical indistinguishability — the output of an analysis is approximately the same whether or not any individual's data is included.

| Characteristic | Detail |
|---------------|--------|
| Approach | Add calibrated noise to query results or model gradients |
| Privacy guarantee | Mathematically provable (epsilon, delta) bounds |
| Data utility | Configurable via epsilon; lower epsilon = more privacy, less utility |
| Performance overhead | Minimal for query-time noise; moderate for DP-SGD training |
| Maturity | Production-ready (Apple, Google, US Census Bureau) |
| GDPR relevance | Supports Recital 26 anonymization when epsilon is sufficiently small; Art. 25(1) by design measure |

**Best for:** Statistical analytics, aggregate reporting, ML model training on sensitive data.

**Libraries:** Google DP Library, OpenDP, IBM diffprivlib, PyDP.

### 2. Homomorphic Encryption (HE)

**Privacy property:** Computation on encrypted data — results are decrypted only by the data owner.

| Characteristic | Detail |
|---------------|--------|
| Approach | Encrypt data such that mathematical operations on ciphertext produce valid results when decrypted |
| Privacy guarantee | Cryptographic (lattice-based hardness assumptions) |
| Data utility | Exact results (no noise added) |
| Performance overhead | High: 1,000x-1,000,000x slower than plaintext, depending on scheme and operation |
| Maturity | Emerging for production; active research on performance optimization |
| GDPR relevance | Art. 32(1)(a) encryption as security measure; enables processing without exposing plaintext to processor |

**Schemes:**
- **BFV (Brakerski/Fan-Vercauteren):** Integer arithmetic, exact. Suitable for counting, matching.
- **BGV (Brakerski-Gentry-Vaikuntanathan):** Integer arithmetic with modulus switching. Efficient for deep circuits.
- **CKKS (Cheon-Kim-Kim-Song):** Approximate arithmetic on real/complex numbers. Suitable for ML inference.
- **TFHE (Torus FHE):** Fast bootstrapping, gate-by-gate evaluation. Suitable for boolean circuits.

**Libraries:** Microsoft SEAL, IBM HELib, Google FHE (Fully Homomorphic Encryption transpiler), TFHE-rs, OpenFHE.

### 3. Secure Multi-Party Computation (SMPC)

**Privacy property:** Joint computation without revealing individual inputs — each party learns only the final result.

| Characteristic | Detail |
|---------------|--------|
| Approach | Secret sharing, garbled circuits, or oblivious transfer protocols |
| Privacy guarantee | Information-theoretic (for secret sharing) or computational (for garbled circuits) |
| Data utility | Exact results |
| Performance overhead | Moderate to high; depends on circuit complexity and number of parties |
| Maturity | Production deployments in financial services, healthcare consortia |
| GDPR relevance | Enables joint controllership (Art. 26) analytics without data sharing; supports data minimization (Art. 5(1)(c)) |

**Frameworks:** MP-SPDZ, CrypTen (Meta), MOTION, ABY/ABY3, Sharemind.

### 4. Federated Learning (FL)

**Privacy property:** Model training without centralizing data — raw data never leaves the data owner's environment.

| Characteristic | Detail |
|---------------|--------|
| Approach | Distribute model training to data owners; aggregate only model updates (gradients) |
| Privacy guarantee | Data locality (raw data stays on device); strengthened with secure aggregation and DP |
| Data utility | Depends on data distribution across participants (IID vs non-IID) |
| Performance overhead | Communication overhead for gradient exchange; multiple training rounds |
| Maturity | Production at Google (Gboard), Apple (Siri), hospitals (NVIDIA FLARE) |
| GDPR relevance | Supports Art. 5(1)(c) minimization; reduces cross-border transfer requirements (Chapter V) |

**Frameworks:** TensorFlow Federated, PySyft (OpenMined), NVIDIA FLARE, Flower, FedML.

### 5. Zero-Knowledge Proofs (ZKP)

**Privacy property:** Prove a statement is true without revealing the underlying data.

| Characteristic | Detail |
|---------------|--------|
| Approach | Prover demonstrates knowledge of a secret (e.g., age ≥ 18) without revealing the secret (date of birth) |
| Privacy guarantee | Soundness (false statements cannot be proven) and zero-knowledge (verifier learns nothing beyond the statement's truth) |
| Data utility | Binary verification (proof valid/invalid); no data disclosed |
| Performance overhead | Proof generation: moderate to high; proof verification: fast |
| Maturity | Production in blockchain identity; emerging in enterprise identity verification |
| GDPR relevance | Ultimate data minimization — prove compliance without disclosing data; supports Art. 5(1)(c), Art. 25 |

**Systems:** zk-SNARKs (Groth16, PLONK), zk-STARKs, Bulletproofs.

### 6. Trusted Execution Environments (TEE)

**Privacy property:** Isolated computation — data is processed inside a hardware-protected enclave that even the system administrator cannot access.

| Characteristic | Detail |
|---------------|--------|
| Approach | Hardware-enforced isolation using secure enclaves (Intel SGX, AMD SEV, ARM TrustZone, AWS Nitro) |
| Privacy guarantee | Hardware-based attestation and memory encryption |
| Data utility | Full computation capability inside enclave |
| Performance overhead | Low to moderate; limited enclave memory may require data streaming |
| Maturity | Production: Azure Confidential Computing, AWS Nitro Enclaves, Google Confidential VMs |
| GDPR relevance | Art. 32(1)(a) encryption in processing; Art. 28 processor guarantees; protects against insider threats |

## Use-Case Matching Matrix

| Use Case | DP | HE | SMPC | FL | ZKP | TEE | Recommended Primary |
|----------|----|----|------|----|----|-----|-------------------|
| Aggregate analytics on customer data | 5 | 2 | 3 | 2 | 1 | 3 | Differential Privacy |
| ML model training on distributed hospital data | 3 | 1 | 2 | 5 | 1 | 3 | Federated Learning |
| Credit scoring without sharing financial records | 2 | 3 | 5 | 2 | 2 | 3 | Secure MPC |
| Age verification without revealing date of birth | 1 | 1 | 1 | 1 | 5 | 2 | Zero-Knowledge Proofs |
| Processing encrypted customer data in third-party cloud | 2 | 5 | 2 | 1 | 1 | 4 | Homomorphic Encryption |
| Anti-money laundering across banks | 2 | 2 | 5 | 3 | 2 | 3 | Secure MPC |
| Private genomic analysis | 3 | 4 | 3 | 3 | 1 | 4 | HE + TEE combination |
| Confidential inference on cloud-hosted ML models | 2 | 4 | 2 | 1 | 1 | 5 | Trusted Execution Environment |
| Privacy-preserving surveys and polls | 5 | 1 | 3 | 1 | 2 | 1 | Differential Privacy |
| Secure keyword search on encrypted database | 1 | 4 | 1 | 1 | 1 | 4 | Homomorphic Encryption |

*Scores: 1 = poor fit, 5 = excellent fit*

## PET Selection Decision Framework

### Step 1: Define Privacy Requirements

- What data protection principle is primary? (minimization, confidentiality, anonymization, unlinkability)
- Is the goal to protect data in transit, at rest, or during processing?
- Is the adversary model honest-but-curious or malicious?
- Are there cross-organizational boundaries (multiple controllers/processors)?

### Step 2: Assess Constraints

- What is the acceptable performance overhead? (real-time vs batch)
- What is the computational budget? (HE requires significantly more resources)
- How many parties are involved? (SMPC scales with party count)
- Is there a hardware trust anchor available? (TEE requires specific hardware)
- What is the team's cryptographic engineering expertise?

### Step 3: Evaluate Combinations

Many production deployments combine PETs for defense in depth:

| Combination | Benefit |
|------------|---------|
| FL + DP | Federated learning with differentially private gradient updates prevents gradient inversion attacks |
| FL + Secure Aggregation | Aggregation server never sees individual gradients |
| HE + TEE | Process encrypted data inside an enclave for double protection |
| SMPC + DP | Add noise to SMPC outputs for formal anonymization guarantee |
| ZKP + TEE | Prove computation was performed correctly inside an enclave without revealing inputs |

### Step 4: GDPR Alignment Verification

- Does the selected PET satisfy Article 25(1) data protection by design?
- Does it implement a specific Article 32(1) security measure?
- Does it support the data minimization principle under Article 5(1)(c)?
- If anonymization is claimed, does it meet Recital 26 standards against singling out, linkability, and inference?
- Is the PET's privacy guarantee documented sufficiently for DPIA (Article 35)?

## Key Regulatory References

- GDPR Article 25(1) — Data protection by design
- GDPR Article 32(1)(a) — Encryption and pseudonymisation as security measures
- GDPR Article 5(1)(c) — Data minimization principle
- GDPR Recital 26 — Anonymous information
- GDPR Recital 78 — Technical measures for data protection
- ENISA Report: Data Protection Engineering (2022)
- European Commission Communication on PETs (February 2025)
- EDPB Guidelines 4/2019 on Article 25 Data Protection by Design and by Default
