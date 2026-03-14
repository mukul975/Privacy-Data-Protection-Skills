"""
Cross-Jurisdiction Data Classification Engine
Maps data elements across GDPR, CCPA, HIPAA, and LGPD frameworks.
"""

import json
from dataclasses import dataclass, field
from enum import Enum
from datetime import date


class Jurisdiction(Enum):
    GDPR = "GDPR (EU/UK)"
    CCPA = "CCPA/CPRA (California)"
    HIPAA = "HIPAA (US)"
    LGPD = "LGPD (Brazil)"
    VCDPA = "VCDPA (Virginia)"


class SensitivityLevel(Enum):
    NOT_APPLICABLE = "not_applicable"
    NON_PERSONAL = "non_personal"
    PERSONAL = "personal"
    SENSITIVE = "sensitive"


class UnifiedTier(Enum):
    PUBLIC = "Public"
    INTERNAL = "Internal"
    CONFIDENTIAL = "Confidential"
    RESTRICTED = "Restricted"


SENSITIVITY_TO_TIER = {
    SensitivityLevel.NOT_APPLICABLE: UnifiedTier.PUBLIC,
    SensitivityLevel.NON_PERSONAL: UnifiedTier.PUBLIC,
    SensitivityLevel.PERSONAL: UnifiedTier.CONFIDENTIAL,
    SensitivityLevel.SENSITIVE: UnifiedTier.RESTRICTED,
}

TIER_RANK = {
    UnifiedTier.PUBLIC: 0,
    UnifiedTier.INTERNAL: 1,
    UnifiedTier.CONFIDENTIAL: 2,
    UnifiedTier.RESTRICTED: 3,
}


@dataclass
class JurisdictionalClassification:
    jurisdiction: Jurisdiction
    sensitivity: SensitivityLevel
    category_name: str
    legal_reference: str
    processing_condition: str = ""
    consumer_right: str = ""


@dataclass
class CrossJurisdictionResult:
    data_element: str
    classifications: list[JurisdictionalClassification]
    unified_tier: UnifiedTier
    most_restrictive_jurisdiction: str
    applicable_jurisdictions: list[str]
    notes: str = ""


DATA_CATEGORY_MAP: dict[str, dict[str, tuple[SensitivityLevel, str, str]]] = {
    "racial_ethnic_origin": {
        "GDPR": (SensitivityLevel.SENSITIVE, "Art. 9 special category", "Art. 9(2)(a)-(j)"),
        "CCPA": (SensitivityLevel.SENSITIVE, "Sensitive PI §1798.140(ae)(1)", "Right to limit §1798.121"),
        "HIPAA": (SensitivityLevel.NOT_APPLICABLE, "N/A unless health-related", ""),
        "LGPD": (SensitivityLevel.SENSITIVE, "Art. 5-II sensitive", "Art. 11 specific consent"),
    },
    "health_data": {
        "GDPR": (SensitivityLevel.SENSITIVE, "Art. 9 special category (Recital 35)", "Art. 9(2)(h)-(i)"),
        "CCPA": (SensitivityLevel.SENSITIVE, "Sensitive PI §1798.140(ae)(2)", "Right to limit §1798.121"),
        "HIPAA": (SensitivityLevel.SENSITIVE, "PHI §160.103", "Minimum necessary §164.502(b)"),
        "LGPD": (SensitivityLevel.SENSITIVE, "Art. 5-II sensitive", "Art. 11 specific consent"),
    },
    "biometric_data": {
        "GDPR": (SensitivityLevel.SENSITIVE, "Art. 9 (for unique identification)", "Art. 9(2)(a)"),
        "CCPA": (SensitivityLevel.SENSITIVE, "Sensitive PI §1798.140(ae)(3)", "Right to limit §1798.121"),
        "HIPAA": (SensitivityLevel.SENSITIVE, "PHI identifier §164.514(b)", "Minimum necessary"),
        "LGPD": (SensitivityLevel.SENSITIVE, "Art. 5-II sensitive", "Art. 11 specific consent"),
    },
    "genetic_data": {
        "GDPR": (SensitivityLevel.SENSITIVE, "Art. 9 special category (Art. 4(13))", "Art. 9(2)"),
        "CCPA": (SensitivityLevel.SENSITIVE, "Sensitive PI §1798.140(ae)(4)", "Right to limit §1798.121"),
        "HIPAA": (SensitivityLevel.SENSITIVE, "PHI if health-related", "Minimum necessary; GINA"),
        "LGPD": (SensitivityLevel.SENSITIVE, "Art. 5-II sensitive", "Art. 11 specific consent"),
    },
    "ssn_government_id": {
        "GDPR": (SensitivityLevel.PERSONAL, "Art. 4(1) personal data (direct identifier)", "Art. 87 national ID"),
        "CCPA": (SensitivityLevel.SENSITIVE, "Sensitive PI §1798.140(ae)(1)", "Right to limit §1798.121"),
        "HIPAA": (SensitivityLevel.SENSITIVE, "PHI identifier §164.514(b)(2)(i)", "Minimum necessary"),
        "LGPD": (SensitivityLevel.PERSONAL, "Art. 5-I personal data", "Art. 7 lawful basis"),
    },
    "precise_geolocation": {
        "GDPR": (SensitivityLevel.PERSONAL, "Art. 4(1) personal data (location data)", "Art. 6 lawful basis"),
        "CCPA": (SensitivityLevel.SENSITIVE, "Sensitive PI §1798.140(ae)(8)", "Right to limit §1798.121"),
        "HIPAA": (SensitivityLevel.NOT_APPLICABLE, "N/A unless health context", ""),
        "LGPD": (SensitivityLevel.PERSONAL, "Art. 5-I personal data", "Art. 7 lawful basis"),
    },
    "email_address": {
        "GDPR": (SensitivityLevel.PERSONAL, "Art. 4(1) personal data (direct identifier)", "Art. 6"),
        "CCPA": (SensitivityLevel.PERSONAL, "PI §1798.140(o)(1)(A)", "Access/deletion rights"),
        "HIPAA": (SensitivityLevel.SENSITIVE, "PHI identifier §164.514(b)(2)(vii)", "Minimum necessary"),
        "LGPD": (SensitivityLevel.PERSONAL, "Art. 5-I personal data", "Art. 7"),
    },
    "customer_name": {
        "GDPR": (SensitivityLevel.PERSONAL, "Art. 4(1) personal data", "Art. 6"),
        "CCPA": (SensitivityLevel.PERSONAL, "PI §1798.140(o)(1)(A)", "Access/deletion rights"),
        "HIPAA": (SensitivityLevel.SENSITIVE, "PHI identifier §164.514(b)(2)(i)", "Minimum necessary"),
        "LGPD": (SensitivityLevel.PERSONAL, "Art. 5-I personal data", "Art. 7"),
    },
    "aggregate_statistics": {
        "GDPR": (SensitivityLevel.NON_PERSONAL, "Anonymised (Recital 26)", ""),
        "CCPA": (SensitivityLevel.NON_PERSONAL, "Aggregate consumer information §1798.140(b)", ""),
        "HIPAA": (SensitivityLevel.NON_PERSONAL, "De-identified §164.514", ""),
        "LGPD": (SensitivityLevel.NON_PERSONAL, "Anonymised (Art. 12)", ""),
    },
}


class CrossJurisdictionClassifier:
    """Maps data elements across regulatory frameworks and assigns unified classification."""

    def classify(
        self,
        data_element: str,
        data_category: str,
        applicable_jurisdictions: list[str],
    ) -> CrossJurisdictionResult:
        """
        Classify a data element across specified jurisdictions.

        Args:
            data_element: Name of the data element
            data_category: Category key from DATA_CATEGORY_MAP
            applicable_jurisdictions: List of jurisdiction keys (GDPR, CCPA, HIPAA, LGPD)
        """
        category_data = DATA_CATEGORY_MAP.get(data_category, {})
        classifications = []
        highest_tier = UnifiedTier.PUBLIC
        most_restrictive = ""

        jurisdiction_enum_map = {
            "GDPR": Jurisdiction.GDPR,
            "CCPA": Jurisdiction.CCPA,
            "HIPAA": Jurisdiction.HIPAA,
            "LGPD": Jurisdiction.LGPD,
        }

        for jur_key in applicable_jurisdictions:
            jur_enum = jurisdiction_enum_map.get(jur_key)
            if not jur_enum:
                continue

            if jur_key in category_data:
                sensitivity, category_name, condition = category_data[jur_key]
            else:
                sensitivity = SensitivityLevel.NOT_APPLICABLE
                category_name = "Not covered"
                condition = ""

            classifications.append(JurisdictionalClassification(
                jurisdiction=jur_enum,
                sensitivity=sensitivity,
                category_name=category_name,
                legal_reference=category_name,
                processing_condition=condition,
            ))

            tier = SENSITIVITY_TO_TIER.get(sensitivity, UnifiedTier.CONFIDENTIAL)
            if TIER_RANK[tier] > TIER_RANK[highest_tier]:
                highest_tier = tier
                most_restrictive = jur_enum.value

        return CrossJurisdictionResult(
            data_element=data_element,
            classifications=classifications,
            unified_tier=highest_tier,
            most_restrictive_jurisdiction=most_restrictive,
            applicable_jurisdictions=applicable_jurisdictions,
        )

    def generate_mapping_report(
        self,
        results: list[CrossJurisdictionResult],
    ) -> dict:
        """Generate a cross-jurisdiction mapping report."""
        tier_counts: dict[str, int] = {}
        jur_counts: dict[str, int] = {}

        for r in results:
            tier = r.unified_tier.value
            tier_counts[tier] = tier_counts.get(tier, 0) + 1
            if r.most_restrictive_jurisdiction:
                jur_counts[r.most_restrictive_jurisdiction] = (
                    jur_counts.get(r.most_restrictive_jurisdiction, 0) + 1
                )

        return {
            "report_date": date.today().isoformat(),
            "total_elements": len(results),
            "by_unified_tier": tier_counts,
            "most_restrictive_by_jurisdiction": jur_counts,
        }


def run_vanguard_example():
    """Demonstrate cross-jurisdiction classification."""
    classifier = CrossJurisdictionClassifier()

    elements = [
        ("employee_ethnicity", "racial_ethnic_origin", ["GDPR", "CCPA", "LGPD"]),
        ("customer_health_record", "health_data", ["GDPR", "CCPA", "HIPAA", "LGPD"]),
        ("fingerprint_template", "biometric_data", ["GDPR", "CCPA", "LGPD"]),
        ("social_security_number", "ssn_government_id", ["GDPR", "CCPA", "HIPAA"]),
        ("customer_gps_location", "precise_geolocation", ["GDPR", "CCPA", "LGPD"]),
        ("customer_email", "email_address", ["GDPR", "CCPA", "HIPAA", "LGPD"]),
        ("website_traffic_aggregate", "aggregate_statistics", ["GDPR", "CCPA", "LGPD"]),
    ]

    print("=" * 70)
    print("VANGUARD FINANCIAL SERVICES — CROSS-JURISDICTION CLASSIFICATION")
    print("=" * 70)

    results = []
    for name, category, jurisdictions in elements:
        result = classifier.classify(name, category, jurisdictions)
        results.append(result)
        print(f"\n  {result.data_element}:")
        print(f"    Unified Tier: {result.unified_tier.value}")
        print(f"    Most Restrictive: {result.most_restrictive_jurisdiction}")
        for c in result.classifications:
            print(f"    {c.jurisdiction.value}: {c.sensitivity.value} — {c.category_name}")

    report = classifier.generate_mapping_report(results)
    print(f"\n{'='*70}")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    run_vanguard_example()
