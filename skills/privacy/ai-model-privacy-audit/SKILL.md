---
name: ai-model-privacy-audit
description: >-
  Conducts privacy auditing of AI models including training data extraction
  testing, membership inference attacks, model inversion testing, and attribute
  inference assessment. Uses ML Privacy Meter and related tools to quantify
  privacy leakage. Keywords: model audit, membership inference, privacy meter,
  model inversion, training data extraction.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "model-audit, membership-inference, privacy-meter, model-inversion, data-extraction, attribute-inference"
---

# AI Model Privacy Audit

## Overview

AI model privacy auditing is the systematic assessment of whether trained ML models leak information about their training data. Models can memorize individual training records, enabling adversaries to extract personal data, determine dataset membership, reconstruct input features, or infer sensitive attributes. This skill implements a comprehensive model privacy audit methodology using established attack techniques and tools (ML Privacy Meter, ART, Foolbox) to quantify privacy leakage before deployment and periodically during operation. The audit results feed directly into the AI DPIA risk assessment and inform mitigation measure selection.

## Privacy Attack Taxonomy

### 1. Training Data Extraction

**Objective**: Extract verbatim or near-verbatim records from the model's training data.

| Attack Vector | Description | Target Models |
|---------------|-------------|---------------|
| Prompt-based extraction | Craft prompts that cause LLMs to regurgitate training data | Language models, generative models |
| Canary extraction | Insert known canary strings into training data and test if model reproduces them | Any model (testing methodology) |
| Gradient-based extraction | Use model gradients to reconstruct training inputs | Models with accessible gradients |
| Generative reconstruction | Use the model as an oracle to iteratively reconstruct training samples | GANs, VAEs, diffusion models |

**Risk Factors Increasing Extraction Likelihood**:
- Large model capacity relative to training data size (overfitting)
- Training data containing duplicated or near-duplicated records
- Longer training duration (more epochs)
- Lower regularisation
- Models with high output granularity (logits, probabilities)

**Testing Methodology**:
1. Insert canary records with unique identifiers into training data
2. Train the model
3. Attempt extraction through various prompting strategies
4. Measure extraction success rate (percentage of canaries recovered)
5. Threshold: extraction rate should be below 0.1% for acceptable risk

### 2. Membership Inference

**Objective**: Determine whether a specific record was in the model's training set.

| Attack Type | Method | Computational Cost |
|-------------|--------|-------------------|
| Shadow model attack | Train shadow models on similar data, build a binary classifier on model outputs | High — requires training multiple shadow models |
| Metric-based attack | Use model confidence, loss, or entropy to distinguish members from non-members | Low — single model query per sample |
| Label-only attack | Use predicted labels (no confidence scores) to infer membership | Medium — requires multiple queries |
| Likelihood ratio attack (LiRA) | Compare per-sample loss to reference distributions | High — most accurate, requires multiple models |

**ML Privacy Meter Implementation**:
- Population metric-based attack: compares target model's loss on a sample against population loss distribution
- Reference metric-based attack: uses reference models to compute per-sample metrics
- Shadow model attack: trains shadow models and uses the attack model to classify members

**Testing Methodology**:
1. Partition data: training set (members) and held-out set (non-members)
2. Run membership inference attacks using ML Privacy Meter
3. Measure attack success: true positive rate at low false positive rate (TPR@FPR=0.1%, 1%)
4. Generate ROC curves per sample and aggregate
5. Threshold: TPR@1%FPR should be below 5% for acceptable privacy

### 3. Model Inversion

**Objective**: Reconstruct input features from model outputs.

| Attack Type | Method | Target |
|-------------|--------|--------|
| Confidence-based inversion | Iteratively optimise input to maximise model confidence for a known label | Classification models |
| Gradient-based inversion | Use model gradients to reconstruct inputs from outputs | White-box models |
| GAN-based inversion | Train a GAN to invert model outputs to input space | Face recognition, image classifiers |

**Testing Methodology**:
1. Select target classes or individuals
2. Run inversion attacks with various initializations
3. Measure reconstruction quality (SSIM, PSNR for images; cosine similarity for embeddings)
4. Assess re-identification risk: can reconstructed data identify specific individuals?
5. Threshold: reconstruction similarity should be below 0.3 (SSIM) for acceptable risk

### 4. Attribute Inference

**Objective**: Infer sensitive attributes not present in the model's output.

| Attack Type | Description |
|-------------|-------------|
| Correlation exploitation | Use correlated features to infer sensitive attributes from model behaviour |
| Partial knowledge attack | Attacker knows some attributes and uses model to infer remaining sensitive ones |
| Group inference | Determine statistical properties of training subgroups |

**Testing Methodology**:
1. Identify sensitive attributes (Art. 9 categories) that may be correlated with model features
2. Train attack models to predict sensitive attributes from model outputs
3. Measure inference accuracy for each sensitive attribute
4. Compare against random baseline
5. Threshold: inference accuracy should not exceed random baseline + 10%

## Audit Methodology

### Phase 1: Audit Scoping (Days 1-3)

1. Define audit scope: which models, what deployment context, what threat model
2. Identify assets: training data, model artefacts, deployment infrastructure
3. Define threat model: who are the adversaries, what access do they have?
   - Black-box: API access only (queries and responses)
   - Grey-box: API access plus model architecture knowledge
   - White-box: Full access to model weights and architecture
4. Select attacks based on threat model and model type
5. Define success criteria (acceptable leakage thresholds)
6. Obtain audit authorisation from model owner and legal

### Phase 2: Environment Setup (Days 4-7)

1. Set up isolated audit environment (no production data leakage)
2. Install audit tools: ML Privacy Meter, ART (Adversarial Robustness Toolbox), custom scripts
3. Obtain model access (API endpoint or model weights depending on threat model)
4. Prepare member/non-member datasets for membership inference
5. Prepare canary data for extraction testing
6. Configure monitoring to log all audit queries

### Phase 3: Attack Execution (Days 8-18)

For each selected attack:
1. Configure attack parameters
2. Execute attack against the target model
3. Collect results (success rates, confidence intervals)
4. Vary attack parameters to find worst-case leakage
5. Document: attack configuration, results, computational cost

### Phase 4: Analysis and Reporting (Days 19-25)

1. Aggregate results across all attacks
2. Calculate privacy risk scores per attack type
3. Identify high-risk data subsets (records most vulnerable to extraction)
4. Cross-reference with DPIA risk register
5. Generate audit report with:
   - Executive summary
   - Attack results per category
   - Risk assessment with GDPR alignment
   - Recommended mitigations
   - Residual risk after proposed mitigations

### Phase 5: Remediation Validation (Days 26-30)

1. If mitigations are applied (differential privacy, output perturbation, etc.)
2. Re-run key attacks to validate mitigation effectiveness
3. Document residual leakage post-mitigation
4. Compare against acceptable thresholds
5. Issue final audit certificate or remediation requirements

## Privacy Leakage Thresholds

| Metric | Acceptable | Elevated | Unacceptable |
|--------|-----------|----------|-------------|
| Membership inference TPR@1%FPR | < 5% | 5-15% | > 15% |
| Training data extraction rate | < 0.1% | 0.1-1% | > 1% |
| Model inversion SSIM | < 0.3 | 0.3-0.6 | > 0.6 |
| Attribute inference accuracy above baseline | < 10% | 10-25% | > 25% |

## Mitigation Measures

| Mitigation | Attacks Mitigated | Trade-off |
|-----------|-------------------|-----------|
| Differential privacy (DP-SGD) | All — provides mathematical guarantee | Model accuracy reduction (calibrate epsilon) |
| Training data deduplication | Extraction, membership inference | One-time preprocessing cost |
| Regularisation (dropout, weight decay) | Membership inference, overfitting-related leakage | May affect model performance |
| Output perturbation | Model inversion, attribute inference | Reduces output precision |
| Confidence score rounding | Metric-based membership inference | Minor output precision loss |
| Model distillation | Extraction, membership inference | Requires additional training |
| Rate limiting | All query-based attacks | Affects legitimate use |
| Input/output PII filtering | Extraction of PII from generative models | May affect model utility |

## Tools and Frameworks

| Tool | Purpose | Source |
|------|---------|--------|
| ML Privacy Meter | Membership inference auditing | github.com/privacytrustlab/ml_privacy_meter |
| IBM ART | Adversarial robustness and privacy testing | github.com/Trusted-AI/adversarial-robustness-toolbox |
| TensorFlow Privacy | Differential privacy training | github.com/tensorflow/privacy |
| Opacus | PyTorch differential privacy | github.com/pytorch/opacus |
| Google DP Library | Differential privacy algorithms | github.com/google/differential-privacy |
| Foolbox | Adversarial attack library | github.com/bethgelab/foolbox |

## Enforcement Relevance

Model privacy auditing is not explicitly required by the GDPR or AI Act, but is effectively mandated through:

- **Art. 35 DPIA**: Risk assessment for AI systems must evaluate privacy leakage risks — auditing is the standard methodology
- **Art. 32 Security**: Appropriate technical measures to ensure security of processing — privacy auditing validates these measures
- **AI Act Art. 9**: Risk management for high-risk AI requires identification and mitigation of privacy risks
- **AI Act Art. 15**: Accuracy, robustness, and cybersecurity requirements — privacy attacks are a cybersecurity concern
- **EDPB Guidelines 04/2025**: Controllers must assess whether AI models have effectively anonymised training data — auditing tests this claim

## Integration Points

- **ai-dpia**: Audit results feed into DPIA Phase 3 risk assessment
- **ai-data-retention**: Audit validates whether deletion from training data is effective
- **ai-deployment-checklist**: Pre-deployment privacy audit is a checklist requirement
- **ai-federated-learning**: Federated learning models require distributed privacy auditing
