#!/usr/bin/env python3
"""
Singapore PDPA Compliance Assessment Tool

Manages consent, DNC compliance, breach notification assessment,
and cross-border transfer requirements under Singapore's PDPA.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


PDPA_OBLIGATIONS = [
    "consent", "purpose_limitation", "notification", "access",
    "correction", "accuracy", "protection", "retention_limitation",
    "transfer_limitation", "breach_notification",
]

CONSENT_TYPES = {
    "express": {"section": "Section 14", "description": "Explicit consent (oral, written, electronic)"},
    "deemed_conduct": {"section": "Section 15", "description": "Deemed consent by voluntary provision"},
    "deemed_notification": {"section": "Section 15A", "description": "Deemed consent by notification"},
    "deemed_contractual": {"section": "Section 15A(2)", "description": "Deemed consent by contractual necessity"},
    "exception": {"section": "Schedules 2-4", "description": "Exception to consent requirement"},
}

SIGNIFICANT_HARM_DATA = [
    "nric_numbers", "financial_account_info", "health_info",
    "authentication_credentials", "minor_personal_data",
]


def assess_breach_notification(
    data_types_affected: list,
    individuals_affected: int,
    breach_date: str,
    awareness_date: str,
) -> dict:
    """Assess whether a breach is notifiable under Part VIA."""
    is_significant_harm = any(dt in SIGNIFICANT_HARM_DATA for dt in data_types_affected)
    is_significant_scale = individuals_affected >= 500

    notifiable_to_pdpc = is_significant_harm or is_significant_scale
    notifiable_to_individuals = is_significant_harm

    aware_date = datetime.strptime(awareness_date, "%Y-%m-%d")
    assessment_deadline = aware_date + timedelta(days=30)
    pdpc_notification_deadline = assessment_deadline + timedelta(days=3)

    return {
        "breach_date": breach_date,
        "awareness_date": awareness_date,
        "data_types_affected": data_types_affected,
        "individuals_affected": individuals_affected,
        "significant_harm": is_significant_harm,
        "significant_scale": is_significant_scale,
        "notifiable_to_pdpc": notifiable_to_pdpc,
        "notifiable_to_individuals": notifiable_to_individuals,
        "assessment_deadline": assessment_deadline.strftime("%Y-%m-%d"),
        "pdpc_notification_deadline": pdpc_notification_deadline.strftime("%Y-%m-%d"),
        "assessment_date": datetime.utcnow().isoformat(),
    }


def assess_deemed_consent_notification(
    purpose: str,
    adverse_effect_assessment: bool,
    notification_method: str,
    opt_out_period_days: int,
    opt_outs_received: int,
    total_notified: int,
) -> dict:
    """Assess validity of deemed consent by notification under Section 15A."""
    issues = []
    if not adverse_effect_assessment:
        issues.append("Adverse effect assessment not conducted (required under Section 15A)")
    if opt_out_period_days < 30:
        issues.append("Opt-out period may be insufficient (PDPC recommends minimum 30 days for significant changes)")

    deemed_consented = total_notified - opt_outs_received

    return {
        "purpose": purpose,
        "adverse_effect_assessment_conducted": adverse_effect_assessment,
        "notification_method": notification_method,
        "opt_out_period_days": opt_out_period_days,
        "total_notified": total_notified,
        "opt_outs_received": opt_outs_received,
        "deemed_consented": deemed_consented,
        "consent_rate_pct": round((deemed_consented / total_notified) * 100, 1) if total_notified > 0 else 0,
        "valid": len(issues) == 0,
        "issues": issues,
        "assessment_date": datetime.utcnow().isoformat(),
    }


def assess_dnc_compliance(
    campaign_type: str,
    target_numbers: int,
    dnc_checked: bool,
    check_date: Optional[str] = None,
    campaign_date: Optional[str] = None,
) -> dict:
    """Assess DNC Registry compliance for marketing campaigns."""
    issues = []
    if campaign_type in ["voice_call", "text_message", "fax"] and not dnc_checked:
        issues.append("DNC Registry check not performed (required for voice, text, and fax marketing)")

    if check_date and campaign_date:
        check_dt = datetime.strptime(check_date, "%Y-%m-%d")
        campaign_dt = datetime.strptime(campaign_date, "%Y-%m-%d")
        if (campaign_dt - check_dt).days > 30:
            issues.append("DNC check results expired (valid for 30 days only)")

    return {
        "campaign_type": campaign_type,
        "target_numbers": target_numbers,
        "dnc_checked": dnc_checked,
        "check_date": check_date,
        "campaign_date": campaign_date,
        "compliant": len(issues) == 0,
        "issues": issues,
        "max_penalty_sgd": 1_000_000,
        "assessment_date": datetime.utcnow().isoformat(),
    }


def calculate_penalty_exposure(
    annual_turnover_sgd: float,
    violation_type: str = "general",
    violation_count: int = 1,
) -> dict:
    """Calculate potential PDPC penalty exposure."""
    if violation_type == "serious":
        turnover_cap = annual_turnover_sgd * 0.10
        max_penalty = max(1_000_000, turnover_cap)
    else:
        max_penalty = 1_000_000

    return {
        "violation_type": violation_type,
        "annual_turnover_sgd": annual_turnover_sgd,
        "max_penalty_per_violation_sgd": round(max_penalty, 2),
        "total_exposure_sgd": round(max_penalty * violation_count, 2),
        "note": "For serious violations: higher of SGD 1M or 10% of Singapore annual turnover",
        "assessment_date": datetime.utcnow().isoformat(),
    }


if __name__ == "__main__":
    print("=== Breach Notification Assessment ===")
    result = assess_breach_notification(
        data_types_affected=["nric_numbers", "financial_account_info"],
        individuals_affected=1500,
        breach_date="2026-03-01",
        awareness_date="2026-03-05",
    )
    print(json.dumps(result, indent=2))

    print("\n=== DNC Compliance ===")
    dnc = assess_dnc_compliance("text_message", 5000, True, "2026-03-01", "2026-03-10")
    print(json.dumps(dnc, indent=2))

    print("\n=== Penalty Exposure ===")
    penalty = calculate_penalty_exposure(50_000_000, "serious", 1)
    print(json.dumps(penalty, indent=2))
