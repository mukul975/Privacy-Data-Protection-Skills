# Standards and Regulatory References — AI Training Data Classification

## Primary Legislation

### GDPR — Regulation (EU) 2016/679

- **Article 5(1)(b)**: Purpose limitation — personal data collected for specified purposes shall not be further processed in a manner incompatible with those purposes. Further processing for scientific research purposes in accordance with Art. 89(1) shall not be considered incompatible (but ML training for commercial purposes is generally not scientific research).
- **Article 6(4)**: Compatibility test for new purposes — factors include link between original and new purpose, context, nature of the data, consequences for data subjects, and existence of appropriate safeguards including encryption or pseudonymisation.
- **Article 9**: Special category prohibitions and exceptions apply to training data containing protected attributes or from which protected attributes can be inferred.
- **Article 22**: Right not to be subject to solely automated decision-making producing legal or significant effects — applies to ML model outputs.
- **Article 35**: DPIA required for systematic and extensive evaluation of personal aspects based on automated processing (Art. 35(3)(a)) — ML model development triggers this.

### EU AI Act — Regulation (EU) 2024/1689

- **Article 10(1)**: High-risk AI systems shall be developed on the basis of training, validation, and testing datasets that meet quality criteria.
- **Article 10(2)**: Training datasets shall be subject to appropriate data governance practices covering design choices, data collection processes, preparation (annotation, labelling, cleaning, enrichment), formulation of assumptions, prior assessment of availability/suitability/biases, identification of gaps or shortcomings.
- **Article 10(3)**: Training datasets shall be relevant, sufficiently representative, and to the best extent possible free of errors and complete.
- **Article 10(5)**: Processing of special categories under Art. 9 GDPR is permitted "to the extent that is strictly necessary for the purposes of ensuring bias monitoring, detection and correction" with appropriate safeguards, including technical limitations on re-use, pseudonymisation, encryption, and temporal limits.
- **Annex IV(2)(d)**: Technical documentation must include information about training data, including data provenance, data collection, labelling procedures, and cleaning methods.

## Regulatory Guidance

### EDPB Guidelines 06/2023 — Processing Personal Data in the Context of AI (Draft)

- **Key Content**: Detailed analysis of GDPR application to AI development lifecycle. Lawful basis assessment for training, legitimate interests balancing factors, purpose limitation for training data reuse, data minimisation in feature engineering, transparency requirements, and data subject rights (including the right to erasure and its implications for trained models).

### CNIL — Practical Guide: AI Systems and Personal Data (2024)

- **Key Content**: French DPA guidance on GDPR compliance for AI, covering: web scraping for training data (requires lawful basis), consent for training use (must be specific to AI purpose), legitimate interests for ML training (requires detailed balancing test), data minimisation through feature engineering, and data subject rights including requests for model retraining after erasure.

### ICO — Guidance on AI and Data Protection (2023)

- **Key Content**: UK ICO guidance covering lawful basis for AI training, fairness and bias in AI, transparency and explainability, DPIA requirements for AI systems, and accountability documentation.

## Technical Standards

### Google Model Cards (Mitchell et al., 2019)

- **Reference**: "Model Cards for Model Reporting" — Conference on Fairness, Accountability, and Transparency (FAT* 2019)
- **Key Content**: Framework for documenting ML models including intended use, factors, metrics, evaluation data, training data, quantitative analysis, and ethical considerations.

### Datasheets for Datasets (Gebru et al., 2021)

- **Reference**: "Datasheets for Datasets" — Communications of the ACM, December 2021
- **Key Content**: Structured documentation framework for ML datasets covering motivation, composition, collection process, preprocessing, uses, distribution, and maintenance.

### ISO/IEC 23894:2023 — Artificial Intelligence — Guidance on Risk Management

- **Key Content**: Risk management framework for AI systems including data quality risks, bias risks, and privacy risks in training data.

### NIST AI Risk Management Framework (AI RMF 1.0, January 2023)

- **Map 1.1**: Legal and regulatory requirements related to AI identified
- **Map 2.3**: Scientific integrity and TEVV (test, evaluation, verification, validation) considerations documented
- **Measure 2.6**: Computational bias assessment across demographic groups
- **Measure 2.7**: AI system evaluated for fairness
