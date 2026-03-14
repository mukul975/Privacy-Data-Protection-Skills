---
name: maintaining-breach-documentation-records
description: >-
  Maintains the GDPR Article 33(5) breach register documenting all personal data
  breaches regardless of whether supervisory authority notification was required.
  Covers mandatory register fields including facts, effects, and remedial actions,
  retention periods, audit readiness, and integration with the accountability
  framework. Keywords: breach register, Article 33(5), breach documentation,
  accountability, audit readiness, remedial actions.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-breach-response
  tags: "breach-register, article-33-5, documentation, accountability, audit, remedial-actions"
---

# Maintaining Breach Documentation Records

## Overview

Article 33(5) of the GDPR requires every controller to document all personal data breaches, regardless of whether the breach triggered supervisory authority notification. The documentation must include "the facts relating to the personal data breach, its effects and the remedial action taken" and must "enable the supervisory authority to verify compliance with this Article." This creates a comprehensive breach register that serves as a primary accountability document under Art. 5(2).

## Mandatory Documentation Requirements — Art. 33(5)

### Facts Relating to the Breach

Every breach register entry must document:

| Field | Description | Example |
|-------|-------------|---------|
| Breach reference number | Unique sequential identifier | SPG-BREACH-2026-003 |
| Discovery date and time | UTC timestamp when controller became aware | 13 March 2026, 14:30 UTC |
| Breach date and time | UTC timestamp of the breach itself (if different from discovery) | 13 March 2026, 11:15 UTC |
| Breach type | Confidentiality, integrity, availability, or combined | Availability (primary), Confidentiality (under investigation) |
| Breach description | Factual narrative of what occurred | LockBit 3.0 ransomware encrypted production customer database cluster. Attack vector: compromised service account obtained via spear-phishing. |
| Affected systems | Systems involved in the breach | db-prod-eu-west-01 through db-prod-eu-west-04 |
| Data subject categories | Types of individuals affected | Individual account holders, business account holders, joint account holders |
| Data subject count | Approximate number of affected individuals | 15,230 |
| Personal data categories | Types of data compromised | Names, postal addresses, emails, payment card last-4, transaction histories, account balances |
| Record count | Approximate number of affected records | 48,720 |
| Root cause | Identified cause of the breach | Stale privileged service account + phishing + push-fatigue MFA bypass |
| Containment timestamp | When the breach was contained | 13 March 2026, 12:45 UTC |

### Effects of the Breach

| Field | Description | Example |
|-------|-------------|---------|
| Risk assessment score | Aggregate score from the risk assessment methodology | 18/24 |
| Risk level | Resulting risk determination | Approaching high risk |
| Actual harm identified | Any confirmed harm to data subjects | No confirmed harm as of assessment date |
| Potential harm | Likely consequences if data is misused | Financial fraud, identity theft, targeted phishing |
| Duration of impact | How long data subjects were affected | 36 hours (database unavailability); ongoing (potential confidentiality impact) |

### Remedial Actions Taken

| Field | Description | Example |
|-------|-------------|---------|
| Containment measures | Immediate actions to stop the breach | Network isolation, credential revocation, backup restoration |
| Remediation measures | Longer-term corrective actions | MFA upgrade to FIDO2, service account lifecycle management, network segmentation |
| Remediation status | Current status of each action | 4 of 7 measures completed; 3 in progress |
| Remediation deadline | Target completion date | 15 June 2026 |

## Notification Decision Documentation

Every breach entry must also record the notification decision and rationale:

| Field | Description |
|-------|-------------|
| Art. 33 SA notification decision | Required / Not required |
| Art. 33 notification rationale | Why notification was or was not required (reference risk assessment) |
| Art. 33 notification date | Date and time of SA notification (if applicable) |
| SA reference number | Reference number assigned by the supervisory authority |
| SA follow-up status | Any follow-up inquiries or actions from the authority |
| Art. 34 DS notification decision | Required / Not required / Exempt under Art. 34(3) |
| Art. 34 notification rationale | Why DS notification was or was not required |
| Art. 34 notification date | Date of DS communication (if applicable) |
| Art. 34 notification method | Channels used (email, postal, public communication) |

## Register Structure and Maintenance

### Single Centralized Register

All breaches must be recorded in a single centralized register maintained by the DPO's office. Stellar Payments Group uses a dedicated module in the OneTrust Privacy Management Platform with the following access controls:

- **Write access**: DPO, Deputy DPO, Privacy Incident Coordinator
- **Read access**: CISO, General Counsel, Internal Audit, Board Audit Committee
- **No access**: Business unit managers, IT operations staff (access to individual breach records provided on a need-to-know basis via separate reports)

### All Breaches Documented — Including Non-Notifiable

The register must include every personal data breach, regardless of severity or whether SA/DS notification was triggered. This explicitly includes:

- Misdirected emails containing personal data (even single-recipient incidents)
- Temporary availability breaches resolved from backup
- Unsuccessful exfiltration attempts where personal data was targeted but not accessed
- Breaches at processors that affected the controller's data
- Physical breaches (lost devices, unauthorized office access)

### Retention Period

Breach register entries are retained for a minimum of 7 years from the date of breach closure. This accounts for:
- The 5-year statute of limitations for GDPR enforcement actions in most EU member states
- The need to demonstrate patterns (or absence of patterns) to supervisory authorities
- Litigation time limits for data subject compensation claims under Art. 82

After the 7-year retention period, entries are anonymized (data subject counts retained, specific identifiers removed) and maintained indefinitely for trend analysis.

## Audit Readiness

### Supervisory Authority Access — Art. 33(5)

The breach register must be available to the supervisory authority "on request." Audit readiness requires:

1. **Instant availability**: The register must be exportable in a structured format (CSV, JSON, PDF) within 24 hours of a supervisory authority request.
2. **Completeness verification**: Monthly self-audit to verify all reported security incidents were assessed for personal data impact and, where applicable, added to the register.
3. **Cross-reference integrity**: Each register entry must link to supporting documentation (risk assessment form, SA notification copy, DS notification copy, investigation report, remediation evidence).
4. **Trend reporting**: The register must support generation of trend reports showing: breach frequency over time, breach types, root cause categories, notification rates, and remediation completion rates.

### Annual Breach Register Review

The DPO conducts an annual review of the breach register covering:

1. **Completeness**: Are all known breaches documented? Cross-reference against the security incident management system.
2. **Accuracy**: Sample 20% of entries and verify accuracy against source documentation.
3. **Timeliness**: Were entries created within 72 hours of breach discovery?
4. **Remediation closure**: Are remediation actions tracked to completion? Flag overdue actions.
5. **Pattern identification**: Are there recurring breach types or root causes indicating systemic issues?
6. **Board reporting**: Prepare an annual breach summary report for the Board Audit Committee.

## Integration with Other Records

| Related Record | Integration Point |
|---------------|-------------------|
| Art. 30 RoPA | Link affected processing activities to the breach entry |
| DPIA Register | Update DPIAs for affected processing activities with breach as risk event |
| Vendor Register | Update processor risk assessment if breach originated at a processor |
| Training Records | Document post-breach training delivered to relevant personnel |
| Audit Log | Reference internal audit findings related to the breach |
| Insurance Records | Link to cyber insurance claim reference (if applicable) |

## Common Documentation Deficiencies

1. **Breaches documented in security incident systems but not in the Art. 33(5) register**: The security incident ticket is not a substitute for the breach register entry.
2. **Missing notification decision rationale**: Recording "not notified" without documenting why the breach was assessed as unlikely to result in risk.
3. **Incomplete remediation tracking**: Remedial actions listed but never updated to reflect completion status.
4. **Delayed documentation**: Entries created weeks after the breach, making it difficult to demonstrate timely awareness and response.
5. **No processor breach entries**: Breaches that occur at processors but affect the controller's data are not recorded in the controller's register.
