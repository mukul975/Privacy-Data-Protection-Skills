# PET Selection Workflows

## Workflow 1: PET Selection for a New Processing Activity

```
Step 1: Requirements Gathering
├── Define the processing activity and its purpose
├── Identify data categories and sensitivity levels
├── Determine the adversary model (honest-but-curious, malicious, insider)
├── Identify performance requirements (latency, throughput)
├── Map organizational constraints (budget, expertise, infrastructure)
└── Identify cross-organizational boundaries (joint controllers, processors)

Step 2: Privacy Property Mapping
├── Identify primary privacy property needed:
│   ├── Confidentiality → HE, TEE, SMPC
│   ├── Anonymity/Unlinkability → DP, k-anonymity
│   ├── Data minimization → ZKP, FL, DP
│   └── Computation integrity → ZKP, TEE
├── Identify secondary privacy properties
└── Map to the use-case matching matrix

Step 3: Feasibility Assessment
├── For each candidate PET:
│   ├── Evaluate performance overhead against requirements
│   ├── Assess implementation complexity and team expertise
│   ├── Check infrastructure prerequisites (TEE needs hardware support)
│   ├── Estimate cost (cloud compute for HE can be 100-1000x standard)
│   └── Verify library maturity and community support
├── Score each candidate on a 1-5 scale across dimensions
└── Rank candidates by composite score

Step 4: Proof of Concept
├── Implement the top-ranked PET on a representative data sample
├── Measure actual performance (latency, memory, accuracy if DP)
├── Validate privacy guarantees with the security team
├── Document integration requirements with existing systems
└── Assess operational complexity (key management, monitoring)

Step 5: GDPR Alignment Review
├── Verify PET satisfies Article 25(1) data protection by design
├── Document PET as Article 32(1) security measure
├── If anonymization is claimed, validate against WP216 criteria
├── Include PET analysis in DPIA under Article 35
├── Obtain DPO sign-off on PET selection and configuration
└── Update Article 30 records with PET deployment details

Step 6: Production Deployment
├── Implement PET with production-grade library and configuration
├── Configure monitoring for PET-specific metrics
├── Establish key management procedures (for HE, SMPC)
├── Train operations team on PET management
├── Schedule annual review of PET effectiveness and alternatives
└── Document in system architecture diagrams
```

## Workflow 2: PET Combination Design

```
Step 1: Identify Residual Risks
├── After selecting primary PET, identify residual privacy risks
├── Common residual risks:
│   ├── FL without DP: gradient inversion can reconstruct training data
│   ├── SMPC without DP: exact outputs may leak information over many queries
│   ├── HE alone: does not protect against computation pattern analysis
│   └── DP alone: may not provide sufficient utility for small datasets
└── Rank residual risks by likelihood and impact

Step 2: Select Complementary PET
├── Map residual risks to PETs that address them
├── FL + DP: prevents gradient inversion with provable guarantees
├── SMPC + DP: adds formal anonymization to exact computation outputs
├── HE + TEE: protects computation patterns and encrypted data
├── FL + Secure Aggregation: prevents server from observing individual updates
└── Verify that the combination does not introduce conflicting requirements

Step 3: Integration Design
├── Define the interaction model between PETs
├── Determine key management topology (separate or shared key infrastructure)
├── Design the data flow showing where each PET applies
├── Establish performance budget allocation between PETs
└── Document the combined privacy guarantee

Step 4: Validation
├── Test combined PET system on representative workload
├── Verify that combining PETs does not degrade individual guarantees
├── Measure combined performance overhead
├── Validate with security team using formal threat model
└── Update DPIA with combined PET analysis
```

## Workflow 3: Annual PET Review

```
Step 1: Technology Landscape Assessment
├── Review new PET developments in the past year
├── Check for vulnerabilities in deployed PET libraries
├── Assess whether performance improvements enable previously infeasible PETs
├── Review regulatory updates affecting PET requirements
└── Survey peer organizations for PET adoption trends

Step 2: Effectiveness Review
├── Review PET performance metrics from the past year
├── Assess whether privacy guarantees remain adequate (e.g., DP epsilon budget)
├── Evaluate operational incidents involving PET systems
├── Gather feedback from development and operations teams
└── Assess cost-effectiveness compared to alternatives

Step 3: Update Recommendations
├── Recommend PET upgrades or replacements where warranted
├── Propose new PET deployments for processing activities lacking PET coverage
├── Update the use-case matching matrix with new entries
├── Revise budget estimates for PET infrastructure
└── File annual PET review report with DPO and CISO
```
