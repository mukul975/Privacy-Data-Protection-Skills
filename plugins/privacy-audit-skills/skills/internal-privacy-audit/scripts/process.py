#!/usr/bin/env python3
"""
Internal Privacy Audit Program Processor

Manages audit universe risk scoring, annual plan generation, finding tracking,
and remediation monitoring for internal privacy audit programs.
"""

import json
import os
from datetime import datetime, timedelta
from typing import Any


RISK_FACTORS = {
    "regulatory_exposure": {"weight": 0.25, "max": 5},
    "data_volume": {"weight": 0.20, "max": 5},
    "prior_findings": {"weight": 0.15, "max": 5},
    "organizational_change": {"weight": 0.15, "max": 5},
    "third_party_dependency": {"weight": 0.10, "max": 5},
    "incident_history": {"weight": 0.10, "max": 5},
    "time_since_last_audit": {"weight": 0.05, "max": 5},
}

FINDING_SEVERITY = {
    "critical": {"response_days": 30, "label": "Critical"},
    "high": {"response_days": 60, "label": "High"},
    "medium": {"response_days": 90, "label": "Medium"},
    "low": {"response_days": 180, "label": "Low"},
    "advisory": {"response_days": None, "label": "Advisory"},
}

AUDIT_FREQUENCY = {
    (4.0, 5.0): "Every 6 months",
    (3.0, 3.9): "Annual",
    (2.0, 2.9): "Every 18 months",
    (1.0, 1.9): "Every 24 months",
}


def calculate_risk_score(risk_factors: dict[str, int]) -> float:
    """
    Calculate weighted risk score for an auditable area.

    Args:
        risk_factors: Dict mapping factor names to scores (1-5).

    Returns:
        Weighted risk score (1.0 to 5.0).
    """
    total_score = 0.0
    total_weight = 0.0

    for factor_name, factor_config in RISK_FACTORS.items():
        score = risk_factors.get(factor_name, 1)
        score = max(1, min(score, factor_config["max"]))
        total_score += score * factor_config["weight"]
        total_weight += factor_config["weight"]

    return round(total_score / total_weight if total_weight > 0 else 1.0, 1)


def determine_audit_frequency(risk_score: float) -> str:
    """Determine recommended audit frequency based on risk score."""
    for (low, high), frequency in AUDIT_FREQUENCY.items():
        if low <= risk_score <= high:
            return frequency
    return "Every 24 months"


def generate_annual_plan(
    audit_universe: list[dict[str, Any]],
    available_hours: int,
    year: int,
) -> dict[str, Any]:
    """
    Generate annual privacy audit plan from risk-scored audit universe.

    Args:
        audit_universe: List of auditable areas with risk scores.
        available_hours: Total available audit hours for the year.
        year: Plan year.

    Returns:
        Annual audit plan.
    """
    scored_areas = []
    for area in audit_universe:
        risk_score = calculate_risk_score(area.get("risk_factors", {}))
        frequency = determine_audit_frequency(risk_score)
        scored_areas.append({
            **area,
            "risk_score": risk_score,
            "recommended_frequency": frequency,
            "estimated_hours": area.get("estimated_hours", 80),
        })

    scored_areas.sort(key=lambda x: x["risk_score"], reverse=True)

    quarterly_plan = {f"Q{q}": [] for q in range(1, 5)}
    hours_allocated = 0
    contingency_hours = int(available_hours * 0.1)
    usable_hours = available_hours - contingency_hours

    quarter = 1
    for area in scored_areas:
        if hours_allocated + area["estimated_hours"] > usable_hours:
            break
        quarterly_plan[f"Q{quarter}"].append({
            "area": area["name"],
            "risk_score": area["risk_score"],
            "estimated_hours": area["estimated_hours"],
            "last_audit": area.get("last_audit_date", "Never"),
        })
        hours_allocated += area["estimated_hours"]
        quarter = (quarter % 4) + 1

    return {
        "metadata": {
            "year": year,
            "approval_date": "",
            "approved_by": "Audit Committee",
            "total_hours": available_hours,
            "allocated_hours": hours_allocated,
            "contingency_hours": contingency_hours,
        },
        "risk_scored_universe": scored_areas,
        "quarterly_plan": quarterly_plan,
        "deferred_areas": [
            a for a in scored_areas
            if not any(
                a["name"] == s["area"]
                for q in quarterly_plan.values()
                for s in q
            )
        ],
    }


def track_findings(
    findings: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Generate finding tracking dashboard from a list of findings.

    Args:
        findings: List of finding dictionaries with keys:
            - id, title, severity, status, registered_date, target_date,
              actual_close_date, owner, source

    Returns:
        Finding tracking dashboard.
    """
    today = datetime.now().date()
    summary = {
        "total_open": 0,
        "by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "advisory": 0},
        "overdue": 0,
        "closed_this_month": 0,
        "on_time_rate": 0,
    }

    open_findings = []
    closed_findings = []
    overdue_findings = []

    for finding in findings:
        status = finding.get("status", "open")
        severity = finding.get("severity", "medium")

        if status in ("open", "in_progress", "pending_verification"):
            summary["total_open"] += 1
            summary["by_severity"][severity] = summary["by_severity"].get(severity, 0) + 1
            open_findings.append(finding)

            target_date_str = finding.get("target_date", "")
            if target_date_str:
                try:
                    target_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()
                    if target_date < today:
                        summary["overdue"] += 1
                        overdue_findings.append(finding)
                except ValueError:
                    pass

        elif status == "closed":
            closed_findings.append(finding)
            close_date_str = finding.get("actual_close_date", "")
            if close_date_str:
                try:
                    close_date = datetime.strptime(close_date_str, "%Y-%m-%d").date()
                    if close_date.month == today.month and close_date.year == today.year:
                        summary["closed_this_month"] += 1
                except ValueError:
                    pass

    on_time_closed = sum(
        1 for f in closed_findings
        if f.get("actual_close_date") and f.get("target_date")
        and f["actual_close_date"] <= f["target_date"]
    )
    total_closed = len(closed_findings)
    summary["on_time_rate"] = round(
        on_time_closed / total_closed * 100, 1
    ) if total_closed > 0 else 0

    return {
        "dashboard_date": today.isoformat(),
        "summary": summary,
        "open_findings": open_findings,
        "overdue_findings": overdue_findings,
        "closed_findings_count": total_closed,
    }


def calculate_sample_size(
    population: int,
    confidence: float = 0.95,
    expected_error: float = 0.0,
) -> int:
    """
    Calculate audit sample size for attribute sampling.

    Args:
        population: Total population size.
        confidence: Confidence level (default 0.95).
        expected_error: Expected error rate (default 0.0).

    Returns:
        Recommended sample size.
    """
    if population <= 0:
        return 0
    if population <= 50:
        return population

    if expected_error <= 0.05:
        if population <= 250:
            return 30 if confidence >= 0.95 else 25
        elif population <= 1000:
            return 50 if confidence >= 0.95 else 40
        else:
            return 60 if confidence >= 0.95 else 45
    else:
        base = 60 if confidence >= 0.95 else 45
        adjustment = int(expected_error * 100)
        return min(base + adjustment * 5, population)


if __name__ == "__main__":
    universe = [
        {
            "name": "DSAR Response Process",
            "risk_factors": {
                "regulatory_exposure": 5,
                "data_volume": 4,
                "prior_findings": 3,
                "organizational_change": 2,
                "third_party_dependency": 1,
                "incident_history": 2,
                "time_since_last_audit": 3,
            },
            "estimated_hours": 120,
            "last_audit_date": "2024-06-15",
        },
        {
            "name": "Third-Party Processor Management",
            "risk_factors": {
                "regulatory_exposure": 5,
                "data_volume": 4,
                "prior_findings": 4,
                "organizational_change": 3,
                "third_party_dependency": 5,
                "incident_history": 2,
                "time_since_last_audit": 4,
            },
            "estimated_hours": 160,
            "last_audit_date": "2023-12-01",
        },
        {
            "name": "Data Retention and Deletion",
            "risk_factors": {
                "regulatory_exposure": 4,
                "data_volume": 5,
                "prior_findings": 3,
                "organizational_change": 2,
                "third_party_dependency": 2,
                "incident_history": 1,
                "time_since_last_audit": 3,
            },
            "estimated_hours": 100,
            "last_audit_date": "2024-06-15",
        },
    ]

    plan = generate_annual_plan(universe, 1200, 2025)

    print("Privacy Audit Annual Plan 2025")
    print(f"Total Hours: {plan['metadata']['total_hours']}")
    print(f"Allocated: {plan['metadata']['allocated_hours']}")
    print(f"Contingency: {plan['metadata']['contingency_hours']}")
    print()

    for area in plan["risk_scored_universe"]:
        print(f"  {area['name']}: Risk Score {area['risk_score']} — {area['recommended_frequency']}")

    for quarter, audits in plan["quarterly_plan"].items():
        if audits:
            print(f"\n{quarter}:")
            for audit in audits:
                print(f"  - {audit['area']} (Risk: {audit['risk_score']}, Hours: {audit['estimated_hours']})")
