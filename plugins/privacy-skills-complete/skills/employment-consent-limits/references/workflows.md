# Employment Consent Limits Workflows

## Workflow 1: Lawful Basis Selection for Employment Processing

```
START: Employer needs to process employee personal data
│
├─ Step 1: Is the processing required by law?
│  ├─ Tax law (PAYE, income tax reporting) → Art. 6(1)(c)
│  ├─ Social security (contributions, reporting) → Art. 6(1)(c)
│  ├─ Health and safety (incident reporting, surveillance) → Art. 6(1)(c)
│  ├─ Immigration (right-to-work verification) → Art. 6(1)(c)
│  ├─ Working time (CCOO v Deutsche Bank — recording obligation) → Art. 6(1)(c)
│  └─ NOT legally required → Continue to Step 2
│
├─ Step 2: Is the processing necessary for the employment contract?
│  ├─ Payroll processing → Art. 6(1)(b)
│  ├─ Work scheduling and shift management → Art. 6(1)(b)
│  ├─ Performance management per contractual objectives → Art. 6(1)(b)
│  ├─ Absence management → Art. 6(1)(b)
│  ├─ Provision of contractual benefits → Art. 6(1)(b)
│  └─ NOT necessary for contract → Continue to Step 3
│
├─ Step 3: Is the employer a public authority processing for public tasks?
│  ├─ YES → Art. 6(1)(e) — Public Interest
│  └─ NO → Continue to Step 4
│
├─ Step 4: Does the employer have a legitimate interest?
│  ├─ YES → Conduct three-part Legitimate Interest Assessment:
│  │  ├─ Purpose test: Is the interest legitimate? [Document]
│  │  ├─ Necessity test: Is processing necessary for that interest? [Document]
│  │  ├─ Balancing test: Do employer interests override employee rights? [Document]
│  │  ├─ Balancing favours employer → Art. 6(1)(f)
│  │  └─ Balancing favours employee → Cannot use Art. 6(1)(f). Continue to Step 5.
│  └─ NO → Continue to Step 5
│
├─ Step 5: Is the processing genuinely voluntary?
│  ├─ ALL of the following must be TRUE:
│  │  □ Processing is for an optional benefit (not core employment)
│  │  □ Refusal has ZERO employment consequences
│  │  □ Employee can withdraw at any time
│  │  □ Withdrawal is easy and has no consequences
│  │  □ Processing is separate from employment terms
│  │  □ No national law prohibits consent in this context
│  ├─ ALL TRUE → Art. 6(1)(a) Consent may be valid. Document safeguards.
│  └─ ANY FALSE → Consent is NOT valid. Processing cannot proceed.
│
└─ END: If no lawful basis identified, the processing must not take place.
```

## Workflow 2: Consent Validity Audit for Existing Employment Processing

```
START: Annual audit of consent-based employment processing
│
├─ Step 1: Identify all processing activities currently based on consent
│  └─ Review ROPA, privacy notices, and consent forms for consent references
│
├─ Step 2: For each consent-based activity, assess validity:
│  │
│  ├─ Is there a genuine power imbalance? (Always YES for employment)
│  │
│  ├─ Could refusal result in ANY negative consequence?
│  │  ├─ YES → Consent is INVALID. Reassign to alternative lawful basis or cease processing.
│  │  └─ NO → Continue assessment
│  │
│  ├─ Is the consent specific (one purpose per consent)?
│  │  ├─ YES → Continue
│  │  └─ NO → Consent is INVALID. Separate consents required.
│  │
│  ├─ Is the consent informed (purpose, data types, rights, withdrawal)?
│  │  ├─ YES → Continue
│  │  └─ NO → Consent is INVALID. Update consent form.
│  │
│  ├─ Is withdrawal as easy as giving consent?
│  │  ├─ YES → Continue
│  │  └─ NO → Consent is INVALID. Implement easy withdrawal mechanism.
│  │
│  ├─ Does national law restrict or prohibit consent for this purpose?
│  │  ├─ YES → Consent is INVALID under national law. Find alternative basis.
│  │  └─ NO → Consent may be valid.
│  │
│  └─ RESULT: Consent is [ ] Valid [ ] Invalid → [ ] Reassign basis [ ] Cease processing
│
├─ Step 3: For invalid consents, select alternative lawful basis per Workflow 1
│
├─ Step 4: Update ROPA, privacy notices, and internal documentation
│
└─ END: Document audit findings and remediation actions.
```

## Workflow 3: Works Council Consultation for New Processing (DE, FR, NL, AT)

```
START: New employment processing activity proposed
│
├─ Is the processing subject to works council co-determination?
│  ├─ Germany: Section 87(1)(6) BetrVG — technical monitoring → YES
│  ├─ France: CSE consultation for employee data processing → YES
│  ├─ Netherlands: Art. 27(1)(k)/(l) WOR — personal data systems → YES
│  ├─ Austria: Section 96(1)(3) ArbVG — monitoring systems → YES
│  └─ Other jurisdiction → Check national requirements
│
├─ Notify works council of proposed processing
│  ├─ Provide: description, purpose, lawful basis, scope, data categories
│  ├─ Timeline: before implementation, allow adequate consultation period
│  └─ Document notification
│
├─ Works council response:
│  ├─ AGREEMENT → Document agreement. Proceed with implementation.
│  ├─ OBJECTION → Negotiate modifications.
│  │  ├─ Agreement reached → Document. Proceed.
│  │  └─ No agreement → Escalate per national procedure (conciliation committee in DE).
│  └─ NO RESPONSE within agreed period → Follow national default rules.
│
└─ END: Document works council consultation outcome in DPIA / processing record.
```
