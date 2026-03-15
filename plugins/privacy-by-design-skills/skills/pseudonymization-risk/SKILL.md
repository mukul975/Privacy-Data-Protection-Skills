---
name: pseudonymization-risk
description: >-
  Assessment of pseudonymization techniques and re-identification risk. Covers
  tokenization, hashing, encryption-based pseudonymization, and hybrid approaches.
  Includes re-identification risk scoring using the motivated intruder test,
  quantitative metrics (marketer, journalist, prosecutor models), and linkage
  attack resilience evaluation. References ENISA 2019 pseudonymization report.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-by-design
  tags: "pseudonymization, re-identification, tokenization, hashing, enisa, motivated-intruder, linkage-attack"
---

# Assessing Pseudonymization and Re-Identification Risk

## Overview

Pseudonymization (GDPR Article 4(5)) means processing personal data in such a manner that the data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to technical and organisational measures to ensure non-attribution. Unlike anonymization (Recital 26), pseudonymized data remains personal data — but it significantly reduces risk and is explicitly recognized as an appropriate safeguard under Articles 25, 32, and 89.

The ENISA report "Pseudonymisation Techniques and Best Practices" (November 2019) provides a comprehensive taxonomy of pseudonymization techniques and their properties. This skill implements a structured assessment framework for selecting appropriate techniques and quantifying residual re-identification risk.

## Pseudonymization Techniques Taxonomy

### Technique 1: Counter-Based Pseudonyms

| Property | Value |
|----------|-------|
| Mechanism | Sequential or random counter assigned to each identifier |
| Reversibility | Reversible via lookup table |
| Collision resistance | Guaranteed (bijective mapping) |
| Performance | O(1) lookup |
| Storage overhead | Mapping table size proportional to identifier count |
| Key management | Protect the mapping table as additional information |

**Prism Data Systems AG Implementation:**
Customer IDs are replaced with UUIDv4 pseudonyms at the analytics ingestion boundary. The mapping table is stored in a separate HSM-backed database accessible only to the DPO and the identity resolution service (which requires dual-approval access).

### Technique 2: Cryptographic Hashing (HMAC)

| Property | Value |
|----------|-------|
| Mechanism | HMAC-SHA256 with secret key applied to identifier |
| Reversibility | Not directly reversible; vulnerable to brute-force on low-entropy inputs |
| Collision resistance | Negligible collision probability (256-bit output) |
| Performance | O(1) computation |
| Storage overhead | Fixed 32-byte output per identifier |
| Key management | HMAC key must be protected as additional information |

**Risk:** Plain SHA-256 hashing (without key) is vulnerable to rainbow table attacks on low-entropy identifiers like email addresses. HMAC with a secret key mitigates this but the key becomes the single point of re-identification.

**Prism Data Systems AG Implementation:**
HMAC-SHA256 with a 256-bit key rotated quarterly is used for pseudonymizing user identifiers in the analytics pipeline. The HMAC key is stored in AWS KMS with access restricted to the pseudonymization service account. Key rotation triggers re-pseudonymization of the active analytics dataset.

### Technique 3: Encryption-Based Pseudonymization

| Property | Value |
|----------|-------|
| Mechanism | AES-256-GCM or format-preserving encryption (FF1/FF3-1) |
| Reversibility | Fully reversible with decryption key |
| Collision resistance | Guaranteed (bijective for same key) |
| Performance | O(1) computation; FPE slower than standard AES |
| Storage overhead | Ciphertext size ≈ plaintext + 16-byte tag (GCM) |
| Key management | Encryption key is the additional information per Art. 4(5) |

**Format-Preserving Encryption** preserves the format of the original identifier (e.g., encrypting a 10-digit phone number produces another 10-digit number), enabling pseudonymization without schema changes.

**Prism Data Systems AG Implementation:**
FPE (FF3-1 mode) is used for pseudonymizing phone numbers and IBAN fields in the support ticket system. This allows Tier 1 support agents to see structurally valid but pseudonymized identifiers, reducing accidental exposure while maintaining workflow compatibility.

### Technique 4: Tokenization

| Property | Value |
|----------|-------|
| Mechanism | Random token generated and stored in a secure vault; no mathematical relationship to original |
| Reversibility | Reversible only via vault lookup |
| Collision resistance | Guaranteed by vault uniqueness constraint |
| Performance | O(1) vault lookup; network latency for centralized vault |
| Storage overhead | Vault stores original-to-token mapping |
| Key management | Vault access controls replace key management |

**Prism Data Systems AG Implementation:**
Payment card data is tokenized using a PCI DSS-compliant token vault. The vault is operated by the payment processor and is logically separated from Prism's infrastructure. Detokenization requires a PCI-scoped service account with transaction-level authorization.

### Technique 5: Synthetic Data Replacement

| Property | Value |
|----------|-------|
| Mechanism | Replace real identifiers with structurally similar but fictional values |
| Reversibility | Not reversible (one-way replacement) |
| Collision resistance | Depends on generation method; risk of accidental collision with real data |
| Performance | O(1) generation |
| Storage overhead | No mapping table needed (irreversible) |
| Key management | Not applicable |

**Use case:** Test environments where referential integrity must be maintained but no re-identification path is acceptable.

## Technique Comparison Matrix

| Criterion | Counter | HMAC | Encryption | Tokenization | Synthetic |
|-----------|---------|------|------------|-------------|-----------|
| Reversibility | Lookup table | Brute-force only | Decryption key | Vault lookup | Irreversible |
| Deterministic | Configurable | Yes (same key) | Yes (same key+IV) | Configurable | No |
| Format preserving | No | No | FPE only | Configurable | Yes |
| Linkability (same dataset) | Yes | Yes | Yes | Configurable | No |
| Linkability (cross-dataset) | No | Same key: Yes | Same key: Yes | No | No |
| Brute-force resistance | N/A | Key-dependent | Key-dependent | N/A | N/A |
| Suited for analytics | Yes | Yes | Limited | Yes | Limited |
| Suited for testing | No | No | No | Yes | Yes |
| ENISA recommendation level | Basic | Intermediate | Advanced | Advanced | Specialized |

## Re-Identification Risk Assessment Framework

### The Motivated Intruder Test

The UK Information Commissioner's Office (ICO) Anonymisation Code of Practice defines the motivated intruder test: would a reasonably competent, motivated person with access to resources such as the internet, public libraries, and public records be able to identify an individual from the pseudonymized data?

**Assessment Factors:**

| Factor | Low Risk (1) | Medium Risk (3) | High Risk (5) |
|--------|-------------|-----------------|---------------|
| Population uniqueness | Common attributes, large equivalence classes | Moderate uniqueness, some rare combinations | Highly unique attribute combinations |
| Auxiliary information availability | No public datasets linkable | Some public records overlap | Rich public profiles (social media, registers) |
| Identifier entropy | High entropy (e.g., UUID) | Medium entropy (e.g., hashed email) | Low entropy (e.g., hashed phone number) |
| Dataset richness | Few quasi-identifiers | Moderate quasi-identifiers (5-10) | Many quasi-identifiers (>10) |
| Temporal precision | Yearly or coarser | Monthly | Daily or finer |
| Geographic precision | Country level | Region/city level | Postcode or finer |
| Domain sensitivity | Low sensitivity domain | Moderate sensitivity | Health, financial, political data |

### Quantitative Risk Models

#### Prosecutor Model
The attacker knows a specific individual is in the dataset and attempts to find their record. Risk = 1 / k, where k is the size of the equivalence class containing the target record.

#### Journalist Model
The attacker does not know if the target is in the dataset but attempts to re-identify any individual for a story. Risk = max(1/k) across all equivalence classes (the smallest group is most vulnerable).

#### Marketer Model
The attacker attempts to re-identify as many individuals as possible. Risk = (1/n) * Σ(1/k_i) — the average re-identification probability across all records.

### Linkage Attack Categories

| Attack Type | Description | Mitigation |
|-------------|-------------|------------|
| Record linkage | Matching pseudonymized records with identified records in external datasets using quasi-identifiers | Generalize quasi-identifiers, enforce k-anonymity |
| Attribute linkage | Inferring sensitive attributes from group characteristics even without identifying the individual | Enforce l-diversity on sensitive attributes |
| Table linkage | Determining that an individual is present in a sensitive dataset (membership inference) | Apply differential privacy, enforce t-closeness |
| Composition attack | Combining multiple independent pseudonymized releases to narrow equivalence classes | Track cumulative privacy budget, limit releases |
| Temporal linkage | Linking records across time periods using behavioral patterns or trajectory data | Apply temporal generalization, add noise to timestamps |

## Risk Scoring Methodology

### Step 1: Technique Assessment (0-100)

Score the pseudonymization technique on five properties:

| Property | Weight | Score Range |
|----------|--------|-------------|
| Key/mapping security | 30% | 0-100 based on key management maturity |
| Brute-force resistance | 25% | 0-100 based on input entropy and computational cost |
| Cross-dataset unlinkability | 20% | 0-100 based on determinism and key reuse |
| Implementation maturity | 15% | 0-100 based on library validation and audit history |
| Operational resilience | 10% | 0-100 based on key rotation, backup, disaster recovery |

### Step 2: Data Environment Assessment (0-100)

Score the data environment on re-identification risk factors:

| Factor | Weight | Score Range |
|--------|--------|-------------|
| Population uniqueness | 25% | 0-100 (higher = more unique = higher risk) |
| Auxiliary data availability | 25% | 0-100 (higher = more auxiliary data = higher risk) |
| Quasi-identifier count | 20% | 0-100 based on number and granularity |
| Dataset size | 15% | 0-100 (smaller datasets = higher risk per record) |
| Release frequency | 15% | 0-100 (more frequent releases = higher composition risk) |

### Step 3: Residual Risk Score

```
Residual Risk = Data Environment Risk × (1 - Technique Score / 100)
```

| Residual Risk Range | Classification | Action Required |
|--------------------|----------------|-----------------|
| 0-15 | Low | Acceptable. Document and monitor |
| 16-35 | Moderate | Additional controls recommended |
| 36-60 | High | Technique upgrade or data reduction required |
| 61-100 | Very High | Processing should not proceed without anonymization |

## Prism Data Systems AG — Assessment Summary

| Data Flow | Technique | Technique Score | Environment Risk | Residual Risk | Classification |
|-----------|-----------|----------------|-----------------|---------------|----------------|
| Analytics pipeline | HMAC-SHA256 (keyed) | 78 | 42 | 9.2 | Low |
| Support dashboard | FPE (FF3-1) | 82 | 35 | 6.3 | Low |
| Payment processing | Tokenization (vault) | 91 | 55 | 5.0 | Low |
| Test environments | Synthetic replacement | 95 | 20 | 1.0 | Low |
| Research exports | Counter + k-anonymity | 72 | 58 | 16.2 | Moderate |
| ML training data | HMAC + differential privacy | 85 | 48 | 7.2 | Low |

The research exports flow received a "Moderate" classification due to the combination of rich quasi-identifiers in the exported dataset and the counter-based technique's susceptibility to record linkage. Remediation: apply l-diversity (l≥3) on sensitive attributes and generalize quasi-identifiers to achieve k≥11 before export.

## Key Regulatory References

- GDPR Article 4(5) — Definition of pseudonymization
- GDPR Recital 26 — Anonymization vs. pseudonymization distinction
- GDPR Article 25(1) — Pseudonymization as a data protection by design measure
- GDPR Article 32(1)(a) — Pseudonymization as a security measure
- GDPR Article 89(1) — Pseudonymization for research processing safeguards
- ENISA "Pseudonymisation Techniques and Best Practices" (November 2019)
- ICO Anonymisation Code of Practice — Motivated intruder test
- Article 29 Working Party Opinion 05/2014 (WP216) on Anonymisation Techniques
- EDPB Guidelines 4/2019 on Article 25 — Pseudonymization as by-design measure
