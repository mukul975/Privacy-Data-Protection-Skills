# Children's Deletion Request Workflows

## Workflow 1: Deletion Request Intake and Triage

```
Deletion request received concerning a child's data
│
├─ Step 1: Log the request
│  ├─ Assign reference number: DEL-CHILD-[YEAR]-[SEQ]
│  ├─ Record: channel (dashboard/email/postal), date, requester details
│  ├─ Set response deadline: 30 days from receipt (Art. 12(3))
│  └─ Send acknowledgement within 48 hours
│
├─ Step 2: Determine requester type
│  ├─ PARENT requesting deletion of current child's data
│  │  └─ Verify parental authority → Workflow 2
│  │
│  ├─ CHILD requesting deletion of own data
│  │  ├─ Is the child above the applicable consent threshold?
│  │  │  ├─ YES → Child may request independently → Workflow 3
│  │  │  └─ NO → Redirect to parent:
│  │  │     "We need your parent or guardian to submit this request.
│  │  │      Here's how they can do it: [instructions]"
│  │  │     Do NOT refuse the request outright; assist the child.
│  │  │
│  │  └─ Exception: if the child demonstrates Gillick competency
│  │     (UK) or equivalent maturity, consider accepting directly
│  │     with DPO review → Workflow 3 with DPO escalation
│  │
│  ├─ FORMER CHILD (now adult) requesting deletion of childhood data
│  │  └─ Adult capacity; standard verification → Workflow 3
│  │
│  └─ SCHOOL requesting deletion of student data (EdTech context)
│     └─ School authority verified via agreement → Workflow 4
│
└─ Record triage decision and routing
```

## Workflow 2: Parental Deletion Request Processing

```
Parent requests deletion of child's data
│
├─ Step 1: Verify parental identity and authority
│  ├─ Parent has existing verified account?
│  │  ├─ YES → Verify via account credentials (password + security question)
│  │  └─ NO → Verify via:
│  │     ├─ Same method used for original consent (e.g., credit card)
│  │     ├─ Or: government ID (processed in memory, deleted after verification)
│  │     └─ Or: knowledge-based questions matching registered parent data
│  │
│  ├─ Confirm the parent is authorised for this specific child
│  │  (match parent account to child account)
│  │
│  ├─ Verification successful? → Proceed to Step 2
│  └─ Verification failed?
│     ├─ Allow one retry
│     ├─ If retry fails → escalate to DPO for manual review
│     └─ Do NOT reveal child's data to unverified requester
│
├─ Step 2: Determine scope
│  ├─ Ask parent:
│  │  "Would you like to delete:"
│  │  ├─ [A] Your child's entire account and all data
│  │  ├─ [B] Specific data categories (select below)
│  │  └─ [C] Data collected for specific purposes only
│  │
│  ├─ If [A]: Full account deletion
│  │  ├─ Offer data download before deletion
│  │  ├─ Explain what will and will not be deleted:
│  │  │  "We will delete all of [Child]'s account data, activity logs,
│  │  │   content, and communications. We are required to retain the
│  │  │   consent record for 6 years for legal compliance."
│  │  └─ Confirm scope with parent
│  │
│  ├─ If [B] or [C]: Partial deletion
│  │  ├─ Present data categories and purposes with checkboxes
│  │  ├─ Explain impact of each deletion on service functionality
│  │  └─ Confirm selections with parent
│
├─ Step 3: Check for exceptions (Art. 17(3))
│  ├─ Is there an active safeguarding investigation? → Retain relevant data
│  ├─ Is data needed for a legal claim? → Retain relevant data
│  ├─ Is there a legal retention obligation? → Retain relevant data
│  │  (consent records: 6 years; financial records: per law)
│  ├─ Document any exceptions applied
│  └─ Inform parent of any retained data and the legal basis for retention
│
├─ Step 4: Execute deletion
│  ├─ Delete from primary database
│  ├─ Delete from search indices
│  ├─ Invalidate caches
│  ├─ Delete uploaded files from object storage
│  ├─ Remove from analytics databases
│  ├─ Purge from application logs
│  ├─ Schedule backup purge (within 30-day backup cycle)
│  └─ If data was shared with third parties: notify each per Art. 17(2)/19
│
├─ Step 5: Confirm deletion
│  ├─ Send confirmation to parent:
│  │  "We have deleted [scope] for [Child's name]."
│  │  "Backup copies will be removed within 30 days."
│  │  "The following data is retained for legal compliance: [list]."
│  ├─ Include deletion reference number
│  └─ Provide contact for questions
│
└─ Step 6: Post-deletion verification
   ├─ Attempt to retrieve child's data from all systems
   ├─ Confirm no personal data returned (except legally retained)
   ├─ Log verification result
   └─ Schedule backup purge verification (30 days)
```

## Workflow 3: Child/Former-Child Initiated Deletion

```
Child (above threshold) or former child (adult) requests deletion
│
├─ Step 1: Verify identity
│  ├─ Current child (above threshold, existing account):
│  │  └─ Verify via account credentials
│  │
│  ├─ Former child (adult, account may be dormant):
│  │  ├─ Attempt account credential verification
│  │  ├─ If account no longer active: verify via email + security question
│  │  ├─ If no account found: verify via personal details matching historical records
│  │  └─ DPO review for historical data requests
│  │
│  └─ Verification successful? → Proceed to Step 2
│
├─ Step 2: Determine scope
│  ├─ For current child:
│  │  ├─ Same options as parental deletion (full or partial)
│  │  ├─ Explain impact on service functionality
│  │  └─ For children 13-15: consider whether parental notification is appropriate
│  │     (balance child's autonomy with parental oversight)
│  │
│  └─ For former child (adult):
│     ├─ Identify all historical data from childhood
│     ├─ May include: social media posts, educational records, activity logs
│     ├─ Apply Art. 17(1)(f) — data collected from a child under Art. 8(1)
│     └─ This right applies regardless of how long ago the data was collected
│
├─ Step 3: Process deletion (same as Workflow 2, Steps 3-6)
│
└─ Additional for former child:
   ├─ If data has been published online: invoke Art. 17(2)
   │  ├─ Identify all URLs/platforms where childhood data appears
   │  ├─ Send takedown requests to each platform
   │  ├─ Send de-indexing requests to search engines
   │  └─ Document all notifications and responses
   │
   └─ Confirm all actions taken to the requester
```

## Workflow 4: School-Initiated Deletion (EdTech Context)

```
School requests deletion of student data from EdTech platform
│
├─ Step 1: Verify school authority
│  ├─ Request from designated school administrator (named in contract)
│  ├─ Verify via:
│  │  ├─ Administrator account credentials
│  │  ├─ Or: email from registered school domain
│  │  └─ Or: written request on school letterhead
│  └─ Confirm scope: individual student, class, year group, or entire school
│
├─ Step 2: Determine scope
│  ├─ Individual student: parent has requested through school
│  ├─ Class/year group: end of year or program completion
│  ├─ Entire school: end of contract or school switching providers
│  └─ Offer data export before deletion (CSV/JSON/SIF)
│
├─ Step 3: Execute deletion
│  ├─ Delete all student data within the specified scope
│  ├─ Retain only: school agreement, deletion certificate
│  ├─ Do NOT retain anonymised data for product improvement
│  │  (unless school has explicitly authorised this in the agreement)
│  └─ Generate deletion certificate
│
├─ Step 4: Confirm
│  ├─ Send deletion certificate to school administrator
│  ├─ Include: scope, date, reference number, systems covered
│  └─ Confirm backup purge timeline
│
└─ Step 5: Notify parents (if individual deletion)
   ├─ If a specific student's data was deleted at school's request:
   │  inform the parent via existing communication channel
   └─ Include instructions for the parent if they wish to retain data independently
```

## Workflow 5: Third-Party Notification (Art. 17(2))

```
Child's data was shared with third parties and deletion is requested
│
├─ Step 1: Identify all third-party recipients
│  ├─ Query data sharing log for the child's identifier
│  ├─ List all third parties that received the child's data:
│  │  ├─ Third party name and contact
│  │  ├─ Data elements shared
│  │  ├─ Date of sharing
│  │  └─ Legal basis for original sharing
│  └─ Include: sub-processors, analytics providers, cloud infrastructure providers
│
├─ Step 2: Send deletion notifications
│  ├─ For each third party:
│  │  ├─ Send written deletion request:
│  │  │  "Pursuant to GDPR Article 17(2), we notify you that the data subject
│  │  │   (a child) has exercised their right to erasure. Please delete all
│  │  │   personal data relating to [child identifier] that you received from us."
│  │  ├─ Include: child identifier, data elements to delete, deadline (14 days)
│  │  └─ Request confirmation of deletion
│  │
│  └─ For search engines (if data was publicly available):
│     ├─ Submit de-indexing requests per Art. 17(2)
│     └─ Document submission and response
│
├─ Step 3: Track responses
│  ├─ Log each third party's response:
│  │  ├─ Confirmed deletion
│  │  ├─ Refused (with reason)
│  │  └─ No response within 14 days → follow up
│  │
│  └─ If a third party refuses: assess whether refusal is legally justified
│     ├─ If justified (e.g., legal obligation): document
│     └─ If not justified: escalate to DPO for enforcement action
│
├─ Step 4: Report to requester
│  ├─ If the data subject requests it (Art. 19): provide the list of
│  │  third parties notified and their responses
│  └─ Include in deletion confirmation
│
└─ Document all notifications and outcomes in deletion log
```
