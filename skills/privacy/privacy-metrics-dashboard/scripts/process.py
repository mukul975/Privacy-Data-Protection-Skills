"""
Privacy Metrics Dashboard — KPI Calculator

Computes privacy program KPIs including DSAR metrics,
breach metrics, training coverage, and overall privacy health score.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import statistics


@dataclass
class DSARRecord:
    request_id: str
    request_type: str
    received_at: datetime
    completed_at: datetime | None
    status: str
    automated: bool


@dataclass
class BreachRecord:
    breach_id: str
    severity: str
    occurred_at: datetime
    detected_at: datetime
    notified_at: datetime | None
    contained_at: datetime | None
    records_affected: int
    root_cause: str


def compute_dsar_metrics(
    dsars: list[DSARRecord],
    deadline_days: int = 30,
) -> dict:
    """Compute DSAR KPIs for a set of requests."""
    total = len(dsars)
    completed = [d for d in dsars if d.status == "completed" and d.completed_at]

    response_times = [
        (d.completed_at - d.received_at).days for d in completed
    ]

    on_time = [d for d in completed if (d.completed_at - d.received_at).days <= deadline_days]
    automated = [d for d in completed if d.automated]
    open_dsars = [d for d in dsars if d.status in ("open", "in_progress")]

    by_type: dict[str, int] = {}
    for d in dsars:
        by_type[d.request_type] = by_type.get(d.request_type, 0) + 1

    return {
        "total_received": total,
        "total_completed": len(completed),
        "avg_response_days": round(statistics.mean(response_times), 1) if response_times else 0,
        "median_response_days": round(statistics.median(response_times), 1) if response_times else 0,
        "p95_response_days": (
            round(sorted(response_times)[int(len(response_times) * 0.95)], 1)
            if len(response_times) >= 20
            else (round(max(response_times), 1) if response_times else 0)
        ),
        "on_time_rate": round(len(on_time) / len(completed) * 100, 1) if completed else 100.0,
        "automated_rate": round(len(automated) / len(completed) * 100, 1) if completed else 0,
        "backlog": len(open_dsars),
        "by_type": by_type,
    }


def compute_breach_metrics(breaches: list[BreachRecord]) -> dict:
    """Compute breach KPIs."""
    by_severity: dict[str, int] = {}
    detection_hours = []
    notification_hours = []
    total_records = 0

    for b in breaches:
        by_severity[b.severity] = by_severity.get(b.severity, 0) + 1
        total_records += b.records_affected

        if b.detected_at and b.occurred_at:
            detection_hours.append((b.detected_at - b.occurred_at).total_seconds() / 3600)
        if b.notified_at and b.detected_at:
            notification_hours.append((b.notified_at - b.detected_at).total_seconds() / 3600)

    root_causes = [b.root_cause for b in breaches if b.root_cause]
    repeat_count = len(root_causes) - len(set(root_causes))

    return {
        "total_breaches": len(breaches),
        "by_severity": by_severity,
        "avg_detection_hours": round(statistics.mean(detection_hours), 1) if detection_hours else 0,
        "avg_notification_hours": round(statistics.mean(notification_hours), 1) if notification_hours else 0,
        "total_records_affected": total_records,
        "repeat_breaches": repeat_count,
    }


def compute_health_score(dsar_metrics: dict, breach_metrics: dict) -> dict:
    """
    Compute overall privacy health score (0-100).

    Components:
    - DSAR compliance (25%): On-time rate
    - Breach prevention (30%): Inverse of breach count
    - Response timeliness (20%): DSAR response time vs deadline
    - Detection speed (25%): Breach detection vs 72h target
    """
    dsar_score = min(100, dsar_metrics["on_time_rate"])

    breach_count = breach_metrics["total_breaches"]
    breach_score = 100 if breach_count == 0 else max(0, 100 - breach_count * 20)

    avg_resp = dsar_metrics["avg_response_days"]
    response_score = min(100, max(0, (30 - avg_resp) / 30 * 100))

    avg_detect = breach_metrics["avg_detection_hours"]
    detection_score = (
        min(100, max(0, (72 - avg_detect) / 72 * 100))
        if breach_count > 0 else 100
    )

    overall = (
        dsar_score * 0.25
        + breach_score * 0.30
        + response_score * 0.20
        + detection_score * 0.25
    )

    rating = (
        "Excellent" if overall >= 90
        else "Good" if overall >= 75
        else "Needs Improvement" if overall >= 60
        else "Critical"
    )

    return {
        "overall_score": round(overall, 1),
        "rating": rating,
        "components": {
            "dsar_compliance": {"score": round(dsar_score, 1), "weight": "25%"},
            "breach_prevention": {"score": round(breach_score, 1), "weight": "30%"},
            "response_timeliness": {"score": round(response_score, 1), "weight": "20%"},
            "detection_speed": {"score": round(detection_score, 1), "weight": "25%"},
        },
    }


if __name__ == "__main__":
    # Sample DSAR data
    dsars = [
        DSARRecord("DSR-001", "access", datetime(2026, 1, 5, tzinfo=timezone.utc), datetime(2026, 1, 20, tzinfo=timezone.utc), "completed", False),
        DSARRecord("DSR-002", "deletion", datetime(2026, 1, 10, tzinfo=timezone.utc), datetime(2026, 1, 28, tzinfo=timezone.utc), "completed", True),
        DSARRecord("DSR-003", "access", datetime(2026, 2, 1, tzinfo=timezone.utc), datetime(2026, 2, 12, tzinfo=timezone.utc), "completed", True),
        DSARRecord("DSR-004", "portability", datetime(2026, 2, 15, tzinfo=timezone.utc), None, "in_progress", False),
    ]

    # Sample breach data
    breaches = [
        BreachRecord(
            "BR-001", "medium",
            datetime(2026, 1, 15, 8, 0, tzinfo=timezone.utc),
            datetime(2026, 1, 15, 14, 0, tzinfo=timezone.utc),
            datetime(2026, 1, 16, 10, 0, tzinfo=timezone.utc),
            datetime(2026, 1, 15, 18, 0, tzinfo=timezone.utc),
            150, "phishing",
        ),
    ]

    dsar_m = compute_dsar_metrics(dsars)
    breach_m = compute_breach_metrics(breaches)
    health = compute_health_score(dsar_m, breach_m)

    print("=== DSAR Metrics ===")
    print(json.dumps(dsar_m, indent=2))
    print("\n=== Breach Metrics ===")
    print(json.dumps(breach_m, indent=2))
    print("\n=== Health Score ===")
    print(json.dumps(health, indent=2))
