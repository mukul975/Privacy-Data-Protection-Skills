---
name: executing-gdpr-72-hour-breach-notification
description: >-
  Executes the GDPR Article 33 mandatory breach notification to the supervisory
  authority within 72 hours of becoming aware of a personal data breach.
  Covers required notification content, deadline calculation, risk assessment
  for notification threshold, and DPO involvement. Keywords: GDPR, Article 33,
  breach notification, 72 hours, supervisory authority, DPO, EDPB.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-breach-response
  tags: "gdpr, article-33, breach-notification, 72-hour, supervisory-authority, dpo"
---

# Executing GDPR 72-Hour Breach Notification

## Overview

Article 33 of the GDPR requires controllers to notify the competent supervisory authority of a personal data breach without undue delay and, where feasible, not later than 72 hours after becoming aware of it. This skill provides the complete operational workflow from breach discovery through supervisory authority notification, including deadline calculation that accounts for weekends and public holidays, mandatory notification content, and the decision framework for determining whether notification is required.

## Notification Trigger — "Becoming Aware"

The 72-hour clock starts when the controller has a reasonable degree of certainty that a security incident has occurred that has led to personal data being compromised. Per EDPB Guidelines 9/2022, Section 2.3:

- A processor must notify the controller "without undue delay" after becoming aware — the controller's 72-hour window then begins upon the controller's receipt of that notification.
- An initial suspicion of a breach (e.g., an anomalous log entry) does not start the clock. A brief investigation period is permitted to establish whether a breach has actually occurred.
- Once the controller's IT security team confirms data compromise, the controller is deemed "aware" regardless of whether the DPO or senior management has been informed.

## Decision Tree: Is Notification Required?

A controller must notify the supervisory authority unless the breach is "unlikely to result in a risk to the rights and freedoms of natural persons" (Art. 33(1)).

### Step 1: Classify the Breach Type

| Type | Description | Example |
|------|-------------|---------|
| Confidentiality breach | Unauthorized or accidental disclosure of, or access to, personal data | Database exposed via misconfigured firewall revealing 12,000 customer records |
| Integrity breach | Unauthorized or accidental alteration of personal data | Malware modifying patient medication dosage records in clinical database |
| Availability breach | Accidental or unauthorized loss of access to, or destruction of, personal data | Ransomware encrypting the HR payroll system containing 3,400 employee records |

### Step 2: Assess Likelihood of Risk

Evaluate each factor on a scale of 1 (low) to 4 (severe):

| Factor | Assessment Question |
|--------|-------------------|
| Data sensitivity | Does the breach involve special categories (Art. 9), financial data, or government identifiers? |
| Volume | How many data subjects are affected? Under 100 / 100-1,000 / 1,000-100,000 / Over 100,000? |
| Identifiability | Can the breached data be used to directly identify individuals without significant effort? |
| Consequences | What concrete harm could result? Financial loss, discrimination, identity theft, reputational damage? |
| Vulnerable subjects | Are minors, patients, employees, or other vulnerable categories involved? |
| Controller-specific factors | Does the controller's role amplify risk (e.g., healthcare provider, financial institution)? |

### Step 3: Apply the Threshold

- **Aggregate score 6 or below**: Breach unlikely to result in risk — notification not required under Art. 33(1), but must be documented in the breach register per Art. 33(5).
- **Aggregate score 7-15**: Breach likely to result in risk — supervisory authority notification required within 72 hours.
- **Aggregate score 16 or above**: Breach likely to result in high risk — supervisory authority notification required within 72 hours AND data subject notification required under Art. 34.

## Required Notification Content — Art. 33(3)

The notification to the supervisory authority must contain, at minimum:

### (a) Nature of the Breach

- Description of the nature of the personal data breach.
- Categories of data subjects concerned (e.g., customers, employees, patients).
- Approximate number of data subjects concerned.
- Categories of personal data records concerned (e.g., names, email addresses, financial account numbers).
- Approximate number of personal data records concerned.

### (b) DPO Contact Details

- Name of the Data Protection Officer: Dr. Elena Vasquez
- Email: dpo@stellarpayments.eu
- Direct phone: +49 30 7742 8001
- Postal address: Stellar Payments Group, Friedrichstraße 191, 10117 Berlin, Germany

### (c) Likely Consequences

- Detailed description of the likely consequences of the breach, categorized by:
  - Physical harm (if applicable)
  - Material harm (financial loss, fraud risk)
  - Non-material harm (distress, discrimination, reputational damage)
  - Loss of control over personal data
  - Limitation of rights

### (d) Measures Taken or Proposed

- Immediate containment measures already implemented
- Measures to mitigate adverse effects on data subjects
- Planned longer-term remediation actions
- Whether data subjects have been or will be notified under Art. 34

## Phased Notification

Art. 33(4) permits information to be provided in phases where it is not possible to provide all details simultaneously. The initial notification must:

1. State that additional information will follow.
2. Provide reasons for the delay in furnishing complete information.
3. Include whatever information is available at the time of initial notification.
4. Be supplemented with additional details as they become available, without undue further delay.

## Notification Channels by Supervisory Authority

| Authority | Jurisdiction | Notification Method |
|-----------|-------------|-------------------|
| BfDI | Germany (federal) | Online portal at bfdi.bund.de — electronic form submission |
| CNIL | France | Online notification via notifications.cnil.fr/notifications |
| ICO | United Kingdom | Online form at ico.org.uk/for-organisations/report-a-breach |
| DPC | Ireland | Online breach notification form via forms.dataprotection.ie |
| AEPD | Spain | Electronic submission via sedeagpd.gob.es |
| Garante | Italy | PEC (certified email) to protocollo@pec.gpdp.it |
| AP | Netherlands | Online form at autoriteitpersoonsgegevens.nl/meldplicht-datalekken |

## 72-Hour Deadline Calculation Rules

1. The 72-hour period is calculated in continuous hours, including weekends and public holidays.
2. If the breach is discovered at 14:30 CET on a Friday, the deadline is 14:30 CET on the following Monday.
3. Art. 33(1) uses the phrase "where feasible" — if notification exceeds 72 hours, the controller must provide reasons for the delay alongside the notification.
4. The EDPB has confirmed that the 72-hour period runs from the moment the controller "becomes aware," not from the moment of the breach itself.

## Late Notification — Justifying Delay

When notification exceeds 72 hours, Art. 33(1) requires the controller to accompany the notification with reasons for the delay. Acceptable justifications per EDPB guidance include:

- Complex forensic investigation needed to determine scope and affected data categories
- Large-scale breach requiring coordination with law enforcement before notification
- Discovery during a period where key personnel were unavailable and no adequate delegation was in place (though this itself may be a compliance gap)

Unacceptable justifications:

- Internal approval processes delayed sign-off
- The DPO was on annual leave and no deputy was appointed
- The organization wanted to complete its own public communications before notifying the authority

## Post-Notification Obligations

1. **Supplementary information**: Provide any outstanding details from the initial notification as they become available.
2. **Breach register update**: Record the full details of the breach, its effects, and remedial actions in the Art. 33(5) register.
3. **Data subject notification assessment**: Determine whether Art. 34 notification to individuals is also required.
4. **Supervisory authority engagement**: Respond promptly to any follow-up inquiries from the authority.
5. **Remediation evidence**: Document all corrective measures implemented and provide evidence to the authority if requested.
