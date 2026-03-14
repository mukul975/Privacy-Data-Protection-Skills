# PET Selection Assessment Template

## Processing Activity

| Item | Value |
|------|-------|
| Activity Name | Customer Behavior Analytics |
| Organization | Prism Data Systems AG |
| Assessment Date | 2026-03-14 |
| Assessor | Thomas Richter (Privacy Engineering Lead) |
| DPO Review | Dr. Lukas Meier |

## Requirements Summary

| Requirement | Value |
|-------------|-------|
| Primary privacy property | Anonymity (statistical indistinguishability) |
| Secondary properties | Unlinkability |
| Adversary model | Honest-but-curious (internal analytics team) |
| Performance requirement | Batch (nightly processing acceptable) |
| Data categories | pseudonymized_user_id, feature_events, session_duration |
| Cross-organizational | No |
| Special categories (Art. 9) | No |
| Team cryptographic expertise | 3/5 (moderate) |
| Budget constraint | Medium |

## Candidate Evaluation

| PET | Score | Privacy Match | Performance Match | Maturity | Complexity | Recommendation |
|-----|-------|--------------|-------------------|----------|------------|----------------|
| Differential Privacy | 85/100 | Directly provides anonymity and unlinkability | Exceeds batch requirement (real-time capable) | 5/5 | 2/5 | **Primary selection** |
| Trusted Execution Environment | 62/100 | Provides confidentiality, not anonymity | Meets batch requirement | 4/5 | 3/5 | Consider as complement |
| Secure MPC | 55/100 | Provides confidentiality and minimization | Meets batch requirement | 4/5 | 4/5 | Not needed (single org) |
| Federated Learning | 48/100 | Provides minimization, not anonymity | Meets batch requirement | 4/5 | 3/5 | Not needed (single org) |
| Homomorphic Encryption | 42/100 | Provides confidentiality only | Meets batch requirement | 3/5 | 5/5 | Overhead unjustified |
| Zero-Knowledge Proofs | 38/100 | Provides minimization and integrity | Performance risk | 3/5 | 5/5 | Wrong use case |

## Selected PET: Differential Privacy

### Configuration

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Mechanism | Laplace (counting queries), Gaussian (mean/variance) | Standard mechanisms for analytics workloads |
| Epsilon (per query) | 0.3 | Strong privacy for behavioral data per NIST guidance |
| Delta | 1e-5 | Standard for dataset size of approximately 316,000 records |
| Annual budget | 3.6 (0.3 per month) | Allows monthly analytics refresh with strong guarantee |
| Minimum group size | 11 | Prism Data Systems AG standard for suppression threshold |
| Library | OpenDP 0.10+ | Composable framework with verified privacy accounting |

### GDPR Alignment

| GDPR Requirement | Alignment |
|-----------------|-----------|
| Art. 5(1)(c) data minimization | DP noise ensures statistical outputs cannot identify individuals |
| Art. 25(1) by design | DP implemented at the analytics pipeline boundary as a design measure |
| Art. 32(1) security measure | DP documented as a technical measure in security register |
| Recital 26 anonymization | At epsilon = 0.3, outputs satisfy Recital 26 standard for statistical outputs per WP216 criteria |
| Art. 35 DPIA | DP configuration documented in DPIA for analytics processing activity |

### Recommended Combination

| Complement PET | Rationale | Priority |
|---------------|-----------|----------|
| HMAC-SHA256 Pseudonymization | Pre-processing step: pseudonymize identifiers before analytics pipeline | Mandatory (already deployed) |
| Field-level encryption | Protect raw data at rest; DP protects query outputs | Mandatory (already deployed) |

## Approval

| Role | Name | Decision | Date |
|------|------|----------|------|
| Privacy Engineering Lead | Thomas Richter | Recommended | 2026-03-14 |
| Data Protection Officer | Dr. Lukas Meier | Approved | 2026-03-14 |
| CISO | Michael Baumann | Acknowledged | 2026-03-14 |

## Next Review Date

2027-03-14 — Annual PET effectiveness review
