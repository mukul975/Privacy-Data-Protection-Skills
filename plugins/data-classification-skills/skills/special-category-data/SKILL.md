---
name: special-category-data
description: >-
  Identifies and classifies GDPR Art. 9 special category data including racial
  origin, political opinions, religious beliefs, trade union membership, genetic,
  biometric, health, and sexual orientation data. Covers processing conditions
  under Art. 9(2)(a)-(j). Keywords: special category, Art 9, sensitive data,
  biometric, genetic, health data, explicit consent.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-classification
  tags: "special-category, art-9, sensitive-data, biometric, genetic, health-data"
---

# Special Category Data Classification — GDPR Art. 9

## Overview

Article 9(1) of the GDPR establishes a general prohibition on processing special categories of personal data. These categories were identified by the European legislature as carrying heightened risk to fundamental rights and freedoms due to their potential for discrimination, social stigma, or irreversible harm. Processing is permitted only when one of the ten conditions in Art. 9(2)(a)-(j) is satisfied, in addition to a valid lawful basis under Art. 6. This skill provides a systematic framework for identifying special category data across enterprise systems and mapping each instance to an appropriate processing condition.

## The Eight Special Categories — Art. 9(1)

### Category 1: Racial or Ethnic Origin

**Definition**: Data revealing or from which racial or ethnic origin can be inferred, including direct declarations, photographs, names characteristic of particular ethnic groups, or nationality data when used as a proxy for ethnic origin.

**Examples at Vanguard Financial Services**:
- Employee self-identification forms for diversity monitoring
- Customer photographs in KYC documentation
- Nationality fields when used to infer ethnicity
- Language preference data when combined with geographic data to infer origin

**Boundary Cases**:
- Nationality alone is not necessarily racial/ethnic origin data, but becomes special category when processed for diversity analysis (EDPB, WP251rev.01)
- Photographs are special category only when processed through facial recognition for the purpose of uniquely identifying — a passport photo stored for KYC is not biometric data, but the same photo run through facial comparison software becomes biometric data

### Category 2: Political Opinions

**Definition**: Data revealing political views, party membership, voting behaviour, political donations, or participation in political activities.

**Examples at Vanguard Financial Services**:
- Employee political donation records (where legally collected for compliance with US PAC reporting requirements)
- Customer complaints referencing political views
- Social media data processed for marketing that reveals political affiliations

**Key Precedent**: Austrian Post (Österreichische Post AG) — Austrian DPA and subsequently CJEU Case C-300/21 (2023) — fined EUR 18 million for processing political affinity scores derived from statistical models applied to demographic data. The CJEU confirmed that data revealing political opinions includes inferred data, not only data directly provided by the data subject.

### Category 3: Religious or Philosophical Beliefs

**Definition**: Data revealing religious faith, atheism, agnosticism, philosophical convictions, or related practices. Includes dietary preferences when they indicate religious observance (halal, kosher), religious holiday requests, and membership of religious organisations.

**Examples at Vanguard Financial Services**:
- Employee religious holiday accommodation requests
- Dietary restriction data for corporate event catering
- Charitable donation patterns to religious organisations (from transaction data)

### Category 4: Trade Union Membership

**Definition**: Data revealing whether an individual is or was a member of a trade union. Includes union dues deductions from payroll, attendance at union meetings, and communications with union representatives.

**Examples at Vanguard Financial Services**:
- Payroll deduction records for union dues
- HR records of union membership status
- Meeting room booking records for union activities

### Category 5: Genetic Data — Art. 4(13)

**Definition**: Personal data relating to the inherited or acquired genetic characteristics of a natural person which give unique information about the physiology or health of that natural person, resulting in particular from an analysis of a biological sample from the natural person in question.

**Examples at Vanguard Financial Services**:
- Genetic test results in employee wellness programs (if offered)
- Insurance underwriting data derived from genetic testing (prohibited in many jurisdictions)
- Biobank research data from corporate health initiatives

**Regulatory Note**: The Genetic Information Nondiscrimination Act (GINA) in the US prohibits use of genetic information in health insurance and employment. In the EU, genetic data receives dual protection under both Art. 9 and specific Member State genetic data legislation.

### Category 6: Biometric Data — Art. 4(14)

**Definition**: Personal data resulting from specific technical processing relating to the physical, physiological, or behavioural characteristics of a natural person, which allow or confirm the unique identification of that natural person, such as facial images or dactyloscopic data.

**Critical Distinction**: Biometric data is special category ONLY when processed "for the purpose of uniquely identifying a natural person" (Art. 9(1)). A photograph stored in an HR file is personal data but not special category. The same photograph processed through facial recognition software for access control is special category biometric data.

**Examples at Vanguard Financial Services**:
- Fingerprint scanners for building access control
- Facial recognition for secure facility entry
- Voice recognition for telephone banking authentication
- Behavioural biometrics (keystroke dynamics) for fraud detection

**Key Precedent**: Clearview AI — CNIL Decision SAN-2022-019 (20 October 2022) — EUR 20 million fine for processing biometric data (facial recognition) without lawful basis and without conducting DPIA.

### Category 7: Health Data — Recital 35

**Definition**: Personal data related to the physical or mental health of a natural person, including the provision of health care services, which reveal information about their health status. Recital 35 specifies this includes data pertaining to the health status of a data subject which reveals information relating to the past, current, or future physical or mental health of the data subject, including: registration for health care services, number/symbol/identifier assigned for health purposes, information derived from testing or examination of a body part or bodily substance, and any information on a disease, disability, disease risk, medical history, clinical treatment, or physiological or biomedical condition.

**Examples at Vanguard Financial Services**:
- Employee sick leave records and medical certificates
- Disability accommodation requests
- Occupational health assessment results
- Health insurance claims data
- Wellness program participation data (step counts, health metrics)
- COVID-19 vaccination status records
- Drug and alcohol testing results
- Ergonomic assessment data indicating physical conditions

**Breadth of Health Data**: The CJEU has interpreted health data broadly. In Case C-184/20 (Vyriausioji tarnybinės etikos komisija, 2022), the Court held that data which indirectly reveals health information (such as a spouse's name in a declaration of interests that could reveal sexual orientation or health status) may constitute special category data.

### Category 8: Sex Life or Sexual Orientation

**Definition**: Data concerning sexual behaviour, sexual preferences, or sexual orientation. Includes data from which sexual orientation can be inferred.

**Examples at Vanguard Financial Services**:
- Employee diversity monitoring data including sexual orientation
- Beneficiary designations that reveal same-sex partnerships
- Customer data from which sexual orientation can be inferred (partner names, household composition)

## Processing Conditions — Art. 9(2)(a)-(j)

Processing of special category data is lawful ONLY when one of these conditions is met (in addition to Art. 6 lawful basis):

| Condition | Art. 9(2) | Requirements | Vanguard Application |
|-----------|-----------|-------------|---------------------|
| **Explicit consent** | (a) | Must be freely given, specific, informed, unambiguous, and EXPLICIT (higher standard than Art. 6(1)(a) consent). Must be a clear affirmative statement, not implied. | Employee diversity monitoring with opt-in explicit consent |
| **Employment and social security law** | (b) | Processing necessary for obligations under employment, social security, or social protection law. Must be authorised by EU or Member State law or collective agreement with appropriate safeguards. | Payroll processing of trade union dues, occupational health assessments required by law |
| **Vital interests** | (c) | Processing necessary to protect vital interests where data subject is physically or legally incapable of giving consent. | Emergency medical situations where employee is incapacitated |
| **Legitimate activities of non-profit** | (d) | Processing by foundation, association, or not-for-profit body with political, philosophical, religious, or trade union aims, relating to members or regular contacts, with no disclosure outside the body without consent. | Not applicable to Vanguard (commercial entity) |
| **Data manifestly made public** | (e) | Data subject has manifestly made the data public (e.g., publicly declared political views on social media, public disclosure of health condition). | Customer data voluntarily posted on public forums |
| **Legal claims** | (f) | Processing necessary for establishment, exercise, or defence of legal claims, or whenever courts are acting in their judicial capacity. | Litigation holds involving health data in employment disputes |
| **Substantial public interest** | (g) | Processing necessary for reasons of substantial public interest, on basis of EU or Member State law, proportionate to the aim, with appropriate safeguards. | Regulatory reporting obligations (e.g., AML suspicious activity involving special category data) |
| **Health care and occupational medicine** | (h) | Processing necessary for preventive or occupational medicine, assessment of working capacity, medical diagnosis, health/social care provision, or management of health systems. Must be processed by or under responsibility of a professional with secrecy obligation. | Occupational health surveillance mandated by workplace health regulations |
| **Public health** | (i) | Processing necessary for public health reasons such as protection against serious cross-border threats to health, ensuring high standards of quality and safety for medicines/medical devices. | COVID-19 workplace safety measures (now largely wound down) |
| **Archiving, research, statistics** | (j) | Processing necessary for archiving in the public interest, scientific or historical research, or statistical purposes under Art. 89(1), with appropriate safeguards including data minimisation. | Internal workforce diversity statistical analysis |

## Identification Methodology

### Automated Detection Indicators

| Indicator Type | Detection Approach | Special Category Flag |
|---------------|-------------------|---------------------|
| Field names containing health terminology | Regex pattern matching: `diagnosis|symptom|medical|patient|prescription|allergy|disability|illness|treatment|vaccine` | Health data |
| ICD-10/ICD-11 codes | Code format detection: `[A-Z][0-9]{2}(\.[0-9]{1,4})?` | Health data |
| Biometric template formats | Binary header detection for ISO 19795, ANSI/INCITS 378 fingerprint templates | Biometric data |
| Diversity form fields | Field labels matching: `ethnicity|race|religion|orientation|gender_identity|union_member` | Multiple categories |
| Genetic marker identifiers | SNP identifiers (rs-numbers), gene names (HUGO nomenclature) | Genetic data |

### Manual Review Triggers

Processing activities that warrant manual special category review:
1. Any processing involving employee HR data (may contain health, union, diversity data)
2. Customer onboarding with identity verification (photographs may become biometric)
3. Marketing analytics using behavioural profiling (may infer political views, health status)
4. Insurance or benefits processing (health data inherent)
5. AI/ML training using customer or employee data (risk of inferring special categories)

## Data Protection Impact Assessment Requirement

Under Art. 35(3)(b), processing special category data on a large scale automatically triggers a mandatory DPIA. For Vanguard Financial Services:

| Processing Activity | Scale Assessment | DPIA Required? |
|--------------------|-----------------|---------------|
| Employee health records | 12,000 employees — large scale for employer | YES |
| Fingerprint access control | All office buildings, 8,500 users | YES |
| Customer KYC photographs | 2.4 million customers | YES (if facial recognition applied) |
| Diversity monitoring survey | Voluntary, ~3,000 respondents | YES (special category + employment context) |

## Enforcement Precedents

- **Österreichische Post AG (Austrian DPA / CJEU C-300/21, 2023)**: EUR 18 million fine for processing inferred political affinity scores. Established that data need not be directly provided by the data subject to constitute special category data — statistical inference suffices.
- **Clearview AI (CNIL SAN-2022-019, 2022)**: EUR 20 million fine for biometric data processing without lawful basis or DPIA.
- **Asociación Profesional Elite Taxi v Uber Systems Spain (CJEU C-434/15, 2017)**: While primarily an internal market case, the opinion addressed processing of driver data that could reveal trade union membership.
- **Hungarian NAIH (2021)**: Fined a retailer HUF 100 million for processing employee health data (COVID-19 test results) beyond the scope authorised by public health legislation.
- **Swedish DPA (2019)**: Fined a school SEK 200,000 for using facial recognition (biometric data) for student attendance tracking without valid legal basis under Art. 9(2).

## Integration Points

- **personal-data-test**: Special category classification presupposes personal data classification — Art. 9 applies only to data that is first personal data under Art. 4(1)
- **criminal-data-handling**: Art. 10 criminal data has separate rules but is often processed alongside special categories
- **classification-policy**: Special category designation drives the highest classification tier (Restricted)
- **data-inventory-mapping**: Art. 30 RoPA must identify special category data per processing activity
