---
name: ai-transparency-reqs
description: >-
  Implements AI transparency requirements under EU AI Act Arts. 13-14 and GDPR
  Arts. 13-14. Covers user notification of AI interaction, system capability
  disclosure, limitation documentation, and meaningful information about
  automated logic. Keywords: AI transparency, EU AI Act, GDPR notification,
  explainability, automated decision.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "ai-transparency, eu-ai-act, gdpr-notification, explainability, disclosure, automated-logic"
---

# AI Transparency Requirements

## Overview

AI transparency operates at the intersection of two regulatory frameworks: the GDPR's data subject information rights (Arts. 13-14) and the EU AI Act's transparency obligations (Arts. 13-14, 50). Together they require controllers and deployers to provide meaningful, accessible information about AI system capabilities, limitations, decision logic, and personal data processing. This skill implements the combined transparency framework, addressing both the technical explainability challenge of complex ML models and the legal obligation to communicate AI processing in plain language to affected individuals.

## GDPR Transparency for AI Systems

### Art. 13-14 Information Requirements Applied to AI

When personal data is processed by AI systems, data subjects must receive:

| Information Element | GDPR Article | AI-Specific Application |
|--------------------|-------------|------------------------|
| Purposes of processing | Art. 13(1)(c) / 14(1)(c) | Specific AI use case, not generic "service improvement" |
| Lawful basis | Art. 13(1)(c) / 14(1)(c) | The basis for AI training and for AI inference separately |
| Legitimate interest | Art. 13(1)(d) / 14(2)(b) | The specific interest served by AI processing |
| Recipients | Art. 13(1)(e) / 14(1)(e) | AI infrastructure providers, model hosting services |
| International transfers | Art. 13(1)(f) / 14(1)(f) | Where AI processing occurs (training and inference locations) |
| Retention period | Art. 13(2)(a) / 14(2)(a) | Training data retention, inference log retention, model lifecycle |
| Data subject rights | Art. 13(2)(b) / 14(2)(c) | Including AI-specific rights: explanation, contestation, human review |
| Automated decision-making | Art. 13(2)(f) / 14(2)(g) | Meaningful information about logic, significance, and envisaged consequences |
| Source of data | Art. 14(2)(f) | Training data sources (categories, not necessarily individual sources) |

### Art. 13(2)(f) / 14(2)(g) — Meaningful Information About Automated Logic

This is the most challenging transparency requirement for AI systems. The EDPB and Article 29 Working Party have clarified:

**What "meaningful information about the logic involved" requires:**

1. **System-level explanation**: General description of how the AI system works — what factors are considered, what methodology is used, how the model was trained
2. **Purpose and context**: Why the AI system is used and what role its output plays in decisions
3. **Key variables**: The main data points or features that influence the AI output, without requiring disclosure of proprietary algorithms
4. **Decision criteria**: How the model output translates into a decision (e.g., score thresholds, classification categories)
5. **Significance**: What the decision means for the data subject in practical terms
6. **Consequences**: The potential effects (both intended and foreseeable) of the AI-driven decision

**What it does not require:**

- Full disclosure of source code or model weights
- Mathematical description of the algorithm
- Proprietary trade secrets (but this does not exempt from meaningful explanation)
- Explanation of individual model predictions in real-time (though this may be required under Art. 22)

### Layered Approach to AI Transparency

The EDPB recommends a layered transparency approach:

| Layer | Content | Delivery |
|-------|---------|----------|
| Layer 1: Initial notice | AI is used in processing; general purpose; link to full information | At point of interaction (banner, tooltip, notification) |
| Layer 2: Summary | AI system description, key data used, decision logic summary, rights available | Privacy notice section, AI information page |
| Layer 3: Detailed information | Full technical description, training data categories, fairness measures, accuracy metrics, limitations | Supplementary documentation, upon request |
| Layer 4: Individual explanation | Specific factors influencing a particular decision, appeal mechanism | Upon request or automatically for significant decisions |

## EU AI Act Transparency Obligations

### Art. 13 — Transparency and Provision of Information to Deployers (High-Risk)

High-risk AI systems (Annex III) must be designed and developed to ensure:

| Requirement | Description |
|-------------|-------------|
| Interpretability | System design enables deployers to interpret outputs and use them appropriately |
| Instructions for use | Detailed documentation of capabilities, limitations, intended purpose, foreseeable misuse |
| Performance metrics | Accuracy levels, robustness metrics, known limitations for specific groups |
| Human oversight info | Description of human oversight measures and how to implement them |
| Input data specs | Description of input data the system was designed to process |
| Training data description | Relevant information about training data including provenance and preprocessing |

### Art. 14 — Human Oversight (High-Risk)

High-risk AI systems must be designed to enable effective human oversight:

- Clear indication of AI system outputs and confidence levels
- Ability to correctly interpret AI outputs in context
- Ability to override or reverse AI decisions
- Ability to intervene or stop the system ("stop button")
- Awareness of automation bias risk

### Art. 50 — Transparency for Specific AI Systems

| AI System Type | Transparency Obligation |
|----------------|----------------------|
| AI interacting with persons | Inform that they are interacting with an AI system (unless obvious from context) |
| Emotion recognition / biometric categorisation | Inform about the system's operation and process personal data in compliance with GDPR |
| AI-generated or manipulated content (deepfakes) | Label content as AI-generated in a machine-readable format |
| AI-generated text on matters of public interest | Disclose that the text has been artificially generated or manipulated |

### Art. 50(1) — AI Interaction Notification

Controllers must inform natural persons that they are interacting with an AI system. This applies to:

- Chatbots and virtual assistants
- AI-powered customer service systems
- Automated email or message generation
- AI-driven recommendation systems with direct user interface
- Voice-based AI assistants

Exceptions: where it is obvious from the circumstances and context that the person is interacting with AI (e.g., a robot in a factory setting).

## AI Transparency Documentation Framework

### Model Card Requirements

For each deployed AI model, maintain a model card containing:

| Section | Content |
|---------|---------|
| Model overview | Name, version, type, developer, deployment date |
| Intended use | Specific purpose, target users, deployment context |
| Out-of-scope use | Uses the model is not designed for; foreseeable misuse |
| Training data summary | Data sources (categories), volume, temporal range, geographic scope, known biases |
| Performance metrics | Accuracy, precision, recall, F1 by relevant subgroup; fairness metrics |
| Limitations | Known failure modes, demographic performance disparities, edge cases |
| Privacy properties | Differential privacy applied (epsilon), membership inference test results, training data extraction risk |
| Human oversight | Level of oversight required, reviewer qualifications, override procedures |
| Update history | Retraining dates, data updates, performance changes |

### AI System Transparency Register

Organisations operating multiple AI systems should maintain a central register:

| Field | Description |
|-------|-------------|
| System ID | Unique identifier |
| System name | Human-readable name |
| AI Act classification | Unacceptable / High / Limited / Minimal |
| Purpose | Specific processing purpose |
| Data subjects affected | Categories and estimated numbers |
| Personal data processed | At training and inference |
| Decision authority | AI decision-support vs. automated decision |
| Transparency measures | Notification, explanation, documentation |
| Deployer | Internal / External deployment |
| Registration date | EU AI Act database registration (if high-risk) |

## Explainability Techniques for Compliance

### Global Explainability (System-Level)

Techniques for providing Art. 13(2)(f) "meaningful information about the logic":

| Technique | Best For | Limitation |
|-----------|----------|------------|
| Feature importance (SHAP, LIME) | Identifying key variables | May oversimplify complex interactions |
| Decision rules extraction | Converting model logic to human-readable rules | Loss of accuracy for complex models |
| Partial dependence plots | Showing how features affect predictions | Assumes feature independence |
| Counterfactual explanations | Showing what change would lead to different outcome | Computationally expensive for many features |
| Attention visualisation | Transformer models — showing what the model focuses on | Attention does not always equal importance |

### Local Explainability (Individual Decision)

For Art. 22 right to explanation of individual decisions:

| Technique | Description | Use Case |
|-----------|-------------|----------|
| LIME | Local Interpretable Model-agnostic Explanations | Any model — approximate local behaviour with interpretable model |
| SHAP values | Shapley Additive Explanations for individual predictions | Feature contribution to specific prediction |
| Counterfactual | "You were denied because X; if X were Y, outcome would be different" | Credit, hiring, insurance decisions |
| Anchors | Sufficient conditions for a prediction | Rule-based explanation of individual case |
| Concept-based | High-level concepts that influenced the decision | When features are not directly interpretable |

## Enforcement Precedents

- **Garante v. OpenAI (2023)**: Required transparency about AI training data processing, model capabilities, and limitations — privacy notice deemed insufficient for AI system transparency.
- **CNIL v. Clearview AI (SAN-2022-019, 2022)**: EUR 20M fine — complete absence of transparency about facial recognition AI processing; data subjects had no notice their images were scraped and processed.
- **Austrian DPA v. CRIF (DSB-D213.636, 2023)**: Credit scoring AI — insufficient explanation of automated decision-making logic per Art. 13(2)(f); data subject received only a score without meaningful information about factors.
- **Dutch DPA v. Tax Authority (SyRI, 2020)**: Court found algorithmic fraud detection lacked transparency — citizens could not understand how the system assessed them, violating right to private life.
- **AEPD v. CaixaBank (PS/00421/2020, 2021)**: EUR 6M fine — automated credit decision-making without adequate transparency about the logic involved and significance for data subjects.

## Integration Points

- **ai-automated-decisions**: Art. 22 explanation requirements integrate with transparency obligations
- **ai-dpia**: Transparency assessment is part of DPIA necessity and proportionality analysis
- **ai-act-high-risk-docs**: Art. 13 AI Act documentation requirements overlap with transparency framework
- **ai-deployment-checklist**: Pre-deployment transparency validation is a checklist item
