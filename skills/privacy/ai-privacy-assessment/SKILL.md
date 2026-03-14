---
name: ai-privacy-assessment
description: >-
  Guides the combined DPIA and AI Act conformity assessment for AI systems
  processing personal data. Covers EDPB-EDPS Joint Opinion 5/2021, training
  data lawfulness under Art. 6 and Art. 9, Art. 22 automated decision-making,
  algorithmic bias detection, and NIST AI RMF MAP function. Keywords: AI
  privacy, DPIA, AI Act, algorithmic bias, automated decision-making,
  Art. 22, training data, NIST AI RMF.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "ai-privacy, dpia, ai-act, algorithmic-bias, art-22, nist-ai-rmf"
---

# Conducting AI System Privacy Assessment

## Overview

AI systems that process personal data require a combined privacy and conformity assessment addressing both GDPR obligations and the EU AI Act (Regulation 2024/1689). This skill integrates the GDPR Art. 35 DPIA framework with AI-specific risk assessment, encompassing training data lawfulness, Art. 22 automated decision-making implications, algorithmic fairness, and the NIST AI Risk Management Framework MAP function. The assessment methodology draws from the EDPB-EDPS Joint Opinion 5/2021 on the AI Act proposal and subsequent EDPB Guidelines 06/2025 on AI and data protection.

## Legal Framework

### GDPR Provisions Applicable to AI

| Provision | Application to AI Systems |
|-----------|--------------------------|
| Art. 5(1)(a) — Lawfulness, fairness, transparency | AI processing must have a lawful basis; the logic of AI decisions must be explainable to data subjects |
| Art. 5(1)(b) — Purpose limitation | Training data collected for one purpose cannot be used to train AI models for an incompatible purpose without further lawful basis |
| Art. 5(1)(c) — Data minimisation | AI models should not require more personal data than necessary; synthetic data and anonymisation should be considered |
| Art. 5(1)(d) — Accuracy | AI outputs affecting individuals must be accurate; model drift must be monitored |
| Art. 6(1) — Lawful basis | Each stage of AI processing (data collection, model training, inference, output use) requires a lawful basis |
| Art. 9 — Special categories | Training on health, biometric, genetic, racial, political, religious, sexual orientation, or trade union data requires an Art. 9(2) exemption |
| Art. 13-14 — Transparency | Privacy notices must disclose the existence of automated decision-making, meaningful information about the logic involved, and the significance and envisaged consequences |
| Art. 22 — Automated decision-making | Data subjects have the right not to be subject to decisions based solely on automated processing that produce legal effects or similarly significantly affect them, with exceptions under Art. 22(2) |
| Art. 25 — Data protection by design | AI systems must embed privacy protections from the design phase: privacy-preserving ML techniques, differential privacy, federated learning |
| Art. 35 — DPIA | AI systems meeting EDPB WP248rev.01 criteria (evaluation/scoring, automated decision-making, innovative technology) require a DPIA |

### EU AI Act (Regulation 2024/1689) Risk Classification

| Risk Category | Description | AI Act Requirements | GDPR Overlap |
|--------------|-------------|---------------------|--------------|
| Unacceptable Risk (Art. 5) | AI practices prohibited outright: social scoring by public authorities, real-time remote biometric identification in public spaces (with exceptions), emotion recognition in workplace/education, untargeted scraping for facial recognition databases | Prohibited — cannot be deployed | Art. 9 special categories, Art. 35 DPIA |
| High Risk (Annex III) | AI systems in listed areas: biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, administration of justice | Conformity assessment, risk management system, data governance, transparency, human oversight, accuracy/robustness/cybersecurity | Art. 22, Art. 35 DPIA, Art. 25 DPbD |
| Limited Risk (Art. 50) | AI systems with specific transparency obligations: chatbots, emotion recognition, deep fakes | Transparency obligations (notify users they are interacting with AI) | Art. 13-14 transparency |
| Minimal Risk | All other AI systems | No specific AI Act obligations; voluntary codes of practice | Standard GDPR compliance |

### EDPB-EDPS Joint Opinion 5/2021

Key recommendations from the Joint Opinion on the AI Act proposal:

1. **Prohibition of remote biometric identification in public spaces** — supported without exceptions
2. **AI-specific DPIA** — the EDPB recommended mandatory DPIAs for all high-risk AI systems, not limited to Art. 35 triggers
3. **Right to explanation** — Art. 22(3) right to obtain human intervention and contest decisions should apply to all AI-assisted decisions, not only fully automated ones
4. **Training data governance** — controllers must ensure lawfulness of personal data used for AI training throughout the model lifecycle, including when training data is subsequently deleted
5. **Purpose limitation for AI training** — repurposing personal data for AI model training requires a compatibility assessment under Art. 6(4) or a separate lawful basis

## Assessment Methodology

### Phase 1: AI System Classification (Week 1)

#### 1.1 AI Act Risk Classification

Determine the AI system's risk category under the AI Act:

1. Check Art. 5 prohibited practices list — if the system falls within a prohibition, it cannot be deployed.
2. Check Annex III high-risk categories:
   - Biometric identification and categorisation of natural persons
   - Management and operation of critical infrastructure
   - Education and vocational training (admissions, assessment, proctoring)
   - Employment, worker management, and access to self-employment (recruitment, task allocation, performance evaluation, termination)
   - Access to and enjoyment of essential private and public services (credit scoring, insurance pricing, emergency services dispatch)
   - Law enforcement (crime risk assessment, polygraph, evidence evaluation)
   - Migration, asylum, and border control
   - Administration of justice and democratic processes
3. Check Art. 50 transparency obligations for limited-risk AI.
4. If not high-risk or limited-risk, classify as minimal risk.

#### 1.2 GDPR Processing Assessment

1. Identify all personal data processed at each AI lifecycle stage: data collection, data preparation, model training, model validation, inference/deployment, output use.
2. For each stage, identify the lawful basis under Art. 6(1).
3. If special category data is involved, identify the Art. 9(2) condition.
4. Assess whether Art. 22 applies (solely automated decisions with legal or significant effect).

### Phase 2: Training Data Lawfulness (Week 2)

#### 2.1 Data Collection Lawfulness

| Assessment Question | Requirement |
|--------------------|-------------|
| Was the training data collected with a lawful basis under Art. 6(1)? | Each data source must have an identified lawful basis |
| Is the use of data for AI training compatible with the original collection purpose? | Art. 6(4) compatibility assessment or Art. 5(1)(b) further processing analysis |
| Was consent obtained for AI training specifically? | If relying on Art. 6(1)(a), consent must be specific, informed, and freely given for the AI training purpose |
| If using legitimate interest, has a balancing test been conducted? | Art. 6(1)(f) requires documented LIA including AI-specific impacts |
| Does training data include special categories? | Art. 9(2) exemption required; Art. 9(2)(j) scientific research may apply with safeguards |

#### 2.2 Data Quality and Bias Assessment

| Assessment Area | Requirements |
|-----------------|-------------|
| Representativeness | Training data must be representative of the population the AI system will be applied to. Underrepresentation of demographic groups must be identified and addressed. |
| Label accuracy | If supervised learning, labels must be accurate and free from historical bias. Human labellers must be trained on anti-discrimination principles. |
| Temporal validity | Training data must reflect current conditions. Stale training data can produce discriminatory outputs. |
| Proxy variables | Identify features that may serve as proxies for protected characteristics (postcode as proxy for ethnicity, name as proxy for gender). |
| Data provenance | Document the source, collection methodology, and processing history for all training data. |

#### 2.3 Training Data Retention

- Art. 5(1)(e) storage limitation applies to training data.
- Once training is complete, assess whether original training data must be retained or can be deleted.
- If training data is deleted, document how data subject rights (access, erasure) will be facilitated regarding data embedded in the trained model.
- Consider whether the trained model itself constitutes personal data (if individual data points can be extracted through model inversion attacks).

### Phase 3: Art. 22 Automated Decision-Making Assessment (Week 3)

#### 3.1 Art. 22(1) Applicability Test

```
Does the AI system make decisions about individuals?
├─ NO → Art. 22 does not apply.
└─ YES → Continue.
    │
    Are decisions based solely on automated processing?
    ├─ NO → Art. 22(1) does not apply, but Art. 13-14 transparency still applies.
    │   (Note: "meaningful human involvement" must be genuine, not rubber-stamping.)
    └─ YES → Continue.
        │
        Do decisions produce legal effects or similarly significantly affect the individual?
        ├─ NO → Art. 22(1) does not apply.
        └─ YES → Art. 22(1) applies. The individual has the right not to be subject
            to the decision unless an Art. 22(2) exception applies.
```

#### 3.2 Art. 22(2) Exceptions

| Exception | Requirements |
|-----------|-------------|
| Art. 22(2)(a) — Necessary for contract | Decision must be necessary for entering into or performing a contract with the data subject |
| Art. 22(2)(b) — Authorised by law | Union or Member State law must authorise the decision and provide suitable safeguards |
| Art. 22(2)(c) — Explicit consent | Data subject has given explicit consent to the automated decision |

#### 3.3 Art. 22(3) Safeguards

Even where an Art. 22(2) exception applies, the controller must implement suitable measures including:
- Right to obtain human intervention
- Right to express the data subject's point of view
- Right to contest the decision
- Meaningful information about the logic involved (not the full algorithm, but sufficient to understand the factors and their relative weight)

### Phase 4: Algorithmic Bias and Fairness Assessment (Week 3-4)

#### 4.1 Fairness Metrics

| Metric | Description | Application |
|--------|-------------|-------------|
| Demographic parity | Positive outcome rates should be equal across protected groups | Credit scoring, hiring |
| Equalized odds | True positive and false positive rates should be equal across groups | Criminal risk assessment, fraud detection |
| Predictive parity | Positive predictive value should be equal across groups | Medical diagnosis, recidivism prediction |
| Individual fairness | Similar individuals should receive similar outcomes | Loan pricing, insurance premium calculation |
| Counterfactual fairness | Outcome should not change if only the protected characteristic changes | Any decision-making system |

#### 4.2 Bias Testing Protocol

1. Define protected characteristics relevant to the jurisdiction and use case (race, gender, age, disability, religion, sexual orientation per Equality Act 2010 / EU Charter Art. 21).
2. Partition test dataset by protected characteristics.
3. Calculate fairness metrics for each group.
4. Identify disparate impact: if the selection rate for any protected group is less than 80% of the rate for the group with the highest rate (four-fifths rule from US EEOC, widely adopted as a starting benchmark).
5. If disparate impact is detected, assess whether the disparity is justified by a legitimate, non-discriminatory factor.
6. Document bias testing methodology, results, and remediation actions.

### Phase 5: NIST AI RMF MAP Function Integration (Week 4)

The NIST AI Risk Management Framework (AI RMF 1.0, January 2023) MAP function identifies the context, capabilities, and potential impacts of AI systems. Integrate the following MAP subcategories:

| Subcategory | Assessment Action |
|-------------|-------------------|
| MAP 1.1 | Document the intended purpose, context of use, and deployment environment |
| MAP 1.2 | Document interdependent and interconnected systems |
| MAP 1.5 | Identify intended users, affected individuals, and stakeholders |
| MAP 1.6 | Assess impacts on individuals, groups, communities, organisations, and society |
| MAP 2.1 | Establish the AI system's knowledge limits and conditions where it may fail |
| MAP 2.2 | Document scientific integrity of training and testing methodologies |
| MAP 2.3 | Assess environmental impact of AI system training and deployment |
| MAP 3.1 | Document potential benefits of the AI system |
| MAP 3.2 | Document potential costs, risks, and negative impacts |
| MAP 3.4 | Map risks specifically to affected communities and stakeholders |
| MAP 3.5 | Document likelihood and severity of identified risks |
| MAP 5.1 | Engage with diverse stakeholders and affected communities |
| MAP 5.2 | Engage with domain experts, AI practitioners, and sociotechnical experts |

### Phase 6: Combined Risk Assessment and Reporting (Week 5-6)

1. Consolidate GDPR DPIA risks, AI Act compliance gaps, and NIST AI RMF findings.
2. For each risk, assess likelihood and severity using the DPIA risk matrix.
3. Identify mitigation measures combining privacy controls and AI governance controls.
4. Calculate residual risk levels.
5. If high-risk AI under the AI Act, prepare conformity assessment documentation.
6. Submit to DPO for Art. 35(2) advice.
7. If residual risk remains high, initiate Art. 36 prior consultation.

## AI-Specific Privacy Risks

| Risk Category | Description | Mitigation Approach |
|---------------|-------------|---------------------|
| Model inversion | Attacker reconstructs training data from model outputs | Differential privacy during training, output perturbation, access controls on model API |
| Membership inference | Attacker determines whether a specific individual's data was in the training set | Regularisation, differential privacy, limiting model confidence scores |
| Data poisoning | Malicious manipulation of training data to bias model outputs | Training data provenance verification, anomaly detection, robust training techniques |
| Concept drift | Model accuracy degrades over time as real-world data distribution changes | Continuous monitoring, automated retraining triggers, human review of edge cases |
| Explanation manipulation | Gaming of AI explanations to hide discriminatory factors | Multiple explanation methods, adversarial testing of explanation consistency |
| Feedback loops | AI decisions create data that reinforces existing biases | Regular bias auditing, human-in-the-loop review, outcome monitoring by demographic group |

## Common Assessment Deficiencies

1. **Treating AI training as a single processing operation**: Each stage (collection, preparation, training, inference) is a distinct processing operation requiring its own lawful basis assessment.
2. **Relying on anonymisation claims without verification**: Data claimed to be anonymised may be re-identifiable through model inversion or linkage attacks.
3. **Inadequate Art. 22 human involvement**: Rubber-stamp human review of AI decisions does not constitute meaningful human involvement.
4. **Ignoring purpose limitation for training data**: Using customer data collected for service delivery to train AI models without compatibility assessment.
5. **No bias testing on protected characteristics**: Fairness assessment limited to overall accuracy without demographic disaggregation.
6. **Static assessment**: AI systems evolve through retraining; the assessment must be updated when the model is retrained or the deployment context changes.

## Enforcement Precedents

- **Italian Garante vs Clearview AI (2022)**: EUR 20 million fine for scraping biometric data from the internet to train facial recognition AI without lawful basis, consent, or DPIA.
- **Italian Garante vs Deliveroo (2021)**: EUR 2.5 million fine for algorithmic management of food delivery riders constituting Art. 22 automated decision-making without adequate safeguards. The algorithm assigned reputation scores and allocated delivery shifts without meaningful human review.
- **Hungarian DPA vs Budapest Bank (2023)**: Fine for automated credit scoring system that used postcode as a proxy for ethnicity without bias impact assessment.
- **CNIL vs Clearview AI (2022)**: EUR 20 million fine; CNIL ordered deletion of all data of French residents and prohibited further collection.
- **Dutch DPA vs Tax Authority (2020)**: EUR 3.7 million fine for algorithmic profiling system (SyRI) that disproportionately targeted ethnic minorities in fraud detection, violating ECHR Art. 8 and Art. 14.
