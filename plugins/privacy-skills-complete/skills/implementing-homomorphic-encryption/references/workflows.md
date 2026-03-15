# Homomorphic Encryption Implementation Workflows

## Workflow 1: HE Deployment for Cloud-Based Data Processing

```
Step 1: Use Case Analysis
├── Define the computation to perform on encrypted data
├── Express computation as additions, multiplications, and rotations
├── Determine required data types (integer vs real number)
├── Calculate the multiplicative depth of the computation circuit
├── Identify input size (number of records, values per record)
└── Define acceptable latency and throughput requirements

Step 2: Scheme and Parameter Selection
├── Integer computation → BFV or BGV
├── Real-number computation → CKKS
├── Arbitrary boolean/integer functions → TFHE
├── Select poly_modulus_degree based on security level and depth:
│   ├── Depth 1-2: N=4096 or N=8192
│   ├── Depth 3-5: N=8192 or N=16384
│   └── Depth 6+: N=16384 or N=32768
├── Select coeff_modulus primes to support required depth
├── For BFV: set plain_modulus to accommodate plaintext range
├── For CKKS: set scale based on required precision
└── Verify parameters provide at least 128-bit security

Step 3: Implementation
├── Generate keys: secret key (sk), public key (pk), relinearization keys (rlk)
├── For SIMD operations: generate Galois keys (gk)
├── Implement plaintext encoding (BatchEncoder for BFV, CKKSEncoder for CKKS)
├── Implement the computation circuit on ciphertexts
├── Implement result decoding and decryption
├── Write plaintext reference implementation for correctness verification
└── Create comprehensive test suite comparing encrypted vs plaintext results

Step 4: Key Management
├── Secret key: store in HSM at controller premises (never export)
├── Public key + evaluation keys: distribute to processor via secure channel
├── Key rotation schedule: annual rotation with re-encryption migration
├── Key backup: encrypted backup of sk in separate HSM with dual-custody access
└── Key destruction: zeroize all key material at end of processing lifecycle

Step 5: Deployment
├── Deploy key generation and encryption at controller (Prism Data Systems AG)
├── Deploy computation service at processor (cloud environment)
├── Configure encrypted result return channel
├── Deploy decryption service at controller
├── Set up monitoring for computation latency and error rates
└── Log all encryption/decryption operations in audit trail

Step 6: Validation
├── Verify encrypted computation matches plaintext reference within tolerance
├── For CKKS: verify approximation error is within acceptable bounds
├── Benchmark end-to-end latency (encrypt + compute + decrypt)
├── Verify the processor environment cannot access the secret key
├── Document HE deployment in DPIA and Article 30 records
└── Obtain DPO sign-off on cryptographic parameter choices
```

## Workflow 2: HE Parameter Tuning

```
Step 1: Baseline Measurement
├── Run computation with initial parameter set
├── Measure: ciphertext size, computation time, memory usage
├── Verify: noise budget remaining after computation
└── Record baseline metrics for comparison

Step 2: Depth Optimization
├── Analyze computation graph for unnecessary depth
├── Apply tree-reduction for summation (log depth instead of linear)
├── Reorder operations to minimize multiplicative depth
├── Apply Horner's method for polynomial evaluation
└── Re-measure noise budget and latency

Step 3: Batching Optimization
├── Restructure data for SIMD encoding (vectorize operations)
├── Maximize slot utilization (fill all N/2 slots if possible)
├── Use rotations to align data for cross-slot operations
├── Measure throughput improvement from batching
└── Calculate effective per-record cost

Step 4: Parameter Refinement
├── If noise budget is abundant: reduce poly_modulus_degree
├── If noise budget is tight: increase coeff_modulus or add primes
├── If memory is constrained: reduce poly_modulus_degree (accept less depth)
├── Verify security level remains at 128 bits after changes
└── Re-run benchmark and compare against baseline

Step 5: Documentation
├── Record final parameter set with justification
├── Document security level achieved
├── Record performance benchmarks (latency, throughput, memory)
├── Note known limitations and failure modes
└── File parameter documentation in cryptographic configuration registry
```

## Workflow 3: HE Key Lifecycle Management

```
Step 1: Key Generation
├── Generate key pair (sk, pk) in HSM at controller premises
├── Generate relinearization keys (rlk) and Galois keys (gk)
├── Record key metadata: algorithm, parameters, creation date, version
├── Store sk in HSM with restricted access (dual-custody retrieval)
└── Export pk, rlk, gk for distribution to processor

Step 2: Key Distribution
├── Transmit pk, rlk, gk to processor via TLS 1.3 with mutual authentication
├── Verify key integrity at processor using hash verification
├── Processor loads keys into computation service memory
└── Log key distribution event with timestamps

Step 3: Key Rotation (Annual)
├── Generate new key pair (sk', pk')
├── Issue pk' to processor; processor begins accepting ciphertexts under pk'
├── Re-encrypt active data: decrypt with sk, re-encrypt with pk'
├── After migration window: deactivate old pk, confirm processor no longer uses it
├── Destroy old sk after confirmation period (30 days)
└── Update key metadata and audit trail

Step 4: Key Destruction
├── At end of processing lifecycle or retention period expiry
├── Zeroize sk in HSM using FIPS 140-2 Level 3 destruction command
├── Instruct processor to delete pk, rlk, gk from all systems
├── Verify key deletion via processor attestation
├── Encrypted data without sk is cryptographically inaccessible (crypto-shredding)
└── Log destruction event in audit trail and update Article 30 records
```
