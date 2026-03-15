# AI Privacy Inference and Derived Data — Standards References

## Primary Legislation

### GDPR (Regulation 2016/679)
- **Article 4(4)** — Definition of profiling: any form of automated processing to evaluate personal aspects
- **Article 5(1)(d)** — Accuracy principle: personal data must be accurate and kept up to date
- **Article 6** — Lawful basis required for generating inferences as a processing activity
- **Article 9** — Special category data: inferences predicting Art. 9 characteristics trigger heightened protections
- **Article 13(2)(f)** — Right to information about the existence of automated decision-making including profiling, meaningful information about the logic involved, and significance and envisaged consequences
- **Article 14(2)(g)** — Same information requirement when data not obtained from data subject
- **Article 15(1)(h)** — Right of access to information about automated decision-making and profiling
- **Article 16** — Right to rectification of inaccurate personal data, including inaccurate inferences
- **Article 21** — Right to object to processing including profiling
- **Article 22** — Restrictions on solely automated decision-making producing legal or similarly significant effects
- **Recital 71** — Safeguards for profiling: right to obtain human intervention, express point of view, contest decision
- **Recital 72** — EDPB guidance on profiling

### EU AI Act (Regulation 2024/1689)
- **Article 6 + Annex III** — High-risk classification for AI systems evaluating persons for employment (para. 4), access to services (para. 5), creditworthiness (para. 5(b))
- **Article 10** — Data governance obligations for training data in high-risk AI inference systems
- **Article 13** — Transparency: deployers must be informed about AI system capabilities and limitations
- **Article 14** — Human oversight: high-risk AI systems must allow effective human oversight of inferences
- **Article 52** — Transparency for systems interacting with natural persons (inform users of AI interaction)

## Case Law

### CJEU C-434/16 (Nowak, 2017)
- Personal data includes "any information" relating to an identified or identifiable person
- Assessments, opinions, and inferences about a person are personal data
- Data subjects have right of access and rectification to such assessments

### CJEU C-634/21 (SCHUFA, 2023)
- Credit scoring by a private entity constitutes automated decision-making under Art. 22 when the score plays a decisive role in a third party's subsequent decision
- Score generation itself may be subject to Art. 22 safeguards
- Data subjects have right to explanation of scoring logic

### CJEU C-252/21 (Meta Platforms, 2023)
- Data protection authorities can consider compliance with competition law when assessing lawful basis
- Relevant to inference generation from cross-platform data aggregation

### Austrian DPA — DSB-D550.038 (2022)
- Inferred political opinions from social media constitute Art. 9 special category data
- Probabilistic nature does not exempt from Art. 9 classification

### Norwegian DPA — Grindr Decision (2021)
- NOK 65 million fine for enabling inference of sexual orientation through data sharing
- Data enabling inference of Art. 9 characteristics is itself special category data

## Regulatory Guidance

### EDPB Guidelines on Automated Decision-Making (WP 251 rev.01)
- Defines profiling and solely automated decision-making
- Three categories: profiling only, profiling with human decision, solely automated with legal effects
- Safeguards required: human intervention, expression of views, contestation

### EDPB Guidelines 8/2020 on Targeting of Social Media Users
- Inferred data (created by controller through observation or derivation) is personal data
- Full GDPR rights apply to inferred data
- Transparency obligations extend to inferred characteristics

### ICO Guidance on AI and Data Protection (2023)
- Inferences and predictions about individuals are personal data
- Accuracy principle applies: controllers must take steps to ensure inferences are not inaccurate
- Right to rectification extends to incorrect inferences

### CNIL AI Action Plan (2023-2024)
- AI inferences about individuals require lawful basis independent of original data collection
- Purpose limitation applies: inferences cannot be used for incompatible purposes

## Technical Standards

### ISO/IEC 42001:2023 — AI Management System
- Framework for managing AI system lifecycle including inference governance

### IEEE 7010-2020 — Wellbeing Impact Assessment
- Assessment framework for evaluating AI inference impact on individuals

### NIST AI RMF 1.0 (January 2023)
- Map function: identify inference types and their potential impacts
- Measure function: assess inference accuracy and bias across groups
- Manage function: implement controls for inference quality and fairness
