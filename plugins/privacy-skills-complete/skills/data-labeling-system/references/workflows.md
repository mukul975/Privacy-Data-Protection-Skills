# Workflows — Data Labelling System

## Workflow 1: Label Configuration and Deployment

```
START: New label required or existing label modification
  │
  ├─► Step 1: Label Design
  │     - Define label name, description, scope, colour, visual marking
  │     - Define encryption settings (Azure RMS configuration)
  │     - Define DLP policy association
  │     - Define auto-labelling conditions (SITs, confidence threshold)
  │     Output: Label specification document
  │
  ├─► Step 2: Approval
  │     - DPO reviews label alignment with classification policy
  │     - CISO reviews encryption and DLP settings
  │     - Privacy Steering Committee approves
  │     Output: Approved label specification
  │
  ├─► Step 3: Configuration
  │     - Create/modify label in Microsoft Purview compliance centre
  │     - Configure auto-labelling policies
  │     - Configure DLP policies linked to the label
  │     - Configure endpoint DLP for the label
  │     Output: Label configured in Purview
  │
  ├─► Step 4: Testing
  │     - Test in pilot group (Privacy Engineering team)
  │     - Verify auto-labelling accuracy on sample documents
  │     - Verify DLP policy enforcement
  │     - Verify label inheritance rules
  │     Output: Test results
  │
  └─► Step 5: Deployment
        - Publish label policy to all users (phased if major change)
        - Communicate change to all employees
        - Monitor adoption metrics for 30 days
        Output: Label deployed and monitored
```

## Workflow 2: Label Override and Downgrade Review

```
START: User requests label downgrade or removal
  │
  ├─► Step 1: Justification Capture
  │     - User enters justification text in label prompt
  │     - System logs: user, document, current label, new label, justification, timestamp
  │
  ├─► Step 2: Automated Review
  │     - For Confidential → Internal or Public: flag for Data Owner review
  │     - For Restricted → any lower: flag for DPO immediate review
  │     - For auto-applied label removal: flag for Privacy Engineering review
  │
  ├─► Step 3: Review Decision
  │     - Reviewer assesses: Is the downgrade justified?
  │     - Is the content actually at a lower sensitivity than the label indicates?
  │     - Was the auto-label a false positive?
  │     - Decision: approve, reject, or investigate
  │
  └─► Step 4: Action
        - Approve: downgrade confirmed; update audit record
        - Reject: original label reinstated; user notified
        - Investigate: possible misclassification; escalate to full review
```
