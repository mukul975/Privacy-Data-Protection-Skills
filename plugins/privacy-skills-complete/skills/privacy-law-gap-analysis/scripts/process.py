#!/usr/bin/env python3
"""
Privacy Law Gap Analysis Tool

Conducts gap analysis for market entry into new jurisdictions,
maps existing controls to target requirements, identifies gaps,
and generates remediation plans with effort estimates.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


GAP_CLASSIFICATIONS = {
    "critical": {"priority": "P1", "remediation_before": "market_entry", "color": "RED"},
    "significant": {"priority": "P2", "remediation_days": 90, "color": "AMBER"},
    "minor": {"priority": "P3", "remediation_days": 180, "color": "YELLOW"},
    "enhancement": {"priority": "P4", "remediation_days": 365, "color": "GREEN"},
}

COMPLIANCE_DOMAINS = [
    "lawful_basis", "individual_rights", "consent_management",
    "notice_transparency", "cross_border_transfers", "dpo_governance",
    "breach_notification", "impact_assessment", "security_safeguards",
    "retention_deletion", "enforcement_penalties", "record_keeping",
]

EFFORT_ESTIMATES = {
    "small": {"weeks_min": 1, "weeks_max": 2, "fte_days": 10},
    "medium": {"weeks_min": 2, "weeks_max": 6, "fte_days": 30},
    "large": {"weeks_min": 6, "weeks_max": 16, "fte_days": 80},
}


def conduct_gap_analysis(
    target_jurisdiction: str,
    target_law: str,
    requirements: list,
    current_controls: list,
) -> dict:
    """Conduct a gap analysis between target requirements and current controls."""
    gaps = []
    fully_met = []
    partially_met = []
    not_applicable = []

    for req in requirements:
        req_id = req.get("id", "unknown")
        domain = req.get("domain", "unknown")
        description = req.get("description", "")
        matching_control = None

        for ctrl in current_controls:
            if ctrl.get("domain") == domain and ctrl.get("covers_requirement") == req_id:
                matching_control = ctrl
                break

        if matching_control:
            coverage = matching_control.get("coverage", "none")
            if coverage == "full":
                fully_met.append({"requirement": req_id, "domain": domain, "description": description})
            elif coverage == "partial":
                partially_met.append({
                    "requirement": req_id, "domain": domain, "description": description,
                    "existing_control": matching_control.get("name"),
                    "gap_description": matching_control.get("gap_note", "Enhancement needed"),
                })
            else:
                gaps.append({
                    "requirement": req_id, "domain": domain, "description": description,
                    "classification": "significant",
                })
        else:
            if req.get("applicable", True):
                gaps.append({
                    "requirement": req_id, "domain": domain, "description": description,
                    "classification": "critical",
                })
            else:
                not_applicable.append({"requirement": req_id, "domain": domain})

    total = len(requirements)
    return {
        "target_jurisdiction": target_jurisdiction,
        "target_law": target_law,
        "analysis_date": datetime.utcnow().isoformat(),
        "total_requirements": total,
        "fully_met": len(fully_met),
        "partially_met": len(partially_met),
        "gaps": len(gaps),
        "not_applicable": len(not_applicable),
        "compliance_rate": round(len(fully_met) / total * 100, 1) if total > 0 else 0,
        "gap_details": gaps,
        "partial_details": partially_met,
        "met_details": fully_met,
    }


def generate_remediation_plan(
    gaps: list,
    market_entry_date: str,
) -> dict:
    """Generate a remediation plan with effort estimates and timeline."""
    entry_date = datetime.strptime(market_entry_date, "%Y-%m-%d")
    plan_items = []

    for gap in gaps:
        classification = gap.get("classification", "significant")
        class_info = GAP_CLASSIFICATIONS.get(classification, GAP_CLASSIFICATIONS["significant"])

        if classification == "critical":
            deadline = entry_date
        else:
            deadline = entry_date + timedelta(days=class_info.get("remediation_days", 90))

        effort = gap.get("effort", "medium")
        effort_info = EFFORT_ESTIMATES.get(effort, EFFORT_ESTIMATES["medium"])

        plan_items.append({
            "gap_id": gap.get("requirement", "unknown"),
            "domain": gap.get("domain"),
            "description": gap.get("description"),
            "priority": class_info["priority"],
            "classification": classification,
            "deadline": deadline.strftime("%Y-%m-%d"),
            "effort_weeks": f"{effort_info['weeks_min']}-{effort_info['weeks_max']}",
            "effort_fte_days": effort_info["fte_days"],
            "status": "planned",
        })

    plan_items.sort(key=lambda x: (
        {"P1": 0, "P2": 1, "P3": 2, "P4": 3}.get(x["priority"], 4),
        x["deadline"],
    ))

    total_fte_days = sum(EFFORT_ESTIMATES.get(g.get("effort", "medium"), EFFORT_ESTIMATES["medium"])["fte_days"] for g in gaps)

    return {
        "market_entry_date": market_entry_date,
        "total_gaps": len(gaps),
        "total_effort_fte_days": total_fte_days,
        "critical_gaps": sum(1 for g in gaps if g.get("classification") == "critical"),
        "plan_items": plan_items,
        "generated_date": datetime.utcnow().isoformat(),
    }


def assess_market_readiness(
    gap_analysis: dict,
    remediation_status: dict,
) -> dict:
    """Assess whether the organisation is ready for market entry."""
    total_gaps = gap_analysis.get("gaps", 0)
    critical_remediated = remediation_status.get("critical_remediated", 0)
    critical_total = remediation_status.get("critical_total", 0)
    significant_remediated = remediation_status.get("significant_remediated", 0)
    significant_total = remediation_status.get("significant_total", 0)

    critical_clear = critical_remediated >= critical_total
    significant_progress = significant_remediated >= (significant_total * 0.5) if significant_total > 0 else True

    ready = critical_clear and significant_progress

    return {
        "market_ready": ready,
        "critical_gaps": {"total": critical_total, "remediated": critical_remediated, "clear": critical_clear},
        "significant_gaps": {"total": significant_total, "remediated": significant_remediated, "fifty_pct": significant_progress},
        "recommendation": "Proceed with market entry" if ready else "Defer market entry until critical gaps are remediated",
        "residual_risks": [] if critical_clear else ["Critical compliance gaps remain unremediated"],
        "assessment_date": datetime.utcnow().isoformat(),
    }


if __name__ == "__main__":
    print("=== Gap Analysis Example ===")
    requirements = [
        {"id": "VN-001", "domain": "cross_border_transfers", "description": "File transfer impact dossier with MPS", "applicable": True},
        {"id": "VN-002", "domain": "breach_notification", "description": "72-hour notification to MPS", "applicable": True},
        {"id": "VN-003", "domain": "notice_transparency", "description": "Privacy notice in Vietnamese", "applicable": True},
    ]
    controls = [
        {"domain": "breach_notification", "covers_requirement": "VN-002", "name": "72-hour global breach notification", "coverage": "full"},
    ]
    result = conduct_gap_analysis("Vietnam", "Decree 13/2023/ND-CP", requirements, controls)
    print(json.dumps(result, indent=2))

    print("\n=== Remediation Plan ===")
    plan = generate_remediation_plan(result["gap_details"], "2026-06-01")
    print(json.dumps(plan, indent=2))
