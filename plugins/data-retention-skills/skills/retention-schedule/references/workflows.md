# Data Retention Schedule Workflows

## Workflow 1: New Data Category Retention Period Determination

```
[New Data Category Identified]
         │
         ▼
[Identify Processing Purpose(s)]
         │
         ▼
[Determine Legal Basis (Art. 6)]
         │
         ▼
[Scan Statutory Retention Requirements]
   ├── Tax/fiscal requirements?
   ├── Company law requirements?
   ├── Employment law requirements?
   ├── Sector-specific requirements?
   └── Limitation periods?
         │
         ▼
[Calculate Retention Period]
   - Statutory minimum (longest applicable)
   - Contractual necessity (duration + post-contract period)
   - Limitation period buffer
   - Proportionality check
         │
         ▼
[Document Justification]
   - Complete Retention Period Justification Template
   - Attach supporting legal references
         │
         ▼
[DPO Review and Approval]
   ├── Approved ──► Add to retention schedule
   └── Not Approved ──► Revise period with DPO guidance
         │
         ▼
[Update Retention Schedule Matrix]
[Update ROPA (Art. 30)]
[Update Privacy Notice (Art. 13/14)]
[Configure technical enforcement]
```

## Workflow 2: Annual Retention Schedule Review

```
[Annual Review Trigger — Q1]
         │
         ▼
[Legislative Scan]
   - Check for new or amended statutes affecting retention
   - Check for new regulatory guidance
   - Check for relevant court decisions
         │
         ▼
[For Each Data Category]
   │
   ├── [Has the legal basis changed?]
   │     ├── Yes ──► Reassess retention period
   │     └── No ──► Continue
   │
   ├── [Has the processing purpose changed?]
   │     ├── Yes ──► Reassess retention period
   │     └── No ──► Continue
   │
   ├── [Have applicable statutory requirements changed?]
   │     ├── Yes ──► Update retention period
   │     └── No ──► Continue
   │
   └── [Is the current period still proportionate?]
         ├── Yes ──► Confirm — no change
         └── No ──► Adjust period (shorten or extend with justification)
         │
         ▼
[Update Schedule with Review Date]
[Publish Updated Schedule]
[Reconfigure Technical Enforcement]
```

## Workflow 3: Retention Period Trigger Event Processing

```
[Trigger Event Occurs]
   (e.g., account closure, contract termination, employment end)
         │
         ▼
[System Records Trigger Event Date]
         │
         ▼
[Calculate Deletion Date]
   Deletion Date = Trigger Date + Retention Period
         │
         ▼
[Metadata Updated on All Affected Records]
   - trigger_event_date: [date]
   - calculated_deletion_date: [date]
   - data_category: [CAT-XXX]
         │
         ▼
[Record Enters Retention Monitoring]
   - 30-day pre-expiry alert configured
   - Added to deletion queue for calculated_deletion_date
         │
         ▼
[On Deletion Date]
   ├── Check: Litigation hold? ──► Suspend deletion
   ├── Check: Retention exception? ──► Apply exception
   └── No holds/exceptions ──► Execute deletion per auto-deletion-workflow
```
