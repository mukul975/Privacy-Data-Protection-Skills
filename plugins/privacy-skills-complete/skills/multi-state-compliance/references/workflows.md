# Workflows — Multi-State Compliance

## Workflow 1: State-Aware Consumer Request Routing

```
START: Consumer submits privacy request
  │
  ├─► Step 1: Determine Consumer's State
  │     ├─ Check account address
  │     ├─ Check IP geolocation (supplementary)
  │     ├─ Check consumer's self-identification
  │     └─ If ambiguous: apply highest common standard
  │
  ├─► Step 2: Apply Common Baseline (Tier 1)
  │     ├─ Log request with 45-day SLA
  │     ├─ Authenticate using commercially reasonable methods
  │     ├─ Route to privacy operations team
  │     └─ Send acknowledgment
  │
  ├─► Step 3: Apply State-Specific Rules (Tier 3)
  │     ├─ California: CCPA/CPRA verification requirements
  │     │     ├─ Know (specific): 3 data points + declaration
  │     │     ├─ Know (categories): 2 data points
  │     │     └─ Include 12-month lookback + CPRA-specific rights
  │     ├─ Oregon: Include specific third-party list (§646A.578(1)(f))
  │     ├─ Montana: Extension limited to 15 days (not 45)
  │     └─ All others: Standard 45-day + 45-day extension
  │
  ├─► Step 4: Execute Request
  │     ├─ Access: Compile data per state disclosure requirements
  │     ├─ Delete: Cascading deletion with state-specific exceptions
  │     ├─ Correct: Update and propagate
  │     ├─ Portability: Generate export (JSON)
  │     └─ Opt-Out: Apply per state scope
  │
  └─► Step 5: Response
        ├─ Include state-specific appeal rights (non-CA states)
        ├─ Include AG contact information for consumer's state
        └─ Log completion metrics per state
```

## Workflow 2: Multi-State Privacy Notice Update

```
TRIGGER: Annual review or material change in data practices
  │
  ├─► Step 1: Compile Requirements
  │     ├─ List all applicable state privacy notice requirements
  │     ├─ Identify additions since last review (new states)
  │     └─ Map each requirement to a notice section
  │
  ├─► Step 2: Draft Unified Notice
  │     ├─ Include all 17 harmonized sections (see SKILL.md)
  │     ├─ Use layered format: summary table + detailed sections
  │     ├─ State-specific supplements as addenda
  │     └─ Ensure language at Flesch-Kincaid grade 8 or below
  │
  ├─► Step 3: Legal Review
  │     ├─ Review against each state's specific requirements
  │     ├─ Verify retention periods per category (CA requirement)
  │     ├─ Verify targeted advertising disclosure (non-CA states)
  │     └─ Verify universal opt-out disclosure (CA, CO, CT, MT)
  │
  ├─► Step 4: Publish
  │     ├─ Post at privacy.libertycommerce.com/us-privacy
  │     ├─ Update "Last Updated" date
  │     ├─ Archive prior version
  │     └─ Notify consumers of material changes
  │
  └─► Step 5: Ongoing Monitoring
        ├─ Monitor for new state laws and amendments
        ├─ Track AG rulemaking (especially CA CPPA, CO AG)
        └─ Update within 30 days of material changes
```

## Workflow 3: State-by-State Applicability Review

```
TRIGGER: Annual or upon entering new state market
  │
  ├─► Step 1: For Each State
  │     ├─ Count consumers in that state
  │     ├─ Assess revenue thresholds
  │     ├─ Check entity-level exemptions
  │     └─ Document determination
  │
  ├─► Step 2: Activate/Deactivate State Modules
  │     ├─ If newly applicable: activate state-specific module
  │     ├─ If no longer applicable: maintain as best practice
  │     └─ Update privacy notice accordingly
  │
  └─► Step 3: Document and Review
        ├─ Maintain applicability register
        └─ Review quarterly for threshold changes
```
