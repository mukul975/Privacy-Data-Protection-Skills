#!/usr/bin/env python3
"""
Vendor Breach Cascade — Notification Chain and Response Management

Implements vendor breach notification tracking, cascade timing,
risk assessment, regulatory notification, and remediation coordination
per GDPR Articles 33-34.
"""

import json
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class BreachSeverity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class BreachType(Enum):
    CONFIDENTIALITY = "confidentiality"
    INTEGRITY = "integrity"
    AVAILABILITY = "availability"
    COMBINED = "combined"


class CascadePhase(Enum):
    INITIAL_RECEIPT = "initial_receipt"
    ASSESSMENT = "assessment"
    NOTIFICATION_DECISION = "notification_decision"
    SA_NOTIFICATION = "sa_notification"
    DS_NOTIFICATION = "ds_notification"
    COORDINATED_RESPONSE = "coordinated_response"
    POST_INCIDENT = "post_incident"
    CLOSED = "closed"


class RiskLevel(Enum):
    NO_RISK = "unlikely_to_result_in_risk"
    RISK = "likely_to_result_in_risk"
    HIGH_RISK = "likely_to_result_in_high_risk"


class NotificationDecision(Enum):
    NOTIFY = "notify"
    DO_NOT_NOTIFY = "do_not_notify"
    PHASED = "phased_notification"


SA_NOTIFICATION_HOURS = 72
PROCESSOR_NOTIFICATION_HOURS = 24  # Summit DPA standard


@dataclass
class VendorBreachNotification:
    """Initial breach notification received from a vendor."""
    notification_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_name: str = ""
    vendor_contact: str = ""
    vendor_dpo: str = ""
    breach_occurred: str = ""  # When breach actually happened
    vendor_became_aware: str = ""  # When vendor detected the breach
    notification_sent: str = ""  # When vendor sent notification
    notification_received: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    breach_description: str = ""
    breach_type: str = BreachType.CONFIDENTIALITY.value
    data_categories_affected: list[str] = field(default_factory=list)
    estimated_data_subjects: int = 0
    estimated_records: int = 0
    containment_status: str = "unknown"
    exfiltration_confirmed: str = "unknown"  # yes / no / unknown
    multi_tenant: bool = False
    initial_measures: list[str] = field(default_factory=list)


@dataclass
class BreachCascadeRecord:
    """Complete breach cascade tracking record."""
    case_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_notification: Optional[dict] = None
    severity: str = BreachSeverity.MEDIUM.value
    current_phase: str = CascadePhase.INITIAL_RECEIPT.value
    phase_history: list[dict] = field(default_factory=list)
    risk_assessment: Optional[dict] = None
    risk_level: str = RiskLevel.RISK.value
    sa_notification_decision: str = ""
    sa_notification_filed: bool = False
    sa_notification_date: Optional[str] = None
    sa_reference_number: str = ""
    ds_notification_decision: str = ""
    ds_notification_sent: bool = False
    ds_notification_date: Optional[str] = None
    ds_affected_count: int = 0
    timeline: list[dict] = field(default_factory=list)
    vendor_information_requests: list[dict] = field(default_factory=list)
    remediation_status: str = "pending"
    vendor_risk_score_updated: bool = False
    lessons_learned: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    closed_at: Optional[str] = None

    @property
    def sa_notification_deadline(self) -> str:
        """Calculate 72-hour SA notification deadline from awareness."""
        if self.vendor_notification:
            received = self.vendor_notification.get("notification_received", "")
            if received:
                dt = datetime.fromisoformat(received.replace("Z", "+00:00"))
                return (dt + timedelta(hours=SA_NOTIFICATION_HOURS)).isoformat()
        return ""


class VendorBreachCascadeEngine:
    """
    Manages the vendor breach notification cascade including
    notification tracking, risk assessment, regulatory filing,
    and coordinated response.
    """

    def __init__(self):
        self.cases: dict[str, BreachCascadeRecord] = {}

    def receive_vendor_notification(
        self, notification: VendorBreachNotification
    ) -> BreachCascadeRecord:
        """Process an incoming vendor breach notification."""
        case = BreachCascadeRecord(
            vendor_notification=asdict(notification),
        )

        case.timeline.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event": "Vendor breach notification received",
            "detail": f"From: {notification.vendor_name}, Contact: {notification.vendor_contact}",
        })

        # Auto-classify severity
        if notification.estimated_data_subjects > 10000 or notification.exfiltration_confirmed == "yes":
            case.severity = BreachSeverity.CRITICAL.value
        elif notification.estimated_data_subjects > 1000:
            case.severity = BreachSeverity.HIGH.value
        elif notification.estimated_data_subjects > 100:
            case.severity = BreachSeverity.MEDIUM.value
        else:
            case.severity = BreachSeverity.LOW.value

        case.current_phase = CascadePhase.INITIAL_RECEIPT.value
        case.phase_history.append({
            "phase": CascadePhase.INITIAL_RECEIPT.value,
            "entered": datetime.now(timezone.utc).isoformat(),
        })

        self.cases[case.case_id] = case
        return case

    def check_notification_timeliness(self, case_id: str) -> dict:
        """Check whether the vendor met the DPA notification timeframe."""
        case = self.cases.get(case_id)
        if not case or not case.vendor_notification:
            raise ValueError(f"Case {case_id} not found")

        vn = case.vendor_notification
        aware = vn.get("vendor_became_aware", "")
        sent = vn.get("notification_sent", "")

        if aware and sent:
            aware_dt = datetime.fromisoformat(aware.replace("Z", "+00:00"))
            sent_dt = datetime.fromisoformat(sent.replace("Z", "+00:00"))
            hours_elapsed = (sent_dt - aware_dt).total_seconds() / 3600

            compliant = hours_elapsed <= PROCESSOR_NOTIFICATION_HOURS
            return {
                "case_id": case_id,
                "vendor_aware": aware,
                "notification_sent": sent,
                "hours_elapsed": round(hours_elapsed, 1),
                "dpa_requirement_hours": PROCESSOR_NOTIFICATION_HOURS,
                "compliant": compliant,
                "assessment": "Within DPA timeframe" if compliant else f"LATE — exceeded by {round(hours_elapsed - PROCESSOR_NOTIFICATION_HOURS, 1)} hours",
            }

        return {"case_id": case_id, "assessment": "Insufficient timing data to assess"}

    def advance_phase(self, case_id: str, new_phase: CascadePhase) -> str:
        """Advance the case to the next cascade phase."""
        case = self.cases.get(case_id)
        if not case:
            raise ValueError(f"Case {case_id} not found")

        case.current_phase = new_phase.value
        case.phase_history.append({
            "phase": new_phase.value,
            "entered": datetime.now(timezone.utc).isoformat(),
        })
        case.timeline.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event": f"Phase advanced to: {new_phase.value}",
            "detail": "",
        })
        return new_phase.value

    def perform_risk_assessment(
        self,
        case_id: str,
        breach_type: str,
        data_sensitivity: str,
        ease_of_identification: str,
        severity_of_consequences: str,
        volume: str,
        special_characteristics: bool,
        assessor: str,
    ) -> dict:
        """Perform risk assessment per EDPB criteria to determine notification obligations."""
        case = self.cases.get(case_id)
        if not case:
            raise ValueError(f"Case {case_id} not found")

        risk_factors = 0

        sensitivity_scores = {"low": 1, "medium": 2, "high": 3, "very_high": 4}
        risk_factors += sensitivity_scores.get(data_sensitivity, 2)

        if ease_of_identification in ["easy", "very_easy"]:
            risk_factors += 2
        elif ease_of_identification == "moderate":
            risk_factors += 1

        consequence_scores = {"low": 1, "medium": 2, "high": 3, "very_high": 4}
        risk_factors += consequence_scores.get(severity_of_consequences, 2)

        volume_scores = {"small": 1, "medium": 2, "large": 3, "very_large": 4}
        risk_factors += volume_scores.get(volume, 2)

        if special_characteristics:
            risk_factors += 2

        if breach_type in ["confidentiality", "combined"]:
            risk_factors += 1

        if risk_factors >= 10:
            risk_level = RiskLevel.HIGH_RISK
        elif risk_factors >= 5:
            risk_level = RiskLevel.RISK
        else:
            risk_level = RiskLevel.NO_RISK

        assessment = {
            "assessor": assessor,
            "assessment_date": datetime.now(timezone.utc).isoformat(),
            "breach_type": breach_type,
            "data_sensitivity": data_sensitivity,
            "ease_of_identification": ease_of_identification,
            "severity_of_consequences": severity_of_consequences,
            "volume": volume,
            "special_characteristics": special_characteristics,
            "risk_factor_score": risk_factors,
            "risk_level": risk_level.value,
            "sa_notification_required": risk_level != RiskLevel.NO_RISK,
            "ds_notification_required": risk_level == RiskLevel.HIGH_RISK,
        }

        case.risk_assessment = assessment
        case.risk_level = risk_level.value
        self.advance_phase(case_id, CascadePhase.NOTIFICATION_DECISION)

        return assessment

    def record_sa_notification(
        self, case_id: str, reference_number: str = ""
    ) -> dict:
        """Record that supervisory authority notification has been filed."""
        case = self.cases.get(case_id)
        if not case:
            raise ValueError(f"Case {case_id} not found")

        case.sa_notification_decision = NotificationDecision.NOTIFY.value
        case.sa_notification_filed = True
        case.sa_notification_date = datetime.now(timezone.utc).isoformat()
        case.sa_reference_number = reference_number

        case.timeline.append({
            "timestamp": case.sa_notification_date,
            "event": "Supervisory authority notification filed",
            "detail": f"Reference: {reference_number}",
        })

        deadline = case.sa_notification_deadline
        if deadline and case.sa_notification_date <= deadline:
            within_deadline = True
        else:
            within_deadline = False

        self.advance_phase(case_id, CascadePhase.SA_NOTIFICATION)

        return {
            "filed": True,
            "date": case.sa_notification_date,
            "reference": reference_number,
            "within_72_hours": within_deadline,
            "deadline_was": deadline,
        }

    def get_case_summary(self, case_id: str) -> dict:
        """Generate a complete case summary."""
        case = self.cases.get(case_id)
        if not case:
            raise ValueError(f"Case {case_id} not found")

        vn = case.vendor_notification or {}

        return {
            "case_id": case.case_id,
            "vendor": vn.get("vendor_name", "Unknown"),
            "severity": case.severity,
            "current_phase": case.current_phase,
            "breach_type": vn.get("breach_type", "unknown"),
            "data_subjects_affected": vn.get("estimated_data_subjects", 0),
            "risk_level": case.risk_level,
            "sa_notification_filed": case.sa_notification_filed,
            "sa_notification_date": case.sa_notification_date,
            "sa_reference": case.sa_reference_number,
            "ds_notification_sent": case.ds_notification_sent,
            "72h_deadline": case.sa_notification_deadline,
            "timeline_events": len(case.timeline),
            "created": case.created_at,
        }


if __name__ == "__main__":
    engine = VendorBreachCascadeEngine()

    # Simulate vendor breach notification
    notification = VendorBreachNotification(
        vendor_name="NimbusAnalytics GmbH",
        vendor_contact="Dr. Klaus Weber, DPO",
        vendor_dpo="dpo@nimbusanalytics.de",
        breach_occurred="2026-03-12T02:15:00+00:00",
        vendor_became_aware="2026-03-12T06:30:00+00:00",
        notification_sent="2026-03-12T14:00:00+00:00",
        notification_received="2026-03-12T14:15:00+00:00",
        breach_description="Unauthorized access to analytics database via compromised API key. "
                          "Attacker accessed customer usage data for approximately 8 hours before detection. "
                          "API key immediately revoked and access terminated.",
        breach_type=BreachType.CONFIDENTIALITY.value,
        data_categories_affected=["email_address", "user_id", "usage_metrics", "ip_address"],
        estimated_data_subjects=12500,
        estimated_records=450000,
        containment_status="contained",
        exfiltration_confirmed="unknown",
        multi_tenant=True,
        initial_measures=[
            "Compromised API key revoked",
            "All API keys rotated",
            "Affected database access logs preserved",
            "External forensic firm engaged",
        ],
    )

    # Receive and process notification
    case = engine.receive_vendor_notification(notification)
    print(f"Case ID: {case.case_id}")
    print(f"Severity: {case.severity}")
    print(f"72-hour SA deadline: {case.sa_notification_deadline}")

    # Check vendor notification timeliness
    timeliness = engine.check_notification_timeliness(case.case_id)
    print(f"\nVendor Notification Timeliness:")
    print(json.dumps(timeliness, indent=2))

    # Perform risk assessment
    risk = engine.perform_risk_assessment(
        case.case_id,
        breach_type="confidentiality",
        data_sensitivity="medium",
        ease_of_identification="moderate",
        severity_of_consequences="medium",
        volume="large",
        special_characteristics=False,
        assessor="Dr. Maria Santos, DPO — Summit Cloud Partners",
    )
    print(f"\nRisk Assessment:")
    print(json.dumps(risk, indent=2))

    # File SA notification
    sa_result = engine.record_sa_notification(
        case.case_id,
        reference_number="SA-2026-BN-04521",
    )
    print(f"\nSA Notification:")
    print(json.dumps(sa_result, indent=2))

    # Full case summary
    summary = engine.get_case_summary(case.case_id)
    print(f"\n=== Breach Cascade Case Summary ===")
    print(json.dumps(summary, indent=2))
