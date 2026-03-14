#!/usr/bin/env python3
"""
Federated Learning Simulation Engine

Simulates horizontal federated learning with FedAvg and FedProx
aggregation, differential privacy, and secure aggregation concepts.
Demonstrates GDPR-compliant distributed ML without data sharing.
"""

import math
import random
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional


@dataclass
class ModelUpdate:
    """A local model update from a participant."""
    participant_id: str
    weights: list[float]
    sample_count: int
    local_loss: float
    local_epochs: int
    clipped: bool = False
    noised: bool = False
    gradient_norm: float = 0.0


@dataclass
class FLParticipant:
    """A federated learning participant."""
    participant_id: str
    organization: str
    sample_count: int
    data_distribution: str  # "iid" or "non-iid"
    local_data_mean: float = 0.0
    local_data_std: float = 1.0


class FederatedAggregator:
    """
    Central aggregation server for federated learning.
    Implements FedAvg and FedProx aggregation strategies.
    """

    def __init__(self, model_dim: int, strategy: str = "fedavg",
                 proximal_mu: float = 0.0):
        self.model_dim = model_dim
        self.strategy = strategy
        self.proximal_mu = proximal_mu
        self.global_weights = [random.gauss(0, 0.1) for _ in range(model_dim)]
        self.round_number = 0
        self.history: list[dict] = []

    def aggregate(self, updates: list[ModelUpdate]) -> list[float]:
        """
        Aggregate participant updates using FedAvg (weighted average).

        Args:
            updates: List of local model updates from participants.

        Returns:
            New global model weights.
        """
        total_samples = sum(u.sample_count for u in updates)

        new_weights = [0.0] * self.model_dim
        for update in updates:
            weight_factor = update.sample_count / total_samples
            for i in range(self.model_dim):
                new_weights[i] += weight_factor * update.weights[i]

        self.global_weights = new_weights
        self.round_number += 1

        avg_loss = sum(u.local_loss * u.sample_count for u in updates) / total_samples

        self.history.append({
            "round": self.round_number,
            "participants": len(updates),
            "total_samples": total_samples,
            "avg_loss": avg_loss,
            "strategy": self.strategy,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })

        return new_weights


class DPMechanism:
    """Differential privacy mechanism for federated learning gradients."""

    def __init__(self, clipping_norm: float = 1.0, noise_multiplier: float = 1.1,
                 target_epsilon: float = 3.0, target_delta: float = 1e-5):
        self.clipping_norm = clipping_norm
        self.noise_multiplier = noise_multiplier
        self.target_epsilon = target_epsilon
        self.target_delta = target_delta
        self.epsilon_consumed = 0.0
        self.rounds_processed = 0

    def clip_and_noise(self, gradients: list[float]) -> tuple[list[float], bool, float]:
        """
        Apply gradient clipping and Gaussian noise for differential privacy.

        Returns:
            Tuple of (noised_gradients, was_clipped, gradient_norm).
        """
        # Compute gradient norm
        norm = math.sqrt(sum(g * g for g in gradients))
        clipped = False

        # Clip if norm exceeds threshold
        if norm > self.clipping_norm:
            scale = self.clipping_norm / norm
            gradients = [g * scale for g in gradients]
            clipped = True

        # Add Gaussian noise
        sigma = self.noise_multiplier * self.clipping_norm
        noised = [g + random.gauss(0, sigma) for g in gradients]

        # Simple privacy accounting (production should use Renyi DP accountant)
        per_round_epsilon = self.clipping_norm / (sigma * math.sqrt(2 * math.log(1.25 / self.target_delta)))
        self.epsilon_consumed += per_round_epsilon
        self.rounds_processed += 1

        return noised, clipped, norm

    @property
    def budget_remaining(self) -> float:
        return max(0.0, self.target_epsilon - self.epsilon_consumed)

    @property
    def budget_utilization(self) -> float:
        return (self.epsilon_consumed / self.target_epsilon * 100) if self.target_epsilon > 0 else 0


class SecureAggregationSimulator:
    """
    Simulates secure aggregation using pairwise masking.

    In production, this would use cryptographic protocols (Bonawitz et al., 2017)
    to ensure the server only sees the aggregate of participant updates.
    """

    @staticmethod
    def aggregate_with_masks(updates: list[ModelUpdate]) -> list[float]:
        """
        Simulate secure aggregation: each participant adds a random mask,
        masks cancel in the sum, server learns only the aggregate.
        """
        dim = len(updates[0].weights)
        n = len(updates)

        # Generate pairwise masks (in production: cryptographic PRG seeds)
        masked_updates = []
        for i, update in enumerate(updates):
            mask = [0.0] * dim
            for j in range(n):
                if i != j:
                    # Pairwise random values: mask[i,j] = -mask[j,i]
                    seed = min(i, j) * 1000 + max(i, j)
                    rng = random.Random(seed)
                    for d in range(dim):
                        val = rng.gauss(0, 1000)
                        if i < j:
                            mask[d] += val
                        else:
                            mask[d] -= val

            masked = [w + m for w, m in zip(update.weights, mask)]
            masked_updates.append(masked)

        # Server sums masked updates — masks cancel out
        aggregate = [0.0] * dim
        for masked in masked_updates:
            for d in range(dim):
                aggregate[d] += masked[d]

        # Divide by number of participants for average
        return [a / n for a in aggregate]


def simulate_local_training(participant: FLParticipant, global_weights: list[float],
                            local_epochs: int, learning_rate: float,
                            dp: Optional[DPMechanism] = None,
                            proximal_mu: float = 0.0) -> ModelUpdate:
    """Simulate local model training at a participant."""
    dim = len(global_weights)
    weights = list(global_weights)

    # Simulate SGD updates
    total_loss = 0.0
    for epoch in range(local_epochs):
        # Simulate gradient from local data
        gradients = [
            random.gauss(participant.local_data_mean * 0.1, participant.local_data_std * 0.5)
            for _ in range(dim)
        ]

        # FedProx: add proximal term
        if proximal_mu > 0:
            for i in range(dim):
                gradients[i] += proximal_mu * (weights[i] - global_weights[i])

        # Update weights
        for i in range(dim):
            weights[i] -= learning_rate * gradients[i]

        loss = sum(g * g for g in gradients) / dim
        total_loss += loss

    avg_loss = total_loss / local_epochs

    # Compute update (difference from global model)
    update_vector = [w - g for w, g in zip(weights, global_weights)]

    # Apply DP if enabled
    clipped = False
    norm = math.sqrt(sum(u * u for u in update_vector))
    noised = False

    if dp is not None and dp.budget_remaining > 0:
        update_vector, clipped, norm = dp.clip_and_noise(update_vector)
        noised = True

    # Apply update to get final local weights
    final_weights = [g + u for g, u in zip(global_weights, update_vector)]

    return ModelUpdate(
        participant_id=participant.participant_id,
        weights=final_weights,
        sample_count=participant.sample_count,
        local_loss=avg_loss,
        local_epochs=local_epochs,
        clipped=clipped,
        noised=noised,
        gradient_norm=norm,
    )


def run_example():
    """Demonstrate federated learning for Prism Data Systems AG consortium."""

    print("=== Federated Learning Architecture Demo ===")
    print("Scenario: Prism Data Systems AG coordinates FL across three partner hospitals")
    print("Task: Train a diagnostic prediction model without sharing patient data")
    print()

    # Define participants
    participants = [
        FLParticipant(
            participant_id="hospital-zurich",
            organization="Universitatsspital Zurich",
            sample_count=5000,
            data_distribution="non-iid",
            local_data_mean=0.2,
            local_data_std=1.0,
        ),
        FLParticipant(
            participant_id="hospital-bern",
            organization="Inselspital Bern",
            sample_count=8000,
            data_distribution="non-iid",
            local_data_mean=-0.1,
            local_data_std=0.8,
        ),
        FLParticipant(
            participant_id="hospital-basel",
            organization="Universitatsspital Basel",
            sample_count=3000,
            data_distribution="non-iid",
            local_data_mean=0.0,
            local_data_std=1.2,
        ),
    ]

    model_dim = 10  # Simplified model dimension

    # Configure DP
    dp = DPMechanism(
        clipping_norm=1.0,
        noise_multiplier=1.1,
        target_epsilon=3.0,
        target_delta=1e-5,
    )

    print("--- Participants ---")
    for p in participants:
        print(f"  {p.participant_id} ({p.organization}): {p.sample_count} samples, {p.data_distribution}")
    print()

    print("--- DP Configuration ---")
    print(f"  Clipping norm: {dp.clipping_norm}")
    print(f"  Noise multiplier: {dp.noise_multiplier}")
    print(f"  Target epsilon: {dp.target_epsilon}")
    print(f"  Target delta: {dp.target_delta}")
    print()

    # FedAvg training
    print("=== FedAvg Training (5 rounds) ===")
    aggregator = FederatedAggregator(model_dim=model_dim, strategy="fedavg")

    for round_num in range(5):
        updates = []
        for participant in participants:
            update = simulate_local_training(
                participant=participant,
                global_weights=aggregator.global_weights,
                local_epochs=3,
                learning_rate=0.01,
                dp=dp,
            )
            updates.append(update)

        new_weights = aggregator.aggregate(updates)

        round_info = aggregator.history[-1]
        print(f"  Round {round_info['round']}: "
              f"avg_loss={round_info['avg_loss']:.6f}, "
              f"participants={round_info['participants']}, "
              f"DP budget used={dp.budget_utilization:.1f}%")

        for u in updates:
            clipped_str = " [CLIPPED]" if u.clipped else ""
            print(f"    {u.participant_id}: loss={u.local_loss:.6f}, "
                  f"grad_norm={u.gradient_norm:.4f}{clipped_str}")

    print()
    print(f"  Total DP epsilon consumed: {dp.epsilon_consumed:.4f} / {dp.target_epsilon}")
    print(f"  DP budget remaining: {dp.budget_remaining:.4f}")
    print()

    # FedProx comparison
    print("=== FedProx Training (5 rounds, mu=0.01) ===")
    aggregator_prox = FederatedAggregator(model_dim=model_dim, strategy="fedprox", proximal_mu=0.01)
    dp_prox = DPMechanism(clipping_norm=1.0, noise_multiplier=1.1, target_epsilon=3.0)

    for round_num in range(5):
        updates = []
        for participant in participants:
            update = simulate_local_training(
                participant=participant,
                global_weights=aggregator_prox.global_weights,
                local_epochs=3,
                learning_rate=0.01,
                dp=dp_prox,
                proximal_mu=0.01,
            )
            updates.append(update)

        aggregator_prox.aggregate(updates)
        round_info = aggregator_prox.history[-1]
        print(f"  Round {round_info['round']}: avg_loss={round_info['avg_loss']:.6f}")

    print()

    # Secure aggregation demo
    print("=== Secure Aggregation Demo ===")
    # Create sample updates
    sample_updates = []
    for p in participants:
        update = ModelUpdate(
            participant_id=p.participant_id,
            weights=[random.gauss(0, 1) for _ in range(5)],
            sample_count=p.sample_count,
            local_loss=0.1,
            local_epochs=3,
        )
        sample_updates.append(update)

    # Plain aggregation (server sees individual updates)
    plain_avg = [0.0] * 5
    for u in sample_updates:
        for d in range(5):
            plain_avg[d] += u.weights[d]
    plain_avg = [a / len(sample_updates) for a in plain_avg]

    # Secure aggregation (server sees only the sum)
    secure_avg = SecureAggregationSimulator.aggregate_with_masks(sample_updates)

    print("  Plain aggregation result:  ", [f"{v:.4f}" for v in plain_avg])
    print("  Secure aggregation result: ", [f"{v:.4f}" for v in secure_avg])
    max_diff = max(abs(a - b) for a, b in zip(plain_avg, secure_avg))
    print(f"  Maximum difference: {max_diff:.10f}")
    print(f"  Results match: {max_diff < 1e-6}")
    print()

    print("=== GDPR Compliance Summary ===")
    print("  Art. 5(1)(c) data minimization: Raw patient data never leaves hospital premises")
    print("  Art. 25(1) by design: Privacy-preserving architecture (FL + DP + secure aggregation)")
    print("  Art. 26 joint controller: Consortium governed by joint controller agreement")
    print("  Art. 35 DPIA: Required for health data processing (special category, Art. 9)")
    print(f"  DP guarantee: (epsilon={dp.target_epsilon}, delta={dp.target_delta})")


if __name__ == "__main__":
    run_example()
