---
name: processing-right-to-rectification
description: >-
  Processes GDPR Article 16 right to rectification requests, covering verification
  of corrected data accuracy, notification to recipients under Article 19,
  timeline management, and completion of incomplete data. Activate for rectification,
  correction request, inaccurate data, Art. 16, data correction queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-subject-rights
  tags: "right-to-rectification, gdpr-article-16, data-correction, inaccurate-data, data-quality"
---

# Processing Right to Rectification

## Overview

The right to rectification under GDPR Article 16 gives data subjects the right to have inaccurate personal data corrected without undue delay, and to have incomplete personal data completed. This skill provides the complete workflow for receiving, verifying, implementing, and confirming rectification requests.

## Legal Foundation

### GDPR Article 16 — Right to Rectification

The data subject has the right to obtain from the controller without undue delay the rectification of inaccurate personal data concerning them. Taking into account the purposes of the processing, the data subject has the right to have incomplete personal data completed, including by means of providing a supplementary statement.

### GDPR Article 19 — Notification Obligation

The controller shall communicate any rectification to each recipient to whom the personal data have been disclosed, unless this proves impossible or involves disproportionate effort. The controller shall inform the data subject about those recipients if the data subject requests it.

### GDPR Article 5(1)(d) — Accuracy Principle

Personal data shall be accurate and, where necessary, kept up to date. Every reasonable step must be taken to ensure that personal data that are inaccurate, having regard to the purposes for which they are processed, are erased or rectified without delay.

## Rectification Processing Workflow

### Step 1: Receive and Log the Request

1. Log the request with reference REC-YYYY-NNNN.
2. Record the specific data the subject claims is inaccurate or incomplete.
3. Record what the subject asserts the correct or complete data should be.
4. Record any supporting evidence provided.
5. Send acknowledgement within 3 business days.
6. Verify identity using tiered verification.

### Step 2: Identify Affected Data

1. Locate the specific data items cited as inaccurate across all systems:
   - CRM and customer database
   - Marketing platforms
   - Analytics systems
   - Third-party processors
   - Backup systems
2. Document the current value of each data item.
3. Document the correction requested for each item.

### Step 3: Verify the Correction

Two types of rectification require different verification:

#### Type A: Correction of Inaccurate Data

| Data Category | Verification Method | Example |
|---------------|-------------------|---------|
| Name / spelling | Accept subject's assertion unless reason to doubt | Subject states name is "MacLeod" not "McLeod" — accept |
| Date of birth | Request documentary evidence (passport, birth certificate) | Subject provides passport scan showing correct DOB |
| Address | Accept subject's assertion for current address; verify historical addresses against postal records if relevant | Subject provides utility bill as confirmation |
| Employment details | Accept subject's assertion or verify with employer (with subject's consent) | Subject states correct job title |
| Financial data | Verify against source records (bank statements, invoices) | Cross-reference with payment processor records |
| Technical data (IP, device) | Assess whether correction is factually possible — these are system-generated observations | If system logs show IP X, correction may not be appropriate unless a logging error occurred |

#### Type B: Completion of Incomplete Data

1. Assess whether the additional data is relevant to the purposes of processing.
2. If relevant, add the supplementary data.
3. If not relevant (i.e., the additional data is not necessary for any processing purpose), the controller may decline to add it but should inform the subject of the reason.

### Step 4: Decision

| Scenario | Action |
|----------|--------|
| Verification confirms inaccuracy | Rectify the data across all systems |
| Verification is inconclusive | Apply restriction under Art. 18(1)(a) while investigation continues |
| Verification confirms data is accurate | Inform the subject that the data has been verified as accurate; note the subject's objection; offer the right to add a supplementary statement |
| Completion request is relevant | Add the supplementary data |
| Completion request is not relevant to processing purposes | Decline with explanation |

### Step 5: Implement the Rectification

1. Update the data across all primary systems simultaneously (or as close to simultaneously as technically feasible).
2. Update any derived data or reports that incorporate the inaccurate data.
3. Flag data in backup systems for correction at next rotation.
4. Document:
   - Original value
   - Corrected value
   - Date of rectification
   - Systems updated
   - Person who implemented the change

### Step 6: Notify Recipients Under Art. 19

1. Identify all recipients who received the inaccurate data (reference Art. 30 records).
2. Send rectification notification to each recipient:
   - The specific data that has been corrected (without disclosing the subject's identity where possible)
   - The corrected value
   - Instruction to update their records accordingly
   - 14-day confirmation deadline
3. Log all notifications and confirmations.

### Step 7: Confirm to the Data Subject

Within the 30-day response deadline, send confirmation including:
- The specific data items that have been rectified
- The corrected values now held
- Confirmation that all systems have been updated
- Expected completion date for backup system corrections (if applicable)
- List of third-party recipients notified (if requested by the subject)
- If any part of the rectification was declined, the reasons and the subject's right to complain

## Response Timeline

- **Standard deadline**: 30 calendar days from receipt of the request.
- **Extension**: Up to 60 additional days for complex cases (Art. 12(3)).
- **Implementation target**: Rectification should be applied to primary systems within 5 business days of the verification decision, even if the formal response is still being prepared.
