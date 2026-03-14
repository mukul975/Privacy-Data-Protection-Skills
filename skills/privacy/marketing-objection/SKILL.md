---
name: marketing-objection
description: >-
  Manages the absolute right to object to direct marketing under GDPR Article 21(2)-(3),
  covering immediate cessation of all direct marketing processing, suppression
  list management, cross-channel enforcement, and profiling for marketing purposes.
  Activate for marketing opt-out, unsubscribe, Art. 21(2), direct marketing objection queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-subject-rights
  tags: "direct-marketing-objection, gdpr-article-21, suppression-list, marketing-opt-out, unsubscribe"
---

# Managing Direct Marketing Objection

## Overview

The right to object to direct marketing under GDPR Article 21(2)-(3) is an **absolute right** — there is no balancing test, no compelling grounds exception, and no basis on which the controller can refuse. When a data subject objects to processing for direct marketing purposes, the controller must cease that processing immediately. This skill provides the complete operational procedure for handling marketing objections across all channels.

## Legal Foundation

### GDPR Article 21(2)-(3) — Direct Marketing Objection

1. **Art. 21(2)** — Where personal data are processed for direct marketing purposes, the data subject has the right to object at any time to processing of personal data concerning them for such marketing, which includes profiling to the extent that it is related to such direct marketing.

2. **Art. 21(3)** — Where the data subject objects to processing for direct marketing purposes, the personal data shall no longer be processed for such purposes.

### Key Characteristics

- **Absolute right**: No balancing test. No compelling grounds exception. No fee. No refusal possible.
- **Immediate effect**: Processing for direct marketing must cease as soon as the objection is received.
- **Scope**: Covers ALL forms of direct marketing including email, SMS, telephone, postal mail, targeted online advertising, and profiling for marketing segmentation.
- **Includes profiling**: Any profiling conducted for the purpose of direct marketing must also cease.

### Privacy and Electronic Communications Regulations 2003 (PECR)

- **Regulation 22** — Unsolicited communications by electronic mail: requires prior consent for marketing emails to individuals (unless soft opt-in exception applies).
- **Regulation 21** — Unsolicited calls for direct marketing: requires compliance with the Telephone Preference Service (TPS).

### ePrivacy Directive 2002/58/EC (as amended by 2009/136/EC)

- **Article 13** — Unsolicited communications: consent required for electronic marketing communications, with limited exception for existing customer relationships.

## Direct Marketing Objection Workflow

### Step 1: Receive the Objection

Objections may arrive through any channel:

| Channel | Example | Handling |
|---------|---------|----------|
| Email unsubscribe link | Click on "Unsubscribe" in marketing email | Automated processing within 24 hours |
| Reply to marketing email | "Please stop emailing me" | Manual triage, process within 24 hours |
| Web form | Privacy preference centre opt-out | Automated processing immediately |
| Telephone | "Take me off your mailing list" | Agent records objection, process within 24 hours |
| Written letter | "I object to you using my data for marketing" | Process within 48 hours of receipt |
| Social media message | Direct message requesting marketing cessation | Process within 48 hours of receipt |
| Verbal (in-person) | "Stop sending me marketing" | Staff member records objection, process within 24 hours |

1. Log with reference MKT-YYYY-NNNN.
2. Record the channel, timestamp, and scope of the objection.
3. No identity verification is required beyond confirming the identity matches the marketing recipient (e.g., the email address matches the unsubscribe request).

### Step 2: Determine the Scope

1. **Full opt-out**: Data subject objects to ALL direct marketing — cease all marketing processing.
2. **Partial opt-out**: Data subject objects to specific channels only (e.g., "stop calling me but email is fine") — cease the specified channels.
3. **If unclear**: Treat as a full opt-out. Contact the data subject to clarify preferences only after cessation.

### Step 3: Immediate Cessation

Within **24 hours** of receiving the objection:

1. **Email marketing**: Remove from all active email marketing lists, suppress email address.
2. **SMS marketing**: Remove from SMS distribution lists, suppress mobile number.
3. **Telephone marketing**: Add to internal do-not-call list, register with Telephone Preference Service (TPS) if applicable.
4. **Postal marketing**: Remove from postal mailing lists, add to internal do-not-mail list.
5. **Online targeted advertising**: Remove from remarketing audiences, customer match lists, and lookalike audience seed lists.
6. **Profiling for marketing**: Cease all profiling activities related to marketing segmentation for this individual. Remove from marketing segments.

### Step 4: Suppression List Management

A suppression list is essential to prevent re-subscription or re-targeting:

1. Add the data subject's identifiers to the marketing suppression list:
   - Email address (store as SHA-256 hash for matching against future lists)
   - Phone number (store as SHA-256 hash)
   - Postal address (store normalised address components)
   - Customer ID
2. The suppression list entry must be retained **indefinitely** (or until the data subject explicitly consents to marketing again) to prevent re-contact.
3. The suppression list must be checked before every marketing campaign distribution:
   - Email campaigns: check suppression list before send
   - SMS campaigns: check suppression list before send
   - Postal campaigns: check suppression list before print/dispatch
   - Online advertising: exclude suppression list from audience uploads
4. New data imports must be screened against the suppression list before any marketing processing.

### Step 5: Cross-Channel Enforcement

Ensure the objection is enforced across ALL marketing channels and systems:

| System | Action | Owner |
|--------|--------|-------|
| Email platform (Mailchimp) | Unsubscribe + add to suppression segment | Marketing Operations |
| SMS platform | Opt-out + add to suppression list | Marketing Operations |
| CRM (Salesforce) | Set marketing_opt_out = TRUE, update consent record | CRM Administrator |
| Advertising platforms (Google Ads, Meta Ads) | Remove from customer match and remarketing audiences | Digital Marketing |
| Analytics platform | Exclude from marketing attribution and segment analysis | Data Analytics |
| Data warehouse | Update marketing consent flag, trigger downstream sync | Data Engineering |
| Third-party data brokers | Issue suppression notification | Data Partnerships |

### Step 6: Third-Party Notification

1. Identify all third parties who process the data subject's data for direct marketing purposes on behalf of Meridian Analytics Ltd (e.g., marketing agencies, advertising platforms, data enrichment providers).
2. Send suppression instructions to each third party within 48 hours.
3. Request confirmation of suppression within 14 calendar days.
4. Log all notifications and confirmations.

### Step 7: Confirm to the Data Subject

Send confirmation within **14 calendar days** (best practice, well within the 30-day Art. 12 deadline):

1. Confirm that all direct marketing processing has ceased.
2. Specify the channels suppressed.
3. Confirm that a suppression record has been created.
4. If any non-marketing processing continues under a different legal basis, inform the data subject.
5. Provide contact details for further enquiries.

### Step 8: Ongoing Compliance

1. **Pre-campaign check**: Before every marketing campaign, the suppression list must be applied.
2. **New data imports**: All new customer data must be screened against the suppression list before any marketing processing.
3. **Quarterly audit**: Review suppression list completeness and effectiveness. Test that suppressed individuals do not receive marketing communications.
4. **Staff training**: All marketing team members must be trained on the absolute nature of the Art. 21(2) right and the suppression list process.
