#!/usr/bin/env python3
"""HIPAA Business Associate Agreement management, inventory tracking, and compliance assessment."""

import json
import os
from datetime import datetime, timedelta
from typing import Any


BAA_REQUIRED_PROVISIONS = [
    {
        "id": "permitted_uses",
        "description": "Establish permitted and required uses and disclosures of PHI",
        "cfr_reference": "§164.504(e)(2)(i)",
    },
    {
        "id": "prohibition_unauthorized",
        "description": "Prohibit unauthorized use or disclosure",
        "cfr_reference": "§164.504(e)(2)(ii)(A)",
    },
    {
        "id": "appropriate_safeguards",
        "description": "Require appropriate safeguards and Security Rule compliance",
        "cfr_reference": "§164.504(e)(2)(ii)(B)",
    },
    {
        "id": "breach_reporting",
        "description": "Require breach reporting to covered entity",
        "cfr_reference": "§164.504(e)(2)(ii)(C)",
    },
    {
        "id": "subcontractor_requirements",
        "description": "Ensure subcontractors agree to same restrictions",
        "cfr_reference": "§164.504(e)(2)(ii)(D)",
    },
    {
        "id": "access_rights",
        "description": "Make PHI available for individual access rights",
        "cfr_reference": "§164.504(e)(2)(ii)(E)",
    },
    {
        "id": "amendment_rights",
        "description": "Make PHI available for amendment",
        "cfr_reference": "§164.504(e)(2)(ii)(F)",
    },
    {
        "id": "accounting_disclosures",
        "description": "Provide information for accounting of disclosures",
        "cfr_reference": "§164.504(e)(2)(ii)(G)",
    },
    {
        "id": "hhs_access",
        "description": "Make practices and records available to HHS",
        "cfr_reference": "§164.504(e)(2)(ii)(H)",
    },
    {
        "id": "return_destroy_phi",
        "description": "Return or destroy PHI at termination",
        "cfr_reference": "§164.504(e)(2)(ii)(I)",
    },
]

BA_RISK_CATEGORIES = {
    "critical": {"phi_access": "full_record", "data_volume": "high", "system_access": "direct"},
    "high": {"phi_access": "clinical", "data_volume": "medium", "system_access": "direct"},
    "medium": {"phi_access": "limited", "data_volume": "low", "system_access": "indirect"},
    "low": {"phi_access": "incidental", "data_volume": "minimal", "system_access": "none"},
}


def determine_ba_status(vendor: dict[str, Any]) -> dict[str, Any]:
    """Determine whether a vendor qualifies as a business associate.

    Args:
        vendor: Dictionary containing vendor relationship details.

    Returns:
        BA determination result with rationale.
    """
    result = {
        "vendor_name": vendor.get("name", ""),
        "determination_date": datetime.now().isoformat(),
        "is_business_associate": False,
        "baa_required": False,
        "rationale": "",
        "exceptions_applied": [],
    }

    creates_phi = vendor.get("creates_phi", False)
    receives_phi = vendor.get("receives_phi", False)
    maintains_phi = vendor.get("maintains_phi", False)
    transmits_phi = vendor.get("transmits_phi", False)
    has_phi_access = creates_phi or receives_phi or maintains_phi or transmits_phi

    if not has_phi_access:
        result["rationale"] = "Vendor does not create, receive, maintain, or transmit PHI"
        return result

    if vendor.get("is_workforce_member", False):
        result["rationale"] = "Entity is a workforce member, not a business associate"
        result["exceptions_applied"].append("workforce_exception")
        return result

    if vendor.get("treatment_disclosure_only", False):
        result["rationale"] = "PHI exchange is solely for treatment between covered entities"
        result["exceptions_applied"].append("treatment_ce_exception")
        return result

    if vendor.get("is_conduit", False):
        result["rationale"] = "Entity is a conduit — merely transports PHI without persistent access"
        result["exceptions_applied"].append("conduit_exception")
        return result

    result["is_business_associate"] = True
    result["baa_required"] = True

    functions = vendor.get("functions", [])
    result["rationale"] = (
        f"Vendor {('creates' if creates_phi else '')}"
        f"{(', receives' if receives_phi else '')}"
        f"{(', maintains' if maintains_phi else '')}"
        f"{(', transmits' if transmits_phi else '')} "
        f"PHI for functions: {', '.join(functions) if functions else 'not specified'}"
    )

    return result


def validate_baa_provisions(baa: dict[str, Any]) -> dict[str, Any]:
    """Validate BAA against all required provisions per §164.504(e)(2).

    Args:
        baa: Dictionary containing BAA provisions status.

    Returns:
        Validation result with compliance status per provision.
    """
    result = {
        "ba_name": baa.get("ba_name", ""),
        "baa_date": baa.get("baa_date", ""),
        "validation_date": datetime.now().isoformat(),
        "valid": True,
        "provisions": [],
        "missing_provisions": [],
        "summary": {
            "total_required": len(BAA_REQUIRED_PROVISIONS),
            "present": 0,
            "missing": 0,
        },
    }

    provisions_status = baa.get("provisions", {})
    for provision in BAA_REQUIRED_PROVISIONS:
        present = provisions_status.get(provision["id"], False)
        result["provisions"].append({
            "id": provision["id"],
            "description": provision["description"],
            "cfr_reference": provision["cfr_reference"],
            "present": present,
        })
        if present:
            result["summary"]["present"] += 1
        else:
            result["summary"]["missing"] += 1
            result["missing_provisions"].append(provision["description"])
            result["valid"] = False

    if baa.get("breach_reporting_days", 60) > 60:
        result["provisions"].append({
            "id": "breach_timeline_check",
            "description": "Breach reporting timeline exceeds 60-day regulatory maximum",
            "present": False,
            "warning": True,
        })

    return result


def assess_ba_inventory(
    business_associates: list[dict[str, Any]],
) -> dict[str, Any]:
    """Assess the complete BA inventory for compliance status.

    Args:
        business_associates: List of BA records.

    Returns:
        Inventory assessment with risk categorization and gaps.
    """
    assessment = {
        "assessment_date": datetime.now().isoformat(),
        "total_bas": len(business_associates),
        "risk_distribution": {"critical": 0, "high": 0, "medium": 0, "low": 0},
        "compliance_status": {
            "baa_current": 0,
            "baa_expired": 0,
            "baa_missing": 0,
            "security_assessment_current": 0,
            "security_assessment_overdue": 0,
        },
        "action_items": [],
        "business_associates": [],
    }

    for ba in business_associates:
        ba_record = {
            "name": ba.get("name", ""),
            "category": ba.get("category", ""),
            "risk_level": ba.get("risk_level", "medium"),
            "baa_status": ba.get("baa_status", "unknown"),
            "baa_expiration": ba.get("baa_expiration", ""),
            "last_security_assessment": ba.get("last_security_assessment", ""),
            "subcontractors": ba.get("subcontractors", 0),
            "incidents_reported": ba.get("incidents_reported", 0),
        }

        risk_level = ba.get("risk_level", "medium")
        if risk_level in assessment["risk_distribution"]:
            assessment["risk_distribution"][risk_level] += 1

        baa_status = ba.get("baa_status", "missing")
        if baa_status == "current":
            assessment["compliance_status"]["baa_current"] += 1
        elif baa_status == "expired":
            assessment["compliance_status"]["baa_expired"] += 1
            assessment["action_items"].append({
                "ba_name": ba.get("name", ""),
                "issue": "BAA expired",
                "priority": "high",
                "action": "Execute renewed BAA immediately",
            })
        else:
            assessment["compliance_status"]["baa_missing"] += 1
            assessment["action_items"].append({
                "ba_name": ba.get("name", ""),
                "issue": "No BAA in place",
                "priority": "critical",
                "action": "Execute BAA before any PHI access; suspend PHI access until BAA signed",
            })

        last_assessment = ba.get("last_security_assessment", "")
        if last_assessment:
            try:
                last_date = datetime.strptime(last_assessment, "%Y-%m-%d")
                if (datetime.now() - last_date).days <= 365:
                    assessment["compliance_status"]["security_assessment_current"] += 1
                else:
                    assessment["compliance_status"]["security_assessment_overdue"] += 1
                    assessment["action_items"].append({
                        "ba_name": ba.get("name", ""),
                        "issue": "Security assessment overdue",
                        "priority": "medium",
                        "action": "Request updated security questionnaire and SOC 2 report",
                    })
            except ValueError:
                assessment["compliance_status"]["security_assessment_overdue"] += 1
        else:
            assessment["compliance_status"]["security_assessment_overdue"] += 1

        assessment["business_associates"].append(ba_record)

    return assessment


def generate_termination_checklist(
    ba_name: str,
    termination_date: str,
    phi_return_method: str = "destroy",
) -> dict[str, Any]:
    """Generate a BAA termination and PHI return/destruction checklist.

    Args:
        ba_name: Name of the business associate.
        termination_date: Effective termination date (YYYY-MM-DD).
        phi_return_method: Method for PHI handling — 'return' or 'destroy'.

    Returns:
        Termination checklist with tasks and deadlines.
    """
    term_date = datetime.strptime(termination_date, "%Y-%m-%d")

    checklist = {
        "ba_name": ba_name,
        "termination_date": termination_date,
        "phi_method": phi_return_method,
        "generated_date": datetime.now().isoformat(),
        "tasks": [
            {
                "task": "Send written termination notice to BA",
                "deadline": (term_date - timedelta(days=60)).strftime("%Y-%m-%d"),
                "responsible": "Legal / Privacy Office",
                "status": "pending",
            },
            {
                "task": "Restrict BA PHI access to minimum necessary for transition",
                "deadline": (term_date - timedelta(days=30)).strftime("%Y-%m-%d"),
                "responsible": "IT Security",
                "status": "pending",
            },
            {
                "task": "Revoke all system access (VPN, API keys, user accounts)",
                "deadline": termination_date,
                "responsible": "IT Security",
                "status": "pending",
            },
            {
                "task": f"BA {'returns' if phi_return_method == 'return' else 'certifies destruction of'} all PHI",
                "deadline": (term_date + timedelta(days=30)).strftime("%Y-%m-%d"),
                "responsible": "BA / Privacy Office verification",
                "status": "pending",
            },
            {
                "task": "Obtain written certification of PHI destruction/return",
                "deadline": (term_date + timedelta(days=30)).strftime("%Y-%m-%d"),
                "responsible": "Privacy Office",
                "status": "pending",
            },
            {
                "task": "Update BA tracking system (status: terminated)",
                "deadline": (term_date + timedelta(days=5)).strftime("%Y-%m-%d"),
                "responsible": "Privacy Office",
                "status": "pending",
            },
            {
                "task": "Archive BAA and all related documentation (retain 6 years)",
                "deadline": (term_date + timedelta(days=30)).strftime("%Y-%m-%d"),
                "responsible": "Compliance / Records Management",
                "status": "pending",
            },
        ],
    }

    return checklist


def export_report(data: dict[str, Any], output_path: str) -> str:
    """Export report to JSON file."""
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return output_path


if __name__ == "__main__":
    print("=== HIPAA BAA Management Assessment ===\n")

    vendor_test = {
        "name": "CloudHealth Analytics Inc.",
        "creates_phi": False,
        "receives_phi": True,
        "maintains_phi": True,
        "transmits_phi": True,
        "functions": ["data analytics", "population health management", "quality reporting"],
    }
    determination = determine_ba_status(vendor_test)
    print(f"BA Determination: {vendor_test['name']}")
    print(f"  Is BA: {determination['is_business_associate']}")
    print(f"  BAA Required: {determination['baa_required']}")
    print(f"  Rationale: {determination['rationale']}\n")

    sample_bas = [
        {"name": "Epic Systems (EHR)", "category": "IT Vendor", "risk_level": "critical", "baa_status": "current", "last_security_assessment": "2025-09-15", "subcontractors": 3, "incidents_reported": 0},
        {"name": "TranscribeMed LLC", "category": "Transcription", "risk_level": "high", "baa_status": "current", "last_security_assessment": "2025-06-01", "subcontractors": 1, "incidents_reported": 0},
        {"name": "SecureShred Corp", "category": "Destruction", "risk_level": "low", "baa_status": "expired", "last_security_assessment": "2024-01-15", "subcontractors": 0, "incidents_reported": 0},
        {"name": "DataInsight Analytics", "category": "Analytics", "risk_level": "high", "baa_status": "missing", "last_security_assessment": "", "subcontractors": 2, "incidents_reported": 0},
    ]

    inventory = assess_ba_inventory(sample_bas)
    print(f"BA Inventory Assessment:")
    print(f"  Total BAs: {inventory['total_bas']}")
    print(f"  BAA Current: {inventory['compliance_status']['baa_current']}")
    print(f"  BAA Expired: {inventory['compliance_status']['baa_expired']}")
    print(f"  BAA Missing: {inventory['compliance_status']['baa_missing']}")
    print(f"  Action Items: {len(inventory['action_items'])}")
    for item in inventory["action_items"]:
        print(f"    [{item['priority'].upper()}] {item['ba_name']}: {item['issue']}")
