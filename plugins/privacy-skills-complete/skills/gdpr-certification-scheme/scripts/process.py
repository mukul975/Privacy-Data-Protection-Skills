#!/usr/bin/env python3
"""
GDPR Certification Scheme Assessment Processor

Evaluates readiness for GDPR certification under Articles 42-43,
tracks certification criteria compliance, and manages certification lifecycle.
"""

import json
import os
from datetime import datetime, timedelta
from typing import Any


CERTIFICATION_CRITERIA = {
    "C1": {"category": "Lawfulness, Fairness, Transparency", "article": "Art. 5(1)(a)",
           "subcriteria": ["C1.1", "C1.2", "C1.3", "C1.4"]},
    "C2": {"category": "Purpose Limitation", "article": "Art. 5(1)(b)",
           "subcriteria": ["C2.1", "C2.2", "C2.3"]},
    "C3": {"category": "Data Minimisation", "article": "Art. 5(1)(c)",
           "subcriteria": ["C3.1", "C3.2", "C3.3"]},
    "C4": {"category": "Accuracy", "article": "Art. 5(1)(d)",
           "subcriteria": ["C4.1", "C4.2", "C4.3"]},
    "C5": {"category": "Storage Limitation", "article": "Art. 5(1)(e)",
           "subcriteria": ["C5.1", "C5.2", "C5.3"]},
    "C6": {"category": "Integrity and Confidentiality", "article": "Art. 5(1)(f), Art. 32",
           "subcriteria": ["C6.1", "C6.2", "C6.3", "C6.4", "C6.5", "C6.6"]},
    "C7": {"category": "Accountability", "article": "Art. 5(2), Art. 24",
           "subcriteria": ["C7.1", "C7.2", "C7.3", "C7.4", "C7.5", "C7.6"]},
    "C8": {"category": "Data Subject Rights", "article": "Art. 12-22",
           "subcriteria": ["C8.1", "C8.2", "C8.3", "C8.4", "C8.5", "C8.6"]},
    "C9": {"category": "International Transfers", "article": "Art. 44-49",
           "subcriteria": ["C9.1", "C9.2", "C9.3"]},
    "C10": {"category": "Breach Notification", "article": "Art. 33-34",
            "subcriteria": ["C10.1", "C10.2", "C10.3", "C10.4"]},
}


def assess_certification_readiness(
    organization_name: str,
    scheme: str,
    criteria_assessments: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """
    Assess readiness for GDPR certification.

    Args:
        organization_name: Organization name.
        scheme: Certification scheme name.
        criteria_assessments: Dict mapping sub-criteria IDs to assessment data.
            Each: {'met': bool, 'evidence': str, 'gap': str, 'remediation': str}

    Returns:
        Certification readiness assessment.
    """
    category_results = []
    total_subcriteria = 0
    total_met = 0

    for cat_id, cat_info in CERTIFICATION_CRITERIA.items():
        subcriteria = cat_info["subcriteria"]
        met_count = 0

        for sc in subcriteria:
            total_subcriteria += 1
            assessment = criteria_assessments.get(sc, {})
            if assessment.get("met", False):
                met_count += 1
                total_met += 1

        compliance_rate = round(met_count / len(subcriteria) * 100, 1) if subcriteria else 0

        category_results.append({
            "category_id": cat_id,
            "category_name": cat_info["category"],
            "gdpr_article": cat_info["article"],
            "subcriteria_total": len(subcriteria),
            "subcriteria_met": met_count,
            "compliance_rate": compliance_rate,
            "status": "met" if compliance_rate == 100 else "partial" if compliance_rate >= 50 else "not_met",
        })

    overall_rate = round(total_met / total_subcriteria * 100, 1) if total_subcriteria > 0 else 0

    if overall_rate == 100:
        readiness = "Ready for certification audit"
    elif overall_rate >= 90:
        readiness = "Near-ready; minor criteria gaps to address"
    elif overall_rate >= 75:
        readiness = "Moderate gaps; targeted remediation needed"
    else:
        readiness = "Significant preparation required"

    major_nonconformities = [c for c in category_results if c["compliance_rate"] < 50]
    minor_nonconformities = [c for c in category_results if 50 <= c["compliance_rate"] < 100]

    return {
        "metadata": {
            "organization": organization_name,
            "scheme": scheme,
            "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        },
        "summary": {
            "total_criteria": total_subcriteria,
            "criteria_met": total_met,
            "overall_compliance": overall_rate,
            "readiness_level": readiness,
            "major_nonconformities": len(major_nonconformities),
            "minor_nonconformities": len(minor_nonconformities),
        },
        "categories": category_results,
        "gaps": [
            {
                "subcriteria_id": sc_id,
                "gap": data.get("gap", ""),
                "remediation": data.get("remediation", ""),
            }
            for sc_id, data in criteria_assessments.items()
            if not data.get("met", False)
        ],
    }


def calculate_certification_timeline(
    gap_count: int,
    major_nonconformities: int,
) -> dict[str, str]:
    """
    Estimate certification timeline based on gap assessment.

    Args:
        gap_count: Total number of gaps to remediate.
        major_nonconformities: Number of categories with <50% compliance.

    Returns:
        Timeline estimate.
    """
    if gap_count == 0:
        return {
            "self_assessment": "Complete",
            "documentation_review": "4-6 weeks",
            "on_site_audit": "1-2 weeks",
            "certification_decision": "2-4 weeks",
            "total_estimated": "2-3 months",
        }
    elif major_nonconformities == 0:
        remediation_weeks = max(4, gap_count * 2)
        return {
            "remediation": f"{remediation_weeks} weeks",
            "self_assessment": "6-8 weeks",
            "documentation_review": "4-6 weeks",
            "on_site_audit": "1-2 weeks",
            "certification_decision": "2-4 weeks",
            "total_estimated": f"{3 + remediation_weeks // 4}-{6 + remediation_weeks // 4} months",
        }
    else:
        remediation_weeks = max(8, gap_count * 2 + major_nonconformities * 4)
        return {
            "remediation": f"{remediation_weeks} weeks",
            "self_assessment": "6-8 weeks",
            "documentation_review": "4-6 weeks",
            "on_site_audit": "1-2 weeks",
            "certification_decision": "2-4 weeks",
            "total_estimated": f"{6 + remediation_weeks // 4}-{12 + remediation_weeks // 4} months",
        }


def manage_certification_lifecycle(
    certification_date: str,
    validity_years: int = 3,
) -> dict[str, Any]:
    """
    Calculate certification lifecycle dates and milestones.

    Args:
        certification_date: Certification issuance date (YYYY-MM-DD).
        validity_years: Validity period (default 3 years per Art. 42(7)).

    Returns:
        Lifecycle milestones.
    """
    cert_date = datetime.strptime(certification_date, "%Y-%m-%d")
    expiry_date = cert_date + timedelta(days=validity_years * 365)

    return {
        "certification_date": certification_date,
        "expiry_date": expiry_date.strftime("%Y-%m-%d"),
        "milestones": [
            {"event": "Year 1 Surveillance", "date": (cert_date + timedelta(days=365)).strftime("%Y-%m-%d"),
             "preparation_start": (cert_date + timedelta(days=300)).strftime("%Y-%m-%d")},
            {"event": "Year 2 Surveillance", "date": (cert_date + timedelta(days=730)).strftime("%Y-%m-%d"),
             "preparation_start": (cert_date + timedelta(days=665)).strftime("%Y-%m-%d")},
            {"event": "Recertification Audit", "date": (cert_date + timedelta(days=1000)).strftime("%Y-%m-%d"),
             "preparation_start": (cert_date + timedelta(days=910)).strftime("%Y-%m-%d")},
            {"event": "Certificate Expiry", "date": expiry_date.strftime("%Y-%m-%d")},
        ],
    }


if __name__ == "__main__":
    sample_assessments = {}
    for cat_id, cat_info in CERTIFICATION_CRITERIA.items():
        for sc in cat_info["subcriteria"]:
            sample_assessments[sc] = {
                "met": sc not in ["C6.5", "C6.6", "C8.5", "C8.6", "C9.2", "C9.3", "C10.3", "C10.4"],
                "evidence": "Documented and implemented",
                "gap": "" if sc not in ["C6.5", "C6.6", "C8.5", "C8.6", "C9.2", "C9.3", "C10.3", "C10.4"] else "Gap identified",
            }

    report = assess_certification_readiness("Sentinel Compliance Group", "Europrivacy", sample_assessments)
    print(f"Organization: {report['metadata']['organization']}")
    print(f"Scheme: {report['metadata']['scheme']}")
    print(f"Overall Compliance: {report['summary']['overall_compliance']}%")
    print(f"Readiness: {report['summary']['readiness_level']}")
    print(f"Major Nonconformities: {report['summary']['major_nonconformities']}")
    print(f"Gaps: {len(report['gaps'])}")
