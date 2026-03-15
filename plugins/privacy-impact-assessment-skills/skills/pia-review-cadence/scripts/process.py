#!/usr/bin/env python3
"""PIA Review and Update Cadence Management Engine.

Implements DPIA review lifecycle management including trigger detection,
review scheduling, version control, and register management.
"""

import json
from datetime import datetime, timedelta
from typing import Any

REVIEW_INTERVALS = {
    "very_high": {"months": 6, "label": "Every 6 months"},
    "high": {"months": 12, "label": "Every 12 months"},
    "medium": {"months": 12, "label": "Every 12 months"},
    "low": {"months": 24, "label": "Every 24 months"},
}

TRIGGER_CATEGORIES = {
    "regulatory": {
        "name": "Regulatory Triggers",
        "triggers": [
            "New EDPB or national SA guidance",
            "Adequacy decision change",
            "National SA DPIA list updated",
            "New sector-specific legislation",
            "Enforcement decision against similar processing",
        ],
    },
    "processing_change": {
        "name": "Processing Change Triggers",
        "triggers": [
            "New data category",
            "New data subject category",
            "New recipient or processor",
            "Lawful basis change",
            "Retention period change",
            "New purpose for existing data",
            "Volume increase",
            "Geographic expansion",
        ],
    },
    "technology_change": {
        "name": "Technology Change Triggers",
        "triggers": [
            "New system deployment",
            "System upgrade or migration",
            "New algorithm or AI model",
            "New tracking technology",
            "Security vulnerability discovered",
            "System end-of-life",
        ],
    },
    "incident": {
        "name": "Incident Triggers",
        "triggers": [
            "Personal data breach",
            "Near-miss security incident",
            "Data subject complaint",
            "Supervisory authority enquiry",
            "Internal audit finding",
        ],
    },
    "organisational": {
        "name": "Organisational Change Triggers",
        "triggers": [
            "Merger, acquisition, or divestiture",
            "DPO change",
            "Staff restructuring",
            "New business unit using the processing",
        ],
    },
}


def calculate_next_review_date(
    risk_level: str,
    last_review_date: str | None = None,
) -> dict[str, Any]:
    """Calculate the next review date based on risk level.

    Args:
        risk_level: Current risk level (very_high, high, medium, low)
        last_review_date: ISO format date of last review, or None for new DPIA

    Returns:
        Next review date and interval information
    """
    interval = REVIEW_INTERVALS.get(risk_level, REVIEW_INTERVALS["medium"])
    base_date = (
        datetime.strptime(last_review_date, "%Y-%m-%d")
        if last_review_date
        else datetime.now()
    )
    next_date = base_date + timedelta(days=interval["months"] * 30)

    overdue = next_date < datetime.now()

    return {
        "risk_level": risk_level,
        "review_interval": interval["label"],
        "last_review_date": last_review_date or datetime.now().strftime("%Y-%m-%d"),
        "next_review_date": next_date.strftime("%Y-%m-%d"),
        "overdue": overdue,
        "days_until_review": (next_date - datetime.now()).days if not overdue else 0,
        "days_overdue": (datetime.now() - next_date).days if overdue else 0,
    }


def assess_trigger_event(
    trigger_category: str,
    trigger_description: str,
    affected_dpia_references: list[str],
    severity: str,
) -> dict[str, Any]:
    """Assess a trigger event and determine review scope.

    Args:
        trigger_category: Category key (regulatory, processing_change, etc.)
        trigger_description: Description of the trigger event
        affected_dpia_references: List of DPIA references affected
        severity: Impact severity (critical, major, minor)

    Returns:
        Trigger assessment with recommended action
    """
    category = TRIGGER_CATEGORIES.get(trigger_category, {})

    review_scope = {
        "critical": "full",
        "major": "full",
        "minor": "targeted",
    }

    escalation = {
        "critical": "Immediate review required. Notify senior management. Consider pausing processing.",
        "major": "Review within 30 days. Notify DPO and processing owner.",
        "minor": "Include in next scheduled review. Log in DPIA register.",
    }

    return {
        "trigger_date": datetime.now().strftime("%Y-%m-%d"),
        "trigger_category": category.get("name", trigger_category),
        "trigger_description": trigger_description,
        "affected_dpias": affected_dpia_references,
        "severity": severity,
        "review_scope": review_scope.get(severity, "targeted"),
        "escalation_action": escalation.get(severity, "Include in next scheduled review."),
    }


def generate_dpia_register_entry(
    reference: str,
    processing_name: str,
    version: str,
    status: str,
    risk_level: str,
    processing_owner: str,
    dpo_reviewer: str,
    prior_consultation: bool,
    last_review: str,
) -> dict[str, Any]:
    """Generate a DPIA register entry."""
    review_info = calculate_next_review_date(risk_level, last_review)

    return {
        "reference": reference,
        "processing_name": processing_name,
        "version": version,
        "status": status,
        "risk_level": risk_level,
        "processing_owner": processing_owner,
        "dpo_reviewer": dpo_reviewer,
        "prior_consultation_required": prior_consultation,
        "created_date": "2026-02-10",
        "last_review_date": last_review,
        "next_review_date": review_info["next_review_date"],
        "review_interval": review_info["review_interval"],
        "overdue": review_info["overdue"],
    }


def run_example() -> dict[str, Any]:
    """Generate example DPIA register for QuantumLeap Health Technologies."""
    register = [
        generate_dpia_register_entry(
            reference="DPIA-QLH-2026-0001",
            processing_name="Employee Workplace Monitoring System",
            version="1.0",
            status="Approved",
            risk_level="high",
            processing_owner="Marcus Chen, Head of HR Operations",
            dpo_reviewer="Dr. Elena Vasquez",
            prior_consultation=False,
            last_review="2026-02-10",
        ),
        generate_dpia_register_entry(
            reference="DPIA-QLH-2026-0008",
            processing_name="Secure Lab Fingerprint Access Control",
            version="1.0",
            status="Approved",
            risk_level="medium",
            processing_owner="Prof. Dr. Henrik Johansson",
            dpo_reviewer="Dr. Elena Vasquez",
            prior_consultation=False,
            last_review="2026-03-05",
        ),
    ]

    trigger = assess_trigger_event(
        trigger_category="technology_change",
        trigger_description="SAP SuccessFactors major version upgrade changing productivity metric calculation methodology",
        affected_dpia_references=["DPIA-QLH-2026-0001"],
        severity="major",
    )

    return {
        "organisation": "QuantumLeap Health Technologies",
        "register": register,
        "pending_triggers": [trigger],
        "total_dpias": len(register),
        "overdue_reviews": len([d for d in register if d["overdue"]]),
    }


if __name__ == "__main__":
    result = run_example()
    print(json.dumps(result, indent=2, default=str))
