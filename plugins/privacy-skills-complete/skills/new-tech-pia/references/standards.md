# Standards and Regulatory References for New Technology Privacy Impact

## Primary Legislation

### GDPR — Key Provisions for New Technologies
- **Art. 35(1)**: "Where a type of processing in particular using new technologies... is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall... carry out an assessment of the impact."
- **Art. 25(1)**: Data protection by design — "Taking into account the state of the art, the cost of implementation and the nature, scope, context and purposes of processing as well as the risks... the controller shall... implement appropriate technical and organisational measures."
- **Art. 25(2)**: Data protection by default — "The controller shall implement appropriate technical and organisational measures for ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed."
- **Art. 32**: Security of processing — measures must be appropriate to the state of the art and the risks.
- **Recital 91**: Clarifies that DPIAs should be carried out for processing operations involving new technologies where no DPIA has been previously conducted.

### EU AI Act (Regulation 2024/1689)
- Relevant for AI-enabled emerging technologies (AI-powered IoT, ML-based AR/VR, quantum ML).
- Art. 6 and Annex III for high-risk AI classification.

### ePrivacy Directive (2002/58/EC)
- **Art. 5(3)**: Consent required for storing or accessing information on terminal equipment (relevant to IoT devices, AR/VR headsets, wearables).
- **Art. 9**: Location data processing requires consent or anonymisation.

## EDPB and WP29 Guidance

### WP248rev.01 — DPIA Guidelines
- **Criterion 8 (Innovative Technology)**: "The use of a new technology can trigger the need to carry out a DPIA because it can involve novel forms of data collection and usage, possibly with a high risk to individuals' rights and freedoms."
- Combined with any other criterion, innovative technology use presumptively requires a DPIA.

### EDPB Guidelines 02/2023 on Connected Devices (IoT and Wearables)
- IoT devices must comply with data minimisation, purpose limitation, and transparency.
- Consent mechanisms must be adapted to device constraints (no screen, limited interface).
- Data protection by design requires: local processing where possible, encrypted communications, firmware update capability, data portability.

### WP29 Opinion 8/2014 on the Internet of Things
- Identified three IoT ecosystems: wearable computing, quantified self, home automation.
- Key risks: lack of control, insufficient information, quality of consent, profiling, security.
- Recommended: granular consent mechanisms, right to local processing, anonymisation by default.

### CNIL Blockchain Solutions Guidance (2018)
- Personal data should not be stored on-chain in clear text.
- Off-chain storage with on-chain hash references recommended.
- Participants who determine the purposes and means of blockchain-based processing are controllers.
- Miners and node validators are not controllers unless they determine processing purposes.
- Right to erasure: technical measures such as commitment schemes, zero-knowledge proofs, or chameleon hashes may demonstrate reasonable efforts to comply.

## ENISA Publications

### ENISA IoT Security Guidelines (2020)
- Security baseline for IoT devices: secure boot, encrypted communications, authentication, firmware updates.
- Privacy-specific recommendations: data minimisation at the device level, local processing, anonymisation of telemetry.

### ENISA Post-Quantum Cryptography Report (2024)
- Timeline for quantum threat: cryptographically relevant quantum computers estimated within 10-15 years.
- Recommended migration to NIST PQC standards: ML-KEM (lattice-based key encapsulation), ML-DSA (lattice-based digital signature), SLH-DSA (hash-based digital signature).
- "Harvest now, decrypt later" threat requires proactive migration for data with long-term confidentiality requirements.

## ISO/IEC Standards

### ISO/IEC 27030:2024 — IoT Security and Privacy
- Provides guidelines for IoT security and privacy risk assessment.
- Addresses device lifecycle management, data protection, and user notification.

### ISO/IEC 20547-4:2020 — Big Data Reference Architecture Security and Privacy
- Relevant to emerging technologies processing large volumes of personal data.
- Privacy fabric concept: embedding privacy controls throughout the data processing pipeline.

### ISO/IEC 29134:2023 — Privacy Impact Assessment Guidelines
- Technology-agnostic PIA methodology applicable to all emerging technologies.
- Emphasizes the need to assess novel risks that may not be captured by standard risk frameworks.

## Enforcement Precedents

- **Spanish AEPD vs CaixaBank (PS/00098/2020, 2021)**: EUR 6 million fine for deploying advanced behavioural analytics profiling system for customer segmentation without conducting DPIA for innovative technology. The system combined transaction data, location data, and online behaviour to predict financial product preferences.
- **ICO vs Clearview AI (2022)**: GBP 7.5 million fine for facial recognition technology scraping publicly available images to build a biometric database — novel technology with no established regulatory framework at the time of deployment.
- **French CNIL vs Amazon Europe Core (SAN-2020-013, 2020)**: EUR 35 million fine for placing advertising tracking cookies on amazon.fr without valid consent. While cookies are not new technology, the scale and sophistication of the tracking ecosystem constituted innovative technology use.
- **Italian Garante vs Foodinho/Glovo (2021)**: Fine for deploying algorithmic management platform for gig economy workers without DPIA. The platform's AI-driven task allocation, performance scoring, and automated deactivation constituted novel technology use with significant effects on workers.
- **Norwegian DPA vs Grindr (2021)**: EUR 6.5 million (reduced from EUR 10 million on appeal) for sharing precise GPS location data and sexual orientation data with advertising technology partners without valid consent.
