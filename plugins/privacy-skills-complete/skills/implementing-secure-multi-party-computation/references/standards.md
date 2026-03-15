# Secure Multi-Party Computation Standards and References

## Academic Foundations

### Yao's Garbled Circuits (1986)
Yao, A.C. "How to Generate and Exchange Secrets." FOCS. Introduced the garbled circuit protocol for secure two-party computation, enabling one party to garble a boolean circuit and the other to evaluate it without learning intermediate values.

### Shamir's Secret Sharing (1979)
Shamir, A. "How to Share a Secret." Communications of the ACM. Introduced threshold secret sharing (t-out-of-n), fundamental to multi-party computation protocols.

### SPDZ Protocol (2012)
Damgard, I., Pastro, V., Smart, N.P., & Zakarias, S. "Multiparty Computation from Somewhat Homomorphic Encryption." CRYPTO. Efficient SMPC protocol with security against malicious adversaries using Beaver multiplication triples.

### MASCOT (2016)
Keller, M., Orsini, E., & Scholl, P. "MASCOT: Faster Malicious Arithmetic Secure Computation with Oblivious Transfer." ACM CCS. Improved preprocessing phase for SPDZ using OT extensions, significantly reducing preprocessing cost.

### ABY Framework (2015)
Demmler, D., Schneider, T., & Zohner, M. "ABY — A Framework for Efficient Mixed-Protocol Secure Two-Party Computation." NDSS. Framework supporting arithmetic, boolean, and Yao sharing with efficient conversion between share types.

## GDPR Regulatory Basis

### Article 5(1)(c) — Data Minimization
SMPC implements data minimization at the architectural level: parties compute jointly without sharing raw data, and each party's input remains private throughout the computation.

### Article 25(1) — Data Protection by Design
SMPC is a data-protection-by-design measure that cryptographically prevents unauthorized access to individual inputs during collaborative computation.

### Article 26 — Joint Controller Arrangements
SMPC consortia typically require joint controller agreements specifying each party's processing responsibilities, the computation to be performed, output sharing rules, and privacy parameters.

### Article 32(1) — Security of Processing
SMPC provides cryptographic security guarantees (information-theoretic for secret sharing, computational for garbled circuits) as part of the technical security measures under Article 32.

## Framework Documentation

### MP-SPDZ
Comprehensive SMPC framework implementing over 30 protocol variants. Written in C++ with a Python-like high-level language for computation specification. Supports semi-honest and malicious security models. Maintained by Marcel Keller (CSIRO). Available at github.com/data61/MP-SPDZ.

### CrypTen
Meta's framework for privacy-preserving ML using SMPC. Built on PyTorch. Supports secret-shared tensor operations for ML training and inference. Provides a familiar PyTorch-like API for ML engineers. Available at github.com/facebookresearch/CrypTen.

### Sharemind
Enterprise SMPC platform using additive 3-party secret sharing with honest majority. Includes the SecreC domain-specific language for specifying secure computations. Commercial deployment support from Cybernetica AS.

### MOTION
High-performance SMPC framework implementing GMW and BMR protocols. Written in C++ with focus on computational efficiency. Supports arithmetic and boolean sharing. Available at github.com/encryptogroup/MOTION.
