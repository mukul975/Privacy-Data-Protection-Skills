"""
AI Training Data Classifier
Classifies ML training datasets for GDPR and AI Act compliance.
"""

import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from datetime import date


class TrainingDataClass(Enum):
    PII_DIRECT = "TRAINING_PII_DIRECT"
    PII_INDIRECT = "TRAINING_PII_INDIRECT"
    SPECIAL_CATEGORY = "TRAINING_SPECIAL_CAT"
    CRIMINAL = "TRAINING_CRIMINAL"
    PSEUDONYMISED = "TRAINING_PSEUDONYMISED"
    ANONYMISED = "TRAINING_ANONYMISED"
    SYNTHETIC = "TRAINING_SYNTHETIC"
    NON_PERSONAL = "TRAINING_NON_PERSONAL"


class ConsentScope(Enum):
    COVERS_TRAINING = "consent_covers_training"
    DOES_NOT_COVER = "consent_does_not_cover"
    LEGITIMATE_INTEREST = "legitimate_interest"
    CONTRACT = "contract_performance"
    PUBLIC_DATA = "public_data"
    RESEARCH = "research_exemption"
    NOT_ASSESSED = "not_assessed"


class BiasRiskLevel(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NONE_DETECTED = "none_detected"


@dataclass
class ProxyVariable:
    """A feature that may serve as a proxy for a protected characteristic."""
    feature_name: str
    correlated_characteristic: str
    correlation_strength: float
    detection_method: str
    mitigation_recommendation: str


@dataclass
class DemographicRepresentation:
    """Representation statistics for a demographic group."""
    group_name: str
    dataset_percentage: float
    population_percentage: float
    representation_ratio: float
    under_represented: bool


@dataclass
class BiasAssessment:
    """Bias assessment results for a training dataset."""
    proxy_variables: list[ProxyVariable] = field(default_factory=list)
    demographic_stats: list[DemographicRepresentation] = field(default_factory=list)
    disparate_impact_ratio: float = 0.0
    overall_risk: BiasRiskLevel = BiasRiskLevel.NOT_ASSESSED
    four_fifths_rule_pass: bool = True
    notes: str = ""


@dataclass
class DataCard:
    """GDPR-compliant data card for an ML training dataset."""
    dataset_name: str
    version: str
    creation_date: str
    owner: str
    purpose: str
    data_classification: TrainingDataClass
    data_elements: list[str]
    data_subjects: str
    record_count: int
    geographic_scope: str
    original_collection_purpose: str
    source_systems: list[str]
    consent_scope: ConsentScope
    lawful_basis: str
    art9_condition: str
    de_identification_technique: str
    de_identification_assessment_ref: str
    bias_assessment: BiasAssessment
    retention_period: str
    access_controls: str
    dpia_reference: str
    limitations: list[str]
    ai_act_high_risk: bool = False


class TrainingDataClassifier:
    """
    Classifies AI/ML training datasets for GDPR and AI Act compliance.
    """

    SPECIAL_CATEGORY_FEATURES = {
        "ethnicity", "race", "racial_origin", "ethnic_origin",
        "political_opinion", "political_affiliation", "party_membership",
        "religion", "religious_belief", "faith",
        "trade_union", "union_membership",
        "genetic_marker", "dna", "genotype",
        "biometric", "fingerprint", "facial_embedding",
        "health_status", "diagnosis", "medical_condition", "disability",
        "sexual_orientation", "gender_identity",
    }

    PROXY_INDICATORS = {
        "postcode": ("racial_ethnic_origin", "Geographic demographics correlate with ethnic composition"),
        "zip_code": ("racial_ethnic_origin", "Geographic demographics correlate with ethnic composition"),
        "first_name": ("gender_ethnic_origin", "Names correlate with gender and ethnic background"),
        "language": ("ethnic_origin", "Language preference correlates with ethnic background"),
        "credit_score": ("racial_ethnic_origin", "Credit scores show documented racial disparities"),
        "employment_gap": ("gender_disability", "Employment gaps correlate with maternity and disability"),
        "marital_status": ("sexual_orientation", "Marital status may indicate sexual orientation"),
    }

    def classify_dataset(
        self,
        features: list[str],
        contains_direct_identifiers: bool,
        contains_indirect_identifiers: bool,
        re_identification_key_exists: bool,
        is_synthetic: bool,
        is_anonymised_verified: bool,
    ) -> TrainingDataClass:
        """Classify a training dataset based on its personal data content."""
        if is_synthetic:
            return TrainingDataClass.SYNTHETIC

        if is_anonymised_verified:
            return TrainingDataClass.ANONYMISED

        has_special = any(
            f.lower() in self.SPECIAL_CATEGORY_FEATURES for f in features
        )

        if has_special:
            return TrainingDataClass.SPECIAL_CATEGORY

        if contains_direct_identifiers:
            return TrainingDataClass.PII_DIRECT

        if contains_indirect_identifiers:
            if re_identification_key_exists:
                return TrainingDataClass.PSEUDONYMISED
            return TrainingDataClass.PII_INDIRECT

        return TrainingDataClass.NON_PERSONAL

    def detect_proxy_variables(self, features: list[str]) -> list[ProxyVariable]:
        """Detect features that may serve as proxies for protected characteristics."""
        proxies = []
        for feature in features:
            feature_lower = feature.lower()
            for proxy_key, (characteristic, description) in self.PROXY_INDICATORS.items():
                if proxy_key in feature_lower:
                    proxies.append(ProxyVariable(
                        feature_name=feature,
                        correlated_characteristic=characteristic,
                        correlation_strength=0.35,
                        detection_method="keyword_matching",
                        mitigation_recommendation=(
                            f"Consider removing '{feature}' or applying fairness "
                            f"constraints during training to mitigate {characteristic} proxy effect"
                        ),
                    ))
        return proxies

    def assess_demographic_representation(
        self, dataset_demographics: dict[str, float], population_demographics: dict[str, float]
    ) -> list[DemographicRepresentation]:
        """Compare dataset demographics to target population."""
        stats = []
        for group, pop_pct in population_demographics.items():
            ds_pct = dataset_demographics.get(group, 0.0)
            ratio = ds_pct / pop_pct if pop_pct > 0 else 0.0
            stats.append(DemographicRepresentation(
                group_name=group,
                dataset_percentage=ds_pct,
                population_percentage=pop_pct,
                representation_ratio=round(ratio, 2),
                under_represented=ratio < 0.8,
            ))
        return stats

    def assess_bias(
        self,
        features: list[str],
        dataset_demographics: dict[str, float] | None = None,
        population_demographics: dict[str, float] | None = None,
        selection_rates: dict[str, float] | None = None,
    ) -> BiasAssessment:
        """Run comprehensive bias assessment on training dataset."""
        proxy_vars = self.detect_proxy_variables(features)

        demo_stats = []
        if dataset_demographics and population_demographics:
            demo_stats = self.assess_demographic_representation(
                dataset_demographics, population_demographics
            )

        four_fifths_pass = True
        di_ratio = 1.0
        if selection_rates and len(selection_rates) >= 2:
            max_rate = max(selection_rates.values())
            min_rate = min(selection_rates.values())
            di_ratio = min_rate / max_rate if max_rate > 0 else 0
            four_fifths_pass = di_ratio >= 0.8

        if not four_fifths_pass:
            risk = BiasRiskLevel.HIGH
        elif proxy_vars or any(d.under_represented for d in demo_stats):
            risk = BiasRiskLevel.MEDIUM
        else:
            risk = BiasRiskLevel.LOW

        return BiasAssessment(
            proxy_variables=proxy_vars,
            demographic_stats=demo_stats,
            disparate_impact_ratio=round(di_ratio, 2),
            overall_risk=risk,
            four_fifths_rule_pass=four_fifths_pass,
        )

    def generate_data_card(
        self,
        dataset_name: str,
        features: list[str],
        classification: TrainingDataClass,
        bias_assessment: BiasAssessment,
        record_count: int,
        purpose: str,
        source_systems: list[str],
        consent_scope: ConsentScope,
        lawful_basis: str,
    ) -> DataCard:
        """Generate a GDPR-compliant data card."""
        return DataCard(
            dataset_name=dataset_name,
            version="1.0",
            creation_date=date.today().isoformat(),
            owner="ML Engineering Team",
            purpose=purpose,
            data_classification=classification,
            data_elements=features,
            data_subjects="Vanguard customers",
            record_count=record_count,
            geographic_scope="United Kingdom",
            original_collection_purpose="Financial services delivery",
            source_systems=source_systems,
            consent_scope=consent_scope,
            lawful_basis=lawful_basis,
            art9_condition="N/A" if classification != TrainingDataClass.SPECIAL_CATEGORY else "Art. 9(2)(j) Research",
            de_identification_technique="Pseudonymisation (tokenisation of customer IDs)",
            de_identification_assessment_ref="ANON-2026-ML-001",
            bias_assessment=bias_assessment,
            retention_period="Duration of model lifecycle + 1 year",
            access_controls="ML team (5 persons) via Vanguard ML Platform with audit logging",
            dpia_reference="DPIA-ML-2026-001",
            limitations=[
                "Dataset covers UK customers only — model should not be applied to non-UK populations",
                "Temporal coverage: 2023-2025 — may not reflect post-2025 market conditions",
                "Proxy variable 'postcode' present — fairness constraints required during training",
            ],
        )


def run_vanguard_example():
    """Demonstrate training data classification for Vanguard Financial Services."""
    classifier = TrainingDataClassifier()

    features = [
        "customer_token", "age_band", "postcode", "account_tenure_months",
        "transaction_count_30d", "avg_transaction_amount", "product_holdings",
        "channel_preference", "complaint_flag", "credit_score",
        "churn_label",
    ]

    classification = classifier.classify_dataset(
        features=features,
        contains_direct_identifiers=False,
        contains_indirect_identifiers=True,
        re_identification_key_exists=True,
        is_synthetic=False,
        is_anonymised_verified=False,
    )

    bias = classifier.assess_bias(
        features=features,
        dataset_demographics={
            "White British": 72.0, "Asian": 10.5, "Black": 5.2,
            "Mixed": 3.8, "Other": 8.5,
        },
        population_demographics={
            "White British": 81.7, "Asian": 7.5, "Black": 3.3,
            "Mixed": 2.2, "Other": 5.3,
        },
        selection_rates={
            "White British": 0.85, "Asian": 0.78, "Black": 0.71,
            "Mixed": 0.82, "Other": 0.76,
        },
    )

    data_card = classifier.generate_data_card(
        dataset_name="Customer Churn Prediction Training Set v2.1",
        features=features,
        classification=classification,
        bias_assessment=bias,
        record_count=1_500_000,
        purpose="Train churn prediction model to identify customers at risk of leaving",
        source_systems=["Salesforce CRM", "Oracle Data Warehouse"],
        consent_scope=ConsentScope.LEGITIMATE_INTEREST,
        lawful_basis="Art. 6(1)(f) — Legitimate interests (improving customer retention)",
    )

    print("=" * 70)
    print("VANGUARD FINANCIAL SERVICES — AI TRAINING DATA CLASSIFICATION")
    print("=" * 70)
    print(f"\nDataset: {data_card.dataset_name}")
    print(f"Classification: {classification.value}")
    print(f"Records: {data_card.record_count:,}")
    print(f"Lawful Basis: {data_card.lawful_basis}")
    print(f"Consent Scope: {data_card.consent_scope.value}")

    print(f"\nBIAS ASSESSMENT:")
    print(f"  Overall Risk: {bias.overall_risk.value}")
    print(f"  Four-Fifths Rule: {'PASS' if bias.four_fifths_rule_pass else 'FAIL'}")
    print(f"  Disparate Impact Ratio: {bias.disparate_impact_ratio}")
    print(f"  Proxy Variables: {len(bias.proxy_variables)}")
    for pv in bias.proxy_variables:
        print(f"    - {pv.feature_name} → {pv.correlated_characteristic}")
    print(f"  Under-represented Groups:")
    for ds in bias.demographic_stats:
        if ds.under_represented:
            print(f"    - {ds.group_name}: {ds.dataset_percentage}% vs {ds.population_percentage}% population")

    print(f"\nLIMITATIONS:")
    for lim in data_card.limitations:
        print(f"  - {lim}")


if __name__ == "__main__":
    run_vanguard_example()
