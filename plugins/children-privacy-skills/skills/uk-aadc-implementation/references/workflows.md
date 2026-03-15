# UK AADC Implementation Workflows

## Workflow 1: AADC Applicability Assessment

```
Organisation provides an online service
│
├─ Is the service an "information society service"?
│  ├─ Provided for remuneration (including ad-supported)? → YES/NO
│  ├─ Provided at a distance? → YES/NO
│  ├─ Provided by electronic means? → YES/NO
│  ├─ At the individual request of a recipient? → YES/NO
│  │
│  ├─ ALL YES → ISS confirmed. Continue.
│  └─ ANY NO → Not an ISS. AADC does not apply. Document.
│     NOTE: "Remuneration" includes ad-funded services and services where
│     the user pays with personal data. Almost all online services qualify.
│
├─ Is the service a "preventive or counselling service" offered directly to a child?
│  ├─ YES → Excluded from AADC. Document.
│  └─ NO → Continue.
│
├─ Is the service "likely to be accessed by children" (under 18)?
│  ├─ Consider:
│  │  □ Does the service have any users under 18?
│  │  □ Could a child foreseeably access the service?
│  │  □ Is the content attractive or relevant to children?
│  │  □ Is the service listed in app stores without age restrictions?
│  │  □ Is the service promoted in channels children use?
│  │  □ Does analytics show any under-18 traffic?
│  │
│  ├─ YES (any indicator) → AADC applies. Proceed to Workflow 2.
│  └─ NO (can demonstrate children cannot access) → AADC does not apply.
│     Document evidence that reasonable steps prevent child access.
│
└─ Record applicability determination with date and evidence.
```

## Workflow 2: AADC Conformance Self-Assessment

```
AADC applies to the service
│
├─ For each of the 15 standards, conduct assessment:
│
│  STANDARD 1: Best Interests
│  ├─ Has a Best Interests Assessment (BIA) been completed? [Y/N]
│  ├─ Does the BIA reference UNCRC Articles 3, 12, 16, 31? [Y/N]
│  ├─ Are children's interests weighed against commercial interests? [Y/N]
│  ├─ Is the BIA reviewed when features change? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
│  STANDARD 2: DPIA
│  ├─ Has a child-specific DPIA been conducted? [Y/N]
│  ├─ Does the DPIA segment risk by age group? [Y/N]
│  ├─ Are child-specific harms assessed (grooming, bullying, commercial pressure)? [Y/N]
│  ├─ Is the DPIA reviewed annually? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
│  STANDARD 3: Age-Appropriate Application
│  ├─ Is an age assurance mechanism implemented? [Y/N]
│  ├─ Is the mechanism proportionate to the risk? [Y/N]
│  ├─ Are different design standards applied to different age groups? [Y/N]
│  ├─ Is age information used only for age assurance purposes? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
│  STANDARD 4: Transparency
│  ├─ Is a child-friendly privacy notice provided? [Y/N]
│  ├─ Is the notice tested with children for comprehension? [Y/N]
│  ├─ Are just-in-time notices used at collection points? [Y/N]
│  ├─ Is the language appropriate to the target age group? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
│  STANDARD 5: Detrimental Use
│  ├─ Is there a register of processing activities assessed for detrimental impact? [Y/N]
│  ├─ Is behavioural advertising absent for child users? [Y/N]
│  ├─ Are dark patterns absent from the child experience? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
│  STANDARD 6: Policies and Community Standards
│  ├─ Are published policies enforced consistently? [Y/N]
│  ├─ Are reporting mechanisms accessible to children? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
│  STANDARD 7: Default Settings
│  ├─ Is profile visibility defaulted to private? [Y/N]
│  ├─ Is location sharing defaulted to off? [Y/N]
│  ├─ Is personalised advertising defaulted to off? [Y/N]
│  ├─ Is data sharing defaulted to off? [Y/N]
│  ├─ Are non-high-privacy defaults documented with compelling reason? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
│  STANDARD 8: Data Minimisation
│  ├─ Is data limited to active, knowing engagement features? [Y/N]
│  ├─ Is background data collection disabled unless feature-triggered? [Y/N]
│  ├─ Are separate choices offered for optional data-intensive features? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
│  STANDARD 9: Data Sharing
│  ├─ Is children's data shared with third parties? [Y/N → if YES, compelling reason?]
│  ├─ Are third parties contractually bound to equivalent protections? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
│  STANDARD 10: Geolocation
│  ├─ Is geolocation defaulted to off? [Y/N]
│  ├─ Is a visible indicator displayed when location is active? [Y/N]
│  ├─ Is location visibility to others defaulted to off? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
│  STANDARD 11: Parental Controls
│  ├─ If parental controls exist, is the child informed? [Y/N]
│  ├─ Is a visible indicator shown when monitoring is active? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
│  STANDARD 12: Profiling
│  ├─ Is profiling defaulted to off? [Y/N]
│  ├─ If profiling is enabled, are protective measures in place? [Y/N]
│  ├─ Are content diversity and time limit safeguards implemented? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
│  STANDARD 13: Nudge Techniques
│  ├─ Are accept/reject options equally prominent? [Y/N]
│  ├─ Are rewards for data/weakened privacy absent? [Y/N]
│  ├─ Are dark patterns absent from consent flows? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
│  STANDARD 14: Connected Toys and Devices
│  ├─ N/A if no connected devices → Mark N/A
│  ├─ If applicable: are all standards applied to the device? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming / N/A]
│
│  STANDARD 15: Online Tools
│  ├─ Is a child-accessible privacy centre provided? [Y/N]
│  ├─ Can children download and delete their data easily? [Y/N]
│  ├─ Is a reporting mechanism available without extra data collection? [Y/N]
│  └─ Assessment: [Conforming / Partially Conforming / Non-Conforming]
│
├─ Generate conformance summary:
│  ├─ Conforming: [count]/15
│  ├─ Partially Conforming: [count]/15
│  ├─ Non-Conforming: [count]/15
│  ├─ N/A: [count]/15
│  └─ Overall assessment and remediation priority list
│
└─ Schedule annual reassessment date.
```

## Workflow 3: Best Interests Assessment (BIA)

```
New feature or processing activity proposed for a service accessed by children
│
├─ Step 1: Describe the feature/processing
│  ├─ What does it do?
│  ├─ What data does it collect/process?
│  ├─ Who does it affect (which age groups)?
│  └─ What is the commercial benefit?
│
├─ Step 2: Assess impact on children's interests
│  ├─ Physical safety: Could this feature lead to physical harm? (contact with strangers,
│  │   real-world meetups, location disclosure)
│  ├─ Mental health: Could this feature affect mental wellbeing? (social comparison,
│  │   addictive design, anxiety-inducing notifications, body image)
│  ├─ Development: Does this support or hinder healthy development? (creativity,
│  │   learning, social skills vs. passive consumption, isolation)
│  ├─ Education: Does this provide educational value?
│  ├─ Privacy: How does this affect the child's right to privacy? (data collection,
│  │   exposure to others, profiling)
│  ├─ Play and recreation: Does this support the child's right to play? (engagement,
│  │   creativity, fun vs. commercial exploitation)
│  └─ Agency: Does this respect the child's evolving capacity for autonomous decision-making?
│
├─ Step 3: Weigh children's interests against commercial interests
│  ├─ Document the commercial benefit of the feature
│  ├─ If children's interests conflict with commercial interests, children's interests prevail
│  ├─ If modification can protect children while preserving commercial value, implement modification
│  └─ Document the balancing exercise and reasoning
│
├─ Step 4: Decision
│  ├─ PROCEED: Feature is in the child's best interests (or neutral) → Implement with monitoring
│  ├─ MODIFY: Feature can be adapted to protect children → Implement modified version
│  └─ REJECT: Feature is contrary to children's best interests → Do not implement for child users
│
└─ Step 5: Record and review
   ├─ Document the BIA with all assessments and reasoning
   ├─ Assign review date (quarterly or upon feature change)
   └─ File in AADC conformance records
```

## Workflow 4: AADC Default Settings Audit

```
Quarterly audit of default settings for child users
│
├─ For each configurable setting:
│  ├─ Setting name: [description]
│  ├─ Current default: [value]
│  ├─ Is the default "high privacy"? [Y/N]
│  │  ├─ YES → Conforming. No action.
│  │  └─ NO → Is there a documented compelling reason?
│  │     ├─ YES → Review compelling reason for continued validity
│  │     └─ NO → Non-conforming. Remediate to high-privacy default.
│  │
│  └─ Log audit result
│
├─ Generate audit report:
│  ├─ Total settings audited: [count]
│  ├─ High-privacy default: [count]
│  ├─ Compelling-reason exceptions: [count]
│  ├─ Non-conforming (remediation needed): [count]
│  └─ Remediation timeline for non-conforming settings
│
└─ DPO sign-off on audit report
```
