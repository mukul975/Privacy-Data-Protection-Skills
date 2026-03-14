#!/usr/bin/env python3
"""Prior Consultation Process Management Engine.

Implements Art. 36 prior consultation workflow including documentation
checklist, timeline tracking, and outcome management.
"""

import json
from datetime import datetime, timedelta
from typing import Any

ART_36_3_DOCUMENTATION = [
    {"id": "DOC1", "description": "Complete DPIA report per Art. 35(7)", "mandatory": True},
    {"id": "DOC2", "description": "Controller and processor responsibilities", "mandatory": True},
    {"id": "DOC3", "description": "Technical, organisational, and contractual measures and safeguards", "mandatory": True},
    {"id": "DOC4", "description": "DPO contact details", "mandatory": True},
    {"id": "DOC5", "description": "Executive summary (1-2 pages)", "mandatory": False},
    {"id": "DOC6", "description": "Data flow diagram", "mandatory": False},
    {"id": "DOC7", "description": "Detailed risk register with residual risk levels", "mandatory": False},
    {"id": "DOC8", "description": "DPO advice letter per Art. 35(2)", "mandatory": False},
    {"id": "DOC9", "description": "Art. 35(9) data subject consultation evidence", "mandatory": False},
    {"id": "DOC10", "description": "Legitimate interest assessment (if Art. 6(1)(f))", "mandatory": False},
]


def check_consultation_requirement(
    residual_risk_level: str,
) -> dict[str, Any]:
    """Determine whether prior consultation is required based on residual risk."""
    recommendations = {
        "low": {"required": False, "recommendation": "No prior consultation needed. Processing may proceed."},
        "medium": {"required": False, "recommendation": "No prior consultation required. DPO should document risk acceptance rationale."},
        "high": {"required": True, "recommendation": "Prior consultation recommended. Processing should not proceed without SA review."},
        "very_high": {"required": True, "recommendation": "Prior consultation mandatory under Art. 36(1). Processing must not proceed."},
    }
    rec = recommendations.get(residual_risk_level.lower(), recommendations["high"])
    return {
        "residual_risk_level": residual_risk_level,
        "prior_consultation_required": rec["required"],
        "recommendation": rec["recommendation"],
    }


def prepare_documentation_checklist(
    documents_ready: dict[str, bool],
) -> dict[str, Any]:
    """Verify completeness of Art. 36(3) documentation package."""
    results = []
    for doc in ART_36_3_DOCUMENTATION:
        ready = documents_ready.get(doc["id"], False)
        results.append({
            "id": doc["id"],
            "description": doc["description"],
            "mandatory": doc["mandatory"],
            "ready": ready,
            "status": "Complete" if ready else ("Missing — mandatory" if doc["mandatory"] else "Missing — recommended"),
        })

    mandatory_missing = [r for r in results if r["mandatory"] and not r["ready"]]
    submission_ready = len(mandatory_missing) == 0

    return {
        "documents": results,
        "total": len(results),
        "complete": len([r for r in results if r["ready"]]),
        "mandatory_missing": len(mandatory_missing),
        "submission_ready": submission_ready,
        "action": (
            "Documentation package is complete. Ready for submission."
            if submission_ready
            else f"{len(mandatory_missing)} mandatory document(s) missing. "
            "Complete before submission."
        ),
    }


def track_consultation_timeline(
    submission_date: str,
    extension_notified: bool = False,
    information_request_dates: list[str] | None = None,
    information_response_dates: list[str] | None = None,
) -> dict[str, Any]:
    """Track Art. 36(2) consultation timeline."""
    sub_date = datetime.strptime(submission_date, "%Y-%m-%d")
    standard_deadline = sub_date + timedelta(weeks=8)
    extended_deadline = sub_date + timedelta(weeks=14) if extension_notified else None

    pause_days = 0
    if information_request_dates and information_response_dates:
        for req, resp in zip(information_request_dates, information_response_dates):
            req_date = datetime.strptime(req, "%Y-%m-%d")
            resp_date = datetime.strptime(resp, "%Y-%m-%d")
            pause_days += (resp_date - req_date).days

    effective_deadline = (
        (extended_deadline or standard_deadline) + timedelta(days=pause_days)
    )

    days_remaining = (effective_deadline - datetime.now()).days

    return {
        "submission_date": submission_date,
        "standard_deadline": standard_deadline.strftime("%Y-%m-%d"),
        "extension_notified": extension_notified,
        "extended_deadline": extended_deadline.strftime("%Y-%m-%d") if extended_deadline else None,
        "pause_days": pause_days,
        "effective_deadline": effective_deadline.strftime("%Y-%m-%d"),
        "days_remaining": max(days_remaining, 0),
        "deadline_passed": days_remaining < 0,
    }


def run_example() -> dict[str, Any]:
    """Run example prior consultation tracking."""
    requirement = check_consultation_requirement("high")

    docs = prepare_documentation_checklist({
        "DOC1": True, "DOC2": True, "DOC3": True, "DOC4": True,
        "DOC5": True, "DOC6": True, "DOC7": True, "DOC8": True,
        "DOC9": True, "DOC10": False,
    })

    timeline = track_consultation_timeline(
        submission_date="2026-02-15",
        extension_notified=False,
        information_request_dates=["2026-03-01"],
        information_response_dates=["2026-03-05"],
    )

    return {
        "reference": "PC-QLH-2026-0001",
        "organisation": "QuantumLeap Health Technologies",
        "dpia_reference": "DPIA-QLH-2026-0003",
        "processing": "Patient Data Analytics Platform — genetic data component",
        "supervisory_authority": "Berliner Beauftragte fur Datenschutz und Informationsfreiheit",
        "requirement_assessment": requirement,
        "documentation_checklist": docs,
        "timeline": timeline,
    }


if __name__ == "__main__":
    result = run_example()
    print(json.dumps(result, indent=2, default=str))
