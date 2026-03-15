#!/usr/bin/env python3
"""
EU Code of Conduct Adherence Assessment Processor

Evaluates organizational readiness for adhering to an approved EU Code of Conduct
under GDPR Articles 40-41, tracks compliance, and generates adherence documentation.
"""

import json
import os
from datetime import datetime
from typing import Any


GDPR_BENEFITS = {
    "art_24_3": "Element demonstrating controller compliance obligations",
    "art_28_5": "Element demonstrating processor sufficient guarantees",
    "art_32_3": "Element demonstrating security obligation compliance",
    "art_35_8": "Factor in DPIA impact assessment consideration",
    "art_46_2_e": "Appropriate safeguard for international transfers",
    "art_83_2_j": "Mitigating factor for administrative fines",
}

CODE_REQUIREMENT_CATEGORIES = [
    "fair_transparent_processing",
    "legitimate_interests",
    "collection_standards",
    "pseudonymisation",
    "data_subject_information",
    "data_subject_rights",
    "child_protection",
    "technical_organisational_measures",
    "breach_notification",
    "international_transfers",
    "dispute_resolution",
]


def assess_code_adherence(
    organization_name: str,
    code_name: str,
    requirement_assessments: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """
    Assess organization's readiness to adhere to an approved EU Code of Conduct.

    Args:
        organization_name: Name of the organization.
        code_name: Name of the code of conduct.
        requirement_assessments: Dict mapping requirement IDs to assessment data.
            Each value: {'compliant': bool, 'evidence': str, 'gap': str}

    Returns:
        Adherence readiness assessment.
    """
    total = len(requirement_assessments)
    compliant = sum(1 for a in requirement_assessments.values() if a.get("compliant", False))
    non_compliant = total - compliant
    compliance_rate = round(compliant / total * 100, 1) if total > 0 else 0

    if compliance_rate == 100:
        status = "Ready for adherence application"
    elif compliance_rate >= 90:
        status = "Near-ready; minor gaps remain"
    elif compliance_rate >= 70:
        status = "Moderate gaps; targeted remediation needed"
    else:
        status = "Significant gaps; comprehensive remediation required"

    gaps = [
        {
            "requirement_id": req_id,
            "gap": data.get("gap", ""),
            "remediation": data.get("remediation", ""),
        }
        for req_id, data in requirement_assessments.items()
        if not data.get("compliant", False)
    ]

    return {
        "metadata": {
            "organization": organization_name,
            "code": code_name,
            "assessment_date": datetime.now().strftime("%Y-%m-%d"),
            "framework": "GDPR Art. 40-41",
        },
        "summary": {
            "total_requirements": total,
            "compliant": compliant,
            "non_compliant": non_compliant,
            "compliance_rate": compliance_rate,
            "status": status,
        },
        "gaps": gaps,
        "regulatory_benefits": GDPR_BENEFITS,
    }


def generate_adherence_declaration(
    organization_name: str,
    code_name: str,
    monitoring_body: str,
    adherence_date: str,
    scope: str,
) -> dict[str, str]:
    """
    Generate adherence declaration document content.

    Args:
        organization_name: Legal entity name.
        code_name: Approved code of conduct name.
        monitoring_body: Accredited monitoring body name.
        adherence_date: Date of adherence (YYYY-MM-DD).
        scope: Description of processing activities covered.

    Returns:
        Adherence declaration content.
    """
    return {
        "title": f"Declaration of Adherence to {code_name}",
        "organization": organization_name,
        "code": code_name,
        "monitoring_body": monitoring_body,
        "adherence_date": adherence_date,
        "scope": scope,
        "declaration": (
            f"{organization_name} hereby declares its adherence to the {code_name}, "
            f"an approved code of conduct under Article 40 of Regulation (EU) 2016/679 (GDPR). "
            f"This adherence covers the following processing activities: {scope}. "
            f"{organization_name} commits to comply with all requirements of the code and to "
            f"submit to the monitoring and enforcement procedures administered by {monitoring_body}."
        ),
        "commitments": [
            "Comply with all requirements of the code",
            "Submit to periodic compliance assessments by the monitoring body",
            "Cooperate with complaint investigations by the monitoring body",
            "Report material changes in privacy practices within 30 days",
            "Accept enforcement actions including suspension or exclusion for non-compliance",
            "Maintain evidence of compliance for monitoring body review",
        ],
    }


if __name__ == "__main__":
    sample_requirements = {
        f"REQ-{i:03d}": {
            "compliant": i <= 140,
            "evidence": f"Evidence document {i}" if i <= 140 else "",
            "gap": "" if i <= 140 else f"Gap in requirement {i}",
        }
        for i in range(1, 157)
    }

    report = assess_code_adherence(
        "Sentinel Compliance Group",
        "EU Cloud Code of Conduct",
        sample_requirements,
    )
    print(f"Organization: {report['metadata']['organization']}")
    print(f"Code: {report['metadata']['code']}")
    print(f"Compliance Rate: {report['summary']['compliance_rate']}%")
    print(f"Status: {report['summary']['status']}")
    print(f"Gaps: {report['summary']['non_compliant']}")
