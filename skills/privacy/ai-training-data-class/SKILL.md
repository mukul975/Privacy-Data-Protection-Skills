---
name: ai-training-data-class
description: >-
  Classifies sensitive data in AI/ML training datasets including bias detection
  for Art. 9 categories, data card documentation, provenance tracking, and
  consent verification for model training. Keywords: AI training data, ML
  dataset, bias detection, data card, model training, Art 9, consent, GDPR AI.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-classification
  tags: "ai-training-data, ml-dataset, bias-detection, data-card, model-training, gdpr-ai"
---

# Sensitive Data Classification for AI/ML Training Datasets

## Overview

AI and machine learning models trained on personal data raise distinct classification challenges. Training data may contain direct personal data, inferred special categories, proxy variables for protected characteristics, and data whose consent scope does not extend to model training. The EU AI Act (Regulation (EU) 2024/1689) imposes additional requirements for high-risk AI systems, including data governance obligations under Art. 10 that intersect with GDPR classification requirements. This skill provides a framework for classifying training data, detecting bias-relevant features, documenting data provenance, and verifying consent coverage.

## GDPR and AI Act Intersection

### GDPR Requirements for Training Data

| GDPR Article | Application to AI Training |
|-------------|--------------------------|
| **Art. 5(1)(b) — Purpose limitation** | Training a model is a distinct processing purpose; if data was collected for customer service, using it for ML training requires a compatible purpose assessment or new lawful basis |
| **Art. 5(1)(c) — Data minimisation** | Training datasets must not include more personal data than necessary for the model objective |
| **Art. 6 — Lawful basis** | Model training requires its own lawful basis; legitimate interests (Art. 6(1)(f)) is most common, but requires LIA documentation |
| **Art. 9 — Special categories** | If training data contains or enables inference of special category data, Art. 9(2) condition required |
| **Art. 22 — Automated decision-making** | If the trained model makes decisions with legal or significant effects, additional safeguards apply |
| **Art. 25 — Data protection by design** | Classification of training data is a by-design measure enabling appropriate technical protections |
| **Art. 35 — DPIA** | High-risk AI processing (profiling, automated decision-making) requires DPIA |

### EU AI Act Art. 10 — Data Governance for High-Risk AI

The AI Act Art. 10 requires that training, validation, and testing datasets for high-risk AI systems:

1. Are subject to appropriate data governance and management practices (Art. 10(2))
2. Are relevant, sufficiently representative, and to the extent possible free of errors and complete (Art. 10(3))
3. Take into account the specific geographical, contextual, behavioural, or functional setting within which the AI system is intended to be used (Art. 10(4))
4. Where special category data processing is strictly necessary for bias detection and correction, this is permitted under Art. 10(5), subject to appropriate safeguards including pseudonymisation and GDPR compliance

## Training Data Classification Framework

### Classification Tier 1: Personal Data Content

| Classification | Description | Example |
|---------------|-------------|---------|
| **TRAINING_PII_DIRECT** | Dataset contains direct identifiers | Customer names, email addresses in NLP training corpus |
| **TRAINING_PII_INDIRECT** | Dataset contains indirect identifiers | Customer IDs, transaction patterns enabling singling out |
| **TRAINING_SPECIAL_CAT** | Dataset contains Art. 9 special category data | Health records for medical diagnosis model |
| **TRAINING_CRIMINAL** | Dataset contains Art. 10 criminal data | Fraud transaction labels derived from criminal investigations |
| **TRAINING_PSEUDONYMISED** | Personal data replaced with tokens but re-identification key exists | Pseudonymised customer data with mapping held by data team |
| **TRAINING_ANONYMISED** | Data verified as anonymised per WP29 criteria | Aggregated population statistics with k ≥ 10 |
| **TRAINING_SYNTHETIC** | Artificially generated data with no real personal data | GAN-generated synthetic transaction data |
| **TRAINING_NON_PERSONAL** | No personal data content | Market price data, weather data, product specifications |

### Classification Tier 2: Bias and Proxy Detection

Even when a dataset does not directly contain Art. 9 special category data, it may contain proxy variables that correlate with protected characteristics:

| Proxy Variable | Correlated Protected Characteristic | Detection Method |
|---------------|-------------------------------------|-----------------|
| **Postcode/ZIP code** | Racial/ethnic origin, socioeconomic status | Geographic demographic analysis |
| **First name** | Gender, ethnic origin, age cohort | Name demographics database lookup |
| **Language preference** | Ethnic origin, nationality | Statistical correlation analysis |
| **Shopping patterns** | Religious belief (halal/kosher purchases), health status | Purchase category analysis |
| **Web browsing history** | Political opinions, sexual orientation, health status | Topic modelling on browsing categories |
| **Employment gap patterns** | Gender (maternity), disability, health | Statistical pattern analysis |
| **Credit score** | Racial/ethnic origin (documented correlation in US/UK studies) | Disparate impact analysis |

### Classification Tier 3: Consent and Purpose Scope

| Classification | Description | Compliance Requirement |
|---------------|-------------|----------------------|
| **CONSENT_COVERS_TRAINING** | Original consent explicitly covers AI/ML training | Document consent text and verify specificity |
| **CONSENT_DOES_NOT_COVER** | Original consent did not anticipate ML training | New consent required or alternative lawful basis needed |
| **LEGITIMATE_INTEREST** | ML training relies on legitimate interests (Art. 6(1)(f)) | Documented LIA required |
| **CONTRACT_PERFORMANCE** | ML training is necessary for contract performance | Narrow scope — must be genuinely necessary |
| **PUBLIC_DATA** | Data sourced from publicly available sources | Still requires lawful basis; public availability is not a lawful basis |
| **RESEARCH_EXEMPTION** | Processing under Art. 89(1) research exemption | Appropriate safeguards including pseudonymisation required |

## Data Card Documentation

A data card is a structured document accompanying each training dataset, providing transparency about its contents, provenance, and limitations. Modelled on the "Datasheets for Datasets" framework (Gebru et al., 2021) and adapted for GDPR compliance.

### Required Data Card Fields for Vanguard Financial Services

| Section | Fields |
|---------|--------|
| **1. Dataset Identity** | Name, version, creation date, owner, purpose |
| **2. Personal Data Classification** | Tier 1 classification, data elements present, classification labels |
| **3. Data Subjects** | Categories of data subjects, volume, geographic scope |
| **4. Provenance** | Original collection purpose, source systems, processing chain from collection to training set |
| **5. Consent/Lawful Basis** | Tier 3 classification, consent text reference or LIA reference, purpose compatibility assessment |
| **6. Special Category Assessment** | Whether Art. 9 data is present (direct or inferred), Art. 9(2) condition if applicable |
| **7. Bias Assessment** | Proxy variables identified, disparate impact analysis results, demographic representation statistics |
| **8. De-identification** | Technique applied (pseudonymisation, anonymisation, synthetic generation), assessment reference |
| **9. Retention** | Training data retention period, model retention period, deletion schedule |
| **10. Access Controls** | Who can access the training data, who can access the model, audit logging |
| **11. DPIA Reference** | DPIA document reference if applicable |
| **12. Limitations** | Known biases, geographic limitations, temporal limitations, data quality issues |

## Bias Detection Methodology

### Step 1: Demographic Representation Analysis

For each training dataset, calculate representation statistics:
- What percentage of records come from each demographic group (to the extent known)?
- Does the representation match the target population?
- Are any groups under-represented by more than 20% relative to population?

### Step 2: Proxy Variable Identification

Scan all features for proxy correlation with Art. 9 protected characteristics:
- Calculate correlation coefficient between each feature and known protected characteristics (where available)
- Flag features with |correlation| > 0.3 as potential proxies
- Document all proxy variables in the data card

### Step 3: Disparate Impact Analysis

For classification or scoring models:
- Calculate model performance metrics by demographic group
- Apply the 80% (four-fifths) rule: if the selection rate for any protected group is less than 80% of the rate for the most favoured group, disparate impact may exist
- Document disparate impact analysis results in the data card

### Step 4: AI Act Art. 10(5) Assessment

If bias detection requires processing special category data:
- Document why processing is "strictly necessary" for bias detection and correction
- Implement pseudonymisation of the special category data used for bias testing
- Ensure GDPR Art. 9(2) condition is established (typically Art. 9(2)(g) substantial public interest or Art. 9(2)(j) research)
- Process in a controlled environment with access restricted to the bias assessment team
- Delete special category data after bias assessment is complete

## Enforcement and Regulatory Precedents

- **Italian Garante — Clearview AI (2022)**: EUR 20 million fine for processing biometric data scraped from public sources for AI facial recognition training without lawful basis, consent, or transparency. Established that public availability does not provide lawful basis for AI training.
- **Italian Garante — ChatGPT/OpenAI (2023)**: Temporary ban and subsequent enforcement requiring OpenAI to establish lawful basis for training data collection, implement age verification, and provide opt-out mechanisms. Highlighted that AI training on personal data requires GDPR compliance throughout the data lifecycle.
- **CNIL — Enforcement Notice on AI Training Data (2024)**: CNIL published guidance sheets on AI training data requiring purpose limitation assessment, proportionality analysis, and specific measures when training data contains special category data.
- **ICO — Generative AI and Data Protection Consultation (2024)**: ICO's position that legitimate interests is the most likely lawful basis for AI training but requires documented LIA considering data subject reasonable expectations.

## Integration Points

- **personal-data-test**: Training data must first be classified as personal or non-personal
- **special-category-data**: Art. 9 data in training sets requires heightened protections
- **pseudo-vs-anon-data**: De-identification of training data must be validated
- **classification-policy**: Training data classified under enterprise classification tiers
- **data-lineage-tracking**: Full provenance from original collection to model deployment must be tracked
