# HITECH Act Privacy — Workflows

## Workflow 1: HITECH Penalty Tier Assessment

```
HIPAA Violation Identified
│
├── Step 1: Determine Culpability Level
│   │
│   ├── Did the entity know about the violation?
│   │   ├── NO → Did not know AND would not have known with reasonable diligence?
│   │   │   └── YES → Tier A (Did Not Know)
│   │   │   └── NO → Tier B (Reasonable Cause)
│   │   │
│   │   └── YES → Was it willful neglect?
│   │       ├── NO → Tier B (Reasonable Cause)
│   │       └── YES → Was it corrected within 30 days of knowledge?
│   │           ├── YES → Tier C (Willful Neglect, Timely Corrected)
│   │           └── NO → Tier D (Willful Neglect, Not Corrected)
│   │                     Investigation and penalty MANDATORY
│
├── Step 2: Determine Penalty Range (2024 inflation-adjusted)
│   │
│   ├── Tier A: $137 - $68,928 per violation; $2,067,813 annual cap
│   ├── Tier B: $1,379 - $68,928 per violation; $2,067,813 annual cap
│   ├── Tier C: $13,785 - $68,928 per violation; $2,067,813 annual cap
│   └── Tier D: $68,928 - $2,067,813 per violation; $2,067,813 annual cap
│
├── Step 3: Mitigating Factors
│   ├── Recognized security practices in place for 12+ months (§13412)?
│   │   ├── NIST CSF implementation
│   │   ├── HITRUST certification
│   │   └── Section 405(d) HICP practices
│   ├── History of compliance
│   ├── Financial condition of the entity
│   ├── Cooperation with OCR investigation
│   └── Number of individuals affected
│
└── Step 4: Resolution
    ├── Informal resolution (technical assistance)
    ├── Resolution agreement (settlement + corrective action plan)
    └── Civil monetary penalty (formal adjudication)
```

## Workflow 2: State AG HIPAA Enforcement Process

```
State AG Identifies Potential HIPAA Violation
│
├── Step 1: Investigation
│   ├── Consumer complaints received by AG office
│   ├── Breach affecting state residents identified
│   ├── Investigation of entity practices in the state
│   └── Coordinate with state consumer protection division
│
├── Step 2: Mandatory HHS Notice
│   ├── State AG must notify HHS Secretary before filing suit
│   ├── Provide HHS with details of intended action
│   └── HHS has right to intervene and assume primary responsibility
│
├── Step 3: Is there a pending HHS action?
│   ├── YES → State AG may NOT bring action during pending HHS action
│   └── NO → State AG may proceed
│
├── Step 4: Civil Action in Federal District Court
│   ├── File on behalf of state residents affected
│   ├── Seek injunctive relief
│   ├── Seek damages (up to $100/violation, $25,000/year per identical violation)
│   ├── Seek attorneys' fees and costs
│   └── May proceed alongside state consumer protection claims
│
└── Step 5: Resolution
    ├── Consent decree / settlement agreement
    ├── Injunctive orders requiring compliance improvements
    ├── Monetary penalties paid to the state
    └── Monitoring and reporting obligations
```

## Workflow 3: Promoting Interoperability Privacy Attestation

```
CMS Promoting Interoperability Program Reporting Period
│
├── Step 1: Security Risk Analysis
│   ├── Conduct or review security risk analysis (required for attestation)
│   ├── Document analysis covers all ePHI
│   ├── Address identified risks with security updates
│   └── Correct identified security deficiencies
│
├── Step 2: Privacy Measure Compliance
│   ├── Patient electronic access to health information
│   │   ├── Provide portal access within 36 hours of availability
│   │   └── Measure: >80% of patients offered access
│   ├── Secure messaging
│   │   └── Patients can send secure messages to care team
│   ├── Electronic prescribing
│   │   └── Prescriptions transmitted electronically
│   └── Health information exchange
│       └── Support interoperability with external providers
│
├── Step 3: Attestation
│   ├── Attest that security risk analysis was conducted
│   ├── Attest that security deficiencies were corrected
│   ├── Report on privacy-related measures
│   └── Submit attestation to CMS within reporting period
│
└── Failure to Attest
    ├── Payment adjustment (penalty for non-participation)
    ├── Hardship exceptions available in limited circumstances
    └── Future participation requirements
```
