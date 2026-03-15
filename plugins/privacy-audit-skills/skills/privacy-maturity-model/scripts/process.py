#!/usr/bin/env python3
"""
Privacy Maturity Model Assessment Processor

Calculates privacy maturity scores across ten domains, generates maturity
profiles, performs gap analysis, and creates improvement roadmaps.
"""

import json
import os
from datetime import datetime
from typing import Any

DOMAINS = {
    "privacy_governance": {"name": "Privacy Governance", "weight": 0.15},
    "data_inventory": {"name": "Data Inventory and Mapping", "weight": 0.10},
    "risk_management": {"name": "Privacy Risk Management", "weight": 0.15},
    "regulatory_compliance": {"name": "Regulatory Compliance", "weight": 0.10},
    "data_subject_rights": {"name": "Data Subject Rights", "weight": 0.10},
    "consent_lawful_basis": {"name": "Consent and Lawful Basis", "weight": 0.10},
    "third_party": {"name": "Third-Party Management", "weight": 0.10},
    "incident_management": {"name": "Incident Management", "weight": 0.05},
    "privacy_by_design": {"name": "Privacy by Design", "weight": 0.10},
    "training_awareness": {"name": "Training and Awareness", "weight": 0.05},
}

MATURITY_LEVELS = {
    1.0: "Ad Hoc",
    2.0: "Repeating",
    3.0: "Defined",
    4.0: "Managed",
    5.0: "Optimized",
}

OVERALL_RATINGS = [
    (1.0, 1.9, "Initial", "Significant privacy risk; immediate action required"),
    (2.0, 2.4, "Developing", "Basic capabilities; substantial gaps remain"),
    (2.5, 2.9, "Emerging", "Progressing toward defined program; key gaps exist"),
    (3.0, 3.4, "Established", "Solid foundation; opportunities for optimization"),
    (3.5, 3.9, "Advanced", "Strong program; moving toward quantitative management"),
    (4.0, 4.4, "Leading", "Mature program; quantitatively managed"),
    (4.5, 5.0, "Exemplary", "Industry-leading; continuous innovation"),
]

INDUSTRY_BENCHMARKS = {
    "financial_services": {
        "privacy_governance": 3.5, "data_inventory": 3.0, "risk_management": 3.5,
        "regulatory_compliance": 3.5, "data_subject_rights": 3.0, "consent_lawful_basis": 3.0,
        "third_party": 3.0, "incident_management": 3.5, "privacy_by_design": 2.5,
        "training_awareness": 3.0,
    },
    "healthcare": {
        "privacy_governance": 3.0, "data_inventory": 2.5, "risk_management": 3.0,
        "regulatory_compliance": 3.5, "data_subject_rights": 2.5, "consent_lawful_basis": 2.5,
        "third_party": 2.5, "incident_management": 3.0, "privacy_by_design": 2.0,
        "training_awareness": 3.0,
    },
    "technology_saas": {
        "privacy_governance": 3.0, "data_inventory": 3.5, "risk_management": 3.0,
        "regulatory_compliance": 3.0, "data_subject_rights": 3.5, "consent_lawful_basis": 3.5,
        "third_party": 3.0, "incident_management": 3.5, "privacy_by_design": 3.0,
        "training_awareness": 2.5,
    },
    "retail": {
        "privacy_governance": 2.5, "data_inventory": 2.0, "risk_management": 2.5,
        "regulatory_compliance": 2.5, "data_subject_rights": 2.5, "consent_lawful_basis": 3.0,
        "third_party": 2.0, "incident_management": 2.5, "privacy_by_design": 2.0,
        "training_awareness": 2.0,
    },
}


def assess_maturity(
    organization_name: str,
    domain_scores: dict[str, float],
    target_scores: dict[str, float] | None = None,
    industry: str | None = None,
) -> dict[str, Any]:
    """
    Calculate privacy maturity assessment.

    Args:
        organization_name: Name of the organization.
        domain_scores: Dict mapping domain IDs to scores (1.0 to 5.0, 0.5 increments).
        target_scores: Optional target scores for gap analysis.
        industry: Optional industry for benchmarking.

    Returns:
        Complete maturity assessment report.
    """
    domain_results = []
    weighted_total = 0.0
    total_weight = 0.0

    for domain_id, domain_config in DOMAINS.items():
        score = domain_scores.get(domain_id, 1.0)
        score = max(1.0, min(5.0, round(score * 2) / 2))
        weight = domain_config["weight"]

        weighted_total += score * weight
        total_weight += weight

        level_name = MATURITY_LEVELS.get(int(score), f"Between {MATURITY_LEVELS.get(int(score), 'Unknown')} and {MATURITY_LEVELS.get(int(score) + 1, 'Unknown')}")
        if score != int(score):
            lower = MATURITY_LEVELS.get(int(score), "")
            upper = MATURITY_LEVELS.get(int(score) + 1, "")
            level_name = f"Predominantly {lower} with {upper} elements"

        target = target_scores.get(domain_id, score + 0.5) if target_scores else score + 0.5
        gap = round(target - score, 1)

        benchmark_score = None
        if industry and industry in INDUSTRY_BENCHMARKS:
            benchmark_score = INDUSTRY_BENCHMARKS[industry].get(domain_id)

        domain_results.append({
            "domain_id": domain_id,
            "domain_name": domain_config["name"],
            "score": score,
            "weight": weight,
            "weighted_score": round(score * weight, 2),
            "level": level_name,
            "target": target,
            "gap": gap,
            "benchmark": benchmark_score,
            "vs_benchmark": round(score - benchmark_score, 1) if benchmark_score else None,
        })

    overall_score = round(weighted_total / total_weight, 1) if total_weight > 0 else 1.0

    overall_rating = "Unknown"
    overall_description = ""
    for low, high, rating, description in OVERALL_RATINGS:
        if low <= overall_score <= high:
            overall_rating = rating
            overall_description = description
            break

    return {
        "metadata": {
            "organization": organization_name,
            "assessment_date": datetime.now().strftime("%Y-%m-%d"),
            "framework": "Privacy Maturity Model (AICPA/NIST hybrid)",
            "industry": industry,
        },
        "overall": {
            "score": overall_score,
            "rating": overall_rating,
            "description": overall_description,
        },
        "domains": domain_results,
        "strengths": [d for d in domain_results if d["gap"] <= 0],
        "improvement_areas": sorted(
            [d for d in domain_results if d["gap"] > 0],
            key=lambda x: x["gap"],
            reverse=True,
        ),
    }


def generate_roadmap(
    assessment: dict[str, Any],
) -> list[dict[str, Any]]:
    """
    Generate improvement roadmap from maturity assessment.

    Args:
        assessment: Maturity assessment report from assess_maturity().

    Returns:
        Phased improvement roadmap.
    """
    improvement_areas = assessment.get("improvement_areas", [])
    roadmap = []

    for i, area in enumerate(improvement_areas):
        gap = area["gap"]
        if gap <= 0.5:
            phase = "Phase 1: Quick Wins (0-3 months)"
            effort = "Low"
        elif gap <= 1.0:
            phase = "Phase 2: Foundation Building (3-6 months)"
            effort = "Medium"
        elif gap <= 1.5:
            phase = "Phase 3: Maturation (6-12 months)"
            effort = "High"
        else:
            phase = "Phase 4: Optimization (12-18 months)"
            effort = "High"

        roadmap.append({
            "domain": area["domain_name"],
            "current_score": area["score"],
            "target_score": area["target"],
            "gap": gap,
            "phase": phase,
            "effort": effort,
            "priority": i + 1,
        })

    return roadmap


if __name__ == "__main__":
    scores = {
        "privacy_governance": 3.5,
        "data_inventory": 3.0,
        "risk_management": 3.5,
        "regulatory_compliance": 3.0,
        "data_subject_rights": 3.5,
        "consent_lawful_basis": 3.0,
        "third_party": 2.5,
        "incident_management": 3.0,
        "privacy_by_design": 2.5,
        "training_awareness": 3.0,
    }

    targets = {
        "privacy_governance": 4.0,
        "data_inventory": 3.5,
        "risk_management": 4.0,
        "regulatory_compliance": 3.5,
        "data_subject_rights": 4.0,
        "consent_lawful_basis": 3.5,
        "third_party": 3.5,
        "incident_management": 3.5,
        "privacy_by_design": 3.5,
        "training_awareness": 3.5,
    }

    assessment = assess_maturity(
        "Sentinel Compliance Group", scores, targets, "technology_saas"
    )

    print(f"Organization: {assessment['metadata']['organization']}")
    print(f"Overall Score: {assessment['overall']['score']}")
    print(f"Rating: {assessment['overall']['rating']}")
    print(f"\nDomain Scores:")
    for d in assessment["domains"]:
        benchmark = f" (benchmark: {d['benchmark']})" if d["benchmark"] else ""
        print(f"  {d['domain_name']}: {d['score']} → {d['target']} (gap: {d['gap']}){benchmark}")

    roadmap = generate_roadmap(assessment)
    print(f"\nImprovement Roadmap:")
    for item in roadmap:
        print(f"  #{item['priority']} {item['domain']}: {item['current_score']}→{item['target_score']} [{item['phase']}]")
