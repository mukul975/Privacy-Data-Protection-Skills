#!/usr/bin/env python3
"""
Continuous Privacy Compliance Monitoring Processor

Manages control scoring, deviation tracking, alert management,
and compliance dashboard generation for continuous monitoring programs.
"""

import json
import os
from datetime import datetime, timedelta
from typing import Any

CONTROL_SCORE_LEVELS = {
    (90, 100): {"status": "Effective", "color": "green"},
    (75, 89): {"status": "Mostly Effective", "color": "yellow"},
    (50, 74): {"status": "Partially Effective", "color": "orange"},
    (25, 49): {"status": "Largely Ineffective", "color": "red"},
    (0, 24): {"status": "Ineffective", "color": "darkred"},
}

ALERT_SEVERITY = {
    "critical": {"response_hours": 4, "label": "Critical"},
    "high": {"response_hours": 24, "label": "High"},
    "medium": {"response_hours": 72, "label": "Medium"},
    "low": {"response_hours": 168, "label": "Low"},
}


def score_control(test_results: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Calculate control compliance score from test results.

    Args:
        test_results: List of test result dicts with 'test_name', 'passed' (bool),
                     'weight' (float, 0-1), 'timestamp' (str).

    Returns:
        Control score with status and details.
    """
    if not test_results:
        return {"score": 0, "status": "Ineffective", "tests_passed": 0, "tests_total": 0}

    weighted_score = 0.0
    total_weight = 0.0

    for result in test_results:
        weight = result.get("weight", 1.0)
        passed = result.get("passed", False)
        weighted_score += (100 if passed else 0) * weight
        total_weight += weight

    score = int(weighted_score / total_weight) if total_weight > 0 else 0

    status = "Unknown"
    for (low, high), info in CONTROL_SCORE_LEVELS.items():
        if low <= score <= high:
            status = info["status"]
            break

    return {
        "score": score,
        "status": status,
        "tests_passed": sum(1 for r in test_results if r.get("passed", False)),
        "tests_total": len(test_results),
        "last_tested": max((r.get("timestamp", "") for r in test_results), default=""),
    }


def aggregate_domain_score(control_scores: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Aggregate control scores into a domain-level score.

    Args:
        control_scores: List of control score dicts from score_control().

    Returns:
        Domain aggregate score.
    """
    if not control_scores:
        return {"score": 0, "status": "Ineffective", "controls_count": 0}

    total_score = sum(c["score"] for c in control_scores)
    avg_score = int(total_score / len(control_scores))

    status = "Unknown"
    for (low, high), info in CONTROL_SCORE_LEVELS.items():
        if low <= avg_score <= high:
            status = info["status"]
            break

    return {
        "score": avg_score,
        "status": status,
        "controls_count": len(control_scores),
        "controls_effective": sum(1 for c in control_scores if c["score"] >= 90),
        "controls_at_risk": sum(1 for c in control_scores if c["score"] < 75),
    }


def generate_compliance_dashboard(
    organization_name: str,
    regulations: dict[str, dict[str, Any]],
    deviations: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Generate executive compliance dashboard data.

    Args:
        organization_name: Name of the organization.
        regulations: Dict mapping regulation names to compliance data.
            Each: {'score': int, 'controls_total': int, 'controls_compliant': int}
        deviations: List of open deviations.
            Each: {'id': str, 'control': str, 'severity': str, 'days_open': int, 'owner': str}

    Returns:
        Dashboard data structure.
    """
    overall_score = 0
    if regulations:
        overall_score = int(sum(r["score"] for r in regulations.values()) / len(regulations))

    severity_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for dev in deviations:
        sev = dev.get("severity", "low")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1

    status = "Unknown"
    for (low, high), info in CONTROL_SCORE_LEVELS.items():
        if low <= overall_score <= high:
            status = info["status"]
            break

    return {
        "metadata": {
            "organization": organization_name,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        },
        "overall_compliance": {
            "score": overall_score,
            "status": status,
        },
        "by_regulation": {
            name: {
                "score": data["score"],
                "controls_total": data.get("controls_total", 0),
                "controls_compliant": data.get("controls_compliant", 0),
            }
            for name, data in regulations.items()
        },
        "deviations": {
            "total_open": len(deviations),
            "by_severity": severity_counts,
            "top_deviations": sorted(deviations, key=lambda x: (
                {"critical": 0, "high": 1, "medium": 2, "low": 3}.get(x.get("severity", "low"), 4),
                -x.get("days_open", 0),
            ))[:5],
        },
    }


def process_regulatory_change(
    change_description: str,
    affected_controls: list[str],
    severity: str,
) -> dict[str, Any]:
    """
    Process a regulatory change and determine response requirements.

    Args:
        change_description: Description of the regulatory change.
        affected_controls: List of control IDs affected.
        severity: Change severity ('new_regulation', 'amendment', 'guidance', 'enforcement').

    Returns:
        Regulatory change response plan.
    """
    timelines = {
        "new_regulation": {"assessment_days": 30, "implementation": "By effective date"},
        "amendment": {"assessment_days": 14, "implementation": "Per amendment effective date"},
        "guidance": {"assessment_days": 30, "implementation": "Within 90 days"},
        "enforcement": {"assessment_days": 14, "implementation": "Within 30 days"},
    }

    timeline = timelines.get(severity, timelines["guidance"])

    return {
        "change_id": f"RC-{datetime.now().strftime('%Y%m%d')}-001",
        "detected_date": datetime.now().strftime("%Y-%m-%d"),
        "description": change_description,
        "severity": severity,
        "affected_controls": affected_controls,
        "assessment_deadline": (
            datetime.now() + timedelta(days=timeline["assessment_days"])
        ).strftime("%Y-%m-%d"),
        "implementation_timeline": timeline["implementation"],
        "status": "detected",
        "actions": [
            "Conduct relevance assessment",
            "Identify affected controls and processes",
            "Perform gap analysis",
            "Develop remediation plan",
            "Implement changes",
            "Update monitoring rules",
            "Verify compliance",
        ],
    }


if __name__ == "__main__":
    test_results = [
        {"test_name": "Encryption at rest enabled", "passed": True, "weight": 1.0, "timestamp": "2025-01-15"},
        {"test_name": "TLS 1.2+ enforced", "passed": True, "weight": 1.0, "timestamp": "2025-01-15"},
        {"test_name": "RBAC configured", "passed": True, "weight": 0.8, "timestamp": "2025-01-15"},
        {"test_name": "Access logging active", "passed": False, "weight": 0.6, "timestamp": "2025-01-15"},
    ]
    control = score_control(test_results)
    print(f"Control Score: {control['score']}% — {control['status']}")
    print(f"Tests: {control['tests_passed']}/{control['tests_total']} passed")

    dashboard = generate_compliance_dashboard(
        "Sentinel Compliance Group",
        {"GDPR": {"score": 96, "controls_total": 180, "controls_compliant": 173},
         "CCPA/CPRA": {"score": 93, "controls_total": 85, "controls_compliant": 79}},
        [
            {"id": "DEV-001", "control": "Vendor DPA Renewal", "severity": "high", "days_open": 12, "owner": "Procurement"},
            {"id": "DEV-002", "control": "DSAR SLA LGPD", "severity": "medium", "days_open": 5, "owner": "Privacy Ops"},
        ],
    )
    print(f"\nOverall Compliance: {dashboard['overall_compliance']['score']}%")
    print(f"Open Deviations: {dashboard['deviations']['total_open']}")
