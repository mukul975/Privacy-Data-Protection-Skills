"""
Background Check Privacy Compliance Engine

Implements role-based necessity assessments for employee background checks,
proportionality testing, and retention management per Art. 10 GDPR and
national criminal record frameworks.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


ROLE_CATEGORIES = {
    "general_office": {
        "name": "General Office Worker",
        "justified_checks": ["right_to_work", "references", "qualifications"],
        "unjustified_checks": ["criminal_record", "credit_check", "social_media"],
    },
    "financial_controller": {
        "name": "Financial Controller / Accountant",
        "justified_checks": ["right_to_work", "references", "qualifications", "credit_check", "criminal_basic"],
        "unjustified_checks": ["criminal_enhanced", "social_media"],
    },
    "teacher_youth_worker": {
        "name": "Teacher / Youth Worker",
        "justified_checks": ["right_to_work", "references", "qualifications", "criminal_enhanced_barred"],
        "unjustified_checks": ["credit_check", "social_media"],
    },
    "security_guard": {
        "name": "Security Guard",
        "justified_checks": ["right_to_work", "references", "sia_licence", "criminal_standard"],
        "unjustified_checks": ["criminal_enhanced", "credit_check"],
    },
    "warehouse_operative": {
        "name": "Warehouse Operative",
        "justified_checks": ["right_to_work", "references"],
        "unjustified_checks": ["criminal_record", "credit_check", "qualifications"],
    },
    "senior_executive": {
        "name": "Senior Executive",
        "justified_checks": ["right_to_work", "references", "qualifications", "directorship_check", "criminal_basic"],
        "unjustified_checks": ["criminal_enhanced"],
    },
    "healthcare_professional": {
        "name": "Healthcare Professional",
        "justified_checks": ["right_to_work", "references", "qualifications", "professional_registration", "criminal_enhanced", "health_screening"],
        "unjustified_checks": ["credit_check", "social_media"],
    },
    "driver_delivery": {
        "name": "Driver / Delivery",
        "justified_checks": ["right_to_work", "references", "driving_licence", "criminal_basic"],
        "unjustified_checks": ["credit_check", "social_media", "criminal_enhanced"],
    },
}

CHECK_TYPES = {
    "right_to_work": {"name": "Right-to-Work Verification", "basis": "Art. 6(1)(c)", "retention": "employment + 2 years"},
    "references": {"name": "Professional References", "basis": "Art. 6(1)(b) + Art. 6(1)(f)", "retention": "6 months from hire"},
    "qualifications": {"name": "Qualification Verification", "basis": "Art. 6(1)(b)", "retention": "duration of employment"},
    "criminal_basic": {"name": "Basic Criminal Record Check", "basis": "Art. 10 + national law", "retention": "duration of employment"},
    "criminal_standard": {"name": "Standard Criminal Record Check", "basis": "Art. 10 + national law", "retention": "duration of employment"},
    "criminal_enhanced": {"name": "Enhanced Criminal Record Check", "basis": "Art. 10 + national law", "retention": "duration of employment"},
    "criminal_enhanced_barred": {"name": "Enhanced DBS with Barred List", "basis": "Art. 10 + national law", "retention": "duration of employment"},
    "credit_check": {"name": "Credit Check", "basis": "Art. 6(1)(f)", "retention": "6 months from hire"},
    "social_media": {"name": "Social Media Screening", "basis": "Art. 6(1)(f)", "retention": "6 months from hire or immediately if not hired"},
    "driving_licence": {"name": "Driving Licence Verification", "basis": "Art. 6(1)(b)", "retention": "duration of employment"},
    "sia_licence": {"name": "SIA Licence Verification", "basis": "Art. 6(1)(c)", "retention": "duration of employment"},
    "directorship_check": {"name": "Directorship / Disqualification Check", "basis": "Art. 6(1)(f)", "retention": "duration of employment"},
    "professional_registration": {"name": "Professional Registration Verification", "basis": "Art. 6(1)(b)", "retention": "duration of employment"},
    "health_screening": {"name": "Pre-Employment Health Screening", "basis": "Art. 9(2)(b)", "retention": "duration of employment"},
}


def assess_check_proportionality(
    role_category: str,
    proposed_checks: list[str],
) -> dict:
    """
    Assess whether proposed background checks are proportionate to the role.

    Args:
        role_category: Key from ROLE_CATEGORIES.
        proposed_checks: List of check type keys.

    Returns:
        Proportionality assessment with justified and unjustified checks.
    """
    role = ROLE_CATEGORIES.get(role_category)
    if not role:
        return {"error": f"Unknown role category: {role_category}"}

    justified = []
    unjustified = []
    missing_recommended = []

    for check in proposed_checks:
        check_info = CHECK_TYPES.get(check, {"name": check, "basis": "Unknown", "retention": "Unknown"})
        if check in role["justified_checks"]:
            justified.append({
                "check": check_info["name"],
                "basis": check_info["basis"],
                "retention": check_info["retention"],
                "status": "justified",
            })
        elif check in role["unjustified_checks"]:
            unjustified.append({
                "check": check_info["name"],
                "basis": check_info["basis"],
                "status": "unjustified",
                "reason": f"Not proportionate for {role['name']} role. Remove from screening scope.",
            })
        else:
            justified.append({
                "check": check_info["name"],
                "basis": check_info["basis"],
                "retention": check_info["retention"],
                "status": "review_required",
            })

    for rec_check in role["justified_checks"]:
        if rec_check not in proposed_checks:
            check_info = CHECK_TYPES.get(rec_check, {"name": rec_check})
            missing_recommended.append(check_info["name"])

    return {
        "assessment_date": datetime.now().isoformat(),
        "role": role["name"],
        "proposed_checks": len(proposed_checks),
        "justified_checks": justified,
        "unjustified_checks": unjustified,
        "missing_recommended_checks": missing_recommended,
        "proportionate": len(unjustified) == 0,
        "recommendation": (
            f"All proposed checks are proportionate for {role['name']}."
            if len(unjustified) == 0
            else f"{len(unjustified)} check(s) are disproportionate for {role['name']}. "
            f"Remove: {', '.join(u['check'] for u in unjustified)}."
        ),
    }


def calculate_retention_deadline(
    check_type: str,
    event_date: datetime,
    candidate_hired: bool,
) -> dict:
    """Calculate retention deadline for background check data."""
    check_info = CHECK_TYPES.get(check_type, {})

    if not candidate_hired:
        deadline = event_date + timedelta(days=180)  # 6 months
        return {
            "check": check_info.get("name", check_type),
            "hired": False,
            "retention_period": "6 months from hiring decision",
            "deletion_deadline": deadline.strftime("%Y-%m-%d"),
        }

    retention = check_info.get("retention", "6 months from hire")
    if "duration of employment" in retention:
        return {
            "check": check_info.get("name", check_type),
            "hired": True,
            "retention_period": retention,
            "deletion_deadline": "Termination date + applicable post-employment retention",
        }
    elif "6 months" in retention:
        deadline = event_date + timedelta(days=180)
        return {
            "check": check_info.get("name", check_type),
            "hired": True,
            "retention_period": retention,
            "deletion_deadline": deadline.strftime("%Y-%m-%d"),
        }
    else:
        return {
            "check": check_info.get("name", check_type),
            "hired": True,
            "retention_period": retention,
            "deletion_deadline": "See specific retention schedule",
        }


def main():
    """Example: Atlas Manufacturing Group background check audit."""
    print("=== Background Check Proportionality Assessment ===")
    print("Organisation: Atlas Manufacturing Group\n")

    # Assess warehouse role with over-screening
    result = assess_check_proportionality(
        role_category="warehouse_operative",
        proposed_checks=["right_to_work", "references", "criminal_basic", "credit_check"],
    )

    print(f"Role: {result['role']}")
    print(f"Proportionate: {result['proportionate']}")
    print(f"Recommendation: {result['recommendation']}")

    if result["unjustified_checks"]:
        print("\nUnjustified checks:")
        for u in result["unjustified_checks"]:
            print(f"  - {u['check']}: {u['reason']}")

    print("\n" + json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
