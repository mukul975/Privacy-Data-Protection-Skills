---
name: brazil-lgpd
description: >-
  Guides compliance with Brazil's Lei Geral de Proteção de Dados (LGPD, Lei 13.709/2018).
  Covers the 10 lawful bases under Art. 7, DPO appointment, ANPD enforcement, data subject
  rights under Arts. 17-22, and international transfer mechanisms. Keywords: LGPD, Brazil
  data protection, ANPD, lawful bases, data subject rights, international transfers.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: global-privacy-regulations
  tags: "lgpd, brazil-data-protection, anpd, lawful-bases, international-transfers"
---

# Brazil LGPD Compliance (Lei 13.709/2018)

## Overview

The Lei Geral de Proteção de Dados Pessoais (LGPD), enacted as Lei 13.709 on 14 August 2018 and effective from 18 September 2020 (with sanctions enforceable from 1 August 2021), is Brazil's comprehensive data protection law. The LGPD applies to any processing of personal data carried out in Brazil, where the processing activity aims to offer goods or services to individuals located in Brazil, or where the personal data was collected in Brazil (Art. 3). The Autoridade Nacional de Proteção de Dados (ANPD) serves as the supervisory authority with rulemaking, enforcement, and advisory functions.

## Ten Lawful Bases Under Article 7

The LGPD provides ten distinct legal bases for processing personal data, exceeding the six lawful bases under EU GDPR. Each base operates independently — organisations may rely on any applicable base without a prescribed hierarchy.

### 1. Consent of the Data Subject (Art. 7, I)

**Requirements under Art. 8**:
- Consent must be provided in writing or by other means that demonstrate the free, informed, and unequivocal expression of the data subject's will
- Written consent must appear in a clause separate from other contractual provisions (Art. 8, §1)
- The burden of proof that consent was obtained rests with the controller (Art. 8, §2)
- Consent is void if based on misleading information or where the data subject was not adequately informed (Art. 9, §1)
- Consent may be revoked at any time by express statement of the data subject, via a free and facilitated procedure (Art. 8, §5)

**Implementation at Zenith Global Enterprises**:
- Marketing communications to Brazilian customers require opt-in consent with a standalone consent clause
- Consent records stored in the consent management platform with timestamp, scope, and version
- Consent withdrawal mechanism accessible through the customer privacy portal within two clicks
- Granular consent for each processing purpose (marketing, profiling, third-party sharing)

### 2. Compliance with Legal or Regulatory Obligation (Art. 7, II)

**Scope**: Processing necessary for the controller to comply with a legal or regulatory obligation under Brazilian law. This includes tax reporting under the Código Tributário Nacional, anti-money laundering under Lei 9.613/1998, and employment record retention under the Consolidação das Leis do Trabalho (CLT).

**Implementation at Zenith Global Enterprises**:
- Employee payroll records retained for 5 years per CTN Art. 173
- Employment records retained for the duration of the employment relationship plus 5 years per CLT Art. 11
- Anti-money laundering records retained for 5 years from the last transaction per Lei 9.613/1998, Art. 10

### 3. Execution of Public Policies by the Public Administration (Art. 7, III)

**Scope**: Processing by the public administration for the execution of public policies provided in laws, regulations, or contracts. This base is available only to public administration bodies and is not applicable to private-sector organisations.

**Zenith Global Enterprises relevance**: Not applicable as a private-sector entity. If engaged in public-private partnerships, the government partner invokes this base.

### 4. Research by Research Bodies (Art. 7, IV)

**Scope**: Processing for carrying out studies by research bodies, ensuring anonymisation of personal data whenever possible. Research bodies must comply with specific ethical standards and are subject to oversight by the relevant ethics committees.

**Zenith Global Enterprises relevance**: If collaborating with academic institutions on logistics optimisation research, ensure data shared for research purposes is anonymised or pseudonymised with the research body assuming controller responsibility.

### 5. Contract Performance (Art. 7, V)

**Scope**: Processing necessary for the execution of a contract or preliminary procedures related to a contract to which the data subject is a party, at the request of the data subject.

**Implementation at Zenith Global Enterprises**:
- Processing customer shipping addresses, contact details, and payment information to fulfil freight forwarding contracts
- Pre-contractual processing of credit assessments when customers request trade credit terms
- Processing employee data necessary for execution of the employment contract

### 6. Exercise of Rights in Judicial, Administrative, or Arbitration Proceedings (Art. 7, VI)

**Scope**: Processing necessary for the regular exercise of rights in judicial, administrative, or arbitration proceedings. This permits retention and use of personal data where necessary for litigation or regulatory proceedings.

**Implementation at Zenith Global Enterprises**:
- Retention of customer correspondence and transaction records relevant to pending or anticipated customs disputes
- Preservation of employee performance records where termination is contested before the Justiça do Trabalho (Labour Courts)

### 7. Protection of Life or Physical Safety (Art. 7, VII)

**Scope**: Processing necessary for the protection of the life or physical safety of the data subject or a third party. This base is reserved for genuine emergency situations where consent cannot reasonably be obtained.

**Implementation at Zenith Global Enterprises**:
- Processing of employee medical emergency information during workplace incidents at Brazilian warehouse facilities
- Sharing driver location data with emergency services during road transport incidents

### 8. Health Protection (Art. 7, VIII)

**Scope**: Processing necessary for the protection of health, exclusively in a procedure carried out by health professionals, health services, or health authorities. This base is narrower than the life protection base and is restricted to health-sector actors.

**Zenith Global Enterprises relevance**: Limited to occupational health processing by the company's contracted occupational medicine providers under Norma Regulamentadora NR-7 (PCMSO).

### 9. Legitimate Interest of the Controller or Third Party (Art. 7, IX)

**Requirements under Art. 10**:
- Processing must be for legitimate purposes based on concrete situations, including:
  - (I) Support and promotion of the controller's activities
  - (II) Protection of the data subject or of the provision of services that benefit the data subject, in connection with the exercise of their rights
- Only strictly necessary data may be processed for the stated purpose
- The controller must adopt transparency measures, including a legitimate interest impact assessment
- If the ANPD requests it, the controller must produce a Relatório de Impacto à Proteção de Dados Pessoais (RIPD) — the LGPD equivalent of a DPIA

**Implementation at Zenith Global Enterprises**:
- Fraud detection on customer payment transactions using pattern analysis
- IT security monitoring of employee network activity to prevent data breaches
- Customer relationship management analytics to improve service quality
- Legitimate interest assessment documented for each use case using the three-part balancing test: (1) legitimate purpose, (2) necessity, (3) balancing against data subject rights

### 10. Credit Protection (Art. 7, X)

**Scope**: Processing for the protection of credit, including credit scoring. This base is unique to the LGPD and has no direct equivalent in the GDPR. It permits processing for credit risk assessment, credit bureau operations, and commercial credit evaluation.

**Implementation at Zenith Global Enterprises**:
- Credit scoring of corporate customers applying for trade credit terms
- Sharing payment history with credit bureaus (Serasa Experian, SPC Brasil, Boa Vista) in compliance with Lei 12.414/2011 (Positive Credit Registry)
- Retention of credit assessment records for the statutory period

## Sensitive Data Processing Under Article 11

Sensitive personal data (dados pessoais sensíveis) includes data on racial or ethnic origin, religious conviction, political opinion, trade union membership, health data, sex life, genetic data, and biometric data (Art. 5, II).

Processing of sensitive data requires one of eight specific bases under Art. 11:
1. Specific and highlighted consent from the data subject
2. Compliance with a legal obligation (without consent)
3. Shared processing by the public administration for public policy execution
4. Research bodies (with anonymisation where possible)
5. Exercise of rights in judicial/administrative/arbitration proceedings
6. Protection of life or physical safety
7. Health protection in medical procedures
8. Fraud prevention and security of the data subject in identification processes

**Key distinction from GDPR**: The LGPD does not include legitimate interest or contract performance as bases for sensitive data processing.

## Data Protection Officer (Encarregado) Requirements

### Appointment (Art. 41)

The controller must appoint a Data Protection Officer (Encarregado pelo Tratamento de Dados Pessoais). ANPD Resolution CD/ANPD No. 2/2022 (amended by Resolution CD/ANPD No. 18/2024) provides that:
- Small-scale processing agents (agentes de tratamento de pequeno porte) may appoint a simplified contact channel instead of a formal DPO
- The DPO's identity and contact information must be publicly disclosed, preferably on the controller's website
- The ANPD may establish additional rules regarding the DPO's qualifications

### DPO Functions (Art. 41, §2)

| Function | Description |
|----------|-------------|
| Receiving complaints | Accept complaints and communications from data subjects and adopt measures |
| Receiving communications from ANPD | Act as the point of contact for the ANPD |
| Advising employees | Guide the controller's employees and contractors regarding data protection practices |
| Performing other duties | Execute other attributions determined by the controller or established by supplementary regulation |

### Zenith Global Enterprises DPO Structure

| Element | Detail |
|---------|--------|
| DPO for Brazil | Maria Fernanda Oliveira, Compliance Director — São Paulo office |
| Public disclosure | Listed on zenithglobal.com.br/privacidade and in the company's Política de Privacidade |
| Contact channel | dpo-brasil@zenithglobal.com — acknowledged within 5 business days |
| Reporting line | Reports directly to the Chief Privacy Officer with a dotted line to the Brazil Country Manager |

## Data Subject Rights (Arts. 17-22)

### Rights Catalogue

| Right | LGPD Article | Response Deadline | Implementation |
|-------|-------------|-------------------|----------------|
| Confirmation of processing | Art. 18, I | Simplified format: immediately or within 15 days; complete format: within 15 days | Automated lookup in data inventory system |
| Access to data | Art. 18, II | Within 15 days | Data export via privacy portal in machine-readable format |
| Correction of incomplete, inaccurate, or out-of-date data | Art. 18, III | Reasonable period | Self-service correction in customer portal; employee corrections through HR system |
| Anonymisation, blocking, or deletion of unnecessary or excessive data | Art. 18, IV | Reasonable period | Automated deletion workflows; manual review for complex cases |
| Data portability | Art. 18, V | Per ANPD regulation | Export in structured JSON/CSV format via privacy portal |
| Deletion of data processed with consent | Art. 18, VI | Reasonable period | Automated purge upon consent withdrawal, subject to legal retention requirements |
| Information about shared data | Art. 18, VII | Within 15 days | Disclosure of third-party recipients from data sharing register |
| Information about consent denial consequences | Art. 18, VIII | At point of collection | Privacy notice includes consequences of not providing consent |
| Revocation of consent | Art. 18, IX | Immediately effective | One-click withdrawal in privacy portal; processing ceases within 24 hours |

### Right to Review Automated Decisions (Art. 20)

The data subject has the right to request review of decisions made solely on the basis of automated processing, including profiling, that affect their interests. The controller must provide clear and adequate information regarding the criteria and procedures used for automated decision-making, subject to commercial and industrial secrecy.

**ANPD Resolution CD/ANPD No. 2/2022** clarified that small-scale processing agents may provide simplified explanations, but all controllers must enable human review upon request.

**Zenith Global Enterprises implementation**:
- Automated credit scoring decisions are flagged for human review upon data subject request
- Credit model criteria documented and available in simplified form for disclosure
- Human reviewer assigned within 5 business days of request receipt

## International Data Transfer Mechanisms (Art. 33)

The LGPD permits international transfer of personal data only under the following conditions:

| Mechanism | LGPD Article | Status |
|-----------|-------------|--------|
| Countries or international organisations with adequate level of protection | Art. 33, I | ANPD has not yet published adequacy decisions as of March 2026 |
| Standard contractual clauses approved by ANPD | Art. 33, II(b) | ANPD Resolution CD/ANPD No. 19/2024 adopted standard contractual clauses effective from August 2025 |
| Global corporate rules (binding corporate rules) | Art. 33, II(c) | ANPD has published draft guidance; formal BCR approval mechanism pending |
| Specific consent for the transfer | Art. 33, VIII | Valid only if the data subject is informed specifically about the international nature of the transfer |
| Compliance with legal or regulatory obligation | Art. 33, IV | Applicable for cross-border regulatory reporting |
| Contract performance or preliminary procedures (at data subject's request) | Art. 33, V | For transfers necessary to execute a contract with the data subject |
| Exercise of rights in judicial/administrative/arbitration proceedings | Art. 33, VI | For litigation support transfers |
| Protection of life or physical safety | Art. 33, VII | Emergency transfers |
| International judicial cooperation | Art. 33, III | For mutual legal assistance |

### Zenith Global Enterprises International Transfer Framework

| Transfer Flow | Destination | Mechanism | Documentation |
|---------------|-------------|-----------|---------------|
| Customer data to EU headquarters | Germany | Standard contractual clauses (ANPD-approved) | SCC register entry BR-EU-001 |
| Employee data to regional HR hub | Singapore | Standard contractual clauses (ANPD-approved) | SCC register entry BR-SG-001 |
| Payment data to payment processor | United States | Specific consent + supplementary measures | Consent records + TIA-BR-US-001 |
| Logistics data to APAC operations | Japan | Standard contractual clauses (ANPD-approved) | SCC register entry BR-JP-001 |

## ANPD Enforcement Framework

### Administrative Sanctions (Art. 52)

| Sanction | Detail |
|----------|--------|
| Warning | With deadline for corrective measures |
| Simple fine | Up to 2% of revenue in Brazil for the private legal entity, group, or conglomerate, per violation, limited to R$50 million per violation |
| Daily fine | To compel compliance, subject to the R$50 million cap |
| Public disclosure of the violation | After confirmation of the occurrence |
| Blocking of personal data | Until regularisation |
| Deletion of personal data | Related to the violation |
| Partial suspension of database operation | For up to 6 months, renewable |
| Suspension of processing activity | For up to 6 months, renewable |
| Partial or total prohibition of processing activities | Most severe sanction |

### ANPD Dosimetry Regulation (Resolution CD/ANPD No. 4/2023)

The ANPD published its dosimetry regulation establishing the methodology for calculating administrative sanctions. Key factors:

| Factor | Weight |
|--------|--------|
| Severity of the violation | High — nature, conditions, and duration of the processing activity |
| Good faith of the violator | Medium — evidence of intent or negligence |
| Economic advantage obtained or intended | High — financial gain from the violation |
| Economic condition of the violator | Medium — ability to pay |
| Recidivism | High — prior violations within 5 years |
| Degree of harm | High — number of data subjects affected and severity of consequences |
| Adoption of good practices and governance | Mitigating — documented privacy programme, DPO appointment, privacy impact assessments |
| Adoption of corrective measures | Mitigating — timely remediation following the violation |
| Proportionality between the violation and the sanction | Balancing factor |

### Notable ANPD Enforcement Actions

**ANPD Administrative Proceeding No. 00261.000489/2022-62 (Telekall Infoservice)**:
- First administrative fine imposed by the ANPD (July 2023)
- Violation: Offering a list of WhatsApp contacts for political campaign messaging without lawful basis
- Sanctions: Warning for failure to appoint a DPO; fine of R$14,400 for processing personal data without a lawful basis
- Significance: Established that even microenterprises must comply with LGPD fundamentals

**ANPD Administrative Proceeding regarding INSS data sharing (2023)**:
- The ANPD investigated the sharing of social security benefit data by the Instituto Nacional do Seguro Social (INSS) with financial institutions
- Resulted in a recommendation to suspend data sharing until appropriate safeguards were implemented
- Significance: Demonstrated ANPD willingness to act against public administration bodies

## LGPD Data Protection Impact Assessment (RIPD)

### When Required

The ANPD may request a Relatório de Impacto à Proteção de Dados Pessoais (RIPD) from the controller under Art. 38. While not mandatory for every processing activity, the RIPD is strongly recommended for:
- Processing based on legitimate interest (Art. 10, §3)
- Processing of sensitive data (Art. 11)
- Processing of children's data (Art. 14)
- Automated decision-making (Art. 20)
- International data transfers (Art. 33)

### RIPD Contents (Art. 38, sole paragraph)

| Element | Description |
|---------|-------------|
| Description of processing activities | Types of data collected, methodology, and processing operations |
| Specific processing purposes | Detailed purpose specification beyond generic descriptions |
| Legal basis | Identification and justification of the applicable Art. 7 or Art. 11 base |
| Data protection measures | Technical and organisational safeguards implemented |
| Risk analysis | Identification and assessment of risks to data subjects |
| Mitigation measures | Steps taken to address identified risks |

### Zenith Global Enterprises RIPD Register

| RIPD Reference | Processing Activity | Legal Basis | Risk Level | Last Updated |
|---------------|---------------------|-------------|------------|-------------|
| RIPD-BR-001 | Customer credit scoring automation | Art. 7, X (credit protection) | High | January 2026 |
| RIPD-BR-002 | Employee biometric access control | Art. 11, I (specific consent) | High | November 2025 |
| RIPD-BR-003 | Marketing analytics profiling | Art. 7, IX (legitimate interest) | Medium | December 2025 |
| RIPD-BR-004 | International transfer to EU headquarters | Art. 33, II(b) (SCCs) | Medium | February 2026 |

## Compliance Programme Implementation Checklist

| Phase | Action | Status | Owner |
|-------|--------|--------|-------|
| 1. Foundation | Appoint Encarregado (DPO) and publish contact details | Complete | Legal Department |
| 1. Foundation | Map all processing activities involving Brazilian personal data | Complete | Privacy Team |
| 1. Foundation | Identify and document lawful basis for each processing activity | Complete | Privacy Team |
| 2. Documentation | Draft and publish Política de Privacidade (Privacy Policy) in Portuguese | Complete | Legal + Marketing |
| 2. Documentation | Implement consent collection mechanism with granular purposes | Complete | IT + Privacy Team |
| 2. Documentation | Create RIPD template aligned with Art. 38 requirements | Complete | Privacy Team |
| 3. Rights Management | Implement data subject rights request portal in Portuguese | Complete | IT Development |
| 3. Rights Management | Establish 15-day response workflow for access/confirmation requests | Complete | Privacy Operations |
| 3. Rights Management | Configure automated deletion workflows with legal hold exceptions | Complete | IT + Legal |
| 4. Transfers | Implement ANPD-approved standard contractual clauses for international transfers | Complete | Legal + Transfer Team |
| 4. Transfers | Document all international transfer flows in the transfer register | Complete | Privacy Team |
| 5. Governance | Conduct annual LGPD compliance audit | Scheduled Q2 2026 | Internal Audit |
| 5. Governance | Train all Brazilian employees on LGPD requirements (annual) | Complete for 2025 | HR + Privacy Team |
| 5. Governance | Establish ANPD regulatory monitoring for new resolutions | Active | Legal + Privacy Team |
