# Differential Privacy in Production — Standards References

## Foundational Papers

### Dwork and Roth (2014)
- "The Algorithmic Foundations of Differential Privacy." Foundations and Trends in Theoretical Computer Science, 9(3-4):211-407.
- Definitive reference for differential privacy theory, mechanisms, and composition.

### Mironov (2017)
- "Renyi Differential Privacy." IEEE CSF, 2017.
- Introduces RDP composition for tighter privacy accounting.

### Abadi et al. (2016)
- "Deep Learning with Differential Privacy." ACM CCS, 2016.
- DP-SGD algorithm and moments accountant for ML training.

## Industry Implementations

### Google Differential Privacy Library
- Open-source C++ and Go implementations of core DP mechanisms
- Used in RAPPOR for Chrome telemetry collection

### Apple Differential Privacy
- Technical Overview published 2017
- Local differential privacy for iOS telemetry (emoji usage, Safari, Health)

### U.S. Census Bureau (2020)
- Disclosure Avoidance System for 2020 Census
- First large-scale deployment of formal differential privacy for national statistics

## Libraries and Tools

### OpenDP Project (opendp.org)
- Community-driven framework for statistical analyses with provable privacy guarantees
- Harvard Privacy Tools Project

### Google dp Library (github.com/google/differential-privacy)
- Production-ready DP building blocks in C++, Go, Java

### IBM diffprivlib
- Python library for DP machine learning built on scikit-learn

### PyTorch Opacus
- DP-SGD training for PyTorch models with privacy accounting

### TensorFlow Privacy
- DP-SGD training for TensorFlow models
