# Data Retention Schedule Template

## Organization Details

| Item | Value |
|------|-------|
| Organization | Prism Data Systems AG |
| Schedule Version | 3.2 |
| Effective Date | 2026-01-01 |
| Approved By | Dr. Lukas Meier (DPO), Anna Kowalski (CTO) |
| Next Review Date | 2026-07-01 |

## Retention Schedule

### Customer Data

| Data Category | Purpose | Lawful Basis | Retention Period | Trigger Event | Archival | Deletion Method | Legal Reference |
|--------------|---------|-------------|-----------------|---------------|----------|-----------------|-----------------|
| Account credentials | Authentication | Art. 6(1)(b) | Contract duration + 30 days | Account closure | No | Hard delete + cache invalidation | Art. 5(1)(e) |
| Profile information | Service delivery | Art. 6(1)(b) | Contract duration + 90 days | Account closure | Warm: 90 days | Hard delete | Art. 5(1)(e), Art. 17(1)(a) |
| Billing records | Tax compliance | Art. 6(1)(c) | 10 years | Transaction date | Warm: 1 year, Cold: 9 years | Hard delete | Swiss CO Art. 958f |
| Support tickets | Customer service | Art. 6(1)(b) | 3 years | Ticket closure | Warm: 6 months | Hard delete | Art. 5(1)(e) |
| Marketing preferences | Direct marketing | Art. 6(1)(a) | Consent duration + 5 years | Consent withdrawal | No | Hard delete | Art. 7(1), Art. 5(2) |

### Operational Data

| Data Category | Purpose | Lawful Basis | Retention Period | Trigger Event | Archival | Deletion Method | Legal Reference |
|--------------|---------|-------------|-----------------|---------------|----------|-----------------|-----------------|
| Server access logs | Security monitoring | Art. 6(1)(f) | 12 months | Log creation | No | Hard delete | Art. 5(1)(e), ENISA |
| Application logs | Debugging | Art. 6(1)(f) | 90 days | Log creation | No | Hard delete | Art. 5(1)(e) |
| API request logs | Rate limiting, abuse detection | Art. 6(1)(f) | 30 days | Log creation | No | Hard delete | Art. 5(1)(e) |
| Audit trail | Accountability | Art. 6(1)(c) | 7 years | Event date | Warm: 1 year, Cold: 6 years | Hard delete | Art. 5(2), Art. 24 |

### Compliance Data

| Data Category | Purpose | Lawful Basis | Retention Period | Trigger Event | Archival | Deletion Method | Legal Reference |
|--------------|---------|-------------|-----------------|---------------|----------|-----------------|-----------------|
| Consent records | Demonstrating consent | Art. 6(1)(c) | Consent duration + 5 years | Consent withdrawal | Warm: 2 years | Hard delete | Art. 7(1) |
| DPIA records | Accountability | Art. 6(1)(c) | Processing duration + 3 years | Processing cessation | Warm: 3 years | Hard delete | Art. 35, Art. 5(2) |
| Data breach records | Accountability | Art. 6(1)(c) | 5 years | Breach closure | Warm: 5 years | Hard delete | Art. 33(5) |
| DSR fulfillment records | Accountability | Art. 6(1)(c) | 6 years | Request completion | Warm: 3 years | Hard delete | Art. 5(2), limitation period |

## Legal Hold Register

| Hold ID | Matter Reference | Scope | Issued By | Issue Date | Last Review | Status |
|---------|-----------------|-------|-----------|------------|-------------|--------|
| HOLD-2026-0023 | Regulatory inquiry RA-2026-CH-0089 | customer_account, transaction_record (2025-01-01 to 2025-12-31) | Dr. Eva Hartmann (General Counsel) | 2026-02-15 | 2026-03-14 | Active |

## Automation Configuration

| Parameter | Value |
|-----------|-------|
| Expiry scan frequency | Daily at 02:00 UTC |
| Archival transition frequency | Daily at 03:00 UTC |
| Cold archive transition frequency | Monthly, 1st day at 04:00 UTC |
| Deletion verification frequency | Immediately after each deletion batch |
| Overdue alert threshold | 7 days past TTL |
| Backup rotation alignment | Longest retention period in schedule (10 years) |
| Crypto-shredding | Enabled for backup media; per-category DEKs destroyed at TTL expiry |

## Change Log

| Version | Date | Change | Author |
|---------|------|--------|--------|
| 3.2 | 2026-01-01 | Added legal hold HOLD-2026-0023; updated API log retention from 90 to 30 days | Dr. Lukas Meier |
| 3.1 | 2025-07-01 | Added DPIA records retention; aligned billing records with Swiss CO Art. 958f | Anna Kowalski |
| 3.0 | 2025-01-01 | Major revision: added three-tier storage lifecycle, crypto-shredding for backups | Thomas Richter |
