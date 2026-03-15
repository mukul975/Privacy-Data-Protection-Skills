# Standards and Regulatory References — Federated Learning

## Primary Legislation

### GDPR
- **Art. 5(1)(c)**: Data minimisation — FL directly supports by keeping data local.
- **Art. 25**: Data protection by design and by default — FL is a privacy-by-design architecture.
- **Art. 26**: Joint controllers — cross-silo FL participants may be joint controllers.
- **Art. 28**: Processor obligations — FL aggregator may be a processor.
- **Art. 32**: Security of processing — secure aggregation implements technical security measures.
- **Art. 44-49**: International transfers — FL may avoid transfer obligations if data stays local with privacy-preserving aggregation.

### EU AI Act
- **Art. 10**: Data governance — FL enables governance while maintaining data locality.
- **Art. 25**: Measures for providers of general-purpose AI — FL architecture can demonstrate data governance.
- **Recital 45**: Without prejudice to GDPR — FL must still comply with underlying data protection requirements.

## EDPB Guidance
- **EDPB Guidelines 04/2025**: Federated learning identified as data minimisation measure for AI training.
- **EDPB Guidelines 03/2021 on Virtual Voice Assistants**: Mentioned on-device processing as privacy-preserving alternative.

## National DPA Guidance
- **CNIL AI Action Plan (2024)**: Recommends federated learning as a PET for AI training data processing.
- **ICO AI Guidance (2024)**: References distributed training as a data minimisation technique.

## Technical Standards
- **ISO/IEC 20547-4:2020**: Big data reference architecture — federated architectures for distributed data processing.
- **ISO/IEC 27001:2022**: Information security controls applicable to FL infrastructure.
- **NIST AI RMF 1.0**: Map 1.5 — privacy risk mapping includes distributed training architectures.

## Academic References
- McMahan, B. et al. (2017): "Communication-Efficient Learning of Deep Networks from Decentralized Data" — foundational FedAvg paper.
- Bonawitz, K. et al. (2017): "Practical Secure Aggregation for Privacy-Preserving Machine Learning" — masking-based secure aggregation protocol.
- Kairouz, P. et al. (2021): "Advances and Open Problems in Federated Learning" — comprehensive FL survey with privacy analysis.
- Melis, L. et al. (2019): "Exploiting Unintended Feature Leakage in Collaborative Learning" — gradient leakage attacks on FL.
- Zhu, L. et al. (2019): "Deep Leakage from Gradients" — demonstrated pixel-perfect reconstruction from gradients.
