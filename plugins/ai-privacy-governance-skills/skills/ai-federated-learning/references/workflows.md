# Federated Learning Workflows

## Workflow 1: FL Architecture Selection

```
START: AI training requires personal data from multiple sources
│
├─ Step 1: Assess data distribution
│  ├─ Same features, different samples (horizontal) → Cross-device or cross-silo FL
│  ├─ Different features, same samples (vertical) → Vertical FL
│  └─ Different features, different samples → Transfer learning or FL hybrid
│
├─ Step 2: Assess participant characteristics
│  ├─ Many participants (1000+), small data each → Cross-device FL
│  ├─ Few participants (2-100), large data each → Cross-silo FL
│  └─ 2-10 organisations with complementary features → Vertical FL
│
├─ Step 3: Select aggregation protocol
│  ├─ High privacy requirement + moderate compute → Masking-based secure aggregation
│  ├─ High privacy + high compute budget → Homomorphic encryption
│  ├─ High performance + hardware trust → TEE-based aggregation
│  └─ Moderate privacy requirement → DP-only (without secure aggregation)
│
├─ Step 4: Select DP integration
│  ├─ Untrusted aggregator → Local DP (noise added at participant)
│  ├─ Trusted/secure aggregator → Central DP (noise added after aggregation)
│  └─ Calibrate epsilon budget for target accuracy/privacy trade-off
│
└─ Step 5: Document architecture decision with GDPR justification
```

## Workflow 2: GDPR Compliance for FL Deployment

```
START: FL architecture selected
│
├─ Step 1: Controller/processor determination
│  ├─ Who determines purpose and means of processing?
│  ├─ Cross-device: platform operator = controller; device owners = data subjects
│  ├─ Cross-silo: each silo may be independent controller or joint controllers
│  ├─ Aggregator: processor (if acting on instructions) or joint controller
│  └─ Document: roles per Art. 26 or Art. 28 as applicable
│
├─ Step 2: Legal agreements
│  ├─ Joint controller agreement (Art. 26) if joint controllers identified
│  ├─ Data processing agreement (Art. 28) if aggregator is processor
│  ├─ Data sharing agreement between silos if required
│  └─ Define responsibilities: transparency, rights, security, breach notification
│
├─ Step 3: Lawful basis per participant
│  ├─ Each participant needs lawful basis for local training
│  ├─ Aggregator needs basis for processing model updates (likely legitimate interest)
│  ├─ Document per-participant lawful basis assessment
│  └─ Assess Art. 6(4) compatibility if data repurposed for FL training
│
├─ Step 4: Transparency
│  ├─ Inform data subjects about FL participation
│  ├─ Explain what data is processed locally and what is transmitted
│  ├─ Describe privacy measures (secure aggregation, DP)
│  └─ Update privacy notices per Arts. 13-14
│
├─ Step 5: Data subject rights
│  ├─ Right to erasure: mechanism to exclude participant and address model impact
│  ├─ Right to object: opt-out from FL participation
│  ├─ Right to access: clarify what data is processed and how
│  └─ Document rights exercise procedures for FL context
│
├─ Step 6: International transfers
│  ├─ If participants are in different jurisdictions:
│  │  ├─ Are model updates "personal data"? (Depends on privacy measures)
│  │  ├─ With secure aggregation + DP: may not constitute personal data transfer
│  │  └─ Without sufficient privacy measures: transfer safeguards required (SCCs, adequacy)
│  └─ Document transfer assessment
│
├─ Step 7: DPIA
│  ├─ Conduct AI DPIA covering FL architecture
│  ├─ Assess gradient leakage risks
│  ├─ Assess model memorization risks
│  ├─ Document privacy measures and residual risk
│  └─ Register DPIA with review schedule
│
└─ END: FL deployment compliant. Schedule periodic review.
```

## Workflow 3: Privacy Budget Management

```
START: FL training with differential privacy
│
├─ Step 1: Set privacy budget
│  ├─ Target epsilon: based on data sensitivity
│  │  ├─ Special category data: ε ≤ 1 (strong privacy)
│  │  ├─ General personal data: ε ≤ 8 (moderate privacy)
│  │  └─ Low-sensitivity data: ε ≤ 16 (basic privacy)
│  ├─ Delta: δ < 1/N (N = total data points across participants)
│  └─ Document: privacy budget targets with justification
│
├─ Step 2: Calibrate parameters
│  ├─ Clip norm (C): set based on gradient norm distribution analysis
│  ├─ Noise multiplier (σ): compute from ε, δ, C, and number of rounds
│  ├─ Sampling rate (q): fraction of participants per round
│  └─ Use privacy accounting (Renyi DP or GDP) for tight composition
│
├─ Step 3: Monitor privacy consumption
│  ├─ Track cumulative privacy loss per round
│  ├─ Alert when approaching budget threshold (80%, 90%, 100%)
│  ├─ If budget exhausted: stop training or accept increased epsilon
│  └─ Log: per-round privacy consumption
│
├─ Step 4: Evaluate utility-privacy trade-off
│  ├─ Compare model accuracy with and without DP
│  ├─ If accuracy unacceptable: increase epsilon, add participants, or adjust architecture
│  ├─ Document: accuracy at target epsilon
│  └─ Report: privacy-utility trade-off analysis
│
└─ END: Privacy budget consumed or training complete. Document final epsilon.
```
