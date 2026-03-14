# Workflows — Assessing Legitimate Interest vs Consent

## Workflow 1: Lawful Basis Selection for New Processing Activity

```
TRIGGER: New processing activity proposed at CloudVault SaaS Inc.
  │
  ├─► Step 1: Document the processing activity
  │     ├─ What personal data is processed?
  │     ├─ What is the purpose?
  │     ├─ Who is the data subject population?
  │     ├─ Are any third parties involved?
  │     └─ Is special category data involved?
  │
  ├─► Step 2: Check for mandatory consent requirements
  │     ├─ Is this cookie/tracker processing? → ePrivacy Art. 5(3) requires consent
  │     ├─ Is this unsolicited e-marketing to new contacts? → ePrivacy Art. 13 requires consent
  │     ├─ Is special category data involved? → Art. 9(2)(a) requires explicit consent
  │     ├─ Is this automated decision-making with legal effects? → Art. 22(2)(c) requires consent
  │     └─ If any YES: MUST use consent. Stop here.
  │
  ├─► Step 3: Assess power imbalance
  │     ├─ Is there an employment relationship?
  │     ├─ Is the controller a public authority?
  │     ├─ Is consent conditioned on service access?
  │     ├─ Does the data subject have no reasonable alternative?
  │     └─ If imbalance exists: Consent likely invalid → proceed with LI assessment
  │
  ├─► Step 4: If no mandatory consent and no power imbalance, evaluate both options
  │     │
  │     ├─► Consent evaluation:
  │     │     ├─ Can consent be genuinely free?
  │     │     ├─ Is granular per-purpose consent feasible?
  │     │     ├─ Is withdrawal operationally manageable?
  │     │     └─ Is the user experience acceptable with consent UI?
  │     │
  │     └─► Legitimate interest evaluation:
  │           ├─ Can you articulate a legitimate interest?
  │           ├─ Is the processing necessary for that interest?
  │           ├─ Does the balancing test favor the controller?
  │           └─ Can you provide an easy opt-out?
  │
  ├─► Step 5: Select and document lawful basis
  │     ├─ Record: chosen basis, reasoning, analysis date
  │     ├─ If consent: implement Art. 7 requirements
  │     └─ If LI: document three-part LIA, implement opt-out
  │
  └─► Step 6: DPO review and sign-off
```

## Workflow 2: Legitimate Interest Assessment (LIA) Process

```
TRIGGER: Legitimate interest selected as lawful basis
  │
  ├─► Part 1: Purpose Test
  │     ├─ State the legitimate interest:
  │     │   "CloudVault SaaS Inc. has a legitimate interest in detecting and
  │     │    preventing fraudulent account creation to protect service integrity
  │     │    and legitimate users."
  │     ├─ Confirm the interest is:
  │     │   ├─ Lawful (not illegal in itself) ✓
  │     │   ├─ Real and present (not speculative) ✓
  │     │   └─ Sufficiently clearly articulated ✓
  │     └─ PASS / FAIL
  │
  ├─► Part 2: Necessity Test
  │     ├─ Is the processing necessary for the stated interest?
  │     ├─ Could the interest be achieved with less data?
  │     ├─ Could the interest be achieved without personal data?
  │     ├─ Is there a less intrusive alternative?
  │     └─ PASS / FAIL
  │
  ├─► Part 3: Balancing Test
  │     ├─ Nature of data: is it sensitive? (lower weight for non-sensitive)
  │     ├─ Reasonable expectation: would the data subject expect this?
  │     ├─ Relationship: existing relationship with data subject?
  │     ├─ Impact: what is the likely impact on the data subject?
  │     ├─ Safeguards: what measures mitigate impact?
  │     ├─ Vulnerable groups: are children or vulnerable adults involved?
  │     └─ Overall balance: controller interest > data subject rights?
  │
  ├─► Document the LIA
  │     ├─ Date of assessment
  │     ├─ Processing activity description
  │     ├─ Purpose test result with reasoning
  │     ├─ Necessity test result with reasoning
  │     ├─ Balancing test result with factor-by-factor analysis
  │     └─ Conclusion and DPO sign-off
  │
  └─► Implement safeguards
        ├─ Opt-out mechanism (Art. 21 right to object)
        ├─ Privacy notice updated with LI disclosure (Art. 13(1)(d))
        ├─ Data minimization measures
        └─ Regular LIA review schedule (annual)
```
