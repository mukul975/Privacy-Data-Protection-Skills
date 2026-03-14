# HIPAA Privacy Rule — Workflows

## Workflow 1: PHI Use/Disclosure Decision Tree

```
PHI Use or Disclosure Request Received
│
├── Is this for Treatment, Payment, or Healthcare Operations (TPO)?
│   ├── YES → Disclosure permitted without authorization (§164.506)
│   │         Apply minimum necessary standard (except treatment)
│   │         Document if non-routine
│   │
│   └── NO → Continue evaluation
│
├── Is this required by law?
│   ├── YES → Disclosure required (§164.512(a))
│   │         Limit to what is legally mandated
│   │
│   └── NO → Continue evaluation
│
├── Does the individual authorize the disclosure?
│   ├── YES → Verify authorization meets §164.508(c) requirements
│   │         (all required elements, not expired, not revoked)
│   │         Disclose as authorized
│   │
│   └── NO → Continue evaluation
│
├── Does a §164.512 public interest exception apply?
│   │   (public health, judicial, law enforcement, research with
│   │    IRB waiver, serious threat, etc.)
│   ├── YES → Apply the specific §164.512 requirements for that category
│   │         Apply minimum necessary
│   │         Document disclosure
│   │
│   └── NO → Disclosure NOT permitted
│
└── STOP — Do not disclose PHI
```

## Workflow 2: Individual Right of Access Request Processing

```
Access Request Received
│
├── Step 1: Verify identity of requestor
│   ├── Individual (patient) → Verify identity per policy
│   ├── Personal representative → Verify authority (§164.502(g))
│   └── Third party with authorization → Verify valid authorization (§164.508(c))
│
├── Step 2: Determine if requested information is in designated record set
│   ├── YES → Continue to Step 3
│   └── NO → Inform requestor; no obligation to provide
│
├── Step 3: Evaluate for exceptions to access right (§164.524(a)(2)-(3))
│   ├── Psychotherapy notes? → May deny
│   ├── Compiled for legal proceedings? → May deny
│   ├── CLIA-restricted lab results? → May deny
│   ├── Endangerment to life/safety (reviewable)? → May deny with right to review
│   ├── Reference to another person (not provider)? → May deny if harm likely
│   └── No exception applies → Must provide access
│
├── Step 4: Provide access within 30 days
│   ├── In requested format if readily producible
│   ├── Electronic if ePHI and requested electronically
│   ├── May charge reasonable cost-based fee
│   └── If extension needed: written notice within 30 days; complete within 60 days
│
└── Step 5: If denied
    ├── Written denial with basis for denial
    ├── If reviewable: inform of right to have denial reviewed by designated reviewer
    ├── Inform of right to file complaint with CE and OCR
    └── Log denial in access request tracking system
```

## Workflow 3: Authorization Validation

```
Authorization Form Received
│
├── Check Required Core Elements (§164.508(c)(1)):
│   ├── [ ] Description of information to be used/disclosed
│   ├── [ ] Name of person(s) authorized to make disclosure
│   ├── [ ] Name of person(s) to whom disclosure may be made
│   ├── [ ] Purpose of disclosure (or "at request of individual")
│   ├── [ ] Expiration date or event
│   └── [ ] Individual's signature and date
│
├── Check Required Statements (§164.508(c)(2)):
│   ├── [ ] Right to revoke in writing
│   ├── [ ] Ability/inability to condition treatment/payment on authorization
│   └── [ ] Potential for re-disclosure (no longer HIPAA-protected)
│
├── Check for Defects (§164.508(b)(2)):
│   ├── [ ] Not expired
│   ├── [ ] Not revoked
│   ├── [ ] Completely filled in (no blank required elements)
│   ├── [ ] Known material false information → INVALID
│   └── [ ] Compound authorization check (only research + related treatment may be combined; §164.508(b)(3))
│
├── If personal representative signed:
│   └── [ ] Description of representative's authority included
│
├── ALL checks pass → Authorization is VALID → Proceed with use/disclosure
│
└── ANY check fails → Authorization is INVALID → Do NOT disclose
    └── Contact requestor to correct deficiency
```

## Workflow 4: Notice of Privacy Practices Distribution

```
NPP Distribution Requirement
│
├── Healthcare Provider with Direct Treatment Relationship (§164.520(c)(1)):
│   ├── Provide NPP at first service delivery
│   ├── Make good faith effort to obtain written acknowledgment
│   ├── If acknowledgment not obtained → Document good faith effort and reason
│   ├── Post NPP in clear and prominent location in facility
│   ├── Make NPP available to anyone who requests a copy
│   └── Post NPP on website (if entity maintains a website)
│
├── Health Plan (§164.520(c)(1)(ii)):
│   ├── Provide NPP at enrollment
│   ├── Provide revised NPP within 60 days of material revision
│   ├── Provide NPP to individual within 60 days of request
│   └── Post NPP on website (if entity maintains a website)
│
└── Material Revision:
    ├── Update NPP to reflect change
    ├── Make revised NPP available upon request
    ├── Post revised NPP in facility and on website
    └── Health plans: distribute within 60 days or include with next annual mailing
```
