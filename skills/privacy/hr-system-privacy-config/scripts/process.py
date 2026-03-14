"""
HR System Privacy Configuration Audit Engine

Audits role-based access controls, retention automation, and cross-border
transfer configuration for enterprise HR systems.
"""

import json
from datetime import datetime
from typing import Optional


RBAC_MATRIX = {
    "employee_self": {
        "name": "Employee (Self-Service)",
        "personal_details": "own",
        "salary": "own",
        "performance": "own",
        "absence": "own",
        "health": "own_oh_reports",
        "disciplinary": "own",
        "recruitment": "own_application",
    },
    "line_manager": {
        "name": "Line Manager",
        "personal_details": "direct_reports_limited",
        "salary": "none",
        "performance": "direct_reports",
        "absence": "direct_reports_dates_only",
        "health": "none",
        "disciplinary": "none",
        "recruitment": "hiring_candidates",
    },
    "hr_bp": {
        "name": "HR Business Partner",
        "personal_details": "client_group_full",
        "salary": "client_group_full",
        "performance": "client_group_full",
        "absence": "client_group_dates_fit_status",
        "health": "fit_unfit_only",
        "disciplinary": "client_group_full",
        "recruitment": "client_group_all",
    },
    "payroll": {
        "name": "Payroll Administrator",
        "personal_details": "minimal_payroll",
        "salary": "all_full",
        "performance": "none",
        "absence": "ssp_relevant_only",
        "health": "none",
        "disciplinary": "none",
        "recruitment": "none",
    },
    "benefits_admin": {
        "name": "Benefits Administrator",
        "personal_details": "minimal_benefits",
        "salary": "salary_bands",
        "performance": "none",
        "absence": "none",
        "health": "none",
        "disciplinary": "none",
        "recruitment": "none",
    },
    "it_admin": {
        "name": "IT Administrator",
        "personal_details": "system_access_only",
        "salary": "none",
        "performance": "none",
        "absence": "none",
        "health": "none",
        "disciplinary": "none",
        "recruitment": "none",
    },
    "dpo": {
        "name": "DPO",
        "personal_details": "audit_only",
        "salary": "audit_only",
        "performance": "audit_only",
        "absence": "audit_only",
        "health": "audit_only",
        "disciplinary": "audit_only",
        "recruitment": "audit_only",
    },
}

RETENTION_SCHEDULE = {
    "recruitment_unsuccessful": {"period": "6 months", "trigger": "application_decision_date"},
    "employment_contract": {"period": "6 years post-termination", "trigger": "termination_date"},
    "payroll_tax": {"period": "6-7 years", "trigger": "tax_year_end"},
    "performance_reviews": {"period": "2 years post-termination", "trigger": "termination_date"},
    "absence_records": {"period": "2 years current + 1 year archive", "trigger": "absence_year_end"},
    "disciplinary_warnings": {"period": "6-12 months per policy", "trigger": "warning_date"},
    "disciplinary_dismissal": {"period": "6 years", "trigger": "dismissal_date"},
    "health_standard": {"period": "6 years post-termination", "trigger": "termination_date"},
    "health_occupational": {"period": "40 years", "trigger": "exposure_end_date"},
    "training_records": {"period": "3 years post-termination", "trigger": "termination_date"},
    "dsar_records": {"period": "2 years", "trigger": "response_date"},
}


def audit_access_controls(
    actual_access: dict[str, dict[str, str]],
) -> dict:
    """
    Audit actual HR system access configuration against the RBAC matrix.

    Args:
        actual_access: Dict mapping role keys to dicts of data category → access level.

    Returns:
        Audit results with violations.
    """
    violations = []
    compliant_roles = []

    for role_key, role_config in RBAC_MATRIX.items():
        actual_role = actual_access.get(role_key, {})
        role_violations = []

        for data_category in ["personal_details", "salary", "performance", "absence", "health", "disciplinary", "recruitment"]:
            expected = role_config.get(data_category, "none")
            actual = actual_role.get(data_category, "not_configured")

            if expected == "none" and actual not in ("none", "not_configured"):
                role_violations.append({
                    "data_category": data_category,
                    "expected_access": expected,
                    "actual_access": actual,
                    "severity": "critical" if data_category in ("health", "disciplinary", "salary") else "high",
                    "remediation": f"Remove {data_category} access for {role_config['name']}.",
                })

        if role_violations:
            violations.extend(role_violations)
        else:
            compliant_roles.append(role_config["name"])

    return {
        "audit_date": datetime.now().isoformat(),
        "roles_audited": len(RBAC_MATRIX),
        "compliant_roles": compliant_roles,
        "violations": violations,
        "critical_violations": len([v for v in violations if v["severity"] == "critical"]),
        "high_violations": len([v for v in violations if v["severity"] == "high"]),
        "compliant": len(violations) == 0,
    }


def audit_retention_config(
    configured_rules: dict[str, Optional[str]],
) -> dict:
    """
    Audit HR system retention configuration against the retention schedule.

    Args:
        configured_rules: Dict mapping retention category keys to configured period
            (None if not configured).

    Returns:
        Retention audit results.
    """
    gaps = []
    configured = []

    for category, schedule in RETENTION_SCHEDULE.items():
        config = configured_rules.get(category)
        if config is None:
            gaps.append({
                "category": category,
                "required_period": schedule["period"],
                "trigger": schedule["trigger"],
                "status": "NOT_CONFIGURED",
                "remediation": f"Configure automated purge rule: {schedule['period']} from {schedule['trigger']}.",
            })
        else:
            configured.append({
                "category": category,
                "required_period": schedule["period"],
                "configured_period": config,
                "status": "CONFIGURED",
            })

    return {
        "audit_date": datetime.now().isoformat(),
        "total_categories": len(RETENTION_SCHEDULE),
        "configured": len(configured),
        "gaps": len(gaps),
        "retention_gaps": gaps,
        "configured_rules": configured,
        "compliant": len(gaps) == 0,
    }


def generate_privacy_config_report(
    organisation: str,
    hr_system: str,
    actual_access: dict[str, dict[str, str]],
    configured_retention: dict[str, Optional[str]],
    data_centre_location: str,
    audit_logging_enabled: bool,
    dsar_export_tested: bool,
) -> dict:
    """Generate a complete HR system privacy configuration audit report."""
    access_audit = audit_access_controls(actual_access)
    retention_audit = audit_retention_config(configured_retention)

    overall_compliant = (
        access_audit["compliant"]
        and retention_audit["compliant"]
        and audit_logging_enabled
        and dsar_export_tested
    )

    return {
        "report_date": datetime.now().isoformat(),
        "organisation": organisation,
        "hr_system": hr_system,
        "access_control_audit": access_audit,
        "retention_audit": retention_audit,
        "data_centre_location": data_centre_location,
        "audit_logging_enabled": audit_logging_enabled,
        "dsar_export_tested": dsar_export_tested,
        "overall_compliant": overall_compliant,
        "priority_actions": (
            [v for v in access_audit["violations"] if v["severity"] == "critical"]
            + [g for g in retention_audit["retention_gaps"]]
        ),
    }


def main():
    """Example: Atlas Manufacturing Group HR system audit."""
    report = generate_privacy_config_report(
        organisation="Atlas Manufacturing Group",
        hr_system="SAP SuccessFactors",
        actual_access={
            "line_manager": {
                "personal_details": "direct_reports_limited",
                "salary": "none",
                "performance": "direct_reports",
                "absence": "direct_reports_dates_only",
                "health": "none",
                "disciplinary": "none",
                "recruitment": "hiring_candidates",
            },
            "payroll": {
                "personal_details": "minimal_payroll",
                "salary": "all_full",
                "performance": "none",
                "absence": "ssp_relevant_only",
                "health": "none",
                "disciplinary": "none",
                "recruitment": "none",
            },
        },
        configured_retention={
            "recruitment_unsuccessful": "6 months",
            "employment_contract": "6 years post-termination",
            "payroll_tax": "7 years",
            "performance_reviews": "2 years post-termination",
            "absence_records": None,
            "training_records": None,
        },
        data_centre_location="EU (Frankfurt, Germany)",
        audit_logging_enabled=True,
        dsar_export_tested=True,
    )

    print(json.dumps(report, indent=2))
    print(f"\nOverall Compliant: {report['overall_compliant']}")
    print(f"Priority Actions: {len(report['priority_actions'])}")


if __name__ == "__main__":
    main()
