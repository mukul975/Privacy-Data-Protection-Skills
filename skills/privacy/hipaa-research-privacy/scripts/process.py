#!/usr/bin/env python3
"""
HIPAA Research Privacy Compliance Assessment Tool

Evaluates research PHI access pathways for compliance with HIPAA Privacy
Rule research provisions under 45 CFR §164.512(i), §164.508, and §164.514.
"""

import json
import sys
from datetime import datetime


AUTHORIZATION_REQUIRED_ELEMENTS = [
    "phi_description",
    "authorized_discloser",
    "authorized_recipient",
    "purpose_description",
    "expiration_date_or_event",
    "right_to_revoke_statement",
    "redisclosure_warning",
    "signature_and_date",
]

WAIVER_CRITERIA = [
    "minimal_risk_to_privacy",
    "could_not_practicably_conduct_without_waiver",
    "could_not_practicably_conduct_without_phi",
]

WAIVER_DOCUMENTATION_ELEMENTS = [
    "irb_or_privacy_board_identification",
    "statement_criteria_satisfied",
    "phi_description",
    "chair_signature",
    "approval_date",
]

DUA_REQUIRED_ELEMENTS = [
    "permitted_uses_and_disclosures",
    "authorized_users_identified",
    "prohibition_on_reidentification",
    "prohibition_on_contacting_individuals",
    "adequate_safeguards_commitment",
    "violation_reporting_procedure",
]


def assess_authorization(auth_data: dict) -> dict:
    """Assess a HIPAA research authorization for compliance."""
    findings = []
    elements_present = auth_data.get("elements_present", [])

    missing = [e for e in AUTHORIZATION_REQUIRED_ELEMENTS if e not in elements_present]
    if missing:
        findings.append({
            "severity": "critical",
            "finding": f"Authorization missing required elements: {', '.join(missing)}",
            "regulation": "45 CFR §164.508(c)",
            "remediation": "Add missing elements to authorization form before obtaining signatures",
        })

    compound_authorization = auth_data.get("compound_authorization", False)
    conditioned_on_research = auth_data.get("conditioned_on_research_participation", False)
    if compound_authorization and not auth_data.get("research_clearly_distinguishable", True):
        findings.append({
            "severity": "high",
            "finding": "Combined consent/authorization does not clearly distinguish the authorization portion",
            "regulation": "45 CFR §164.508(b)(3)(i)",
            "remediation": "Ensure authorization portion is clearly marked and distinguishable from informed consent",
        })

    if conditioned_on_research:
        findings.append({
            "severity": "info",
            "finding": "Authorization is conditioned on research participation — permitted per §164.508(b)(4)(i)",
            "regulation": "45 CFR §164.508(b)(4)(i)",
            "remediation": "No action needed; conditioning permitted for research",
        })

    status = "compliant"
    if any(f["severity"] == "critical" for f in findings):
        status = "non_compliant"
    elif any(f["severity"] == "high" for f in findings):
        status = "partially_compliant"

    return {
        "pathway": "individual_authorization",
        "compliance_status": status,
        "findings": findings,
    }


def assess_waiver(waiver_data: dict) -> dict:
    """Assess an IRB/Privacy Board waiver of authorization."""
    findings = []
    criteria_met = waiver_data.get("criteria_met", [])
    documentation = waiver_data.get("documentation_elements", [])
    identifier_destruction_plan = waiver_data.get("identifier_destruction_plan", False)
    no_reuse_assurances = waiver_data.get("no_reuse_assurances", False)

    missing_criteria = [c for c in WAIVER_CRITERIA if c not in criteria_met]
    if missing_criteria:
        findings.append({
            "severity": "critical",
            "finding": f"IRB/Privacy Board waiver missing required criteria: {', '.join(missing_criteria)}",
            "regulation": "45 CFR §164.512(i)(1)(i)",
            "remediation": "IRB/Privacy Board must document that all three waiver criteria are satisfied",
        })

    missing_docs = [d for d in WAIVER_DOCUMENTATION_ELEMENTS if d not in documentation]
    if missing_docs:
        findings.append({
            "severity": "high",
            "finding": f"Waiver documentation missing required elements: {', '.join(missing_docs)}",
            "regulation": "45 CFR §164.512(i)(2)",
            "remediation": "Obtain complete waiver documentation from IRB/Privacy Board",
        })

    if not identifier_destruction_plan:
        findings.append({
            "severity": "high",
            "finding": "No plan to destroy identifiers at the earliest opportunity",
            "regulation": "45 CFR §164.512(i)(1)(i)(A)(2)",
            "remediation": "Document plan for identifier destruction or provide health/research justification for retention",
        })

    if not no_reuse_assurances:
        findings.append({
            "severity": "high",
            "finding": "No written assurances that PHI will not be reused or redisclosed",
            "regulation": "45 CFR §164.512(i)(1)(i)(A)(3)",
            "remediation": "Obtain written assurances from researcher regarding reuse/redisclosure restrictions",
        })

    status = "compliant"
    if any(f["severity"] == "critical" for f in findings):
        status = "non_compliant"
    elif any(f["severity"] == "high" for f in findings):
        status = "partially_compliant"

    return {
        "pathway": "irb_waiver_of_authorization",
        "compliance_status": status,
        "findings": findings,
    }


def assess_limited_data_set(lds_data: dict) -> dict:
    """Assess limited data set and data use agreement compliance."""
    findings = []
    dua_elements = lds_data.get("dua_elements_present", [])
    direct_identifiers_removed = lds_data.get("direct_identifiers_removed", [])

    required_removals = [
        "names", "postal_address_other_than_town_city_state_zip",
        "phone_numbers", "fax_numbers", "email_addresses", "ssn",
        "medical_record_numbers", "health_plan_beneficiary_numbers",
        "account_numbers", "certificate_license_numbers",
        "vehicle_identifiers", "device_identifiers", "web_urls",
        "ip_addresses", "biometric_identifiers", "full_face_photos",
    ]

    not_removed = [i for i in required_removals if i not in direct_identifiers_removed]
    if not_removed:
        findings.append({
            "severity": "critical",
            "finding": f"Limited data set retains direct identifiers that must be removed: {', '.join(not_removed)}",
            "regulation": "45 CFR §164.514(e)(2)",
            "remediation": "Remove all 16 direct identifiers specified in §164.514(e)(2)",
        })

    missing_dua = [e for e in DUA_REQUIRED_ELEMENTS if e not in dua_elements]
    if missing_dua:
        findings.append({
            "severity": "high",
            "finding": f"Data use agreement missing required elements: {', '.join(missing_dua)}",
            "regulation": "45 CFR §164.514(e)(4)",
            "remediation": "Execute compliant data use agreement before disclosing limited data set",
        })

    status = "compliant"
    if any(f["severity"] == "critical" for f in findings):
        status = "non_compliant"
    elif any(f["severity"] == "high" for f in findings):
        status = "partially_compliant"

    return {
        "pathway": "limited_data_set",
        "compliance_status": status,
        "findings": findings,
    }


def generate_research_privacy_report(input_data: dict) -> dict:
    """Generate comprehensive research privacy compliance report."""
    organization = input_data.get("organization", "Unknown Organization")
    research_studies = input_data.get("research_studies", [])

    study_assessments = []
    for study in research_studies:
        study_name = study.get("study_name", "Unknown Study")
        pathway = study.get("pathway", "")

        if pathway == "authorization":
            assessment = assess_authorization(study.get("authorization_data", {}))
        elif pathway == "irb_waiver":
            assessment = assess_waiver(study.get("waiver_data", {}))
        elif pathway == "limited_data_set":
            assessment = assess_limited_data_set(study.get("lds_data", {}))
        elif pathway == "de_identified":
            assessment = {
                "pathway": "de_identified",
                "compliance_status": "compliant",
                "findings": [{
                    "severity": "info",
                    "finding": "Using de-identified data; HIPAA restrictions do not apply",
                    "regulation": "45 CFR §164.514(a)",
                    "remediation": "Verify de-identification method (Safe Harbor or Expert Determination) is properly documented",
                }],
            }
        elif pathway == "preparatory":
            representations = study.get("preparatory_representations", {})
            assessment = {
                "pathway": "preparatory_to_research",
                "compliance_status": "compliant" if all([
                    representations.get("solely_to_prepare_protocol"),
                    representations.get("no_phi_removed"),
                    representations.get("phi_necessary"),
                ]) else "non_compliant",
                "findings": [],
            }
            if not representations.get("solely_to_prepare_protocol"):
                assessment["findings"].append({
                    "severity": "critical",
                    "finding": "Missing representation that access is solely preparatory",
                    "regulation": "45 CFR §164.512(i)(1)(ii)(A)",
                    "remediation": "Obtain written representation from researcher",
                })
            if not representations.get("no_phi_removed"):
                assessment["findings"].append({
                    "severity": "critical",
                    "finding": "Missing representation that no PHI will be removed",
                    "regulation": "45 CFR §164.512(i)(1)(ii)(B)",
                    "remediation": "Obtain written representation; ensure no export/copy capabilities",
                })
            if not representations.get("phi_necessary"):
                assessment["findings"].append({
                    "severity": "high",
                    "finding": "Missing representation that PHI is necessary for research purposes",
                    "regulation": "45 CFR §164.512(i)(1)(ii)(C)",
                    "remediation": "Obtain written representation documenting necessity",
                })
        else:
            assessment = {
                "pathway": "unknown",
                "compliance_status": "non_compliant",
                "findings": [{
                    "severity": "critical",
                    "finding": f"Unknown or undocumented PHI access pathway: '{pathway}'",
                    "regulation": "45 CFR §164.512(i)",
                    "remediation": "Identify and document a valid HIPAA pathway for research PHI access",
                }],
            }

        assessment["study_name"] = study_name
        study_assessments.append(assessment)

    all_findings = []
    for sa in study_assessments:
        for f in sa["findings"]:
            f["study"] = sa["study_name"]
            all_findings.append(f)

    return {
        "report_title": "HIPAA Research Privacy Compliance Report",
        "organization": organization,
        "report_date": datetime.now().strftime("%Y-%m-%d"),
        "regulatory_basis": [
            "45 CFR §164.512(i) — Research Uses and Disclosures",
            "45 CFR §164.508 — Authorization",
            "45 CFR §164.514(e) — Limited Data Set",
        ],
        "summary": {
            "studies_assessed": len(study_assessments),
            "compliant": sum(1 for s in study_assessments if s["compliance_status"] == "compliant"),
            "partially_compliant": sum(1 for s in study_assessments if s["compliance_status"] == "partially_compliant"),
            "non_compliant": sum(1 for s in study_assessments if s["compliance_status"] == "non_compliant"),
            "total_findings": len(all_findings),
            "critical_findings": len([f for f in all_findings if f["severity"] == "critical"]),
        },
        "study_assessments": study_assessments,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <research_privacy_data.json>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        input_data = json.load(f)

    report = generate_research_privacy_report(input_data)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
