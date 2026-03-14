# Standards and Regulatory References — South Korea PIPA

## Primary Legislation

### Personal Information Protection Act (PIPA, 개인정보 보호법)
- **Original enactment**: Act No. 10465, 29 September 2011
- **Major amendment (Data Three Acts)**: Effective 5 August 2020 — consolidated enforcement under PIPC; introduced pseudonymisation framework
- **2023 Amendment**: Effective 15 September 2023 — introduced legitimate interest basis, cross-border transfer reform, automated decision rights, data portability
- **Scope**: Applies to all data handlers (개인정보처리자) processing personal information in South Korea

### Enforcement Decree of PIPA (Presidential Decree)
- **Most recent revision**: 2023, aligned with PIPA amendments
- **Key provisions**: Detailed consent requirements (Art. 17); technical and organisational safeguards standards (Arts. 30-48); cross-border transfer notification content (Art. 28-9)

### Act on Promotion of Information and Communications Network Utilisation and Information Protection (Network Act)
- **Relevance**: Previously the primary data protection law for telecommunications and internet service providers; personal information provisions largely migrated to PIPA in 2020
- **Remaining provisions**: Network security obligations; spam regulation; online advertising transparency

### Credit Information Use and Protection Act (Credit Information Act)
- **Relevance**: Governs personal credit information processing; includes MyData (data portability) framework for financial sector
- **Key provisions**: Credit information handlers must comply with PIPA and additional sector-specific requirements; Financial Services Commission (FSC) enforces alongside PIPC

## PIPC Guidance and Standards

### PIPC Personal Information Processing Guidelines (2023, revised)
- Comprehensive guidance on PIPA compliance for all data handlers
- Detailed interpretation of consent requirements, lawful processing bases, data subject rights
- Guidance on the legitimate interest basis introduced by the 2023 amendments

### PIPC Pseudonymisation Guidelines (2020, revised 2022)
- Detailed methodology for pseudonymisation under Arts. 28-2 to 28-7
- Risk-based approach to determining adequate pseudonymisation level
- Examples of acceptable pseudonymisation techniques: generalisation, suppression, noise addition, permutation, tokenisation

### PIPC Standard Personal Information Protection Guidelines
- Practical implementation guidance for data handlers
- Model privacy notices and consent forms
- Personal information file registration procedures

### PIPC Cross-Border Transfer Standard Contractual Clauses (2024)
- Published pursuant to Art. 28-8(1)(4) of the 2023 amended PIPA
- Structure: Data handler obligations, recipient obligations, data subject rights, remedies
- Filing with the PIPC within 30 days of execution

## International Framework

### EU Adequacy Decision for South Korea (17 December 2021)
- **Commission Implementing Decision (EU) 2021/2238**
- **Scope**: PIPA, PIPC enforcement, supplementary rules for data transferred from the EU
- **Supplementary rules**: Additional protections for EU personal data transferred to Korea, including limitations on processing sensitive information and enhanced enforcement cooperation with EU DPAs
- **Review**: Subject to periodic review (first review scheduled for 2025)

### APEC CBPR Certification
- South Korea is a participant in the APEC Cross-Border Privacy Rules (CBPR) system
- Korean Information Security Agency (KISA) designated as the accountability agent
- CBPR certification available as an additional cross-border transfer mechanism

## Enforcement Precedents

### PIPC v. Meta Platforms (September 2022)
- Fine: KRW 30.8 billion (USD ~22 million)
- Violation: Collecting sensitive information (political views, sexual orientation, religious beliefs) from approximately 3.3 million Facebook users without consent; sharing with third-party advertisers
- Corrective measures: Cease collection and use of sensitive information without proper consent

### PIPC v. Kakao (2023)
- Fine: KRW 15.1 billion
- Violation: Processing personal information beyond consented purposes for targeted advertising
- Significance: Demonstrated enforcement against Korea's largest domestic internet platform

### PIPC v. Scatter Lab (Lee Luda chatbot, 2021)
- Fine: KRW 103 million
- Violation: Training AI chatbot on 9.4 billion personal conversation messages without consent
- Significance: First PIPC enforcement action specifically addressing AI training data

### PIPC v. Google (2022)
- Fine: KRW 69.2 billion (USD ~50 million)
- Violation: Collecting and combining location data without transparent consent mechanisms
- Significance: Joint investigation with other agencies; demonstrated PIPC global enforcement reach

## Technical Standards

### KISA Personal Information Technical Safeguards Standards
- Encryption requirements: Resident registration numbers, financial account numbers, biometric data must be encrypted in storage and transmission
- Access control: Role-based access; multi-factor authentication for administrative access
- Logging: Minimum 2-year retention of access logs; review at least semi-annually
- Destruction: Irreversible deletion methods specified for electronic and physical media

### Korean Information Security Management System (ISMS-P)
- Combined information security and personal information protection certification
- Mandatory for certain sectors (telecommunications, medical, education above thresholds)
- Voluntary for other data handlers but demonstrates PIPA compliance
- Certification body: KISA

## PIPA vs GDPR Key Differences

| Feature | PIPA | GDPR |
|---------|------|------|
| Supervisory authority | PIPC (single authority) | Multiple DPAs (lead authority mechanism) |
| Legitimate interest | Introduced 2023 (Art. 15(1)(6)) | Available since 2018 (Art. 6(1)(f)) |
| Pseudonymisation framework | Detailed statutory framework (Arts. 28-2 to 28-7) | Defined but no dedicated processing basis |
| Consent requirements | Highly prescriptive (font size, separate boxes) | Principle-based (freely given, specific, informed, unambiguous) |
| Criminal penalties | Yes — imprisonment up to 5 years | No (administrative fines only in GDPR; Member State criminal law varies) |
| Penalty surcharge | Up to 3% of related revenue | Up to 4% of global annual turnover |
| Breach notification | 72 hours to PIPC for 1,000+ individuals | 72 hours to DPA for all breaches likely to result in risk |
| Data destruction deadline | Within 5 days of purpose fulfilment | Without undue delay (no specific day count) |
| Resident registration number | Special protection category with encryption mandate | No equivalent concept |
