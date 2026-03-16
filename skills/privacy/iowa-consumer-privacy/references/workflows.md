# Workflows — Iowa ICDPA

## Workflow 1: ICDPA Applicability Assessment

```
TRIGGER: Organization operates in or targets Iowa consumers
  │
  ├─► Step 1: Iowa Nexus Determination
  │     ├─ Confirm business operations in Iowa
  │     ├─ OR confirm products/services target Iowa consumers
  │     └─ Document nexus determination
  │
  ├─► Step 2: Threshold Calculation
  │     ├─ Count Iowa consumers (calendar year basis)
  │     ├─ Exclude data processed solely for payment transactions
  │     ├─ Calculate revenue percentage from sale of personal data
  │     ├─ Threshold 1: >= 100,000 Iowa consumers
  │     └─ Threshold 2: >= 25,000 consumers AND > 50% revenue from sale
  │
  ├─► Step 3: Exemption Check
  │     ├─ Entity-level: government, GLBA, HIPAA, nonprofit, higher ed
  │     └─ Data-level: GLBA, HIPAA, FERPA, FCRA, DPPA, COPPA data
  │
  └─► Step 4: Document Determination
        ├─ Record applicable/not applicable with basis
        ├─ Set annual review date for re-assessment
        └─ If applicable: proceed to compliance workflows
```

## Workflow 2: Consumer Rights Request Processing

```
START: Iowa consumer submits privacy request (after January 1, 2025)
  │
  ├─► Step 1: Intake and Classification
  │     ├─ Assign tracking ID: IA-REQ-YYYY-NNNNN
  │     ├─ Record receipt date (Day 0 of 90-day clock)
  │     ├─ Classify request type:
  │     │     ├─ Access (§715D.4(1)(a))
  │     │     ├─ Deletion (§715D.4(1)(b))
  │     │     └─ Opt-out: sale or targeted advertising (§715D.4(1)(c))
  │     └─ Note: No right to correct or portability under Iowa law
  │
  ├─► Step 2: Identity Verification
  │     ├─ Apply commercially reasonable verification methods
  │     ├─ Match consumer identity to records
  │     └─ If unable to verify: request additional information
  │
  ├─► Step 3: Process Request (within 90 days)
  │     ├─ Access: compile personal data and generate report
  │     ├─ Deletion: identify all data stores, execute deletion, confirm
  │     └─ Opt-out: update processing flags, confirm to downstream processors
  │
  ├─► Step 4: Respond to Consumer
  │     ├─ Fulfill request OR deny with specific basis
  │     ├─ Inform consumer of right to appeal
  │     └─ Record response date and outcome
  │
  └─► Step 5: Appeal Process (if consumer appeals)
        ├─ Log appeal and assign reviewer
        ├─ Respond within 60 days
        ├─ If appeal denied: inform consumer of right to contact Iowa AG
        │     └─ Provide AG contact: consumer@ag.iowa.gov
        └─ Document appeal outcome
```

## Workflow 3: Sensitive Data Consent Management

```
TRIGGER: Processing activity involves Iowa sensitive data categories
  │
  ├─► Step 1: Identify Sensitive Data
  │     ├─ Racial or ethnic origin
  │     ├─ Religious beliefs
  │     ├─ Health diagnosis
  │     ├─ Sexual orientation
  │     ├─ Citizenship or immigration status
  │     ├─ Genetic or biometric data
  │     ├─ Known child data
  │     └─ Precise geolocation
  │
  ├─► Step 2: Obtain Opt-In Consent
  │     ├─ Present clear consent request before processing
  │     ├─ Consent must be freely given, specific, informed
  │     ├─ Record consent: timestamp, scope, mechanism
  │     └─ Do NOT process until consent obtained
  │
  ├─► Step 3: Maintain Consent Records
  │     ├─ Store consent evidence with processing record
  │     ├─ Enable consumer to withdraw consent
  │     └─ Cease processing upon withdrawal
  │
  └─► Step 4: Periodic Review
        ├─ Verify active consent for ongoing processing
        └─ Re-consent if purpose or scope changes
```

## Workflow 4: AG Enforcement Response

```
TRIGGER: Iowa AG issues notice of alleged ICDPA violation
  │
  ├─► Step 1: Receive and Log Notice (Day 0)
  │     ├─ Record date of receipt
  │     ├─ Identify alleged violation(s)
  │     └─ Escalate to privacy counsel and DPO
  │
  ├─► Step 2: Investigation (Days 1-30)
  │     ├─ Assess validity of alleged violation
  │     ├─ Identify root cause
  │     ├─ Determine scope of impact
  │     └─ Develop remediation plan
  │
  ├─► Step 3: Remediation (Days 31-75)
  │     ├─ Implement corrective measures
  │     ├─ Test and validate fixes
  │     └─ Document all remediation steps
  │
  ├─► Step 4: Cure Response (before Day 90)
  │     ├─ Prepare written statement of cure
  │     ├─ Detail violations identified and corrected
  │     ├─ Provide evidence of remediation
  │     ├─ Include future prevention measures
  │     └─ Submit to AG before 90-day deadline
  │
  └─► Step 5: Post-Cure Monitoring
        ├─ Monitor for recurrence
        ├─ Update compliance procedures
        └─ Retain all documentation
```
