#!/usr/bin/env python3
"""HIPAA risk analysis processor — threat/vulnerability assessment and risk scoring engine."""

import json
import os
from datetime import datetime
from typing import Any


LIKELIHOOD_SCALE = {
    1: "Very Low — Remote possibility; no known threat source",
    2: "Low — Unlikely but possible; limited threat capability",
    3: "Medium — Possible occurrence; controls partially effective",
    4: "High — Likely to occur; known weaknesses in controls",
    5: "Very High — Almost certain; active exploitation observed",
}

IMPACT_SCALE = {
    1: "Negligible — Minimal or no harm",
    2: "Low — Limited harm to few individuals",
    3: "Medium — Moderate harm; multi-day system disruption",
    4: "High — Significant harm to many individuals; OCR investigation likely",
    5: "Critical — Catastrophic harm; breach of 500K+ records; insolvency risk",
}

RISK_LEVELS = {
    (20, 25): {"level": "Critical", "action": "Immediate mitigation required", "timeline_days": 0},
    (12, 19): {"level": "High", "action": "Mitigation plan within 30 days", "timeline_days": 30},
    (6, 11): {"level": "Medium", "action": "Mitigation plan within 90 days", "timeline_days": 90},
    (2, 5): {"level": "Low", "action": "Monitor; address in normal operations", "timeline_days": 365},
    (1, 1): {"level": "Minimal", "action": "Accept and document; annual review", "timeline_days": 365},
}

THREAT_CATEGORIES = {
    "natural": [
        "Flood", "Earthquake", "Tornado/Hurricane", "Wildfire", "Pandemic",
    ],
    "human_intentional": [
        "Ransomware attack", "Phishing/social engineering", "Insider theft",
        "Nation-state APT", "Unauthorized access by former employee",
        "SQL injection/web application attack", "Denial of service",
    ],
    "human_unintentional": [
        "Misdirected email/fax", "Lost/stolen device",
        "Improper media disposal", "Misconfiguration",
        "Unauthorized software installation", "Training failure",
    ],
    "environmental": [
        "Power failure", "HVAC failure", "Water damage", "Fire",
    ],
    "technical": [
        "Software vulnerability (zero-day)", "Hardware failure",
        "Network outage", "Cryptographic weakness", "Certificate expiration",
    ],
}

EPHI_ASSET_CATEGORIES = [
    "Electronic Health Record (EHR)",
    "Practice Management System",
    "Laboratory Information System",
    "Radiology PACS",
    "Email System",
    "Mobile Devices",
    "Medical Devices (networked)",
    "Backup and Archive",
    "Business Associate Systems",
    "Health Information Exchange",
    "Patient Portal",
    "Telehealth Platform",
    "Remote Patient Monitoring",
]


def calculate_risk_score(likelihood: int, impact: int) -> dict[str, Any]:
    """Calculate risk score and determine risk level.

    Args:
        likelihood: Likelihood rating (1-5).
        impact: Impact rating (1-5).

    Returns:
        Dictionary with risk score, level, and recommended action.
    """
    if not (1 <= likelihood <= 5) or not (1 <= impact <= 5):
        return {"error": "Likelihood and impact must be between 1 and 5"}

    score = likelihood * impact

    risk_info = {"level": "Unknown", "action": "", "timeline_days": 0}
    for (low, high), info in RISK_LEVELS.items():
        if low <= score <= high:
            risk_info = info
            break

    return {
        "likelihood": likelihood,
        "likelihood_description": LIKELIHOOD_SCALE.get(likelihood, ""),
        "impact": impact,
        "impact_description": IMPACT_SCALE.get(impact, ""),
        "risk_score": score,
        "risk_level": risk_info["level"],
        "recommended_action": risk_info["action"],
        "mitigation_timeline_days": risk_info["timeline_days"],
    }


def create_risk_entry(
    risk_id: str,
    asset: str,
    threat: str,
    vulnerability: str,
    likelihood: int,
    impact: int,
    existing_controls: list[str] | None = None,
    mitigation_plan: str = "",
) -> dict[str, Any]:
    """Create a risk register entry.

    Args:
        risk_id: Unique risk identifier.
        asset: ePHI asset affected.
        threat: Threat description.
        vulnerability: Vulnerability description.
        likelihood: Likelihood rating (1-5).
        impact: Impact rating (1-5).
        existing_controls: List of current controls in place.
        mitigation_plan: Planned mitigation measures.

    Returns:
        Complete risk register entry.
    """
    risk_calc = calculate_risk_score(likelihood, impact)

    return {
        "risk_id": risk_id,
        "asset": asset,
        "threat": threat,
        "vulnerability": vulnerability,
        "existing_controls": existing_controls or [],
        "risk_assessment": risk_calc,
        "mitigation_plan": mitigation_plan,
        "status": "open",
        "owner": "",
        "created_date": datetime.now().strftime("%Y-%m-%d"),
        "last_reviewed": datetime.now().strftime("%Y-%m-%d"),
        "next_review_date": "",
    }


def build_risk_register(risks: list[dict[str, Any]]) -> dict[str, Any]:
    """Build a complete risk register from individual risk entries.

    Args:
        risks: List of risk entry dictionaries.

    Returns:
        Risk register with summary statistics and sorted entries.
    """
    register = {
        "organization": "",
        "assessment_date": datetime.now().isoformat(),
        "methodology": "NIST SP 800-30 Rev. 1 aligned with OCR Nine Essential Elements",
        "risk_entries": sorted(
            risks,
            key=lambda r: r.get("risk_assessment", {}).get("risk_score", 0),
            reverse=True,
        ),
        "summary": {
            "total_risks": len(risks),
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "minimal": 0,
        },
        "risk_distribution": {},
    }

    for risk in risks:
        level = risk.get("risk_assessment", {}).get("risk_level", "Unknown").lower()
        if level in register["summary"]:
            register["summary"][level] += 1

    for category in THREAT_CATEGORIES:
        count = sum(
            1 for r in risks
            if any(t.lower() in r.get("threat", "").lower() for t in THREAT_CATEGORIES[category])
        )
        register["risk_distribution"][category] = count

    return register


def validate_risk_analysis_completeness(
    analysis: dict[str, Any],
) -> dict[str, Any]:
    """Validate a risk analysis against OCR's nine essential elements.

    Args:
        analysis: Dictionary representing the risk analysis documentation.

    Returns:
        Validation results with compliance status per element.
    """
    elements = {
        "scope": {
            "description": "Element 1: Scope — All ePHI in all forms and locations",
            "checks": [
                ("all_ephi_locations_identified", "All ePHI storage locations identified"),
                ("all_transmission_paths_mapped", "All ePHI transmission paths documented"),
                ("ba_systems_included", "Business associate systems with ePHI included"),
                ("mobile_devices_included", "Mobile devices and portable media included"),
                ("medical_devices_included", "Networked medical devices included"),
            ],
        },
        "data_collection": {
            "description": "Element 2: Data Collection — Where ePHI is stored, received, maintained, transmitted",
            "checks": [
                ("automated_discovery", "Automated discovery tools used"),
                ("data_flow_mapping", "Data flow diagrams documented"),
                ("interviews_conducted", "Workforce interviews conducted"),
                ("system_inventory_current", "System inventory current and complete"),
            ],
        },
        "threats_vulnerabilities": {
            "description": "Element 3: Identify and Document Potential Threats and Vulnerabilities",
            "checks": [
                ("natural_threats", "Natural threats assessed"),
                ("human_threats", "Human threats (intentional and unintentional) assessed"),
                ("environmental_threats", "Environmental threats assessed"),
                ("technical_threats", "Technical threats assessed"),
                ("vulnerability_scanning", "Vulnerability scanning performed"),
                ("penetration_testing", "Penetration testing performed"),
            ],
        },
        "current_security": {
            "description": "Element 4: Assess Current Security Measures",
            "checks": [
                ("administrative_safeguards_assessed", "Administrative safeguards documented and assessed"),
                ("physical_safeguards_assessed", "Physical safeguards documented and assessed"),
                ("technical_safeguards_assessed", "Technical safeguards documented and assessed"),
                ("control_effectiveness_rated", "Control effectiveness rated"),
            ],
        },
        "likelihood": {
            "description": "Element 5: Determine the Likelihood of Threat Occurrence",
            "checks": [
                ("likelihood_methodology_defined", "Likelihood assessment methodology documented"),
                ("likelihood_ratings_consistent", "Consistent rating scale applied across all risks"),
                ("threat_intelligence_used", "Current threat intelligence incorporated"),
            ],
        },
        "impact": {
            "description": "Element 6: Determine the Potential Impact",
            "checks": [
                ("impact_methodology_defined", "Impact assessment methodology documented"),
                ("impact_ratings_consistent", "Consistent rating scale applied"),
                ("cia_triad_considered", "Confidentiality, integrity, and availability all considered"),
            ],
        },
        "risk_level": {
            "description": "Element 7: Determine the Level of Risk",
            "checks": [
                ("risk_calculation_documented", "Risk calculation method documented"),
                ("risk_levels_assigned", "Risk levels assigned to all threat/vulnerability pairs"),
                ("risk_register_maintained", "Risk register maintained with all entries"),
            ],
        },
        "documentation": {
            "description": "Element 8: Finalize Documentation",
            "checks": [
                ("date_and_period", "Analysis date and period documented"),
                ("assessor_qualifications", "Assessor names and qualifications documented"),
                ("methodology_described", "Methodology fully described"),
                ("management_signoff", "Management sign-off obtained"),
            ],
        },
        "periodic_review": {
            "description": "Element 9: Periodic Review and Updates",
            "checks": [
                ("review_schedule", "Annual review schedule established"),
                ("trigger_events_defined", "Trigger events for interim updates defined"),
                ("previous_analysis_available", "Previous risk analysis available for comparison"),
                ("changes_since_last_tracked", "Changes since last analysis tracked"),
            ],
        },
    }

    analysis_status = analysis.get("compliance_status", {})
    results = {
        "validation_date": datetime.now().isoformat(),
        "elements": {},
        "summary": {
            "total_checks": 0,
            "passed": 0,
            "failed": 0,
            "not_assessed": 0,
        },
    }

    for element_key, element_config in elements.items():
        element_result = {
            "description": element_config["description"],
            "checks": [],
            "passed_count": 0,
            "total_count": len(element_config["checks"]),
        }

        for check_key, check_desc in element_config["checks"]:
            status = analysis_status.get(check_key, "not_assessed")
            element_result["checks"].append({
                "key": check_key,
                "description": check_desc,
                "status": status,
            })
            results["summary"]["total_checks"] += 1
            if status == "passed":
                element_result["passed_count"] += 1
                results["summary"]["passed"] += 1
            elif status == "failed":
                results["summary"]["failed"] += 1
            else:
                results["summary"]["not_assessed"] += 1

        results["elements"][element_key] = element_result

    total = results["summary"]["total_checks"]
    passed = results["summary"]["passed"]
    results["summary"]["completeness_percentage"] = (
        round(passed / total * 100, 1) if total > 0 else 0
    )

    return results


def export_risk_register(register: dict[str, Any], output_path: str) -> str:
    """Export risk register to JSON file."""
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(register, f, indent=2, ensure_ascii=False)
    return output_path


if __name__ == "__main__":
    print("=== HIPAA Risk Analysis Engine ===\n")

    sample_risks = [
        create_risk_entry(
            "R-001", "Clinical EHR System", "Ransomware attack",
            "Insufficient network segmentation between clinical and administrative networks",
            4, 5, ["EDR on endpoints", "Daily backups", "Firewall"],
            "Implement micro-segmentation; deploy immutable backups; quarterly tabletop exercises",
        ),
        create_risk_entry(
            "R-002", "Employee email", "Phishing leading to credential compromise",
            "No MFA on email system; workforce susceptible to phishing",
            4, 4, ["Spam filter", "Annual security training"],
            "Deploy MFA for all email access; implement monthly phishing simulations",
        ),
        create_risk_entry(
            "R-003", "Mobile devices", "Lost/stolen unencrypted mobile device",
            "12 legacy tablets without full disk encryption",
            2, 3, ["MDM enrollment", "Remote wipe capability"],
            "Replace legacy tablets with encrypted devices; enforce FDE policy",
        ),
        create_risk_entry(
            "R-004", "Patient Portal", "SQL injection attack",
            "Web application not tested for OWASP Top 10 vulnerabilities",
            3, 4, ["WAF in place", "Input validation on some forms"],
            "Conduct DAST/SAST testing; implement parameterized queries; annual pen test",
        ),
        create_risk_entry(
            "R-005", "Medical devices", "Unpatched vulnerabilities on networked infusion pumps",
            "Manufacturer does not release patches timely; devices run outdated OS",
            3, 4, ["Network segmentation (partial)", "Monitoring"],
            "Complete network isolation of medical device VLAN; compensating monitoring controls",
        ),
    ]

    register = build_risk_register(sample_risks)
    register["organization"] = "Asclepius Health Network"

    print(f"Risk Register Summary for {register['organization']}:")
    print(f"  Total risks: {register['summary']['total_risks']}")
    print(f"  Critical: {register['summary']['critical']}")
    print(f"  High: {register['summary']['high']}")
    print(f"  Medium: {register['summary']['medium']}")
    print(f"  Low: {register['summary']['low']}")
    print(f"\nTop 3 Risks:")
    for risk in register["risk_entries"][:3]:
        ra = risk["risk_assessment"]
        print(f"  {risk['risk_id']}: {risk['threat']} — Score: {ra['risk_score']} ({ra['risk_level']})")
