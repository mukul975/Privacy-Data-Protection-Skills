# Standards and Regulatory References — China PIPL

## Primary Legislation

### Personal Information Protection Law (PIPL, 个人信息保护法)
- **Adopted**: 20 August 2021 by the Standing Committee of the 13th NPC
- **Effective date**: 1 November 2021
- **Structure**: 8 chapters, 74 articles
- **Scope**: Applies to processing of personal information of natural persons within the PRC (Art. 3); extraterritorial application for processors providing services to or analysing behaviour of individuals in the PRC

### Cybersecurity Law (CSL, 网络安全法)
- **Effective date**: 1 June 2017
- **Key provisions**: Network operator obligations (Art. 22-28); personal information protection (Arts. 40-44); CII protection (Arts. 31-39); data localisation for CIIOs (Art. 37)
- **Relationship to PIPL**: CSL provides the foundational cybersecurity framework; PIPL adds comprehensive personal information protection obligations

### Data Security Law (DSL, 数据安全法)
- **Effective date**: 1 September 2021
- **Key provisions**: Data classification and grading (Art. 21); important data catalogue (Art. 21); data security review (Art. 24); cross-border data transfer restrictions (Art. 31)
- **Relationship to PIPL**: DSL governs data security broadly (including non-personal data); PIPL specifically addresses personal information

## Implementing Regulations

### Measures on Security Assessment of Data Cross-Border Transfer (CAC, 数据出境安全评估办法)
- **Effective date**: 1 September 2022
- **Issuing authority**: Cyberspace Administration of China (CAC)
- **Key provisions**:
  - Art. 4: Mandatory security assessment triggers (CIIO, 1M+ individuals, 100K+ cumulative transfers, 10K+ sensitive PI transfers)
  - Art. 5: Self-assessment requirements before application
  - Art. 7: Application materials (self-assessment report, legal documents with overseas recipient, other relevant materials)
  - Art. 8: CAC review period (7 working days to accept; 45 working days to complete, extendable by 15 days)
  - Art. 14: Assessment result valid for 2 years
  - Art. 15: Re-assessment triggers (changes in data export purpose/method/scope, changes in overseas data protection policies/environment, changes in overseas recipient's ability to protect data)

### Measures on Standard Contract for Cross-Border Transfer of Personal Information (CAC)
- **Effective date**: 1 June 2023
- **Key provisions**:
  - Annex: Full text of the standard contract (not modifiable)
  - Art. 4: Applicability conditions (non-CIIO, <1M individuals, <100K cumulative transfers, <10K sensitive PI transfers)
  - Art. 6: Filing with provincial CAC within 10 working days
  - Art. 7: PIPIA must be conducted before executing the standard contract
  - Art. 9: Re-filing upon material changes

### Provisions on Facilitating and Regulating Cross-Border Data Flows (CAC)
- **Effective date**: 22 March 2024
- **Key provisions**:
  - Art. 3: Exemption for contract/HR necessity transfers
  - Art. 4: Exemption for transfers of <100,000 individuals (excluding sensitive PI) within one year
  - Art. 5: Free trade zone negative list mechanism
  - Art. 6: Simplified security assessment re-filing for material changes
  - Art. 8: Standard contract and certification exemptions aligned with security assessment exemptions

### Specification for Cross-Border Processing Activities of Personal Information (TC260, GB/T 35273 related)
- **Published**: November 2022 by National Information Security Standardization Technical Committee (TC260)
- **Purpose**: Technical specification for personal information protection certification for cross-border transfers under Art. 38(3)
- **Key requirements**: Both parties must accept supervision; binding internal PI protection rules for multinational groups; annual supervision audits

## National Standards (GB/T)

### GB/T 35273-2020 — Information Security Technology: Personal Information Security Specification
- **Status**: Recommended national standard (not mandatory, but referenced by regulators)
- **Key provisions**: Personal information classification; consent requirements; purpose limitation; data minimisation; security measures; individual rights implementation
- **Practical significance**: Widely used as the benchmark for demonstrating PIPL compliance in enforcement proceedings

### GB/T 39335-2020 — Information Security Technology: Personal Information Security Impact Assessment Guide
- **Purpose**: Guidance for conducting personal information protection impact assessments (PIPIAs) under Art. 55-56
- **Structure**: Risk identification methodology; impact assessment criteria; mitigation measures catalogue

### GB/T 41479-2022 — Information Security Technology: Network Data Processing Security Requirements
- **Purpose**: Technical requirements for secure data processing in network environments
- **Relevance**: Implements CSL and DSL requirements for network operators processing personal information

## Sector-Specific Regulations

### Financial Sector
- **PBOC Personal Financial Information Protection Technical Specification (JR/T 0171-2020)**: Classification of personal financial information into C3 (highest sensitivity), C2, and C1 categories; processing requirements per category
- **CBIRC Data Governance Guidelines for Banking Institutions (2018)**: Data governance framework for banking; board-level accountability

### Healthcare
- **Measures for Population Health Information Management (2014)**: Health information localisation; cross-border transfer restrictions for population health data
- **Measures for Network Security Management of Medical and Health Institutions (Draft, 2022)**: PIPL-aligned requirements for medical data processors

### Telecommunications
- **MIIT Provisions on Protecting Personal Information of Telecommunications and Internet Users (2013, under revision)**: Pre-PIPL framework still applicable for telecom operators
- **MIIT App Personal Information Protection Regulation**: Informed consent requirements; minimum necessary principle; deletion upon account cancellation

## PIPL vs GDPR Comparison

| Feature | PIPL | GDPR |
|---------|------|------|
| Consent as default basis | Yes (Art. 13(1) is the primary basis) | No (six co-equal bases under Art. 6) |
| Legitimate interest basis | No standalone basis | Yes (Art. 6(1)(f)) |
| Separate/specific consent | Required for 5 specific scenarios | Explicit consent for Art. 9 sensitive data |
| Cross-border transfer mechanisms | CAC assessment, standard contract, certification | Adequacy decisions, SCCs, BCRs, derogations |
| Data localisation | Mandatory for CIIOs (Art. 40) | Not required (but may arise from Member State law) |
| Maximum fine | 5% of previous year's revenue or RMB 50M | 4% of global annual turnover or EUR 20M |
| DPO equivalent | Personal information protection responsible person (Art. 52) | Data Protection Officer (Art. 37) |
| Government access | No transparency report obligation | Limited by EU fundamental rights framework |
| Impact assessment | Mandatory for 6 specific triggers (Art. 55) | Required for high-risk processing (Art. 35) |
| Deceased persons' rights | Yes — relatives may exercise rights (Art. 49) | Not addressed in GDPR |

## Enforcement Precedents

### Didi Global (2022)
- Fine: RMB 8.026 billion (approximately USD 1.2 billion)
- Violations: 16 counts across PIPL, CSL, and DSL including unlawful collection, excessive processing, and failure to comply with cybersecurity review
- Personal fines: RMB 1 million each on CEO and President
- Significance: Largest data protection enforcement action in China

### App Store Compliance Campaigns (2021-2025)
- MIIT and CAC jointly conducted regular compliance inspections of mobile applications
- Common violations: Excessive data collection, bundled consent, failure to provide deletion mechanisms, unclear privacy notices
- Remediation: Apps given 5-15 working days to remediate; non-compliant apps removed from app stores

### Ant Group (2021)
- PBOC-led investigation into personal information handling practices in financial services
- Required comprehensive rectification of data collection and consent practices
- Significance: Demonstrated enforcement of financial sector PI protection requirements
