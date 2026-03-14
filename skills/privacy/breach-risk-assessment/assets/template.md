# Breach Risk Assessment Form

## Assessment Metadata

| Field | Value |
|-------|-------|
| Breach Reference | SPG-BREACH-2026-003 |
| Assessment Date | 13 March 2026 |
| Assessor | Dr. Elena Vasquez, Data Protection Officer |
| Assessment Version | 1.0 |
| Methodology | EDPB Guidelines 9/2022, Section 3.1 |

## Breach Summary

| Field | Value |
|-------|-------|
| Breach Discovery Timestamp | 13 March 2026, 14:30 UTC |
| Breach Type | Availability (primary); Confidentiality (under investigation) |
| Description | LockBit 3.0 ransomware encrypted 48,720 customer records on production database cluster db-prod-eu-west-01 through db-prod-eu-west-04. Attack vector: compromised service account via spear-phishing. Backup restoration in progress. |
| Systems Affected | db-prod-eu-west-01, db-prod-eu-west-02, db-prod-eu-west-03, db-prod-eu-west-04 |
| Breach Contained | Yes — network isolation at 12:45 UTC on 13 March 2026 |
| Data Subjects Affected | Approximately 15,230 (individual, business, and joint account holders) |
| Data Categories | Full names, postal addresses, email addresses, payment card last-4-digits, transaction histories, account balances |

## Factor-by-Factor Scoring

### Factor 1: Data Sensitivity

| Element | Assessment |
|---------|-----------|
| Score | 3 (High) |
| Rationale | Financial data (payment card partial numbers, transaction histories, account balances) and postal addresses. Not special category data under Art. 9, but financial data significantly elevates sensitivity. |
| Data categories driving score | Payment card last-4-digits, transaction histories, account balances |

### Factor 2: Volume of Affected Data Subjects

| Element | Assessment |
|---------|-----------|
| Score | 3 (1,000 to 100,000) |
| Rationale | Approximately 15,230 data subjects affected across three account holder categories. |
| Count methodology | Query of affected database cluster against customer identity records, deduplicated by unique customer ID. |

### Factor 3: Ease of Identification

| Element | Assessment |
|---------|-----------|
| Score | 4 (Immediate identification) |
| Rationale | Affected records contain full names combined with postal addresses, email addresses, and partial payment card numbers. Individuals are directly and immediately identifiable. |
| Mitigation considered | Payment card numbers are stored as last-4-digits only. Full card numbers are tokenized and stored in a separate PCI DSS-compliant vault that was not affected by the ransomware. |

### Factor 4: Consequence Severity

| Element | Assessment |
|---------|-----------|
| Score | 3 (Significant) |
| Rationale | Primary consequence is temporary loss of access to financial account information (availability breach). If exfiltration is later confirmed, consequences escalate to identity theft risk, targeted phishing, and potential financial fraud using the combination of names, addresses, and partial payment details. |
| Worst case | Identity theft and targeted financial fraud using compromised personal + financial data combination |

### Factor 5: Individual Characteristics

| Element | Assessment |
|---------|-----------|
| Score | 1 (General adult population) |
| Rationale | Affected data subjects are adult individual and business account holders. No minors, patients, or specially vulnerable populations identified in the affected dataset. |
| Vulnerable categories check | Minors: No. Patients: No. Elderly: Not disproportionately. Asylum seekers: No. |

### Factor 6: Controller-Specific Factors

| Element | Assessment |
|---------|-----------|
| Score | 4 (Large-scale data processing as core business) |
| Rationale | Stellar Payments Group is a payment services provider. Processing of financial personal data is the core business activity. Data subjects entrust their financial information to the controller with an expectation of heightened security. Regulatory expectations for payment processors are elevated under both GDPR and PSD2. |

## Aggregate Score and Threshold

| Element | Value |
|---------|-------|
| Aggregate Score | 18 / 24 |
| Risk Percentage | 75.0% |
| Risk Level | APPROACHING HIGH RISK |
| Art. 33 SA Notification | REQUIRED within 72 hours |
| Art. 34 DS Notification | STRONGLY RECOMMENDED |

## DPO Recommendation

Based on the aggregate risk score of 18/24, I recommend:

1. **Immediate Art. 33 notification** to the Berliner Beauftragte für Datenschutz und Informationsfreiheit within the 72-hour deadline (by 16 March 2026, 14:30 UTC).
2. **Art. 34 data subject notification** to all 15,230 affected individuals within 7 calendar days, given the proximity to the high-risk threshold and the financial nature of the data. The score of 18 is at the boundary of the "approaching high risk" and "high risk" thresholds, and the precautionary principle favors notification.
3. **Re-assessment** upon completion of the Mandiant forensic analysis, particularly regarding whether data exfiltration occurred. If exfiltration is confirmed, the consequence score should be increased to 4, raising the aggregate to 19 and confirming high risk.
4. **Credit monitoring offer** to affected individuals as a mitigating measure regardless of the formal Art. 34 determination.

**DPO Signature:** Dr. Elena Vasquez
**Date:** 13 March 2026

## Management Decision

| Element | Decision |
|---------|----------|
| Art. 33 SA Notification | Approved — proceed immediately |
| Art. 34 DS Notification | Approved — proceed with notification to all affected individuals |
| Credit Monitoring | Approved — 12 months Experian IdentityWorks |
| Additional Measures | Engage external communications firm for data subject notification support |

**Approved by:** Marcus Lindqvist, Chief Executive Officer
**Approved by:** Sarah Chen, General Counsel
**Date:** 13 March 2026
