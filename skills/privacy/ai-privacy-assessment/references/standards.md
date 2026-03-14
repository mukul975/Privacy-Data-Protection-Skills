# Standards and Regulatory References for AI System Privacy Assessment

## Primary Legislation

### GDPR — Key Provisions for AI

- **Art. 5(1)(a)-(f)**: Data protection principles apply fully to AI processing. Fairness under Art. 5(1)(a) encompasses algorithmic fairness and non-discrimination.
- **Art. 6(1)**: Lawful basis required for each processing stage (collection, training, inference, output use). Art. 6(4) compatibility test applies to repurposing data for AI training.
- **Art. 9**: Processing of special categories (health, biometric, genetic, racial or ethnic origin, political opinions, religious beliefs, trade union membership, sexual orientation) in AI training requires an Art. 9(2) exemption.
- **Art. 13(2)(f)**: Transparency obligation to provide meaningful information about the logic involved in automated decision-making, the significance, and envisaged consequences.
- **Art. 14(2)(g)**: Same transparency obligation for data not obtained directly from the data subject.
- **Art. 22(1)**: Right not to be subject to decisions based solely on automated processing which produce legal effects or similarly significantly affect the data subject.
- **Art. 22(2)**: Exceptions: (a) necessary for contract; (b) authorised by law with suitable safeguards; (c) explicit consent.
- **Art. 22(3)**: Safeguards: right to human intervention, right to express point of view, right to contest the decision.
- **Art. 22(4)**: Automated decisions must not be based on special category data unless Art. 9(2)(a) or (g) applies with suitable measures.
- **Art. 35**: DPIA required for AI systems meeting high-risk criteria (evaluation/scoring, automated decision-making, innovative technology).
- **Art. 25**: Data protection by design and by default — AI systems must incorporate privacy-preserving techniques.

### EU AI Act — Regulation (EU) 2024/1689

- **Art. 5**: Prohibited AI practices (social scoring, real-time biometric identification in public spaces with exceptions, emotion recognition in workplace/education, untargeted facial recognition scraping).
- **Art. 6 + Annex III**: High-risk AI classification based on deployment domain.
- **Art. 9**: Risk management system required for high-risk AI (identification, estimation, evaluation, and mitigation of risks).
- **Art. 10**: Data governance requirements for training, validation, and testing datasets: relevance, representativeness, freedom from errors, completeness, statistical properties.
- **Art. 11**: Technical documentation requirements for high-risk AI.
- **Art. 13**: Transparency and provision of information to deployers.
- **Art. 14**: Human oversight measures for high-risk AI.
- **Art. 15**: Accuracy, robustness, and cybersecurity requirements.
- **Art. 26**: Obligations of deployers of high-risk AI systems.
- **Art. 50**: Transparency obligations for limited-risk AI (chatbots, deep fakes, emotion recognition).
- **Art. 85**: Right to explanation of individual decision-making by high-risk AI system.

## EDPB and EDPS Guidance

### EDPB-EDPS Joint Opinion 5/2021 on the AI Act Proposal (18 June 2021)
- Recommended extending the prohibition on remote biometric identification to all spaces, not just public.
- Recommended mandatory DPIAs for all high-risk AI systems.
- Emphasized that the AI Act should complement, not replace, GDPR obligations.
- Called for stronger provisions on the right to explanation for AI decisions.
- Recommended that AI Act conformity assessments integrate DPIA requirements.

### EDPB Guidelines 06/2025 on AI and Data Protection
- Clarified the application of purpose limitation to AI model training.
- Established criteria for assessing whether AI training constitutes compatible further processing under Art. 6(4).
- Provided guidance on the application of Art. 22 to AI-assisted (not solely automated) decisions.
- Addressed the question of whether trained AI models constitute personal data.
- Provided guidance on exercising data subject rights in the context of AI (right to erasure of training data, right to explanation of AI logic).

### EDPB Guidelines 05/2020 on Consent for Scientific Research
- Relevant to AI training that may qualify as scientific research under Art. 89.
- Clarifies that consent for scientific research can be broader but must still be specific to a research area.

## NIST AI Risk Management Framework (AI RMF 1.0, January 2023)

### GOVERN Function
- GOVERN 1: Policies, processes, procedures for AI risk management
- GOVERN 2: Accountability structures for AI risk management
- GOVERN 3: Workforce diversity, equity, inclusion, and accessibility for AI
- GOVERN 4: Organisational practices for AI risk culture
- GOVERN 5: Processes for engagement with external stakeholders
- GOVERN 6: Policies for AI system decommissioning

### MAP Function
- MAP 1: Context established and understood (purpose, intended users, affected stakeholders)
- MAP 2: Categorisation of AI system (capabilities, knowledge limits, failure conditions)
- MAP 3: AI risks and benefits mapped (potential positive and negative impacts on individuals, groups, communities)
- MAP 4: Risks mapped to impact area (people, planet, prosperity)
- MAP 5: Stakeholder engagement (affected communities, domain experts)

### MEASURE Function
- MEASURE 1: Appropriate methods and metrics for AI risk assessment
- MEASURE 2: AI systems evaluated for trustworthy characteristics (valid, reliable, safe, secure, resilient, accountable, transparent, explainable, fair, privacy-enhanced)
- MEASURE 3: Mechanisms for tracking AI risks over time
- MEASURE 4: Feedback from users and affected communities

### MANAGE Function
- MANAGE 1: AI risks prioritised, responded to, managed
- MANAGE 2: Risk treatments allocated resources and monitored
- MANAGE 3: Risk management integrated with overall organisational risk management
- MANAGE 4: Risks managed for deployed AI systems

## ISO/IEC Standards

### ISO/IEC 42001:2023 — Artificial Intelligence Management System
- Establishes requirements for an AI management system within organisations.
- Annex B: AI objectives and controls including data management, transparency, bias management.
- Annex D: Guidance on AI-specific risk assessment.

### ISO/IEC 23894:2023 — AI Risk Management
- Provides guidance on managing risks throughout the AI lifecycle.
- Aligned with ISO 31000 risk management framework.
- Addresses AI-specific risks: bias, lack of transparency, unintended outputs.

### ISO/IEC 38507:2022 — Governance of IT — Governance of AI
- Governance framework for AI at the organisational level.
- Addresses accountability, transparency, and ethical considerations.

### ISO/IEC 24027:2021 — Bias in AI Systems
- Taxonomy of biases in AI: data bias, algorithmic bias, deployment bias, societal bias.
- Guidance on bias measurement and mitigation techniques.

## Enforcement Precedents

- **Italian Garante vs Clearview AI (GPDP Decision, 10 February 2022)**: EUR 20 million fine. Biometric data scraping from public internet for AI facial recognition training without lawful basis (Art. 6), without consent (Art. 7), without transparency (Art. 14), and without DPIA (Art. 35).
- **Italian Garante vs Deliveroo Italy (GPDP Decision, 2 November 2021)**: EUR 2.5 million fine. Algorithmic management system for food delivery riders constituted Art. 22 automated decision-making (reputation scoring, shift allocation) without adequate safeguards, human intervention, or right to contest.
- **Dutch DPA vs SyRI (District Court of The Hague, C/09/550982, 5 February 2020)**: System Risk Indication (SyRI) algorithmic profiling system for fraud detection declared unlawful. Court found insufficient transparency about the algorithm, disproportionate impact on lower-income and ethnic minority neighbourhoods, and insufficient safeguards against discriminatory profiling.
- **CNIL vs Clearview AI (Decision SAN-2022-019, 17 October 2022)**: EUR 20 million fine. Confirmed Italian findings and additionally ordered deletion of all French residents' biometric data and prohibition of further collection.
- **Hungarian NAIH vs Budapest Bank (2023)**: Fine for automated credit scoring system using postcode as proxy variable for ethnicity without conducting bias impact assessment or DPIA.
- **ICO vs Serco Leisure (2022)**: Enforcement notice for requiring employees to use facial recognition for time and attendance without conducting DPIA and without offering a less intrusive alternative.
