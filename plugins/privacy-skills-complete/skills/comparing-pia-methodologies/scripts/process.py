#!/usr/bin/env python3
"""PIA Methodology Comparison and Selection Engine.

Implements methodology comparison scoring, selection recommendation,
cross-methodology mapping, and Art. 35(7) compliance verification.
"""

import json
from datetime import datetime
from typing import Any

METHODOLOGIES = {
    "cnil": {
        "name": "CNIL PIA Tool",
        "origin": "France (CNIL)",
        "legal_framework": "GDPR",
        "steps": 4,
        "risk_model": "3 feared events (illegitimate access, unwanted modification, disappearance)",
        "risk_scale": "4x4 matrix (Negligible, Limited, Significant, Maximum)",
        "tool_availability": "Open-source software",
        "cost": "Free",
        "typical_duration_weeks": (2, 4),
        "strengths": [
            "Structured risk model with feared events",
            "Open-source software tool",
            "Direct mapping to Art. 35 and Art. 36",
            "Well-documented knowledge bases",
        ],
        "limitations": [
            "French-centric — may not align with other DPA expectations",
            "Feared events model can be unfamiliar to non-security professionals",
            "Less emphasis on data subject consultation",
        ],
        "jurisdictions": ["France", "Belgium", "Luxembourg", "Switzerland"],
        "maturity_fit": "Medium",
    },
    "ico": {
        "name": "ICO DPIA Template",
        "origin": "United Kingdom (ICO)",
        "legal_framework": "UK GDPR",
        "steps": 7,
        "risk_model": "Harm to individuals",
        "risk_scale": "Qualitative (Low, Medium, High)",
        "tool_availability": "Word template",
        "cost": "Free",
        "typical_duration_weeks": (1, 3),
        "strengths": [
            "Simplest to adopt — practical template format",
            "Explicit data subject consultation step",
            "Clear DPO advice recording requirement",
            "Widely used as starting point by organisations new to DPIAs",
        ],
        "limitations": [
            "Less structured risk model — qualitative only",
            "UK-specific regulatory context post-Brexit",
            "No software tool — manual Word document",
            "Less suitable for complex multi-system processing",
        ],
        "jurisdictions": ["United Kingdom", "Ireland"],
        "maturity_fit": "Low",
    },
    "nist_pf": {
        "name": "NIST Privacy Framework",
        "origin": "United States (NIST)",
        "legal_framework": "Sector-agnostic",
        "steps": 5,
        "risk_model": "Organisation-defined",
        "risk_scale": "Implementation Tiers (Partial, Risk Informed, Repeatable, Adaptive)",
        "tool_availability": "Excel self-assessment",
        "cost": "Free",
        "typical_duration_weeks": None,
        "strengths": [
            "Aligns with NIST Cybersecurity Framework",
            "Flexible — works across all sectors and jurisdictions",
            "Privacy engineering objectives (Predictability, Manageability, Disassociability)",
            "Maturity-based approach supports progressive improvement",
        ],
        "limitations": [
            "Not a PIA methodology — framework for programme-level assessment",
            "No prescribed risk scale or matrix",
            "US-centric — limited recognition by EU supervisory authorities",
            "Requires supplementation with DPIA methodology for GDPR compliance",
        ],
        "jurisdictions": ["United States"],
        "maturity_fit": "Medium-High",
    },
    "iso_29134": {
        "name": "ISO/IEC 29134:2017",
        "origin": "International (ISO/IEC)",
        "legal_framework": "International",
        "steps": 3,
        "risk_model": "ISO 31000-based (likelihood x consequence)",
        "risk_scale": "Quantitative/qualitative per ISO 31000",
        "tool_availability": "No official tool",
        "cost": "Standard purchase (~CHF 166)",
        "typical_duration_weeks": (4, 8),
        "strengths": [
            "Most comprehensive and structured methodology",
            "Internationally recognised across all jurisdictions",
            "Auditable — aligns with ISO 27701 and ISO 27001 certification",
            "ISO 31000 risk framework provides rigorous risk analysis",
            "Prescribed PIA report structure (13 required sections)",
        ],
        "limitations": [
            "Most resource-intensive methodology",
            "Standard must be purchased — not freely available",
            "Requires ISO risk management expertise",
            "Overkill for simple, low-risk processing",
        ],
        "jurisdictions": [
            "International", "Singapore", "South Korea", "Japan",
            "EU (accepted)", "UK (accepted)",
        ],
        "maturity_fit": "High",
    },
}

SELECTION_WEIGHTS = {
    "jurisdiction_match": 0.30,
    "maturity_alignment": 0.25,
    "processing_complexity": 0.20,
    "resource_availability": 0.15,
    "certification_goals": 0.10,
}

MATURITY_LEVELS = {
    "Low": 1,
    "Medium": 2,
    "Medium-High": 3,
    "High": 4,
}

ART_35_7_REQUIREMENTS = [
    {"ref": "Art. 35(7)(a)", "requirement": "Systematic description of processing operations and purposes including, where applicable, the legitimate interest pursued by the controller"},
    {"ref": "Art. 35(7)(b)", "requirement": "Assessment of necessity and proportionality of processing in relation to purposes"},
    {"ref": "Art. 35(7)(c)", "requirement": "Assessment of risks to the rights and freedoms of data subjects"},
    {"ref": "Art. 35(7)(d)", "requirement": "Measures envisaged to address the risks, including safeguards, security measures, and mechanisms to ensure protection of personal data"},
]

CROSS_METHODOLOGY_MAP = [
    {
        "activity": "Processing description and context",
        "cnil": "Step 1: Context",
        "ico": "Step 2: Describe processing",
        "nist_pf": "ID.IM (Inventory & Mapping)",
        "iso_29134": "Clause 6: Preparation",
        "art_35_7": "Art. 35(7)(a)",
    },
    {
        "activity": "DPIA necessity screening",
        "cnil": "N/A (assumed necessary)",
        "ico": "Step 1: Identify need",
        "nist_pf": "N/A",
        "iso_29134": "Clause 6.1: Determine necessity",
        "art_35_7": "N/A (pre-assessment)",
    },
    {
        "activity": "Stakeholder and data subject consultation",
        "cnil": "Recommended",
        "ico": "Step 3: Consultation",
        "nist_pf": "CT.PO (Communication Policies)",
        "iso_29134": "Clause 6.4: Stakeholder engagement",
        "art_35_7": "Art. 35(9)",
    },
    {
        "activity": "Necessity and proportionality assessment",
        "cnil": "Step 2: Fundamental Principles",
        "ico": "Step 4: Necessity & proportionality",
        "nist_pf": "GV.PO (Governance Policies)",
        "iso_29134": "Clause 7.3: Privacy safeguard analysis",
        "art_35_7": "Art. 35(7)(b)",
    },
    {
        "activity": "Risk identification and assessment",
        "cnil": "Step 3: Risks (feared events)",
        "ico": "Step 5: Identify & assess risks",
        "nist_pf": "ID.RA (Risk Assessment)",
        "iso_29134": "Clause 7.4: Risk analysis",
        "art_35_7": "Art. 35(7)(c)",
    },
    {
        "activity": "Risk mitigation measures",
        "cnil": "Step 4: Validation",
        "ico": "Step 6: Mitigation measures",
        "nist_pf": "CT.DM (Data Processing Management)",
        "iso_29134": "Clause 7.5: Risk treatment",
        "art_35_7": "Art. 35(7)(d)",
    },
    {
        "activity": "Sign-off and documentation",
        "cnil": "Step 4: Validation (DPO sign-off)",
        "ico": "Step 7: Sign off & record",
        "nist_pf": "GV.AT (Awareness & Training)",
        "iso_29134": "Clause 8: Follow-up",
        "art_35_7": "N/A (good practice)",
    },
]


def score_methodology(
    methodology_id: str,
    jurisdiction: str,
    maturity_level: str,
    processing_complexity: str,
    resource_level: str,
    certification_goals: bool,
) -> dict[str, Any]:
    """Score a methodology against selection criteria.

    Args:
        methodology_id: Key from METHODOLOGIES dict.
        jurisdiction: Primary regulatory jurisdiction.
        maturity_level: One of Low, Medium, Medium-High, High.
        processing_complexity: One of Low, Medium, High.
        resource_level: One of Limited, Moderate, Extensive.
        certification_goals: Whether the organisation seeks ISO certification.
    """
    methodology = METHODOLOGIES.get(methodology_id)
    if not methodology:
        return {"error": f"Unknown methodology: {methodology_id}"}

    scores = {}

    # Jurisdiction match
    jurisdiction_lower = jurisdiction.lower()
    jurisdiction_matches = [j.lower() for j in methodology["jurisdictions"]]
    if jurisdiction_lower in jurisdiction_matches or "international" in jurisdiction_matches:
        scores["jurisdiction_match"] = 1.0
    elif any(jurisdiction_lower in j for j in jurisdiction_matches):
        scores["jurisdiction_match"] = 0.7
    else:
        scores["jurisdiction_match"] = 0.3

    # Maturity alignment
    org_maturity = MATURITY_LEVELS.get(maturity_level, 2)
    method_maturity = MATURITY_LEVELS.get(methodology["maturity_fit"], 2)
    maturity_diff = abs(org_maturity - method_maturity)
    scores["maturity_alignment"] = max(0, 1.0 - (maturity_diff * 0.3))

    # Processing complexity
    complexity_map = {"Low": 1, "Medium": 2, "High": 3}
    complexity_val = complexity_map.get(processing_complexity, 2)
    if methodology_id == "ico" and complexity_val <= 2:
        scores["processing_complexity"] = 1.0
    elif methodology_id == "cnil" and complexity_val == 2:
        scores["processing_complexity"] = 1.0
    elif methodology_id == "iso_29134" and complexity_val >= 2:
        scores["processing_complexity"] = 1.0
    elif methodology_id == "nist_pf":
        scores["processing_complexity"] = 0.6
    else:
        scores["processing_complexity"] = 0.5

    # Resource availability
    resource_map = {"Limited": 1, "Moderate": 2, "Extensive": 3}
    resource_val = resource_map.get(resource_level, 2)
    duration = methodology["typical_duration_weeks"]
    if duration is None:
        scores["resource_availability"] = 0.5 if resource_val >= 2 else 0.3
    elif resource_val == 1 and duration[0] <= 2:
        scores["resource_availability"] = 1.0
    elif resource_val == 2 and duration[0] <= 3:
        scores["resource_availability"] = 0.9
    elif resource_val == 3:
        scores["resource_availability"] = 1.0
    else:
        scores["resource_availability"] = 0.4

    # Certification goals
    if certification_goals and methodology_id == "iso_29134":
        scores["certification_goals"] = 1.0
    elif certification_goals and methodology_id == "nist_pf":
        scores["certification_goals"] = 0.6
    elif not certification_goals:
        scores["certification_goals"] = 0.7
    else:
        scores["certification_goals"] = 0.3

    # Weighted total
    total = sum(
        scores[criterion] * weight
        for criterion, weight in SELECTION_WEIGHTS.items()
    )

    return {
        "methodology": methodology["name"],
        "methodology_id": methodology_id,
        "criterion_scores": scores,
        "weighted_total": round(total, 3),
    }


def recommend_methodology(
    jurisdiction: str,
    maturity_level: str,
    processing_complexity: str,
    resource_level: str,
    certification_goals: bool,
) -> dict[str, Any]:
    """Recommend the best-fit PIA methodology based on selection criteria."""
    results = []
    for method_id in METHODOLOGIES:
        result = score_methodology(
            methodology_id=method_id,
            jurisdiction=jurisdiction,
            maturity_level=maturity_level,
            processing_complexity=processing_complexity,
            resource_level=resource_level,
            certification_goals=certification_goals,
        )
        results.append(result)

    results.sort(key=lambda x: x["weighted_total"], reverse=True)
    top = results[0]

    return {
        "recommendation": top["methodology"],
        "score": top["weighted_total"],
        "all_scores": results,
        "selection_criteria": {
            "jurisdiction": jurisdiction,
            "maturity_level": maturity_level,
            "processing_complexity": processing_complexity,
            "resource_level": resource_level,
            "certification_goals": certification_goals,
        },
        "rationale": (
            f"{top['methodology']} is recommended with a weighted score of "
            f"{top['weighted_total']:.3f} based on the organisation's jurisdiction "
            f"({jurisdiction}), maturity level ({maturity_level}), and processing "
            f"complexity ({processing_complexity})."
        ),
    }


def verify_art35_7_compliance(
    dpia_sections: dict[str, bool],
) -> dict[str, Any]:
    """Verify that a completed DPIA meets Art. 35(7) minimum content requirements.

    Args:
        dpia_sections: Dict mapping Art. 35(7) references to whether
            the requirement is addressed in the DPIA.
    """
    results = []
    for req in ART_35_7_REQUIREMENTS:
        met = dpia_sections.get(req["ref"], False)
        results.append({
            "reference": req["ref"],
            "requirement": req["requirement"],
            "addressed": met,
        })

    all_met = all(r["addressed"] for r in results)
    unmet = [r for r in results if not r["addressed"]]

    return {
        "compliant": all_met,
        "requirements": results,
        "unmet_count": len(unmet),
        "unmet_requirements": unmet,
        "assessment": (
            "DPIA meets all Art. 35(7) minimum content requirements."
            if all_met
            else f"DPIA does not meet Art. 35(7) — {len(unmet)} requirement(s) not addressed: "
            + ", ".join(r["reference"] for r in unmet)
        ),
    }


def get_cross_methodology_map() -> list[dict[str, str]]:
    """Return the cross-methodology mapping table."""
    return CROSS_METHODOLOGY_MAP


def compare_methodologies(
    methodology_ids: list[str],
) -> dict[str, Any]:
    """Compare two or more methodologies side by side."""
    comparisons = {}
    for mid in methodology_ids:
        m = METHODOLOGIES.get(mid)
        if m:
            comparisons[mid] = {
                "name": m["name"],
                "origin": m["origin"],
                "steps": m["steps"],
                "risk_model": m["risk_model"],
                "risk_scale": m["risk_scale"],
                "cost": m["cost"],
                "typical_duration_weeks": m["typical_duration_weeks"],
                "strengths": m["strengths"],
                "limitations": m["limitations"],
                "maturity_fit": m["maturity_fit"],
            }

    return {
        "methodologies_compared": len(comparisons),
        "comparison": comparisons,
    }


def run_example() -> dict[str, Any]:
    """Run example methodology comparison for QuantumLeap Health Technologies."""
    recommendation = recommend_methodology(
        jurisdiction="Germany",
        maturity_level="Medium",
        processing_complexity="High",
        resource_level="Moderate",
        certification_goals=True,
    )

    compliance_check = verify_art35_7_compliance(
        dpia_sections={
            "Art. 35(7)(a)": True,
            "Art. 35(7)(b)": True,
            "Art. 35(7)(c)": True,
            "Art. 35(7)(d)": True,
        },
    )

    comparison = compare_methodologies(["cnil", "ico", "iso_29134"])

    return {
        "reference": "PIA-METHOD-QLH-2026-001",
        "organisation": "QuantumLeap Health Technologies",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "methodology_recommendation": recommendation,
        "art_35_7_compliance": compliance_check,
        "methodology_comparison": comparison,
        "cross_mapping": get_cross_methodology_map(),
    }


if __name__ == "__main__":
    result = run_example()
    print(json.dumps(result, indent=2, default=str))
