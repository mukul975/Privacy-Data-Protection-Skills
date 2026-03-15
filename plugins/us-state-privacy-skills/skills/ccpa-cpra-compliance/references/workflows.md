# Workflows — CCPA/CPRA Compliance

## Workflow 1: Consumer Request Intake and Processing

```
START: Consumer submits privacy request via Liberty Commerce Inc. portal
  │
  ├─► Step 1: Request Classification
  │     ├─ Right to Know (categories or specific pieces)
  │     ├─ Right to Delete
  │     ├─ Right to Correct
  │     ├─ Right to Opt-Out of Sale/Sharing
  │     ├─ Right to Limit Sensitive PI Use
  │     └─ Authorized Agent request (requires signed permission or POA)
  │
  ├─► Step 2: Identity Verification (§1798.130, CPPA Regs §7060-7062)
  │     ├─ Opt-out requests: No verification required beyond reasonable belief
  │     ├─ Know (categories): Match at least TWO data points
  │     ├─ Know (specific pieces): Match at least THREE data points
  │     ├─ Delete: Match at least TWO data points
  │     ├─ Correct: Match at least TWO data points
  │     └─ If cannot verify → deny request with explanation
  │
  ├─► Step 3: Request Processing
  │     ├─ Log request receipt date (Day 0 of 45-day clock)
  │     ├─ Send acknowledgment to consumer within 10 business days
  │     ├─ Assign to privacy operations analyst
  │     └─ If extension needed: notify consumer within 45 days with reason
  │
  ├─► Step 4: Fulfillment
  │     ├─ Know: Generate disclosure report (JSON + PDF)
  │     ├─ Delete: Execute cascading deletion across all systems
  │     │     ├─ Core database
  │     │     ├─ Service providers (payment, shipping, analytics)
  │     │     ├─ Contractors
  │     │     ├─ Backups (mark for deletion at next rotation)
  │     │     └─ Document retained data with legal basis
  │     ├─ Correct: Update records, verify propagation
  │     ├─ Opt-out: Apply opt-out flag, cease sale/sharing within 15 business days
  │     └─ Limit sensitive PI: Restrict processing to permitted purposes
  │
  ├─► Step 5: Response Delivery
  │     ├─ Deliver response to consumer via secure portal
  │     ├─ For specific pieces: delivered in machine-readable format
  │     └─ Record completion date and response details
  │
  └─► Step 6: Metrics Logging
        ├─ Request type, receipt date, completion date, days to respond
        ├─ Disposition: fulfilled, partially fulfilled, denied (with reason)
        └─ Aggregate for annual metrics report per CPPA Regs §7101
```

## Workflow 2: GPC Signal Processing

```
START: HTTP request received with Sec-GPC: 1 header
  │
  ├─► Step 1: Signal Detection
  │     ├─ Check HTTP header: Sec-GPC: 1
  │     ├─ Check JavaScript API: navigator.globalPrivacyControl === true
  │     └─ Log signal detection timestamp and session ID
  │
  ├─► Step 2: Determine Consumer Identity
  │     ├─ If authenticated: Associate GPC opt-out with consumer account
  │     │     └─ Set persistent opt-out flag in consumer profile
  │     └─ If unauthenticated: Apply session-level opt-out
  │           └─ Suppress all sale/sharing for the browsing session
  │
  ├─► Step 3: Apply Opt-Out
  │     ├─ Suppress third-party advertising tags/pixels
  │     ├─ Suppress cross-context behavioral advertising data sharing
  │     ├─ Allow first-party analytics (not a sale/sharing)
  │     ├─ Allow service provider processing under written contract
  │     └─ Update consent management platform state
  │
  ├─► Step 4: Confirmation
  │     ├─ Display opt-out confirmation banner (optional, recommended)
  │     └─ Log opt-out application for compliance records
  │
  └─► NOTE: Per CPPA Regulations §7025(c), business may not require
        the consumer to verify their identity for opt-out preference signals.
        The signal itself constitutes a valid opt-out request.
```

## Workflow 3: Annual Privacy Notice Review

```
TRIGGER: January 1 each year OR material change in data practices
  │
  ├─► Step 1: Data Practice Inventory
  │     ├─ Review all PI categories collected in preceding 12 months
  │     ├─ Review all sensitive PI categories collected
  │     ├─ Identify any new categories added since last review
  │     └─ Map purposes for each category
  │
  ├─► Step 2: Third-Party and Sharing Review
  │     ├─ Identify all categories of PI sold in preceding 12 months
  │     ├─ Identify all categories of PI shared for cross-context behavioral advertising
  │     ├─ Review service provider and contractor agreements
  │     └─ Identify any new third-party disclosures
  │
  ├─► Step 3: Retention Schedule Review
  │     ├─ Verify retention periods for each PI category
  │     ├─ Update retention criteria if business needs have changed
  │     └─ Ensure privacy notice reflects actual retention practices
  │
  ├─► Step 4: Draft Updated Notice
  │     ├─ Update categories, purposes, retention periods
  │     ├─ Update sale/sharing disclosures
  │     ├─ Review consumer request submission instructions
  │     ├─ Update metrics (if 10M+ consumers processed)
  │     └─ Legal review and approval
  │
  ├─► Step 5: Publish
  │     ├─ Post updated notice at privacy.libertycommerce.com/california
  │     ├─ Update "last updated" date
  │     ├─ Archive prior version
  │     └─ Notify consumers of material changes (if applicable)
  │
  └─► Step 6: Documentation
        ├─ Record review date, participants, changes made
        └─ Schedule next annual review
```

## Workflow 4: Data Processing Agreement Lifecycle

```
TRIGGER: New service provider/contractor engagement OR contract renewal
  │
  ├─► Step 1: Classify Recipient
  │     ├─ Service Provider (§1798.140(ag)): processes PI on behalf of business
  │     ├─ Contractor (§1798.140(j)): receives PI from business under contract
  │     └─ Third Party (§1798.140(ai)): receives PI not as SP or contractor
  │
  ├─► Step 2: Draft Agreement (§1798.100(d))
  │     ├─ Specify business purpose for PI disclosure
  │     ├─ Prohibit selling or sharing the PI
  │     ├─ Prohibit use beyond specified business purpose
  │     ├─ Require compliance with CCPA/CPRA obligations
  │     ├─ Require notification if recipient cannot meet obligations
  │     ├─ Grant right to take reasonable steps to ensure compliance
  │     ├─ For contractors: require certification of understanding
  │     ├─ For contractors: grant audit rights
  │     └─ Include subcontractor flow-down requirements
  │
  ├─► Step 3: Legal Review and Execution
  │     ├─ Privacy team review of data flow and purpose limitation
  │     ├─ Legal counsel review of contractual terms
  │     └─ Execute agreement before PI is disclosed
  │
  ├─► Step 4: Ongoing Monitoring
  │     ├─ Annual review of agreement compliance
  │     ├─ Process consumer deletion requests through SP/contractor
  │     └─ Respond to recipient notification of inability to comply
  │
  └─► Step 5: Termination (if needed)
        ├─ Require return or deletion of PI
        ├─ Obtain certification of deletion
        └─ Update data inventory to reflect terminated relationship
```
