#!/usr/bin/env python3
"""
APPI Compliance Assessment Tool

Assesses compliance with Japan's Act on the Protection of Personal Information,
manages cross-border transfer pre-transfer information, individual rights,
and pseudonymously processed information under the 2022 amendments.
"""

import json
from datetime import datetime, timedelta
from typing import Optional

PPC_ADEQUATE_COUNTRIES = ["EU/EEA", "United Kingdom"]

SPECIAL_CARE_CATEGORIES = [
    "race", "creed", "social_status", "medical_history",
    "criminal_record", "crime_victimisation", "disability",
    "physical_examination_results", "medical_guidance",
    "diagnosis_treatment", "genetic_testing",
]

CESSATION_TRIGGERS_2022 = [
    "purpose_achieved",
    "data_no_longer_needed",
    "security_incident_occurred",
    "rights_likely_harmed",
]


def assess_cbt_mechanism(
    destination_country: str,
    has_equivalent_measures: bool = False,
    equivalent_basis: Optional[str] = None,
) -> dict:
    """Determine cross-border transfer mechanism under APPI Art. 28."""
    is_adequate = destination_country in PPC_ADEQUATE_COUNTRIES

    if is_adequate:
        return {
            "destination": destination_country,
            "mechanism": "PPC-recognised adequate country (Art. 28 exception)",
            "pre_transfer_information_required": False,
            "consent_required": False,
            "supplementary_rules_apply": destination_country == "EU/EEA",
        }

    if has_equivalent_measures:
        return {
            "destination": destination_country,
            "mechanism": f"Recipient with equivalent measures ({equivalent_basis})",
            "pre_transfer_information_required": False,
            "consent_required": False,
            "periodic_verification_required": True,
            "verification_frequency": "At least annually",
        }

    return {
        "destination": destination_country,
        "mechanism": "Consent with pre-transfer information (Art. 28(1))",
        "pre_transfer_information_required": True,
        "required_information": [
            "Name of destination country",
            "Personal information protection system of destination country",
            "Whether comprehensive PI protection law exists",
            "Whether independent enforcement authority exists",
            "Individual rights available in destination",
            "Specific measures taken by the recipient",
        ],
        "consent_required": True,
    }


def assess_pseudonymisation(
    data_set: str,
    deleted_direct_identifiers: bool,
    deleted_my_number: bool,
    deleted_id_codes: bool,
    deleted_financial_info: bool,
    separated_additional_info: bool,
    internal_use_only: bool,
    purpose_announced: bool,
) -> dict:
    """Assess pseudonymously processed information compliance under Art. 41."""
    checks = {
        "direct_identifiers_deleted": deleted_direct_identifiers,
        "my_number_deleted": deleted_my_number,
        "identification_codes_deleted": deleted_id_codes,
        "financial_damage_info_deleted": deleted_financial_info,
        "additional_info_separated": separated_additional_info,
        "internal_use_only": internal_use_only,
        "purpose_publicly_announced": purpose_announced,
    }

    issues = [k.replace("_", " ").capitalize() for k, v in checks.items() if not v]

    return {
        "data_set": data_set,
        "checks": checks,
        "compliant": len(issues) == 0,
        "issues": issues,
        "benefits_if_compliant": [
            "May use for purposes beyond original collection",
            "No individual rights requests applicable",
            "No accuracy obligation",
        ],
        "restrictions": [
            "Internal use only — no third-party provision",
            "Must not attempt re-identification",
            "Must publicly announce purpose of use",
        ],
    }


def calculate_penalty_exposure(violation_type: str = "order_violation") -> dict:
    """Calculate potential PPC enforcement exposure."""
    penalties = {
        "order_violation": {
            "individual": "Imprisonment up to 1 year or fine up to JPY 1,000,000",
            "corporate": "Fine up to JPY 100,000,000",
        },
        "wrongful_provision": {
            "individual": "Imprisonment up to 1 year or fine up to JPY 500,000",
            "corporate": "Fine up to JPY 100,000,000",
        },
        "false_reporting": {
            "individual": "Fine up to JPY 500,000",
            "corporate": "Fine up to JPY 500,000",
        },
    }

    penalty = penalties.get(violation_type, penalties["order_violation"])
    return {
        "violation_type": violation_type,
        "penalties": penalty,
        "enforcement_path": "PPC guidance → recommendation → order → criminal prosecution",
        "note": "APPI does not have administrative fines; enforcement is through orders backed by criminal penalties",
    }


if __name__ == "__main__":
    print("=== Cross-Border Transfer Assessment ===")
    result = assess_cbt_mechanism("Singapore")
    print(json.dumps(result, indent=2))

    print("\n=== Pseudonymisation Assessment ===")
    pseudo = assess_pseudonymisation(
        "Customer shipping analytics", True, True, True, True, True, True, True
    )
    print(json.dumps(pseudo, indent=2))
