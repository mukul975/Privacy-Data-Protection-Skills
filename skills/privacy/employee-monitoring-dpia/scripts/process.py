"""
Employee Monitoring DPIA Assessment Engine

Automates the screening, proportionality assessment, and risk scoring for
employee monitoring Data Protection Impact Assessments per EDPB Guidelines
3/2019, WP248rev.01, and Barbulescu v Romania six-factor test.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


# EDPB WP248rev.01 Criteria
EDPB_CRITERIA = {
    "evaluation_scoring": "Evaluation or scoring of individuals",
    "automated_decisions": "Automated decision-making with legal or significant effect",
    "systematic_monitoring": "Systematic monitoring of data subjects",
    "sensitive_data": "Sensitive data or data of a highly personal nature",
    "large_scale": "Data processed on a large scale",
    "dataset_matching": "Matching or combining datasets",
    "vulnerable_subjects": "Data concerning vulnerable data subjects (employees)",
    "innovative_technology": "Innovative use or applying new technological solutions",
    "preventing_rights": "Processing that prevents data subjects from exercising a right",
}

# Monitoring categories with inherent risk profiles
MONITORING_CATEGORIES = {
    "video_surveillance": {
        "name": "Video Surveillance (CCTV)",
        "inherent_risk": "high",
        "edpb_criteria_met": [
            "systematic_monitoring",
            "vulnerable_subjects",
            "large_scale",
        ],
        "barbulescu_concerns": [
            "extent_of_monitoring",
            "less_intrusive_alternatives",
        ],
    },
    "email_monitoring": {
        "name": "Email and Internet Monitoring",
        "inherent_risk": "high",
        "edpb_criteria_met": [
            "systematic_monitoring",
            "vulnerable_subjects",
            "sensitive_data",
        ],
        "barbulescu_concerns": [
            "prior_notification",
            "extent_of_monitoring",
            "less_intrusive_alternatives",
            "consequences",
        ],
    },
    "gps_tracking": {
        "name": "GPS and Location Tracking",
        "inherent_risk": "high",
        "edpb_criteria_met": [
            "systematic_monitoring",
            "vulnerable_subjects",
            "large_scale",
        ],
        "barbulescu_concerns": [
            "extent_of_monitoring",
            "less_intrusive_alternatives",
        ],
    },
    "keystroke_logging": {
        "name": "Keystroke Logging and Screen Capture",
        "inherent_risk": "very_high",
        "edpb_criteria_met": [
            "systematic_monitoring",
            "vulnerable_subjects",
            "sensitive_data",
            "innovative_technology",
        ],
        "barbulescu_concerns": [
            "extent_of_monitoring",
            "less_intrusive_alternatives",
            "consequences",
            "safeguards",
        ],
    },
    "productivity_analytics": {
        "name": "Productivity and Behavioural Analytics",
        "inherent_risk": "very_high",
        "edpb_criteria_met": [
            "evaluation_scoring",
            "systematic_monitoring",
            "vulnerable_subjects",
            "innovative_technology",
            "automated_decisions",
        ],
        "barbulescu_concerns": [
            "prior_notification",
            "extent_of_monitoring",
            "less_intrusive_alternatives",
            "consequences",
            "safeguards",
        ],
    },
    "biometric_access": {
        "name": "Biometric Access Control / Timekeeping",
        "inherent_risk": "very_high",
        "edpb_criteria_met": [
            "sensitive_data",
            "vulnerable_subjects",
            "innovative_technology",
        ],
        "barbulescu_concerns": [
            "less_intrusive_alternatives",
            "safeguards",
        ],
    },
}

# Barbulescu six-factor test
BARBULESCU_FACTORS = {
    "prior_notification": {
        "name": "Factor 1: Prior Notification",
        "question": "Has the employee been notified in advance of the nature and extent of monitoring?",
        "weight": 1.5,
    },
    "extent_of_monitoring": {
        "name": "Factor 2: Extent of Monitoring and Degree of Intrusion",
        "question": "What is the scope of the monitoring (content vs metadata, continuous vs triggered)?",
        "weight": 2.0,
    },
    "legitimate_reasons": {
        "name": "Factor 3: Legitimate Reasons",
        "question": "Does the employer have documented legitimate reasons to justify the monitoring?",
        "weight": 1.5,
    },
    "less_intrusive_alternatives": {
        "name": "Factor 4: Less Intrusive Alternatives",
        "question": "Could the employer's aims be achieved through less intrusive methods?",
        "weight": 2.0,
    },
    "consequences": {
        "name": "Factor 5: Consequences for the Employee",
        "question": "What are the consequences of monitoring for the employee (disciplinary action, dismissal)?",
        "weight": 1.5,
    },
    "safeguards": {
        "name": "Factor 6: Adequate Safeguards",
        "question": "Are adequate safeguards in place (access controls, retention limits, grievance mechanisms)?",
        "weight": 1.5,
    },
}

# Risk matrix
LIKELIHOOD_SCORES = {"remote": 1, "possible": 2, "likely": 3, "almost_certain": 4}
SEVERITY_SCORES = {"negligible": 1, "limited": 2, "significant": 3, "maximum": 4}

RISK_LEVELS = {
    (1, 1): "low", (1, 2): "low", (1, 3): "medium", (1, 4): "medium",
    (2, 1): "low", (2, 2): "medium", (2, 3): "high", (2, 4): "high",
    (3, 1): "medium", (3, 2): "high", (3, 3): "high", (3, 4): "very_high",
    (4, 1): "medium", (4, 2): "high", (4, 3): "very_high", (4, 4): "very_high",
}


def generate_dpia_reference() -> str:
    """Generate a unique DPIA reference number for monitoring assessments."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"DPIA-MON-{datetime.now().year}-{timestamp[-4:]}"


def screen_monitoring_system(monitoring_types: list[str]) -> dict:
    """
    Screen a proposed monitoring system against EDPB WP248rev.01 criteria.

    Args:
        monitoring_types: List of monitoring category keys from MONITORING_CATEGORIES.

    Returns:
        Screening result with criteria count, DPIA obligation, and risk profile.
    """
    all_criteria_met = set()
    highest_risk = "low"
    risk_hierarchy = ["low", "medium", "high", "very_high"]
    categories_assessed = []

    for mt in monitoring_types:
        if mt not in MONITORING_CATEGORIES:
            continue
        category = MONITORING_CATEGORIES[mt]
        categories_assessed.append(category["name"])
        all_criteria_met.update(category["edpb_criteria_met"])
        cat_risk = category["inherent_risk"]
        if risk_hierarchy.index(cat_risk) > risk_hierarchy.index(highest_risk):
            highest_risk = cat_risk

    # Employees are always vulnerable data subjects
    all_criteria_met.add("vulnerable_subjects")

    criteria_details = [
        {"id": c, "description": EDPB_CRITERIA[c]} for c in all_criteria_met
    ]

    dpia_required = len(all_criteria_met) >= 2

    return {
        "reference": generate_dpia_reference(),
        "screening_date": datetime.now().isoformat(),
        "monitoring_categories": categories_assessed,
        "edpb_criteria_met": criteria_details,
        "criteria_count": len(all_criteria_met),
        "dpia_required": dpia_required,
        "dpia_obligation_reason": (
            f"Processing meets {len(all_criteria_met)} of 9 EDPB WP248rev.01 criteria "
            f"(threshold: 2). DPIA is mandatory."
            if dpia_required
            else "Fewer than 2 criteria met — DPIA not presumptively required but recommended."
        ),
        "inherent_risk_level": highest_risk,
    }


def assess_barbulescu_compliance(
    factor_scores: dict[str, int],
) -> dict:
    """
    Assess monitoring compliance against the Barbulescu v Romania six-factor test.

    Args:
        factor_scores: Dict mapping factor keys to scores (1-5, where 1=non-compliant,
                       5=fully compliant).

    Returns:
        Compliance assessment with weighted score and recommendations.
    """
    results = []
    total_weighted = 0.0
    max_weighted = 0.0

    for factor_key, factor_info in BARBULESCU_FACTORS.items():
        score = factor_scores.get(factor_key, 1)
        score = max(1, min(5, score))
        weight = factor_info["weight"]
        weighted_score = score * weight
        total_weighted += weighted_score
        max_weighted += 5 * weight

        compliance_status = "compliant" if score >= 4 else "partial" if score >= 3 else "non_compliant"

        results.append({
            "factor": factor_info["name"],
            "question": factor_info["question"],
            "score": score,
            "weight": weight,
            "weighted_score": round(weighted_score, 2),
            "compliance_status": compliance_status,
        })

    overall_percentage = round((total_weighted / max_weighted) * 100, 1) if max_weighted > 0 else 0
    overall_status = (
        "compliant" if overall_percentage >= 80
        else "partial_compliance" if overall_percentage >= 60
        else "non_compliant"
    )

    non_compliant_factors = [r for r in results if r["compliance_status"] == "non_compliant"]

    recommendations = []
    for ncf in non_compliant_factors:
        if "Prior Notification" in ncf["factor"]:
            recommendations.append(
                "Update acceptable use policy and privacy notice to describe monitoring "
                "scope before activation. Provide individual notification to each employee."
            )
        elif "Extent" in ncf["factor"]:
            recommendations.append(
                "Reduce monitoring scope: prefer metadata over content monitoring, "
                "triggered over continuous, targeted over blanket."
            )
        elif "Legitimate" in ncf["factor"]:
            recommendations.append(
                "Document specific, concrete legitimate aims for each monitoring measure. "
                "A general desire for 'productivity' is insufficient."
            )
        elif "Less Intrusive" in ncf["factor"]:
            recommendations.append(
                "Evaluate less intrusive alternatives for each monitoring measure. "
                "Document why less invasive methods are insufficient."
            )
        elif "Consequences" in ncf["factor"]:
            recommendations.append(
                "Implement policy that monitoring data cannot be used as sole basis "
                "for adverse employment decisions. Require human review."
            )
        elif "Safeguards" in ncf["factor"]:
            recommendations.append(
                "Implement access controls, retention limits, audit logging, "
                "grievance procedure, and annual proportionality review."
            )

    return {
        "assessment_date": datetime.now().isoformat(),
        "factor_results": results,
        "overall_weighted_score": round(total_weighted, 2),
        "maximum_possible_score": round(max_weighted, 2),
        "overall_percentage": overall_percentage,
        "overall_status": overall_status,
        "non_compliant_factors": len(non_compliant_factors),
        "recommendations": recommendations,
    }


def calculate_risk_level(likelihood: str, severity: str) -> str:
    """Calculate risk level from likelihood and severity ratings."""
    l_score = LIKELIHOOD_SCORES.get(likelihood, 2)
    s_score = SEVERITY_SCORES.get(severity, 2)
    return RISK_LEVELS.get((l_score, s_score), "medium")


def assess_monitoring_risks(monitoring_types: list[str]) -> list[dict]:
    """
    Generate a risk register for the specified monitoring system types.

    Args:
        monitoring_types: List of monitoring category keys.

    Returns:
        List of risk entries with inherent and suggested residual risk levels.
    """
    standard_risks = [
        {
            "id": "MON-R001",
            "description": "Chilling effect on legitimate workplace communication and trade union activity",
            "likelihood": "likely",
            "severity": "significant",
            "affected_rights": "Freedom of expression, freedom of association",
            "mitigation": "Exclude trade union communications from monitoring scope; limit monitoring to security-relevant channels",
        },
        {
            "id": "MON-R002",
            "description": "Disproportionate surveillance creating hostile work environment",
            "likelihood": "possible",
            "severity": "significant",
            "affected_rights": "Dignity at work, private life",
            "mitigation": "Annual proportionality review; employee feedback mechanism",
        },
        {
            "id": "MON-R003",
            "description": "Monitoring data used for discriminatory employment decisions",
            "likelihood": "possible",
            "severity": "maximum",
            "affected_rights": "Non-discrimination, fair treatment",
            "mitigation": "Prohibition on using monitoring data as sole basis for decisions; mandatory human review",
        },
        {
            "id": "MON-R004",
            "description": "Unauthorised access to monitoring data by line managers",
            "likelihood": "likely",
            "severity": "limited",
            "affected_rights": "Data protection, confidentiality",
            "mitigation": "RBAC restricting access to authorised HR/security personnel; audit logging",
        },
        {
            "id": "MON-R005",
            "description": "Function creep — monitoring data used beyond original justification",
            "likelihood": "likely",
            "severity": "significant",
            "affected_rights": "Purpose limitation, data minimisation",
            "mitigation": "Document purpose; automated access controls enforce purpose limitation; DPO oversight",
        },
        {
            "id": "MON-R006",
            "description": "Capture of legally privileged communications (legal, medical, union)",
            "likelihood": "possible",
            "severity": "maximum",
            "affected_rights": "Legal professional privilege, medical confidentiality",
            "mitigation": "Whitelist privileged communication addresses; automated exclusion rules",
        },
        {
            "id": "MON-R007",
            "description": "Cross-border transfer of monitoring data to non-adequate jurisdiction",
            "likelihood": "possible",
            "severity": "significant",
            "affected_rights": "Data protection, transfer safeguards",
            "mitigation": "Verify monitoring platform data residency; implement SCCs; conduct TIA",
        },
        {
            "id": "MON-R008",
            "description": "Inability of employees to exercise DSAR rights over monitoring data",
            "likelihood": "possible",
            "severity": "significant",
            "affected_rights": "Right of access (Art. 15)",
            "mitigation": "Configure monitoring system to support individual data export; document DSAR procedure for monitoring data",
        },
    ]

    # Add category-specific risks
    if "keystroke_logging" in monitoring_types:
        standard_risks.append({
            "id": "MON-R009",
            "description": "Keystroke logging captures personal passwords, financial data, and private messages",
            "likelihood": "almost_certain",
            "severity": "maximum",
            "affected_rights": "Private life, data protection, financial privacy",
            "mitigation": "RECOMMENDATION: Do not deploy keystroke logging. If absolutely necessary, limit to specific investigation with time limit.",
        })

    if "productivity_analytics" in monitoring_types:
        standard_risks.append({
            "id": "MON-R010",
            "description": "AI-driven productivity scoring constitutes automated decision-making under Art. 22",
            "likelihood": "likely",
            "severity": "significant",
            "affected_rights": "Right not to be subject to automated decisions (Art. 22)",
            "mitigation": "Ensure human review before any employment decision based on productivity scores; provide Art. 22(3) safeguards",
        })

    # Calculate risk levels
    for risk in standard_risks:
        risk["inherent_risk_level"] = calculate_risk_level(
            risk["likelihood"], risk["severity"]
        )

    return standard_risks


def generate_dpia_report(
    organisation: str,
    monitoring_types: list[str],
    employee_count: int,
    barbulescu_scores: dict[str, int],
    dpo_name: str = "Data Protection Officer",
) -> dict:
    """
    Generate a complete DPIA report for an employee monitoring system.

    Args:
        organisation: Organisation name.
        monitoring_types: List of monitoring category keys.
        employee_count: Number of employees subject to monitoring.
        barbulescu_scores: Scores for each Barbulescu factor (1-5).
        dpo_name: Name of the DPO.

    Returns:
        Complete DPIA report as a structured dictionary.
    """
    screening = screen_monitoring_system(monitoring_types)
    barbulescu = assess_barbulescu_compliance(barbulescu_scores)
    risks = assess_monitoring_risks(monitoring_types)

    high_risks = [r for r in risks if r["inherent_risk_level"] in ("high", "very_high")]
    prior_consultation_required = any(
        r["inherent_risk_level"] == "very_high" for r in risks
    ) and barbulescu["overall_status"] == "non_compliant"

    review_date = datetime.now() + timedelta(days=365)

    report = {
        "dpia_reference": screening["reference"],
        "organisation": organisation,
        "assessment_date": datetime.now().isoformat(),
        "dpo": dpo_name,
        "section_1_screening": screening,
        "section_2_description": {
            "monitoring_categories": [
                MONITORING_CATEGORIES[mt]["name"]
                for mt in monitoring_types
                if mt in MONITORING_CATEGORIES
            ],
            "employees_in_scope": employee_count,
            "data_subjects_type": "Employees (vulnerable data subjects per EDPB WP248rev.01)",
        },
        "section_3_proportionality": barbulescu,
        "section_4_risk_assessment": {
            "total_risks_identified": len(risks),
            "high_very_high_risks": len(high_risks),
            "risks": risks,
        },
        "section_5_conclusion": {
            "dpia_required": screening["dpia_required"],
            "proportionality_status": barbulescu["overall_status"],
            "prior_consultation_required": prior_consultation_required,
            "prior_consultation_reason": (
                "Residual risk remains Very High after mitigation and proportionality "
                "assessment is non-compliant. Art. 36 prior consultation with the "
                "supervisory authority is required before processing begins."
                if prior_consultation_required
                else "Prior consultation not required at this stage."
            ),
            "next_review_date": review_date.strftime("%Y-%m-%d"),
        },
    }

    return report


def main():
    """Example: Atlas Manufacturing Group employee monitoring DPIA."""
    report = generate_dpia_report(
        organisation="Atlas Manufacturing Group",
        monitoring_types=["video_surveillance", "email_monitoring", "gps_tracking"],
        employee_count=2400,
        barbulescu_scores={
            "prior_notification": 4,
            "extent_of_monitoring": 3,
            "legitimate_reasons": 4,
            "less_intrusive_alternatives": 3,
            "consequences": 4,
            "safeguards": 4,
        },
        dpo_name="Dr. Sarah Müller, CIPP/E",
    )

    print(json.dumps(report, indent=2, default=str))

    print("\n--- DPIA Summary ---")
    print(f"Reference: {report['dpia_reference']}")
    print(f"Organisation: {report['organisation']}")
    print(f"DPIA Required: {report['section_1_screening']['dpia_required']}")
    print(f"EDPB Criteria Met: {report['section_1_screening']['criteria_count']}/9")
    print(f"Inherent Risk Level: {report['section_1_screening']['inherent_risk_level']}")
    print(f"Barbulescu Compliance: {report['section_3_proportionality']['overall_percentage']}%")
    print(f"Barbulescu Status: {report['section_3_proportionality']['overall_status']}")
    print(f"Total Risks: {report['section_4_risk_assessment']['total_risks_identified']}")
    print(f"High/Very High Risks: {report['section_4_risk_assessment']['high_very_high_risks']}")
    print(f"Prior Consultation Required: {report['section_5_conclusion']['prior_consultation_required']}")
    print(f"Next Review: {report['section_5_conclusion']['next_review_date']}")


if __name__ == "__main__":
    main()
