#!/usr/bin/env python3
"""
Privacy Program Metrics Processor

Calculates privacy program KPIs, generates executive dashboards,
performs benchmarking, and computes program ROI.
"""

import json
import os
from datetime import datetime
from typing import Any


def calculate_dsar_metrics(dsar_records: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Calculate DSAR operational metrics.

    Args:
        dsar_records: List of DSAR records with 'received_date', 'response_date',
                     'jurisdiction', 'status', 'denied'.

    Returns:
        DSAR metrics.
    """
    if not dsar_records:
        return {"volume": 0, "avg_response_days": 0, "sla_compliance": 0}

    total = len(dsar_records)
    completed = [r for r in dsar_records if r.get("status") == "completed"]
    denied = sum(1 for r in dsar_records if r.get("denied", False))

    response_days = []
    sla_met = 0
    for r in completed:
        if r.get("received_date") and r.get("response_date"):
            try:
                received = datetime.strptime(r["received_date"], "%Y-%m-%d")
                responded = datetime.strptime(r["response_date"], "%Y-%m-%d")
                days = (responded - received).days
                response_days.append(days)

                jurisdiction = r.get("jurisdiction", "GDPR")
                sla = 30 if jurisdiction == "GDPR" else 45
                if days <= sla:
                    sla_met += 1
            except ValueError:
                pass

    avg_days = round(sum(response_days) / len(response_days), 1) if response_days else 0
    sla_rate = round(sla_met / len(completed) * 100, 1) if completed else 0

    return {
        "volume": total,
        "completed": len(completed),
        "avg_response_days": avg_days,
        "sla_compliance_rate": sla_rate,
        "denial_rate": round(denied / total * 100, 1) if total > 0 else 0,
        "backlog": sum(1 for r in dsar_records if r.get("status") in ("open", "in_progress")),
    }


def calculate_incident_metrics(incidents: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Calculate privacy incident metrics.

    Args:
        incidents: List of incidents with 'severity', 'detection_time', 'containment_time',
                  'resolution_time', 'notified_dpa', 'notified_subjects'.

    Returns:
        Incident metrics.
    """
    if not incidents:
        return {"total": 0}

    by_severity = {}
    for inc in incidents:
        sev = inc.get("severity", "medium")
        by_severity[sev] = by_severity.get(sev, 0) + 1

    detection_times = [i.get("detection_hours", 0) for i in incidents if i.get("detection_hours")]
    containment_times = [i.get("containment_hours", 0) for i in incidents if i.get("containment_hours")]

    return {
        "total": len(incidents),
        "by_severity": by_severity,
        "mttd_hours": round(sum(detection_times) / len(detection_times), 1) if detection_times else 0,
        "mttc_hours": round(sum(containment_times) / len(containment_times), 1) if containment_times else 0,
        "dpa_notifications": sum(1 for i in incidents if i.get("notified_dpa")),
        "subject_notifications": sum(1 for i in incidents if i.get("notified_subjects")),
    }


def calculate_compliance_score(
    controls: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Calculate overall compliance score from control assessments.

    Args:
        controls: List of controls with 'regulation', 'compliant' (bool), 'weight' (float).

    Returns:
        Compliance metrics by regulation and overall.
    """
    by_regulation = {}
    for control in controls:
        reg = control.get("regulation", "General")
        if reg not in by_regulation:
            by_regulation[reg] = {"total": 0, "compliant": 0, "weighted_score": 0, "total_weight": 0}

        by_regulation[reg]["total"] += 1
        weight = control.get("weight", 1.0)
        by_regulation[reg]["total_weight"] += weight
        if control.get("compliant", False):
            by_regulation[reg]["compliant"] += 1
            by_regulation[reg]["weighted_score"] += weight

    results = {}
    for reg, data in by_regulation.items():
        score = round(data["weighted_score"] / data["total_weight"] * 100, 1) if data["total_weight"] > 0 else 0
        results[reg] = {
            "total_controls": data["total"],
            "compliant_controls": data["compliant"],
            "score": score,
        }

    overall_score = 0
    if results:
        overall_score = round(sum(r["score"] for r in results.values()) / len(results), 1)

    return {
        "overall_score": overall_score,
        "by_regulation": results,
    }


def calculate_program_roi(
    program_costs: dict[str, float],
    avoided_costs: dict[str, float],
    revenue_enabled: float = 0,
    efficiency_gains: float = 0,
) -> dict[str, Any]:
    """
    Calculate privacy program ROI.

    Args:
        program_costs: Dict of cost categories and amounts.
        avoided_costs: Dict of avoided cost categories and estimated amounts.
        revenue_enabled: Revenue enabled by privacy certification/compliance.
        efficiency_gains: Dollar value of efficiency improvements.

    Returns:
        ROI calculation.
    """
    total_cost = sum(program_costs.values())
    total_avoided = sum(avoided_costs.values())
    total_value = total_avoided + revenue_enabled + efficiency_gains
    roi = round((total_value - total_cost) / total_cost, 2) if total_cost > 0 else 0

    return {
        "total_program_cost": total_cost,
        "value_components": {
            "avoided_costs": total_avoided,
            "revenue_enabled": revenue_enabled,
            "efficiency_gains": efficiency_gains,
            "total_value": total_value,
        },
        "roi_ratio": roi,
        "roi_percentage": round(roi * 100, 1),
        "net_value": round(total_value - total_cost, 2),
    }


def generate_board_scorecard(
    metrics: dict[str, Any],
) -> dict[str, Any]:
    """
    Generate board-level privacy KPI scorecard.

    Args:
        metrics: Dict containing various metric results.

    Returns:
        Board scorecard data.
    """
    scorecard = {
        "generated_date": datetime.now().strftime("%Y-%m-%d"),
        "kpis": [],
    }

    kpi_definitions = [
        ("Overall Compliance Score", "compliance_score", "%", ">=95"),
        ("Material Privacy Incidents", "material_incidents", "count", "0"),
        ("Regulatory Fines", "regulatory_fines", "$", "$0"),
        ("DSAR SLA Compliance", "dsar_sla_rate", "%", "100%"),
        ("Risk Appetite Utilization", "risk_utilization", "%", "<80%"),
        ("Vendor DPA Coverage", "vendor_dpa_coverage", "%", "100%"),
        ("Training Completion", "training_completion", "%", ">=95%"),
        ("Maturity Score", "maturity_score", "score", ">=3.5"),
        ("Privacy Debt Score", "privacy_debt", "index", "declining"),
        ("Transfer Compliance", "transfer_compliance", "%", "100%"),
        ("DPIA Coverage", "dpia_coverage", "%", "100%"),
        ("Program ROI", "program_roi", "ratio", ">1.0x"),
    ]

    for name, key, unit, target in kpi_definitions:
        value = metrics.get(key, "N/A")
        scorecard["kpis"].append({
            "name": name,
            "value": value,
            "unit": unit,
            "target": target,
            "status": "met" if value != "N/A" else "no_data",
        })

    return scorecard


if __name__ == "__main__":
    roi = calculate_program_roi(
        program_costs={"staff": 1200000, "tools": 400000, "training": 100000, "external": 300000, "other": 400000},
        avoided_costs={"regulatory_fines": 2000000, "breach_costs": 1500000, "litigation": 500000},
        revenue_enabled=800000,
        efficiency_gains=300000,
    )
    print(f"Privacy Program ROI: {roi['roi_ratio']}x ({roi['roi_percentage']}%)")
    print(f"Total Cost: ${roi['total_program_cost']:,.0f}")
    print(f"Total Value: ${roi['value_components']['total_value']:,.0f}")
    print(f"Net Value: ${roi['net_value']:,.0f}")
