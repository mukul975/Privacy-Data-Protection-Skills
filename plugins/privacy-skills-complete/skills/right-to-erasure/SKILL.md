---
name: right-to-erasure
description: >-
  Implements the GDPR Article 17 right to erasure (right to be forgotten) workflow,
  covering all six grounds for erasure, five exceptions, technical deletion versus
  anonymization decisions, and third-party notification under Article 19.
  Activate for erasure request, deletion request, right to be forgotten, Art. 17 queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-subject-rights
  tags: "right-to-erasure, right-to-be-forgotten, gdpr-article-17, data-deletion, anonymization"
---

# Implementing Right to Erasure Workflow

## Overview

The right to erasure under GDPR Article 17 allows data subjects to request the deletion of their personal data. This right is not absolute — it is subject to specific grounds for erasure and a set of exceptions. This skill provides the complete operational procedure for receiving, assessing, executing, and confirming erasure requests.

## Legal Foundation

### GDPR Article 17 — Right to Erasure ('Right to be Forgotten')

#### Six Grounds for Erasure Under Art. 17(1)

The data subject has the right to obtain erasure where one of the following grounds applies:

1. **Art. 17(1)(a) — Purpose fulfilment**: The personal data are no longer necessary in relation to the purposes for which they were collected or otherwise processed.
2. **Art. 17(1)(b) — Consent withdrawal**: The data subject withdraws consent on which the processing is based under Art. 6(1)(a) or Art. 9(2)(a), and there is no other legal ground for the processing.
3. **Art. 17(1)(c) — Successful objection**: The data subject objects pursuant to Art. 21(1) and there are no overriding legitimate grounds for the processing, or the data subject objects to processing for direct marketing under Art. 21(2).
4. **Art. 17(1)(d) — Unlawful processing**: The personal data have been unlawfully processed.
5. **Art. 17(1)(e) — Legal obligation**: The personal data have to be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject.
6. **Art. 17(1)(f) — Child's data (information society services)**: The personal data have been collected in relation to the offer of information society services referred to in Art. 8(1).

#### Five Exceptions Under Art. 17(3)

Erasure does NOT apply to the extent that processing is necessary for:

1. **Art. 17(3)(a) — Freedom of expression and information**: Exercising the right of freedom of expression and information.
2. **Art. 17(3)(b) — Legal obligation**: Compliance with a legal obligation which requires processing by Union or Member State law to which the controller is subject, or for the performance of a task carried out in the public interest or in the exercise of official authority vested in the controller.
3. **Art. 17(3)(c) — Public health**: Reasons of public interest in the area of public health in accordance with Art. 9(2)(h) and (i), and Art. 9(3).
4. **Art. 17(3)(d) — Archiving/research**: Archiving purposes in the public interest, scientific or historical research purposes, or statistical purposes in accordance with Art. 89(1), in so far as the right to erasure is likely to render impossible or seriously impair the achievement of the objectives of that processing.
5. **Art. 17(3)(e) — Legal claims**: The establishment, exercise, or defence of legal claims.

### GDPR Article 19 — Notification Obligation

The controller shall communicate any erasure of personal data to each recipient to whom the personal data have been disclosed, unless this proves impossible or involves disproportionate effort. The controller shall inform the data subject about those recipients if the data subject requests it.

## Erasure Processing Workflow

### Step 1: Receive and Log the Erasure Request

1. Log the request with a unique reference (format: ERA-YYYY-NNNN).
2. Record the channel, timestamp (UTC), and identity of the requester.
3. Send acknowledgement within 3 business days.
4. Verify identity using the same tiered approach as DSAR processing (low/medium/high risk).

### Step 2: Identify the Ground for Erasure

1. Review the request to determine which of the six grounds under Art. 17(1)(a)-(f) the data subject is invoking.
2. If the data subject has not specified a ground, assess which ground(s) are applicable based on the facts.
3. Document the identified ground(s) in the processing record.

### Step 3: Check for Applicable Exceptions

For each ground identified, evaluate whether any of the five exceptions under Art. 17(3)(a)-(e) apply:

| Exception | Assessment Question | Common Scenarios at Meridian Analytics Ltd |
|-----------|--------------------|--------------------------------------------|
| Freedom of expression (a) | Is this data published as part of journalism or public discourse? | Published research reports, public-facing analytics |
| Legal obligation (b) | Is there a statutory retention requirement? | Financial records under Companies Act 2006 (6 years), tax records under HMRC requirements (6 years), anti-money laundering records under MLR 2017 (5 years) |
| Public health (c) | Is this data necessary for public health purposes? | Rare — applies to health data processors |
| Archiving/research (d) | Would erasure render research impossible or seriously impaired? | Anonymised datasets used in published research |
| Legal claims (e) | Are there pending or anticipated legal proceedings involving this data? | Active disputes, regulatory investigations, litigation hold data |

### Step 4: Deletion vs Anonymization Decision Tree

```
[Erasure Ground Established & No Exception Applies]
         │
         ▼
[Can data be permanently deleted from all systems?]
   │
   ├── Yes ──► [PERMANENT DELETION]
   │            - Remove from primary databases
   │            - Remove from backup systems within next backup cycle
   │            - Remove from third-party processors (Art. 19)
   │            - Purge from caches, logs, and temporary storage
   │            - Verify deletion across all systems
   │
   └── No ──► [Assess why deletion is not possible]
               │
               ├── Technical constraint (embedded in backup tapes)
               │     └── [ANONYMIZE + schedule deletion at next backup rotation]
               │         [Maximum retention of backup: 90 days at Meridian Analytics Ltd]
               │
               ├── Partial exception applies (some data needed for legal obligation)
               │     └── [PARTIAL DELETION + ANONYMIZATION]
               │         [Delete data not subject to exception]
               │         [Retain excepted data with restricted access]
               │         [Anonymize where possible]
               │
               └── Data is intermingled with other subjects' data
                     └── [TARGETED ANONYMIZATION]
                         [Replace identifiers with irreversible pseudonyms]
                         [Remove all direct identifiers]
                         [Verify re-identification risk < 0.05%]
```

### Step 5: Execute the Erasure

1. **Primary systems**: Execute deletion queries/commands across all identified data stores.
2. **Backup systems**: Flag data for deletion at next backup rotation cycle (document the expected completion date, maximum 90 days).
3. **Third-party processors**: Issue erasure instructions to all processors under Art. 28 agreements. Record the instruction date and request confirmation of completion.
4. **Caches and temporary storage**: Purge application caches, CDN caches, and temporary files.
5. **Search engine de-indexing**: Where personal data was made public (Art. 17(2)), submit de-indexing requests to search engines.

### Step 6: Notify Third-Party Recipients (Art. 19)

1. Identify all recipients to whom the personal data was disclosed (reference the Art. 30 records of processing).
2. Send erasure notification to each recipient with:
   - The data subject reference (anonymised)
   - The specific data to be erased
   - The legal basis for the erasure request
   - A deadline for confirmation of erasure (14 calendar days)
3. Record each notification and the recipient's confirmation.
4. If the data subject requests it, provide the list of recipients notified.

### Step 7: Verify and Confirm

1. Run verification checks across all systems to confirm data has been erased or anonymised.
2. Obtain confirmation from all third-party processors.
3. Compile the erasure completion record.
4. Send confirmation to the data subject within the 30-day response deadline, including:
   - Confirmation that erasure has been completed
   - Any partial exceptions applied (with legal basis)
   - Expected completion date for backup system erasure (if applicable)
   - List of third parties notified (if requested)

### Step 8: Record Retention

1. Retain the erasure processing record (request details, assessment, execution log, confirmations) for 3 years.
2. The record must NOT contain the erased personal data itself — only metadata about the erasure process.
3. Store a suppression record (minimum identifiers needed to recognise future requests from the same individual and prevent re-collection) where appropriate.

## Response Timeline

- **Standard deadline**: 30 calendar days from receipt (or from identity verification).
- **Extension**: Up to 60 additional days for complex requests (Art. 12(3)), with notification to the data subject within the initial 30-day period.
- **Backup erasure**: Must be completed within the next full backup rotation cycle (maximum 90 days at Meridian Analytics Ltd), documented in the response.
