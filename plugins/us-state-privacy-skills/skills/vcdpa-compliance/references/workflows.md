# Workflows — VCDPA Compliance

## Workflow 1: Consumer Rights Request Processing

```
START: Virginia consumer submits privacy request
  │
  ├─► Step 1: Residency and Applicability Check
  │     ├─ Confirm consumer is a Virginia resident (natural person, not acting in commercial/employment context)
  │     ├─ Confirm Liberty Commerce Inc. meets VCDPA thresholds for this consumer
  │     └─ If not applicable → inform consumer and suggest applicable state law
  │
  ├─► Step 2: Right Classification
  │     ├─ Right to Access (§59.1-577(A)(1))
  │     ├─ Right to Correct (§59.1-577(A)(2))
  │     ├─ Right to Delete (§59.1-577(A)(3))
  │     ├─ Right to Portability (§59.1-577(A)(4))
  │     └─ Right to Opt Out (§59.1-577(A)(5)) — targeted ads, sale, profiling
  │
  ├─► Step 3: Authentication
  │     ├─ Use commercially reasonable methods to authenticate request
  │     ├─ Do not require creation of new account for verification
  │     └─ If unable to authenticate → may request additional information
  │
  ├─► Step 4: Process Request (within 45 days)
  │     ├─ Access: Compile personal data, categories, sources, purposes, third parties
  │     ├─ Correct: Verify inaccuracy, update records, propagate to processors
  │     ├─ Delete: Execute deletion, notify processors to delete
  │     ├─ Portability: Generate data export in portable, machine-readable format
  │     └─ Opt-Out: Apply opt-out preferences (targeted ads, sale, profiling)
  │
  ├─► Step 5: Response Delivery
  │     ├─ Provide response within 45 days (extendable by 45 days with notice)
  │     ├─ At least one free response per 12-month period
  │     ├─ If denied: provide basis for denial and instructions for appeal
  │     └─ Inform consumer of right to appeal
  │
  └─► Step 6: Appeal Process (§59.1-578(C))
        ├─ Consumer may appeal denial within reasonable time
        ├─ Controller must respond to appeal within 60 days
        ├─ If appeal denied: inform consumer of right to contact Virginia AG
        └─ Provide AG contact information: oag.state.va.us
```

## Workflow 2: Sensitive Data Consent Collection

```
START: Business activity requires processing of sensitive data from Virginia consumer
  │
  ├─► Step 1: Identify Sensitive Data Category
  │     ├─ Racial/ethnic origin
  │     ├─ Religious beliefs
  │     ├─ Mental/physical health diagnosis
  │     ├─ Sexual orientation
  │     ├─ Citizenship/immigration status
  │     ├─ Genetic/biometric data for identification
  │     ├─ Precise geolocation (within 1,750 feet)
  │     └─ Known child's personal data
  │
  ├─► Step 2: Design Consent Mechanism
  │     ├─ Present consent request with clear description of:
  │     │     ├─ Specific sensitive data category
  │     │     ├─ Purpose of processing
  │     │     ├─ Third parties who may receive the data
  │     │     └─ Right to withdraw consent
  │     ├─ Use unticked checkbox or equivalent affirmative action
  │     └─ Do not bundle with non-sensitive data consent
  │
  ├─► Step 3: Record Consent
  │     ├─ Consumer ID, timestamp, consent text version
  │     ├─ Sensitive data category, purpose
  │     ├─ Mechanism (checkbox, toggle, typed statement)
  │     └─ Store in consent management system
  │
  ├─► Step 4: Process Data
  │     ├─ Only after consent is obtained and recorded
  │     ├─ Process strictly within consented purpose
  │     └─ Apply data minimization per §59.1-578(A)(1)
  │
  └─► Step 5: Consent Withdrawal
        ├─ Consumer may withdraw consent at any time
        ├─ Withdrawal must be as easy as granting consent
        ├─ Upon withdrawal: cease processing for that purpose
        └─ Does not affect lawfulness of prior processing based on consent
```

## Workflow 3: Data Protection Impact Assessment

```
TRIGGER: New or modified processing activity involving targeted advertising, sale, profiling, or sensitive data
  │
  ├─► Step 1: Determine if DPIA Required (§59.1-580)
  │     ├─ Targeted advertising? → YES
  │     ├─ Sale of personal data? → YES
  │     ├─ Profiling with risk of significant effects? → YES
  │     ├─ Sensitive data processing? → YES
  │     └─ Other heightened risk of harm? → ASSESS
  │
  ├─► Step 2: Document Processing Activity
  │     ├─ Description of processing operations
  │     ├─ Categories of personal data involved
  │     ├─ Purpose and necessity of processing
  │     ├─ Categories of consumers affected
  │     └─ Third-party recipients
  │
  ├─► Step 3: Identify and Weigh Benefits vs. Risks
  │     ├─ Benefits to controller, consumer, and public
  │     ├─ Potential risks to consumers:
  │     │     ├─ Unfair/deceptive treatment or disparate impact
  │     │     ├─ Financial, physical, or reputational injury
  │     │     ├─ Physical intrusion or surveillance
  │     │     └─ Other substantial injury
  │     └─ Consider context and consumer expectations
  │
  ├─► Step 4: Mitigation Measures
  │     ├─ Consider de-identification or pseudonymization
  │     ├─ Implement purpose limitation controls
  │     ├─ Apply data minimization
  │     └─ Implement consumer rights mechanisms (opt-out for targeted ads, sale, profiling)
  │
  ├─► Step 5: Document and Review
  │     ├─ Prepare DPIA report
  │     ├─ Legal review and sign-off
  │     ├─ Retain for at least 5 years
  │     └─ Must be made available to AG upon request (§59.1-580(D))
  │
  └─► Step 6: Ongoing Monitoring
        ├─ Review DPIA when processing activity changes
        ├─ Annual reassessment
        └─ Update upon new risk indicators or enforcement developments
```
