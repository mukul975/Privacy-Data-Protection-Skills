# Audit Sampling Workflows

## Workflow 1: Designing and Executing an Audit Sample

```
Step 1: Define the Audit Objective
├── Identify the control or compliance requirement to be tested
├── Define the population (e.g., all DSARs received in Q1 2026)
├── Determine the attribute to test (e.g., response within 30 days)
└── Clarify what constitutes a deviation (e.g., response >30 days without extension)

Step 2: Select Sampling Approach
├── Statistical sampling:
│   ├── Required when results must be defensible to regulators
│   ├── Required when population is large (>100 items)
│   └── Required when extrapolation to population is needed
├── Non-statistical sampling:
│   ├── Appropriate for small populations (<50 items)
│   ├── Appropriate for targeted risk-based testing
│   └── Must document judgemental selection rationale
└── Document the chosen approach and rationale in working papers

Step 3: Determine Sample Size (Statistical)
├── Set confidence level:
│   ├── 95% for critical controls (breach notification, consent, special category)
│   └── 90% for standard controls
├── Set tolerable deviation rate:
│   ├── 2% for critical controls
│   └── 5% for standard controls
├── Estimate expected deviation rate from prior audits or risk assessment
├── Look up sample size from attribute sampling table
└── Adjust upward for stratification if applicable

Step 4: Stratify the Population (if applicable)
├── Identify stratification factors:
│   ├── Jurisdiction (EU, US, APAC)
│   ├── Data sensitivity (standard, sensitive, special category)
│   ├── Business unit
│   └── Time period
├── Calculate proportional or risk-weighted sample allocation per stratum
└── Document stratification rationale

Step 5: Select the Sample
├── For statistical sampling: use random number generator or systematic selection
├── For non-statistical: document selection criteria and items chosen
├── Record the full sample list with item identifiers
└── Verify sample items exist and are accessible

Step 6: Execute Audit Procedures
├── Apply the defined test to each sample item
├── Record the result for each item (compliant / deviation)
├── For each deviation:
│   ├── Document the nature of the deviation
│   ├── Investigate the root cause
│   ├── Assess whether deviation is isolated or systemic
│   └── Cross-reference to evidence repository
└── Complete testing for all sample items (no items may be discarded)

Step 7: Evaluate Results
├── Calculate sample deviation rate = deviations / sample size
├── Compare to tolerable deviation rate:
│   ├── Below tolerable → conclude population is compliant
│   ├── At tolerable → consider expanding sample or raising medium finding
│   └── Above tolerable → material finding; extrapolate to population
├── Calculate point estimate of population deviations
├── Determine upper deviation limit at selected confidence level
└── Document conclusion with statistical basis
```

## Workflow 2: Stratified Sampling for Multi-Jurisdiction Privacy Audit

```
Step 1: Define population and strata
├── Population: 1,200 vendor data processing agreements across 3 regions
├── Strata:
│   ├── EU vendors (500 DPAs) — GDPR Article 28 compliance
│   ├── US vendors (450 DPAs) — CCPA/state law compliance
│   └── APAC vendors (250 DPAs) — local law compliance
└── Attribute: DPA contains all required clauses per applicable regulation

Step 2: Risk-weighted allocation
├── EU (highest regulatory risk): 40% of sample → 24 items
├── US (medium regulatory risk): 35% of sample → 21 items
├── APAC (lower regulatory risk): 25% of sample → 15 items
└── Total sample: 60 items

Step 3: Within-stratum selection
├── Random selection within each stratum
├── Ensure representation across vendor tiers within each stratum
└── Document selection method

Step 4: Testing and evaluation
├── Test each item against stratum-specific criteria
├── Calculate deviation rate per stratum
├── Calculate overall weighted deviation rate
└── Report per-stratum and overall results
```

## Workflow 3: Expanding a Sample When Deviations Are Found

```
START: Initial sample of 50 items; 4 deviations found (8%)
│
├─ Step 1: 8% exceeds 5% tolerable deviation rate
│  └─ Decision: expand sample to increase precision
│
├─ Step 2: Calculate expanded sample size
│  ├── At 95% confidence with 8% expected deviation and 5% tolerable
│  └── Expanded sample size: 100 items (additional 50 items)
│
├─ Step 3: Select additional 50 items using same method
│  └── Test all additional items
│
├─ Step 4: Combined evaluation
│  ├── Total deviations across 100 items
│  ├── Revised deviation rate
│  ├── If still above tolerable → formal finding with extrapolation
│  └── If now within tolerable → conclude with expanded sample support
│
END: Document expanded sampling rationale and revised conclusion
```
