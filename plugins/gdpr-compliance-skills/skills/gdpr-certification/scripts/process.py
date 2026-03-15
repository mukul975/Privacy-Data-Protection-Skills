#!/usr/bin/env python3
"""
Data Protection Certification Readiness Assessment

Evaluates organisational readiness for GDPR certification by assessing
controls against certification criteria categories.
"""

import json
import sys
from datetime import datetime

CERTIFICATION_CATEGORIES = {
    "governance": {
        "name": "Governance and Accountability",
        "criteria": [
            "data_protection_policy_approved",
            "dpo_appointed_and_resourced",
            "governance_structure_defined",
            "board_reporting_established",
            "training_programme_implemented",
        ],
    },
    "lawfulness": {
        "name": "Lawfulness and Transparency",
        "criteria": [
            "lawful_basis_documented_per_activity",
            "privacy_notices_complete_and_current",
            "consent_mechanisms_compliant",
            "special_category_conditions_documented",
        ],
    },
    "data_subject_rights": {
        "name": "Data Subject Rights",
        "criteria": [
            "dsar_procedures_documented",
            "dsar_response_within_one_month",
            "portability_capability_available",
            "erasure_capability_available",
        ],
    },
    "security": {
        "name": "Security of Processing",
        "criteria": [
            "risk_assessment_conducted",
            "encryption_implemented",
            "access_controls_implemented",
            "incident_detection_and_response",
            "regular_security_testing",
        ],
    },
    "processor_management": {
        "name": "Processor Management",
        "criteria": [
            "all_processors_identified",
            "dpas_in_place_with_all_processors",
            "sub_processor_management",
            "processor_audit_programme",
        ],
    },
    "records_and_documentation": {
        "name": "Records and Documentation",
        "criteria": [
            "ropa_complete_and_current",
            "dpia_programme_implemented",
            "breach_register_maintained",
            "retention_schedule_enforced",
        ],
    },
}


def assess_readiness(input_data: dict) -> dict:
    assessments = input_data.get("assessments", {})
    category_results = {}
    total_met = 0
    total_criteria = 0

    for cat_key, cat_spec in CERTIFICATION_CATEGORIES.items():
        met = 0
        details = []
        for criterion in cat_spec["criteria"]:
            status = assessments.get(criterion, False)
            if status:
                met += 1
            details.append({"criterion": criterion, "met": status})

        total_met += met
        total_criteria += len(cat_spec["criteria"])
        pct = (met / len(cat_spec["criteria"]) * 100) if cat_spec["criteria"] else 0

        category_results[cat_key] = {
            "name": cat_spec["name"],
            "criteria_met": met,
            "total_criteria": len(cat_spec["criteria"]),
            "readiness_percentage": round(pct, 1),
            "details": details,
        }

    overall_pct = (total_met / total_criteria * 100) if total_criteria > 0 else 0

    ready = overall_pct >= 80
    recommendation = (
        "Organisation meets readiness threshold. Proceed with certification audit engagement."
        if ready else
        "Organisation does not meet readiness threshold (80%). Address gaps before engaging certification body."
    )

    return {
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "organisation": input_data.get("organisation", ""),
        "target_certification": input_data.get("target_certification", ""),
        "overall_readiness": round(overall_pct, 1),
        "ready_for_audit": ready,
        "recommendation": recommendation,
        "category_results": category_results,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <readiness_input.json>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        input_data = json.load(f)

    result = assess_readiness(input_data)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
