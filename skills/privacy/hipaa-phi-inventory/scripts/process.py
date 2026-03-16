#!/usr/bin/env python3
"""
HIPAA PHI Inventory Assessment Tool

Generates and assesses a PHI inventory against HIPAA Security Rule
requirements. Identifies gaps in ePHI asset documentation, data flow
mapping, and security controls per 45 CFR §164.308(a)(1)(ii)(A).
"""

import json
import sys
from datetime import datetime


REQUIRED_ASSET_FIELDS = [
    "system_name",
    "system_owner",
    "phi_types",
    "record_volume_estimate",
    "hosting_location",
    "encryption_at_rest",
    "encryption_in_transit",
    "access_control_method",
    "audit_logging_enabled",
    "baa_required",
    "last_risk_assessment_date",
]

PHI_CATEGORIES = [
    "demographics",
    "clinical_records",
    "billing_financial",
    "lab_results",
    "imaging",
    "pharmacy",
    "mental_health",
    "substance_abuse",
    "hiv_sti",
    "genetic",
    "reproductive",
]

SENSITIVE_PHI_CATEGORIES = [
    "mental_health",
    "substance_abuse",
    "hiv_sti",
    "genetic",
    "reproductive",
]


def assess_asset(asset: dict) -> dict:
    """Assess a single PHI asset for inventory completeness and security."""
    system_name = asset.get("system_name", "Unknown System")
    findings = []

    # Check required fields
    missing_fields = [f for f in REQUIRED_ASSET_FIELDS if not asset.get(f)]
    if missing_fields:
        findings.append({
            "severity": "high",
            "finding": f"Incomplete inventory record — missing fields: {', '.join(missing_fields)}",
            "regulation": "45 CFR §164.308(a)(1)(ii)(A)",
            "remediation": "Complete all required inventory fields for accurate risk analysis",
        })

    # Check encryption at rest
    if asset.get("encryption_at_rest") is False:
        findings.append({
            "severity": "critical",
            "finding": f"ePHI at rest is NOT encrypted on '{system_name}'",
            "regulation": "45 CFR §164.312(a)(2)(iv)",
            "remediation": "Implement encryption at rest (AES-256) or document equivalent alternative measure",
        })

    # Check encryption in transit
    if asset.get("encryption_in_transit") is False:
        findings.append({
            "severity": "critical",
            "finding": f"ePHI in transit is NOT encrypted for '{system_name}'",
            "regulation": "45 CFR §164.312(e)(1)",
            "remediation": "Implement TLS 1.2+ for all ePHI transmissions",
        })

    # Check audit logging
    if asset.get("audit_logging_enabled") is False:
        findings.append({
            "severity": "high",
            "finding": f"Audit logging not enabled on '{system_name}'",
            "regulation": "45 CFR §164.312(b)",
            "remediation": "Enable audit logging to record and examine access to ePHI",
        })

    # Check BAA status
    baa_required = asset.get("baa_required", False)
    baa_executed = asset.get("baa_executed", False)
    if baa_required and not baa_executed:
        findings.append({
            "severity": "critical",
            "finding": f"BAA required but not executed for '{system_name}'",
            "regulation": "45 CFR §164.502(e)",
            "remediation": "Execute BAA with vendor before continued PHI processing",
        })

    # Check risk assessment currency
    last_ra = asset.get("last_risk_assessment_date", "")
    if last_ra:
        try:
            ra_date = datetime.strptime(last_ra, "%Y-%m-%d")
            days_since = (datetime.now() - ra_date).days
            if days_since > 365:
                findings.append({
                    "severity": "medium",
                    "finding": f"Risk assessment for '{system_name}' is {days_since} days old (last: {last_ra})",
                    "regulation": "45 CFR §164.308(a)(1)(ii)(A)",
                    "remediation": "Conduct updated risk assessment; recommend annual reviews",
                })
        except ValueError:
            pass

    # Check for sensitive PHI requiring additional protections
    phi_types = asset.get("phi_types", [])
    sensitive_types = [t for t in phi_types if t in SENSITIVE_PHI_CATEGORIES]
    additional_controls = asset.get("additional_sensitivity_controls", False)
    if sensitive_types and not additional_controls:
        findings.append({
            "severity": "high",
            "finding": f"System '{system_name}' contains sensitive PHI ({', '.join(sensitive_types)}) "
                       f"without documented additional controls",
            "regulation": "45 CFR §164.312(a)(1) + state/federal sensitivity requirements",
            "remediation": "Implement enhanced access controls and consent management for sensitive data categories",
        })

    status = "compliant"
    if any(f["severity"] == "critical" for f in findings):
        status = "non_compliant"
    elif any(f["severity"] == "high" for f in findings):
        status = "partially_compliant"

    return {
        "system_name": system_name,
        "compliance_status": status,
        "phi_types": phi_types,
        "sensitive_phi": sensitive_types,
        "findings_count": len(findings),
        "findings": findings,
    }


def assess_data_flows(flows: list) -> list:
    """Assess data flow documentation for completeness."""
    findings = []
    for flow in flows:
        flow_name = flow.get("name", f"{flow.get('source', '?')} -> {flow.get('destination', '?')}")

        if not flow.get("encryption_method"):
            findings.append({
                "severity": "critical",
                "finding": f"Data flow '{flow_name}' has no encryption documented",
                "regulation": "45 CFR §164.312(e)(1)",
                "remediation": "Document and verify encryption method for this data flow",
            })

        if not flow.get("phi_types_transmitted"):
            findings.append({
                "severity": "medium",
                "finding": f"Data flow '{flow_name}' does not specify PHI types transmitted",
                "regulation": "45 CFR §164.308(a)(1)(ii)(A)",
                "remediation": "Document the specific PHI categories transmitted in this flow",
            })

    return findings


def generate_inventory_report(input_data: dict) -> dict:
    """Generate comprehensive PHI inventory assessment report."""
    organization = input_data.get("organization", "Unknown Organization")
    assets = input_data.get("phi_assets", [])
    data_flows = input_data.get("data_flows", [])

    asset_assessments = [assess_asset(a) for a in assets]
    flow_findings = assess_data_flows(data_flows)

    all_findings = []
    for a in asset_assessments:
        for f in a["findings"]:
            f["source_system"] = a["system_name"]
            all_findings.append(f)
    for f in flow_findings:
        all_findings.append(f)

    total_assets = len(assets)
    compliant = sum(1 for a in asset_assessments if a["compliance_status"] == "compliant")
    partial = sum(1 for a in asset_assessments if a["compliance_status"] == "partially_compliant")
    non_compliant = sum(1 for a in asset_assessments if a["compliance_status"] == "non_compliant")

    all_phi_types = set()
    for a in assets:
        all_phi_types.update(a.get("phi_types", []))

    return {
        "report_title": "HIPAA PHI Inventory Assessment Report",
        "organization": organization,
        "report_date": datetime.now().strftime("%Y-%m-%d"),
        "regulatory_basis": "45 CFR §164.308(a)(1)(ii)(A) — Risk Analysis (ePHI asset identification)",
        "summary": {
            "total_phi_assets": total_assets,
            "compliant": compliant,
            "partially_compliant": partial,
            "non_compliant": non_compliant,
            "data_flows_documented": len(data_flows),
            "phi_categories_identified": sorted(list(all_phi_types)),
            "total_findings": len(all_findings),
            "critical_findings": len([f for f in all_findings if f["severity"] == "critical"]),
            "high_findings": len([f for f in all_findings if f["severity"] == "high"]),
        },
        "asset_assessments": asset_assessments,
        "data_flow_findings": flow_findings,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <phi_inventory_data.json>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        input_data = json.load(f)

    report = generate_inventory_report(input_data)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
