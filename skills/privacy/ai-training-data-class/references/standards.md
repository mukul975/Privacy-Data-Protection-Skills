# Standards and Regulatory References — AI Training Data Classification

## Primary Legislation

### GDPR — Regulation (EU) 2016/679

- **Article 5(1)(b)**: Purpose limitation — training data collected for one purpose may not be used for ML training without compatible purpose assessment per Art. 6(4) or new lawful basis.
- **Article 5(1)(c)**: Data minimisation — training datasets must contain only personal data necessary for the model objective.
- **Article 9**: Special category data in training datasets requires Art. 9(2) condition, even if the model's purpose is not to process special category data.
- **Article 22**: Automated individual decision-making, including profiling — models producing legal or significant effects on individuals require human oversight, contestability, and transparency.
- **Article 35**: DPIA required for systematic evaluation of personal aspects through automated processing, including profiling.

### EU AI Act — Regulation (EU) 2024/1689

- **Article 10(1)**: High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5.
- **Article 10(2)**: Data governance and management practices — training datasets shall address design choices, data collection processes, data preparation operations, formulation of assumptions, prior assessment of data availability and suitability, bias examination and mitigation.
- **Article 10(3)**: Training datasets shall be relevant, sufficiently representative, and to the extent possible, free of errors and complete.
- **Article 10(5)**: Processing of special categories of personal data for bias detection — permitted where strictly necessary for the purposes of ensuring bias monitoring, detection and correction, subject to appropriate safeguards including technical limitations on re-use, pseudonymisation, encryption, and GDPR compliance.
- **Article 11**: Technical documentation for high-risk AI systems must include information about the data used for training, including data cards.
- **Annex III**: List of high-risk AI areas: biometric identification, critical infrastructure, education, employment, essential services, law enforcement, migration, administration of justice.

## Regulatory Guidance

### EDPB-EDPS Joint Opinion 5/2021 on the Proposal for an AI Act

- **Section 4.3**: The EDPB and EDPS stressed that the AI Act must not lower GDPR protections for personal data used in AI training. Any use of personal data in training datasets must comply with GDPR independently.

### ICO — Generative AI and Data Protection: Consultation Series (2024)

- **Chapter 2 — Lawful Basis for Training**: Legitimate interests (Art. 6(1)(f)) is the most likely lawful basis for web-scraped training data, but requires documented LIA considering: data subject reasonable expectations, volume and sensitivity of data, ability to opt out, and safeguards.
- **Chapter 3 — Purpose Limitation**: Using existing customer data for internal ML model training may be compatible with original purpose if model improves the service data was collected for. Assessment under Art. 6(4) required.
- **Chapter 4 — Accuracy and Bias**: AI Act requirements for training data quality complement GDPR accuracy principle. Bias in training data can lead to discriminatory outcomes that engage Art. 9 protections.

### CNIL — AI Guidance Sheets (2024)

- **Sheet 1**: Defining the purpose of AI processing — training a model is a distinct processing activity.
- **Sheet 2**: Lawful basis — legitimate interests most common; consent rarely practical for large-scale training.
- **Sheet 3**: Data minimisation — principle applies at training data collection, feature engineering, and model deployment stages.
- **Sheet 4**: Data retention — training data retention must be justified; model weights may embed personal data.

## Academic Standards

### Datasheets for Datasets (Gebru et al., 2021)

- **Citation**: Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J.W., Wallach, H., Daumé III, H. and Crawford, K. (2021). "Datasheets for Datasets." Communications of the ACM, 64(12), 86-92.
- **Key Content**: Proposed framework for documenting ML datasets covering motivation, composition, collection process, preprocessing, uses, distribution, and maintenance.

### Model Cards for Model Reporting (Mitchell et al., 2019)

- **Citation**: Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I.D. and Gebru, T. (2019). "Model Cards for Model Reporting." Proceedings of FAT* '19, 220-229.
- **Key Content**: Framework for documenting trained ML models including intended use, performance metrics by demographic group, ethical considerations, and limitations.
