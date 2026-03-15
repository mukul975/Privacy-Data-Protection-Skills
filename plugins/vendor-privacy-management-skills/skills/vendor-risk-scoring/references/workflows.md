# Workflows — Vendor Risk Scoring

## Workflow 1: Initial Vendor Risk Scoring

```
TRIGGER: New vendor due diligence completed; vendor approved for engagement
  │
  ├─► Step 1: Gather Scoring Inputs (Privacy Team — 2 business days)
  │     ├─ From due diligence assessment:
  │     │     ├─ Data categories and sensitivity levels
  │     │     ├─ Data subject count (approximate)
  │     │     ├─ Processing locations
  │     │     ├─ Certifications verified
  │     │     ├─ Breach/enforcement history findings
  │     │     └─ Control maturity assessment
  │     ├─ From DPA:
  │     │     ├─ Processing scope and purpose
  │     │     ├─ Sub-processor chain
  │     │     └─ Transfer mechanisms
  │     └─ From business unit:
  │           └─ Processing autonomy level
  │
  ├─► Step 2: Score Each Dimension (Privacy Team — 1 business day)
  │     ├─ D1: Data Volume — score 1-5 per criteria
  │     ├─ D2: Data Sensitivity — score 1-5 per criteria
  │     ├─ D3: Transfer Locations — score 1-5 per criteria
  │     ├─ D4: Certifications — score 1-5 (inverse) per criteria
  │     ├─ D5: Breach History — score 1-5 per criteria
  │     ├─ D6: Control Maturity — score 1-5 per criteria
  │     ├─ D7: Processing Autonomy — score 1-5 per criteria
  │     └─ Document justification for each score
  │
  ├─► Step 3: Calculate Weighted Score
  │     ├─ Apply dimension weights
  │     ├─ Sum to produce Weighted Risk Score
  │     └─ Assign Risk Tier (1/2/3)
  │
  ├─► Step 4: Review and Approval (Privacy Team Lead — 1 business day)
  │     ├─ Review scoring against supporting evidence
  │     ├─ Verify tier assignment is appropriate
  │     ├─ Override if warranted (document rationale)
  │     └─ Approve risk classification
  │
  └─► Step 5: Record and Configure Oversight
        ├─ Record risk score and tier in vendor register
        ├─ Configure tier-based oversight schedule:
        │     ├─ Audit type and frequency
        │     ├─ Monitoring cadence
        │     └─ Reassessment date
        ├─ Notify business unit of vendor risk tier
        └─ Add to aggregated risk dashboard
```

## Workflow 2: Periodic Risk Score Recalculation

```
TRIGGER: Scheduled recalculation date (semi-annual for Tier 1, annual for Tier 2/3)
  │
  ├─► Step 1: Update Scoring Inputs
  │     ├─ Refresh data volume estimates from business unit
  │     ├─ Verify current certifications (check for lapses or scope changes)
  │     ├─ Review breach/enforcement history for new events
  │     ├─ Check for processing location changes
  │     ├─ Collect latest audit findings
  │     └─ Assess any changes in processing scope
  │
  ├─► Step 2: Re-Score Dimensions
  │     ├─ Score each dimension with updated inputs
  │     ├─ Document changes from previous scoring
  │     └─ Calculate updated Weighted Risk Score
  │
  ├─► Step 3: Assess Tier Change
  │     ├─ Compare new score against previous score
  │     ├─ If tier change:
  │     │     ├─ Escalation: Automatically apply higher oversight level
  │     │     └─ De-escalation: Requires DPO approval + clean audit history
  │     └─ Document tier decision
  │
  └─► Step 4: Update Records
        ├─ Update vendor register with new score and tier
        ├─ Adjust oversight schedule if tier changed
        ├─ Update aggregated risk dashboard
        └─ Notify stakeholders of tier changes
```

## Workflow 3: Trigger-Based Risk Escalation

```
TRIGGER: Escalation event detected for a vendor
  ├─ Personal data breach reported
  ├─ Regulatory enforcement action published
  ├─ Certification expired or scope narrowed
  ├─ Material service change without notification
  ├─ Critical audit findings
  │
  ├─► Step 1: Automatic Temporary Escalation
  │     ├─ Increase vendor tier by one level immediately
  │     ├─ Apply higher oversight requirements
  │     ├─ Record escalation trigger and date
  │     └─ Notify DPO and business unit
  │
  ├─► Step 2: Expedited Reassessment (within 30 days)
  │     ├─ Conduct focused risk scoring update
  │     ├─ Assess impact of triggering event on each dimension
  │     └─ Calculate updated Weighted Risk Score
  │
  ├─► Step 3: Confirm or Adjust Tier
  │     ├─ If reassessment confirms elevated risk: Maintain escalated tier
  │     ├─ If triggering event adequately remediated: May return to previous tier
  │     └─ DPO approval required for any de-escalation after trigger event
  │
  └─► Step 4: Document and Track
        ├─ Update vendor register
        ├─ Track escalation in vendor risk history
        └─ Set enhanced monitoring until next scheduled reassessment
```
