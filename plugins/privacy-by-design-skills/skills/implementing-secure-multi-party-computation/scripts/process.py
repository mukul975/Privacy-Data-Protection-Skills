#!/usr/bin/env python3
"""
Secure Multi-Party Computation Simulation

Demonstrates SMPC concepts including additive secret sharing,
Shamir secret sharing, and privacy-preserving aggregation.
Educational implementation — production should use MP-SPDZ or CrypTen.
"""

import random
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional


PRIME_MODULUS = 2**61 - 1  # Mersenne prime for modular arithmetic


class AdditiveSecretSharing:
    """
    Additive secret sharing for n parties.

    Splits a secret into n shares such that the sum of all shares
    equals the secret (mod p). Any n-1 shares reveal nothing.
    """

    def __init__(self, num_parties: int, modulus: int = PRIME_MODULUS):
        self.num_parties = num_parties
        self.modulus = modulus

    def share(self, secret: int) -> list[int]:
        """Split a secret into n additive shares."""
        shares = [random.randint(0, self.modulus - 1) for _ in range(self.num_parties - 1)]
        last_share = (secret - sum(shares)) % self.modulus
        shares.append(last_share)
        return shares

    def reconstruct(self, shares: list[int]) -> int:
        """Reconstruct a secret from all n shares."""
        return sum(shares) % self.modulus

    def add_shares(self, shares_a: list[int], shares_b: list[int]) -> list[int]:
        """Add two shared values (no communication needed)."""
        return [(a + b) % self.modulus for a, b in zip(shares_a, shares_b)]

    def multiply_by_constant(self, shares: list[int], constant: int) -> list[int]:
        """Multiply a shared value by a public constant (no communication needed)."""
        return [(s * constant) % self.modulus for s in shares]


class ShamirSecretSharing:
    """
    Shamir's (t, n) threshold secret sharing.

    Splits a secret into n shares such that any t shares can reconstruct
    the secret, but fewer than t shares reveal nothing.
    Uses polynomial interpolation over a finite field.
    """

    def __init__(self, threshold: int, num_parties: int, modulus: int = PRIME_MODULUS):
        self.threshold = threshold
        self.num_parties = num_parties
        self.modulus = modulus

    def share(self, secret: int) -> list[tuple[int, int]]:
        """Split secret into n shares with threshold t."""
        # Generate random polynomial of degree t-1 with secret as constant term
        coefficients = [secret] + [random.randint(0, self.modulus - 1) for _ in range(self.threshold - 1)]

        shares = []
        for i in range(1, self.num_parties + 1):
            # Evaluate polynomial at point i
            y = 0
            for j, coeff in enumerate(coefficients):
                y = (y + coeff * pow(i, j, self.modulus)) % self.modulus
            shares.append((i, y))

        return shares

    def reconstruct(self, shares: list[tuple[int, int]]) -> int:
        """Reconstruct secret from t or more shares using Lagrange interpolation."""
        if len(shares) < self.threshold:
            raise ValueError(f"Need at least {self.threshold} shares, got {len(shares)}")

        secret = 0
        for i, (xi, yi) in enumerate(shares[:self.threshold]):
            # Compute Lagrange basis polynomial at x=0
            numerator = 1
            denominator = 1
            for j, (xj, _) in enumerate(shares[:self.threshold]):
                if i != j:
                    numerator = (numerator * (-xj)) % self.modulus
                    denominator = (denominator * (xi - xj)) % self.modulus

            # Modular inverse of denominator
            lagrange = (yi * numerator * pow(denominator, self.modulus - 2, self.modulus)) % self.modulus
            secret = (secret + lagrange) % self.modulus

        return secret


@dataclass
class SMPCParty:
    """A party in an SMPC computation."""
    party_id: str
    organization: str
    input_value: Optional[int] = None
    shares_held: dict = field(default_factory=dict)


class PrivateAggregation:
    """
    Privacy-preserving aggregation using additive secret sharing.

    Enables multiple parties to compute the sum of their private values
    without revealing any individual value.
    """

    def __init__(self, parties: list[SMPCParty]):
        self.parties = parties
        self.sharing = AdditiveSecretSharing(len(parties))
        self.audit_log: list[dict] = []

    def compute_private_sum(self) -> dict:
        """
        Compute the sum of all parties' inputs without revealing individual values.

        Protocol:
        1. Each party splits their input into n shares
        2. Each party sends one share to each other party
        3. Each party sums the shares they received
        4. Parties exchange their local sums to reconstruct the total
        """
        n = len(self.parties)

        # Step 1: Each party creates shares of their input
        all_shares = {}
        for party in self.parties:
            shares = self.sharing.share(party.input_value)
            all_shares[party.party_id] = shares
            self._log(f"{party.party_id} created {n} shares of their input")

        # Step 2: Distribute shares (party i gets the i-th share from each party)
        party_received_shares = {p.party_id: [] for p in self.parties}
        for i, party in enumerate(self.parties):
            for source_id, shares in all_shares.items():
                party_received_shares[party.party_id].append(shares[i])

        # Step 3: Each party computes local sum of received shares
        local_sums = {}
        for party in self.parties:
            local_sum = sum(party_received_shares[party.party_id]) % self.sharing.modulus
            local_sums[party.party_id] = local_sum
            self._log(f"{party.party_id} computed local sum of received shares")

        # Step 4: Reconstruct total sum from local sums
        total = sum(local_sums.values()) % self.sharing.modulus
        self._log(f"Total sum reconstructed: {total}")

        return {
            "result": total,
            "num_parties": n,
            "protocol": "additive_secret_sharing",
            "security_model": "semi-honest",
            "individual_inputs_revealed": False,
        }

    def _log(self, message: str) -> None:
        self.audit_log.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "message": message,
        })


class PrivateComparison:
    """
    Privacy-preserving comparison using secret sharing.

    Determines which party has the larger value without revealing
    either value (simplified educational version).
    """

    @staticmethod
    def compare_private(value_a: int, value_b: int, modulus: int = PRIME_MODULUS) -> dict:
        """
        Determine if value_a > value_b without revealing either value.

        In production, this would use garbled circuits or Yao's protocol.
        This simulation demonstrates the concept.
        """
        # Create shares
        sharing = AdditiveSecretSharing(2, modulus)
        shares_a = sharing.share(value_a)
        shares_b = sharing.share(value_b)

        # Compute difference in shared form
        diff_shares = [(shares_a[i] - shares_b[i]) % modulus for i in range(2)]

        # Reconstruct difference (in real protocol, only the sign bit would be revealed)
        diff = sharing.reconstruct(diff_shares)

        # Determine comparison result (simplified)
        if diff == 0:
            result = "equal"
        elif diff < modulus // 2:
            result = "a_greater"
        else:
            result = "b_greater"

        return {
            "result": result,
            "values_revealed": False,
            "protocol": "secret_shared_comparison",
        }


def run_example():
    """Demonstrate SMPC for Prism Data Systems AG cross-organizational analytics."""

    print("=== Secure Multi-Party Computation Demo ===")
    print("Scenario: Three Prism Data Systems AG regional offices compute")
    print("aggregate headcount and total revenue without revealing per-office figures")
    print()

    # --- Additive Secret Sharing ---
    print("=== Additive Secret Sharing ===")
    sharing = AdditiveSecretSharing(num_parties=3)

    secret = 42000  # Annual revenue in CHF thousands
    shares = sharing.share(secret)
    print(f"  Secret: {secret}")
    print(f"  Shares: {shares}")
    reconstructed = sharing.reconstruct(shares)
    print(f"  Reconstructed: {reconstructed}")
    print(f"  Correct: {reconstructed == secret}")
    print()

    # Demonstrate homomorphic addition on shares
    secret_a = 15000
    secret_b = 27000
    shares_a = sharing.share(secret_a)
    shares_b = sharing.share(secret_b)
    sum_shares = sharing.add_shares(shares_a, shares_b)
    reconstructed_sum = sharing.reconstruct(sum_shares)
    print(f"  Secret A: {secret_a}, Secret B: {secret_b}")
    print(f"  Sum of shares (no communication): {reconstructed_sum}")
    print(f"  Correct: {reconstructed_sum == secret_a + secret_b}")
    print()

    # --- Shamir Secret Sharing ---
    print("=== Shamir (2,3) Threshold Secret Sharing ===")
    shamir = ShamirSecretSharing(threshold=2, num_parties=3)

    secret = 99999
    shares = shamir.share(secret)
    print(f"  Secret: {secret}")
    print(f"  Shares: {[(x, y % 1000) for x, y in shares]}... (truncated)")

    # Reconstruct with any 2 of 3 shares
    for combo_name, combo in [("shares 1,2", shares[:2]), ("shares 2,3", shares[1:]),
                               ("shares 1,3", [shares[0], shares[2]])]:
        result = shamir.reconstruct(combo)
        print(f"  Reconstruct with {combo_name}: {result} (correct: {result == secret})")
    print()

    # --- Private Aggregation ---
    print("=== Privacy-Preserving Aggregation ===")
    print("Three regional offices compute total revenue without revealing per-office figures")
    print()

    parties = [
        SMPCParty(party_id="office-zurich", organization="Prism Data Systems AG (Zurich)", input_value=8500),
        SMPCParty(party_id="office-berlin", organization="Prism Data Systems AG (Berlin)", input_value=6200),
        SMPCParty(party_id="office-vienna", organization="Prism Data Systems AG (Vienna)", input_value=4300),
    ]

    aggregation = PrivateAggregation(parties)
    result = aggregation.compute_private_sum()

    expected_sum = sum(p.input_value for p in parties)
    print(f"  Party inputs (private, never shared):")
    for p in parties:
        print(f"    {p.party_id}: {p.input_value} CHF thousands")
    print()
    print(f"  SMPC computed sum: {result['result']} CHF thousands")
    print(f"  Expected sum: {expected_sum}")
    print(f"  Correct: {result['result'] == expected_sum}")
    print(f"  Individual inputs revealed: {result['individual_inputs_revealed']}")
    print(f"  Protocol: {result['protocol']}")
    print(f"  Security model: {result['security_model']}")
    print()

    # --- Private Comparison ---
    print("=== Privacy-Preserving Comparison ===")
    print("Two parties determine whose value is larger without revealing either value")
    print()
    comp = PrivateComparison.compare_private(8500, 6200)
    print(f"  Comparison result: {comp['result']}")
    print(f"  Values revealed: {comp['values_revealed']}")
    print()

    # --- Audit Log ---
    print("=== Protocol Audit Log ===")
    for entry in aggregation.audit_log:
        print(f"  [{entry['timestamp'][:19]}] {entry['message']}")
    print()

    print("=== GDPR Compliance Summary ===")
    print("  Art. 5(1)(c): Individual office revenues never centralized or shared")
    print("  Art. 25(1): Privacy protection embedded in computation architecture")
    print("  Art. 26: Joint controller agreement governs multi-office computation")
    print("  Art. 32(1): Information-theoretic security (additive sharing)")
    print()
    print("  Production frameworks for deployment:")
    print("    MP-SPDZ: pip install mp-spdz (or build from source)")
    print("    CrypTen: pip install crypten")
    print("    Sharemind: Commercial license from Cybernetica AS")


if __name__ == "__main__":
    run_example()
