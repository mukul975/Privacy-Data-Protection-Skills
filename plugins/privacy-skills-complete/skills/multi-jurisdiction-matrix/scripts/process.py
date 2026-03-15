#!/usr/bin/env python3
"""
Multi-Jurisdiction Privacy Compliance Matrix Builder

Builds and manages a compliance matrix across multiple jurisdictions,
identifies common requirements, jurisdiction-specific deltas, and
generates harmonised control recommendations.
"""

import json
from datetime import datetime
from typing import Optional


JURISDICTION_REGISTRY = {
    "EU": {"law": "GDPR", "regulator": "National DPAs / EDPB", "effective": "2018-05-25"},
    "UK": {"law": "UK GDPR + DPA 2018", "regulator": "ICO", "effective": "2021-01-01"},
    "Brazil": {"law": "LGPD", "regulator": "ANPD", "effective": "2020-09-18"},
    "China": {"law": "PIPL", "regulator": "CAC", "effective": "2021-11-01"},
    "Korea": {"law": "PIPA", "regulator": "PIPC", "effective": "2011-09-30"},
    "India": {"law": "DPDP Act", "regulator": "DPBI", "effective": "2023-08-11"},
    "Thailand": {"law": "PDPA", "regulator": "PDPC", "effective": "2022-06-01"},
    "Singapore": {"law": "PDPA", "regulator": "PDPC/IMDA", "effective": "2014-07-02"},
    "Japan": {"law": "APPI", "regulator": "PPC", "effective": "2022-04-01"},
    "Australia": {"law": "Privacy Act", "regulator": "OAIC", "effective": "1988-01-01"},
}

BREACH_TIMELINES = {
    "EU": {"authority_hours": 72, "individual": "without undue delay"},
    "UK": {"authority_hours": 72, "individual": "without undue delay"},
    "Brazil": {"authority_business_days": 3, "individual_business_days": 3},
    "China": {"authority": "promptly", "individual": "promptly"},
    "Korea": {"authority_hours": 72, "individual": "without delay"},
    "India": {"authority_hours": 72, "individual_hours": 72},
    "Thailand": {"authority_hours": 72, "individual": "without delay if high risk"},
    "Singapore": {"authority_days_after_assessment": 3, "assessment_days": 30},
    "Japan": {"authority_business_days": 5, "individual": "promptly"},
    "Australia": {"assessment_days": 30, "individual": "as soon as practicable"},
}

CHILDREN_THRESHOLDS = {
    "EU": 16, "UK": 13, "Brazil": None, "China": 14, "Korea": 14,
    "India": 18, "Thailand": 10, "Singapore": None, "Japan": None, "Australia": 18,
}

MAX_PENALTIES = {
    "EU": "EUR 20M or 4% global turnover",
    "UK": "GBP 17.5M or 4% global turnover",
    "Brazil": "2% revenue in Brazil, max BRL 50M per violation",
    "China": "RMB 50M or 5% previous year revenue",
    "Korea": "3% related revenue or KRW 50M admin fine",
    "India": "INR 250 crore (~USD 30M)",
    "Thailand": "THB 5M admin + THB 1M criminal",
    "Singapore": "SGD 1M or 10% Singapore turnover",
    "Japan": "JPY 100M corporate (criminal) — no admin fines",
    "Australia": "AUD 50M or 3x benefit or 30% turnover",
}


def build_comparison_matrix(jurisdictions: list, categories: list) -> dict:
    """Build a comparison matrix for specified jurisdictions and categories."""
    matrix = {
        "generated_date": datetime.utcnow().isoformat(),
        "jurisdictions_count": len(jurisdictions),
        "categories_count": len(categories),
        "jurisdictions": {},
    }

    for j in jurisdictions:
        if j in JURISDICTION_REGISTRY:
            matrix["jurisdictions"][j] = {
                "law": JURISDICTION_REGISTRY[j]["law"],
                "regulator": JURISDICTION_REGISTRY[j]["regulator"],
                "breach_timeline": BREACH_TIMELINES.get(j, {}),
                "children_threshold": CHILDREN_THRESHOLDS.get(j),
                "max_penalty": MAX_PENALTIES.get(j),
            }

    return matrix


def identify_harmonised_standard(jurisdictions: list, requirement_type: str) -> dict:
    """Identify the most stringent (harmonised) standard across jurisdictions."""
    if requirement_type == "breach_notification":
        most_stringent = {"jurisdiction": "EU/Korea/India", "standard": "72 hours", "basis": "Shortest fixed timeline"}
        return {
            "requirement": requirement_type,
            "harmonised_standard": most_stringent,
            "all_timelines": {j: BREACH_TIMELINES.get(j) for j in jurisdictions if j in BREACH_TIMELINES},
        }

    if requirement_type == "children_age":
        thresholds = {j: CHILDREN_THRESHOLDS.get(j) for j in jurisdictions if CHILDREN_THRESHOLDS.get(j) is not None}
        highest = max(thresholds.items(), key=lambda x: x[1]) if thresholds else None
        return {
            "requirement": requirement_type,
            "harmonised_standard": {"jurisdiction": highest[0], "threshold": highest[1]} if highest else None,
            "all_thresholds": thresholds,
            "recommendation": f"Apply age {highest[1]} as global threshold (driven by {highest[0]})" if highest else "No specific threshold in selected jurisdictions",
        }

    return {"requirement": requirement_type, "note": "Use build_comparison_matrix for full analysis"}


def gap_analysis(
    current_controls: dict,
    required_controls: dict,
) -> dict:
    """Perform gap analysis between current and required controls."""
    gaps = []
    met = []

    for requirement, jurisdictions in required_controls.items():
        current = current_controls.get(requirement, {})
        if current.get("implemented"):
            satisfies = []
            shortfalls = []
            for j, standard in jurisdictions.items():
                if current.get("level", 0) >= standard.get("level", 0):
                    satisfies.append(j)
                else:
                    shortfalls.append({"jurisdiction": j, "required_level": standard.get("level"), "current_level": current.get("level")})

            if shortfalls:
                gaps.append({"requirement": requirement, "shortfalls": shortfalls, "satisfies": satisfies})
            else:
                met.append({"requirement": requirement, "satisfies": list(jurisdictions.keys())})
        else:
            gaps.append({"requirement": requirement, "shortfalls": [{"jurisdiction": j} for j in jurisdictions], "satisfies": []})

    return {
        "analysis_date": datetime.utcnow().isoformat(),
        "total_requirements": len(required_controls),
        "fully_met": len(met),
        "gaps_identified": len(gaps),
        "gap_details": gaps,
        "met_details": met,
        "compliance_rate": round(len(met) / len(required_controls) * 100, 1) if required_controls else 100,
    }


def generate_matrix_report(jurisdictions: list) -> dict:
    """Generate a comprehensive multi-jurisdiction compliance matrix report."""
    matrix = build_comparison_matrix(jurisdictions, ["breach", "children", "penalties"])
    breach_harmonised = identify_harmonised_standard(jurisdictions, "breach_notification")
    children_harmonised = identify_harmonised_standard(jurisdictions, "children_age")

    return {
        "report_date": datetime.utcnow().isoformat(),
        "matrix": matrix,
        "harmonised_standards": {
            "breach_notification": breach_harmonised,
            "children_age": children_harmonised,
        },
        "recommendations": [
            "Apply 72-hour breach notification as global standard",
            f"Apply age {children_harmonised['harmonised_standard']['threshold']} as global children's consent threshold" if children_harmonised.get("harmonised_standard") else "No harmonised children's threshold",
            "Implement separate consent for all China PIPL triggers globally",
            "Maintain data localisation for China CIIO data",
            "Integrate with registered consent manager for India operations",
        ],
    }


if __name__ == "__main__":
    print("=== Multi-Jurisdiction Matrix ===")
    jurisdictions = ["EU", "Brazil", "China", "Korea", "India", "Japan", "Australia", "Singapore", "Thailand"]
    report = generate_matrix_report(jurisdictions)
    print(json.dumps(report, indent=2))
