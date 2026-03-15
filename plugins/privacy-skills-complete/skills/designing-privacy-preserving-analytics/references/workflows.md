# Privacy-Preserving Analytics Workflows

## Workflow 1: Deploying Differential Privacy for a New Analytics Pipeline

```
Step 1: Data Sensitivity Classification
├── Identify all personal data fields in the source dataset
├── Classify fields as direct identifiers, quasi-identifiers, or sensitive attributes
├── Determine the global sensitivity for each planned query function
└── Document the processing purpose and lawful basis under Article 6(1)

Step 2: Privacy Budget Planning
├── Define the annual privacy budget (total epsilon allocation)
├── Allocate epsilon across analytics functions by priority
├── Set per-query epsilon limits and refresh cadences
├── Configure budget exhaustion thresholds (80%, 95%, 100%)
└── Obtain Data Protection Officer approval for budget plan

Step 3: Mechanism Selection
├── Counting queries → Laplace mechanism (pure ε-DP)
├── Mean/variance queries → Gaussian mechanism ((ε,δ)-DP)
├── Selection/optimization queries → Exponential mechanism
├── Set union queries → Partition selection with thresholding
└── Document mechanism choice and sensitivity calibration for each query

Step 4: Implementation
├── Deploy Privacy Gateway service between analyst interface and data store
├── Implement query parser with allowlisted query templates
├── Integrate noise injection layer with selected mechanisms
├── Deploy centralized budget ledger with atomic epsilon deduction
├── Configure minimum group size enforcement (≥11 records)
└── Set up output validation to suppress small-count results

Step 5: Testing and Validation
├── Run utility analysis: compare noised vs. true results at planned epsilon
├── Verify budget accounting under sequential and parallel composition
├── Test budget exhaustion: confirm queries are blocked when budget reaches 100%
├── Perform membership inference attack tests to validate privacy guarantees
└── Document acceptable utility loss thresholds per analytics function

Step 6: Operational Monitoring
├── Monitor per-query epsilon consumption in real time
├── Alert at 80% budget consumption threshold
├── Log analyst identity, query hash, epsilon consumed, and timestamp
├── Generate monthly privacy budget utilization reports for DPO
└── Schedule quarterly recalibration of epsilon allocations based on utility feedback
```

## Workflow 2: Applying k-Anonymity to a Published Dataset

```
Step 1: Quasi-Identifier Identification
├── Enumerate all attributes in the dataset
├── Classify each as: direct identifier, quasi-identifier, sensitive, or non-sensitive
├── Remove all direct identifiers before proceeding
└── Define generalization hierarchies for each quasi-identifier

Step 2: Generalization Hierarchy Design
├── Age: exact → 5-year range → 10-year range → 20-year range → all
├── Postal code: full → first 4 digits → first 3 digits → first 2 digits → all
├── Gender: exact → suppressed
├── Occupation: specific → category → broad category → all
└── Test each level for information loss using normalized certainty penalty

Step 3: Achieve k-Anonymity
├── Set target k-value (minimum k=5 for general analytics, k=11 for health data)
├── Apply Mondrian multidimensional partitioning algorithm
├── For residual records that cannot achieve k: apply suppression
├── Calculate suppression rate (target: below 5% of total records)
└── If suppression exceeds threshold, relax generalization granularity

Step 4: Verify l-Diversity (if sensitive attributes present)
├── Check that each equivalence class contains ≥ l distinct sensitive values
├── Calculate entropy l-diversity for each class
├── Apply additional generalization or suppression where l-diversity fails
└── Document the achieved l and entropy values

Step 5: Assess t-Closeness (if distributional privacy required)
├── Compute Earth Mover's Distance between each class distribution and overall
├── Verify EMD ≤ t for all equivalence classes
├── If t-closeness fails, apply additional generalization
└── Document achieved t-values and any utility trade-offs

Step 6: Release and Documentation
├── Generate anonymization report documenting techniques, parameters, and residual risk
├── Publish dataset with metadata describing generalization hierarchies applied
├── Record the anonymization event in the Article 30 processing register
└── Schedule re-identification risk assessment at 12-month intervals
```

## Workflow 3: Privacy Budget Reconciliation (Monthly)

```
Step 1: Collect Budget Consumption Data
├── Export epsilon consumption logs from the Privacy Gateway
├── Aggregate consumption by analytics function and time period
├── Calculate remaining budget per function and overall
└── Identify any budget overruns or unauthorized queries

Step 2: Utility Assessment
├── Compare noised results with ground truth for sampled queries
├── Calculate relative error and confidence interval widths
├── Flag analytics functions where utility has degraded below threshold
└── Identify opportunities to reduce epsilon for low-sensitivity queries

Step 3: Budget Rebalancing
├── Propose reallocation from under-utilized functions to over-demand functions
├── Ensure total reallocation does not exceed annual ceiling
├── Obtain DPO approval for any rebalancing adjustments
└── Update Privacy Gateway configuration with new allocations

Step 4: Reporting
├── Generate monthly privacy budget utilization report
├── Include: consumption vs allocation, utility metrics, rebalancing actions
├── Distribute to DPO, analytics leads, and security operations
└── Archive report in compliance documentation repository
```
