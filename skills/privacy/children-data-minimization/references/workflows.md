# Children's Data Minimisation Workflows

## Workflow 1: Data Necessity Assessment for Children

```
New data collection proposed for a feature used by children
│
├─ Step 1: Identify the data element
│  ├─ What data is proposed for collection? [specific element]
│  ├─ How is it collected? (active input, passive tracking, derived, inferred)
│  ├─ What feature does it support?
│  └─ Which age groups will be affected?
│
├─ Step 2: Apply Strict Necessity Test
│  ├─ Q1: Is this data required for the specific feature the child is actively using?
│  │  ├─ YES → Continue to Q2
│  │  └─ NO → REJECT. Do not collect.
│  │
│  ├─ Q2: Could the feature work with less precise data?
│  │  ├─ YES → Collect the less precise version (e.g., age range instead of DOB)
│  │  └─ NO → Continue to Q3
│  │
│  ├─ Q3: Could the feature work with anonymised or pseudonymised data?
│  │  ├─ YES → Anonymise/pseudonymise at collection point
│  │  └─ NO → Continue to Q4
│  │
│  ├─ Q4: Is the primary beneficiary the child or the controller?
│  │  ├─ CHILD → Continue to Q5
│  │  └─ CONTROLLER → REJECT unless secondary benefit to child is significant
│  │
│  ├─ Q5: Would a reasonable parent expect this collection?
│  │  ├─ YES → Continue to Q6
│  │  └─ NO → REJECT or require explicit parental consent
│  │
│  └─ Q6: Is retention limited to the feature session or shortest necessary period?
│     ├─ YES → APPROVE. Document justification.
│     └─ NO → Reduce retention to shortest necessary period, then APPROVE.
│
├─ Step 3: Document decision
│  ├─ Data element, feature, justification
│  ├─ Test outcomes (Q1-Q6)
│  ├─ Retention period assigned
│  ├─ Reviewer and date
│  └─ Next review date (annual or feature change)
│
└─ File in data minimisation assessment register
```

## Workflow 2: Retention Period Assignment for Children's Data

```
Data element requires retention period assignment
│
├─ Step 1: Classify data category
│  ├─ Account data (name, username, age, parent email)
│  ├─ Activity data (usage logs, feature interactions)
│  ├─ Content data (created by child — drawings, text, projects)
│  ├─ Learning data (progress, scores, assessments)
│  ├─ Communication data (messages, chat logs)
│  ├─ Technical data (error logs, crash reports, session IDs)
│  ├─ Consent records (parental consent, verification)
│  └─ Financial data (transactions, purchase records)
│
├─ Step 2: Apply retention limits
│  ├─ Account data → Duration of account + 30 days
│  ├─ Activity data → 30 days rolling
│  ├─ Content data → Duration of account (return to parent on deletion)
│  ├─ Learning data → Academic year + 30 days (or duration of account if shorter)
│  ├─ Communication data → 90 days rolling (safety moderation)
│  ├─ Technical data → 7 days rolling
│  ├─ Consent records → Duration of account + 6 years (legal compliance)
│  └─ Financial data → As required by applicable tax/accounting law
│
├─ Step 3: Implement automated deletion
│  ├─ Assign retention_category and expires_at to each data record
│  ├─ Configure daily deletion job to purge expired records
│  ├─ Configure cascade deletion for account deletion
│  ├─ Configure backup purge within 30 days of primary deletion
│  └─ Test deletion pipeline end-to-end
│
├─ Step 4: Verify deletion
│  ├─ Monthly: sample check that expired records are actually deleted
│  ├─ Quarterly: full audit of retention compliance
│  └─ Log verification results
│
└─ Document retention schedule and update privacy notice
```

## Workflow 3: Parental Dashboard Data Review

```
Parent accesses dashboard to review child's data
│
├─ Step 1: Authenticate parent
│  ├─ Verify parent identity (account credentials + security question)
│  └─ If verification fails → require additional verification (email OTP)
│
├─ Step 2: Display data inventory
│  ├─ Present all data categories held about the child:
│  │  ├─ Category name | Purpose | Status | Retention remaining
│  │  ├─ Account data | Service delivery | Required | Account duration
│  │  ├─ Learning progress | Progress reports | Consented | Year end + 30d
│  │  ├─ Activity logs | Service improvement | Consented | 30d rolling
│  │  └─ [additional categories as applicable]
│  │
│  └─ For each category: expandable view showing actual data elements
│
├─ Step 3: Parent actions
│  ├─ VIEW: Parent can browse all data held about the child
│  ├─ DOWNLOAD: Parent can export all data in JSON/CSV format
│  ├─ DELETE CATEGORY: Parent can request deletion of specific data category
│  ├─ DELETE ACCOUNT: Parent can request full account and data deletion
│  ├─ MODIFY CONSENT: Parent can withdraw consent for optional processing
│  └─ RESTRICT: Parent can restrict specific features or data collection
│
├─ Step 4: Process parent request
│  ├─ If DELETE requested:
│  │  ├─ Confirm scope with parent
│  │  ├─ Offer data download before deletion
│  │  ├─ Execute deletion within 30 days
│  │  └─ Send confirmation to parent
│  │
│  ├─ If MODIFY CONSENT requested:
│  │  ├─ Update consent record
│  │  ├─ Disable affected features
│  │  ├─ Delete data collected under withdrawn consent
│  │  └─ Confirm changes to parent
│  │
│  └─ If RESTRICT requested:
│     ├─ Apply restrictions to child's account
│     ├─ Confirm changes to parent
│     └─ Notify child (age-appropriate) that parent has changed settings
│
└─ Log all dashboard interactions for accountability
```

## Workflow 4: End-of-Academic-Year Data Lifecycle

```
Academic year end approaching (for educational platforms)
│
├─ 60 days before year end:
│  ├─ Identify all active student/child accounts
│  ├─ Prepare end-of-year data lifecycle notices
│  └─ Notify school administrators (if school deployment)
│
├─ 30 days before year end:
│  ├─ Send notification to parents:
│  │  "The academic year is ending. Your child's learning data will be
│  │   archived and a progress report generated. Unless you request retention,
│  │   detailed activity data will be deleted 30 days after the year ends."
│  ├─ Provide parent with:
│  │  ├─ Option to download all data
│  │  ├─ Option to request retention for next year
│  │  └─ Option to request immediate deletion
│  └─ Generate end-of-year progress reports (PDF)
│
├─ Year end (last day of academic year):
│  ├─ Export progress reports to parent dashboard
│  ├─ Archive detailed activity data to deletion queue
│  └─ Retain only aggregate progress scores for next year placement
│
├─ 14 days after year end:
│  ├─ If parent has NOT requested retention:
│  │  ├─ Delete detailed activity data from deletion queue
│  │  └─ Retain aggregate scores only
│  ├─ If parent HAS requested retention:
│  │  ├─ Extend retention for specified data categories
│  │  └─ Set new expiry (next academic year end)
│  └─ If parent has requested immediate deletion:
│     ├─ Delete all data including aggregate scores
│     └─ Send deletion confirmation
│
├─ 60 days after year end:
│  ├─ Delete aggregate scores unless child continues to next year
│  ├─ Purge backups containing deleted data
│  ├─ Send final data lifecycle confirmation to parent
│  └─ Generate deletion audit report
│
└─ Log all lifecycle events for accountability
```

## Workflow 5: Background Collection Audit

```
Quarterly audit of background data collection for child accounts
│
├─ Step 1: Inventory all passive/background data collection
│  ├─ Device identifiers (IDFA, GAID, device fingerprint)
│  ├─ Location data (GPS, IP geolocation, Wi-Fi)
│  ├─ Sensor data (accelerometer, gyroscope)
│  ├─ Microphone/camera access
│  ├─ Contact list access
│  ├─ Clipboard access
│  ├─ Browsing/navigation history within the app
│  ├─ Third-party SDK data collection (analytics, crash reporting)
│  └─ Cookies and local storage
│
├─ Step 2: For each collection point, assess:
│  ├─ Is this collection triggered by a feature the child is actively using?
│  │  ├─ YES → Is it proportionate and necessary? [Assess]
│  │  └─ NO → VIOLATION. Disable immediately.
│  ├─ Is the collected data transmitted to a server?
│  │  ├─ YES → Is transmission necessary? Could processing be on-device?
│  │  └─ NO → Lower risk; assess necessity anyway
│  └─ Is the data shared with third parties?
│     ├─ YES → Is sharing necessary for the child's benefit?
│     └─ NO → Acceptable if collection itself is justified
│
├─ Step 3: Review third-party SDKs
│  ├─ List all SDKs integrated in the app
│  ├─ For each SDK: what data does it collect from child users?
│  ├─ Is the SDK configured to respect child accounts (no advertising IDs, no profiling)?
│  ├─ Does the SDK vendor's privacy policy comply with COPPA/GDPR for children?
│  └─ Can the SDK be replaced with a more privacy-preserving alternative?
│
├─ Step 4: Remediate violations
│  ├─ Disable any background collection not justified by active feature use
│  ├─ Configure SDKs to exclude child accounts from non-essential tracking
│  ├─ Update permission requests to remove unnecessary permissions
│  └─ Document remediation actions and timeline
│
└─ Step 5: Report
   ├─ Generate audit report with findings and remediation status
   ├─ DPO review and sign-off
   └─ Schedule next quarterly audit
```
