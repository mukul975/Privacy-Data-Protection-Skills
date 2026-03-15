---
name: hipaa-breach-notify
description: >-
  Implements HIPAA breach notification requirements under 45 CFR §164.400-414.
  Covers individual notification within 60 days, HHS reporting thresholds
  (500+ immediate, under 500 annual), state attorney general notification,
  media notification for 500+ in a state, and breach risk assessment.
  Keywords: HIPAA breach notification, HHS reporting, OCR breach portal,
  individual notice, state attorney general.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: healthcare-privacy
  tags: "hipaa, breach-notification, hhs-reporting, ocr-breach-portal, individual-notice, state-ag"
---

# HIPAA Breach Notification Rule — 45 CFR §164.400-414

## Overview

The HIPAA Breach Notification Rule, added by the HITECH Act of 2009 and finalized in the Omnibus Rule of 2013 (78 FR 5566), requires covered entities and business associates to provide notification following a breach of unsecured protected health information (PHI). The rule establishes specific timeframes, content requirements, and reporting obligations that vary based on the number of individuals affected. Post-2013, the rule applies a presumption that any impermissible acquisition, access, use, or disclosure of PHI is a breach unless the covered entity demonstrates through a risk assessment that there is a low probability the PHI was compromised.

## Definition of Breach — §164.402

### What Constitutes a Breach

A breach is the acquisition, access, use, or disclosure of PHI in a manner not permitted under the Privacy Rule that compromises the security or privacy of the PHI.

### Presumption of Breach

Under the 2013 Omnibus Rule, an impermissible use or disclosure of PHI is presumed to be a breach unless the covered entity or business associate demonstrates through a four-factor risk assessment that there is a low probability that the PHI has been compromised.

### Four-Factor Risk Assessment — §164.402(2)

| Factor | Assessment Questions |
|--------|---------------------|
| **1. Nature and extent of PHI involved** | What types of identifiers and clinical information were involved? Does the PHI include sensitive data (SSN, financial, substance abuse, mental health, HIV)? How many data elements were exposed? |
| **2. Unauthorized person who used or received the PHI** | Who impermissibly accessed the PHI? Was it an unauthorized employee, an external attacker, an unintended recipient? Does the person have obligations to protect PHI (e.g., another covered entity)? |
| **3. Whether the PHI was actually acquired or viewed** | Was the PHI actually accessed or viewed, or was there only an opportunity for access? Are there forensic logs demonstrating whether data was exfiltrated? Was an encrypted laptop stolen but the encryption verified as NIST-compliant? |
| **4. Extent to which the risk has been mitigated** | Were satisfactory assurances obtained from the recipient that the PHI will not be further used or disclosed? Was the PHI recovered? Was the recipient a covered entity that has agreed to destroy the information? |

If the risk assessment demonstrates low probability of compromise across all four factors, the incident is not a breach and notification is not required. The assessment must be documented regardless of the conclusion.

### Exceptions to the Breach Definition — §164.402(1)

Three circumstances are excluded from the definition of breach:

1. **Unintentional good-faith acquisition**: PHI acquired unintentionally by a workforce member or person acting under the authority of the covered entity or BA, made in good faith and within the scope of authority, and the PHI is not further used or disclosed impermissibly
2. **Inadvertent disclosure between authorized persons**: PHI inadvertently disclosed by a person authorized to access PHI to another person authorized to access PHI at the same covered entity, BA, or organized healthcare arrangement, and the information is not further used or disclosed impermissibly
3. **Good-faith belief of non-retention**: The covered entity or BA has a good-faith belief that the unauthorized person to whom the disclosure was made would not reasonably have been able to retain the information

## Unsecured PHI — §164.402

Breach notification obligations apply only to "unsecured PHI" — PHI that has not been rendered unusable, unreadable, or indecipherable to unauthorized individuals through one of the technologies specified by HHS:

### Safe Harbor Technologies (HHS Guidance, 74 FR 19006)

| Technology | Specification |
|-----------|--------------|
| **Encryption** | NIST-validated encryption processes consistent with NIST Special Publication 800-111 (data at rest) and FIPS 140-2/140-3 validated modules. AES-128 or AES-256 for data at rest; TLS 1.2+ for data in transit |
| **Destruction** | Paper: shredding or destruction such that PHI cannot be read or reconstructed. Electronic media: clearing, purging, or destroying consistent with NIST SP 800-88 Rev. 1 |

If PHI was properly encrypted and the encryption key was not compromised, or if PHI was properly destroyed, then it is "secured" and the breach notification provisions do not apply.

## Notification Requirements

### Individual Notification — §164.404

**Who must notify**: The covered entity (not the business associate directly, unless delegated by the BA agreement).

**Timeframe**: Without unreasonable delay, and no later than 60 calendar days from the date of discovery of the breach. Discovery occurs on the first day the breach is known or, by exercising reasonable diligence, would have been known. Knowledge of a workforce member or agent is imputed to the covered entity.

**Method**: Written notice by first-class mail to the individual's last known address (or next of kin if deceased). Email is permitted if the individual has agreed to electronic notice. If contact information is insufficient or out of date for 10 or more individuals, a conspicuous posting on the covered entity's website for 90 days or a notice in major print or broadcast media is required.

**Content requirements (§164.404(c))**:

1. A brief description of what happened, including the date of the breach and the date of discovery
2. A description of the types of unsecured PHI involved (e.g., name, SSN, date of birth, diagnosis, treatment information — do not include the actual PHI)
3. Steps individuals should take to protect themselves from potential harm
4. A brief description of what the covered entity is doing to investigate, mitigate harm, and prevent future breaches
5. Contact procedures including a toll-free telephone number, email address, postal address, or website

**Asclepius Health Network Individual Notice Template**:

Asclepius Health Network maintains pre-approved breach notification letter templates reviewed by legal counsel, with variable fields for breach-specific details. The template includes:
- Description of the incident
- Types of information involved
- Steps Asclepius has taken (investigation, remediation, enhanced safeguards)
- Offer of complimentary credit monitoring and identity theft protection services (24 months for breaches involving SSN or financial data)
- Toll-free call center number staffed by trained representatives
- Instructions for placing fraud alerts and security freezes
- Contact information for the Asclepius Privacy Office, HHS OCR, and relevant state attorney general

### HHS Secretary Notification — §164.408

| Breach Size | Reporting Requirement | Timeframe | Method |
|------------|----------------------|-----------|--------|
| 500+ individuals | Individual report to HHS | Without unreasonable delay, no later than 60 days from discovery (concurrent with individual notification) | HHS breach reporting portal (ocrportal.hhs.gov) |
| Fewer than 500 individuals | Log and report annually | Within 60 days of end of calendar year in which breach was discovered | HHS breach reporting portal — annual breach log submission |

Breaches affecting 500 or more individuals are posted on the HHS "Wall of Shame" — the public breach reporting portal at ocrportal.hhs.gov/ocr/breach/breach_report.jsf.

**HHS Portal Required Fields**:
- Covered entity name, address, contact information
- Covered entity type (health plan, healthcare provider, healthcare clearinghouse, BA acting as agent)
- Number of individuals affected
- Date of breach, date of discovery
- Type of breach (hacking/IT incident, unauthorized access/disclosure, theft, loss, improper disposal, other)
- Location of breached information (email, electronic medical record, network server, paper/films, laptop, desktop, portable device, other)
- Type of PHI involved
- Description of breach
- Safeguards in place at time of breach
- Actions taken in response

### State Attorney General Notification — §13402(e)(3) HITECH

For breaches affecting 500 or more residents of a state or jurisdiction, the covered entity must notify the state attorney general concurrent with individual notification.

**Asclepius Health Network operates across 4 states**. If a breach affects 500+ residents of any single state, the AG of that state must be notified. Many states have their own breach notification laws with additional requirements; Asclepius tracks requirements across all 50 states and files notifications as required.

### Media Notification — §164.406

For breaches affecting 500 or more residents of a state or jurisdiction, the covered entity must provide notice to prominent media outlets serving the state or jurisdiction without unreasonable delay and no later than 60 days from discovery. This is typically accomplished through a press release distributed to major media outlets in the affected area.

## Business Associate Breach Obligations — §164.410

Business associates must:

1. **Notify the covered entity** of a breach without unreasonable delay and no later than 60 days from discovery (or shorter if specified in the BAA)
2. **Identify affected individuals** to the extent possible
3. **Provide information** the covered entity needs to fulfill its notification obligations

The covered entity retains responsibility for individual, HHS, state AG, and media notification unless the BAA delegates notification to the BA. Asclepius Health Network BAAs require BA breach notification within 5 business days of discovery and require the BA to bear notification costs when the breach results from the BA's acts or omissions.

## Breach Response Timeline — Asclepius Health Network

| Day | Action | Responsible Party |
|-----|--------|------------------|
| Day 0 | Incident detected or reported | Workforce member, IT security, BA |
| Day 0-1 | Incident response team activated; containment initiated | CISO, Incident Response Team |
| Day 1-7 | Forensic investigation; scope and nature of PHI determined | Forensic investigators (internal or third-party) |
| Day 7-14 | Four-factor risk assessment completed; breach determination made | Privacy Officer, Legal Counsel |
| Day 14-21 | If breach confirmed: notification letters drafted, reviewed by legal, call center prepared | Privacy Office, Legal, Communications |
| Day 21-30 | Notification letters mailed; HHS portal submission prepared | Privacy Office, Compliance |
| Day 30-45 | HHS notified; state AG notified (if 500+ in a state); media notified (if 500+ in a state) | Compliance, Legal |
| Day 45-60 | Substitute notice posted if needed; call center operational; credit monitoring enrollment tracked | Privacy Office, Vendor Management |
| Within 60 days | All individual notifications completed (hard deadline) | Privacy Office |
| Ongoing | Remediation measures implemented; risk analysis updated; workforce re-trained | CISO, Privacy Office, Training |

## Documentation Requirements — §164.414(b)

Covered entities must maintain documentation of breach risk assessments, notifications, and related actions for a minimum of 6 years from the date of creation or the date when the document was last in effect, whichever is later. This includes:

- Breach risk assessment and determination
- Individual notification copies and mailing records
- HHS notification records
- State AG notification records
- Media notification records
- Remediation documentation
- Workforce sanctions applied

## Enforcement Actions for Breach Notification Failures

- **Presence Health (2017)**: $475,000 — delayed breach notification by over 100 days beyond the 60-day deadline for breach affecting 836 individuals
- **Cottage Health (2019)**: $3 million — failure to conduct thorough risk assessment prior to breach; inadequate security measures contributing to breach of 62,500 records
- **Lafourche Medical Group (2023)**: $480,000 — phishing breach affecting approximately 34,862 individuals; failure to conduct risk analysis and implement security measures; late breach notification

## Integration Points

- **hipaa-privacy-rule**: Breach is defined as impermissible use/disclosure under the Privacy Rule
- **hipaa-security-rule**: Security safeguards determine whether PHI is "unsecured" for notification purposes
- **hipaa-risk-analysis**: Post-breach risk analysis update required; breach risk assessment is related but distinct from Security Rule risk analysis
- **hipaa-baa-management**: BAA breach notification provisions define BA obligations
- **hitech-act-privacy**: HITECH established the breach notification requirement and penalty tiers
