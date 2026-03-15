# Standards and Regulatory References — AI DPIA

## Primary Legislation

### GDPR Article 35 — Data Protection Impact Assessment

- **Art. 35(1)**: Where processing using new technologies is likely to result in high risk to rights and freedoms, the controller shall carry out an assessment of the impact prior to processing. AI and ML systems constitute "new technologies" per EDPB interpretation.
- **Art. 35(3)(a)**: Mandatory DPIA for systematic and extensive automated evaluation producing legal or similarly significant effects — directly applicable to AI-driven decision-making.
- **Art. 35(7)**: DPIA must contain systematic description, necessity/proportionality assessment, risk assessment, and mitigation measures — extended for AI systems by EDPB Guidelines 04/2025.

### GDPR Article 22 — Automated Individual Decision-Making

- **Art. 22(1)**: Data subjects have the right not to be subject to decisions based solely on automated processing, including profiling, which produce legal or similarly significant effects.
- **Art. 22(2)**: Exceptions: contract necessity, Union/Member State law authorisation, explicit consent.
- **Art. 22(3)**: Controller must implement suitable safeguards including right to obtain human intervention, express their point of view, and contest the decision.
- **Art. 22(4)**: Art. 9 special category data may only be used in automated decisions under Art. 9(2)(a) or (g) with suitable safeguards.

### EU AI Act (Regulation (EU) 2024/1689)

- **Art. 5**: Prohibited AI practices — social scoring, real-time remote biometric identification (with exceptions), emotion recognition in workplace/education, untargeted facial image scraping.
- **Art. 6 + Annex III**: High-risk AI systems classification — biometric identification, critical infrastructure management, education/vocational training, employment/worker management, access to essential services, law enforcement, migration/border control, administration of justice.
- **Art. 9**: Risk management system requirements for high-risk AI systems.
- **Art. 10**: Data governance requirements for training, validation, and testing data sets.
- **Art. 13**: Transparency requirements — high-risk AI systems must be designed to enable users to interpret outputs and use them appropriately.
- **Art. 14**: Human oversight requirements for high-risk AI systems.
- **Art. 15**: Accuracy, robustness, and cybersecurity requirements.
- **Art. 26(9)**: Deployers of high-risk AI systems must use GDPR Art. 35 DPIA results when fulfilling their AI Act obligations.
- **Art. 50**: Transparency obligations for AI systems interacting with natural persons, generating synthetic content, or performing emotion recognition/biometric categorisation.

## EDPB Guidance

### EDPB Guidelines 04/2025 — Processing Personal Data in the Context of AI Models

Key provisions for AI DPIA:
- AI model training constitutes processing of personal data when personal data is used in training datasets, even if the model itself does not contain identifiable personal data.
- Legitimate interest as lawful basis for AI training requires a three-part balancing test with heightened scrutiny for large-scale training data collection.
- Web scraping of personal data for AI training generally cannot rely on legitimate interest without comprehensive safeguards.
- Controllers must assess and document whether AI models have effectively anonymised training data or whether extraction risks persist.
- The DPIA for AI must address the full lifecycle including training, fine-tuning, deployment, and ongoing inference.

### EDPB-AI Report on ChatGPT Taskforce (2024)

- Coordinated enforcement findings on LLM privacy compliance across multiple DPAs.
- Training data lawfulness: requiring documentation of lawful basis for each training data source.
- Output accuracy: GDPR accuracy principle (Art. 5(1)(d)) applies to AI-generated statements about identifiable persons.
- Right to erasure: controller must demonstrate capability to address erasure requests affecting training data.
- DPIA adequacy: specific findings on DPIA requirements for foundation models.

### WP248rev.01 — Guidelines on Data Protection Impact Assessment

- Nine criteria for high-risk determination — AI systems routinely meet 3 or more criteria.
- "Innovative technology" criterion explicitly encompasses AI and machine learning.
- Two or more criteria trigger presumptive DPIA obligation.

### EDPB Guidelines 06/2020 — Article 22 and Profiling

- Profiling encompasses any form of automated processing used to evaluate personal aspects.
- "Solely automated" includes processing where human oversight is nominal or ineffective.
- Meaningful human intervention requires competence, authority, and genuine ability to override.

## National DPA AI Guidance

### CNIL — AI Action Plan and Position on AI Training Data (2024)

- Published AI-specific DPIA framework addressing training data lawful basis.
- Legitimate interest balancing test for AI training must account for data subjects' reasonable expectations.
- Training data audit requirements: controllers must be able to document the content of training datasets.
- Recommended differential privacy and federated learning as mitigation measures.

### ICO — AI and Data Protection Guidance (Updated 2024)

- AI-specific DPIA guidance integrated into ICO Accountability Framework.
- Fairness assessment requirement: controllers must evaluate AI systems for discriminatory outcomes.
- Explainability requirement: meaningful information about the logic involved under Arts. 13-14 GDPR.
- Recommended DPIA review triggers: model retraining, distribution shift, new use case deployment.

### BfDI (Germany) — AI and Data Protection Position Paper (2023)

- AI training on publicly available personal data does not exempt from GDPR obligations.
- DPIA requirement for AI systems processing employee data (surveillance, performance assessment).
- Specific guidance on AI in the healthcare sector and additional DPIA requirements.

### Garante (Italy) — AI Processing Measures (2023-2024)

- Ordered OpenAI to conduct DPIA for ChatGPT processing of Italian data subjects.
- Required age verification mechanisms for AI services accessible to minors.
- Established precedent that DPIA for AI must address model output accuracy risks.

## Technical Standards

### ISO/IEC 42001:2023 — AI Management System

- Establishes management system requirements for AI development and deployment.
- Annex B: AI risk assessment methodology complementing GDPR DPIA.
- Requires documented AI impact assessment addressing societal and individual risks.

### ISO/IEC 23894:2023 — AI Risk Management

- Provides AI-specific risk management guidance.
- Risk identification methodology for AI systems covering technical and societal risks.
- Integrates with ISO 31000 risk management framework.

### NIST AI Risk Management Framework (AI RMF 1.0, 2023)

- Govern, Map, Measure, Manage framework for AI risk.
- Map 1.5: addresses privacy risk in AI systems.
- Measure 2.6: privacy risk measurement approaches for AI.
- Complementary to GDPR DPIA — provides technical risk assessment methodology.

### IEEE 7010-2020 — Well-being Impact Assessment for AI

- Assessment framework for AI impact on human well-being.
- Broader than privacy-focused DPIA but includes privacy indicators.
- Recommended for supplementing DPIA with societal impact assessment.

## Enforcement Decisions

- **CNIL v. Clearview AI (SAN-2022-019, 2022)**: EUR 20M fine — no DPIA for biometric AI, no lawful basis, no transparency. Model trained on 20 billion scraped facial images.
- **Garante v. OpenAI (2023)**: Temporary processing ban for ChatGPT in Italy — inadequate DPIA, no age verification, no lawful basis for training data, inaccurate outputs about data subjects.
- **ICO v. Clearview AI (MPN, 2022)**: GBP 7.5M fine and enforcement notice — no DPIA for facial recognition AI deployed with UK law enforcement data.
- **AEPD v. CaixaBank (PS/00421/2020, 2021)**: EUR 6M fine — automated credit scoring without adequate DPIA addressing algorithmic risk.
- **Dutch Court (The Hague, ECLI:NL:RBDHA:2020:1878, 2020)**: SyRI algorithmic fraud detection declared unlawful — disproportionate AI profiling without adequate DPIA and safeguards.
- **Datatilsynet v. Municipality of Trondheim (2023)**: Fine for deploying AI-based welfare fraud detection without conducting DPIA per Art. 35.
