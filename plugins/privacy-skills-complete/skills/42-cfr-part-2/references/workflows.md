# 42 CFR Part 2 — Workflows

## Workflow 1: Part 2 Consent Decision Tree

```
SUD Patient Record Disclosure Request
│
├── Is this a medical emergency (§2.51)?
│   ├── YES → Disclose minimum necessary to medical personnel
│   │         Document: recipient, authorizing person, date/time, nature of emergency
│   │         No consent required
│   └── NO → Continue
│
├── Is this an audit/evaluation by government or payer (§2.53)?
│   ├── YES → Permit access without consent (subject to re-disclosure restrictions)
│   └── NO → Continue
│
├── Is this for internal program communication (§2.12(c)(3))?
│   ├── YES → Internal communication within Part 2 program permitted
│   │         (between personnel with need for information in connection with duties)
│   └── NO → Continue
│
├── Does the patient have a §2.33 TPO consent on file?
│   ├── YES → Is the disclosure for Treatment, Payment, or Healthcare Operations?
│   │   ├── YES → Disclosure permitted to HIPAA covered entities/BAs
│   │   │         Include re-disclosure notice
│   │   │         Anti-discrimination protections preserved
│   │   └── NO → Need specific consent (§2.31) or court order (§2.64)
│   │
│   └── NO → Continue to traditional consent
│
├── Does the patient have a specific §2.31 consent for this disclosure?
│   ├── YES → Verify all required elements present:
│   │   ├── [ ] Patient name
│   │   ├── [ ] Name of Part 2 program
│   │   ├── [ ] Recipient name/designation
│   │   ├── [ ] Purpose of disclosure
│   │   ├── [ ] Information to be disclosed (how much, what kind)
│   │   ├── [ ] Patient signature
│   │   ├── [ ] Date signed
│   │   ├── [ ] Revocability statement
│   │   ├── [ ] Expiration date/event/condition
│   │   └── [ ] Re-disclosure prohibition notice
│   │
│   │   All elements present and consent not expired/revoked?
│   │   ├── YES → Disclose as specified; include re-disclosure notice
│   │   └── NO → Cannot disclose; correct consent deficiency
│   │
│   └── NO → Is a court order available (§2.64)?
│       ├── YES → Disclose per court order scope; include re-disclosure notice
│       └── NO → Disclosure NOT permitted
│
└── STOP — Do not disclose Part 2 records
```

## Workflow 2: §2.33 TPO Consent Implementation

```
Patient Intake at SUD Treatment Program
│
├── Step 1: Explain §2.33 TPO consent option
│   ├── Explain that a single consent can cover future TPO disclosures
│   ├── Explain right to revoke at any time
│   ├── Explain anti-discrimination protections remain in effect
│   ├── Explain that recipients who are HIPAA entities may use under HIPAA
│   └── Explain alternative: traditional per-disclosure consent
│
├── Step 2: Patient decision
│   ├── Patient SIGNS §2.33 consent
│   │   ├── Record consent in EHR with effective date
│   │   ├── Flag SUD records for TPO sharing eligibility
│   │   ├── Enable automated HIE feeds for Part 2 records (if applicable)
│   │   └── Provide patient with copy of signed consent
│   │
│   └── Patient DECLINES §2.33 consent
│       ├── Document patient's decision in EHR
│       ├── SUD records remain segmented from standard PHI sharing
│       ├── Per-disclosure consent process applies for each disclosure
│       └── Reassess at future visits (do not coerce)
│
├── Step 3: Consent revocation
│   ├── Patient submits written revocation
│   ├── Effective prospectively only (prior disclosures remain valid)
│   ├── Update EHR consent status
│   ├── Disable automated PHI sharing for Part 2 records
│   └── Notify downstream recipients if feasible
│
└── Step 4: Ongoing management
    ├── Consent status visible to clinical staff in EHR
    ├── Consent review at each treatment encounter
    └── Annual consent audit for Part 2 program patients
```

## Workflow 3: Court Order Process (§2.64)

```
Need to Disclose Part 2 Records Without Patient Consent
│
├── Step 1: Determine if court order path is appropriate
│   ├── Is this for a civil, criminal, or administrative proceeding?
│   ├── Other disclosure methods unavailable or ineffective?
│   └── Public interest outweighs potential harm to patient?
│
├── Step 2: File application under seal
│   ├── Use fictitious name for patient
│   ├── Do NOT disclose patient-identifying information in application
│   ├── State good cause for disclosure
│   └── Serve notice on patient and Part 2 program (opportunity to respond)
│
├── Step 3: Court hearing
│   ├── Court evaluates good cause:
│   │   ├── Other means of obtaining information unavailable/ineffective?
│   │   └── Public interest > potential injury to patient/treatment relationship?
│   ├── If criminal investigation (§2.65): additional finding required
│   │   └── Crime is extremely serious (death or serious bodily injury)
│   └── Court issues order specifying scope of disclosure
│
├── Step 4: Comply with court order
│   ├── Disclose only information specified in the order
│   ├── Include re-disclosure prohibition notice
│   ├── Limit access to persons specified in the order
│   └── Document compliance with order
│
└── Note: A general subpoena is NOT sufficient for Part 2 records
    A specific Part 2 court order following §2.64 procedures is required
```
