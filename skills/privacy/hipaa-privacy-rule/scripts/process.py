#!/usr/bin/env python3
"""HIPAA Privacy Rule compliance assessment and PHI disclosure tracking processor."""

import json
import csv
import os
from datetime import datetime, timedelta
from typing import Any


# --- PHI Disclosure Decision Engine ---

TREATMENT_PAYMENT_OPERATIONS = "tpo"
REQUIRED_BY_LAW = "required_by_law"
INDIVIDUAL_AUTHORIZATION = "authorization"
PUBLIC_INTEREST = "public_interest"
NOT_PERMITTED = "not_permitted"

PUBLIC_INTEREST_CATEGORIES = {
    "public_health": "§164.512(b)",
    "abuse_neglect": "§164.512(c)",
    "health_oversight": "§164.512(d)",
    "judicial_proceedings": "§164.512(e)",
    "law_enforcement": "§164.512(f)",
    "decedents": "§164.512(g)",
    "organ_donation": "§164.512(h)",
    "research": "§164.512(i)",
    "serious_threat": "§164.512(j)",
    "essential_government": "§164.512(k)",
    "workers_compensation": "§164.512(l)",
}

AUTHORIZATION_REQUIRED_ELEMENTS = [
    "description_of_information",
    "authorized_persons_to_disclose",
    "authorized_recipients",
    "purpose_of_disclosure",
    "expiration_date_or_event",
    "individual_signature",
    "signature_date",
    "right_to_revoke_statement",
    "conditioning_statement",
    "redisclosure_statement",
]

MINIMUM_NECESSARY_EXCEPTIONS = [
    "treatment_disclosure",
    "disclosure_to_individual",
    "pursuant_to_authorization",
    "disclosure_to_hhs",
    "required_by_law",
    "administrative_simplification",
]

PHI_18_IDENTIFIERS = [
    "names",
    "geographic_data_smaller_than_state",
    "dates_related_to_individual",
    "telephone_numbers",
    "fax_numbers",
    "email_addresses",
    "social_security_numbers",
    "medical_record_numbers",
    "health_plan_beneficiary_numbers",
    "account_numbers",
    "certificate_license_numbers",
    "vehicle_identifiers",
    "device_identifiers",
    "web_urls",
    "ip_addresses",
    "biometric_identifiers",
    "full_face_photographs",
    "other_unique_identifiers",
]


def evaluate_disclosure_permissibility(
    purpose: str,
    is_tpo: bool = False,
    is_required_by_law: bool = False,
    has_valid_authorization: bool = False,
    public_interest_category: str | None = None,
) -> dict[str, Any]:
    """Evaluate whether a PHI disclosure is permitted under the Privacy Rule.

    Args:
        purpose: Description of the disclosure purpose.
        is_tpo: Whether the disclosure is for treatment, payment, or healthcare operations.
        is_required_by_law: Whether the disclosure is required by law.
        has_valid_authorization: Whether a valid authorization exists per §164.508.
        public_interest_category: Public interest category key from §164.512.

    Returns:
        Dictionary with disclosure determination, legal basis, and conditions.
    """
    result = {
        "purpose": purpose,
        "timestamp": datetime.now().isoformat(),
        "permitted": False,
        "legal_basis": None,
        "cfr_reference": None,
        "minimum_necessary_applies": True,
        "conditions": [],
        "documentation_required": True,
    }

    if is_tpo:
        result["permitted"] = True
        result["legal_basis"] = TREATMENT_PAYMENT_OPERATIONS
        result["cfr_reference"] = "45 CFR §164.506"
        if "treatment" in purpose.lower():
            result["minimum_necessary_applies"] = False
            result["conditions"].append(
                "Treatment exception: minimum necessary does not apply"
            )
        else:
            result["conditions"].append(
                "Apply minimum necessary standard per §164.502(b)"
            )
        return result

    if is_required_by_law:
        result["permitted"] = True
        result["legal_basis"] = REQUIRED_BY_LAW
        result["cfr_reference"] = "45 CFR §164.512(a)"
        result["minimum_necessary_applies"] = False
        result["conditions"].append("Limit disclosure to what is legally mandated")
        return result

    if has_valid_authorization:
        result["permitted"] = True
        result["legal_basis"] = INDIVIDUAL_AUTHORIZATION
        result["cfr_reference"] = "45 CFR §164.508"
        result["minimum_necessary_applies"] = False
        result["conditions"].append(
            "Disclose only as specified in the authorization"
        )
        result["conditions"].append(
            "Verify authorization has not expired or been revoked"
        )
        return result

    if public_interest_category and public_interest_category in PUBLIC_INTEREST_CATEGORIES:
        result["permitted"] = True
        result["legal_basis"] = PUBLIC_INTEREST
        result["cfr_reference"] = PUBLIC_INTEREST_CATEGORIES[public_interest_category]
        result["conditions"].append(
            f"Apply {public_interest_category} specific requirements"
        )
        result["conditions"].append(
            "Apply minimum necessary standard per §164.502(b)"
        )
        return result

    result["legal_basis"] = NOT_PERMITTED
    result["conditions"].append(
        "No legal basis identified for disclosure. Do NOT disclose PHI."
    )
    return result


def validate_authorization(authorization: dict[str, Any]) -> dict[str, Any]:
    """Validate a HIPAA authorization form against §164.508(c) requirements.

    Args:
        authorization: Dictionary containing authorization form fields.

    Returns:
        Dictionary with validation result, missing elements, and defects.
    """
    result = {
        "valid": True,
        "missing_elements": [],
        "defects": [],
        "warnings": [],
        "timestamp": datetime.now().isoformat(),
    }

    for element in AUTHORIZATION_REQUIRED_ELEMENTS:
        if element not in authorization or not authorization[element]:
            result["missing_elements"].append(element)
            result["valid"] = False

    if authorization.get("expiration_date_or_event"):
        expiration = authorization["expiration_date_or_event"]
        if isinstance(expiration, str):
            try:
                exp_date = datetime.strptime(expiration, "%Y-%m-%d")
                if exp_date < datetime.now():
                    result["defects"].append("Authorization has expired")
                    result["valid"] = False
            except ValueError:
                pass  # May be an event-based expiration

    if authorization.get("revoked"):
        result["defects"].append("Authorization has been revoked")
        result["valid"] = False

    if authorization.get("material_false_information"):
        result["defects"].append(
            "Authorization contains known material false information"
        )
        result["valid"] = False

    if authorization.get("is_compound") and not authorization.get("research_related"):
        result["defects"].append(
            "Compound authorization not permitted except for research and related treatment (§164.508(b)(3))"
        )
        result["valid"] = False

    if authorization.get("personal_representative_signed"):
        if not authorization.get("representative_authority_description"):
            result["missing_elements"].append("representative_authority_description")
            result["valid"] = False

    return result


def assess_access_request(request: dict[str, Any]) -> dict[str, Any]:
    """Evaluate an individual right of access request under §164.524.

    Args:
        request: Dictionary containing access request details.

    Returns:
        Dictionary with access determination, timeline, and any denial basis.
    """
    result = {
        "request_id": request.get("request_id", ""),
        "requestor_type": request.get("requestor_type", "individual"),
        "identity_verified": request.get("identity_verified", False),
        "in_designated_record_set": request.get("in_designated_record_set", True),
        "access_granted": True,
        "denial_basis": None,
        "response_deadline": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
        "extension_available": True,
        "maximum_deadline": (datetime.now() + timedelta(days=60)).strftime("%Y-%m-%d"),
        "format_requested": request.get("format", "electronic"),
        "fee_applicable": True,
        "timestamp": datetime.now().isoformat(),
    }

    if not result["identity_verified"]:
        result["access_granted"] = False
        result["denial_basis"] = "Identity not verified — request identity verification before processing"
        return result

    if not result["in_designated_record_set"]:
        result["access_granted"] = False
        result["denial_basis"] = "Requested information is not in the designated record set"
        return result

    denial_grounds = request.get("denial_grounds", [])
    reviewable_denials = ["endangerment", "reference_to_other_person", "personal_representative_harm"]
    unreviewable_denials = ["psychotherapy_notes", "legal_proceedings", "clia_restricted", "inmate_safety", "research_in_progress"]

    for ground in denial_grounds:
        if ground in unreviewable_denials:
            result["access_granted"] = False
            result["denial_basis"] = f"Unreviewable denial: {ground} (§164.524(a)(2))"
            result["review_available"] = False
            return result
        if ground in reviewable_denials:
            result["access_granted"] = False
            result["denial_basis"] = f"Reviewable denial: {ground} (§164.524(a)(3))"
            result["review_available"] = True
            return result

    return result


def generate_disclosure_accounting(
    disclosures: list[dict[str, Any]],
    period_years: int = 6,
) -> dict[str, Any]:
    """Generate an accounting of disclosures per §164.528.

    Args:
        disclosures: List of disclosure records.
        period_years: Accounting period in years (default 6 per §164.528).

    Returns:
        Dictionary containing the accounting report.
    """
    cutoff_date = datetime.now() - timedelta(days=365 * period_years)

    excluded_categories = [
        "treatment",
        "payment",
        "healthcare_operations",
        "to_individual",
        "pursuant_to_authorization",
        "facility_directory",
        "persons_involved_in_care",
        "national_security",
        "correctional_institution",
        "limited_data_set",
    ]

    accountable_disclosures = []
    for disclosure in disclosures:
        disc_date = datetime.strptime(disclosure.get("date", ""), "%Y-%m-%d")
        if disc_date < cutoff_date:
            continue
        if disclosure.get("category") in excluded_categories:
            continue
        accountable_disclosures.append({
            "date": disclosure["date"],
            "recipient_name": disclosure.get("recipient_name", ""),
            "recipient_address": disclosure.get("recipient_address", ""),
            "description": disclosure.get("description", ""),
            "purpose": disclosure.get("purpose", ""),
        })

    return {
        "accounting_period_start": cutoff_date.strftime("%Y-%m-%d"),
        "accounting_period_end": datetime.now().strftime("%Y-%m-%d"),
        "total_disclosures_reviewed": len(disclosures),
        "accountable_disclosures": len(accountable_disclosures),
        "disclosures": accountable_disclosures,
        "generated_date": datetime.now().isoformat(),
    }


def run_privacy_compliance_assessment(
    organization: dict[str, Any],
) -> dict[str, Any]:
    """Run a HIPAA Privacy Rule compliance assessment for an organization.

    Args:
        organization: Dictionary containing organization details and current compliance status.

    Returns:
        Dictionary with compliance assessment results and gap analysis.
    """
    assessment_areas = {
        "npp_distribution": {
            "description": "Notice of Privacy Practices (§164.520)",
            "checks": [
                ("npp_current", "NPP is current and reflects actual practices"),
                ("npp_distributed_at_first_service", "NPP provided at first service delivery"),
                ("npp_acknowledgment_process", "Good faith effort to obtain written acknowledgment"),
                ("npp_posted_in_facility", "NPP posted in clear and prominent location"),
                ("npp_posted_on_website", "NPP posted on website if applicable"),
                ("npp_available_on_request", "NPP available to anyone who requests a copy"),
            ],
        },
        "individual_rights": {
            "description": "Individual Rights (§164.522-528)",
            "checks": [
                ("access_process_documented", "Right of access process documented and functioning"),
                ("access_30_day_response", "Access requests responded to within 30 days"),
                ("amendment_process", "Amendment request process documented"),
                ("accounting_of_disclosures", "Accounting of disclosures capability maintained"),
                ("restriction_requests", "Process for restriction requests including mandatory out-of-pocket restriction"),
                ("confidential_communications", "Confidential communications requests accommodated"),
            ],
        },
        "minimum_necessary": {
            "description": "Minimum Necessary Standard (§164.502(b), §164.514(d))",
            "checks": [
                ("role_based_access", "Role-based access policies define PHI categories per workforce class"),
                ("routine_disclosure_protocols", "Standard PHI sets for routine disclosures documented"),
                ("non_routine_review", "Case-by-case review criteria for non-routine disclosures"),
                ("reasonable_reliance", "Reasonable reliance policies documented"),
            ],
        },
        "authorization_management": {
            "description": "Authorization Management (§164.508)",
            "checks": [
                ("authorization_form_compliant", "Authorization form contains all required elements"),
                ("psychotherapy_notes_separated", "Psychotherapy notes authorization separate from other authorizations"),
                ("marketing_authorization", "Marketing uses require specific authorization"),
                ("authorization_tracking", "Authorization status tracked (active, expired, revoked)"),
            ],
        },
        "administrative_requirements": {
            "description": "Administrative Requirements (§164.530)",
            "checks": [
                ("privacy_officer_designated", "Privacy Officer designated"),
                ("privacy_policies_documented", "Privacy policies and procedures documented"),
                ("workforce_training", "All workforce members trained on privacy policies"),
                ("safeguards_implemented", "Administrative, technical, and physical safeguards for PHI"),
                ("complaint_process", "Complaint process documented and accessible"),
                ("sanction_policy", "Sanction policy for privacy violations"),
                ("no_retaliation_policy", "No retaliation policy for individuals exercising rights or filing complaints"),
                ("documentation_retention", "Documentation retained for 6 years from creation or last effective date"),
            ],
        },
        "business_associates": {
            "description": "Business Associate Requirements (§164.502(e), §164.504(e))",
            "checks": [
                ("ba_identification", "All business associate relationships identified"),
                ("baa_execution", "BAAs executed with all business associates"),
                ("baa_required_provisions", "BAAs contain all required provisions per §164.504(e)(2)"),
                ("ba_monitoring", "Business associate compliance monitored"),
            ],
        },
    }

    org_name = organization.get("name", "Unknown Organization")
    compliance_status = organization.get("compliance_status", {})

    results = {
        "organization": org_name,
        "assessment_date": datetime.now().isoformat(),
        "areas": {},
        "summary": {
            "total_checks": 0,
            "compliant": 0,
            "non_compliant": 0,
            "not_assessed": 0,
        },
    }

    for area_key, area_config in assessment_areas.items():
        area_result = {
            "description": area_config["description"],
            "checks": [],
            "compliant_count": 0,
            "total_count": len(area_config["checks"]),
        }

        for check_key, check_description in area_config["checks"]:
            status = compliance_status.get(check_key, "not_assessed")
            area_result["checks"].append({
                "key": check_key,
                "description": check_description,
                "status": status,
            })
            results["summary"]["total_checks"] += 1
            if status == "compliant":
                area_result["compliant_count"] += 1
                results["summary"]["compliant"] += 1
            elif status == "non_compliant":
                results["summary"]["non_compliant"] += 1
            else:
                results["summary"]["not_assessed"] += 1

        results["areas"][area_key] = area_result

    total = results["summary"]["total_checks"]
    compliant = results["summary"]["compliant"]
    results["summary"]["compliance_percentage"] = (
        round(compliant / total * 100, 1) if total > 0 else 0
    )

    return results


def export_assessment_report(assessment: dict[str, Any], output_path: str) -> str:
    """Export a compliance assessment to JSON file.

    Args:
        assessment: Assessment results from run_privacy_compliance_assessment.
        output_path: File path for the output JSON report.

    Returns:
        Path to the generated report file.
    """
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(assessment, f, indent=2, ensure_ascii=False)
    return output_path


if __name__ == "__main__":
    print("=== HIPAA Privacy Rule Compliance Assessment ===\n")

    disclosure_result = evaluate_disclosure_permissibility(
        purpose="Sending lab results to referring physician for treatment",
        is_tpo=True,
    )
    print(f"Disclosure Evaluation: {json.dumps(disclosure_result, indent=2)}\n")

    auth_test = {
        "description_of_information": "Complete medical records from 2023-2024",
        "authorized_persons_to_disclose": "Asclepius Health Network",
        "authorized_recipients": "Patient's personal injury attorney",
        "purpose_of_disclosure": "Legal representation",
        "expiration_date_or_event": "2026-12-31",
        "individual_signature": True,
        "signature_date": "2025-01-15",
        "right_to_revoke_statement": True,
        "conditioning_statement": True,
        "redisclosure_statement": True,
    }
    auth_result = validate_authorization(auth_test)
    print(f"Authorization Validation: {json.dumps(auth_result, indent=2)}\n")

    access_result = assess_access_request({
        "request_id": "AR-2025-0042",
        "requestor_type": "individual",
        "identity_verified": True,
        "in_designated_record_set": True,
        "format": "electronic",
    })
    print(f"Access Request Assessment: {json.dumps(access_result, indent=2)}\n")

    org = {
        "name": "Asclepius Health Network",
        "compliance_status": {
            "npp_current": "compliant",
            "npp_distributed_at_first_service": "compliant",
            "npp_acknowledgment_process": "compliant",
            "npp_posted_in_facility": "compliant",
            "npp_posted_on_website": "compliant",
            "npp_available_on_request": "compliant",
            "access_process_documented": "compliant",
            "access_30_day_response": "non_compliant",
            "amendment_process": "compliant",
            "accounting_of_disclosures": "compliant",
            "restriction_requests": "compliant",
            "confidential_communications": "compliant",
            "role_based_access": "compliant",
            "routine_disclosure_protocols": "compliant",
            "non_routine_review": "non_compliant",
            "reasonable_reliance": "compliant",
            "authorization_form_compliant": "compliant",
            "psychotherapy_notes_separated": "compliant",
            "marketing_authorization": "compliant",
            "authorization_tracking": "compliant",
            "privacy_officer_designated": "compliant",
            "privacy_policies_documented": "compliant",
            "workforce_training": "compliant",
            "safeguards_implemented": "compliant",
            "complaint_process": "compliant",
            "sanction_policy": "compliant",
            "no_retaliation_policy": "compliant",
            "documentation_retention": "compliant",
            "ba_identification": "compliant",
            "baa_execution": "non_compliant",
            "baa_required_provisions": "compliant",
            "ba_monitoring": "non_compliant",
        },
    }
    assessment = run_privacy_compliance_assessment(org)
    print(f"Compliance Assessment Summary:")
    print(f"  Total checks: {assessment['summary']['total_checks']}")
    print(f"  Compliant: {assessment['summary']['compliant']}")
    print(f"  Non-compliant: {assessment['summary']['non_compliant']}")
    print(f"  Compliance rate: {assessment['summary']['compliance_percentage']}%")
