# HIPAA Interoperability — Workflows

## Workflow 1: Information Blocking Exception Assessment

```
Request for EHI Access, Exchange, or Use Received
│
├── Step 1: Determine if Actor is Subject to Information Blocking Rules
│   ├── Health IT developer of certified health IT? → YES, subject
│   ├── Health information exchange (HIE)? → YES, subject
│   ├── Health information network (HIN)? → YES, subject
│   ├── Healthcare provider? → YES, subject
│   └── None of the above? → Not subject to information blocking rules
│
├── Step 2: Is the Practice Likely to Interfere with Access/Exchange/Use of EHI?
│   ├── NO → No information blocking concern; proceed normally
│   └── YES → Evaluate whether an exception applies
│
├── Step 3: Evaluate Applicable Exceptions (45 CFR Part 171)
│   │
│   ├── Privacy Exception (§171.202)?
│   │   ├── Is the practice required by HIPAA Privacy Rule?
│   │   ├── Is the practice permitted by HIPAA Privacy Rule and tailored to privacy risk?
│   │   ├── Does the practice satisfy all sub-requirements of §171.202?
│   │   └── If YES to all → Exception applies; document rationale
│   │
│   ├── Security Exception (§171.203)?
│   │   ├── Is the practice directly related to safeguarding C/I/A of EHI?
│   │   ├── Is the practice tailored to specific security risks?
│   │   ├── Is it implemented consistently and not discriminatory?
│   │   └── If YES to all → Exception applies; document rationale
│   │
│   ├── Preventing Harm Exception (§171.201)?
│   │   ├── Is there a reasonable belief that the practice will prevent harm?
│   │   ├── Is the practice no broader than necessary?
│   │   └── If YES to all → Exception applies; document rationale
│   │
│   ├── Infeasibility Exception (§171.204)?
│   │   ├── Is fulfillment segmented, technically infeasible, or infeasible due to uncontrollable events?
│   │   ├── Has the actor made reasonable efforts to fulfill?
│   │   └── If YES → Exception applies; document rationale
│   │
│   └── No exception applies?
│       └── Practice constitutes information blocking; must cease or modify
│
└── Step 4: Document Exception Determination
    ├── Record the request, the practice, the exception invoked
    ├── Document the factual basis supporting the exception
    ├── Retain documentation per organizational retention policy
    └── Periodically review whether the practice remains justified
```

## Workflow 2: Patient Access API (FHIR) Privacy Compliance

```
Patient Requests API Access to Health Data
│
├── Step 1: Identity Verification
│   ├── Authenticate patient using NIST IAL2/AAL2 standards
│   ├── Methods: patient portal credentials + MFA, or in-person identity proofing
│   ├── If identity cannot be verified → Deny access; offer alternative (in-person request)
│   └── Log authentication attempt and outcome
│
├── Step 2: Determine Scope of Access
│   ├── Right of access per §164.524 → Entire designated record set
│   │   ├── INCLUDE: clinical notes, lab results, imaging reports, claims data
│   │   └── EXCLUDE: psychotherapy notes (§164.524(a)(1)(i)), info compiled for litigation
│   ├── Minimum necessary does NOT apply to individual access (§164.502(b)(2)(v))
│   └── Map FHIR resources to designated record set content
│
├── Step 3: Third-Party App Authorization
│   ├── Patient selects third-party app to receive data?
│   │   ├── YES → Present disclosure notice:
│   │   │   ├── "Once shared with [App Name], your data may no longer be protected by HIPAA"
│   │   │   ├── "Review the app's privacy policy before authorizing"
│   │   │   └── Obtain patient confirmation to proceed
│   │   └── NO → Data delivered directly to patient portal
│   │
│   ├── SMART on FHIR authorization flow:
│   │   ├── App requests authorization with defined OAuth 2.0 scopes
│   │   ├── Patient reviews and approves requested scopes
│   │   ├── Access token issued with scope-limited permissions
│   │   └── Token expiration set per policy (recommended: 1 hour with refresh)
│   │
│   └── Log: app name, scopes authorized, timestamp, patient confirmation
│
├── Step 4: Data Delivery
│   ├── Serve FHIR R4 resources over TLS 1.2+
│   ├── Format per USCDI data classes and elements
│   ├── Include provenance metadata
│   └── Respond within 1 business day per §164.524(b)(2) where feasible
│
└── Step 5: Audit and Accounting
    ├── Log all API access in audit system (§164.312(b))
    ├── Maintain accounting of disclosures for third-party app access (§164.528)
    └── Retain logs for minimum 6 years
```

## Workflow 3: TEFCA Health Information Exchange

```
Health Information Exchange Request via TEFCA
│
├── Step 1: Validate Exchange Purpose
│   ├── Treatment → Verify requesting provider has treatment relationship
│   ├── Payment → Verify payer/plan relationship and coverage
│   ├── Healthcare Operations → Verify operations relationship
│   ├── Public Health → Verify requesting authority status
│   ├── Individual Access → Verify patient identity and authorization
│   └── Benefits Determination → Verify plan participant relationship
│
├── Step 2: Consent and Authorization Check
│   ├── Does state law require specific consent for this data type?
│   │   ├── 42 CFR Part 2 (substance abuse) → Patient consent required
│   │   ├── State-sensitive categories (HIV, mental health, genetic) → Check state law
│   │   └── Standard PHI → HIPAA TPO basis sufficient for treatment/payment/operations
│   │
│   ├── Is consent on file?
│   │   ├── YES → Proceed with exchange
│   │   └── NO → Request consent or apply consent exception if applicable
│   │
│   └── Apply consent directives (opt-in, opt-out) per organizational policy
│
├── Step 3: Apply Minimum Necessary
│   ├── Treatment purpose → Exception applies; provide full clinical information
│   ├── Payment/operations → Limit to minimum necessary for stated purpose
│   └── Individual access → Exception applies; provide full designated record set
│
├── Step 4: Execute Exchange
│   ├── Route through QHIN (Qualified Health Information Network)
│   ├── Apply TEFCA Common Agreement security requirements
│   ├── Encrypt in transit (TLS 1.2+)
│   ├── Include digital provenance and source attribution
│   └── Confirm receipt by receiving QHIN participant
│
└── Step 5: Post-Exchange Documentation
    ├── Log exchange: purpose, parties, data types, timestamp
    ├── Update accounting of disclosures (if applicable)
    ├── Retain exchange records per TEFCA and HIPAA requirements
    └── Report any exchange failures or anomalies to QHIN
```

## Workflow 4: Payer-to-Payer Data Exchange (CMS-0057-F)

```
Patient Switches Health Plan and Requests Data Transfer
│
├── Step 1: Patient Request Validation
│   ├── Verify patient identity with new plan
│   ├── Confirm patient has opted in to payer-to-payer exchange
│   ├── Obtain prior plan information from patient
│   └── Validate coverage dates with prior plan
│
├── Step 2: Prior Plan Data Assembly
│   ├── Prior plan assembles patient data:
│   │   ├── Claims and encounter data (minimum 5 years)
│   │   ├── Clinical data received via prior authorizations
│   │   └── Provider directory information relevant to patient
│   ├── Format per FHIR R4 and USCDI standards
│   └── Apply HIPAA minimum necessary to payment/operations data
│
├── Step 3: Secure Transfer
│   ├── FHIR Bulk Data export from prior plan
│   ├── Encrypted transfer to new plan via FHIR API
│   ├── Mutual TLS authentication between plan systems
│   └── Confirm data integrity upon receipt
│
├── Step 4: New Plan Data Integration
│   ├── Ingest and validate received data
│   ├── Map to new plan's data model
│   ├── Apply access controls per new plan's HIPAA policies
│   └── Make data available to patient via Patient Access API
│
└── Step 5: Documentation
    ├── Log transfer: date, data types, prior/new plan identifiers
    ├── Retain patient consent/opt-in record
    ├── Update accounting of disclosures at prior plan
    └── Retain records for 6 years
```
