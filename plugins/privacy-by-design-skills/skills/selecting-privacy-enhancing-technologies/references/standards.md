# Privacy-Enhancing Technologies Standards and References

## Regulatory Framework

### GDPR Article 25(1) — Data Protection by Design
The controller shall implement appropriate technical and organisational measures, such as pseudonymisation, which are designed to implement data-protection principles in an effective manner and to integrate the necessary safeguards into the processing.

### GDPR Article 32(1) — Security of Processing
Taking into account the state of the art, the costs of implementation and the nature, scope, context and purposes of processing: (a) the pseudonymisation and encryption of personal data; (b) the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services.

### GDPR Recital 78 — Appropriate Technical Measures
The protection of the rights and freedoms of natural persons with regard to the processing of personal data require that appropriate technical and organisational measures be taken. The controller should adopt internal policies and implement measures which meet in particular the principles of data protection by design and data protection by default.

## European Commission and ENISA Guidance

### European Commission Communication on PETs (February 2025)
Recognizes PETs as critical enablers for privacy-preserving data sharing across the EU Data Strategy. Highlights differential privacy, secure MPC, federated learning, and homomorphic encryption as mature PETs suitable for adoption in health, finance, and public administration sectors.

### ENISA Report: Data Protection Engineering (2022)
Maps PETs to GDPR data protection principles. Recommends differential privacy for anonymization, homomorphic encryption for confidential processing, secure MPC for cross-organizational analytics, and federated learning for distributed ML.

### ENISA Report: Pseudonymisation techniques and best practices (2019)
Evaluates pseudonymisation techniques as a specific PET category. Recommends HMAC-based pseudonymization with HSM key management for enterprise deployments.

## Technical Standards

### ISO/IEC 20889:2018 — Privacy Enhancing Data De-identification
Classifies PETs for de-identification including statistical techniques, cryptographic techniques, and suppression-based methods.

### ISO/IEC 27559:2022 — Privacy Enhancing Data De-identification Framework
Provides a framework for selecting and implementing de-identification techniques considering data utility requirements and re-identification risk.

### NIST Cybersecurity White Paper: Privacy-Enhancing Cryptography (2023)
Surveys homomorphic encryption, secure MPC, zero-knowledge proofs, and private set intersection. Provides performance benchmarks and deployment considerations.

## Academic Foundations

### Differential Privacy
Dwork, C., Roth, A. (2014). "The Algorithmic Foundations of Differential Privacy." Foundations and Trends in Theoretical Computer Science. Comprehensive treatment of DP mechanisms, composition theorems, and applications.

### Homomorphic Encryption
Gentry, C. (2009). "A Fully Homomorphic Encryption Scheme." Stanford PhD thesis. First construction of FHE. Brakerski, Fan, Vercauteren (BFV), Cheon, Kim, Kim, Song (CKKS) — practical schemes for integer and approximate arithmetic.

### Secure Multi-Party Computation
Yao, A. (1986). "How to Generate and Exchange Secrets." FOCS. Introduced garbled circuits. Shamir, A. (1979). "How to Share a Secret." Communications of the ACM. Introduced secret sharing.

### Federated Learning
McMahan, B. et al. (2017). "Communication-Efficient Learning of Deep Networks from Decentralized Data." AISTATS. Introduced FedAvg, the foundational federated learning algorithm.

### Zero-Knowledge Proofs
Goldwasser, S., Micali, S., Rackoff, C. (1989). "The Knowledge Complexity of Interactive Proof Systems." SIAM Journal on Computing. Formal definition of zero-knowledge proofs.
