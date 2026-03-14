# Standards and Regulatory References — Automated Data Discovery

## Primary Legislation

### GDPR — Regulation (EU) 2016/679

- **Article 30**: Records of processing activities — controllers must maintain records containing categories of personal data, categories of recipients, and transfers to third countries. Automated discovery tools directly support maintaining accurate and complete Art. 30 records.
- **Article 5(1)(d)**: Accuracy principle — personal data shall be accurate and where necessary kept up to date. Automated discovery validates that data inventories accurately reflect actual data holdings.
- **Article 25**: Data protection by design and by default — implementing automated discovery is a technical measure demonstrating proactive identification and management of personal data.
- **Article 32**: Security of processing — discovery tools identify where personal data resides to ensure appropriate security measures are applied to all repositories containing personal data.
- **Article 35(7)(a)**: DPIA requirement for systematic description of processing — automated discovery provides the data inventory needed for comprehensive DPIA descriptions.

## Regulatory Guidance

### ICO — Accountability Framework Tool (2023)

- **Expectation 1.3**: "You have an accurate and comprehensive record of all the personal data you hold, including where it came from, who it is shared with, and what you do with it."
- **Recommended Practice**: The ICO recommends automated data mapping tools for organisations processing personal data at scale, noting that manual inventories are insufficient for complex processing environments.

### EDPB Guidelines 4/2019 on Article 25 — Data Protection by Design and by Default (v2.0, 2020)

- **Section 3.1**: Implementing appropriate technical measures includes data mapping and inventory tools that provide continuous visibility into personal data processing.
- **Section 4.2**: Data protection by default requires understanding where personal data resides before applying minimisation and access control measures.

### NIST Privacy Framework v1.0 (January 2020)

- **ID.IM-P1**: Inventory and mapping — systems, products, and services that process personal data are inventoried.
- **ID.IM-P3**: Data processing ecosystem — data actions are mapped, including personal data flows and processing relationships.
- **CT.DM-P1**: Data minimisation — personal data processing is limited to what is necessary.
- **Relevance**: NIST Privacy Framework's Identify function aligns directly with automated discovery capabilities.

### ISO/IEC 27701:2019 — Privacy Information Management System (PIMS)

- **Clause 7.2.8**: Inventory of personal data processing — the organisation shall determine and document an inventory covering personal data, processing purposes, security measures, and access controls.
- **Clause 7.4.5**: PII de-identification and deletion — the organisation shall identify mechanisms for de-identifying and deleting PII, which requires knowing where PII resides (discovery).

### CNIL — Practical Guide to Data Mapping (2020)

- **Key Content**: Step-by-step methodology for data mapping, recommending automated tools for organisations processing data across multiple systems. Emphasis on identifying all data flows, not just primary databases.

## Industry Standards

### Microsoft Purview — Sensitive Information Types Reference

- **Reference**: Microsoft Learn documentation — over 300 built-in sensitive information types covering 40+ countries and regions
- **GDPR-specific types**: EU Debit Card Number, EU Driver's License Number, EU National Identification Number, EU Passport Number, EU Social Security Number, EU Tax Identification Number (per Member State)
- **Accuracy framework**: Each SIT has defined confidence levels (65% low, 75% medium, 85% high) based on pattern match plus corroborative evidence (keywords, checksums, format validation)

### Cloud Security Alliance (CSA) — Cloud Controls Matrix v4.0

- **DSP-02**: Data inventory — establish and maintain a data inventory that includes data type, classification, residency/location, and authorised access.
- **DSP-04**: Data classification — classify data according to its type and sensitivity level.
