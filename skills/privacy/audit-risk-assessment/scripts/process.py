#!/usr/bin/env python3
"""
Privacy Audit Risk Assessment Tool

Calculates inherent risk, control effectiveness, residual risk scores,
and generates risk-based audit plans for privacy auditable entities.
"""

import json
from typing import Optional


RISK_FACTORS = {
    "data_volume": {"weight": 0.20, "description": "Volume of personal data processed"},
    "data_sensitivity": {"weight": 0.25, "description": "Sensitivity of data categories"},
    "regulatory_exposure": {"weight": 0.25, "description": "Number and stringency of applicable regulations"},
    "processing_complexity": {"weight": 0.15, "description": "Complexity of processing operations"},
    "external_sharing": {"weight": 0.15, "description": "Extent of data sharing with external parties"},
}

CONTROL_EFFECTIVENESS = {
    "effective": {"score": 1, "description": "Controls designed and operating effectively"},
    "partially_effective": {"score": 2, "description": "Controls exist but have gaps"},
    "ineffective": {"score": 3, "description": "Controls absent, poorly designed, or not operating"},
}

RESIDUAL_RISK_BANDS = [
    {"min": 1.0, "max": 2.0, "rating": "low", "audit_frequency": "every 3 years"},
    {"min": 2.1, "max": 3.5, "rating": "medium", "audit_frequency": "every 2 years"},
    {"min": 3.6, "max": 4.5, "rating": "high", "audit_frequency": "annually"},
    {"min": 4.6, "max": 5.0, "rating": "critical", "audit_frequency": "semi-annually"},
]


def calculate_inherent_risk(
    data_volume: int,
    data_sensitivity: int,
    regulatory_exposure: int,
    processing_complexity: int,
    external_sharing: int,
) -> dict:
    """Calculate weighted inherent risk score (1-5 scale for each factor)."""
    for val, name in [
        (data_volume, "data_volume"),
        (data_sensitivity, "data_sensitivity"),
        (regulatory_exposure, "regulatory_exposure"),
        (processing_complexity, "processing_complexity"),
        (external_sharing, "external_sharing"),
    ]:
        if not 1 <= val <= 5:
            raise ValueError(f"{name} must be between 1 and 5, got {val}")

    scores = {
        "data_volume": data_volume,
        "data_sensitivity": data_sensitivity,
        "regulatory_exposure": regulatory_exposure,
        "processing_complexity": processing_complexity,
        "external_sharing": external_sharing,
    }

    weighted_score = sum(
        scores[factor] * RISK_FACTORS[factor]["weight"]
        for factor in RISK_FACTORS
    )

    return {
        "factor_scores": scores,
        "weights": {f: RISK_FACTORS[f]["weight"] for f in RISK_FACTORS},
        "inherent_risk_score": round(weighted_score, 2),
    }


def assess_control_effectiveness(
    design_adequate: bool,
    operating_consistent: bool,
) -> dict:
    """Assess control effectiveness based on design and operating assessment."""
    if design_adequate and operating_consistent:
        rating = "effective"
    elif design_adequate and not operating_consistent:
        rating = "partially_effective"
    else:
        rating = "ineffective"

    return {
        "design_adequate": design_adequate,
        "operating_consistent": operating_consistent,
        "rating": rating,
        "score": CONTROL_EFFECTIVENESS[rating]["score"],
        "description": CONTROL_EFFECTIVENESS[rating]["description"],
    }


def calculate_residual_risk(
    inherent_risk_score: float,
    control_effectiveness_score: int,
) -> dict:
    """Calculate residual risk and determine audit priority."""
    raw_residual = inherent_risk_score * control_effectiveness_score
    normalized = min(raw_residual / 3.0, 5.0)  # Normalize to 1-5 scale

    rating = "low"
    audit_frequency = "every 3 years"
    for band in RESIDUAL_RISK_BANDS:
        if band["min"] <= normalized <= band["max"]:
            rating = band["rating"]
            audit_frequency = band["audit_frequency"]
            break

    return {
        "inherent_risk_score": inherent_risk_score,
        "control_effectiveness_score": control_effectiveness_score,
        "raw_residual": round(raw_residual, 2),
        "normalized_residual": round(normalized, 2),
        "rating": rating,
        "recommended_audit_frequency": audit_frequency,
    }


def generate_risk_heat_map(entities: list) -> dict:
    """Generate a risk heat map summary from a list of assessed entities."""
    distribution = {"critical": [], "high": [], "medium": [], "low": []}

    for entity in entities:
        rating = entity.get("residual_risk_rating", "low")
        if rating in distribution:
            distribution[rating].append(entity.get("name", "unknown"))

    return {
        "total_entities": len(entities),
        "distribution": {k: len(v) for k, v in distribution.items()},
        "critical_entities": distribution["critical"],
        "high_entities": distribution["high"],
        "entities_exceeding_appetite": distribution["critical"] + distribution["high"],
    }


def build_audit_plan(entities: list, available_audit_days: int) -> dict:
    """Build a risk-prioritised audit plan given resource constraints."""
    priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    sorted_entities = sorted(
        entities,
        key=lambda e: priority_order.get(e.get("residual_risk_rating", "low"), 3),
    )

    plan = []
    days_allocated = 0
    deferred = []

    estimated_days = {"critical": 15, "high": 10, "medium": 7, "low": 5}

    for entity in sorted_entities:
        rating = entity.get("residual_risk_rating", "low")
        days_needed = estimated_days.get(rating, 5)

        if days_allocated + days_needed <= available_audit_days:
            plan.append({
                "entity": entity.get("name"),
                "residual_risk": rating,
                "estimated_days": days_needed,
            })
            days_allocated += days_needed
        else:
            deferred.append({
                "entity": entity.get("name"),
                "residual_risk": rating,
                "reason": "insufficient_audit_resource",
            })

    return {
        "planned_audits": plan,
        "total_audit_days_planned": days_allocated,
        "available_audit_days": available_audit_days,
        "utilization_pct": round(days_allocated / available_audit_days * 100, 1) if available_audit_days > 0 else 0,
        "deferred_audits": deferred,
    }


if __name__ == "__main__":
    print("=== Inherent Risk Calculation ===")
    inherent = calculate_inherent_risk(
        data_volume=4,
        data_sensitivity=5,
        regulatory_exposure=4,
        processing_complexity=3,
        external_sharing=3,
    )
    print(json.dumps(inherent, indent=2))

    print("\n=== Control Effectiveness ===")
    control = assess_control_effectiveness(
        design_adequate=True, operating_consistent=False,
    )
    print(json.dumps(control, indent=2))

    print("\n=== Residual Risk ===")
    residual = calculate_residual_risk(
        inherent["inherent_risk_score"], control["score"],
    )
    print(json.dumps(residual, indent=2))

    print("\n=== Risk Heat Map ===")
    entities = [
        {"name": "DSAR Processing", "residual_risk_rating": "high"},
        {"name": "Consent Management", "residual_risk_rating": "medium"},
        {"name": "International Transfers", "residual_risk_rating": "critical"},
        {"name": "Employee Data Processing", "residual_risk_rating": "low"},
        {"name": "Vendor DPA Management", "residual_risk_rating": "high"},
    ]
    heat_map = generate_risk_heat_map(entities)
    print(json.dumps(heat_map, indent=2))

    print("\n=== Audit Plan ===")
    plan = build_audit_plan(entities, available_audit_days=40)
    print(json.dumps(plan, indent=2))
