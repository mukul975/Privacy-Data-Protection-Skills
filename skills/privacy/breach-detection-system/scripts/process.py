#!/usr/bin/env python3
"""
Breach Detection System — Alert Classification and Escalation Engine

Classifies security alerts against the breach detection taxonomy,
calculates composite insider threat scores, and determines escalation
paths based on data sensitivity and alert severity.
"""

import json
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class BreachType(Enum):
    CONFIDENTIALITY = "confidentiality"
    INTEGRITY = "integrity"
    AVAILABILITY = "availability"


class AttackVector(Enum):
    EXTERNAL = "external_attack"
    INSIDER = "insider_threat"
    THIRD_PARTY = "third_party_compromise"
    ACCIDENTAL = "accidental_disclosure"
    SYSTEM_FAILURE = "system_failure"
    PHYSICAL = "physical_breach"


class DataSensitivity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class AlertSeverity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFORMATIONAL = "informational"


ESCALATION_MATRIX = {
    ("critical", "critical"): {
        "escalation_targets": ["DPO", "CISO", "CEO", "General Counsel"],
        "response_time_minutes": 15,
        "auto_actions": ["isolate_system", "preserve_evidence", "activate_ir_team"],
    },
    ("critical", "high"): {
        "escalation_targets": ["DPO", "CISO", "SOC Lead"],
        "response_time_minutes": 30,
        "auto_actions": ["isolate_system", "preserve_evidence"],
    },
    ("high", "critical"): {
        "escalation_targets": ["DPO", "CISO", "SOC Lead"],
        "response_time_minutes": 30,
        "auto_actions": ["isolate_system", "preserve_evidence"],
    },
    ("high", "high"): {
        "escalation_targets": ["DPO", "SOC Lead"],
        "response_time_minutes": 60,
        "auto_actions": ["preserve_evidence"],
    },
    ("medium", "high"): {
        "escalation_targets": ["SOC Lead", "Privacy Coordinator"],
        "response_time_minutes": 60,
        "auto_actions": [],
    },
    ("medium", "medium"): {
        "escalation_targets": ["SOC Analyst"],
        "response_time_minutes": 120,
        "auto_actions": [],
    },
    ("low", "medium"): {
        "escalation_targets": ["SOC Analyst"],
        "response_time_minutes": 240,
        "auto_actions": [],
    },
    ("low", "low"): {
        "escalation_targets": ["SOC Analyst (batch review)"],
        "response_time_minutes": 480,
        "auto_actions": [],
    },
}


def classify_alert(
    alert_source: str,
    alert_description: str,
    affected_system: str,
    data_sensitivity: str,
    alert_severity: str,
    user_involved: Optional[str] = None,
    source_ip: Optional[str] = None,
    data_subject_estimate: Optional[int] = None,
) -> dict:
    """
    Classify a security alert and determine escalation path.

    Args:
        alert_source: Origin of the alert (SIEM, DLP, EDR, IDS).
        alert_description: Description of the detected activity.
        affected_system: Hostname or system identifier.
        data_sensitivity: Data sensitivity level of the affected system.
        alert_severity: Severity of the alert from the detection platform.
        user_involved: Username associated with the activity (if applicable).
        source_ip: Source IP address (if applicable).
        data_subject_estimate: Estimated number of data subjects on the system.

    Returns:
        Classification result with escalation path and recommended actions.
    """
    sensitivity = DataSensitivity(data_sensitivity)
    severity = AlertSeverity(alert_severity)

    breach_type = BreachType.CONFIDENTIALITY
    desc_lower = alert_description.lower()
    if any(kw in desc_lower for kw in ["ransomware", "encrypt", "unavailable", "destruction", "deleted"]):
        breach_type = BreachType.AVAILABILITY
    elif any(kw in desc_lower for kw in ["modified", "altered", "integrity", "injection", "tampered"]):
        breach_type = BreachType.INTEGRITY

    attack_vector = AttackVector.EXTERNAL
    if any(kw in desc_lower for kw in ["insider", "employee", "internal user", "authorized user"]):
        attack_vector = AttackVector.INSIDER
    elif any(kw in desc_lower for kw in ["accidental", "misdirected", "human error", "misconfigured"]):
        attack_vector = AttackVector.ACCIDENTAL
    elif any(kw in desc_lower for kw in ["vendor", "processor", "third-party", "supply chain"]):
        attack_vector = AttackVector.THIRD_PARTY
    elif any(kw in desc_lower for kw in ["hardware failure", "disk failure", "system crash"]):
        attack_vector = AttackVector.SYSTEM_FAILURE
    elif any(kw in desc_lower for kw in ["stolen device", "lost laptop", "physical"]):
        attack_vector = AttackVector.PHYSICAL

    lookup_key = (sensitivity.value, severity.value)
    escalation = ESCALATION_MATRIX.get(
        lookup_key,
        {"escalation_targets": ["SOC Analyst"], "response_time_minutes": 240, "auto_actions": []},
    )

    involves_personal_data = sensitivity in (DataSensitivity.CRITICAL, DataSensitivity.HIGH, DataSensitivity.MEDIUM)
    privacy_escalation_needed = (
        involves_personal_data
        and severity in (AlertSeverity.CRITICAL, AlertSeverity.HIGH)
    )

    return {
        "classification": {
            "breach_type": breach_type.value,
            "attack_vector": attack_vector.value,
            "data_sensitivity": sensitivity.value,
            "alert_severity": severity.value,
        },
        "alert_details": {
            "source": alert_source,
            "description": alert_description,
            "affected_system": affected_system,
            "user_involved": user_involved,
            "source_ip": source_ip,
            "data_subject_estimate": data_subject_estimate,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
        "involves_personal_data": involves_personal_data,
        "privacy_escalation_needed": privacy_escalation_needed,
        "escalation": {
            "targets": escalation["escalation_targets"],
            "response_time_minutes": escalation["response_time_minutes"],
            "automated_actions": escalation["auto_actions"],
        },
        "recommended_actions": generate_recommended_actions(breach_type, attack_vector, severity),
    }


def generate_recommended_actions(
    breach_type: BreachType,
    attack_vector: AttackVector,
    severity: AlertSeverity,
) -> list:
    """Generate context-specific recommended actions based on classification."""
    actions = []

    if severity in (AlertSeverity.CRITICAL, AlertSeverity.HIGH):
        actions.append("Immediately preserve volatile evidence (RAM dump, network connections)")

    if breach_type == BreachType.AVAILABILITY:
        actions.extend([
            "Verify backup integrity and availability for affected systems",
            "Determine whether data destruction is permanent or recoverable",
            "Check for ransomware indicators (ransom notes, encrypted file extensions)",
        ])
    elif breach_type == BreachType.CONFIDENTIALITY:
        actions.extend([
            "Determine whether data was exfiltrated or only accessed",
            "Identify all data subjects whose records were accessed",
            "Check for ongoing data transfer to external destinations",
        ])
    elif breach_type == BreachType.INTEGRITY:
        actions.extend([
            "Identify which records were modified and the nature of modifications",
            "Compare current data against last known good backup",
            "Assess whether data integrity issues could cause harm to data subjects",
        ])

    if attack_vector == AttackVector.INSIDER:
        actions.extend([
            "Preserve the suspect user account access logs before any account changes",
            "Coordinate with HR and legal before any employee confrontation",
            "Check DLP logs for data transfers by the identified user in the past 30 days",
        ])
    elif attack_vector == AttackVector.EXTERNAL:
        actions.extend([
            "Block identified attacker IPs at the network perimeter",
            "Check for lateral movement from the compromised system",
            "Verify that attacker access has been fully revoked",
        ])

    actions.append("Notify the DPO within 1 hour if personal data breach is confirmed")
    actions.append("Update the Art. 33(5) breach register with initial findings")

    return actions


def calculate_insider_threat_score(
    off_hours_access: bool = False,
    bulk_data_download: bool = False,
    personal_cloud_usage: bool = False,
    notice_period: bool = False,
    out_of_scope_access: bool = False,
    security_control_bypass: bool = False,
    repeated_failed_access: bool = False,
) -> dict:
    """
    Calculate composite insider threat risk score.

    Returns score, risk level, and recommended monitoring actions.
    """
    indicators = {
        "off_hours_access_to_personal_data": {"present": off_hours_access, "weight": 15},
        "bulk_data_download": {"present": bulk_data_download, "weight": 25},
        "personal_cloud_usage": {"present": personal_cloud_usage, "weight": 10},
        "notice_period_or_pip": {"present": notice_period, "weight": 20},
        "access_outside_role_scope": {"present": out_of_scope_access, "weight": 20},
        "security_control_bypass": {"present": security_control_bypass, "weight": 30},
        "repeated_failed_access_to_restricted_data": {"present": repeated_failed_access, "weight": 10},
    }

    total_score = sum(
        ind["weight"] for ind in indicators.values() if ind["present"]
    )
    max_score = sum(ind["weight"] for ind in indicators.values())

    if total_score >= 80:
        risk_level = "CRITICAL"
        action = "Immediate SOC investigation and DPO notification required"
    elif total_score >= 60:
        risk_level = "HIGH"
        action = "Enhanced monitoring activated; SOC analyst review within 4 hours"
    elif total_score >= 40:
        risk_level = "MEDIUM"
        action = "Elevated monitoring; weekly review by SOC team"
    else:
        risk_level = "LOW"
        action = "Standard monitoring; no additional action required"

    return {
        "composite_score": total_score,
        "max_possible_score": max_score,
        "risk_level": risk_level,
        "recommended_action": action,
        "indicators": {
            name: {"present": ind["present"], "weight": ind["weight"]}
            for name, ind in indicators.items()
        },
        "active_indicators": [
            name for name, ind in indicators.items() if ind["present"]
        ],
    }


def main():
    print("=" * 70)
    print("ALERT CLASSIFICATION — Ransomware Detection")
    print("=" * 70)

    alert1 = classify_alert(
        alert_source="CrowdStrike Falcon",
        alert_description="Ransomware behavior detected: rapid file encryption (LockBit 3.0 indicators) on db-prod-eu-west-01. Over 500 file rename operations per second.",
        affected_system="db-prod-eu-west-01",
        data_sensitivity="critical",
        alert_severity="critical",
        source_ip="10.0.1.50",
        data_subject_estimate=15230,
    )
    print(json.dumps(alert1, indent=2))

    print("\n" + "=" * 70)
    print("ALERT CLASSIFICATION — Suspicious Data Access")
    print("=" * 70)

    alert2 = classify_alert(
        alert_source="Splunk Enterprise Security",
        alert_description="Internal user accessed 2,847 customer records in a 15-minute window, exceeding the 500-record threshold. Access from authorized workstation during business hours.",
        affected_system="crm-prod-01",
        data_sensitivity="high",
        alert_severity="high",
        user_involved="m.schmidt@stellarpayments.eu",
        source_ip="10.10.5.34",
        data_subject_estimate=2847,
    )
    print(json.dumps(alert2, indent=2))

    print("\n" + "=" * 70)
    print("INSIDER THREAT SCORE — Departing Employee")
    print("=" * 70)

    insider_score = calculate_insider_threat_score(
        off_hours_access=True,
        bulk_data_download=True,
        personal_cloud_usage=True,
        notice_period=True,
        out_of_scope_access=False,
        security_control_bypass=False,
        repeated_failed_access=True,
    )
    print(json.dumps(insider_score, indent=2))

    print("\n" + "=" * 70)
    print("ALERT CLASSIFICATION — Accidental Email Disclosure")
    print("=" * 70)

    alert3 = classify_alert(
        alert_source="Microsoft 365 DLP",
        alert_description="Accidental disclosure: outbound email containing 8 customer invoices (names, addresses, amounts) sent to incorrect external recipient. DLP policy 'PII Outbound' triggered after delivery.",
        affected_system="Microsoft 365 Exchange Online",
        data_sensitivity="medium",
        alert_severity="medium",
        user_involved="l.martinez@stellarpayments.eu",
        data_subject_estimate=8,
    )
    print(json.dumps(alert3, indent=2))


if __name__ == "__main__":
    main()
