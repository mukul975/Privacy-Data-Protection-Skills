# Workflows — California Consumer Rights

## Workflow 1: Consumer Request Intake Pipeline

```
START: Request received via web portal / email / toll-free number
  │
  ├─► Step 1: Request Classification
  │     ├─ Parse request type: Know / Delete / Correct / Opt-Out / Limit
  │     ├─ Identify requestor: Consumer or Authorized Agent
  │     ├─ Assign request ID (format: REQ-YYYY-NNNNN)
  │     └─ Log receipt timestamp (Day 0 of 45-day clock)
  │
  ├─► Step 2: Acknowledgment (within 10 business days)
  │     ├─ Send acknowledgment email/letter to consumer
  │     ├─ Include request ID, expected timeline, and contact information
  │     └─ For authorized agent: request authorization documentation
  │
  ├─► Step 3: Identity Verification
  │     ├─ Opt-Out / Limit Sensitive PI: No verification beyond reasonable belief
  │     ├─ Know (categories) / Delete / Correct:
  │     │     ├─ Accountholders: Re-authentication via existing login
  │     │     └─ Non-accountholders: Match 2+ data points via probability-based method
  │     ├─ Know (specific pieces):
  │     │     ├─ Match 3+ data points
  │     │     └─ Obtain signed declaration under penalty of perjury
  │     └─ Verification failure: Deny request, explain, provide resubmission instructions
  │
  ├─► Step 4: Exception Assessment (Delete and Know requests)
  │     ├─ Delete: Review 9 statutory exceptions (§1798.105(d))
  │     │     ├─ Flag data subject to legal hold or tax retention
  │     │     ├─ Flag data needed for active security investigation
  │     │     └─ Document each exception invoked with specific legal basis
  │     └─ Know: No exceptions (but do not disclose SSN, financial accounts in full)
  │
  ├─► Step 5: Fulfillment Execution
  │     ├─ Know: Generate report (PDF + JSON), apply 12-month lookback
  │     ├─ Delete: Execute cascading deletion, notify SPs/contractors
  │     ├─ Correct: Update records, propagate to downstream systems
  │     ├─ Opt-Out: Set opt-out flag, suppress sale/sharing within 15 business days
  │     └─ Limit: Restrict sensitive PI to permitted purposes
  │
  ├─► Step 6: Response Delivery
  │     ├─ Deliver via secure channel (encrypted email, secure portal download)
  │     ├─ For denied/partial requests: cite specific statutory exception
  │     └─ Include consumer's right to appeal/complain to CPPA
  │
  └─► Step 7: Record and Metrics
        ├─ Log completion date, disposition, response days
        ├─ Update annual metrics dashboard (CPPA Regs §7101)
        └─ Retain request records for 24 months
```

## Workflow 2: GPC Opt-Out Signal Processing

```
START: HTTP request arrives at Liberty Commerce Inc. server
  │
  ├─► Step 1: Signal Detection Layer
  │     ├─ Check HTTP header: Sec-GPC: 1
  │     ├─ Check JavaScript: navigator.globalPrivacyControl === true
  │     └─ If no GPC signal detected → proceed to normal processing
  │
  ├─► Step 2: Consumer Identification
  │     ├─ Authenticated user (logged in):
  │     │     ├─ Associate opt-out with consumer account
  │     │     ├─ Set persistent opt-out flag: sale_sharing_opt_out = true
  │     │     └─ Override any prior opt-in for sale/sharing
  │     └─ Unauthenticated user:
  │           ├─ Apply session-level opt-out to browser/device
  │           ├─ Set first-party cookie: gpc_opt_out=1 (session duration)
  │           └─ Do NOT display interstitial or pop-up asking to validate
  │
  ├─► Step 3: Real-Time Enforcement
  │     ├─ Suppress third-party advertising tags before page render:
  │     │     ├─ AdReach Network pixel — BLOCKED
  │     │     ├─ TargetAds retargeting tag — BLOCKED
  │     │     ├─ BidStream header bidding — BLOCKED
  │     │     └─ Social media sharing widgets with tracking — BLOCKED
  │     ├─ Allow first-party analytics (Google Analytics with SP agreement)
  │     ├─ Allow essential cookies (session, cart, security)
  │     └─ Update server-side data sharing pipeline flags
  │
  ├─► Step 4: Conflict Resolution (§7025(f))
  │     ├─ If authenticated user previously opted IN to sale/sharing:
  │     │     ├─ GPC signal takes precedence as most recent expression
  │     │     └─ Update account opt-out status
  │     └─ If authenticated user previously opted OUT:
  │           └─ No action needed — opt-out already applied
  │
  └─► Step 5: Compliance Logging
        ├─ Log: timestamp, session_id, GPC signal value, consumer_id (if auth)
        ├─ Log: actions taken (tags blocked, flags set)
        └─ Retain for compliance audit purposes (24 months)
```

## Workflow 3: Authorized Agent Request Processing

```
START: Request received from entity claiming authorized agent status
  │
  ├─► Step 1: Classify Authorization Type
  │     ├─ Option A: Signed written permission from consumer
  │     └─ Option B: Valid power of attorney (Cal. Prob. Code §§4000-4465)
  │
  ├─► Step 2: Verify Authorization
  │     ├─ If signed written permission:
  │     │     ├─ Verify permission document is signed by the consumer
  │     │     ├─ Verify document identifies the agent and specifies scope
  │     │     ├─ Verify document is dated and not expired
  │     │     ├─ Contact consumer directly to confirm authorization
  │     │     └─ May also verify consumer's identity per standard verification
  │     └─ If power of attorney:
  │           ├─ Verify POA document validity under California law
  │           ├─ Verify scope includes privacy rights requests
  │           └─ No additional consumer verification required
  │
  ├─► Step 3: Process Request
  │     ├─ If authorization verified: process as standard consumer request
  │     └─ If authorization not verified:
  │           ├─ Notify agent of deficiency
  │           ├─ Provide 15 business days to cure
  │           └─ Deny if not cured within 15 business days
  │
  └─► Step 4: Response Delivery
        ├─ Deliver response to authorized agent (as designated by consumer)
        └─ Send copy of response to consumer directly (for transparency)
```

## Workflow 4: Deletion Exception Handling

```
START: Deletion request verified — proceed to exception assessment
  │
  ├─► Step 1: Legal Hold Check
  │     ├─ Query legal hold database for consumer identifier
  │     ├─ If active hold: RETAIN data subject to hold
  │     │     ├─ Document: hold name, issuing authority, date, scope
  │     │     └─ Exception: §1798.105(d)(8) — legal obligation
  │     └─ If no hold: proceed
  │
  ├─► Step 2: Tax and Financial Records Check
  │     ├─ Query transaction records for consumer
  │     ├─ If records within retention period (7 years per 26 U.S.C. §6001):
  │     │     ├─ RETAIN transaction records, receipts, financial data
  │     │     ├─ DELETE all non-financial PI (browsing history, preferences)
  │     │     └─ Exception: §1798.105(d)(8) — legal obligation
  │     └─ If records past retention period: proceed to delete
  │
  ├─► Step 3: Active Security Investigation Check
  │     ├─ Query fraud/security investigation database
  │     ├─ If active investigation involving consumer:
  │     │     ├─ RETAIN relevant evidence data
  │     │     └─ Exception: §1798.105(d)(2) — security/fraud
  │     └─ If no investigation: proceed to delete
  │
  ├─► Step 4: Pending Transaction Check
  │     ├─ Query open orders, returns, warranty claims
  │     ├─ If pending transaction:
  │     │     ├─ RETAIN data needed to complete transaction
  │     │     └─ Exception: §1798.105(d)(1) — transaction completion
  │     └─ If no pending transactions: proceed to delete
  │
  ├─► Step 5: Execute Partial or Full Deletion
  │     ├─ DELETE all PI not subject to an exception
  │     ├─ RETAIN only PI covered by documented exceptions
  │     └─ Segregate retained PI — restrict to exception purpose only
  │
  └─► Step 6: Consumer Notification
        ├─ Inform consumer which PI was deleted
        ├─ Inform consumer which PI was retained and specific exception
        ├─ Provide estimated retention duration for retained PI
        └─ Inform consumer of right to file complaint with CPPA
```
