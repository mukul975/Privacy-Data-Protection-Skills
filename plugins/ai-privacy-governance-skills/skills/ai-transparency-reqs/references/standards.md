# Standards and Regulatory References — AI Transparency

## Primary Legislation

### GDPR — Transparency Provisions

- **Art. 5(1)(a)**: Principle of transparency — personal data must be processed in a transparent manner.
- **Art. 12**: Transparent information, communication, and modalities — concise, transparent, intelligible, easily accessible form, clear and plain language.
- **Art. 13(2)(f)**: Existence of automated decision-making including profiling, and meaningful information about the logic involved, significance, and envisaged consequences.
- **Art. 14(2)(g)**: Same as Art. 13(2)(f) for data not obtained directly from the data subject.
- **Art. 15(1)(h)**: Right of access includes meaningful information about logic of automated decisions.
- **Art. 22**: Rights related to automated individual decision-making — right not to be subject, right to obtain human intervention, express point of view, contest decision.
- **Recital 58**: Transparency principle requires information be easily accessible, easy to understand, clear and plain language, and visualisation where appropriate.
- **Recital 60**: Information about automated decision-making should include meaningful information about logic, significance, and consequences.
- **Recital 71**: Right to obtain explanation of the decision reached after automated assessment.

### EU AI Act (Regulation (EU) 2024/1689)

- **Art. 13(1)**: High-risk AI systems designed for transparency enabling deployers to interpret system output.
- **Art. 13(2)**: Accompanied by instructions for use with concise, correct, clear information relevant and accessible to deployers.
- **Art. 13(3)(b)**: Instructions must include level of accuracy, robustness, and cybersecurity and any known circumstances affecting performance.
- **Art. 13(3)(d)**: Instructions must include specifications for input data and other relevant information on training, validation, and testing datasets.
- **Art. 14**: Human oversight — systems designed to enable effective oversight, including understanding of AI capabilities and limitations.
- **Art. 50(1)**: AI systems intended to interact with persons must inform the natural person of the AI interaction.
- **Art. 50(2)**: Emotion recognition and biometric categorisation — inform about operation.
- **Art. 50(3)**: Deployers using AI to generate or manipulate content must disclose AI-generated nature.
- **Art. 50(4)**: AI-generated text on public interest matters must be labelled.
- **Art. 86**: Right to explanation of individual decision-making by AI — affected persons have the right to obtain from the deployer clear and meaningful explanations of the role of the high-risk AI system in the decision-making procedure and the main elements of the decision taken.
- **Recital 47**: High-risk AI systems should be transparent enough for deployers to appropriately use the system.
- **Recital 132**: Transparency obligations apply to providers and deployers of certain AI systems.

## EDPB and WP29 Guidance

### WP251rev.01 — Guidelines on Transparency (Revised April 2018)

- Transparency must be assessed from the perspective of the data subject.
- "Meaningful information about the logic" does not require complex technical explanations but must enable data subjects to understand reasons and possible consequences.
- Layered approach recommended: short notice at collection, detailed information accessible on request.
- Icons and visualisations may supplement but not replace written information.

### EDPB Guidelines 06/2020 — Automated Decision-Making and Profiling

- "Meaningful information about the logic involved" requires more than a list of factors — must explain how factors are weighted and interact.
- Machine learning models require explanation of the general methodology and key predictive features.
- The explanation should be tailored to the audience — plain language for consumers, more detail for sophisticated parties.
- Controllers cannot refuse to provide explanations on grounds of trade secret protection — proportionate explanation is always required.

### EDPB Guidelines 04/2025 — AI Processing

- AI training data transparency: data subjects should be informed when their data is used for AI training.
- Model output accuracy: transparency about AI system limitations and accuracy levels.
- Foundation model transparency: specific obligations for LLMs regarding training data and system capabilities.

### EDPB-AI ChatGPT Taskforce Report (2024)

- OpenAI required to provide comprehensive privacy notice covering AI training and inference processing.
- Transparency about training data sources (categories, not individual records).
- Information about model capabilities and limitations must be accessible.
- Accuracy disclaimer required for AI-generated content about identifiable persons.

## Technical Standards

### ISO/IEC 42001:2023 — AI Management System

- Section 6.1.2: Requires identification and documentation of AI system characteristics for transparency.
- Section 8.2: Documentation requirements for AI system lifecycle.
- Annex C: AI system transparency and explainability provisions.

### ISO/IEC TR 24028:2020 — AI Trustworthiness

- Section 8: Transparency in AI systems — principles and techniques.
- Recommends documentation of model behaviour, training data characteristics, and known limitations.
- Distinguishes between transparency (disclosure) and explainability (understanding).

### ISO/IEC 24027:2021 — Bias in AI Systems

- Section 6.4: Transparency about bias assessment results and mitigation measures.
- Recommends disclosure of fairness metrics and demographic performance variations.

### NIST AI RMF 1.0 (2023)

- Govern 1.4: Organisational transparency about AI system use.
- Map 1.1-1.5: Mapping AI system capabilities, limitations, and risks for disclosure.
- Measure 2.5: Measures of AI system explainability and interpretability.
- Manage 4.1: Communication of AI-related risks and impacts to affected stakeholders.

## Enforcement Decisions

- **Garante v. OpenAI (2023)**: Privacy notice for ChatGPT found insufficient — ordered to provide comprehensive information about AI training, data processing, and system limitations.
- **CNIL v. Clearview AI (SAN-2022-019, 2022)**: Total transparency failure — EUR 20M fine for processing biometric data through AI without any notice to data subjects.
- **Austrian DPA v. CRIF (DSB-D213.636, 2023)**: Credit scoring system provided only a score without meaningful explanation of factors and logic — violation of Art. 13(2)(f) and Art. 15(1)(h).
- **Dutch Court v. SyRI (ECLI:NL:RBDHA:2020:1878, 2020)**: Government algorithmic system violated transparency requirements — citizens could not understand how the system assessed them.
- **AEPD v. CaixaBank (2021)**: EUR 6M — automated credit decisions without adequate transparency about AI logic and significance.
- **Polish DPA v. Company (ZSPR.421.25.2019, 2019)**: First GDPR fine for AI-related Art. 14 violation — scoring individuals without providing required information about automated processing logic.
