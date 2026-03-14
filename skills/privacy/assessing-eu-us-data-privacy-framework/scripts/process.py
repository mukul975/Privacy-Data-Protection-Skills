#!/usr/bin/env python3
"""
EU-US Data Privacy Framework Certification Tracker and Compliance Checker

Tracks DPF certification status, conducts principle compliance assessments,
and manages the verification workflow for EU data exporters.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


DPF_PRINCIPLES = {
    "notice": {
        "name": "Notice",
        "requirements": [
            "Types of personal data collected are disclosed",
            "Purposes of processing are specified",
            "Right to access and correct data is communicated",
            "Third parties to whom data may be disclosed are identified",
            "Choices for limiting use and disclosure are explained",
            "Independent recourse mechanism is identified",
            "Organisation liability in onward transfer cases is stated",
        ],
    },
    "choice": {
        "name": "Choice",
        "requirements": [
            "Opt-out mechanism for disclosure to third-party controllers",
            "Opt-out mechanism for materially different purpose use",
            "Opt-in (affirmative consent) for sensitive data disclosure",
            "Opt-in (affirmative consent) for sensitive data new purpose use",
            "Choice mechanism is clear, conspicuous, and readily available",
        ],
    },
    "accountability_onward_transfer": {
        "name": "Accountability for Onward Transfer",
        "requirements": [
            "Contracts with third-party controllers require same level of protection",
            "Third-party controllers must notify if they cannot meet protection obligations",
            "Contracts with agents restrict processing to specified purposes",
            "Agents must provide same level of protection as DPF Principles",
            "Agents must notify and take remedial steps for unauthorised processing",
            "Due diligence on third-party and agent data protection capabilities",
        ],
    },
    "security": {
        "name": "Security",
        "requirements": [
            "Reasonable measures against loss of personal data",
            "Reasonable measures against misuse of personal data",
            "Reasonable measures against unauthorised access",
            "Reasonable measures against disclosure",
            "Reasonable measures against alteration and destruction",
            "Measures proportionate to risk and nature of data",
        ],
    },
    "data_integrity_purpose_limitation": {
        "name": "Data Integrity and Purpose Limitation",
        "requirements": [
            "Data relevant for the purposes of processing",
            "Data reliable for its intended use",
            "Data accurate and current",
            "Data complete for the processing purpose",
            "Processing not incompatible with collection purposes",
            "Retention limited to what is necessary for purpose",
        ],
    },
    "access": {
        "name": "Access",
        "requirements": [
            "Individuals can obtain confirmation of data processing",
            "Data communicated within a reasonable time",
            "Individuals can challenge data accuracy",
            "Data can be corrected, amended, or deleted",
            "Access restrictions documented and justified",
        ],
    },
    "recourse_enforcement_liability": {
        "name": "Recourse, Enforcement, and Liability",
        "requirements": [
            "Independent dispute resolution mechanism engaged",
            "Compliance verification procedures in place (self-assessment or outside review)",
            "Remediation procedures for non-compliance issues",
            "FTC/DoT enforcement jurisdiction confirmed",
            "Binding arbitration available as last resort",
            "Annual re-certification commitment documented",
        ],
    },
}

FEE_SCHEDULE = [
    {"min_revenue": 0, "max_revenue": 5_000_000, "fee": 0},
    {"min_revenue": 5_000_001, "max_revenue": 25_000_000, "fee": 575},
    {"min_revenue": 25_000_001, "max_revenue": 500_000_000, "fee": 1150},
    {"min_revenue": 500_000_001, "max_revenue": 5_000_000_000, "fee": 2300},
    {"min_revenue": 5_000_000_001, "max_revenue": float("inf"), "fee": 3450},
]


def verify_dpf_certification(
    org_name: str,
    certification_date: str,
    certification_expiry: str,
    status: str,
    covers_hr_data: bool,
    covers_non_hr_data: bool,
    irm_provider: str,
    jurisdiction: str,
    verification_date: Optional[str] = None,
) -> dict:
    """Verify DPF certification for a US data importer."""
    if verification_date:
        check_date = datetime.strptime(verification_date, "%Y-%m-%d")
    else:
        check_date = datetime.utcnow()

    expiry = datetime.strptime(certification_expiry, "%Y-%m-%d")
    days_until_expiry = (expiry - check_date).days

    issues = []
    if status.lower() != "active":
        issues.append(f"Certification status is '{status}', not 'Active'")
    if days_until_expiry < 0:
        issues.append(f"Certification expired {abs(days_until_expiry)} days ago")
    elif days_until_expiry < 30:
        issues.append(
            f"Certification expires in {days_until_expiry} days — re-certification needed"
        )
    if jurisdiction.upper() not in ("FTC", "DOT"):
        issues.append(f"Jurisdiction '{jurisdiction}' is not FTC or DoT — outside DPF scope")
    if not irm_provider:
        issues.append("No independent recourse mechanism identified")

    transfer_permitted = len(issues) == 0

    return {
        "organisation": org_name,
        "verification_date": check_date.strftime("%Y-%m-%d"),
        "certification_status": status,
        "certification_date": certification_date,
        "certification_expiry": certification_expiry,
        "days_until_expiry": days_until_expiry,
        "covers_hr_data": covers_hr_data,
        "covers_non_hr_data": covers_non_hr_data,
        "irm_provider": irm_provider,
        "regulatory_jurisdiction": jurisdiction,
        "issues": issues,
        "transfer_permitted": transfer_permitted,
        "recommendation": "Transfer may proceed under DPF adequacy decision"
        if transfer_permitted
        else "Transfer NOT permitted — resolve issues before transferring data",
    }


def assess_dpf_principle_compliance(compliance_data: dict) -> dict:
    """Assess an organisation's compliance with all seven DPF Principles."""
    results = {
        "assessment_date": datetime.utcnow().isoformat(),
        "principles": {},
        "total_requirements": 0,
        "met_requirements": 0,
        "overall_compliance_pct": 0.0,
        "gaps": [],
    }

    for principle_key, principle_info in DPF_PRINCIPLES.items():
        org_compliance = compliance_data.get(principle_key, {})
        requirements = principle_info["requirements"]
        met = 0
        principle_gaps = []

        for req in requirements:
            if org_compliance.get(req, False):
                met += 1
            else:
                principle_gaps.append(req)
                results["gaps"].append(
                    {
                        "principle": principle_info["name"],
                        "requirement": req,
                    }
                )

        results["total_requirements"] += len(requirements)
        results["met_requirements"] += met
        results["principles"][principle_key] = {
            "name": principle_info["name"],
            "total_requirements": len(requirements),
            "met": met,
            "gaps": principle_gaps,
            "compliance_pct": round(met / len(requirements) * 100, 1)
            if requirements
            else 100.0,
        }

    if results["total_requirements"] > 0:
        results["overall_compliance_pct"] = round(
            results["met_requirements"] / results["total_requirements"] * 100, 1
        )

    results["certification_ready"] = results["overall_compliance_pct"] == 100.0
    return results


def calculate_certification_fee(annual_revenue_usd: float) -> dict:
    """Calculate the DPF annual certification fee based on organisation revenue."""
    for bracket in FEE_SCHEDULE:
        if bracket["min_revenue"] <= annual_revenue_usd <= bracket["max_revenue"]:
            return {
                "annual_revenue_usd": annual_revenue_usd,
                "annual_fee_usd": bracket["fee"],
                "revenue_bracket": f"USD {bracket['min_revenue']:,.0f} - USD {bracket['max_revenue']:,.0f}"
                if bracket["max_revenue"] != float("inf")
                else f"Over USD {bracket['min_revenue']:,.0f}",
            }
    return {"error": "Revenue amount could not be matched to fee schedule"}


def generate_dpf_transfer_register_entry(
    exporter_name: str,
    importer_name: str,
    dpf_certification_date: str,
    dpf_expiry_date: str,
    data_categories: list,
    covers_hr: bool,
    covers_non_hr: bool,
    backup_mechanism: Optional[str] = None,
) -> dict:
    """Generate a transfer register entry for a DPF-based transfer."""
    return {
        "transfer_mechanism": "EU-US DPF Adequacy Decision (EU) 2023/1795",
        "exporter": exporter_name,
        "importer": importer_name,
        "importer_country": "United States",
        "dpf_certification_date": dpf_certification_date,
        "dpf_expiry_date": dpf_expiry_date,
        "data_categories": data_categories,
        "covers_hr_data": covers_hr,
        "covers_non_hr_data": covers_non_hr,
        "backup_mechanism": backup_mechanism or "SCCs Module 2 (executed, held in reserve)",
        "next_verification_date": (
            datetime.strptime(dpf_expiry_date, "%Y-%m-%d") - timedelta(days=30)
        ).strftime("%Y-%m-%d"),
        "register_entry_date": datetime.utcnow().strftime("%Y-%m-%d"),
    }


def contingency_assessment(
    dpf_transfers: list,
    backup_sccs_in_place: dict,
) -> dict:
    """Assess contingency readiness if the DPF adequacy decision is invalidated."""
    covered = []
    uncovered = []

    for transfer in dpf_transfers:
        importer = transfer["importer"]
        has_backup = backup_sccs_in_place.get(importer, False)
        entry = {
            "importer": importer,
            "data_categories": transfer.get("data_categories", []),
        }
        if has_backup:
            covered.append(entry)
        else:
            uncovered.append(entry)

    return {
        "assessment_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "total_dpf_transfers": len(dpf_transfers),
        "with_backup_sccs": len(covered),
        "without_backup_sccs": len(uncovered),
        "contingency_readiness_pct": round(
            len(covered) / len(dpf_transfers) * 100, 1
        )
        if dpf_transfers
        else 100.0,
        "uncovered_transfers": uncovered,
        "recommendation": "All DPF transfers have backup SCCs in place"
        if not uncovered
        else f"URGENT: {len(uncovered)} transfer(s) lack backup SCCs — execute SCCs immediately",
    }


if __name__ == "__main__":
    print("=== DPF Certification Verification ===")
    verification = verify_dpf_certification(
        org_name="Meridian Cloud Services Inc",
        certification_date="2024-09-15",
        certification_expiry="2025-09-15",
        status="Active",
        covers_hr_data=False,
        covers_non_hr_data=True,
        irm_provider="JAMS",
        jurisdiction="FTC",
        verification_date="2025-03-14",
    )
    print(json.dumps(verification, indent=2))

    print("\n=== Certification Fee Calculation ===")
    fee = calculate_certification_fee(150_000_000)
    print(json.dumps(fee, indent=2))

    print("\n=== Contingency Assessment ===")
    transfers = [
        {"importer": "Meridian Cloud Services Inc", "data_categories": ["customer data"]},
        {"importer": "Pacific Analytics Corp", "data_categories": ["employee data", "customer data"]},
    ]
    backups = {"Meridian Cloud Services Inc": True, "Pacific Analytics Corp": False}
    contingency = contingency_assessment(transfers, backups)
    print(json.dumps(contingency, indent=2))
