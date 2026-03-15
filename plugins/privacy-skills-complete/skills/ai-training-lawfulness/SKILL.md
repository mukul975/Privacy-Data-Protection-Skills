---
name: ai-training-lawfulness
description: >-
  Assesses lawful basis for AI training data processing per EDPB April 2025
  report on LLMs and general-purpose AI. Covers legitimate interest balancing
  tests, consent challenges for ML training, public dataset assessment, and
  web scraping lawfulness. Keywords: AI training data, lawful basis, EDPB LLM,
  legitimate interest, consent, web scraping.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "ai-training, lawful-basis, edpb-llm, legitimate-interest, web-scraping, consent"
---

# Lawful Basis for AI Training Data

## Overview

The processing of personal data for AI model training constitutes a distinct processing operation requiring its own lawful basis under GDPR Art. 6(1). The EDPB Guidelines 04/2025 and the coordinated ChatGPT Taskforce findings establish that AI training creates unique lawful basis challenges: the scale of data collection, the difficulty of obtaining meaningful consent for open-ended AI training purposes, the tension between legitimate interest and data subject expectations, and the complexity of determining lawfulness for web-scraped and third-party datasets. This skill provides the comprehensive lawful basis assessment framework for AI training data processing, addressing each Art. 6(1) basis as applied to ML training contexts.

## Fundamental Principles

### AI Training as Personal Data Processing

The EDPB has confirmed that AI model training constitutes processing of personal data under Art. 4(2) GDPR when:

1. Training datasets contain personal data (directly or indirectly identifiable natural persons)
2. The model is trained on data that includes personal data, even if the intent is to learn general patterns
3. The resulting model retains the capability to generate or reproduce personal data from training sets
4. Personal data is used in any pipeline stage: collection, cleaning, annotation, augmentation, validation, testing

The controller cannot avoid GDPR obligations by claiming the model has "learned" rather than "stored" personal data. The processing occurs at the point of training, regardless of whether the model can later reproduce specific records.

### Purpose Specification for AI Training

Art. 5(1)(b) requires that personal data be collected for specified, explicit, and legitimate purposes. For AI training, this means:

- "Training an AI model" is insufficiently specific — the controller must articulate the specific capability being developed
- "Improving our services" through AI training must be disaggregated into concrete purposes
- Each purpose must be documented before training begins, not retroactively justified
- The purpose must be communicated to data subjects in privacy notices per Arts. 13-14

## Lawful Basis Analysis for AI Training

### Art. 6(1)(a) — Consent

#### Requirements for Valid AI Training Consent

| Requirement | AI Training Application |
|-------------|----------------------|
| Freely given | Data subjects must have genuine choice; consent cannot be bundled with service access unless AI training is necessary for the service |
| Specific | "AI training" alone is insufficient — must specify what type of model, for what purpose, what data elements are used |
| Informed | Must explain how personal data will be used in training, retention period for training data, risk of model memorization, inability to fully delete data from trained models |
| Unambiguous | Clear affirmative action; pre-ticked boxes or implied consent from terms of service are insufficient |
| Withdrawable | Controller must provide mechanism to withdraw consent; but model already trained on the data presents technical challenge |

#### Consent Challenges in AI Training

1. **Granularity problem**: AI training often uses all available data — difficult to obtain specific consent for each data element's use in training
2. **Withdrawal complexity**: Once a model is trained on personal data, true erasure requires model retraining or verified machine unlearning
3. **Purpose evolution**: Foundation models and transfer learning mean the model may be repurposed — original consent may not cover downstream uses
4. **Scale impracticality**: Obtaining consent from millions of data subjects whose data appears in web-scraped training corpora is practically impossible
5. **Power imbalance**: When AI service use requires consent to training (e.g., "use our AI assistant and your conversations train our model"), consent may not be freely given

#### When Consent Works for AI Training

- Users explicitly opt into a research programme where AI model training is a primary purpose
- Users contribute data to a specific AI system with clear disclosure (e.g., "your feedback trains this recommendation engine")
- Fine-tuning on user-provided data where the user understands and consents to the training purpose

### Art. 6(1)(b) — Contract Necessity

AI training can rely on contractual necessity only when:

- The AI model training is genuinely necessary for performing the contract with the data subject
- The data subject has entered into a contract that requires AI-powered features
- The training cannot be separated from the service delivery

Limitations per EDPB:
- General improvement of AI systems through aggregate training is not "necessary" for any individual contract
- Training a general-purpose model that benefits future users is not necessary for the current data subject's contract
- Fine-tuning based on individual user interactions may qualify if the personalised model is part of the contracted service

### Art. 6(1)(f) — Legitimate Interest

This is the most commonly relied-upon basis for AI training. The EDPB requires a rigorous three-part assessment:

#### Part 1: Legitimate Interest Identification

The controller must identify a specific, real, and lawful interest:

| Interest Type | Example | EDPB Assessment |
|---------------|---------|-----------------|
| Commercial product improvement | Training a fraud detection model to protect customers | Generally legitimate — concrete benefit to data subjects |
| Research and development | Training models for medical imaging analysis | Legitimate if research purpose is genuine and specific |
| General AI capability | Training a foundation model for general-purpose use | Scrutinised — interest must be articulated with specificity |
| Competitive advantage | Training to match competitor AI capabilities | Legitimate commercial interest but weak in balancing |

#### Part 2: Necessity Assessment

| Question | Assessment Criteria |
|----------|-------------------|
| Is AI training necessary for the identified interest? | Could the interest be pursued without training on personal data? |
| Could anonymised data achieve the same result? | Has the controller tested model performance with anonymised data? |
| Could synthetic data supplement or replace personal data? | Has synthetic data generation been evaluated? |
| Is the volume of personal data proportionate? | Has the minimum effective dataset been determined? |
| Could federated learning avoid centralising personal data? | Has distributed training been assessed? |

#### Part 3: Balancing Test

Factors weighing in favour of the controller:
- Training data is publicly available (but this alone is not decisive)
- Model serves a beneficial purpose (fraud prevention, medical research)
- Strong technical safeguards applied (differential privacy, access controls)
- Data subjects can exercise opt-out rights effectively
- Training data is pseudonymised before use

Factors weighing in favour of data subjects:
- Data was not collected with AI training in mind — processing is far from original expectations
- Large-scale data collection from diverse sources without data subjects' awareness
- Special category data is present or can be inferred from training data
- Children's data is present in the training corpus
- No practical opt-out mechanism exists
- Model may memorize and regurgitate personal data
- Web scraping bypasses data subjects' choices about data sharing

#### EDPB Position on Legitimate Interest for AI Training

The EDPB Guidelines 04/2025 establish that:

1. Legitimate interest for AI training is not automatically available — it requires case-by-case assessment
2. Web scraping of personal data for AI training faces a particularly high bar
3. The scale of data collection is a relevant factor — larger datasets require stronger justification
4. The controller must demonstrate necessity: evidence that personal data is required rather than anonymised or synthetic alternatives
5. Effective opt-out mechanisms are expected as a minimum safeguard
6. The balancing test should consider the cumulative impact of multiple AI developers scraping and training on the same data subjects' data

### Art. 6(1)(e) — Public Interest

Available to public bodies and organisations performing tasks in the public interest:

- Academic research institutions training AI models for publicly beneficial research
- Government agencies training AI for public service delivery
- Must have a basis in national or Union law
- Proportionality requirements apply

### Special Situations

#### Web-Scraped Data

The EDPB has given specific guidance on web scraping for AI training:

1. **Robots.txt is not consent**: Compliance with robots.txt does not establish lawful basis
2. **Public availability is not a lawful basis**: Data being publicly accessible does not mean it can be freely used for AI training
3. **Reasonable expectations**: Data subjects who post content online do not reasonably expect it to be used for AI training
4. **Children's data**: Web-scraped data likely contains children's data — heightened protections apply
5. **Technical measures**: Data subjects who implement privacy settings have expressed a preference against broad data use

Assessment framework for web-scraped training data:

| Factor | High Lawfulness Indicator | Low Lawfulness Indicator |
|--------|--------------------------|-------------------------|
| Data source | Explicitly open-licence data (CC0, public domain) | Personal profiles, social media, private websites |
| Data type | Factual, non-personal content | Identifiable personal information, photos, opinions |
| Data subject expectations | Data published with intent for wide reuse | Data shared in specific context (social media, forums) |
| Safeguards | Differential privacy, PII filtering pre-training | No preprocessing to remove personal data |
| Opt-out | Effective and accessible opt-out mechanism | No opt-out or technically impractical opt-out |
| Transparency | Privacy notice covers AI training use | No notice to data subjects about AI training |

#### Third-Party Datasets

When using datasets obtained from third parties:

1. **Upstream lawful basis verification**: The controller must verify that the data provider had a lawful basis to collect and share the data
2. **Contractual warranties**: Obtain warranties from the provider regarding lawful collection, consent scope, and right to license for AI training
3. **Due diligence**: Conduct reasonable due diligence on the provider's data collection practices
4. **Chain of accountability**: The AI developer remains a controller responsible for lawful processing, even if the data was provided by a third party

#### Public Datasets

Academic and government datasets require assessment:

1. Is personal data present? (Many datasets contain inadvertent personal data)
2. What was the original purpose of the dataset? Is AI training compatible?
3. Does the dataset licence permit commercial AI training?
4. Has the dataset been ethically reviewed for consent and privacy?
5. Are there known issues (bias, PII leakage, consent gaps)?

## Training Data Retention

Art. 5(1)(e) storage limitation applies to AI training data:

- Training data must not be retained longer than necessary for the training purpose
- Once the model is trained, is continued retention of training data justified?
- If training data is retained for retraining, what is the maximum retention period?
- Model artefacts (weights, embeddings) that encode personal data are also subject to retention limits
- Deletion verification: can the controller demonstrate that training data has been effectively deleted?

## Data Subject Rights for Training Data

| Right | AI Training Application | Technical Challenge |
|-------|------------------------|-------------------|
| Access (Art. 15) | Data subject can request confirmation that their data was used in training and receive a copy | Identifying specific records in large training datasets |
| Rectification (Art. 16) | Inaccurate personal data in training sets must be corrected | Correction may require model retraining |
| Erasure (Art. 17) | Data subjects can request deletion of their data from training sets | Requires machine unlearning or model retraining |
| Objection (Art. 21) | Data subjects can object to processing based on legitimate interest | Controller must cease processing unless compelling grounds override |
| Restriction (Art. 18) | Processing must be restricted while accuracy or objection is contested | May require quarantining data from training pipeline |

## Enforcement Precedents

- **Garante v. OpenAI (2023)**: Temporary processing ban — no lawful basis identified for ChatGPT training data. Ordered OpenAI to identify Art. 6(1) basis for training data, implement age verification, and provide opt-out mechanism.
- **CNIL v. Clearview AI (SAN-2022-019, 2022)**: EUR 20M fine — web scraping of biometric data without lawful basis. No consent, legitimate interest balancing test not conducted.
- **Datatilsynet (Norway) v. Meta (2023)**: Temporary ban on using Norwegian user data for AI training — legitimate interest basis not sufficiently documented; balancing test inadequate.
- **DPC (Ireland) v. Meta (2024)**: Investigation into use of public Facebook/Instagram posts for AI training under legitimate interest basis. Meta paused EU AI training following DPC engagement.
- **EDPB Taskforce on ChatGPT (2024)**: Coordinated finding that legitimate interest for LLM training requires comprehensive balancing test, transparency, and effective opt-out — mere assertion of legitimate interest is insufficient.

## Integration Points

- **ai-dpia**: Training data lawfulness feeds into DPIA Phase 2 assessment
- **ai-data-subject-rights**: Rights exercise mechanisms for training data
- **ai-data-retention**: Retention and deletion requirements for training datasets
- **ai-transparency-reqs**: Transparency obligations regarding training data use
