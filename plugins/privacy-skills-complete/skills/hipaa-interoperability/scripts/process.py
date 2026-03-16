#!/usr/bin/env python3
"""
HIPAA Interoperability Compliance Assessment Tool

Assesses compliance with interoperability requirements under the 21st Century
Cures Act, ONC Information Blocking Rule, CMS Interoperability and Patient
Access Final Rule, and TEFCA requirements.
"""

import json
import sys
from datetime import datetime


INFORMATION_BLOCKING_EXCEPTIONS = {
    "preventing_harm": {
        "cfr": "45 CFR §171.201",
        "description": "Practice is reasonable and necessary to prevent harm",
    },
    "privacy": {
        "cfr": "45 CFR §171.202",
        "description": "Practice is required by or consistent with HIPAA Privacy Rule",
    },
    "security": {
        "cfr": "45 CFR §171.203",
        "description": "Practice is directly related to safeguarding C/I/A of EHI",
    },
    "infeasibility": {
        "cfr": "45 CFR §171.204",
        "description": "Fulfilling the request is technically infeasible",
    },
    "health_it_performance": {
        "cfr": "45 CFR §171.205",
        "description": "Practice is for reasonable maintenance or improvements",
    },
    "content_and_manner": {
        "cfr": "45 CFR §171.301",
        "description": "Actor fulfills request in alternative manner or content",
    },
    "fees": {
        "cfr": "45 CFR §171.302",
        "description": "Fees are reasonable and based on objective criteria",
    },
    "licensing": {
        "cfr": "45 CFR §171.303",
        "description": "Licensing terms are reasonable and non-discriminatory",
    },
}

REQUIRED_PATIENT_ACCESS_API_ELEMENTS = [
    "fhir_r4_endpoint",
    "uscdi_data_classes",
    "oauth2_authorization",
    "smart_on_fhir",
    "patient_identity_verification",
    "third_party_app_disclosure",
    "audit_logging",
    "tls_encryption",
]

TEFCA_EXCHANGE_PURPOSES = [
    "treatment",
    "payment",
    "healthcare_operations",
    "public_health",
    "benefits_determination",
    "individual_access",
]


def assess_information_blocking_compliance(org_data: dict) -> dict:
    """Assess an organization's information blocking compliance."""
    findings = []
    actor_type = org_data.get("actor_type", "healthcare_provider")
    ehi_practices = org_data.get("ehi_practices", [])
    documented_exceptions = org_data.get("documented_exceptions", [])

    for practice in ehi_practices:
        practice_name = practice.get("name", "Unknown practice")
        interferes_with_access = practice.get("interferes_with_access", False)
        exception_claimed = practice.get("exception_claimed", "")
        exception_documented = practice.get("exception_documented", False)

        if interferes_with_access:
            if not exception_claimed:
                findings.append({
                    "severity": "critical",
                    "finding": f"Practice '{practice_name}' may constitute information blocking: "
                               f"interferes with EHI access/exchange with no exception claimed",
                    "regulation": "21st Century Cures Act §4004",
                    "remediation": "Evaluate practice against information blocking exceptions "
                                   "(45 CFR Part 171) or cease the practice",
                })
            elif exception_claimed not in INFORMATION_BLOCKING_EXCEPTIONS:
                findings.append({
                    "severity": "high",
                    "finding": f"Practice '{practice_name}' claims invalid exception '{exception_claimed}'",
                    "regulation": "45 CFR Part 171",
                    "remediation": "Review and correct exception classification",
                })
            elif not exception_documented:
                findings.append({
                    "severity": "high",
                    "finding": f"Practice '{practice_name}' claims '{exception_claimed}' exception "
                               f"but documentation is incomplete",
                    "regulation": INFORMATION_BLOCKING_EXCEPTIONS[exception_claimed]["cfr"],
                    "remediation": "Complete documentation of factual basis supporting the exception",
                })
            else:
                findings.append({
                    "severity": "info",
                    "finding": f"Practice '{practice_name}' has documented exception: "
                               f"{exception_claimed}",
                    "regulation": INFORMATION_BLOCKING_EXCEPTIONS[exception_claimed]["cfr"],
                    "remediation": "Periodically review whether exception remains justified",
                })

    return {
        "area": "information_blocking",
        "actor_type": actor_type,
        "practices_assessed": len(ehi_practices),
        "findings": findings,
    }


def assess_patient_access_api(api_data: dict) -> dict:
    """Assess Patient Access API compliance."""
    findings = []
    implemented_elements = api_data.get("implemented_elements", [])

    for element in REQUIRED_PATIENT_ACCESS_API_ELEMENTS:
        if element not in implemented_elements:
            severity = "critical" if element in [
                "fhir_r4_endpoint", "patient_identity_verification", "tls_encryption"
            ] else "high"
            findings.append({
                "severity": severity,
                "finding": f"Missing required Patient Access API element: {element}",
                "regulation": "CMS-9115-F §431.60" if element != "tls_encryption"
                              else "45 CFR §164.312(e)(1)",
                "remediation": f"Implement {element} to meet Patient Access API requirements",
            })

    third_party_disclosure = api_data.get("third_party_app_disclosure_text", "")
    if not third_party_disclosure:
        findings.append({
            "severity": "high",
            "finding": "No disclosure notice for patients sharing data with third-party apps",
            "regulation": "CMS-9115-F",
            "remediation": "Implement notice informing patients that data shared with "
                           "third-party apps may not be protected by HIPAA",
        })

    token_expiry_minutes = api_data.get("access_token_expiry_minutes", 0)
    if token_expiry_minutes > 60:
        findings.append({
            "severity": "medium",
            "finding": f"Access token expiry ({token_expiry_minutes} minutes) exceeds "
                       f"recommended 60-minute maximum",
            "regulation": "45 CFR §164.312(a)(1)",
            "remediation": "Reduce access token lifetime to 60 minutes or less with refresh token support",
        })

    return {
        "area": "patient_access_api",
        "elements_implemented": len(implemented_elements),
        "elements_required": len(REQUIRED_PATIENT_ACCESS_API_ELEMENTS),
        "findings": findings,
    }


def assess_tefca_readiness(tefca_data: dict) -> dict:
    """Assess TEFCA participation readiness."""
    findings = []
    supported_purposes = tefca_data.get("supported_exchange_purposes", [])
    qhin_connected = tefca_data.get("qhin_connected", False)
    consent_management = tefca_data.get("consent_management_implemented", False)
    baa_with_qhin = tefca_data.get("baa_with_qhin", False)

    missing_purposes = [p for p in TEFCA_EXCHANGE_PURPOSES if p not in supported_purposes]
    if missing_purposes:
        findings.append({
            "severity": "medium",
            "finding": f"Missing TEFCA exchange purposes: {', '.join(missing_purposes)}",
            "regulation": "TEFCA Common Agreement",
            "remediation": "Implement support for all required exchange purposes",
        })

    if not qhin_connected:
        findings.append({
            "severity": "medium",
            "finding": "Not connected to a Qualified Health Information Network (QHIN)",
            "regulation": "TEFCA Common Agreement",
            "remediation": "Evaluate QHIN options and establish connection",
        })

    if not consent_management:
        findings.append({
            "severity": "high",
            "finding": "Consent management system not implemented for TEFCA exchanges",
            "regulation": "TEFCA Common Agreement + state law requirements",
            "remediation": "Implement consent management supporting opt-in/opt-out and "
                           "sensitive data categories (42 CFR Part 2, state laws)",
        })

    if not baa_with_qhin:
        findings.append({
            "severity": "high",
            "finding": "No BAA executed with QHIN",
            "regulation": "45 CFR §164.502(e)",
            "remediation": "Execute BAA with QHIN before exchanging PHI",
        })

    return {
        "area": "tefca_readiness",
        "qhin_connected": qhin_connected,
        "exchange_purposes_supported": len(supported_purposes),
        "findings": findings,
    }


def generate_interoperability_report(input_data: dict) -> dict:
    """Generate comprehensive interoperability compliance report."""
    organization = input_data.get("organization", "Unknown Organization")

    assessments = []
    if "ehi_practices" in input_data:
        assessments.append(assess_information_blocking_compliance(input_data))
    if "patient_access_api" in input_data:
        assessments.append(assess_patient_access_api(input_data["patient_access_api"]))
    if "tefca" in input_data:
        assessments.append(assess_tefca_readiness(input_data["tefca"]))

    all_findings = []
    for a in assessments:
        all_findings.extend(a["findings"])

    critical = [f for f in all_findings if f["severity"] == "critical"]
    high = [f for f in all_findings if f["severity"] == "high"]

    overall_status = "compliant"
    if critical:
        overall_status = "non_compliant"
    elif high:
        overall_status = "partially_compliant"

    return {
        "report_title": "HIPAA Interoperability Compliance Assessment",
        "organization": organization,
        "report_date": datetime.now().strftime("%Y-%m-%d"),
        "regulatory_framework": [
            "21st Century Cures Act §4004",
            "45 CFR Part 171 (Information Blocking)",
            "CMS-9115-F (Patient Access)",
            "TEFCA Common Agreement",
            "45 CFR Part 164 (HIPAA Privacy and Security Rules)",
        ],
        "overall_status": overall_status,
        "summary": {
            "total_findings": len(all_findings),
            "critical": len(critical),
            "high": len(high),
            "medium": len([f for f in all_findings if f["severity"] == "medium"]),
            "info": len([f for f in all_findings if f["severity"] == "info"]),
        },
        "assessments": assessments,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <interoperability_data.json>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        input_data = json.load(f)

    report = generate_interoperability_report(input_data)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
