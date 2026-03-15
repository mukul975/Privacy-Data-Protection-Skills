---
name: llm-output-privacy-risk
description: >-
  Assessing privacy risks in large language model outputs including training
  data memorisation, PII leakage in generated text, prompt injection leading
  to data extraction, and hallucinated personal data. Covers output filtering,
  guardrails, and monitoring. Keywords: LLM privacy, output risk, memorisation,
  PII leakage, prompt injection, hallucinated PII.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "llm-privacy, output-risk, pii-leakage, memorisation, prompt-injection, hallucinated-pii"
---

# LLM Output Privacy Risk Assessment

## Overview

Large language models (LLMs) present unique privacy risks that go beyond traditional ML systems. Because LLMs are trained on massive corpora that may contain personal data, they can memorise and reproduce verbatim training data — including names, email addresses, phone numbers, and other PII. Additionally, LLMs can hallucinate plausible but false personal data, creating defamation and accuracy risks. Prompt injection attacks can bypass safety guardrails to extract training data or system prompts containing confidential information. This skill provides a structured framework for assessing, mitigating, and monitoring privacy risks in LLM-generated outputs at Cerebrum AI Labs.

## LLM Output Privacy Risk Categories

### Risk 1: Training Data Memorisation

LLMs memorise training data, particularly sequences that appear multiple times or are distinctive. Extractable memorisation occurs when a model, given a prefix, completes the text with verbatim training data.

| Factor | Impact on Memorisation Risk |
|--------|---------------------------|
| Model size | Larger models memorise more (Carlini et al., 2023) |
| Data duplication | Repeated sequences are memorised at higher rates |
| Training epochs | More passes over data increase memorisation |
| Data distinctiveness | Unique sequences (names, numbers) are more extractable |
| Temperature at inference | Lower temperature increases verbatim reproduction |

**Regulatory concern**: If a model reproduces personal data from training, this constitutes processing under GDPR Art. 4(2). The data subject has not consented to this output, and the controller must have a lawful basis for the disclosure.

### Risk 2: PII Leakage in Generated Text

Even without verbatim memorisation, models can combine partial information to produce outputs containing personal data — email patterns, phone number formats with real area codes, or names associated with specific contexts.

| Leakage Type | Example | Detection Method |
|-------------|---------|-----------------|
| Verbatim reproduction | Model outputs exact email address from training data | Exact match against known training PII |
| Recombination | Model combines real first name + real surname from different records | Named entity recognition + cross-reference |
| Pattern completion | Model generates plausible phone number matching real format | Regex + validation against real registries |
| Contextual leakage | Model associates real person with correct employer when prompted | Entity relationship extraction |

### Risk 3: Prompt Injection and Data Extraction

Adversarial prompts can cause models to bypass safety instructions and output training data, system prompts, or information about other users' conversations.

| Attack Vector | Description | Mitigation |
|--------------|-------------|------------|
| Direct prompt injection | User crafts prompt to extract training data ("Repeat your training data starting with...") | Input filtering + output monitoring |
| Indirect prompt injection | Malicious content in retrieved documents instructs model to leak data | Sanitise retrieved content + instruction hierarchy |
| System prompt extraction | Prompts designed to reveal system-level instructions | System prompt isolation + extraction detection |
| Multi-turn extraction | Gradual extraction across conversation turns | Conversation-level monitoring |
| Jailbreaking | Bypassing safety alignment to disable PII filters | Robust alignment + secondary output filter |

### Risk 4: Hallucinated Personal Data

LLMs can generate plausible but fabricated personal data — attributing false statements to real people, inventing credentials, or creating fictional but realistic-seeming personal records.

| Hallucination Type | Privacy Risk | Legal Concern |
|-------------------|-------------|---------------|
| False attribution | Model attributes a statement to a real person who never said it | Defamation, Art. 5(1)(d) accuracy principle |
| Fabricated credentials | Model invents qualifications for a real person | Accuracy, potential reputational harm |
| Fictional PII | Model generates realistic but fake personal details (e.g., social security numbers) | May match real individuals by coincidence |
| Confabulated relationships | Model invents relationships between real people | Art. 5(1)(d) accuracy, potential harm |

**EDPB position**: EDPB Guidelines 04/2025 state that generating inaccurate personal data about identifiable individuals violates the accuracy principle (Art. 5(1)(d)) and may require the controller to implement effective rectification mechanisms.

## Output Privacy Risk Assessment Framework

### Assessment Dimensions

| Dimension | Weight | Scoring Criteria |
|-----------|--------|-----------------|
| Memorisation exposure | 25% | Model size, training data PII density, deduplication status |
| PII leakage likelihood | 25% | Output modality, user interaction pattern, PII filter coverage |
| Prompt injection resilience | 20% | Input validation, instruction hierarchy, extraction testing results |
| Hallucination risk | 15% | Factual grounding, attribution verification, entity linking |
| Monitoring coverage | 15% | Real-time PII detection, logging, alerting, human review |

### Risk Scoring

| Score Range | Risk Level | Action Required |
|-------------|-----------|-----------------|
| 0-20 | Low | Standard monitoring; annual review |
| 21-40 | Moderate | Enhanced PII filtering; quarterly review |
| 41-60 | Elevated | Mandatory output scanning; human review for sensitive queries |
| 61-80 | High | Restrict deployment scope; implement guardrails before production |
| 81-100 | Critical | Do not deploy; fundamental architecture changes required |

## Mitigation Measures

### Pre-Deployment Mitigations

| Measure | Description | Effectiveness |
|---------|-------------|---------------|
| Training data deduplication | Remove duplicate sequences to reduce memorisation | High for verbatim memorisation |
| PII scrubbing of training data | Detect and remove/mask PII before training | High but incomplete (novel PII patterns missed) |
| Differential privacy training | Train with DP-SGD to bound memorisation | High theoretical guarantee; accuracy trade-off |
| RLHF safety alignment | Train model to refuse PII-generating requests | Moderate; can be bypassed by jailbreaking |
| Instruction tuning | Fine-tune model to follow safety instructions | Moderate; requires robust instruction hierarchy |

### Runtime Mitigations

| Measure | Description | Effectiveness |
|---------|-------------|---------------|
| Output PII scanner | NER-based scanner detecting PII in outputs before delivery | High for known PII patterns |
| Regex PII filter | Pattern matching for emails, phones, SSNs, credit cards | High for structured PII |
| Input prompt classifier | Classify incoming prompts for injection/extraction attempts | Moderate; adversarial prompts evolve |
| Retrieval grounding | Ground outputs in retrieved documents to reduce hallucination | Moderate; depends on retrieval quality |
| Rate limiting | Limit query volume to slow extraction attacks | Low-moderate; raises cost of attack |
| Conversation monitoring | Analyse multi-turn conversations for progressive extraction | Moderate; complex to implement |

### Post-Deployment Monitoring

| Monitor | Metric | Alert Threshold |
|---------|--------|----------------|
| PII detection rate | % of outputs flagged by PII scanner | >0.1% of outputs in any 1-hour window |
| Prompt injection detection | % of inputs classified as injection attempts | >0.5% of inputs in any 1-hour window |
| User reports of PII exposure | Count of user-reported PII incidents | Any confirmed report |
| Extraction pattern detection | Repeated similar queries from same user/IP | >10 similar extraction-pattern queries per session |
| Hallucination complaints | Reports of false personal information | Any confirmed report about real individuals |

## Cerebrum AI Labs — LLM Output Privacy Controls

### Architecture

```
User Input → Input Filter → LLM → Output PII Scanner → Delivery
                │                         │
                ▼                         ▼
         Prompt Injection          PII Detected?
         Classifier                  │
                │                YES → Redact + Log + Alert
             Block/Allow         NO  → Deliver + Log
```

### PII Detection Categories for Output Scanning

| PII Type | Detection Method | Action on Detection |
|----------|-----------------|-------------------|
| Email addresses | Regex + validation | Redact and log |
| Phone numbers | Regex + country format validation | Redact and log |
| National ID numbers | Country-specific regex patterns | Block output + alert |
| Credit card numbers | Luhn algorithm + regex | Block output + alert |
| Physical addresses | NER + geocoding validation | Redact and log |
| Person names + context | NER + co-occurrence with other PII | Flag for review |
| Medical information | Medical NER + PHI patterns | Block output + alert |

## Enforcement Relevance

- **EDPB Guidelines 04/2025**: Controllers deploying LLMs must assess memorisation risk and implement measures to prevent unlawful disclosure of personal data in outputs.
- **Garante v. OpenAI (2023)**: Italian DPA ordered temporary ban partly due to lack of age verification and data accuracy concerns in ChatGPT outputs. Required implementation of output filtering.
- **EDPB ChatGPT Taskforce Report (2024)**: Recommended that LLM providers implement technical measures to minimise inaccurate personal data in outputs and provide effective rectification mechanisms.
- **CNIL AI Action Plan (2024)**: French DPA guidance emphasises that LLM outputs containing personal data constitute processing, requiring lawful basis and compliance with data quality principles.

## Integration Points

- **ai-model-privacy-audit**: Memorisation testing is part of the model privacy audit
- **ai-data-subject-rights**: Rectification of hallucinated data, erasure requests
- **ai-transparency-reqs**: Disclosure that system is AI-generated, accuracy limitations
- **ai-deployment-checklist**: Output privacy controls verified before deployment
