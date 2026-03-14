"""
AI/ML Training Data Classification Engine
Classifies training datasets for privacy compliance, bias risk, and provenance.
"""

import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from datetime import date
from collections import Counter


class PrivacyClassification(Enum):
    PERSONAL_DIRECT = "personal_direct"
    PERSONAL_INDIRECT = "personal_indirect"
    SPECIAL_CATEGORY = "special_category"
    CRIMINAL_DATA = "criminal_data"
    PSEUDONYMISED = "pseudonymised"
    ANONYMISED = "anonymised"
    NON_PERSONAL = "non_personal"


class BiasRiskLevel(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NONE = "none"


class ProvenanceType(Enum):
    FIRST_PARTY = "first_party_collected"
    THIRD_PARTY = "third_party_sourced"
    PUBLIC_DATA = "public_data"
    SYNTHETIC = "synthetic_data"
    MIXED = "mixed_sources"


class ConsentStatus(Enum):
    CONSENT_OBTAINED = "explicit_consent_for_training"
    COMPATIBLE_PURPOSE = "compatible_with_original_purpose"
    LEGITIMATE_INTEREST = "legitimate_interest_assessed"
    NOT_REQUIRED = "no_personal_data"
    UNKNOWN = "consent_status_unknown"
    NOT_OBTAINED = "consent_not_obtained"


@dataclass
class FeatureClassification:
    """Privacy classification for a single training feature."""
    feature_name: str
    data_type: str
    privacy_class: PrivacyClassification
    is_art9_direct: bool = False
    is_art9_proxy: bool = False
    proxy_for: str = ""
    proxy_correlation: float = 0.0
    necessary_for_model: bool = True
    can_be_pseudonymised: bool = False
    can_be_removed: bool = False
    notes: str = ""


@dataclass
class FairnessMetric:
    """A fairness metric measurement for a protected group."""
    metric_name: str
    group_a: str
    group_b: str
    group_a_value: float
    group_b_value: float
    ratio: float
    passes_threshold: bool
    threshold: str


@dataclass
class DataCard:
    """Data card documentation for an ML training dataset."""
    dataset_name: str
    version: str
    created_date: str
    owner: str
    purpose: str
    record_count: int
    feature_count: int
    temporal_coverage: str
    feature_classifications: list[FeatureClassification]
    provenance: ProvenanceType
    provenance_details: str
    consent_status: ConsentStatus
    lawful_basis: str
    art9_condition: str
    bias_risk: BiasRiskLevel
    fairness_metrics: list[FairnessMetric]
    quality_score: float
    known_limitations: list[str]
    dpia_reference: str
    retention_period: str
    review_date: str

    @property
    def contains_personal_data(self) -> bool:
        return any(
            fc.privacy_class not in (PrivacyClassification.NON_PERSONAL, PrivacyClassification.ANONYMISED)
            for fc in self.feature_classifications
        )

    @property
    def contains_special_category(self) -> bool:
        return any(
            fc.is_art9_direct or fc.is_art9_proxy
            for fc in self.feature_classifications
        )

    @property
    def removable_features(self) -> list[str]:
        return [fc.feature_name for fc in self.feature_classifications if fc.can_be_removed]


class TrainingDataClassifier:
    """
    Classifies ML training dataset features for privacy compliance.
    """

    PROTECTED_ATTRIBUTE_PATTERNS = {
        "racial_ethnic": ["ethnicity", "race", "nationality", "country_of_origin", "skin_color"],
        "gender": ["gender", "sex", "male_female"],
        "age": ["age", "date_of_birth", "birth_year", "birth_date"],
        "religion": ["religion", "faith", "denomination"],
        "disability": ["disability", "handicap", "impairment"],
        "sexual_orientation": ["sexual_orientation", "partner_gender"],
        "political": ["political_party", "political_affiliation", "voting"],
    }

    KNOWN_PROXIES = {
        "postcode": {"proxy_for": "racial_ethnic", "typical_correlation": 0.65},
        "zip_code": {"proxy_for": "racial_ethnic", "typical_correlation": 0.65},
        "surname": {"proxy_for": "racial_ethnic", "typical_correlation": 0.55},
        "language_preference": {"proxy_for": "racial_ethnic", "typical_correlation": 0.60},
        "graduation_year": {"proxy_for": "age", "typical_correlation": 0.90},
        "years_experience": {"proxy_for": "age", "typical_correlation": 0.85},
        "dietary_preference": {"proxy_for": "religion", "typical_correlation": 0.40},
        "household_size": {"proxy_for": "racial_ethnic", "typical_correlation": 0.35},
        "insurance_claims": {"proxy_for": "disability", "typical_correlation": 0.50},
    }

    def classify_feature(self, feature_name: str, data_type: str, description: str = "") -> FeatureClassification:
        """Classify a single training feature for privacy risk."""
        feature_lower = feature_name.lower()
        desc_lower = description.lower()
        combined = f"{feature_lower} {desc_lower}"

        # Check for direct Art. 9 attributes
        for category, patterns in self.PROTECTED_ATTRIBUTE_PATTERNS.items():
            if any(p in combined for p in patterns):
                return FeatureClassification(
                    feature_name=feature_name,
                    data_type=data_type,
                    privacy_class=PrivacyClassification.SPECIAL_CATEGORY,
                    is_art9_direct=True,
                    proxy_for=category,
                    can_be_removed=True,
                    notes=f"Direct Art. 9 attribute: {category}",
                )

        # Check for known proxies
        if feature_lower in self.KNOWN_PROXIES:
            proxy_info = self.KNOWN_PROXIES[feature_lower]
            return FeatureClassification(
                feature_name=feature_name,
                data_type=data_type,
                privacy_class=PrivacyClassification.PERSONAL_INDIRECT,
                is_art9_proxy=True,
                proxy_for=proxy_info["proxy_for"],
                proxy_correlation=proxy_info["typical_correlation"],
                can_be_pseudonymised=True,
                notes=f"Known proxy for {proxy_info['proxy_for']} "
                      f"(typical correlation: {proxy_info['typical_correlation']:.0%})",
            )

        # Check for direct identifiers
        direct_id_patterns = ["name", "email", "phone", "ssn", "nino", "passport", "address"]
        if any(p in combined for p in direct_id_patterns):
            return FeatureClassification(
                feature_name=feature_name,
                data_type=data_type,
                privacy_class=PrivacyClassification.PERSONAL_DIRECT,
                can_be_removed=True,
                can_be_pseudonymised=True,
                notes="Direct identifier — should be removed or pseudonymised for training",
            )

        # Check for indirect identifiers
        indirect_patterns = ["customer_id", "account_id", "employee_id", "user_id", "ip_address"]
        if any(p in combined for p in indirect_patterns):
            return FeatureClassification(
                feature_name=feature_name,
                data_type=data_type,
                privacy_class=PrivacyClassification.PERSONAL_INDIRECT,
                can_be_pseudonymised=True,
                notes="Indirect identifier — consider pseudonymisation",
            )

        return FeatureClassification(
            feature_name=feature_name,
            data_type=data_type,
            privacy_class=PrivacyClassification.NON_PERSONAL,
            notes="No personal data indicators detected",
        )

    def assess_demographic_parity(
        self,
        group_a_positive_rate: float,
        group_b_positive_rate: float,
        group_a_name: str = "Group A",
        group_b_name: str = "Group B",
    ) -> FairnessMetric:
        """Calculate demographic parity (80% rule)."""
        ratio = (
            group_a_positive_rate / group_b_positive_rate
            if group_b_positive_rate > 0
            else 0.0
        )
        passes = 0.8 <= ratio <= 1.25

        return FairnessMetric(
            metric_name="Demographic Parity",
            group_a=group_a_name,
            group_b=group_b_name,
            group_a_value=round(group_a_positive_rate, 4),
            group_b_value=round(group_b_positive_rate, 4),
            ratio=round(ratio, 4),
            passes_threshold=passes,
            threshold="Ratio within 0.8-1.25 (80% rule)",
        )

    def classify_dataset(
        self,
        dataset_name: str,
        features: list[dict],
        record_count: int,
        provenance: ProvenanceType,
        purpose: str,
    ) -> DataCard:
        """
        Classify an entire training dataset and generate a data card.

        Args:
            dataset_name: Name of the dataset
            features: List of dicts with keys: name, data_type, description
            record_count: Number of records
            provenance: Data provenance type
            purpose: Purpose of the training
        """
        classifications = []
        for f in features:
            fc = self.classify_feature(f["name"], f.get("data_type", ""), f.get("description", ""))
            classifications.append(fc)

        has_personal = any(
            fc.privacy_class not in (PrivacyClassification.NON_PERSONAL, PrivacyClassification.ANONYMISED)
            for fc in classifications
        )
        has_art9 = any(fc.is_art9_direct or fc.is_art9_proxy for fc in classifications)

        if has_art9:
            bias_risk = BiasRiskLevel.HIGH
        elif has_personal:
            bias_risk = BiasRiskLevel.MEDIUM
        else:
            bias_risk = BiasRiskLevel.LOW

        consent = ConsentStatus.NOT_REQUIRED if not has_personal else ConsentStatus.UNKNOWN
        lawful_basis = "" if not has_personal else "Art. 6(1)(f) — Legitimate interests (assessment required)"
        art9_cond = "" if not has_art9 else "Art. 10(5) EU AI Act (bias monitoring) or Art. 9(2)(j) (research)"

        limitations = []
        if has_art9:
            limitations.append("Contains features correlated with Art. 9 protected categories — bias risk")
        removable = [fc.feature_name for fc in classifications if fc.can_be_removed]
        if removable:
            limitations.append(f"Features recommended for removal: {', '.join(removable)}")

        today = date.today()
        return DataCard(
            dataset_name=dataset_name,
            version="1.0",
            created_date=today.isoformat(),
            owner="Data Science Team",
            purpose=purpose,
            record_count=record_count,
            feature_count=len(features),
            temporal_coverage="",
            feature_classifications=classifications,
            provenance=provenance,
            provenance_details="",
            consent_status=consent,
            lawful_basis=lawful_basis,
            art9_condition=art9_cond,
            bias_risk=bias_risk,
            fairness_metrics=[],
            quality_score=0.0,
            known_limitations=limitations,
            dpia_reference="",
            retention_period="Duration of model lifecycle + 1 year",
            review_date=today.replace(year=today.year + 1).isoformat(),
        )


def run_vanguard_example():
    """Demonstrate training data classification for Vanguard credit risk model."""
    classifier = TrainingDataClassifier()

    features = [
        {"name": "customer_name", "data_type": "string", "description": "Customer full name"},
        {"name": "customer_id", "data_type": "string", "description": "Unique customer identifier"},
        {"name": "age", "data_type": "integer", "description": "Customer age in years"},
        {"name": "postcode", "data_type": "string", "description": "Customer residential postcode"},
        {"name": "annual_income", "data_type": "float", "description": "Annual gross income in GBP"},
        {"name": "employment_years", "data_type": "float", "description": "Years in current employment"},
        {"name": "credit_utilisation", "data_type": "float", "description": "Percentage of credit limit used"},
        {"name": "payment_history_score", "data_type": "integer", "description": "Score based on payment history"},
        {"name": "num_credit_accounts", "data_type": "integer", "description": "Number of active credit accounts"},
        {"name": "loan_amount", "data_type": "float", "description": "Requested loan amount in GBP"},
        {"name": "default_flag", "data_type": "boolean", "description": "Whether the customer defaulted (label)"},
    ]

    data_card = classifier.classify_dataset(
        dataset_name="Credit Risk Training Dataset v2.1",
        features=features,
        record_count=450000,
        provenance=ProvenanceType.FIRST_PARTY,
        purpose="Train credit risk scoring model for loan approval decisions",
    )

    print("=" * 70)
    print("VANGUARD FINANCIAL SERVICES — TRAINING DATA CLASSIFICATION")
    print(f"Dataset: {data_card.dataset_name}")
    print("=" * 70)

    print(f"\nRecords: {data_card.record_count:,}")
    print(f"Features: {data_card.feature_count}")
    print(f"Contains personal data: {data_card.contains_personal_data}")
    print(f"Contains Art. 9 risk: {data_card.contains_special_category}")
    print(f"Bias risk: {data_card.bias_risk.value}")

    print("\nFeature Classifications:")
    for fc in data_card.feature_classifications:
        status = fc.privacy_class.value
        flags = []
        if fc.is_art9_direct:
            flags.append("ART9-DIRECT")
        if fc.is_art9_proxy:
            flags.append(f"ART9-PROXY({fc.proxy_for})")
        if fc.can_be_removed:
            flags.append("REMOVE")
        if fc.can_be_pseudonymised:
            flags.append("PSEUDONYMISE")
        flag_str = f" [{', '.join(flags)}]" if flags else ""
        print(f"  {fc.feature_name:30s} {status:20s}{flag_str}")

    if data_card.known_limitations:
        print("\nKnown Limitations:")
        for lim in data_card.known_limitations:
            print(f"  - {lim}")

    # Fairness assessment
    print(f"\n{'='*70}")
    print("FAIRNESS ASSESSMENT (Demographic Parity)")
    metric = classifier.assess_demographic_parity(
        group_a_positive_rate=0.12,
        group_b_positive_rate=0.15,
        group_a_name="Postcode Group A (urban)",
        group_b_name="Postcode Group B (rural)",
    )
    print(f"  {metric.group_a}: {metric.group_a_value:.1%} positive rate")
    print(f"  {metric.group_b}: {metric.group_b_value:.1%} positive rate")
    print(f"  Ratio: {metric.ratio:.2f} (threshold: {metric.threshold})")
    print(f"  Passes: {metric.passes_threshold}")


if __name__ == "__main__":
    run_vanguard_example()
