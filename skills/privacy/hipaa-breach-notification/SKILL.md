---
name: hipaa-breach-notification
description: >-
  Executes breach notification under HIPAA Breach Notification Rule (45 CFR
  164.400-414). Covers 60-day individual notification, HHS/OCR reporting for
  breaches of 500+ individuals (immediate) and under 500 (annual log), state
  attorney general notification, media notification for 500+ in a single state,
  and breach risk assessment using the four-factor test. Keywords: HIPAA, breach
  notification, PHI, HHS, OCR, covered entity, business associate.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-breach-response
  tags: "hipaa, breach-notification, phi, hhs-ocr, covered-entity, business-associate"
---

# Executing HIPAA Breach Notification

## Overview

The HIPAA Breach Notification Rule (45 CFR §§164.400-414) requires HIPAA covered entities and their business associates to provide notification following a breach of unsecured protected health information (PHI). This skill covers the complete HIPAA breach notification workflow, including the four-factor risk assessment, individual notification requirements, HHS/OCR reporting obligations, state attorney general notification, and media notification thresholds.

## Key Definitions

| Term | Definition | Source |
|------|-----------|--------|
| Breach | Acquisition, access, use, or disclosure of PHI in a manner not permitted under the Privacy Rule that compromises the security or privacy of the PHI | 45 CFR §164.402 |
| Unsecured PHI | PHI that is not rendered unusable, unreadable, or indecipherable to unauthorized persons through encryption or destruction per HHS guidance | 45 CFR §164.402 |
| Covered Entity | Health plan, healthcare clearinghouse, or healthcare provider that transmits health information electronically | 45 CFR §160.103 |
| Business Associate | Person or entity that creates, receives, maintains, or transmits PHI on behalf of a covered entity | 45 CFR §160.103 |
| Discovery | The first day the breach is known to the covered entity (or would have been known through reasonable diligence) | 45 CFR §164.404(a)(2) |

## Four-Factor Breach Risk Assessment — 45 CFR §164.402(2)

A covered entity must assess the probability that PHI has been compromised using four factors:

### Factor 1: Nature and Extent of PHI Involved
- What types of identifiers were involved? (name, SSN, date of birth, diagnosis codes, treatment records)
- How many records were involved?
- Does the PHI include information that increases the risk of identity theft or financial fraud (SSN, financial information)?
- Does the PHI include clinical information that could cause stigma or embarrassment (mental health, substance abuse, HIV status, reproductive health)?

### Factor 2: Unauthorized Person Who Used or Received the PHI
- Was the recipient another covered entity or business associate bound by HIPAA?
- Was the recipient a person with no obligation to protect the PHI?
- Is the recipient known or unknown?
- Does the recipient have the ability to re-identify de-identified data?

### Factor 3: Whether the PHI Was Actually Acquired or Viewed
- Is there evidence the PHI was actually accessed or viewed?
- Was the PHI returned unopened (e.g., misdirected mail returned by postal service)?
- Do forensic logs show the data was downloaded, copied, or transmitted?
- Was the exposure theoretical (e.g., server was accessible but no evidence of access)?

### Factor 4: Extent to Which Risk Has Been Mitigated
- Was the PHI recovered or destroyed?
- Did the unauthorized recipient provide assurances (written attestation) of destruction?
- Were technical controls in place that limited access (password-protected files, short exposure window)?
- Has the covered entity obtained confirmation that the PHI was not further disclosed?

### Assessment Outcome
If the four-factor assessment demonstrates a **low probability** that the PHI has been compromised, the incident is not a reportable breach. The assessment must be documented. If there is any doubt, the incident should be treated as a reportable breach.

## Notification Requirements

### Individual Notification — 45 CFR §164.404

| Requirement | Detail |
|-------------|--------|
| Timeline | Without unreasonable delay, no later than 60 calendar days from discovery |
| Method | First-class mail to last known address; email if individual has agreed to electronic notice |
| Content — Brief description of breach | What happened and date(s) of breach and discovery |
| Content — Types of information | Description of PHI types involved (not the actual PHI) |
| Content — Protective steps | Steps individual should take to protect from potential harm |
| Content — Entity's actions | Brief description of what the entity is doing to investigate, mitigate harm, and prevent recurrence |
| Content — Contact information | Toll-free number, email, website, or postal address for questions |
| Substitute notice (10+ individuals with insufficient contact info) | Conspicuous posting on entity's website for 90 days OR conspicuous notice in major print or broadcast media serving the area. Must include toll-free number active for 90 days. |
| Urgent notice | If there is possible imminent misuse, notice by telephone or other means in addition to written notice |

### HHS/OCR Notification — 45 CFR §164.408

| Breach Size | Reporting Method | Timeline |
|-------------|-----------------|----------|
| 500 or more individuals | HHS Breach Portal (ocrportal.hhs.gov) | Without unreasonable delay, no later than 60 days from discovery. HHS posts on the "Wall of Shame" (breach portal) |
| Fewer than 500 individuals | HHS Breach Portal — annual log | Within 60 days of the end of the calendar year in which the breach was discovered (by March 1 of the following year) |

### State Attorney General Notification — 45 CFR §164.412

| Requirement | Detail |
|-------------|--------|
| Threshold | Breaches involving residents of the state; most states require notification for 500+ affected residents |
| Timeline | Concurrent with or prior to individual notification |
| Content | Same as individual notification content |
| Method | Written notice to the attorney general of each state where affected individuals reside |

### Media Notification — 45 CFR §164.406

| Requirement | Detail |
|-------------|--------|
| Threshold | Breach affecting 500 or more individuals in a single state or jurisdiction |
| Timeline | Without unreasonable delay, no later than 60 days from discovery |
| Method | Prominent media outlets serving the state or jurisdiction (newspaper, TV, radio) |
| Content | Same as individual notification content |

## Breach Exceptions — 45 CFR §164.402(1)

Three exceptions to the definition of "breach" (not reportable even if unsecured PHI is involved):

### Exception 1: Unintentional Acquisition
Good-faith, unintentional acquisition, access, or use of PHI by a workforce member or person acting under the covered entity's authority, if made within the scope of authority and without further impermissible use or disclosure.

### Exception 2: Inadvertent Disclosure Within Organization
Inadvertent disclosure of PHI by a person authorized to access PHI at a covered entity or business associate to another person authorized to access PHI at the same entity, and the PHI is not further used or disclosed impermissibly.

### Exception 3: Good Faith Belief of No Retention
Disclosure of PHI where the covered entity or business associate has a good-faith belief that the unauthorized person would not reasonably have been able to retain the information.

## Business Associate Obligations — 45 CFR §164.410

1. Business associate must notify the covered entity of a breach without unreasonable delay, and no later than 60 days from discovery (or a shorter period specified in the BAA).
2. The notification must include: identification of each individual affected (if known), and any other available information the covered entity needs to provide individual notification.
3. The covered entity is ultimately responsible for providing all required notifications.

## Penalties for Non-Compliance

| Tier | Knowledge Level | Per Violation | Annual Cap |
|------|----------------|---------------|-----------|
| Tier 1 | Did not know and could not have known | $137 - $68,928 | $2,067,813 |
| Tier 2 | Reasonable cause, not willful neglect | $1,379 - $68,928 | $2,067,813 |
| Tier 3 | Willful neglect, corrected within 30 days | $13,785 - $68,928 | $2,067,813 |
| Tier 4 | Willful neglect, not corrected | $68,928 - $2,067,813 | $2,067,813 |

(Penalty amounts adjusted for inflation per Federal Register notice, effective 2025.)

## Integration with State Laws

HIPAA breach notification does not preempt state breach notification laws that provide greater protection or additional requirements. Covered entities must comply with both HIPAA and applicable state laws. In practice:
- HIPAA 60-day deadline is the outer limit; some states impose shorter deadlines.
- State content requirements may exceed HIPAA minimums.
- State AG notification may be required even for breaches under 500 individuals depending on state law.
