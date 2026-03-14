# Workflows — Vendor Monitoring Program

## Workflow 1: Annual Monitoring Cycle

```
TRIGGER: Annual planning cycle (January)
  │
  ├─► Step 1: Plan Annual Monitoring Calendar
  │     ├─ Generate list of all vendors with assigned monitoring activities
  │     ├─ Schedule per tier: reassessments, audits, reviews
  │     ├─ Assign responsible team members
  │     ├─ Budget allocation for audit activities
  │     └─ DPO approval of annual monitoring plan
  │
  ├─► Step 2: Monthly Execution
  │     ├─ Execute scheduled monitoring activities for the month
  │     ├─ Process continuous monitoring alerts
  │     ├─ Track completions against plan
  │     └─ Report monthly status
  │
  ├─► Step 3: Quarterly Review
  │     ├─ Review KPIs against targets
  │     ├─ Assess vendor risk score trends
  │     ├─ Review monitoring signal effectiveness
  │     ├─ Adjust plan if needed (new vendors, changed risks)
  │     └─ Produce quarterly DPO report
  │
  └─► Step 4: Year-End Summary
        ├─ Compile annual program metrics
        ├─ Assess program effectiveness
        ├─ Identify improvements for next year
        └─ Present to senior management
```

## Workflow 2: Monitoring Signal Alert Response

```
TRIGGER: Automated monitoring signal alert received
  │
  ├─► Step 1: Triage (Privacy Team — 4 hours)
  │     ├─ Review alert details and source
  │     ├─ Verify alert is valid (not false positive)
  │     ├─ Classify severity: Critical / High / Medium / Low
  │     └─ Assign to team member for investigation
  │
  ├─► Step 2: Investigation (varies by severity)
  │     ├─ Critical (vendor breach, enforcement action):
  │     │     ├─ Activate breach cascade protocol if applicable
  │     │     ├─ Contact vendor immediately
  │     │     └─ Brief DPO within 4 hours
  │     ├─ High (certification lapse, score drop):
  │     │     ├─ Contact vendor within 1 business day
  │     │     ├─ Request explanation and remediation plan
  │     │     └─ Brief Privacy Team Lead
  │     ├─ Medium (sub-processor change, minor score change):
  │     │     ├─ Investigate within 5 business days
  │     │     └─ Update vendor records
  │     └─ Low (informational):
  │           └─ Note for next scheduled review
  │
  └─► Step 3: Resolution
        ├─ Document investigation findings
        ├─ Update vendor risk score if warranted
        ├─ Trigger reassessment if significant issue identified
        └─ Close alert with documented resolution
```

## Workflow 3: Contract Renewal Privacy Gate

```
TRIGGER: Contract renewal approaching (120 days for Tier 1, 90 days for Tier 2/3)
  │
  ├─► Step 1: Privacy Compliance Status Review
  │     ├─ Current risk score and tier
  │     ├─ Last reassessment date and outcome
  │     ├─ Open audit findings
  │     ├─ Breach history (rolling 12 months)
  │     ├─ Sub-processor compliance status
  │     └─ Certification currency
  │
  ├─► Step 2: Renewal Privacy Assessment
  │     ├─ If reassessment overdue: Complete reassessment before renewal
  │     ├─ If material changes since last assessment: Conduct focused review
  │     ├─ If no changes and recent clean assessment: Abbreviated review
  │     └─ Review DPA for any needed updates
  │
  ├─► Step 3: Renewal Recommendation
  │     ├─ RENEW: Fully compliant, clean record
  │     ├─ RENEW WITH CONDITIONS: Minor issues, conditions for continued engagement
  │     ├─ DO NOT RENEW: Significant non-compliance or unacceptable risk
  │     └─ Document recommendation with rationale
  │
  └─► Step 4: Execution
        ├─ If renewing: Execute any required DPA amendments
        ├─ If not renewing: Initiate vendor termination data workflow
        └─ Update vendor register and monitoring schedule
```
