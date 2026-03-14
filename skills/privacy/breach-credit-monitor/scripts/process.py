#!/usr/bin/env python3
"""
Breach Credit Monitoring Manager

Manages vendor coordination, enrollment tracking, cost estimation,
and coverage metrics for post-breach identity protection services.
"""

import json
from datetime import datetime, timezone, timedelta


VENDOR_CATALOG = {
    "experian_identityworks": {
        "name": "Experian IdentityWorks",
        "monthly_cost_eur": 8.50,
        "monthly_cost_usd": 9.25,
        "setup_cost_eur": 15000,
        "activation_time_hours": 48,
        "languages": ["de", "en", "fr", "nl", "es", "it", "pl"],
        "coverage_eu": True,
        "coverage_us": True,
        "insurance_eur": 25000,
        "insurance_usd": 1000000,
        "dark_web_monitoring": True,
        "credit_bureaus_monitored": {"EU": ["SCHUFA", "Experian"], "US": ["Experian", "Equifax", "TransUnion"]},
    },
    "transunion_trueidentity": {
        "name": "TransUnion TrueIdentity",
        "monthly_cost_eur": 0,
        "monthly_cost_usd": 7.80,
        "setup_cost_eur": 0,
        "activation_time_hours": 72,
        "languages": ["en", "fr"],
        "coverage_eu": False,
        "coverage_us": True,
        "insurance_eur": 0,
        "insurance_usd": 1000000,
        "dark_web_monitoring": True,
        "credit_bureaus_monitored": {"US": ["TransUnion"]},
    },
    "kroll_identity_monitoring": {
        "name": "Kroll Identity Monitoring",
        "monthly_cost_eur": 9.00,
        "monthly_cost_usd": 9.75,
        "setup_cost_eur": 20000,
        "activation_time_hours": 48,
        "languages": ["de", "en", "fr", "nl", "ja", "ko"],
        "coverage_eu": True,
        "coverage_us": True,
        "insurance_eur": 25000,
        "insurance_usd": 1000000,
        "dark_web_monitoring": True,
        "credit_bureaus_monitored": {"EU": ["SCHUFA", "Experian"], "US": ["Experian", "Equifax", "TransUnion"]},
    },
}


def estimate_cost(
    affected_count: int,
    estimated_enrollment_rate: float,
    coverage_months: int,
    vendor_key: str,
    currency: str = "EUR",
    support_months: int = 3,
    support_monthly_cost: float = 15000,
) -> dict:
    """
    Estimate total credit monitoring program cost.

    Args:
        affected_count: Total number of affected individuals.
        estimated_enrollment_rate: Expected enrollment percentage (0-100).
        coverage_months: Duration of monitoring in months.
        vendor_key: Vendor identifier from VENDOR_CATALOG.
        currency: EUR or USD.
        support_months: Duration of enrollment support staffing.
        support_monthly_cost: Monthly cost of support team.

    Returns:
        Detailed cost breakdown.
    """
    vendor = VENDOR_CATALOG.get(vendor_key)
    if not vendor:
        raise ValueError(f"Unknown vendor: {vendor_key}")

    enrollees = int(affected_count * (estimated_enrollment_rate / 100))
    monthly_cost = vendor["monthly_cost_eur"] if currency == "EUR" else vendor["monthly_cost_usd"]
    setup_cost = vendor["setup_cost_eur"] if currency == "EUR" else vendor["setup_cost_eur"] * 1.08

    monitoring_cost = enrollees * monthly_cost * coverage_months
    support_cost = support_months * support_monthly_cost
    total = setup_cost + monitoring_cost + support_cost

    return {
        "vendor": vendor["name"],
        "currency": currency,
        "affected_count": affected_count,
        "estimated_enrollment_rate": f"{estimated_enrollment_rate}%",
        "estimated_enrollees": enrollees,
        "coverage_months": coverage_months,
        "cost_breakdown": {
            "vendor_setup": round(setup_cost, 2),
            "monthly_per_individual": monthly_cost,
            "total_monitoring": round(monitoring_cost, 2),
            "enrollment_support": round(support_cost, 2),
            "total_estimated_cost": round(total, 2),
        },
        "insurance_coverage": {
            "per_individual": vendor[f"insurance_{currency.lower()}"],
            "dark_web_monitoring": vendor["dark_web_monitoring"],
        },
        "insurance_recovery": {
            "policy": "Allianz Cyber Enterprise SPG-CYB-2025-001",
            "coverage_limit": 2000000 if currency == "EUR" else 2160000,
            "deductible": 50000 if currency == "EUR" else 54000,
            "estimated_recovery": round(min(total - 50000, 2000000), 2) if currency == "EUR" else round(min(total - 54000, 2160000), 2),
        },
    }


def generate_enrollment_report(
    affected_count: int,
    enrolled_count: int,
    days_since_notification: int,
    alerts_generated: int = 0,
    claims_filed: int = 0,
) -> dict:
    """Generate an enrollment tracking report."""
    enrollment_rate = (enrolled_count / affected_count * 100) if affected_count > 0 else 0

    if days_since_notification <= 7:
        target_rate = 20
    elif days_since_notification <= 14:
        target_rate = 40
    elif days_since_notification <= 30:
        target_rate = 55
    elif days_since_notification <= 60:
        target_rate = 65
    else:
        target_rate = 70

    return {
        "report_date": datetime.now(timezone.utc).isoformat(),
        "days_since_notification": days_since_notification,
        "enrollment_window_remaining_days": max(0, 90 - days_since_notification),
        "metrics": {
            "total_affected": affected_count,
            "enrolled": enrolled_count,
            "enrollment_rate": f"{enrollment_rate:.1f}%",
            "target_rate": f"{target_rate}%",
            "on_track": enrollment_rate >= target_rate,
        },
        "monitoring_activity": {
            "alerts_generated": alerts_generated,
            "claims_filed": claims_filed,
        },
        "actions_needed": (
            [] if enrollment_rate >= target_rate else
            [f"Send follow-up reminder — current rate {enrollment_rate:.1f}% is below target {target_rate}%"]
        ),
    }


def main():
    print("=" * 70)
    print("CREDIT MONITORING COST ESTIMATE")
    print("=" * 70)

    cost = estimate_cost(
        affected_count=15230,
        estimated_enrollment_rate=70,
        coverage_months=12,
        vendor_key="experian_identityworks",
        currency="EUR",
    )
    print(json.dumps(cost, indent=2))

    print("\n" + "=" * 70)
    print("ENROLLMENT REPORT — Week 2")
    print("=" * 70)

    report = generate_enrollment_report(
        affected_count=15230,
        enrolled_count=6218,
        days_since_notification=14,
        alerts_generated=3,
        claims_filed=0,
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
