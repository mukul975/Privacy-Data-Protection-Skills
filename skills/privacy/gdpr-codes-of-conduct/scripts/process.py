#!/usr/bin/env python3
"""
Code of Conduct Compliance Checker

Validates a draft code of conduct against GDPR Art. 40(2) subject areas
and Art. 41 monitoring body requirements.
"""

import json
import sys
from datetime import datetime

ART_40_2_SUBJECTS = [
    ("fair_transparent_processing", "Art. 40(2)(a)", "Fair and transparent processing"),
    ("legitimate_interests", "Art. 40(2)(b)", "Legitimate interests pursued in specific contexts"),
    ("data_collection", "Art. 40(2)(c)", "Collection of personal data"),
    ("pseudonymisation", "Art. 40(2)(d)", "Pseudonymisation of personal data"),
    ("public_data_subject_information", "Art. 40(2)(e)", "Information provided to public and data subjects"),
    ("data_subject_rights", "Art. 40(2)(f)", "Exercise of data subject rights"),
    ("children_protection", "Art. 40(2)(g)", "Information and protection of children"),
    ("technical_organisational_measures", "Art. 40(2)(h)", "Technical and organisational measures including privacy by design"),
    ("breach_notification", "Art. 40(2)(i)", "Breach notification"),
    ("transfer_mechanisms", "Art. 40(2)(j)", "Transfer of personal data to third countries"),
    ("dispute_resolution", "Art. 40(2)(k)", "Out-of-court dispute resolution"),
]


def validate_code(code_data: dict) -> dict:
    findings = []
    subjects_covered = 0

    for field, article, description in ART_40_2_SUBJECTS:
        covered = code_data.get("subjects", {}).get(field, False)
        if covered:
            subjects_covered += 1
        else:
            findings.append({
                "article": article,
                "subject": description,
                "status": "Not covered",
                "severity": "Minor",
            })

    monitoring = code_data.get("monitoring_body", {})
    if not monitoring.get("identified"):
        findings.append({
            "article": "Art. 41(1)",
            "subject": "Monitoring body identification",
            "status": "No monitoring body identified",
            "severity": "Major",
        })

    if not monitoring.get("independence_demonstrated"):
        findings.append({
            "article": "Art. 41(2)",
            "subject": "Monitoring body independence",
            "status": "Independence not demonstrated",
            "severity": "Major",
        })

    coverage_pct = (subjects_covered / len(ART_40_2_SUBJECTS) * 100)

    return {
        "validation_date": datetime.now().strftime("%Y-%m-%d"),
        "code_name": code_data.get("code_name", ""),
        "sector": code_data.get("sector", ""),
        "subjects_covered": subjects_covered,
        "total_subjects": len(ART_40_2_SUBJECTS),
        "coverage_percentage": round(coverage_pct, 1),
        "total_findings": len(findings),
        "findings": findings,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <code_of_conduct.json>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        code_data = json.load(f)

    result = validate_code(code_data)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
