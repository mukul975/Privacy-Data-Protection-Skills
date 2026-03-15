---
name: japan-appi
description: >-
  Guides compliance with Japan's Act on the Protection of Personal Information (APPI,
  2022 amendments). Covers individual rights expansion, cross-border transfer restrictions
  including pre-transfer information requirements, PPC enforcement, and pseudonymised
  and anonymously processed information. Keywords: APPI, Japan data protection, PPC,
  cross-border transfer, pseudonymised information, individual rights.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: global-privacy-regulations
  tags: "appi, japan-data-protection, ppc-enforcement, cross-border-transfer, pseudonymised-data"
---

# Japan APPI Compliance (2022 Amendments)

## Overview

The Act on the Protection of Personal Information (APPI, 個人情報の保護に関する法律) was originally enacted in 2003, substantially reformed in 2015 (effective May 2017), and further amended in 2020 (effective 1 April 2022). The 2022 amendments significantly strengthened individual rights, tightened cross-border transfer requirements, expanded the scope of anonymously processed information, and introduced the concept of pseudonymously processed information.

The Personal Information Protection Commission (PPC, 個人情報保護委員会) is the independent supervisory authority with rulemaking, enforcement, and international cooperation functions.

Japan received an EU adequacy decision on 23 January 2019, enabling free flow of personal data between the EU/EEA and Japan under supplementary rules adopted by the PPC.

## Key Categories of Information

| Category | APPI Definition | Processing Framework |
|----------|----------------|---------------------|
| Personal Information (個人情報) | Information relating to a living individual that can identify the individual (Art. 2(1)) | Full APPI obligations apply |
| Personal Data (個人データ) | Personal information forming part of a personal information database (Art. 16(1)) | Additional obligations: accuracy, security, third-party provision rules |
| Retained Personal Data (保有個人データ) | Personal data that the business operator has authority to disclose, correct, or delete (Art. 16(4)) | Subject to individual rights requests |
| Special Care-Required Personal Information (要配慮個人情報) | Race, creed, social status, medical history, criminal record, crime victimisation, disability, and other categories prescribed by Cabinet Order (Art. 2(3)) | Consent required for collection (Art. 20(2)) |
| Pseudonymously Processed Information (仮名加工情報) | Personal information processed to prevent identification without additional information (Art. 2(5)) — introduced 2022 | Relaxed obligations: internal use only; no individual rights; no third-party provision |
| Anonymously Processed Information (匿名加工情報) | Information derived from personal information that cannot identify individuals and cannot be restored (Art. 2(6)) | May be provided to third parties with proper disclosure; no individual consent required |

## Cross-Border Transfer (Art. 28, 2022 Amendments)

### Pre-Transfer Information Requirement

The 2022 amendments introduced a significant new requirement: before obtaining consent for cross-border transfer, the business operator must provide the individual with information regarding the personal information protection system of the destination country.

### Transfer Mechanisms

| Mechanism | APPI Article | Requirements |
|-----------|-------------|--------------|
| Consent with pre-transfer information | Art. 28(1) | Consent after providing: (1) name of destination country, (2) personal information protection system of that country, (3) measures taken by the recipient for PI protection |
| Adequate country | Art. 28(1) exception | Transfer to a country recognised by the PPC as having equivalent protection (EU/EEA and UK recognised) |
| Recipient with equivalent measures | Art. 28(1) exception | Transfer to a recipient that has established a system conforming to APPI standards, verified by: (a) contract with the recipient, or (b) recipient is part of a corporate group with equivalent internal rules |
| Article 27 bases | Art. 28(2) | Transfer necessary for life protection, public hygiene, or cooperation with government agencies |

### PPC-Recognised Adequate Countries/Regions
As of March 2026: EU/EEA member states, United Kingdom (under supplementary rules)

### Pre-Transfer Information Content (PPC Guidelines)

| Information Element | Detail |
|--------------------|--------|
| Destination country name | Specific country or countries to which data may be transferred |
| PI protection system | Whether the destination has a comprehensive PI protection law; key features and limitations |
| Enforcement mechanism | Whether an independent enforcement authority exists |
| Individual rights | Whether individuals have enforceable rights in the destination |
| Recipient's protection measures | Specific measures the recipient has implemented (encryption, access control, contractual obligations) |

### Zenith Global Enterprises Cross-Border Transfer Register

| Transfer ID | Flow | Destination | Mechanism | Pre-Transfer Info Provided | Status |
|------------|------|-------------|-----------|--------------------------|--------|
| CBT-JP-001 | Customer data → EU HQ | Germany (EU) | Adequate country (PPC recognition) | N/A (adequacy exemption) | Active |
| CBT-JP-002 | Employee data → Regional HR | Singapore | Consent with pre-transfer info | Yes — Singapore PDPA briefing provided | Active |
| CBT-JP-003 | Logistics data → APAC | Thailand | Consent with pre-transfer info | Yes — Thailand PDPA briefing provided | Active |
| CBT-JP-004 | Payment data → Treasury | UK | Adequate country (PPC recognition) | N/A (adequacy exemption) | Active |

## Individual Rights (2022 Expansion)

### Expanded Rights Under 2022 Amendments

| Right | Article | 2022 Enhancement |
|-------|---------|------------------|
| Disclosure | Art. 33 | Expanded to include electronic format disclosure; individual may specify format (electromagnetic record) |
| Correction, addition, deletion | Art. 34 | Unchanged |
| Cessation of use and erasure | Art. 35(1) | Expanded triggers: (1) purpose achieved, (2) data no longer needed, (3) security incident occurred, (4) rights or legitimate interests likely to be harmed |
| Cessation of third-party provision | Art. 35(3) | Expanded to match cessation of use triggers |
| Disclosure of third-party provision records | Art. 33(5) | New right: individuals may request disclosure of records of third-party data provisions |
| Explanation of processing | Art. 32(2) | New: business operator must explain the basis for decisions regarding retained personal data |

### Retained Personal Data Definition Change
Prior to the 2022 amendments, data scheduled for deletion within 6 months was excluded from retained personal data. The 2022 amendments removed this 6-month exception, meaning all personal data in a personal information database is now subject to individual rights requests regardless of planned retention period.

### Response Deadlines
The APPI does not prescribe a specific day count, but the PPC Guidelines require response "without delay" (遅滞なく). The PPC has indicated that 1-2 weeks is expected for straightforward requests, with up to 2 months for complex cases with notification to the individual.

## Pseudonymously Processed Information (2022 Introduction)

### Purpose and Benefits
Pseudonymously processed information allows business operators to process personal data for internal purposes (analytics, research, product development) with relaxed obligations:

| Feature | Personal Data | Pseudonymously Processed |
|---------|--------------|------------------------|
| Purpose limitation | Strict — specific purpose required | Relaxed — may be used for purposes beyond original collection purpose (internal only) |
| Individual rights | Full rights apply | No individual rights requests |
| Accuracy obligation | Must keep accurate | No accuracy obligation |
| Third-party provision | Consent or exception required | Prohibited — internal use only |
| Notification of purpose | Required | Must publicly announce the purpose |
| Security measures | Required | Required — including separation of additional information |

### Processing Standards (Art. 41)
1. Delete information that can identify a specific individual through description alone (e.g., unique identifiers)
2. Delete or replace Individual Number (My Number) and other specified identifiers
3. Delete personal identification codes
4. Delete information that may cause property damage if misused (e.g., credit card numbers)
5. Take into account the characteristics of the personal information database

### Zenith Global Enterprises Pseudonymisation Register

| Data Set | Purpose | Method | Additional Info Separated | Annual Review |
|----------|---------|--------|--------------------------|---------------|
| Customer shipping analytics | Route optimisation research | Tokenisation + generalisation | Yes — key table in separate secured environment | March 2027 |
| Employee performance trends | Workforce planning | Aggregation to department level | Yes — name mapping in HR vault | June 2026 |

## PPC Enforcement

### Administrative Actions

| Action Type | Detail |
|------------|--------|
| Guidance (指導) | Non-binding recommendations for compliance improvement |
| Recommendations (勧告) | Art. 148: Formal recommendation to take specific measures; most common enforcement tool |
| Orders (命令) | Art. 148: Legally binding order to comply; failure constitutes criminal offence |
| Emergency orders (緊急命令) | Art. 148(3): Immediate compliance order in urgent cases |

### Criminal Penalties (2022 Enhancement)

| Violation | Penalty |
|-----------|---------|
| Violation of a PPC order | Imprisonment up to 1 year or fine up to JPY 1 million |
| Providing personal information for wrongful purposes | Imprisonment up to 1 year or fine up to JPY 500,000 |
| Corporate penalty for order violation | Fine up to JPY 100 million (increased from JPY 50 million by 2022 amendments) |
| False reporting to PPC | Fine up to JPY 500,000 |

### Notable PPC Enforcement

**Recruit Career (2019)**:
- PPC recommendation regarding the Rikunabi DMP service that scored job applicants' likelihood of declining employment offers
- Used browsing data to predict job candidate behaviour without adequate consent
- Significance: Led to increased scrutiny of profiling and automated decision-making

**LINE Corporation (2021)**:
- PPC guidance following disclosure that personal data of Japanese users was accessible from China-based subsidiaries
- Required enhanced cross-border transfer controls and transparency
- Significance: Contributed to the tightening of cross-border transfer rules in the 2022 amendments

## Compliance Programme

| Component | Detail |
|-----------|--------|
| Privacy Manager (Japan) | Tanaka Yuki, Chief Compliance Officer — Tokyo office |
| PPC registration | Business operator registered with the PPC |
| Privacy policy | Published at zenithglobal.co.jp/privacy in Japanese |
| Consent framework | Opt-in for special care-required info; pre-transfer information for cross-border |
| Individual rights | Disclosure in electronic format; expanded cessation rights per 2022 amendments |
| Pseudonymisation programme | Internal analytics using pseudonymously processed information |
| Third-party provision records | Maintained per Art. 29-30; subject to individual disclosure requests |
| Cross-border safeguards | PPC adequacy for EU/UK; consent with pre-transfer info for other destinations |
| Annual training | APPI compliance training for all Japan employees |
