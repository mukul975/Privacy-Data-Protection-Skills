#!/usr/bin/env python3
"""
GDPR Data Protection Audit Scoring Tool

Processes audit control point assessments and generates a scored audit report
with domain-level maturity ratings and prioritised findings.
"""

import json
import sys
from datetime import datetime
from typing import Any


AUDIT_DOMAINS = {
    "principles": {
        "name": "Data Protection Principles",
        "gdpr_ref": "Art. 5",
        "controls": ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7"],
    },
    "accountability": {
        "name": "Accountability and Governance",
        "gdpr_ref": "Art. 24, 5(2)",
        "controls": ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7"],
    },
    "privacy_by_design": {
        "name": "Privacy by Design and Default",
        "gdpr_ref": "Art. 25",
        "controls": ["3.1", "3.2", "3.3", "3.4", "3.5", "3.6"],
    },
    "processor_management": {
        "name": "Processor Management",
        "gdpr_ref": "Art. 28",
        "controls": ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7"],
    },
    "records": {
        "name": "Records of Processing",
        "gdpr_ref": "Art. 30",
        "controls": ["5.1", "5.2", "5.3", "5.4", "5.5"],
    },
    "security": {
        "name": "Security of Processing",
        "gdpr_ref": "Art. 32",
        "controls": ["6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7", "6.8"],
    },
    "dpia": {
        "name": "Data Protection Impact Assessments",
        "gdpr_ref": "Art. 35",
        "controls": ["7.1", "7.2", "7.3", "7.4", "7.5", "7.6", "7.7"],
    },
    "dpo": {
        "name": "Data Protection Officer",
        "gdpr_ref": "Art. 37-39",
        "controls": ["8.1", "8.2", "8.3", "8.4", "8.5", "8.6"],
    },
}

RATING_SCORES = {
    "effective": 3,
    "partially_effective": 2,
    "ineffective": 1,
    "not_implemented": 0,
}

SEVERITY_MAP = {
    0: "Critical",
    1: "Major",
    2: "Minor",
}

MATURITY_LEVELS = [
    (90, "Optimised", "Controls are effective, continuously improved, and integrated into BAU"),
    (70, "Managed", "Controls are effective with minor gaps; monitoring is in place"),
    (50, "Defined", "Controls are designed but inconsistently implemented or monitored"),
    (30, "Initial", "Some controls exist but significant gaps remain"),
    (0, "Ad Hoc", "Minimal or no controls; compliance is not managed"),
]


def get_maturity_level(score_pct: float) -> tuple[str, str]:
    for threshold, level, description in MATURITY_LEVELS:
        if score_pct >= threshold:
            return level, description
    return "Ad Hoc", "Minimal or no controls; compliance is not managed"


def calculate_domain_score(assessments: dict, domain_controls: list[str]) -> dict:
    total_score = 0
    max_score = len(domain_controls) * 3
    control_results = []

    for ctrl_id in domain_controls:
        ctrl_data = assessments.get(ctrl_id, {})
        rating = ctrl_data.get("rating", "not_implemented")
        score = RATING_SCORES.get(rating, 0)
        total_score += score
        control_results.append({
            "control_id": ctrl_id,
            "description": ctrl_data.get("description", ""),
            "rating": rating,
            "score": score,
            "finding": ctrl_data.get("finding", ""),
            "evidence": ctrl_data.get("evidence", ""),
        })

    score_pct = (total_score / max_score * 100) if max_score > 0 else 0
    maturity_level, maturity_desc = get_maturity_level(score_pct)

    return {
        "total_score": total_score,
        "max_score": max_score,
        "score_percentage": round(score_pct, 1),
        "maturity_level": maturity_level,
        "maturity_description": maturity_desc,
        "controls": control_results,
    }


def generate_findings(domain_results: dict) -> list[dict]:
    findings = []
    finding_id = 1

    for domain_key, domain_data in domain_results.items():
        domain_info = AUDIT_DOMAINS[domain_key]
        for ctrl in domain_data["controls"]:
            if ctrl["rating"] in ("not_implemented", "ineffective", "partially_effective"):
                severity = SEVERITY_MAP.get(ctrl["score"], "Minor")
                findings.append({
                    "finding_id": f"F-{finding_id:03d}",
                    "domain": domain_info["name"],
                    "gdpr_ref": domain_info["gdpr_ref"],
                    "control_id": ctrl["control_id"],
                    "control_description": ctrl["description"],
                    "severity": severity,
                    "rating": ctrl["rating"],
                    "finding_detail": ctrl["finding"],
                    "evidence_gap": ctrl["evidence"],
                })
                finding_id += 1

    findings.sort(key=lambda x: {"Critical": 0, "Major": 1, "Minor": 2}.get(x["severity"], 3))
    return findings


def generate_report(audit_input: dict) -> dict:
    org_name = audit_input.get("organisation", "")
    audit_date = audit_input.get("audit_date", datetime.now().strftime("%Y-%m-%d"))
    auditor = audit_input.get("auditor", "")
    assessments = audit_input.get("assessments", {})

    domain_results = {}
    overall_total = 0
    overall_max = 0

    for domain_key, domain_spec in AUDIT_DOMAINS.items():
        result = calculate_domain_score(assessments, domain_spec["controls"])
        domain_results[domain_key] = result
        overall_total += result["total_score"]
        overall_max += result["max_score"]

    overall_pct = (overall_total / overall_max * 100) if overall_max > 0 else 0
    overall_maturity, overall_desc = get_maturity_level(overall_pct)

    findings = generate_findings(domain_results)

    severity_counts = {"Critical": 0, "Major": 0, "Minor": 0}
    for f in findings:
        severity_counts[f["severity"]] = severity_counts.get(f["severity"], 0) + 1

    report = {
        "report_title": f"Data Protection Audit Report — {org_name}",
        "audit_date": audit_date,
        "auditor": auditor,
        "organisation": org_name,
        "overall_score": {
            "total": overall_total,
            "maximum": overall_max,
            "percentage": round(overall_pct, 1),
            "maturity_level": overall_maturity,
            "maturity_description": overall_desc,
        },
        "domain_scores": {},
        "findings_summary": severity_counts,
        "total_findings": len(findings),
        "findings": findings,
    }

    for domain_key, result in domain_results.items():
        domain_info = AUDIT_DOMAINS[domain_key]
        report["domain_scores"][domain_key] = {
            "name": domain_info["name"],
            "gdpr_ref": domain_info["gdpr_ref"],
            "score_percentage": result["score_percentage"],
            "maturity_level": result["maturity_level"],
        }

    return report


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <audit_input.json> [--output report.json]")
        print("\nExpected JSON structure:")
        example = {
            "organisation": "Nexus Technologies GmbH",
            "audit_date": "2026-01-20",
            "auditor": "Dr. Katharina Weiss",
            "assessments": {
                "1.1": {
                    "description": "Processing purposes are specified and documented",
                    "rating": "effective",
                    "finding": "",
                    "evidence": "RoPA with specific purpose statements reviewed",
                },
                "1.2": {
                    "description": "Valid lawful basis identified for each activity",
                    "rating": "partially_effective",
                    "finding": "3 of 47 processing activities lack documented lawful basis",
                    "evidence": "Lawful basis register incomplete",
                },
            },
        }
        print(json.dumps(example, indent=2))
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]

    with open(input_path, "r", encoding="utf-8") as f:
        audit_input = json.load(f)

    report = generate_report(audit_input)

    report_json = json.dumps(report, indent=2)
    print(report_json)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report_json)

    critical_count = report["findings_summary"].get("Critical", 0)
    if critical_count > 0:
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
