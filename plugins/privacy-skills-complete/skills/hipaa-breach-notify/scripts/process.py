#!/usr/bin/env python3
"""HIPAA breach notification assessment, risk scoring, and timeline management processor."""

import json
import os
from datetime import datetime, timedelta
from typing import Any


RISK_ASSESSMENT_FACTORS = [
    "nature_and_extent_of_phi",
    "unauthorized_person",
    "phi_actually_acquired_or_viewed",
    "risk_mitigated",
]

NOTIFICATION_THRESHOLDS = {
    "individual_notice_deadline_days": 60,
    "hhs_large_breach_threshold": 500,
    "state_ag_threshold": 500,
    "media_threshold": 500,
    "ba_to_ce_deadline_days": 5,  # Asclepius standard
}

BREACH_EXCEPTIONS = {
    "unintentional_good_faith": {
        "ref": "§164.402(1)(i)",
        "conditions": ["within_scope_of_authority", "no_further_impermissible_use"],
    },
    "inadvertent_authorized_disclosure": {
        "ref": "§164.402(1)(ii)",
        "conditions": ["same_entity_or_oha", "no_further_impermissible_use"],
    },
    "good_faith_no_retention": {
        "ref": "§164.402(1)(iii)",
        "conditions": ["recipient_cannot_reasonably_retain"],
    },
}

PHI_SENSITIVITY_WEIGHTS = {
    "names_only": 1,
    "demographics": 2,
    "clinical_diagnosis": 3,
    "medications": 3,
    "substance_abuse": 5,
    "mental_health": 5,
    "hiv_status": 5,
    "genetic_information": 5,
    "ssn": 5,
    "financial_account": 5,
}

HHS_PORTAL_REQUIRED_FIELDS = [
    "covered_entity_name",
    "covered_entity_address",
    "covered_entity_type",
    "contact_name",
    "contact_phone",
    "contact_email",
    "number_affected",
    "breach_date",
    "discovery_date",
    "breach_type",
    "location_of_info",
    "phi_types_involved",
    "description",
    "safeguards_in_place",
    "actions_taken",
]


def conduct_four_factor_risk_assessment(
    incident: dict[str, Any],
) -> dict[str, Any]:
    """Conduct the four-factor breach risk assessment per §164.402(2).

    Args:
        incident: Dictionary containing incident details for each factor.

    Returns:
        Risk assessment with determination of whether notification is required.
    """
    result = {
        "incident_id": incident.get("incident_id", ""),
        "assessment_date": datetime.now().isoformat(),
        "factors": {},
        "overall_risk": "high",
        "breach_determination": "breach",
        "notification_required": True,
        "rationale": "",
    }

    # Factor 1: Nature and extent of PHI involved
    phi_types = incident.get("phi_types", [])
    max_sensitivity = max(
        (PHI_SENSITIVITY_WEIGHTS.get(pt, 3) for pt in phi_types),
        default=1,
    )
    phi_count = incident.get("data_elements_count", 0)

    factor1_risk = "low"
    if max_sensitivity >= 4 or phi_count > 5:
        factor1_risk = "high"
    elif max_sensitivity >= 3 or phi_count > 3:
        factor1_risk = "medium"

    result["factors"]["nature_and_extent_of_phi"] = {
        "phi_types": phi_types,
        "sensitivity_score": max_sensitivity,
        "data_elements_count": phi_count,
        "risk_level": factor1_risk,
    }

    # Factor 2: Unauthorized person
    unauthorized_person = incident.get("unauthorized_person", {})
    has_hipaa_obligation = unauthorized_person.get("hipaa_covered", False)
    is_malicious = unauthorized_person.get("malicious_intent", False)

    factor2_risk = "medium"
    if is_malicious:
        factor2_risk = "high"
    elif has_hipaa_obligation:
        factor2_risk = "low"

    result["factors"]["unauthorized_person"] = {
        "description": unauthorized_person.get("description", ""),
        "hipaa_covered": has_hipaa_obligation,
        "malicious_intent": is_malicious,
        "risk_level": factor2_risk,
    }

    # Factor 3: Whether PHI was actually acquired or viewed
    phi_accessed = incident.get("phi_accessed", {})
    actually_viewed = phi_accessed.get("actually_viewed", None)
    forensic_evidence = phi_accessed.get("forensic_evidence_available", False)
    encrypted_and_key_secure = phi_accessed.get("encrypted_and_key_secure", False)

    factor3_risk = "medium"
    if encrypted_and_key_secure:
        factor3_risk = "low"
        result["factors"]["phi_actually_acquired_or_viewed"] = {
            "encrypted_safe_harbor": True,
            "risk_level": "low",
            "note": "PHI was encrypted per HHS safe harbor; breach notification may not be required",
        }
    elif actually_viewed is True:
        factor3_risk = "high"
        result["factors"]["phi_actually_acquired_or_viewed"] = {
            "actually_viewed": True,
            "forensic_evidence": forensic_evidence,
            "risk_level": "high",
        }
    elif actually_viewed is False and forensic_evidence:
        factor3_risk = "low"
        result["factors"]["phi_actually_acquired_or_viewed"] = {
            "actually_viewed": False,
            "forensic_evidence": True,
            "risk_level": "low",
        }
    else:
        result["factors"]["phi_actually_acquired_or_viewed"] = {
            "actually_viewed": "unknown",
            "forensic_evidence": forensic_evidence,
            "risk_level": "medium",
            "note": "Unable to determine if PHI was viewed; risk remains elevated",
        }

    # Factor 4: Extent risk has been mitigated
    mitigation = incident.get("mitigation", {})
    assurances_obtained = mitigation.get("assurances_obtained", False)
    phi_recovered = mitigation.get("phi_recovered", False)
    recipient_destroyed = mitigation.get("recipient_destroyed", False)

    factor4_risk = "high"
    if phi_recovered or recipient_destroyed:
        factor4_risk = "low"
    elif assurances_obtained:
        factor4_risk = "medium"

    result["factors"]["risk_mitigated"] = {
        "assurances_obtained": assurances_obtained,
        "phi_recovered": phi_recovered,
        "recipient_destroyed": recipient_destroyed,
        "risk_level": factor4_risk,
    }

    # Overall determination
    risk_levels = [
        result["factors"]["nature_and_extent_of_phi"]["risk_level"],
        factor2_risk,
        factor3_risk,
        factor4_risk,
    ]

    if all(r == "low" for r in risk_levels):
        result["overall_risk"] = "low"
        result["breach_determination"] = "not_a_breach"
        result["notification_required"] = False
        result["rationale"] = "Low probability of compromise demonstrated across all four factors"
    elif encrypted_and_key_secure:
        result["overall_risk"] = "low"
        result["breach_determination"] = "secured_phi"
        result["notification_required"] = False
        result["rationale"] = "PHI was rendered unusable per HHS safe harbor (encryption with secure key)"
    else:
        high_count = sum(1 for r in risk_levels if r == "high")
        if high_count >= 2:
            result["overall_risk"] = "high"
        else:
            result["overall_risk"] = "medium"
        result["breach_determination"] = "breach"
        result["notification_required"] = True
        result["rationale"] = f"Risk assessment does not demonstrate low probability of compromise ({high_count} high-risk factors)"

    return result


def generate_notification_timeline(
    discovery_date: str,
    individuals_affected: int,
    states_affected: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Generate the complete notification timeline with all deadlines.

    Args:
        discovery_date: Date breach was discovered (YYYY-MM-DD).
        individuals_affected: Total number of individuals affected.
        states_affected: Dictionary mapping state codes to count of affected residents.

    Returns:
        Timeline with all notification deadlines and requirements.
    """
    discovery = datetime.strptime(discovery_date, "%Y-%m-%d")
    deadline_60 = discovery + timedelta(days=60)

    timeline = {
        "discovery_date": discovery_date,
        "individuals_affected": individuals_affected,
        "notification_deadline": deadline_60.strftime("%Y-%m-%d"),
        "days_remaining": (deadline_60 - datetime.now()).days,
        "notifications_required": {
            "individual": True,
            "hhs": True,
            "state_ag": [],
            "media": [],
        },
        "milestones": [],
    }

    timeline["milestones"].append({
        "action": "Complete forensic investigation and four-factor risk assessment",
        "target_date": (discovery + timedelta(days=14)).strftime("%Y-%m-%d"),
        "status": "pending",
    })
    timeline["milestones"].append({
        "action": "Draft notification letters; prepare call center",
        "target_date": (discovery + timedelta(days=30)).strftime("%Y-%m-%d"),
        "status": "pending",
    })

    if individuals_affected >= NOTIFICATION_THRESHOLDS["hhs_large_breach_threshold"]:
        timeline["notifications_required"]["hhs_type"] = "immediate"
        timeline["milestones"].append({
            "action": "Submit HHS breach portal notification (500+ — concurrent with individual notice)",
            "target_date": deadline_60.strftime("%Y-%m-%d"),
            "status": "pending",
        })
    else:
        timeline["notifications_required"]["hhs_type"] = "annual_log"
        timeline["milestones"].append({
            "action": "Log breach for annual HHS submission (within 60 days of calendar year end)",
            "target_date": f"{datetime.now().year}-12-31",
            "status": "pending",
        })

    if states_affected:
        for state, count in states_affected.items():
            if count >= NOTIFICATION_THRESHOLDS["state_ag_threshold"]:
                timeline["notifications_required"]["state_ag"].append({
                    "state": state,
                    "count": count,
                    "deadline": deadline_60.strftime("%Y-%m-%d"),
                })
                timeline["notifications_required"]["media"].append({
                    "state": state,
                    "count": count,
                    "deadline": deadline_60.strftime("%Y-%m-%d"),
                })

    timeline["milestones"].append({
        "action": "Mail individual notification letters (HARD DEADLINE)",
        "target_date": deadline_60.strftime("%Y-%m-%d"),
        "status": "pending",
    })
    timeline["milestones"].append({
        "action": "Post-notification monitoring and remediation",
        "target_date": (deadline_60 + timedelta(days=30)).strftime("%Y-%m-%d"),
        "status": "pending",
    })

    return timeline


def validate_hhs_submission(submission: dict[str, Any]) -> dict[str, Any]:
    """Validate HHS breach portal submission for required fields.

    Args:
        submission: Dictionary containing HHS portal submission fields.

    Returns:
        Validation result with missing fields and warnings.
    """
    result = {
        "valid": True,
        "missing_fields": [],
        "warnings": [],
        "timestamp": datetime.now().isoformat(),
    }

    for field in HHS_PORTAL_REQUIRED_FIELDS:
        if field not in submission or not submission[field]:
            result["missing_fields"].append(field)
            result["valid"] = False

    if submission.get("number_affected", 0) >= 500:
        if not submission.get("state_ag_notifications"):
            result["warnings"].append(
                "Breach affects 500+ individuals — verify state AG notifications are planned"
            )
        if not submission.get("media_notification_planned"):
            result["warnings"].append(
                "Breach affects 500+ individuals — verify media notification is planned for states with 500+ affected"
            )

    return result


def check_breach_exception(
    incident: dict[str, Any],
    exception_type: str,
) -> dict[str, Any]:
    """Check if a breach exception applies under §164.402(1).

    Args:
        incident: Incident details.
        exception_type: Type of exception to evaluate.

    Returns:
        Exception evaluation result.
    """
    result = {
        "exception_type": exception_type,
        "applicable": False,
        "conditions_met": {},
        "cfr_reference": "",
    }

    if exception_type not in BREACH_EXCEPTIONS:
        result["error"] = f"Unknown exception type: {exception_type}"
        return result

    exception = BREACH_EXCEPTIONS[exception_type]
    result["cfr_reference"] = exception["ref"]

    all_met = True
    for condition in exception["conditions"]:
        met = incident.get(condition, False)
        result["conditions_met"][condition] = met
        if not met:
            all_met = False

    result["applicable"] = all_met
    return result


def export_report(data: dict[str, Any], output_path: str) -> str:
    """Export report to JSON file."""
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return output_path


if __name__ == "__main__":
    print("=== HIPAA Breach Notification Assessment ===\n")

    incident = {
        "incident_id": "INC-2025-0087",
        "phi_types": ["demographics", "clinical_diagnosis", "ssn"],
        "data_elements_count": 7,
        "unauthorized_person": {
            "description": "External attacker via phishing",
            "hipaa_covered": False,
            "malicious_intent": True,
        },
        "phi_accessed": {
            "actually_viewed": True,
            "forensic_evidence_available": True,
            "encrypted_and_key_secure": False,
        },
        "mitigation": {
            "assurances_obtained": False,
            "phi_recovered": False,
            "recipient_destroyed": False,
        },
    }

    assessment = conduct_four_factor_risk_assessment(incident)
    print(f"Four-Factor Risk Assessment:")
    print(f"  Incident: {assessment['incident_id']}")
    print(f"  Overall Risk: {assessment['overall_risk']}")
    print(f"  Determination: {assessment['breach_determination']}")
    print(f"  Notification Required: {assessment['notification_required']}")
    print(f"  Rationale: {assessment['rationale']}\n")

    timeline = generate_notification_timeline(
        discovery_date="2026-02-15",
        individuals_affected=12500,
        states_affected={"CA": 3200, "TX": 4100, "NY": 2800, "FL": 2400},
    )
    print(f"Notification Timeline:")
    print(f"  Discovery Date: {timeline['discovery_date']}")
    print(f"  Deadline: {timeline['notification_deadline']}")
    print(f"  Days Remaining: {timeline['days_remaining']}")
    print(f"  HHS Report Type: {timeline['notifications_required']['hhs_type']}")
    print(f"  State AG Notifications: {len(timeline['notifications_required']['state_ag'])}")
    print(f"  Media Notifications: {len(timeline['notifications_required']['media'])}")
