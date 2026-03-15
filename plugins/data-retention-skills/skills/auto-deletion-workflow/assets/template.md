# Automated Deletion Workflow Templates — Orion Data Vault Corp

## Deletion Job Record Template

```
DELETION JOB RECORD
--------------------
Reference: DEL-YYYY-NNNN
Trigger: [retention_expiry / art17_erasure / consent_withdrawal / account_closure]
Priority: [STANDARD / HIGH / URGENT]
Data Subject Reference: DS-HASH-[hash]

REQUEST DETAILS:
- Request Date: [YYYY-MM-DD] (if applicable)
- Data Categories: [CAT-XXX, CAT-YYY]
- Systems Identified: [list]

PRE-DELETION CHECKS:
- [ ] Litigation hold check: [CLEAR / HELD — ref: LH-YYYY-NNNN]
- [ ] Retention exception check: [CLEAR / EXCEPTED — ref: RET-EXC-YYYY-NNNN]
- [ ] Pending DSAR check: [CLEAR / COORDINATED]
- [ ] DPO approval (Art. 17 only): [APPROVED / N/A]

EXECUTION:
| System | Records | Action | Status | Timestamp |
|--------|---------|--------|--------|-----------|
| | | | | |

THIRD-PARTY NOTIFICATIONS (Art. 19):
| Processor | Notified | Confirmed |
|-----------|----------|-----------|
| | | |

EXCEPTIONS APPLIED:
| Category | Exception Basis | Retention Until |
|----------|----------------|-----------------|
| | | |

BACKUP DELETION:
- Next rotation date: [YYYY-MM-DD]
- Expected completion: [YYYY-MM-DD]

VERIFICATION:
- Post-deletion scan: [PASS / FAIL]
- Timestamp: [ISO 8601]
- Verification hash: SHA-256:[hash]

Executed by: [System / Operator]
Reviewed by: [DPO Name] (Art. 17 only)
```

## Quarterly Compliance Report Template

```
AUTOMATED DELETION — QUARTERLY COMPLIANCE REPORT
Organization: Orion Data Vault Corp
Period: Q[X] [YYYY]

SUMMARY METRICS:
- Total deletions executed: [count]
- By trigger type:
  - Retention expiry: [count]
  - Art. 17 erasure: [count]
  - Consent withdrawal: [count]
  - Account closure: [count]
  - Other: [count]

COMPLETION RATES:
- Retention expiry within 30 days: [%] (target: 99.5%)
- Art. 17 within 30 days: [%] (target: 100%)
- Average execution time: [hours]
- Failed deletion rate: [%] (target: <0.5%)

THIRD-PARTY COMPLIANCE:
- Notifications sent: [count]
- Confirmations received within 14 days: [%]
- Outstanding confirmations: [count]

BACKUP DELETION:
- Completions within rotation cycle: [%]
- Outstanding backup deletions: [count]

EXCEPTIONS:
- Total exceptions applied: [count]
- Breakdown by Art. 17(3) basis: [table]

TREND ANALYSIS:
- Quarter-over-quarter volume change: [%]
- System coverage: [% of registered data stores]
```
