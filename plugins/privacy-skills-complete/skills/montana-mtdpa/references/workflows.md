# Workflows — Montana MTDPA

## Workflow 1: Consumer Rights Request (Shorter Extension)

```
START: Montana consumer submits privacy request
  │
  ├─► Step 1: Log and Classify
  │     ├─ Assign: MT-REQ-YYYY-NNNNN
  │     ├─ Right: Access / Correct / Delete / Portability / Opt-Out
  │     └─ Day 0 of 45-day clock
  │
  ├─► Step 2: Authenticate
  │     └─ Commercially reasonable verification
  │
  ├─► Step 3: Process Request
  │     ├─ Standard deadline: 45 days
  │     ├─ Extension: ONLY 15 additional days (total 60)
  │     │     ├─ Note: Most states allow 45-day extension (total 90)
  │     │     └─ Must notify consumer of extension and reason
  │     └─ Free response at least once per 12 months per right
  │
  ├─► Step 4: Respond
  │     ├─ Fulfill or deny with specific basis
  │     └─ Inform of appeal right (60-day appeal response)
  │
  └─► Step 5: Appeal
        ├─ Controller responds within 60 days
        ├─ If denied: inform consumer of right to contact Montana AG
        └─ AG contact: doj.mt.gov
```

## Workflow 2: Universal Opt-Out (Effective October 1, 2025)

```
START: Montana consumer's browser sends GPC signal
  │
  ├─► Step 1: Detect Signal
  │     ├─ Sec-GPC: 1 HTTP header
  │     └─ navigator.globalPrivacyControl === true
  │
  ├─► Step 2: Apply Opt-Out
  │     ├─ Scope: Targeted advertising + sale of personal data
  │     ├─ Authenticated: Account-level persistent opt-out
  │     └─ Unauthenticated: Session/device-level opt-out
  │
  ├─► Step 3: Enforce
  │     ├─ Suppress advertising tags
  │     ├─ Block data sharing with third-party ad partners
  │     └─ Allow first-party analytics
  │
  └─► Step 4: Log
        └─ Record signal detection and actions for compliance
```
