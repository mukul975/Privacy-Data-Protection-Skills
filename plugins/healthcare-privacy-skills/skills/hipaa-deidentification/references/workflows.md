# HIPAA De-Identification — Workflows

## Workflow 1: De-Identification Method Selection

```
PHI Dataset Requires De-Identification
│
├── Step 1: Determine intended use
│   ├── Research (no IRB waiver available) → De-identification needed
│   ├── Public release / open dataset → Strong de-identification needed
│   ├── Internal analytics → Consider limited data set alternative
│   ├── AI/ML model training → Assess based on model type and deployment
│   └── Regulatory reporting → Check if de-identification required
│
├── Step 2: Assess data utility requirements
│   ├── Are full dates needed? → Safe harbor removes dates; expert may retain with perturbation
│   ├── Are geographic details needed? → Safe harbor limits to 3-digit ZIP; expert may retain finer
│   ├── Are ages >89 needed? → Safe harbor aggregates to 90+; expert may retain with risk assessment
│   └── Is individual-level data needed? → If only aggregates, consider aggregation over de-identification
│
├── Step 3: Select method
│   │
│   ├── Safe Harbor (§164.514(b)(2))
│   │   ├── Advantages: Clear, prescriptive, defensible, no expert needed
│   │   ├── Disadvantages: May reduce data utility significantly
│   │   └── Best for: Standard releases, low-complexity datasets, when dates/geography not critical
│   │
│   ├── Expert Determination (§164.514(b)(1))
│   │   ├── Advantages: More data utility; tailored to specific dataset and use case
│   │   ├── Disadvantages: Requires qualified expert; more expensive; documentation burden
│   │   └── Best for: Research datasets needing dates/geography, complex datasets, AI training data
│   │
│   └── Limited Data Set (§164.514(e))
│       ├── Note: Still PHI — requires Data Use Agreement
│       ├── Advantages: Retains dates, city, state, ZIP code, ages >89
│       ├── Disadvantages: Still subject to Privacy Rule; restricted to research, public health, healthcare ops
│       └── Best for: Internal research, quality improvement, when full dates and geography needed
│
└── Document selection rationale
```

## Workflow 2: Safe Harbor De-Identification Process

```
Apply Safe Harbor Method
│
├── Step 1: Structured Data De-Identification
│   ├── For each of the 18 identifier categories:
│   │   ├── Names → Remove all
│   │   ├── Geographic data → Truncate ZIP to 3 digits; validate against Census 20K threshold
│   │   │   └── If 3-digit ZIP population ≤20,000 → Replace with 000
│   │   ├── Dates → Remove month and day; retain year only
│   │   │   └── Ages >89 → Replace all dates/ages with 90+
│   │   ├── Phone numbers → Remove all
│   │   ├── Fax numbers → Remove all
│   │   ├── Email addresses → Remove all
│   │   ├── SSN → Remove all
│   │   ├── MRN → Remove all (may assign random study ID per §164.514(c))
│   │   ├── Health plan ID → Remove all
│   │   ├── Account numbers → Remove all
│   │   ├── Certificate/license numbers → Remove all
│   │   ├── Vehicle identifiers → Remove all
│   │   ├── Device identifiers → Remove all
│   │   ├── Web URLs → Remove all
│   │   ├── IP addresses → Remove all
│   │   ├── Biometric identifiers → Remove all
│   │   ├── Full-face photographs → Remove all
│   │   └── Other unique identifiers → Remove (except permitted re-identification code)
│   │
│   └── Verify: no actual knowledge that remaining information can identify
│
├── Step 2: Unstructured Data (Clinical Notes) De-Identification
│   ├── Run NLP/NER to identify identifiers in free text
│   ├── Redact identified entities (replace with category tags: [NAME], [DATE], [LOCATION])
│   ├── Human review sample (minimum 10%) for NER accuracy
│   ├── If NER accuracy < 95%, expand human review or retrain NER model
│   └── Document NER methodology and accuracy metrics
│
├── Step 3: Imaging Data De-Identification
│   ├── Strip DICOM headers of all patient identifiers
│   ├── Remove private DICOM tags
│   ├── Review for burned-in annotations (patient name, MRN on images)
│   ├── Apply defacing algorithms to facial photographs
│   └── Validate with DICOM header audit tool
│
├── Step 4: Quality Assurance
│   ├── Automated re-scan of output for residual identifiers
│   │   (regex patterns for SSN, phone, email, MRN formats; name dictionary matching)
│   ├── Cross-reference output against source data for accidental inclusion
│   ├── Statistical uniqueness check (are any records unique on remaining quasi-identifiers?)
│   └── Document QA results and sign-off
│
└── Step 5: Release Approval
    ├── Privacy Officer review and approval
    ├── Confirm no actual knowledge of identifiability
    ├── Document safe harbor compliance for the dataset
    └── Release dataset with de-identification certification
```

## Workflow 3: Limited Data Set with Data Use Agreement

```
Limited Data Set Release Requested
│
├── Step 1: Verify permitted purpose
│   ├── [ ] Research
│   ├── [ ] Public health
│   ├── [ ] Healthcare operations
│   └── If none of the above → Cannot use limited data set; use full de-identification
│
├── Step 2: Prepare limited data set
│   ├── Remove direct identifiers: names, street addresses, phone/fax/email, SSN, MRN,
│   │   health plan ID, account numbers, certificate/license numbers, vehicle/device IDs,
│   │   URLs, IP addresses, biometric identifiers, full-face photographs
│   ├── RETAIN: dates, city, state, ZIP code, ages (including >89)
│   └── Verify no additional identifiers beyond permitted elements
│
├── Step 3: Execute Data Use Agreement (§164.514(e)(4))
│   ├── DUA must include:
│   │   ├── Permitted uses and purposes
│   │   ├── Authorized persons to use/receive
│   │   ├── Prohibition on further use/disclosure beyond DUA
│   │   ├── Appropriate safeguards requirement
│   │   ├── Unauthorized use/disclosure reporting obligation
│   │   ├── Agent binding requirement
│   │   └── Prohibition on identifying or contacting individuals
│   ├── Legal review of DUA
│   └── Both parties sign DUA
│
└── Step 4: Release with monitoring
    ├── Transmit limited data set via secure channel
    ├── Log release in disclosure accounting (limited data set disclosures are excluded from accounting)
    ├── Retain DUA for 6 years
    └── Monitor for DUA violations
```
