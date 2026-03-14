# Children's Data Minimisation Workflows

## Workflow 1: Strict Necessity Test

```
New data collection from children proposed
│
├─ Step 1: Identify the data element and purpose
│  ├─ Data element: [name, DOB, email, location, device ID, etc.]
│  ├─ Purpose: [specific feature or function requiring this data]
│  ├─ Age group affected: [under 8, 8-12, 13-15, 16-17]
│  └─ Lawful basis: [consent (parental under Art. 8), legitimate interest, contract, etc.]
│
├─ Step 2: Apply Strict Necessity Test questions
│  ├─ Q1: Is this data required for the specific feature the child is actively using?
│  │  ├─ YES → Continue to Q2
│  │  └─ NO → REJECT. Do not collect.
│  │
│  ├─ Q2: Could the feature work with less precise data?
│  │  ├─ YES → Collect the less precise version (e.g., age band instead of DOB)
│  │  └─ NO → Continue to Q3
│  │
│  ├─ Q3: Could the feature work with anonymised or pseudonymised data?
│  │  ├─ YES → Anonymise/pseudonymise at collection point
│  │  └─ NO → Continue to Q4
│  │
│  ├─ Q4: Is this collected for the child's benefit or the controller's?
│  │  ├─ CHILD'S BENEFIT → Continue to Q5
│  │  └─ CONTROLLER'S BENEFIT ONLY → REJECT. Not proportionate for children.
│  │
│  ├─ Q5: Would a reasonable parent expect this collection?
│  │  ├─ YES → Continue to Q6
│  │  └─ NO → REJECT or require explicit parental consent with clear explanation.
│  │
│  └─ Q6: Is retention limited to the feature's active use?
│     ├─ YES → APPROVE. Document justification.
│     └─ NO → Define minimum retention period. APPROVE with retention limit.
│
├─ Step 3: Document the assessment
│  ├─ Data element, purpose, necessity test answers
│  ├─ Decision: approved / rejected / approved with conditions
│  ├─ Conditions (if any): data precision reduction, pseudonymisation, retention limit
│  ├─ Reviewer: DPO name and date
│  └─ Next review date: [quarterly or upon feature change]
│
└─ File in data minimisation register
```

## Workflow 2: Data Collection Audit

```
Quarterly audit of data collected from children
│
├─ Step 1: Generate data inventory
│  ├─ Extract all data elements currently collected from child accounts
│  ├─ For each element, record:
│  │  ├─ Data element name
│  │  ├─ Collection method (active user input, automatic, third-party)
│  │  ├─ Feature/purpose it supports
│  │  ├─ Current retention period
│  │  ├─ Last necessity test date
│  │  └─ Actual usage in the past quarter (is this data actually used?)
│
├─ Step 2: Assessment against necessity
│  ├─ For each element:
│  │  ├─ Is the feature this supports still active? [Y/N]
│  │  │  └─ NO → Flag for deletion
│  │  ├─ Is the data actually used for the stated purpose? [Y/N]
│  │  │  └─ NO → Flag for deletion
│  │  ├─ Could the feature work with less data now? [Y/N]
│  │  │  └─ YES → Flag for reduction
│  │  ├─ Is the retention period still justified? [Y/N]
│  │  │  └─ NO → Flag for retention reduction
│  │  └─ Is any background collection occurring? [Y/N]
│  │     └─ YES → Flag for immediate review
│
├─ Step 3: Remediation
│  ├─ DELETE: Data elements flagged for deletion → schedule deletion within 30 days
│  ├─ REDUCE: Data elements flagged for reduction → implement less precise collection
│  ├─ SHORTEN: Retention periods flagged → update retention schedule
│  ├─ REVIEW: Background collection → conduct emergency necessity test
│  └─ NO CHANGE: Data elements passing all checks → confirm and log
│
├─ Step 4: Report
│  ├─ Audit date and scope
│  ├─ Total data elements audited: [count]
│  ├─ Deletions ordered: [count]
│  ├─ Reductions ordered: [count]
│  ├─ Retention changes: [count]
│  ├─ No change: [count]
│  └─ DPO sign-off
│
└─ Schedule next audit (quarterly)
```

## Workflow 3: Retention Schedule Management

```
Establish and maintain retention schedule for children's data
│
├─ Step 1: Define retention categories
│  ├─ Category A — Session data: 0-30 days
│  ├─ Category B — Activity data: 30-90 days
│  ├─ Category C — Account data: duration of account + 30 days
│  ├─ Category D — Educational progress: academic year + 30 days
│  ├─ Category E — Content created by child: duration of account (return to parent on deletion)
│  ├─ Category F — Consent records: duration of account + 6 years (legal compliance)
│  ├─ Category G — Verification data: immediate deletion after verification (max 48 hours)
│  └─ Category H — Financial records: per applicable tax law (typically 7 years)
│
├─ Step 2: Map each data element to a retention category
│  ├─ For each element: assign category and set expires_at timestamp
│  └─ Document mapping in retention schedule register
│
├─ Step 3: Implement automated deletion
│  ├─ Daily batch job: SELECT * WHERE expires_at < NOW()
│  ├─ Execute deletion across all storage:
│  │  ├─ Primary database
│  │  ├─ Search indices
│  │  ├─ Caches (Redis, CDN)
│  │  ├─ File storage (S3, Azure Blob)
│  │  ├─ Analytics databases
│  │  └─ Application logs
│  ├─ Log each deletion: deletion_id, data_category, records_deleted, timestamp
│  └─ Schedule backup purge within 30-day rotation cycle
│
├─ Step 4: End-of-academic-year trigger (for educational platforms)
│  ├─ T-30 days: Notify parent of impending data archival
│  ├─ T-0 (year end): Export progress report to parent; archive data to deletion queue
│  ├─ T+14: If parent has not requested retention: delete granular activity data
│  ├─ T+30: Delete all year-specific data
│  └─ T+60: Purge from backups
│
├─ Step 5: Verify deletions
│  ├─ Post-deletion query: attempt to retrieve deleted records
│  ├─ If records found: investigate and re-execute deletion
│  ├─ Log verification outcome
│  └─ Backup purge verification: 30 days after primary deletion
│
└─ Step 6: Annual retention schedule review
   ├─ Are retention periods still justified?
   ├─ Have any legal requirements changed?
   ├─ Can any periods be shortened?
   └─ DPO approval and sign-off
```

## Workflow 4: Parental Dashboard Data Access

```
Parent accesses parental dashboard
│
├─ Step 1: Authenticate parent
│  ├─ Parent logs in with dashboard credentials
│  ├─ Two-factor authentication (if enabled)
│  └─ Session established
│
├─ Step 2: Display data inventory
│  ├─ Show all data categories held about the child:
│  │  ├─ Account data (name, age band, account status)
│  │  ├─ Activity data (recent sessions, features used)
│  │  ├─ Learning progress (scores, levels, achievements)
│  │  ├─ Content (creations, saved items)
│  │  └─ Consent records (active consents, dates)
│  │
│  ├─ For each category show:
│  │  ├─ What data exists
│  │  ├─ Why it is held (purpose)
│  │  ├─ How long it will be retained
│  │  └─ When it was last accessed or used
│
├─ Step 3: Enable parental actions
│  ├─ [View details]: expand any category to see specific data
│  ├─ [Download]: export child's data in JSON/CSV format
│  ├─ [Delete category]: request deletion of specific data category
│  ├─ [Delete account]: request full account and data deletion
│  ├─ [Modify consent]: toggle consent for optional processing purposes
│  ├─ [Privacy settings]: adjust profile visibility, sharing, notifications
│  └─ [Activity log]: view child's recent activity summary
│
├─ Step 4: Process parent actions
│  ├─ Downloads: generate export file and email secure download link
│  ├─ Category deletion: confirm scope, execute within 30 days, confirm
│  ├─ Account deletion: confirm, offer data download, execute within 30 days
│  ├─ Consent changes: apply immediately, update consent registry
│  └─ Settings changes: apply immediately, log change
│
└─ Step 5: Log dashboard access
   ├─ Parent ID, access timestamp, actions taken
   └─ Retain access log for 90 days (security audit)
```
