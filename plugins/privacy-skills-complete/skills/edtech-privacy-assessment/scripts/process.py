#!/usr/bin/env python3
"""
EdTech Privacy Assessment Tool

Evaluates educational technology platforms against COPPA school exception,
FERPA, GDPR, and state student privacy law requirements.
"""

import json
from datetime import datetime, timezone

ASSESSMENT_CATEGORIES = {
    "privacy_policy": {
        "name": "Privacy Policy",
        "items": [
            {"id": "PP1", "item": "COPPA-compliant privacy policy posted", "reference": "312.4"},
            {"id": "PP2", "item": "All data collection disclosed", "reference": "312.4(b)(2)"},
            {"id": "PP3", "item": "Data not used for advertising", "reference": "312.7, SOPIPA"},
            {"id": "PP4", "item": "Data not sold", "reference": "Student Privacy Pledge"},
            {"id": "PP5", "item": "Deletion practices described", "reference": "312.10"},
            {"id": "PP6", "item": "Third parties named", "reference": "312.4(b)(4)"},
            {"id": "PP7", "item": "Student Privacy Pledge signed", "reference": "Voluntary"},
        ],
    },
    "school_exception": {
        "name": "COPPA School Exception",
        "items": [
            {"id": "SE1", "item": "Collection solely for educational purposes", "reference": "312.5(c)(4)"},
            {"id": "SE2", "item": "No commercial use of student data", "reference": "312.5(c)(4)"},
            {"id": "SE3", "item": "No disclosure to non-school third parties", "reference": "312.5(c)(4)"},
            {"id": "SE4", "item": "School has authorised the collection", "reference": "312.5(c)(4)"},
            {"id": "SE5", "item": "Written agreement with school executed", "reference": "Best practice"},
        ],
    },
    "ferpa": {
        "name": "FERPA Compliance",
        "items": [
            {"id": "FE1", "item": "Vendor designated as school official", "reference": "34 CFR 99.31(a)(1)"},
            {"id": "FE2", "item": "Under school's direct control", "reference": "34 CFR 99.31(a)(1)"},
            {"id": "FE3", "item": "Records used only for authorised purposes", "reference": "34 CFR 99.31(a)(1)"},
            {"id": "FE4", "item": "No re-disclosure without consent", "reference": "34 CFR 99.33(a)"},
        ],
    },
    "contract": {
        "name": "School Agreement",
        "items": [
            {"id": "CO1", "item": "Prohibition on commercial use", "reference": "COPPA, SOPIPA"},
            {"id": "CO2", "item": "Prohibition on advertising to students", "reference": "COPPA, state laws"},
            {"id": "CO3", "item": "Prohibition on selling student data", "reference": "COPPA, state laws"},
            {"id": "CO4", "item": "End-of-year deletion requirement", "reference": "Best practice"},
            {"id": "CO5", "item": "End-of-contract deletion requirement", "reference": "312.10"},
            {"id": "CO6", "item": "Breach notification timeline (24-72h)", "reference": "GDPR Art. 33"},
            {"id": "CO7", "item": "School audit rights", "reference": "Best practice"},
            {"id": "CO8", "item": "Sub-processor disclosure", "reference": "GDPR Art. 28"},
        ],
    },
    "security": {
        "name": "Data Security",
        "items": [
            {"id": "SC1", "item": "Encryption at rest", "reference": "312.8"},
            {"id": "SC2", "item": "Encryption in transit (TLS 1.2+)", "reference": "312.8"},
            {"id": "SC3", "item": "Access controls (RBAC)", "reference": "312.8"},
            {"id": "SC4", "item": "Regular security audits", "reference": "312.8"},
            {"id": "SC5", "item": "Incident response plan", "reference": "312.8"},
            {"id": "SC6", "item": "SOC 2 Type II or equivalent", "reference": "Best practice"},
        ],
    },
}


def run_edtech_assessment(responses: dict[str, str]) -> dict:
    """
    Run a comprehensive EdTech privacy assessment.

    Args:
        responses: Dict mapping item ID to "pass", "fail", or "na".

    Returns:
        Assessment report with category-level and overall scores.
    """
    results = {}
    overall_pass = 0
    overall_fail = 0
    overall_na = 0

    for cat_id, category in ASSESSMENT_CATEGORIES.items():
        cat_results = []
        cat_pass = 0
        cat_fail = 0
        cat_na = 0

        for item in category["items"]:
            status = responses.get(item["id"], "not_assessed")
            if status == "pass":
                cat_pass += 1
                overall_pass += 1
            elif status == "fail":
                cat_fail += 1
                overall_fail += 1
            elif status == "na":
                cat_na += 1
                overall_na += 1

            cat_results.append({
                "id": item["id"],
                "item": item["item"],
                "reference": item["reference"],
                "status": status,
            })

        applicable = cat_pass + cat_fail
        results[cat_id] = {
            "name": category["name"],
            "results": cat_results,
            "passed": cat_pass,
            "failed": cat_fail,
            "not_applicable": cat_na,
            "compliance_rate": round(cat_pass / applicable * 100, 1) if applicable > 0 else 0,
        }

    total_applicable = overall_pass + overall_fail
    return {
        "assessment_date": datetime.now(timezone.utc).isoformat(),
        "platform": "BrightPath Learning Inc.",
        "categories": results,
        "summary": {
            "total_items": sum(len(c["items"]) for c in ASSESSMENT_CATEGORIES.values()),
            "passed": overall_pass,
            "failed": overall_fail,
            "not_applicable": overall_na,
            "compliance_rate": round(overall_pass / total_applicable * 100, 1) if total_applicable > 0 else 0,
        },
        "recommendation": (
            "APPROVE for deployment" if overall_fail == 0
            else f"CONDITIONAL — {overall_fail} item(s) require remediation"
            if overall_fail <= 3
            else f"REJECT — {overall_fail} item(s) failed"
        ),
    }


if __name__ == "__main__":
    print("=== EdTech Privacy Assessment ===")
    responses = {
        "PP1": "pass", "PP2": "pass", "PP3": "pass", "PP4": "pass",
        "PP5": "pass", "PP6": "pass", "PP7": "pass",
        "SE1": "pass", "SE2": "pass", "SE3": "pass", "SE4": "pass", "SE5": "pass",
        "FE1": "pass", "FE2": "pass", "FE3": "pass", "FE4": "pass",
        "CO1": "pass", "CO2": "pass", "CO3": "pass", "CO4": "pass",
        "CO5": "pass", "CO6": "pass", "CO7": "pass", "CO8": "pass",
        "SC1": "pass", "SC2": "pass", "SC3": "pass", "SC4": "pass",
        "SC5": "pass", "SC6": "pass",
    }

    report = run_edtech_assessment(responses)
    print(f"Overall: {report['summary']['compliance_rate']}% — {report['recommendation']}")
    for cat_id, cat in report["categories"].items():
        print(f"  {cat['name']}: {cat['compliance_rate']}% ({cat['passed']} pass, {cat['failed']} fail)")
