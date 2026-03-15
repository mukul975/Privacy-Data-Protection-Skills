#!/usr/bin/env python3
"""42 CFR Part 2 substance use disorder records consent management and compliance assessment."""

import json
import os
from datetime import datetime
from typing import Any


PART2_CONSENT_ELEMENTS = [
    "patient_name",
    "part2_program_name",
    "recipient_name_or_designation",
    "purpose_of_disclosure",
    "information_to_be_disclosed",
    "patient_signature",
    "date_signed",
    "revocability_statement",
    "expiration_date_event_condition",
    "redisclosure_prohibition_notice",
]

TPO_CONSENT_ELEMENTS_233 = [
    "patient_name",
    "part2_program_name",
    "general_recipient_designation",
    "tpo_purpose_statement",
    "patient_signature",
    "date_signed",
    "revocability_statement",
    "no_expiration_unless_revoked_statement",
    "antidiscrimination_notice",
    "redisclosure_notice",
]

DISCLOSURE_WITHOUT_CONSENT = [
    {"type": "medical_emergency", "ref": "§2.51", "conditions": ["bona_fide_emergency", "to_medical_personnel"]},
    {"type": "audit_evaluation", "ref": "§2.53", "conditions": ["government_agency_or_payer", "for_audit_evaluation"]},
    {"type": "internal_communication", "ref": "§2.12(c)(3)", "conditions": ["within_part2_program", "need_to_know"]},
    {"type": "crime_on_premises", "ref": "§2.12(c)(5)", "conditions": ["crime_on_program_premises", "to_law_enforcement"]},
    {"type": "child_abuse_reporting", "ref": "§2.12(c)(6)", "conditions": ["initial_report_only", "state_law_mandated"]},
]

REDISCLOSURE_NOTICE = (
    "This record which has been disclosed to you is protected by federal confidentiality rules "
    "(42 CFR Part 2). The federal rules prohibit you from making any further disclosure of "
    "information in this record that identifies a patient as having or having had a substance use "
    "disorder either directly, by reference to publicly available information, or through "
    "verification of such identification by another person unless further disclosure is expressly "
    "permitted by the written consent of the individual whose information is being disclosed or "
    "as otherwise permitted by 42 CFR Part 2. A general authorization for the release of medical "
    "or other information is NOT sufficient for this purpose (see §2.31). The federal rules "
    "restrict any use of the information to investigate or prosecute with regard to a crime any "
    "patient with a substance use disorder, except as provided at §§2.12(c)(5) and 2.65."
)


def validate_part2_consent(consent: dict[str, Any]) -> dict[str, Any]:
    """Validate a 42 CFR Part 2 consent form against required elements.

    Args:
        consent: Dictionary containing consent form fields.

    Returns:
        Validation result with missing elements and defects.
    """
    consent_type = consent.get("consent_type", "traditional")

    if consent_type == "tpo_233":
        required_elements = TPO_CONSENT_ELEMENTS_233
    else:
        required_elements = PART2_CONSENT_ELEMENTS

    result = {
        "consent_type": consent_type,
        "valid": True,
        "missing_elements": [],
        "defects": [],
        "validation_date": datetime.now().isoformat(),
    }

    for element in required_elements:
        if element not in consent or not consent[element]:
            result["missing_elements"].append(element)
            result["valid"] = False

    if consent.get("revoked"):
        result["defects"].append("Consent has been revoked")
        result["valid"] = False

    if consent_type == "traditional":
        expiration = consent.get("expiration_date_event_condition")
        if expiration and isinstance(expiration, str):
            try:
                exp_date = datetime.strptime(expiration, "%Y-%m-%d")
                if exp_date < datetime.now():
                    result["defects"].append("Consent has expired")
                    result["valid"] = False
            except ValueError:
                pass  # May be event-based

    return result


def evaluate_disclosure_permissibility(
    disclosure: dict[str, Any],
) -> dict[str, Any]:
    """Evaluate whether a Part 2 record disclosure is permitted.

    Args:
        disclosure: Dictionary describing the disclosure scenario.

    Returns:
        Permissibility determination with legal basis.
    """
    result = {
        "purpose": disclosure.get("purpose", ""),
        "evaluation_date": datetime.now().isoformat(),
        "permitted": False,
        "legal_basis": None,
        "consent_required": True,
        "redisclosure_notice_required": True,
        "conditions": [],
    }

    for exception in DISCLOSURE_WITHOUT_CONSENT:
        if disclosure.get("disclosure_type") == exception["type"]:
            conditions_met = all(
                disclosure.get(cond, False) for cond in exception["conditions"]
            )
            if conditions_met:
                result["permitted"] = True
                result["legal_basis"] = exception["ref"]
                result["consent_required"] = False
                result["conditions"].append(
                    f"Exception applies: {exception['type']} ({exception['ref']})"
                )
                if exception["type"] == "medical_emergency":
                    result["conditions"].append(
                        "Document: recipient, authorizing person, date/time, nature of emergency"
                    )
                return result

    if disclosure.get("has_tpo_consent_233"):
        is_tpo = disclosure.get("is_tpo", False)
        if is_tpo:
            result["permitted"] = True
            result["legal_basis"] = "§2.33 TPO consent"
            result["consent_required"] = False
            result["conditions"].append("§2.33 TPO consent covers this disclosure")
            result["conditions"].append("Anti-discrimination protections preserved (§2.12(d))")
            if disclosure.get("recipient_hipaa_covered"):
                result["conditions"].append(
                    "HIPAA-covered recipient may further use under HIPAA for TPO"
                )
            else:
                result["conditions"].append(
                    "Non-HIPAA recipient bound by traditional re-disclosure prohibition"
                )
            return result

    if disclosure.get("has_specific_consent"):
        consent_valid = disclosure.get("consent_validated", False)
        if consent_valid:
            result["permitted"] = True
            result["legal_basis"] = "§2.31 specific written consent"
            result["conditions"].append("Disclose as specified in consent")
            result["conditions"].append("Include re-disclosure prohibition notice")
            return result
        else:
            result["conditions"].append("Consent exists but has not been validated — validate before disclosure")
            return result

    if disclosure.get("court_order"):
        result["permitted"] = True
        result["legal_basis"] = "§2.64 court order"
        result["conditions"].append("Disclose only within scope of court order")
        result["conditions"].append("Include re-disclosure prohibition notice")
        return result

    result["conditions"].append("No consent, exception, or court order — disclosure NOT permitted")
    return result


def assess_part2_compliance(
    program: dict[str, Any],
) -> dict[str, Any]:
    """Assess a Part 2 program's compliance with 42 CFR Part 2 requirements.

    Args:
        program: Dictionary containing program compliance status.

    Returns:
        Compliance assessment results.
    """
    checks = [
        ("federally_assisted_determination", "Program has documented its federally assisted status"),
        ("consent_forms_compliant", "Consent forms contain all required Part 2 elements"),
        ("tpo_consent_offered", "§2.33 TPO consent option offered to patients"),
        ("redisclosure_notice_attached", "Re-disclosure prohibition notice attached to all disclosures"),
        ("ehr_segmentation", "Part 2 records segmented in EHR with appropriate access controls"),
        ("hie_exclusion_configured", "Part 2 records excluded from automated HIE feeds unless consent"),
        ("staff_trained", "All staff trained on Part 2 requirements (annual)"),
        ("consent_tracking", "Consent status tracked in EHR (granted/revoked/not requested)"),
        ("emergency_disclosure_documented", "Medical emergency disclosures documented per §2.51"),
        ("qsoa_or_baa_in_place", "QSOAs or Part 2-compliant BAAs with all service organizations"),
        ("court_order_procedures", "Court order request/response procedures documented"),
        ("minor_patient_procedures", "Minor patient consent procedures documented per §2.14"),
        ("breach_notification_aligned", "Breach notification aligned with HIPAA (2024 amendments)"),
        ("antidiscrimination_protections", "Anti-discrimination protections communicated to recipients"),
    ]

    compliance_status = program.get("compliance_status", {})
    result = {
        "program_name": program.get("name", ""),
        "assessment_date": datetime.now().isoformat(),
        "checks": [],
        "summary": {"total": 0, "compliant": 0, "non_compliant": 0, "not_assessed": 0},
    }

    for check_key, check_desc in checks:
        status = compliance_status.get(check_key, "not_assessed")
        result["checks"].append({
            "key": check_key,
            "description": check_desc,
            "status": status,
        })
        result["summary"]["total"] += 1
        if status == "compliant":
            result["summary"]["compliant"] += 1
        elif status == "non_compliant":
            result["summary"]["non_compliant"] += 1
        else:
            result["summary"]["not_assessed"] += 1

    total = result["summary"]["total"]
    compliant = result["summary"]["compliant"]
    result["summary"]["compliance_rate"] = round(compliant / total * 100, 1) if total > 0 else 0

    return result


if __name__ == "__main__":
    print("=== 42 CFR Part 2 Compliance Assessment ===\n")

    tpo_consent = {
        "consent_type": "tpo_233",
        "patient_name": "John Doe",
        "part2_program_name": "Asclepius SUD Treatment Center",
        "general_recipient_designation": "My treating providers and health plan",
        "tpo_purpose_statement": "Treatment, payment, and healthcare operations",
        "patient_signature": True,
        "date_signed": "2026-01-15",
        "revocability_statement": True,
        "no_expiration_unless_revoked_statement": True,
        "antidiscrimination_notice": True,
        "redisclosure_notice": True,
    }
    consent_result = validate_part2_consent(tpo_consent)
    print(f"TPO Consent Validation: Valid = {consent_result['valid']}")
    print(f"  Missing elements: {consent_result['missing_elements']}\n")

    disclosure_test = evaluate_disclosure_permissibility({
        "purpose": "Share SUD treatment records with patient's PCP for treatment coordination",
        "has_tpo_consent_233": True,
        "is_tpo": True,
        "recipient_hipaa_covered": True,
    })
    print(f"Disclosure Evaluation: Permitted = {disclosure_test['permitted']}")
    print(f"  Legal basis: {disclosure_test['legal_basis']}")
    for cond in disclosure_test["conditions"]:
        print(f"  Condition: {cond}")
