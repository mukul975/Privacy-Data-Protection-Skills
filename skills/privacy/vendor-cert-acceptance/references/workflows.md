# Workflows — Vendor Certification Acceptance

## Workflow 1: Certification Evaluation for New Vendor

```
TRIGGER: Vendor presents certifications during due diligence process
  │
  ├─► Step 1: Collect Certification Documentation (Privacy Team — 2 business days)
  │     ├─ Request from vendor:
  │     │     ├─ Certificate copies (PDF) for all claimed certifications
  │     │     ├─ SOC 2 Type II report (under NDA if required)
  │     │     ├─ Certification scope statements
  │     │     ├─ Certification body details
  │     │     └─ Most recent surveillance audit confirmation (ISO)
  │     └─ Log received certifications in vendor assessment file
  │
  ├─► Step 2: Verify Certification Authenticity (Privacy Team — 3 business days)
  │     ├─ ISO certifications:
  │     │     ├─ Check certification body accreditation on IAF MLA signatory list
  │     │     ├─ Verify certificate on certification body's online registry
  │     │     └─ Confirm certificate is current (not expired)
  │     ├─ SOC 2 reports:
  │     │     ├─ Verify CPA firm is licensed and in good standing
  │     │     ├─ Review report period (should be recent, ideally within 12 months)
  │     │     └─ Check for qualified opinions or material exceptions
  │     ├─ CSA STAR:
  │     │     ├─ Verify on CSA STAR Registry (cloudsecurityalliance.org/star)
  │     │     └─ Confirm level (self-assessment vs. third-party audit)
  │     ├─ GDPR certifications (Art. 42):
  │     │     ├─ Verify certification body accreditation per Art. 43
  │     │     └─ Check EDPB registry of approved certification mechanisms
  │     └─ Document all verification results
  │
  ├─► Step 3: Scope Alignment Check (Privacy Team — 2 business days)
  │     ├─ Map certification scope against services provided to Summit:
  │     │     ├─ Does the scope cover the specific service/product?
  │     │     ├─ Does it cover all processing locations?
  │     │     ├─ Are there any exclusions relevant to Summit's data?
  │     │     └─ For ISO 27701: Is the processor annex (Annex B) in scope?
  │     └─ Document any scope gaps
  │
  ├─► Step 4: GDPR Gap Analysis (Privacy Team — 3 business days)
  │     ├─ Map certifications against GDPR equivalence matrix
  │     ├─ Identify uncovered Art. 28(3) requirements
  │     ├─ Determine supplementary evidence needed per gap
  │     ├─ Request supplementary evidence from vendor
  │     └─ Document gap analysis results
  │
  ├─► Step 5: Certification Acceptance Decision (Privacy Team Lead — 1 business day)
  │     ├─ ACCEPTED — FULL COVERAGE:
  │     │     └─ Certifications cover all GDPR requirements; minimal supplementation
  │     ├─ ACCEPTED — WITH SUPPLEMENTATION:
  │     │     └─ Certifications cover core areas; supplementary evidence addresses gaps
  │     ├─ INSUFFICIENT:
  │     │     └─ Certifications do not cover critical requirements; full assessment required
  │     └─ Document acceptance decision with rationale
  │
  └─► Step 6: Record and Integrate (Privacy Team — 1 business day)
        ├─ Record certification details in vendor register
        ├─ Set certification expiry monitoring alerts
        ├─ Factor certification score into vendor risk scoring
        └─ Note renewal dates for ongoing monitoring
```

## Workflow 2: Certification Renewal Monitoring

```
TRIGGER: Certification expiry approaching (90 days) or surveillance audit due
  │
  ├─► Step 1: Alert Triage (Privacy Team — 1 business day)
  │     ├─ Identify which vendor and certification is expiring
  │     ├─ Assess impact if certification lapses
  │     └─ Contact vendor to confirm renewal status
  │
  ├─► Step 2: Vendor Response Assessment
  │     ├─ Renewal on track: Note confirmed renewal date
  │     ├─ Renewal delayed: Assess risk; determine if interim measures needed
  │     └─ Not renewing: Trigger reassessment of vendor sufficiency
  │
  └─► Step 3: Post-Renewal Verification
        ├─ Obtain new certificate upon issuance
        ├─ Verify scope unchanged (or assess scope changes)
        ├─ Update vendor register
        └─ Reset monitoring alert for next expiry
```

## Workflow 3: Cross-Framework Equivalence Assessment

```
TRIGGER: Vendor holds certification not in Summit's standard recognition list
  │
  ├─► Step 1: Framework Research (Privacy Team — 5 business days)
  │     ├─ Research the certification framework:
  │     │     ├─ Issuing organization and governance
  │     │     ├─ Assessment methodology (self vs. third-party)
  │     │     ├─ Control domain coverage
  │     │     └─ Regulatory recognition (any supervisory authority endorsement)
  │     └─ Document framework analysis
  │
  ├─► Step 2: Equivalence Mapping
  │     ├─ Map framework controls against GDPR Art. 28 requirements
  │     ├─ Identify coverage level: Full / Partial / None per requirement
  │     └─ Determine overall equivalence assessment
  │
  ├─► Step 3: Acceptance Decision
  │     ├─ If equivalent to Tier A/B: Accept with standard supplementation
  │     ├─ If equivalent to Tier C/D: Accept as supplementary evidence only
  │     └─ Add to recognition list if expected to recur
  │
  └─► Step 4: Update Framework
        ├─ If recurring framework: Add to certification acceptance criteria
        └─ If one-off: Document assessment in vendor file only
```
