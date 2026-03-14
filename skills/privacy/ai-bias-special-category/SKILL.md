---
name: ai-bias-special-category
description: >-
  Assesses AI bias risks for GDPR Art. 9 special category data and AI Act
  Art. 10 data governance. Covers fairness metrics, bias detection methods,
  mitigation strategies, and documentation requirements for protected
  characteristics. Keywords: AI bias, special category, fairness metrics,
  discrimination, Art. 9, Art. 10.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "ai-bias, special-category, fairness-metrics, discrimination, art-9, data-governance"
---

# AI Bias Assessment for Special Category Data

## Overview

AI systems can amplify, perpetuate, or introduce bias against protected groups defined by GDPR Art. 9 special categories (race, ethnicity, political opinion, religion, trade union membership, genetic data, biometric data, health, sexual orientation) and by EU equality law (gender, age, disability). The AI Act Art. 10 requires data governance practices for training data that address bias, while Art. 5 prohibits AI-based social scoring. This skill provides the methodology for detecting, measuring, and mitigating bias in AI systems that process or infer special category data, with documentation requirements meeting both GDPR and AI Act obligations.

## Art. 9 Special Categories and AI Bias

### Direct Processing of Special Category Data

When AI systems directly process Art. 9 data:

| Category | AI Bias Risk | Example |
|----------|-------------|---------|
| Racial or ethnic origin | Discrimination in hiring, credit, policing | CV screening penalising names associated with ethnic minorities |
| Political opinions | Political profiling, content suppression | News recommendation amplifying or suppressing political viewpoints |
| Religious beliefs | Service denial, discriminatory targeting | Insurance pricing varying by religious affiliation |
| Trade union membership | Employment discrimination | Performance scoring penalising union activity |
| Genetic data | Genetic discrimination in insurance/employment | Health insurance pricing based on genetic predisposition |
| Biometric data | Differential accuracy across demographics | Facial recognition with higher error rates for darker skin tones |
| Health data | Health-based discrimination | Hiring algorithms penalising disability or mental health history |
| Sexual orientation | Discrimination, outing | Content recommendation inadvertently revealing sexual orientation |

### Proxy Inference of Special Categories

AI models frequently infer Art. 9 data from non-sensitive features:

| Proxy Feature | Inferred Category | Mechanism |
|---------------|-------------------|-----------|
| Postcode/zip code | Race/ethnicity, income | Residential segregation patterns |
| First/last name | Race/ethnicity, religion | Name-ethnicity correlations |
| Browsing history | Political opinion, religion, health | Content consumption patterns |
| Purchase history | Health status, religion | Medication purchases, dietary products |
| Language patterns | National origin, education | Dialect, vocabulary, grammar patterns |
| Device/app usage | Age, income, disability | Accessibility features, device type |

EDPB position: inferring Art. 9 data from non-sensitive inputs constitutes processing of special category data — the same protections apply.

## Fairness Metrics

### Group Fairness Metrics

| Metric | Definition | When to Use |
|--------|-----------|-------------|
| Demographic parity | P(positive outcome | group A) = P(positive outcome | group B) | When equal selection rates are desired regardless of qualification |
| Equalized odds | TPR and FPR equal across groups | When accuracy should be equal across groups |
| Equal opportunity | TPR equal across groups (relaxed equalized odds) | When true positive detection should be equal |
| Calibration | P(Y=1 | score=s, group=A) = P(Y=1 | score=s, group=B) | When scores should mean the same thing across groups |
| Predictive parity | PPV equal across groups | When positive predictions should be equally reliable |

### Individual Fairness Metrics

| Metric | Definition |
|--------|-----------|
| Consistency | Similar individuals receive similar outcomes |
| Counterfactual fairness | Outcome would be the same if protected attribute were different |
| Causal fairness | No causal path from protected attribute to outcome |

### Metric Selection Guidance

| Decision Context | Recommended Metric | Justification |
|-----------------|-------------------|---------------|
| Hiring/admissions | Equalized odds or equal opportunity | Equal detection of qualified candidates across groups |
| Credit scoring | Calibration | Score should mean the same probability regardless of group |
| Criminal risk | Equalized odds | Both FPR and TPR should be equal to avoid disproportionate impact |
| Healthcare | Equal opportunity + calibration | Equal detection of conditions; equal meaning of risk scores |
| Content moderation | Demographic parity | Content removal should not disproportionately affect groups |

Note: Mathematical impossibility results show that demographic parity, equalized odds, and calibration cannot all be satisfied simultaneously when base rates differ across groups. Document the trade-off explicitly.

## Bias Detection Methodology

### Phase 1: Data Audit

1. Profile training data demographics against target population
2. Identify underrepresented groups that may have lower model performance
3. Check for historical bias in labelled data (e.g., biased hiring decisions used as ground truth)
4. Identify label noise differential across groups
5. Assess feature distributions across groups for proxy discrimination potential

### Phase 2: Model Testing

1. Evaluate model performance disaggregated by protected groups
2. Compute selected fairness metrics for each protected group pair
3. Run counterfactual testing: change protected attributes, observe output changes
4. Test for intersectional bias (combinations of protected attributes)
5. Evaluate model performance on edge cases and adversarial examples per group

### Phase 3: Output Analysis

1. Analyse decision distribution across groups
2. Identify threshold effects that disproportionately impact specific groups
3. Test for feedback loop amplification over time
4. Assess output explanation fairness (are explanations equally informative across groups?)

## Bias Mitigation Strategies

### Pre-processing (Data-Level)

| Strategy | Description | Trade-off |
|----------|-------------|-----------|
| Resampling | Over-sample underrepresented groups, under-sample overrepresented | May reduce data diversity or introduce duplicates |
| Reweighting | Assign higher weights to underrepresented group samples | Computationally simple; may not address structural bias |
| Relabelling | Correct historically biased labels | Requires domain expertise; may be subjective |
| Fair representation learning | Learn latent representation that removes protected attribute information | May lose legitimate correlations |

### In-processing (Algorithm-Level)

| Strategy | Description | Trade-off |
|----------|-------------|-----------|
| Adversarial debiasing | Train adversary to predict protected attribute from model; penalise success | Accuracy-fairness trade-off; requires protected attribute data |
| Fairness constraints | Add fairness metric as training constraint | May reduce overall accuracy; constraint satisfaction varies |
| Regularisation | Add fairness-related regularisation term to loss function | Balances accuracy and fairness; requires tuning |
| Causal modelling | Use causal graph to block discriminatory paths | Requires causal knowledge; complex to implement |

### Post-processing (Output-Level)

| Strategy | Description | Trade-off |
|----------|-------------|-----------|
| Threshold adjustment | Different decision thresholds per group to equalise metrics | May be perceived as unfair; legally complex |
| Score calibration | Calibrate scores per group | Requires sufficient group data; may reduce discrimination |
| Reject option | Abstain from decision for borderline cases across groups | Reduces coverage; requires human fallback |

## AI Act Art. 10 Data Governance

Art. 10 requires for high-risk AI training data:

| Requirement | Implementation |
|-------------|---------------|
| Relevant data | Training data must be relevant to the intended purpose |
| Sufficiently representative | Data must represent the population the system will be deployed on |
| Free of errors | Data quality assessment and cleaning processes |
| Complete | Sufficient coverage of deployment scenarios |
| Appropriate statistical properties | Distribution analysis including demographic representation |
| Bias examination | Examine training data for possible biases, especially related to Art. 10(2)(f) |

Art. 10(5): Processing of special category data for bias detection is permitted for high-risk AI if:
- Strictly necessary for bias monitoring, detection, and correction
- Subject to appropriate safeguards (pseudonymisation, access controls)
- Data is not used for other purposes
- Deleted after bias assessment unless retention is required for compliance documentation

## Documentation Requirements

### Bias Assessment Report

| Section | Content |
|---------|---------|
| System description | Model, purpose, affected groups |
| Protected attributes assessed | Art. 9 categories + equality law characteristics |
| Fairness metrics selected | With justification for selection |
| Data audit results | Training data demographics, representation gaps |
| Model testing results | Per-group performance, fairness metrics, counterfactual results |
| Bias findings | Identified disparities with severity assessment |
| Mitigation measures | Applied strategies with effectiveness evidence |
| Residual bias | Remaining disparities after mitigation |
| Trade-off documentation | Accuracy-fairness trade-offs, metric impossibility acknowledgement |
| Ongoing monitoring plan | Post-deployment fairness monitoring |

## Enforcement Precedents

- **Dutch Tax Authority (SyRI, 2020)**: Court struck down algorithmic fraud detection for discriminatory profiling — system disproportionately targeted residents of low-income, immigrant-background neighbourhoods.
- **Italian DPA v. Deliveroo (2021)**: Algorithmic worker management found to discriminate based on protected characteristics — Art. 22 and equality law violations.
- **Austrian DPA v. AMS Algorithm (2020)**: Austrian employment service algorithm that scored job seekers lower based on gender, age, disability, and citizenship — DPA found processing unlawful.
- **AEPD guidance (2021)**: Spanish DPA issued guidance on algorithmic discrimination, emphasising DPIA requirement for AI systems processing protected characteristics.
- **CNIL (2024)**: AI bias assessment framework published requiring fairness testing for high-impact AI systems.

## Integration Points

- **ai-dpia**: Bias assessment feeds into DPIA risk assessment for discrimination harms
- **ai-automated-decisions**: Biased automated decisions trigger Art. 22 and equality law violations
- **ai-training-lawfulness**: Art. 10(5) processing of special category data for bias detection requires documentation
- **ai-transparency-reqs**: Bias findings should be disclosed in model cards and transparency documentation
- **ai-act-high-risk-docs**: Art. 10 data governance documentation is part of conformity assessment
