"""
Whistleblower Data Protection Compliance Engine

Manages data protection compliance for whistleblowing channels per EU Directive
2019/1937 and GDPR. Handles access controls, retention management, and
identity protection assessment.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


NATIONAL_RETENTION = {
    "FR": {"name": "France", "law": "Loi Waserman + CNIL", "period_months": 2, "from": "investigation_closure"},
    "DE": {"name": "Germany", "law": "HinSchG Art. 11", "period_months": 36, "from": "investigation_closure"},
    "ES": {"name": "Spain", "law": "Ley 2/2023", "period_months": 3, "from": "investigation_closure"},
    "IT": {"name": "Italy", "law": "D.Lgs. 24/2023", "period_months": 60, "from": "investigation_closure"},
    "NL": {"name": "Netherlands", "law": "Wet bescherming klokkenluiders", "period_months": 24, "from": "investigation_closure"},
    "UK": {"name": "United Kingdom", "law": "No specific statutory period — apply proportionality", "period_months": 6, "from": "investigation_closure"},
}

ACCESS_ROLES = {
    "ethics_officer": {
        "name": "Ethics/Compliance Officer",
        "access": "Full access to reports and investigation files",
        "max_persons": 3,
    },
    "investigation_team": {
        "name": "Investigation Team Member",
        "access": "Specific assigned cases only; revoked on case conclusion",
        "max_persons": "case_dependent",
    },
    "dpo": {
        "name": "DPO",
        "access": "Processing records and DPIA; no routine content access",
        "max_persons": 1,
    },
    "legal_counsel": {
        "name": "Legal Counsel",
        "access": "Assigned cases where legal advice sought; subject to privilege",
        "max_persons": "case_dependent",
    },
    "ceo_board": {
        "name": "CEO/Board",
        "access": "Investigation outcomes only; no routine content access",
        "max_persons": "limited",
    },
    "line_manager": {
        "name": "Line Manager",
        "access": "NO ACCESS — frequently subject of reports",
        "max_persons": 0,
    },
    "hr": {
        "name": "HR",
        "access": "NO ACCESS unless specifically assigned to investigation by Ethics Officer",
        "max_persons": 0,
    },
    "it_admin": {
        "name": "IT Administrator",
        "access": "System administration only; content encrypted and inaccessible",
        "max_persons": "system_admin",
    },
}


def assess_channel_compliance(
    anonymous_reporting: bool,
    identified_reporting: bool,
    encryption_at_rest: bool,
    encryption_in_transit: bool,
    access_segregation: bool,
    audit_logging: bool,
    secure_feedback: bool,
    separate_from_hr: bool,
    dpia_completed: bool,
    conflict_routing: bool,
    jurisdictions: list[str],
) -> dict:
    """
    Assess whistleblowing channel compliance with Directive 2019/1937 and GDPR.

    Args:
        anonymous_reporting: Channel supports anonymous reporting.
        identified_reporting: Channel supports identified reporting.
        encryption_at_rest: Report data encrypted at rest (AES-256).
        encryption_in_transit: Communications encrypted in transit (TLS 1.3).
        access_segregation: Only designated persons can access reports.
        audit_logging: All access to reports is logged.
        secure_feedback: Reporter can receive feedback securely.
        separate_from_hr: System separated from HR systems.
        dpia_completed: DPIA conducted for the channel.
        conflict_routing: Auto-routing for reports about designated persons.
        jurisdictions: List of jurisdiction codes where the channel operates.

    Returns:
        Compliance assessment.
    """
    checks = {
        "anonymous_reporting": {
            "check": "Anonymous reporting supported",
            "required": True,
            "passed": anonymous_reporting,
            "note": "Required by FR, ES, IT national law; recommended by Directive Art. 6(2).",
        },
        "identified_reporting": {
            "check": "Identified reporting supported",
            "required": True,
            "passed": identified_reporting,
            "note": "Primary reporting mechanism under Directive Art. 9.",
        },
        "encryption_at_rest": {
            "check": "Encryption at rest (AES-256)",
            "required": True,
            "passed": encryption_at_rest,
            "note": "Required for Art. 32 security; protects confidentiality.",
        },
        "encryption_in_transit": {
            "check": "Encryption in transit (TLS 1.3)",
            "required": True,
            "passed": encryption_in_transit,
            "note": "Required for Art. 32 security.",
        },
        "access_segregation": {
            "check": "Access restricted to designated persons only",
            "required": True,
            "passed": access_segregation,
            "note": "Art. 16(1) — confidentiality of reporter identity.",
        },
        "audit_logging": {
            "check": "Audit logging for all report access",
            "required": True,
            "passed": audit_logging,
            "note": "Detects unauthorized access attempts.",
        },
        "secure_feedback": {
            "check": "Secure two-way communication with reporter",
            "required": True,
            "passed": secure_feedback,
            "note": "Art. 9(1)(b) — diligent follow-up requires communication.",
        },
        "separate_from_hr": {
            "check": "System separated from HR systems",
            "required": True,
            "passed": separate_from_hr,
            "note": "Prevents data leakage to HR/management.",
        },
        "dpia_completed": {
            "check": "DPIA completed for whistleblowing channel",
            "required": True,
            "passed": dpia_completed,
            "note": "Required: vulnerable subjects, Art. 10 data, significant consequences.",
        },
        "conflict_routing": {
            "check": "Conflict of interest routing configured",
            "required": True,
            "passed": conflict_routing,
            "note": "Reports about designated persons routed to alternative recipient.",
        },
    }

    passed = sum(1 for c in checks.values() if c["passed"])
    total = len(checks)
    compliant = all(c["passed"] for c in checks.values() if c["required"])

    # Determine strictest retention period
    retention_info = []
    for j in jurisdictions:
        nat = NATIONAL_RETENTION.get(j)
        if nat:
            retention_info.append(nat)

    strictest = min(retention_info, key=lambda x: x["period_months"]) if retention_info else None

    return {
        "assessment_date": datetime.now().isoformat(),
        "checks": checks,
        "passed": passed,
        "total": total,
        "compliant": compliant,
        "jurisdictions": jurisdictions,
        "strictest_retention": strictest,
        "recommendation": (
            "Whistleblowing channel meets all compliance requirements."
            if compliant
            else f"Channel has {total - passed} compliance gap(s). Address before operation."
        ),
    }


def calculate_retention_deadline(
    jurisdiction: str,
    investigation_closure_date: datetime,
    legal_proceedings: bool = False,
) -> dict:
    """Calculate retention deadline for a whistleblowing case."""
    nat = NATIONAL_RETENTION.get(jurisdiction)
    if not nat:
        return {"error": f"Unknown jurisdiction: {jurisdiction}"}

    if legal_proceedings:
        return {
            "jurisdiction": nat["name"],
            "retention_rule": "Legal proceedings in progress — retain until conclusion + statutory limitation",
            "deletion_deadline": "To be determined upon proceedings conclusion",
        }

    deadline = investigation_closure_date + timedelta(days=nat["period_months"] * 30)
    return {
        "jurisdiction": nat["name"],
        "law": nat["law"],
        "retention_period": f"{nat['period_months']} months from investigation closure",
        "investigation_closed": investigation_closure_date.strftime("%Y-%m-%d"),
        "deletion_deadline": deadline.strftime("%Y-%m-%d"),
    }


def main():
    """Example: Atlas Manufacturing Group whistleblowing channel assessment."""
    result = assess_channel_compliance(
        anonymous_reporting=True,
        identified_reporting=True,
        encryption_at_rest=True,
        encryption_in_transit=True,
        access_segregation=True,
        audit_logging=True,
        secure_feedback=True,
        separate_from_hr=True,
        dpia_completed=True,
        conflict_routing=True,
        jurisdictions=["DE", "FR", "UK", "NL"],
    )

    print(json.dumps(result, indent=2))
    print(f"\nCompliant: {result['compliant']}")
    print(f"Checks Passed: {result['passed']}/{result['total']}")
    if result["strictest_retention"]:
        print(f"Strictest Retention: {result['strictest_retention']['name']} — {result['strictest_retention']['period_months']} months")

    # Retention example
    print("\n=== Retention Calculation ===")
    ret = calculate_retention_deadline("FR", datetime(2026, 1, 15))
    print(json.dumps(ret, indent=2))


if __name__ == "__main__":
    main()
