# Standards and Regulatory References — AI Model Privacy Audit

## Primary Legislation

### GDPR

- **Art. 5(1)(f)**: Integrity and confidentiality — personal data processed with appropriate security, including protection against unauthorised access and accidental loss.
- **Art. 25**: Data protection by design and by default — implement appropriate technical measures to ensure data protection principles.
- **Art. 32**: Security of processing — implement appropriate technical and organisational measures including testing, assessing, and evaluating the effectiveness of security measures.
- **Art. 35**: DPIA — assess risks to rights and freedoms, including risks from AI model privacy leakage.

### EU AI Act

- **Art. 9**: Risk management system for high-risk AI — identify and analyse known and foreseeable risks, including privacy risks from model memorization.
- **Art. 10(5)**: Training data governance — measures to detect and correct bias, which intersects with privacy testing methodology.
- **Art. 15**: Accuracy, robustness, and cybersecurity — high-risk AI systems must be resilient against attempts to exploit vulnerabilities, including privacy attacks.

## EDPB Guidance

### EDPB Guidelines 04/2025

- Controllers must assess whether AI models have anonymised training data or retain the capacity to generate personal data.
- Model privacy testing (membership inference, extraction) is the standard methodology for this assessment.
- If the model fails privacy testing, the training data is not effectively anonymised, and GDPR obligations persist for the model.

## Technical Standards

### NIST AI RMF 1.0 (2023)

- Measure 2.6: Privacy risk measurement for AI systems — recommends membership inference and data extraction testing.
- Manage 2.4: Management of AI privacy risks through testing and monitoring.

### ISO/IEC 27001:2022 — Information Security Management

- A.8.8: Management of technical vulnerabilities — model privacy vulnerabilities fall under this control.
- A.8.16: Monitoring activities — continuous privacy monitoring for deployed AI models.

### ISO/IEC 42001:2023 — AI Management System

- Section 8.4: AI system verification and validation — includes privacy testing.
- Annex B: AI risk assessment methodology — privacy leakage as a risk category.

## Academic References

- Shokri, R. et al. (2017): "Membership Inference Attacks Against Machine Learning Models" — foundational membership inference attack paper. IEEE Symposium on Security and Privacy.
- Carlini, N. et al. (2021): "Extracting Training Data from Large Language Models" — demonstrated verbatim training data extraction from GPT-2. USENIX Security Symposium.
- Carlini, N. et al. (2023): "Quantifying Memorization Across Neural Language Models" — systematic study of memorization in language models across scales.
- Fredrikson, M. et al. (2015): "Model Inversion Attacks that Exploit Confidence Information" — model inversion attack methodology. ACM CCS.
- Yeom, S. et al. (2018): "Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting" — connection between overfitting and privacy risk. IEEE CSF.
- Murakonda, S. and Shokri, R. (2020): "ML Privacy Meter: Aiding Regulatory Compliance by Quantifying the Privacy Risks of Machine Learning" — the ML Privacy Meter tool paper.
- Nasr, M. et al. (2023): "Scalable Extraction of Training Data from (Production) Language Models" — extraction attacks against production LLMs including ChatGPT.
