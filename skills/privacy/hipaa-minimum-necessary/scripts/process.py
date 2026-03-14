#!/usr/bin/env python3
"""HIPAA minimum necessary standard compliance assessment and role-based access analysis."""

import json
import os
from datetime import datetime
from typing import Any


MINIMUM_NECESSARY_EXCEPTIONS = [
    {"code": "treatment", "description": "Disclosure to/request by provider for treatment", "ref": "§164.502(b)(2)(i)"},
    {"code": "to_individual", "description": "Use or disclosure to the individual", "ref": "§164.502(b)(2)(ii)"},
    {"code": "authorization", "description": "Pursuant to valid authorization under §164.508", "ref": "§164.502(b)(2)(iii)"},
    {"code": "hhs_enforcement", "description": "Disclosure to HHS for compliance investigation", "ref": "§164.502(b)(2)(iv)"},
    {"code": "required_by_law", "description": "Use or disclosure required by law", "ref": "§164.502(b)(2)(v)"},
    {"code": "admin_simplification", "description": "HIPAA Administrative Simplification compliance", "ref": "§164.502(b)(2)(vi)"},
]

PHI_CATEGORIES = [
    "demographics",
    "insurance_information",
    "clinical_notes",
    "diagnoses",
    "medications",
    "lab_results",
    "radiology_reports",
    "surgical_records",
    "vital_signs",
    "allergies",
    "mental_health_notes",
    "substance_abuse_records",
    "hiv_status",
    "psychotherapy_notes",
    "billing_codes",
    "appointment_history",
    "correspondence",
    "advance_directives",
]


def evaluate_minimum_necessary(
    disclosure: dict[str, Any],
) -> dict[str, Any]:
    """Evaluate whether minimum necessary applies and what PHI should be disclosed.

    Args:
        disclosure: Dictionary describing the disclosure scenario.

    Returns:
        Evaluation result with minimum necessary determination and PHI scope.
    """
    result = {
        "purpose": disclosure.get("purpose", ""),
        "evaluation_date": datetime.now().isoformat(),
        "minimum_necessary_applies": True,
        "exception_applied": None,
        "disclosure_type": disclosure.get("disclosure_type", "non_routine"),
        "recommended_phi_scope": [],
        "excluded_phi": [],
        "rationale": "",
    }

    exception_code = disclosure.get("exception_code")
    if exception_code:
        for exc in MINIMUM_NECESSARY_EXCEPTIONS:
            if exc["code"] == exception_code:
                result["minimum_necessary_applies"] = False
                result["exception_applied"] = exc
                result["rationale"] = f"Minimum necessary does not apply: {exc['description']} ({exc['ref']})"
                result["recommended_phi_scope"] = disclosure.get("requested_phi", PHI_CATEGORIES)
                return result

    requested_phi = disclosure.get("requested_phi", [])
    necessary_phi = disclosure.get("necessary_phi", [])
    purpose = disclosure.get("purpose", "")

    if necessary_phi:
        result["recommended_phi_scope"] = necessary_phi
        result["excluded_phi"] = [p for p in requested_phi if p not in necessary_phi]
        if result["excluded_phi"]:
            result["rationale"] = (
                f"Minimum necessary applied: {len(result['excluded_phi'])} PHI categories "
                f"excluded as not necessary for stated purpose: {purpose}"
            )
        else:
            result["rationale"] = "All requested PHI categories are necessary for stated purpose"
    else:
        result["recommended_phi_scope"] = requested_phi
        result["rationale"] = "Minimum necessary review required — necessary PHI categories not pre-determined"

    return result


def assess_role_based_access(
    role_definitions: list[dict[str, Any]],
    user_access_records: list[dict[str, Any]],
) -> dict[str, Any]:
    """Assess user access against role-based PHI access definitions.

    Args:
        role_definitions: List of role definitions with permitted PHI categories.
        user_access_records: List of user records with current access.

    Returns:
        Assessment with compliance status, excess access findings, and gaps.
    """
    role_map = {rd["role"]: set(rd["permitted_phi"]) for rd in role_definitions}

    assessment = {
        "assessment_date": datetime.now().isoformat(),
        "total_users": len(user_access_records),
        "compliant_users": 0,
        "excess_access_users": 0,
        "insufficient_access_users": 0,
        "unknown_role_users": 0,
        "findings": [],
        "users": [],
    }

    for user in user_access_records:
        user_id = user.get("user_id", "")
        role = user.get("role", "")
        current_access = set(user.get("current_phi_access", []))

        user_result = {
            "user_id": user_id,
            "role": role,
            "status": "compliant",
            "current_access_count": len(current_access),
        }

        if role not in role_map:
            user_result["status"] = "unknown_role"
            assessment["unknown_role_users"] += 1
            assessment["findings"].append({
                "user_id": user_id,
                "issue": f"Role '{role}' not defined in role-based access policy",
                "severity": "high",
                "action": "Define role or reassign user to existing role",
            })
        else:
            permitted = role_map[role]
            excess = current_access - permitted
            missing = permitted - current_access

            if excess:
                user_result["status"] = "excess_access"
                user_result["excess_categories"] = list(excess)
                assessment["excess_access_users"] += 1
                assessment["findings"].append({
                    "user_id": user_id,
                    "issue": f"Excess access to {len(excess)} PHI categories beyond role definition",
                    "excess_categories": list(excess),
                    "severity": "high",
                    "action": "Remove excess PHI access immediately",
                })
            elif missing:
                user_result["status"] = "insufficient_access"
                assessment["insufficient_access_users"] += 1
            else:
                user_result["status"] = "compliant"
                assessment["compliant_users"] += 1

        assessment["users"].append(user_result)

    total = assessment["total_users"]
    compliant = assessment["compliant_users"]
    assessment["compliance_rate"] = round(compliant / total * 100, 1) if total > 0 else 0

    return assessment


def audit_disclosure_log(
    disclosures: list[dict[str, Any]],
) -> dict[str, Any]:
    """Audit disclosure log for minimum necessary compliance.

    Args:
        disclosures: List of disclosure records.

    Returns:
        Audit results with findings.
    """
    audit = {
        "audit_date": datetime.now().isoformat(),
        "total_disclosures": len(disclosures),
        "routine_disclosures": 0,
        "non_routine_disclosures": 0,
        "exempt_disclosures": 0,
        "findings": [],
        "compliant": 0,
        "non_compliant": 0,
    }

    for disc in disclosures:
        disc_type = disc.get("type", "non_routine")
        exception = disc.get("exception_code")

        if exception:
            audit["exempt_disclosures"] += 1
            continue

        if disc_type == "routine":
            audit["routine_disclosures"] += 1
            if not disc.get("standard_protocol_used"):
                audit["non_compliant"] += 1
                audit["findings"].append({
                    "disclosure_id": disc.get("id", ""),
                    "issue": "Routine disclosure made without standard protocol",
                    "severity": "medium",
                })
            else:
                audit["compliant"] += 1
        else:
            audit["non_routine_disclosures"] += 1
            if not disc.get("case_by_case_review"):
                audit["non_compliant"] += 1
                audit["findings"].append({
                    "disclosure_id": disc.get("id", ""),
                    "issue": "Non-routine disclosure without case-by-case review documentation",
                    "severity": "high",
                })
            else:
                audit["compliant"] += 1

        if disc.get("entire_record_disclosed") and not disc.get("entire_record_justified"):
            audit["findings"].append({
                "disclosure_id": disc.get("id", ""),
                "issue": "Entire medical record disclosed without documented justification",
                "severity": "high",
            })

    return audit


if __name__ == "__main__":
    print("=== HIPAA Minimum Necessary Compliance Assessment ===\n")

    treatment_disclosure = evaluate_minimum_necessary({
        "purpose": "Referral to cardiologist for treatment",
        "exception_code": "treatment",
        "requested_phi": ["clinical_notes", "medications", "lab_results", "vital_signs"],
    })
    print(f"Treatment Disclosure: Minimum necessary applies = {treatment_disclosure['minimum_necessary_applies']}")
    print(f"  Rationale: {treatment_disclosure['rationale']}\n")

    insurance_disclosure = evaluate_minimum_necessary({
        "purpose": "Insurance eligibility verification",
        "disclosure_type": "routine",
        "requested_phi": ["demographics", "insurance_information", "diagnoses", "clinical_notes"],
        "necessary_phi": ["demographics", "insurance_information"],
    })
    print(f"Insurance Verification: Minimum necessary applies = {insurance_disclosure['minimum_necessary_applies']}")
    print(f"  Recommended scope: {insurance_disclosure['recommended_phi_scope']}")
    print(f"  Excluded: {insurance_disclosure['excluded_phi']}\n")

    roles = [
        {"role": "attending_physician", "permitted_phi": ["demographics", "clinical_notes", "diagnoses", "medications", "lab_results", "radiology_reports", "vital_signs", "allergies", "surgical_records"]},
        {"role": "billing_specialist", "permitted_phi": ["demographics", "insurance_information", "billing_codes", "diagnoses"]},
        {"role": "registration_clerk", "permitted_phi": ["demographics", "insurance_information", "appointment_history"]},
    ]
    users = [
        {"user_id": "jsmith4821", "role": "attending_physician", "current_phi_access": ["demographics", "clinical_notes", "diagnoses", "medications", "lab_results", "radiology_reports", "vital_signs", "allergies", "surgical_records"]},
        {"user_id": "mjones2233", "role": "billing_specialist", "current_phi_access": ["demographics", "insurance_information", "billing_codes", "diagnoses", "clinical_notes", "medications"]},
        {"user_id": "klee5567", "role": "registration_clerk", "current_phi_access": ["demographics", "insurance_information", "appointment_history"]},
    ]

    access_assessment = assess_role_based_access(roles, users)
    print(f"Role-Based Access Assessment:")
    print(f"  Total users: {access_assessment['total_users']}")
    print(f"  Compliant: {access_assessment['compliant_users']}")
    print(f"  Excess access: {access_assessment['excess_access_users']}")
    print(f"  Compliance rate: {access_assessment['compliance_rate']}%")
    for finding in access_assessment["findings"]:
        print(f"  [{finding['severity'].upper()}] {finding['user_id']}: {finding['issue']}")
