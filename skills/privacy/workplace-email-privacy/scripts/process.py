"""
Workplace Email Privacy Compliance Engine

Implements the Barbulescu v Romania six-factor proportionality test for
workplace email and internet monitoring compliance assessment.
"""

import json
from datetime import datetime
from typing import Optional


BARBULESCU_FACTORS = {
    "prior_notification": {
        "name": "Factor 1: Prior Notification",
        "description": "Employee notified in advance of nature and extent of monitoring",
        "weight": 1.5,
        "compliance_checks": [
            "Acceptable Use Policy in place and current",
            "AUP specifies what is monitored (metadata, content, or both)",
            "AUP specifies when monitoring occurs",
            "AUP specifies who has access to monitoring data",
            "All employees have acknowledged the AUP in writing",
            "AUP provided before monitoring began",
        ],
    },
    "extent_of_monitoring": {
        "name": "Factor 2: Extent of Monitoring",
        "description": "Scope of monitoring and degree of intrusion into privacy",
        "weight": 2.0,
        "compliance_checks": [
            "Monitoring limited to metadata where possible",
            "Content monitoring only where metadata is insufficient",
            "Monitoring is triggered rather than continuous where possible",
            "Individual monitoring only where aggregate is insufficient",
            "Personal communications excluded from monitoring scope",
        ],
    },
    "legitimate_reasons": {
        "name": "Factor 3: Legitimate Reasons",
        "description": "Documented legitimate reasons for monitoring and content access",
        "weight": 1.5,
        "compliance_checks": [
            "Specific legitimate aim documented (not generic productivity)",
            "Aim relates to security, compliance, or specific misconduct concern",
            "Aim is current and relevant (not historical justification)",
        ],
    },
    "less_intrusive_alternatives": {
        "name": "Factor 4: Less Intrusive Alternatives",
        "description": "Whether employer aims could be achieved through less intrusive methods",
        "weight": 2.0,
        "compliance_checks": [
            "Less intrusive alternatives have been formally considered",
            "Reasons for rejecting alternatives are documented",
            "Metadata monitoring considered before content monitoring",
            "Automated DLP considered before human content review",
            "Training and policy enforcement considered before monitoring",
        ],
    },
    "consequences": {
        "name": "Factor 5: Consequences for Employee",
        "description": "Potential consequences of monitoring for the monitored employee",
        "weight": 1.5,
        "compliance_checks": [
            "Monitoring data not used as sole basis for adverse decisions",
            "Human review required before any disciplinary action",
            "Separation between monitoring function and disciplinary function",
            "Employee informed if monitoring data contributes to an adverse decision",
        ],
    },
    "safeguards": {
        "name": "Factor 6: Adequate Safeguards",
        "description": "Safeguards to protect employee privacy during monitoring",
        "weight": 1.5,
        "compliance_checks": [
            "Access to monitoring data restricted to authorised personnel",
            "Legal professional privilege communications excluded",
            "Medical communications excluded",
            "Trade union communications excluded",
            "Retention period defined and technically enforced",
            "Audit logging enabled for all monitoring data access",
            "Employee grievance procedure available for monitoring concerns",
            "Annual proportionality review scheduled",
        ],
    },
}

MONITORING_TYPES = {
    "email_metadata": {
        "name": "Email Metadata Monitoring",
        "intrusiveness": "low",
        "description": "Sender, recipient, timestamp, subject line, attachment names",
    },
    "email_content_dlp": {
        "name": "Email Content — Automated DLP Scanning",
        "intrusiveness": "medium",
        "description": "Automated keyword/pattern scanning of email content and attachments",
    },
    "email_content_human": {
        "name": "Email Content — Human Review",
        "intrusiveness": "high",
        "description": "Human review of actual email content",
    },
    "internet_url_logging": {
        "name": "Internet URL Logging",
        "intrusiveness": "medium",
        "description": "Recording URLs visited, browsing duration, bandwidth",
    },
    "internet_content_filtering": {
        "name": "Internet Content Filtering",
        "intrusiveness": "low",
        "description": "Blocking access to categories of websites without logging individual activity",
    },
    "messaging_logging": {
        "name": "Instant Messaging Logging",
        "intrusiveness": "medium",
        "description": "Retention and potential review of corporate messaging platform messages",
    },
}


def assess_barbulescu_compliance(
    factor_check_results: dict[str, list[bool]],
) -> dict:
    """
    Assess email monitoring compliance against Barbulescu six-factor test.

    Args:
        factor_check_results: Dict mapping factor key to list of booleans
            (True = check passed, False = check failed).

    Returns:
        Full compliance assessment with recommendations.
    """
    results = []
    total_weighted = 0.0
    max_weighted = 0.0

    for factor_key, factor_info in BARBULESCU_FACTORS.items():
        checks = factor_check_results.get(factor_key, [])
        expected_checks = factor_info["compliance_checks"]

        # Pad or truncate to match expected length
        check_results = []
        for i, check_desc in enumerate(expected_checks):
            passed = checks[i] if i < len(checks) else False
            check_results.append({"check": check_desc, "passed": passed})

        passed_count = sum(1 for c in check_results if c["passed"])
        total_checks = len(check_results)
        factor_score = (passed_count / total_checks) * 5 if total_checks > 0 else 0

        weight = factor_info["weight"]
        weighted_score = factor_score * weight
        total_weighted += weighted_score
        max_weighted += 5 * weight

        compliance = (
            "compliant" if factor_score >= 4
            else "partial" if factor_score >= 2.5
            else "non_compliant"
        )

        results.append({
            "factor": factor_info["name"],
            "description": factor_info["description"],
            "checks": check_results,
            "passed": passed_count,
            "total": total_checks,
            "score": round(factor_score, 2),
            "weighted_score": round(weighted_score, 2),
            "compliance": compliance,
        })

    overall_pct = round((total_weighted / max_weighted) * 100, 1) if max_weighted > 0 else 0
    overall_status = (
        "compliant" if overall_pct >= 80
        else "partial_compliance" if overall_pct >= 60
        else "non_compliant"
    )

    failed_factors = [r for r in results if r["compliance"] == "non_compliant"]
    recommendations = []
    for ff in failed_factors:
        failed_checks = [c["check"] for c in ff["checks"] if not c["passed"]]
        recommendations.append({
            "factor": ff["factor"],
            "failed_checks": failed_checks,
            "action_required": f"Address {len(failed_checks)} failed checks before monitoring can proceed.",
        })

    return {
        "assessment_date": datetime.now().isoformat(),
        "framework": "Barbulescu v Romania (ECHR Grand Chamber, 2017)",
        "factor_results": results,
        "overall_percentage": overall_pct,
        "overall_status": overall_status,
        "recommendations": recommendations,
        "monitoring_may_proceed": overall_status == "compliant",
    }


def assess_monitoring_type_proportionality(
    monitoring_type: str,
    purpose: str,
    metadata_sufficient: bool,
    automated_sufficient: bool,
) -> dict:
    """
    Assess whether a specific monitoring type is proportionate to the stated purpose.

    Args:
        monitoring_type: Key from MONITORING_TYPES.
        purpose: Stated purpose for monitoring.
        metadata_sufficient: Whether metadata monitoring alone would achieve the purpose.
        automated_sufficient: Whether automated scanning would achieve the purpose.

    Returns:
        Proportionality assessment.
    """
    mt = MONITORING_TYPES.get(monitoring_type)
    if not mt:
        return {"error": f"Unknown monitoring type: {monitoring_type}"}

    intrusiveness = mt["intrusiveness"]
    proportionate = True
    reasons = []

    if intrusiveness == "high" and metadata_sufficient:
        proportionate = False
        reasons.append(
            "Content monitoring (human review) is disproportionate when metadata monitoring would achieve the stated purpose."
        )

    if intrusiveness in ("medium", "high") and automated_sufficient and monitoring_type == "email_content_human":
        proportionate = False
        reasons.append(
            "Human content review is disproportionate when automated DLP scanning would achieve the stated purpose."
        )

    return {
        "monitoring_type": mt["name"],
        "intrusiveness_level": intrusiveness,
        "stated_purpose": purpose,
        "metadata_would_suffice": metadata_sufficient,
        "automated_would_suffice": automated_sufficient,
        "proportionate": proportionate,
        "reasons": reasons if not proportionate else ["Monitoring type is proportionate to the stated purpose."],
        "recommendation": (
            f"Use {mt['name']} for the stated purpose: {purpose}."
            if proportionate
            else f"Do not use {mt['name']}. Prefer less intrusive alternative."
        ),
    }


def generate_aup_checklist(
    permits_personal_use: bool,
    monitoring_types: list[str],
) -> dict:
    """
    Generate an Acceptable Use Policy completeness checklist.

    Args:
        permits_personal_use: Whether the policy permits limited personal use.
        monitoring_types: List of monitoring type keys.

    Returns:
        AUP checklist with required sections.
    """
    required_sections = [
        {"section": "Scope", "content": "Which systems are covered", "mandatory": True},
        {"section": "Personal Use", "content": "Whether personal use is permitted and conditions", "mandatory": True},
        {"section": "Monitoring Disclosure", "content": "What monitoring takes place, when, by whom", "mandatory": True},
        {"section": "Monitoring Purpose", "content": "Specific purposes for monitoring", "mandatory": True},
        {"section": "Content Exclusions", "content": "Privileged communications excluded", "mandatory": True},
        {"section": "Access Controls", "content": "Who has access to monitoring data", "mandatory": True},
        {"section": "Consequences", "content": "What may happen following policy violation", "mandatory": True},
        {"section": "Employee Rights", "content": "Right to access data, right to challenge, grievance", "mandatory": True},
        {"section": "Retention", "content": "How long monitoring data is retained", "mandatory": True},
        {"section": "Review", "content": "When policy is reviewed and how changes communicated", "mandatory": True},
    ]

    if permits_personal_use:
        required_sections.append({
            "section": "Personal Use Monitoring",
            "content": "How personal communications during permitted time are treated",
            "mandatory": True,
        })

    monitoring_descriptions = [
        MONITORING_TYPES[mt]["description"]
        for mt in monitoring_types
        if mt in MONITORING_TYPES
    ]

    return {
        "aup_checklist": required_sections,
        "monitoring_types_to_describe": monitoring_descriptions,
        "permits_personal_use": permits_personal_use,
        "total_required_sections": len(required_sections),
    }


def main():
    """Example: Atlas Manufacturing Group email monitoring assessment."""
    print("=== Barbulescu Compliance Assessment ===")
    print("Organisation: Atlas Manufacturing Group\n")

    assessment = assess_barbulescu_compliance({
        "prior_notification": [True, True, True, True, True, True],
        "extent_of_monitoring": [True, True, False, True, True],
        "legitimate_reasons": [True, True, True],
        "less_intrusive_alternatives": [True, True, True, True, False],
        "consequences": [True, True, True, True],
        "safeguards": [True, True, True, True, True, True, True, True],
    })

    print(f"Overall Score: {assessment['overall_percentage']}%")
    print(f"Status: {assessment['overall_status']}")
    print(f"Monitoring May Proceed: {assessment['monitoring_may_proceed']}")

    for factor in assessment["factor_results"]:
        status_icon = "PASS" if factor["compliance"] == "compliant" else "PARTIAL" if factor["compliance"] == "partial" else "FAIL"
        print(f"\n[{status_icon}] {factor['factor']}: {factor['passed']}/{factor['total']} checks passed")

    if assessment["recommendations"]:
        print("\n--- Recommendations ---")
        for rec in assessment["recommendations"]:
            print(f"\n{rec['factor']}:")
            for fc in rec["failed_checks"]:
                print(f"  - {fc}")

    print(json.dumps(assessment, indent=2))


if __name__ == "__main__":
    main()
