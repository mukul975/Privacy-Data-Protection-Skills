# Workflows — US State Privacy Law Tracker

## Workflow 1: Legislative Monitoring and Tracker Maintenance

```
TRIGGER: New state legislative session opens OR new privacy bill introduced
  │
  ├─► Phase 1: Bill Identification
  │     ├─ Step 1.1: Monitor NCSL privacy legislation database weekly
  │     ├─ Step 1.2: Monitor IAPP state law tracker for updates
  │     ├─ Step 1.3: Subscribe to state legislature bill alert services
  │     │     for states with active privacy legislation
  │     ├─ Step 1.4: Track committee hearing schedules for pending bills
  │     └─ Step 1.5: Flag bills that have passed at least one chamber
  │
  ├─► Phase 2: Bill Analysis
  │     ├─ Step 2.1: Classify bill type:
  │     │     ├─ Comprehensive consumer privacy
  │     │     ├─ Sector-specific (health, children, biometric, employee)
  │     │     ├─ Amendment to existing law
  │     │     └─ Data breach notification modification
  │     │
  │     ├─ Step 2.2: Extract key provisions:
  │     │     ├─ Applicability thresholds (revenue, consumer volume, data sales)
  │     │     ├─ Consumer rights granted
  │     │     ├─ Controller/processor obligations
  │     │     ├─ Sensitive data definition and protections
  │     │     ├─ Enforcement mechanism (AG only, private right of action)
  │     │     ├─ Cure period (duration, sunset, AG discretion)
  │     │     ├─ Universal opt-out requirement
  │     │     ├─ Exemptions (GLBA, HIPAA, non-profits, small business)
  │     │     └─ Proposed effective date
  │     │
  │     └─ Step 2.3: Compare against existing law matrix to identify
  │           unique or novel provisions
  │
  ├─► Phase 3: Tracker Update
  │     ├─ Step 3.1: Update state law status (introduced / committee / passed chamber /
  │     │     enacted / signed / effective)
  │     ├─ Step 3.2: Update comparison matrices for new provisions
  │     ├─ Step 3.3: Flag compliance impact assessment needed for enacted laws
  │     └─ Step 3.4: Distribute update notification to compliance team
  │
  └─► Phase 4: Regulatory Monitoring (for enacted laws)
        ├─ Step 4.1: Track rulemaking proceedings by state AGs and agencies
        ├─ Step 4.2: Monitor AG enforcement actions and guidance
        ├─ Step 4.3: Track cure period expirations
        └─ Step 4.4: Monitor universal opt-out mechanism deadlines
```

## Workflow 2: New Enacted Law Impact Assessment

```
TRIGGER: Governor signs comprehensive state privacy bill into law
  │
  ├─► Step 1: Applicability Determination
  │     ├─ Does the organisation conduct business in the state?
  │     ├─ Does the organisation meet the consumer volume threshold?
  │     ├─ Does the organisation meet the revenue or data sales threshold?
  │     ├─ Do any entity-level exemptions apply (non-profit, GLBA, HIPAA)?
  │     └─ Do any data-level exemptions apply (employee, B2B, publicly available)?
  │
  ├─► Step 2: Gap Analysis Against Existing Compliance Programme
  │     ├─ Identify rights not already supported by current programme
  │     ├─ Identify obligations that differ from currently implemented states
  │     ├─ Assess sensitive data definition differences
  │     ├─ Evaluate opt-out mechanism requirements
  │     ├─ Determine if DPIA or risk assessment is newly required
  │     └─ Review data processing agreement requirements for processors
  │
  ├─► Step 3: Implementation Planning
  │     ├─ Calculate time to effective date
  │     ├─ Assign implementation tasks with deadlines
  │     ├─ Prioritise by risk:
  │     │     ├─ Consumer-facing rights and requests (highest)
  │     │     ├─ Privacy notice updates
  │     │     ├─ Opt-out mechanisms and consent management
  │     │     ├─ Processor agreement amendments
  │     │     └─ Internal policy and training updates
  │     └─ Estimate implementation budget and resource needs
  │
  ├─► Step 4: Implementation
  │     ├─ Update privacy notices with state-specific disclosures
  │     ├─ Configure consumer request intake for new rights
  │     ├─ Implement or extend universal opt-out signal recognition
  │     ├─ Update processor/vendor agreements
  │     ├─ Conduct DPIAs where required by new law
  │     └─ Train customer service and privacy team on new requirements
  │
  └─► Step 5: Validation and Go-Live
        ├─ Test consumer request workflows end-to-end
        ├─ Verify privacy notice accuracy for new state
        ├─ Confirm opt-out mechanism compliance
        ├─ Document compliance readiness
        └─ Schedule first compliance review after effective date
```

## Workflow 3: Multi-State Enforcement Action Response

```
TRIGGER: AG from any state initiates inquiry, CID, or enforcement action
  │
  ├─► Step 1: Identify Applicable Law and Requirements
  │     ├─ Determine which state law is at issue
  │     ├─ Review cure period availability (if any)
  │     ├─ Identify maximum penalties and enforcement powers
  │     └─ Engage state-specific outside counsel
  │
  ├─► Step 2: Cross-State Impact Assessment
  │     ├─ Determine if the alleged violation also exists under other state laws
  │     ├─ Assess whether remediation in one state addresses issues in others
  │     ├─ Evaluate risk of coordinated multi-AG enforcement
  │     └─ Review prior AG enforcement patterns in this state
  │
  ├─► Step 3: Response and Remediation
  │     ├─ Respond to AG inquiry within specified timeframe
  │     ├─ Invoke cure period if available and appropriate
  │     ├─ Implement remediation across all applicable states (not just enforcing state)
  │     └─ Document remediation evidence for AG submission
  │
  └─► Step 4: Programme Update
        ├─ Update tracker with enforcement precedent
        ├─ Revise compliance programme based on AG interpretation
        ├─ Communicate lessons learned to compliance team
        └─ Schedule enhanced monitoring for enforcement-active states
```
