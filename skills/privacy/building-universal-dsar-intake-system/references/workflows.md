# Universal DSAR Intake System Workflows

## Workflow 1: End-to-End Request Lifecycle

```
[Request Received (any channel)]
         │
         ▼
[Channel Adapter: Normalise to Standard Format]
   ├── Web form ──► Auto-parse fields
   ├── Email ──► Extract key fields (NLP/rules)
   ├── Telephone ──► Agent completes intake form
   ├── Postal ──► Scan + digitise + manual entry
   └── In-person ──► Staff completes intake form
         │
         ▼
[Create Record in Central Register]
   - Assign reference: [TYPE]-YYYY-NNNN
   - Set receipt timestamp
   - Classify request type
   - Detect jurisdiction
         │
         ▼
[Identity Verification]
   ├── Tier 1 ──► Auto-verified
   ├── Tier 2 ──► Request 2 data points
   └── Tier 3 ──► Request ID + authorisation
         │
         ▼
[Route to Assignee]
   - Apply routing matrix
   - Set priority
   - Calculate deadline
   - Send acknowledgement
         │
         ▼
[Process Request]
   - Collect data from systems
   - Apply exemptions
   - Compile response
   - QA review
   - DPO sign-off
         │
         ▼
[Deliver Response]
   - Secure delivery method
   - Record delivery confirmation
         │
         ▼
[Close and Archive]
   - Update register
   - Retain for 3 years
```

## Workflow 2: SLA Monitoring and Escalation

```
[Daily SLA Check (automated)]
         │
         ▼
[For Each Open Request]
   │
   ├── Days elapsed < 20 ──► Green (on track)
   │
   ├── Days elapsed = 20 ──► Amber
   │     └── Alert assignee + team lead
   │
   ├── Days elapsed = 25 ──► Red
   │     └── Alert DPO
   │
   ├── Days elapsed = 28 and no extension notified ──► Critical
   │     └── Alert DPO + General Counsel
   │         DPO must decide: extend or emergency response
   │
   └── Days elapsed > 30 (no extension) ──► Overdue
         └── Alert DPO + General Counsel + CEO
             Compliance breach — document and remediate
```

## Workflow 3: Email Channel Intake

```
[Email Received at dsar@meridiananalytics.co.uk]
         │
         ▼
[Auto-parser: Extract Key Fields]
   - Sender name and email
   - Request type keywords:
     "access" / "copy of my data" ──► DSAR
     "delete" / "erase" / "remove" ──► Erasure
     "correct" / "update" / "wrong" ──► Rectification
     "unsubscribe" / "stop marketing" ──► Marketing opt-out
     "export" / "transfer" / "portability" ──► Portability
     "opt out" / "do not sell" ──► CCPA opt-out
   - Data subject identifiers in body/signature
         │
         ▼
[Confidence Score]
   ├── High (clear request type + identifiers) ──► Auto-create record
   │     Send auto-acknowledgement
   │
   ├── Medium (ambiguous request type) ──► Create record as "unclassified"
   │     Assign to triage queue for manual review
   │
   └── Low (unclear if it's a rights request) ──► Send to triage queue
         Manual review within 2 business days
```

## Workflow 4: Multi-Jurisdiction Request Handling

```
[Request Received]
         │
         ▼
[Determine Data Subject Jurisdiction]
   │
   ├── UK/EEA resident ──► GDPR workflow
   │     Deadline: 30 calendar days
   │     Extension: up to 60 additional days
   │
   ├── California resident ──► CCPA workflow
   │     Deadline: 45 calendar days
   │     Extension: up to 45 additional days
   │
   ├── Colorado/Connecticut/Virginia resident ──► State privacy law workflow
   │     Deadline: 45 calendar days
   │     Extension: up to 15 additional days
   │
   └── Other jurisdiction ──► Assess applicable law
         Default to GDPR standard if uncertain
         Consult DPO for novel jurisdictions
```

## Workflow 5: Response Assembly

```
[Request Processing Complete]
         │
         ▼
[Select Response Template by Request Type]
         │
         ▼
[Assemble Modular Components]
   │
   ├── Cover letter (auto-generated from template)
   ├── Right-specific content (pre-written paragraphs)
   ├── Data extract (system-generated)
   ├── Supplementary information (Art. 15(1)(a)-(h) block)
   ├── Redaction log (if applicable)
   ├── Third-party notification log (if applicable)
   ├── Rights information block
   └── DPO sign-off
         │
         ▼
[QA Review Checklist]
   - All GDPR article elements addressed?
   - Data extract complete?
   - Redactions justified?
   - Deadline met?
   - Plain language?
   - Secure delivery method?
   - DPO sign-off?
         │
         ▼
[Approved?]
   ├── Yes ──► Deliver via secure channel
   └── No ──► Return to assignee with QA notes
```
