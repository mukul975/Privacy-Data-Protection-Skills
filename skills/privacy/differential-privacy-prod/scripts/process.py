"""
Differential Privacy Production Implementation

Core mechanisms (Laplace, Gaussian, Exponential, Randomized Response),
privacy budget management, and utility measurement.
"""

import math
import numpy as np
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional
import json


@dataclass
class BudgetAllocation:
    query_id: str
    epsilon_spent: float
    delta_spent: float
    timestamp: str
    description: str
    analyst: str


class LaplaceMechanism:
    """Pure epsilon-differential privacy via Laplace noise."""

    @staticmethod
    def add_noise(true_value: float, sensitivity: float, epsilon: float) -> float:
        scale = sensitivity / epsilon
        noise = np.random.laplace(loc=0, scale=scale)
        return true_value + noise

    @staticmethod
    def add_noise_vector(values: np.ndarray, sensitivity: float, epsilon: float) -> np.ndarray:
        scale = sensitivity / epsilon
        noise = np.random.laplace(loc=0, scale=scale, size=values.shape)
        return values + noise

    @staticmethod
    def required_epsilon(sensitivity: float, target_error: float, confidence: float = 0.95) -> float:
        """Calculate epsilon needed to achieve target error at given confidence."""
        return sensitivity * math.log(1 / (1 - confidence)) / target_error


class GaussianMechanism:
    """(epsilon, delta)-differential privacy via Gaussian noise."""

    @staticmethod
    def add_noise(true_value: float, sensitivity: float, epsilon: float, delta: float) -> float:
        sigma = sensitivity * math.sqrt(2 * math.log(1.25 / delta)) / epsilon
        noise = np.random.normal(loc=0, scale=sigma)
        return true_value + noise

    @staticmethod
    def calibrate_sigma(sensitivity: float, epsilon: float, delta: float) -> float:
        return sensitivity * math.sqrt(2 * math.log(1.25 / delta)) / epsilon


class ExponentialMechanism:
    """Epsilon-differential privacy for categorical outputs."""

    @staticmethod
    def select(candidates: list, utility_scores: np.ndarray, sensitivity: float, epsilon: float):
        probabilities = np.exp(epsilon * utility_scores / (2 * sensitivity))
        probabilities = probabilities / probabilities.sum()
        index = np.random.choice(len(candidates), p=probabilities)
        return candidates[index]


class RandomizedResponse:
    """Local differential privacy via randomized response."""

    @staticmethod
    def respond(true_bit: bool, epsilon: float) -> bool:
        p = math.exp(epsilon) / (math.exp(epsilon) + 1)
        if np.random.random() < p:
            return true_bit
        return not true_bit

    @staticmethod
    def estimate_proportion(responses: list[bool], epsilon: float) -> float:
        n = len(responses)
        if n == 0:
            return 0.0
        observed = sum(responses) / n
        p = math.exp(epsilon) / (math.exp(epsilon) + 1)
        estimated = (observed - (1 - p)) / (2 * p - 1)
        return max(0.0, min(1.0, estimated))


class PrivacyBudgetManager:
    """Track and enforce differential privacy budget."""

    def __init__(self, total_epsilon: float, total_delta: float, composition: str = "advanced"):
        self.total_epsilon = total_epsilon
        self.total_delta = total_delta
        self.composition = composition
        self.allocations: list[BudgetAllocation] = []

    def remaining_budget(self) -> tuple[float, float]:
        if self.composition == "basic":
            eps = self.total_epsilon - sum(a.epsilon_spent for a in self.allocations)
            delta = self.total_delta - sum(a.delta_spent for a in self.allocations)
            return (max(0, eps), max(0, delta))

        elif self.composition == "advanced":
            k = len(self.allocations)
            if k == 0:
                return (self.total_epsilon, self.total_delta)

            epsilons = [a.epsilon_spent for a in self.allocations]
            deltas = [a.delta_spent for a in self.allocations]
            max_eps = max(epsilons)
            sum_delta = sum(deltas)

            delta_prime = max(1e-10, (self.total_delta - sum_delta) / 2)
            composed_eps = (
                math.sqrt(2 * k * math.log(1 / delta_prime)) * max_eps
                + k * max_eps * (math.exp(max_eps) - 1)
            )
            return (
                max(0, self.total_epsilon - composed_eps),
                max(0, self.total_delta - sum_delta - delta_prime),
            )

        else:
            eps = self.total_epsilon - sum(a.epsilon_spent for a in self.allocations)
            delta = self.total_delta - sum(a.delta_spent for a in self.allocations)
            return (max(0, eps), max(0, delta))

    def request_budget(
        self, query_id: str, epsilon: float, delta: float, description: str, analyst: str
    ) -> bool:
        remaining_eps, remaining_delta = self.remaining_budget()
        if epsilon > remaining_eps or delta > remaining_delta:
            return False

        self.allocations.append(BudgetAllocation(
            query_id=query_id,
            epsilon_spent=epsilon,
            delta_spent=delta,
            timestamp=datetime.now(timezone.utc).isoformat(),
            description=description,
            analyst=analyst,
        ))
        return True

    def usage_report(self) -> dict:
        remaining_eps, remaining_delta = self.remaining_budget()
        return {
            "total_epsilon": self.total_epsilon,
            "total_delta": self.total_delta,
            "remaining_epsilon": round(remaining_eps, 6),
            "remaining_delta": remaining_delta,
            "utilization_pct": round((1 - remaining_eps / self.total_epsilon) * 100, 1),
            "num_queries": len(self.allocations),
            "composition_method": self.composition,
        }


class UtilityMeasurer:
    """Measure utility loss from differential privacy mechanisms."""

    @staticmethod
    def mean_absolute_error(true_values: np.ndarray, noisy_values: np.ndarray) -> float:
        return float(np.mean(np.abs(true_values - noisy_values)))

    @staticmethod
    def relative_error(true_value: float, noisy_value: float) -> float:
        if abs(true_value) < 1e-10:
            return float("inf") if abs(noisy_value) > 1e-10 else 0.0
        return abs(noisy_value - true_value) / abs(true_value)

    @staticmethod
    def utility_report(true_values: np.ndarray, noisy_values: np.ndarray) -> dict:
        errors = np.abs(true_values - noisy_values)
        relative_errors = np.where(
            np.abs(true_values) > 1e-10,
            errors / np.abs(true_values),
            0,
        )
        return {
            "mean_absolute_error": float(np.mean(errors)),
            "median_absolute_error": float(np.median(errors)),
            "max_absolute_error": float(np.max(errors)),
            "mean_relative_error": float(np.mean(relative_errors)),
            "within_10pct": float(np.mean(relative_errors < 0.10)),
            "within_25pct": float(np.mean(relative_errors < 0.25)),
        }


if __name__ == "__main__":
    np.random.seed(42)

    # Laplace mechanism example
    true_count = 1500
    noisy_count = LaplaceMechanism.add_noise(true_count, sensitivity=1.0, epsilon=1.0)
    print(f"True count: {true_count}, Noisy count: {noisy_count:.1f}")

    # Budget management example
    budget = PrivacyBudgetManager(total_epsilon=5.0, total_delta=1e-5, composition="advanced")
    budget.request_budget("q1", 0.5, 1e-6, "Monthly user count", "analyst-1")
    budget.request_budget("q2", 1.0, 1e-6, "Revenue by region", "analyst-1")
    budget.request_budget("q3", 0.5, 1e-6, "Feature adoption rate", "analyst-2")

    report = budget.usage_report()
    print(f"\nBudget utilization: {report['utilization_pct']}%")
    print(f"Remaining epsilon: {report['remaining_epsilon']}")

    # Utility measurement
    true_vals = np.array([100, 250, 500, 750, 1000])
    noisy_vals = np.array([LaplaceMechanism.add_noise(v, 1.0, 1.0) for v in true_vals])
    utility = UtilityMeasurer.utility_report(true_vals, noisy_vals)
    print(f"\nUtility: MAE={utility['mean_absolute_error']:.2f}, Within 10%: {utility['within_10pct']*100:.0f}%")
