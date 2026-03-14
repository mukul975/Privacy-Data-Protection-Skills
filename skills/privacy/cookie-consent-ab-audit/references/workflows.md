# Workflows — Auditing Cookie Consent A/B Testing

## Workflow 1: Consent Banner A/B Test Audit

```
TRIGGER: New A/B test deployed on consent banner OR quarterly audit
  │
  ├─► Step 1: Inventory active experiments
  │     ├─ List all active A/B tests on consent-related UI
  │     ├─ For each: variant name, description, traffic allocation
  │     ├─ Identify experiment owner and start date
  │     └─ Retrieve hypothesis and success metric definitions
  │
  ├─► Step 2: Capture each variant
  │     ├─ Desktop screenshot (1920x1080)
  │     ├─ Mobile screenshot (375x812, iPhone 14 equivalent)
  │     ├─ Full accept flow recording (click path, page loads)
  │     ├─ Full reject flow recording (click path, page loads)
  │     ├─ HTML/CSS extraction for accept and reject elements
  │     └─ Network trace showing scripts loaded before/after consent
  │
  ├─► Step 3: Dark pattern assessment per variant
  │     │
  │     ├─► Category 1: Visual Asymmetry
  │     │     ├─ Measure accept button: 240x48px, #2563EB blue, 16px bold
  │     │     ├─ Measure reject button: 240x48px, #2563EB blue, 16px bold
  │     │     ├─ Position: accept left, reject right (equal level)
  │     │     └─ Score: 0/10 (fully symmetric) ✓
  │     │
  │     ├─► Category 2: Interaction Asymmetry
  │     │     ├─ Accept path: 1 click ("Accept All")
  │     │     ├─ Reject path: 1 click ("Reject All")
  │     │     └─ Score: 0/10 (equal clicks) ✓
  │     │
  │     ├─► Category 3: Language Manipulation
  │     │     ├─ Accept text: "Accept All Cookies"
  │     │     ├─ Reject text: "Reject All Cookies"
  │     │     ├─ Both neutral, no emotional manipulation
  │     │     └─ Score: 0/10 ✓
  │     │
  │     ├─► Category 4: Timing/Delay
  │     │     ├─ Both buttons render simultaneously
  │     │     ├─ No loading delay on reject path
  │     │     └─ Score: 0/10 ✓
  │     │
  │     └─► Category 5: Repeated Prompting
  │           ├─ Banner dismissed after choice
  │           ├─ Choice persisted for 6 months
  │           └─ Score: 0/10 ✓
  │
  ├─► Step 4: Consent rate analysis
  │     ├─ Variant A: 67.2% accept (n=50,000)
  │     ├─ Variant B: 69.1% accept (n=50,000)
  │     ├─ Difference: 1.9 percentage points
  │     ├─ Statistical significance: p=0.04
  │     ├─ Both variants have symmetric design → difference is from layout, not manipulation
  │     └─ Assessment: ACCEPTABLE — no manipulation-driven uplift
  │
  └─► Step 5: Generate audit report
        ├─ Screenshots and measurements for each variant
        ├─ Dark pattern scores
        ├─ Consent rate comparison
        ├─ Compliance determination
        └─ Submit to DPO
```

## Workflow 2: Non-Compliant Variant Detection and Remediation

```
TRIGGER: Audit identifies a variant with dark pattern score > 3.0
  │
  ├─► Step 1: Immediate assessment
  │     ├─ Identify specific non-compliant elements
  │     ├─ Classify severity:
  │     │   ├─ Score 3.0-5.0: HIGH — remediate within 7 days
  │     │   └─ Score 5.0+: CRITICAL — remove variant immediately
  │     └─ Estimate number of users affected (traffic * duration)
  │
  ├─► Step 2: For CRITICAL (score > 5.0)
  │     ├─ Immediately disable the non-compliant variant
  │     ├─ Route all traffic to the compliant control variant
  │     ├─ Notify DPO within 1 hour
  │     └─ Assess whether invalidated consents affect downstream processing
  │
  ├─► Step 3: Consent validity assessment
  │     ├─ Were consents collected under the non-compliant variant valid?
  │     ├─ If manipulation was material (score > 5.0):
  │     │   ├─ Consents collected under this variant may be invalid
  │     │   ├─ Flag affected consent records
  │     │   ├─ Consider re-consent campaign for affected users
  │     │   └─ Document assessment and DPO decision
  │     └─ If manipulation was minor (score 3.0-5.0):
  │           ├─ Fix the variant design
  │           └─ Existing consents likely remain valid (proportionality)
  │
  ├─► Step 4: Root cause analysis
  │     ├─ How was the non-compliant variant approved?
  │     ├─ Was there a privacy review before launch?
  │     ├─ Update A/B test approval process to include privacy review
  │     └─ Train relevant teams on consent banner compliance
  │
  └─► Step 5: Documentation
        ├─ Incident report with timeline
        ├─ Users affected and consent impact
        ├─ Remediation actions taken
        ├─ Process improvements implemented
        └─ File in compliance records for potential regulatory inquiry
```

## Workflow 3: Pre-Launch Privacy Review for Consent Banner Experiments

```
TRIGGER: Product team proposes a new A/B test on consent UI
  │
  ├─► Step 1: Submit experiment proposal
  │     ├─ Experiment description and hypothesis
  │     ├─ Mockups of all proposed variants
  │     ├─ Success metrics (consent rate, engagement, etc.)
  │     └─ Traffic allocation and duration
  │
  ├─► Step 2: Privacy team review (within 48 hours)
  │     ├─ Apply dark pattern assessment to each proposed variant
  │     ├─ Verify equal prominence of accept/reject in all variants
  │     ├─ Verify equal interaction cost in all variants
  │     ├─ Check language neutrality
  │     └─ Review success metrics (flag if primary metric is consent rate)
  │
  ├─► Step 3: Decision
  │     ├─ APPROVED: All variants pass dark pattern assessment
  │     ├─ APPROVED WITH CONDITIONS: Minor adjustments needed
  │     └─ REJECTED: Fundamental design issues (must redesign)
  │
  └─► Step 4: Post-launch monitoring
        ├─ Monitor consent rates in first 48 hours
        ├─ Flag if any variant shows >20% uplift (potential manipulation)
        └─ Schedule audit at experiment midpoint
```
