---
name: auto-deletion-workflow
description: >-
  Implements automated data deletion workflows for GDPR Article 17 right to erasure and
  retention period expiry. Covers cascading deletion across dependent systems, dependency
  handling for referential integrity, confirmation logging, and audit trail generation.
  Activate for automated deletion, erasure automation, data purge, retention expiry queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-retention-deletion
  tags: "automated-deletion, right-to-erasure, gdpr-article-17, data-purge, retention-expiry"
---

# Automated Data Deletion Workflow

## Overview

Automated deletion workflows ensure that personal data is removed from all systems when retention periods expire or when a valid erasure request is received under GDPR Article 17. Manual deletion at scale is error-prone and fails to meet the storage limitation principle consistently. This skill defines the architecture, logic, and operational procedures for building automated deletion pipelines that handle cascading dependencies, maintain referential integrity, produce audit-grade confirmation logs, and satisfy both scheduled retention expiry and on-demand erasure requests.

## Legal Foundation

### GDPR Article 17(1) — Right to Erasure

The data subject shall have the right to obtain from the controller the erasure of personal data concerning him or her without undue delay, and the controller shall have the obligation to erase personal data without undue delay where one of the specified grounds applies.

### GDPR Article 5(1)(e) — Storage Limitation

Personal data shall be kept for no longer than is necessary for the purposes for which the personal data are processed. Automated deletion is the primary technical measure for enforcing this principle at scale.

### GDPR Article 25(1) — Data Protection by Design

The controller shall implement appropriate technical and organisational measures designed to implement data-protection principles, such as data minimisation, in an effective manner. Automated deletion is a core by-design control.

### GDPR Article 30(1)(f) — Envisaged Time Limits for Erasure

Records of processing activities must include, where possible, the envisaged time limits for erasure of the different categories of data. Automated deletion systems operationalize these envisaged time limits.

## Automated Deletion Architecture

### Deletion Trigger Types

| Trigger Type | Source | SLA | Priority |
|-------------|--------|-----|----------|
| Retention expiry | Retention schedule metadata reaching calculated deletion date | Within 30 days of expiry | Standard |
| Data subject erasure request | Verified Art. 17 request via DSAR workflow | Within 30 calendar days of verified request | High |
| Consent withdrawal | Consent management platform event | Within 30 days (best practice: 72 hours) | High |
| Account closure | Customer account termination event | Per retention schedule (post-closure retention period) | Standard |
| Purpose completion | Processing purpose fulfilled, no further legal basis | Within 30 days of purpose completion | Standard |
| Legal hold release | Litigation hold lifted by Legal counsel | Within 14 days of hold release | Standard |

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   DELETION ORCHESTRATOR                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │  Trigger      │  │  Dependency  │  │  Execution       │  │
│  │  Engine       │  │  Resolver    │  │  Engine          │  │
│  │              │  │              │  │                  │  │
│  │ - Scheduled   │  │ - FK mapping │  │ - System agents  │  │
│  │ - Event-driven│  │ - Cascade    │  │ - API calls      │  │
│  │ - On-demand   │  │   rules      │  │ - Direct DB ops  │  │
│  │ - Hold check  │  │ - Orphan     │  │ - File system    │  │
│  │              │  │   handling   │  │   purge          │  │
│  └──────┬───────┘  └──────┬───────┘  └────────┬─────────┘  │
│         │                 │                    │             │
│         └────────┬────────┘                    │             │
│                  ▼                             │             │
│  ┌──────────────────────────┐                 │             │
│  │  Deletion Job Queue      │─────────────────┘             │
│  │  (Priority-ordered)      │                               │
│  └──────────────────────────┘                               │
│                  │                                           │
│                  ▼                                           │
│  ┌──────────────────────────┐  ┌──────────────────────────┐ │
│  │  Confirmation Logger     │  │  Audit Trail Generator   │ │
│  │  - Per-system status     │  │  - Immutable audit log   │ │
│  │  - Completion timestamp  │  │  - Deletion certificate  │ │
│  │  - Verification hash     │  │  - Regulatory report     │ │
│  └──────────────────────────┘  └──────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Deletion Workflow Procedures

### Workflow 1: Scheduled Retention Expiry Deletion

```
[Daily Retention Scan — 02:00 UTC]
         │
         ▼
[Query all records where calculated_deletion_date <= TODAY + 30 days]
         │
         ▼
[For each record approaching expiry]
   │
   ├── [Check: Active litigation hold?]
   │     ├── Yes ──► [Skip — log hold reference, notify Legal]
   │     └── No ──► Continue
   │
   ├── [Check: Active regulatory investigation?]
   │     ├── Yes ──► [Skip — log investigation reference]
   │     └── No ──► Continue
   │
   ├── [Check: Pending data subject request referencing this data?]
   │     ├── Yes ──► [Coordinate with DSAR workflow]
   │     └── No ──► Continue
   │
   ├── [Check: Retention exception approved?]
   │     ├── Yes ──► [Skip — log exception reference and expiry]
   │     └── No ──► Continue
   │
   ▼
[Add to deletion job queue with priority: STANDARD]
         │
         ▼
[On calculated_deletion_date: Execute deletion]
```

### Workflow 2: On-Demand Erasure Request Deletion

```
[Verified Art. 17 Erasure Request Received]
         │
         ▼
[Data Discovery — Identify all instances of data subject's data]
   │
   ├── Primary databases (CRM, ERP, HR system)
   ├── Data warehouse and analytics platforms
   ├── File storage (SharePoint, network drives, cloud storage)
   ├── Email and communication systems
   ├── Backup and archive systems
   ├── Third-party processor systems
   └── Logs and audit trails
         │
         ▼
[Generate Deletion Manifest]
   Reference: DEL-YYYY-NNNN
   Data Subject: [Pseudonymised reference]
   Systems identified: [List with record counts]
   Exceptions identified: [Any Art. 17(3) exceptions]
   Estimated completion: [Date]
         │
         ▼
[DPO Review and Approval]
   ├── Approved ──► [Add to deletion job queue with priority: HIGH]
   └── Exceptions found ──► [Partial deletion — exclude excepted data]
         │
         ▼
[Execute deletion across all identified systems]
```

### Workflow 3: Cascading Deletion Logic

When deleting a primary record, dependent records across related systems must also be deleted. The cascading deletion resolver handles referential integrity:

```
[Primary Record Identified for Deletion]
         │
         ▼
[Load Dependency Map for Record Type]
         │
         ▼
[Resolve Dependencies — Depth-First Traversal]
   │
   ├── [Level 0: Primary record]
   │     Example: Customer record in CRM
   │
   ├── [Level 1: Direct dependents]
   │     Example: Orders, support tickets, consent records
   │
   ├── [Level 2: Secondary dependents]
   │     Example: Order line items, payment records, shipping records
   │
   └── [Level 3+: Tertiary dependents]
         Example: Invoice line items, refund records
         │
         ▼
[For each dependent record]
   │
   ├── [Shared dependency?]
   │     (Record also linked to other primary records not being deleted)
   │     ├── Yes ──► [Nullify foreign key — do NOT delete]
   │     └── No ──► [Add to deletion manifest]
   │
   ├── [Legal retention override?]
   │     (Dependent record has its own statutory retention requirement)
   │     ├── Yes ──► [Anonymize link to primary record, retain dependent]
   │     └── No ──► [Add to deletion manifest]
   │
   └── [Aggregated/statistical record?]
         (Record contributes to aggregated reporting)
         ├── Yes ──► [Anonymize — remove personal identifiers, retain aggregate]
         └── No ──► [Add to deletion manifest]
         │
         ▼
[Execute deletion in reverse order (deepest dependents first)]
   Level 3+ ──► Level 2 ──► Level 1 ──► Level 0
```

## Dependency Map Template

The following dependency map is configured for Orion Data Vault Corp:

| Primary Entity | Dependent Entity | Relationship | Deletion Action | Retention Override |
|---------------|-----------------|-------------|-----------------|-------------------|
| Customer | Orders | 1:N | Cascade delete (after statutory retention) | 6 years — HMRC |
| Customer | Support Tickets | 1:N | Cascade delete | 3 years — limitation period |
| Customer | Consent Records | 1:N | Cascade delete | Retain suppression record |
| Customer | Marketing Preferences | 1:1 | Cascade delete | Retain opt-out on suppression list |
| Customer | Account Audit Log | 1:N | Anonymize (nullify customer reference) | 7 years — audit retention |
| Order | Order Lines | 1:N | Cascade delete | Follows order retention |
| Order | Payment Records | 1:N | Anonymize | 6 years — financial records |
| Order | Shipping Records | 1:N | Cascade delete | Follows order retention |
| Order | Invoices | 1:N | Anonymize | 6 years — tax records |
| Employee | Payroll Records | 1:N | Cascade delete (after statutory retention) | 6 years — PAYE Regulations |
| Employee | Performance Reviews | 1:N | Cascade delete | Duration of employment + 6 years |
| Employee | Access Logs | 1:N | Anonymize | 2 years — security retention |

## Confirmation Logging

### Deletion Confirmation Record Structure

Every deletion execution produces an immutable confirmation record:

```
DELETION CONFIRMATION RECORD — Orion Data Vault Corp
-----------------------------------------------------
Reference: DEL-2026-0142
Trigger: Retention expiry / Art. 17 request / Consent withdrawal
Data Subject Reference: DS-HASH-a3f8c2e1
Request Date: 2026-02-15 (if applicable)
Execution Date: 2026-03-14
Completed Date: 2026-03-14T14:23:07Z

SYSTEMS PROCESSED:
┌─────────────────────────┬──────────┬───────────────┬──────────────────┐
│ System                  │ Records  │ Action        │ Status           │
├─────────────────────────┼──────────┼───────────────┼──────────────────┤
│ CRM (Salesforce)        │ 1        │ Hard delete   │ Confirmed        │
│ ERP (SAP)               │ 47       │ Hard delete   │ Confirmed        │
│ Data Warehouse (BQ)     │ 312      │ Hard delete   │ Confirmed        │
│ Email (Exchange)        │ 23       │ Hard delete   │ Confirmed        │
│ File Storage (S3)       │ 8        │ Hard delete   │ Confirmed        │
│ Backup (Veeam)          │ N/A      │ Flagged       │ Pending (cycle)  │
│ Analytics (Mixpanel)    │ 156      │ Hard delete   │ Confirmed        │
│ Support (Zendesk)       │ 12       │ Hard delete   │ Confirmed        │
│ Audit Log               │ 89       │ Anonymized    │ Confirmed        │
│ Payment (Stripe)        │ 5        │ Anonymized    │ Confirmed        │
└─────────────────────────┴──────────┴───────────────┴──────────────────┘

THIRD-PARTY NOTIFICATIONS (Art. 19):
- Processor A (Analytics SaaS): Notified 2026-03-14, confirmed 2026-03-16
- Processor B (Email service): Notified 2026-03-14, confirmed 2026-03-15
- Processor C (Payment gateway): Notified 2026-03-14, pending

EXCEPTIONS APPLIED:
- Financial records (invoices): Anonymized, retained until 2032-03-14 (6-year statutory period)
- Audit log entries: Anonymized, retained until 2033-03-14 (7-year audit retention)

BACKUP DELETION:
- Backup system: Next full rotation cycle completes 2026-06-12
- Expected complete erasure from backups: 2026-06-12

VERIFICATION:
- Post-deletion scan completed: 2026-03-14T14:45:00Z
- Residual data found: None
- Verification hash: SHA-256:e3b0c44298fc1c149afbf4c8996fb924...

Executed by: Deletion Orchestrator v3.2 (automated)
Reviewed by: [DPO Name] (for Art. 17 requests only)
```

### Audit Trail Requirements

1. **Immutability**: Deletion confirmation records are written to an append-only audit log (write-once storage or blockchain-anchored hash).
2. **Retention of confirmation records**: 3 years from deletion date (sufficient to demonstrate compliance if challenged).
3. **No personal data in logs**: Confirmation records reference data subjects by pseudonymised identifier only — never by name, email, or other direct identifier.
4. **Searchability**: Records must be searchable by deletion reference, data subject hash, trigger type, system, and date range.

## Error Handling and Retry Logic

### Deletion Failure Handling

| Failure Type | Action | Retry | Escalation |
|-------------|--------|-------|------------|
| System unavailable | Queue for retry | 3 attempts at 1h, 4h, 24h intervals | Alert IT Operations after 3 failures |
| Permission denied | Log error, flag for manual review | No automatic retry | Escalate to system administrator |
| Referential integrity violation | Route to dependency resolver | Re-resolve dependencies, retry | Escalate to DPO if unresolvable |
| Partial deletion (some records failed) | Log successful deletions, retry failed | 3 attempts | Escalate to IT + DPO |
| Third-party processor non-response | Send reminder at 7 days | Follow up at 14 days | Escalate to DPO + Legal at 21 days |
| Backup system — cannot delete from active backup | Flag for next rotation cycle | Monitor backup rotation schedule | Alert if not completed within 90 days |

### Rollback Considerations

Deletion is inherently irreversible. Therefore:

1. **Pre-deletion snapshot**: For Art. 17 requests, take a temporary encrypted snapshot of the data to be deleted. Retain for 72 hours after deletion execution to allow for error correction. Auto-destroy after 72 hours.
2. **Staged execution**: For large-scale retention expiry deletions (>10,000 records), execute in batches of 1,000 with verification between batches.
3. **Dry-run mode**: All new deletion rules must be tested in dry-run mode for 30 days before activation. Dry-run produces the deletion manifest and confirmation record without executing actual deletion.

## Monitoring and Reporting

### Key Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Retention expiry deletion completion rate | 99.5% within 30 days of expiry | Monthly |
| Art. 17 erasure request completion rate | 100% within 30 calendar days | Per request |
| Average deletion execution time | < 4 hours (end-to-end across all systems) | Per execution |
| Failed deletion rate | < 0.5% | Monthly |
| Backup deletion completion rate | 100% within backup rotation cycle | Per rotation |
| Third-party processor confirmation rate | 100% within 14 days | Per notification |

### Quarterly Compliance Report

The automated deletion system generates a quarterly report containing:

1. Total records deleted by trigger type (retention expiry, Art. 17, consent withdrawal, etc.)
2. Deletion completion rates against SLA targets
3. Exceptions applied (with legal basis breakdown)
4. Failed deletions and resolution status
5. Third-party processor compliance rates
6. Backup deletion status and outstanding items
7. Trend analysis (volume growth, system coverage, performance)
