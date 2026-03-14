---
name: ai-privacy-inference
description: >-
  Managing privacy risks from AI-driven inferences about individuals including
  derived data classification, profiling under GDPR Art. 22, inference accuracy
  obligations, and controlling automated personality/behaviour predictions.
  Keywords: AI inference, derived data, profiling, automated predictions, GDPR.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "ai-inference, derived-data, profiling, automated-predictions, gdpr-art-22"
---

# AI Privacy Inference and Derived Data

## Overview

AI systems routinely generate inferences about individuals — predictions about creditworthiness, health risks, personality traits, political opinions, or behavioural patterns that were never directly provided by the data subject. These AI-derived inferences raise critical privacy questions: Are inferences personal data? When does inference become profiling under GDPR Article 22? What accuracy obligations apply to AI predictions? Can data subjects access, rectify, or object to inferences drawn about them? The CJEU, EDPB, and national DPAs have progressively clarified that inferences are personal data when they relate to an identified or identifiable person, and that GDPR rights extend to derived and inferred data. Cerebrum AI Labs must classify, govern, and provide transparency over all inferences its AI systems generate about individuals.

## Legal Framework for AI Inferences

### When Inferences Are Personal Data

| Criterion | Analysis | Example |
|-----------|----------|---------|
| **Relates to an identified person** | Inference is linked to a specific customer record or user profile | "Customer C-12345 has 78% churn probability" |
| **Relates to an identifiable person** | Inference can be linked to a person through combination with other data | "User with session token X-789 is likely aged 25-34" |
| **Used to evaluate a person** | Inference is used to assess, classify, or make decisions about someone | Credit score derived from transaction patterns |
| **Has impact on a person** | Inference affects how the person is treated or what options are available | Insurance premium adjusted based on predicted health risk |

**CJEU C-434/16 (Nowak, 2017)**: Personal data includes "any information" relating to a data subject — this encompasses opinions, assessments, and inferences, not only factual data directly provided by the individual.

**EDPB Guidelines 8/2020 on Targeting of Social Media Users**: Inferred data (data created by the controller through observation or derivation) constitutes personal data and is subject to the full scope of GDPR rights.

### GDPR Classification of Inference Types

| Inference Type | Classification | GDPR Implications |
|---------------|---------------|-------------------|
| **Observed data** | Data collected through direct interaction (browsing history, purchase records) | Standard personal data — Art. 6 lawful basis required |
| **Derived data** | Data created by the controller through computation on existing data (credit score, risk rating) | Personal data — subject to access, rectification, objection rights |
| **Inferred data** | Probabilistic predictions about characteristics not directly observed (personality, health risk) | Personal data — potentially special category if predicting Art. 9 characteristics |
| **Aggregated data** | Statistical outputs at group level, not linked to individuals | Not personal data if truly anonymous (k-anonymity verified) |

### When Inferences Become Special Category Data

| Predicted Characteristic | Art. 9 Category | Trigger |
|------------------------|----------------|---------|
| Ethnic origin from name/location patterns | Racial or ethnic origin | Any inference about ethnic background, even probabilistic |
| Political leaning from content engagement | Political opinions | Prediction used to classify or target based on politics |
| Religious affiliation from purchase patterns | Religious beliefs | Halal/kosher purchase scoring, prayer time activity patterns |
| Health condition from behavioural signals | Health data | Step count decline predicting depression, typing pattern analysis |
| Sexual orientation from browsing/social data | Sexual orientation | Any inference about sexual orientation regardless of accuracy |
| Pregnancy from purchase pattern shifts | Health data + gender | Purchase category analysis predicting pregnancy status |

**Cerebrum AI Labs Policy**: Any inference that predicts, estimates, or classifies an Art. 9 characteristic — even indirectly or probabilistically — must be treated as special category data and requires an Art. 9(2) condition for processing.

## Profiling Under GDPR Article 22

### Profiling Definition (Art. 4(4))

Profiling means any form of automated processing of personal data consisting of the use of personal data to evaluate certain personal aspects relating to a natural person, in particular to analyse or predict aspects concerning:
- Work performance
- Economic situation
- Health
- Personal preferences
- Interests
- Reliability
- Behaviour
- Location
- Movements

### Three-Level Framework

| Level | Description | GDPR Requirement | Cerebrum AI Labs Example |
|-------|-------------|------------------|-------------------------|
| **Profiling only** | Automated evaluation without decision | Art. 6 lawful basis + Art. 13-14 transparency | Customer segmentation for analytics dashboard |
| **Profiling + human decision** | Automated evaluation informing a human decision-maker | Art. 6 lawful basis + transparency + meaningful human involvement | Credit risk score reviewed by loan officer |
| **Solely automated decision with legal/significant effects** | Automated decision with no meaningful human involvement producing legal or similarly significant effects | Art. 22(1) prohibition applies — must fall within Art. 22(2) exceptions | Automated loan rejection based solely on AI credit score |

### Art. 22(2) Exceptions Allowing Solely Automated Decisions

| Exception | Requirement | Cerebrum AI Labs Application |
|-----------|-------------|------------------------------|
| **Art. 22(2)(a) — Contract** | Decision necessary for entering into or performing a contract | Automated credit pre-approval for existing customers |
| **Art. 22(2)(b) — Law** | Authorised by EU or Member State law with suitable safeguards | Regulatory-mandated fraud screening |
| **Art. 22(2)(c) — Explicit consent** | Data subject's explicit consent obtained | Customer opts in to automated portfolio rebalancing |

### Safeguards Required (Art. 22(3))

| Safeguard | Implementation at Cerebrum AI Labs |
|-----------|-----------------------------------|
| **Right to obtain human intervention** | Escalation button in customer portal routes to trained human reviewer within 2 business days |
| **Right to express point of view** | Customer can submit additional context through contestation form before human review |
| **Right to contest the decision** | Appeal process with independent review panel; decision reversed if AI error demonstrated |
| **Right to explanation** | Individual explanation generated using SHAP values showing top 5 factors influencing the AI decision |

## Inference Accuracy and Quality Obligations

### GDPR Article 5(1)(d) — Accuracy Principle

AI inferences must be accurate, and where necessary, kept up to date. For probabilistic predictions this means:

| Obligation | Implementation |
|-----------|---------------|
| **Accuracy measurement** | Track prediction accuracy metrics (precision, recall, F1) per demographic group |
| **Confidence thresholds** | Do not present inferences with confidence below 70% as actionable without human review |
| **Staleness detection** | Re-evaluate inferences when underlying data changes; flag inferences older than 90 days |
| **Accuracy disclosure** | Inform data subjects of the probabilistic nature and known accuracy of inferences |
| **Rectification of inferences** | Allow data subjects to challenge inferences; if input data is corrected, regenerate inference |

### EDPB Position on Inference Accuracy

The EDPB Guidelines on Automated Decision-Making (WP 251 rev.01) state that controllers must:
1. Use appropriate mathematical or statistical procedures for profiling
2. Implement appropriate technical and organisational measures to minimise the risk of errors
3. Correct inaccuracies and enable rectification
4. Secure personal data to prevent discriminatory effects

## Transparency Requirements for AI Inferences

### Art. 13-14 Information Requirements

| Information | Requirement | Cerebrum AI Labs Implementation |
|-------------|-------------|-------------------------------|
| **Existence of profiling** | Inform data subjects that profiling occurs | Privacy notice section: "How we use AI to analyse your data" |
| **Logic involved** | Meaningful information about the logic involved | Technical explainer: "Our AI analyses your transaction patterns, account tenure, and product usage to predict service needs" |
| **Significance** | Envisaged consequences of such processing | "This analysis may affect the products and offers shown to you, and may influence credit decisions" |
| **Categories of data used** | What data feeds the inference | "We use: transaction history, account tenure, product holdings, service interactions" |
| **Inference outputs** | What inferences are generated | "We generate: churn probability, product affinity scores, credit risk indicators" |

### AI Act Transparency Requirements

| Obligation | AI Act Article | Cerebrum AI Labs Implementation |
|-----------|---------------|-------------------------------|
| Inform users they are interacting with AI | Art. 52(1) | Chat interface disclosure: "You are interacting with an AI assistant" |
| Disclose AI-generated content | Art. 52(3) | Outputs marked: "This recommendation was generated by AI" |
| Disclose emotion recognition | Art. 52(2) | Not applicable — Cerebrum AI Labs does not use emotion recognition |
| High-risk system deployer transparency | Art. 13 | Technical documentation available to regulators on request |

## Inference Governance Framework

### Cerebrum AI Labs Inference Registry

All AI systems that generate inferences about individuals must be registered in the Cerebrum AI Labs Inference Registry:

| Registry Field | Description |
|---------------|-------------|
| System ID | Unique identifier for the AI system |
| Inference type | Category of inference generated (behavioural, demographic, financial, health) |
| Data subjects affected | Categories and approximate volume of individuals profiled |
| Input features | Data elements used to generate the inference |
| Output format | Inference output (score, category, probability, ranking) |
| Accuracy metrics | Latest precision, recall, F1 by demographic group |
| Retention period | How long inferences are stored before deletion |
| Art. 22 assessment | Whether the inference feeds a solely automated decision |
| Lawful basis | Art. 6 and (if applicable) Art. 9 basis for generating the inference |
| DPIA reference | Associated DPIA document ID |

### Inference Lifecycle Controls

| Phase | Control |
|-------|---------|
| **Generation** | Log all inferences with timestamp, model version, confidence score, input data hash |
| **Storage** | Encrypt inference outputs; apply access controls limiting who can read individual-level inferences |
| **Usage** | Track downstream consumption of inferences; prevent scope creep beyond documented purposes |
| **Disclosure** | Make inferences available to data subjects on request (Art. 15 access right) |
| **Rectification** | If underlying data is corrected, flag dependent inferences for regeneration |
| **Deletion** | Delete inferences per retention schedule (90 days operational, 12 months audit) |

## Enforcement and Regulatory Precedents

- **CJEU C-634/21 (SCHUFA, 2023)**: The CJEU held that the generation of a credit score by a private entity constitutes "automated individual decision-making" under Art. 22 if the score plays a decisive role in a subsequent decision by a third party. This means AI-derived scores used in downstream decisions may trigger Art. 22 protections even if the AI provider is not the final decision-maker.
- **Austrian DPA — Case DSB-D550.038 (2022)**: Found that inferred political opinions from social media activity constitute special category data under Art. 9, even when the inference is probabilistic and may be inaccurate.
- **Norwegian DPA — Grindr Decision (2021)**: NOK 65 million fine for sharing data enabling inference of sexual orientation. Established that data enabling inference of Art. 9 characteristics is itself special category data.
- **CNIL — Clearview AI (2022)**: EUR 20 million fine, finding that biometric inferences (face embeddings) from public photographs are personal data subject to full GDPR compliance.

## Key Legal References

- **GDPR Article 4(4)** — Definition of profiling
- **GDPR Article 5(1)(d)** — Accuracy principle
- **GDPR Article 13(2)(f)** — Right to information about profiling logic and significance
- **GDPR Article 15(1)(h)** — Right of access to profiling information
- **GDPR Article 22** — Automated individual decision-making including profiling
- **GDPR Recital 71** — Safeguards for profiling and automated decisions
- **GDPR Recital 72** — Guidelines on profiling
- **CJEU C-434/16 (Nowak, 2017)** — Broad interpretation of personal data including assessments
- **CJEU C-634/21 (SCHUFA, 2023)** — Credit scoring as automated decision-making
- **EDPB Guidelines on Automated Decision-Making (WP 251 rev.01)** — Art. 22 interpretation
- **EDPB Guidelines 8/2020 on Targeting of Social Media Users** — Inferred data as personal data
- **EU AI Act Article 52** — Transparency obligations for AI systems
- **EU AI Act Article 14** — Human oversight for high-risk AI systems
