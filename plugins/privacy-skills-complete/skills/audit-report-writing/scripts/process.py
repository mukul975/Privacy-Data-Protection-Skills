#!/usr/bin/env python3
"""
Privacy Audit Report Writing Tool

Generates structured audit report components including findings classification,
executive summary statistics, and report quality validation.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


SEVERITY_LEVELS = {
    "critical": {
        "response_days": 1,
        "board_notification": True,
        "description": "Material non-compliance creating immediate risk of regulatory enforcement or harm to data subjects",
    },
    "high": {
        "response_days": 14,
        "board_notification": False,
        "description": "Significant control weakness that could lead to breach or regulatory action",
    },
    "medium": {
        "response_days": 90,
        "board_notification": False,
        "description": "Control deficiency not posing immediate risk but could deteriorate",
    },
    "low": {
        "response_days": 180,
        "board_notification": False,
        "description": "Opportunity for improvement; minor procedural gap",
    },
}

REQUIRED_FINDING_FIELDS = [
    "finding_id",
    "title",
    "condition",
    "criteria",
    "cause",
    "effect",
    "severity",
    "recommendation",
]

REQUIRED_REPORT_SECTIONS = [
    "cover_page",
    "executive_summary",
    "scope_and_objectives",
    "methodology",
    "findings",
    "recommendations",
    "management_response",
    "appendices",
]


def classify_finding_severity(
    active_harm_to_subjects: bool,
    regulatory_enforcement_risk: bool,
    control_weakness_could_deteriorate: bool,
    improvement_opportunity_only: bool,
) -> dict:
    """Classify a finding's severity based on impact assessment criteria."""
    if active_harm_to_subjects:
        severity = "critical"
    elif regulatory_enforcement_risk:
        severity = "high"
    elif control_weakness_could_deteriorate:
        severity = "medium"
    elif improvement_opportunity_only:
        severity = "low"
    else:
        severity = "observation"

    result = {
        "severity": severity,
        "response_timeline_days": SEVERITY_LEVELS.get(severity, {}).get("response_days", None),
        "board_notification_required": SEVERITY_LEVELS.get(severity, {}).get("board_notification", False),
        "description": SEVERITY_LEVELS.get(severity, {}).get(
            "description", "Good practice note or suggestion; not a formal finding"
        ),
    }
    return result


def validate_finding(finding: dict) -> dict:
    """Validate that a finding record contains all required fields."""
    missing_fields = [f for f in REQUIRED_FINDING_FIELDS if f not in finding or not finding[f]]
    severity_valid = finding.get("severity", "") in list(SEVERITY_LEVELS.keys()) + ["observation"]

    issues = []
    if missing_fields:
        issues.append(f"Missing required fields: {', '.join(missing_fields)}")
    if not severity_valid:
        issues.append(f"Invalid severity: {finding.get('severity', 'not set')}. Must be one of: {', '.join(list(SEVERITY_LEVELS.keys()) + ['observation'])}")
    if finding.get("evidence_references") is not None and len(finding.get("evidence_references", [])) == 0:
        issues.append("Evidence references field is present but empty; at least one reference required")

    return {
        "finding_id": finding.get("finding_id", "unknown"),
        "valid": len(issues) == 0,
        "issues": issues,
    }


def generate_executive_summary_stats(findings: list) -> dict:
    """Generate statistics for the executive summary from a list of findings."""
    severity_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0, "observation": 0}
    for f in findings:
        sev = f.get("severity", "observation")
        if sev in severity_counts:
            severity_counts[sev] += 1

    total_findings = sum(severity_counts.values())
    total_formal = total_findings - severity_counts["observation"]

    if severity_counts["critical"] > 0:
        overall_opinion = "unsatisfactory"
    elif severity_counts["high"] > 0:
        overall_opinion = "needs_improvement"
    else:
        overall_opinion = "satisfactory"

    return {
        "total_findings": total_findings,
        "total_formal_findings": total_formal,
        "severity_distribution": severity_counts,
        "overall_opinion": overall_opinion,
        "board_notification_required": severity_counts["critical"] > 0,
        "immediate_action_items": severity_counts["critical"] + severity_counts["high"],
    }


def calculate_report_timeline(fieldwork_end_date: str, management_response_days: int = 5) -> dict:
    """Calculate key dates in the report production timeline."""
    fieldwork_end = datetime.strptime(fieldwork_end_date, "%Y-%m-%d")

    milestones = {
        "fieldwork_end": fieldwork_end_date,
        "report_planning_start": fieldwork_end.strftime("%Y-%m-%d"),
        "report_planning_end": (fieldwork_end + timedelta(days=2)).strftime("%Y-%m-%d"),
        "findings_drafting_end": (fieldwork_end + timedelta(days=6)).strftime("%Y-%m-%d"),
        "executive_summary_draft": (fieldwork_end + timedelta(days=7)).strftime("%Y-%m-%d"),
        "draft_to_management": (fieldwork_end + timedelta(days=7)).strftime("%Y-%m-%d"),
        "management_response_deadline": (fieldwork_end + timedelta(days=7 + management_response_days)).strftime("%Y-%m-%d"),
        "quality_review_end": (fieldwork_end + timedelta(days=7 + management_response_days + 2)).strftime("%Y-%m-%d"),
        "final_report_issuance": (fieldwork_end + timedelta(days=7 + management_response_days + 3)).strftime("%Y-%m-%d"),
    }

    return milestones


def validate_report_completeness(sections_present: list) -> dict:
    """Validate that an audit report contains all required sections."""
    missing = [s for s in REQUIRED_REPORT_SECTIONS if s not in sections_present]
    extra = [s for s in sections_present if s not in REQUIRED_REPORT_SECTIONS]

    return {
        "required_sections": REQUIRED_REPORT_SECTIONS,
        "sections_present": sections_present,
        "missing_sections": missing,
        "extra_sections": extra,
        "complete": len(missing) == 0,
        "completeness_pct": round((len(REQUIRED_REPORT_SECTIONS) - len(missing)) / len(REQUIRED_REPORT_SECTIONS) * 100, 1),
    }


if __name__ == "__main__":
    print("=== Finding Severity Classification ===")
    result = classify_finding_severity(
        active_harm_to_subjects=False,
        regulatory_enforcement_risk=True,
        control_weakness_could_deteriorate=True,
        improvement_opportunity_only=False,
    )
    print(json.dumps(result, indent=2))

    print("\n=== Finding Validation ===")
    sample_finding = {
        "finding_id": "AUDIT-2026-001",
        "title": "DSAR response exceeds 30-day deadline",
        "condition": "15 of 50 sampled DSARs exceeded the one-month response deadline",
        "criteria": "GDPR Article 12(3) — response within one month",
        "cause": "Manual triage process with no automated deadline tracking",
        "effect": "Regulatory risk; data subject complaints to supervisory authority",
        "severity": "high",
        "recommendation": "Implement automated DSAR tracking with escalation at day 20",
        "evidence_references": ["DOC-023", "ANA-005"],
    }
    validation = validate_finding(sample_finding)
    print(json.dumps(validation, indent=2))

    print("\n=== Executive Summary Statistics ===")
    findings = [
        {"severity": "high"},
        {"severity": "high"},
        {"severity": "medium"},
        {"severity": "medium"},
        {"severity": "medium"},
        {"severity": "low"},
        {"severity": "observation"},
    ]
    stats = generate_executive_summary_stats(findings)
    print(json.dumps(stats, indent=2))

    print("\n=== Report Timeline ===")
    timeline = calculate_report_timeline("2026-03-10")
    print(json.dumps(timeline, indent=2))

    print("\n=== Report Completeness ===")
    completeness = validate_report_completeness([
        "cover_page", "executive_summary", "scope_and_objectives",
        "methodology", "findings", "recommendations",
    ])
    print(json.dumps(completeness, indent=2))
