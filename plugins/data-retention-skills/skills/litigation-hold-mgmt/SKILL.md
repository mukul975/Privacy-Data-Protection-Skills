---
name: litigation-hold-mgmt
description: >-
  Manages legal hold and data preservation processes including triggering events, custodian
  notification, hold-in-place technical implementation, release procedures, and interaction
  with retention schedules. Covers litigation hold registers, compliance monitoring, and
  Art. 17(3)(e) exception documentation. Activate for legal hold, litigation preservation,
  data freeze, e-discovery hold queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-retention-deletion
  tags: "litigation-hold, legal-preservation, e-discovery, data-freeze, legal-hold-management"
---

# Litigation Hold Management

## Overview

A litigation hold (also called legal hold or preservation order) is a directive to preserve all data and documents relevant to pending or reasonably anticipated litigation, regulatory investigation, or audit. Litigation holds override normal retention schedules and automated deletion processes — data subject to a hold must NOT be deleted, modified, or destroyed until the hold is formally released. This skill provides the complete operational framework for issuing, tracking, implementing, and releasing litigation holds, including the critical interaction between holds and GDPR data retention and erasure obligations.

## Legal Foundation

### GDPR Article 17(3)(e) — Legal Claims Exception

The right to erasure does not apply where processing is necessary for the establishment, exercise, or defence of legal claims. This is the primary GDPR basis for retaining personal data under a litigation hold beyond its normal retention period.

### Duty to Preserve (Common Law Jurisdictions)

In England and Wales, the duty to preserve documents arises when litigation is reasonably contemplated or has commenced:
- **CPR Part 31** (Civil Procedure Rules): Imposes disclosure obligations once proceedings are issued.
- **Practice Direction 31B**: Electronic disclosure — requires parties to preserve electronic documents once litigation is reasonably anticipated.
- **Spoliation doctrine**: Intentional or negligent destruction of relevant evidence after litigation is anticipated can result in adverse inferences, costs sanctions, or striking out of claims.

### US Federal Rules (Cross-Reference for Multinational Operations)

- **FRCP Rule 37(e)**: Failure to preserve electronically stored information (ESI) can result in sanctions, adverse inference instructions, or case dismissal.
- **Zubulake v UBS Warburg (2003-2004)**: Established the duty to preserve begins when litigation is reasonably anticipated.

### EU Regulatory Investigations

Regulatory bodies (European Commission, national competition authorities, financial regulators) may require preservation of documents relevant to an investigation. Failure to preserve can constitute obstruction.

## Litigation Hold Lifecycle

### Phase 1: Triggering Events

A litigation hold must be issued when any of the following events occur:

| Trigger Category | Specific Events | Response Time |
|-----------------|-----------------|---------------|
| **Litigation filed** | Claim form received; writ served; arbitration notice received | Immediate (within 24 hours) |
| **Litigation anticipated** | Pre-action protocol letter received; demand letter received; formal complaint indicating likely litigation | Within 48 hours |
| **Regulatory investigation** | Notice of investigation; dawn raid; regulatory inquiry letter; request for information from supervisory authority | Immediate (within 24 hours) |
| **Internal investigation** | Whistleblower report triggering formal investigation; fraud suspicion; compliance breach identified | Within 48 hours |
| **DPA inquiry** | Data protection authority opens formal investigation or requests information under GDPR Art. 58 | Within 48 hours |
| **Tax audit** | HMRC opens formal enquiry; VAT inspection notice | Within 48 hours |
| **Employment dispute** | Tribunal claim filed; formal grievance raising likelihood of tribunal proceedings | Within 48 hours |

### Phase 2: Hold Scope Definition

```
LITIGATION HOLD SCOPE DEFINITION — Orion Data Vault Corp
---------------------------------------------------------
Hold Reference: LH-2026-0023
Matter: [Description of litigation/investigation]
Legal Counsel: [Internal/External counsel name]
Date Issued: 2026-03-14
Anticipated Duration: [Estimate — reassess quarterly]

SCOPE — DATA TO PRESERVE:
1. Date Range: [Start date] to [End date / ongoing]
2. Data Subjects: [Named individuals, departments, or "all"]
3. Data Categories:
   □ Email and electronic communications
   □ Documents (Word, Excel, PowerPoint, PDF)
   □ Financial records and transactions
   □ Customer/client records
   □ Employee records
   □ CCTV/surveillance footage
   □ Access logs and audit trails
   □ Database records (specify: _____________)
   □ Backup tapes/archives
   □ Mobile device data (text messages, call logs)
   □ Collaboration platforms (Teams, Slack, SharePoint)
   □ Other: _____________

4. Systems in Scope:
   □ Email system (Exchange/Gmail)
   □ File servers / network drives
   □ SharePoint / OneDrive / Google Drive
   □ CRM (Salesforce)
   □ ERP (SAP)
   □ HR system
   □ Financial system
   □ Cloud storage (AWS S3 / Azure / GCP)
   □ Backup systems
   □ Messaging platforms
   □ Other: _____________

5. Custodians (individuals who may hold relevant data):
   - [Name, Title, Department]
   - [Name, Title, Department]
   - [Name, Title, Department]

EXCLUSIONS:
- [Specify any data explicitly outside scope]

INTERACTION WITH RETENTION SCHEDULE:
- Normal retention schedule: SUSPENDED for all in-scope data
- Automated deletion: PAUSED for in-scope data categories
- Art. 17 erasure requests: EXCEPTION applies under Art. 17(3)(e)
```

### Phase 3: Custodian Notification

Every individual identified as a custodian must receive a formal hold notice:

```
LITIGATION HOLD NOTICE — CONFIDENTIAL
Orion Data Vault Corp

To: [Custodian Name, Title]
From: [General Counsel / Legal Department]
Date: [YYYY-MM-DD]
Re: Litigation Hold — Reference LH-2026-0023

DIRECTIVE: PRESERVE ALL POTENTIALLY RELEVANT DATA

You are hereby directed to preserve all documents and electronically
stored information (ESI) that may be relevant to the above-referenced
matter. This obligation is effective IMMEDIATELY and supersedes all
existing retention schedules and deletion policies.

WHAT YOU MUST DO:
1. STOP all deletion, destruction, or modification of potentially
   relevant documents and data.
2. PRESERVE all emails, documents, files, messages, voicemails,
   text messages, and other records related to [description of
   subject matter].
3. DISABLE any auto-delete functions on your email or messaging
   accounts for the duration of this hold.
4. DO NOT move, rename, or reorganize files that may be relevant.
5. PRESERVE all physical documents (paper files, notebooks, etc.).

SCOPE:
- Time period: [Start date] to present
- Subject matter: [Description]
- Document types: All formats (electronic and physical)

THIS HOLD REMAINS IN EFFECT until you receive a formal written
release notice from the Legal Department. Do not assume the hold
has been lifted based on the passage of time or resolution of
the underlying matter.

QUESTIONS: Contact [Legal Department contact] immediately if you
have any questions about this notice or are unsure whether specific
documents fall within scope.

ACKNOWLEDGEMENT REQUIRED: Please confirm receipt and understanding
of this notice by signing below and returning to the Legal
Department within 48 hours.

I acknowledge receipt and understanding of this Litigation Hold Notice.

Name: ________________________
Signature: ____________________
Date: ________________________
```

### Phase 4: Technical Implementation (Hold-in-Place)

| System | Hold Implementation Method |
|--------|--------------------------|
| **Email (Exchange Online)** | In-Place Hold or Litigation Hold via Exchange Admin Center / Compliance Center; applies to mailbox and archive |
| **Email (Google Workspace)** | Google Vault — create a Matter and apply Hold to specified users and date range |
| **SharePoint / OneDrive** | Preservation Hold via Microsoft Purview Compliance; applies at site, library, or folder level |
| **Cloud Storage (AWS S3)** | Apply S3 Object Lock Legal Hold (`s3:PutObjectLegalHold`) to relevant objects |
| **Cloud Storage (Azure Blob)** | Apply Legal Hold tags to containers via immutability policy |
| **Cloud Storage (GCP)** | Apply temporary hold to objects (`gcloud storage objects update --temporary-hold`) |
| **Databases** | Disable automated deletion jobs for in-scope records; flag records with hold reference |
| **Backup systems** | Tag relevant backup sets for indefinite retention; exclude from rotation/overwrite |
| **Automated deletion system** | Add hold reference to exclusion list in deletion orchestrator; all in-scope records bypass deletion queue |
| **Collaboration (Teams/Slack)** | Microsoft Purview retention policy; Slack Enterprise Grid Legal Hold (via Compliance API) |

### Phase 5: Ongoing Compliance Monitoring

| Activity | Frequency | Responsible |
|----------|-----------|-------------|
| Custodian compliance reminder | Quarterly (or more frequently for active litigation) | Legal Department |
| New custodian identification | Ongoing — as new individuals are identified as relevant | Legal Counsel |
| System hold verification | Monthly — verify holds remain active on all in-scope systems | IT + Legal |
| New data source assessment | When new systems are deployed or data is migrated | IT + Legal |
| Hold scope review | Quarterly — assess whether scope should be expanded or narrowed | Legal Counsel |
| Interaction with Art. 17 requests | Per request — assess whether hold applies to data subject's data | DPO + Legal |

### Phase 6: Release Procedures

```
[Litigation/Investigation Concluded]
         │
         ▼
[Legal Counsel Authorizes Release]
   - Written authorization from lead counsel
   - Confirmation that all proceedings (including appeals) are concluded
   - Confirmation that no related proceedings are anticipated
         │
         ▼
[Issue Hold Release Notice]
   - Formal written notice to all custodians
   - Notify IT to remove technical holds
   - Notify DPO to resume normal retention schedule
         │
         ▼
[Technical Hold Removal]
   - Remove litigation hold from email systems
   - Remove legal holds from cloud storage objects
   - Re-enable automated deletion for affected data categories
   - Remove hold exclusion from deletion orchestrator
   - Unfreeze backup rotation for affected backup sets
         │
         ▼
[Post-Release Retention Assessment]
   - For each data category previously under hold:
     ├── Has normal retention period expired during hold? ──► Schedule immediate deletion
     ├── Is normal retention period still active? ──► Resume normal retention countdown
     └── Were Art. 17 requests received during hold? ──► Process queued erasure requests
         │
         ▼
[Update Litigation Hold Register]
   - Record release date, authorizing counsel, matter outcome
   - Archive hold documentation (retain for 6 years)
```

## Litigation Hold Register

Orion Data Vault Corp maintains a central register of all active and closed litigation holds:

```
LITIGATION HOLD REGISTER — Orion Data Vault Corp
(Extract — Active Holds as of 2026-03-14)

┌───────────────┬───────────────────────────┬────────────┬──────────────┬───────────┬──────────────────┐
│ Hold Ref      │ Matter Description        │ Date Issued│ Custodians   │ Systems   │ Next Review      │
├───────────────┼───────────────────────────┼────────────┼──────────────┼───────────┼──────────────────┤
│ LH-2025-0018  │ Employment tribunal —     │ 2025-06-15 │ 4 custodians │ Email,    │ 2026-06-15       │
│               │ unfair dismissal claim    │            │              │ HR system │                  │
├───────────────┼───────────────────────────┼────────────┼──────────────┼───────────┼──────────────────┤
│ LH-2025-0021  │ ICO investigation —       │ 2025-09-01 │ 7 custodians │ All       │ 2026-03-01       │
│               │ data breach notification  │            │              │ systems   │ (overdue —       │
│               │                           │            │              │           │  under review)   │
├───────────────┼───────────────────────────┼────────────┼──────────────┼───────────┼──────────────────┤
│ LH-2026-0023  │ Commercial dispute —      │ 2026-03-14 │ 3 custodians │ Email,    │ 2026-06-14       │
│               │ contract breach claim     │            │              │ CRM, ERP, │                  │
│               │                           │            │              │ Finance   │                  │
└───────────────┴───────────────────────────┴────────────┴──────────────┴───────────┴──────────────────┘
```

## Interaction with GDPR Rights

### Art. 17 Erasure Requests During Active Hold

When an Art. 17 erasure request is received for data subject to a litigation hold:

1. **Acknowledge the request** within normal timeline (30 days).
2. **Inform the data subject** that an exception under Art. 17(3)(e) applies — the data is necessary for the establishment, exercise, or defence of legal claims.
3. **Do NOT disclose** the specific litigation or investigation (legal privilege may apply).
4. **Queue the erasure request** for processing upon hold release.
5. **Document** the exception in the erasure request record and the litigation hold register.
6. **Periodic review**: If the hold is subsequently released, process the queued erasure request promptly.

### Art. 15 Access Requests During Active Hold

Access requests are generally NOT affected by litigation holds. The data subject retains the right to access their data. However:
- Consult Legal counsel before disclosing data that is subject to legal privilege.
- Redact information that could prejudice the litigation (Art. 15(4) — shall not adversely affect the rights and freedoms of others).

### Retention Schedule Interaction

During an active hold:
- The retention clock is **paused** for all in-scope data.
- Automated deletion is **suspended** for in-scope data.
- Upon hold release, the remaining retention period resumes (not resets).
- If the normal retention period would have expired during the hold, deletion is scheduled promptly after release.
