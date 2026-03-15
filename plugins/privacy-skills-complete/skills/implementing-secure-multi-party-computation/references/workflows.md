# Secure Multi-Party Computation Workflows

## Workflow 1: Deploying SMPC for Cross-Organizational Analytics

```
Step 1: Use Case Definition
├── Define the joint computation function f(x_1, x_2, ..., x_n)
├── Identify each party's input (data categories and sensitivity)
├── Define the output and who receives it
├── Determine the adversary model (semi-honest vs malicious)
└── Estimate input sizes and computation complexity

Step 2: Legal Framework
├── Execute joint controller agreement under Article 26
├── Define each party's role (data controller, computation coordinator)
├── Agree on output usage limitations and retention
├── Conduct DPIA for the joint computation (Art. 35 if high risk)
└── Notify respective DPOs at each participating organization

Step 3: Protocol Selection
├── Two parties → Consider Yao's GC (constant rounds) or ABY (mixed protocols)
├── Three parties, honest majority → Rep3 or Shamir (fastest)
├── Multiple parties, dishonest majority → SPDZ/MASCOT (malicious secure)
├── ML workload → CrypTen (PyTorch-based)
├── Evaluate: communication volume, round complexity, memory requirements
└── Benchmark on representative data to verify feasibility

Step 4: Implementation
├── Express computation in framework DSL (MP-SPDZ .mpc file or CrypTen Python)
├── Implement input preprocessing at each party
├── Configure secure communication channels (mTLS between parties)
├── Implement output validation and post-processing
├── Test end-to-end on synthetic data matching real schema
└── Verify correctness: compare SMPC output with plaintext reference

Step 5: Deployment
├── Deploy computation nodes at each party's infrastructure
├── Configure SMPC coordinator for protocol orchestration
├── Establish key material distribution (for OT-based protocols)
├── Set up monitoring: computation latency, communication volume, error rates
├── Deploy audit logging at each party
└── Execute dry run with production data subset

Step 6: Operations
├── Schedule computation execution cadence (daily, weekly, quarterly)
├── Monitor protocol execution health
├── Rotate cryptographic keys per agreed schedule
├── Review joint controller agreement annually
├── Reassess computation function if business requirements change
└── Update Article 30 records at each party
```

## Workflow 2: Private Set Intersection Deployment

```
Step 1: PSI Requirements
├── Party A has set S_A (e.g., customer email hashes)
├── Party B has set S_B
├── Goal: compute S_A ∩ S_B without revealing non-intersecting elements
├── Select PSI variant:
│   ├── Standard PSI: both parties learn the intersection
│   ├── PSI-cardinality: parties learn only |S_A ∩ S_B| (count)
│   └── Circuit-PSI: parties learn a function of the intersection elements
└── Determine set sizes and acceptable latency

Step 2: Protocol Selection
├── Small sets (< 10,000): Diffie-Hellman based PSI (simple, efficient)
├── Large sets (10,000 - 1,000,000): OT-extension based PSI (OPRF)
├── Very large sets (> 1,000,000): Cuckoo hashing + OPRF
└── If only cardinality needed: Bloom filter based PSI-CA (fastest)

Step 3: Implementation
├── Hash identifiers with agreed-upon hash function before PSI
├── Implement chosen PSI protocol using MP-SPDZ or dedicated library
├── Test with synthetic data of equivalent size
├── Measure: computation time, communication volume, memory usage
└── Verify: non-intersecting elements are not revealed

Step 4: Joint Processing on Intersection
├── For matched records, parties proceed to SMPC on features
├── Define the joint function (e.g., aggregate risk score)
├── Each party provides their features for matched records only
├── Execute SMPC protocol on matched-record features
└── Both parties receive the agreed output

Step 5: Audit and Documentation
├── Log PSI execution: timestamp, set sizes, intersection cardinality
├── Do NOT log intersection elements (privacy violation)
├── Document protocol parameters and security guarantees
├── File execution report with respective DPOs
└── Schedule next execution per agreed cadence
```

## Workflow 3: SMPC Incident Response

```
Step 1: Detection
├── Protocol execution failure or timeout
├── Suspicious communication patterns detected
├── Output validation fails (result outside expected range)
└── Party reports potential compromise

Step 2: Containment
├── Halt all in-progress SMPC computations
├── Preserve communication logs and local computation state
├── Notify all parties and the computation coordinator
└── Assess whether any party's input may have been exposed

Step 3: Investigation
├── Determine root cause: network failure, software bug, or adversarial action
├── If adversarial: assess whether the adversary exceeded the security model's assumptions
├── If semi-honest protocol was used: determine if a party deviated from the protocol
├── Review communication logs for anomalies
└── Engage cryptographic security expert for assessment

Step 4: Remediation
├── Fix root cause (software patch, network reconfiguration)
├── If party compromise suspected: revoke that party's credentials
├── Consider upgrading from semi-honest to malicious-secure protocol
├── Re-execute the failed computation with corrective measures
└── Update security model assessment

Step 5: Reporting
├── File incident report with all participating DPOs
├── If personal data exposure is confirmed: assess Art. 33/34 notification requirements
├── Update joint controller agreement if security model changes
├── Document lessons learned and preventive measures
└── Schedule follow-up review at 30 days
```
