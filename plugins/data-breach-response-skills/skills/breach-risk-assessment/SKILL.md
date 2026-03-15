---
name: breach-risk-assessment
description: >-
  Determines whether a personal data breach triggers notification obligations
  under GDPR Articles 33 and 34 using structured risk assessment methodology.
  Covers breach type classification (CIA triad), data sensitivity scoring,
  volume assessment, identifiability analysis, and consequence severity evaluation.
  References EDPB Guidelines 01/2021 with 18 breach scenarios. Keywords: breach
  risk assessment, GDPR, Article 33, Article 34, EDPB, notification threshold.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-breach-response
  tags: "breach-risk-assessment, gdpr, article-33, article-34, edpb, cia-triad"
---

# Conducting Breach Risk Assessment

## Overview

When a personal data breach occurs, the controller must assess whether the breach is "likely to result in a risk to the rights and freedoms of natural persons" (Art. 33(1)) to determine whether supervisory authority notification is required, and whether it is "likely to result in a high risk" (Art. 34(1)) to determine whether data subject notification is required. This skill provides a structured, repeatable methodology based on EDPB Guidelines 9/2022 and Guidelines 01/2021.

## Breach Type Classification (CIA Triad)

Every breach must first be classified according to the type of security compromise:

### Confidentiality Breach
Unauthorized or accidental disclosure of, or access to, personal data.

| Scenario | Severity Indicator |
|----------|-------------------|
| Email containing 50 customer records sent to wrong internal department | Low — limited exposure, same organization |
| Database export of 200,000 records posted on public file-sharing service | Severe — mass exposure, publicly accessible |
| Employee accesses medical records of a colleague without authorization | Medium — limited scope but sensitive data |
| Backup tape containing unencrypted payroll data lost during transport | High — financial data, unknown accessor |

### Integrity Breach
Unauthorized or accidental alteration of personal data.

| Scenario | Severity Indicator |
|----------|-------------------|
| Malware modifies patient medication dosages in a clinical database | Severe — potential physical harm |
| Software bug overwrites postal codes in 5,000 customer records | Low — non-sensitive field, reversible from backup |
| Unauthorized modification of employee performance review scores | Medium — potential employment consequences |
| SQL injection alters financial transaction records | High — financial integrity compromised |

### Availability Breach
Accidental or unauthorized loss of access to, or destruction of, personal data.

| Scenario | Severity Indicator |
|----------|-------------------|
| Ransomware encrypts the HR system for 48 hours; clean backup restored | Medium — temporary unavailability, data recovered |
| Fire destroys the only copy of archived patient records | Severe — permanent loss, healthcare impact |
| DDoS attack renders the customer portal unavailable for 6 hours | Low — temporary, no data loss or compromise |
| Cryptographic key destruction makes encrypted dataset permanently unreadable | Severe — irreversible data loss |

## Risk Assessment Methodology

### Factor 1: Data Sensitivity (Weight: High)

| Score | Criteria | Examples |
|-------|----------|---------|
| 1 — Low | Non-sensitive data already in the public domain or easily obtainable | Business contact details, publicly listed addresses |
| 2 — Medium | Personal data that could cause minor inconvenience if disclosed | Email addresses, phone numbers, purchase history |
| 3 — High | Sensitive personal data or data with significant impact potential | Financial account details, government ID numbers, employment records |
| 4 — Severe | Special category data (Art. 9), criminal conviction data (Art. 10), or data enabling significant harm | Health records, biometric data, genetic data, sexual orientation, political opinions |

### Factor 2: Volume of Affected Data Subjects

| Score | Data Subject Count | Rationale |
|-------|-------------------|-----------|
| 1 | Fewer than 100 | Limited scale — individual assessment feasible |
| 2 | 100 to 1,000 | Moderate scale — structured response required |
| 3 | 1,000 to 100,000 | Large scale — significant organizational impact |
| 4 | More than 100,000 | Mass scale — potential for widespread societal impact |

### Factor 3: Ease of Identification

| Score | Criteria |
|-------|----------|
| 1 | Data is pseudonymized or encrypted; re-identification requires additional data held separately and securely |
| 2 | Data contains indirect identifiers only; re-identification possible with moderate effort |
| 3 | Data contains direct identifiers (name + one other element); individuals readily identifiable |
| 4 | Data contains multiple direct identifiers, photographs, or biometric data; immediate identification possible |

### Factor 4: Consequence Severity

| Score | Potential Consequences |
|-------|----------------------|
| 1 | Minor inconvenience — e.g., receiving unsolicited marketing, needing to change a password |
| 2 | Moderate impact — e.g., targeted phishing risk, minor financial exposure, reputational inconvenience |
| 3 | Significant impact — e.g., identity theft risk, substantial financial loss, employment consequences, discrimination risk |
| 4 | Severe impact — e.g., physical safety threat, significant financial fraud, denial of essential services, threat to life |

### Factor 5: Individual Characteristics

| Score | Criteria |
|-------|----------|
| 1 | General adult population with no heightened vulnerability |
| 2 | Population includes some individuals in dependent relationships (employees, tenants) |
| 3 | Population includes elderly, financially vulnerable, or individuals in unequal power dynamics |
| 4 | Population includes minors, patients, asylum seekers, or individuals whose safety depends on data confidentiality |

### Factor 6: Controller-Specific Factors

| Score | Criteria |
|-------|----------|
| 1 | Controller processes personal data as an ancillary activity (e.g., office administration) |
| 2 | Controller processes personal data as a core activity for service delivery |
| 3 | Controller is in a position of trust (financial institution, healthcare provider, education) |
| 4 | Controller processes data at scale as a core business (data broker, payment processor, social media platform) |

## Scoring Matrix and Thresholds

| Aggregate Score | Risk Level | Art. 33 SA Notification | Art. 34 DS Notification | Required Action |
|----------------|-----------|------------------------|------------------------|----------------|
| 6-8 | Unlikely to result in risk | Not required | Not required | Document in Art. 33(5) breach register only |
| 9-12 | Risk present but below high threshold | Required within 72 hours | Not required | Notify supervisory authority; document fully |
| 13-18 | Likely to result in risk, approaching high | Required within 72 hours | Recommended | Notify SA; strongly consider DS notification |
| 19-24 | Likely to result in high risk | Required within 72 hours | Required without undue delay | Notify both SA and data subjects |

## EDPB Breach Scenario Analysis (Guidelines 01/2021)

### Scenario 1: Ransomware with Backup Available
- **Facts**: Hospital hit by ransomware. Patient data encrypted. Clean backup restored within 24 hours. No evidence of exfiltration.
- **Classification**: Availability breach.
- **Risk assessment**: Data sensitivity = 4 (health data), Volume = 3 (2,500 patients), Identifiability = 4, Consequences = 3 (delayed treatment), Vulnerable = 4 (patients), Controller = 3 (healthcare). Total = 21.
- **EDPB conclusion**: Notify SA and data subjects. Even though backup was available, the temporary unavailability of health data during the 24-hour restoration window posed high risk to patient safety.

### Scenario 2: Ransomware Without Backup
- **Facts**: Small manufacturing company hit by ransomware. Employee payroll data permanently lost. No backup exists.
- **Classification**: Availability breach (permanent).
- **Risk assessment**: Data sensitivity = 3, Volume = 1 (45 employees), Identifiability = 4, Consequences = 3, Vulnerable = 2, Controller = 2. Total = 15.
- **EDPB conclusion**: Notify SA and data subjects. Permanent loss of payroll data directly impacts employees' financial interests.

### Scenario 3: Data Exfiltration from Website
- **Facts**: SQL injection attack extracts usernames, hashed passwords, and email addresses of 1.2 million registered users from an e-commerce platform.
- **Classification**: Confidentiality breach.
- **Risk assessment**: Data sensitivity = 2, Volume = 4, Identifiability = 3, Consequences = 2, Vulnerable = 1, Controller = 3. Total = 15.
- **EDPB conclusion**: Notify SA and data subjects. The combination of email addresses with hashed passwords enables credential-stuffing attacks against other services.

### Scenario 4: Misdirected Email (Single Recipient)
- **Facts**: HR department sends a single employee's salary slip to the wrong internal colleague by email. Error discovered within 10 minutes. Recipient confirms deletion.
- **Classification**: Confidentiality breach.
- **Risk assessment**: Data sensitivity = 3, Volume = 1, Identifiability = 4, Consequences = 1, Vulnerable = 2, Controller = 1. Total = 12.
- **EDPB conclusion**: Notify SA (marginal). No DS notification required. The breach is contained, the recipient is known and cooperative, and financial data exposure is limited.

### Scenario 5: Lost Unencrypted USB Drive
- **Facts**: Employee loses an unencrypted USB drive containing names, addresses, and national insurance numbers of 3,500 pension scheme members.
- **Classification**: Confidentiality breach.
- **Risk assessment**: Data sensitivity = 3, Volume = 3, Identifiability = 4, Consequences = 3, Vulnerable = 3 (elderly/retirees), Controller = 3. Total = 19.
- **EDPB conclusion**: Notify SA and data subjects. Government identifiers combined with vulnerable population (retirees) creates high identity theft risk.

### Scenario 6: Accidental Publication of Student Grades
- **Facts**: University accidentally publishes exam results with student names on a publicly accessible web page for 36 hours before removal.
- **Classification**: Confidentiality breach.
- **Risk assessment**: Data sensitivity = 2, Volume = 2 (800 students), Identifiability = 4, Consequences = 2, Vulnerable = 2, Controller = 3 (education). Total = 15.
- **EDPB conclusion**: Notify SA and data subjects. Academic performance data linked to names, public exposure for 36 hours, potential impact on students' academic and professional prospects.

## Assessment Documentation Requirements

Every breach risk assessment must be documented with the following elements:

1. **Assessment metadata**: Date, assessor name, breach reference number, version
2. **Breach description**: Factual summary of what occurred
3. **CIA classification**: Which type(s) of breach
4. **Factor-by-factor scoring**: Each factor scored with written justification
5. **Aggregate score and threshold determination**: Which notification obligations apply
6. **DPO recommendation**: DPO's concurrence or dissent with the assessment
7. **Management decision**: Final notification decision with sign-off
8. **Re-assessment trigger**: Conditions that would require re-scoring (e.g., exfiltration later confirmed)

## Common Assessment Errors

1. **Underscoring consequences because exfiltration is "unconfirmed"**: The absence of evidence of exfiltration is not evidence of absence. Score consequences based on what could happen if the data is in unauthorized hands.
2. **Treating encrypted data as automatically low-risk**: Encryption is only mitigating if the encryption keys were not also compromised and the encryption standard is robust (AES-256 or equivalent).
3. **Aggregating multiple small breaches**: Recurrent similar breaches (e.g., repeated misdirected emails) may indicate a systemic issue that elevates the aggregate risk beyond what each individual incident would suggest.
4. **Ignoring availability breaches**: Temporary loss of access to health records, financial data, or safety-critical information can cause harm even if confidentiality is not compromised.
5. **Applying the 250-employee exemption to notification**: Art. 30(5) provides a limited RoPA exemption for small organizations, but there is no such exemption for Art. 33/34 breach notification obligations.
