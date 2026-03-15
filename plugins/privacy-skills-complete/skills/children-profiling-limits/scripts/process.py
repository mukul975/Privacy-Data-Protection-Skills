#!/usr/bin/env python3
"""
Children's Profiling Restrictions Assessment Tool

Evaluates profiling activities against restrictions under GDPR Recital 71,
Art. 22, UK AADC Standards 5, 12, and 13, and DSA Art. 28(2).
"""

import json
from datetime import datetime, timezone

PROHIBITED_PROFILING = [
    {"id": "P1", "type": "Behavioural advertising targeting", "regulation": "DSA Art. 28(2), AADC Std 12"},
    {"id": "P2", "type": "Social scoring / popularity ranking", "regulation": "AADC Std 5"},
    {"id": "P3", "type": "Emotional profiling / sentiment targeting", "regulation": "AADC Std 5, GDPR Art. 9"},
    {"id": "P4", "type": "Predictive analytics for commercial targeting", "regulation": "AADC Std 5, Recital 71"},
    {"id": "P5", "type": "Cross-service behavioural tracking", "regulation": "AADC Std 9, COPPA, DSA Art. 28(2)"},
]

RESTRICTED_PROFILING = [
    {"id": "R1", "type": "Content-based recommendations", "conditions": "Default OFF; parental consent; diversity safeguards"},
    {"id": "R2", "type": "Educational adaptive learning", "conditions": "Necessary for educational purpose; DPO review"},
    {"id": "R3", "type": "Safety and moderation profiling", "conditions": "Legitimate interest (safeguarding); DPIA; not for commercial use"},
    {"id": "R4", "type": "Age-appropriate content filtering", "conditions": "Necessary for child protection; not for advertising"},
]

NUDGE_TECHNIQUES_PROHIBITED = [
    {"id": "N1", "technique": "Confirmshaming", "example": "Are you sure you want to miss out?"},
    {"id": "N2", "technique": "Reward-for-data", "example": "Earn 100 coins by enabling notifications"},
    {"id": "N3", "technique": "Asymmetric choice", "example": "Large bright Accept vs small grey Decline"},
    {"id": "N4", "technique": "Hidden opt-out", "example": "Opt-out buried in sub-menu Settings > Privacy > Advanced"},
    {"id": "N5", "technique": "Social proof", "example": "95% of users allow notifications!"},
    {"id": "N6", "technique": "Urgency/scarcity", "example": "Enable sharing now or lose your streak!"},
    {"id": "N7", "technique": "Default-to-share", "example": "Sharing pre-selected; must actively opt out"},
]


def classify_profiling_activity(
    uses_personal_data: bool,
    evaluates_personal_aspects: bool,
    predicts_behaviour: bool,
    activity_type: str,
) -> dict:
    """
    Classify a processing activity as profiling or not, and determine its status.

    Returns classification and applicable restrictions.
    """
    is_profiling = uses_personal_data and (evaluates_personal_aspects or predicts_behaviour)

    if not is_profiling:
        return {
            "is_profiling": False,
            "classification": "not_profiling",
            "status": "permitted",
            "restrictions": "None — this processing does not constitute profiling under Art. 4(4).",
        }

    # Check if prohibited
    for prohibited in PROHIBITED_PROFILING:
        if activity_type.lower() in prohibited["type"].lower():
            return {
                "is_profiling": True,
                "classification": "prohibited",
                "status": "not_permitted",
                "matched_prohibition": prohibited,
                "restrictions": f"PROHIBITED: {prohibited['type']} ({prohibited['regulation']})",
            }

    # Check if restricted
    for restricted in RESTRICTED_PROFILING:
        if activity_type.lower() in restricted["type"].lower():
            return {
                "is_profiling": True,
                "classification": "restricted",
                "status": "permitted_with_safeguards",
                "matched_restriction": restricted,
                "restrictions": f"RESTRICTED: {restricted['conditions']}",
            }

    return {
        "is_profiling": True,
        "classification": "unclassified",
        "status": "requires_assessment",
        "restrictions": "Profiling activity requires individual assessment against AADC Standards 5, 12, 13.",
    }


def audit_default_settings(profiling_features: list[dict]) -> dict:
    """
    Audit profiling feature default settings against AADC Standard 12.

    Args:
        profiling_features: List of dicts with keys: name, default_on, compelling_reason.
    """
    conforming = 0
    non_conforming = 0
    exceptions = 0
    details = []

    for feature in profiling_features:
        if not feature.get("default_on", False):
            conforming += 1
            details.append({"name": feature["name"], "status": "conforming", "note": "Default OFF"})
        elif feature.get("compelling_reason"):
            exceptions += 1
            details.append({
                "name": feature["name"],
                "status": "exception",
                "note": f"Default ON with compelling reason: {feature['compelling_reason']}",
            })
        else:
            non_conforming += 1
            details.append({
                "name": feature["name"],
                "status": "non_conforming",
                "note": "Default ON without compelling reason — MUST change to OFF",
            })

    return {
        "audit_date": datetime.now(timezone.utc).isoformat(),
        "total_features": len(profiling_features),
        "conforming": conforming,
        "exceptions": exceptions,
        "non_conforming": non_conforming,
        "overall": "PASS" if non_conforming == 0 else "FAIL",
        "details": details,
    }


def audit_nudge_techniques(ui_elements: list[dict]) -> dict:
    """
    Audit UI elements for prohibited nudge techniques.

    Args:
        ui_elements: List of dicts with keys: element_name, description.
    """
    flags = []
    for element in ui_elements:
        desc = element.get("description", "").lower()
        for nudge in NUDGE_TECHNIQUES_PROHIBITED:
            example_words = nudge["example"].lower().split()
            if any(word in desc for word in ["miss out", "earn", "coins", "streak",
                                              "95%", "users allow", "pre-selected"]):
                flags.append({
                    "element": element["element_name"],
                    "matched_technique": nudge["technique"],
                    "prohibition_id": nudge["id"],
                    "severity": "high",
                })

    return {
        "audit_date": datetime.now(timezone.utc).isoformat(),
        "elements_reviewed": len(ui_elements),
        "flags": flags,
        "overall": "PASS" if not flags else "FAIL",
    }


if __name__ == "__main__":
    print("=== Profiling Classification ===")
    test_cases = [
        (True, True, True, "Behavioural advertising"),
        (True, True, False, "Educational adaptive learning"),
        (False, False, False, "Contextual advertising"),
    ]

    for personal, aspects, predicts, activity in test_cases:
        result = classify_profiling_activity(personal, aspects, predicts, activity)
        print(f"  {activity}: {result['classification']} — {result['status']}")

    print("\n=== Default Settings Audit ===")
    features = [
        {"name": "Content recommendations", "default_on": False},
        {"name": "Learning difficulty adaptation", "default_on": True,
         "compelling_reason": "Necessary for educational content delivery"},
        {"name": "Behavioural analytics", "default_on": False},
    ]

    audit = audit_default_settings(features)
    print(f"  Overall: {audit['overall']}")
    for detail in audit["details"]:
        print(f"    {detail['name']}: {detail['status']} — {detail['note']}")
