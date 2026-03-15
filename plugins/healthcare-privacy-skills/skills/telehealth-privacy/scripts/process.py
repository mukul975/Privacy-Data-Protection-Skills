#!/usr/bin/env python3
"""Telehealth privacy compliance assessment — platform evaluation, consent tracking, and RPM governance."""

import json
import os
from datetime import datetime
from typing import Any


TWO_PARTY_CONSENT_STATES = {
    "CA", "CT", "DE", "FL", "IL", "MD", "MA", "MI", "MT", "NH", "PA", "WA",
}

ONE_PARTY_CONSENT_STATES_AND_DC = {
    "AL", "AK", "AZ", "AR", "CO", "DC", "GA", "HI", "ID", "IN", "IA",
    "KS", "KY", "LA", "ME", "MN", "MS", "MO", "NE", "NV", "NJ", "NM",
    "NY", "NC", "ND", "OH", "OK", "OR", "RI", "SC", "SD", "TN", "TX",
    "UT", "VT", "VA", "WV", "WI", "WY",
}

COMPACT_MEMBERSHIPS = {
    "IMLC": {
        "name": "Interstate Medical Licensure Compact",
        "profession": "Physicians",
        "member_count": 42,
    },
    "NLC": {
        "name": "Nurse Licensure Compact",
        "profession": "RN/LPN",
        "member_count": 41,
    },
    "PSYPACT": {
        "name": "Psychology Interjurisdictional Compact",
        "profession": "Psychologists",
        "member_count": 42,
    },
}

PLATFORM_SECURITY_REQUIREMENTS = [
    {"id": "baa_available", "description": "Business Associate Agreement available and executed", "required": True},
    {"id": "e2e_encryption", "description": "End-to-end encryption for video/audio/data (AES-128+)", "required": True},
    {"id": "tls_1_2_plus", "description": "TLS 1.2 or higher for signaling channels", "required": True},
    {"id": "srtp_media", "description": "SRTP for media streams", "required": True},
    {"id": "no_unencrypted_fallback", "description": "No unencrypted fallback mode", "required": True},
    {"id": "unique_user_auth", "description": "Unique user authentication for providers", "required": True},
    {"id": "patient_verification", "description": "Patient identity verification process", "required": True},
    {"id": "session_access_control", "description": "Session-level access controls", "required": True},
    {"id": "auto_session_termination", "description": "Automatic session termination on disconnect/inactivity", "required": True},
    {"id": "mfa_provider", "description": "Multi-factor authentication for provider access", "required": True},
    {"id": "session_logging", "description": "Session event logging", "required": True},
    {"id": "recording_access_logs", "description": "Recording access audit logs", "required": True},
    {"id": "log_retention_6yr", "description": "Log retention minimum 6 years", "required": True},
    {"id": "tamper_resistant_logs", "description": "Tamper-resistant audit logs", "required": True},
    {"id": "data_location_documented", "description": "Data storage location documented", "required": True},
    {"id": "data_retention_policy", "description": "Data retention/deletion policies documented", "required": True},
]


def evaluate_platform_compliance(
    platform: dict[str, Any],
) -> dict[str, Any]:
    """Evaluate a telehealth platform for HIPAA compliance.

    Args:
        platform: Dictionary with platform security features.

    Returns:
        Compliance evaluation with pass/fail per requirement.
    """
    result = {
        "platform_name": platform.get("name", ""),
        "vendor": platform.get("vendor", ""),
        "evaluation_date": datetime.now().isoformat(),
        "requirements": [],
        "approved": True,
        "summary": {"total": 0, "passed": 0, "failed": 0},
    }

    features = platform.get("features", {})
    for req in PLATFORM_SECURITY_REQUIREMENTS:
        status = "passed" if features.get(req["id"], False) else "failed"
        result["requirements"].append({
            "id": req["id"],
            "description": req["description"],
            "required": req["required"],
            "status": status,
        })
        result["summary"]["total"] += 1
        if status == "passed":
            result["summary"]["passed"] += 1
        else:
            result["summary"]["failed"] += 1
            if req["required"]:
                result["approved"] = False

    total = result["summary"]["total"]
    passed = result["summary"]["passed"]
    result["summary"]["compliance_rate"] = round(passed / total * 100, 1) if total > 0 else 0

    return result


def determine_recording_consent(
    provider_state: str,
    patient_state: str,
) -> dict[str, Any]:
    """Determine recording consent requirements based on provider and patient states.

    Args:
        provider_state: Two-letter state code where provider is located.
        patient_state: Two-letter state code where patient is physically located.

    Returns:
        Recording consent requirements.
    """
    result = {
        "provider_state": provider_state,
        "patient_state": patient_state,
        "determination_date": datetime.now().isoformat(),
        "consent_model": "",
        "consent_required_from_patient": True,
        "governing_law": "",
        "recommendations": [],
    }

    provider_two_party = provider_state in TWO_PARTY_CONSENT_STATES
    patient_two_party = patient_state in TWO_PARTY_CONSENT_STATES

    if provider_two_party or patient_two_party:
        result["consent_model"] = "two_party"
        two_party_states = []
        if provider_two_party:
            two_party_states.append(provider_state)
        if patient_two_party:
            two_party_states.append(patient_state)
        result["governing_law"] = f"Two-party consent required ({', '.join(set(two_party_states))} law applies)"
        result["consent_required_from_patient"] = True
        result["recommendations"].append(
            "Obtain explicit consent from patient before recording"
        )
        result["recommendations"].append(
            "If patient declines, proceed without recording"
        )
    else:
        result["consent_model"] = "one_party"
        result["governing_law"] = f"One-party consent applies ({patient_state} law); provider consent is sufficient"
        result["consent_required_from_patient"] = False
        result["recommendations"].append(
            "Best practice: inform patient of recording even in one-party states"
        )

    result["recommendations"].append(
        "Document consent decision in the encounter record"
    )

    return result


def assess_cross_state_compliance(
    provider: dict[str, Any],
    patient_state: str,
) -> dict[str, Any]:
    """Assess cross-state telehealth practice compliance.

    Args:
        provider: Dictionary with provider licensing information.
        patient_state: State where patient is physically located.

    Returns:
        Cross-state compliance assessment.
    """
    result = {
        "provider_name": provider.get("name", ""),
        "provider_home_state": provider.get("home_state", ""),
        "patient_state": patient_state,
        "assessment_date": datetime.now().isoformat(),
        "licensed_in_patient_state": False,
        "compact_applicable": False,
        "compact_name": "",
        "prescribing_permitted": False,
        "controlled_substances_permitted": False,
        "issues": [],
    }

    provider_licenses = provider.get("licenses", [])
    if patient_state in provider_licenses:
        result["licensed_in_patient_state"] = True
        result["prescribing_permitted"] = True
    else:
        provider_type = provider.get("type", "physician")
        compact_map = {
            "physician": "IMLC",
            "nurse": "NLC",
            "psychologist": "PSYPACT",
        }
        compact = compact_map.get(provider_type)
        if compact and provider.get(f"{compact.lower()}_member"):
            result["compact_applicable"] = True
            result["compact_name"] = compact
            result["licensed_in_patient_state"] = True
            result["prescribing_permitted"] = True
        else:
            result["issues"].append(
                f"Provider not licensed in {patient_state} and no applicable compact — telehealth may not be permitted"
            )

    if result["prescribing_permitted"]:
        if provider.get("dea_registered"):
            ryan_haight_met = provider.get("ryan_haight_exemption") or provider.get("prior_in_person_eval")
            if ryan_haight_met:
                result["controlled_substances_permitted"] = True
            else:
                result["controlled_substances_permitted"] = False
                result["issues"].append(
                    "Ryan Haight Act: in-person evaluation required before prescribing controlled substances via telehealth (or DEA exemption must apply)"
                )

    pdmp_required = provider.get("pdmp_check_required", True)
    if pdmp_required and result["prescribing_permitted"]:
        result["pdmp_check_required"] = True
        result["pdmp_state"] = patient_state

    return result


def generate_telehealth_compliance_report(
    organization: dict[str, Any],
) -> dict[str, Any]:
    """Generate a comprehensive telehealth privacy compliance report.

    Args:
        organization: Dictionary containing organization telehealth program details.

    Returns:
        Compliance report.
    """
    checks = [
        ("platform_baa", "BAA executed with telehealth platform vendor"),
        ("platform_hipaa_compliant", "Telehealth platform meets HIPAA Security Rule requirements"),
        ("provider_training", "Annual telehealth-specific privacy training for providers"),
        ("patient_education", "Telehealth privacy information provided to patients at scheduling"),
        ("location_verification", "Patient physical location confirmed at each encounter"),
        ("recording_consent_process", "Recording consent process compliant with two-party consent states"),
        ("environmental_security", "Provider environmental security requirements documented and enforced"),
        ("incident_response", "Telehealth-specific incident response playbook maintained"),
        ("cross_state_licensing", "Cross-state licensing compliance tracked for all telehealth providers"),
        ("controlled_substance_protocol", "Ryan Haight Act compliance protocol for telehealth prescribing"),
        ("rpm_baa", "BAAs in place with all RPM platform vendors"),
        ("rpm_consent", "RPM informed consent obtained from enrolled patients"),
        ("compliance_monitoring", "Monthly telehealth compliance audits conducted"),
    ]

    compliance_status = organization.get("compliance_status", {})
    report = {
        "organization": organization.get("name", ""),
        "report_date": datetime.now().isoformat(),
        "checks": [],
        "summary": {"total": 0, "compliant": 0, "non_compliant": 0, "not_assessed": 0},
    }

    for check_key, check_desc in checks:
        status = compliance_status.get(check_key, "not_assessed")
        report["checks"].append({
            "key": check_key,
            "description": check_desc,
            "status": status,
        })
        report["summary"]["total"] += 1
        if status == "compliant":
            report["summary"]["compliant"] += 1
        elif status == "non_compliant":
            report["summary"]["non_compliant"] += 1
        else:
            report["summary"]["not_assessed"] += 1

    total = report["summary"]["total"]
    compliant = report["summary"]["compliant"]
    report["summary"]["compliance_rate"] = round(compliant / total * 100, 1) if total > 0 else 0

    return report


if __name__ == "__main__":
    print("=== Telehealth Privacy Compliance Assessment ===\n")

    platform = {
        "name": "Zoom for Healthcare",
        "vendor": "Zoom Video Communications",
        "features": {
            "baa_available": True,
            "e2e_encryption": True,
            "tls_1_2_plus": True,
            "srtp_media": True,
            "no_unencrypted_fallback": True,
            "unique_user_auth": True,
            "patient_verification": True,
            "session_access_control": True,
            "auto_session_termination": True,
            "mfa_provider": True,
            "session_logging": True,
            "recording_access_logs": True,
            "log_retention_6yr": True,
            "tamper_resistant_logs": True,
            "data_location_documented": True,
            "data_retention_policy": True,
        },
    }
    eval_result = evaluate_platform_compliance(platform)
    print(f"Platform: {eval_result['platform_name']}")
    print(f"  Approved: {eval_result['approved']}")
    print(f"  Compliance: {eval_result['summary']['compliance_rate']}%\n")

    recording = determine_recording_consent("NY", "CA")
    print(f"Recording Consent (NY provider, CA patient):")
    print(f"  Model: {recording['consent_model']}")
    print(f"  Patient consent required: {recording['consent_required_from_patient']}")
    print(f"  Law: {recording['governing_law']}\n")

    cross_state = assess_cross_state_compliance(
        provider={"name": "Dr. Smith", "home_state": "NY", "type": "physician", "licenses": ["NY", "NJ"], "dea_registered": True, "prior_in_person_eval": False},
        patient_state="CA",
    )
    print(f"Cross-State Assessment:")
    print(f"  Licensed in {cross_state['patient_state']}: {cross_state['licensed_in_patient_state']}")
    print(f"  Prescribing permitted: {cross_state['prescribing_permitted']}")
    for issue in cross_state["issues"]:
        print(f"  Issue: {issue}")
