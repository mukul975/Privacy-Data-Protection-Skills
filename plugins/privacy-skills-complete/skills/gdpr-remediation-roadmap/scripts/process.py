#!/usr/bin/env python3
"""
GDPR Remediation Roadmap Tool

Processes assessment input data and generates a scored report with
findings and recommendations.
"""

import json
import sys
from datetime import datetime


ASSESSMENT_DOMAINS = {
    "principles": {"name": "Data Protection Principles (Art. 5)", "weight": 1.5},
    "lawfulness": {"name": "Lawfulness of Processing (Art. 6-11)", "weight": 1.3},
    "transparency": {"name": "Transparency (Art. 12-14)", "weight": 1.2},
    "data_subject_rights": {"name": "Data Subject Rights (Art. 15-22)", "weight": 1.3},
    "controller_obligations": {"name": "Controller Obligations (Art. 24-31)", "weight": 1.4},
    "security": {"name": "Security of Processing (Art. 32-34)", "weight": 1.5},
    "dpia": {"name": "Impact Assessments (Art. 35-36)", "weight": 1.2},
    "dpo": {"name": "Data Protection Officer (Art. 37-39)", "weight": 1.1},
    "transfers": {"name": "International Transfers (Art. 44-49)", "weight": 1.3},
}

MATURITY_LEVELS = [
    (90, "Optimised"),
    (70, "Managed"),
    (50, "Defined"),
    (30, "Initial"),
    (0, "Ad Hoc"),
]


def get_maturity(score: float) -> str:
    for threshold, level in MATURITY_LEVELS:
        if score >= threshold:
            return level
    return "Ad Hoc"


def run_assessment(input_data: dict) -> dict:
    assessments = input_data.get("assessments", {})
    domain_results = {}
    total_weighted = 0
    total_weight = 0

    for domain_key, domain_spec in ASSESSMENT_DOMAINS.items():
        domain_data = assessments.get(domain_key, {})
        controls = domain_data.get("controls", [])
        if not controls:
            score_pct = 0
            gap_count = len(domain_data.get("gaps", []))
        else:
            compliant = sum(1 for c in controls if c.get("status") == "compliant")
            score_pct = (compliant / len(controls) * 100) if controls else 0
            gap_count = len(controls) - compliant

        weighted = score_pct * domain_spec["weight"]
        total_weighted += weighted
        total_weight += domain_spec["weight"] * 100

        domain_results[domain_key] = {
            "name": domain_spec["name"],
            "score": round(score_pct, 1),
            "maturity": get_maturity(score_pct),
            "gap_count": gap_count,
        }

    overall = (total_weighted / total_weight * 100) if total_weight > 0 else 0

    return {
        "report_title": f"GDPR Remediation Roadmap Report",
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "organisation": input_data.get("organisation", ""),
        "overall_score": round(overall, 1),
        "overall_maturity": get_maturity(overall),
        "domain_results": domain_results,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <assessment_input.json>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        input_data = json.load(f)

    result = run_assessment(input_data)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
