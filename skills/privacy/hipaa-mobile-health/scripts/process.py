#!/usr/bin/env python3
"""
HIPAA Mobile Health Compliance Assessment Tool

Assesses mobile device and mHealth application compliance with HIPAA
Security Rule requirements, BYOD policies, and mobile-specific safeguards.
"""

import json
import sys
from datetime import datetime


MOBILE_SECURITY_REQUIREMENTS = {
    "device_encryption": {
        "regulation": "45 CFR §164.312(a)(2)(iv)",
        "description": "Full-disk encryption on all mobile devices with ePHI",
        "severity_if_missing": "critical",
    },
    "screen_lock": {
        "regulation": "45 CFR §164.312(a)(2)(iii)",
        "description": "Auto-logoff after inactivity (max 2 minutes)",
        "severity_if_missing": "high",
    },
    "remote_wipe": {
        "regulation": "45 CFR §164.310(d)(2)(iii)",
        "description": "Remote wipe capability via MDM",
        "severity_if_missing": "critical",
    },
    "transmission_encryption": {
        "regulation": "45 CFR §164.312(e)(1)",
        "description": "TLS 1.2+ for all data in transit",
        "severity_if_missing": "critical",
    },
    "authentication": {
        "regulation": "45 CFR §164.312(d)",
        "description": "Per-app authentication for ePHI access",
        "severity_if_missing": "high",
    },
    "mdm_enrollment": {
        "regulation": "45 CFR §164.310(d)",
        "description": "Mobile device management enrollment",
        "severity_if_missing": "high",
    },
    "malware_protection": {
        "regulation": "45 CFR §164.308(a)(5)(ii)(B)",
        "description": "Mobile threat defense software",
        "severity_if_missing": "medium",
    },
    "audit_logging": {
        "regulation": "45 CFR §164.312(b)",
        "description": "Audit trails for device access and data transfers",
        "severity_if_missing": "high",
    },
    "jailbreak_detection": {
        "regulation": "45 CFR §164.312(a)(1)",
        "description": "Jailbreak/root detection blocking ePHI access",
        "severity_if_missing": "high",
    },
    "os_patch_policy": {
        "regulation": "45 CFR §164.308(a)(5)(ii)(B)",
        "description": "OS and app update policy enforced via MDM",
        "severity_if_missing": "medium",
    },
}


def assess_mobile_device(device: dict) -> dict:
    """Assess a single mobile device's HIPAA compliance."""
    device_id = device.get("device_id", "Unknown")
    device_type = device.get("device_type", "smartphone")
    ownership = device.get("ownership", "organization")
    implemented_controls = device.get("implemented_controls", [])

    findings = []
    for control_id, control in MOBILE_SECURITY_REQUIREMENTS.items():
        if control_id not in implemented_controls:
            findings.append({
                "severity": control["severity_if_missing"],
                "finding": f"Missing control: {control['description']}",
                "regulation": control["regulation"],
                "remediation": f"Implement {control_id} on device {device_id}",
            })

    missing_critical = sum(1 for f in findings if f["severity"] == "critical")
    missing_high = sum(1 for f in findings if f["severity"] == "high")

    if missing_critical > 0:
        status = "non_compliant"
    elif missing_high > 0:
        status = "partially_compliant"
    elif len(findings) > 0:
        status = "partially_compliant"
    else:
        status = "compliant"

    return {
        "device_id": device_id,
        "device_type": device_type,
        "ownership": ownership,
        "compliance_status": status,
        "controls_implemented": len(implemented_controls),
        "controls_required": len(MOBILE_SECURITY_REQUIREMENTS),
        "findings": findings,
    }


def assess_mhealth_app(app: dict) -> dict:
    """Assess an mHealth application's privacy and security posture."""
    app_name = app.get("name", "Unknown App")
    findings = []

    is_hipaa_covered = app.get("hipaa_covered", False)
    has_baa = app.get("baa_executed", False)
    encryption_at_rest = app.get("encryption_at_rest", False)
    encryption_in_transit = app.get("encryption_in_transit", False)
    consent_mechanism = app.get("consent_mechanism", False)
    data_retention_defined = app.get("data_retention_defined", False)
    penetration_tested = app.get("penetration_tested", False)

    if is_hipaa_covered and not has_baa:
        findings.append({
            "severity": "critical",
            "finding": f"App '{app_name}' processes PHI but no BAA executed with vendor",
            "regulation": "45 CFR §164.502(e)",
            "remediation": "Execute BAA with app vendor before processing PHI",
        })

    if not encryption_at_rest:
        findings.append({
            "severity": "critical",
            "finding": f"App '{app_name}' does not encrypt data at rest",
            "regulation": "45 CFR §164.312(a)(2)(iv)",
            "remediation": "Implement AES-256 encryption for stored data",
        })

    if not encryption_in_transit:
        findings.append({
            "severity": "critical",
            "finding": f"App '{app_name}' does not encrypt data in transit",
            "regulation": "45 CFR §164.312(e)(1)",
            "remediation": "Implement TLS 1.2+ for all network communications",
        })

    if not consent_mechanism:
        findings.append({
            "severity": "high",
            "finding": f"App '{app_name}' lacks a clear consent mechanism for data collection",
            "regulation": "45 CFR §164.508" if is_hipaa_covered else "16 CFR Part 318",
            "remediation": "Implement informed consent flow for health data collection",
        })

    if not data_retention_defined:
        findings.append({
            "severity": "medium",
            "finding": f"App '{app_name}' has no defined data retention period",
            "regulation": "45 CFR §164.530(j)",
            "remediation": "Define and implement data retention and disposal policy",
        })

    if not penetration_tested:
        findings.append({
            "severity": "medium",
            "finding": f"App '{app_name}' has not undergone penetration testing",
            "regulation": "45 CFR §164.308(a)(8)",
            "remediation": "Conduct penetration test and OWASP Mobile Top 10 assessment",
        })

    status = "compliant"
    if any(f["severity"] == "critical" for f in findings):
        status = "non_compliant"
    elif any(f["severity"] == "high" for f in findings):
        status = "partially_compliant"

    return {
        "app_name": app_name,
        "hipaa_covered": is_hipaa_covered,
        "compliance_status": status,
        "findings": findings,
    }


def generate_mobile_health_report(input_data: dict) -> dict:
    """Generate mobile health compliance report."""
    organization = input_data.get("organization", "Unknown Organization")
    devices = input_data.get("devices", [])
    apps = input_data.get("mhealth_apps", [])
    byod_policy_exists = input_data.get("byod_policy_exists", False)

    device_assessments = [assess_mobile_device(d) for d in devices]
    app_assessments = [assess_mhealth_app(a) for a in apps]

    all_findings = []
    for a in device_assessments:
        for f in a["findings"]:
            f["source"] = f"Device: {a['device_id']}"
            all_findings.append(f)
    for a in app_assessments:
        for f in a["findings"]:
            f["source"] = f"App: {a['app_name']}"
            all_findings.append(f)

    if not byod_policy_exists and any(d.get("ownership") == "personal" for d in devices):
        all_findings.append({
            "severity": "high",
            "finding": "Personal (BYOD) devices access ePHI but no BYOD policy exists",
            "regulation": "45 CFR §164.310(b)",
            "remediation": "Develop and implement BYOD acceptable use policy",
            "source": "Policy",
        })

    critical = [f for f in all_findings if f["severity"] == "critical"]
    high = [f for f in all_findings if f["severity"] == "high"]

    return {
        "report_title": "HIPAA Mobile Health Compliance Assessment",
        "organization": organization,
        "report_date": datetime.now().strftime("%Y-%m-%d"),
        "summary": {
            "devices_assessed": len(device_assessments),
            "apps_assessed": len(app_assessments),
            "total_findings": len(all_findings),
            "critical": len(critical),
            "high": len(high),
            "medium": len([f for f in all_findings if f["severity"] == "medium"]),
        },
        "device_assessments": device_assessments,
        "app_assessments": app_assessments,
        "policy_findings": [f for f in all_findings if f.get("source") == "Policy"],
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <mobile_health_data.json>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        input_data = json.load(f)

    report = generate_mobile_health_report(input_data)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
