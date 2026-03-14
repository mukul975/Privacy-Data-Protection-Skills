# HIPAA BAA Management — Workflows

## Workflow 1: BAA Requirement Determination

```
New Vendor Relationship Under Consideration
│
├── Step 1: Will the vendor create, receive, maintain, or transmit PHI?
│   ├── NO → No BAA required
│   └── YES → Continue evaluation
│
├── Step 2: Is the vendor a member of the covered entity's workforce?
│   ├── YES → Not a BA (workforce member); no BAA required
│   └── NO → Continue evaluation
│
├── Step 3: Is this a treatment disclosure to another covered entity?
│   ├── YES → Not a BA relationship; no BAA required
│   └── NO → Continue evaluation
│
├── Step 4: Is the vendor a conduit (transient access only)?
│   ├── YES (postal service, ISP, courier) → No BAA required
│   └── NO → BAA IS REQUIRED
│       └── Proceed to BAA execution workflow
│
└── Document determination regardless of outcome
```

## Workflow 2: BAA Lifecycle Management

```
BAA Identified as Required
│
├── Phase 1: Pre-Execution (Before PHI Access)
│   ├── Vendor risk assessment (security questionnaire, SOC 2 review)
│   ├── Legal review of vendor's proposed BAA or negotiation of Asclepius standard BAA
│   ├── Verify all §164.504(e)(2) required provisions are included
│   ├── Obtain authorized signatories
│   └── Execute BAA — NO PHI access before execution
│
├── Phase 2: Active Management
│   ├── Annual security assessment of BA
│   ├── SOC 2 Type II report review
│   ├── Breach incident tracking for BA
│   ├── Subcontractor registry updates from BA
│   └── BAA amendment for scope changes
│
├── Phase 3: Renewal/Amendment
│   ├── Review BAA at MSA renewal
│   ├── Update for regulatory changes (Omnibus Rule, state laws)
│   ├── Verify subcontractor provisions current
│   └── Re-execute if material changes required
│
└── Phase 4: Termination
    ├── Issue termination notice per BAA terms
    ├── Transition plan for PHI return or migration
    ├── BA returns or destroys all PHI within 30 days
    ├── Obtain written certification of destruction (NIST 800-88 compliant)
    ├── If return/destruction infeasible: BA certifies ongoing protection
    └── Update BAA tracking system
```

## Workflow 3: BA Breach Response

```
BA Reports Breach to Covered Entity
│
├── Step 1: Validate BA Notification (within 24 hours of receipt)
│   ├── Was notification within BAA-required timeframe?
│   ├── Does notification include required information?
│   └── If incomplete: request supplemental information from BA
│
├── Step 2: CE Independent Assessment
│   ├── Conduct four-factor risk assessment
│   ├── Determine scope (individuals affected)
│   ├── Assess whether notification is required
│   └── Determine notification obligations (individual, HHS, AG, media)
│
├── Step 3: Notification Execution
│   ├── CE fulfills notification obligations (or delegates to BA per BAA)
│   ├── BA cooperates with investigation
│   └── Cost allocation per BAA terms
│
└── Step 4: Remediation
    ├── BA implements corrective actions
    ├── CE verifies remediation
    ├── If material breach of BAA: evaluate cure or termination
    └── Update BA risk rating and monitoring frequency
```
