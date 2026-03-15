# Age-Gating Services Workflows

## Workflow 1: Age Gate Type Selection

```
Service requires age-gating implementation
│
├─ Step 1: Classify content/feature risk
│  ├─ Does the service contain age-restricted content (gambling, alcohol, adult)? → HARD GATE
│  ├─ Does the service have social features with strangers? → SOFT GATE (enhanced restrictions)
│  ├─ Does the service have in-app purchases or monetisation? → SOFT GATE (purchase restrictions)
│  ├─ Is the service educational or informational? → SOFT GATE (privacy-focused restrictions)
│  └─ Is the service static content with no interaction? → ADAPTIVE GATE or minimal screening
│
├─ Step 2: Determine age tiers
│  ├─ Under 5: Access denied or parent-managed only
│  ├─ 5-7: Highly restricted (no text input, no social, parent-managed)
│  ├─ 8-12: Restricted (moderated features, parental oversight, no advertising)
│  ├─ 13-15: Standard child protections (AADC-compliant defaults, parental notification)
│  ├─ 16-17: Young adult protections (most features available, high-privacy defaults)
│  └─ 18+: Full access (standard adult experience)
│
├─ Step 3: Select age assurance method
│  ├─ Hard gate → Document-based or facial estimation + liveness
│  ├─ Soft gate → Self-declaration + parental verification (for under-threshold)
│  └─ Adaptive gate → Self-declaration with layered escalation
│
└─ Document gate type, age tiers, and assurance method with rationale.
```

## Workflow 2: Neutral Age Prompt Implementation

```
Implement neutral age prompt for age screening
│
├─ Design requirements:
│  ├─ Prompt text: "Enter your date of birth" or "What year were you born?"
│  ├─ Input method: scrollable date picker
│  ├─ Default: no date selected (blank/empty state)
│  ├─ No threshold displayed or implied
│  ├─ No leading questions ("Are you over 13?")
│  ├─ No immediate feedback on gate outcome
│  └─ Submit button: neutral label ("Continue" or "Next")
│
├─ Processing:
│  ├─ Calculate age from entered DOB and current date
│  ├─ Look up applicable age threshold for user's jurisdiction
│  ├─ Determine routing: above threshold (independent) or below (child flow)
│  └─ Log: hashed DOB, jurisdiction, threshold applied, outcome, timestamp
│
├─ Anti-circumvention:
│  ├─ Set secure cookie on age gate completion (HttpOnly, Secure, SameSite=Strict)
│  ├─ Cookie content: encrypted outcome (not the DOB)
│  ├─ Cookie expiry: 24-72 hours for failed attempts; account duration for successful
│  ├─ If cookie detected on re-visit: enforce previous outcome
│  ├─ If cookies cleared: device fingerprint fallback (canvas, WebGL, screen resolution)
│  ├─ Rate limiting: maximum 3 age gate attempts per device per 24 hours
│  └─ Progressive escalation: after 2 failed attempts, require higher-assurance method
│
└─ Testing:
   ├─ Verify neutral design with UX review
   ├─ Test with children to confirm they cannot infer the threshold
   ├─ Test anti-circumvention measures with attempt-replay scenarios
   └─ Accessibility testing: screen reader compatibility, keyboard navigation
```

## Workflow 3: Soft Gate Feature Restriction

```
User identified as below age threshold (child account)
│
├─ Step 1: Apply age-tier feature restrictions
│  ├─ Look up user's age tier from account data
│  ├─ Load feature restriction matrix for that tier
│  └─ Apply restrictions at the application layer
│
├─ Step 2: Feature-level enforcement
│  ├─ For each restricted feature:
│  │  ├─ UI level: hide or grey out the feature in the interface
│  │  ├─ API level: reject requests for restricted features with appropriate error
│  │  ├─ Data level: do not collect data for restricted purposes
│  │  └─ Communication level: do not send restricted notifications
│  │
│  ├─ For partially restricted features:
│  │  ├─ Apply the modified version (e.g., pre-set messages instead of free text)
│  │  ├─ Apply additional safeguards (moderation, content filtering)
│  │  └─ Log usage for safety monitoring
│  │
│  └─ For unrestricted features:
│     └─ Apply standard child protections (high-privacy defaults, data minimisation)
│
├─ Step 3: User communication
│  ├─ Do NOT tell the user "this feature is blocked because you're under [age]"
│  │  (reveals the threshold)
│  ├─ Instead: "This feature isn't available for your account type"
│  │  or "Ask your parent to enable this from their dashboard"
│  └─ Provide age-appropriate explanation where possible
│
└─ Step 4: Parental override
   ├─ Parent can view restricted features in parental dashboard
   ├─ Parent can enable specific features if they determine it's appropriate
   ├─ Each override requires explicit parental action (not bulk enable)
   └─ Log parental overrides in consent registry
```

## Workflow 4: Re-Verification Trigger Processing

```
Re-verification event detected
│
├─ Identify trigger type:
│  ├─ AGE_TRANSITION: User's birthday moves them to a new age tier
│  ├─ ACCOUNT_RECOVERY: User requests account access restoration
│  ├─ DOB_CHANGE: Request to modify date of birth on account
│  ├─ ANOMALY: Behavioural signals inconsistent with declared age
│  ├─ ANNUAL_REVIEW: Scheduled annual age confirmation
│  └─ FEATURE_REQUEST: User requests access to age-restricted feature
│
├─ Process by trigger type:
│  ├─ AGE_TRANSITION:
│  │  ├─ Confirm new age tier
│  │  ├─ Unlock features for new tier
│  │  ├─ Send notification to child and parent
│  │  ├─ If reaching consent threshold: trigger consent authority transfer
│  │  └─ Update account restrictions
│  │
│  ├─ ACCOUNT_RECOVERY:
│  │  ├─ Verify identity through standard recovery mechanism
│  │  ├─ Re-confirm age before restoring access
│  │  ├─ Notify parent if child account
│  │  └─ Apply current age-tier restrictions
│  │
│  ├─ DOB_CHANGE:
│  │  ├─ Require parental verification for any DOB change
│  │  ├─ If change moves user to different tier: apply new restrictions
│  │  ├─ Log change with old and new DOB (hashed)
│  │  └─ Flag for manual review if change is significant (>2 years)
│  │
│  ├─ ANOMALY:
│  │  ├─ Escalate to higher-assurance verification method
│  │  ├─ If verification confirms original age: no action
│  │  ├─ If verification reveals different age: update account and restrictions
│  │  └─ Log anomaly and resolution
│  │
│  ├─ ANNUAL_REVIEW:
│  │  ├─ Display age confirmation prompt (neutral design)
│  │  ├─ Update age tier if birthday has passed
│  │  └─ Confirm continued parental oversight status
│  │
│  └─ FEATURE_REQUEST:
│     ├─ Check if feature is available for user's age tier
│     ├─ If available: confirm age and enable
│     ├─ If restricted: inform user; offer parental override path
│     └─ Log request and outcome
│
└─ Record re-verification event:
   ├─ Trigger type, timestamp, outcome
   ├─ Verification method used
   └─ Account changes applied
```

## Workflow 5: Circumvention Monitoring

```
Weekly circumvention analysis (automated)
│
├─ Step 1: Analyse registration data
│  ├─ Count accounts where declared age = exact threshold age
│  │  (e.g., exactly 13 years 0 days in jurisdictions with threshold 13)
│  ├─ If count exceeds statistical expectation (>2x expected): FLAG
│  ├─ Count age gate re-attempts from same device within 24 hours
│  ├─ If re-attempt rate exceeds 5%: FLAG
│  └─ Count accounts with DOB on January 1 (common fake date): FLAG
│
├─ Step 2: Analyse behavioural signals
│  ├─ Compare in-app behaviour against age-typical patterns:
│  │  ├─ Typing speed and vocabulary level
│  │  ├─ Content engagement patterns
│  │  ├─ Session duration and timing
│  │  └─ Feature usage patterns
│  ├─ If signals suggest actual age differs significantly from declared age: FLAG
│  └─ Note: behavioural analysis must be privacy-preserving and documented in DPIA
│
├─ Step 3: Review flagged accounts
│  ├─ Manual review by trust and safety team
│  ├─ If circumvention suspected: trigger re-verification (Workflow 4 — ANOMALY)
│  ├─ If circumvention confirmed: apply correct age-tier restrictions
│  └─ If analysis inconclusive: monitor; no action
│
├─ Step 4: Report and improve
│  ├─ Generate weekly circumvention analysis report
│  ├─ Track circumvention rate over time
│  ├─ If rate increases: review and strengthen age gate design
│  └─ Report to DPO quarterly
│
└─ Document analysis methodology and outcomes for accountability
```
