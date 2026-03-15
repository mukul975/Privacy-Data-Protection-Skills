#!/usr/bin/env python3
"""HITECH Act penalty calculation, BA liability assessment, and enforcement tracking processor."""

import json
import os
from datetime import datetime
from typing import Any


PENALTY_TIERS_2024 = {
    "A": {
        "name": "Did Not Know",
        "description": "Did not know and would not have known with reasonable diligence",
        "per_violation_min": 137,
        "per_violation_max": 68928,
        "annual_cap": 2067813,
        "correction_required": True,
        "correction_period_days": 30,
        "investigation_mandatory": False,
    },
    "B": {
        "name": "Reasonable Cause",
        "description": "Reasonable cause, not willful neglect",
        "per_violation_min": 1379,
        "per_violation_max": 68928,
        "annual_cap": 2067813,
        "correction_required": True,
        "correction_period_days": 30,
        "investigation_mandatory": False,
    },
    "C": {
        "name": "Willful Neglect — Timely Corrected",
        "description": "Willful neglect, corrected within 30 days of knowledge",
        "per_violation_min": 13785,
        "per_violation_max": 68928,
        "annual_cap": 2067813,
        "correction_required": True,
        "correction_period_days": 30,
        "investigation_mandatory": True,
    },
    "D": {
        "name": "Willful Neglect — Not Corrected",
        "description": "Willful neglect, not timely corrected",
        "per_violation_min": 68928,
        "per_violation_max": 2067813,
        "annual_cap": 2067813,
        "correction_required": False,
        "correction_period_days": 0,
        "investigation_mandatory": True,
    },
}

CRIMINAL_PENALTIES = {
    "tier_1": {
        "conduct": "Knowingly obtaining or disclosing PHI",
        "max_fine": 50000,
        "max_imprisonment_years": 1,
    },
    "tier_2": {
        "conduct": "Under false pretenses",
        "max_fine": 100000,
        "max_imprisonment_years": 5,
    },
    "tier_3": {
        "conduct": "Intent to sell, transfer, or use for commercial advantage, personal gain, or malicious harm",
        "max_fine": 250000,
        "max_imprisonment_years": 10,
    },
}

RECOGNIZED_SECURITY_PRACTICES = [
    "nist_csf",
    "hitrust_csf",
    "section_405d_hicp",
    "nist_sp_800_171",
    "other_recognized_standard",
]


def determine_penalty_tier(
    violation: dict[str, Any],
) -> dict[str, Any]:
    """Determine the applicable HITECH penalty tier for a HIPAA violation.

    Args:
        violation: Dictionary describing the violation circumstances.

    Returns:
        Penalty tier determination with applicable ranges.
    """
    result = {
        "violation_id": violation.get("violation_id", ""),
        "determination_date": datetime.now().isoformat(),
        "tier": "",
        "tier_details": {},
        "mitigating_factors": [],
        "aggravating_factors": [],
    }

    knew_about_violation = violation.get("knew_about_violation", False)
    willful_neglect = violation.get("willful_neglect", False)
    corrected_timely = violation.get("corrected_within_30_days", False)
    reasonable_diligence_would_reveal = violation.get("reasonable_diligence_would_reveal", False)

    if not knew_about_violation and not reasonable_diligence_would_reveal:
        result["tier"] = "A"
    elif not willful_neglect:
        result["tier"] = "B"
    elif willful_neglect and corrected_timely:
        result["tier"] = "C"
    else:
        result["tier"] = "D"

    result["tier_details"] = PENALTY_TIERS_2024[result["tier"]]

    if violation.get("recognized_security_practices"):
        practices = violation["recognized_security_practices"]
        valid_practices = [p for p in practices if p in RECOGNIZED_SECURITY_PRACTICES]
        if valid_practices:
            result["mitigating_factors"].append({
                "factor": "Recognized security practices (§13412)",
                "details": f"Practices in place: {', '.join(valid_practices)}",
                "impact": "OCR must consider as mitigating factor; may reduce penalty amount",
            })

    if violation.get("prior_compliance_history") == "good":
        result["mitigating_factors"].append({
            "factor": "History of compliance",
            "impact": "May reduce penalty within tier range",
        })

    if violation.get("cooperation_with_investigation"):
        result["mitigating_factors"].append({
            "factor": "Cooperation with OCR investigation",
            "impact": "May favor resolution agreement over CMP",
        })

    if violation.get("individuals_affected", 0) > 500:
        result["aggravating_factors"].append({
            "factor": f"Large breach: {violation['individuals_affected']} individuals affected",
            "impact": "Likely to increase penalty amount within tier range",
        })

    if violation.get("prior_violations"):
        result["aggravating_factors"].append({
            "factor": "Prior HIPAA violations on record",
            "impact": "May increase penalty; indicates systemic compliance failure",
        })

    return result


def calculate_penalty_range(
    tier: str,
    violation_count: int,
    identical_violations_per_year: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Calculate the penalty range for a violation.

    Args:
        tier: Penalty tier (A, B, C, or D).
        violation_count: Number of violations.
        identical_violations_per_year: Dict mapping year to count of identical violations.

    Returns:
        Penalty range calculation.
    """
    if tier not in PENALTY_TIERS_2024:
        return {"error": f"Invalid tier: {tier}"}

    tier_info = PENALTY_TIERS_2024[tier]

    min_total = tier_info["per_violation_min"] * violation_count
    max_total = tier_info["per_violation_max"] * violation_count

    if identical_violations_per_year:
        annual_capped_max = 0
        for year, count in identical_violations_per_year.items():
            year_max = min(
                tier_info["per_violation_max"] * count,
                tier_info["annual_cap"],
            )
            annual_capped_max += year_max
        max_total = min(max_total, annual_capped_max)

    return {
        "tier": tier,
        "tier_name": tier_info["name"],
        "violation_count": violation_count,
        "per_violation_range": f"${tier_info['per_violation_min']:,} - ${tier_info['per_violation_max']:,}",
        "annual_cap": f"${tier_info['annual_cap']:,}",
        "total_min": f"${min_total:,}",
        "total_max": f"${max_total:,}",
        "investigation_mandatory": tier_info["investigation_mandatory"],
    }


def assess_ba_direct_liability(
    ba: dict[str, Any],
) -> dict[str, Any]:
    """Assess business associate direct liability under HITECH.

    Args:
        ba: Dictionary describing BA compliance status.

    Returns:
        Liability assessment.
    """
    result = {
        "ba_name": ba.get("name", ""),
        "assessment_date": datetime.now().isoformat(),
        "direct_liability_areas": [],
        "compliance_gaps": [],
    }

    security_rule_areas = [
        ("administrative_safeguards", "Administrative safeguards (§164.308)"),
        ("physical_safeguards", "Physical safeguards (§164.310)"),
        ("technical_safeguards", "Technical safeguards (§164.312)"),
        ("policies_documentation", "Policies and documentation (§164.316)"),
    ]

    for area_key, area_desc in security_rule_areas:
        status = ba.get(area_key, "not_assessed")
        result["direct_liability_areas"].append({
            "area": area_desc,
            "status": status,
            "directly_enforceable": True,
        })
        if status != "compliant":
            result["compliance_gaps"].append({
                "area": area_desc,
                "status": status,
                "risk": "BA subject to direct OCR enforcement and penalties",
            })

    privacy_areas = [
        ("impermissible_use_controls", "Controls against impermissible uses/disclosures (§164.502(a)(3))"),
        ("minimum_necessary", "Minimum necessary standard (§164.502(b))"),
        ("breach_notification", "Breach notification to CE (§164.410)"),
        ("subcontractor_management", "Subcontractor BAA management"),
    ]

    for area_key, area_desc in privacy_areas:
        status = ba.get(area_key, "not_assessed")
        result["direct_liability_areas"].append({
            "area": area_desc,
            "status": status,
            "directly_enforceable": True,
        })
        if status != "compliant":
            result["compliance_gaps"].append({
                "area": area_desc,
                "status": status,
                "risk": "BA subject to direct Privacy Rule enforcement",
            })

    result["total_areas"] = len(result["direct_liability_areas"])
    result["gaps_count"] = len(result["compliance_gaps"])

    return result


if __name__ == "__main__":
    print("=== HITECH Act Penalty Assessment ===\n")

    violation = {
        "violation_id": "VIO-2025-0003",
        "knew_about_violation": True,
        "willful_neglect": False,
        "corrected_within_30_days": True,
        "individuals_affected": 15000,
        "recognized_security_practices": ["nist_csf", "hitrust_csf"],
        "prior_compliance_history": "good",
        "cooperation_with_investigation": True,
    }
    tier_result = determine_penalty_tier(violation)
    print(f"Penalty Tier: {tier_result['tier']} ({tier_result['tier_details']['name']})")
    print(f"  Mitigating factors: {len(tier_result['mitigating_factors'])}")
    for mf in tier_result["mitigating_factors"]:
        print(f"    - {mf['factor']}")
    print()

    penalty = calculate_penalty_range("B", 5, {"2025": 5})
    print(f"Penalty Range for Tier B, 5 violations:")
    print(f"  Per violation: {penalty['per_violation_range']}")
    print(f"  Total range: {penalty['total_min']} - {penalty['total_max']}")
    print(f"  Annual cap: {penalty['annual_cap']}")
