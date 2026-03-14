"""
Remote Work Monitoring Proportionality Engine

Assesses the proportionality of remote work monitoring technologies against
EDPB guidance, Barbulescu six-factor test, and national DPA positions.
Recommends output-based alternatives where monitoring is disproportionate.
"""

import json
from datetime import datetime
from typing import Optional


MONITORING_TECHNOLOGIES = {
    "screen_capture": {
        "name": "Screen Capture / Recording",
        "intrusiveness": "very_high",
        "proportionate_for_remote": False,
        "dpa_position": "CNIL, Garante, ICO: disproportionate for remote work",
        "risk_factors": [
            "Captures personal content on screen",
            "Captures home environment if sharing screen",
            "May reveal special category data (health sites, political content)",
            "Family members may be visible",
        ],
        "less_intrusive_alternative": "Application usage monitoring or output-based metrics",
    },
    "webcam_monitoring": {
        "name": "Webcam / Camera Monitoring",
        "intrusiveness": "very_high",
        "proportionate_for_remote": False,
        "dpa_position": "Dutch Court (Chetu, 2022): wrongful dismissal for requiring webcam",
        "risk_factors": [
            "Captures employee's home environment",
            "Captures family members including children",
            "May reveal health conditions, religious items, disability",
            "Equivalent to employer looking into employee's home",
        ],
        "less_intrusive_alternative": "Login/logout times, scheduled check-in meetings",
    },
    "keystroke_logging": {
        "name": "Keystroke Logging",
        "intrusiveness": "very_high",
        "proportionate_for_remote": False,
        "dpa_position": "BfDI/Federal Labour Court: evidence inadmissible; CNIL: prohibited",
        "risk_factors": [
            "Captures personal passwords and financial data",
            "Captures private messages and personal searches",
            "Captures everything typed, including personal and medical information",
            "Cannot distinguish corporate from personal input",
        ],
        "less_intrusive_alternative": "Output metrics, task completion tracking",
    },
    "mouse_activity_tracking": {
        "name": "Mouse Movement / Activity Tracking",
        "intrusiveness": "high",
        "proportionate_for_remote": False,
        "dpa_position": "Generally disproportionate; poor correlation with productivity",
        "risk_factors": [
            "Creates continuous surveillance record",
            "Poor accuracy: reading, thinking, phone calls involve no mouse movement",
            "Drives evasion (mouse jigglers) rather than productivity",
            "Creates anxiety and hostile work culture",
        ],
        "less_intrusive_alternative": "Task management tools, regular check-ins",
    },
    "productivity_scoring_ai": {
        "name": "AI-Powered Productivity Scoring",
        "intrusiveness": "very_high",
        "proportionate_for_remote": False,
        "dpa_position": "Art. 22 automated decision-making restrictions apply",
        "risk_factors": [
            "Creates comprehensive behavioural profile",
            "Algorithms may disadvantage employees with disabilities or caring responsibilities",
            "Rewards visible activity over deep work",
            "Art. 22 GDPR: right not to be subject to automated decision-making",
        ],
        "less_intrusive_alternative": "Regular 1:1 meetings, objective-based performance management",
    },
    "application_monitoring": {
        "name": "Application Usage Monitoring",
        "intrusiveness": "medium",
        "proportionate_for_remote": True,
        "dpa_position": "May be proportionate if limited to corporate apps with safeguards",
        "risk_factors": [
            "Must be limited to corporate applications only",
            "Must not log personal app usage on BYOD",
            "Aggregate reporting preferred over individual",
            "Must not be sole basis for adverse decisions",
        ],
        "less_intrusive_alternative": "Output metrics (even less intrusive)",
        "conditions": [
            "Limited to corporate-managed applications",
            "Aggregate team-level reporting preferred",
            "Not used as sole basis for performance evaluation",
            "Employees informed before deployment",
        ],
    },
    "login_logout_vpn": {
        "name": "Login/Logout and VPN Connection Logging",
        "intrusiveness": "low",
        "proportionate_for_remote": True,
        "dpa_position": "Generally proportionate; confirms working hours",
        "risk_factors": [
            "Records connection times only, not activity content",
            "Low intrusiveness",
            "Useful for Working Time Directive compliance",
        ],
        "less_intrusive_alternative": "Self-reporting (less reliable)",
        "conditions": [
            "Employees informed that login times are recorded",
            "Used only for working time management",
            "Not used for micro-management of breaks",
        ],
    },
}


def assess_monitoring_proportionality(
    proposed_technologies: list[str],
    organisation: str = "Organisation",
    employee_count: int = 0,
    jurisdiction: str = "EU",
) -> dict:
    """
    Assess proportionality of proposed remote monitoring technologies.

    Args:
        proposed_technologies: List of technology keys.
        organisation: Organisation name.
        employee_count: Number of remote workers affected.
        jurisdiction: Jurisdiction code.

    Returns:
        Proportionality assessment with recommendations.
    """
    proportionate = []
    disproportionate = []
    recommendations = []

    for tech_key in proposed_technologies:
        tech = MONITORING_TECHNOLOGIES.get(tech_key)
        if not tech:
            continue

        assessment = {
            "technology": tech["name"],
            "intrusiveness": tech["intrusiveness"],
            "proportionate": tech["proportionate_for_remote"],
            "dpa_position": tech["dpa_position"],
            "risk_factors": tech["risk_factors"],
            "alternative": tech["less_intrusive_alternative"],
        }

        if tech["proportionate_for_remote"]:
            assessment["conditions"] = tech.get("conditions", [])
            proportionate.append(assessment)
        else:
            disproportionate.append(assessment)
            recommendations.append(
                f"Do NOT deploy {tech['name']} for remote workers. "
                f"Use instead: {tech['less_intrusive_alternative']}."
            )

    # Always recommend output-based management
    recommendations.append(
        "Consider output-based management as the primary approach: "
        "clear objectives, regular check-ins, task management tools. "
        "Both ICO and CNIL recommend this approach."
    )

    overall_proportionate = len(disproportionate) == 0

    return {
        "assessment_date": datetime.now().isoformat(),
        "organisation": organisation,
        "remote_workers_affected": employee_count,
        "jurisdiction": jurisdiction,
        "technologies_assessed": len(proposed_technologies),
        "proportionate_technologies": proportionate,
        "disproportionate_technologies": disproportionate,
        "overall_proportionate": overall_proportionate,
        "recommendations": recommendations,
        "dpia_required": True,
        "output_based_alternative": {
            "name": "Output-Based Remote Work Management",
            "components": [
                "Documented, measurable objectives",
                "Regular 1:1 manager check-ins (weekly)",
                "Task management platform (Jira, Asana, Monday.com)",
                "Daily team stand-ups (15 minutes)",
                "Agreed core hours and response times",
                "Manager training on remote leadership",
            ],
            "endorsement": "Recommended by ICO and CNIL as proportionate alternative to monitoring",
        },
    }


def main():
    """Example: Atlas Manufacturing Group remote monitoring assessment."""
    print("=== Remote Work Monitoring Proportionality Assessment ===")
    print("Organisation: Atlas Manufacturing Group\n")

    # Assess proposed monitoring suite
    result = assess_monitoring_proportionality(
        proposed_technologies=[
            "screen_capture",
            "mouse_activity_tracking",
            "login_logout_vpn",
            "application_monitoring",
        ],
        organisation="Atlas Manufacturing Group",
        employee_count=400,
        jurisdiction="EU",
    )

    print(f"Technologies Assessed: {result['technologies_assessed']}")
    print(f"Overall Proportionate: {result['overall_proportionate']}")

    print("\nProportionate Technologies:")
    for tech in result["proportionate_technologies"]:
        print(f"  [OK] {tech['technology']} (intrusiveness: {tech['intrusiveness']})")
        if tech.get("conditions"):
            for cond in tech["conditions"]:
                print(f"       Condition: {cond}")

    print("\nDisproportionate Technologies:")
    for tech in result["disproportionate_technologies"]:
        print(f"  [FAIL] {tech['technology']} (intrusiveness: {tech['intrusiveness']})")
        print(f"         DPA Position: {tech['dpa_position']}")
        print(f"         Alternative: {tech['alternative']}")

    print("\nRecommendations:")
    for rec in result["recommendations"]:
        print(f"  - {rec}")

    print("\n" + json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
