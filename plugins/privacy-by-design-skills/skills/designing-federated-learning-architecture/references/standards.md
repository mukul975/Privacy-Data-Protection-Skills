# Federated Learning Standards and References

## Academic Foundations

### FedAvg
McMahan, B., Moore, E., Ramage, D., Hampson, S., & Arcas, B. (2017). "Communication-Efficient Learning of Deep Networks from Decentralized Data." AISTATS. Introduced the Federated Averaging algorithm for training deep networks across distributed participants.

### FedProx
Li, T., Sahu, A.K., Zaheer, M., Sanjabi, M., Talwalkar, A., & Smith, V. (2020). "Federated Optimization in Heterogeneous Networks." MLSys. Extended FedAvg with a proximal term for robustness in heterogeneous (non-IID) settings.

### Secure Aggregation
Bonawitz, K., et al. (2017). "Practical Secure Aggregation for Privacy-Preserving Machine Learning." ACM CCS. Protocol ensuring the server only learns the aggregate of client updates, not individual contributions.

### DP-FedAvg
McMahan, D., Ramage, D., Talwar, K., & Zhang, L. (2018). "Learning Differentially Private Recurrent Language Models." ICLR. Combined federated learning with user-level differential privacy.

### Gradient Inversion Attacks
Zhu, L., Liu, Z., & Han, S. (2019). "Deep Leakage from Gradients." NeurIPS. Demonstrated that shared gradients can reconstruct training data, motivating secure aggregation and DP.

## GDPR Regulatory Basis

### Article 5(1)(c) — Data Minimization
FL implements data minimization by sharing only model updates (gradients or parameters) rather than raw personal data. The raw data never leaves the participant's environment.

### Article 25(1) — Data Protection by Design
FL is a data-protection-by-design measure: the architecture inherently prevents centralized data collection while enabling collaborative model training.

### Article 26 — Joint Controller Arrangements
FL consortia typically require joint controller agreements specifying each party's responsibilities, the aggregation protocol, privacy parameters, and model ownership.

### Chapter V — Cross-Border Transfers
FL can reduce the need for international data transfers: instead of moving data across borders, only model updates (which are not personal data when properly anonymized) are exchanged.

## Framework Documentation

### TensorFlow Federated (TFF)
Google's open-source framework for FL research and production. Supports FedAvg, FedProx, and custom aggregation strategies. Integrates with TensorFlow's privacy library for DP.

### PySyft (OpenMined)
Privacy-preserving ML framework supporting FL, secure aggregation, and differential privacy. Python-based, integrates with PyTorch.

### NVIDIA FLARE
Enterprise FL framework for healthcare and finance. Supports federated averaging, federated proximal, secure aggregation, and heterogeneous participant management.

### Flower
Framework-agnostic FL framework supporting PyTorch, TensorFlow, scikit-learn, and custom backends. Designed for research flexibility with production scalability.

### FedML
End-to-end FL platform supporting cross-silo (enterprise) and cross-device (mobile) deployments. Includes MLOps for FL lifecycle management.
