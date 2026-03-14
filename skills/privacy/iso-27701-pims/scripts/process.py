#!/usr/bin/env python3
"""
ISO 27701 PIMS Gap Assessment and Certification Readiness Processor

Provides automated gap assessment scoring, SoA generation, and certification
readiness tracking for ISO 27701 PIMS implementation projects.
"""

import json
import os
from datetime import datetime, timedelta
from typing import Any


# ISO 27701 Annex A Controls (PII Controller)
ANNEX_A_CONTROLS = {
    "A.7.2.1": {"title": "Identify and document purpose", "gdpr": "Art. 5(1)(b), Art. 13-14"},
    "A.7.2.2": {"title": "Identify lawful basis", "gdpr": "Art. 6(1), Art. 9(2)"},
    "A.7.2.3": {"title": "Determine when and how consent is to be obtained", "gdpr": "Art. 7"},
    "A.7.2.4": {"title": "Obtain and record consent", "gdpr": "Art. 7(1)"},
    "A.7.2.5": {"title": "Privacy impact assessment", "gdpr": "Art. 35"},
    "A.7.2.6": {"title": "Contracts with PII processors", "gdpr": "Art. 28"},
    "A.7.2.7": {"title": "Joint PII controller", "gdpr": "Art. 26"},
    "A.7.2.8": {"title": "Records related to processing PII", "gdpr": "Art. 30"},
    "A.7.3.1": {"title": "Obligations to PII principals", "gdpr": "Art. 12-22"},
    "A.7.3.2": {"title": "Determining information for PII principals", "gdpr": "Art. 13-14"},
    "A.7.3.3": {"title": "Providing information to PII principals", "gdpr": "Art. 12"},
    "A.7.3.4": {"title": "Mechanism to modify or withdraw consent", "gdpr": "Art. 7(3)"},
    "A.7.3.5": {"title": "Mechanism to object to PII processing", "gdpr": "Art. 21"},
    "A.7.3.6": {"title": "Access, correction and/or erasure", "gdpr": "Art. 15-17"},
    "A.7.3.7": {"title": "Obligations to inform third parties", "gdpr": "Art. 19"},
    "A.7.3.8": {"title": "Providing copy of PII processed", "gdpr": "Art. 15(3), Art. 20"},
    "A.7.3.9": {"title": "Handling requests", "gdpr": "Art. 12(3)-(4)"},
    "A.7.3.10": {"title": "Automated decision making", "gdpr": "Art. 22"},
    "A.7.4.1": {"title": "Limit collection", "gdpr": "Art. 5(1)(c)"},
    "A.7.4.2": {"title": "Limit processing", "gdpr": "Art. 5(1)(b)"},
    "A.7.4.3": {"title": "Accuracy and quality", "gdpr": "Art. 5(1)(d)"},
    "A.7.4.4": {"title": "PII minimization objectives", "gdpr": "Art. 25(2)"},
    "A.7.4.5": {"title": "PII de-identification and deletion at end of processing", "gdpr": "Art. 5(1)(e), Art. 17"},
    "A.7.4.6": {"title": "Temporary files", "gdpr": "Art. 5(1)(e)"},
    "A.7.4.7": {"title": "Retention", "gdpr": "Art. 5(1)(e)"},
    "A.7.4.8": {"title": "Disposal", "gdpr": "Art. 17"},
    "A.7.4.9": {"title": "PII transmission controls", "gdpr": "Art. 32"},
    "A.7.5.1": {"title": "Identify basis for PII transfer between jurisdictions", "gdpr": "Art. 44-49"},
    "A.7.5.2": {"title": "Countries and international organizations for transfer", "gdpr": "Art. 45"},
    "A.7.5.3": {"title": "Records of PII disclosure to third parties", "gdpr": "Art. 30(1)(d)"},
    "A.7.5.4": {"title": "Notification of PII disclosure requests", "gdpr": "Art. 19"},
}

# ISO 27701 Annex B Controls (PII Processor)
ANNEX_B_CONTROLS = {
    "B.8.2.1": {"title": "Customer agreement", "gdpr": "Art. 28(3)"},
    "B.8.2.2": {"title": "Organization's purposes", "gdpr": "Art. 28(3)(a)"},
    "B.8.2.3": {"title": "Marketing and advertising use", "gdpr": "Art. 28(3)(a)"},
    "B.8.2.4": {"title": "Infringing instruction", "gdpr": "Art. 28(3)"},
    "B.8.2.5": {"title": "Customer obligations", "gdpr": "Art. 28(3)"},
    "B.8.2.6": {"title": "Records related to processing PII", "gdpr": "Art. 30(2)"},
    "B.8.3.1": {"title": "Obligations to PII principals", "gdpr": "Art. 28(3)(e)"},
    "B.8.3.2": {"title": "Information for PII principals", "gdpr": "—"},
    "B.8.4.1": {"title": "Temporary files", "gdpr": "Art. 28(3)(g)"},
    "B.8.4.2": {"title": "Return, transfer or disposal of PII", "gdpr": "Art. 28(3)(g)"},
    "B.8.4.3": {"title": "PII transmission controls", "gdpr": "Art. 32"},
    "B.8.5.1": {"title": "Basis for PII transfer between jurisdictions", "gdpr": "Art. 44-49"},
    "B.8.5.2": {"title": "Countries and intl orgs for transfer", "gdpr": "Art. 45, 46"},
    "B.8.5.3": {"title": "Records of PII disclosure to third parties", "gdpr": "Art. 30(2)"},
    "B.8.5.4": {"title": "Notification of PII disclosure requests", "gdpr": "—"},
    "B.8.5.5": {"title": "Legally binding PII disclosures", "gdpr": "Art. 28(3)(a)"},
    "B.8.5.6": {"title": "Disclosure of subcontractors used to process PII", "gdpr": "Art. 28(2)"},
    "B.8.5.7": {"title": "Engagement of a subcontractor to process PII", "gdpr": "Art. 28(2), (4)"},
    "B.8.5.8": {"title": "Change of subcontractor to process PII", "gdpr": "Art. 28(2)"},
}

IMPLEMENTATION_STATUS = {
    "fully_implemented": {"label": "Fully Implemented", "score": 1.0},
    "partially_implemented": {"label": "Partially Implemented", "score": 0.5},
    "not_implemented": {"label": "Not Implemented", "score": 0.0},
    "not_applicable": {"label": "Not Applicable", "score": None},
}


def create_gap_assessment(
    organization_name: str,
    role: str,
    assessments: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """
    Create an ISO 27701 gap assessment report.

    Args:
        organization_name: Name of the organization being assessed.
        role: Organization role - 'controller', 'processor', or 'both'.
        assessments: Dict mapping control IDs to assessment data.
            Each value should contain:
            - status: One of 'fully_implemented', 'partially_implemented',
                      'not_implemented', 'not_applicable'
            - current_state: Description of current implementation
            - gap_description: Description of the gap (if any)
            - remediation_action: Planned remediation (if any)
            - owner: Remediation owner
            - target_date: Target remediation date (YYYY-MM-DD)

    Returns:
        Gap assessment report as a dictionary.
    """
    applicable_controls = {}

    if role in ("controller", "both"):
        applicable_controls.update(ANNEX_A_CONTROLS)
    if role in ("processor", "both"):
        applicable_controls.update(ANNEX_B_CONTROLS)

    results = []
    total_applicable = 0
    total_implemented = 0
    total_partial = 0
    total_not_implemented = 0

    for control_id, control_info in applicable_controls.items():
        assessment = assessments.get(control_id, {})
        status = assessment.get("status", "not_implemented")
        status_info = IMPLEMENTATION_STATUS.get(status, IMPLEMENTATION_STATUS["not_implemented"])

        result = {
            "control_id": control_id,
            "title": control_info["title"],
            "gdpr_mapping": control_info["gdpr"],
            "status": status_info["label"],
            "score": status_info["score"],
            "current_state": assessment.get("current_state", "Not assessed"),
            "gap_description": assessment.get("gap_description", ""),
            "remediation_action": assessment.get("remediation_action", ""),
            "owner": assessment.get("owner", "Unassigned"),
            "target_date": assessment.get("target_date", ""),
        }
        results.append(result)

        if status_info["score"] is not None:
            total_applicable += 1
            if status == "fully_implemented":
                total_implemented += 1
            elif status == "partially_implemented":
                total_partial += 1
            else:
                total_not_implemented += 1

    implementation_rate = (
        (total_implemented + 0.5 * total_partial) / total_applicable * 100
        if total_applicable > 0
        else 0
    )

    report = {
        "metadata": {
            "organization": organization_name,
            "role": role,
            "assessment_date": datetime.now().strftime("%Y-%m-%d"),
            "standard": "ISO/IEC 27701:2019",
            "assessor": "Privacy Audit Team",
        },
        "summary": {
            "total_controls": len(applicable_controls),
            "total_applicable": total_applicable,
            "fully_implemented": total_implemented,
            "partially_implemented": total_partial,
            "not_implemented": total_not_implemented,
            "not_applicable": len(applicable_controls) - total_applicable,
            "implementation_rate": round(implementation_rate, 1),
        },
        "controls": results,
        "gaps": [r for r in results if r["status"] != "Fully Implemented" and r["score"] is not None],
        "remediation_roadmap": generate_remediation_roadmap(
            [r for r in results if r["status"] != "Fully Implemented" and r["score"] is not None]
        ),
    }

    return report


def generate_remediation_roadmap(gaps: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Generate a prioritized remediation roadmap from gap assessment results.

    Args:
        gaps: List of gap dictionaries from the assessment.

    Returns:
        Prioritized remediation items with phases.
    """
    high_priority_prefixes = ["A.7.2", "A.7.3", "B.8.2"]
    medium_priority_prefixes = ["A.7.4", "B.8.4", "B.8.3"]

    roadmap = []
    for gap in gaps:
        control_id = gap["control_id"]
        priority = "low"
        phase = 3

        for prefix in high_priority_prefixes:
            if control_id.startswith(prefix):
                priority = "high"
                phase = 1
                break

        if priority == "low":
            for prefix in medium_priority_prefixes:
                if control_id.startswith(prefix):
                    priority = "medium"
                    phase = 2
                    break

        if gap["status"] == "Not Implemented":
            if priority == "high":
                phase = 1
            elif priority == "medium":
                phase = 2
        elif gap["status"] == "Partially Implemented":
            phase = min(phase, 2)

        roadmap.append({
            "control_id": control_id,
            "title": gap["title"],
            "current_status": gap["status"],
            "priority": priority,
            "phase": phase,
            "remediation_action": gap["remediation_action"],
            "owner": gap["owner"],
            "target_date": gap["target_date"],
        })

    roadmap.sort(key=lambda x: (x["phase"], {"high": 0, "medium": 1, "low": 2}[x["priority"]]))
    return roadmap


def generate_soa_extension(
    role: str,
    assessments: dict[str, dict[str, Any]],
) -> list[dict[str, str]]:
    """
    Generate Statement of Applicability extension entries for ISO 27701 controls.

    Args:
        role: Organization role - 'controller', 'processor', or 'both'.
        assessments: Dict mapping control IDs to assessment data.

    Returns:
        List of SoA entries.
    """
    applicable_controls = {}
    if role in ("controller", "both"):
        applicable_controls.update(ANNEX_A_CONTROLS)
    if role in ("processor", "both"):
        applicable_controls.update(ANNEX_B_CONTROLS)

    soa_entries = []
    for control_id, control_info in applicable_controls.items():
        assessment = assessments.get(control_id, {})
        status = assessment.get("status", "not_implemented")

        applicable = status != "not_applicable"
        justification = assessment.get("justification", "")

        if not applicable and not justification:
            justification = "Processing activity not performed by the organization"

        soa_entries.append({
            "control_id": control_id,
            "control_title": control_info["title"],
            "gdpr_reference": control_info["gdpr"],
            "applicable": "Yes" if applicable else "No",
            "implementation_status": IMPLEMENTATION_STATUS.get(status, {}).get("label", "Unknown"),
            "implementation_description": assessment.get("current_state", ""),
            "justification_for_exclusion": justification if not applicable else "",
        })

    return soa_entries


def calculate_certification_readiness(
    gap_report: dict[str, Any],
    internal_audit_complete: bool = False,
    management_review_complete: bool = False,
    corrective_actions_closed: bool = False,
) -> dict[str, Any]:
    """
    Calculate certification readiness score based on gap assessment and prerequisites.

    Args:
        gap_report: Gap assessment report from create_gap_assessment().
        internal_audit_complete: Whether PIMS internal audit has been completed.
        management_review_complete: Whether PIMS management review has been completed.
        corrective_actions_closed: Whether all major corrective actions are closed.

    Returns:
        Certification readiness assessment.
    """
    implementation_score = gap_report["summary"]["implementation_rate"]

    prerequisite_score = 0
    prerequisites = {
        "internal_audit": internal_audit_complete,
        "management_review": management_review_complete,
        "corrective_actions": corrective_actions_closed,
    }
    for _name, completed in prerequisites.items():
        if completed:
            prerequisite_score += 33.3

    overall_readiness = (implementation_score * 0.7) + (min(prerequisite_score, 100) * 0.3)

    if overall_readiness >= 90:
        recommendation = "Ready for Stage 1 certification audit"
        timeline = "Schedule Stage 1 within 4-6 weeks"
    elif overall_readiness >= 75:
        recommendation = "Near-ready; address remaining gaps before scheduling"
        timeline = "Estimated 2-3 months to readiness"
    elif overall_readiness >= 50:
        recommendation = "Significant work remaining; continue implementation"
        timeline = "Estimated 4-6 months to readiness"
    else:
        recommendation = "Early stages; focus on foundational controls"
        timeline = "Estimated 6-12 months to readiness"

    return {
        "implementation_readiness": round(implementation_score, 1),
        "prerequisite_readiness": round(min(prerequisite_score, 100), 1),
        "overall_readiness": round(overall_readiness, 1),
        "prerequisites": {
            "internal_audit_complete": internal_audit_complete,
            "management_review_complete": management_review_complete,
            "corrective_actions_closed": corrective_actions_closed,
        },
        "recommendation": recommendation,
        "estimated_timeline": timeline,
        "gaps_requiring_remediation": gap_report["summary"]["not_implemented"]
        + gap_report["summary"]["partially_implemented"],
    }


def export_gap_report(report: dict[str, Any], output_path: str) -> str:
    """
    Export gap assessment report to JSON file.

    Args:
        report: Gap assessment report dictionary.
        output_path: File path for the output JSON.

    Returns:
        Path to the exported file.
    """
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    return output_path


if __name__ == "__main__":
    sample_assessments = {
        "A.7.2.1": {
            "status": "partially_implemented",
            "current_state": "Purposes documented in privacy notice but not in processing register",
            "gap_description": "Processing register lacks specific purpose documentation per activity",
            "remediation_action": "Update processing register template, populate for all activities",
            "owner": "Data Protection Officer",
            "target_date": "2025-06-30",
        },
        "A.7.2.2": {
            "status": "fully_implemented",
            "current_state": "Lawful basis documented for all processing activities in RoPA",
        },
        "A.7.2.5": {
            "status": "partially_implemented",
            "current_state": "DPIAs conducted for major projects only",
            "gap_description": "No systematic DPIA threshold assessment for all processing changes",
            "remediation_action": "Implement PTA process for all new/changed processing",
            "owner": "Privacy Operations Manager",
            "target_date": "2025-05-31",
        },
        "A.7.3.1": {
            "status": "fully_implemented",
            "current_state": "DSAR procedures documented and operational with SLA tracking",
        },
    }

    report = create_gap_assessment(
        organization_name="Sentinel Compliance Group",
        role="both",
        assessments=sample_assessments,
    )

    print(f"Organization: {report['metadata']['organization']}")
    print(f"Assessment Date: {report['metadata']['assessment_date']}")
    print(f"Role: {report['metadata']['role']}")
    print(f"\nSummary:")
    print(f"  Total Controls: {report['summary']['total_controls']}")
    print(f"  Fully Implemented: {report['summary']['fully_implemented']}")
    print(f"  Partially Implemented: {report['summary']['partially_implemented']}")
    print(f"  Not Implemented: {report['summary']['not_implemented']}")
    print(f"  Implementation Rate: {report['summary']['implementation_rate']}%")
    print(f"\nGaps Found: {len(report['gaps'])}")
    print(f"Remediation Items: {len(report['remediation_roadmap'])}")

    readiness = calculate_certification_readiness(
        gap_report=report,
        internal_audit_complete=True,
        management_review_complete=True,
        corrective_actions_closed=False,
    )
    print(f"\nCertification Readiness:")
    print(f"  Implementation: {readiness['implementation_readiness']}%")
    print(f"  Prerequisites: {readiness['prerequisite_readiness']}%")
    print(f"  Overall: {readiness['overall_readiness']}%")
    print(f"  Recommendation: {readiness['recommendation']}")
    print(f"  Timeline: {readiness['estimated_timeline']}")
