# Storage Limitation Control Workflows

## Workflow 1: Implementing Automated Retention for a New Data Store

```
Step 1: Data Classification
├── Identify all personal data categories stored in the new system
├── Map each category to its processing purpose and lawful basis
├── Determine the applicable retention period for each category
├── Identify any statutory retention requirements (tax, AML, employment)
└── Document the retention trigger event for each category

Step 2: Schema Design
├── Add retention metadata columns:
│   ├── created_at (timestamp, set at record creation)
│   ├── retention_trigger_event (enum: account_closure, transaction_date, consent_withdrawal)
│   ├── retention_trigger_date (timestamp, set when trigger event occurs)
│   ├── ttl_expiry_date (timestamp, calculated from trigger + retention period)
│   └── legal_hold_id (nullable FK, set when legal hold applies)
├── Create indexes on ttl_expiry_date for efficient scanning
└── Configure database-level TTL if supported (Redis EXPIRY, DynamoDB TTL, Cassandra TTL)

Step 3: Lifecycle Job Implementation
├── Deploy daily expiry scanner that queries records where ttl_expiry_date < now()
├── Filter out records with active legal_hold_id
├── For each expired record batch:
│   ├── Check for downstream dependencies (cascade requirements)
│   ├── Move to warm storage if archival is required
│   ├── Execute hard delete from primary store
│   ├── Invalidate cached copies (Redis, CDN)
│   └── Log deletion event in immutable audit trail
└── Implement idempotent deletion to handle retry scenarios

Step 4: Verification
├── Run post-deletion verification query to confirm records removed
├── Check replica lag to ensure deletions propagated to read replicas
├── Verify cache invalidation for in-memory stores
├── Generate deletion report with record counts per data category
└── Alert if any records exceed TTL by more than 7 days without deletion

Step 5: Monitoring Setup
├── Dashboard: records approaching expiry (7-day lookahead)
├── Dashboard: deletion job success rate and latency
├── Alert: deletion job failure or timeout
├── Alert: records exceeding TTL by more than 7 days
├── Monthly: retention compliance report to DPO
└── Quarterly: retention policy review trigger
```

## Workflow 2: Legal Hold Lifecycle

```
Step 1: Hold Initiation
├── Legal counsel issues hold notice with:
│   ├── Matter reference (e.g., HOLD-2026-0023)
│   ├── Data categories in scope
│   ├── Date range (data created between start and end dates)
│   ├── Subject identifiers (if specific to individuals)
│   └── Estimated hold duration
├── Hold notice reviewed by DPO for scope appropriateness
└── Hold registered in the Legal Hold Registry

Step 2: Hold Enforcement
├── Retention Policy Engine creates exemption rule matching hold scope
├── Expiry scanner skips records matching the hold criteria
├── Affected records tagged with legal_hold_id in their metadata
├── Downstream deletion cascades suspended for held records
└── Confirmation sent to legal counsel with count of records held

Step 3: Hold Monitoring (Monthly)
├── Legal counsel reviews active holds for continued necessity
├── DPO reviews hold scope for minimal impact on routine retention
├── Generate report: number of records held, storage impact, affected categories
├── If hold no longer necessary, proceed to Step 4
└── If hold continues, document monthly review in hold registry

Step 4: Hold Release
├── Legal counsel issues release notice with matter reference
├── DPO co-approves the release (dual approval required)
├── Hold exemption removed from Retention Policy Engine
├── legal_hold_id cleared from affected records
└── Release event logged in immutable audit trail

Step 5: Catch-Up Deletion
├── Expiry scanner processes previously held records
├── Records that would have been deleted during the hold are now evaluated:
│   ├── If TTL has expired: delete per normal retention policy
│   ├── If TTL has not expired: resume normal lifecycle
│   └── If new hold applies: re-hold under new matter reference
├── Generate catch-up deletion report
└── Archive hold documentation with the matter file
```

## Workflow 3: Backup Retention and Crypto-Shredding

```
Step 1: Backup Policy Alignment
├── Inventory all backup systems (database backups, file backups, snapshots)
├── Map backup retention periods to the longest applicable data retention period
├── Ensure backup rotation schedule aligns with retention requirements
└── Document backup systems in the Article 30 processing register

Step 2: Crypto-Shredding Implementation
├── For systems where granular deletion from backups is impractical:
│   ├── Encrypt personal data with per-category Data Encryption Keys (DEKs)
│   ├── Store DEKs in a Key Management System (KMS) separate from backup storage
│   ├── When retention period expires, destroy the DEK in the KMS
│   ├── Backed-up data becomes cryptographically inaccessible (effectively deleted)
│   └── Document crypto-shredding event in deletion audit trail
├── For systems supporting granular backup deletion:
│   ├── Use point-in-time-recovery-aware deletion scripts
│   ├── Verify deletion across all backup copies
│   └── Rotate backup encryption keys on schedule
└── Test backup restore does not resurface deleted data

Step 3: Verification and Documentation
├── Quarterly: attempt restore of a sample backup to verify crypto-shredded data is inaccessible
├── Document verification results in compliance records
├── Review backup retention alignment at each policy review
└── Update Article 30 records when backup systems change
```
