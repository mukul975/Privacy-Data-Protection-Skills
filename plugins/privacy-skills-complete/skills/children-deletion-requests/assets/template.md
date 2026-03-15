# Children's Data Deletion Request Report

## Request Information

| Field | Value |
|-------|-------|
| **Reference** | DEL-CHILD-2026-0284 |
| **Controller** | BrightPath Learning Inc. |
| **Request Date** | 2026-02-15 |
| **Requester** | Parent (verified via account credentials) |
| **Child** | Account child_bp_8f3a2d (age 11, France) |
| **Scope** | Full account deletion |
| **Deadline** | 2026-03-15 (30 days per Art. 12(3)) |

## Processing Timeline

| Stage | Status | Date | Notes |
|-------|--------|------|-------|
| 1. Acknowledgement | Completed | 2026-02-16 | Email sent to parent within 48 hours |
| 2. Identity verification | Completed | 2026-02-16 | Account credentials + security question |
| 3. Scope determination | Completed | 2026-02-17 | Full account; download offered (declined) |
| 4. Primary deletion | Completed | 2026-02-17 | All primary systems cleared |
| 5. Third-party notification | Completed | 2026-02-17 | AWS notified (hosting provider) |
| 6. Backup purge | Scheduled | 2026-03-17 | 30-day backup rotation |
| 7. Confirmation | Completed | 2026-02-17 | Email sent to parent |

## Deletion Scope

| Category | Action | Notes |
|----------|--------|-------|
| Account data | DELETED | Name, age, parent email |
| Activity logs | DELETED | All session and usage data |
| Learning progress | DELETED | Scores, assessments, progress data |
| Content created | DELETED | Download offered; parent declined |
| Communications | DELETED | No active safeguarding investigation |
| Consent records | RETAINED | Legal compliance (expires 2032-02-17) |
| Backup copies | SCHEDULED | Purge by 2026-03-17 |

## Exceptions Applied

| Exception | Art. 17(3) Ground | Data Retained | Expiry |
|-----------|------------------|---------------|--------|
| Consent records | Art. 17(3)(b) Legal obligation | Consent ID, dates, verification outcome | 2032-02-17 |

## Third-Party Notifications

| Recipient | Notification Date | Scope | Confirmation |
|-----------|------------------|-------|-------------|
| AWS (hosting) | 2026-02-17 | All stored objects | Confirmed 2026-02-18 |

## Post-Deletion Verification

| System | Verified Clear | Date |
|--------|:-------------:|------|
| Primary database | Yes | 2026-02-17 |
| Search index | Yes | 2026-02-17 |
| Redis cache | Yes | 2026-02-17 |
| File storage (S3) | Yes | 2026-02-17 |
| Analytics DB | Yes | 2026-02-17 |
| Backups | Pending | Scheduled 2026-03-17 |

## Sign-Off

| Role | Name | Date |
|------|------|------|
| Data Operations | Erik Svensson | 2026-02-17 |
| DPO | Dr. Claudia Meier | 2026-02-17 |
