#!/usr/bin/env python3
"""
GDPR Accountability Framework Maturity Assessment Tool

Assesses an organisation's accountability maturity across the four tiers
of documentation and produces a maturity scorecard with gap analysis.
"""

import json
import sys
from datetime import datetime


ACCOUNTABILITY_TIERS = {
    "tier_1_governance": {
        "name": "Governance Documents",
        "weight": 1.5,
        "documents": [
            "data_protection_policy",
            "data_protection_strategy",
            "governance_charter",
            "dpo_appointment",
            "training_framework",
        ],
    },
    "tier_2_operational": {
        "name": "Operational Records",
        "weight": 1.3,
        "documents": [
            "ropa",
            "lawful_basis_register",
            "dpia_register",
            "lia_register",
            "dpa_register",
            "transfer_records",
            "consent_records",
        ],
    },
    "tier_3_incident": {
        "name": "Incident and Response Records",
        "weight": 1.2,
        "documents": [
            "breach_register",
            "breach_notification_records",
            "dsar_log",
            "complaints_register",
        ],
    },
    "tier_4_assurance": {
        "name": "Review and Assurance Records",
        "weight": 1.0,
        "documents": [
            "audit_reports",
            "training_completion_records",
            "policy_review_records",
            "dpo_annual_reports",
            "risk_register",
        ],
    },
}

DOCUMENT_STATUS_SCORES = {
    "complete_and_current": 4,
    "complete_but_outdated": 3,
    "incomplete": 2,
    "draft_only": 1,
    "not_exists": 0,
}

MATURITY_LEVELS = [
    (90, "Optimised", "Continuous improvement with proactive risk management"),
    (70, "Managed", "Framework actively maintained with metrics and monitoring"),
    (50, "Defined", "Systematic framework established with documented procedures"),
    (30, "Reactive", "Basic compliance efforts triggered by incidents or complaints"),
    (0, "Ad Hoc", "No systematic accountability measures"),
]


def assess_tier(tier_key: str, tier_spec: dict, documents: dict) -> dict:
    tier_docs = tier_spec["documents"]
    max_score = len(tier_docs) * 4
    total_score = 0
    doc_results = []

    for doc_id in tier_docs:
        doc_data = documents.get(doc_id, {})
        status = doc_data.get("status", "not_exists")
        score = DOCUMENT_STATUS_SCORES.get(status, 0)
        total_score += score

        doc_results.append({
            "document_id": doc_id,
            "document_name": doc_data.get("name", doc_id.replace("_", " ").title()),
            "status": status,
            "score": score,
            "last_reviewed": doc_data.get("last_reviewed", ""),
            "owner": doc_data.get("owner", ""),
            "notes": doc_data.get("notes", ""),
        })

    score_pct = (total_score / max_score * 100) if max_score > 0 else 0
    weighted_score = score_pct * tier_spec["weight"]

    return {
        "tier": tier_key,
        "name": tier_spec["name"],
        "score_percentage": round(score_pct, 1),
        "weighted_score": round(weighted_score, 1),
        "weight": tier_spec["weight"],
        "documents": doc_results,
        "gaps": [d for d in doc_results if d["score"] < 3],
    }


def get_maturity(score: float) -> tuple[str, str]:
    for threshold, level, desc in MATURITY_LEVELS:
        if score >= threshold:
            return level, desc
    return "Ad Hoc", "No systematic accountability measures"


def run_assessment(input_data: dict) -> dict:
    org_name = input_data.get("organisation", "")
    documents = input_data.get("documents", {})

    tier_results = {}
    total_weighted = 0
    total_weight = 0

    for tier_key, tier_spec in ACCOUNTABILITY_TIERS.items():
        result = assess_tier(tier_key, tier_spec, documents)
        tier_results[tier_key] = result
        total_weighted += result["weighted_score"]
        total_weight += tier_spec["weight"] * 100

    overall_score = (total_weighted / total_weight * 100) if total_weight > 0 else 0
    maturity_level, maturity_desc = get_maturity(overall_score)

    all_gaps = []
    for tier_result in tier_results.values():
        for gap in tier_result["gaps"]:
            gap["tier"] = tier_result["name"]
            all_gaps.append(gap)

    all_gaps.sort(key=lambda x: x["score"])

    return {
        "report_title": f"Accountability Maturity Assessment — {org_name}",
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "organisation": org_name,
        "overall_score": round(overall_score, 1),
        "maturity_level": maturity_level,
        "maturity_description": maturity_desc,
        "tier_results": {k: {
            "name": v["name"],
            "score_percentage": v["score_percentage"],
            "gap_count": len(v["gaps"]),
        } for k, v in tier_results.items()},
        "total_documents_assessed": sum(
            len(t["documents"]) for t in tier_results.values()
        ),
        "total_gaps": len(all_gaps),
        "priority_gaps": all_gaps[:10],
        "recommendations": generate_recommendations(tier_results, all_gaps),
    }


def generate_recommendations(tier_results: dict, gaps: list) -> list[str]:
    recommendations = []

    critical_gaps = [g for g in gaps if g["score"] == 0]
    if critical_gaps:
        doc_names = ", ".join(g["document_name"] for g in critical_gaps[:5])
        recommendations.append(
            f"Immediate action required: {len(critical_gaps)} accountability documents do not exist. "
            f"Priority documents: {doc_names}."
        )

    for tier_key, result in tier_results.items():
        if result["score_percentage"] < 50:
            recommendations.append(
                f"{result['name']} tier scores {result['score_percentage']}% — "
                f"below the minimum Defined maturity threshold. "
                f"Address {len(result['gaps'])} gaps in this tier as a priority."
            )

    outdated = [g for g in gaps if g["status"] == "complete_but_outdated"]
    if outdated:
        recommendations.append(
            f"{len(outdated)} documents are complete but outdated. "
            f"Schedule reviews within the next 30 days."
        )

    if not recommendations:
        recommendations.append(
            "Framework is well-maintained. Continue the current review cycle and "
            "focus on continuous improvement opportunities."
        )

    return recommendations


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <accountability_input.json>")
        print("\nExample input:")
        example = {
            "organisation": "Nexus Technologies GmbH",
            "documents": {
                "data_protection_policy": {
                    "name": "Data Protection Policy",
                    "status": "complete_and_current",
                    "last_reviewed": "2025-11-01",
                    "owner": "Dr. Katharina Weiss",
                },
                "ropa": {
                    "name": "Records of Processing Activities",
                    "status": "complete_but_outdated",
                    "last_reviewed": "2024-06-15",
                    "owner": "DPO Office",
                    "notes": "Last full review was 18 months ago",
                },
                "breach_register": {
                    "name": "Personal Data Breach Register",
                    "status": "complete_and_current",
                    "last_reviewed": "2026-01-05",
                    "owner": "CISO Office",
                },
            },
        }
        print(json.dumps(example, indent=2))
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        input_data = json.load(f)

    result = run_assessment(input_data)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
