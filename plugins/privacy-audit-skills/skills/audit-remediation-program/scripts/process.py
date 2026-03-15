#!/usr/bin/env python3
"""
Audit Remediation Program Processor

Manages finding lifecycle, prioritization, deadline tracking,
verification testing, and management reporting for audit remediation programs.
"""

import json
import os
from datetime import datetime, timedelta
from typing import Any

SEVERITY_CONFIG = {
    "critical": {"deadline_days": 30, "response_days": 10, "escalation_days": [5, 15, 15]},
    "high": {"deadline_days": 60, "response_days": 10, "escalation_days": [10, 30, 45]},
    "medium": {"deadline_days": 90, "response_days": 10, "escalation_days": [30, 60, 60]},
    "low": {"deadline_days": 180, "response_days": 10, "escalation_days": [90, 150, 150]},
    "advisory": {"deadline_days": None, "response_days": None, "escalation_days": []},
}

PRIORITY_WEIGHTS = {
    "severity": 0.40,
    "regulatory_exposure": 0.20,
    "data_subject_impact": 0.15,
    "systemic_risk": 0.10,
    "recurrence": 0.10,
    "external_visibility": 0.05,
}


def calculate_priority_score(factors: dict[str, int]) -> float:
    """
    Calculate multi-factor priority score for a finding.

    Args:
        factors: Dict mapping factor names to scores (1-5).

    Returns:
        Weighted priority score (1.0 to 5.0).
    """
    total = 0.0
    total_weight = 0.0
    for factor, weight in PRIORITY_WEIGHTS.items():
        score = factors.get(factor, 1)
        score = max(1, min(5, score))
        total += score * weight
        total_weight += weight
    return round(total / total_weight, 1) if total_weight > 0 else 1.0


def register_finding(
    finding_id: str,
    title: str,
    severity: str,
    source: str,
    condition: str,
    criteria: str,
    cause: str,
    consequence: str,
    recommendation: str,
    priority_factors: dict[str, int] | None = None,
) -> dict[str, Any]:
    """
    Register a new audit finding.

    Args:
        finding_id: Unique finding identifier.
        title: Finding title.
        severity: Severity level (critical/high/medium/low/advisory).
        source: Finding source (internal_audit, soc2, iso27701, dpa, self_assessment).
        condition: What was found.
        criteria: What should be happening.
        cause: Why it happened.
        consequence: What is the risk.
        recommendation: Recommended remediation.
        priority_factors: Optional priority scoring factors.

    Returns:
        Registered finding record.
    """
    severity_config = SEVERITY_CONFIG.get(severity, SEVERITY_CONFIG["medium"])
    registered_date = datetime.now()

    target_date = None
    if severity_config["deadline_days"]:
        target_date = (registered_date + timedelta(days=severity_config["deadline_days"])).strftime("%Y-%m-%d")

    response_due = None
    if severity_config["response_days"]:
        response_due = (registered_date + timedelta(days=severity_config["response_days"])).strftime("%Y-%m-%d")

    priority_score = None
    if priority_factors:
        priority_score = calculate_priority_score(priority_factors)

    return {
        "finding_id": finding_id,
        "title": title,
        "severity": severity,
        "source": source,
        "status": "new",
        "registered_date": registered_date.strftime("%Y-%m-%d"),
        "management_response_due": response_due,
        "target_date": target_date,
        "priority_score": priority_score,
        "condition": condition,
        "criteria": criteria,
        "cause": cause,
        "consequence": consequence,
        "recommendation": recommendation,
        "finding_owner": "",
        "remediation_owner": "",
        "management_response": "",
        "actual_close_date": None,
        "verification_result": None,
    }


def generate_remediation_dashboard(
    findings: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Generate remediation tracking dashboard.

    Args:
        findings: List of finding records.

    Returns:
        Dashboard data.
    """
    today = datetime.now().date()

    total_open = 0
    by_severity = {"critical": 0, "high": 0, "medium": 0, "low": 0, "advisory": 0}
    overdue = 0
    closed_this_month = 0
    total_closed = 0
    on_time_closed = 0

    for f in findings:
        status = f.get("status", "new")

        if status in ("new", "in_progress", "pending_verification"):
            total_open += 1
            sev = f.get("severity", "medium")
            by_severity[sev] = by_severity.get(sev, 0) + 1

            target = f.get("target_date")
            if target:
                try:
                    if datetime.strptime(target, "%Y-%m-%d").date() < today:
                        overdue += 1
                except ValueError:
                    pass

        elif status == "closed":
            total_closed += 1
            close_date = f.get("actual_close_date", "")
            target = f.get("target_date", "")
            if close_date:
                try:
                    cd = datetime.strptime(close_date, "%Y-%m-%d").date()
                    if cd.month == today.month and cd.year == today.year:
                        closed_this_month += 1
                    if target and close_date <= target:
                        on_time_closed += 1
                except ValueError:
                    pass

    on_time_rate = round(on_time_closed / total_closed * 100, 1) if total_closed > 0 else 0

    avg_days = 0
    closed_with_dates = [
        f for f in findings
        if f.get("status") == "closed" and f.get("registered_date") and f.get("actual_close_date")
    ]
    if closed_with_dates:
        total_days = sum(
            (datetime.strptime(f["actual_close_date"], "%Y-%m-%d") -
             datetime.strptime(f["registered_date"], "%Y-%m-%d")).days
            for f in closed_with_dates
        )
        avg_days = round(total_days / len(closed_with_dates), 0)

    return {
        "dashboard_date": today.isoformat(),
        "summary": {
            "total_open": total_open,
            "by_severity": by_severity,
            "overdue": overdue,
            "closed_this_month": closed_this_month,
            "total_closed": total_closed,
            "on_time_rate": on_time_rate,
            "avg_days_to_close": avg_days,
        },
        "overdue_findings": [
            f for f in findings
            if f.get("status") in ("new", "in_progress", "pending_verification")
            and f.get("target_date")
            and datetime.strptime(f["target_date"], "%Y-%m-%d").date() < today
        ],
    }


def check_escalation(finding: dict[str, Any]) -> dict[str, Any] | None:
    """
    Check if a finding requires escalation.

    Args:
        finding: Finding record.

    Returns:
        Escalation action if needed, None otherwise.
    """
    status = finding.get("status", "new")
    if status == "closed":
        return None

    severity = finding.get("severity", "medium")
    config = SEVERITY_CONFIG.get(severity, SEVERITY_CONFIG["medium"])

    if not config["escalation_days"]:
        return None

    registered = finding.get("registered_date", "")
    if not registered:
        return None

    try:
        reg_date = datetime.strptime(registered, "%Y-%m-%d").date()
        days_open = (datetime.now().date() - reg_date).days
    except ValueError:
        return None

    target = finding.get("target_date", "")
    days_overdue = 0
    if target:
        try:
            target_date = datetime.strptime(target, "%Y-%m-%d").date()
            if datetime.now().date() > target_date:
                days_overdue = (datetime.now().date() - target_date).days
        except ValueError:
            pass

    if days_overdue > 0:
        if severity in ("critical", "high"):
            return {
                "finding_id": finding["finding_id"],
                "severity": severity,
                "days_overdue": days_overdue,
                "action": f"Escalate to {'CEO and Board' if severity == 'critical' else 'Audit Committee'}",
                "urgency": "immediate",
            }
        else:
            return {
                "finding_id": finding["finding_id"],
                "severity": severity,
                "days_overdue": days_overdue,
                "action": "Escalate to management",
                "urgency": "within 3 business days",
            }

    return None


if __name__ == "__main__":
    finding = register_finding(
        finding_id="RA-2025-017",
        title="Incomplete vendor sub-processor notification",
        severity="high",
        source="internal_audit",
        condition="14 of 47 processor DPAs had outdated sub-processor lists",
        criteria="Art. 28(2) requires prior notification of sub-processor changes",
        cause="No operational workflow for sub-processor change management",
        consequence="Risk of unauthorized sub-processing; GDPR Art. 28 non-compliance",
        recommendation="Implement sub-processor change notification workflow",
        priority_factors={"severity": 4, "regulatory_exposure": 5, "data_subject_impact": 3,
                         "systemic_risk": 4, "recurrence": 2, "external_visibility": 2},
    )

    print(f"Finding: {finding['finding_id']} — {finding['title']}")
    print(f"Severity: {finding['severity']}")
    print(f"Priority Score: {finding['priority_score']}")
    print(f"Target Date: {finding['target_date']}")
    print(f"Response Due: {finding['management_response_due']}")
