#!/usr/bin/env python3
"""
California Breach Notification Compliance Checker

Determines whether a breach triggers California notification obligations,
validates notification content against §1798.82 requirements, and generates
AG submission records.
"""

import json
from datetime import datetime, timezone
from typing import Optional


CA_COVERED_DATA_ELEMENTS = {
    "ssn": "Social Security number",
    "drivers_license": "Driver's license or CA identification card number",
    "financial_account": "Financial account/credit/debit card number with security code",
    "medical_info": "Medical information",
    "health_insurance": "Health insurance information",
    "biometric": "Unique biometric data (fingerprint, retina, iris)",
    "license_plate": "Automated license plate recognition data",
    "genetic": "Genetic data",
    "credentials": "Username/email with password or security Q&A",
    "tax_id": "Tax identification number",
}

NOTIFICATION_HEADINGS = [
    "What Happened",
    "What Information Was Involved",
    "What We Are Doing",
    "What You Can Do",
    "For More Information",
]


def assess_ca_notification_obligation(
    ca_residents_affected: int,
    data_elements_compromised: list,
    includes_first_last_name: bool,
    data_encrypted: bool,
    encryption_key_compromised: bool,
) -> dict:
    """
    Determine California breach notification obligations.

    Args:
        ca_residents_affected: Number of California residents affected.
        data_elements_compromised: List of data element keys from CA_COVERED_DATA_ELEMENTS.
        includes_first_last_name: Whether first name/initial + last name is included.
        data_encrypted: Whether the data was encrypted.
        encryption_key_compromised: Whether the encryption key was also compromised.

    Returns:
        Obligation assessment including AG notification requirement.
    """
    covered_elements = [
        elem for elem in data_elements_compromised
        if elem in CA_COVERED_DATA_ELEMENTS
    ]

    trigger = (
        includes_first_last_name
        and len(covered_elements) > 0
        and (not data_encrypted or encryption_key_compromised)
    )

    ag_required = ca_residents_affected >= 500 and trigger

    substitute_notice_eligible = ca_residents_affected >= 500000

    ssn_involved = "ssn" in covered_elements
    financial_involved = "financial_account" in covered_elements
    credential_involved = "credentials" in covered_elements

    content_requirements = [
        "Entity name and contact information",
        "Types of personal information involved",
        "Date of breach (if known) and date of notice",
        "General description of the breach incident",
    ]

    if ssn_involved or "drivers_license" in covered_elements:
        content_requirements.extend([
            "Credit reporting agency toll-free numbers and websites",
            "Security freeze information per Cal. Civ. Code §1785.11.2",
        ])

    if credential_involved:
        content_requirements.append("Instructions for password change and account security")

    return {
        "ca_residents_affected": ca_residents_affected,
        "notification_triggered": trigger,
        "covered_data_elements": {
            elem: CA_COVERED_DATA_ELEMENTS[elem] for elem in covered_elements
        },
        "encryption_safe_harbor": data_encrypted and not encryption_key_compromised,
        "ag_notification_required": ag_required,
        "ag_submission_portal": "oag.ca.gov/privacy/databreach/reporting",
        "substitute_notice_eligible": substitute_notice_eligible,
        "content_requirements": content_requirements,
        "format_requirements": {
            "title": "Notice of Data Breach (prominently displayed)",
            "headings": NOTIFICATION_HEADINGS,
            "minimum_font_size": "10-point type",
            "language": "Plain, easily understood",
        },
        "ccpa_private_right_of_action": {
            "applicable": not data_encrypted and trigger,
            "statutory_damages": "$100-$750 per consumer per incident",
            "cure_notice_required": True,
            "cure_period_days": 30,
        },
        "credit_monitoring_recommended": ssn_involved or financial_involved,
        "security_freeze_notice_required": ssn_involved or "drivers_license" in covered_elements,
    }


def validate_notification_letter(letter_text: str) -> dict:
    """Validate a California breach notification letter against §1798.82(d) requirements."""
    checks = {}
    letter_lower = letter_text.lower()

    for heading in NOTIFICATION_HEADINGS:
        checks[f"heading_{heading.lower().replace(' ', '_')}"] = {
            "required": True,
            "present": heading.lower() in letter_lower,
            "description": f"Required heading: '{heading}'",
        }

    checks["title_notice_of_data_breach"] = {
        "required": True,
        "present": "notice of data breach" in letter_lower,
        "description": "Title 'Notice of Data Breach' must be prominently displayed",
    }

    checks["entity_contact_info"] = {
        "required": True,
        "present": any(kw in letter_lower for kw in ["contact", "phone", "email", "call"]),
        "description": "Entity name and contact information",
    }

    checks["data_types_described"] = {
        "required": True,
        "present": any(kw in letter_lower for kw in ["information was involved", "types of", "data elements"]),
        "description": "Types of personal information involved",
    }

    all_required_passed = all(
        c["present"] for c in checks.values() if c["required"]
    )

    return {
        "compliant": all_required_passed,
        "checks": checks,
        "summary": "Letter meets §1798.82(d) requirements" if all_required_passed
        else "Letter is MISSING required elements",
    }


def main():
    print("=" * 70)
    print("CALIFORNIA BREACH NOTIFICATION OBLIGATION ASSESSMENT")
    print("=" * 70)

    assessment = assess_ca_notification_obligation(
        ca_residents_affected=2340,
        data_elements_compromised=["ssn", "financial_account", "medical_info", "credentials"],
        includes_first_last_name=True,
        data_encrypted=False,
        encryption_key_compromised=False,
    )
    print(json.dumps(assessment, indent=2))

    print("\n" + "=" * 70)
    print("ENCRYPTION SAFE HARBOR TEST")
    print("=" * 70)

    safe_harbor = assess_ca_notification_obligation(
        ca_residents_affected=5000,
        data_elements_compromised=["ssn", "financial_account"],
        includes_first_last_name=True,
        data_encrypted=True,
        encryption_key_compromised=False,
    )
    print(f"Encryption safe harbor applies: {safe_harbor['encryption_safe_harbor']}")
    print(f"Notification triggered: {safe_harbor['notification_triggered']}")


if __name__ == "__main__":
    main()
