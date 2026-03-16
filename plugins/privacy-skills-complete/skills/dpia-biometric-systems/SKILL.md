---
name: dpia-biometric-systems
description: >-
  Conducts Data Protection Impact Assessments for biometric identification
  and authentication systems under GDPR Article 35 and Article 9 special
  category rules. Covers facial recognition, fingerprint, iris scanning,
  voice recognition, and behavioural biometrics. Applies EDPB Guidelines
  3/2019, CNIL Reglement Type Biometrie, and ISO/IEC 24745 biometric
  template protection. Keywords: DPIA biometric, facial recognition,
  fingerprint, Art. 35, Art. 9, biometric template, special category.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "dpia-biometric, facial-recognition, fingerprint, art-35, art-9, biometric-template"
---

# DPIA for Biometric Systems

## Overview

Biometric data processing for uniquely identifying natural persons falls under GDPR Article 9(1) special category data and triggers a mandatory DPIA under Article 35(3)(b) — "processing on a large scale of special categories of data." The European Data Protection Board (EDPB) Guidelines on DPIA list biometric processing as an inherently high-risk activity requiring assessment regardless of scale. This skill provides a structured DPIA methodology specifically designed for biometric identification and authentication systems.

## When a DPIA Is Mandatory for Biometric Systems

Under EDPB WP248rev.01, a DPIA is required when processing meets two or more criteria from the nine-factor list. Biometric systems commonly trigger:

| EDPB Criterion | Biometric Relevance |
|----------------|---------------------|
| Special category data (Criterion 4) | Biometric data under Art. 9(1) when used for unique identification |
| Systematic monitoring (Criterion 3) | Facial recognition CCTV, continuous gait analysis |
| Large-scale processing (Criterion 5) | Organisation-wide deployment of fingerprint scanners |
| Innovative technology (Criterion 8) | Behavioural biometrics, emotion detection, multimodal biometrics |
| Vulnerable data subjects (Criterion 7) | Employees (power imbalance), children, patients |
| Automated decision-making (Criterion 2) | Biometric-based access decisions without human review |

National DPA blacklists universally include biometric processing:
- **CNIL (France)**: Deliberation 2018-327, List 11 — Biometric processing for identification
- **ICO (UK)**: DPIA required for biometric data processing at any scale
- **AEPD (Spain)**: List includes biometric processing for access control
- **BfDI (Germany)**: All biometric employee processing requires DPIA

## DPIA Assessment Structure

### Section 1: Processing Description (Art. 35(7)(a))

Document the biometric system in detail:

**System Architecture**:
- Biometric modality: fingerprint, facial recognition, iris, voice, behavioural, or multimodal
- Capture device specifications: sensor type, resolution, liveness detection capability
- Template extraction algorithm: vendor, version, ISO/IEC 19795 compliance
- Template storage: on-device (token/badge), local server, centralised database, cloud
- Matching architecture: 1:1 verification or 1:N identification
- Integration points: access control, time and attendance, HR systems, CCTV

**Data Flows**:
- Raw biometric data capture (image, audio, behavioural signal)
- Feature extraction and template creation
- Template storage location and encryption
- Matching and decision process
- Audit logging
- Template deletion and lifecycle

**Data Subjects and Scale**:
- Number of enrolled individuals
- Number of daily biometric transactions
- Categories of data subjects (employees, visitors, contractors, customers)
- Vulnerable groups affected (employees with power imbalance, children)

### Section 2: Necessity and Proportionality (Art. 35(7)(b))

**Lawful Basis Assessment**:

| Basis | Art. 6(1) | Art. 9(2) | Assessment |
|-------|-----------|-----------|------------|
| Consent | Art. 6(1)(a) | Art. 9(2)(a) | Problematic for employees (power imbalance); may be valid for voluntary customer opt-in |
| Legal obligation | Art. 6(1)(c) | Art. 9(2)(b) | Valid where national law mandates biometric verification (nuclear facilities, pharmaceutical production) |
| Legitimate interest | Art. 6(1)(f) | Not available | Art. 9(2) does not include legitimate interest; must pair with another Art. 9(2) condition |
| Public interest | Art. 6(1)(e) | Art. 9(2)(g) | Valid for border control, law enforcement with Member State law basis |
| Employment law | Art. 6(1)(b) | Art. 9(2)(b) | Valid where national employment law authorises biometric processing with appropriate safeguards |

**Necessity Test**:
1. Define the specific, concrete purpose (not "security" but "controlling access to pharmaceutical clean room")
2. Demonstrate that biometric processing achieves the purpose more effectively than alternatives
3. Document why less intrusive alternatives are insufficient (badge sharing documented incidents, PIN security breaches)
4. Confirm processing is limited to what is necessary (no function creep, no secondary uses)

**Proportionality Assessment**:
- Severity of the security risk vs. intrusiveness of biometric processing
- Scope: targeted deployment (specific areas/roles) vs. blanket deployment
- Alternative non-biometric method available for those who object
- Safeguards proportionate to the heightened risk of special category data

### Section 3: Risk Identification and Assessment (Art. 35(7)(c))

**Biometric-Specific Risk Categories**:

| Risk ID | Risk Category | Description | Typical Severity |
|---------|--------------|-------------|-----------------|
| BIO-R1 | Template breach | Unauthorised access to biometric template database; unlike passwords, biometric characteristics cannot be changed | Very High |
| BIO-R2 | Function creep | Biometric data collected for access control repurposed for monitoring, emotion detection, or performance tracking | High |
| BIO-R3 | Discrimination | Biometric system accuracy varies by demographic group (skin tone, age, disability), causing disproportionate false rejections | High |
| BIO-R4 | Covert collection | Facial recognition or behavioural biometrics collected without active data subject participation or awareness | High |
| BIO-R5 | Cross-system linkage | Biometric templates matched across unrelated systems enabling tracking beyond original purpose | Very High |
| BIO-R6 | Spoofing and fraud | Biometric data used to create synthetic representations (deepfakes, artificial fingerprints) | High |
| BIO-R7 | Chilling effect | Employees alter behaviour due to awareness of biometric monitoring, impacting freedom of expression and association | Medium |
| BIO-R8 | Irrevocability | Compromised biometric data cannot be reset like a password; lifetime impact on data subjects | Very High |

### Section 4: Mitigation Measures (Art. 35(7)(d))

**Technical Safeguards**:

| Measure | Standard Reference | Implementation |
|---------|-------------------|----------------|
| Biometric template protection | ISO/IEC 24745:2022 | Cancelable biometrics or biometric encryption ensuring templates cannot be reverse-engineered to raw data |
| On-device template storage | CNIL Reglement Type Biometrie | Templates stored on employee-held badges/tokens; no centralised database |
| Liveness detection | ISO/IEC 30107 | Anti-spoofing measures: 3D depth sensing, pulse detection, challenge-response |
| Encryption at rest | AES-256 minimum | All biometric templates and audit logs encrypted |
| Encryption in transit | TLS 1.3 | All biometric data transmission between capture device and matching engine |
| Template irreversibility | ISO/IEC 24745 Section 6 | One-way transformation ensuring raw biometric cannot be reconstructed |
| System isolation | Network segmentation | Biometric systems on dedicated VLAN, no internet connectivity |
| Audit logging | Immutable logs | All enrolment, matching, and administrative access events logged |

**Organisational Safeguards**:

| Measure | Implementation |
|---------|----------------|
| DPIA review cycle | Annual reassessment or upon system change |
| Alternative access method | Non-biometric alternative (PIN + badge) available for all data subjects |
| Employee objection procedure | Formal objection mechanism with no adverse consequences |
| Deletion upon termination | Biometric templates deleted within 24 hours of employment termination |
| Access restriction | Biometric database access limited to named security administrators with MFA |
| Vendor due diligence | Biometric vendor assessed for Art. 28 compliance, subprocessor chain, international transfers |
| Training | All operators trained on biometric system operation and data protection obligations |
| Incident response | Specific breach procedure for biometric data compromise including notification of irrevocability risk |

## DPO Consultation Requirements

Under Art. 35(2), the controller shall seek the advice of the DPO when carrying out a DPIA. For biometric systems, the DPO should specifically assess:

1. Whether the Art. 9(2) exception is robustly established
2. Whether the necessity test has been rigorously applied
3. Whether less intrusive alternatives have been genuinely evaluated (not dismissed pro forma)
4. Whether the proposed safeguards are adequate for the heightened risk
5. Whether Art. 36 prior consultation with the supervisory authority is required

## Art. 36 Prior Consultation Triggers

If the DPIA concludes that residual risk remains high after all mitigation measures, the controller must consult the supervisory authority under Art. 36(1) before commencing processing. For biometric systems, prior consultation is typically required when:

- Large-scale facial recognition is deployed in public or semi-public spaces
- Biometric processing involves vulnerable populations (children, patients) without explicit legal basis
- Centralised biometric database stores templates for more than 10,000 individuals
- Biometric system operates in 1:N identification mode across multiple sites
- No adequate alternative to biometric processing can be provided for objecting individuals

## Integration Points

- **Employee Biometric Data**: Detailed guidance on biometric processing in employment (see employee-biometric-data skill)
- **DPIA Risk Scoring**: Risk scoring methodology for DPIA findings (see dpia-risk-scoring skill)
- **DPIA Mitigation Plan**: Structured mitigation planning (see dpia-mitigation-plan skill)
- **DPIA Stakeholder Consult**: Data subject consultation requirements (see dpia-stakeholder-consult skill)
- **Employee Monitoring DPIA**: Broader employee monitoring assessment (see employee-monitoring-dpia skill)
