#!/usr/bin/env python3
"""NIST Privacy Framework IDENTIFY Function Implementation Engine.

Implements the ID.IM, ID.BE, ID.RA, and ID.DE subcategories with
GDPR cross-mapping.
"""

import json
from datetime import datetime
from typing import Any

IDENTIFY_SUBCATEGORIES = {
    "ID.IM": {
        "name": "Inventory and Mapping",
        "controls": [
            {"id": "ID.IM-P1", "description": "Systems/products/services that process data are inventoried", "gdpr_map": "Art. 30(1)"},
            {"id": "ID.IM-P2", "description": "Owners of systems/products/services are identified", "gdpr_map": "Art. 30(1)(a)"},
            {"id": "ID.IM-P3", "description": "Categories of individuals whose data are processed are inventoried", "gdpr_map": "Art. 30(1)(c)"},
            {"id": "ID.IM-P4", "description": "Data actions of the systems are inventoried", "gdpr_map": "Art. 30(1)(b)"},
            {"id": "ID.IM-P5", "description": "Purposes for data actions are inventoried", "gdpr_map": "Art. 30(1)(b)"},
            {"id": "ID.IM-P6", "description": "Data elements within data actions are inventoried", "gdpr_map": "Art. 30(1)(c)"},
            {"id": "ID.IM-P7", "description": "Environmental factors are understood", "gdpr_map": "Art. 35(1)"},
            {"id": "ID.IM-P8", "description": "Data processing is mapped", "gdpr_map": "Art. 30, Art. 35(7)(a)"},
        ],
    },
    "ID.BE": {
        "name": "Business Environment",
        "controls": [
            {"id": "ID.BE-P1", "description": "Organisation's role in data processing ecosystem is identified", "gdpr_map": "Art. 26, Art. 28"},
            {"id": "ID.BE-P2", "description": "Priorities for mission, objectives, activities are established", "gdpr_map": "Art. 25 (DPbD)"},
            {"id": "ID.BE-P3", "description": "Systems supporting priorities are identified", "gdpr_map": "Art. 24"},
        ],
    },
    "ID.RA": {
        "name": "Risk Assessment",
        "controls": [
            {"id": "ID.RA-P1", "description": "Contextual factors related to data actions are identified", "gdpr_map": "Art. 35(7)(a)"},
            {"id": "ID.RA-P2", "description": "Data analytic inputs and outputs are identified", "gdpr_map": "Art. 22, Art. 35"},
            {"id": "ID.RA-P3", "description": "Potential problems for individuals are identified", "gdpr_map": "Art. 35(7)(c)"},
            {"id": "ID.RA-P4", "description": "Problematic data actions assessed for likelihood and impact", "gdpr_map": "Art. 35(7)(c)"},
            {"id": "ID.RA-P5", "description": "Risk responses are identified and prioritised", "gdpr_map": "Art. 35(7)(d)"},
        ],
    },
    "ID.DE": {
        "name": "Data Processing Ecosystem Risk Management",
        "controls": [
            {"id": "ID.DE-P1", "description": "Ecosystem risk management policies are established", "gdpr_map": "Art. 28"},
            {"id": "ID.DE-P2", "description": "Ecosystem parties are identified and assessed", "gdpr_map": "Art. 28(1)"},
            {"id": "ID.DE-P3", "description": "Contracts with ecosystem parties are managed", "gdpr_map": "Art. 28(3)"},
            {"id": "ID.DE-P4", "description": "Interoperability frameworks are established", "gdpr_map": "Art. 20 (portability)"},
            {"id": "ID.DE-P5", "description": "Ecosystem parties managed per risk strategy", "gdpr_map": "Art. 28(3)(h)"},
        ],
    },
}

PROBLEMATIC_DATA_ACTIONS = [
    {"id": "PDA1", "name": "Appropriation", "description": "Use of data in ways beyond data subject expectations"},
    {"id": "PDA2", "name": "Distortion", "description": "Use of inaccurate data or misleading inferences"},
    {"id": "PDA3", "name": "Induced Disclosure", "description": "Pressure to reveal more data than intended"},
    {"id": "PDA4", "name": "Insecurity", "description": "Inadequate protection of data"},
    {"id": "PDA5", "name": "Re-identification", "description": "Linking anonymised data back to individuals"},
    {"id": "PDA6", "name": "Stigmatisation", "description": "Association with disfavoured groups"},
    {"id": "PDA7", "name": "Surveillance", "description": "Excessive monitoring beyond reasonable expectations"},
    {"id": "PDA8", "name": "Unanticipated Revelation", "description": "Discovery of information beyond original data"},
    {"id": "PDA9", "name": "Unwarranted Restriction", "description": "Limiting access to services based on data"},
]


def assess_identify_maturity(
    control_statuses: dict[str, str],
) -> dict[str, Any]:
    """Assess IDENTIFY function implementation maturity.

    Args:
        control_statuses: Mapping of control IDs to status
            ("implemented", "partial", "planned", "not_started")

    Returns:
        Maturity assessment per subcategory and overall
    """
    maturity_scores = {"implemented": 4, "partial": 2, "planned": 1, "not_started": 0}
    subcategory_results = {}

    for subcat_id, subcat_info in IDENTIFY_SUBCATEGORIES.items():
        controls = subcat_info["controls"]
        scores = [maturity_scores.get(control_statuses.get(c["id"], "not_started"), 0) for c in controls]
        avg_score = sum(scores) / len(scores) if scores else 0
        subcategory_results[subcat_id] = {
            "name": subcat_info["name"],
            "average_score": round(avg_score, 1),
            "maturity_level": (
                "Optimised" if avg_score >= 3.5
                else "Managed" if avg_score >= 2.5
                else "Developing" if avg_score >= 1.5
                else "Initial" if avg_score >= 0.5
                else "Not Started"
            ),
            "controls": [
                {
                    "id": c["id"],
                    "description": c["description"],
                    "gdpr_map": c["gdpr_map"],
                    "status": control_statuses.get(c["id"], "not_started"),
                }
                for c in controls
            ],
        }

    all_scores = [s["average_score"] for s in subcategory_results.values()]
    overall = sum(all_scores) / len(all_scores) if all_scores else 0

    return {
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "subcategories": subcategory_results,
        "overall_score": round(overall, 1),
        "overall_maturity": (
            "Optimised" if overall >= 3.5
            else "Managed" if overall >= 2.5
            else "Developing" if overall >= 1.5
            else "Initial" if overall >= 0.5
            else "Not Started"
        ),
    }


def run_example() -> dict[str, Any]:
    """Run example NIST PF IDENTIFY assessment for QuantumLeap Health Technologies."""
    return assess_identify_maturity({
        "ID.IM-P1": "implemented", "ID.IM-P2": "implemented",
        "ID.IM-P3": "implemented", "ID.IM-P4": "partial",
        "ID.IM-P5": "implemented", "ID.IM-P6": "partial",
        "ID.IM-P7": "partial", "ID.IM-P8": "implemented",
        "ID.BE-P1": "implemented", "ID.BE-P2": "partial",
        "ID.BE-P3": "partial",
        "ID.RA-P1": "implemented", "ID.RA-P2": "partial",
        "ID.RA-P3": "implemented", "ID.RA-P4": "implemented",
        "ID.RA-P5": "implemented",
        "ID.DE-P1": "implemented", "ID.DE-P2": "implemented",
        "ID.DE-P3": "implemented", "ID.DE-P4": "planned",
        "ID.DE-P5": "partial",
    })


if __name__ == "__main__":
    result = run_example()
    print(json.dumps(result, indent=2, default=str))
