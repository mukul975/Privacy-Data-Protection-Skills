#!/usr/bin/env python3
"""Marketing Analytics Privacy Assessment Engine.

Implements DPIA methodology for marketing profiling, behavioural targeting,
cross-device tracking, and advertising analytics processing.
"""

import json
from datetime import datetime, timedelta
from typing import Any

MARKETING_PROCESSING_TYPES = {
    "customer_profiling": {
        "name": "Customer Profiling and Segmentation",
        "wp248_criteria": ["C1", "C6"],
        "consent_required": False,
        "lia_possible": True,
        "risk_level": "Medium",
    },
    "behavioural_targeting": {
        "name": "Behavioural Advertising Targeting",
        "wp248_criteria": ["C1", "C3", "C6", "C8"],
        "consent_required": True,
        "lia_possible": False,
        "risk_level": "High",
    },
    "cross_device_tracking": {
        "name": "Cross-Device Tracking and Profile Linking",
        "wp248_criteria": ["C1", "C3", "C6", "C8"],
        "consent_required": True,
        "lia_possible": False,
        "risk_level": "High",
    },
    "conversion_attribution": {
        "name": "Conversion Attribution and Marketing Measurement",
        "wp248_criteria": ["C3", "C6"],
        "consent_required": True,
        "lia_possible": True,
        "risk_level": "Medium",
    },
    "email_marketing": {
        "name": "Email Marketing (Direct Marketing)",
        "wp248_criteria": ["C1"],
        "consent_required": True,
        "lia_possible": True,
        "risk_level": "Low",
    },
    "social_media_advertising": {
        "name": "Social Media Custom Audience Targeting",
        "wp248_criteria": ["C1", "C6"],
        "consent_required": True,
        "lia_possible": False,
        "risk_level": "High",
    },
}


def assess_marketing_processing(
    processing_type: str,
    lawful_basis: str,
    consent_obtained: bool,
    lia_documented: bool,
    data_subjects_count: int,
    third_party_recipients: list[str],
    cross_border_transfer: bool,
    children_possible: bool,
) -> dict[str, Any]:
    """Assess a marketing processing activity for DPIA compliance."""
    proc = MARKETING_PROCESSING_TYPES.get(processing_type)
    if not proc:
        return {"error": f"Unknown processing type: {processing_type}"}

    issues = []

    if proc["consent_required"] and not consent_obtained:
        issues.append("Consent is required for this processing type but has not been obtained.")

    if lawful_basis == "legitimate_interest" and not proc["lia_possible"]:
        issues.append(
            "Legitimate interest is not an appropriate lawful basis for this "
            "processing type. Consent is required."
        )

    if lawful_basis == "legitimate_interest" and not lia_documented:
        issues.append("Legitimate interest claimed but LIA not documented.")

    if len(third_party_recipients) > 5:
        issues.append(
            f"{len(third_party_recipients)} third-party recipients identified. "
            "Complex adtech supply chains increase data leakage risk."
        )

    if children_possible:
        issues.append(
            "Children may be affected. Age verification and parental consent "
            "mechanisms required under Art. 8."
        )

    compliant = len(issues) == 0

    return {
        "processing_type": proc["name"],
        "wp248_criteria": proc["wp248_criteria"],
        "dpia_required": len(proc["wp248_criteria"]) >= 2,
        "risk_level": proc["risk_level"],
        "lawful_basis": lawful_basis,
        "consent_obtained": consent_obtained,
        "issues": issues,
        "compliant": compliant,
        "data_subjects_count": data_subjects_count,
        "third_party_recipients": third_party_recipients,
        "cross_border_transfer": cross_border_transfer,
    }


def run_example_assessment() -> dict[str, Any]:
    """Run example marketing analytics DPIA for QuantumLeap Health Technologies."""
    assessments = [
        assess_marketing_processing(
            processing_type="email_marketing",
            lawful_basis="legitimate_interest",
            consent_obtained=False,
            lia_documented=True,
            data_subjects_count=4200,
            third_party_recipients=["Mailchimp (processor)"],
            cross_border_transfer=False,
            children_possible=False,
        ),
        assess_marketing_processing(
            processing_type="customer_profiling",
            lawful_basis="legitimate_interest",
            consent_obtained=False,
            lia_documented=True,
            data_subjects_count=4200,
            third_party_recipients=["HubSpot (processor)"],
            cross_border_transfer=False,
            children_possible=False,
        ),
    ]

    return {
        "reference": "DPIA-QLH-2026-0011",
        "organisation": "QuantumLeap Health Technologies",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "assessments": assessments,
        "overall_compliant": all(a["compliant"] for a in assessments),
    }


if __name__ == "__main__":
    result = run_example_assessment()
    print(json.dumps(result, indent=2, default=str))
