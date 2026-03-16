---
name: pia-health-data
description: >-
  Conducts Privacy Impact Assessment for health data processing under GDPR
  Article 9, HIPAA, and sector-specific health privacy regulations. Covers
  special category data safeguards, clinical research data, patient portals,
  health wearables, genetic data, and cross-border health data transfers.
  Keywords: health data PIA, DPIA, Article 9, HIPAA, special category data,
  clinical research, patient privacy, genetic data.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "pia, health-data, article-9, hipaa, special-category, clinical-research"
---

# Privacy Impact Assessment for Health Data

## Overview

Health data processing triggers mandatory DPIA requirements under GDPR Article 35(3)(b) (processing on a large scale of special categories of data referred to in Article 9(1)). The EDPB in WP248rev.01 identifies health data processing as meeting multiple DPIA-triggering criteria: special category data (C5), vulnerable data subjects (C7), and often innovative use or applying new technological or organisational solutions (C8). This skill provides a structured PIA methodology specific to health data processing across clinical, research, wearable, and digital health contexts.

## Regulatory Framework

### GDPR Article 9 — Special Category Data

Health data falls within the special categories of personal data under Article 9(1). Processing is prohibited unless one of the Article 9(2) exceptions applies:

| Exception | Application to Health Data |
|-----------|--------------------------|
| Art. 9(2)(a) Explicit consent | Patient consent for clinical care beyond treatment necessity; health app consent |
| Art. 9(2)(b) Employment obligations | Occupational health assessments, fitness-to-work evaluations |
| Art. 9(2)(c) Vital interests | Emergency medical treatment when data subject cannot consent |
| Art. 9(2)(h) Health care provision | Medical diagnosis, treatment, health system management by health professionals under secrecy obligations |
| Art. 9(2)(i) Public health | Epidemiological surveillance, disease registries, pharmacovigilance |
| Art. 9(2)(j) Scientific research | Clinical trials, health research with appropriate safeguards under Art. 89(1) |

### HIPAA Privacy Rule (US)

The HIPAA Privacy Rule (45 CFR Part 160, 164) governs the use and disclosure of Protected Health Information (PHI) by covered entities (health plans, health care clearinghouses, health care providers) and business associates. Key privacy requirements include:

- Minimum necessary standard for PHI use and disclosure
- Individual access rights to PHI within 30 days
- Accounting of disclosures of PHI
- De-identification standards: Expert Determination (45 CFR 164.514(b)(1)) and Safe Harbor (45 CFR 164.514(b)(2))
- Business Associate Agreements (BAAs) for third-party processors

### Sector-Specific Regulations

| Regulation | Scope |
|-----------|-------|
| EU Clinical Trials Regulation (536/2014) | Personal data in clinical trial conduct and reporting |
| UK Data Protection Act 2018 Schedule 1 | Health data processing conditions for UK-based organisations |
| 42 CFR Part 2 (US) | Substance use disorder treatment records — stricter than HIPAA |
| HITECH Act (US) | Breach notification requirements for health data; strengthened HIPAA enforcement |
| eHealth Network guidelines | Cross-border exchange of health data within the EU |

## Health Data Processing Scenarios

### 1. Electronic Health Records (EHR)

**Data elements**: Medical history, diagnoses, medications, lab results, imaging, clinician notes, patient demographics.
**Key risks**: Unauthorised access by non-treating staff, insufficient access controls, data retention beyond clinical necessity, secondary use for research without consent or legal basis.
**Mitigation**: Role-based access control, audit logging, break-glass procedures with post-access review, encryption at rest and in transit, purpose-bound access policies.

### 2. Clinical Research

**Data elements**: Study participant identifiers, health measurements, biospecimens, genomic data, adverse event reports.
**Key risks**: Re-identification from research datasets, consent scope creep (using data beyond original study purpose), international transfers to non-adequate jurisdictions.
**Mitigation**: Pseudonymisation with key separation, Data Access Committees, informed consent with granular options, data sharing agreements with re-identification prohibitions.

### 3. Health Wearables and mHealth Apps

**Data elements**: Heart rate, blood pressure, sleep patterns, activity levels, glucose levels, medication adherence, location data.
**Key risks**: Continuous monitoring creating comprehensive health profiles, data sharing with third-party advertisers, insufficient user control over data, insecure data transmission.
**Mitigation**: Privacy by design (on-device processing where possible), granular consent for data sharing, transparency about all data recipients, secure API design, data minimisation.

### 4. Genetic and Genomic Data

**Data elements**: DNA sequence data, genetic test results, family health history, polygenic risk scores.
**Key risks**: Uniquely identifying and irrevocable (cannot be changed), impacts on biological relatives who did not consent, insurance and employment discrimination, law enforcement access.
**Mitigation**: Purpose limitation (prohibit use for insurance underwriting or employment decisions where legally required), access restrictions, separate storage from clinical records, genetic counselling before data collection.

## DPIA Methodology for Health Data

### Phase 1: Processing Inventory (Week 1)

1. Identify all health data processing activities and map data flows.
2. Classify health data by sensitivity tier: routine clinical data, sensitive diagnoses (mental health, HIV, substance use), genetic/genomic data.
3. Identify all data processors and sub-processors handling health data.
4. Verify Business Associate Agreements (HIPAA) or Data Processing Agreements (GDPR) are in place.
5. Document the lawful basis and Article 9(2) exception for each processing activity.

### Phase 2: Necessity and Proportionality (Week 2)

1. For each processing activity, assess whether the purpose could be achieved with less data.
2. Evaluate anonymisation or pseudonymisation alternatives.
3. Assess data retention periods against clinical, legal, and research requirements.
4. Review access controls: principle of least privilege, need-to-know basis.
5. Evaluate whether aggregate or statistical data could serve the purpose instead of individual-level health data.

### Phase 3: Risk Assessment (Week 3)

1. Assess risks to data subjects from each processing activity.
2. Apply the severity factors: sensitivity of health condition (stigma, discrimination risk), vulnerability of data subjects (patients, children, elderly), volume of records, identifiability.
3. Assess likelihood factors: threat landscape (insider threats, ransomware targeting health sector), control maturity, regulatory scrutiny.
4. Score risks on the standard likelihood x severity matrix.

### Phase 4: Mitigation and Controls (Week 4)

1. For each identified risk, define technical and organisational measures.
2. Implement health-sector-specific controls: clinical audit trails, break-glass access, pseudonymisation key management, encrypted backup.
3. Assess residual risk after mitigation.
4. If residual risk remains high, consider prior consultation with the supervisory authority (Art. 36) or abandoning the processing activity.

### Phase 5: Documentation and Review (Week 5)

1. Document the DPIA in the required format (Art. 35(7)): systematic description of processing, necessity and proportionality assessment, risk assessment, measures to address risks.
2. Obtain sign-off from DPO, Caldicott Guardian (UK NHS), Chief Medical Information Officer, or equivalent.
3. Schedule periodic review (at least annually for health data processing, or on trigger events).
4. File with supervisory authority if required (prior consultation).

## Enforcement Precedents

- **Finnish DPA vs Pihlajalinna (2021)**: EUR 608,000 fine for inadequate access controls to patient records in a private healthcare company; employees accessed patient records without clinical justification.
- **Dutch DPA vs OLVG Hospital (2021)**: EUR 440,000 fine for insufficient access controls to patient medical records; inadequate two-factor authentication and insufficient log review.
- **Portuguese DPA vs Hospital do Barreiro (2018)**: EUR 400,000 fine for excessive access to patient data; 985 users had profiles allowing access to clinical information, but only 296 were physicians.
- **Swedish DPA vs Capio St Goran Hospital (2020)**: EUR 30,000 fine for insufficient access controls and logging in EHR system.
- **HHS OCR vs Anthem Inc (2018)**: USD 16 million HIPAA settlement for data breach affecting 78.8 million individuals due to insufficient access controls and risk analysis.
