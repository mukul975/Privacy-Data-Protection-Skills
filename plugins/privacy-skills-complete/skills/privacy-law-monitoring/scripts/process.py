#!/usr/bin/env python3
"""
Privacy Law Change Monitoring and Impact Assessment Tool

Tracks regulatory changes across jurisdictions, classifies changes,
calculates impact scores, and generates implementation prioritisation.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


CHANGE_CLASSIFICATIONS = {
    "LAW-NEW": {"name": "New law enacted", "response_days": 90},
    "LAW-AMD": {"name": "Major amendment", "response_days": 60},
    "REG-GUID": {"name": "Regulatory guidance", "response_days": 30},
    "ENF-DEC": {"name": "Enforcement decision", "response_days": 14},
    "DRAFT-LEG": {"name": "Draft legislation", "response_days": None},
    "ADQ-DEC": {"name": "Adequacy decision", "response_days": 30},
    "INT-DEV": {"name": "International development", "response_days": 30},
}

IMPACT_DIMENSIONS = {
    "geographic_scope": {"weight": 0.25, "max": 5},
    "operational_change": {"weight": 0.30, "max": 5},
    "data_subject_volume": {"weight": 0.15, "max": 5},
    "enforcement_risk": {"weight": 0.20, "max": 5},
    "timeline_pressure": {"weight": 0.10, "max": 5},
}

IMPACT_CATEGORIES = {
    "critical": {"min_score": 4.0, "response": "Immediate project initiation"},
    "high": {"min_score": 3.0, "response": "Prioritised project within 30 days"},
    "medium": {"min_score": 2.0, "response": "Planned implementation within 90 days"},
    "low": {"min_score": 1.0, "response": "Next review cycle"},
}


def classify_change(
    jurisdiction: str,
    change_description: str,
    change_type: str,
    effective_date: Optional[str] = None,
) -> dict:
    """Classify a regulatory change and determine response timeline."""
    classification = CHANGE_CLASSIFICATIONS.get(change_type)
    if not classification:
        return {"error": f"Unknown type: {change_type}", "valid_types": list(CHANGE_CLASSIFICATIONS.keys())}

    response_deadline = None
    if classification["response_days"] and effective_date:
        eff_date = datetime.strptime(effective_date, "%Y-%m-%d")
        response_deadline = min(
            eff_date,
            datetime.utcnow() + timedelta(days=classification["response_days"])
        ).strftime("%Y-%m-%d")
    elif classification["response_days"]:
        response_deadline = (
            datetime.utcnow() + timedelta(days=classification["response_days"])
        ).strftime("%Y-%m-%d")

    return {
        "change_id": f"RC-{datetime.utcnow().strftime('%Y%m%d')}-{abs(hash(change_description)) % 1000:03d}",
        "jurisdiction": jurisdiction,
        "description": change_description,
        "classification": change_type,
        "classification_name": classification["name"],
        "effective_date": effective_date,
        "response_deadline": response_deadline,
        "status": "identified",
        "logged_date": datetime.utcnow().isoformat(),
    }


def calculate_impact_score(
    geographic_scope: int,
    operational_change: int,
    data_subject_volume: int,
    enforcement_risk: int,
    timeline_pressure: int,
) -> dict:
    """Calculate the weighted impact score for a regulatory change."""
    scores = {
        "geographic_scope": min(geographic_scope, 5),
        "operational_change": min(operational_change, 5),
        "data_subject_volume": min(data_subject_volume, 5),
        "enforcement_risk": min(enforcement_risk, 5),
        "timeline_pressure": min(timeline_pressure, 5),
    }

    weighted_score = sum(
        scores[dim] * IMPACT_DIMENSIONS[dim]["weight"]
        for dim in scores
    )

    category = "low"
    for cat, info in sorted(IMPACT_CATEGORIES.items(), key=lambda x: x[1]["min_score"], reverse=True):
        if weighted_score >= info["min_score"]:
            category = cat
            break

    return {
        "dimension_scores": scores,
        "weighted_score": round(weighted_score, 2),
        "impact_category": category,
        "response": IMPACT_CATEGORIES[category]["response"],
        "assessment_date": datetime.utcnow().isoformat(),
    }


def prioritise_changes(changes: list) -> dict:
    """Prioritise a list of regulatory changes by impact score and deadline."""
    prioritised = sorted(
        changes,
        key=lambda x: (-x.get("impact_score", 0), x.get("response_deadline", "9999-12-31")),
    )

    return {
        "total_changes": len(changes),
        "prioritised_list": [
            {
                "rank": i + 1,
                "change_id": c.get("change_id"),
                "jurisdiction": c.get("jurisdiction"),
                "description": c.get("description"),
                "impact_score": c.get("impact_score"),
                "impact_category": c.get("impact_category"),
                "response_deadline": c.get("response_deadline"),
            }
            for i, c in enumerate(prioritised)
        ],
        "generated_date": datetime.utcnow().isoformat(),
    }


def generate_monitoring_report(
    changes_tracked: int,
    assessments_completed: int,
    implementations_completed: int,
    implementations_overdue: int,
    average_turnaround_days: float,
) -> dict:
    """Generate a monitoring programme performance report."""
    return {
        "report_period": datetime.utcnow().strftime("%Y-Q%q").replace(
            "%q", str((datetime.utcnow().month - 1) // 3 + 1)
        ),
        "metrics": {
            "changes_tracked": changes_tracked,
            "impact_assessments_completed": assessments_completed,
            "implementations_completed": implementations_completed,
            "implementations_overdue": implementations_overdue,
            "average_turnaround_days": average_turnaround_days,
            "completion_rate": round(
                implementations_completed / (implementations_completed + implementations_overdue) * 100, 1
            ) if (implementations_completed + implementations_overdue) > 0 else 100.0,
        },
        "health": "GREEN" if implementations_overdue == 0 else (
            "AMBER" if implementations_overdue <= 2 else "RED"
        ),
        "generated_date": datetime.utcnow().isoformat(),
    }


if __name__ == "__main__":
    print("=== Classify Regulatory Change ===")
    change = classify_change(
        "Australia",
        "Privacy Act reform amendments enacted — automated decision-making transparency, children's code",
        "LAW-AMD",
        "2026-07-01",
    )
    print(json.dumps(change, indent=2))

    print("\n=== Impact Score Calculation ===")
    impact = calculate_impact_score(
        geographic_scope=1,
        operational_change=4,
        data_subject_volume=2,
        enforcement_risk=4,
        timeline_pressure=3,
    )
    print(json.dumps(impact, indent=2))

    print("\n=== Monitoring Report ===")
    report = generate_monitoring_report(
        changes_tracked=75,
        assessments_completed=12,
        implementations_completed=10,
        implementations_overdue=1,
        average_turnaround_days=11.5,
    )
    print(json.dumps(report, indent=2))
