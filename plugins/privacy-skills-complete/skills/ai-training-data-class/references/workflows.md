# Workflows — AI Training Data Classification

## Workflow 1: Training Dataset Classification and Approval

### Process Flow

```
START: ML team requests use of dataset for model training
  │
  ├─► Step 1: Personal Data Screening
  │     - Scan dataset for PII using automated discovery tools
  │     - Classify each data element per personal-data-test framework
  │     - Identify Art. 9 special category data (direct or inferred)
  │     - Identify Art. 10 criminal data
  │     Output: Dataset personal data classification report
  │
  ├─► Step 2: Purpose Compatibility Assessment
  │     - Document the original purpose for which data was collected
  │     - Document the proposed ML training purpose
  │     - Assess compatibility under Art. 6(4) factors:
  │       (a) link between original and training purpose
  │       (b) context of collection and data subject expectations
  │       (c) nature of the data (sensitivity)
  │       (d) consequences for data subjects
  │       (e) safeguards (pseudonymisation, access controls)
  │     - If not compatible: establish new lawful basis
  │     Output: Purpose compatibility assessment
  │
  ├─► Step 3: Lawful Basis Establishment
  │     - For compatible purpose: rely on original lawful basis
  │     - For new purpose: most likely Art. 6(1)(f) legitimate interests
  │       → Conduct and document Legitimate Interest Assessment (LIA)
  │     - For special category data: establish Art. 9(2) condition
  │       → Typically Art. 9(2)(j) research with Art. 89(1) safeguards
  │       → Or Art. 9(2)(g) substantial public interest for bias detection
  │     Output: Documented lawful basis
  │
  ├─► Step 4: Bias and Proxy Variable Assessment
  │     - Scan all features for proxy correlation with protected characteristics
  │     - Calculate demographic representation statistics
  │     - Flag proxy variables (correlation > 0.3 with protected characteristic)
  │     - Document in data card bias assessment section
  │     Output: Bias assessment report
  │
  ├─► Step 5: De-identification Assessment
  │     - Can the training objective be achieved with anonymised data?
  │       YES → Apply anonymisation, verify per pseudo-vs-anon-data framework
  │       NO  → Apply pseudonymisation as minimum safeguard
  │     - Can synthetic data substitute for real data?
  │       YES → Generate synthetic data, validate model performance
  │       NO  → Document why real data is necessary
  │     Output: De-identification strategy and assessment
  │
  ├─► Step 6: Data Card Creation
  │     - Complete all required data card fields
  │     - Include provenance chain from original collection to training set
  │     - Include bias assessment results
  │     - Include de-identification assessment
  │     Output: Completed data card
  │
  ├─► Step 7: DPIA (if required)
  │     - High-risk AI system (AI Act Annex III)? → DPIA required
  │     - Automated decision-making with legal/significant effects? → DPIA required
  │     - Large-scale special category processing? → DPIA required
  │     - If DPIA required: conduct per conducting-gdpr-dpia skill
  │     Output: DPIA reference (or documented assessment that DPIA not required)
  │
  └─► Step 8: Approval and Access Provisioning
        - DPO reviews classification, lawful basis, data card, and DPIA
        - ML team lead signs acceptance of data handling conditions
        - Access provisioned to approved training environment only
        - Audit logging enabled for all training data access
        Output: Approved dataset with data card and access controls
```

## Workflow 2: Ongoing Training Data Governance

### Process Flow

```
Quarterly Review Cycle
  │
  ├─► Review training data inventory
  │     - Are all active training datasets registered with data cards?
  │     - Have any datasets been modified since last review?
  │     - Are retention periods being observed?
  │
  ├─► Bias monitoring
  │     - Re-run disparate impact analysis on deployed models
  │     - Compare with training data bias assessment
  │     - Flag models with degraded fairness metrics
  │
  ├─► Consent/lawful basis review
  │     - Any changes to consent scope or withdrawal rates?
  │     - Any regulatory guidance affecting lawful basis assessment?
  │
  └─► Retention enforcement
        - Delete training data past retention date
        - Document model weights that may embed personal data
        - Assess whether model retraining requires fresh consent
```
