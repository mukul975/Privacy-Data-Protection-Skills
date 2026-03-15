---
name: privacy-data-sharing
description: >-
  Build privacy-preserving data sharing platforms using synthetic data generation
  with the SDV library, data clean rooms, secure enclaves, and utility
  measurement. Covers end-to-end architecture for sharing analytical datasets
  while preserving individual privacy guarantees.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-engineering
  tags: "data-sharing, synthetic-data, data-clean-rooms, secure-enclaves, sdv-library"
---

# Privacy-Preserving Data Sharing Platform

## Overview

Privacy-preserving data sharing enables organizations to derive analytical value from combined datasets without exposing raw personal data. This skill covers four primary approaches: synthetic data generation, data clean rooms, secure enclaves, and federated analytics, along with utility measurement frameworks to ensure shared data remains useful.

## Approach Selection Framework

| Approach | Privacy Guarantee | Data Utility | Computational Cost | Trust Model |
|----------|-------------------|-------------|-------------------|-------------|
| Synthetic Data | Statistical (configurable) | High for distributions, lower for edge cases | Medium (training) | No trust required |
| Data Clean Rooms | Contractual + technical | High (real data, restricted queries) | Low-Medium | Trusted operator |
| Secure Enclaves (TEE) | Hardware-backed isolation | Very high (real data) | Medium | Trust hardware vendor |
| Federated Analytics | Cryptographic/DP | Medium-High | High (communication) | Minimal trust |
| Homomorphic Encryption | Cryptographic | High | Very High | No trust required |
| Secure Multi-Party Computation | Cryptographic | High | High | Honest majority |

## Synthetic Data Generation with SDV

### Architecture

```
Source Data --> Statistical Profiling --> Model Training --> Synthetic Generation
                    |                        |                      |
                    v                        v                      v
            Metadata Analysis        Model Selection         Quality Assessment
            - Column types           - GaussianCopula        - Statistical tests
            - Distributions          - CTGAN                 - Privacy metrics
            - Correlations           - CopulaGAN             - Utility metrics
            - Constraints            - TVAE                  - Visual comparison
```

### SDV Implementation

```python
"""
Synthetic data generation using the Synthetic Data Vault (SDV) library.
Generates privacy-preserving synthetic datasets that maintain statistical
properties of the original data.
"""

import pandas as pd
import numpy as np
from sdv.metadata import SingleTableMetadata
from sdv.single_table import GaussianCopulaSynthesizer, CTGANSynthesizer, TVAESynthesizer
from sdv.evaluation.single_table import run_diagnostic, evaluate_quality
from sdmetrics.reports.single_table import QualityReport


def create_metadata(df: pd.DataFrame) -> SingleTableMetadata:
    """Auto-detect and create metadata for a DataFrame."""
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(df)
    return metadata


def train_gaussian_copula(
    df: pd.DataFrame,
    metadata: SingleTableMetadata,
    enforce_min_max: bool = True
) -> GaussianCopulaSynthesizer:
    """
    Train a Gaussian Copula model for synthetic data generation.
    Best for: Datasets with mostly numerical data and linear correlations.
    """
    synthesizer = GaussianCopulaSynthesizer(
        metadata,
        enforce_min_max_values=enforce_min_max,
        numerical_distributions={
            "norm": "beta",  # Fit beta distributions for bounded numerical data
        }
    )
    synthesizer.fit(df)
    return synthesizer


def train_ctgan(
    df: pd.DataFrame,
    metadata: SingleTableMetadata,
    epochs: int = 300,
    batch_size: int = 500
) -> CTGANSynthesizer:
    """
    Train a CTGAN model for synthetic data generation.
    Best for: Complex distributions, mixed data types, mode-specific patterns.
    """
    synthesizer = CTGANSynthesizer(
        metadata,
        epochs=epochs,
        batch_size=batch_size,
        verbose=True
    )
    synthesizer.fit(df)
    return synthesizer


def train_tvae(
    df: pd.DataFrame,
    metadata: SingleTableMetadata,
    epochs: int = 300
) -> TVAESynthesizer:
    """
    Train a TVAE model for synthetic data generation.
    Best for: Datasets where CTGAN struggles, faster training than CTGAN.
    """
    synthesizer = TVAESynthesizer(
        metadata,
        epochs=epochs
    )
    synthesizer.fit(df)
    return synthesizer


def generate_synthetic_data(
    synthesizer,
    num_rows: int
) -> pd.DataFrame:
    """Generate synthetic data from a trained synthesizer."""
    return synthesizer.sample(num_rows=num_rows)


def evaluate_synthetic_quality(
    real_data: pd.DataFrame,
    synthetic_data: pd.DataFrame,
    metadata: SingleTableMetadata
) -> dict:
    """
    Evaluate the quality of synthetic data against real data.

    Returns diagnostic and quality scores.
    """
    # Run diagnostic checks
    diagnostic = run_diagnostic(
        real_data=real_data,
        synthetic_data=synthetic_data,
        metadata=metadata
    )

    # Run quality evaluation
    quality = evaluate_quality(
        real_data=real_data,
        synthetic_data=synthetic_data,
        metadata=metadata
    )

    return {
        "diagnostic_score": diagnostic.get_score(),
        "quality_score": quality.get_score(),
    }


def measure_privacy_risk(
    real_data: pd.DataFrame,
    synthetic_data: pd.DataFrame,
    metadata: SingleTableMetadata,
    key_fields: list[str]
) -> dict:
    """
    Measure re-identification risk in synthetic data.

    Checks for exact matches and nearest-neighbor distances
    between real and synthetic records.
    """
    # Check for exact record matches
    merged = real_data.merge(synthetic_data, how="inner")
    exact_match_rate = len(merged) / len(real_data)

    # Check key field matches
    if key_fields:
        key_merged = real_data[key_fields].merge(
            synthetic_data[key_fields], how="inner"
        )
        key_match_rate = len(key_merged) / len(real_data)
    else:
        key_match_rate = 0.0

    return {
        "exact_match_rate": exact_match_rate,
        "key_match_rate": key_match_rate,
        "privacy_safe": exact_match_rate < 0.01 and key_match_rate < 0.05,
    }
```

### Model Selection Guide

| Factor | GaussianCopula | CTGAN | TVAE |
|--------|---------------|-------|------|
| Training speed | Fast (minutes) | Slow (hours) | Medium (30-60 min) |
| Small datasets (<1K rows) | Good | Poor | Fair |
| Large datasets (>100K rows) | Good | Good | Good |
| Numerical data | Excellent | Good | Good |
| Categorical data (high cardinality) | Fair | Good | Good |
| Complex correlations | Fair | Good | Good |
| Constraint handling | Good | Fair | Fair |
| Reproducibility | Excellent | Fair (seed-dependent) | Fair |

## Data Clean Room Architecture

### Components

```
Organization A                    Clean Room                    Organization B
+-------------+    encrypted    +------------------+    encrypted    +-------------+
| Source Data  |  ----------->  | Ingestion Layer  |  <-----------  | Source Data  |
+-------------+                 +------------------+                 +-------------+
                                        |
                                        v
                                +------------------+
                                | Data Preparation |
                                | - Schema mapping |
                                | - Normalization  |
                                | - Deduplication  |
                                +------------------+
                                        |
                                        v
                                +------------------+
                                | Approved Queries |
                                | - Pre-approved   |
                                |   query templates|
                                | - Aggregate only |
                                | - Min group size |
                                +------------------+
                                        |
                                        v
                                +------------------+
                                | Output Validation|
                                | - k-anonymity    |
                                | - DP noise       |
                                | - Disclosure risk|
                                +------------------+
                                        |
                            +-----------+-----------+
                            |                       |
                            v                       v
                    Results for Org A        Results for Org B
```

### Clean Room Policy Engine

```python
"""
Policy engine for data clean room query validation.
Enforces privacy rules on all queries before execution.
"""

from dataclasses import dataclass


@dataclass
class CleanRoomPolicy:
    min_group_size: int = 50
    allowed_operations: list[str] = None
    blocked_columns: list[str] = None
    max_output_rows: int = 1000
    require_aggregation: bool = True
    dp_epsilon: float = 1.0

    def __post_init__(self):
        if self.allowed_operations is None:
            self.allowed_operations = ["COUNT", "SUM", "AVG", "MEDIAN", "PERCENTILE"]
        if self.blocked_columns is None:
            self.blocked_columns = ["ssn", "email", "phone", "full_name", "address"]


class QueryValidator:
    """Validate clean room queries against privacy policies."""

    def __init__(self, policy: CleanRoomPolicy):
        self.policy = policy

    def validate(self, query_ast: dict) -> tuple[bool, list[str]]:
        """
        Validate a parsed query against the policy.

        Returns (is_valid, list_of_violations).
        """
        violations = []

        # Check for blocked columns
        referenced_columns = query_ast.get("columns", [])
        for col in referenced_columns:
            if col.lower() in self.policy.blocked_columns:
                violations.append(f"Column '{col}' is blocked by policy")

        # Check aggregation requirement
        if self.policy.require_aggregation:
            if not query_ast.get("has_aggregation", False):
                violations.append("Query must include aggregation (no raw record output)")

        # Check operations
        operations = query_ast.get("operations", [])
        for op in operations:
            if op.upper() not in self.policy.allowed_operations:
                violations.append(f"Operation '{op}' is not in allowed operations list")

        # Check output size
        if query_ast.get("limit", float("inf")) > self.policy.max_output_rows:
            violations.append(
                f"Output exceeds max rows ({self.policy.max_output_rows})"
            )

        return (len(violations) == 0, violations)
```

## Secure Enclave Integration

### Intel SGX / Azure Confidential Computing

```
Data Owner A           Confidential Computing          Data Owner B
                       +----------------------+
Data (encrypted) ----> | Enclave Environment  | <---- Data (encrypted)
                       | - Decryption in TEE  |
                       | - Join/Analysis      |
                       | - Re-encrypt results |
                       +----------------------+
                               |
                       Encrypted Results
                       (only to authorized parties)
```

### Key Properties
- **Confidentiality**: Data is encrypted outside the enclave; only decrypted within the TEE
- **Integrity**: Enclave code is measured and attested; tampering is detectable
- **Attestation**: Remote parties can verify the enclave is running approved code
- **Isolation**: Even the cloud provider cannot access data inside the enclave

## Utility Measurement Framework

### Statistical Utility Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| Column Shapes | Distribution similarity per column (KS test) | > 0.85 |
| Column Pair Trends | Correlation preservation between column pairs | > 0.80 |
| Boundary Adherence | Values within real data min/max ranges | > 0.95 |
| Category Coverage | All categories in real data appear in synthetic | > 0.90 |
| Range Coverage | Numeric ranges adequately represented | > 0.85 |

### Privacy Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| Exact Match Rate | % of synthetic records identical to real records | < 1% |
| Nearest Neighbor Distance | Minimum distance from synthetic to nearest real record | > threshold |
| Membership Inference AUC | Ability of attack model to determine membership | < 0.55 |
| Attribute Inference Accuracy | Ability to infer sensitive attributes | < random + 5% |
| k-Anonymity of output | Minimum equivalence class size | k >= 5 |

## References

- Patki, N., Wedge, R., and Veeramachaneni, K. "The Synthetic Data Vault." IEEE DSAA, 2016.
- SDV Documentation: docs.sdv.dev
- Xu, L. et al. "Modeling Tabular Data Using Conditional GAN." NeurIPS, 2019.
- Google BigQuery Clean Rooms Documentation
- AWS Clean Rooms Service Documentation
- Microsoft Azure Confidential Computing Documentation
- Stadler, T. et al. "Synthetic Data — Anonymisation Groundhog Day." USENIX Security, 2022.
