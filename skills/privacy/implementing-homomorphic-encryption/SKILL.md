---
name: implementing-homomorphic-encryption
description: >-
  Guide to implementing homomorphic encryption for privacy-preserving computation
  under GDPR. Covers scheme selection (BFV, BGV, CKKS, TFHE), Microsoft SEAL,
  IBM HELib, and Google FHE transpiler. Includes performance benchmarks, parameter
  tuning, and basic HE example code for encrypted arithmetic operations.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-by-design
  tags: "homomorphic-encryption, microsoft-seal, ckks, bfv, privacy-preserving-computation"
---

# Implementing Homomorphic Encryption

## Overview

Homomorphic encryption (HE) enables computation on encrypted data without decryption. The data owner encrypts their data, sends the ciphertext to a computing party (e.g., a cloud processor under Article 28), and the computing party performs operations on the ciphertext. The encrypted results are returned to the data owner, who decrypts them to obtain the plaintext result. At no point does the computing party see unencrypted data.

This directly supports GDPR Article 32(1)(a), which identifies encryption as an appropriate technical measure, and Article 25(1), which requires data protection by design. HE enables a controller to outsource computation to a processor while maintaining cryptographic confidentiality of personal data.

## HE Scheme Selection

### Scheme Comparison

| Scheme | Arithmetic Type | Exact/Approximate | Operations | Best For | Libraries |
|--------|---------------|-------------------|------------|----------|-----------|
| BFV | Integer (modular) | Exact | Add, Multiply (limited depth) | Counting, matching, exact integer computation | Microsoft SEAL, OpenFHE |
| BGV | Integer (modular) | Exact | Add, Multiply (with modulus switching) | Deep circuits on integers, batched operations | HELib, OpenFHE |
| CKKS | Real/Complex | Approximate | Add, Multiply, Rotation | ML inference, statistical analysis, floating-point computation | Microsoft SEAL, OpenFHE, HEAAN |
| TFHE | Boolean/Integer | Exact | Arbitrary (gate-by-gate) | Programmable bootstrapping, arbitrary functions | TFHE-rs, Concrete (Zama) |

### Decision Criteria

| Criterion | BFV/BGV | CKKS | TFHE |
|-----------|---------|------|------|
| Need exact results? | Yes | No (approximate) | Yes |
| Data type | Integers | Real numbers | Boolean/Small integers |
| Multiplicative depth | Limited (plan ahead) | Limited (plan ahead) | Unlimited (with bootstrapping) |
| SIMD batching | Yes (thousands of slots) | Yes (thousands of slots) | Limited |
| Performance | Fast for shallow circuits | Fast for ML workloads | Slow per operation, fast bootstrapping |
| Typical latency | Milliseconds (shallow) to seconds | Milliseconds to seconds | Seconds to minutes |

### Parameter Selection Guide

For BFV/CKKS with Microsoft SEAL, the key parameters are:

| Parameter | Description | Security Impact | Performance Impact |
|-----------|-------------|----------------|-------------------|
| poly_modulus_degree (N) | Degree of the polynomial ring | Higher N = more security | Higher N = slower operations, more memory |
| coeff_modulus | Product of primes defining the coefficient modulus | Determines noise budget and multiplicative depth | More primes = deeper circuits but larger ciphertexts |
| plain_modulus (BFV only) | Modulus for plaintext encoding | Must accommodate plaintext values | Larger = less noise budget available |
| scale (CKKS only) | Encoding scale factor | Determines precision of approximate results | Higher scale = more precision but faster noise growth |

**Recommended parameter sets (128-bit security):**

| Use Case | N | coeff_modulus bits | Mult Depth | Memory/Ciphertext |
|----------|---|-------------------|------------|-------------------|
| Simple addition/comparison | 4096 | [40, 40] | 1 | ~64 KB |
| Moderate computation (sum + multiply) | 8192 | [60, 40, 40, 60] | 2-3 | ~256 KB |
| ML inference (logistic regression) | 16384 | [60, 40, 40, 40, 40, 60] | 4-5 | ~1 MB |
| Deep neural network inference | 32768 | [60, 40×8, 60] | 8+ | ~4 MB |

## Architecture for GDPR-Compliant HE Processing

```
┌────────────────────────────────────────────────────────────┐
│              Data Controller (Prism Data Systems AG)        │
│  ┌──────────────────┐  ┌──────────────────────────────┐   │
│  │ Key Generator     │  │ Encrypt personal data        │   │
│  │ (sk stays here)   │  │ with public key              │   │
│  └────────┬─────────┘  └──────────┬───────────────────┘   │
│           │ pk, rlk, gk           │ ciphertext             │
└───────────┼───────────────────────┼────────────────────────┘
            │                       │
            ▼                       ▼
┌────────────────────────────────────────────────────────────┐
│              Data Processor (Cloud Service)                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Compute on ciphertext using pk, rlk, gk              │  │
│  │ (NEVER has access to sk — cannot decrypt)             │  │
│  │                                                        │  │
│  │ Operations: HE.Add, HE.Multiply, HE.Rotate           │  │
│  └──────────────────────────┬───────────────────────────┘  │
│                              │ encrypted result             │
└──────────────────────────────┼─────────────────────────────┘
                               │
                               ▼
┌────────────────────────────────────────────────────────────┐
│              Data Controller (Prism Data Systems AG)        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Decrypt result using sk                               │  │
│  │ Plaintext result = f(data) computed without exposure   │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────┘

Key:
  sk = Secret key (never leaves controller)
  pk = Public key (for encryption and computation)
  rlk = Relinearization keys (for ciphertext multiplication)
  gk = Galois keys (for ciphertext rotation/SIMD operations)
```

## Performance Considerations

### Benchmark Reference (Microsoft SEAL, BFV, N=8192, 128-bit security)

| Operation | Latency | Throughput (ops/sec) |
|-----------|---------|---------------------|
| Key generation | 50 ms | 20 |
| Encryption | 2 ms | 500 |
| Decryption | 1 ms | 1,000 |
| Ciphertext addition | 0.1 ms | 10,000 |
| Ciphertext multiplication | 5 ms | 200 |
| Relinearization | 3 ms | 333 |
| SIMD rotation | 4 ms | 250 |

### Optimization Strategies

| Strategy | Benefit | Trade-off |
|----------|---------|-----------|
| SIMD batching | Process thousands of values in parallel | Requires data to be structured as vectors |
| Circuit depth minimization | Fewer multiplications = less noise, smaller parameters | May require algorithmic redesign |
| Lazy relinearization | Skip intermediate relinearizations | Larger intermediate ciphertexts |
| Level-aware computation | Use modulus switching to control noise | Requires careful depth planning |
| Hybrid HE + plaintext | Perform non-sensitive operations in plaintext | Reduces privacy guarantee scope |

## Implementation Workflow

1. **Identify computation** — Define the exact mathematical function to compute on encrypted data. Express it as additions and multiplications (and rotations for SIMD).

2. **Select scheme** — Choose BFV for exact integer results, CKKS for approximate real-number results, TFHE for arbitrary boolean/integer functions.

3. **Estimate circuit depth** — Count the maximum number of sequential multiplications in the computation graph. This determines parameter requirements.

4. **Select parameters** — Choose poly_modulus_degree and coeff_modulus to support the required depth at 128-bit security.

5. **Implement and test** — Implement the computation using an HE library. Test against plaintext reference implementation to verify correctness.

6. **Benchmark** — Measure encryption, computation, and decryption latency. Verify memory requirements are within infrastructure limits.

7. **Deploy** — Establish key management (secret key in HSM at controller, public keys distributed to processor), monitoring, and audit logging.

## Key Regulatory References

- GDPR Article 25(1) — Data protection by design (encryption as a design measure)
- GDPR Article 32(1)(a) — Encryption as a security measure
- GDPR Article 28 — Processor obligations (HE enables processing without plaintext exposure)
- GDPR Recital 83 — Encryption to maintain security
- ENISA Report: Data Protection Engineering (2022)
- HomomorphicEncryption.org Standard: Homomorphic Encryption Standardization (2018)
