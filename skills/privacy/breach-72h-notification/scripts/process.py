#!/usr/bin/env python3
"""
GDPR Article 33 — 72-Hour Breach Notification Deadline Calculator

Calculates the notification deadline from the breach discovery timestamp,
accounting for the continuous 72-hour clock. Provides risk scoring for
notification threshold determination and generates the notification
timeline with key milestones.
"""

import json
import sys
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Optional


class BreachType(Enum):
    CONFIDENTIALITY = "confidentiality"
    INTEGRITY = "integrity"
    AVAILABILITY = "availability"
    COMBINED = "combined"


class RiskLevel(Enum):
    NO_RISK = "unlikely_to_result_in_risk"
    RISK = "likely_to_result_in_risk"
    HIGH_RISK = "likely_to_result_in_high_risk"


EU_PUBLIC_HOLIDAYS_2026 = [
    datetime(2026, 1, 1, tzinfo=timezone.utc),    # New Year's Day
    datetime(2026, 4, 3, tzinfo=timezone.utc),     # Good Friday
    datetime(2026, 4, 6, tzinfo=timezone.utc),     # Easter Monday
    datetime(2026, 5, 1, tzinfo=timezone.utc),     # Labour Day
    datetime(2026, 5, 14, tzinfo=timezone.utc),    # Ascension Day
    datetime(2026, 5, 25, tzinfo=timezone.utc),    # Whit Monday
    datetime(2026, 10, 3, tzinfo=timezone.utc),    # German Unity Day
    datetime(2026, 12, 25, tzinfo=timezone.utc),   # Christmas Day
    datetime(2026, 12, 26, tzinfo=timezone.utc),   # St. Stephen's Day
]

SUPERVISORY_AUTHORITIES = {
    "DE": {
        "name": "BfDI / Landesdatenschutzbehörde",
        "portal": "bfdi.bund.de",
        "method": "Online portal submission",
    },
    "FR": {
        "name": "CNIL",
        "portal": "notifications.cnil.fr/notifications",
        "method": "Online notification form",
    },
    "GB": {
        "name": "ICO",
        "portal": "ico.org.uk/for-organisations/report-a-breach",
        "method": "Online self-service portal",
    },
    "IE": {
        "name": "DPC",
        "portal": "forms.dataprotection.ie",
        "method": "Online breach notification form",
    },
    "ES": {
        "name": "AEPD",
        "portal": "sedeagpd.gob.es",
        "method": "Electronic submission via sede electrónica",
    },
    "IT": {
        "name": "Garante",
        "portal": "protocollo@pec.gpdp.it",
        "method": "PEC certified email",
    },
    "NL": {
        "name": "Autoriteit Persoonsgegevens",
        "portal": "autoriteitpersoonsgegevens.nl/meldplicht-datalekken",
        "method": "Online notification form",
    },
    "BE": {
        "name": "APD/GBA",
        "portal": "gegevensbeschermingsautoriteit.be",
        "method": "Online notification form",
    },
    "AT": {
        "name": "DSB",
        "portal": "dsb.gv.at",
        "method": "Online notification form",
    },
    "PL": {
        "name": "UODO",
        "portal": "uodo.gov.pl",
        "method": "Electronic notification via ePUAP",
    },
}


def calculate_72_hour_deadline(
    discovery_timestamp: datetime,
) -> dict:
    """
    Calculate the 72-hour notification deadline from the discovery timestamp.

    The GDPR 72-hour clock runs continuously — weekends and holidays do NOT
    pause the clock. However, this function flags whether the deadline falls
    on a weekend or public holiday for operational awareness.

    Args:
        discovery_timestamp: UTC datetime when the controller became aware.

    Returns:
        Dictionary with deadline details and operational flags.
    """
    deadline = discovery_timestamp + timedelta(hours=72)

    milestone_4h = discovery_timestamp + timedelta(hours=4)
    milestone_12h = discovery_timestamp + timedelta(hours=12)
    milestone_24h = discovery_timestamp + timedelta(hours=24)
    milestone_48h = discovery_timestamp + timedelta(hours=48)
    milestone_60h = discovery_timestamp + timedelta(hours=60)

    deadline_date = deadline.replace(hour=0, minute=0, second=0, microsecond=0)
    falls_on_weekend = deadline.weekday() in (5, 6)
    falls_on_holiday = deadline_date in [
        h.replace(tzinfo=timezone.utc) for h in EU_PUBLIC_HOLIDAYS_2026
    ]

    now = datetime.now(timezone.utc)
    remaining = deadline - now
    remaining_hours = max(0, remaining.total_seconds() / 3600)

    if remaining_hours <= 0:
        urgency = "OVERDUE"
    elif remaining_hours <= 12:
        urgency = "CRITICAL"
    elif remaining_hours <= 24:
        urgency = "HIGH"
    elif remaining_hours <= 48:
        urgency = "MEDIUM"
    else:
        urgency = "NORMAL"

    return {
        "discovery_timestamp": discovery_timestamp.isoformat(),
        "notification_deadline": deadline.isoformat(),
        "remaining_hours": round(remaining_hours, 2),
        "urgency_level": urgency,
        "falls_on_weekend": falls_on_weekend,
        "falls_on_public_holiday": falls_on_holiday,
        "milestones": {
            "triage_complete_by": milestone_4h.isoformat(),
            "rapid_assessment_by": milestone_12h.isoformat(),
            "risk_assessment_by": milestone_24h.isoformat(),
            "notification_drafted_by": milestone_48h.isoformat(),
            "final_review_by": milestone_60h.isoformat(),
            "submission_deadline": deadline.isoformat(),
        },
        "operational_note": (
            "The 72-hour clock runs continuously per EDPB Guidelines 9/2022. "
            "Weekends and public holidays do NOT pause the countdown. "
            f"{'WARNING: Deadline falls on a weekend. Ensure on-call DPO availability. ' if falls_on_weekend else ''}"
            f"{'WARNING: Deadline falls on a public holiday. Confirm supervisory authority portal availability. ' if falls_on_holiday else ''}"
        ).strip(),
    }


def assess_breach_risk(
    data_sensitivity: int,
    volume: int,
    identifiability: int,
    consequences: int,
    vulnerable_subjects: int,
    controller_specific: int,
) -> dict:
    """
    Assess breach risk using the EDPB-aligned scoring methodology.

    Each factor is scored 1-4:
        1 = Low
        2 = Medium
        3 = High
        4 = Severe

    Args:
        data_sensitivity: Sensitivity of data involved (1-4).
        volume: Number of data subjects affected (1-4).
        identifiability: Ease of identifying individuals from breached data (1-4).
        consequences: Severity of potential consequences (1-4).
        vulnerable_subjects: Whether vulnerable individuals are affected (1-4).
        controller_specific: Controller role amplification factor (1-4).

    Returns:
        Dictionary with risk score, level, and notification requirements.
    """
    factors = {
        "data_sensitivity": data_sensitivity,
        "volume": volume,
        "identifiability": identifiability,
        "consequences": consequences,
        "vulnerable_subjects": vulnerable_subjects,
        "controller_specific": controller_specific,
    }

    for name, value in factors.items():
        if not 1 <= value <= 4:
            raise ValueError(f"{name} must be between 1 and 4, got {value}")

    total_score = sum(factors.values())

    if total_score <= 6:
        risk_level = RiskLevel.NO_RISK
        sa_notification = False
        ds_notification = False
        rationale = (
            "Aggregate risk score of {score} indicates the breach is unlikely "
            "to result in a risk to the rights and freedoms of natural persons. "
            "Supervisory authority notification is NOT required under Art. 33(1). "
            "The breach MUST still be documented in the Art. 33(5) breach register."
        ).format(score=total_score)
    elif total_score <= 15:
        risk_level = RiskLevel.RISK
        sa_notification = True
        ds_notification = False
        rationale = (
            "Aggregate risk score of {score} indicates the breach is likely "
            "to result in a risk to the rights and freedoms of natural persons. "
            "Supervisory authority notification is REQUIRED within 72 hours "
            "under Art. 33(1). Data subject notification under Art. 34 is not "
            "required at this risk level unless specific high-risk indicators "
            "are present."
        ).format(score=total_score)
    else:
        risk_level = RiskLevel.HIGH_RISK
        sa_notification = True
        ds_notification = True
        rationale = (
            "Aggregate risk score of {score} indicates the breach is likely "
            "to result in a HIGH risk to the rights and freedoms of natural "
            "persons. Supervisory authority notification is REQUIRED within "
            "72 hours under Art. 33(1). Data subject notification is also "
            "REQUIRED without undue delay under Art. 34(1)."
        ).format(score=total_score)

    return {
        "factor_scores": factors,
        "total_score": total_score,
        "max_possible_score": 24,
        "risk_level": risk_level.value,
        "supervisory_authority_notification_required": sa_notification,
        "data_subject_notification_required": ds_notification,
        "rationale": rationale,
        "art_33_5_documentation_required": True,
    }


def generate_notification_record(
    breach_type: str,
    discovery_timestamp: str,
    affected_subjects_count: int,
    affected_records_count: int,
    data_categories: list,
    subject_categories: list,
    description: str,
    containment_measures: list,
    remediation_measures: list,
    jurisdiction: str = "DE",
    risk_scores: Optional[dict] = None,
) -> dict:
    """
    Generate a structured Art. 33(3) notification record.

    Args:
        breach_type: One of 'confidentiality', 'integrity', 'availability', 'combined'.
        discovery_timestamp: ISO 8601 UTC timestamp of awareness.
        affected_subjects_count: Approximate number of affected data subjects.
        affected_records_count: Approximate number of affected records.
        data_categories: List of personal data categories compromised.
        subject_categories: List of data subject categories affected.
        description: Narrative description of the breach.
        containment_measures: List of containment actions taken.
        remediation_measures: List of planned remediation actions.
        jurisdiction: ISO 3166-1 alpha-2 country code for lead SA.
        risk_scores: Optional pre-computed risk assessment scores.

    Returns:
        Complete notification record dictionary.
    """
    discovery_dt = datetime.fromisoformat(discovery_timestamp)
    if discovery_dt.tzinfo is None:
        discovery_dt = discovery_dt.replace(tzinfo=timezone.utc)

    deadline_info = calculate_72_hour_deadline(discovery_dt)

    authority = SUPERVISORY_AUTHORITIES.get(jurisdiction, SUPERVISORY_AUTHORITIES["DE"])

    notification = {
        "notification_metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "gdpr_article": "Article 33",
            "notification_type": "initial",
            "competent_supervisory_authority": authority,
            "jurisdiction": jurisdiction,
        },
        "art_33_3_a_nature_of_breach": {
            "breach_type": breach_type,
            "description": description,
            "categories_of_data_subjects": subject_categories,
            "approximate_number_of_data_subjects": affected_subjects_count,
            "categories_of_personal_data": data_categories,
            "approximate_number_of_records": affected_records_count,
        },
        "art_33_3_b_dpo_contact": {
            "name": "Dr. Elena Vasquez",
            "title": "Data Protection Officer",
            "organization": "Stellar Payments Group",
            "email": "dpo@stellarpayments.eu",
            "phone": "+49 30 7742 8001",
            "address": "Friedrichstraße 191, 10117 Berlin, Germany",
        },
        "art_33_3_c_likely_consequences": {
            "assessment_pending": risk_scores is None,
            "risk_assessment": risk_scores,
        },
        "art_33_3_d_measures": {
            "containment_measures_taken": containment_measures,
            "remediation_measures_planned": remediation_measures,
            "data_subjects_notified": False,
            "data_subject_notification_planned": (
                risk_scores.get("data_subject_notification_required", False)
                if risk_scores
                else "pending_assessment"
            ),
        },
        "deadline_information": deadline_info,
    }

    return notification


def main():
    print("=" * 70)
    print("GDPR Art. 33 — 72-Hour Breach Notification Deadline Calculator")
    print("=" * 70)

    # Scenario: Breach discovered at 14:30 UTC on Friday, March 13, 2026
    discovery = datetime(2026, 3, 13, 14, 30, 0, tzinfo=timezone.utc)

    print(f"\nBreach Discovery: {discovery.strftime('%A, %d %B %Y at %H:%M UTC')}")

    deadline_info = calculate_72_hour_deadline(discovery)
    deadline_dt = datetime.fromisoformat(deadline_info["notification_deadline"])

    print(f"Notification Deadline: {deadline_dt.strftime('%A, %d %B %Y at %H:%M UTC')}")
    print(f"Remaining Hours: {deadline_info['remaining_hours']}")
    print(f"Urgency Level: {deadline_info['urgency_level']}")
    print(f"Falls on Weekend: {deadline_info['falls_on_weekend']}")
    print(f"Falls on Public Holiday: {deadline_info['falls_on_public_holiday']}")

    print("\nMilestones:")
    for milestone, timestamp in deadline_info["milestones"].items():
        dt = datetime.fromisoformat(timestamp)
        print(f"  {milestone}: {dt.strftime('%A %d %B %H:%M UTC')}")

    print(f"\nOperational Note: {deadline_info['operational_note']}")

    # Risk Assessment Example: Ransomware encrypting customer database
    print("\n" + "=" * 70)
    print("Risk Assessment — Ransomware Attack on Customer Database")
    print("=" * 70)

    risk = assess_breach_risk(
        data_sensitivity=3,     # Financial and identity data
        volume=3,               # ~15,000 data subjects
        identifiability=4,      # Directly identifiable (names + addresses)
        consequences=3,         # Financial loss and identity theft risk
        vulnerable_subjects=2,  # General adult population
        controller_specific=3,  # Payment processor — elevated responsibility
    )

    print(f"\nFactor Scores: {json.dumps(risk['factor_scores'], indent=2)}")
    print(f"Total Score: {risk['total_score']} / {risk['max_possible_score']}")
    print(f"Risk Level: {risk['risk_level']}")
    print(f"SA Notification Required: {risk['supervisory_authority_notification_required']}")
    print(f"DS Notification Required: {risk['data_subject_notification_required']}")
    print(f"Rationale: {risk['rationale']}")

    # Generate Full Notification Record
    print("\n" + "=" * 70)
    print("Generated Art. 33(3) Notification Record")
    print("=" * 70)

    record = generate_notification_record(
        breach_type="availability",
        discovery_timestamp="2026-03-13T14:30:00+00:00",
        affected_subjects_count=15230,
        affected_records_count=48720,
        data_categories=[
            "Full names",
            "Postal addresses",
            "Email addresses",
            "Payment card numbers (last 4 digits)",
            "Transaction histories",
            "Account balances",
        ],
        subject_categories=[
            "Individual account holders",
            "Business account holders",
            "Joint account holders",
        ],
        description=(
            "On 13 March 2026 at approximately 11:15 UTC, Stellar Payments Group "
            "detected anomalous encryption activity on the production customer "
            "database cluster (db-prod-eu-west-01 through db-prod-eu-west-04). "
            "Investigation confirmed a ransomware attack (LockBit 3.0 variant) "
            "that encrypted 48,720 customer records across three account holder "
            "categories. The attack vector was a compromised service account "
            "credential obtained through a spear-phishing email targeting an IT "
            "operations engineer on 10 March 2026. The encryption rendered all "
            "affected records unavailable. No evidence of data exfiltration has "
            "been identified as of the time of this notification, though "
            "forensic analysis is ongoing."
        ),
        containment_measures=[
            "Isolated affected database cluster from the network at 12:45 UTC on 13 March 2026",
            "Revoked all service account credentials associated with the compromised account",
            "Activated backup restoration from the 12 March 2026 23:00 UTC snapshot",
            "Deployed endpoint detection and response (EDR) sweep across all infrastructure",
            "Engaged Mandiant incident response team under retainer agreement SPG-IR-2025-007",
        ],
        remediation_measures=[
            "Complete restoration of customer database from verified clean backups (ETA: 15 March 2026)",
            "Implement mandatory multi-factor authentication for all service accounts",
            "Deploy network segmentation between database tier and application tier",
            "Conduct organization-wide phishing awareness retraining",
            "Perform full vulnerability assessment of database infrastructure",
            "Review and update access control policies for privileged accounts",
        ],
        jurisdiction="DE",
        risk_scores=risk,
    )

    print(json.dumps(record, indent=2, default=str))


if __name__ == "__main__":
    main()
