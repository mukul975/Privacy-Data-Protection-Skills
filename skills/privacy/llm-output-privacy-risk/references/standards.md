# LLM Output Privacy Risk — Standards References

## Primary Legislation

### GDPR (Regulation 2016/679)
- **Article 4(2)** — Definition of processing: generating personal data in LLM output constitutes processing
- **Article 5(1)(d)** — Accuracy principle: hallucinated personal data violates accuracy requirements
- **Article 5(1)(f)** — Integrity and confidentiality: training data leakage through outputs is a confidentiality failure
- **Article 6(1)** — Lawful basis required for processing personal data in outputs
- **Article 13-14** — Information to data subjects: users must be informed that AI may generate inaccurate information
- **Article 16** — Right to rectification: mechanism needed for correcting hallucinated personal data
- **Article 17** — Right to erasure: mechanism needed for removing memorised personal data from model
- **Article 25** — Data protection by design: PII output filtering as a design requirement
- **Article 32** — Security of processing: output monitoring as a security measure
- **Article 33-34** — Breach notification: large-scale PII leakage in outputs may constitute a data breach

### EU AI Act (Regulation 2024/1689)
- **Article 50** — Transparency obligations: users must be informed they are interacting with an AI system
- **Article 52** — Specific transparency for AI-generated content: applies to deepfakes and synthetic text
- **Article 15** — Accuracy, robustness, and cybersecurity: includes robustness against adversarial attacks (prompt injection)

## Research References

### Training Data Memorisation
- **Carlini et al. (2023)** — "Quantifying Memorization Across Neural Language Models" — Demonstrates that larger models memorise more training data and proposes extractable memorisation metrics
- **Carlini et al. (2021)** — "Extracting Training Data from Large Language Models" — Shows that GPT-2 memorises and regurgitates training data including PII
- **Ippolito et al. (2023)** — "Preventing Verbatim Memorization in Language Models Gives a False Sense of Privacy" — Demonstrates that non-verbatim memorisation still leaks private information

### Prompt Injection
- **Greshake et al. (2023)** — "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection" — Taxonomy of indirect prompt injection attacks
- **Perez and Ribeiro (2022)** — "Ignore This Title and HackAPrompt: Exposing Systemic Weaknesses of LLMs through a Global Scale Prompt Hacking Competition" — Systematic prompt injection attack patterns

### PII Detection and Filtering
- **Microsoft Presidio** — Open-source PII detection and anonymisation framework; supports custom recognisers
- **AWS Comprehend PII Detection** — Cloud-based NER service for PII detection in text
- **spaCy NER models** — Named entity recognition for person names, locations, organisations

## Regulatory Guidance

### EDPB Guidelines 04/2025 on Processing of Personal Data through AI Systems
- Section on output accuracy: controllers must implement measures to prevent generation of inaccurate personal data
- Memorisation risk assessment required as part of DPIA for LLM deployments

### EDPB ChatGPT Taskforce Report (2024)
- Recommendations on output filtering for personal data
- Technical measures to address accuracy of AI-generated content about individuals
- Right to rectification implementation for LLM-generated content

### Garante v. OpenAI (April 2023)
- Temporary processing ban due to (among other issues) inaccurate personal data in ChatGPT outputs
- Required implementation of measures to improve accuracy of information about individuals

### CNIL AI Action Plan (2024)
- Guidance on GDPR compliance for generative AI
- Output containing personal data constitutes processing requiring lawful basis
- Recommendations for PII filtering in LLM output pipelines

### ICO Guidance on Generative AI (2023)
- UK perspective on LLM privacy risks
- Accuracy requirements for AI-generated content about individuals
- Recommendations for transparency about AI limitations
