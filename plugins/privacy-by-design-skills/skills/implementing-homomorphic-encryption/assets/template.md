# Homomorphic Encryption Deployment Assessment

## Deployment Details

| Item | Value |
|------|-------|
| Organization | Prism Data Systems AG |
| Processing Activity | Revenue analytics on encrypted customer transaction data |
| Assessment Date | 2026-03-14 |
| Assessor | Thomas Richter (Privacy Engineering Lead) |
| DPO Approval | Dr. Lukas Meier |

## Scheme Selection

| Criterion | Decision | Justification |
|-----------|----------|---------------|
| Data type | Integer (transaction amounts in centimes) | Revenue data is integer-valued; exact results required |
| Scheme | BFV | Exact integer arithmetic with SIMD batching |
| Circuit depth | 2 (sum + one multiplication for weighted aggregation) | Shallow circuit keeps parameters small |
| Library | Microsoft SEAL via TenSEAL (Python) | Production-grade, well-documented, Microsoft-supported |

## Parameter Configuration

| Parameter | Value | Justification |
|-----------|-------|---------------|
| poly_modulus_degree | 8192 | Supports depth 3 at 128-bit security; sufficient for revenue sum and weighted aggregation |
| coeff_modulus | [60, 40, 40, 60] (200 bits total) | 3 primes for 2 multiplications + final decryption |
| plain_modulus | 786433 | Prime, supports batching; accommodates transaction values up to ~786K centimes |
| Security level | 128-bit | HomomorphicEncryption.org recommended minimum |
| SIMD slot count | 4096 | Batch 4096 transactions per ciphertext |

## Performance Benchmarks

| Operation | Measured Latency | Throughput |
|-----------|-----------------|------------|
| Key generation | 48 ms | N/A (one-time) |
| Encryption (4096 values batched) | 1.8 ms | 2.3M values/sec |
| Ciphertext addition | 0.08 ms | 51M values/sec (batched) |
| Ciphertext-plaintext multiplication | 0.3 ms | 13.7M values/sec (batched) |
| Ciphertext-ciphertext multiplication | 4.2 ms | 975K values/sec (batched) |
| Decryption | 0.9 ms | 4.6M values/sec |
| End-to-end (encrypt + sum 10K values + decrypt) | 12 ms | N/A |

## Key Management Plan

| Key | Storage | Access Control | Rotation |
|-----|---------|---------------|----------|
| Secret key (sk) | HSM at Prism Data Systems AG Zurich datacenter (FIPS 140-2 Level 3) | Dual-custody: DPO + CISO required for access | Annual |
| Public key (pk) | Cloud processor key store | Processor operations team | Rotated with sk |
| Relinearization keys (rlk) | Cloud processor key store | Processor operations team | Rotated with sk |
| Galois keys (gk) | Cloud processor key store | Processor operations team | Rotated with sk |

## GDPR Compliance Documentation

| GDPR Requirement | How HE Addresses It |
|-----------------|---------------------|
| Art. 25(1) data protection by design | HE is embedded as a design measure in the analytics architecture; personal data is encrypted before leaving the controller's environment |
| Art. 32(1)(a) encryption | Transaction data is encrypted end-to-end; the cloud processor never accesses plaintext values |
| Art. 28 processor obligations | The processor computes on ciphertexts only; even a compromised processor cannot access personal data without the secret key held by Prism Data Systems AG |
| Art. 5(1)(c) data minimization | Only encrypted aggregation results are returned; individual transaction values are never exposed to the processing environment |

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Secret key compromise | Low (HSM-stored, dual-custody) | High (all encrypted data exposed) | HSM with tamper detection; annual key rotation; audit logging |
| Noise budget exhaustion | Low (shallow circuit, conservative parameters) | Medium (incorrect results) | Pre-deployment circuit analysis; runtime noise budget monitoring |
| Side-channel attack on processor | Low | Medium | TEE complement for defense in depth (future phase) |
| Parameter vulnerability (future cryptanalysis) | Very Low | High | Monitor NIST PQC and HE standardization updates; annual parameter review |

## Approval

| Role | Name | Decision | Date |
|------|------|----------|------|
| Privacy Engineering Lead | Thomas Richter | Recommended | 2026-03-14 |
| Data Protection Officer | Dr. Lukas Meier | Approved | 2026-03-14 |
| CISO | Michael Baumann | Approved (key management plan) | 2026-03-14 |
