# Workflows — Colorado Privacy Act

## Workflow 1: Universal Opt-Out Signal Processing

```
START: HTTP request received from Colorado consumer
  │
  ├─► Step 1: Signal Detection
  │     ├─ Check HTTP header: Sec-GPC: 1
  │     ├─ Check JavaScript: navigator.globalPrivacyControl === true
  │     └─ If no signal → proceed to normal processing
  │
  ├─► Step 2: Validate Mechanism
  │     ├─ Confirm mechanism is on AG-recognized list (4 CCR 904-3 Rule 5.14)
  │     ├─ GPC is a recognized mechanism as of July 1, 2024
  │     └─ If unrecognized mechanism → log and monitor for AG biennial update
  │
  ├─► Step 3: Apply Opt-Out
  │     ├─ Scope: Targeted advertising + sale of personal data
  │     ├─ Does NOT automatically apply to profiling (separate mechanism needed)
  │     ├─ Authenticated consumer:
  │     │     ├─ Associate opt-out with account
  │     │     └─ Set persistent preferences: targeted_ads=opt_out, sale=opt_out
  │     ├─ Unauthenticated consumer:
  │     │     ├─ Apply to browser/device session
  │     │     └─ Set session cookie: co_opt_out=targeted_ads,sale
  │     └─ Do NOT display pop-up or interstitial (Rule 5.11)
  │
  ├─► Step 4: Tag Management Enforcement
  │     ├─ Suppress AdReach Network pixel
  │     ├─ Suppress cross-context behavioral advertising tags
  │     ├─ Block data sharing with third-party ad partners
  │     ├─ Allow first-party analytics (under processor agreement)
  │     └─ Allow essential functionality cookies
  │
  └─► Step 5: Logging
        ├─ Log: signal detected, mechanism type, consumer_id (if auth), actions taken
        └─ Retain for compliance audit (3 years per Rule 7.04 analogy)
```

## Workflow 2: Consumer Rights Request with Appeal

```
START: Colorado consumer submits privacy request
  │
  ├─► Step 1: Request Classification
  │     ├─ Access / Correct / Delete / Portability / Opt-Out
  │     └─ Assign ticket: CO-REQ-YYYY-NNNNN
  │
  ├─► Step 2: Authentication (commercially reasonable, per Rule 3.02)
  │     ├─ Account holders: re-authentication
  │     ├─ Non-account holders: probability-based matching
  │     └─ Ensure method is accessible to consumers with disabilities (Rule 3.01)
  │
  ├─► Step 3: Process Request (within 45 days, §6-1-1307(1))
  │     ├─ Extension: up to 45 additional days with notice and reason
  │     ├─ Free response at least once per 12 months per right
  │     └─ Execute per right type
  │
  ├─► Step 4: Response
  │     ├─ Fulfill request OR deny with specific basis
  │     ├─ Inform consumer of right to appeal
  │     └─ Provide appeal instructions
  │
  ├─► Step 5: Appeal (if consumer appeals denial, §6-1-1307(3))
  │     ├─ Consumer submits written appeal
  │     ├─ Controller must respond within 45 days
  │     ├─ If appeal upheld: process the original request
  │     └─ If appeal denied:
  │           ├─ Inform consumer of right to contact Colorado AG
  │           └─ Provide AG contact: coag.gov/office-sections/consumer-protection
  │
  └─► Step 6: Metrics
        └─ Log request and appeal data for compliance records
```

## Workflow 3: Sensitive Data Consent Under Colorado Rules

```
TRIGGER: Processing activity requires sensitive data from Colorado consumer
  │
  ├─► Step 1: Classify Sensitive Data (§6-1-1304(26))
  │     ├─ Racial/ethnic origin
  │     ├─ Religious beliefs
  │     ├─ Mental/physical health condition or diagnosis
  │     ├─ Sex life or sexual orientation
  │     ├─ Citizenship or citizenship status
  │     ├─ Genetic or biometric data for identification
  │     └─ Known child's personal data
  │
  ├─► Step 2: Design Consent Per AG Rules (Rule 6)
  │     ├─ Separate consent for each category and purpose (Rule 6.02)
  │     ├─ Freely given, specific, informed, unambiguous (Rule 6.01)
  │     ├─ Clear affirmative action (unticked checkbox)
  │     ├─ Disclose: category, purpose, recipients, withdrawal right
  │     └─ For children: obtain parent/guardian consent (Rule 6.04)
  │
  ├─► Step 3: Record Consent
  │     ├─ Consumer ID, category, purpose, timestamp
  │     ├─ Consent text version, mechanism
  │     └─ Store in consent management system
  │
  ├─► Step 4: Process Within Consent Scope
  │     ├─ Only for consented purpose
  │     ├─ Apply data minimization (§6-1-1308(3))
  │     └─ Apply retention limits
  │
  └─► Step 5: Withdrawal
        ├─ Consumer may withdraw at any time (Rule 6.03)
        ├─ Withdrawal must be as easy as granting consent
        └─ Upon withdrawal: cease processing, delete if no other basis
```
