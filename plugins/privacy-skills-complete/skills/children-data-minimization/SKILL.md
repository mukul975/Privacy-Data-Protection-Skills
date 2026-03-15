---
name: children-data-minimization
description: >-
  Implements strict data minimization and retention limits for
  children's personal data under GDPR Art. 5(1)(c), Recital 38, UK
  AADC Standard 8, and COPPA Section 312.7. Covers strict necessity
  testing, shorter retention periods, limited profiling, parental
  dashboard design, and automated deletion. Keywords: data
  minimization, children, retention, necessity test, parental dashboard.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: children-data-protection
  tags: "data-minimization, children, retention, necessity-test, parental-dashboard, deletion"
---

# Children's Data Minimisation and Retention Limits

## Overview

Data minimisation for children's data requires a stricter interpretation of GDPR Article 5(1)(c) ("adequate, relevant and limited to what is necessary") than the standard adult context. Recital 38 states that children merit specific protection with regard to their personal data, as they may be less aware of the risks, consequences, and safeguards concerned and their rights in relation to the processing of personal data. The UK AADC Standard 8 explicitly requires that services collect and retain "only the minimum amount of personal data needed to provide the elements of the service in which a child is actively and knowingly engaged." COPPA Section 312.7 prohibits conditioning a child's participation on the collection of more personal information than is reasonably necessary. This skill provides a comprehensive framework for applying these heightened standards.

## Legal Framework

### GDPR Article 5(1)(c) — Data Minimisation Principle

"Personal data shall be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed."

When applied to children's data, "necessary" is interpreted strictly. The EDPB has confirmed that the vulnerability of children as data subjects (WP248rev.01 Criterion 7) elevates the data minimisation obligation.

### GDPR Article 5(1)(e) — Storage Limitation Principle

"Personal data shall be kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed."

For children's data, retention periods should be shorter than for adult data given that: (a) the purposes of processing often have a shorter useful life for children (e.g., educational progress in a specific grade), (b) the risk of harm from data exposure increases with retention duration, and (c) the child may not have meaningfully consented to long-term retention.

### GDPR Recital 38 — Specific Protection for Children

"Children merit specific protection with regard to their personal data, as they may be less aware of the risks, consequences and safeguards concerned and their rights in relation to the processing of personal data. Such specific protection should, in particular, apply to the use of personal data of children for the purposes of marketing or creating personality or user profiles and the collection of personal data with regard to children when using services offered directly to children."

### UK AADC Standard 8 — Data Minimisation

"Collect and retain only the minimum amount of personal data you need to provide the elements of your service in which a child is actively and knowingly engaged. Give children separate choices over which elements they wish to activate."

Key ICO interpretations:
- "Actively and knowingly engaged" means the child is intentionally using a specific feature, not passively generating data through background collection
- "Separate choices" means children must be able to use core service features without being forced to activate data-intensive optional features
- Background data collection (location, microphone, contacts, gyroscope) is prohibited unless the child actively triggers a feature requiring it

### COPPA Section 312.7 — Data Minimisation

"An operator is prohibited from conditioning a child's participation in a game, the offering of a prize, or another activity on the child disclosing more personal information than is reasonably necessary to participate in such activity."

## Strict Necessity Test

For each data element collected from a child, the controller must apply the Strict Necessity Test — a more demanding evaluation than the standard proportionality assessment used for adult data.

### Test Questions

| # | Question | Pass Criteria |
|---|---------|---------------|
| 1 | Is this data element required for the specific feature the child is actively using? | The feature cannot function without this specific data element |
| 2 | Could the feature work with less precise data? | No less granular alternative exists (e.g., age range instead of exact DOB, city instead of precise location) |
| 3 | Could the feature work with anonymised or pseudonymised data? | Anonymisation or pseudonymisation would make the feature non-functional |
| 4 | Is this data element collected for the child's benefit or the controller's benefit? | Primary beneficiary must be the child; controller benefit alone is insufficient |
| 5 | Would a reasonable parent expect this data to be collected for this feature? | The collection aligns with parental expectations for the service |
| 6 | Is the data retained only for the duration the feature is in active use? | Data is deleted when the feature session ends or the shortest defensible retention period expires |

### Application to Common Data Categories

| Data Category | Typical Justification | Strict Necessity Outcome |
|--------------|----------------------|------------------------|
| Full name | Account identification | Minimise to first name or username only. Full legal name needed only for parental verification. |
| Exact date of birth | Age verification | Collect for age gate, then retain only age band (e.g., "10-12") or a boolean "is_under_threshold". Do not retain exact DOB unless legally required. |
| Email address | Account recovery, notifications | For children under the applicable consent threshold, collect only the parent's email. Child email collected only if the child is above the consent threshold. |
| Precise geolocation | Content localisation | Country or region-level derivation from IP sufficient for localisation. Precise GPS never collected from children unless the feature specifically requires it (e.g., emergency location service) and the child actively triggers it. |
| Device identifiers (IDFA, GAID) | Analytics, advertising | Never collected for advertising. Collected for analytics only if anonymised at collection point. Use session-based or first-party identifiers instead. |
| Photos/videos/audio | Profile picture, content creation | Profile: use pre-set avatars, not photo upload. Content creation: process in session, do not store server-side unless the child explicitly saves. Delete on session end. |
| Browsing history | Personalisation | Do not retain browsing history for children. Use session-only context for recommendations. |
| Contact list | Social features | Never access or upload the child's contact list. Use invite codes or usernames instead. |
| Purchase history | Transaction records | Retain for legal compliance (tax, consumer protection) only. Minimise to transaction ID and amount, not item details. |

## Retention Period Framework

Children's data must be subject to shorter retention periods than adult data. The following framework establishes maximum retention periods for common categories.

### Retention Schedule

| Data Category | Maximum Retention | Justification | Deletion Method |
|--------------|------------------|---------------|-----------------|
| **Age verification data** (DOB, verification outcome) | Duration of account + 30 days | Required to maintain age-appropriate experience | Automated purge on account deletion + 30 days |
| **Account data** (name, username, parent email) | Duration of account + 30 days | Required for service delivery and parental oversight | Automated purge on account deletion + 30 days |
| **Learning/activity progress** | Duration of account or academic year, whichever is shorter | Educational purpose expires at end of learning period | Parent-triggered or automated end-of-year deletion |
| **Session data** (pages viewed, features used) | 30 days | Service improvement analytics | Rolling 30-day automated deletion |
| **Content created by child** (drawings, text, projects) | Duration of account | Created by the child for their own use | Returned to parent/child on account deletion |
| **Communication data** (messages within platform) | 90 days | Safety moderation and abuse prevention | Rolling 90-day automated deletion |
| **Error/crash logs** | 7 days | Technical debugging | Rolling 7-day automated deletion |
| **Parental consent records** | Duration of account + 6 years | Legal compliance (statute of limitations for GDPR claims) | Automated purge 6 years after account deletion |
| **Parental verification data** (credit card, ID) | Verification outcome retained; source documents deleted within 48 hours | Verification purpose fulfilled immediately | Immediate deletion of source; outcome flag retained |

### End-of-Academic-Year Deletion

For educational platforms, the end of the academic year represents a natural data lifecycle milestone. BrightPath Learning implements the following end-of-year protocol:

1. **30 days before academic year end**: Parent receives notification that learning data will be archived
2. **End of academic year**: Learning progress data is exported to a parent-downloadable report (PDF)
3. **14 days after year end**: If parent has not requested retention, granular activity data is deleted; only aggregate progress scores are retained for the next year's placement
4. **60 days after year end**: Aggregate scores deleted unless the child continues to the next year's service

## Parental Dashboard Design

The parental dashboard is the primary mechanism for parental oversight and control over children's data. It must provide meaningful transparency and actionable controls.

### Required Dashboard Features

| Feature | Description | GDPR Basis |
|---------|-------------|-----------|
| **Data inventory** | Visual display of all personal data held about the child, organised by category | Art. 15 (access right, exercised by parent under Art. 8) |
| **Purpose display** | For each data category, show the specific purpose and lawful basis | Art. 13(1)(c) transparency |
| **Consent controls** | Per-purpose toggles to grant or withdraw consent | Art. 7(3) withdrawal mechanism |
| **Data download** | One-click export of all child's data in machine-readable format (JSON, CSV) | Art. 20 portability (exercised by parent) |
| **Data deletion** | One-click account and data deletion with confirmation | Art. 17 erasure (exercised by parent) |
| **Activity log** | Summary of child's recent activity on the platform (features used, time spent) | AADC Standard 11 (parental controls) |
| **Privacy settings** | Controls for profile visibility, data sharing, communication features | AADC Standard 7 (default settings) |
| **Notification preferences** | Control over what notifications the child receives | AADC Standard 13 (nudge techniques) |
| **Child age display** | Shows the child's current age and the date when they will reach the next age threshold | AADC Standard 3 (age-appropriate application) |

### BrightPath Learning — Dashboard Implementation

```
┌─────────────────────────────────────────────────────────┐
│  BrightPath Learning — Parent Dashboard                 │
│  Child: Alex (Age 11, France — threshold: 15)           │
│  Account created: 2025-09-01                            │
│  Next age review: 2026-09-01 (age 12)                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  DATA WE HOLD                                           │
│  ┌──────────────────┬─────────────────┬──────────────┐  │
│  │ Category         │ Purpose         │ Status       │  │
│  ├──────────────────┼─────────────────┼──────────────┤  │
│  │ First name       │ Account ID      │ Required     │  │
│  │ Age band (10-12) │ Content level   │ Required     │  │
│  │ Learning scores  │ Progress track  │ ✓ Consented  │  │
│  │ Game activity    │ Recommendations │ ✗ Not active │  │
│  └──────────────────┴─────────────────┴──────────────┘  │
│                                                         │
│  PRIVACY CONTROLS                                       │
│  [✓] Share progress reports with me (parent)            │
│  [ ] Allow content-based recommendations                │
│  [✓] Show learning badges on Alex's profile             │
│                                                         │
│  ACTIONS                                                │
│  [Download Alex's data]  [Delete Alex's account]        │
│  [View activity log]     [Contact DPO]                  │
│                                                         │
│  ACTIVITY THIS WEEK                                     │
│  Mon: 25 min — Maths Level 3                            │
│  Tue: 30 min — Reading Comprehension                    │
│  Wed: 15 min — Science Quiz                             │
│  Total: 1h 10min                                        │
│                                                         │
│  Alex will reach the French consent threshold (15)      │
│  on approximately 2029-06-15. At that point, consent    │
│  authority will transfer to Alex.                       │
└─────────────────────────────────────────────────────────┘
```

## Automated Deletion Implementation

### Technical Architecture

1. **Retention metadata**: Every data record includes a `retention_category` field mapped to the retention schedule and an `expires_at` timestamp
2. **Deletion scheduler**: A daily batch job identifies all records where `expires_at < current_timestamp` and executes deletion
3. **Cascade deletion**: Account deletion triggers cascade deletion across all related tables (activity logs, content, communications, consent records subject to their own retention schedule)
4. **Deletion verification**: Post-deletion audit confirms that records are removed from primary storage, backup systems, and any caches
5. **Backup purge**: Backups containing children's data are subject to a maximum 30-day retention cycle. Backup restoration procedures include a re-deletion step for expired children's data.

### Deletion Logging

Every deletion event is logged for accountability:
```json
{
  "deletion_id": "DEL-2026-0047821",
  "trigger": "automated_retention_expiry",
  "data_category": "session_data",
  "child_identifier": "child_bp_8f3a2d",
  "records_deleted": 847,
  "deletion_timestamp": "2026-03-14T02:00:00Z",
  "deletion_scope": "primary_database, elasticsearch_index, redis_cache",
  "backup_purge_scheduled": "2026-04-13T02:00:00Z",
  "verified_by": "automated_verification_check"
}
```

## Common Compliance Failures

1. **Adult-equivalent retention**: Applying the same retention periods to children's data as adult data, without justification for why shorter periods are not feasible
2. **Indefinite retention until deletion request**: Retaining children's data indefinitely unless a parent specifically requests deletion violates Art. 5(1)(e) storage limitation
3. **Background data collection**: Collecting device identifiers, location, accelerometer, or microphone data in the background without the child actively using a feature that requires it
4. **Contact list access**: Requesting access to the child's device contact list for "find friends" features without strict necessity
5. **No parental dashboard**: Failing to provide parents with a meaningful mechanism to view, control, and delete their child's data
6. **Backup retention gap**: Deleting data from production systems but retaining it indefinitely in backups

## Enforcement Precedents

- **TikTok (DPC Ireland, 2023)**: EUR 345 million fine included findings on excessive data collection from children, including default public profiles exposing children's content to all users, violating Art. 5(1)(c) data minimisation.
- **YouTube/Google (FTC, 2019)**: USD 170 million settlement for collecting persistent identifiers from child-directed channel viewers for advertising purposes — data not necessary for the service the child was using.
- **Epic Games/Fortnite (FTC, 2022)**: USD 275 million for collecting personal information from children beyond what was necessary, including enabling real-time voice communications by default.

## Integration Points

- **GDPR Parental Consent**: Parental consent scope should be limited to data collection justified by the necessity test — parents should not be asked to consent to unnecessary collection
- **UK AADC Implementation**: AADC Standard 8 is the primary operational standard for children's data minimisation in the UK
- **Children's Profiling Limits**: Data minimisation directly limits the data available for profiling, reinforcing AADC Standard 12 restrictions
- **Children's Deletion Requests**: The retention framework defines what data exists to be deleted and when automatic deletion occurs
- **EdTech Privacy Assessment**: Educational platforms must balance data minimisation with legitimate educational record-keeping needs
