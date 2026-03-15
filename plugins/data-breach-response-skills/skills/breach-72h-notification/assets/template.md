# Art. 33 Supervisory Authority Breach Notification Template

## Section 1: Controller Information

| Field | Details |
|-------|---------|
| Controller Name | Stellar Payments Group GmbH |
| Registration Number | HRB 182734 B (Amtsgericht Charlottenburg) |
| Registered Address | Friedrichstraße 191, 10117 Berlin, Germany |
| DPO Name | Dr. Elena Vasquez |
| DPO Email | dpo@stellarpayments.eu |
| DPO Phone | +49 30 7742 8001 |
| EU Representative (if applicable) | N/A — established in the EU |
| Notification Reference | SPG-BREACH-2026-003 |
| Date of Notification | 15 March 2026 |

## Section 2: Nature of the Breach — Art. 33(3)(a)

### 2.1 Breach Description

On 13 March 2026 at approximately 11:15 UTC, Stellar Payments Group detected anomalous encryption activity on the production customer database cluster (db-prod-eu-west-01 through db-prod-eu-west-04). Investigation confirmed a ransomware attack (LockBit 3.0 variant) that encrypted 48,720 customer records across three account holder categories. The attack vector was a compromised service account credential obtained through a spear-phishing email targeting an IT operations engineer on 10 March 2026. The encryption rendered all affected records unavailable. Forensic analysis by Mandiant (engaged under retainer SPG-IR-2025-007) is ongoing to determine whether data exfiltration occurred.

### 2.2 Breach Classification

| Attribute | Value |
|-----------|-------|
| Breach Type | Availability (primary), Confidentiality (under investigation) |
| Discovery Timestamp | 13 March 2026, 14:30 UTC |
| Breach Start (estimated) | 13 March 2026, 11:15 UTC |
| Breach Contained | 13 March 2026, 12:45 UTC (network isolation) |
| Ongoing | Forensic investigation ongoing; data availability restored from backup |

### 2.3 Categories and Numbers of Data Subjects

| Category | Approximate Count |
|----------|------------------|
| Individual account holders | 11,420 |
| Business account holders | 2,890 |
| Joint account holders | 920 |
| **Total** | **15,230** |

### 2.4 Categories and Numbers of Personal Data Records

| Data Category | Approximate Records |
|--------------|-------------------|
| Full names | 15,230 |
| Postal addresses | 15,230 |
| Email addresses | 14,870 |
| Payment card numbers (last 4 digits only) | 12,650 |
| Transaction histories (last 24 months) | 48,720 |
| Account balances | 15,230 |

**Total approximate personal data records affected: 48,720**

## Section 3: DPO Contact Details — Art. 33(3)(b)

| Field | Details |
|-------|---------|
| Name | Dr. Elena Vasquez |
| Title | Data Protection Officer |
| Email | dpo@stellarpayments.eu |
| Phone | +49 30 7742 8001 |
| Address | Stellar Payments Group GmbH, Friedrichstraße 191, 10117 Berlin, Germany |

## Section 4: Likely Consequences — Art. 33(3)(c)

### 4.1 Assessment of Likely Consequences

Based on the risk assessment conducted using the EDPB Guidelines 9/2022 methodology:

**Material harm:**
- Temporary inability to access account information and transaction history during the restoration period (estimated 48 hours from discovery).
- If exfiltration is confirmed, risk of financial fraud using partial payment card data combined with identity information.
- Potential for targeted phishing attacks using the combination of names, email addresses, and account relationship details.

**Non-material harm:**
- Distress and anxiety for affected account holders regarding the security of their financial data.
- Loss of trust and confidence in Stellar Payments Group's data protection capabilities.
- Potential reputational harm to business account holders if their use of payment services becomes known to competitors.

**Risk Level Determination:**
- Risk assessment aggregate score: 18/24 (High Risk).
- Supervisory authority notification: Required under Art. 33(1).
- Data subject notification: Required under Art. 34(1) due to high risk determination.

### 4.2 Vulnerable Data Subjects

No minors or specially vulnerable individuals have been identified among the affected data subjects. The affected population consists of adult individual and business account holders.

## Section 5: Measures Taken or Proposed — Art. 33(3)(d)

### 5.1 Immediate Containment Measures (Completed)

1. Isolated affected database cluster from the production network at 12:45 UTC on 13 March 2026.
2. Revoked all service account credentials associated with the compromised account within 30 minutes of breach confirmation.
3. Activated backup restoration from the 12 March 2026, 23:00 UTC snapshot — verified as clean and uncompromised.
4. Deployed full endpoint detection and response (EDR) sweep across all production infrastructure.
5. Engaged Mandiant incident response team under existing retainer agreement SPG-IR-2025-007 at 15:00 UTC.

### 5.2 Remediation Measures (Planned and In Progress)

| Measure | Status | Target Completion |
|---------|--------|------------------|
| Full database restoration from clean backups | In progress | 15 March 2026 |
| Mandatory MFA for all service and privileged accounts | Planned | 22 March 2026 |
| Network segmentation between database and application tiers | Planned | 31 March 2026 |
| Organization-wide phishing awareness retraining | Planned | 15 April 2026 |
| Full vulnerability assessment of database infrastructure | Planned | 30 April 2026 |
| Review and update privileged access control policies | Planned | 30 April 2026 |

### 5.3 Data Subject Communication

Art. 34 notification letters will be dispatched to all 15,230 affected data subjects by 22 March 2026. The communication will include:
- Plain-language description of the breach
- DPO contact details for individual inquiries
- Description of likely consequences
- Steps data subjects can take to protect themselves (password changes, transaction monitoring)
- Offer of 12 months complimentary credit monitoring through Experian IdentityWorks

## Section 6: Phased Notification Declaration — Art. 33(4)

This notification is submitted as an initial notification under Art. 33(4). The following information will be supplemented as it becomes available:

| Outstanding Element | Reason | Expected Delivery |
|--------------------|--------|------------------|
| Confirmation of whether data exfiltration occurred | Forensic analysis by Mandiant is ongoing | Within 14 calendar days |
| Final count of affected data subjects | Data reconciliation in progress during restoration | Within 7 calendar days |
| Root cause analysis report | Full investigation timeline extends beyond 72-hour window | Within 30 calendar days |

## Section 7: Declaration

This notification is submitted in accordance with Article 33 of Regulation (EU) 2016/679. The information provided is accurate to the best of our knowledge as of the date of this notification. Supplementary information will be provided without undue further delay as it becomes available.

**Submitted by:** Dr. Elena Vasquez, Data Protection Officer
**Date:** 15 March 2026
**Reference:** SPG-BREACH-2026-003
