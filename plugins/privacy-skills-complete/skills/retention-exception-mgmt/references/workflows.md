# Retention Exception Management Workflows

## Workflow 1: Exception Request and Approval

```
[Retention Period Approaching Expiry — Data Owner Identifies Need to Retain]
         │
         ▼
[Submit Retention Exception Request Form]
   - Data identification
   - Exception category
   - Justification (specific, not speculative)
   - Proportionality assessment
   - Supporting documentation
         │
         ▼
[DPO Assessment]
   ├── Necessity test ──► Is the exception genuinely necessary?
   ├── Proportionality test ──► Is the duration proportionate?
   ├── Legal basis check ──► Does a valid basis exist for continued processing?
   └── Risk assessment ──► Risk to data subjects vs. risk of not retaining
         │
         ▼
[DPO Recommendation]
   ├── APPROVE ──► Route to approval authority
   ├── APPROVE WITH CONDITIONS ──► Route with conditions
   ├── APPROVE REDUCED DURATION ──► Route with reduced period
   └── REJECT ──► Notify requestor; proceed with scheduled deletion
         │
         ▼
[Approval Authority Sign-Off]
   (Per approval authority matrix — DPO, Legal, IT Director, Board)
         │
         ▼
[Register Exception]
   - Add to Exception Register
   - Configure technical hold on affected data
   - Suspend automated deletion
   - Set review date
   - Notify relevant stakeholders
```

## Workflow 2: Periodic Exception Review

```
[Review Date Reached]
         │
         ▼
[Retrieve Exception Record]
         │
         ▼
[Reassess Necessity]
   ├── Underlying circumstance still active?
   │     ├── Yes ──► Continue assessment
   │     └── No ──► EXPIRE exception; schedule deletion within 30 days
   │
   ├── Can scope be reduced?
   │     ├── Yes ──► Minimize data; update exception scope
   │     └── No ──► Document justification
   │
   └── Maximum duration reached?
         ├── Yes ──► EXPIRE (escalate if requestor objects)
         └── No ──► RENEW with updated justification
         │
         ▼
[Update Exception Register]
[Notify Requestor of Outcome]
[Set Next Review Date]
```

## Workflow 3: Auto-Expiry Process

```
[Exception Review Date Passes Without Renewal]
         │
         ▼
[14-Day Grace Period — Alert to Requestor and DPO]
         │
         ▼
[Grace Period Expires — No Renewal Submitted]
         │
         ▼
[Auto-Expire Exception]
   - Remove technical hold
   - Re-enable automated deletion
   - Schedule deletion within 30 days
         │
         ▼
[Notify Requestor]
   - Exception expired
   - Data scheduled for deletion on [date]
   - If retention still needed: submit new exception request before deletion date
         │
         ▼
[Execute Deletion on Schedule]
[Update Exception Register — Status: Expired]
```
