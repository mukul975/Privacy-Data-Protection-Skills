# Workflows — Special Category Data Classification

## Workflow 1: Special Category Data Identification and Mapping

### Purpose
Systematically identify all instances of Art. 9 special category data across enterprise systems and map each to an appropriate processing condition.

### Process Flow

```
START: System or processing activity under review
  │
  ├─► Step 1: Data Element Extraction
  │     - Extract complete field/column inventory from system schema
  │     - Include derived fields, calculated fields, and free-text fields
  │     - Include data received from third parties and processors
  │     Output: Complete data element inventory for the system
  │
  ├─► Step 2: Automated Pre-Screening
  │     - Run field name pattern matching against special category indicators
  │     - Scan free-text fields with NLP for health terms, political references,
  │       religious references, genetic identifiers
  │     - Check for biometric template formats (ISO 19795, ANSI/INCITS 378)
  │     - Flag ICD-10/ICD-11 codes, genetic marker identifiers (rs-numbers)
  │     Output: Pre-screened data elements with confidence scores
  │
  ├─► Step 3: Manual Classification Review
  │     For each flagged element:
  │     3a. Determine which of the eight Art. 9(1) categories applies
  │     3b. Assess whether the data directly reveals OR permits inference of
  │         special category information (per Österreichische Post C-300/21)
  │     3c. For biometric data: confirm whether processing is "for the purpose
  │         of uniquely identifying" (Art. 9(1) qualifier)
  │     3d. For photographs: distinguish storage (not special category) from
  │         facial recognition processing (special category)
  │     Output: Confirmed special category classification per element
  │
  ├─► Step 4: Processing Condition Mapping
  │     For each confirmed special category element:
  │     4a. Identify the applicable Art. 9(2) processing condition
  │     4b. Verify the condition is supported by:
  │         - For (a): Evidence of explicit consent meeting EDPB WP259rev.01 standard
  │         - For (b): Specific EU or Member State employment law authorisation
  │         - For (f): Specific legal claim or proceeding
  │         - For (g): EU or Member State substantial public interest law
  │         - For (h): Processing under supervision of health professional
  │     4c. Confirm Art. 6 lawful basis is also established
  │     Output: Processing condition mapping with supporting evidence
  │
  ├─► Step 5: DPIA Trigger Assessment
  │     - Assess whether processing is "on a large scale" per Art. 35(3)(b)
  │     - If large scale: confirm DPIA has been conducted or initiate one
  │     - If not large scale: document the scale assessment reasoning
  │     Output: DPIA status for each special category processing activity
  │
  └─► Step 6: Documentation and Governance
        - Update Art. 30 Records of Processing with special category flags
        - Record Art. 9(2) condition per processing activity
        - Apply "Restricted" classification label
        - Set enhanced access controls and audit logging
        - Schedule review (6-monthly for special category data)
        Output: Complete special category data register
```

## Workflow 2: Explicit Consent Collection for Art. 9(2)(a)

### Purpose
Implement compliant explicit consent collection for special category data processing that satisfies Art. 9(2)(a) and EDPB WP259rev.01 requirements.

### Process Flow

```
START: Processing requires explicit consent under Art. 9(2)(a)
  │
  ├─► Step 1: Consent Design
  │     - Draft specific consent statement identifying:
  │       • The specific special category data to be processed
  │       • The specific purpose for processing
  │       • The identity of the controller
  │       • Any recipients of the data
  │       • The right to withdraw consent at any time
  │     - Ensure consent request is separate from other terms/agreements
  │     - Use clear, plain language — no legal jargon
  │     Output: Draft consent statement
  │
  ├─► Step 2: Explicit Consent Mechanism
  │     Select appropriate mechanism per EDPB guidance:
  │     - Written signed statement (paper forms)
  │     - Electronic form with affirmative checkbox (not pre-ticked)
  │       with additional confirmation step (double opt-in)
  │     - Oral statement with recording (telephone banking)
  │     - Two-factor consent: initial selection + confirmation email/SMS
  │     Output: Configured consent mechanism
  │
  ├─► Step 3: Freely Given Assessment
  │     Verify consent can be freely given:
  │     - No power imbalance that vitiates free choice
  │       (employer-employee: consent rarely appropriate — Swedish DPA school case)
  │     - No conditionality on service provision (Art. 7(4))
  │     - Genuine alternative available if consent refused
  │     - No detriment for refusing consent
  │     Output: Freely given assessment record
  │
  ├─► Step 4: Deployment and Record-Keeping
  │     - Deploy consent mechanism
  │     - Record: who consented, when, what they were told, how consent was given
  │     - Implement withdrawal mechanism (as easy to withdraw as to give)
  │     - Configure data processing to check consent status before each use
  │     Output: Operational consent management
  │
  └─► Step 5: Ongoing Monitoring
        - Monitor consent withdrawal rates (high rates may indicate consent
          was not truly freely given)
        - Refresh consent if processing purpose or scope changes
        - Conduct annual review of consent validity
        Output: Consent monitoring dashboard
```

## Workflow 3: Inference Detection — Protecting Against Implicit Special Category Processing

### Purpose
Identify processing operations that derive or infer special category data from non-special-category inputs, per the Österreichische Post AG ruling (C-300/21).

### Process Flow

```
START: Analytics, profiling, or AI processing activity under review
  │
  ├─► Step 1: Input-Output Mapping
  │     - Document all input data elements
  │     - Document all output data elements, including derived attributes
  │     - Document all intermediate calculations and model features
  │     Output: Complete data lineage for the processing activity
  │
  ├─► Step 2: Inference Risk Assessment
  │     For each output or intermediate attribute, assess:
  │     - Could this attribute reveal racial or ethnic origin?
  │       (e.g., postcode + surname model → ethnic origin inference)
  │     - Could this attribute reveal political opinions?
  │       (e.g., media consumption patterns → political affinity score)
  │     - Could this attribute reveal religious beliefs?
  │       (e.g., transaction patterns showing religious donations)
  │     - Could this attribute reveal trade union membership?
  │       (e.g., payroll patterns showing periodic deductions)
  │     - Could this attribute reveal health status?
  │       (e.g., purchase patterns revealing pharmaceutical purchases)
  │     - Could this attribute reveal sexual orientation?
  │       (e.g., household composition data, partner details)
  │     Output: Inference risk register
  │
  ├─► Step 3: Classification Decision
  │     IF inference of special category data is a purpose of the processing
  │       → SPECIAL CATEGORY DATA (Art. 9 applies in full)
  │     IF inference is an unintended but foreseeable byproduct
  │       → SPECIAL CATEGORY DATA (per C-300/21, intent is irrelevant)
  │     IF inference is purely theoretical and not operationalised
  │       → Document risk, implement safeguards, monitor
  │     Output: Classification with reasoning
  │
  └─► Step 4: Remediation
        IF classified as special category:
        - Establish Art. 9(2) processing condition
        - Conduct DPIA if large-scale
        - Implement purpose limitation to prevent special category inference
        - Consider whether the processing can be redesigned to avoid inference
        Output: Remediation plan or processing redesign
```
