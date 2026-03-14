#!/usr/bin/env python3
"""Employee Surveillance Privacy Assessment Engine.

Implements DPIA methodology for workplace monitoring systems including
proportionality scoring, Barbulescu criteria assessment, and monitoring
type-specific risk analysis.
"""

import json
from datetime import datetime, timedelta
from typing import Any

MONITORING_TYPES = {
    "email_metadata": {
        "name": "Email Metadata Monitoring",
        "intrusiveness": 2,
        "description": "Monitoring of email sender, recipient, timestamp, and subject line without content access",
        "typical_purposes": ["Regulatory compliance", "Insider threat detection", "eDiscovery preparedness"],
    },
    "email_content": {
        "name": "Email Content Monitoring",
        "intrusiveness": 4,
        "description": "Scanning or accessing the body content of employee emails",
        "typical_purposes": ["DLP enforcement", "Harassment investigation", "Regulatory compliance"],
    },
    "internet_category": {
        "name": "Internet Usage Category Monitoring",
        "intrusiveness": 2,
        "description": "Classification of web browsing into categories without URL-level logging",
        "typical_purposes": ["Acceptable use enforcement", "Bandwidth management", "Malware prevention"],
    },
    "internet_url": {
        "name": "Internet URL-Level Monitoring",
        "intrusiveness": 3,
        "description": "Logging of specific URLs visited by employees",
        "typical_purposes": ["Security incident investigation", "DLP enforcement"],
    },
    "cctv_common": {
        "name": "CCTV in Common Areas",
        "intrusiveness": 2,
        "description": "Video surveillance in reception, corridors, and common workspaces",
        "typical_purposes": ["Physical security", "Health and safety", "Theft prevention"],
    },
    "cctv_workstation": {
        "name": "CCTV at Individual Workstations",
        "intrusiveness": 4,
        "description": "Video surveillance directed at individual employee workstations",
        "typical_purposes": ["Fraud detection", "Cash handling oversight"],
    },
    "gps_vehicle": {
        "name": "GPS Vehicle Tracking",
        "intrusiveness": 3,
        "description": "GPS tracking of company vehicles during working hours",
        "typical_purposes": ["Fleet management", "Route optimisation", "Vehicle theft prevention"],
    },
    "gps_personnel": {
        "name": "GPS Personnel Tracking",
        "intrusiveness": 4,
        "description": "Location tracking of individual employees via mobile device or wearable",
        "typical_purposes": ["Lone worker safety", "Field service management"],
    },
    "keystroke": {
        "name": "Keystroke Logging",
        "intrusiveness": 5,
        "description": "Recording of all keystrokes typed by employees",
        "typical_purposes": ["Insider threat detection (high-security environments)", "Fraud investigation"],
    },
    "screen_capture": {
        "name": "Screen Capture/Recording",
        "intrusiveness": 5,
        "description": "Periodic or continuous screenshots or screen recording of employee desktops",
        "typical_purposes": ["Insider threat detection", "Compliance monitoring"],
    },
}

BARBULESCU_CRITERIA = [
    {
        "id": "BC1",
        "name": "Prior notification",
        "question": "Has the employee been notified in advance of the possibility and scope of monitoring?",
    },
    {
        "id": "BC2",
        "name": "Extent of monitoring",
        "question": "What is the extent of the monitoring and the degree of intrusion into the employee's privacy?",
    },
    {
        "id": "BC3",
        "name": "Legitimate reasons",
        "question": "Has the employer provided legitimate reasons to justify monitoring and accessing the content?",
    },
    {
        "id": "BC4",
        "name": "Less intrusive methods",
        "question": "Would it have been possible to establish a monitoring system based on less intrusive methods?",
    },
    {
        "id": "BC5",
        "name": "Consequences for employee",
        "question": "What are the consequences of monitoring for the employee subjected to it?",
    },
    {
        "id": "BC6",
        "name": "Adequate safeguards",
        "question": "Has the employee been provided with adequate safeguards, especially when monitoring is intrusive?",
    },
]


def assess_monitoring_proportionality(
    monitoring_type: str,
    purpose: str,
    scope: str,
    employee_count: int,
    alternatives_considered: list[str],
    private_use_permitted: bool,
    retention_days: int,
) -> dict[str, Any]:
    """Assess proportionality of an employee monitoring measure.

    Args:
        monitoring_type: Key from MONITORING_TYPES
        purpose: Stated purpose of monitoring
        scope: Scope description (all employees, specific roles, etc.)
        employee_count: Number of employees affected
        alternatives_considered: List of less intrusive alternatives evaluated
        private_use_permitted: Whether private use of the monitored system is permitted
        retention_days: Monitoring data retention period in days

    Returns:
        Proportionality assessment
    """
    mon_info = MONITORING_TYPES.get(monitoring_type)
    if not mon_info:
        return {"error": f"Unknown monitoring type: {monitoring_type}"}

    issues = []

    if mon_info["intrusiveness"] >= 4 and len(alternatives_considered) < 2:
        issues.append(
            "Highly intrusive monitoring requires thorough evaluation of less "
            "intrusive alternatives. At least two alternatives should be documented."
        )

    if private_use_permitted and mon_info["intrusiveness"] >= 3:
        issues.append(
            "Private use is permitted but monitoring is intrusive. Personal "
            "communications and browsing may be captured. Implement technical "
            "measures to exclude personal activity from monitoring."
        )

    if retention_days > 90 and mon_info["intrusiveness"] >= 3:
        issues.append(
            f"Retention of {retention_days} days is potentially excessive for "
            f"monitoring data with intrusiveness level {mon_info['intrusiveness']}/5. "
            "Consider reducing retention to 30-90 days."
        )

    if scope.lower() in ("all employees", "blanket", "company-wide") and mon_info["intrusiveness"] >= 3:
        issues.append(
            "Blanket monitoring of all employees with intrusive technology is "
            "generally disproportionate. Target monitoring to specific roles or risk areas."
        )

    proportionate = len(issues) == 0

    return {
        "monitoring_type": mon_info["name"],
        "intrusiveness_score": mon_info["intrusiveness"],
        "purpose": purpose,
        "scope": scope,
        "employees_affected": employee_count,
        "alternatives_considered": alternatives_considered,
        "private_use_permitted": private_use_permitted,
        "retention_days": retention_days,
        "proportionality_issues": issues,
        "proportionate": proportionate,
        "recommendation": (
            "Monitoring measure is proportionate to the stated purpose."
            if proportionate
            else f"Monitoring measure raises {len(issues)} proportionality concern(s). "
            "Address identified issues before proceeding."
        ),
    }


def assess_barbulescu_criteria(
    criteria_scores: dict[str, int],
) -> dict[str, Any]:
    """Assess employee monitoring against Barbulescu v Romania six criteria.

    Args:
        criteria_scores: Mapping of criterion IDs (BC1-BC6) to compliance score (1-5)
            1 = Not met, 3 = Partially met, 5 = Fully met

    Returns:
        Barbulescu criteria compliance assessment
    """
    results = []
    for criterion in BARBULESCU_CRITERIA:
        cid = criterion["id"]
        score = criteria_scores.get(cid, 1)
        results.append({
            "id": cid,
            "name": criterion["name"],
            "question": criterion["question"],
            "score": score,
            "status": (
                "Fully met" if score >= 4
                else "Partially met" if score >= 3
                else "Not met"
            ),
        })

    avg_score = sum(r["score"] for r in results) / len(results)
    not_met = [r for r in results if r["score"] < 3]

    return {
        "criteria_results": results,
        "average_score": round(avg_score, 1),
        "criteria_not_met": [r["name"] for r in not_met],
        "compliant": len(not_met) == 0,
        "assessment": (
            "All Barbulescu criteria are met. Monitoring is consistent with "
            "ECHR Art. 8 requirements."
            if len(not_met) == 0
            else f"{len(not_met)} Barbulescu criterion/criteria not met: "
            f"{', '.join(r['name'] for r in not_met)}. "
            "Address deficiencies before implementing monitoring."
        ),
    }


def generate_employee_surveillance_report(
    reference: str,
    org_name: str,
    monitoring_assessments: list[dict[str, Any]],
    barbulescu_assessment: dict[str, Any],
    works_council_consulted: bool,
    works_council_agreement_date: str | None,
) -> dict[str, Any]:
    """Generate a complete employee surveillance DPIA report."""
    disproportionate = [m for m in monitoring_assessments if not m.get("proportionate", True)]

    return {
        "metadata": {
            "reference": reference,
            "organisation": org_name,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "next_review": (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d"),
            "type": "Employee Surveillance DPIA",
        },
        "monitoring_measures": monitoring_assessments,
        "total_measures": len(monitoring_assessments),
        "disproportionate_measures": len(disproportionate),
        "barbulescu_assessment": barbulescu_assessment,
        "works_council": {
            "consulted": works_council_consulted,
            "agreement_date": works_council_agreement_date,
        },
        "conclusion": {
            "all_proportionate": len(disproportionate) == 0,
            "barbulescu_compliant": barbulescu_assessment["compliant"],
            "approved": len(disproportionate) == 0 and barbulescu_assessment["compliant"],
        },
    }


def run_example_assessment() -> dict[str, Any]:
    """Run example employee surveillance DPIA for QuantumLeap Health Technologies."""

    email_assessment = assess_monitoring_proportionality(
        monitoring_type="email_metadata",
        purpose="FCA SYSC 10A.1 compliance for regulated communications",
        scope="87 employees in regulated financial advisory roles",
        employee_count=87,
        alternatives_considered=[
            "No monitoring (rejected: regulatory non-compliance)",
            "Post-hoc audit only (rejected: insufficient for real-time compliance)",
        ],
        private_use_permitted=False,
        retention_days=30,
    )

    internet_assessment = assess_monitoring_proportionality(
        monitoring_type="internet_category",
        purpose="Network security and acceptable use policy enforcement",
        scope="All employees (2,847)",
        employee_count=2847,
        alternatives_considered=[
            "URL-level logging (rejected: disproportionate for category-level purpose)",
            "No monitoring with policy reliance only (rejected: insufficient malware protection)",
        ],
        private_use_permitted=True,
        retention_days=90,
    )

    barbulescu = assess_barbulescu_criteria({
        "BC1": 5,  # Prior notification in privacy notice and employment contract
        "BC2": 4,  # Metadata only; limited intrusion
        "BC3": 5,  # Regulatory compliance and security
        "BC4": 4,  # Less intrusive alternatives evaluated and documented
        "BC5": 4,  # No disciplinary consequences from monitoring data alone
        "BC6": 5,  # DPO oversight, works council agreement, audit logging
    })

    return generate_employee_surveillance_report(
        reference="DPIA-QLH-2026-0009",
        org_name="QuantumLeap Health Technologies",
        monitoring_assessments=[email_assessment, internet_assessment],
        barbulescu_assessment=barbulescu,
        works_council_consulted=True,
        works_council_agreement_date="2026-01-15",
    )


if __name__ == "__main__":
    result = run_example_assessment()
    print(json.dumps(result, indent=2, default=str))
