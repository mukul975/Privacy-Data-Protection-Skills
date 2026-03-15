---
name: differential-privacy-prod
description: >-
  Deploy differential privacy in production systems including epsilon selection
  strategies, noise calibration with Laplace and Gaussian mechanisms, privacy
  budget tracking, composition theorems, and Python implementation patterns.
  Covers both central and local differential privacy models.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-engineering
  tags: "differential-privacy, epsilon-delta, noise-calibration, privacy-budget, composition-theorems"
---

# Differential Privacy in Production

## Overview

Differential privacy is a mathematical framework for quantifying and bounding the privacy loss incurred when publishing statistical information about a dataset. It provides a provable guarantee that the output of a computation does not significantly depend on whether any single individual's data is included. This skill covers the practical engineering of differential privacy systems for production deployment.

## Core Definitions

### (epsilon, delta)-Differential Privacy

A randomized mechanism M satisfies (epsilon, delta)-differential privacy if for all neighboring datasets D and D' (differing in at most one record) and for all possible outputs S:

```
P[M(D) in S] <= e^epsilon * P[M(D') in S] + delta
```

Where:
- **epsilon (privacy loss budget)**: Quantifies the maximum information leakage. Lower epsilon = stronger privacy.
- **delta**: Probability of an additional privacy breach beyond the epsilon guarantee. Should be cryptographically small (< 1/n^2 where n is the dataset size).

### Sensitivity

The sensitivity of a function f measures how much one individual can affect the output:

- **Global sensitivity**: max over all neighboring D,D' of |f(D) - f(D')|
- **Local sensitivity**: for a specific D, max over all neighboring D' of |f(D) - f(D')|

## Epsilon Selection Strategy

### Epsilon Guidelines by Use Case

| Use Case | Epsilon Range | Rationale |
|----------|--------------|-----------|
| Census/government statistics | 0.1 - 1.0 | Maximum protection for mandatory participation |
| Healthcare analytics | 0.5 - 2.0 | High sensitivity, regulatory requirements |
| Location analytics | 1.0 - 3.0 | Moderate sensitivity, aggregate insights |
| Product analytics | 1.0 - 5.0 | Lower sensitivity, business utility needs |
| A/B testing | 2.0 - 8.0 | Statistical significance requirements |
| Aggregate reporting | 0.5 - 3.0 | Public-facing outputs need stronger guarantees |

### Factors Influencing Epsilon Choice

1. **Data sensitivity**: More sensitive data requires lower epsilon
2. **Dataset size**: Larger datasets tolerate lower epsilon with acceptable utility
3. **Query frequency**: More queries consume more budget (see composition)
4. **Regulatory requirements**: Some regulations imply specific privacy levels
5. **Utility requirements**: Business needs may set a floor on acceptable accuracy
6. **Audience**: Public release needs stronger guarantees than internal analytics

## Noise Mechanisms

### Laplace Mechanism

For numeric queries with bounded global sensitivity. Provides pure epsilon-differential privacy.

```python
import numpy as np

def laplace_mechanism(true_value: float, sensitivity: float, epsilon: float) -> float:
    """
    Apply Laplace noise for epsilon-differential privacy.

    Args:
        true_value: The true query result
        sensitivity: Global sensitivity of the query (L1)
        epsilon: Privacy parameter

    Returns:
        Noisy result satisfying epsilon-differential privacy
    """
    scale = sensitivity / epsilon
    noise = np.random.laplace(loc=0, scale=scale)
    return true_value + noise


def laplace_mechanism_vector(true_values: np.ndarray, sensitivity: float, epsilon: float) -> np.ndarray:
    """Apply Laplace noise to a vector of values."""
    scale = sensitivity / epsilon
    noise = np.random.laplace(loc=0, scale=scale, size=true_values.shape)
    return true_values + noise
```

### Gaussian Mechanism

For numeric queries. Provides (epsilon, delta)-differential privacy with tighter noise for high-dimensional outputs.

```python
import numpy as np
import math

def gaussian_mechanism(true_value: float, sensitivity: float, epsilon: float, delta: float) -> float:
    """
    Apply Gaussian noise for (epsilon, delta)-differential privacy.

    Uses the analytic Gaussian mechanism calibration.

    Args:
        true_value: The true query result
        sensitivity: Global sensitivity of the query (L2)
        epsilon: Privacy parameter
        delta: Failure probability parameter

    Returns:
        Noisy result satisfying (epsilon, delta)-differential privacy
    """
    sigma = sensitivity * math.sqrt(2 * math.log(1.25 / delta)) / epsilon
    noise = np.random.normal(loc=0, scale=sigma)
    return true_value + noise
```

### Exponential Mechanism

For non-numeric outputs (categorical selection) where adding noise directly is not meaningful.

```python
import numpy as np

def exponential_mechanism(
    candidates: list,
    utility_scores: np.ndarray,
    sensitivity: float,
    epsilon: float
) -> object:
    """
    Select an output using the exponential mechanism.

    Args:
        candidates: List of possible outputs
        utility_scores: Utility score for each candidate
        sensitivity: Global sensitivity of the utility function
        epsilon: Privacy parameter

    Returns:
        Selected candidate satisfying epsilon-differential privacy
    """
    # Calculate selection probabilities
    probabilities = np.exp(epsilon * utility_scores / (2 * sensitivity))
    probabilities = probabilities / probabilities.sum()

    # Sample according to probabilities
    index = np.random.choice(len(candidates), p=probabilities)
    return candidates[index]
```

### Randomized Response (Local DP)

For collecting individual data points with local differential privacy.

```python
import random
import math

def randomized_response(true_bit: bool, epsilon: float) -> bool:
    """
    Apply randomized response for local differential privacy.

    Args:
        true_bit: The individual's true binary response
        epsilon: Privacy parameter

    Returns:
        Randomized response satisfying epsilon-local-DP
    """
    p = math.exp(epsilon) / (math.exp(epsilon) + 1)

    if random.random() < p:
        return true_bit  # Report truthfully
    else:
        return not true_bit  # Flip the answer


def estimate_from_randomized_responses(
    responses: list,
    epsilon: float
) -> float:
    """
    Estimate true proportion from randomized responses.

    Args:
        responses: List of randomized boolean responses
        epsilon: The epsilon used during collection

    Returns:
        Estimated true proportion
    """
    n = len(responses)
    observed_proportion = sum(responses) / n
    p = math.exp(epsilon) / (math.exp(epsilon) + 1)

    # Correct for randomization bias
    estimated_proportion = (observed_proportion - (1 - p)) / (2 * p - 1)
    return max(0.0, min(1.0, estimated_proportion))
```

## Privacy Budget Tracking

### Budget Manager Implementation

```python
import threading
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import math


@dataclass
class BudgetAllocation:
    query_id: str
    epsilon_spent: float
    delta_spent: float
    timestamp: datetime
    query_description: str
    analyst_id: str


class PrivacyBudgetManager:
    """
    Track and enforce differential privacy budget across queries.

    Supports both basic and advanced composition theorems.
    """

    def __init__(
        self,
        total_epsilon: float,
        total_delta: float,
        composition_method: str = "advanced"
    ):
        self.total_epsilon = total_epsilon
        self.total_delta = total_delta
        self.composition_method = composition_method
        self.allocations: list[BudgetAllocation] = []
        self._lock = threading.Lock()

    def remaining_budget(self) -> tuple[float, float]:
        """Calculate remaining (epsilon, delta) budget."""
        if self.composition_method == "basic":
            return self._basic_composition_remaining()
        elif self.composition_method == "advanced":
            return self._advanced_composition_remaining()
        elif self.composition_method == "rdp":
            return self._rdp_composition_remaining()
        else:
            raise ValueError(f"Unknown composition method: {self.composition_method}")

    def _basic_composition_remaining(self) -> tuple[float, float]:
        """Basic sequential composition: epsilons and deltas sum."""
        spent_epsilon = sum(a.epsilon_spent for a in self.allocations)
        spent_delta = sum(a.delta_spent for a in self.allocations)
        return (self.total_epsilon - spent_epsilon, self.total_delta - spent_delta)

    def _advanced_composition_remaining(self) -> tuple[float, float]:
        """
        Advanced composition theorem:
        k queries each with epsilon_i satisfy
        (sqrt(2k * ln(1/delta')) * max(epsilon_i) + k * epsilon_i * (e^epsilon_i - 1),
         k * delta_i + delta')-DP
        """
        k = len(self.allocations)
        if k == 0:
            return (self.total_epsilon, self.total_delta)

        epsilons = [a.epsilon_spent for a in self.allocations]
        deltas = [a.delta_spent for a in self.allocations]

        max_eps = max(epsilons)
        sum_delta = sum(deltas)

        # Reserve delta' for composition overhead
        delta_prime = (self.total_delta - sum_delta) / 2
        if delta_prime <= 0:
            return (0.0, 0.0)

        composed_epsilon = (
            math.sqrt(2 * k * math.log(1 / delta_prime)) * max_eps
            + k * max_eps * (math.exp(max_eps) - 1)
        )
        composed_delta = sum_delta + delta_prime

        return (
            max(0.0, self.total_epsilon - composed_epsilon),
            max(0.0, self.total_delta - composed_delta)
        )

    def _rdp_composition_remaining(self) -> tuple[float, float]:
        """Renyi DP composition (simplified)."""
        # RDP provides tighter bounds through Renyi divergence
        spent_epsilon = sum(a.epsilon_spent for a in self.allocations)
        spent_delta = sum(a.delta_spent for a in self.allocations)
        return (self.total_epsilon - spent_epsilon, self.total_delta - spent_delta)

    def request_budget(
        self,
        query_id: str,
        epsilon_requested: float,
        delta_requested: float,
        query_description: str,
        analyst_id: str
    ) -> bool:
        """
        Request budget allocation for a query.

        Returns True if budget is available and allocated, False otherwise.
        """
        with self._lock:
            remaining_eps, remaining_delta = self.remaining_budget()

            if epsilon_requested > remaining_eps or delta_requested > remaining_delta:
                return False

            allocation = BudgetAllocation(
                query_id=query_id,
                epsilon_spent=epsilon_requested,
                delta_spent=delta_requested,
                timestamp=datetime.utcnow(),
                query_description=query_description,
                analyst_id=analyst_id
            )
            self.allocations.append(allocation)
            return True

    def get_usage_report(self) -> dict:
        """Generate budget usage report."""
        remaining_eps, remaining_delta = self.remaining_budget()
        return {
            "total_epsilon": self.total_epsilon,
            "total_delta": self.total_delta,
            "remaining_epsilon": remaining_eps,
            "remaining_delta": remaining_delta,
            "utilization_pct": (1 - remaining_eps / self.total_epsilon) * 100,
            "num_queries": len(self.allocations),
            "composition_method": self.composition_method,
            "allocations": [
                {
                    "query_id": a.query_id,
                    "epsilon": a.epsilon_spent,
                    "delta": a.delta_spent,
                    "timestamp": a.timestamp.isoformat(),
                    "analyst": a.analyst_id,
                }
                for a in self.allocations
            ],
        }
```

## Composition Theorems

### Basic Composition

If M1 satisfies (e1, d1)-DP and M2 satisfies (e2, d2)-DP, then releasing both M1(D) and M2(D) satisfies (e1 + e2, d1 + d2)-DP.

### Advanced Composition

For k mechanisms each satisfying (epsilon, delta)-DP, the composed mechanism satisfies (epsilon', k*delta + delta')-DP where:

```
epsilon' = sqrt(2k * ln(1/delta')) * epsilon + k * epsilon * (e^epsilon - 1)
```

### Renyi Differential Privacy (RDP) Composition

RDP provides tighter composition bounds by tracking privacy loss through Renyi divergence of order alpha. Convert to (epsilon, delta)-DP at the end:

```
For alpha > 1: epsilon(delta) = RDP_alpha - ln(delta) / (alpha - 1)
```

### Moments Accountant

Used by TensorFlow Privacy and Opacus. Tracks the log of the moment-generating function of the privacy loss variable. Provides the tightest known bounds for iterative mechanisms (e.g., DP-SGD).

## Production Deployment Patterns

### Pattern 1: Central DP Analytics Pipeline

```
Raw Data Store --> Sensitivity Calibration --> DP Mechanism --> Result Cache
                         |                         |
                         v                         v
                  Budget Manager <------------- Audit Log
```

### Pattern 2: Local DP Collection

```
Client Device --> Local Randomizer --> Aggregation Server --> Estimator
                  (epsilon-LDP)              |                    |
                                             v                    v
                                       Budget Tracker      Utility Monitor
```

### Pattern 3: DP Model Training (DP-SGD)

```
Training Data --> Mini-batch Sampling --> Per-example Gradient
                  (Poisson sampling)            |
                                                v
                                        Gradient Clipping (norm bound C)
                                                |
                                                v
                                        Gaussian Noise Addition (sigma * C)
                                                |
                                                v
                                        Model Update --> Privacy Accountant
```

## Utility Measurement

| Metric | Description | Formula |
|--------|-------------|---------|
| Mean Absolute Error | Average absolute difference from true value | MAE = (1/n) * sum(|noisy_i - true_i|) |
| Relative Error | Error as fraction of true value | RE = |noisy - true| / |true| |
| Coverage | Fraction of true values within confidence interval | Count(true in CI) / n |
| Utility Ratio | Ratio of noisy to true signal-to-noise ratio | SNR_noisy / SNR_true |

## References

- Dwork, C. and Roth, A. "The Algorithmic Foundations of Differential Privacy." Foundations and Trends in Theoretical Computer Science, 9(3-4):211-407, 2014.
- Mironov, I. "Renyi Differential Privacy." IEEE CSF, 2017.
- Abadi, M. et al. "Deep Learning with Differential Privacy." ACM CCS, 2016.
- Google Differential Privacy Library: github.com/google/differential-privacy
- OpenDP Project: opendp.org
- Apple Differential Privacy Technical Overview (2017)
- U.S. Census Bureau Disclosure Avoidance System (2020 Census)
