# Pseudonymization and Re-Identification Risk Assessment Report

## Organization Information

| Item | Value |
|------|-------|
| Organization | Prism Data Systems AG |
| Assessment Date | 2026-03-14 |
| Assessor | Thomas Richter (Privacy Engineering Lead) |
| DPO Reviewer | Dr. Lukas Meier |
| Scope | All pseudonymized data flows in production |
| Reference Standard | ENISA Pseudonymisation Techniques and Best Practices (2019) |

## Data Flow Inventory

| # | Data Flow | Source System | Destination | Technique | Key Storage |
|---|-----------|--------------|-------------|-----------|-------------|
| 1 | Analytics pipeline | Application servers | Analytics warehouse | HMAC-SHA256 (keyed) | AWS KMS (eu-central-1) |
| 2 | Support dashboard | CRM database | Support portal | FPE (FF3-1) | Azure Key Vault |
| 3 | Payment processing | Checkout service | Payment processor | Tokenization (vault) | PCI token vault (processor-hosted) |
| 4 | Test environments | Production mirror | Dev/staging | Synthetic replacement | N/A (irreversible) |
| 5 | Research exports | Data lake | Research partners | Counter + k-anonymity | HSM-backed mapping DB |
| 6 | ML training data | Feature store | Training pipeline | HMAC + differential privacy | AWS KMS (eu-central-1) |

## Technique Assessments

### Data Flow 1: Analytics Pipeline (HMAC-SHA256)

| Property | Score (0-100) | Weight | Weighted |
|----------|-------------|--------|----------|
| Key/mapping security | 82 | 30% | 24.6 |
| Brute-force resistance | 75 | 25% | 18.8 |
| Cross-dataset unlinkability | 65 | 20% | 13.0 |
| Implementation maturity | 85 | 15% | 12.8 |
| Operational resilience | 78 | 10% | 7.8 |
| **Technique Score** | | | **77.0** |

Notes: HMAC key stored in AWS KMS with quarterly rotation. Same key used across analytics datasets enables cross-dataset linkage — mitigated by per-quarter key rotation creating temporal unlinkability. Key access restricted to pseudonymization service account (arn:aws:iam::123456789012:role/PseudonymizationService).

### Data Flow 2: Support Dashboard (FPE FF3-1)

| Property | Score (0-100) | Weight | Weighted |
|----------|-------------|--------|----------|
| Key/mapping security | 88 | 30% | 26.4 |
| Brute-force resistance | 80 | 25% | 20.0 |
| Cross-dataset unlinkability | 70 | 20% | 14.0 |
| Implementation maturity | 78 | 15% | 11.7 |
| Operational resilience | 82 | 10% | 8.2 |
| **Technique Score** | | | **80.3** |

Notes: FPE preserves phone number format (10-digit to 10-digit) allowing support agents to verify format without exposure. Encryption key in Azure Key Vault with hardware security module backing. Decryption requires Tier 2 escalation approval.

### Data Flow 3: Payment Processing (Tokenization)

| Property | Score (0-100) | Weight | Weighted |
|----------|-------------|--------|----------|
| Key/mapping security | 95 | 30% | 28.5 |
| Brute-force resistance | 92 | 25% | 23.0 |
| Cross-dataset unlinkability | 90 | 20% | 18.0 |
| Implementation maturity | 88 | 15% | 13.2 |
| Operational resilience | 85 | 10% | 8.5 |
| **Technique Score** | | | **91.2** |

Notes: PCI DSS Level 1 compliant token vault operated by payment processor. No mathematical relationship between token and original PAN. Detokenization requires transaction-level authorization from PCI-scoped service account.

### Data Flow 4: Test Environments (Synthetic Replacement)

| Property | Score (0-100) | Weight | Weighted |
|----------|-------------|--------|----------|
| Key/mapping security | 100 | 30% | 30.0 |
| Brute-force resistance | 95 | 25% | 23.8 |
| Cross-dataset unlinkability | 100 | 20% | 20.0 |
| Implementation maturity | 82 | 15% | 12.3 |
| Operational resilience | 90 | 10% | 9.0 |
| **Technique Score** | | | **95.1** |

Notes: Irreversible replacement — no mapping exists. Synthetic values generated using Faker library with Swiss locale. Referential integrity maintained via deterministic seed per source record.

### Data Flow 5: Research Exports (Counter + k-Anonymity)

| Property | Score (0-100) | Weight | Weighted |
|----------|-------------|--------|----------|
| Key/mapping security | 75 | 30% | 22.5 |
| Brute-force resistance | 60 | 25% | 15.0 |
| Cross-dataset unlinkability | 70 | 20% | 14.0 |
| Implementation maturity | 80 | 15% | 12.0 |
| Operational resilience | 72 | 10% | 7.2 |
| **Technique Score** | | | **70.7** |

Notes: Counter-based pseudonyms with k-anonymity (k=5) applied to quasi-identifiers. Mapping table in HSM-backed PostgreSQL accessible only to DPO. Lower brute-force score due to limited quasi-identifier generalization in current export format.

### Data Flow 6: ML Training Data (HMAC + Differential Privacy)

| Property | Score (0-100) | Weight | Weighted |
|----------|-------------|--------|----------|
| Key/mapping security | 85 | 30% | 25.5 |
| Brute-force resistance | 82 | 25% | 20.5 |
| Cross-dataset unlinkability | 80 | 20% | 16.0 |
| Implementation maturity | 88 | 15% | 13.2 |
| Operational resilience | 80 | 10% | 8.0 |
| **Technique Score** | | | **83.2** |

Notes: HMAC pseudonymization combined with Gaussian differential privacy (epsilon=1.0, delta=1e-5) on feature vectors. Privacy budget tracked per training run. Membership inference testing conducted quarterly.

## Data Environment Risk Assessments

| Data Flow | Pop. Uniq. (25%) | Aux. Data (25%) | QI Count (20%) | Dataset Size (15%) | Release Freq. (15%) | **Env. Risk** |
|-----------|-----------------|----------------|----------------|-------------------|--------------------|----|
| Analytics pipeline | 45 | 40 | 50 | 30 | 45 | **42.3** |
| Support dashboard | 35 | 30 | 40 | 35 | 20 | **32.5** |
| Payment processing | 50 | 55 | 45 | 25 | 30 | **43.0** |
| Test environments | 10 | 10 | 15 | 10 | 5 | **10.3** |
| Research exports | 55 | 60 | 50 | 40 | 35 | **50.3** |
| ML training data | 40 | 45 | 48 | 35 | 40 | **42.1** |

## Re-Identification Risk Scoring

### Quantitative Risk Models

| Data Flow | Prosecutor Risk | Journalist Risk | Marketer Risk | Aux. Amplification | Adjusted Risk |
|-----------|----------------|-----------------|---------------|--------------------|----|
| Analytics pipeline | 50.0% | 50.0% | 50.0% | 1.5x (moderate) | 75.0% |
| Support dashboard | 33.3% | 33.3% | 33.3% | 1.0x (low) | 33.3% |
| Payment processing | N/A (tokenized) | N/A | N/A | N/A | N/A |
| Test environments | N/A (synthetic) | N/A | N/A | N/A | N/A |
| Research exports | 20.0% | 20.0% | 20.0% | 2.0x (high) | 40.0% |
| ML training data | 10.0% | 10.0% | 8.3% | 1.5x (moderate) | 15.0% |

Note: Prosecutor/journalist/marketer risks above are computed on the pseudonymized dataset before additional controls (k-anonymity, DP). After applying k-anonymity (k=11) and differential privacy, effective risks are substantially lower.

## Residual Risk Summary

| Data Flow | Technique Score | Env. Risk | Residual Risk | Classification | Acceptable |
|-----------|----------------|-----------|---------------|----------------|------------|
| Analytics pipeline | 77.0 | 42.3 | 9.7 | LOW | Yes |
| Support dashboard | 80.3 | 32.5 | 6.4 | LOW | Yes |
| Payment processing | 91.2 | 43.0 | 3.8 | LOW | Yes |
| Test environments | 95.1 | 10.3 | 0.5 | LOW | Yes |
| Research exports | 70.7 | 50.3 | 14.7 | LOW | Yes (marginal) |
| ML training data | 83.2 | 42.1 | 7.1 | LOW | Yes |

## Findings and Remediations

| # | Data Flow | Finding | Severity | Remediation | Target Date |
|---|-----------|---------|----------|-------------|-------------|
| 1 | Research exports | k-anonymity at k=5 is below recommended k=11 threshold | Medium | Increase generalization on age and location quasi-identifiers to achieve k>=11 | 2026-04-30 |
| 2 | Research exports | High auxiliary data availability (public company registers overlap with exported fields) | Medium | Remove company_name from export schema; apply l-diversity (l>=3) on industry attribute | 2026-04-30 |
| 3 | Analytics pipeline | Same HMAC key used across quarterly datasets enables temporal linkage | Low | Implement per-quarter key rotation with automatic re-pseudonymization of active dataset | 2026-06-14 |
| 4 | ML training data | No membership inference testing has been conducted in last 2 quarters | Low | Schedule membership inference audit with ML security team | 2026-04-15 |

## Linkage Attack Resilience

| Attack Type | Analytics | Support | Payment | Test | Research | ML Training |
|-------------|-----------|---------|---------|------|----------|-------------|
| Record linkage | Moderate (HMAC linkable with same key) | Low (FPE per-system key) | Minimal (random tokens) | None (synthetic) | Moderate (counter-based) | Low (HMAC + DP noise) |
| Attribute linkage | Low (limited sensitive attrs) | Low (no sensitive attrs exposed) | N/A | N/A | Medium (industry attr has low diversity) | Low (DP noise protects) |
| Membership inference | Low | Low | Minimal | None | Low | Medium (model memorization risk) |
| Composition attack | Low (quarterly key rotation) | Minimal (single-use) | Minimal | None | Medium (annual releases) | Low (budget tracked) |

## Approval

| Role | Name | Decision | Date |
|------|------|----------|------|
| Privacy Engineering Lead | Thomas Richter | Assessment verified | 2026-03-14 |
| Data Protection Officer | Dr. Lukas Meier | Approved with conditions (findings #1-2 must be resolved by 2026-04-30) | 2026-03-14 |

## Next Assessment

Scheduled: 2026-06-14 (quarterly) and upon any new data flow involving pseudonymized personal data, or when significant new auxiliary data sources are identified.
