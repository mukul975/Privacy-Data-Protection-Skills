# LINDDUN Threat Modeling Workflows

## Workflow 1: Full LINDDUN Assessment

```
Step 1: System Modeling (DFD Creation)
├── Identify all external entities (data subjects, third parties, regulators)
├── Identify all processes (system components that process personal data)
├── Identify all data stores (databases, caches, file systems, logs)
├── Map all data flows between elements
├── Draw trust boundaries (internal network, cloud, third-party)
├── Annotate DFD elements with data categories processed
└── Review DFD with development team for completeness

Step 2: Threat Mapping
├── For each DFD element, identify applicable LINDDUN categories:
│   ├── External entities → I, U
│   ├── Processes → L, I, N, D, DD, NC
│   ├── Data stores → L, I, N, DD, NC
│   └── Data flows → L, I, N, D, DD, NC
├── Generate threat mapping matrix (DFD elements x LINDDUN categories)
└── Calculate total threat combinations to evaluate

Step 3: Threat Elicitation
├── For each applicable (element, category) pair:
│   ├── Consult the LINDDUN threat tree for that category
│   ├── Walk through each branch of the threat tree
│   ├── Determine if the threat is applicable to this system
│   ├── If applicable, document:
│   │   ├── Threat ID (e.g., L-DS01: Linking via data store quasi-identifiers)
│   │   ├── Description
│   │   ├── Affected DFD element
│   │   ├── Attack scenario
│   │   └── Affected data categories
│   └── If not applicable, document reason for exclusion
└── Compile complete threat register

Step 4: Risk Assessment
├── For each identified threat, assess:
│   ├── Likelihood (1-5): How likely is this threat to materialize?
│   ├── Impact (1-5): What is the harm to data subjects if it materializes?
│   └── Risk score = Likelihood x Impact (1-25)
├── Classify risks:
│   ├── 1-6: Low (accept with documentation)
│   ├── 7-12: Medium (mitigate within 6 months)
│   ├── 13-19: High (mitigate within 3 months)
│   └── 20-25: Critical (mitigate immediately)
└── Sort threat register by risk score (descending)

Step 5: Mitigation Selection
├── For each threat requiring mitigation:
│   ├── Identify applicable privacy design patterns (Hoepman's eight)
│   ├── Select specific technical controls from pattern sub-patterns
│   ├── Evaluate mitigation effectiveness (does it reduce risk to acceptable level?)
│   ├── Assess implementation feasibility and cost
│   └── Assign responsible team and target completion date
├── Document mitigation plan
└── Review with DPO for risk acceptance of residual risks

Step 6: Validation and Documentation
├── Verify mitigations are correctly implemented
├── Re-assess residual risk after mitigation
├── Update DFD to reflect implemented controls
├── Generate LINDDUN assessment report
├── File report as part of DPIA documentation (Art. 35)
└── Schedule reassessment (annually or on significant system changes)
```

## Workflow 2: LINDDUN GO (Lightweight Assessment)

```
Step 1: Preparation (30 minutes)
├── Gather: system description, architecture diagram, data flow overview
├── Prepare LINDDUN GO threat type cards (one per LINDDUN category)
├── Assemble assessment team (developer, architect, privacy engineer, DPO)
└── Set time limit: 2-3 hours for the session

Step 2: System Overview (15 minutes)
├── Present system architecture to assessment team
├── Identify the scope boundary (which components are assessed)
├── Identify the primary data flows involving personal data
└── Agree on the data subjects and their expectations

Step 3: Threat Card Walkthrough (90 minutes)
├── For each LINDDUN category card:
│   ├── Read the threat category description
│   ├── Brainstorm: "How could this threat apply to our system?"
│   ├── Document each identified threat on a sticky note or card
│   ├── Quick-score: High/Medium/Low risk
│   └── Note potential mitigations
├── Time-box each category to 10-12 minutes
└── Capture all identified threats in a shared document

Step 4: Prioritization (30 minutes)
├── Group threats by risk level (High/Medium/Low)
├── Discuss and resolve any disagreements on risk levels
├── Select the top 10 threats for detailed mitigation planning
└── Accept Low-risk threats with documentation

Step 5: Action Planning (15 minutes)
├── For each High-risk threat, assign owner and target date
├── For Medium-risk threats, schedule follow-up assessment
├── Document results in the LINDDUN GO assessment report
└── Schedule next assessment (quarterly for actively developed systems)
```
