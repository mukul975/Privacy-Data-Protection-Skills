#!/usr/bin/env python3
"""
PIPL Compliance Assessment and Cross-Border Transfer Management Tool

Assesses compliance with China's Personal Information Protection Law,
manages cross-border transfer mechanism selection, tracks PIPIA requirements,
and evaluates separate consent obligations.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


PIPL_LAWFUL_BASES = {
    "consent": {"article": "Art. 13(1)", "name": "Consent of the individual"},
    "contract_necessity": {"article": "Art. 13(2)", "name": "Contract performance or HR management"},
    "statutory_duty": {"article": "Art. 13(3)", "name": "Statutory duties or obligations"},
    "public_health": {"article": "Art. 13(4)", "name": "Public health emergency response"},
    "public_interest": {"article": "Art. 13(5)", "name": "Public interest activities"},
    "publicly_disclosed": {"article": "Art. 13(6)", "name": "Processing lawfully disclosed PI"},
    "other_statutory": {"article": "Art. 13(7)", "name": "Other circumstances in laws/regulations"},
}

SEPARATE_CONSENT_TRIGGERS = {
    "sharing_with_processor": {
        "article": "Art. 23",
        "description": "Providing personal information to another processor",
        "required_disclosures": [
            "Recipient's name and contact information",
            "Processing purpose",
            "Processing method",
            "Categories of personal information",
            "Method and procedure for exercising rights with the recipient",
        ],
    },
    "public_disclosure": {
        "article": "Art. 25",
        "description": "Publicly disclosing personal information",
        "required_disclosures": [
            "Purpose of disclosure",
            "Categories of information to be disclosed",
            "Impact on individual rights",
        ],
    },
    "public_surveillance": {
        "article": "Art. 26",
        "description": "Using public surveillance images for non-security purposes",
        "required_disclosures": [
            "Purpose of use beyond public safety",
            "Method of processing",
        ],
    },
    "sensitive_pi": {
        "article": "Art. 29",
        "description": "Processing sensitive personal information",
        "required_disclosures": [
            "Necessity of processing sensitive PI",
            "Impact on individual rights and interests",
            "Specific categories of sensitive PI processed",
        ],
    },
    "cross_border_transfer": {
        "article": "Art. 39",
        "description": "Cross-border transfer of personal information",
        "required_disclosures": [
            "Overseas recipient's name and contact information",
            "Processing purpose and processing method",
            "Categories of personal information transferred",
            "Method and procedure for exercising rights with overseas recipient",
        ],
    },
}

SENSITIVE_PI_CATEGORIES = [
    "biometric_information",
    "religious_beliefs",
    "specific_identity_information",
    "medical_health_information",
    "financial_account_information",
    "location_tracking_information",
    "minors_under_14",
]

CBT_THRESHOLDS = {
    "cac_security_assessment": {
        "is_ciio": True,
        "total_individuals_processed": 1_000_000,
        "cumulative_transfers": 100_000,
        "cumulative_sensitive_transfers": 10_000,
    },
    "standard_contract": {
        "max_individuals_processed": 999_999,
        "max_cumulative_transfers": 99_999,
        "max_cumulative_sensitive_transfers": 9_999,
    },
    "exemptions_2024": {
        "contract_hr_necessity": True,
        "small_volume_threshold": 100_000,
        "free_trade_zone": True,
    },
}


def determine_cbt_mechanism(
    is_ciio: bool,
    total_individuals_processed: int,
    cumulative_transfers_past_year: int,
    cumulative_sensitive_transfers_past_year: int,
    transfer_purpose: str,
    is_contract_necessity: bool = False,
    is_hr_management: bool = False,
    is_free_trade_zone: bool = False,
) -> dict:
    """Determine the required cross-border transfer mechanism under PIPL Art. 38."""

    if is_ciio:
        return {
            "mechanism": "CAC Security Assessment (mandatory for CIIO)",
            "article": "Art. 40",
            "reason": "Critical information infrastructure operator — no alternative mechanism permitted",
            "data_localisation_required": True,
            "assessment_validity_years": 2,
            "process_steps": [
                "Conduct self-assessment (PIPIA)",
                "Submit application to provincial CAC office",
                "CAC review within 45+15 working days",
                "Implement conditions from assessment result",
            ],
            "exemption_available": False,
        }

    requires_cac = False
    cac_reasons = []

    if total_individuals_processed >= 1_000_000:
        requires_cac = True
        cac_reasons.append(
            f"Processor handles PI of {total_individuals_processed:,} individuals "
            f"(threshold: 1,000,000)"
        )

    if cumulative_transfers_past_year >= 100_000:
        requires_cac = True
        cac_reasons.append(
            f"Cumulative transfers of {cumulative_transfers_past_year:,} individuals "
            f"(threshold: 100,000)"
        )

    if cumulative_sensitive_transfers_past_year >= 10_000:
        requires_cac = True
        cac_reasons.append(
            f"Cumulative sensitive PI transfers of {cumulative_sensitive_transfers_past_year:,} "
            f"individuals (threshold: 10,000)"
        )

    if requires_cac:
        return {
            "mechanism": "CAC Security Assessment (mandatory — thresholds exceeded)",
            "article": "Art. 38(1) / Art. 40",
            "reasons": cac_reasons,
            "data_localisation_required": False,
            "assessment_validity_years": 2,
            "process_steps": [
                "Conduct self-assessment (PIPIA)",
                "Submit application to provincial CAC office",
                "CAC review within 45+15 working days",
                "Implement conditions from assessment result",
            ],
            "exemption_available": False,
        }

    exemption_applicable = False
    exemption_reason = None

    if is_contract_necessity:
        exemption_applicable = True
        exemption_reason = "Contract/HR necessity exemption (March 2024 Provisions, Art. 3)"
    elif is_hr_management:
        exemption_applicable = True
        exemption_reason = "HR management exemption (March 2024 Provisions, Art. 3)"
    elif cumulative_transfers_past_year < 100_000 and cumulative_sensitive_transfers_past_year == 0:
        exemption_applicable = True
        exemption_reason = (
            f"Small volume exemption: {cumulative_transfers_past_year:,} non-sensitive transfers "
            f"< 100,000 threshold (March 2024 Provisions, Art. 4)"
        )
    elif is_free_trade_zone:
        exemption_applicable = True
        exemption_reason = "Free trade zone negative list exemption (March 2024 Provisions, Art. 5)"

    if exemption_applicable:
        return {
            "mechanism": "Exempt from CAC assessment / standard contract / certification",
            "article": "March 2024 Provisions",
            "reason": exemption_reason,
            "requirements": [
                "Document the exemption basis",
                "Maintain record of transfer details",
                "Obtain separate consent if applicable (Art. 39)",
                "Conduct PIPIA if processing involves sensitive PI or automated decisions",
            ],
            "exemption_available": True,
        }

    return {
        "mechanism": "Standard Contract or Certification",
        "article": "Art. 38(2) or Art. 38(3)",
        "options": [
            {
                "name": "Standard Contract",
                "article": "Art. 38(2)",
                "process": [
                    "Conduct PIPIA per Art. 55-56",
                    "Execute CAC-published standard contract (no modifications to standard terms)",
                    "Complete transfer-specific annexes",
                    "File with provincial CAC within 10 working days",
                ],
                "filing_deadline_days": 10,
            },
            {
                "name": "Certification",
                "article": "Art. 38(3)",
                "process": [
                    "Both parties jointly engage accredited certification body",
                    "Submit PI protection documentation",
                    "Certification review (3-6 months typical)",
                    "Accept ongoing supervision and annual audits",
                ],
                "certification_validity_years": 3,
            },
        ],
        "separate_consent_required": True,
        "pipia_required": True,
    }


def assess_separate_consent(processing_activities: list) -> dict:
    """Assess which processing activities require separate consent under PIPL."""
    results = []

    for activity in processing_activities:
        triggers_found = []
        activity_name = activity.get("name", "Unknown activity")

        if activity.get("shares_with_third_party"):
            triggers_found.append(SEPARATE_CONSENT_TRIGGERS["sharing_with_processor"])

        if activity.get("publicly_discloses"):
            triggers_found.append(SEPARATE_CONSENT_TRIGGERS["public_disclosure"])

        if activity.get("uses_surveillance_images"):
            triggers_found.append(SEPARATE_CONSENT_TRIGGERS["public_surveillance"])

        if activity.get("involves_sensitive_pi"):
            triggers_found.append(SEPARATE_CONSENT_TRIGGERS["sensitive_pi"])

        if activity.get("cross_border_transfer"):
            triggers_found.append(SEPARATE_CONSENT_TRIGGERS["cross_border_transfer"])

        results.append({
            "activity": activity_name,
            "separate_consent_required": len(triggers_found) > 0,
            "trigger_count": len(triggers_found),
            "triggers": [
                {
                    "article": t["article"],
                    "description": t["description"],
                    "required_disclosures": t["required_disclosures"],
                }
                for t in triggers_found
            ],
        })

    total_requiring_consent = sum(1 for r in results if r["separate_consent_required"])
    return {
        "assessment_date": datetime.utcnow().isoformat(),
        "total_activities_assessed": len(results),
        "requiring_separate_consent": total_requiring_consent,
        "activities": results,
    }


def assess_pipia_requirement(processing_activities: list) -> dict:
    """Assess which processing activities require a PIPIA under Art. 55."""
    results = []

    for activity in processing_activities:
        triggers = []
        activity_name = activity.get("name", "Unknown")

        if activity.get("involves_sensitive_pi"):
            triggers.append("Processing sensitive personal information (Art. 55(1))")
        if activity.get("automated_decision_making"):
            triggers.append("Automated decision-making using PI (Art. 55(2))")
        if activity.get("entrusted_processing"):
            triggers.append("Entrusting processing to a third party (Art. 55(3))")
        if activity.get("shares_with_third_party"):
            triggers.append("Providing PI to another processor (Art. 55(4))")
        if activity.get("cross_border_transfer"):
            triggers.append("Cross-border transfer of PI (Art. 55(5))")
        if activity.get("significant_impact"):
            triggers.append("Other processing significantly impacting rights (Art. 55(6))")

        results.append({
            "activity": activity_name,
            "pipia_required": len(triggers) > 0,
            "triggers": triggers,
            "retention_period_years": 3,
        })

    return {
        "assessment_date": datetime.utcnow().isoformat(),
        "total_assessed": len(results),
        "requiring_pipia": sum(1 for r in results if r["pipia_required"]),
        "activities": results,
    }


def calculate_fine_exposure(
    previous_year_revenue_rmb: float,
    violation_type: str = "general",
    violation_count: int = 1,
) -> dict:
    """Calculate potential PIPL fine exposure under Arts. 66-69."""
    if violation_type == "serious":
        max_fine_rmb = min(previous_year_revenue_rmb * 0.05, 50_000_000)
        individual_fine_range = {"min": 100_000, "max": 1_000_000}
        additional_penalties = [
            "Suspension of relevant business",
            "Revocation of business licence",
            "Prohibition from serving as director/supervisor/senior manager/DPO",
        ]
    else:
        max_fine_rmb = min(1_000_000, previous_year_revenue_rmb * 0.05)
        individual_fine_range = {"min": 10_000, "max": 100_000}
        additional_penalties = [
            "Order to rectify",
            "Warning",
            "Confiscation of unlawful income",
            "Suspension or termination of related application",
        ]

    return {
        "violation_type": violation_type,
        "violation_count": violation_count,
        "previous_year_revenue_rmb": previous_year_revenue_rmb,
        "organisation_fine": {
            "max_per_violation_rmb": round(max_fine_rmb, 2),
            "total_exposure_rmb": round(max_fine_rmb * violation_count, 2),
            "percentage_of_revenue": round(
                (max_fine_rmb / previous_year_revenue_rmb) * 100, 4
            ) if previous_year_revenue_rmb > 0 else 0,
        },
        "individual_fine": individual_fine_range,
        "additional_penalties": additional_penalties,
        "assessment_date": datetime.utcnow().isoformat(),
    }


def generate_compliance_report(
    entity_name: str,
    is_ciio: bool,
    total_individuals: int,
    processing_activities: list,
    cbt_records: list,
    pipia_records: list,
) -> dict:
    """Generate a PIPL compliance summary report."""
    consent_assessment = assess_separate_consent(processing_activities)
    pipia_assessment = assess_pipia_requirement(processing_activities)

    cbt_by_mechanism = {}
    for record in cbt_records:
        mechanism = record.get("mechanism", "unknown")
        cbt_by_mechanism[mechanism] = cbt_by_mechanism.get(mechanism, 0) + 1

    pipia_status = {"current": 0, "overdue": 0, "missing": 0}
    required_count = pipia_assessment["requiring_pipia"]
    completed_count = len(pipia_records)
    pipia_status["current"] = min(completed_count, required_count)
    pipia_status["missing"] = max(0, required_count - completed_count)

    for record in pipia_records:
        review_date_str = record.get("next_review", "2099-01-01")
        review_date = datetime.strptime(review_date_str, "%Y-%m-%d")
        if review_date < datetime.utcnow():
            pipia_status["overdue"] += 1
            pipia_status["current"] -= 1

    return {
        "report_date": datetime.utcnow().isoformat(),
        "entity": entity_name,
        "is_ciio": is_ciio,
        "total_individuals_processed": total_individuals,
        "processing_activities": {
            "total": len(processing_activities),
            "requiring_separate_consent": consent_assessment["requiring_separate_consent"],
            "requiring_pipia": pipia_assessment["requiring_pipia"],
        },
        "cross_border_transfers": {
            "total": len(cbt_records),
            "by_mechanism": cbt_by_mechanism,
        },
        "pipia_status": pipia_status,
        "compliance_health": _assess_health(pipia_status, consent_assessment),
    }


def _assess_health(pipia_status: dict, consent_assessment: dict) -> str:
    """Assess overall compliance health."""
    issues = 0
    if pipia_status.get("missing", 0) > 0:
        issues += 2
    if pipia_status.get("overdue", 0) > 0:
        issues += 1

    if issues == 0:
        return "GREEN — PIPL compliance indicators within acceptable parameters"
    elif issues <= 1:
        return "AMBER — Minor gaps identified; remediation recommended within 30 days"
    else:
        return "RED — Significant compliance gaps requiring immediate remediation"


if __name__ == "__main__":
    print("=== Cross-Border Transfer Mechanism Determination ===")
    result = determine_cbt_mechanism(
        is_ciio=False,
        total_individuals_processed=1_500_000,
        cumulative_transfers_past_year=150_000,
        cumulative_sensitive_transfers_past_year=5_000,
        transfer_purpose="Transfer customer logistics data to EU headquarters",
    )
    print(json.dumps(result, indent=2))

    print("\n=== Separate Consent Assessment ===")
    activities = [
        {
            "name": "Customer data sharing with logistics partners",
            "shares_with_third_party": True,
            "cross_border_transfer": True,
            "involves_sensitive_pi": False,
        },
        {
            "name": "Employee background checks",
            "shares_with_third_party": True,
            "involves_sensitive_pi": True,
            "cross_border_transfer": False,
        },
    ]
    consent_result = assess_separate_consent(activities)
    print(json.dumps(consent_result, indent=2))

    print("\n=== Fine Exposure (Serious Violation) ===")
    fine = calculate_fine_exposure(
        previous_year_revenue_rmb=2_000_000_000,
        violation_type="serious",
        violation_count=1,
    )
    print(json.dumps(fine, indent=2))
