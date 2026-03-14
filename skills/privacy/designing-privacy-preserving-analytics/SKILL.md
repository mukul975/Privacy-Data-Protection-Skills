---
name: designing-privacy-preserving-analytics
description: >-
  Design privacy-preserving analytics systems using differential privacy, k-anonymity,
  l-diversity, and t-closeness. Covers privacy budget allocation with epsilon tracking,
  references Google DP library, OpenDP, and Apple PPML. Includes Python differential
  privacy implementation for GDPR-compliant statistical analysis.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-by-design
  tags: "differential-privacy, k-anonymity, privacy-budget, opendp, privacy-preserving-analytics"
---

# Designing Privacy-Preserving Analytics

## Overview

Privacy-preserving analytics enables organizations to extract statistical insights from personal data without exposing individual-level information. This directly supports GDPR Article 5(1)(c) (data minimization) and Recital 26 (which exempts truly anonymous data from the regulation). The Article 29 Working Party Opinion 05/2014 on Anonymisation Techniques (WP216) established that effective anonymization must resist singling out, linkability, and inference attacks.

Four primary statistical disclosure control techniques form the foundation of privacy-preserving analytics: differential privacy, k-anonymity, l-diversity, and t-closeness. Each offers different trade-offs between privacy guarantees and data utility.

## Statistical Disclosure Control Techniques

### Differential Privacy

Differential privacy (Dwork et al., 2006) provides a mathematical guarantee that the output of an analysis is approximately the same whether or not any single individual's data is included. Formally, a randomized mechanism M satisfies (epsilon, delta)-differential privacy if for all datasets D1 and D2 differing in at most one record, and for all sets of outputs S:

```
P[M(D1) ∈ S] ≤ e^ε × P[M(D2) ∈ S] + δ
```

Where epsilon (ε) is the privacy loss parameter and delta (δ) bounds the probability of privacy breach.

**Privacy Budget Allocation:**

| Epsilon Range | Privacy Level | Typical Use Cases |
|--------------|---------------|-------------------|
| 0.01 — 0.1 | Very strong | Medical research, genetic data, highly sensitive analytics |
| 0.1 — 1.0 | Strong | General-purpose analytics, demographic analysis |
| 1.0 — 5.0 | Moderate | Aggregate business metrics, trend analysis |
| 5.0 — 10.0 | Weak | Low-sensitivity counts, already-public statistics |

**Key Libraries:**

| Library | Maintainer | Language | Mechanism Types |
|---------|-----------|----------|-----------------|
| Google DP Library | Google | C++/Java/Go | Laplace, Gaussian, partition selection |
| OpenDP | Harvard IQSS & Microsoft | Rust/Python | Composable framework, Laplace, Gaussian, exponential |
| Apple PPML | Apple | Swift | Local DP, count-mean-sketch, Hadamard response |
| IBM diffprivlib | IBM Research | Python | Scikit-learn compatible, ML with DP |
| PyDP | OpenMined | Python (C++ backend) | Python wrapper around Google DP library |

### k-Anonymity

A dataset satisfies k-anonymity (Sweeney, 2002) if every record is indistinguishable from at least k-1 other records with respect to quasi-identifier attributes. Quasi-identifiers are attributes that could be combined with external data to re-identify individuals (e.g., age, postal code, gender).

**Implementation approach:**
1. Identify quasi-identifiers in the dataset
2. Apply generalization hierarchies (e.g., age 27 → age range 25-30, postal code 8001 → 80**)
3. Apply suppression for records that cannot achieve k-anonymity through generalization alone
4. Verify k-value across all equivalence classes

**Limitations:** k-anonymity does not protect against attribute disclosure when sensitive values within an equivalence class are homogeneous.

### l-Diversity

l-Diversity (Machanavajjhala et al., 2007) extends k-anonymity by requiring that each equivalence class contains at least l "well-represented" values of the sensitive attribute. This prevents attribute disclosure attacks.

**Variants:**
- **Distinct l-diversity:** Each equivalence class has at least l distinct sensitive values
- **Entropy l-diversity:** Entropy of sensitive values in each class ≥ log(l)
- **Recursive (c,l)-diversity:** The most frequent sensitive value appears less than c times the frequency of the least frequent value

### t-Closeness

t-Closeness (Li et al., 2007) requires that the distribution of a sensitive attribute in any equivalence class is within distance t of the distribution of the attribute in the entire dataset, measured using Earth Mover's Distance (EMD).

This prevents skewness attacks where an adversary can infer sensitive attributes from the distribution within an equivalence class, even when l-diversity is satisfied.

## Privacy Budget Management

Privacy budgets track cumulative privacy loss across multiple queries. Under sequential composition, the total privacy loss is the sum of individual epsilons. Under parallel composition (disjoint subsets), the total privacy loss is the maximum individual epsilon.

**Budget Allocation Framework for Prism Data Systems AG:**

| Analytics Function | Epsilon Allocation | Refresh Cadence | Justification |
|-------------------|-------------------|-----------------|---------------|
| Daily active user counts | 0.1 per day | Daily | Low sensitivity, high frequency |
| Revenue by region | 0.5 per quarter | Quarterly | Medium sensitivity, aggregate metric |
| Feature usage patterns | 0.3 per month | Monthly | Used for product development under Art. 6(1)(f) |
| Customer churn analysis | 0.2 per quarter | Quarterly | Involves behavioral profiling |
| A/B test results | 0.1 per experiment | Per experiment | Binary outcome, low disclosure risk |
| **Total annual budget** | **≤ 8.0** | | Sum across all functions with composition |

**Budget Exhaustion Protocol:**
1. When 80% of annual budget is consumed, alert the Data Protection Officer
2. When 95% is consumed, require DPO approval for each additional query
3. When 100% is consumed, block all further differentially private queries until the next budget period
4. Emergency queries require joint approval from DPO and Chief Information Security Officer

## Architecture Design

```
┌──────────────────────────────────────────────────────────┐
│                    Analyst Interface                      │
│              (SQL-like query submission)                  │
└──────────────────────┬───────────────────────────────────┘
                       │
┌──────────────────────▼───────────────────────────────────┐
│                 Privacy Gateway                           │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────┐  │
│  │ Query Parser │  │ Budget Check │  │ Sensitivity    │  │
│  │ & Validator  │  │ (ε tracker)  │  │ Calibration    │  │
│  └──────┬──────┘  └──────┬───────┘  └───────┬────────┘  │
│         └────────────────┼──────────────────┘            │
└──────────────────────────┼───────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────┐
│              Noise Injection Layer                        │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │ Laplace      │  │ Gaussian     │  │ Exponential   │  │
│  │ Mechanism    │  │ Mechanism    │  │ Mechanism     │  │
│  └──────────────┘  └──────────────┘  └───────────────┘  │
└──────────────────────────┬───────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────┐
│              Data Processing Layer                        │
│  ┌─────────────────┐  ┌──────────────────────────────┐   │
│  │ k-Anonymization │  │ Aggregation Engine           │   │
│  │ Pre-processing  │  │ (min group size: 11)         │   │
│  └─────────────────┘  └──────────────────────────────┘   │
└──────────────────────────┬───────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────┐
│              Encrypted Data Store                         │
│         (Field-level AES-256-GCM encrypted)              │
└──────────────────────────────────────────────────────────┘
```

## Implementation Workflow

1. **Classify Analytics Queries** — Categorize each analytics use case by sensitivity (direct identifiers accessed, quasi-identifiers combined, sensitive attributes involved) and assign an epsilon budget allocation.

2. **Select Mechanism** — Choose the appropriate noise mechanism based on query type: Laplace for counting queries, Gaussian for mean/variance queries requiring (ε,δ)-DP, exponential mechanism for selection queries.

3. **Calibrate Sensitivity** — Determine the global sensitivity of each query function (maximum change in output when one record is added or removed). Use bounded sensitivity where possible by clipping input values.

4. **Implement Budget Tracking** — Deploy a centralized privacy budget ledger that records every query's epsilon consumption, enforces composition bounds, and blocks queries when the budget is exhausted.

5. **Apply Pre-processing** — Where differential privacy alone provides insufficient utility, apply k-anonymity as a pre-processing step to reduce the sensitivity of downstream DP queries.

6. **Validate Output** — Verify that released statistics do not violate minimum group sizes (11 records per Prism Data Systems AG policy) and that confidence intervals are reported alongside noised results.

7. **Audit Trail** — Log every privacy-preserving query with: timestamp, analyst identity, query hash, epsilon consumed, mechanism used, and cumulative budget remaining.

## Key Regulatory References

- GDPR Article 5(1)(c) — Data minimization principle
- GDPR Article 5(1)(e) — Storage limitation
- GDPR Article 25 — Data protection by design and by default
- GDPR Article 89 — Safeguards for processing for scientific/historical research or statistical purposes
- GDPR Recital 26 — Scope of anonymous information
- GDPR Recital 162 — Statistical purposes
- Article 29 Working Party Opinion 05/2014 on Anonymisation Techniques (WP216)
- ENISA Report: Pseudonymisation techniques and best practices (November 2019)
