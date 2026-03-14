"""
Anonymization as Retention Alternative Process
Implements k-anonymity, l-diversity, and t-closeness validation for anonymized datasets.
"""

import json
import math
from collections import Counter
from datetime import datetime
from typing import Optional


class AnonymizationTechnique:
    """Represents an anonymization technique with its properties."""

    def __init__(self, name: str, category: str, singling_out: str, linkability: str, inference: str):
        self.name = name
        self.category = category
        self.singling_out = singling_out
        self.linkability = linkability
        self.inference = inference

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "category": self.category,
            "singling_out_mitigation": self.singling_out,
            "linkability_mitigation": self.linkability,
            "inference_mitigation": self.inference,
        }


# WP29 Opinion 05/2014 technique catalog
WP29_TECHNIQUES = [
    AnonymizationTechnique("Noise addition", "Randomization", "Partial", "Partial", "Mitigates"),
    AnonymizationTechnique("Permutation", "Randomization", "Partial", "Mitigates", "Partial"),
    AnonymizationTechnique("Differential privacy", "Randomization", "Mitigates", "Mitigates", "Mitigates"),
    AnonymizationTechnique("Aggregation", "Generalization", "Mitigates", "Mitigates", "Partial"),
    AnonymizationTechnique("K-anonymity", "Generalization", "Mitigates", "Partial", "Does not mitigate"),
    AnonymizationTechnique("L-diversity", "Generalization", "Mitigates", "Partial", "Partial"),
    AnonymizationTechnique("T-closeness", "Generalization", "Mitigates", "Partial", "Mitigates"),
    AnonymizationTechnique("Top/bottom coding", "Generalization", "Partial", "Partial", "Partial"),
    AnonymizationTechnique("Data masking", "Generalization", "Mitigates", "Partial", "Partial"),
    AnonymizationTechnique("Record suppression", "Suppression", "Eliminates", "N/A", "N/A"),
    AnonymizationTechnique("Attribute suppression", "Suppression", "N/A", "Eliminates", "N/A"),
    AnonymizationTechnique("Cell suppression", "Suppression", "Targeted", "Partial", "Partial"),
]


def check_k_anonymity(
    dataset: list[dict],
    quasi_identifiers: list[str],
    k: int,
) -> dict:
    """
    Check if a dataset satisfies k-anonymity.
    Each combination of quasi-identifiers must appear in at least k records.
    """
    equivalence_classes: dict[tuple, int] = Counter()
    for record in dataset:
        key = tuple(record.get(qi, None) for qi in quasi_identifiers)
        equivalence_classes[key] += 1

    violations = {str(k_val): v for k_val, v in equivalence_classes.items() if v < k}
    min_class_size = min(equivalence_classes.values()) if equivalence_classes else 0
    total_classes = len(equivalence_classes)

    return {
        "k_target": k,
        "satisfied": len(violations) == 0,
        "total_equivalence_classes": total_classes,
        "min_class_size": min_class_size,
        "violations": len(violations),
        "violation_details": violations if len(violations) <= 10 else f"{len(violations)} violations (showing first 10)",
        "quasi_identifiers": quasi_identifiers,
    }


def check_l_diversity(
    dataset: list[dict],
    quasi_identifiers: list[str],
    sensitive_attribute: str,
    l_value: int,
) -> dict:
    """
    Check if a dataset satisfies l-diversity.
    Each equivalence class must have at least l distinct values for the sensitive attribute.
    """
    equivalence_classes: dict[tuple, set] = {}
    for record in dataset:
        key = tuple(record.get(qi, None) for qi in quasi_identifiers)
        if key not in equivalence_classes:
            equivalence_classes[key] = set()
        equivalence_classes[key].add(record.get(sensitive_attribute))

    violations = {}
    min_diversity = float("inf")
    for key, values in equivalence_classes.items():
        diversity = len(values)
        if diversity < min_diversity:
            min_diversity = diversity
        if diversity < l_value:
            violations[str(key)] = diversity

    return {
        "l_target": l_value,
        "sensitive_attribute": sensitive_attribute,
        "satisfied": len(violations) == 0,
        "total_equivalence_classes": len(equivalence_classes),
        "min_diversity": min_diversity if min_diversity != float("inf") else 0,
        "violations": len(violations),
    }


def check_t_closeness(
    dataset: list[dict],
    quasi_identifiers: list[str],
    sensitive_attribute: str,
    t_threshold: float,
) -> dict:
    """
    Check if a dataset satisfies t-closeness.
    The distribution of the sensitive attribute within each equivalence class
    must be close to the overall distribution (Earth Mover's Distance <= t).
    """
    # Compute overall distribution
    overall_values = [record.get(sensitive_attribute) for record in dataset]
    overall_counter = Counter(overall_values)
    total = len(overall_values)
    overall_dist = {k: v / total for k, v in overall_counter.items()}

    # Compute per-class distributions
    equivalence_classes: dict[tuple, list] = {}
    for record in dataset:
        key = tuple(record.get(qi, None) for qi in quasi_identifiers)
        if key not in equivalence_classes:
            equivalence_classes[key] = []
        equivalence_classes[key].append(record.get(sensitive_attribute))

    max_distance = 0.0
    violations = 0

    for key, values in equivalence_classes.items():
        class_counter = Counter(values)
        class_total = len(values)
        class_dist = {k: v / class_total for k, v in class_counter.items()}

        # Compute simplified EMD (for categorical data: half the L1 distance)
        all_categories = set(overall_dist.keys()) | set(class_dist.keys())
        l1_distance = sum(
            abs(class_dist.get(cat, 0) - overall_dist.get(cat, 0))
            for cat in all_categories
        )
        emd = l1_distance / 2

        if emd > max_distance:
            max_distance = emd
        if emd > t_threshold:
            violations += 1

    return {
        "t_threshold": t_threshold,
        "sensitive_attribute": sensitive_attribute,
        "satisfied": violations == 0,
        "max_distance": round(max_distance, 4),
        "violations": violations,
        "total_equivalence_classes": len(equivalence_classes),
    }


def compute_reidentification_risk(
    dataset: list[dict],
    quasi_identifiers: list[str],
) -> dict:
    """Compute the re-identification risk of a dataset."""
    equivalence_classes: dict[tuple, int] = Counter()
    for record in dataset:
        key = tuple(record.get(qi, None) for qi in quasi_identifiers)
        equivalence_classes[key] += 1

    total_records = len(dataset)
    unique_records = sum(1 for count in equivalence_classes.values() if count == 1)

    # Prosecutor risk: probability that a specific individual can be re-identified
    prosecutor_risk = max(1 / count for count in equivalence_classes.values()) if equivalence_classes else 0

    # Journalist risk: probability that any record can be uniquely identified
    journalist_risk = unique_records / total_records if total_records > 0 else 0

    # Marketer risk: expected proportion of records that can be correctly re-identified
    marketer_risk = sum(1 / count for count in equivalence_classes.values()) / total_records if total_records > 0 else 0

    return {
        "total_records": total_records,
        "unique_records": unique_records,
        "equivalence_classes": len(equivalence_classes),
        "prosecutor_risk": round(prosecutor_risk, 4),
        "journalist_risk": round(journalist_risk, 4),
        "marketer_risk": round(marketer_risk, 4),
        "singling_out_risk_pct": round(journalist_risk * 100, 2),
        "acceptable": journalist_risk < 0.05 and prosecutor_risk < 0.2,
    }


def recommend_technique(
    data_type: str,
    sensitivity: str,
    intended_use: str,
) -> dict:
    """Recommend anonymization technique based on data characteristics."""
    recommendations = {
        ("numerical", "standard", "statistical"): {
            "primary": "Generalization (aggregation) + noise addition",
            "validation": "k-anonymity (k >= 5)",
        },
        ("numerical", "sensitive", "statistical"): {
            "primary": "Differential privacy (epsilon <= 0.1)",
            "validation": "k-anonymity (k >= 10) + t-closeness (t <= 0.15)",
        },
        ("categorical", "standard", "research"): {
            "primary": "Generalization (hierarchy-based) + suppression",
            "validation": "l-diversity (l >= 3)",
        },
        ("text", "standard", "analysis"): {
            "primary": "Full suppression of identifiers + NER-based redaction",
            "validation": "Manual review sample + automated NER validation",
        },
        ("transactional", "standard", "reporting"): {
            "primary": "Aggregation to cohort level + noise addition",
            "validation": "t-closeness (t <= 0.15) + k-anonymity (k >= 10)",
        },
        ("location", "standard", "analytics"): {
            "primary": "Spatial generalization + cloaking",
            "validation": "k-anonymity (k >= 20)",
        },
    }

    key = (data_type, sensitivity, intended_use)
    if key in recommendations:
        return recommendations[key]
    return {
        "primary": "Combination of generalization + randomization",
        "validation": "k-anonymity (k >= 5) + manual re-identification test",
    }


def generate_anonymization_record(
    anon_ref: str,
    source_category: str,
    records: int,
    technique: str,
    k_result: dict,
    reid_risk: dict,
) -> dict:
    """Generate an anonymization register entry."""
    return {
        "anonymization_reference": anon_ref,
        "organization": "Orion Data Vault Corp",
        "date": datetime.utcnow().isoformat(),
        "source_category": source_category,
        "records_anonymized": records,
        "technique_applied": technique,
        "k_anonymity_result": k_result,
        "reidentification_risk": reid_risk,
        "gdpr_status": "Outside GDPR scope (Recital 26)" if reid_risk.get("acceptable") else "Requires further anonymization",
        "next_review_date": (datetime.utcnow().replace(year=datetime.utcnow().year + 1)).isoformat(),
    }


if __name__ == "__main__":
    # Sample anonymized dataset for validation
    sample_data = [
        {"age_band": "28-37", "region": "London", "job_function": "Engineering", "salary_band": "40-60k"},
        {"age_band": "28-37", "region": "London", "job_function": "Engineering", "salary_band": "60-80k"},
        {"age_band": "28-37", "region": "London", "job_function": "Sales", "salary_band": "40-60k"},
        {"age_band": "28-37", "region": "London", "job_function": "Sales", "salary_band": "60-80k"},
        {"age_band": "28-37", "region": "London", "job_function": "Sales", "salary_band": "80-100k"},
        {"age_band": "38-47", "region": "London", "job_function": "Engineering", "salary_band": "60-80k"},
        {"age_band": "38-47", "region": "London", "job_function": "Engineering", "salary_band": "80-100k"},
        {"age_band": "38-47", "region": "London", "job_function": "Sales", "salary_band": "60-80k"},
        {"age_band": "38-47", "region": "Midlands", "job_function": "Engineering", "salary_band": "40-60k"},
        {"age_band": "38-47", "region": "Midlands", "job_function": "Engineering", "salary_band": "60-80k"},
    ]

    qi = ["age_band", "region", "job_function"]

    k_result = check_k_anonymity(sample_data, qi, k=2)
    l_result = check_l_diversity(sample_data, qi, "salary_band", l_value=2)
    t_result = check_t_closeness(sample_data, qi, "salary_band", t_threshold=0.3)
    risk = compute_reidentification_risk(sample_data, qi)

    print("K-Anonymity:", json.dumps(k_result, indent=2))
    print("L-Diversity:", json.dumps(l_result, indent=2))
    print("T-Closeness:", json.dumps(t_result, indent=2))
    print("Re-ID Risk:", json.dumps(risk, indent=2))
