---
name: children-deletion-requests
description: >-
  Manages deletion requests for children's personal data. Covers
  parental-initiated versus child-initiated requests, age of capacity
  assessment, identity verification, scope determination, third-party
  notification obligations, and regulatory timelines under GDPR Art. 17,
  COPPA Section 312.6, and UK AADC Standard 15. Keywords: deletion,
  children, right to erasure, parental request, data deletion, COPPA.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: children-data-protection
  tags: "deletion, children, right-to-erasure, parental-request, data-deletion, coppa"
---

# Managing Deletion Requests for Children's Data

## Overview

Deletion of children's personal data operates under heightened obligations compared to adult data deletion. Under GDPR Article 17, the right to erasure applies with particular force when data was collected from a child — Article 17(1)(f) explicitly creates a right to erasure where personal data has been collected in relation to the offer of information society services to a child under Article 8(1). COPPA Section 312.6 requires operators to provide parents with the ability to review and delete personal information collected from their child. The UK AADC Standard 15 requires prominent and accessible tools to help children exercise their data protection rights. This skill provides a comprehensive framework for processing deletion requests involving children's data, including the complex questions of who can request deletion, verification procedures, scope determination, and third-party notification.

## Legal Framework

### GDPR Article 17(1)(f) — Right to Erasure for Children's Data

"The data subject shall have the right to obtain from the controller the erasure of personal data concerning him or her without undue delay and the controller shall have the obligation to erase personal data without undue delay where [...] the personal data have been collected in relation to the offer of information society services directly to a child referred to in Article 8(1)."

This ground for erasure is distinct from the other Art. 17(1) grounds because:
- It does not require that the original lawful basis has been withdrawn (unlike Art. 17(1)(b) consent withdrawal)
- It does not require that the data is no longer necessary (unlike Art. 17(1)(a))
- It applies specifically because the data was collected from a child, regardless of whether the data subject is still a child at the time of the request
- The CJEU has confirmed in Case C-131/12 (Google Spain) that the right to erasure is especially important where the data was collected when the data subject was a minor

### GDPR Article 17(2) — Third-Party Notification

"Where the controller has made the personal data public, the controller shall, taking account of available technology and the cost of implementation, take reasonable steps, including technical measures, to inform controllers which are processing the personal data that the data subject has requested the erasure [...] of any links to, or copy or replication of, those personal data."

### GDPR Article 12(3) — Response Timeline

"The controller shall provide information on action taken on a request under Articles 15 to 22 to the data subject without undue delay and in any event within one month of receipt of the request."

### COPPA Section 312.6 — Parental Access and Deletion Rights

- **312.6(a)**: Operator must provide a parent, upon request, with a description of the specific types of personal information collected from the child, and the opportunity to refuse to permit the operator's further use or future online collection of personal information from that child, and to direct the operator to delete the personal information collected from that child
- **312.6(b)**: The operator must delete the child's personal information within a reasonable time after receiving the parental request

### UK AADC Standard 15 — Online Tools

"Provide prominent and accessible tools to help children exercise their data protection rights and report concerns."

## Who Can Request Deletion

### Parental-Initiated Deletion

**Applicable When**: The child is below the age at which they can independently exercise data protection rights.

| Jurisdiction | Age Below Which Parent Acts | Legal Basis |
|-------------|:-------------------------:|-------------|
| GDPR (default) | 16 (or national threshold 13-16) | Art. 8(1) — parental consent grounds extend to parental exercise of rights |
| UK | 13 (DPA 2018 Section 9) | ICO guidance: parent exercises rights for children who cannot understand the implications |
| US (COPPA) | 13 | 16 CFR 312.6 — explicit parental right to direct deletion |
| France | 15 | Loi Informatique et Libertes Art. 45 |
| Germany | 16 | GDPR default |
| Spain | 14 | Organic Law 3/2018 Art. 7 |

**Verification Requirements**:
- Verify that the requester is the parent or legal guardian of the child
- Verification methods (proportionate to risk): match against existing parental account, email verification to registered parent email, knowledge-based questions, government ID (for high-risk scenarios)
- Verify the identity of the child whose data is to be deleted (match against account records)

### Child-Initiated Deletion

**Applicable When**: The child has reached sufficient maturity to understand and exercise their data protection rights independently.

**Age of Capacity Assessment**:

The capacity of a child to independently exercise data protection rights is not determined solely by the Art. 8 age threshold. The ICO has stated that a child who is competent to understand their rights may exercise them independently, regardless of the Art. 8 threshold. This is analogous to the Gillick competency principle in UK common law.

| Scenario | Who Initiates | Capacity Assessment |
|----------|--------------|-------------------|
| Child aged 10 requests deletion | Parent must submit the request | Child below Art. 8 threshold in all jurisdictions; lacks capacity |
| Child aged 14 in Belgium (threshold 13) requests deletion | Child can submit independently | Above national threshold; presumed competent |
| Child aged 14 in Germany (threshold 16) requests deletion | Depends on maturity assessment | Below national threshold; controller may accept if child demonstrates understanding |
| Former child (now 18) requests deletion of childhood data | Former child submits independently | Adult; full capacity; Art. 17(1)(f) explicitly protects this scenario |

### Former Child (Adult) Requesting Deletion of Childhood Data

Art. 17(1)(f) does not require the data subject to still be a child at the time of the request. An adult may request deletion of personal data collected when they were a child. This is particularly relevant for:
- Social media posts from adolescence
- Educational records from childhood
- Health data from paediatric treatment
- Photos and videos uploaded by the child or their parents during childhood

The GDPR explicitly supports this by creating Art. 17(1)(f) as a standalone ground — the passage of time does not diminish the right.

## Deletion Request Processing Workflow

### Step 1: Receive and Log Request

```
Request received
│
├─ Channel: email / parental dashboard / in-app tool / postal mail
├─ Requester identity: parent / child / former child (adult)
├─ Child identifier: account ID / name / email
├─ Scope requested: full account deletion / specific data categories
├─ Timestamp: [logged automatically]
├─ Reference number assigned: DEL-CHILD-[YEAR]-[SEQ]
│
└─ Acknowledgement sent within 48 hours
```

### Step 2: Verify Requester Identity and Authority

| Requester | Verification Method | Escalation |
|-----------|-------------------|-----------|
| **Parent (existing account)** | Match request email against registered parent email + security question | If match fails, request government ID |
| **Parent (no existing account)** | Request proof of parental relationship (birth certificate or equivalent) + matching identification | Manual review by DPO |
| **Child (above threshold, existing account)** | Match request against child's registered email + account security | If match fails, involve parent |
| **Child (below threshold)** | Redirect to parent; inform child their parent can submit the request | Provide parent contact mechanism |
| **Former child (adult)** | Standard identity verification (email + security question or ID) | Manual review if account is historical |

### Step 3: Determine Scope of Deletion

| Scope Element | Default Inclusion | Exceptions |
|--------------|:-----------------:|-----------|
| Account profile data (name, DOB, email) | YES | None |
| Activity/usage logs | YES | Anonymised aggregate retained for analytics |
| Content created by child (posts, projects, uploads) | YES | Offer download before deletion |
| Communication records (messages, chats) | YES | May retain if needed for ongoing safeguarding investigation |
| Parental consent records | RETAINED for 6 years | Legal compliance: statute of limitations for GDPR enforcement |
| Financial transaction records | RETAINED for applicable period | Legal compliance: tax and accounting obligations |
| Safety/moderation logs | RETAINED if active investigation | Safeguarding obligation override per Art. 17(3)(d) |
| Backup copies | YES (scheduled purge) | Deleted within backup rotation cycle (max 30 days) |
| Third-party copies | NOTIFIED for deletion | Art. 17(2) obligation to inform third-party controllers |

### Step 4: Execute Deletion

**Timeline**: Within one month of verified request (Art. 12(3)). Extension of up to two additional months permitted for complex requests, with notification to the requester within the initial one-month period.

**Technical Deletion Process**:

1. **Primary database**: Execute DELETE operations across all tables containing the child's personal data
2. **Search indices**: Remove the child's data from Elasticsearch, Solr, or equivalent search indices
3. **Caches**: Invalidate all cached entries containing the child's data (Redis, CDN, application cache)
4. **File storage**: Delete uploaded files (photos, documents, audio) from primary storage (S3, Azure Blob, GCS)
5. **Analytics databases**: Remove or anonymise records in analytics systems (BigQuery, Redshift, Snowflake)
6. **Logs**: Purge application logs containing the child's personal data (ELK stack, Splunk, CloudWatch)
7. **Machine learning models**: If the child's data was used to train ML models, assess whether the model must be retrained or whether the training data inclusion is irreversible (document the assessment)
8. **Backups**: Schedule deletion from backup systems within the next backup rotation cycle (max 30 days)
9. **Third-party notification**: Send deletion requests to all third parties that received the child's data per Art. 17(2)

### Step 5: Confirm Deletion

```json
{
  "deletion_reference": "DEL-CHILD-2026-0284",
  "child_identifier": "child_bp_8f3a2d",
  "requester": "parent_bp_c7e4f1",
  "requester_type": "parent",
  "request_date": "2026-02-15T09:00:00Z",
  "verification_date": "2026-02-16T11:30:00Z",
  "deletion_scope": {
    "account_data": "deleted",
    "activity_logs": "deleted",
    "content": "deleted (download offered, declined by parent)",
    "communications": "deleted",
    "consent_records": "retained (legal compliance, expiry 2032-02-16)",
    "backups": "scheduled_purge_2026-03-16"
  },
  "third_party_notifications": [
    {
      "recipient": "AWS (hosting provider)",
      "notification_date": "2026-02-17",
      "scope": "all stored objects for child account",
      "confirmation": "pending"
    }
  ],
  "deletion_completed_date": "2026-02-17T14:00:00Z",
  "backup_purge_date": "2026-03-16T02:00:00Z",
  "confirmation_sent_to_requester": "2026-02-17T14:30:00Z"
}
```

### Step 6: Post-Deletion Verification

1. Attempt to retrieve the child's data from all systems listed in Step 4
2. Confirm that no personal data is returned from any system (except legally retained records)
3. Log the verification outcome
4. Schedule backup purge verification for 30 days after primary deletion

## BrightPath Learning Inc. — Deletion Implementation

### Deletion Channels

| Channel | Description | Response Time |
|---------|-------------|---------------|
| **Parental dashboard** | One-click "Delete Account" button with confirmation dialog | Immediate processing |
| **In-app (child)** | "Delete my stuff" button in privacy centre (for children above threshold) | Immediate processing |
| **Email** | privacy@brightpathlearning.eu | Acknowledgement within 48 hours |
| **Postal** | BrightPath Learning Inc., 200 Education Lane, Amsterdam, 1012 AB, Netherlands | Acknowledgement within 5 business days |

### Deletion Flow (Parental Dashboard)

```
Parent clicks "Delete Alex's Account"
│
├─ Confirmation dialog:
│  "This will permanently delete Alex's account and all their data,
│   including learning progress and any work they've saved.
│   This cannot be undone."
│  [Download Alex's data first]  [Delete everything]  [Cancel]
│
├─ If "Download first" selected:
│  ├─ Generate data export (JSON + PDF progress report)
│  ├─ Email download link to parent (valid for 7 days)
│  └─ Return to deletion confirmation
│
├─ If "Delete everything" selected:
│  ├─ Re-verify parent identity (password or security question)
│  ├─ Execute deletion across all systems
│  ├─ Send confirmation email to parent
│  └─ Display confirmation: "Alex's account and data have been deleted.
│      Backup copies will be removed within 30 days."
│
└─ If "Cancel" selected:
   └─ Return to dashboard (no action taken)
```

### Handling Competing Interests

| Scenario | Outcome | Rationale |
|----------|---------|-----------|
| Parent requests deletion; child wants to keep account | Parent's request takes priority for children below threshold | Parent holds consent authority under Art. 8 |
| Child (16+) requests deletion; parent wants to retain | Child's request takes priority | Child above UK threshold; autonomous rights holder |
| School requests deletion of student data; parent wants to retain | Delete from BrightPath; inform parent they may retain their own copies | School's FERPA/contractual authority governs school-directed data |
| Safeguarding investigation active on the child's account | Retention of relevant data permitted under Art. 17(3)(d) | Vital interests / public interest in protection of the child |
| Child's data needed for ongoing legal claim | Retention permitted under Art. 17(3)(e) | Legal claims exception |

## Exception Grounds — When Deletion Can Be Refused

Art. 17(3) provides exceptions where the right to erasure does not apply:

| Exception | Art. 17(3) Reference | Application to Children's Data |
|-----------|---------------------|-------------------------------|
| Freedom of expression | Art. 17(3)(a) | Rarely applies to children's data; would require compelling journalistic or artistic purpose |
| Legal obligation | Art. 17(3)(b) | Tax records of transactions; mandatory educational records under national law |
| Public health | Art. 17(3)(c) | Vaccination records; public health surveillance data |
| Archiving in public interest | Art. 17(3)(d) | Educational research (with ethical approval and anonymisation) |
| Legal claims | Art. 17(3)(e) | Data needed for establishment, exercise, or defence of legal claims |

**Important**: Even where an exception applies, the controller should delete as much data as possible and retain only the minimum necessary to satisfy the exception.

## Common Compliance Failures

1. **No child-accessible deletion tool**: Requiring children to navigate adult-oriented privacy settings or contact forms to exercise deletion rights
2. **Parental deletion blocked by verification failure**: Overly burdensome verification requirements that prevent parents from exercising deletion rights
3. **Incomplete deletion scope**: Deleting the account profile but retaining activity logs, analytics data, or cached copies
4. **No backup deletion**: Deleting from production systems but retaining data indefinitely in backups
5. **No third-party notification**: Failing to notify third parties that received the child's data per Art. 17(2)
6. **Exceeding the one-month timeline**: Processing deletion requests beyond the Art. 12(3) one-month deadline without notifying the requester of an extension
7. **No deletion of historical data on adult request**: Refusing to delete childhood data when the (now adult) data subject requests it, on the grounds that the data is "old" or "archived"

## Enforcement Precedents

- **Google (CJEU, C-131/12, Google Spain, 2014)**: Established the right to erasure including for data published during minority; the Court emphasised the importance of erasure for information that is "inadequate, irrelevant or no longer relevant, or excessive"
- **TikTok (ICO, 2023)**: GBP 12.7 million fine included findings on failure to provide adequate mechanisms for parents and children to exercise rights including deletion
- **Musical.ly/TikTok (FTC, 2019)**: USD 5.7 million settlement required TikTok to delete all information collected from children under 13 and provide a mechanism for parents to request deletion going forward
- **Edmodo (FTC, 2023)**: USD 6 million penalty; order required Edmodo to delete children's personal information collected in violation of COPPA and establish a deletion program
- **Google (CNIL France, 2022)**: EUR 150 million fine for making it difficult for users to refuse cookies; the CNIL noted the platform's large child user base as an aggravating factor, and the difficulty children would face in exercising opt-out rights

## Integration Points

- **Children's Data Minimisation**: Data minimisation reduces the scope and complexity of deletion — less data collected means less data to delete
- **COPPA Compliance**: COPPA Section 312.6 provides explicit parental deletion rights that operate alongside GDPR Art. 17
- **GDPR Parental Consent**: The parent who gave consent under Art. 8 has the authority to request deletion by withdrawing consent under Art. 7(3)
- **EdTech Privacy Assessment**: School-directed EdTech must handle deletion requests from both parents and schools, with end-of-year deletion as standard
- **UK AADC Implementation**: AADC Standard 15 requires prominent, accessible deletion tools designed for children
