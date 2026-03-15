#!/usr/bin/env python3
"""
Age Verification Method Assessment Tool

Evaluates and recommends age verification and estimation methods based on
service risk classification, regulatory requirements, and proportionality.
"""

import json
from datetime import datetime, timezone

VERIFICATION_METHODS = {
    "document_based": {
        "name": "Document-Based Verification",
        "accuracy": "very_high",
        "privacy_impact": "very_high",
        "accessibility": "low",
        "scalability": "medium",
        "cost": "high",
        "suitable_risk_levels": ["high"],
        "regulatory_acceptance": ["GDPR", "UK_OSA", "COPPA", "France_SREN"],
    },
    "facial_age_estimation": {
        "name": "Facial Age Estimation (AI)",
        "accuracy": "high",
        "privacy_impact": "medium",
        "accessibility": "medium",
        "scalability": "high",
        "cost": "medium",
        "suitable_risk_levels": ["high", "medium"],
        "regulatory_acceptance": ["GDPR", "UK_OSA", "UK_AADC"],
    },
    "digital_identity": {
        "name": "Digital Identity Verification",
        "accuracy": "very_high",
        "privacy_impact": "low",
        "accessibility": "medium",
        "scalability": "high",
        "cost": "medium",
        "suitable_risk_levels": ["high", "medium"],
        "regulatory_acceptance": ["GDPR", "eIDAS", "UK_DIATF", "France_SREN"],
    },
    "self_declaration": {
        "name": "Self-Declaration with Risk Mitigation",
        "accuracy": "low",
        "privacy_impact": "very_low",
        "accessibility": "high",
        "scalability": "very_high",
        "cost": "low",
        "suitable_risk_levels": ["low"],
        "regulatory_acceptance": ["GDPR", "UK_AADC"],
    },
    "credit_card": {
        "name": "Credit Card / Payment Verification",
        "accuracy": "moderate",
        "privacy_impact": "medium",
        "accessibility": "medium",
        "scalability": "high",
        "cost": "low",
        "suitable_risk_levels": ["medium"],
        "regulatory_acceptance": ["COPPA", "GDPR"],
    },
    "mno_verification": {
        "name": "Mobile Network Operator Verification",
        "accuracy": "high",
        "privacy_impact": "low_medium",
        "accessibility": "medium",
        "scalability": "high",
        "cost": "medium",
        "suitable_risk_levels": ["medium", "high"],
        "regulatory_acceptance": ["UK_OSA", "GDPR"],
    },
}

RISK_FACTORS = {
    "direct_messaging_strangers": 3,
    "user_generated_content_public": 3,
    "age_restricted_content": 3,
    "monetisation_targeting_children": 3,
    "content_personalisation": 2,
    "in_app_purchases": 2,
    "community_features_moderated": 2,
    "educational_with_profiling": 2,
    "static_content": 1,
    "single_player_offline": 1,
    "no_social_features": 1,
    "informational_only": 1,
}


def classify_service_risk(features: list[str]) -> dict:
    """
    Classify a service's risk level based on its features.

    Args:
        features: List of feature keys from RISK_FACTORS.

    Returns:
        Risk classification with score and level.
    """
    total_score = 0
    matched_factors = []

    for feature in features:
        score = RISK_FACTORS.get(feature, 0)
        if score > 0:
            total_score += score
            matched_factors.append({"feature": feature, "score": score})

    if total_score >= 6:
        level = "high"
    elif total_score >= 3:
        level = "medium"
    else:
        level = "low"

    return {
        "risk_level": level,
        "risk_score": total_score,
        "factors": matched_factors,
    }


def recommend_methods(risk_level: str) -> dict:
    """
    Recommend age verification methods based on risk level.

    Returns:
        Recommended and alternative methods with rationale.
    """
    recommended = []
    alternatives = []

    for method_id, method in VERIFICATION_METHODS.items():
        if risk_level in method["suitable_risk_levels"]:
            recommended.append({
                "method_id": method_id,
                "name": method["name"],
                "accuracy": method["accuracy"],
                "privacy_impact": method["privacy_impact"],
            })
        else:
            alternatives.append({
                "method_id": method_id,
                "name": method["name"],
                "note": f"Designed for {', '.join(method['suitable_risk_levels'])} risk",
            })

    return {
        "risk_level": risk_level,
        "recommended_methods": recommended,
        "alternative_methods": alternatives,
        "guidance": {
            "high": "Use document-based, facial estimation, or digital identity verification.",
            "medium": "Use facial estimation, digital identity, credit card, or MNO verification.",
            "low": "Self-declaration with neutral prompt and anti-circumvention is acceptable.",
        }.get(risk_level, ""),
    }


def proportionality_assessment(
    method_id: str, risk_level: str, data_sensitivity: str, user_count: int
) -> dict:
    """
    Assess the proportionality of a chosen age verification method.

    Returns:
        Proportionality assessment result.
    """
    method = VERIFICATION_METHODS.get(method_id)
    if not method:
        return {"proportionate": False, "reason": f"Unknown method: {method_id}"}

    issues = []

    if risk_level == "low" and method["privacy_impact"] in ("high", "very_high"):
        issues.append(
            f"Method '{method['name']}' has {method['privacy_impact']} privacy impact "
            f"but service risk is {risk_level} — a less intrusive method may be proportionate."
        )

    if risk_level == "high" and method["accuracy"] in ("low", "moderate"):
        issues.append(
            f"Method '{method['name']}' has {method['accuracy']} accuracy "
            f"but service risk is {risk_level} — a more accurate method is recommended."
        )

    if method["accessibility"] == "low" and user_count > 100000:
        issues.append(
            f"Method '{method['name']}' has low accessibility and the service "
            f"has {user_count:,} users — provide alternative methods for accessibility."
        )

    return {
        "method": method["name"],
        "risk_level": risk_level,
        "proportionate": len(issues) == 0,
        "issues": issues,
        "recommendation": (
            "Method is proportionate for the assessed risk level."
            if len(issues) == 0
            else "Consider the identified issues and document justification."
        ),
    }


if __name__ == "__main__":
    print("=== Service Risk Classification ===")
    features = ["content_personalisation", "community_features_moderated", "educational_with_profiling"]
    risk = classify_service_risk(features)
    print(f"Risk Level: {risk['risk_level']} (score: {risk['risk_score']})")

    print("\n=== Method Recommendations ===")
    recs = recommend_methods(risk["risk_level"])
    print(f"For {recs['risk_level']} risk services:")
    for m in recs["recommended_methods"]:
        print(f"  - {m['name']} (accuracy: {m['accuracy']}, privacy: {m['privacy_impact']})")
    print(f"Guidance: {recs['guidance']}")

    print("\n=== Proportionality Assessment ===")
    assessment = proportionality_assessment("self_declaration", "medium", "standard", 50000)
    print(f"Method: {assessment['method']}")
    print(f"Proportionate: {assessment['proportionate']}")
    for issue in assessment["issues"]:
        print(f"  Issue: {issue}")
