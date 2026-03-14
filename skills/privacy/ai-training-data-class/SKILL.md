---
name: ai-training-data-class
description: >-
  Classifies sensitive data in AI/ML training datasets including bias detection
  for Art. 9 special categories, data card documentation, provenance tracking,
  and consent verification for model training. Keywords: AI training data, ML
  dataset classification, bias detection, data card, provenance, consent, Art 9.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-classification
  tags: "ai-training-data, ml-dataset, bias-detection, data-card, provenance, consent"
---

# AI/ML Training Data Classification

## Overview

AI and machine learning models are only as good — and as compliant — as their training data. When training datasets contain personal data, GDPR obligations apply in full to the training process, model storage, and inference outputs. When training data includes Art. 9 special categories, the risks multiply: biased models can perpetuate discrimination, inferred attributes can constitute new special category processing, and the inability to exercise erasure rights against trained models creates novel compliance challenges. This skill provides a framework for classifying, documenting, and governing training data for AI/ML systems in compliance with GDPR.

## Regulatory Framework for AI Training Data

### GDPR Obligations Applicable to ML Training

| Obligation | Application to Training Data | Vanguard Implication |
|-----------|-----------------------------|--------------------|
| **Art. 5(1)(a) Lawfulness** | A lawful basis is required for each use of personal data in training | Cannot train on customer data collected for service delivery if training is a new, incompatible purpose |
| **Art. 5(1)(b) Purpose limitation** | Training is a specific purpose; must be compatible with original collection purpose or have independent basis | Legitimate interests assessment or consent required for ML training distinct from original purpose |
| **Art. 5(1)(c) Data minimisation** | Only personal data necessary for effective model training should be used | Feature selection must exclude unnecessary personal attributes |
| **Art. 5(1)(d) Accuracy** | Training data must be accurate; biased or inaccurate training data produces biased models | Data quality assessment required before training |
| **Art. 5(1)(e) Storage limitation** | Training data should not be retained longer than necessary for the training purpose | Post-training retention justification required |
| **Art. 6 Lawful basis** | At least one Art. 6(1) basis for using personal data to train the model | Most commonly: Art. 6(1)(f) legitimate interests (with balancing test) or Art. 6(1)(a) consent |
| **Art. 9 Special categories** | If training data contains or model infers Art. 9 data, Art. 9(2) condition required | Bias detection must identify special category features and proxies |
| **Art. 13/14 Transparency** | Data subjects must be informed their data is used for ML training | Privacy notice must specify AI/ML training as a purpose |
| **Art. 17 Right to erasure** | Erasure requests must be addressed; may require model retraining or unlearning | Machine unlearning strategy or retraining pipeline required |
| **Art. 22 Automated decisions** | If model output produces legal or significant effects, Art. 22 rights apply | Human oversight required for consequential decisions |
| **Art. 35 DPIA** | ML training on personal data at scale likely triggers mandatory DPIA | DPIA required for all ML models using personal data |

### EU AI Act — Regulation (EU) 2024/1689

The EU AI Act (entered into force 1 August 2024) establishes specific requirements for training data:

- **Art. 10**: Data and data governance — training, validation, and testing datasets must be relevant, sufficiently representative, and as free of errors as possible. Must examine for biases that may affect health, safety, or lead to discrimination.
- **Art. 10(5)**: Processing of special categories for bias monitoring — permits processing of Art. 9 special categories "to the extent that is strictly necessary" for ensuring bias detection and correction, subject to appropriate safeguards.
- **Annex IV**: Technical documentation must include information about training data, including data provenance, collection methods, and preparation steps.

## Training Data Classification Framework

### Classification Dimensions

| Dimension | Categories | Assessment Method |
|-----------|-----------|-----------------|
| **Personal data content** | Contains personal data / No personal data / Uncertain | PII scanning (see auto-data-discovery, pii-in-unstructured) |
| **Special category presence** | Contains Art. 9 data / Art. 9 proxies / No Art. 9 data | Feature analysis + proxy detection |
| **Criminal data presence** | Contains Art. 10 data / No Art. 10 data | Criminal data scan (see criminal-data-handling) |
| **Consent status** | Consent obtained / Consent not required / Consent unknown | Consent audit trail verification |
| **Bias risk** | High / Medium / Low | Statistical fairness assessment |
| **Provenance** | First-party collected / Third-party sourced / Public data / Synthetic | Data lineage documentation |
| **Data quality** | High / Medium / Low | Accuracy, completeness, timeliness assessment |

### Art. 9 Special Category Detection in Training Features

Direct special category features are obvious (gender, ethnicity, religion fields). The greater risk is **proxy features** — attributes that correlate with protected characteristics:

| Protected Category | Common Proxy Features | Detection Method |
|-------------------|---------------------|-----------------|
| Racial/ethnic origin | Postcode/ZIP code, surname, language preference | Correlation analysis with census demographic data |
| Political opinions | Media consumption patterns, donation history | Topic modelling on text features |
| Religious beliefs | Dietary preferences, holiday patterns, geographic clusters | Association rule mining |
| Health status | Insurance claim patterns, absence records, purchase history (pharmacy) | Feature importance analysis against health outcome proxies |
| Sexual orientation | Household composition, partner benefits, name analysis | Inference risk assessment |
| Age | Graduation year, employment history length, technology usage patterns | Correlation with age data where available |

### Bias Detection Methodology

#### Statistical Fairness Metrics

For each protected group (defined by Art. 9 categories or proxies):

| Metric | Definition | Threshold |
|--------|-----------|-----------|
| **Demographic parity** | P(positive outcome \| group A) ≈ P(positive outcome \| group B) | Ratio within 0.8-1.25 (80% rule) |
| **Equalised odds** | True positive rate and false positive rate equal across groups | Difference < 5 percentage points |
| **Calibration** | For a given predicted probability, actual outcome rate is similar across groups | Maximum calibration gap < 10% |
| **Counterfactual fairness** | Changing the protected attribute (and its causal descendants) does not change the prediction | Prediction change < 5% |

## Data Card Documentation

Every ML training dataset at Vanguard must have a Data Card documenting:

### Required Data Card Fields

| Section | Required Content |
|---------|-----------------|
| **Dataset overview** | Name, version, creation date, owner, purpose |
| **Composition** | Record count, feature count, label distribution, temporal coverage |
| **Personal data classification** | PII categories present, Art. 9 data present, Art. 10 data present |
| **Collection process** | How data was collected, from whom, under what notice/consent |
| **Provenance** | Original data source, transformations applied, chain of custody |
| **Lawful basis** | Art. 6 basis for training use, Art. 9(2) condition if applicable |
| **Consent status** | Whether data subjects consented to ML training use specifically |
| **Bias assessment** | Protected categories identified, proxy features flagged, fairness metrics |
| **Pre-processing** | Anonymisation, pseudonymisation, feature selection, outlier handling |
| **Quality metrics** | Accuracy, completeness, consistency, timeliness of the data |
| **Representativeness** | Demographic distribution vs. target population, coverage gaps |
| **Known limitations** | Known biases, underrepresented groups, quality issues |
| **Retention** | How long training data is retained, deletion schedule |
| **Access controls** | Who can access the training data, under what conditions |
| **DPIA reference** | Reference to the DPIA covering this training activity |
| **Review schedule** | When the data card is next reviewed |

## Provenance Tracking Requirements

### Chain of Custody Documentation

For each training dataset, maintain:

```
Original Source → Collection → Transformation → Training → Model → Inference
     │                │              │              │          │
     ▼                ▼              ▼              ▼          ▼
  Source ID      Collection      Transform     Training    Model version
  Data owner     method          log           date        Inference
  Legal basis    Date            Features      Hyperparams outputs
  Consent        Volume          selected      Accuracy    Decisions
  status         Quality check   Bias check    Bias eval   affected
```

### Consent Verification Workflow

Before using personal data for ML training:

1. **Identify the original collection purpose** — was ML training specified or compatible?
2. **Check consent scope** — if consent-based, does consent cover ML training?
3. **Assess purpose compatibility** — if legitimate interests, is training compatible under Art. 6(4)?
4. **Verify Art. 9 conditions** — if special category data, is there a valid Art. 9(2) basis for training?
5. **Document the assessment** — record in the data card

## Implementation at Vanguard Financial Services

### ML Models Currently in Use

| Model | Training Data | Personal Data | Art. 9 Risk | Status |
|-------|-------------|---------------|-------------|--------|
| Credit risk scoring | Customer financial history, repayment patterns | YES — financial data, account activity | MEDIUM — postcode proxy for ethnicity | Data card completed, DPIA done |
| Fraud detection (transactions) | Transaction patterns, merchant data, device data | YES — behavioural patterns, IP addresses | LOW — no direct Art. 9 features | Data card completed, DPIA done |
| Customer churn prediction | Service usage, complaint history, demographics | YES — age, postcode, usage patterns | MEDIUM — age and postcode proxies | Data card completed, bias review pending |
| AML suspicious activity | Transaction patterns, counterparty data, geographic risk | YES — transaction data, geographic data | MEDIUM — geographic features may proxy nationality | Data card completed, DPIA done |
| Document classification (NLP) | Historical customer correspondence | YES — names, account details in text | HIGH — health data may appear in complaints | Remediation required — PII scrubbing needed |

## Enforcement Precedents and Guidance

- **Italian DPA (Garante) v Clearview AI (2022)**: EUR 20 million fine — scraped biometric data from social media for facial recognition training without lawful basis, consent, or transparency
- **ICO v Clearview AI (2022)**: GBP 7.5 million fine (reduced from 17M on appeal) — processing UK citizens' images for AI training without lawful basis
- **EDPB Guidelines 06/2023 on AI and GDPR**: Processing personal data for AI training requires a lawful basis; legitimate interests requires careful balancing test considering the intrusiveness of the training and the data subjects' reasonable expectations
- **CNIL Guidance on AI and Personal Data (2024)**: Detailed guidance on applying GDPR to AI model training, including consent requirements, legitimate interests balancing, purpose limitation for training data reuse, and data minimisation in feature engineering

## Integration Points

- **special-category-data**: Art. 9 detection in training features and proxy identification
- **auto-data-discovery**: Automated scanning of training datasets for PII
- **pii-in-unstructured**: Detection of PII in unstructured training data (text corpora, images)
- **pseudo-vs-anon-data**: Assessment of whether training data anonymisation is adequate
- **data-lineage-tracking**: Provenance chain documentation for training data
