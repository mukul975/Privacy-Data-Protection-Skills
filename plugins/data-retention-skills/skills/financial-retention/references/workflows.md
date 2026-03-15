# Financial Records Retention Workflows

## Workflow 1: Financial Record Retention Assignment

```
[New Financial Record Created / Received]
         │
         ▼
[Classify Record]
   - Assign Financial Data Category (FIN-001 through FIN-015)
   - Identify applicable jurisdictions
         │
         ▼
[Determine Retention Period]
   - Look up category in retention schedule
   - If multi-jurisdictional: apply longest period
   - Identify trigger event (financial year end, tax year end, transaction date, etc.)
         │
         ▼
[Tag Record with Metadata]
   - data_category: [FIN-XXX]
   - trigger_event_date: [date]
   - calculated_deletion_date: [date]
   - statutory_basis: [cite statute]
   - jurisdiction: [UK/EU/US]
         │
         ▼
[Store on Compliant Storage]
   - Immutable/WORM if required (audit, AML)
   - Encrypted at rest (AES-256)
   - Access restricted to authorized personnel
         │
         ▼
[Enter Retention Monitoring]
```

## Workflow 2: Art. 17 Request Against Financial Records

```
[Art. 17 Erasure Request Received — Financial Records Identified]
         │
         ▼
[For Each Financial Data Category Held]
   │
   ├── [Statutory retention period still active?]
   │     │
   │     ├── Yes ──► [Exception: Art. 17(3)(b)]
   │     │           │
   │     │           ├── Inform data subject:
   │     │           │   "Your financial records are retained under [statute]
   │     │           │    until [date]. Deletion is not possible until then."
   │     │           │
   │     │           ├── Apply data minimization:
   │     │           │   Delete non-essential fields not required by statute
   │     │           │
   │     │           └── Restrict access:
   │     │               Compliance/legal team only for remainder of period
   │     │
   │     └── No ──► [Delete per normal erasure workflow]
   │
   └── [Provide Art. 15 access if requested]
         (Financial retention does NOT suspend access rights)
         │
         ▼
[Document Response]
   - Which categories deleted
   - Which categories retained (with statute citation)
   - Data minimization applied
   - Access restriction applied
   - Expected deletion date for retained categories
```

## Workflow 3: Annual Financial Retention Review

```
[Annual Review — October]
         │
         ▼
[Legislative Scan]
   - HMRC updates
   - Companies Act amendments
   - FCA handbook changes
   - MiFID II/FCA COBS updates
   - MLR/AMLD amendments
   - SOX/SEC updates (if US-listed)
         │
         ▼
[For Each Financial Category (FIN-001 to FIN-015)]
   │
   ├── [Statutory period changed?]
   │     ├── Yes ──► Update retention schedule
   │     └── No ──► Confirm current period
   │
   ├── [New regulatory guidance issued?]
   │     ├── Yes ──► Assess impact on retention period
   │     └── No ──► Continue
   │
   └── [Records approaching expiry this year?]
         ├── Yes ──► Verify deletion scheduling; check litigation holds
         └── No ──► Continue
         │
         ▼
[Update Financial Retention Schedule]
[Report to Audit Committee]
```
