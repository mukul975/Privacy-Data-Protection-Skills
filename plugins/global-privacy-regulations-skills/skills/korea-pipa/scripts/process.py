#!/usr/bin/env python3
"""
PIPA Compliance Assessment and Management Tool

Assesses compliance with South Korea's Personal Information Protection Act,
manages consent requirements, cross-border transfers, pseudonymisation,
and data subject rights under PIPA and the 2023 amendments.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


PIPA_LAWFUL_BASES = {
    "consent": {"article": "Art. 15(1)(1)", "name": "Data subject's consent"},
    "legal_obligation": {"article": "Art. 15(1)(2)", "name": "Special provisions in laws or legal obligations"},
    "public_institution_duty": {"article": "Art. 15(1)(3)", "name": "Public institution statutory duty"},
    "contract_performance": {"article": "Art. 15(1)(4)", "name": "Contract with the data subject"},
    "urgent_necessity": {"article": "Art. 15(1)(5)", "name": "Urgent necessity for life, body, or property"},
    "legitimate_interest": {"article": "Art. 15(1)(6)", "name": "Legitimate interest of data handler (2023 amendment)"},
}

SENSITIVE_CATEGORIES = [
    "ideology", "beliefs", "trade_union_membership", "political_party_membership",
    "political_opinions", "health_information", "sex_life", "genetic_information",
    "criminal_record", "biometric_data", "race_ethnic_origin",
]

PSEUDONYMISATION_TECHNIQUES = {
    "generalisation": "Reducing the precision of data values (e.g., exact age to age range)",
    "suppression": "Removing identifying data elements entirely",
    "noise_addition": "Adding random values to numerical data while preserving statistical properties",
    "tokenisation": "Replacing identifiers with random tokens with a separate mapping table",
    "permutation": "Shuffling data values among records to break linkage",
    "k_anonymity": "Ensuring each record is indistinguishable from at least k-1 other records",
}

CBT_MECHANISMS = {
    "adequacy": {"article": "Art. 28-8(1)(3)", "name": "PIPC adequacy recognition"},
    "consent": {"article": "Art. 28-8(1)(1)", "name": "Data subject consent with notification"},
    "contract_necessity": {"article": "Art. 28-8(1)(2)", "name": "Contract necessity"},
    "sccs": {"article": "Art. 28-8(1)(4)", "name": "PIPC standard contractual clauses"},
    "bcr": {"article": "Art. 28-8(1)(4)", "name": "PIPC-approved corporate data protection rules"},
    "certification": {"article": "Art. 28-8(1)(5)", "name": "PIPC certification"},
}

ADEQUACY_COUNTRIES = ["EU/EEA", "United Kingdom"]


def assess_consent_requirements(
    processing_purposes: list,
    data_items: list,
    includes_sensitive: bool,
    includes_marketing: bool,
    includes_third_party_provision: bool,
    includes_cross_border: bool,
) -> dict:
    """Assess consent requirements under PIPA for a processing activity."""
    consent_elements = []

    consent_elements.append({
        "element": "Essential processing consent",
        "article": "Art. 15(2)",
        "required_disclosures": [
            "Purpose of collection and use",
            "Items of personal information collected",
            "Retention and use period",
            "Right to refuse and consequences",
        ],
        "separate_box": True,
    })

    if includes_sensitive:
        consent_elements.append({
            "element": "Sensitive information consent",
            "article": "Art. 23",
            "required_disclosures": [
                "Categories of sensitive information processed",
                "Purpose of sensitive information processing",
                "Explicit separate consent required",
            ],
            "separate_box": True,
        })

    if includes_marketing:
        consent_elements.append({
            "element": "Marketing consent",
            "article": "Art. 22(2)",
            "required_disclosures": [
                "Marketing purpose clearly stated",
                "Separate opt-in required",
                "Service must not be refused for declining marketing consent",
            ],
            "separate_box": True,
        })

    if includes_third_party_provision:
        consent_elements.append({
            "element": "Third-party provision consent",
            "article": "Art. 17",
            "required_disclosures": [
                "Identity of the recipient",
                "Purpose of recipient's use",
                "Items of PI provided",
                "Recipient's retention period",
                "Right to refuse and consequences",
            ],
            "separate_box": True,
        })

    if includes_cross_border:
        consent_elements.append({
            "element": "Cross-border transfer consent/notification",
            "article": "Art. 28-8",
            "required_disclosures": [
                "Recipient's identity",
                "Destination country",
                "Items transferred",
                "Purpose of transfer",
                "Retention period",
                "Right to refuse and consequences",
            ],
            "separate_box": True,
        })

    return {
        "assessment_date": datetime.utcnow().isoformat(),
        "processing_purposes": processing_purposes,
        "total_consent_elements": len(consent_elements),
        "consent_elements": consent_elements,
        "display_requirements": {
            "important_content_highlighting": "Larger font, contrasting colour, or bold per Art. 22(1)",
            "no_pre_ticked_boxes": True,
            "language": "Korean (한국어)",
        },
    }


def determine_cbt_mechanism(
    destination_country: str,
    transfer_purpose: str,
    is_contract_necessity: bool = False,
) -> dict:
    """Determine appropriate cross-border transfer mechanism under 2023 PIPA amendments."""
    is_adequate = destination_country in ADEQUACY_COUNTRIES

    if is_adequate:
        return {
            "destination": destination_country,
            "mechanism": CBT_MECHANISMS["adequacy"],
            "adequacy_status": "Recognised by PIPC",
            "notification_required": True,
            "notification_content": [
                "Recipient identity", "Destination country", "PI items",
                "Purpose", "Retention period", "Right to refuse",
            ],
            "additional_requirements": [],
        }

    if is_contract_necessity:
        return {
            "destination": destination_country,
            "mechanism": CBT_MECHANISMS["contract_necessity"],
            "notification_required": True,
            "additional_requirements": [
                "Transfer must be directly necessary for contract performance with the data subject",
            ],
        }

    return {
        "destination": destination_country,
        "mechanism_options": [
            {
                **CBT_MECHANISMS["consent"],
                "process": "Obtain consent with full disclosure per Art. 28-8(3)",
            },
            {
                **CBT_MECHANISMS["sccs"],
                "process": "Execute PIPC-approved SCCs; file within 30 days",
            },
            {
                **CBT_MECHANISMS["certification"],
                "process": "Recipient obtains PIPC-designated certification",
            },
        ],
        "recommended": "PIPC standard contractual clauses" if not is_contract_necessity else "Contract necessity",
        "notification_required": True,
    }


def assess_pseudonymisation(
    data_set_name: str,
    processing_purpose: str,
    technique: str,
    has_separated_additional_info: bool,
    has_encryption: bool,
    has_access_restrictions: bool,
    has_re_identification_prohibition: bool,
) -> dict:
    """Assess pseudonymisation compliance under Arts. 28-2 to 28-7."""
    valid_purposes = ["statistics", "scientific_research", "public_interest_records"]
    purpose_valid = processing_purpose in valid_purposes

    safeguard_checks = {
        "separated_additional_information": has_separated_additional_info,
        "encryption_of_additional_information": has_encryption,
        "access_restrictions": has_access_restrictions,
        "re_identification_prohibition": has_re_identification_prohibition,
    }

    technique_description = PSEUDONYMISATION_TECHNIQUES.get(technique, "Unknown technique")
    all_safeguards_met = all(safeguard_checks.values())

    issues = []
    if not purpose_valid:
        issues.append(f"Purpose '{processing_purpose}' is not within Art. 28-2 permitted uses")
    for safeguard, met in safeguard_checks.items():
        if not met:
            issues.append(f"Safety measure not met: {safeguard} (Art. 28-4)")

    return {
        "data_set": data_set_name,
        "purpose": processing_purpose,
        "purpose_valid": purpose_valid,
        "technique": technique,
        "technique_description": technique_description,
        "safeguard_compliance": safeguard_checks,
        "all_safeguards_met": all_safeguards_met,
        "compliant": purpose_valid and all_safeguards_met,
        "issues": issues,
        "assessment_date": datetime.utcnow().isoformat(),
    }


def calculate_penalty_exposure(
    related_revenue_krw: float,
    violation_type: str = "administrative",
    violation_count: int = 1,
) -> dict:
    """Calculate potential PIPC penalty exposure."""
    if violation_type == "criminal":
        return {
            "violation_type": "criminal",
            "max_imprisonment": "5 years",
            "max_fine_krw": 50_000_000,
            "note": "Criminal penalties under Arts. 71-73 for serious violations",
        }

    if violation_type == "penalty_surcharge":
        max_surcharge = related_revenue_krw * 0.03
        return {
            "violation_type": "penalty_surcharge",
            "related_revenue_krw": related_revenue_krw,
            "max_surcharge_per_violation_krw": round(max_surcharge, 2),
            "total_exposure_krw": round(max_surcharge * violation_count, 2),
            "percentage_of_revenue": 3.0,
            "article": "Art. 64-2",
        }

    return {
        "violation_type": "administrative_fine",
        "max_fine_per_violation_krw": 50_000_000,
        "total_exposure_krw": 50_000_000 * violation_count,
        "article": "Art. 75",
        "additional_sanctions": ["Corrective orders (Art. 64)", "Public naming (Art. 64(4))"],
    }


def create_dsr_request(
    request_type: str,
    data_subject_name: str,
    request_date: Optional[str] = None,
) -> dict:
    """Create a data subject rights request under PIPA."""
    dsr_types = {
        "access": {"article": "Art. 35", "deadline_days": 10},
        "correction": {"article": "Art. 36", "deadline_days": 10},
        "deletion": {"article": "Art. 36", "deadline_days": 10},
        "suspension": {"article": "Art. 37", "deadline_days": 10},
        "portability": {"article": "Art. 35-2", "deadline_days": 10},
        "automated_decision": {"article": "Art. 37-2", "deadline_days": 10},
    }

    dsr_info = dsr_types.get(request_type)
    if not dsr_info:
        return {"error": f"Unknown DSR type: {request_type}", "valid_types": list(dsr_types.keys())}

    req_date = datetime.strptime(request_date, "%Y-%m-%d") if request_date else datetime.utcnow()
    deadline = req_date + timedelta(days=dsr_info["deadline_days"])

    return {
        "request_id": f"DSR-KR-{req_date.strftime('%Y')}-{abs(hash(data_subject_name + str(req_date))) % 10000:04d}",
        "request_type": request_type,
        "article": dsr_info["article"],
        "data_subject": data_subject_name,
        "request_date": req_date.strftime("%Y-%m-%d"),
        "response_deadline": deadline.strftime("%Y-%m-%d"),
        "status": "received",
    }


if __name__ == "__main__":
    print("=== PIPA Consent Requirements Assessment ===")
    result = assess_consent_requirements(
        processing_purposes=["freight contract fulfilment", "marketing communications"],
        data_items=["name", "email", "phone", "shipping_address"],
        includes_sensitive=False,
        includes_marketing=True,
        includes_third_party_provision=True,
        includes_cross_border=True,
    )
    print(json.dumps(result, indent=2))

    print("\n=== Cross-Border Transfer Mechanism ===")
    cbt = determine_cbt_mechanism(
        destination_country="Singapore",
        transfer_purpose="Transfer employee HR data to regional hub",
    )
    print(json.dumps(cbt, indent=2))

    print("\n=== Pseudonymisation Assessment ===")
    pseudo = assess_pseudonymisation(
        data_set_name="Customer shipping patterns",
        processing_purpose="statistics",
        technique="k_anonymity",
        has_separated_additional_info=True,
        has_encryption=True,
        has_access_restrictions=True,
        has_re_identification_prohibition=True,
    )
    print(json.dumps(pseudo, indent=2))
