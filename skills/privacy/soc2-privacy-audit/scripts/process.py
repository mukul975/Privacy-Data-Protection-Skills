#!/usr/bin/env python3
"""
SOC 2 Privacy TSC Readiness Assessment Processor

Evaluates organizational readiness against SOC 2 Privacy Trust Services Criteria
P1.0 through P8.1, tracks evidence collection, and generates readiness reports.
"""

import json
import os
from datetime import datetime
from typing import Any

# SOC 2 Privacy Trust Services Criteria
PRIVACY_CRITERIA = {
    "P1.1": {
        "category": "Notice",
        "description": "The entity provides notice to data subjects about its privacy practices",
        "key_controls": [
            "Privacy notice published on all collection points",
            "Privacy notice describes data types, purposes, recipients, rights, retention",
            "Privacy notice reviewed and updated annually",
            "Material changes communicated to data subjects",
        ],
    },
    "P1.2": {
        "category": "Choice and Consent",
        "description": "The entity communicates choices available regarding collection, use, retention, disclosure, and disposal",
        "key_controls": [
            "Consent obtained prior to or at time of collection",
            "Data subjects informed of consequences of refusal",
            "Opt-out mechanisms for marketing and non-essential processing",
            "Explicit consent for sensitive personal information",
            "Consent withdrawal mechanisms available",
        ],
    },
    "P2.1": {
        "category": "Collection",
        "description": "Personal information is collected consistent with objectives related to privacy",
        "key_controls": [
            "Collection limited to information described in privacy notice",
            "Collection points inventoried and reviewed quarterly",
            "Third-party data sources documented with due diligence",
            "Implicit collection disclosed in privacy notice",
        ],
    },
    "P3.1": {
        "category": "Use, Retention, and Disposal",
        "description": "Personal information is used, retained, and disposed consistent with objectives",
        "key_controls": [
            "Personal information used only for purposes in privacy notice",
            "Retention schedules defined per data category",
            "Automated deletion or anonymization upon expiry",
            "Disposal ensures unrecoverability (NIST SP 800-88)",
            "Retention exceptions documented and time-bound",
        ],
    },
    "P4.1": {
        "category": "Access",
        "description": "The entity provides data subjects access to their personal information",
        "key_controls": [
            "DSAR intake mechanism available",
            "Identity verification before fulfillment",
            "Access requests fulfilled within documented timeframes",
            "Data subjects can request corrections",
            "Denials documented with reasons",
        ],
    },
    "P5.1": {
        "category": "Disclosure to Third Parties",
        "description": "Personal information disclosed to third parties only for identified purposes",
        "key_controls": [
            "Third-party recipients identified and documented",
            "DPAs in place with all third parties",
            "Disclosures consistent with privacy notice",
            "Third parties assessed for adequate controls",
            "Unauthorized disclosures reported and investigated",
        ],
    },
    "P6.1": {
        "category": "Security for Privacy",
        "description": "Personal information protected against unauthorized access",
        "key_controls": [
            "Encryption at rest (AES-256 or equivalent)",
            "Encryption in transit (TLS 1.2+)",
            "Role-based access controls",
            "Access logging with retention",
            "Privacy-impacting incidents trigger breach notification",
        ],
    },
    "P7.1": {
        "category": "Quality",
        "description": "Personal information maintained accurately, completely, and timely",
        "key_controls": [
            "Data quality validation at collection",
            "Correction mechanism available",
            "Periodic accuracy reviews",
        ],
    },
    "P8.1": {
        "category": "Monitoring and Enforcement",
        "description": "Entity monitors compliance and addresses privacy inquiries and complaints",
        "key_controls": [
            "Privacy compliance monitoring at minimum quarterly",
            "Privacy complaint intake mechanism available",
            "Complaints tracked and resolved within timeframes",
            "Employees trained at onboarding and annually",
            "Disciplinary actions for violations",
        ],
    },
}


def assess_privacy_readiness(
    organization_name: str,
    control_assessments: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """
    Assess SOC 2 Privacy TSC readiness.

    Args:
        organization_name: Name of the organization.
        control_assessments: Dict mapping criterion IDs to assessment data.
            Each value should contain:
            - controls: List of dicts with 'description', 'implemented' (bool),
                       'evidence_available' (bool), 'evidence_type' (str)
            - overall_status: 'ready', 'partial', 'not_ready'

    Returns:
        Readiness assessment report.
    """
    criteria_results = []
    total_ready = 0
    total_partial = 0
    total_not_ready = 0

    for criterion_id, criterion_info in PRIVACY_CRITERIA.items():
        assessment = control_assessments.get(criterion_id, {})
        status = assessment.get("overall_status", "not_ready")
        controls = assessment.get("controls", [])

        controls_implemented = sum(1 for c in controls if c.get("implemented", False))
        controls_with_evidence = sum(1 for c in controls if c.get("evidence_available", False))
        total_controls = len(criterion_info["key_controls"])

        if status == "ready":
            total_ready += 1
            score = 100
        elif status == "partial":
            total_partial += 1
            score = int((controls_implemented / max(total_controls, 1)) * 100)
        else:
            total_not_ready += 1
            score = 0

        criteria_results.append({
            "criterion_id": criterion_id,
            "category": criterion_info["category"],
            "description": criterion_info["description"],
            "status": status,
            "score": score,
            "controls_required": total_controls,
            "controls_implemented": controls_implemented,
            "controls_with_evidence": controls_with_evidence,
            "gaps": [
                kc
                for i, kc in enumerate(criterion_info["key_controls"])
                if i >= len(controls) or not controls[i].get("implemented", False)
            ],
        })

    total_criteria = len(PRIVACY_CRITERIA)
    overall_score = int(
        (total_ready * 100 + total_partial * 50) / total_criteria
    )

    if overall_score >= 90:
        readiness_level = "Ready for examination"
    elif overall_score >= 70:
        readiness_level = "Near-ready with minor gaps"
    elif overall_score >= 50:
        readiness_level = "Significant preparation needed"
    else:
        readiness_level = "Not ready — foundational controls missing"

    return {
        "metadata": {
            "organization": organization_name,
            "assessment_date": datetime.now().strftime("%Y-%m-%d"),
            "framework": "SOC 2 Type II — Privacy TSC",
            "criteria_version": "TSP Section 100 (2017)",
        },
        "summary": {
            "total_criteria": total_criteria,
            "ready": total_ready,
            "partial": total_partial,
            "not_ready": total_not_ready,
            "overall_score": overall_score,
            "readiness_level": readiness_level,
        },
        "criteria_results": criteria_results,
        "priority_gaps": [
            {
                "criterion": r["criterion_id"],
                "category": r["category"],
                "gaps": r["gaps"],
            }
            for r in criteria_results
            if r["status"] != "ready" and r["gaps"]
        ],
    }


def generate_evidence_checklist(
    examination_period_start: str,
    examination_period_end: str,
) -> list[dict[str, Any]]:
    """
    Generate an evidence collection checklist for the SOC 2 Privacy examination period.

    Args:
        examination_period_start: Start date (YYYY-MM-DD).
        examination_period_end: End date (YYYY-MM-DD).

    Returns:
        List of evidence items with collection schedule.
    """
    evidence_items = []

    for criterion_id, criterion_info in PRIVACY_CRITERIA.items():
        for control in criterion_info["key_controls"]:
            evidence_items.append({
                "criterion_id": criterion_id,
                "category": criterion_info["category"],
                "control": control,
                "evidence_types": ["documentation", "screenshot", "log_extract"],
                "collection_frequency": "monthly" if "log" in control.lower() or "record" in control.lower() else "quarterly",
                "examination_period": f"{examination_period_start} to {examination_period_end}",
                "status": "pending",
                "owner": "",
                "notes": "",
            })

    return evidence_items


def calculate_sample_sizes(
    examination_period_months: int,
    populations: dict[str, int],
) -> dict[str, dict[str, int]]:
    """
    Calculate audit sample sizes based on population and examination period.

    Args:
        examination_period_months: Length of examination period in months.
        populations: Dict mapping population names to sizes.

    Returns:
        Dict mapping population names to sample size recommendations.
    """
    results = {}

    for name, size in populations.items():
        if size <= 0:
            results[name] = {"population": size, "sample": 0, "method": "N/A"}
            continue

        if examination_period_months <= 6:
            if size <= 50:
                sample = size
            elif size <= 250:
                sample = 25
            else:
                sample = 40
        else:
            if size <= 50:
                sample = size
            elif size <= 250:
                sample = 30
            else:
                sample = 45

        method = "all items" if sample == size else "attribute sampling"
        results[name] = {
            "population": size,
            "sample": sample,
            "method": method,
        }

    return results


def export_readiness_report(report: dict[str, Any], output_path: str) -> str:
    """Export readiness report to JSON."""
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    return output_path


if __name__ == "__main__":
    sample_assessments = {
        "P1.1": {
            "overall_status": "ready",
            "controls": [
                {"description": "Privacy notice published", "implemented": True, "evidence_available": True},
                {"description": "Notice describes all required elements", "implemented": True, "evidence_available": True},
                {"description": "Annual review conducted", "implemented": True, "evidence_available": True},
                {"description": "Change communication process", "implemented": True, "evidence_available": True},
            ],
        },
        "P1.2": {
            "overall_status": "partial",
            "controls": [
                {"description": "Consent at collection", "implemented": True, "evidence_available": True},
                {"description": "Consequence disclosure", "implemented": True, "evidence_available": False},
                {"description": "Opt-out mechanisms", "implemented": True, "evidence_available": True},
                {"description": "Explicit consent for sensitive", "implemented": False, "evidence_available": False},
                {"description": "Withdrawal mechanisms", "implemented": True, "evidence_available": True},
            ],
        },
        "P4.1": {
            "overall_status": "ready",
            "controls": [
                {"description": "DSAR intake", "implemented": True, "evidence_available": True},
                {"description": "Identity verification", "implemented": True, "evidence_available": True},
                {"description": "Timely fulfillment", "implemented": True, "evidence_available": True},
                {"description": "Correction mechanism", "implemented": True, "evidence_available": True},
                {"description": "Denial documentation", "implemented": True, "evidence_available": True},
            ],
        },
    }

    report = assess_privacy_readiness("Sentinel Compliance Group", sample_assessments)

    print(f"Organization: {report['metadata']['organization']}")
    print(f"Overall Score: {report['summary']['overall_score']}%")
    print(f"Readiness: {report['summary']['readiness_level']}")
    print(f"Ready: {report['summary']['ready']}/{report['summary']['total_criteria']}")

    samples = calculate_sample_sizes(12, {
        "DSARs": 847,
        "Consent records": 15000,
        "DPAs": 47,
        "Deletion records": 320,
        "Complaints": 12,
    })
    print("\nSample Sizes:")
    for name, info in samples.items():
        print(f"  {name}: {info['sample']} of {info['population']} ({info['method']})")
