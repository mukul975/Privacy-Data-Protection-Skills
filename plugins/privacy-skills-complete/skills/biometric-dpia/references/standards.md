# Standards and Regulatory References for Biometric Processing Privacy

## Primary Legislation

### GDPR
- **Art. 4(14)**: Definition of biometric data.
- **Art. 9(1)**: Prohibition on processing biometric data for unique identification.
- **Art. 9(2)(a)-(j)**: Exemptions from the prohibition.
- **Art. 35(3)(b)**: Mandatory DPIA for large-scale processing of Art. 9(1) data.
- **Art. 35(3)(c)**: Mandatory DPIA for systematic monitoring of publicly accessible areas (relevant to facial recognition CCTV).
- **Recital 51**: Clarifies that photographs are not systematically considered biometric data unless specifically technically processed to uniquely identify a person.

### EU AI Act (Regulation 2024/1689)
- **Art. 5(1)(d)**: Prohibition on real-time remote biometric identification in publicly accessible spaces for law enforcement (with exceptions for serious crime, terrorism, missing persons).
- **Art. 5(1)(e)**: Prohibition on untargeted scraping of facial images from the internet or CCTV for biometric databases.
- **Art. 5(1)(f)**: Prohibition on emotion recognition in workplace and education (except medical/safety).
- **Art. 6 + Annex III(1)**: High-risk classification for AI systems intended for remote biometric identification (not real-time) and biometric categorisation.
- **Art. 26(10)**: Deployers of high-risk biometric AI systems must conduct a DPIA per GDPR Art. 35.

## EDPB and WP29 Guidance

### EDPB Guidelines 3/2019 on Processing of Personal Data Through Video Devices (Adopted 29 January 2020)
- Section 5: Specific provisions for video surveillance with facial recognition.
- Facial recognition for access control: Art. 9(2)(a) explicit consent or Art. 9(2)(b) employment law basis required. Consent must be freely given — a non-biometric alternative must be available.
- Storage: biometric templates should be stored on a medium controlled by the data subject (smart card, mobile device) rather than a central database.
- Necessity: controller must demonstrate that biometric access control is necessary and that a less intrusive alternative (badge, PIN, card) would not achieve the same purpose.

### EDPB Guidelines 05/2022 on Facial Recognition Technology in Law Enforcement (Adopted 12 May 2022)
- Emphasised strict necessity and proportionality for law enforcement facial recognition.
- Recommended prohibition of facial recognition in publicly accessible spaces except for strictly defined exceptions.
- Required DPIA for all law enforcement facial recognition deployments.

### WP29 Opinion 3/2012 on Developments in Biometric Technologies
- Established that biometric data processing creates higher privacy risks than other personal data.
- Recommended data protection by design for biometric systems.
- Identified key risks: irreversibility, function creep, discrimination, surveillance.

## National Legislation

### France — CNIL
- **CNIL Guidance on Biometric Access Control in the Workplace (2019)**: Established three levels of biometric storage: (1) individual device held by employee (least intrusive); (2) centralised database with strong justification; (3) raw biometric data retention (prohibited except in exceptional circumstances).
- **French Labour Code Art. L1121-1**: Restrictions on biometric processing must be justified and proportionate to the aim pursued.

### Germany — Federal and State Law
- **BDSG Section 26**: Employee biometric data processing only permitted when necessary for the employment relationship and proportionate.
- Various state data protection laws impose additional restrictions on biometric surveillance.

### United Kingdom
- **Data Protection Act 2018 Schedule 1 Part 1**: Biometric data processing for unique identification requires an appropriate policy document under the substantial public interest condition.
- **ICO Employment Practices Code (updated 2023)**: Biometric monitoring in the workplace must be necessary, proportionate, and subject to DPIA.

## ISO/IEC Standards for Biometric Systems

### ISO/IEC 19795-1:2021 — Biometric Performance Testing and Reporting
- Defines metrics: False Acceptance Rate (FAR), False Rejection Rate (FRR), Failure to Enrol Rate (FTE), Failure to Acquire Rate (FTA).
- Methodology for biometric accuracy evaluation.

### ISO/IEC 30107-1:2023 — Presentation Attack Detection
- Framework for evaluating biometric system resistance to spoofing attacks.
- Classification of presentation attack instruments (printed photos, 3D masks, artificial fingerprints).

### ISO/IEC 24745:2022 — Biometric Information Protection
- Template protection techniques: cancellable biometrics, biometric encryption, biometric cryptosystems.
- Storage security requirements for biometric templates.
- Irreversibility and unlinkability requirements for protected templates.

### ISO/IEC 19794 series — Biometric Data Interchange Formats
- Standardised formats for fingerprint (19794-2), face (19794-5), iris (19794-6), and other biometric modalities.

## Enforcement Decisions

- **CNIL vs Clearview AI (SAN-2022-019, 2022)**: EUR 20 million fine for scraping publicly available facial images to build biometric database. No consent, no transparency, no DPIA. Ordered deletion of French residents' data.
- **ICO vs Clearview AI (2022)**: GBP 7.5 million fine. Same processing as CNIL decision. Enforcement notice requiring deletion of UK residents' data.
- **Swedish DPA vs Skelleftea Municipality (DI-2019-2221, 2019)**: SEK 200,000 fine for facial recognition attendance system in school. Student consent was not freely given due to imbalance of power. DPIA conducted but found insufficient.
- **ICO vs Serco Leisure (2022)**: Enforcement notice for deploying facial recognition time-and-attendance for leisure centre employees. No DPIA conducted. No alternative offered to employees. Disproportionate use of biometric data for attendance tracking.
- **French Conseil d'Etat vs Presto (2020)**: Upheld CNIL position that biometric time-and-attendance (fingerprint scanner) for employees was disproportionate where badge-based alternatives existed.
- **AEPD vs Mercadona (PS/00120/2021, 2021)**: EUR 2.5 million fine for deploying facial recognition in supermarkets to identify shoplifters without adequate DPIA, without valid legal basis, and without demonstrating that less intrusive measures were insufficient.
- **Italian Garante vs Iren Energia (2022)**: Order to cease fingerprint-based attendance system for employees; found disproportionate to the purpose of attendance tracking.
