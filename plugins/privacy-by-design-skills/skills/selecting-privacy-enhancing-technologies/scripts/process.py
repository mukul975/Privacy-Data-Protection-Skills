#!/usr/bin/env python3
"""
Privacy-Enhancing Technology Selection Engine

Implements a structured PET selection framework that evaluates candidate
technologies against processing requirements, constraints, and GDPR alignment.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class PrivacyProperty(Enum):
    CONFIDENTIALITY = "confidentiality"
    ANONYMITY = "anonymity"
    UNLINKABILITY = "unlinkability"
    DATA_MINIMIZATION = "data_minimization"
    COMPUTATION_INTEGRITY = "computation_integrity"
    TRANSPARENCY = "transparency"


class AdversaryModel(Enum):
    HONEST_BUT_CURIOUS = "honest_but_curious"
    MALICIOUS = "malicious"
    INSIDER = "insider"
    EXTERNAL = "external"


class PerformanceTier(Enum):
    REAL_TIME = "real_time"        # < 100ms latency
    INTERACTIVE = "interactive"     # < 5s latency
    BATCH = "batch"                # Minutes to hours
    OFFLINE = "offline"            # Hours to days


@dataclass
class PETProfile:
    """Profile of a Privacy-Enhancing Technology."""
    name: str
    abbreviation: str
    privacy_properties: list[PrivacyProperty]
    adversary_models: list[AdversaryModel]
    performance_tier: PerformanceTier
    computational_overhead: str
    maturity_score: int          # 1-5 (1=research, 5=widely deployed)
    implementation_complexity: int  # 1-5 (1=simple, 5=expert required)
    data_utility: str            # "exact", "approximate", "statistical"
    gdpr_articles: list[str]
    libraries: list[str]
    best_for: list[str]
    limitations: list[str]


@dataclass
class ProcessingRequirement:
    """Requirements for a data processing activity."""
    activity_name: str
    description: str
    primary_privacy_property: PrivacyProperty
    secondary_properties: list[PrivacyProperty] = field(default_factory=list)
    adversary_model: AdversaryModel = AdversaryModel.HONEST_BUT_CURIOUS
    performance_requirement: PerformanceTier = PerformanceTier.BATCH
    data_categories: list[str] = field(default_factory=list)
    cross_organizational: bool = False
    special_categories: bool = False
    budget_constraint: str = "medium"
    team_crypto_expertise: int = 3  # 1-5


class PETSelector:
    """PET selection engine implementing the decision framework."""

    def __init__(self):
        self.pet_catalog: dict[str, PETProfile] = {}
        self._load_catalog()

    def _load_catalog(self):
        """Load the PET catalog with technology profiles."""

        self.pet_catalog["DP"] = PETProfile(
            name="Differential Privacy",
            abbreviation="DP",
            privacy_properties=[PrivacyProperty.ANONYMITY, PrivacyProperty.UNLINKABILITY],
            adversary_models=[AdversaryModel.HONEST_BUT_CURIOUS, AdversaryModel.MALICIOUS, AdversaryModel.EXTERNAL],
            performance_tier=PerformanceTier.REAL_TIME,
            computational_overhead="Low (query-time noise) to Moderate (DP-SGD training)",
            maturity_score=5,
            implementation_complexity=2,
            data_utility="statistical",
            gdpr_articles=["Art. 5(1)(c)", "Art. 25(1)", "Recital 26"],
            libraries=["Google DP Library", "OpenDP", "IBM diffprivlib", "PyDP"],
            best_for=["Aggregate analytics", "Statistical reporting", "ML training", "Surveys"],
            limitations=["Not suitable for individual-level queries", "Utility degrades with small datasets"],
        )

        self.pet_catalog["HE"] = PETProfile(
            name="Homomorphic Encryption",
            abbreviation="HE",
            privacy_properties=[PrivacyProperty.CONFIDENTIALITY],
            adversary_models=[AdversaryModel.HONEST_BUT_CURIOUS, AdversaryModel.INSIDER],
            performance_tier=PerformanceTier.BATCH,
            computational_overhead="Very High (1,000x-1,000,000x plaintext)",
            maturity_score=3,
            implementation_complexity=5,
            data_utility="exact",
            gdpr_articles=["Art. 32(1)(a)", "Art. 25(1)", "Art. 28"],
            libraries=["Microsoft SEAL", "IBM HELib", "OpenFHE", "TFHE-rs", "Google FHE"],
            best_for=["Cloud computation on encrypted data", "Encrypted search", "Private inference"],
            limitations=["Extremely high computational overhead", "Limited operation types in early schemes"],
        )

        self.pet_catalog["SMPC"] = PETProfile(
            name="Secure Multi-Party Computation",
            abbreviation="SMPC",
            privacy_properties=[PrivacyProperty.CONFIDENTIALITY, PrivacyProperty.DATA_MINIMIZATION],
            adversary_models=[AdversaryModel.HONEST_BUT_CURIOUS, AdversaryModel.MALICIOUS],
            performance_tier=PerformanceTier.INTERACTIVE,
            computational_overhead="Moderate to High (depends on circuit complexity)",
            maturity_score=4,
            implementation_complexity=4,
            data_utility="exact",
            gdpr_articles=["Art. 5(1)(c)", "Art. 25(1)", "Art. 26"],
            libraries=["MP-SPDZ", "CrypTen", "MOTION", "ABY3", "Sharemind"],
            best_for=["Cross-organizational analytics", "Joint credit scoring", "AML screening"],
            limitations=["Communication overhead scales with parties", "Complex key management"],
        )

        self.pet_catalog["FL"] = PETProfile(
            name="Federated Learning",
            abbreviation="FL",
            privacy_properties=[PrivacyProperty.DATA_MINIMIZATION, PrivacyProperty.CONFIDENTIALITY],
            adversary_models=[AdversaryModel.HONEST_BUT_CURIOUS],
            performance_tier=PerformanceTier.BATCH,
            computational_overhead="Low per participant; communication overhead for aggregation",
            maturity_score=4,
            implementation_complexity=3,
            data_utility="approximate",
            gdpr_articles=["Art. 5(1)(c)", "Art. 25(1)", "Chapter V (reduces transfer need)"],
            libraries=["TensorFlow Federated", "PySyft", "NVIDIA FLARE", "Flower", "FedML"],
            best_for=["Distributed ML training", "Hospital data collaboration", "Mobile device learning"],
            limitations=["Non-IID data degrades model quality", "Gradient inversion attacks without DP"],
        )

        self.pet_catalog["ZKP"] = PETProfile(
            name="Zero-Knowledge Proofs",
            abbreviation="ZKP",
            privacy_properties=[PrivacyProperty.DATA_MINIMIZATION, PrivacyProperty.COMPUTATION_INTEGRITY],
            adversary_models=[AdversaryModel.MALICIOUS, AdversaryModel.EXTERNAL],
            performance_tier=PerformanceTier.INTERACTIVE,
            computational_overhead="Moderate (proof generation); Low (verification)",
            maturity_score=3,
            implementation_complexity=5,
            data_utility="exact",
            gdpr_articles=["Art. 5(1)(c)", "Art. 25(1)", "Art. 25(2)"],
            libraries=["snarkjs", "circom", "bellman", "arkworks", "gnark"],
            best_for=["Age verification", "Identity attestation", "Credential verification", "Regulatory proofs"],
            limitations=["Complex circuit design", "Trusted setup requirement for some schemes"],
        )

        self.pet_catalog["TEE"] = PETProfile(
            name="Trusted Execution Environment",
            abbreviation="TEE",
            privacy_properties=[PrivacyProperty.CONFIDENTIALITY, PrivacyProperty.COMPUTATION_INTEGRITY],
            adversary_models=[AdversaryModel.INSIDER, AdversaryModel.MALICIOUS],
            performance_tier=PerformanceTier.REAL_TIME,
            computational_overhead="Low to Moderate (limited enclave memory)",
            maturity_score=4,
            implementation_complexity=3,
            data_utility="exact",
            gdpr_articles=["Art. 32(1)(a)", "Art. 28", "Art. 25(1)"],
            libraries=["Intel SGX SDK", "Open Enclave", "Gramine", "AWS Nitro SDK", "Azure Confidential Computing SDK"],
            best_for=["Cloud confidential computing", "Encrypted inference", "Secure key management"],
            limitations=["Hardware dependency", "Side-channel attack surface", "Limited enclave memory"],
        )

    def evaluate(self, requirement: ProcessingRequirement) -> list[dict]:
        """
        Evaluate all PETs against a processing requirement.

        Returns sorted list of PET evaluations with scores and rationale.
        """
        evaluations = []

        for abbr, pet in self.pet_catalog.items():
            score = 0
            rationale = []

            # Privacy property match (0-30 points)
            if requirement.primary_privacy_property in pet.privacy_properties:
                score += 20
                rationale.append(f"Directly provides {requirement.primary_privacy_property.value}")
            for sp in requirement.secondary_properties:
                if sp in pet.privacy_properties:
                    score += 5
                    rationale.append(f"Also provides {sp.value}")

            # Adversary model match (0-15 points)
            if requirement.adversary_model in pet.adversary_models:
                score += 15
                rationale.append(f"Handles {requirement.adversary_model.value} adversary")

            # Performance match (0-15 points)
            perf_map = {
                PerformanceTier.REAL_TIME: {PerformanceTier.REAL_TIME: 15, PerformanceTier.INTERACTIVE: 5},
                PerformanceTier.INTERACTIVE: {PerformanceTier.REAL_TIME: 15, PerformanceTier.INTERACTIVE: 15, PerformanceTier.BATCH: 5},
                PerformanceTier.BATCH: {PerformanceTier.REAL_TIME: 15, PerformanceTier.INTERACTIVE: 15, PerformanceTier.BATCH: 15, PerformanceTier.OFFLINE: 5},
                PerformanceTier.OFFLINE: {t: 15 for t in PerformanceTier},
            }
            perf_score = perf_map.get(requirement.performance_requirement, {}).get(pet.performance_tier, 0)
            score += perf_score
            if perf_score >= 10:
                rationale.append(f"Meets {requirement.performance_requirement.value} performance requirement")

            # Maturity (0-10 points)
            maturity_points = pet.maturity_score * 2
            score += maturity_points
            if pet.maturity_score >= 4:
                rationale.append(f"Production-mature (maturity: {pet.maturity_score}/5)")

            # Implementation complexity vs team expertise (0-10 points)
            expertise_gap = max(0, pet.implementation_complexity - requirement.team_crypto_expertise)
            complexity_points = max(0, 10 - expertise_gap * 3)
            score += complexity_points
            if expertise_gap > 1:
                rationale.append(f"Expertise gap: team level {requirement.team_crypto_expertise}, "
                                f"PET requires {pet.implementation_complexity}")

            # Cross-organizational bonus for SMPC and FL
            if requirement.cross_organizational and abbr in ("SMPC", "FL"):
                score += 10
                rationale.append("Well-suited for cross-organizational processing")

            # Special categories: prefer stronger guarantees
            if requirement.special_categories and pet.maturity_score >= 4:
                score += 5
                rationale.append("Adequate for special category data (Art. 9)")

            evaluations.append({
                "pet_name": pet.name,
                "abbreviation": abbr,
                "score": score,
                "max_possible": 100,
                "rationale": rationale,
                "libraries": pet.libraries,
                "gdpr_articles": pet.gdpr_articles,
                "limitations": pet.limitations,
                "data_utility": pet.data_utility,
            })

        evaluations.sort(key=lambda x: x["score"], reverse=True)
        return evaluations

    def recommend_combination(self, primary_pet: str) -> list[dict]:
        """Recommend complementary PETs for defense in depth."""
        combinations = {
            "FL": [
                {"complement": "DP", "reason": "Prevents gradient inversion attacks with provable privacy guarantee"},
                {"complement": "TEE", "reason": "Secure aggregation within enclave protects model updates"},
            ],
            "SMPC": [
                {"complement": "DP", "reason": "Adds formal anonymization to exact computation outputs"},
                {"complement": "TEE", "reason": "Hardware protection for secret share reconstruction"},
            ],
            "HE": [
                {"complement": "TEE", "reason": "Protects computation patterns alongside encrypted data"},
                {"complement": "ZKP", "reason": "Proves correct computation on encrypted data"},
            ],
            "DP": [
                {"complement": "FL", "reason": "Enables distributed DP analytics without centralizing data"},
                {"complement": "SMPC", "reason": "Exact computation with DP output layer"},
            ],
            "ZKP": [
                {"complement": "TEE", "reason": "Proves enclave computation integrity to external verifiers"},
            ],
            "TEE": [
                {"complement": "HE", "reason": "Double protection: hardware isolation plus encryption"},
                {"complement": "DP", "reason": "Adds statistical privacy to enclave outputs"},
            ],
        }
        return combinations.get(primary_pet, [])


def run_example():
    """Demonstrate PET selection for Prism Data Systems AG use cases."""

    selector = PETSelector()

    use_cases = [
        ProcessingRequirement(
            activity_name="Customer behavior analytics",
            description="Aggregate analysis of customer feature usage patterns for product improvement",
            primary_privacy_property=PrivacyProperty.ANONYMITY,
            secondary_properties=[PrivacyProperty.UNLINKABILITY],
            adversary_model=AdversaryModel.HONEST_BUT_CURIOUS,
            performance_requirement=PerformanceTier.BATCH,
            data_categories=["pseudonymized_user_id", "feature_events", "session_duration"],
            team_crypto_expertise=3,
        ),
        ProcessingRequirement(
            activity_name="Cross-hospital ML model training",
            description="Training a diagnostic model across three partner hospitals without sharing patient data",
            primary_privacy_property=PrivacyProperty.DATA_MINIMIZATION,
            secondary_properties=[PrivacyProperty.CONFIDENTIALITY],
            adversary_model=AdversaryModel.HONEST_BUT_CURIOUS,
            performance_requirement=PerformanceTier.OFFLINE,
            data_categories=["medical_images", "diagnosis_labels"],
            cross_organizational=True,
            special_categories=True,
            team_crypto_expertise=2,
        ),
        ProcessingRequirement(
            activity_name="Age verification gateway",
            description="Verify customer age for age-restricted content without collecting date of birth",
            primary_privacy_property=PrivacyProperty.DATA_MINIMIZATION,
            secondary_properties=[PrivacyProperty.COMPUTATION_INTEGRITY],
            adversary_model=AdversaryModel.EXTERNAL,
            performance_requirement=PerformanceTier.REAL_TIME,
            data_categories=[],
            team_crypto_expertise=4,
        ),
    ]

    for uc in use_cases:
        print(f"=== PET Selection: {uc.activity_name} ===")
        print(f"Description: {uc.description}")
        print(f"Primary property: {uc.primary_privacy_property.value}")
        print(f"Performance: {uc.performance_requirement.value}")
        print()

        evaluations = selector.evaluate(uc)

        for i, ev in enumerate(evaluations[:3]):
            rank = i + 1
            print(f"  #{rank} {ev['pet_name']} ({ev['abbreviation']}) — Score: {ev['score']}/{ev['max_possible']}")
            print(f"     Utility: {ev['data_utility']}")
            print(f"     Rationale:")
            for r in ev["rationale"]:
                print(f"       - {r}")
            print(f"     GDPR: {', '.join(ev['gdpr_articles'])}")
            print(f"     Libraries: {', '.join(ev['libraries'][:3])}")
            if ev["limitations"]:
                print(f"     Key limitation: {ev['limitations'][0]}")
            print()

        # Show recommended combination for top pick
        top_pet = evaluations[0]["abbreviation"]
        combos = selector.recommend_combination(top_pet)
        if combos:
            print(f"  Recommended combinations with {top_pet}:")
            for combo in combos:
                print(f"    + {combo['complement']}: {combo['reason']}")
            print()

        print("-" * 70)
        print()


if __name__ == "__main__":
    run_example()
