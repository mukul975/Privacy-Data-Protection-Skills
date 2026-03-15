# AI System Pre-Deployment Privacy Checklist — Standards References

## Primary Legislation

### GDPR (Regulation 2016/679)
- **Article 5** — Principles of personal data processing (lawfulness, fairness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity/confidentiality, accountability)
- **Article 6** — Lawful basis for processing; Art. 6(1)(a)-(f) must be identified before deployment
- **Article 9** — Special categories of personal data; explicit consent or Art. 9(2) exception required
- **Article 13-14** — Information to data subjects; privacy notices must cover AI processing
- **Article 22** — Automated individual decision-making and profiling safeguards
- **Article 25** — Data protection by design and by default
- **Article 35** — Data Protection Impact Assessment for high-risk processing
- **Article 36** — Prior consultation with supervisory authority where residual risk remains high

### EU AI Act (Regulation 2024/1689)
- **Article 9** — Risk management system (continuous, iterative process throughout AI system lifecycle)
- **Article 10** — Data governance for training, validation, and testing datasets
- **Article 13** — Transparency and provision of information to deployers
- **Article 14** — Human oversight requirements
- **Article 15** — Accuracy, robustness, and cybersecurity requirements
- **Article 43** — Conformity assessment procedures
- **Article 47** — EU Declaration of Conformity
- **Article 49** — EU database registration
- **Article 52** — Transparency obligations for certain AI systems (chatbots, deepfakes, emotion recognition)
- **Article 72** — Post-market monitoring by providers

## Supplementary Standards

### ISO/IEC 42001:2023 — AI Management System
- Provides a management system framework for organisations developing or using AI
- Annex A controls map to AI Act quality management requirements (Art. 17)

### ISO/IEC 23894:2023 — AI Risk Management
- Risk management process compatible with EU AI Act Art. 9 requirements
- Integrates with ISO 31000 enterprise risk management

### ISO/IEC 27001:2022 — Information Security Management
- Security controls framework applicable to AI system infrastructure
- Annex A controls for access management, encryption, logging

### NIST AI RMF 1.0 (January 2023)
- AI risk management framework with Govern, Map, Measure, Manage functions
- Complementary to EU AI Act risk approach; useful for cross-jurisdictional deployments

## Regulatory Guidance

### EDPB Guidelines on Automated Decision-Making (WP 251 rev.01)
- Interpretation of GDPR Article 22 for automated decision-making
- Defines "solely automated" and "significant effects" thresholds
- Right to explanation and human intervention requirements

### EDPB-EDPS Joint Opinion 5/2021 on the AI Act Proposal
- Data protection perspective on AI regulation
- Guidance on GDPR and AI Act interplay for high-risk systems

### ICO Guidance on AI and Data Protection (2023)
- Practical approach to DPIA for AI systems
- Fairness in AI processing assessment framework
- Transparency requirements for automated decisions

### CNIL AI Action Plan (2023-2024)
- French DPA guidance on GDPR-compliant AI development
- Training data governance, purpose limitation for ML, legitimate interests assessment

## Fairness and Bias Standards

### US EEOC Four-Fifths Rule (29 CFR 1607.4D)
- Disparate impact threshold: selection rate for any group must be at least 80% of the rate for the most favoured group
- Widely adopted as a bias metric even outside US employment context

### IEEE 7010-2020 — Wellbeing Impact Assessment
- Framework for assessing AI system impact on human wellbeing
- Useful for pre-deployment social impact assessment
