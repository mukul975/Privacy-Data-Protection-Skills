---
name: ai-dpia
description: >-
  Conducts Data Protection Impact Assessments for AI and ML systems per EDPB
  Guidelines 04/2025 on AI processing. Covers training data lawfulness
  evaluation, model risk assessment, automated decision triggers, and AI-specific
  DPIA methodology. Keywords: AI DPIA, machine learning impact assessment,
  EDPB AI guidelines, model risk, training data.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "ai-dpia, machine-learning, edpb-guidelines, model-risk, training-data, impact-assessment"
---

# Data Protection Impact Assessment for AI/ML Systems

## Overview

AI and ML systems present unique privacy challenges that traditional DPIA methodologies fail to adequately address. The EDPB Guidelines 04/2025 on processing personal data through AI systems establish a specialized framework that supplements the general DPIA requirements of GDPR Article 35 and WP248rev.01. AI-specific DPIAs must evaluate the entire ML pipeline — from training data collection through model deployment and inference — assessing risks that emerge from statistical learning, emergent model behaviours, and the opacity of algorithmic decision-making. This skill implements the EDPB's AI-specific DPIA methodology integrated with the EU AI Act risk classification framework.

## AI-Specific DPIA Triggers

### Mandatory DPIA Triggers for AI Systems

All AI processing that meets any of the following criteria requires a DPIA before deployment:

| Trigger | Legal Basis | Description |
|---------|-------------|-------------|
| AI-based profiling with legal effects | Art. 35(3)(a) GDPR | ML models that produce decisions with legal or similarly significant effects on natural persons (credit scoring, hiring, insurance pricing) |
| Training on special category data | Art. 35(3)(b) GDPR | Models trained on health, biometric, genetic, racial, political, religious, sexual orientation, or trade union data at scale |
| AI-powered surveillance | Art. 35(3)(c) GDPR | Computer vision, facial recognition, behavioural analytics, or anomaly detection in public spaces |
| High-risk AI systems | Art. 6 EU AI Act | Systems listed in Annex III of the AI Act (biometric identification, critical infrastructure, employment, law enforcement, migration, justice) |
| Foundation models processing personal data | EDPB Guidelines 04/2025 | LLMs and foundation models trained on datasets containing personal data, regardless of downstream use |
| Automated inference of sensitive attributes | EDPB Guidelines 04/2025 | Models that infer Art. 9 special category data from non-sensitive inputs (inferring health status from purchasing patterns) |

### EDPB WP248 Criteria Applied to AI

AI systems frequently trigger multiple WP248 criteria simultaneously:

- **Evaluation/scoring**: Inherent to classification and regression models
- **Automated decision-making**: Core function of deployed AI systems
- **Innovative technology**: Novel model architectures, training techniques
- **Large-scale processing**: Training datasets containing millions of records
- **Matching/combining datasets**: Multi-source training data aggregation
- **Vulnerable data subjects**: When AI is applied to children, employees, patients

When an AI system meets two or more criteria, a DPIA is presumptively required.

## AI DPIA Methodology — EDPB Framework

### Phase 1: AI System Description (Art. 35(7)(a) Extended)

The systematic description must cover the complete AI lifecycle:

#### 1.1 Training Phase Documentation

- **Training data sources**: Origin, collection method, consent status, lawful basis for each dataset
- **Data categories**: All personal data categories present in training data, including data that may be inadvertently included (background individuals in images, metadata in text corpora)
- **Data volume**: Number of records, data subjects affected, geographic scope
- **Data preprocessing**: Cleaning, augmentation, labelling processes and any human review
- **Feature engineering**: Which personal data attributes are used as features, how derived features are computed
- **Training infrastructure**: Where training occurs (cloud provider, jurisdiction), data residency during training

#### 1.2 Model Architecture Documentation

- **Model type**: Neural network architecture (transformer, CNN, RNN), ensemble methods, decision trees
- **Model parameters**: Number of parameters, model size, complexity indicators
- **Explainability characteristics**: Inherent interpretability level (white-box, grey-box, black-box)
- **Memorization risk**: Assessed propensity for the model to memorize training data (higher for large models with small datasets)

#### 1.3 Deployment Phase Documentation

- **Inference inputs**: What personal data is processed at inference time
- **Output types**: Classifications, scores, recommendations, generated content
- **Decision pipeline**: How model outputs feed into decisions affecting data subjects
- **Human oversight**: Level and effectiveness of human review in the decision chain
- **Monitoring**: Drift detection, performance monitoring, feedback loops

### Phase 2: AI-Specific Necessity and Proportionality

#### 2.1 Purpose Limitation for AI

- Is the AI system necessary for the stated purpose, or could simpler processing achieve it?
- Has the controller evaluated non-AI alternatives and documented why AI is required?
- Are the training data processing purposes compatible with the original collection purposes (Art. 6(4) assessment)?
- For repurposed data: has a compatibility assessment been conducted per EDPB Guidelines 04/2025?

#### 2.2 Data Minimisation for AI

- Has the minimum dataset required for acceptable model performance been determined through ablation studies?
- Can synthetic data, federated learning, or differential privacy reduce the personal data requirement?
- Are there personal data elements in the training data that do not contribute to model performance?
- Has the controller assessed whether anonymised or pseudonymised data could achieve adequate performance?

#### 2.3 Training Data Lawfulness Assessment

For each training dataset, document:

| Assessment Element | Requirement |
|-------------------|-------------|
| Original collection purpose | Was personal data collected for a purpose compatible with AI training? |
| Lawful basis | Art. 6(1) basis for the training processing — legitimate interest requires balancing test |
| Consent validity | If consent is the basis, was AI training specified as a purpose? Was consent freely given? |
| Special category conditions | If Art. 9 data is present, which Art. 9(2) exception applies? |
| Web-scraped data | EDPB position: web scraping for AI training generally cannot rely on legitimate interest without additional safeguards |
| Third-party datasets | Has the controller verified the upstream lawful basis chain? |

### Phase 3: AI-Specific Risk Assessment

#### 3.1 Privacy Risk Categories for AI

| Risk Category | Description | Likelihood Factors |
|---------------|-------------|-------------------|
| Training data extraction | Adversary extracts verbatim training data from the model | Model size, training data repetition, overfitting degree |
| Membership inference | Adversary determines if specific data was in the training set | Model confidence distribution, overfitting, shadow model availability |
| Model inversion | Adversary reconstructs input features from model outputs | Output granularity, model type, auxiliary information available |
| Attribute inference | Model reveals sensitive attributes not provided as input | Correlations in training data, feature interactions |
| Emergent bias amplification | Model amplifies biases present in training data, producing discriminatory outcomes | Training data representativeness, debiasing measures applied |
| Concept drift discrimination | Model performance degrades unequally across demographic groups over time | Monitoring coverage, retraining frequency |
| Re-identification through AI output | Model outputs enable linking back to specific data subjects | Output specificity, population uniqueness, auxiliary data |
| Automated decision errors | Incorrect AI decisions causing material harm to data subjects | Model accuracy, error distribution across groups |

#### 3.2 AI Risk Scoring Matrix

Combine likelihood and severity using the EDPB-recommended matrix:

```
                    Negligible    Limited    Significant    Maximum
Almost Certain      Medium        High       Very High      Very High
Likely              Medium        High       High           Very High
Possible            Low           Medium     High           High
Remote              Low           Low        Medium         High
```

#### 3.3 AI Act Risk Level Integration

Cross-reference GDPR risk assessment with AI Act classification:

- **Unacceptable risk** (Art. 5 AI Act): Processing must not proceed — social scoring, real-time biometric identification in public spaces (with limited exceptions)
- **High risk** (Art. 6 + Annex III): Enhanced DPIA obligations, conformity assessment required
- **Limited risk** (Art. 50): Transparency obligations — inform users they are interacting with AI
- **Minimal risk**: Standard DPIA process applies

### Phase 4: AI-Specific Mitigation Measures

#### Technical Measures

| Measure | Risk Addressed | Implementation |
|---------|---------------|----------------|
| Differential privacy | Training data extraction, membership inference | Apply DP-SGD during training with calibrated epsilon (ε ≤ 8 for moderate protection, ε ≤ 1 for strong) |
| Federated learning | Data centralisation risk | Distribute training across data holders without centralising personal data |
| Model output perturbation | Model inversion, attribute inference | Add calibrated noise to model outputs, round confidence scores |
| Training data deduplication | Memorization risk | Remove duplicate and near-duplicate records before training |
| Membership inference testing | Membership inference | Run MI attacks against the model pre-deployment; retrain if leakage exceeds threshold |
| Fairness constraints | Bias amplification | Apply demographic parity, equalised odds, or calibration constraints during training |
| Input/output filtering | PII leakage in generative models | Deploy PII detection on model inputs and outputs with automated redaction |
| Model pruning and distillation | Memorization, extraction | Compress the model to reduce capacity for memorizing individual records |

#### Organisational Measures

- Establish an AI Ethics Review Board with privacy representation
- Implement model cards documenting privacy properties for each deployed model
- Conduct regular model audits (minimum annually) testing for privacy leakage
- Maintain training data provenance documentation and deletion capability
- Define retraining triggers and ensure DPIA review accompanies each retraining cycle
- Implement incident response procedures specific to AI privacy incidents

### Phase 5: Human Oversight Assessment

Per AI Act Art. 14 and GDPR Art. 22, assess the human oversight mechanism:

| Oversight Element | Assessment Question |
|-------------------|-------------------|
| Meaningful review | Can the human reviewer effectively evaluate the AI recommendation and override it? |
| Time and resources | Is sufficient time allocated for meaningful review, or is the human a rubber stamp? |
| Competence | Does the reviewer have the expertise to identify AI errors? |
| Authority | Does the reviewer have the authority and means to override the AI? |
| Feedback mechanism | Are overrides recorded and fed back into model improvement? |
| Automation bias | Are measures in place to mitigate the tendency to defer to the AI? |

## Prior Consultation Triggers for AI

Art. 36 prior consultation with the supervisory authority is required when:

1. The AI system produces high residual risk after all mitigation measures
2. The AI system processes special category data at scale with novel techniques
3. The supervisory authority's Art. 35(4) list specifically includes the AI use case
4. The AI system is deployed for real-time biometric identification under AI Act Art. 5 exceptions

## Enforcement Precedents

- **Clearview AI (Multiple DPAs, 2021-2024)**: Fines totalling over EUR 90 million across Italy (EUR 20M), France (EUR 20M), UK (GBP 7.5M), Greece (EUR 20M) for facial recognition AI deployed without DPIA, lawful basis, or transparency
- **CNIL v. Clearview AI (SAN-2022-019)**: Specific finding that no DPIA was conducted for biometric AI processing
- **Italian DPA v. Replika (2023)**: Ordered cessation of AI chatbot processing due to inadequate age verification and failure to conduct DPIA for AI processing affecting minors
- **Spanish DPA v. CaixaBank (PS/00421/2020)**: EUR 6 million fine for automated credit scoring without adequate DPIA addressing algorithmic decision-making risks
- **Dutch DPA v. Tax Authority (2020)**: Finding that algorithmic fraud detection system (SyRI) lacked proportionality and adequate DPIA for AI-driven profiling

## Integration Points

- **ai-training-lawfulness**: Detailed lawful basis analysis for training data feeds into Phase 2
- **ai-automated-decisions**: Art. 22 assessment integrates with Phase 5 human oversight
- **ai-model-privacy-audit**: Technical privacy testing results feed into Phase 3 risk assessment
- **ai-act-high-risk-docs**: AI Act conformity assessment aligns with Phase 3.3 risk classification
- **ai-bias-special-category**: Bias assessment results feed into risk scoring for discrimination harms
