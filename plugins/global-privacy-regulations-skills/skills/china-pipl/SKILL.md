---
name: china-pipl
description: >-
  Guides compliance with China's Personal Information Protection Law (PIPL, effective
  1 November 2021). Covers consent requirements, cross-border transfer mechanisms
  (CAC security assessment, standard contracts, certification), separate consent triggers,
  and critical information infrastructure obligations. Keywords: PIPL, China data protection,
  CAC security assessment, cross-border transfer, separate consent, CIIO.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: global-privacy-regulations
  tags: "pipl, china-data-protection, cac-security-assessment, cross-border-transfer, ciio"
---

# China PIPL Compliance

## Overview

The Personal Information Protection Law of the People's Republic of China (PIPL, 个人信息保护法) was adopted by the Standing Committee of the National People's Congress on 20 August 2021 and took effect on 1 November 2021. The PIPL is China's first comprehensive national personal information protection law, operating alongside the Cybersecurity Law (CSL, effective 1 June 2017) and the Data Security Law (DSL, effective 1 September 2021) to form China's data governance framework.

The Cyberspace Administration of China (CAC, 国家互联网信息办公室) is the primary regulator, with enforcement authority shared among the Ministry of Public Security, the Ministry of Industry and Information Technology (MIIT), and sector-specific regulators.

## Scope and Extraterritorial Application

### Territorial Scope (Art. 3)

The PIPL applies to:
1. Processing of personal information of natural persons within the territory of the PRC (Art. 3(1))
2. Processing conducted outside the PRC of personal information of natural persons within the PRC where the purpose is:
   - Providing products or services to natural persons within the PRC (Art. 3(2)(i))
   - Analysing or assessing the behaviour of natural persons within the PRC (Art. 3(2)(ii))
   - Other circumstances provided by laws or administrative regulations (Art. 3(2)(iii))

### Extraterritorial Compliance (Art. 53)

Overseas personal information processors falling under Art. 3(2) must:
- Establish a dedicated entity or designate a representative within the PRC to handle personal information protection matters
- Report the name and contact information of the entity or representative to the relevant CAC department

**Zenith Global Enterprises implementation**: Zenith has designated its Shanghai office (Zenith Global Logistics (Shanghai) Co., Ltd) as the PRC representative entity, with the local Data Protection Manager serving as the designated contact.

## Lawful Bases for Processing (Art. 13)

| Basis | PIPL Article | Key Requirements |
|-------|-------------|------------------|
| Consent | Art. 13(1) | Voluntary, explicit, informed; specific consent for sensitive PI, cross-border transfers, and public disclosure |
| Contract necessity | Art. 13(2) | Necessary to conclude or perform a contract to which the individual is a party, or for HR management per lawfully adopted labour rules |
| Statutory duty or obligation | Art. 13(3) | Necessary to fulfil statutory duties or obligations |
| Public health emergency | Art. 13(4) | Necessary to respond to public health emergencies or protect life/property in emergencies |
| Public interest activities | Art. 13(5) | Processing for news reporting, public opinion supervision, or other public interest activities within a reasonable scope |
| Processing within reasonable scope of lawfully disclosed PI | Art. 13(6) | Information already disclosed by the individual or through other lawful means |
| Other circumstances in laws/administrative regulations | Art. 13(7) | Catch-all provision for sector-specific legislation |

**Key distinction from GDPR**: The PIPL does not include a standalone legitimate interest basis. Art. 13(6) (processing lawfully disclosed information) is the closest analogue but far narrower in scope.

## Consent Framework

### General Consent Requirements (Arts. 14-16)

| Requirement | PIPL Provision | Implementation |
|-------------|---------------|----------------|
| Voluntariness | Art. 14 | Consent must not be obtained through deception, coercion, or inducement; services may not be refused solely for withholding consent unless PI is necessary for the service |
| Informedness | Art. 14 | Individuals must be fully informed before consenting; information provided per Art. 17 |
| Explicitness | Art. 14 | Clear affirmative action required; pre-ticked boxes or bundled consent are non-compliant |
| Withdrawal | Art. 15 | Individuals have the right to withdraw consent; processors must provide convenient withdrawal mechanisms; withdrawal does not affect prior lawful processing |
| Separate consent | Arts. 23, 25, 26, 29, 39 | Required for specific high-risk processing scenarios (see below) |

### Separate Consent Triggers (单独同意)

The PIPL requires separate consent (单独同意, dāndú tóngyì) — consent obtained independently from other consent collection — for the following processing activities:

| Trigger | Article | Context |
|---------|---------|---------|
| Provision of PI to other processors | Art. 23 | When a processor provides personal information to another processor |
| Public disclosure of PI | Art. 25 | When a processor publicly discloses personal information |
| Processing images/personal identification from public surveillance | Art. 26 | Use of images or personal identification information collected via public places for purposes other than public safety |
| Processing sensitive personal information | Art. 29 | All processing of sensitive PI requires separate consent plus disclosure of necessity and impact |
| Cross-border transfer of PI | Art. 39 | International transfer requires separate consent with specified disclosures |

**Zenith Global Enterprises implementation**:
- Consent management platform configured with separate consent flows for each trigger scenario
- Customer onboarding includes distinct consent checkboxes for: (a) primary service processing, (b) data sharing with logistics partners, (c) cross-border transfer to headquarters, (d) credit assessment (sensitive PI)
- Employee consent flows include separate consent for: (a) employment data cross-border transfer, (b) background check (sensitive PI)

## Sensitive Personal Information (Art. 28)

### Definition
Sensitive personal information (敏感个人信息) is personal information that, once leaked or illegally used, may easily lead to infringement of the dignity of natural persons or harm to their personal or property safety. It includes:
- Biometric information
- Religious beliefs
- Specific identity information (including ID numbers)
- Medical and health information
- Financial account information
- Location tracking information
- Personal information of minors under 14 years of age

### Processing Requirements (Arts. 28-32)

| Requirement | Detail |
|-------------|--------|
| Separate consent | Art. 29: Separate consent required; written consent where required by laws/regulations |
| Necessity justification | Art. 28: Must have a specific purpose and sufficient necessity |
| Impact assessment | Art. 55: Personal information protection impact assessment (PIPIA) required before processing |
| Notification | Art. 30: Notify the individual of the necessity and impact on rights; for minors under 14, obtain consent from parent/guardian |
| Retention minimisation | Art. 28: Adopt strict protection measures; minimise retention period |

### Zenith Global Enterprises Sensitive PI Register

| Data Type | Classification | Purpose | Consent Type | PIPIA Reference |
|-----------|---------------|---------|-------------|-----------------|
| National ID numbers (身份证号) | Specific identity | Customs clearance identity verification | Separate written consent | PIPIA-CN-001 |
| Financial account information | Financial | Payment processing for freight charges | Separate consent | PIPIA-CN-002 |
| Employee health certificates | Medical/health | Occupational safety compliance | Separate consent | PIPIA-CN-003 |
| GPS tracking of delivery vehicles | Location tracking | Real-time shipment tracking for customers | Separate consent (drivers) | PIPIA-CN-004 |

## Cross-Border Transfer Mechanisms (Arts. 38-43)

### Three Mandatory Mechanisms

The PIPL provides three primary mechanisms for transferring personal information outside the PRC, applicable based on the processor's scale and nature:

#### 1. CAC Security Assessment (Art. 40; CAC Measures effective 1 September 2022)

**When required** (mandatory for any of the following):
- Critical information infrastructure operators (CIIOs) transferring any personal information abroad
- Processors that process personal information of 1 million or more individuals
- Processors that have cumulatively transferred personal information of 100,000 or more individuals abroad since 1 January of the preceding year
- Processors that have cumulatively transferred sensitive personal information of 10,000 or more individuals abroad since 1 January of the preceding year

**Process**:
1. Conduct a self-assessment (personal information protection impact assessment)
2. Submit the application to the CAC through the provincial-level CAC office
3. CAC completes the assessment within 45 working days (extendable by another 15 working days for complex cases)
4. Assessment valid for 2 years from the date of the assessment result, renewable upon expiry

**Zenith Global Enterprises status**: As Zenith processes personal information of over 100,000 customers and employees in China, and has transferred personal information of more than 100,000 individuals abroad cumulatively, the CAC security assessment is the mandatory transfer mechanism.

#### 2. Standard Contract for Cross-Border Transfer (Art. 38(2); CAC Measures effective 1 June 2023)

**When applicable** (must meet all conditions):
- The processor is not a CIIO
- The processor processes personal information of fewer than 1 million individuals
- Cumulative cross-border transfer of fewer than 100,000 individuals' personal information since 1 January of the preceding year
- Cumulative cross-border transfer of fewer than 10,000 individuals' sensitive personal information since 1 January of the preceding year

**Process**:
1. Conduct a personal information protection impact assessment
2. Execute the CAC-published standard contract with the overseas recipient
3. File the executed contract with the provincial-level CAC office within 10 working days of effectiveness

**Standard contract key provisions**:
- Purpose, scope, and method of processing by the overseas recipient
- Overseas recipient's obligations regarding data protection
- Individual rights protection mechanisms
- Remedies and liability allocation
- Termination conditions

#### 3. Personal Information Protection Certification (Art. 38(3); TC260 Specification effective November 2022)

**When applicable**:
- Cross-border transfers within a multinational group or between entities subject to the same PI protection policies
- Processors that meet the standard contract thresholds

**Process**:
1. The processor and overseas recipient jointly apply to an accredited certification body
2. Certification body evaluates compliance with the TC260 Specification for Cross-Border Processing Activities
3. Certification valid for 3 years with annual supervision audits
4. Both parties must accept supervision by the certification body and the CAC

### CAC Relaxation Measures (March 2024)

The CAC issued the Provisions on Facilitating and Regulating Cross-Border Data Flows (effective 22 March 2024), which introduced exemptions:

| Exemption | Condition |
|-----------|-----------|
| Contract/HR necessity | Cross-border transfer necessary for concluding/performing a contract to which the individual is a party, or for HR management under lawfully adopted labour rules |
| Small volume | Processor expects to transfer personal information of fewer than 100,000 individuals (excluding sensitive PI) abroad within one year |
| Free trade zones | Transfers from designated free trade zones subject to the negative list of that zone |

**Important**: These exemptions do not apply to CIIOs, transfers of important data, or transfers exceeding the specified thresholds.

### Zenith Global Enterprises Cross-Border Transfer Register

| Transfer ID | Flow | Destination | Mechanism | Volume | Assessment Status |
|------------|------|-------------|-----------|--------|-------------------|
| CBT-CN-001 | Customer logistics data → EU HQ | Germany | CAC Security Assessment | 150,000+ individuals | Approved (valid until August 2026) |
| CBT-CN-002 | Employee HR data → Regional HR | Singapore | CAC Security Assessment | 2,500 employees | Approved (valid until August 2026) |
| CBT-CN-003 | Vendor payment data → Treasury | United Kingdom | Standard Contract (filed) | 800 vendors | Filed with Shanghai CAC |
| CBT-CN-004 | Shipment tracking data → API partners | Japan | Contract necessity exemption | 50,000 individuals | Exemption documented |

## Critical Information Infrastructure (CII)

### CIIO Obligations Under PIPL

Critical information infrastructure operators (关键信息基础设施运营者, CIIOs) face additional obligations:

| Obligation | Legal Basis | Detail |
|-----------|-------------|--------|
| Data localisation | Art. 40 | Personal information and important data collected/generated during operations within the PRC must be stored domestically |
| Security assessment for export | Art. 40 | Mandatory CAC security assessment for any cross-border transfer (no alternative mechanisms) |
| Annual security assessment | CSL Art. 38 | Annual network security assessment and submission of assessment reports |
| Data security officer | DSL Art. 27 | Designate a data security responsible person |

### CII Sector Identification

The following sectors are designated as CII under the Critical Information Infrastructure Security Protection Regulations (effective 1 September 2021):
- Public communications and information services
- Energy
- Transportation
- Water conservancy
- Finance
- Public services
- E-government
- National defence science and industry
- Other important network facilities and information systems that may endanger national security, people's livelihood, or the public interest if damaged

**Zenith Global Enterprises assessment**: As a logistics company, Zenith may be designated as CII under the transportation sector if its systems are determined to endanger national security or the public interest if damaged. Zenith maintains ongoing dialogue with the relevant sector authority (Ministry of Transport) regarding CII designation status.

## Personal Information Protection Impact Assessment (PIPIA)

### Mandatory PIPIA Triggers (Art. 55)

| Trigger | Description |
|---------|-------------|
| Processing sensitive personal information | Any processing of sensitive PI (Art. 28) |
| Automated decision-making | Using personal information for automated decisions (Art. 24) |
| Entrusted processing | Entrusting a third party to process personal information (Art. 21) |
| Cross-border transfer | Providing personal information to overseas parties (Art. 38) |
| Public disclosure | Publicly disclosing personal information (Art. 25) |
| Other high-impact processing | Processing that has a significant impact on individual rights |

### PIPIA Contents (Art. 56)

| Element | Description |
|---------|-------------|
| Legality and legitimacy | Whether the processing purpose, method, and scope are lawful, legitimate, and necessary |
| Impact assessment | Assessment of the impact on individual rights and interests and the level of risk |
| Security measures | Whether the protective measures adopted are lawful, effective, and proportionate to the risk |
| Risk mitigation | Identification of risks and proposed mitigation measures |

### PIPIA Retention
The PIPIA report and processing records must be retained for at least 3 years (Art. 56).

## Individual Rights (Arts. 44-50)

| Right | Article | Implementation at Zenith Global Enterprises |
|-------|---------|---------------------------------------------|
| Right to know and to decide | Art. 44 | Privacy notice in Simplified Chinese on all collection points |
| Right to restrict or refuse processing | Art. 44 | Opt-out mechanisms in customer portal; employee objection procedure |
| Right to access and copy | Art. 45 | Self-service data export from customer account; employee requests through HR |
| Right to portability | Art. 45(3) | Structured export to designated recipient (per CAC implementation rules when issued) |
| Right to correction and supplementation | Art. 46 | Self-service correction in customer portal; HR system for employees |
| Right to deletion | Art. 47 | Automated deletion workflows triggered by: purpose fulfilment, consent withdrawal, service termination, processing violation |
| Right to explanation | Art. 48 | Individuals may request explanation of PI processing rules; processor must provide timely response |
| Right regarding automated decision-making | Art. 24 | Right to request explanation of automated decisions; right to refuse decisions made solely through automated means |
| Right of deceased persons' relatives | Art. 49 | Close relatives may exercise rights of deceased individuals unless deceased arranged otherwise |

## Enforcement Framework

### Administrative Penalties (Arts. 66-69)

| Violation Level | Organisation Penalty | Individual Penalty (directly responsible person) |
|----------------|---------------------|--------------------------------------------------|
| General violations | Order to rectify; warning; confiscation of unlawful income; suspension or termination of related application; fine up to RMB 1 million | Fine of RMB 10,000–100,000 |
| Serious violations | Order to rectify; confiscation of unlawful income; fine up to RMB 50 million or up to 5% of previous year's revenue; suspension of business; revocation of business licence | Fine of RMB 100,000–1,000,000; prohibition from serving as director, supervisor, senior manager, or DPO for a specified period |

### Enforcement Actions

**Didi Global CAC Investigation (2021-2022)**:
- CAC launched a cybersecurity review of Didi Chuxing following its NYSE IPO in June 2021
- Didi was found to have committed 16 violations of the CSL, DSL, and PIPL
- Final penalty (July 2022): RMB 8.026 billion fine (approximately USD 1.2 billion), plus personal fines of RMB 1 million each on CEO and President
- Significance: Largest data protection fine in China; demonstrated integration of PIPL, CSL, and DSL enforcement

**SAMR/CAC App Compliance Campaigns (2021-2025)**:
- Regular enforcement campaigns targeting mobile applications for excessive data collection, bundled consent, and failure to provide deletion mechanisms
- Thousands of apps removed from app stores or required to remediate
- Zenith Global Enterprises app compliance: Annual audit by external firm; remediation within 15 days of any finding

## Compliance Programme Structure

| Component | Detail |
|-----------|--------|
| PRC representative entity | Zenith Global Logistics (Shanghai) Co., Ltd |
| Data Protection Manager (China) | Li Wei, Director of Information Security, Shanghai office |
| PIPIA programme | Mandatory PIPIA for all triggers under Art. 55; retained for minimum 3 years |
| Cross-border transfer compliance | CAC Security Assessment approved for primary data flows; standard contracts filed for lower-volume flows |
| Consent management | Platform configured for general and separate consent per Arts. 14, 23, 25, 29, 39 |
| Training | Annual PIPL compliance training for all PRC employees; quarterly refreshers for data handling roles |
| Incident response | 72-hour notification to CAC for incidents affecting PI security; coordinated with headquarters incident response team |
