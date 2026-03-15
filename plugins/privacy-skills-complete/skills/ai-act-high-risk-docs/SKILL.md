---
name: ai-act-high-risk-docs
description: >-
  Preparing EU AI Act compliance documentation for high-risk AI systems.
  Covers Annex III classification, technical documentation under Art. 11,
  conformity assessment, risk management systems, and CE marking requirements.
  Keywords: EU AI Act, high-risk AI, Annex III, conformity assessment, CE marking.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: ai-privacy-governance
  tags: "eu-ai-act, high-risk-ai, annex-iii, conformity-assessment, technical-documentation"
---

# EU AI Act High-Risk AI System Documentation

## Overview

The EU AI Act (Regulation 2024/1689, entered into force 1 August 2024, with high-risk obligations applicable from 2 August 2026) establishes a risk-based regulatory framework for artificial intelligence systems. High-risk AI systems — those listed in Annex III or used as safety components of products covered by Union harmonisation legislation in Annex I — must meet extensive documentation, transparency, and governance requirements before being placed on the EU market. Cerebrum AI Labs must prepare comprehensive technical documentation, implement a risk management system, ensure data governance, and undergo conformity assessment for each high-risk AI system.

## High-Risk Classification

### Annex III Categories Relevant to Cerebrum AI Labs

| Category | Annex III Reference | Cerebrum AI Labs System | Classification |
|----------|-------------------|------------------------|---------------|
| Employment and workers management | Annex III, para. 4(a) | CV Screening AI — automated filtering of job applications | High-risk |
| Access to essential services | Annex III, para. 5(b) | Credit Scoring AI — creditworthiness assessment for financial products | High-risk |
| Law enforcement | Annex III, para. 6(a) | Not applicable | N/A |
| Biometric identification | Annex III, para. 1(a) | Facial Verification AI — identity verification at onboarding | High-risk |
| Education and vocational training | Annex III, para. 3(a) | Not applicable | N/A |

### Classification Decision Tree

```
Is the AI system listed in Annex III?
├── Yes → High-risk (unless exception applies under Art. 6(3))
│   └── Does the system make decisions materially affecting natural persons?
│       ├── Yes → High-risk confirmed
│       └── No → May qualify for Art. 6(3) exception (narrow, profiling, preparatory)
│
├── No → Is it a safety component of a product under Annex I legislation?
│   ├── Yes → High-risk (subject to third-party conformity assessment)
│   └── No → Not high-risk under AI Act
│
└── Is it a general-purpose AI model with systemic risk? (Art. 51)
    ├── Yes → GPAI systemic risk obligations
    └── No → GPAI transparency obligations only
```

## Technical Documentation Requirements (Art. 11)

### Annex IV — Required Documentation Content

**Section 1: General Description**

| Document Element | Content for Cerebrum AI Labs CV Screening AI |
|-----------------|----------------------------------------------|
| Intended purpose | Automated screening and ranking of job applications based on qualification match |
| Provider name and contact | Cerebrum AI Labs, 42 Innovation Drive, Dublin, Ireland |
| AI system version | v2.4.1 (deployed March 2026) |
| Hardware/software requirements | Cloud-hosted on EU infrastructure (AWS eu-west-1), Python 3.11, PyTorch 2.2 |
| Product integration | Integrated into Cerebrum TalentFlow ATS platform |

**Section 2: Detailed Description of System Elements**

| Element | Documentation Required |
|---------|----------------------|
| Development methodology | Model architecture, training approach, design choices and rationale |
| Computational resources | Training compute (GPU hours), energy consumption |
| Training data | Data sources, collection methods, size, labeling methodology, preprocessing |
| Validation and testing | Test datasets, metrics, results, known limitations |
| Input data specifications | Expected input format, quality requirements |
| Output description | Output format, confidence scores, decision thresholds |

**Section 3: Monitoring, Functioning, and Control**

| Element | Documentation Required |
|---------|----------------------|
| Human oversight measures | Art. 14 requirements: override capability, decision review process |
| Technical measures for accuracy | Accuracy metrics, drift detection, retraining triggers |
| Cybersecurity measures | Data encryption, access controls, adversarial robustness testing |
| Performance in edge cases | Known failure modes, boundary conditions, degradation behavior |

**Section 4: Risk Management**

| Element | Documentation Required |
|---------|----------------------|
| Risk management system | Art. 9 risk management process documentation |
| Known and foreseeable risks | Risk register with severity and likelihood |
| Mitigation measures | Controls for each identified risk |
| Residual risk assessment | Acceptable residual risk justification |

## Risk Management System (Art. 9)

### Continuous Risk Management Process for Cerebrum AI Labs

| Phase | Activity | Frequency |
|-------|----------|-----------|
| Identification | Identify risks to health, safety, and fundamental rights | Initial + quarterly |
| Analysis | Estimate risk severity and likelihood | Initial + quarterly |
| Evaluation | Compare risks against acceptance criteria | Initial + quarterly |
| Mitigation | Implement risk reduction measures | Ongoing |
| Monitoring | Track risk indicators in production | Continuous |
| Review | Review and update risk assessment | Quarterly |

### Risk Register — CV Screening AI

| Risk ID | Risk Description | Severity | Likelihood | Mitigation | Residual Risk |
|---------|-----------------|----------|------------|------------|--------------|
| R-001 | Gender bias in screening recommendations | High | Medium | Bias testing on protected attributes, debiasing training data | Low |
| R-002 | Discrimination against non-native language speakers | High | Medium | Multilingual evaluation, language-agnostic features | Medium |
| R-003 | Over-reliance on AI recommendations by recruiters | Medium | High | Mandatory human review, confidence thresholds | Low |
| R-004 | Inaccurate qualification matching for novel job roles | Medium | Medium | Fallback to keyword matching, human review flag | Low |
| R-005 | Privacy breach via training data memorization | High | Low | Differential privacy in training, memorization audit | Low |

## Data Governance (Art. 10)

### Training Data Requirements

| Requirement | Implementation at Cerebrum AI Labs |
|-------------|-----------------------------------|
| Relevance and representativeness | Training data sourced from 50,000 job applications across 12 EU countries, balanced by gender, age, nationality |
| Bias examination | Statistical parity analysis on protected attributes (gender, age, ethnicity, disability) before and after training |
| Gap identification | Identified underrepresentation of applicants with disabilities; augmented with synthetic examples |
| Data quality | Automated data quality checks: completeness >95%, label accuracy >98% (human-verified sample) |
| Personal data processing | DPIA completed (DPIA-AI-2026-001); lawful basis: Art. 6(1)(f) legitimate interest; special categories removed |

## Conformity Assessment (Art. 43)

### Assessment Procedure for Cerebrum AI Labs

| System | Assessment Type | Basis |
|--------|----------------|-------|
| CV Screening AI | Internal conformity assessment (Art. 43(2)) + quality management system | Annex III, para. 4 — not biometric, not critical infrastructure |
| Credit Scoring AI | Internal conformity assessment (Art. 43(2)) | Annex III, para. 5 |
| Facial Verification AI | Third-party conformity assessment (Art. 43(1)) via notified body | Annex III, para. 1 — biometric identification |

### Internal Conformity Assessment Steps

1. Verify quality management system is established (Art. 17)
2. Prepare technical documentation per Annex IV
3. Conduct risk management assessment per Art. 9
4. Verify data governance per Art. 10
5. Verify transparency and information provision per Art. 13
6. Verify human oversight per Art. 14
7. Verify accuracy, robustness, and cybersecurity per Art. 15
8. Draw up EU Declaration of Conformity (Art. 47)
9. Affix CE marking (Art. 48)
10. Register in EU database (Art. 49)

## Post-Market Monitoring (Art. 72)

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Performance metric monitoring | Continuous | ML Engineering |
| Bias drift detection | Weekly | Responsible AI team |
| Incident reporting | As needed (within 15 days for serious incidents per Art. 73) | DPO + Legal |
| User feedback collection | Continuous | Product team |
| Risk register update | Quarterly | Risk Management |
| Technical documentation update | On material change | ML Engineering + Legal |

## Key Legal References

- **EU AI Act (Regulation 2024/1689)** — Full text, entered into force 1 August 2024
- **AI Act Art. 6 + Annex III** — High-risk classification criteria
- **AI Act Art. 9** — Risk management system requirements
- **AI Act Art. 10** — Data and data governance requirements
- **AI Act Art. 11 + Annex IV** — Technical documentation requirements
- **AI Act Art. 13** — Transparency and provision of information to deployers
- **AI Act Art. 14** — Human oversight requirements
- **AI Act Art. 43** — Conformity assessment procedures
- **AI Act Art. 72** — Post-market monitoring obligations
- **AI Act Art. 73** — Reporting of serious incidents
- **GDPR Art. 22** — Automated individual decision-making (complementary to AI Act)
- **EDPB-EDPS Joint Opinion 5/2021 on the AI Act Proposal** — Data protection perspective on AI regulation
