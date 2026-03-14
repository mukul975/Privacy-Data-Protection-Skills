#!/usr/bin/env python3
"""
GDPR Lawful Basis Assessment Tool

Implements a decision-tree assessment for determining the appropriate
lawful basis under GDPR Article 6(1)(a)-(f) for a given processing activity.
"""

import json
import sys
from datetime import datetime
from typing import Any


LAWFUL_BASES = {
    "6(1)(a)": {
        "name": "Consent",
        "description": "Data subject has given consent for specific purposes",
        "available_rights": [
            "access", "rectification", "erasure", "restriction",
            "portability", "withdraw_consent"
        ],
    },
    "6(1)(b)": {
        "name": "Contract Performance",
        "description": "Necessary for performance of a contract with the data subject",
        "available_rights": [
            "access", "rectification", "erasure", "restriction", "portability"
        ],
    },
    "6(1)(c)": {
        "name": "Legal Obligation",
        "description": "Necessary for compliance with a legal obligation",
        "available_rights": ["access", "rectification", "restriction"],
    },
    "6(1)(d)": {
        "name": "Vital Interests",
        "description": "Necessary to protect vital interests of data subject or another person",
        "available_rights": ["access", "rectification", "erasure", "restriction"],
    },
    "6(1)(e)": {
        "name": "Public Task",
        "description": "Necessary for task in public interest or exercise of official authority",
        "available_rights": ["access", "rectification", "restriction", "object"],
    },
    "6(1)(f)": {
        "name": "Legitimate Interests",
        "description": "Necessary for legitimate interests unless overridden by data subject rights",
        "available_rights": [
            "access", "rectification", "erasure", "restriction", "object"
        ],
    },
}

SPECIAL_CATEGORY_CONDITIONS = {
    "9(2)(a)": "Explicit consent",
    "9(2)(b)": "Employment, social security, social protection law",
    "9(2)(c)": "Vital interests where data subject incapable of consent",
    "9(2)(d)": "Legitimate activities of not-for-profit body",
    "9(2)(e)": "Data manifestly made public by the data subject",
    "9(2)(f)": "Legal claims or judicial acts",
    "9(2)(g)": "Substantial public interest (Member State law basis required)",
    "9(2)(h)": "Healthcare purposes under health professional responsibility",
    "9(2)(i)": "Public health (Union or Member State law)",
    "9(2)(j)": "Archiving, scientific/historical research, statistics",
}


def assess_legal_obligation(activity: dict) -> dict:
    result = {"basis": None, "rationale": "", "issues": []}
    legal_ref = activity.get("legal_obligation_reference")

    if not legal_ref:
        result["rationale"] = "No legal obligation identified for this processing."
        return result

    if not legal_ref.get("law_name") or not legal_ref.get("provision"):
        result["issues"].append(
            "Legal obligation referenced but missing specific law name or provision number."
        )
        return result

    law_name = legal_ref["law_name"]
    provision = legal_ref["provision"]
    result["basis"] = "6(1)(c)"
    result["rationale"] = (
        f"Processing is required by {law_name}, {provision}. "
        f"The obligation specifically mandates the processing of the identified personal data categories."
    )
    return result


def assess_contract_performance(activity: dict) -> dict:
    result = {"basis": None, "rationale": "", "issues": []}
    contract = activity.get("contract_details")

    if not contract:
        result["rationale"] = "No contract with the data subject identified."
        return result

    is_necessary = contract.get("processing_objectively_necessary", False)
    is_pre_contractual = contract.get("pre_contractual_at_subject_request", False)

    if not is_necessary and not is_pre_contractual:
        result["issues"].append(
            "Processing is related to a contract but has not been demonstrated as objectively necessary. "
            "Per EDPB Guidelines 2/2019, processing must be essential for contract fulfilment, not merely useful."
        )
        return result

    contract_ref = contract.get("contract_reference", "unspecified contract")
    result["basis"] = "6(1)(b)"
    if is_pre_contractual:
        result["rationale"] = (
            f"Processing is necessary for pre-contractual steps requested by the data subject "
            f"in relation to {contract_ref}."
        )
    else:
        result["rationale"] = (
            f"Processing is objectively necessary for performance of {contract_ref} with the data subject. "
            f"The contract cannot be fulfilled without this processing."
        )
    return result


def assess_vital_interests(activity: dict) -> bool:
    return activity.get("vital_interest_scenario", False)


def assess_public_task(activity: dict) -> dict:
    result = {"basis": None, "rationale": "", "issues": []}
    public_task = activity.get("public_task_details")

    if not public_task:
        return result

    is_public_authority = public_task.get("controller_is_public_authority", False)
    legal_basis_for_task = public_task.get("legal_basis_for_task")

    if is_public_authority and legal_basis_for_task:
        result["basis"] = "6(1)(e)"
        result["rationale"] = (
            f"Processing is necessary for the performance of a public task under "
            f"{legal_basis_for_task}."
        )
    elif is_public_authority and not legal_basis_for_task:
        result["issues"].append(
            "Controller is a public authority but no specific legal basis for the task has been identified."
        )

    return result


def assess_legitimate_interests(activity: dict) -> dict:
    result = {"basis": None, "rationale": "", "issues": []}
    lia = activity.get("legitimate_interest_assessment")

    if not lia:
        result["rationale"] = "No legitimate interest assessment provided."
        return result

    purpose_test = lia.get("purpose_test", {})
    necessity_test = lia.get("necessity_test", {})
    balancing_test = lia.get("balancing_test", {})

    issues = []

    if not purpose_test.get("interest_identified"):
        issues.append("Purpose test: No legitimate interest has been clearly articulated.")

    if not necessity_test.get("is_necessary"):
        issues.append(
            "Necessity test: Processing has not been demonstrated as necessary for the stated interest."
        )

    if necessity_test.get("less_intrusive_alternative_available"):
        issues.append(
            f"Necessity test: A less intrusive alternative exists — "
            f"{necessity_test.get('alternative_description', 'not described')}."
        )

    if balancing_test.get("data_subject_rights_override"):
        issues.append(
            "Balancing test: Data subject's interests, rights, and freedoms override the controller's legitimate interest."
        )

    if issues:
        result["issues"] = issues
        return result

    interest = purpose_test.get("interest_description", "the stated interest")
    result["basis"] = "6(1)(f)"
    result["rationale"] = (
        f"Processing is necessary for the legitimate interest of {interest}. "
        f"The three-part LIA confirms: (1) the interest is legitimate and clearly articulated, "
        f"(2) processing is necessary with no less intrusive alternative, "
        f"(3) the controller's interest is not overridden by the data subject's rights."
    )
    return result


def assess_consent_feasibility(activity: dict) -> dict:
    result = {"basis": None, "rationale": "", "issues": []}
    consent = activity.get("consent_assessment", {})

    issues = []

    if consent.get("power_imbalance"):
        issues.append(
            "Power imbalance exists (e.g., employer-employee). Consent may not be freely given."
        )

    if consent.get("conditional_on_service"):
        issues.append(
            "Service access is conditional on consent for non-essential processing (Art. 7(4) violation)."
        )

    if consent.get("cannot_withdraw_without_detriment"):
        issues.append(
            "Data subject cannot withdraw consent without detriment. Consent is not freely given."
        )

    if issues:
        result["issues"] = issues
        return result

    result["basis"] = "6(1)(a)"
    result["rationale"] = (
        "Consent is the appropriate lawful basis. No power imbalance exists, "
        "consent is not conditional on service provision, and withdrawal is possible without detriment."
    )
    return result


def run_assessment(activity: dict) -> dict:
    assessment = {
        "activity_name": activity.get("name", "Unnamed"),
        "ropa_reference": activity.get("ropa_reference", ""),
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "recommended_basis": None,
        "rationale": "",
        "issues": [],
        "available_rights": [],
        "special_category": None,
        "steps_evaluated": [],
    }

    is_public_authority = activity.get("public_task_details", {}).get(
        "controller_is_public_authority", False
    )

    # Step 1: Legal Obligation
    legal_result = assess_legal_obligation(activity)
    assessment["steps_evaluated"].append({"step": "Legal Obligation (Art. 6(1)(c))", **legal_result})
    if legal_result["basis"]:
        assessment["recommended_basis"] = legal_result["basis"]
        assessment["rationale"] = legal_result["rationale"]
        assessment["available_rights"] = LAWFUL_BASES["6(1)(c)"]["available_rights"]
        return finalize_assessment(assessment, activity)

    # Step 2: Contract Performance
    contract_result = assess_contract_performance(activity)
    assessment["steps_evaluated"].append({"step": "Contract Performance (Art. 6(1)(b))", **contract_result})
    if contract_result["basis"]:
        assessment["recommended_basis"] = contract_result["basis"]
        assessment["rationale"] = contract_result["rationale"]
        assessment["available_rights"] = LAWFUL_BASES["6(1)(b)"]["available_rights"]
        return finalize_assessment(assessment, activity)

    # Step 3: Vital Interests
    if assess_vital_interests(activity):
        assessment["steps_evaluated"].append({
            "step": "Vital Interests (Art. 6(1)(d))",
            "basis": "6(1)(d)",
            "rationale": "Life-threatening or medical emergency scenario identified.",
        })
        assessment["recommended_basis"] = "6(1)(d)"
        assessment["rationale"] = "Processing is necessary to protect the vital interests of the data subject or another person."
        assessment["available_rights"] = LAWFUL_BASES["6(1)(d)"]["available_rights"]
        return finalize_assessment(assessment, activity)

    # Step 4: Public Task
    public_result = assess_public_task(activity)
    assessment["steps_evaluated"].append({"step": "Public Task (Art. 6(1)(e))", **public_result})
    if public_result["basis"]:
        assessment["recommended_basis"] = public_result["basis"]
        assessment["rationale"] = public_result["rationale"]
        assessment["available_rights"] = LAWFUL_BASES["6(1)(e)"]["available_rights"]
        return finalize_assessment(assessment, activity)

    # Step 5: Legitimate Interests (not available to public authorities for their tasks)
    if not is_public_authority:
        li_result = assess_legitimate_interests(activity)
        assessment["steps_evaluated"].append({"step": "Legitimate Interests (Art. 6(1)(f))", **li_result})
        if li_result["basis"]:
            assessment["recommended_basis"] = li_result["basis"]
            assessment["rationale"] = li_result["rationale"]
            assessment["available_rights"] = LAWFUL_BASES["6(1)(f)"]["available_rights"]
            return finalize_assessment(assessment, activity)
        if li_result["issues"]:
            assessment["issues"].extend(li_result["issues"])

    # Step 6: Consent
    consent_result = assess_consent_feasibility(activity)
    assessment["steps_evaluated"].append({"step": "Consent (Art. 6(1)(a))", **consent_result})
    if consent_result["basis"]:
        assessment["recommended_basis"] = consent_result["basis"]
        assessment["rationale"] = consent_result["rationale"]
        assessment["available_rights"] = LAWFUL_BASES["6(1)(a)"]["available_rights"]
        return finalize_assessment(assessment, activity)
    if consent_result["issues"]:
        assessment["issues"].extend(consent_result["issues"])

    # No basis found
    assessment["rationale"] = (
        "No valid lawful basis could be identified for this processing activity. "
        "Processing should not proceed. Consult the DPO for further guidance."
    )
    return assessment


def finalize_assessment(assessment: dict, activity: dict) -> dict:
    special_cat = activity.get("special_category_data")
    if special_cat and special_cat.get("involved"):
        condition = special_cat.get("art9_condition")
        if condition and condition in SPECIAL_CATEGORY_CONDITIONS:
            assessment["special_category"] = {
                "condition": condition,
                "description": SPECIAL_CATEGORY_CONDITIONS[condition],
                "data_types": special_cat.get("data_types", []),
            }
        else:
            assessment["issues"].append(
                "Special category data is involved but no valid Art. 9(2) condition has been identified. "
                "An additional legal basis under Art. 9(2) is required."
            )
    return assessment


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <processing_activity.json>")
        print("\nExample input JSON:")
        example = {
            "name": "Employee payroll processing",
            "ropa_reference": "RPA-001",
            "legal_obligation_reference": {
                "law_name": "German Income Tax Act (EStG)",
                "provision": "Section 41 — Employer obligations for wage tax",
            },
            "contract_details": {
                "contract_reference": "Employment contract",
                "processing_objectively_necessary": True,
            },
            "consent_assessment": {
                "power_imbalance": True,
            },
            "special_category_data": {
                "involved": False,
            },
        }
        print(json.dumps(example, indent=2))
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        activity = json.load(f)

    result = run_assessment(activity)
    print(json.dumps(result, indent=2))

    if not result["recommended_basis"]:
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
