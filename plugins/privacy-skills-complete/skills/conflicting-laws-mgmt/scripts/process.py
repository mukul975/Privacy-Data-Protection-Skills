#!/usr/bin/env python3
"""
Conflicting Privacy Laws Management Tool

Identifies, classifies, and manages conflicts between privacy requirements
across multiple jurisdictions, and generates resolution recommendations.
"""

import json
from datetime import datetime
from typing import Optional


CONFLICT_TYPES = {
    "stringency_difference": {
        "description": "Same requirement type with different thresholds across jurisdictions",
        "resolution_approach": "Apply the most stringent standard globally",
    },
    "unique_requirement": {
        "description": "Requirement exists in one jurisdiction but not others",
        "resolution_approach": "Implement in the relevant jurisdiction; assess global adoption",
    },
    "true_incompatibility": {
        "description": "Requirements cannot both be satisfied simultaneously",
        "resolution_approach": "Jurisdiction-specific controls with risk-based resolution",
    },
}

KNOWN_CONFLICTS = [
    {
        "id": "CON-001",
        "category": "data_localisation",
        "type": "true_incompatibility",
        "jurisdictions": ["China", "EU"],
        "description": "China PIPL Art. 40 requires CIIO data stored in PRC; EU GDPR permits transfers with safeguards",
        "resolution": "Local storage in PRC + processed copies transferred via CAC-approved mechanism",
        "risk_level": "medium",
    },
    {
        "id": "CON-002",
        "category": "consent_standards",
        "type": "stringency_difference",
        "jurisdictions": ["China", "EU", "Korea"],
        "description": "PIPL requires consent as default; GDPR permits legitimate interest; Korea prescribes display requirements",
        "resolution": "Global consent baseline with jurisdiction-specific display adaptations",
        "risk_level": "low",
    },
    {
        "id": "CON-003",
        "category": "children_age",
        "type": "stringency_difference",
        "jurisdictions": ["India", "EU", "China", "Korea", "Thailand"],
        "description": "Age thresholds range from 10 (Thailand) to 18 (India)",
        "resolution": "Apply age 18 as global threshold",
        "risk_level": "low",
    },
    {
        "id": "CON-004",
        "category": "breach_notification",
        "type": "stringency_difference",
        "jurisdictions": ["EU", "Singapore", "Australia"],
        "description": "72-hour notification (EU) vs 30-day assessment window (Singapore, Australia)",
        "resolution": "Two-track: 72h preliminary notification + 30-day full assessment",
        "risk_level": "low",
    },
    {
        "id": "CON-005",
        "category": "legitimate_interest",
        "type": "true_incompatibility",
        "jurisdictions": ["EU", "China", "India", "Singapore"],
        "description": "Legitimate interest available in EU but not in China, India, or Singapore",
        "resolution": "Dual-basis: legitimate interest where available + consent infrastructure as fallback",
        "risk_level": "medium",
    },
]


def identify_conflicts(jurisdictions: list, processing_activity: str) -> dict:
    """Identify potential conflicts for a processing activity across jurisdictions."""
    applicable_conflicts = []
    for conflict in KNOWN_CONFLICTS:
        overlap = set(conflict["jurisdictions"]) & set(jurisdictions)
        if len(overlap) >= 2:
            applicable_conflicts.append({
                **conflict,
                "overlapping_jurisdictions": list(overlap),
            })

    return {
        "processing_activity": processing_activity,
        "jurisdictions_assessed": jurisdictions,
        "conflicts_identified": len(applicable_conflicts),
        "conflicts": applicable_conflicts,
        "assessment_date": datetime.utcnow().isoformat(),
    }


def assess_conflict_risk(conflict_id: str) -> dict:
    """Assess the risk of a specific conflict."""
    conflict = next((c for c in KNOWN_CONFLICTS if c["id"] == conflict_id), None)
    if not conflict:
        return {"error": f"Unknown conflict: {conflict_id}"}

    risk_factors = {
        "enforcement_likelihood": "medium" if conflict["risk_level"] != "low" else "low",
        "penalty_exposure": "high" if "China" in conflict["jurisdictions"] or "EU" in conflict["jurisdictions"] else "medium",
        "data_subject_impact": "medium",
        "resolution_complexity": "high" if conflict["type"] == "true_incompatibility" else "low",
    }

    return {
        "conflict": conflict,
        "risk_factors": risk_factors,
        "overall_risk": conflict["risk_level"],
        "recommendation": conflict["resolution"],
        "review_frequency": "semi-annually" if conflict["risk_level"] != "low" else "annually",
    }


def generate_conflict_register(jurisdictions: list) -> dict:
    """Generate a conflict register for the specified jurisdictions."""
    all_conflicts = identify_conflicts(jurisdictions, "all_processing_activities")

    register = {
        "generated_date": datetime.utcnow().isoformat(),
        "jurisdictions": jurisdictions,
        "total_conflicts": all_conflicts["conflicts_identified"],
        "by_type": {},
        "by_risk": {},
        "register": all_conflicts["conflicts"],
    }

    for conflict in all_conflicts["conflicts"]:
        ctype = conflict["type"]
        register["by_type"][ctype] = register["by_type"].get(ctype, 0) + 1
        risk = conflict["risk_level"]
        register["by_risk"][risk] = register["by_risk"].get(risk, 0) + 1

    return register


if __name__ == "__main__":
    print("=== Conflict Identification ===")
    jurisdictions = ["EU", "China", "India", "Korea", "Singapore", "Australia"]
    result = identify_conflicts(jurisdictions, "Global customer data processing")
    print(json.dumps(result, indent=2))

    print("\n=== Conflict Risk Assessment ===")
    risk = assess_conflict_risk("CON-001")
    print(json.dumps(risk, indent=2))
