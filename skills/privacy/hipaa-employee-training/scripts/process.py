#!/usr/bin/env python3
"""
HIPAA Employee Training Compliance Tracker

Tracks workforce training completion against HIPAA requirements under
45 CFR §164.530(b) and §164.308(a)(5). Evaluates compliance status
per workforce member and generates compliance reports.
"""

import json
import sys
from datetime import datetime, timedelta


REQUIRED_MODULES_TIER1 = [
    "phi_definition",
    "permitted_uses_disclosures",
    "minimum_necessary",
    "patient_rights",
    "breach_identification_reporting",
    "security_basics",
    "social_engineering",
    "sanctions_policy",
]

ROLE_TIER2_MODULES = {
    "clinical": [
        "ehr_access_protocols",
        "verbal_disclosure_rules",
        "patient_identity_verification",
        "break_the_glass_procedures",
    ],
    "administrative": [
        "front_desk_phi_handling",
        "npp_distribution",
        "directory_opt_out",
        "fax_phone_phi_protocols",
    ],
    "him_medical_records": [
        "release_of_information",
        "authorization_validation",
        "minimum_necessary_disclosures",
        "accounting_of_disclosures",
    ],
    "it_technical": [
        "ephi_encryption",
        "access_control_admin",
        "audit_log_management",
        "incident_response",
    ],
    "management": [
        "sanction_administration",
        "workforce_access_reviews",
        "risk_assessment_participation",
        "breach_escalation",
    ],
    "research": [
        "irb_privacy_board_requirements",
        "authorization_vs_waiver",
        "de_identification_methods",
        "limited_data_set_use",
    ],
    "billing": [
        "phi_in_billing_workflows",
        "payer_communications",
        "collections_and_phi",
        "business_associate_interactions",
    ],
}

PASSING_SCORE = 80
ANNUAL_REFRESHER_DAYS = 365
NEW_HIRE_DEADLINE_DAYS = 30


def assess_workforce_member(member: dict) -> dict:
    """Assess a single workforce member's HIPAA training compliance."""
    name = member.get("name", "Unknown")
    role = member.get("role", "administrative")
    hire_date_str = member.get("hire_date", "")
    completed_modules = member.get("completed_modules", [])
    assessment_scores = member.get("assessment_scores", {})
    last_training_date_str = member.get("last_training_date", "")
    policy_change_training = member.get("policy_change_training", [])

    today = datetime.now()
    findings = []
    status = "compliant"

    # Check Tier 1 completion
    missing_tier1 = [m for m in REQUIRED_MODULES_TIER1 if m not in completed_modules]
    if missing_tier1:
        findings.append({
            "severity": "high",
            "finding": f"Missing Tier 1 general training modules: {', '.join(missing_tier1)}",
            "regulation": "45 CFR §164.530(b)(1)",
            "remediation": "Complete missing modules before PHI access is permitted",
        })
        status = "non_compliant"

    # Check Tier 2 role-based completion
    required_tier2 = ROLE_TIER2_MODULES.get(role, [])
    missing_tier2 = [m for m in required_tier2 if m not in completed_modules]
    if missing_tier2:
        findings.append({
            "severity": "medium",
            "finding": f"Missing Tier 2 role-based modules for '{role}': {', '.join(missing_tier2)}",
            "regulation": "45 CFR §164.530(b)(1)",
            "remediation": f"Complete role-specific training for {role} role",
        })
        if status != "non_compliant":
            status = "partially_compliant"

    # Check assessment scores
    for module, score in assessment_scores.items():
        if score < PASSING_SCORE:
            findings.append({
                "severity": "high",
                "finding": f"Failed assessment for module '{module}' with score {score}% (minimum {PASSING_SCORE}%)",
                "regulation": "45 CFR §164.308(a)(5)(i)",
                "remediation": "Remedial training and reassessment required",
            })
            status = "non_compliant"

    # Check new hire training deadline
    if hire_date_str:
        hire_date = datetime.strptime(hire_date_str, "%Y-%m-%d")
        deadline = hire_date + timedelta(days=NEW_HIRE_DEADLINE_DAYS)
        if today > deadline and missing_tier1:
            findings.append({
                "severity": "critical",
                "finding": f"New hire training deadline exceeded. Hired {hire_date_str}, deadline was {deadline.strftime('%Y-%m-%d')}",
                "regulation": "45 CFR §164.530(b)(2)(i)",
                "remediation": "Immediate training required; suspend PHI access until complete",
            })
            status = "non_compliant"

    # Check annual refresher
    if last_training_date_str:
        last_training = datetime.strptime(last_training_date_str, "%Y-%m-%d")
        days_since = (today - last_training).days
        if days_since > ANNUAL_REFRESHER_DAYS:
            findings.append({
                "severity": "medium",
                "finding": f"Annual refresher training overdue by {days_since - ANNUAL_REFRESHER_DAYS} days. Last training: {last_training_date_str}",
                "regulation": "45 CFR §164.308(a)(5)(i)",
                "remediation": "Schedule and complete annual refresher training",
            })
            if status == "compliant":
                status = "partially_compliant"
    else:
        if not missing_tier1:
            findings.append({
                "severity": "low",
                "finding": "No last training date recorded; unable to assess refresher compliance",
                "regulation": "45 CFR §164.530(j)",
                "remediation": "Update training records with completion dates",
            })

    return {
        "workforce_member": name,
        "role": role,
        "compliance_status": status,
        "tier1_complete": len(missing_tier1) == 0,
        "tier2_complete": len(missing_tier2) == 0,
        "findings_count": len(findings),
        "findings": findings,
    }


def generate_training_report(input_data: dict) -> dict:
    """Generate organization-wide training compliance report."""
    organization = input_data.get("organization", "Unknown Organization")
    workforce = input_data.get("workforce_members", [])
    report_date = datetime.now().strftime("%Y-%m-%d")

    assessments = [assess_workforce_member(m) for m in workforce]

    compliant_count = sum(1 for a in assessments if a["compliance_status"] == "compliant")
    partial_count = sum(1 for a in assessments if a["compliance_status"] == "partially_compliant")
    non_compliant_count = sum(1 for a in assessments if a["compliance_status"] == "non_compliant")
    total = len(assessments)

    compliance_rate = (compliant_count / total * 100) if total > 0 else 0

    all_findings = []
    for a in assessments:
        for f in a["findings"]:
            f["workforce_member"] = a["workforce_member"]
            all_findings.append(f)

    critical_findings = [f for f in all_findings if f["severity"] == "critical"]
    high_findings = [f for f in all_findings if f["severity"] == "high"]

    return {
        "report_title": "HIPAA Workforce Training Compliance Report",
        "organization": organization,
        "report_date": report_date,
        "regulatory_basis": [
            "45 CFR §164.530(b) — Privacy Rule Training",
            "45 CFR §164.308(a)(5) — Security Awareness and Training",
        ],
        "summary": {
            "total_workforce_assessed": total,
            "compliant": compliant_count,
            "partially_compliant": partial_count,
            "non_compliant": non_compliant_count,
            "compliance_rate_percent": round(compliance_rate, 1),
        },
        "critical_findings": critical_findings,
        "high_findings": high_findings,
        "individual_assessments": assessments,
        "recommendations": _generate_recommendations(compliance_rate, critical_findings, high_findings),
    }


def _generate_recommendations(compliance_rate, critical_findings, high_findings):
    recommendations = []
    if critical_findings:
        recommendations.append(
            "IMMEDIATE: Suspend PHI access for workforce members with overdue new hire training "
            "until training is completed per §164.530(b)(2)(i)."
        )
    if high_findings:
        recommendations.append(
            "HIGH PRIORITY: Schedule remedial training for workforce members who failed "
            "assessments or are missing required Tier 1 modules."
        )
    if compliance_rate < 95:
        recommendations.append(
            "Implement automated training reminders and escalation to department managers "
            "for non-completers."
        )
    if compliance_rate < 80:
        recommendations.append(
            "Review training delivery methods; consider instructor-led sessions for "
            "departments with low completion rates."
        )
    recommendations.append(
        "Retain all training records for minimum 6 years per §164.530(j)(1)."
    )
    return recommendations


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <workforce_training_data.json>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        input_data = json.load(f)

    report = generate_training_report(input_data)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
