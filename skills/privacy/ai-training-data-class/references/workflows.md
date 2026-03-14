# Workflows — AI Training Data Classification

## Workflow 1: Training Dataset Classification and Approval

### Process Flow

```
START: New ML model development requiring training data
  │
  ├─► Step 1: Data Requirements Definition
  │     - Data scientist defines required features and labels
  │     - Identify candidate data sources (internal systems, third-party, public)
  │     - Estimate required volume and representativeness
  │     Output: Training data requirements specification
  │
  ├─► Step 2: Personal Data Classification
  │     - Scan candidate data for PII (auto-data-discovery)
  │     - Classify each feature as personal/non-personal
  │     - Identify Art. 9 special category features (direct and proxy)
  │     - Identify Art. 10 criminal data features
  │     Output: Feature-level privacy classification
  │
  ├─► Step 3: Lawful Basis Assessment
  │     For each personal data feature:
  │     3a. Was ML training included in the original collection purpose?
  │     3b. If not: is training compatible under Art. 6(4) compatibility test?
  │     3c. What lawful basis applies? (consent, legitimate interests, etc.)
  │     3d. For Art. 9 data: what Art. 9(2) condition applies?
  │     3e. For bias monitoring under EU AI Act Art. 10(5): document necessity
  │     Output: Lawful basis assessment per feature
  │
  ├─► Step 4: Bias Risk Assessment
  │     - Identify protected characteristics in training features
  │     - Identify proxy features correlated with protected characteristics
  │     - Assess label/outcome distribution across demographic groups
  │     - Calculate preliminary fairness metrics on historical data
  │     Output: Bias risk assessment report
  │
  ├─► Step 5: Data Minimisation Review
  │     - For each personal data feature: is it necessary for model performance?
  │     - Can the feature be anonymised or pseudonymised without significant
  │       accuracy loss?
  │     - Can synthetic data substitute for personal data?
  │     - Remove unnecessary features; apply pseudonymisation where possible
  │     Output: Minimised feature set
  │
  ├─► Step 6: Data Card Creation
  │     - Complete all required data card fields
  │     - Document provenance for each data source
  │     - Record consent status and lawful basis
  │     - Record bias assessment findings
  │     - Record quality metrics
  │     Output: Completed data card
  │
  ├─► Step 7: DPIA (if required)
  │     Triggers: personal data at scale, automated profiling, Art. 9 data
  │     - Conduct DPIA per conducting-gdpr-dpia skill
  │     - Document residual risks and mitigations
  │     Output: Completed DPIA
  │
  └─► Step 8: DPO Approval
        - DPO reviews classification, lawful basis, bias assessment, and DPIA
        - Approval/rejection with conditions
        - If approved: training may proceed under documented conditions
        Output: DPO approval record
```

## Workflow 2: Post-Training Data Subject Rights Fulfilment

### Process Flow

```
START: Data subject exercises rights related to ML training data
  │
  ├─► RIGHT TO ACCESS (Art. 15)
  │     - Confirm whether data subject's data was used in training
  │     - Provide: categories of training data, purpose, lawful basis
  │     - Provide: information about automated decision-making (Art. 22)
  │     - Note: obligation is to provide information about the data, not
  │       to explain the model (but meaningful information about logic required)
  │
  ├─► RIGHT TO ERASURE (Art. 17)
  │     - Remove data subject's records from training dataset
  │     - Assess whether the trained model must be retrained:
  │       • If model memorised individual records → retraining required
  │       • If model only learned aggregate patterns → retraining may not
  │         be required (document proportionality assessment)
  │     - If retraining required: schedule retraining, document timeline
  │     - If machine unlearning technique available: apply and validate
  │     - Delete data from training data store and all copies
  │
  ├─► RIGHT TO RECTIFICATION (Art. 16)
  │     - Correct data subject's records in training dataset
  │     - Assess impact on model accuracy
  │     - Schedule retraining if correction is material
  │
  └─► RIGHT TO OBJECT (Art. 21)
        - If processing based on legitimate interests: assess objection
        - If compelling grounds exist for continued processing: document
        - If no compelling grounds: remove data and retrain if necessary
```
