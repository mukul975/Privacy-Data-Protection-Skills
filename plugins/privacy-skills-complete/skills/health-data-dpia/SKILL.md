---
name: health-data-dpia
description: >-
  Guides DPIA for health and medical data processing covering Art. 9(2)(h)-(j)
  exemptions, HIPAA crosswalk for transatlantic operations, clinical trial
  data protection under EU CTR 536/2014, and genetic data specifics under
  Art. 9(1). Activate for healthcare systems, clinical research, health
  apps, or medical device data. Keywords: health data, DPIA, Art. 9,
  clinical trial, genetic data, HIPAA, medical records, special category.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "health-data, dpia, art-9, clinical-trial, genetic-data, hipaa"
---

# Assessing Health Data Processing

## Overview

Health data is classified as a special category under GDPR Art. 9(1), requiring both a lawful basis under Art. 6(1) and an Art. 9(2) exemption for processing. Processing of health data on a large scale triggers a mandatory DPIA under Art. 35(3)(b). This skill provides a DPIA methodology for health data processing scenarios: electronic health records, clinical trials, health research, telemedicine, health applications, medical devices, and genetic data analysis.

## Legal Framework

### Art. 9(1) — Definition of Health Data

GDPR Art. 4(15) defines data concerning health as "personal data related to the physical or mental health of a natural person, including the provision of health care services, which reveal information about his or her health status."

This includes:
- Medical records and diagnoses
- Prescription and medication data
- Laboratory results and imaging
- Mental health assessments
- Disability information
- Genetic data (Art. 4(13))
- Biometric data processed for health purposes
- Health insurance claims
- Fitness and wellness data that reveals health status
- Data inferred from non-health data that reveals health conditions

### Art. 9(2) Exemptions for Health Data

| Exemption | Reference | Application |
|-----------|-----------|-------------|
| Explicit consent | Art. 9(2)(a) | Patient consent for specific health processing. Must be separate from treatment consent. |
| Employment obligations | Art. 9(2)(b) | Occupational health assessments required by employment law. |
| Vital interests | Art. 9(2)(c) | Emergency medical treatment where patient cannot consent. |
| Healthcare provision | Art. 9(2)(h) | Processing necessary for preventive or occupational medicine, medical diagnosis, provision of health or social care, or management of health systems. Must be processed by or under the responsibility of a professional subject to medical secrecy. |
| Public health | Art. 9(2)(i) | Processing necessary for public health purposes including protecting against serious cross-border threats, ensuring high standards of quality and safety of health care, medicinal products, or medical devices. |
| Scientific research | Art. 9(2)(j) | Processing necessary for scientific research purposes (including clinical trials) subject to Art. 89(1) safeguards: data minimisation, pseudonymisation where possible. |

### EU Clinical Trials Regulation 536/2014

- Art. 28: Protection of subjects and informed consent.
- Art. 28(2): Informed consent must be separate from consent for data processing under GDPR.
- Art. 56: Transparency through the EU Clinical Trials Information System.
- Art. 61: Facility requirements including controlled access to clinical trial materials.

## Health Data DPIA Methodology

### Phase 1: Health Data Classification (Week 1)

1. Inventory all health data elements processed.
2. Classify each element:
   - Direct health data (diagnoses, test results, prescriptions)
   - Indirect health data (insurance claims, appointment records)
   - Inferred health data (wellness app data, genetic risk scores)
   - Genetic data (DNA sequences, genotype data, pharmacogenomic data)
3. Identify the Art. 9(2) exemption for each processing activity.
4. Verify that processing is under the responsibility of a health professional subject to professional secrecy (Art. 9(2)(h) and Art. 9(3)).

### Phase 2: Lawful Basis and Exemption Analysis (Week 2)

For each health data processing activity, document:

| Requirement | Documentation |
|-------------|---------------|
| Art. 6(1) lawful basis | Which Art. 6(1)(a)-(f) basis applies |
| Art. 9(2) exemption | Which Art. 9(2)(a)-(j) exemption applies |
| Member State derogation | Whether national law provides additional conditions (Art. 9(4)) |
| Professional secrecy | Whether processing is under a professional subject to secrecy obligation (Art. 9(3)) |
| Data subject consent | If relying on Art. 9(2)(a), evidence of explicit consent separate from treatment consent |

### Phase 3: Clinical Trial Specific Assessment (if applicable)

| Assessment Area | Requirements |
|-----------------|-------------|
| Informed consent | CTR Art. 28 consent separate from GDPR consent; plain language; withdrawal right without impact on treatment |
| Pseudonymisation | Clinical trial data should be pseudonymised with key held by principal investigator; sponsor should not hold re-identification key |
| Data minimisation | Collect only data specified in the clinical trial protocol; no speculative data collection |
| International transfers | Multi-centre trials involve transfers; each transfer requires Chapter V mechanism |
| Retention | CTR Art. 58: sponsor retains trial master file for 25 years; reconcile with GDPR storage limitation |
| Secondary use | Re-use of clinical trial data for future research requires additional ethical approval and GDPR lawful basis |

### Phase 4: HIPAA Crosswalk (for transatlantic operations)

| HIPAA Provision | GDPR Equivalent | Gap Assessment |
|-----------------|-----------------|---------------|
| HIPAA Privacy Rule (45 CFR 164.500-534) | GDPR Art. 5 principles + Art. 9 special categories | GDPR is more restrictive: broader definition of health data; explicit consent standard higher; no Treatment-Payment-Operations (TPO) exception |
| HIPAA Security Rule (45 CFR 164.302-318) | GDPR Art. 32 security of processing | Largely aligned: both require risk assessment, encryption, access controls, audit logging |
| HIPAA Breach Notification (45 CFR 164.400-414) | GDPR Art. 33-34 | GDPR stricter: 72-hour notification to SA; HIPAA allows 60 days |
| HIPAA Minimum Necessary | GDPR Art. 5(1)(c) data minimisation | Aligned in principle; GDPR applies more broadly |
| HIPAA Business Associate Agreement | GDPR Art. 28 DPA | Both require written agreements with processors; GDPR DPA is more prescriptive |
| HIPAA Patient Rights | GDPR Art. 15-22 | GDPR provides broader rights (portability, erasure, restriction, objection) |
| HIPAA De-identification (Safe Harbor / Expert) | GDPR Recital 26 anonymisation | Different standards: HIPAA Safe Harbor has 18 specific identifiers; GDPR requires irreversibility assessment |

### Phase 5: Risk Assessment (Week 3-4)

| Risk | Description | Typical Level |
|------|-------------|--------------|
| HD-R1 | Health data breach exposing sensitive diagnoses, conditions, or genetic information | Very High |
| HD-R2 | Re-identification of pseudonymised health data through linkage with other datasets | High |
| HD-R3 | Discriminatory use of genetic data (insurance denial, employment discrimination) | High |
| HD-R4 | Unauthorised access by healthcare staff beyond clinical need-to-know | High |
| HD-R5 | Secondary use of clinical trial data without participant awareness | Medium |
| HD-R6 | Cross-border transfer of health data to jurisdictions with weaker protections | High |
| HD-R7 | Patient re-identification through aggregation of fitness/wellness app data | Medium |

### Phase 6: Genetic Data Specifics

Genetic data has unique privacy characteristics:
- **Perpetual sensitivity**: Genetic information does not change over a lifetime and reveals information about biological relatives.
- **Familial implications**: An individual's genetic data reveals information about parents, siblings, and children who have not consented to processing.
- **Predictive power**: Genetic data can predict future health conditions, creating insurance and employment discrimination risks.
- **Irreversibility**: Once genetic data is disclosed, it cannot be "unlearned" or reset.

Additional requirements for genetic data:
- Art. 9(4) permits Member States to impose further conditions on genetic data processing.
- Germany: Gendiagnostikgesetz (GenDG) imposes strict limitations on genetic testing in employment and insurance contexts.
- France: Code de la sante publique Art. L1131-1 restricts genetic testing to medical and scientific purposes.

## Enforcement Precedents

- **Finnish DPA vs Pihlajalinna (2021)**: EUR 608,000 fine for health services company where employees accessed patient records without clinical justification — inadequate access controls and logging.
- **Portuguese DPA vs Hospital do Barreiro (2018)**: EUR 400,000 fine for hospital where non-clinical staff had access to patient records through failure to implement role-based access controls.
- **Dutch DPA vs OLVG Hospital (2021)**: EUR 440,000 fine for inadequate access controls on electronic patient records — insufficient two-factor authentication and logging of access.
- **Swedish DPA vs Capio St. Goran (2020)**: SEK 30 million fine for hospital failing to conduct DPIA for patient records system and failing to implement adequate access controls.
- **ICO vs Pharmacy2U (2015)**: GBP 130,000 fine for selling patient data to marketing companies without consent.
