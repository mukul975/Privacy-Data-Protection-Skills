---
name: ai-vendor-privacy-due
description: >-
  Determines controller-processor relationships for AI services and conducts
  privacy due diligence. Covers SaaS AI (processor), embedded AI (joint
  controller), API-based AI (assessment framework), and vendor risk
  assessment. Keywords: AI vendor, controller-processor, due diligence,
  SaaS AI, joint controller, Art. 28.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "ai-vendor, controller-processor, due-diligence, saas-ai, joint-controller, art-28"
---

# AI Vendor Privacy Due Diligence

## Overview

AI services create complex controller-processor relationships that differ significantly from traditional data processing arrangements. Whether an AI vendor is a processor, joint controller, or independent controller depends on the degree of autonomy the vendor has over personal data processing — particularly regarding model training on customer data, data retention for model improvement, and the vendor's independent purposes for the data. This skill provides the framework for determining controller-processor roles in AI service relationships, conducting privacy due diligence on AI vendors, and establishing appropriate contractual protections.

## Controller-Processor Determination for AI

### Decision Framework

| AI Service Model | Typical Role | Key Factors | GDPR Article |
|-----------------|-------------|-------------|-------------|
| **SaaS AI — Customer data processed per instructions** | Vendor = Processor | Vendor processes data solely on controller's instructions; no independent use | Art. 28 DPA required |
| **SaaS AI — Customer data used for model training** | Vendor = Joint Controller or Independent Controller | Vendor uses customer data for own model improvement beyond contracted service | Art. 26 JCA or separate controller notice |
| **Embedded AI — Pre-trained model in customer infrastructure** | Customer = Controller; Vendor = may be processor for support | Model runs in customer environment; vendor may access data for support/updates | Art. 28 if vendor accesses data |
| **API-based AI — Customer sends data for inference** | Vendor = Processor (if no data retention) or Joint Controller (if training on inputs) | Depends on whether vendor retains, uses, or trains on input data | Assessment required |
| **AI Platform — Customer builds models on vendor platform** | Vendor = Processor for infrastructure; Controller for platform data | Vendor provides compute; customer controls data and model | Art. 28 DPA + audit rights |
| **AI Marketplace — Pre-built models with customer data** | Depends on data flow | If customer data enters vendor model → joint controller assessment | Case-by-case |

### Key Determination Questions

1. **Who determines the purpose of processing?** — The entity deciding *why* personal data is processed
2. **Who determines the means of processing?** — The entity deciding *how* data is processed (but "non-essential means" may be delegated to processor)
3. **Does the vendor use data for its own purposes?** — Model training, benchmarking, product improvement using customer data
4. **Does the vendor retain data beyond service delivery?** — Data kept after inference, stored for training, retained in logs
5. **Does the vendor make independent decisions about the data?** — Choosing to train models, sharing with sub-processors not instructed by customer

### Common AI Vendor Patterns

#### Pattern 1: Pure Inference API (Vendor = Processor)
- Customer sends data; receives inference result
- Vendor does not retain input data beyond processing
- Vendor does not train on customer data
- Vendor acts solely on customer's instructions
- **Contractual**: Art. 28 DPA with clear scope

#### Pattern 2: AI with Model Improvement (Vendor = Joint Controller)
- Customer sends data; receives inference result
- Vendor retains data to improve its models
- Vendor determines that model training is a purpose
- Both parties benefit from the model improvement
- **Contractual**: Art. 26 Joint Controller Agreement

#### Pattern 3: AI with Anonymised Analytics (Assessment Required)
- Customer sends data; receives inference result
- Vendor claims to anonymise data and use aggregated analytics
- If anonymisation is effective: no personal data processing for analytics
- If anonymisation is not effective (re-identification possible): vendor is controller for analytics
- **Assessment**: Verify anonymisation effectiveness per WP216

#### Pattern 4: Embedded AI with Telemetry (Vendor = Processor + may be Controller)
- AI model runs in customer environment
- Vendor collects telemetry data including model performance
- If telemetry contains personal data: vendor may be controller for telemetry processing
- **Contractual**: Art. 28 DPA for model support + separate arrangement for telemetry

## Due Diligence Assessment Framework

### Phase 1: Vendor AI Processing Inventory

For each AI vendor, document:

| Element | Documentation Required |
|---------|----------------------|
| AI capabilities | What AI functions does the vendor provide? |
| Personal data inputs | What personal data is sent to the vendor? |
| Personal data outputs | What personal data does the vendor return? |
| Data retention | Does the vendor retain input data? For how long? |
| Model training | Does the vendor train on customer data? |
| Sub-processors | Does the vendor use sub-processors for AI processing? Where? |
| Data location | Where is AI processing performed? What jurisdictions? |
| Security measures | What security controls protect data during AI processing? |
| Human review | Does vendor personnel access customer data? |

### Phase 2: Privacy Risk Assessment

| Risk Factor | Assessment | Risk Level |
|-------------|-----------|-----------|
| Data sensitivity | Special category data sent to AI vendor? | |
| Data volume | Volume of personal data processed by vendor | |
| Vendor data use | Vendor uses customer data for own purposes? | |
| International transfers | Data processed outside EU/EEA? | |
| Sub-processor chain | Number and location of sub-processors | |
| Security posture | Certifications (ISO 27001, SOC 2)? | |
| Incident history | Prior data breaches or enforcement actions? | |
| AI-specific risks | Model memorization, output leakage, bias? | |

### Phase 3: Contractual Assessment

| Contractual Element | Required? | Status |
|--------------------|-----------|--------|
| Art. 28 DPA or Art. 26 JCA | Yes | |
| Processing scope and purpose limitation | Yes | |
| Prohibition on data use beyond instructions (if processor) | Yes | |
| Model training opt-out | Yes (if vendor trains on data) | |
| Sub-processor notification and approval | Yes | |
| International transfer safeguards | If applicable | |
| Data deletion on termination | Yes | |
| Audit rights | Yes | |
| Breach notification obligations | Yes | |
| AI-specific: model privacy testing | Recommended | |
| AI-specific: bias assessment obligations | Recommended for high-risk | |
| AI-specific: output accuracy warranties | Recommended | |

## AI-Specific Contractual Clauses

### Model Training Restrictions

```
The Processor shall not use Customer Data to train, improve, fine-tune, or
otherwise develop any machine learning model, algorithm, or AI system,
whether for the Customer's benefit or for any other purpose, without prior
written consent from the Customer. Any consent granted shall specify the
scope of permitted training, the data categories involved, and the privacy
safeguards to be applied.
```

### AI Output Accuracy

```
The Provider acknowledges that AI system outputs about identifiable data
subjects must comply with the accuracy principle under Art. 5(1)(d) GDPR.
The Provider shall implement measures to minimise inaccurate outputs about
data subjects and shall promptly correct inaccurate outputs upon
notification.
```

### Model Privacy and Bias Obligations

```
The Provider shall conduct periodic privacy audits of AI models processing
Customer Data, including membership inference testing and training data
extraction testing, and shall make results available to the Customer upon
request. The Provider shall monitor AI systems for discriminatory outcomes
and shall implement bias mitigation measures as required.
```

## Enforcement Relevance

- **EDPB Guidelines 07/2020 on Controller-Processor**: Determination depends on factual circumstances, not contractual labels. A vendor labelled "processor" that uses data for its own purposes is factually a controller.
- **Garante v. OpenAI (2023)**: OpenAI's role as controller for ChatGPT training data confirmed — processing personal data for model training is an independent controller purpose.
- **CJEU C-40/17 (Fashion ID)**: Joint controller status can arise when a party has influence over the purpose and means of processing, even without access to the data.
- **DPC v. Meta (WhatsApp, 2023)**: EUR 5.5M fine — processor-controller determination must reflect actual data use, not just contractual terms.

## Integration Points

- **ai-dpia**: Vendor AI processing must be included in DPIA scope
- **ai-training-lawfulness**: Vendor training on customer data requires lawful basis assessment
- **ai-transparency-reqs**: Data subjects must be informed about AI vendor processing
- **ai-deployment-checklist**: Vendor due diligence is a pre-deployment checklist item
