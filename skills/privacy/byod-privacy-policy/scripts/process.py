"""
BYOD Privacy Policy Compliance Engine

Assesses BYOD programme compliance with GDPR data separation requirements,
MDM privacy boundaries, and selective wipe limitations.
"""

import json
from datetime import datetime
from typing import Optional


PERMITTED_MDM_CAPABILITIES = {
    "enforce_passcode": "Enforce device passcode/biometric lock",
    "encrypt_container": "Encrypt corporate container",
    "selective_wipe": "Remote wipe of corporate container only",
    "push_corporate_apps": "Push corporate apps to container",
    "enforce_os_version": "Enforce minimum OS version",
    "vpn_config": "VPN configuration for corporate traffic",
    "certificate_auth": "Certificate-based authentication",
}

PROHIBITED_MDM_CAPABILITIES = {
    "full_device_wipe": "Full device remote wipe",
    "personal_app_inventory": "Personal app inventory/listing",
    "personal_browsing": "Personal browsing history access",
    "personal_location": "Personal location tracking",
    "personal_email": "Personal email access",
    "personal_media": "Personal photo/media access",
    "mic_camera_activation": "Microphone/camera remote activation",
    "personal_call_log": "Personal call log access",
    "keylogging": "Keylogging on personal device",
}

MDM_APPROACHES = {
    "full_mdm": {
        "name": "Full Device MDM Enrolment",
        "privacy_impact": "very_high",
        "recommended_for_byod": False,
        "reason": "Grants employer visibility into personal data. Use only for corporate-owned devices.",
    },
    "work_profile": {
        "name": "Work Profile / Container",
        "privacy_impact": "low",
        "recommended_for_byod": True,
        "reason": "Isolates corporate data. Personal data invisible to employer.",
    },
    "app_level_mam": {
        "name": "App-Level Management (MAM)",
        "privacy_impact": "lowest",
        "recommended_for_byod": True,
        "reason": "Management limited to specific corporate apps. Minimal device access.",
    },
}


def assess_byod_compliance(
    mdm_approach: str,
    voluntary: bool,
    corporate_alternative_available: bool,
    permitted_enabled: list[str],
    prohibited_enabled: list[str],
    privacy_notice_provided: bool,
    byod_agreement_signed: bool,
    selective_wipe_only: bool,
    dpia_completed: bool,
) -> dict:
    """
    Assess BYOD programme compliance with privacy requirements.

    Args:
        mdm_approach: Key from MDM_APPROACHES.
        voluntary: Whether BYOD is genuinely voluntary.
        corporate_alternative_available: Whether corporate device alternative exists.
        permitted_enabled: List of enabled permitted capability keys.
        prohibited_enabled: List of enabled prohibited capability keys (should be empty).
        privacy_notice_provided: Whether privacy notice was given before enrolment.
        byod_agreement_signed: Whether BYOD agreement is in place.
        selective_wipe_only: Whether wipe is limited to corporate data.
        dpia_completed: Whether DPIA has been conducted.

    Returns:
        Compliance assessment with findings.
    """
    approach = MDM_APPROACHES.get(mdm_approach, MDM_APPROACHES["work_profile"])
    findings = []
    critical_failures = []

    # Voluntariness
    if not voluntary:
        critical_failures.append("BYOD is not voluntary — consent/enrolment invalid.")
    if not corporate_alternative_available:
        critical_failures.append("No corporate device alternative — BYOD cannot be considered voluntary.")

    # MDM approach
    if not approach["recommended_for_byod"]:
        critical_failures.append(
            f"MDM approach '{approach['name']}' is not recommended for BYOD. "
            f"Reason: {approach['reason']}"
        )

    # Prohibited capabilities
    for cap in prohibited_enabled:
        cap_name = PROHIBITED_MDM_CAPABILITIES.get(cap, cap)
        critical_failures.append(f"PROHIBITED capability enabled: {cap_name}. Must be disabled.")

    # Permitted capabilities review
    for cap in permitted_enabled:
        if cap in PERMITTED_MDM_CAPABILITIES:
            findings.append(f"Permitted capability enabled: {PERMITTED_MDM_CAPABILITIES[cap]}")

    # Documentation
    if not privacy_notice_provided:
        critical_failures.append("Privacy notice not provided before enrolment — Art. 13 violation.")
    if not byod_agreement_signed:
        findings.append("BYOD agreement not signed — recommended to formalise.")
    if not selective_wipe_only:
        critical_failures.append("Full device wipe capability exists — disproportionate for BYOD.")
    if not dpia_completed:
        findings.append("DPIA not completed — required if MDM includes monitoring capabilities.")

    compliant = len(critical_failures) == 0

    return {
        "assessment_date": datetime.now().isoformat(),
        "mdm_approach": approach["name"],
        "mdm_privacy_impact": approach["privacy_impact"],
        "mdm_recommended_for_byod": approach["recommended_for_byod"],
        "voluntary": voluntary,
        "corporate_alternative": corporate_alternative_available,
        "permitted_capabilities_enabled": len(permitted_enabled),
        "prohibited_capabilities_enabled": len(prohibited_enabled),
        "critical_failures": critical_failures,
        "findings": findings,
        "compliant": compliant,
        "recommendation": (
            "BYOD programme is compliant. Ensure annual review of MDM capabilities and privacy notice."
            if compliant
            else f"BYOD programme has {len(critical_failures)} critical failure(s). "
            f"Address all critical failures before programme can proceed."
        ),
    }


def main():
    """Example: Atlas Manufacturing Group BYOD assessment."""
    result = assess_byod_compliance(
        mdm_approach="app_level_mam",
        voluntary=True,
        corporate_alternative_available=True,
        permitted_enabled=["enforce_passcode", "encrypt_container", "selective_wipe", "push_corporate_apps"],
        prohibited_enabled=[],
        privacy_notice_provided=True,
        byod_agreement_signed=True,
        selective_wipe_only=True,
        dpia_completed=True,
    )

    print(json.dumps(result, indent=2))
    print(f"\nCompliant: {result['compliant']}")
    print(f"Recommendation: {result['recommendation']}")


if __name__ == "__main__":
    main()
