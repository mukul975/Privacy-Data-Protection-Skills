#!/usr/bin/env python3
"""
Breach Documentation Records Manager

Manages the Art. 33(5) breach register, validates entry completeness,
generates trend reports, and exports register data for supervisory
authority requests.
"""

import json
from datetime import datetime, timezone, timedelta
from enum import Enum
from typing import Optional


class BreachStatus(Enum):
    OPEN_INVESTIGATION = "open_investigation_in_progress"
    OPEN_REMEDIATION = "open_remediation_in_progress"
    CLOSED_COMPLETE = "closed_remediation_complete"
    CLOSED_ONGOING = "closed_remediation_ongoing"


class NotificationStatus(Enum):
    NOT_REQUIRED = "not_required"
    REQUIRED_PENDING = "required_pending"
    SUBMITTED = "submitted"
    ACKNOWLEDGED = "acknowledged"
    CLOSED = "closed"


MANDATORY_FIELDS = [
    "breach_reference",
    "discovery_timestamp",
    "breach_type",
    "breach_description",
    "affected_systems",
    "data_subject_categories",
    "data_subject_count",
    "personal_data_categories",
    "record_count",
    "risk_assessment_score",
    "risk_level",
    "containment_measures",
    "remediation_measures",
    "art_33_notification_decision",
    "art_33_notification_rationale",
    "art_34_notification_decision",
    "art_34_notification_rationale",
]


def create_breach_entry(
    breach_reference: str,
    discovery_timestamp: str,
    breach_timestamp: str,
    breach_type: str,
    breach_description: str,
    affected_systems: list,
    data_subject_categories: list,
    data_subject_count: int,
    personal_data_categories: list,
    record_count: int,
    root_cause: str,
    containment_timestamp: str,
    containment_measures: list,
    risk_assessment_score: int,
    risk_level: str,
    remediation_measures: list,
    art_33_notification_decision: str,
    art_33_notification_rationale: str,
    art_34_notification_decision: str,
    art_34_notification_rationale: str,
    sa_notification_date: Optional[str] = None,
    sa_reference_number: Optional[str] = None,
    ds_notification_date: Optional[str] = None,
) -> dict:
    """Create a complete Art. 33(5) breach register entry."""
    return {
        "breach_reference": breach_reference,
        "status": BreachStatus.OPEN_INVESTIGATION.value,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "facts": {
            "discovery_timestamp": discovery_timestamp,
            "breach_timestamp": breach_timestamp,
            "breach_type": breach_type,
            "breach_description": breach_description,
            "affected_systems": affected_systems,
            "data_subject_categories": data_subject_categories,
            "data_subject_count": data_subject_count,
            "personal_data_categories": personal_data_categories,
            "record_count": record_count,
            "root_cause": root_cause,
            "containment_timestamp": containment_timestamp,
        },
        "effects": {
            "risk_assessment_score": risk_assessment_score,
            "risk_assessment_max": 24,
            "risk_level": risk_level,
            "actual_harm_identified": "None confirmed as of entry creation",
            "potential_harm": [],
        },
        "remedial_actions": {
            "containment_measures": containment_measures,
            "remediation_measures": [
                {"action": m, "status": "planned", "target_date": None, "completed_date": None}
                for m in remediation_measures
            ],
        },
        "notification_decisions": {
            "art_33_sa_notification": {
                "decision": art_33_notification_decision,
                "rationale": art_33_notification_rationale,
                "notification_date": sa_notification_date,
                "sa_reference_number": sa_reference_number,
                "sa_follow_up_status": "none",
            },
            "art_34_ds_notification": {
                "decision": art_34_notification_decision,
                "rationale": art_34_notification_rationale,
                "notification_date": ds_notification_date,
                "notification_method": None,
                "ds_count_notified": 0,
            },
        },
        "supporting_documents": [],
        "lessons_learned": None,
    }


def validate_entry_completeness(entry: dict) -> dict:
    """Validate that a breach register entry contains all mandatory Art. 33(5) fields."""
    missing = []
    warnings = []

    field_paths = {
        "breach_reference": entry.get("breach_reference"),
        "discovery_timestamp": entry.get("facts", {}).get("discovery_timestamp"),
        "breach_type": entry.get("facts", {}).get("breach_type"),
        "breach_description": entry.get("facts", {}).get("breach_description"),
        "affected_systems": entry.get("facts", {}).get("affected_systems"),
        "data_subject_categories": entry.get("facts", {}).get("data_subject_categories"),
        "data_subject_count": entry.get("facts", {}).get("data_subject_count"),
        "personal_data_categories": entry.get("facts", {}).get("personal_data_categories"),
        "record_count": entry.get("facts", {}).get("record_count"),
        "risk_assessment_score": entry.get("effects", {}).get("risk_assessment_score"),
        "risk_level": entry.get("effects", {}).get("risk_level"),
        "containment_measures": entry.get("remedial_actions", {}).get("containment_measures"),
        "remediation_measures": entry.get("remedial_actions", {}).get("remediation_measures"),
        "art_33_notification_decision": entry.get("notification_decisions", {}).get("art_33_sa_notification", {}).get("decision"),
        "art_33_notification_rationale": entry.get("notification_decisions", {}).get("art_33_sa_notification", {}).get("rationale"),
        "art_34_notification_decision": entry.get("notification_decisions", {}).get("art_34_ds_notification", {}).get("decision"),
        "art_34_notification_rationale": entry.get("notification_decisions", {}).get("art_34_ds_notification", {}).get("rationale"),
    }

    for field, value in field_paths.items():
        if value is None or value == "" or value == []:
            missing.append(field)

    if not entry.get("facts", {}).get("root_cause"):
        warnings.append("root_cause is empty — acceptable during investigation but must be populated before closure")

    if not entry.get("supporting_documents"):
        warnings.append("No supporting documents linked — risk assessment, notification copies, and investigation report should be attached")

    remediation = entry.get("remedial_actions", {}).get("remediation_measures", [])
    overdue = [
        m for m in remediation
        if m.get("status") == "planned" and m.get("target_date")
        and datetime.fromisoformat(m["target_date"]) < datetime.now(timezone.utc)
    ]
    if overdue:
        warnings.append(f"{len(overdue)} remediation actions are overdue")

    return {
        "entry_reference": entry.get("breach_reference", "UNKNOWN"),
        "compliant": len(missing) == 0,
        "mandatory_fields_present": len(field_paths) - len(missing),
        "mandatory_fields_total": len(field_paths),
        "missing_fields": missing,
        "warnings": warnings,
        "assessment": "COMPLIANT — All mandatory Art. 33(5) fields present" if not missing
        else f"NON-COMPLIANT — {len(missing)} mandatory fields missing",
    }


def generate_trend_report(entries: list) -> dict:
    """Generate a trend analysis report from multiple breach register entries."""
    total = len(entries)
    if total == 0:
        return {"error": "No entries to analyze"}

    types = {}
    risk_levels = {}
    sa_notifications = 0
    ds_notifications = 0
    total_subjects = 0
    root_causes = {}

    for entry in entries:
        bt = entry.get("facts", {}).get("breach_type", "unknown")
        types[bt] = types.get(bt, 0) + 1

        rl = entry.get("effects", {}).get("risk_level", "unknown")
        risk_levels[rl] = risk_levels.get(rl, 0) + 1

        sa_decision = entry.get("notification_decisions", {}).get("art_33_sa_notification", {}).get("decision", "")
        if sa_decision in ("required", "submitted"):
            sa_notifications += 1

        ds_decision = entry.get("notification_decisions", {}).get("art_34_ds_notification", {}).get("decision", "")
        if ds_decision in ("required", "submitted"):
            ds_notifications += 1

        total_subjects += entry.get("facts", {}).get("data_subject_count", 0)

        rc = entry.get("facts", {}).get("root_cause", "not_determined")
        if rc:
            root_causes[rc] = root_causes.get(rc, 0) + 1

    return {
        "report_period": "Annual",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total_breaches": total,
            "total_data_subjects_affected": total_subjects,
            "sa_notification_rate": f"{(sa_notifications / total) * 100:.1f}%",
            "ds_notification_rate": f"{(ds_notifications / total) * 100:.1f}%",
        },
        "breach_type_distribution": types,
        "risk_level_distribution": risk_levels,
        "root_cause_frequency": root_causes,
        "recommendations": [
            "Review recurring root causes for systemic control improvements",
            "Verify all remediation actions are tracked to completion",
            "Ensure new processing activities are covered by detection monitoring",
        ],
    }


def main():
    print("=" * 70)
    print("ART. 33(5) BREACH REGISTER — ENTRY CREATION")
    print("=" * 70)

    entry1 = create_breach_entry(
        breach_reference="SPG-BREACH-2026-003",
        discovery_timestamp="2026-03-13T14:30:00+00:00",
        breach_timestamp="2026-03-13T11:15:00+00:00",
        breach_type="availability_and_confidentiality",
        breach_description="LockBit 3.0 ransomware encrypted production customer database cluster (db-prod-eu-west-01 through 04). Attack vector: spear-phishing leading to compromised service account (svc-migration-2024).",
        affected_systems=["db-prod-eu-west-01", "db-prod-eu-west-02", "db-prod-eu-west-03", "db-prod-eu-west-04"],
        data_subject_categories=["Individual account holders", "Business account holders", "Joint account holders"],
        data_subject_count=15230,
        personal_data_categories=["Full names", "Postal addresses", "Email addresses", "Payment card last-4", "Transaction histories", "Account balances"],
        record_count=48720,
        root_cause="Stale privileged service account not decommissioned; excluded from access review scope; MFA vulnerable to push fatigue",
        containment_timestamp="2026-03-13T12:45:00+00:00",
        containment_measures=["Network isolation of db-prod cluster", "Service account credential revocation", "Backup restoration from 12 Mar 23:00 UTC snapshot", "EDR sweep across infrastructure", "Mandiant IR team engaged"],
        risk_assessment_score=18,
        risk_level="approaching_high_risk",
        remediation_measures=["Deploy FIDO2/WebAuthn MFA for privileged accounts", "Implement service account lifecycle management", "Deploy network segmentation for database tier", "Include service accounts in quarterly access review", "Organization-wide phishing awareness retraining", "Full vulnerability assessment of database infrastructure"],
        art_33_notification_decision="required",
        art_33_notification_rationale="Risk assessment score 18/24 exceeds the 'likely to result in risk' threshold. Supervisory authority notification is mandatory under Art. 33(1).",
        art_34_notification_decision="required",
        art_34_notification_rationale="Risk assessment score approaches high-risk threshold. DPO recommends data subject notification under Art. 34(1) given financial data involvement and controller's position as payment processor.",
        sa_notification_date="2026-03-15T10:00:00+00:00",
        sa_reference_number="BLN-DPA-2026-00847",
        ds_notification_date="2026-03-16T06:00:00+00:00",
    )

    print(json.dumps(entry1, indent=2))

    print("\n" + "=" * 70)
    print("ENTRY COMPLETENESS VALIDATION")
    print("=" * 70)

    validation = validate_entry_completeness(entry1)
    print(json.dumps(validation, indent=2))

    print("\n" + "=" * 70)
    print("ANNUAL TREND REPORT")
    print("=" * 70)

    entries = [
        entry1,
        {
            "breach_reference": "SPG-BREACH-2026-001",
            "facts": {"breach_type": "confidentiality", "data_subject_count": 8, "root_cause": "human_error_misdirected_email"},
            "effects": {"risk_level": "unlikely_to_result_in_risk"},
            "notification_decisions": {
                "art_33_sa_notification": {"decision": "not_required"},
                "art_34_ds_notification": {"decision": "not_required"},
            },
        },
        {
            "breach_reference": "SPG-BREACH-2026-002",
            "facts": {"breach_type": "confidentiality", "data_subject_count": 340, "root_cause": "insider_unauthorized_access"},
            "effects": {"risk_level": "likely_to_result_in_risk"},
            "notification_decisions": {
                "art_33_sa_notification": {"decision": "submitted"},
                "art_34_ds_notification": {"decision": "required"},
            },
        },
    ]

    report = generate_trend_report(entries)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
