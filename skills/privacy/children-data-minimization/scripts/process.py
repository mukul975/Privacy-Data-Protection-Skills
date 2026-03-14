#!/usr/bin/env python3
"""
Children's Data Minimisation Assessment Tool

Assesses data collection practices against strict necessity requirements
for children's data under GDPR Art. 5(1)(c), UK AADC Standard 8, and
COPPA Section 312.7.
"""

import json
from datetime import datetime, timezone

RETENTION_SCHEDULE = {
    "account_data": {"max_days": "account_duration_plus_30", "description": "Account data (name, age, parent email)"},
    "activity_data": {"max_days": 30, "description": "Session and activity logs"},
    "content_data": {"max_days": "account_duration", "description": "Content created by child"},
    "learning_data": {"max_days": "academic_year_plus_30", "description": "Learning progress and scores"},
    "communication_data": {"max_days": 90, "description": "Messages and chat logs"},
    "technical_data": {"max_days": 7, "description": "Error logs and crash reports"},
    "consent_records": {"max_days": "account_duration_plus_6_years", "description": "Parental consent records"},
    "verification_data": {"max_days": 2, "description": "ID/credit card verification source data"},
}

NECESSITY_QUESTIONS = [
    {
        "id": "Q1",
        "question": "Is this data required for the feature the child is actively using?",
        "fail_action": "Do not collect",
    },
    {
        "id": "Q2",
        "question": "Could the feature work with less precise data?",
        "fail_action": "Collect less precise version",
    },
    {
        "id": "Q3",
        "question": "Could the feature work with anonymised/pseudonymised data?",
        "fail_action": "Anonymise or pseudonymise at collection",
    },
    {
        "id": "Q4",
        "question": "Is the primary beneficiary the child (not the controller)?",
        "fail_action": "Reject unless secondary child benefit is significant",
    },
    {
        "id": "Q5",
        "question": "Would a reasonable parent expect this collection?",
        "fail_action": "Reject or require explicit parental consent",
    },
    {
        "id": "Q6",
        "question": "Is retention limited to the shortest necessary period?",
        "fail_action": "Reduce retention to shortest necessary period",
    },
]


def run_necessity_test(data_element: str, feature: str, answers: dict[str, bool]) -> dict:
    """
    Run the strict necessity test for a children's data element.

    Args:
        data_element: Name of the data element being assessed.
        feature: The feature this data supports.
        answers: Dict mapping question ID to True (pass) or False (fail).

    Returns:
        Necessity test result with recommendation.
    """
    results = []
    all_pass = True

    for question in NECESSITY_QUESTIONS:
        qid = question["id"]
        passed = answers.get(qid, False)
        if not passed:
            all_pass = False

        results.append({
            "id": qid,
            "question": question["question"],
            "passed": passed,
            "action_if_failed": question["fail_action"] if not passed else None,
        })

    return {
        "data_element": data_element,
        "feature": feature,
        "assessment_date": datetime.now(timezone.utc).isoformat(),
        "results": results,
        "overall_pass": all_pass,
        "recommendation": (
            f"Collection of '{data_element}' for '{feature}' meets strict necessity requirements."
            if all_pass
            else f"Collection of '{data_element}' for '{feature}' does NOT meet strict necessity. "
            f"Review failed questions and implement recommended actions."
        ),
    }


def audit_data_inventory(inventory: list[dict]) -> dict:
    """
    Audit a data inventory for children's data minimisation compliance.

    Args:
        inventory: List of dicts with keys: data_element, purpose, is_necessary,
                   retention_category, is_background_collection.

    Returns:
        Audit result with findings.
    """
    findings = []
    pass_count = 0
    fail_count = 0

    for item in inventory:
        issues = []

        if not item.get("is_necessary", True):
            issues.append("Data element is not necessary for stated purpose")

        if item.get("is_background_collection", False):
            issues.append(
                "Background collection detected — AADC Standard 8 prohibits unless "
                "triggered by active feature use"
            )

        category = item.get("retention_category", "")
        if category and category not in RETENTION_SCHEDULE:
            issues.append(f"Unknown retention category: {category}")

        if issues:
            fail_count += 1
            findings.append({
                "data_element": item["data_element"],
                "purpose": item.get("purpose", ""),
                "status": "FAIL",
                "issues": issues,
            })
        else:
            pass_count += 1
            findings.append({
                "data_element": item["data_element"],
                "purpose": item.get("purpose", ""),
                "status": "PASS",
                "issues": [],
            })

    return {
        "audit_date": datetime.now(timezone.utc).isoformat(),
        "total_elements": len(inventory),
        "passed": pass_count,
        "failed": fail_count,
        "compliance_rate": round(pass_count / len(inventory) * 100, 1) if inventory else 0,
        "findings": findings,
    }


def generate_retention_report(data_categories: list[str]) -> dict:
    """Generate a retention schedule report for the specified data categories."""
    report = []
    for category in data_categories:
        schedule = RETENTION_SCHEDULE.get(category)
        if schedule:
            report.append({
                "category": category,
                "description": schedule["description"],
                "max_retention": schedule["max_days"],
                "status": "defined",
            })
        else:
            report.append({
                "category": category,
                "description": "Unknown category",
                "max_retention": "undefined",
                "status": "requires_assignment",
            })

    return {
        "report_date": datetime.now(timezone.utc).isoformat(),
        "categories": report,
        "all_defined": all(r["status"] == "defined" for r in report),
    }


if __name__ == "__main__":
    print("=== Strict Necessity Test ===")
    test_result = run_necessity_test(
        data_element="precise_geolocation",
        feature="content_localisation",
        answers={
            "Q1": False,  # GPS not required for country-level localisation
            "Q2": True,
            "Q3": True,
            "Q4": True,
            "Q5": False,  # Parents would not expect GPS tracking
            "Q6": True,
        },
    )
    print(f"  Element: {test_result['data_element']}")
    print(f"  Overall Pass: {test_result['overall_pass']}")
    print(f"  Recommendation: {test_result['recommendation']}")

    print("\n=== Data Inventory Audit ===")
    inventory = [
        {"data_element": "first_name", "purpose": "Account ID", "is_necessary": True,
         "retention_category": "account_data", "is_background_collection": False},
        {"data_element": "device_advertising_id", "purpose": "Analytics",
         "is_necessary": False, "retention_category": "technical_data",
         "is_background_collection": True},
        {"data_element": "learning_scores", "purpose": "Progress tracking",
         "is_necessary": True, "retention_category": "learning_data",
         "is_background_collection": False},
    ]

    audit = audit_data_inventory(inventory)
    print(f"  Compliance Rate: {audit['compliance_rate']}%")
    for finding in audit["findings"]:
        status = finding["status"]
        print(f"    {status}: {finding['data_element']} — {', '.join(finding['issues']) if finding['issues'] else 'OK'}")

    print("\n=== Retention Schedule ===")
    categories = ["account_data", "activity_data", "learning_data", "consent_records"]
    report = generate_retention_report(categories)
    for cat in report["categories"]:
        print(f"  {cat['category']}: {cat['max_retention']} ({cat['description']})")
