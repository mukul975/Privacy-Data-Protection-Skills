#!/usr/bin/env python3
"""
Privacy-Preserving Analytics Engine

Implements differential privacy mechanisms (Laplace, Gaussian),
k-anonymity verification, and privacy budget tracking for
GDPR-compliant statistical analysis.
"""

import math
import random
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional


# ---------------------------------------------------------------------------
# Differential Privacy Mechanisms
# ---------------------------------------------------------------------------

class LaplaceMechanism:
    """
    Laplace mechanism for pure epsilon-differential privacy.

    Adds Laplace noise calibrated to sensitivity/epsilon. Suitable for
    counting queries and sum queries with bounded sensitivity.
    """

    @staticmethod
    def add_noise(true_value: float, sensitivity: float, epsilon: float) -> float:
        """
        Add Laplace noise to a query result.

        Args:
            true_value: The true query result.
            sensitivity: Global sensitivity (max change from one record).
            epsilon: Privacy parameter (smaller = more private).

        Returns:
            Noised result satisfying epsilon-differential privacy.
        """
        scale = sensitivity / epsilon
        # Generate Laplace noise using inverse CDF method
        u = random.random() - 0.5
        noise = -scale * math.copysign(1, u) * math.log(1 - 2 * abs(u))
        return true_value + noise

    @staticmethod
    def required_epsilon(sensitivity: float, accuracy: float, confidence: float) -> float:
        """
        Calculate the epsilon needed to achieve a target accuracy with given confidence.

        Args:
            sensitivity: Global sensitivity of the query.
            accuracy: Maximum acceptable error.
            confidence: Probability of error being within accuracy (e.g., 0.95).

        Returns:
            Required epsilon value.
        """
        return sensitivity * math.log(1.0 / (1.0 - confidence)) / accuracy


class GaussianMechanism:
    """
    Gaussian mechanism for (epsilon, delta)-differential privacy.

    Adds Gaussian noise; suitable for queries where approximate DP is
    acceptable and tighter composition bounds are needed.
    """

    @staticmethod
    def add_noise(true_value: float, sensitivity: float, epsilon: float,
                  delta: float = 1e-5) -> float:
        """
        Add Gaussian noise to a query result.

        Args:
            true_value: The true query result.
            sensitivity: L2 sensitivity of the query function.
            epsilon: Privacy parameter.
            delta: Probability of privacy breach (typically 1/n^2).

        Returns:
            Noised result satisfying (epsilon, delta)-differential privacy.
        """
        sigma = sensitivity * math.sqrt(2 * math.log(1.25 / delta)) / epsilon
        noise = random.gauss(0, sigma)
        return true_value + noise


class ExponentialMechanism:
    """
    Exponential mechanism for differentially private selection queries.

    Selects an output from a discrete set of candidates with probability
    proportional to exp(epsilon * utility / (2 * sensitivity)).
    """

    @staticmethod
    def select(candidates: list, utility_scores: list[float],
               sensitivity: float, epsilon: float) -> object:
        """
        Select a candidate with probability proportional to its utility score.

        Args:
            candidates: List of candidate outputs.
            utility_scores: Utility score for each candidate.
            sensitivity: Maximum change in utility from one record.
            epsilon: Privacy parameter.

        Returns:
            Selected candidate satisfying epsilon-differential privacy.
        """
        weights = []
        for score in utility_scores:
            weight = math.exp(epsilon * score / (2.0 * sensitivity))
            weights.append(weight)

        total = sum(weights)
        probabilities = [w / total for w in weights]

        r = random.random()
        cumulative = 0.0
        for i, p in enumerate(probabilities):
            cumulative += p
            if r <= cumulative:
                return candidates[i]

        return candidates[-1]


# ---------------------------------------------------------------------------
# Privacy Budget Tracker
# ---------------------------------------------------------------------------

@dataclass
class BudgetAllocation:
    """Budget allocation for a specific analytics function."""
    function_name: str
    epsilon_allocated: float
    epsilon_consumed: float = 0.0
    query_count: int = 0
    refresh_cadence: str = "monthly"

    @property
    def epsilon_remaining(self) -> float:
        return max(0.0, self.epsilon_allocated - self.epsilon_consumed)

    @property
    def utilization_percent(self) -> float:
        if self.epsilon_allocated == 0:
            return 0.0
        return (self.epsilon_consumed / self.epsilon_allocated) * 100.0


class PrivacyBudgetTracker:
    """
    Centralized privacy budget ledger for differential privacy accounting.

    Tracks epsilon consumption across analytics functions with
    configurable exhaustion thresholds and alert callbacks.
    """

    def __init__(self, annual_budget: float = 8.0, organization: str = "Prism Data Systems AG"):
        self.annual_budget = annual_budget
        self.organization = organization
        self.allocations: dict[str, BudgetAllocation] = {}
        self.audit_log: list[dict] = []
        self.alert_thresholds = [0.80, 0.95, 1.00]

    def register_function(self, name: str, epsilon: float, cadence: str = "monthly") -> None:
        self.allocations[name] = BudgetAllocation(
            function_name=name,
            epsilon_allocated=epsilon,
            refresh_cadence=cadence,
        )

    def consume(self, function_name: str, epsilon: float, analyst: str,
                query_description: str) -> dict:
        """
        Record epsilon consumption for a query.

        Returns:
            Result dict with status, remaining budget, and any alerts.
        """
        alloc = self.allocations.get(function_name)
        if alloc is None:
            return {"status": "error", "message": f"Unknown function: {function_name}"}

        if epsilon > alloc.epsilon_remaining:
            return {
                "status": "blocked",
                "message": f"Budget exhausted for {function_name}. "
                           f"Remaining: {alloc.epsilon_remaining:.4f}, Requested: {epsilon:.4f}",
            }

        alloc.epsilon_consumed += epsilon
        alloc.query_count += 1

        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "function": function_name,
            "analyst": analyst,
            "query": query_description,
            "epsilon_consumed": epsilon,
            "epsilon_remaining": alloc.epsilon_remaining,
            "cumulative_consumed": alloc.epsilon_consumed,
        }
        self.audit_log.append(log_entry)

        alerts = []
        utilization = alloc.utilization_percent / 100.0
        for threshold in self.alert_thresholds:
            if utilization >= threshold and (utilization - epsilon / alloc.epsilon_allocated) < threshold:
                alerts.append(f"ALERT: {function_name} reached {threshold*100:.0f}% budget utilization")

        return {
            "status": "success",
            "epsilon_consumed": epsilon,
            "epsilon_remaining": alloc.epsilon_remaining,
            "utilization_percent": alloc.utilization_percent,
            "alerts": alerts,
        }

    def get_report(self) -> dict:
        total_consumed = sum(a.epsilon_consumed for a in self.allocations.values())
        total_allocated = sum(a.epsilon_allocated for a in self.allocations.values())

        return {
            "organization": self.organization,
            "report_date": datetime.now(timezone.utc).isoformat(),
            "annual_budget": self.annual_budget,
            "total_allocated": total_allocated,
            "total_consumed": total_consumed,
            "overall_utilization_percent": (total_consumed / self.annual_budget * 100) if self.annual_budget > 0 else 0,
            "functions": {
                name: {
                    "allocated": a.epsilon_allocated,
                    "consumed": a.epsilon_consumed,
                    "remaining": a.epsilon_remaining,
                    "utilization_percent": a.utilization_percent,
                    "query_count": a.query_count,
                }
                for name, a in self.allocations.items()
            },
        }


# ---------------------------------------------------------------------------
# k-Anonymity Verification
# ---------------------------------------------------------------------------

def verify_k_anonymity(dataset: list[dict], quasi_identifiers: list[str], k: int) -> dict:
    """
    Verify whether a dataset satisfies k-anonymity for given quasi-identifiers.

    Args:
        dataset: List of records (dicts).
        quasi_identifiers: List of field names that are quasi-identifiers.
        k: Minimum anonymity set size.

    Returns:
        Dictionary with verification results.
    """
    equivalence_classes: dict[tuple, int] = Counter()
    for record in dataset:
        qi_values = tuple(record.get(qi, None) for qi in quasi_identifiers)
        equivalence_classes[qi_values] += 1

    violations = {qi: count for qi, count in equivalence_classes.items() if count < k}
    min_class_size = min(equivalence_classes.values()) if equivalence_classes else 0
    max_class_size = max(equivalence_classes.values()) if equivalence_classes else 0

    records_in_violation = sum(violations.values())

    return {
        "k_target": k,
        "total_records": len(dataset),
        "equivalence_classes": len(equivalence_classes),
        "min_class_size": min_class_size,
        "max_class_size": max_class_size,
        "satisfies_k_anonymity": len(violations) == 0,
        "violating_classes": len(violations),
        "records_in_violation": records_in_violation,
        "suppression_needed": records_in_violation,
    }


def generalize_age(age: int, level: int) -> str:
    """Apply generalization hierarchy to an age value."""
    if level == 0:
        return str(age)
    elif level == 1:
        lower = (age // 5) * 5
        return f"{lower}-{lower+4}"
    elif level == 2:
        lower = (age // 10) * 10
        return f"{lower}-{lower+9}"
    elif level == 3:
        lower = (age // 20) * 20
        return f"{lower}-{lower+19}"
    else:
        return "*"


def generalize_postal_code(code: str, level: int) -> str:
    """Apply generalization hierarchy to a Swiss postal code."""
    if level == 0:
        return code
    elif level == 1:
        return code[:3] + "*"
    elif level == 2:
        return code[:2] + "**"
    elif level == 3:
        return code[:1] + "***"
    else:
        return "****"


# ---------------------------------------------------------------------------
# Example Usage
# ---------------------------------------------------------------------------

def run_example():
    """Demonstrate privacy-preserving analytics for Prism Data Systems AG."""

    print("=== Differential Privacy: Laplace Mechanism ===")
    true_count = 15234  # True number of active users
    sensitivity = 1.0   # One person changes count by at most 1

    for epsilon in [0.1, 0.5, 1.0, 5.0]:
        noised_results = [
            LaplaceMechanism.add_noise(true_count, sensitivity, epsilon)
            for _ in range(5)
        ]
        avg_error = sum(abs(r - true_count) for r in noised_results) / len(noised_results)
        print(f"  ε={epsilon:.1f}: True={true_count}, "
              f"Noised samples={[round(r) for r in noised_results]}, "
              f"Avg error={avg_error:.1f}")

    print()
    print("=== Differential Privacy: Gaussian Mechanism ===")
    true_mean = 47.3    # True average session duration (minutes)
    l2_sensitivity = 2.0  # Bounded contribution per user

    for epsilon in [0.5, 1.0, 2.0]:
        noised = GaussianMechanism.add_noise(true_mean, l2_sensitivity, epsilon, delta=1e-5)
        print(f"  ε={epsilon:.1f}, δ=1e-5: True={true_mean}, Noised={noised:.2f}")

    print()
    print("=== Exponential Mechanism: Private Feature Selection ===")
    features = ["dark_mode", "two_factor_auth", "api_access", "bulk_export", "sso_login"]
    adoption_rates = [0.72, 0.58, 0.31, 0.15, 0.44]  # True adoption proportions
    selected = ExponentialMechanism.select(features, adoption_rates, sensitivity=0.01, epsilon=1.0)
    print(f"  Most popular feature (private selection): {selected}")

    print()
    print("=== Privacy Budget Tracking ===")
    tracker = PrivacyBudgetTracker(annual_budget=8.0)
    tracker.register_function("daily_active_users", epsilon=1.2, cadence="daily")
    tracker.register_function("revenue_by_region", epsilon=2.0, cadence="quarterly")
    tracker.register_function("feature_usage", epsilon=3.6, cadence="monthly")

    queries = [
        ("daily_active_users", 0.1, "analyst_koch", "DAU count 2026-03-14"),
        ("daily_active_users", 0.1, "analyst_koch", "DAU count 2026-03-15"),
        ("revenue_by_region", 0.5, "analyst_weber", "Q1 2026 revenue by EMEA region"),
        ("feature_usage", 0.3, "analyst_fischer", "March 2026 dark_mode adoption"),
    ]

    for func, eps, analyst, desc in queries:
        result = tracker.consume(func, eps, analyst, desc)
        print(f"  Query: {desc}")
        print(f"    Status: {result['status']}, "
              f"ε consumed: {result.get('epsilon_consumed', 0):.2f}, "
              f"ε remaining: {result.get('epsilon_remaining', 'N/A')}")
        if result.get("alerts"):
            for alert in result["alerts"]:
                print(f"    {alert}")

    print()
    report = tracker.get_report()
    print(f"  Budget Report: {report['total_consumed']:.2f} / {report['annual_budget']:.1f} "
          f"({report['overall_utilization_percent']:.1f}% utilized)")

    print()
    print("=== k-Anonymity Verification ===")
    sample_data = [
        {"age_range": "25-29", "postal_prefix": "80**", "gender": "M", "diagnosis": "flu"},
        {"age_range": "25-29", "postal_prefix": "80**", "gender": "M", "diagnosis": "cold"},
        {"age_range": "25-29", "postal_prefix": "80**", "gender": "M", "diagnosis": "flu"},
        {"age_range": "25-29", "postal_prefix": "80**", "gender": "F", "diagnosis": "allergy"},
        {"age_range": "25-29", "postal_prefix": "80**", "gender": "F", "diagnosis": "flu"},
        {"age_range": "25-29", "postal_prefix": "80**", "gender": "F", "diagnosis": "cold"},
        {"age_range": "30-34", "postal_prefix": "80**", "gender": "M", "diagnosis": "cold"},
        {"age_range": "30-34", "postal_prefix": "80**", "gender": "M", "diagnosis": "flu"},
        {"age_range": "30-34", "postal_prefix": "80**", "gender": "M", "diagnosis": "allergy"},
        {"age_range": "30-34", "postal_prefix": "80**", "gender": "F", "diagnosis": "flu"},
        {"age_range": "30-34", "postal_prefix": "80**", "gender": "F", "diagnosis": "cold"},
        {"age_range": "30-34", "postal_prefix": "80**", "gender": "F", "diagnosis": "allergy"},
    ]

    result = verify_k_anonymity(sample_data, ["age_range", "postal_prefix", "gender"], k=3)
    print(f"  k={result['k_target']}: Satisfies k-anonymity: {result['satisfies_k_anonymity']}")
    print(f"  Equivalence classes: {result['equivalence_classes']}, "
          f"Min class size: {result['min_class_size']}, "
          f"Max class size: {result['max_class_size']}")

    print()
    print("=== Age Generalization Hierarchy ===")
    test_age = 27
    for level in range(5):
        print(f"  Level {level}: {generalize_age(test_age, level)}")


if __name__ == "__main__":
    run_example()
