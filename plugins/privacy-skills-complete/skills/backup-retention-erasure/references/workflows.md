# Backup Retention and Erasure Workflows

## Workflow 1: Backup Erasure for Art. 17 Request

```
[Art. 17 Erasure Completed on Primary Systems]
         │
         ▼
[Data Subject's Data Exists in Backup Sets?]
   ├── No ──► Erasure complete; no backup action needed
   └── Yes ──► Continue
         │
         ▼
[When Does Next Backup Rotation Occur?]
   │
   ├── Within 90 days ──► [Standard Path]
   │     - Apply "beyond use" controls immediately
   │     - Add data subject to suppression list
   │     - Document expected backup deletion date
   │     - Inform data subject of backup timeline
   │     - Await rotation for automatic deletion
   │
   └── Beyond 90 days ──► [Restore-and-Delete Path]
         - Assess cost-benefit of restore-and-delete
         - If proportionate: execute restore-and-delete procedure
         - If disproportionate: document reasoning; apply beyond-use controls
         - Inform data subject of timeline
         │
         ▼
[Confirm Backup Deletion]
   - Verify backup set containing data has been rotated/destroyed
   - Update erasure confirmation record
   - Notify data subject (if still within response window)
```

## Workflow 2: Disaster Recovery with Erasure Compliance

```
[Disaster Recovery Event — Backup Restoration Required]
         │
         ▼
[Select Backup Set for Restoration]
         │
         ▼
[Pre-Restoration Check]
   - Does this backup pre-date any completed erasure requests?
   - Does this backup pre-date any retention expiry deletions?
         │
         ▼
[Retrieve Suppression List]
   (All data subjects whose data has been deleted since backup date)
         │
         ▼
[Restore Backup to Production]
         │
         ▼
[IMMEDIATELY Execute Re-Deletion]
   │
   ├── Automated: Run pre-built deletion script against suppression list
   │     (Script tested quarterly — must exist and be current)
   │
   └── If automated fails: Manual deletion within 24 hours
         │
         ▼
[Verify Re-Deletion]
   - Query for all suppression list entries
   - Expected: zero results
         │
         ▼
[Log Re-Deletion Event]
   - Record in erasure confirmation records
   - Record in DR incident log
         │
         ▼
[Resume Normal Operations]
```

## Workflow 3: Backup Retention Alignment Audit

```
[Quarterly Audit Trigger]
         │
         ▼
[For Each Backup Tier (daily, weekly, monthly, quarterly, annual)]
   │
   ├── [Retention period ≤ longest applicable data category period?]
   │     ├── Yes ──► Compliant
   │     └── No ──► COMPLIANCE GAP
   │           ├── Segregate shorter-retention data into separate backup sets
   │           ├── Or reduce backup tier retention
   │           └── Or document "beyond use" controls + accept overshoot (max 90 days)
   │
   ├── [All backup sets encrypted?]
   │     ├── Yes ──► Compliant
   │     └── No ──► REMEDIATE immediately
   │
   ├── [Suppression list current?]
   │     ├── Yes ──► Compliant
   │     └── No ──► UPDATE — add missing data subjects
   │
   └── [Restore-and-delete script tested?]
         ├── Yes (within last quarter) ──► Compliant
         └── No ──► SCHEDULE test immediately
         │
         ▼
[Generate Audit Report]
[Remediate Findings]
[Report to DPO]
```
