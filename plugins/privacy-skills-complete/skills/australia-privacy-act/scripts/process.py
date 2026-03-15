#!/usr/bin/env python3
"""
Australia Privacy Act Compliance Assessment Tool

Assesses compliance with Australia's Privacy Act 1988 including 2024 reform amendments,
manages APP compliance, automated decision-making assessment, and breach notification.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


APPS = {
    "APP1": "Open and transparent management",
    "APP2": "Anonymity and pseudonymity",
    "APP3": "Collection of solicited personal information",
    "APP4": "Dealing with unsolicited personal information",
    "APP5": "Notification of collection",
    "APP6": "Use or disclosure",
    "APP7": "Direct marketing",
    "APP8": "Cross-border disclosure",
    "APP9": "Government identifiers",
    "APP10": "Quality of personal information",
    "APP11": "Security of personal information",
    "APP12": "Access to personal information",
    "APP13": "Correction of personal information",
}


def assess_breach_notification(
    information_types: list,
    individuals_affected: int,
    likelihood_of_serious_harm: str,
    remedial_action_taken: bool,
    awareness_date: str,
) -> dict:
    """Assess whether a breach is notifiable under Part IIIC."""
    is_eligible = likelihood_of_serious_harm in ["likely", "very_likely"] and not remedial_action_taken

    aware_dt = datetime.strptime(awareness_date, "%Y-%m-%d")
    assessment_deadline = aware_dt + timedelta(days=30)

    return {
        "information_types": information_types,
        "individuals_affected": individuals_affected,
        "likelihood_of_serious_harm": likelihood_of_serious_harm,
        "remedial_action_prevents_harm": remedial_action_taken,
        "eligible_data_breach": is_eligible,
        "awareness_date": awareness_date,
        "assessment_deadline": assessment_deadline.strftime("%Y-%m-%d"),
        "notification_required": is_eligible,
        "notify_oaic": is_eligible,
        "notify_individuals": is_eligible,
    }


def assess_automated_decision(
    system_name: str,
    data_inputs: list,
    decision_type: str,
    significantly_affects_rights: bool,
    human_review_available: bool,
    impact_assessment_conducted: bool,
) -> dict:
    """Assess automated decision-making compliance under 2024 amendments."""
    issues = []
    if significantly_affects_rights:
        if not human_review_available:
            issues.append("Human review mechanism not available for rights-affecting automated decision")
        if not impact_assessment_conducted:
            issues.append("Privacy impact assessment not conducted before deployment")

    return {
        "system_name": system_name,
        "data_inputs": data_inputs,
        "decision_type": decision_type,
        "significantly_affects_rights": significantly_affects_rights,
        "transparency_obligations_apply": significantly_affects_rights,
        "human_review_available": human_review_available,
        "impact_assessment_conducted": impact_assessment_conducted,
        "compliant": len(issues) == 0,
        "issues": issues,
        "required_transparency": [
            "Inform individual that automated decision has been made",
            "Disclose types of personal information used",
            "Explain how the decision was reached",
        ] if significantly_affects_rights else [],
    }


def calculate_penalty_exposure(
    adjusted_turnover_aud: float,
    benefit_obtained_aud: float = 0,
    violation_count: int = 1,
) -> dict:
    """Calculate potential OAIC civil penalty exposure under 2024 amendments."""
    cap_50m = 50_000_000
    cap_3x_benefit = benefit_obtained_aud * 3
    cap_30pct_turnover = adjusted_turnover_aud * 0.30
    max_penalty = max(cap_50m, cap_3x_benefit, cap_30pct_turnover)

    return {
        "adjusted_turnover_aud": adjusted_turnover_aud,
        "benefit_obtained_aud": benefit_obtained_aud,
        "penalty_caps": {
            "aud_50_million": cap_50m,
            "three_times_benefit": cap_3x_benefit,
            "thirty_pct_turnover": cap_30pct_turnover,
        },
        "max_penalty_per_violation_aud": round(max_penalty, 2),
        "total_exposure_aud": round(max_penalty * violation_count, 2),
        "violation_count": violation_count,
    }


def assess_app_compliance(compliance_status: dict) -> dict:
    """Assess overall APP compliance."""
    compliant = []
    non_compliant = []
    for app_id, status in compliance_status.items():
        if app_id in APPS:
            if status:
                compliant.append({"app": app_id, "subject": APPS[app_id]})
            else:
                non_compliant.append({"app": app_id, "subject": APPS[app_id]})

    return {
        "total_apps": len(APPS),
        "compliant": len(compliant),
        "non_compliant_count": len(non_compliant),
        "non_compliant_details": non_compliant,
        "compliance_rate": round(len(compliant) / len(APPS) * 100, 1),
    }


if __name__ == "__main__":
    print("=== Breach Notification Assessment ===")
    result = assess_breach_notification(
        ["names", "email_addresses", "financial_info"],
        5000, "likely", False, "2026-03-01",
    )
    print(json.dumps(result, indent=2))

    print("\n=== Automated Decision Assessment ===")
    auto = assess_automated_decision(
        "Credit scoring engine", ["payment_history", "revenue", "industry"],
        "credit_limit_determination", True, True, True,
    )
    print(json.dumps(auto, indent=2))

    print("\n=== Penalty Exposure ===")
    penalty = calculate_penalty_exposure(200_000_000, 5_000_000, 1)
    print(json.dumps(penalty, indent=2))
