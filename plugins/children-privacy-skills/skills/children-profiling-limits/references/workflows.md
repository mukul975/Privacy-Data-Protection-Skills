# Children's Profiling Limits Workflows

## Workflow 1: Profiling Classification for Children

```
New feature or algorithm proposed that may involve profiling
│
├─ Step 1: Is this profiling?
│  ├─ Does the feature use automated processing of personal data? [Y/N]
│  ├─ Does it evaluate personal aspects (preferences, behaviour, interests)? [Y/N]
│  ├─ Does it analyse or predict behaviour? [Y/N]
│  │
│  ├─ ALL YES → This is profiling under Art. 4(4). Proceed to Step 2.
│  ├─ ANY NO → Not profiling. Document determination.
│  └─ UNCERTAIN → Treat as profiling. Proceed to Step 2.
│
├─ Step 2: Classify profiling type
│  ├─ PROHIBITED:
│  │  □ Behavioural advertising targeting
│  │  □ Social scoring / popularity ranking
│  │  □ Emotional profiling / sentiment targeting
│  │  □ Predictive analytics for commercial targeting
│  │  □ Cross-service behavioural tracking
│  │  → If ANY checked: STOP. This processing is not permitted for children.
│  │
│  ├─ RESTRICTED (permitted with safeguards):
│  │  □ Content-based recommendations
│  │  □ Educational adaptive learning
│  │  □ Safety and moderation profiling
│  │  □ Age-appropriate content filtering
│  │  → If checked: Proceed to Step 3 for safeguard assessment.
│  │
│  └─ NOT PROFILING:
│     □ Contextual advertising (based on page content, not user)
│     □ Aggregate analytics (anonymised, no individual evaluation)
│     □ A/B testing (random assignment)
│     → If checked: Permitted. Document that this is not profiling.
│
├─ Step 3: Safeguard assessment for restricted profiling
│  ├─ Is the profiling defaulted to OFF? [Must be YES]
│  ├─ Is parental consent obtained before activation? [Must be YES for under-threshold]
│  ├─ Are content diversity safeguards in place? [Must be YES for recommendations]
│  ├─ Are time-limitation mechanisms implemented? [Must be YES]
│  ├─ Are mental health circuit-breakers active? [Must be YES]
│  ├─ Is a DPIA completed? [Must be YES]
│  ├─ Is an annual algorithmic impact assessment scheduled? [Must be YES]
│  │
│  ├─ ALL YES → Profiling may proceed with ongoing monitoring.
│  └─ ANY NO → Implement missing safeguards before activation.
│
└─ Document classification, safeguards, and approval in profiling register.
```

## Workflow 2: Default Settings Enforcement for Profiling

```
Ensure all profiling features are off by default for child accounts
│
├─ Step 1: Inventory all profiling features
│  ├─ List every feature that uses personal data to evaluate,
│  │   predict, or personalise the child's experience
│  ├─ For each feature:
│  │  ├─ Feature name and description
│  │  ├─ Personal data elements used
│  │  ├─ Current default setting (on/off)
│  │  └─ Compelling reason for non-off default? [Y/N, with documentation]
│
├─ Step 2: Verify defaults
│  ├─ For each feature:
│  │  ├─ Is the default OFF? → Conforming
│  │  ├─ Is the default ON with compelling reason? → Review compelling reason
│  │  │  ├─ Does the compelling reason pass the best interests test?
│  │  │  ├─ Are protective measures in place?
│  │  │  └─ If BOTH YES → Conditionally conforming (document)
│  │  │  └─ If EITHER NO → Non-conforming. Change to OFF.
│  │  └─ Is the default ON without compelling reason? → Non-conforming. Change to OFF.
│
├─ Step 3: Implement changes
│  ├─ Update feature defaults in account configuration for child accounts
│  ├─ Verify at the application layer: new child accounts get OFF defaults
│  ├─ Verify at the API layer: profiling endpoints reject requests for non-activated features
│  └─ Test: create new child account and verify all profiling features are off
│
└─ Step 4: Audit
   ├─ Log current default settings for all profiling features
   ├─ DPO sign-off on default settings audit
   ├─ Schedule next audit (quarterly)
   └─ File audit report in AADC conformance records
```

## Workflow 3: Algorithmic Impact Assessment

```
Annual algorithmic impact assessment for features affecting children
│
├─ Step 1: Scope
│  ├─ Identify all algorithms that process children's personal data
│  ├─ For each algorithm:
│  │  ├─ Algorithm name and function
│  │  ├─ Input data: what personal data does it use?
│  │  ├─ Output: what decisions or recommendations does it produce?
│  │  ├─ Affected users: which age groups?
│  │  └─ Scale: number of children affected
│
├─ Step 2: Purpose test
│  ├─ Does the algorithm serve the child's interests? [Document]
│  ├─ What is the primary beneficiary? (child / controller / both)
│  └─ Could the purpose be achieved without profiling? [Document]
│
├─ Step 3: Necessity test
│  ├─ Is each input data element necessary for the algorithm's purpose? [Document]
│  ├─ Could the algorithm work with less data? [Document]
│  ├─ Could the algorithm work with anonymised data? [Document]
│  └─ Is the algorithm limited to its stated purpose? [Verify]
│
├─ Step 4: Harm assessment
│  ├─ Could the algorithm produce content rabbit holes? [Assess]
│  ├─ Could it amplify harmful content? [Assess]
│  ├─ Could it create social comparison or status anxiety? [Assess]
│  ├─ Could it encourage excessive engagement? [Assess]
│  ├─ Could it influence the child's behaviour in exploitative ways? [Assess]
│  └─ For each identified harm: what mitigation is in place?
│
├─ Step 5: Bias audit
│  ├─ Test algorithm outputs across demographic groups:
│  │  ├─ Age groups (5-8, 9-12, 13-15, 16-17)
│  │  ├─ Gender
│  │  ├─ Language / geographic region
│  │  └─ Accessibility (users with disabilities)
│  ├─ Statistical analysis for disparate outcomes
│  └─ If bias detected: document and remediate
│
├─ Step 6: Safeguard verification
│  ├─ Content diversity injection: active and effective? [Verify]
│  ├─ Time limitation mechanisms: functioning? [Verify]
│  ├─ Mental health circuit-breakers: configured and tested? [Verify]
│  ├─ Human oversight: override mechanisms available? [Verify]
│  └─ Transparency: privacy notice accurately describes the algorithm? [Verify]
│
├─ Step 7: Report
│  ├─ Generate algorithmic impact assessment report
│  ├─ DPO review and sign-off
│  ├─ Remediation plan for identified issues
│  └─ Schedule next annual assessment
│
└─ File report in AADC conformance records
```

## Workflow 4: Nudge Technique Audit

```
Quarterly audit of UI/UX for nudge techniques affecting children
│
├─ Step 1: Audit consent and privacy choice interfaces
│  ├─ For each choice presented to children:
│  │  ├─ Are accept/reject options equally prominent? [Y/N]
│  │  ├─ Are option labels neutral? [Y/N]
│  │  ├─ Is the default privacy-protective? [Y/N]
│  │  ├─ Is friction equal for privacy-enhancing and privacy-reducing choices? [Y/N]
│  │  └─ Are there rewards for data or weakened privacy? [Y/N — must be NO]
│
├─ Step 2: Check for prohibited patterns
│  ├─ Confirmshaming: "Are you sure you want to miss out?" → PROHIBITED
│  ├─ Reward-for-data: "Earn 100 coins by enabling notifications!" → PROHIBITED
│  ├─ Asymmetric choices: large bright "Accept" vs small grey "Decline" → PROHIBITED
│  ├─ Hidden opt-out: privacy options buried in sub-menus → PROHIBITED
│  ├─ Social proof: "95% of users allow this!" → PROHIBITED
│  ├─ Urgency: "Enable now or lose your streak!" → PROHIBITED
│  ├─ Default-to-share: pre-selected sharing options → PROHIBITED
│  └─ Misdirection: confusing label ordering → PROHIBITED
│
├─ Step 3: User testing
│  ├─ Present the interfaces to 10+ children in target age group
│  ├─ Ask: "What happens if you tap this button?"
│  ├─ Ask: "Which option keeps your information more private?"
│  ├─ Observe: do children make informed choices?
│  └─ Document results
│
├─ Step 4: Remediate
│  ├─ For each prohibited pattern found: redesign the interface
│  ├─ Re-test with children after redesign
│  └─ Document remediation with before/after screenshots
│
└─ Step 5: Report
   ├─ Generate nudge technique audit report
   ├─ DPO sign-off
   └─ Schedule next quarterly audit
```
