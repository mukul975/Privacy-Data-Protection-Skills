# Workflows — Turkey KVKK Compliance

## Workflow 1: KVKK Compliance Programme Implementation

```
TRIGGER: Organisation processes personal data of individuals in Turkey
  │
  ├─► Phase 1: Applicability and Registration
  │     ├─ Step 1.1: Determine if the organisation is a data controller under KVKK
  │     │     ├─ Does the organisation determine the purpose and means of processing?
  │     │     └─ Is personal data of individuals in Turkey being processed?
  │     │
  │     ├─ Step 1.2: Assess VERBIS registration obligation
  │     │     ├─ Does the organisation have 50+ employees?
  │     │     ├─ Does annual turnover exceed TRY 100 million?
  │     │     ├─ Is the core activity processing special category data?
  │     │     └─ If any threshold met: register with VERBIS
  │     │
  │     ├─ Step 1.3: Complete VERBIS registration
  │     │     ├─ Prepare processing inventory: purposes, data categories, recipients
  │     │     ├─ Document retention periods for each category
  │     │     ├─ Submit registration via VERBIS portal
  │     │     └─ Appoint a contact person registered with the Authority
  │     │
  │     └─ Step 1.4: Appoint a data controller representative
  │           (required for controllers not established in Turkey)
  │
  ├─► Phase 2: Legal Basis Mapping
  │     ├─ Step 2.1: For each processing activity, identify legal basis under Article 5:
  │     │     ├─ Explicit consent (Article 5(1))
  │     │     ├─ Expressly provided by law (Article 5(2)(a))
  │     │     ├─ Protection of life or physical integrity (Article 5(2)(b))
  │     │     ├─ Contract performance (Article 5(2)(c))
  │     │     ├─ Legal obligation (Article 5(2)(d))
  │     │     ├─ Manifestly made public (Article 5(2)(e))
  │     │     ├─ Establishment/exercise/defence of right (Article 5(2)(f))
  │     │     └─ Legitimate interest (Article 5(2)(g))
  │     │
  │     ├─ Step 2.2: For special category data, identify basis under Article 6:
  │     │     ├─ Explicit consent of data subject
  │     │     ├─ Express authorisation by law (non-health/sexual life categories)
  │     │     └─ Health/sexual life: processing by authorised persons under secrecy
  │     │
  │     └─ Step 2.3: Document legal basis for each activity in processing register
  │
  ├─► Phase 3: Data Subject Rights Implementation
  │     ├─ Step 3.1: Establish Article 11 rights request intake mechanism
  │     │     ├─ Written application form available on website
  │     │     ├─ Designated email address for data subject requests
  │     │     └─ Registered mail acceptance for formal applications
  │     │
  │     ├─ Step 3.2: Implement 30-day response process
  │     │     ├─ Acknowledge receipt of application
  │     │     ├─ Verify identity of applicant
  │     │     ├─ Process request within 30 days (free of charge for first request)
  │     │     └─ If request is complex or requires additional data: may charge
  │     │         reasonable fee per Board communique
  │     │
  │     └─ Step 3.3: Document refusal mechanism
  │           ├─ Provide written reasons for any refusal
  │           └─ Inform data subject of right to complain to the Board (Article 14)
  │
  ├─► Phase 4: Security Measures (Article 12)
  │     ├─ Step 4.1: Implement technical measures per Board Communique:
  │     │     ├─ Access control and authorisation management
  │     │     ├─ Encryption of personal data at rest and in transit
  │     │     ├─ Logging and monitoring of access to personal data
  │     │     ├─ Vulnerability scanning and penetration testing
  │     │     └─ Backup and disaster recovery
  │     │
  │     ├─ Step 4.2: Implement organisational measures:
  │     │     ├─ Data protection policies and procedures
  │     │     ├─ Staff training and awareness programme
  │     │     ├─ Confidentiality agreements with employees
  │     │     ├─ Incident response plan for data breaches
  │     │     └─ Periodic security audits
  │     │
  │     └─ Step 4.3: Data processor contracts
  │           ├─ Written agreement with each data processor
  │           ├─ Include security requirements per Article 12
  │           └─ Specify that processor acts only on controller instructions
  │
  └─► Phase 5: Ongoing Compliance
        ├─ Step 5.1: Monitor Board decisions and communiques
        ├─ Step 5.2: Update VERBIS registration when processing changes
        ├─ Step 5.3: Conduct annual data protection audit
        ├─ Step 5.4: Renew staff training annually
        └─ Step 5.5: Review and update retention schedule
```

## Workflow 2: Cross-Border Transfer Assessment (Article 9)

```
TRIGGER: Need to transfer personal data outside Turkey
  │
  ├─► Step 1: Identify Transfer Mechanism (Post-2024 Amendment)
  │     ├─ Option A: Transfer to a country with Board-declared adequate protection
  │     │     (Note: as of early 2026, no adequacy list has been published)
  │     ├─ Option B: Standard contractual clauses approved by the Board
  │     ├─ Option C: Binding corporate rules approved by the Board
  │     ├─ Option D: Written undertaking of adequate protection with Board approval
  │     └─ Option E: Explicit consent of the data subject (with derogation conditions)
  │
  ├─► Step 2: Prepare Transfer Documentation
  │     ├─ Document the data categories and data subjects involved
  │     ├─ Identify the receiving entity and country
  │     ├─ Assess the data protection framework of the recipient country
  │     ├─ Draft or execute appropriate transfer mechanism
  │     └─ Submit for Board approval if required (Options C and D)
  │
  ├─► Step 3: Board Application (if required)
  │     ├─ Submit application to the Board with:
  │     │     ├─ Description of the transfer
  │     │     ├─ Proposed safeguards
  │     │     ├─ Copy of the binding agreement or BCRs
  │     │     └─ Assessment of recipient country protections
  │     ├─ Await Board decision (processing time varies)
  │     └─ Do not commence transfer until Board approval received
  │
  └─► Step 4: Record and Monitor
        ├─ Record approved transfers in VERBIS
        ├─ Monitor for changes in recipient country's legal framework
        ├─ Review transfers annually
        └─ Update Board if transfer circumstances change materially
```

## Workflow 3: Data Breach Notification (Article 12(5))

```
TRIGGER: Discovery of a personal data breach
  │
  ├─► Step 1: Internal Assessment (within 24 hours)
  │     ├─ Confirm breach has occurred
  │     ├─ Determine scope: categories of data, number of data subjects
  │     ├─ Assess likely consequences
  │     └─ Activate incident response team
  │
  ├─► Step 2: Board Notification (within 72 hours)
  │     ├─ Notify the Personal Data Protection Board via the Authority's
  │     │   online breach notification system
  │     ├─ Include: nature of breach, data categories, data subject count,
  │     │   possible consequences, measures taken and proposed
  │     └─ If full information unavailable: provide initial notification
  │         and supplement as information becomes available
  │
  ├─► Step 3: Data Subject Notification
  │     ├─ Determine if breach poses high risk to data subjects
  │     ├─ If high risk: notify affected data subjects as soon as possible
  │     ├─ Notification method: directly where possible, otherwise via
  │     │   publication on the controller's website
  │     └─ Include recommended protective actions for data subjects
  │
  └─► Step 4: Post-Breach Actions
        ├─ Conduct root cause analysis
        ├─ Implement remediation measures
        ├─ Update security measures per Article 12
        ├─ Cooperate with Board investigation if initiated
        └─ Document breach in internal register
```
