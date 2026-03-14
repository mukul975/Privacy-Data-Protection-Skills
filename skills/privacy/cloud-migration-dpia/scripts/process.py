#!/usr/bin/env python3
"""Cloud Migration Privacy Assessment Engine.

Implements DPIA methodology for cloud migration covering controller-processor
analysis, shared responsibility evaluation, international transfer assessment,
and encryption posture scoring.
"""

import json
from datetime import datetime, timedelta
from typing import Any

SHARED_RESPONSIBILITY = {
    "iaas": {
        "name": "Infrastructure as a Service",
        "csp_responsibility": [
            "Physical infrastructure security",
            "Hardware lifecycle management",
            "Network infrastructure",
            "Hypervisor security",
        ],
        "customer_responsibility": [
            "Operating system patching",
            "Application security",
            "Data encryption implementation",
            "Identity and access management",
            "Data classification and governance",
            "Logging and monitoring",
            "Data subject rights facilitation",
        ],
        "shared_responsibility": [
            "Network security configuration",
            "Firewall rules",
        ],
    },
    "paas": {
        "name": "Platform as a Service",
        "csp_responsibility": [
            "Physical infrastructure",
            "Network infrastructure",
            "Operating system",
            "Runtime environment",
            "Platform security patching",
        ],
        "customer_responsibility": [
            "Application code security",
            "Data encryption configuration",
            "Identity and access management",
            "Data classification and governance",
            "Data subject rights facilitation",
        ],
        "shared_responsibility": [
            "Application configuration security",
            "Data encryption at rest",
            "Logging and monitoring",
        ],
    },
    "saas": {
        "name": "Software as a Service",
        "csp_responsibility": [
            "Physical infrastructure",
            "Network infrastructure",
            "Operating system",
            "Application security",
            "Data encryption at rest and in transit",
            "Backup and recovery",
        ],
        "customer_responsibility": [
            "Data classification",
            "User access management",
            "Data subject rights facilitation",
            "DPA and governance",
        ],
        "shared_responsibility": [
            "Identity and access management",
            "Security monitoring and alerting",
            "Data retention configuration",
        ],
    },
}

DPA_CHECKLIST = [
    {"id": "DPA1", "reference": "Art. 28(3)(a)", "requirement": "Processing only on documented instructions of the controller"},
    {"id": "DPA2", "reference": "Art. 28(3)(b)", "requirement": "Confidentiality obligations for all authorised processing persons"},
    {"id": "DPA3", "reference": "Art. 28(3)(c)", "requirement": "Appropriate technical and organisational security measures per Art. 32"},
    {"id": "DPA4", "reference": "Art. 28(3)(d)", "requirement": "Sub-processor engagement conditions with prior authorisation and flow-down"},
    {"id": "DPA5", "reference": "Art. 28(3)(e)", "requirement": "Assistance with data subject rights requests"},
    {"id": "DPA6", "reference": "Art. 28(3)(f)", "requirement": "Assistance with security, breach notification, DPIA, and prior consultation"},
    {"id": "DPA7", "reference": "Art. 28(3)(g)", "requirement": "Deletion or return of personal data on processing termination"},
    {"id": "DPA8", "reference": "Art. 28(3)(h)", "requirement": "Audit and inspection rights for the controller"},
]


def assess_dpa_compliance(
    dpa_item_status: dict[str, str],
) -> dict[str, Any]:
    """Assess CSP DPA compliance against Art. 28(3) requirements.

    Args:
        dpa_item_status: Mapping of DPA item IDs to status ("compliant", "partial", "missing")

    Returns:
        DPA compliance assessment
    """
    results = []
    for item in DPA_CHECKLIST:
        status = dpa_item_status.get(item["id"], "missing")
        results.append({
            "id": item["id"],
            "reference": item["reference"],
            "requirement": item["requirement"],
            "status": status,
        })

    missing = [r for r in results if r["status"] == "missing"]
    partial = [r for r in results if r["status"] == "partial"]
    compliant = len(missing) == 0 and len(partial) == 0

    return {
        "checklist_results": results,
        "total_items": len(results),
        "compliant": len([r for r in results if r["status"] == "compliant"]),
        "partial": len(partial),
        "missing": len(missing),
        "overall_compliant": compliant,
        "action_required": (
            "DPA meets all Art. 28(3) requirements."
            if compliant
            else f"DPA has {len(missing)} missing and {len(partial)} partially "
            f"compliant elements. Negotiate DPA amendments before migration."
        ),
    }


def assess_encryption_posture(
    encryption_at_rest: bool,
    encryption_algorithm: str,
    key_management: str,
    encryption_in_transit: bool,
    tls_version: str,
    client_side_encryption: bool,
    byok_available: bool,
    byok_implemented: bool,
) -> dict[str, Any]:
    """Assess cloud encryption posture.

    Args:
        key_management: "csp_managed", "customer_managed_byok", "customer_managed_hyok", or "client_side"

    Returns:
        Encryption posture assessment with score
    """
    score = 0
    findings = []

    if encryption_at_rest:
        score += 20
        if encryption_algorithm in ("AES-256", "AES-256-GCM"):
            score += 10
        else:
            findings.append(f"Encryption algorithm {encryption_algorithm} should be AES-256 or AES-256-GCM.")
    else:
        findings.append("Data at rest is not encrypted. This is a critical deficiency.")

    if encryption_in_transit:
        score += 15
        if tls_version in ("TLS 1.3", "TLS 1.2"):
            score += 5
        else:
            findings.append(f"TLS version {tls_version} is below recommended minimum of TLS 1.2.")
    else:
        findings.append("Data in transit is not encrypted. This is a critical deficiency.")

    if key_management == "client_side":
        score += 30
        findings.append("Client-side encryption provides strongest protection — CSP never accesses clear-text data.")
    elif key_management == "customer_managed_hyok":
        score += 25
        findings.append("Hold Your Own Key (HYOK) provides strong protection — key never leaves customer control.")
    elif key_management == "customer_managed_byok":
        score += 20
        findings.append("Bring Your Own Key (BYOK) provides good protection but key is imported to CSP key management.")
    elif key_management == "csp_managed":
        score += 10
        findings.append(
            "CSP-managed keys protect against physical theft but not against CSP "
            "staff access or government compulsion to the CSP."
        )

    if client_side_encryption:
        score += 20
    elif byok_implemented:
        score += 10
    elif byok_available:
        findings.append("BYOK is available but not implemented. Consider implementing for sensitive data.")

    protection_level = (
        "Strong" if score >= 80
        else "Adequate" if score >= 60
        else "Insufficient" if score >= 40
        else "Critical deficiency"
    )

    return {
        "score": score,
        "max_score": 100,
        "protection_level": protection_level,
        "encryption_at_rest": encryption_at_rest,
        "encryption_algorithm": encryption_algorithm,
        "encryption_in_transit": encryption_in_transit,
        "tls_version": tls_version,
        "key_management": key_management,
        "client_side_encryption": client_side_encryption,
        "byok_available": byok_available,
        "byok_implemented": byok_implemented,
        "findings": findings,
    }


def generate_cloud_migration_report(
    reference: str,
    org_name: str,
    csp_name: str,
    service_model: str,
    data_categories: list[str],
    processing_locations: list[str],
    dpa_assessment: dict[str, Any],
    encryption_assessment: dict[str, Any],
) -> dict[str, Any]:
    """Generate cloud migration DPIA report."""
    model_info = SHARED_RESPONSIBILITY.get(service_model, {})
    non_eea = [loc for loc in processing_locations if loc not in (
        "EU", "EEA", "Germany", "Ireland", "Netherlands", "France",
        "Belgium", "Austria", "Spain", "Italy", "Finland", "Sweden",
    )]

    return {
        "metadata": {
            "reference": reference,
            "organisation": org_name,
            "csp": csp_name,
            "service_model": model_info.get("name", service_model),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "next_review": (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d"),
        },
        "data_categories": data_categories,
        "processing_locations": processing_locations,
        "non_eea_locations": non_eea,
        "international_transfer_required": len(non_eea) > 0,
        "shared_responsibility_model": model_info,
        "dpa_assessment": dpa_assessment,
        "encryption_assessment": encryption_assessment,
        "conclusion": {
            "dpa_compliant": dpa_assessment["overall_compliant"],
            "encryption_adequate": encryption_assessment["protection_level"] in ("Strong", "Adequate"),
            "migration_approved": (
                dpa_assessment["overall_compliant"]
                and encryption_assessment["protection_level"] in ("Strong", "Adequate")
            ),
        },
    }


def run_example_assessment() -> dict[str, Any]:
    """Run example cloud migration DPIA for QuantumLeap Health Technologies."""

    dpa = assess_dpa_compliance({
        "DPA1": "compliant",
        "DPA2": "compliant",
        "DPA3": "compliant",
        "DPA4": "compliant",
        "DPA5": "partial",
        "DPA6": "compliant",
        "DPA7": "compliant",
        "DPA8": "partial",
    })

    encryption = assess_encryption_posture(
        encryption_at_rest=True,
        encryption_algorithm="AES-256",
        key_management="customer_managed_byok",
        encryption_in_transit=True,
        tls_version="TLS 1.3",
        client_side_encryption=False,
        byok_available=True,
        byok_implemented=True,
    )

    return generate_cloud_migration_report(
        reference="DPIA-QLH-2026-0010",
        org_name="QuantumLeap Health Technologies",
        csp_name="Amazon Web Services EMEA SARL",
        service_model="paas",
        data_categories=[
            "Patient clinical trial identifiers (pseudonymised)",
            "Employee HR records",
            "Customer billing and contact information",
            "Research collaboration metadata",
        ],
        processing_locations=["Ireland (eu-west-1)", "Germany (eu-central-1)"],
        dpa_assessment=dpa,
        encryption_assessment=encryption,
    )


if __name__ == "__main__":
    result = run_example_assessment()
    print(json.dumps(result, indent=2, default=str))
