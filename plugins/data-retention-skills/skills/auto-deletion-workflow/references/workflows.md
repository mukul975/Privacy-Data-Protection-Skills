# Automated Deletion Workflows

## Workflow 1: Retention Expiry Deletion Pipeline

```
[Daily Scan — 02:00 UTC]
         │
         ▼
[Query: Records WHERE calculated_deletion_date <= TODAY]
         │
         ▼
[Generate Deletion Batch]
   - Group by data category
   - Group by target system
   - Assign batch reference: BATCH-DEL-YYYY-NNNN
         │
         ▼
[Pre-Deletion Checks]
   ├── Litigation hold check ──► Skip if held
   ├── Retention exception check ──► Skip if excepted
   ├── Pending DSAR check ──► Coordinate with DSAR workflow
   └── All checks passed ──► Proceed
         │
         ▼
[Execute Deletion — System by System]
   ├── Primary databases ──► DELETE/PURGE operations
   ├── Data warehouse ──► DELETE operations
   ├── File storage ──► File deletion
   ├── Email systems ──► Mailbox content removal
   ├── Application caches ──► Cache invalidation
   └── Third-party processors ──► Art. 19 notification
         │
         ▼
[Post-Deletion Verification]
   - Query each system for deleted records
   - Expected: zero results
   - Log verification result
         │
         ▼
[Generate Confirmation Record]
[Update Audit Trail]
```

## Workflow 2: Art. 17 On-Demand Erasure Deletion

```
[Verified Erasure Request — Priority: HIGH]
         │
         ▼
[Data Discovery Scan]
   - Scan all registered data stores
   - Identify all instances of data subject's data
   - Generate Deletion Manifest (DEL-YYYY-NNNN)
         │
         ▼
[Exception Assessment]
   ├── Art. 17(3)(a): Freedom of expression? ──► Exclude if applies
   ├── Art. 17(3)(b): Legal obligation? ──► Exclude (anonymize)
   ├── Art. 17(3)(c): Public health? ──► Exclude if applies
   ├── Art. 17(3)(d): Archiving/research? ──► Exclude if applies
   └── Art. 17(3)(e): Legal claims? ──► Exclude (litigation hold)
         │
         ▼
[DPO Approval of Deletion Manifest]
         │
         ▼
[Execute High-Priority Deletion]
   (Same system-by-system process as Workflow 1)
         │
         ▼
[Third-Party Notification (Art. 19)]
   - Notify all Art. 30 recipients
   - 14-day confirmation deadline
         │
         ▼
[Backup Flagging]
   - Flag data subject in suppression list
   - Mark backups for deletion at next rotation
         │
         ▼
[Data Subject Response]
   - Confirm deletion within 30-day timeline
   - Include: systems processed, exceptions applied, backup timeline
```

## Workflow 3: Cascading Dependency Resolution

```
[Primary Record Flagged for Deletion]
         │
         ▼
[Load Dependency Map]
         │
         ▼
[Depth-First Dependency Scan]
   │
   ├── Level 0: Primary record
   ├── Level 1: Direct FK dependents
   ├── Level 2: Secondary dependents
   └── Level 3+: Deep dependents
         │
         ▼
[For Each Dependent]
   │
   ├── Shared dependency? ──► Nullify FK only
   ├── Retention override? ──► Anonymize link, retain record
   └── No constraints? ──► Add to deletion manifest
         │
         ▼
[Build Deletion Order]
   Deepest ──► ... ──► Level 1 ──► Level 0
         │
         ▼
[Execute in Reverse Depth Order]
   (Prevents referential integrity violations)
```
