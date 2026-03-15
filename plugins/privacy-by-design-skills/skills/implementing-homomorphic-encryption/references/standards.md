# Homomorphic Encryption Standards and References

## Regulatory Basis

### GDPR Article 32(1)(a) — Encryption as Security Measure
The controller and the processor shall implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk, including inter alia as appropriate: (a) the pseudonymisation and encryption of personal data.

### GDPR Article 25(1) — Data Protection by Design
The controller shall implement appropriate technical and organisational measures, such as pseudonymisation, which are designed to implement data-protection principles in an effective manner.

### GDPR Article 28 — Processor Obligations
HE enables a processing model where the processor computes on encrypted data and never accesses plaintext personal data, strengthening the Article 28 relationship by cryptographically enforcing data confidentiality.

### GDPR Recital 83 — Security and Encryption
The controller or processor should evaluate the risks inherent in the processing and implement measures to mitigate those risks, such as encryption.

## Standardization

### HomomorphicEncryption.org Standard (2018)
Community standard for homomorphic encryption parameters, API design, and security levels. Defines recommended parameter sets for 128-bit, 192-bit, and 256-bit security. Supported by Microsoft, Google, IBM, Intel, Samsung, and NIST.

### NIST Post-Quantum Cryptography Project
Lattice-based HE schemes (BFV, BGV, CKKS) are built on the Ring Learning With Errors (RLWE) problem, which is believed to be resistant to quantum attacks. This aligns HE with post-quantum security requirements.

## Library Documentation

### Microsoft SEAL
Open-source HE library implementing BFV and CKKS schemes. Written in C++ with .NET wrapper. Supports SIMD batching, automatic modulus switching, and serialization. Recommended for enterprise deployments due to documentation quality and Microsoft support.

### IBM HELib
Open-source HE library implementing BGV scheme with bootstrapping support. Written in C++. Optimized for deep circuits and large-scale SIMD operations. Includes the HElayers Python API for higher-level operations.

### Google FHE Transpiler
Converts C++ functions into FHE-compatible circuit representations. Uses TFHE as backend. Enables developers to write computation in standard C++ and automatically generates encrypted versions.

### OpenFHE
Open-source library supporting BFV, BGV, CKKS, and TFHE schemes. Written in C++ with Python bindings. Successor to PALISADE. Supports advanced features including proxy re-encryption, threshold FHE, and scheme switching.

### Concrete (Zama)
TFHE-based library with Rust and Python APIs. Includes the Concrete ML library for privacy-preserving ML inference. Compiles standard ML models (scikit-learn, XGBoost) to FHE circuits.

## Academic Foundations

### Gentry (2009)
"A Fully Homomorphic Encryption Scheme." First construction showing that FHE is theoretically possible using ideal lattices and bootstrapping.

### Brakerski/Fan-Vercauteren (BFV, 2012)
"Somewhat Practical Fully Homomorphic Encryption." Practical scheme for exact integer arithmetic based on RLWE.

### Cheon-Kim-Kim-Song (CKKS, 2017)
"Homomorphic Encryption for Arithmetic of Approximate Numbers." Scheme supporting approximate computation on real and complex numbers, enabling ML inference on encrypted data.

### TFHE (Chillotti et al., 2020)
"TFHE: Fast Fully Homomorphic Encryption over the Torus." Fast bootstrapping enabling gate-by-gate evaluation of arbitrary functions.
