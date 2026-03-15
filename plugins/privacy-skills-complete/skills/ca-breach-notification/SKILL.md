---
name: ca-breach-notification
description: >-
  Executes breach notification under California Civil Code Section 1798.82
  (California data breach notification law). Covers data elements triggering
  notification, timing requirements (most expedient time possible), AG
  notification for 500+ California residents, specific content and format
  requirements, and substitute notice provisions. Keywords: California, breach
  notification, Cal. Civ. Code 1798.82, attorney general, CCPA, data elements.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-breach-response
  tags: "california, breach-notification, civil-code-1798-82, attorney-general, ccpa"
---

# Executing California Breach Notification

## Overview

California was the first US state to enact a data breach notification law (SB 1386, 2003). Cal. Civ. Code §1798.82 requires any person, business, or state agency that owns or licenses computerized data containing personal information to notify California residents when unencrypted personal information has been (or is reasonably believed to have been) acquired by an unauthorized person. The California Attorney General must be notified when more than 500 California residents are affected.

## Covered Data Elements — Cal. Civ. Code §1798.81.5(d)

A breach notification is triggered when an individual's first name or first initial and last name is combined with any of the following unencrypted or unredacted data elements:

| Data Element | Category |
|-------------|----------|
| Social Security number | Government identifier |
| Driver's license number or California identification card number | Government identifier |
| Financial account number, credit card number, or debit card number, in combination with any required security code, access code, or password | Financial |
| Medical information | Health |
| Health insurance information | Health |
| Unique biometric data (fingerprint, retina, iris image, or other unique physical representation or digital representation used for authentication) | Biometric |
| Information or data collected through automated license plate recognition systems | Surveillance |
| Genetic data | Genetic |
| A username or email address, in combination with a password or security question and answer that would permit access to an online account | Credentials |
| Tax identification number | Government identifier |

**Note**: "Personal information" does not include publicly available information that is lawfully made available to the general public from federal, state, or local government records.

## Notification Timing — "Most Expedient Time Possible"

Cal. Civ. Code §1798.82(a): Notification must be made "in the most expedient time possible and without unreasonable delay."

### What Constitutes "Unreasonable Delay"
- The statute does not define a specific number of days.
- California AG guidance interprets this as requiring notification as soon as the investigation has progressed sufficiently to determine that notification is required.
- Investigation and law enforcement coordination are recognized legitimate reasons for delay.
- Internal approval processes and desire to prepare PR responses are NOT legitimate reasons for delay.

### Law Enforcement Delay — §1798.82(c)
Notification may be delayed if a law enforcement agency determines that notification would impede a criminal investigation. The notification must be made "promptly" after the law enforcement agency determines notification will not compromise the investigation.

## AG Notification — §1798.82(f)

| Requirement | Detail |
|-------------|--------|
| Threshold | 500 or more California residents affected |
| Method | Electronic submission to the California AG's office (oag.ca.gov/privacy/databreach/reporting) |
| Content | Sample copy of the individual notification letter |
| Timing | Concurrent with or before individual notification |

## Individual Notification Content Requirements — §1798.82(d)

The notification must include:

1. **Name and contact information** of the notifying entity.
2. **List of the types of personal information** that were or are reasonably believed to have been the subject of the breach.
3. **Date of the breach** (if known) and the **date of the notice**.
4. **Whether notification was delayed** as a result of a law enforcement investigation (if applicable).
5. **General description of the breach** incident, if that information is possible to determine at the time of notice.
6. **Toll-free telephone numbers, addresses, and websites** for the major credit reporting agencies (if the breach involved a Social Security number, driver's license number, or California identification card number).
7. **Statement about availability of a security freeze** (if SSN is involved): information about the right to place a security freeze on credit files under Cal. Civ. Code §1785.11.2.

## Format Requirements — §1798.82(d)

California has specific formatting requirements for breach notification letters:

- **Title**: "Notice of Data Breach" — must be prominently displayed.
- **Headings**: Must use the following headings (or substantially similar):
  - "What Happened"
  - "What Information Was Involved"
  - "What We Are Doing"
  - "What You Can Do"
  - "For More Information"
- **Font**: 10-point type or larger.
- **Language**: Written in plain, easily understood language.

## Substitute Notice — §1798.82(j)

Substitute notice is permitted when:
- The cost of individual notice exceeds $250,000; OR
- The number of affected persons exceeds 500,000; OR
- The entity does not have sufficient contact information.

Substitute notice must include ALL of the following:
1. Email notice to affected persons for whom email addresses are available.
2. Conspicuous posting on the entity's website.
3. Notification to major statewide media.

## Encryption Safe Harbor

Encrypted personal information is excluded from the notification requirement IF:
- The encryption key has not been (and is not reasonably believed to have been) acquired by an unauthorized person.
- The data was encrypted using an algorithm that meets industry standards (AES-128 or higher).

## Interaction with CCPA/CPRA

The California Consumer Privacy Act (CCPA) as amended by CPRA provides a private right of action for data breaches under Cal. Civ. Code §1798.150:
- Applies when "nonencrypted and nonredacted personal information" is subject to unauthorized access and exfiltration, theft, or disclosure as a result of the business's failure to implement reasonable security.
- Statutory damages: $100 to $750 per consumer per incident, OR actual damages (whichever is greater).
- Must provide 30-day cure notice before filing suit.

## Key Enforcement Actions

- **Hanna Andersson (2020)**: $400,000 settlement for delayed notification of a Magecart web-skimming breach affecting California consumers. AG cited failure to notify "in the most expedient time possible."
- **DoorDash (2020)**: AG investigation into breach affecting 4.9 million individuals. AG scrutinized the adequacy and timeliness of notification.
- **T-Mobile (2022)**: $350 million class-action settlement (national) with significant California consumer component. AG office monitored compliance with California-specific notification requirements.

## Sample AG Submission Cover Letter

To: California Office of the Attorney General
Privacy Enforcement Section
oag.ca.gov/privacy/databreach/reporting

Re: Data Breach Notification — Stellar Payments Group
Breach Date: 13 March 2026
California Residents Affected: 2,340

Pursuant to Cal. Civ. Code §1798.82(f), Stellar Payments Group hereby provides notice of a data breach affecting 2,340 California residents. Enclosed is a sample copy of the notification letter being sent to affected individuals. Individual notifications will be dispatched on 28 March 2026.

Contact: Dr. Elena Vasquez, DPO, dpo@stellarpayments.eu, +1 (202) 555-0142.
