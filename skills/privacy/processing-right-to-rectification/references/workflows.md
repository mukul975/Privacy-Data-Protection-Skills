# Right to Rectification Workflows

## Workflow 1: Rectification Request Processing

```
[Rectification Request Received]
         │
         ▼
[Identity Verification]
   ├── Verified ──► [Identify Affected Data Items]
   │                    │
   │                    ▼
   │            [Determine Rectification Type]
   │              ├── Correction of inaccuracy ──► [Verify correction]
   │              └── Completion of incomplete data ──► [Assess relevance]
   │
   └── Not Verified ──► [Request ID, pause clock]

[Verify Correction]
   │
   ├── Name/spelling ──► Accept subject's assertion
   ├── DOB ──► Request documentary evidence
   ├── Address ──► Accept for current, verify for historical
   ├── Employment ──► Accept assertion or verify with consent
   ├── Financial ──► Cross-reference source records
   └── Technical ──► Assess whether correction is factually possible
         │
         ▼
[Verification Outcome]
   ├── Confirmed inaccurate ──► [Implement rectification]
   ├── Inconclusive ──► [Apply Art. 18(1)(a) restriction, continue investigation]
   └── Confirmed accurate ──► [Notify subject, offer supplementary statement]
```

## Workflow 2: Multi-System Rectification

```
[Rectification Decision: CORRECT]
         │
         ▼
[Identify All Systems Holding Data]
   │
   ├── Primary Database ──► UPDATE record
   ├── CRM ──► UPDATE record
   ├── Marketing Platform ──► UPDATE record
   ├── Analytics System ──► UPDATE record + regenerate affected reports
   ├── Third-Party Processors ──► Issue Art. 19 notification
   └── Backup Systems ──► Flag for correction at next rotation
         │
         ▼
[Verify consistency across systems]
   - Query each system for the corrected value
   - Confirm all primary systems are synchronised
   - Document any systems pending correction (backups)
         │
         ▼
[Generate rectification log]
   - For each system: original value, corrected value, update timestamp
   - Implementation person
   - Verification confirmation
```

## Workflow 3: Art. 19 Notification for Rectification

```
[Rectification Implemented]
         │
         ▼
[Retrieve Art. 30 Recipient List]
         │
         ▼
[For Each Recipient]
   │
   ├── Send rectification notification
   │     - Data field corrected
   │     - New value
   │     - Instruction to update records
   │     - 14-day confirmation deadline
   │
   ├── Track response
   │     ├── Confirmed ──► Log confirmation
   │     ├── Query ──► Respond and resolve
   │     └── No response ──► Send reminder at day 14
   │
   └── [All recipients processed?]
         ├── Yes ──► Include in response to data subject
         └── No ──► Continue
```
