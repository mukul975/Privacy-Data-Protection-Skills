# Workflows — Connecticut CTDPA

## Workflow 1: Dark Pattern Consent Audit

```
TRIGGER: New consent interface deployment or quarterly audit
  │
  ├─► Step 1: Identify All Consent Interfaces
  │     ├─ Cookie consent banner
  │     ├─ Sensitive data consent forms
  │     ├─ Marketing opt-in flows
  │     ├─ Account creation consent
  │     └─ Loyalty program enrollment
  │
  ├─► Step 2: Visual Design Audit
  │     ├─ Are "Accept" and "Decline" buttons the same size? (YES required)
  │     ├─ Are both options equally prominent in color/contrast? (YES required)
  │     ├─ Is the decline/reject option visible without scrolling? (YES required)
  │     ├─ Are there artificial countdown timers? (NO required)
  │     └─ Is the close/dismiss button clearly visible? (YES required)
  │
  ├─► Step 3: Language Audit
  │     ├─ Does reject language use guilt/shame? (NO required)
  │     │     Example violation: "No thanks, I don't want to save money"
  │     ├─ Are there double negatives? (NO required)
  │     ├─ Is the language at an appropriate reading level? (YES required)
  │     └─ Are purposes described clearly and specifically? (YES required)
  │
  ├─► Step 4: Behavioral Audit
  │     ├─ Does declining trigger repeated re-prompts? (NO required)
  │     ├─ Does declining degrade service access? (NO required)
  │     ├─ Is consent bundled with unrelated features? (NO required)
  │     └─ Are pre-checked boxes used? (NO required)
  │
  ├─► Step 5: Document Findings
  │     ├─ For each interface: pass/fail per criterion
  │     ├─ Screenshot evidence for violations
  │     └─ Remediation plan with deadlines
  │
  └─► Step 6: Remediation
        ├─ Fix identified dark patterns
        ├─ Re-audit after fixes
        └─ Schedule next quarterly audit
```

## Workflow 2: Consumer Rights Request with Appeal

```
START: Connecticut consumer submits rights request
  │
  ├─► Step 1: Classify and Log
  │     ├─ Assign: CT-REQ-YYYY-NNNNN
  │     ├─ Right type: Access / Correct / Delete / Portability / Opt-Out
  │     └─ Day 0 of 45-day clock
  │
  ├─► Step 2: Authenticate
  │     ├─ Commercially reasonable verification
  │     └─ No new account required
  │
  ├─► Step 3: Process (within 45 days)
  │     ├─ Extension: up to 45 days with notice and reason
  │     └─ At least one free response per 12 months
  │
  ├─► Step 4: Respond
  │     ├─ Fulfill or deny with specific basis
  │     ├─ Inform consumer of right to appeal
  │     └─ Provide appeal instructions
  │
  ├─► Step 5: Appeal Process (§42-520(f))
  │     ├─ Consumer files appeal
  │     ├─ Controller responds within 60 days
  │     ├─ If upheld: process original request
  │     └─ If denied:
  │           ├─ Provide written explanation
  │           ├─ Inform consumer of right to contact Connecticut AG
  │           └─ Provide online complaint mechanism: portal.ct.gov/ag
  │
  └─► Step 6: AG Contact (if consumer escalates)
        ├─ Cooperate with AG investigation
        ├─ Provide records of request and appeal
        └─ Note: 60-day cure period expired January 1, 2025
```

## Workflow 3: Loyalty Program Data Processing

```
TRIGGER: Data processing within Liberty Rewards loyalty program
  │
  ├─► Step 1: Verify Bona Fide Status
  │     ├─ Program provides genuine value to consumer (rewards, discounts)
  │     ├─ Participation is voluntary
  │     ├─ Terms clearly disclose data collection and use
  │     └─ Data used solely for program purposes
  │
  ├─► Step 2: Scope Check
  │     ├─ Purchase history: Used for rewards calculation? → EXEMPT
  │     ├─ Preference data: Used for personalized program offers? → EXEMPT
  │     ├─ Purchase history: Shared with third-party advertisers? → NOT EXEMPT
  │     └─ Preference data: Used for non-program targeted ads? → NOT EXEMPT
  │
  ├─► Step 3: Apply Appropriate Rules
  │     ├─ For exempt processing: Standard loyalty program terms apply
  │     ├─ For non-exempt processing: Full CTDPA rights apply
  │     │     ├─ Consumer can opt out of sale and targeted advertising
  │     │     └─ Consumer can delete non-program-essential data
  │     └─ Document the boundary between exempt and non-exempt processing
  │
  └─► Step 4: Annual Review
        ├─ Verify program still meets bona fide criteria
        ├─ Review data use to ensure no scope creep beyond program purposes
        └─ Update program terms if data practices have changed
```
