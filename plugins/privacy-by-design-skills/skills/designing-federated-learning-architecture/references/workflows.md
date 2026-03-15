# Federated Learning Architecture Workflows

## Workflow 1: Deploying a Horizontal FL System

```
Step 1: Consortium Formation
├── Identify participating organizations and their data assets
├── Execute joint controller agreement under GDPR Article 26
├── Define model ownership, IP rights, and exit procedures
├── Agree on privacy parameters (epsilon, secure aggregation protocol)
├── Establish governance committee for FL program oversight
└── Conduct DPIA if processing involves special category data (Art. 35)

Step 2: Data Readiness Assessment
├── Verify each participant's data schema alignment (feature names, types)
├── Assess data distribution across participants (IID vs non-IID)
├── Determine per-participant dataset size for weighted aggregation
├── Identify data quality issues (missing values, label noise)
└── Agree on common preprocessing pipeline (normalization, encoding)

Step 3: Architecture Design
├── Select aggregation strategy:
│   ├── IID data → FedAvg
│   ├── Non-IID data → FedProx (μ=0.01-0.1)
│   └── Untrusted participants → Byzantine-robust (Krum or trimmed mean)
├── Select privacy mechanisms:
│   ├── Secure aggregation (pairwise masking or HE-based)
│   ├── Differential privacy (gradient clipping + Gaussian noise)
│   └── Set privacy budget (target epsilon and delta)
├── Select communication compression:
│   ├── Low bandwidth → Top-k sparsification or SignSGD
│   └── Adequate bandwidth → Full gradient or 8-bit quantization
└── Design model architecture (must be identical across participants)

Step 4: Implementation
├── Deploy aggregation server in neutral infrastructure
├── Deploy local training pipeline at each participant
├── Implement gradient clipping (norm bound C) at each participant
├── Implement Gaussian noise injection for DP at each participant
├── Implement secure aggregation protocol between participants and server
├── Configure communication compression
└── Set up monitoring dashboards for convergence, participation, and privacy budget

Step 5: Training Execution
├── Initialize global model and distribute to participants
├── For each communication round:
│   ├── Server selects participants (random or round-robin)
│   ├── Selected participants train locally for E epochs
│   ├── Participants clip gradients and add DP noise
│   ├── Participants send encrypted/masked updates to server
│   ├── Server aggregates updates and creates new global model
│   ├── Server distributes updated model to participants
│   └── Log round metrics: loss, accuracy, privacy budget consumed
├── Stop when convergence criteria met or privacy budget exhausted
└── Evaluate final model on held-out test sets at each participant

Step 6: Model Deployment and Governance
├── Deploy trained model per agreed ownership terms
├── Document training provenance (rounds, participants, privacy parameters)
├── File model card documenting training methodology and privacy guarantees
├── Schedule model retraining cadence (quarterly or on data drift detection)
├── Establish model sunset procedure (delete model when purpose expires)
└── Update Article 30 records at each participant organization
```

## Workflow 2: Adding Differential Privacy to an Existing FL Pipeline

```
Step 1: Privacy Budget Planning
├── Determine target (epsilon, delta) for the overall training run
├── Calculate per-round epsilon using Rényi DP composition
├── Determine maximum training rounds within budget
├── Set gradient clipping norm (C) based on gradient magnitude analysis
└── Calculate noise multiplier (σ) for target privacy guarantee

Step 2: Implementation
├── Add gradient clipping to local training:
│   ├── After local SGD step, compute gradient norm ||g||
│   ├── If ||g|| > C, rescale: g = g * (C / ||g||)
│   └── Log clipping statistics (fraction of gradients clipped)
├── Add Gaussian noise injection:
│   ├── Sample noise: z ~ N(0, σ²·C²·I)
│   ├── Add noise to clipped gradient: g' = g + z
│   └── Send noised gradient to aggregation server
├── Implement privacy accounting:
│   ├── Track per-round epsilon consumption
│   ├── Accumulate total epsilon using Rényi DP accountant
│   ├── Alert at 80% budget consumed
│   └── Stop training at 100% budget consumed
└── Verify noise does not prevent model convergence

Step 3: Validation
├── Compare model accuracy with and without DP
├── Document accuracy-privacy trade-off
├── Run membership inference attack test to validate privacy
├── Verify privacy accounting is correct
└── Document DP parameters in model card and DPIA
```

## Workflow 3: FL Participant Onboarding

```
Step 1: Technical Readiness
├── Verify participant infrastructure meets minimum requirements:
│   ├── GPU with sufficient memory for local model training
│   ├── Network connectivity to aggregation server (encrypted channel)
│   ├── Storage for local dataset and model checkpoints
│   └── Compute capacity for training within round timeout
├── Deploy local training pipeline software
├── Verify data schema compatibility with consortium standard
└── Run test round with synthetic data

Step 2: Legal and Governance
├── Execute joint controller agreement (Art. 26)
├── Verify participant's lawful basis for processing
├── Confirm participant's DPO is aware of FL participation
├── Review participant's data protection policies
└── Add participant to consortium governance register

Step 3: Integration Testing
├── Run end-to-end test round with participant's real data
├── Verify gradient format and size compatibility
├── Verify secure aggregation protocol works with new participant
├── Measure communication latency and bandwidth usage
├── Confirm model convergence is not degraded by new participant
└── Approve participant for production rounds

Step 4: Ongoing Monitoring
├── Monitor participant's contribution quality (gradient norms, loss)
├── Detect potential free-rider behavior (abnormally low gradient norms)
├── Track participant uptime and round participation rate
├── Reassess data distribution impact quarterly
└── Review joint controller agreement annually
```
