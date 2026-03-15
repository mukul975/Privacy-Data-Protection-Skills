#!/usr/bin/env python3
"""
Pseudonymization Technique Assessment and Re-Identification Risk Scoring Engine

Implements ENISA pseudonymization technique evaluation and quantitative
re-identification risk assessment using prosecutor, journalist, and marketer models.
"""

import hashlib
import hmac
import math
import os
import secrets
import uuid
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class PseudonymizationTechnique(Enum):
    COUNTER = "counter"
    HMAC_SHA256 = "hmac_sha256"
    ENCRYPTION_AES = "encryption_aes"
    FORMAT_PRESERVING = "format_preserving_encryption"
    TOKENIZATION = "tokenization"
    SYNTHETIC = "synthetic_replacement"


class RiskClassification(Enum):
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    VERY_HIGH = "VERY_HIGH"


@dataclass
class TechniqueProperty:
    """Properties of a pseudonymization technique per ENISA taxonomy."""
    reversible: bool
    deterministic: bool
    format_preserving: bool
    linkable_within_dataset: bool
    linkable_across_datasets: bool
    requires_key_management: bool
    brute_force_resistant: bool


TECHNIQUE_PROPERTIES = {
    PseudonymizationTechnique.COUNTER: TechniqueProperty(
        reversible=True, deterministic=True, format_preserving=False,
        linkable_within_dataset=True, linkable_across_datasets=False,
        requires_key_management=False, brute_force_resistant=True,
    ),
    PseudonymizationTechnique.HMAC_SHA256: TechniqueProperty(
        reversible=False, deterministic=True, format_preserving=False,
        linkable_within_dataset=True, linkable_across_datasets=True,
        requires_key_management=True, brute_force_resistant=True,
    ),
    PseudonymizationTechnique.ENCRYPTION_AES: TechniqueProperty(
        reversible=True, deterministic=True, format_preserving=False,
        linkable_within_dataset=True, linkable_across_datasets=True,
        requires_key_management=True, brute_force_resistant=True,
    ),
    PseudonymizationTechnique.FORMAT_PRESERVING: TechniqueProperty(
        reversible=True, deterministic=True, format_preserving=True,
        linkable_within_dataset=True, linkable_across_datasets=True,
        requires_key_management=True, brute_force_resistant=True,
    ),
    PseudonymizationTechnique.TOKENIZATION: TechniqueProperty(
        reversible=True, deterministic=False, format_preserving=False,
        linkable_within_dataset=False, linkable_across_datasets=False,
        requires_key_management=False, brute_force_resistant=True,
    ),
    PseudonymizationTechnique.SYNTHETIC: TechniqueProperty(
        reversible=False, deterministic=False, format_preserving=True,
        linkable_within_dataset=False, linkable_across_datasets=False,
        requires_key_management=False, brute_force_resistant=True,
    ),
}


@dataclass
class TechniqueAssessment:
    """Assessment scores for a pseudonymization technique (0-100 each)."""
    technique: PseudonymizationTechnique
    key_mapping_security: int  # 0-100: quality of key/mapping protection
    brute_force_resistance: int  # 0-100: resistance to brute-force re-identification
    cross_dataset_unlinkability: int  # 0-100: resistance to cross-dataset linkage
    implementation_maturity: int  # 0-100: library quality, audit history
    operational_resilience: int  # 0-100: key rotation, backup, DR readiness

    @property
    def weighted_score(self) -> float:
        """Compute weighted technique score per the 5-property model."""
        return (
            self.key_mapping_security * 0.30
            + self.brute_force_resistance * 0.25
            + self.cross_dataset_unlinkability * 0.20
            + self.implementation_maturity * 0.15
            + self.operational_resilience * 0.10
        )


@dataclass
class DataEnvironmentAssessment:
    """Assessment scores for the data environment re-identification risk (0-100 each)."""
    data_flow_name: str
    population_uniqueness: int  # 0-100: how unique are attribute combinations
    auxiliary_data_availability: int  # 0-100: how much external data can be linked
    quasi_identifier_count: int  # 0-100: based on count and granularity
    dataset_size_risk: int  # 0-100: smaller = higher risk (inverted)
    release_frequency_risk: int  # 0-100: more frequent = higher composition risk

    @property
    def weighted_risk(self) -> float:
        """Compute weighted data environment risk score."""
        return (
            self.population_uniqueness * 0.25
            + self.auxiliary_data_availability * 0.25
            + self.quasi_identifier_count * 0.20
            + self.dataset_size_risk * 0.15
            + self.release_frequency_risk * 0.15
        )


def compute_residual_risk(technique_score: float, environment_risk: float) -> float:
    """
    Residual Risk = Environment Risk * (1 - Technique Score / 100)
    Returns a value between 0 and 100.
    """
    return environment_risk * (1.0 - technique_score / 100.0)


def classify_risk(residual_risk: float) -> RiskClassification:
    """Classify residual risk per the four-tier model."""
    if residual_risk <= 15:
        return RiskClassification.LOW
    elif residual_risk <= 35:
        return RiskClassification.MODERATE
    elif residual_risk <= 60:
        return RiskClassification.HIGH
    else:
        return RiskClassification.VERY_HIGH


# ---------------------------------------------------------------------------
# Re-Identification Risk Quantitative Models
# ---------------------------------------------------------------------------

def compute_equivalence_classes(records: list[dict], quasi_identifiers: list[str]) -> dict[tuple, int]:
    """
    Compute equivalence classes from a dataset.
    Returns a dict mapping quasi-identifier value tuples to their count.
    """
    qi_tuples = []
    for record in records:
        qi_values = tuple(record.get(qi, None) for qi in quasi_identifiers)
        qi_tuples.append(qi_values)
    return dict(Counter(qi_tuples))


def prosecutor_risk(equivalence_classes: dict[tuple, int]) -> float:
    """
    Prosecutor model: attacker knows target is in the dataset.
    Risk = 1 / k_min (worst case).
    """
    if not equivalence_classes:
        return 1.0
    k_min = min(equivalence_classes.values())
    return 1.0 / k_min


def journalist_risk(equivalence_classes: dict[tuple, int]) -> float:
    """
    Journalist model: attacker tries to re-identify anyone.
    Risk = max(1/k_i) across all equivalence classes.
    Same as prosecutor risk in practice (both driven by smallest class).
    """
    if not equivalence_classes:
        return 1.0
    return max(1.0 / k for k in equivalence_classes.values())


def marketer_risk(equivalence_classes: dict[tuple, int], total_records: int) -> float:
    """
    Marketer model: attacker tries to re-identify as many as possible.
    Risk = (1/n) * sum(1/k_i for each record).
    """
    if not equivalence_classes or total_records == 0:
        return 1.0
    # Each record in an equivalence class of size k has risk 1/k
    # There are k records in that class, contributing k * (1/k) = 1
    total_risk = sum(count * (1.0 / count) for count in equivalence_classes.values())
    return total_risk / total_records


def motivated_intruder_amplification(
    auxiliary_data_level: str,
) -> float:
    """
    Amplification factor based on motivated intruder test (ICO).
    """
    factors = {
        "low": 1.0,
        "moderate": 1.5,
        "high": 2.0,
    }
    return factors.get(auxiliary_data_level, 1.0)


def compute_l_diversity(
    records: list[dict],
    quasi_identifiers: list[str],
    sensitive_attribute: str,
) -> dict[tuple, int]:
    """
    Compute l-diversity for each equivalence class.
    Returns a dict mapping QI tuples to the number of distinct sensitive values (l).
    """
    classes: dict[tuple, set] = {}
    for record in records:
        qi_key = tuple(record.get(qi, None) for qi in quasi_identifiers)
        sensitive_val = record.get(sensitive_attribute, None)
        if qi_key not in classes:
            classes[qi_key] = set()
        classes[qi_key].add(sensitive_val)
    return {k: len(v) for k, v in classes.items()}


# ---------------------------------------------------------------------------
# Pseudonymization Engines (Educational Implementations)
# ---------------------------------------------------------------------------

class CounterPseudonymizer:
    """Counter-based pseudonymization with UUID mapping."""

    def __init__(self):
        self._forward_map: dict[str, str] = {}
        self._reverse_map: dict[str, str] = {}

    def pseudonymize(self, identifier: str) -> str:
        if identifier in self._forward_map:
            return self._forward_map[identifier]
        pseudonym = str(uuid.uuid4())
        self._forward_map[identifier] = pseudonym
        self._reverse_map[pseudonym] = identifier
        return pseudonym

    def de_pseudonymize(self, pseudonym: str) -> Optional[str]:
        return self._reverse_map.get(pseudonym)

    @property
    def mapping_size(self) -> int:
        return len(self._forward_map)


class HMACPseudonymizer:
    """HMAC-SHA256 pseudonymization with keyed hashing."""

    def __init__(self, key: Optional[bytes] = None):
        self._key = key or secrets.token_bytes(32)

    def pseudonymize(self, identifier: str) -> str:
        return hmac.new(
            self._key, identifier.encode("utf-8"), hashlib.sha256
        ).hexdigest()

    def rotate_key(self, new_key: Optional[bytes] = None) -> bytes:
        """Rotate the HMAC key. Returns the new key."""
        self._key = new_key or secrets.token_bytes(32)
        return self._key

    @property
    def key_id(self) -> str:
        """Non-sensitive identifier for the current key (first 8 hex chars of key hash)."""
        return hashlib.sha256(self._key).hexdigest()[:8]


class TokenVault:
    """Tokenization vault with random token generation."""

    def __init__(self):
        self._vault: dict[str, str] = {}  # token -> original
        self._reverse: dict[str, str] = {}  # original -> token

    def tokenize(self, identifier: str) -> str:
        if identifier in self._reverse:
            return self._reverse[identifier]
        token = f"TOK-{secrets.token_hex(16)}"
        self._vault[token] = identifier
        self._reverse[identifier] = token
        return token

    def detokenize(self, token: str) -> Optional[str]:
        return self._vault.get(token)

    def revoke_token(self, token: str) -> bool:
        """Revoke a token, removing the mapping."""
        if token in self._vault:
            original = self._vault.pop(token)
            self._reverse.pop(original, None)
            return True
        return False

    @property
    def vault_size(self) -> int:
        return len(self._vault)


# ---------------------------------------------------------------------------
# Full Assessment Pipeline
# ---------------------------------------------------------------------------

@dataclass
class AssessmentResult:
    """Complete pseudonymization and re-identification risk assessment result."""
    data_flow_name: str
    technique: PseudonymizationTechnique
    technique_score: float
    environment_risk: float
    residual_risk: float
    risk_classification: RiskClassification
    prosecutor_risk: float
    journalist_risk: float
    marketer_risk: float
    l_diversity_min: Optional[int]
    mitigations: list[str]


def run_full_assessment(
    data_flow_name: str,
    technique_assessment: TechniqueAssessment,
    environment_assessment: DataEnvironmentAssessment,
    records: list[dict],
    quasi_identifiers: list[str],
    sensitive_attribute: Optional[str] = None,
    auxiliary_data_level: str = "moderate",
) -> AssessmentResult:
    """Run a complete pseudonymization and re-identification risk assessment."""

    technique_score = technique_assessment.weighted_score
    environment_risk = environment_assessment.weighted_risk
    residual = compute_residual_risk(technique_score, environment_risk)
    classification = classify_risk(residual)

    # Compute equivalence classes
    eq_classes = compute_equivalence_classes(records, quasi_identifiers)
    p_risk = prosecutor_risk(eq_classes) * 100
    j_risk = journalist_risk(eq_classes) * 100
    m_risk = marketer_risk(eq_classes, len(records)) * 100

    # Apply motivated intruder amplification
    amplification = motivated_intruder_amplification(auxiliary_data_level)
    p_risk = min(p_risk * amplification, 100.0)
    j_risk = min(j_risk * amplification, 100.0)
    m_risk = min(m_risk * amplification, 100.0)

    # L-diversity check
    l_div_min = None
    if sensitive_attribute:
        l_div = compute_l_diversity(records, quasi_identifiers, sensitive_attribute)
        l_div_min = min(l_div.values()) if l_div else 0

    # Generate mitigations
    mitigations = []
    if classification in (RiskClassification.HIGH, RiskClassification.VERY_HIGH):
        mitigations.append("Upgrade pseudonymization technique or reduce quasi-identifier granularity")
    if p_risk > 20:
        mitigations.append(f"Smallest equivalence class too small — enforce k-anonymity with k >= 11")
    if l_div_min is not None and l_div_min < 3:
        mitigations.append(f"l-diversity is {l_div_min} — enforce l >= 3 on sensitive attributes")
    if environment_assessment.auxiliary_data_availability > 60:
        mitigations.append("High auxiliary data availability — consider differential privacy noise addition")
    if environment_assessment.release_frequency_risk > 50:
        mitigations.append("Frequent data releases — track cumulative privacy budget to prevent composition attacks")
    if technique_assessment.cross_dataset_unlinkability < 50:
        mitigations.append("Cross-dataset linkability detected — use per-dataset keys or non-deterministic technique")

    return AssessmentResult(
        data_flow_name=data_flow_name,
        technique=technique_assessment.technique,
        technique_score=technique_score,
        environment_risk=environment_risk,
        residual_risk=residual,
        risk_classification=classification,
        prosecutor_risk=p_risk,
        journalist_risk=j_risk,
        marketer_risk=m_risk,
        l_diversity_min=l_div_min,
        mitigations=mitigations,
    )


def run_example():
    """Demonstrate pseudonymization assessment for Prism Data Systems AG."""

    print("=" * 70)
    print("Pseudonymization & Re-Identification Risk Assessment")
    print("Organization: Prism Data Systems AG")
    print(f"Assessment Date: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}")
    print("=" * 70)

    # --- Assessment 1: Analytics Pipeline (HMAC-SHA256) ---

    analytics_technique = TechniqueAssessment(
        technique=PseudonymizationTechnique.HMAC_SHA256,
        key_mapping_security=82,
        brute_force_resistance=75,
        cross_dataset_unlinkability=65,
        implementation_maturity=85,
        operational_resilience=78,
    )

    analytics_env = DataEnvironmentAssessment(
        data_flow_name="Analytics Pipeline",
        population_uniqueness=45,
        auxiliary_data_availability=40,
        quasi_identifier_count=50,
        dataset_size_risk=30,
        release_frequency_risk=45,
    )

    # Simulated analytics records with quasi-identifiers
    analytics_records = [
        {"age_group": "25-34", "country": "CH", "plan": "pro", "diagnosis": "none"},
        {"age_group": "25-34", "country": "CH", "plan": "pro", "diagnosis": "none"},
        {"age_group": "25-34", "country": "CH", "plan": "free", "diagnosis": "none"},
        {"age_group": "35-44", "country": "DE", "plan": "enterprise", "diagnosis": "none"},
        {"age_group": "35-44", "country": "DE", "plan": "enterprise", "diagnosis": "none"},
        {"age_group": "35-44", "country": "DE", "plan": "pro", "diagnosis": "none"},
        {"age_group": "45-54", "country": "AT", "plan": "free", "diagnosis": "none"},
        {"age_group": "45-54", "country": "AT", "plan": "free", "diagnosis": "none"},
        {"age_group": "25-34", "country": "FR", "plan": "pro", "diagnosis": "none"},
        {"age_group": "25-34", "country": "FR", "plan": "pro", "diagnosis": "none"},
        {"age_group": "55-64", "country": "CH", "plan": "enterprise", "diagnosis": "none"},
        {"age_group": "55-64", "country": "CH", "plan": "enterprise", "diagnosis": "none"},
    ]

    result1 = run_full_assessment(
        data_flow_name="Analytics Pipeline",
        technique_assessment=analytics_technique,
        environment_assessment=analytics_env,
        records=analytics_records,
        quasi_identifiers=["age_group", "country", "plan"],
        sensitive_attribute="diagnosis",
        auxiliary_data_level="moderate",
    )

    print(f"\n--- {result1.data_flow_name} ---")
    print(f"Technique: {result1.technique.value}")
    print(f"Technique Score: {result1.technique_score:.1f}/100")
    print(f"Environment Risk: {result1.environment_risk:.1f}/100")
    print(f"Residual Risk: {result1.residual_risk:.1f}/100")
    print(f"Classification: {result1.risk_classification.value}")
    print(f"Prosecutor Risk: {result1.prosecutor_risk:.1f}%")
    print(f"Journalist Risk: {result1.journalist_risk:.1f}%")
    print(f"Marketer Risk: {result1.marketer_risk:.1f}%")
    if result1.l_diversity_min is not None:
        print(f"Min l-diversity: {result1.l_diversity_min}")
    if result1.mitigations:
        print("Mitigations:")
        for m in result1.mitigations:
            print(f"  - {m}")

    # --- Assessment 2: Support Dashboard (FPE) ---

    support_technique = TechniqueAssessment(
        technique=PseudonymizationTechnique.FORMAT_PRESERVING,
        key_mapping_security=88,
        brute_force_resistance=80,
        cross_dataset_unlinkability=70,
        implementation_maturity=78,
        operational_resilience=82,
    )

    support_env = DataEnvironmentAssessment(
        data_flow_name="Support Dashboard",
        population_uniqueness=35,
        auxiliary_data_availability=30,
        quasi_identifier_count=40,
        dataset_size_risk=35,
        release_frequency_risk=20,
    )

    support_records = [
        {"country": "CH", "plan": "pro", "ticket_category": "billing"},
        {"country": "CH", "plan": "pro", "ticket_category": "billing"},
        {"country": "CH", "plan": "pro", "ticket_category": "technical"},
        {"country": "DE", "plan": "enterprise", "ticket_category": "technical"},
        {"country": "DE", "plan": "enterprise", "ticket_category": "technical"},
        {"country": "DE", "plan": "enterprise", "ticket_category": "billing"},
    ]

    result2 = run_full_assessment(
        data_flow_name="Support Dashboard",
        technique_assessment=support_technique,
        environment_assessment=support_env,
        records=support_records,
        quasi_identifiers=["country", "plan"],
        auxiliary_data_level="low",
    )

    print(f"\n--- {result2.data_flow_name} ---")
    print(f"Technique: {result2.technique.value}")
    print(f"Technique Score: {result2.technique_score:.1f}/100")
    print(f"Environment Risk: {result2.environment_risk:.1f}/100")
    print(f"Residual Risk: {result2.residual_risk:.1f}/100")
    print(f"Classification: {result2.risk_classification.value}")
    print(f"Prosecutor Risk: {result2.prosecutor_risk:.1f}%")

    # --- Demonstrate pseudonymization engines ---

    print("\n--- Pseudonymization Engine Demonstrations ---")

    # Counter-based
    counter = CounterPseudonymizer()
    email = "anna.mueller@prism-data.ch"
    pseudo_id = counter.pseudonymize(email)
    print(f"\nCounter-based: '{email}' -> '{pseudo_id}'")
    print(f"  De-pseudonymize: '{counter.de_pseudonymize(pseudo_id)}'")
    print(f"  Mapping table size: {counter.mapping_size}")

    # HMAC-based
    hmac_engine = HMACPseudonymizer()
    pseudo_hmac = hmac_engine.pseudonymize(email)
    print(f"\nHMAC-SHA256: '{email}' -> '{pseudo_hmac[:32]}...'")
    print(f"  Key ID: {hmac_engine.key_id}")
    print(f"  Deterministic check: {hmac_engine.pseudonymize(email) == pseudo_hmac}")

    # Tokenization
    vault = TokenVault()
    token = vault.tokenize(email)
    print(f"\nTokenization: '{email}' -> '{token}'")
    print(f"  Detokenize: '{vault.detokenize(token)}'")
    print(f"  Vault size: {vault.vault_size}")
    vault.revoke_token(token)
    print(f"  After revocation, detokenize: {vault.detokenize(token)}")

    # --- Summary table ---
    print("\n" + "=" * 70)
    print("ASSESSMENT SUMMARY — Prism Data Systems AG")
    print("=" * 70)
    print(f"{'Data Flow':<25} {'Technique':<20} {'T.Score':<10} {'Env.Risk':<10} {'Residual':<10} {'Class'}")
    print("-" * 85)
    for r in [result1, result2]:
        print(f"{r.data_flow_name:<25} {r.technique.value:<20} {r.technique_score:<10.1f} {r.environment_risk:<10.1f} {r.residual_risk:<10.1f} {r.risk_classification.value}")


if __name__ == "__main__":
    run_example()
