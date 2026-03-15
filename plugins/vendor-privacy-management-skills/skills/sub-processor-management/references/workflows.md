# Workflows — Sub-Processor Management

## Workflow 1: Sub-Processor Change Notification (General Authorization)

```
TRIGGER: Processor sends notification of intended sub-processor addition/replacement
  │
  ├─► Step 1: Receive and Log Notification (Privacy Team — 1 business day)
  │     ├─ Log notification in sub-processor tracking system
  │     ├─ Record: notification date, proposed engagement date, sub-processor details
  │     ├─ Start objection period countdown (30 calendar days from receipt)
  │     └─ Acknowledge receipt to processor
  │
  ├─► Step 2: Initial Review (Privacy Team — 3 business days)
  │     ├─ Review sub-processor details:
  │     │     ├─ Legal entity name and jurisdiction
  │     │     ├─ Processing location(s)
  │     │     ├─ Processing function and data access scope
  │     │     ├─ Transfer mechanism (if outside EEA)
  │     │     └─ Security certifications
  │     ├─ Check against known risk factors:
  │     │     ├─ Jurisdiction risk (third country without adequacy)
  │     │     ├─ Previous enforcement actions
  │     │     ├─ Breach history
  │     │     └─ Certification gaps
  │     └─ Classify: No Concern / Review Required / Objection Likely
  │
  ├─► Step 3: Detailed Assessment (if Review Required — 10 business days)
  │     ├─ Request additional information from processor:
  │     │     ├─ Sub-processor security posture documentation
  │     │     ├─ Draft sub-processor DPA terms
  │     │     ├─ Transfer Impact Assessment (if third-country transfer)
  │     │     └─ Sub-processor's own sub-processor list
  │     ├─ Conduct independent verification:
  │     │     ├─ Verify certifications
  │     │     ├─ Public record search
  │     │     └─ Cross-reference with internal risk intelligence
  │     └─ Produce assessment recommendation
  │
  ├─► Step 4: Decision (DPO or Privacy Team Lead — within objection period)
  │     ├─ Option A: No Objection
  │     │     ├─ Confirm no objection to processor in writing
  │     │     ├─ Update sub-processor register
  │     │     └─ Set review date (aligned with next annual assessment)
  │     │
  │     ├─ Option B: Conditional Approval
  │     │     ├─ Notify processor of conditions (e.g., supplementary measures)
  │     │     ├─ Request confirmation of conditions met before engagement
  │     │     └─ Track condition fulfillment
  │     │
  │     └─ Option C: Objection
  │           ├─ Issue written objection with data protection grounds
  │           ├─ Propose alternatives (different sub-processor, additional safeguards)
  │           ├─ Enter negotiation period (30 calendar days)
  │           └─ If unresolved: escalate to termination decision
  │
  └─► Step 5: Post-Engagement Verification (Privacy Team — within 30 days of engagement)
        ├─ Confirm sub-processor DPA executed with flow-down obligations
        ├─ Verify transfer mechanism in place (if applicable)
        ├─ Update sub-processor register with confirmed details
        └─ Schedule first periodic review
```

## Workflow 2: Sub-Processor Register Reconciliation

```
TRIGGER: Quarterly scheduled reconciliation (Q1, Q2, Q3, Q4)
  │
  ├─► Step 1: Request Current Sub-Processor Lists
  │     ├─ Send standardized request to all Tier 1 processors
  │     ├─ Request: current sub-processor list per DPA Annex III format
  │     ├─ Response deadline: 10 business days
  │     └─ Track responses in reconciliation tracker
  │
  ├─► Step 2: Compare Against Register
  │     ├─ Match processor-provided lists against internal register
  │     ├─ Identify discrepancies:
  │     │     ├─ Sub-processors in processor list but not in register (unauthorized?)
  │     │     ├─ Sub-processors in register but not in processor list (removed without notice?)
  │     │     └─ Changed details (location, function, certification status)
  │     └─ Document all discrepancies
  │
  ├─► Step 3: Investigate Discrepancies
  │     ├─ Contact processor for each discrepancy
  │     ├─ Determine if notification was missed or if register is outdated
  │     ├─ Classify each discrepancy:
  │     │     ├─ Administrative (name change, corporate restructure)
  │     │     ├─ Process failure (notification not sent or received)
  │     │     └─ Compliance breach (sub-processor engaged without authorization)
  │     └─ Document investigation findings
  │
  ├─► Step 4: Remediate
  │     ├─ Administrative: Update register
  │     ├─ Process failure: Require processor to improve notification procedures
  │     ├─ Compliance breach:
  │     │     ├─ Require immediate retrospective notification
  │     │     ├─ Conduct expedited assessment of unauthorized sub-processor
  │     │     ├─ Document DPA breach and controller response
  │     │     └─ Consider contractual remedies if pattern emerges
  │     └─ Update register to reflect reconciled state
  │
  └─► Step 5: Report
        ├─ Produce quarterly reconciliation report
        ├─ Report to DPO with findings and remediation actions
        └─ Track KPIs: notification compliance rate, register accuracy
```

## Workflow 3: Flow-Down DPA Verification

```
TRIGGER: Annual scheduled review or new sub-processor engagement
  │
  ├─► Step 1: Sample Selection
  │     ├─ High-risk sub-processors: Review all sub-processor DPAs
  │     ├─ Standard-risk: Sample 30% of sub-processor DPAs
  │     └─ Document sampling methodology and rationale
  │
  ├─► Step 2: Request Sub-Processor DPA Copies
  │     ├─ Request from processor (per audit rights in DPA)
  │     ├─ Accept redacted versions protecting commercial terms
  │     ├─ Require visibility of all data protection clauses
  │     └─ 15 business day response deadline
  │
  ├─► Step 3: Compliance Comparison
  │     ├─ Compare each flow-down obligation against controller-processor DPA:
  │     │     ├─ Instructions clause: Present and equivalent?
  │     │     ├─ Confidentiality: Present and equivalent?
  │     │     ├─ Security measures: Present and equivalent or stronger?
  │     │     ├─ Further sub-processing: Cascade restriction present?
  │     │     ├─ DSR assistance: Present and equivalent?
  │     │     ├─ Compliance assistance: Present and equivalent?
  │     │     ├─ Deletion/return: Present and equivalent?
  │     │     ├─ Audit rights: Present with controller access path?
  │     │     └─ Breach notification: Equivalent or shorter timeframe?
  │     └─ Score each obligation: Compliant / Partially Compliant / Non-Compliant
  │
  ├─► Step 4: Issue Findings
  │     ├─ Non-compliant: Require processor to amend sub-processor DPA
  │     ├─ Partially compliant: Request remediation plan with timeline
  │     ├─ Compliant: Document and close
  │     └─ Produce Flow-Down Verification Report
  │
  └─► Step 5: Track Remediation
        ├─ Set remediation deadlines per finding severity
        ├─ Follow up at 30/60/90 day intervals
        └─ Escalate persistent non-compliance to DPO
```
