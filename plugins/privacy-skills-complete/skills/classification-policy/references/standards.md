# Standards and Regulatory References — Data Classification Policy

## Primary Legislation

### GDPR — Regulation (EU) 2016/679

- **Article 5(1)(f)**: Integrity and confidentiality principle — personal data shall be processed in a manner that ensures appropriate security, including protection against unauthorised or unlawful processing and against accidental loss, destruction, or damage.
- **Article 24**: Responsibility of the controller — implement appropriate technical and organisational measures to ensure and be able to demonstrate that processing is performed in accordance with the GDPR. Data classification is a foundational organisational measure.
- **Article 25**: Data protection by design and by default — classification policies implement by-design principles by ensuring data sensitivity drives the selection of technical measures.
- **Article 32**: Security of processing — risk-based security measures "taking into account the state of the art, costs, nature, scope, context, purposes, and risks." Classification enables risk-proportionate security.

## International Standards

### ISO/IEC 27001:2022 — Information Security Management Systems

- **Annex A.5.12**: Classification of information — information shall be classified in terms of legal requirements, value, criticality, and sensitivity to unauthorised disclosure or modification.
- **Annex A.5.13**: Labelling of information — appropriate set of procedures for information labelling shall be developed and implemented in accordance with the information classification scheme.
- **Annex A.5.10**: Acceptable use of information — rules for acceptable use and handling of information shall be identified, documented, and implemented.

### ISO/IEC 27002:2022 — Information Security Controls

- **Control 5.12 Guidance**: Classification scheme should consider confidentiality (unauthorised disclosure), integrity (unauthorised modification), and availability. Four levels are common: public, internal, confidential, restricted.
- **Control 5.13 Guidance**: Labels should be applied to physical and digital assets. Automated labelling tools recommended for large-scale environments.

### NIST SP 800-60 — Guide for Mapping Types of Information and Information Systems to Security Categories

- **Volume I**: Foundation for categorising information based on impact levels (low, moderate, high) across confidentiality, integrity, and availability.
- **Relevance**: Provides a complementary approach to GDPR-focused classification, useful for organisations operating in both EU and US regulatory environments.

### NIST SP 800-88 Rev.1 — Guidelines for Media Sanitization

- **Clear**: Logical techniques to sanitise data in all user-addressable storage locations. Suitable for Confidential tier.
- **Purge**: Physical or logical techniques that render target data recovery infeasible. Required for Restricted tier.
- **Destroy**: Physical destruction rendering media unusable. Required for highest-sensitivity Restricted data.

## Regulatory Guidance

### ICO — Security Outcomes (2023)

- **Outcome A.3**: "You classify and manage information assets according to their sensitivity." The ICO explicitly includes data classification as a security measure controllers must implement.

### EDPB Guidelines 01/2021 on Examples of Data Breach Notification

- **Section 3**: Multiple examples where failure to classify data by sensitivity contributed to breach impact — data treated with uniform (insufficient) security measures.
