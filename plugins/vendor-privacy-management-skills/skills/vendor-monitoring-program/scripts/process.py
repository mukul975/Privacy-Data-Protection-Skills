#!/usr/bin/env python3
"""
Vendor Monitoring Program — Continuous Oversight and KPI Tracking

Implements ongoing vendor compliance monitoring, KPI calculation,
alert management, and governance reporting.
"""

import json
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class AlertSeverity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class AlertSource(Enum):
    RISK_INTELLIGENCE = "vendor_risk_intelligence"
    CERTIFICATION_MONITOR = "certification_monitor"
    CASB_DLP = "casb_dlp"
    NETWORK_MONITOR = "network_monitor"
    SECURITY_SCORECARD = "security_scorecard"
    REGULATORY_DATABASE = "regulatory_database"
    SUB_PROCESSOR_REGISTRY = "sub_processor_registry"


class AlertStatus(Enum):
    NEW = "new"
    INVESTIGATING = "investigating"
    RESOLVED = "resolved"
    ESCALATED = "escalated"
    FALSE_POSITIVE = "false_positive"


class RenewalRecommendation(Enum):
    RENEW = "renew"
    RENEW_WITH_CONDITIONS = "renew_with_conditions"
    DO_NOT_RENEW = "do_not_renew"


@dataclass
class MonitoringAlert:
    """A monitoring signal alert."""
    alert_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_id: str = ""
    vendor_name: str = ""
    source: str = AlertSource.RISK_INTELLIGENCE.value
    severity: str = AlertSeverity.MEDIUM.value
    description: str = ""
    detected_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    status: str = AlertStatus.NEW.value
    assigned_to: str = ""
    investigation_notes: str = ""
    resolution: str = ""
    resolved_date: Optional[str] = None
    risk_score_impact: bool = False


@dataclass
class MonitoringActivity:
    """A scheduled monitoring activity."""
    activity_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_id: str = ""
    vendor_name: str = ""
    activity_type: str = ""
    scheduled_date: str = ""
    completed_date: Optional[str] = None
    outcome: str = ""
    notes: str = ""


@dataclass
class VendorScorecard:
    """Quarterly vendor privacy scorecard."""
    scorecard_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_id: str = ""
    vendor_name: str = ""
    period: str = ""
    dpa_compliance_score: int = 0
    audit_performance_score: int = 0
    breach_history_score: int = 0
    sub_processor_compliance_score: int = 0
    certification_currency_score: int = 0
    cooperation_score: int = 0
    weighted_total: float = 0.0
    trend: str = "stable"


SCORECARD_WEIGHTS = {
    "dpa_compliance": 0.25,
    "audit_performance": 0.20,
    "breach_history": 0.15,
    "sub_processor_compliance": 0.15,
    "certification_currency": 0.15,
    "cooperation": 0.10,
}


class VendorMonitoringEngine:
    """
    Manages ongoing vendor privacy compliance monitoring including
    alerts, scheduled activities, scorecards, and KPI tracking.
    """

    def __init__(self):
        self.alerts: list[MonitoringAlert] = []
        self.activities: list[MonitoringActivity] = []
        self.scorecards: list[VendorScorecard] = []

    def create_alert(self, alert: MonitoringAlert) -> str:
        """Record a new monitoring alert."""
        self.alerts.append(alert)
        return alert.alert_id

    def resolve_alert(
        self, alert_id: str, resolution: str, risk_impact: bool = False
    ) -> str:
        """Resolve a monitoring alert."""
        for a in self.alerts:
            if a.alert_id == alert_id:
                a.status = AlertStatus.RESOLVED.value
                a.resolution = resolution
                a.resolved_date = datetime.now(timezone.utc).isoformat()
                a.risk_score_impact = risk_impact
                return a.status
        raise ValueError(f"Alert {alert_id} not found")

    def schedule_activity(self, activity: MonitoringActivity) -> str:
        """Schedule a monitoring activity."""
        self.activities.append(activity)
        return activity.activity_id

    def complete_activity(
        self, activity_id: str, outcome: str, notes: str = ""
    ) -> str:
        """Record completion of a monitoring activity."""
        for a in self.activities:
            if a.activity_id == activity_id:
                a.completed_date = datetime.now(timezone.utc).isoformat()
                a.outcome = outcome
                a.notes = notes
                return a.completed_date
        raise ValueError(f"Activity {activity_id} not found")

    def generate_scorecard(
        self, vendor_id: str, vendor_name: str, period: str,
        scores: dict, previous_total: float = 0.0,
    ) -> VendorScorecard:
        """Generate a quarterly vendor privacy scorecard."""
        weighted = sum(
            scores.get(dim, 3) * weight
            for dim, weight in SCORECARD_WEIGHTS.items()
        )
        weighted = round(weighted, 2)

        if previous_total > 0:
            if weighted > previous_total + 0.2:
                trend = "improving"
            elif weighted < previous_total - 0.2:
                trend = "deteriorating"
            else:
                trend = "stable"
        else:
            trend = "initial"

        scorecard = VendorScorecard(
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            period=period,
            dpa_compliance_score=scores.get("dpa_compliance", 3),
            audit_performance_score=scores.get("audit_performance", 3),
            breach_history_score=scores.get("breach_history", 3),
            sub_processor_compliance_score=scores.get("sub_processor_compliance", 3),
            certification_currency_score=scores.get("certification_currency", 3),
            cooperation_score=scores.get("cooperation", 3),
            weighted_total=weighted,
            trend=trend,
        )
        self.scorecards.append(scorecard)
        return scorecard

    def assess_renewal(
        self, vendor_id: str, vendor_name: str,
        risk_score: float, open_critical: int, open_major: int,
        last_assessment_months_ago: int, risk_trend: str,
    ) -> dict:
        """Assess privacy recommendation for contract renewal."""
        if open_critical > 0 or risk_score >= 4.0:
            recommendation = RenewalRecommendation.DO_NOT_RENEW
            rationale = "Significant non-compliance or unacceptable risk level"
        elif open_major > 0 or last_assessment_months_ago > 24 or risk_trend == "deteriorating":
            recommendation = RenewalRecommendation.RENEW_WITH_CONDITIONS
            conditions = []
            if open_major > 0:
                conditions.append(f"Remediate {open_major} open Major finding(s) within 30 days")
            if last_assessment_months_ago > 24:
                conditions.append("Complete reassessment within 60 days of renewal")
            if risk_trend == "deteriorating":
                conditions.append("Implement enhanced monitoring for 6 months post-renewal")
            rationale = f"Conditions: {'; '.join(conditions)}"
        else:
            recommendation = RenewalRecommendation.RENEW
            rationale = "Vendor is compliant with no significant outstanding issues"

        return {
            "vendor_id": vendor_id,
            "vendor_name": vendor_name,
            "recommendation": recommendation.value,
            "rationale": rationale,
            "risk_score": risk_score,
            "open_critical_findings": open_critical,
            "open_major_findings": open_major,
            "last_assessment_months_ago": last_assessment_months_ago,
            "risk_trend": risk_trend,
            "assessed_date": datetime.now(timezone.utc).isoformat(),
        }

    def calculate_program_kpis(self) -> dict:
        """Calculate program-level KPIs."""
        now = datetime.now(timezone.utc).isoformat()

        total_alerts = len(self.alerts)
        resolved_alerts = len([a for a in self.alerts if a.status == AlertStatus.RESOLVED.value])
        open_alerts = len([
            a for a in self.alerts
            if a.status in [AlertStatus.NEW.value, AlertStatus.INVESTIGATING.value]
        ])

        total_activities = len(self.activities)
        completed_activities = len([a for a in self.activities if a.completed_date])
        overdue_activities = len([
            a for a in self.activities
            if not a.completed_date and a.scheduled_date < now
        ])

        if self.scorecards:
            latest_scorecards = {}
            for sc in sorted(self.scorecards, key=lambda s: s.period):
                latest_scorecards[sc.vendor_id] = sc
            avg_vendor_score = round(
                sum(sc.weighted_total for sc in latest_scorecards.values())
                / len(latest_scorecards), 2
            )
        else:
            avg_vendor_score = 0.0

        return {
            "monitoring_alerts": {
                "total": total_alerts,
                "resolved": resolved_alerts,
                "open": open_alerts,
                "resolution_rate": f"{round(resolved_alerts/total_alerts*100, 1)}%" if total_alerts > 0 else "N/A",
            },
            "scheduled_activities": {
                "total": total_activities,
                "completed": completed_activities,
                "overdue": overdue_activities,
                "completion_rate": f"{round(completed_activities/total_activities*100, 1)}%" if total_activities > 0 else "N/A",
            },
            "average_vendor_privacy_score": avg_vendor_score,
            "as_of": now,
        }


if __name__ == "__main__":
    engine = VendorMonitoringEngine()

    # Record monitoring alerts
    alert1 = MonitoringAlert(
        vendor_id="nimbus-001", vendor_name="NimbusAnalytics GmbH",
        source=AlertSource.CERTIFICATION_MONITOR.value,
        severity=AlertSeverity.MEDIUM.value,
        description="ISO 27001 certificate expires in 45 days (2026-04-28)",
    )
    alert2 = MonitoringAlert(
        vendor_id="cloudmetrics-001", vendor_name="CloudMetrics US Inc.",
        source=AlertSource.SUB_PROCESSOR_REGISTRY.value,
        severity=AlertSeverity.HIGH.value,
        description="New sub-processor detected on vendor website: DataPipe Inc. (India) — not previously notified",
    )
    engine.create_alert(alert1)
    engine.create_alert(alert2)

    # Resolve alert 1
    engine.resolve_alert(
        alert1.alert_id,
        "Vendor confirmed ISO 27001 renewal audit scheduled for 2026-04-15. Certificate will be reissued before expiry.",
        risk_impact=False,
    )

    # Schedule monitoring activities
    activities = [
        MonitoringActivity(
            vendor_id="nimbus-001", vendor_name="NimbusAnalytics GmbH",
            activity_type="annual_reassessment",
            scheduled_date="2026-04-15",
        ),
        MonitoringActivity(
            vendor_id="nimbus-001", vendor_name="NimbusAnalytics GmbH",
            activity_type="sub_processor_verification",
            scheduled_date="2026-03-31",
        ),
        MonitoringActivity(
            vendor_id="cloudmetrics-001", vendor_name="CloudMetrics US Inc.",
            activity_type="annual_audit_type_2",
            scheduled_date="2026-05-01",
        ),
    ]
    for a in activities:
        engine.schedule_activity(a)

    # Complete an activity
    engine.complete_activity(
        activities[1].activity_id,
        outcome="Compliant — sub-processor list matches register",
        notes="Verified 2 sub-processors. No changes since last verification.",
    )

    # Generate scorecards
    nimbus_scorecard = engine.generate_scorecard(
        "nimbus-001", "NimbusAnalytics GmbH", "2026-Q1",
        scores={
            "dpa_compliance": 5, "audit_performance": 4,
            "breach_history": 5, "sub_processor_compliance": 4,
            "certification_currency": 4, "cooperation": 5,
        },
    )
    print(f"NimbusAnalytics Scorecard: {nimbus_scorecard.weighted_total} ({nimbus_scorecard.trend})")

    cm_scorecard = engine.generate_scorecard(
        "cloudmetrics-001", "CloudMetrics US Inc.", "2026-Q1",
        scores={
            "dpa_compliance": 3, "audit_performance": 3,
            "breach_history": 3, "sub_processor_compliance": 2,
            "certification_currency": 3, "cooperation": 3,
        },
    )
    print(f"CloudMetrics Scorecard: {cm_scorecard.weighted_total} ({cm_scorecard.trend})")

    # Assess renewal
    renewal = engine.assess_renewal(
        "cloudmetrics-001", "CloudMetrics US Inc.",
        risk_score=3.7, open_critical=0, open_major=1,
        last_assessment_months_ago=10, risk_trend="deteriorating",
    )
    print(f"\nRenewal Assessment:")
    print(json.dumps(renewal, indent=2))

    # Program KPIs
    kpis = engine.calculate_program_kpis()
    print(f"\n=== Program KPIs ===")
    print(json.dumps(kpis, indent=2))
