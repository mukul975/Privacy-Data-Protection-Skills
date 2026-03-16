#!/usr/bin/env python3
"""
Audit Follow-Up and Verification Processor

Manages follow-up scheduling, verification testing, finding closure,
escalation of unremediated findings, and follow-up status reporting.
"""

import json
import os
from datetime import datetime, timedelta
from typing import Any


SEVERITY_FOLLOW_UP = {
    "critical": {
        "follow_up_days": 30,
        "retest_days": 15,
        "max_extensions": 1,
        "escalation_overdue_days": 30,
    },
    "high": {
        "follow_up_days": 60,
        "retest_days": 30,
        "max_extensions": 2,
        "escalation_overdue_days": 45,
    },
    "medium": {
        "follow_up_days": 90,
        "retest_days": 45,
        "max_extensions": 2,
        "escalation_overdue_days": 60,
    },
    "low": {
        "follow_up_days": 180,
        "retest_days": 90,
        "max_extensions": 3,
        "escalation_overdue_days": 120,
    },
}

VERIFICATION_OUTCOMES = ("pass", "partial_pass", "fail")


def schedule_follow_up(
    finding: dict[str, Any],
) -> dict[str, Any]:
    """
    Schedule a follow-up verification for an audit finding.

    Args:
        finding: Finding record with severity, target_date, and status.

    Returns:
        Follow-up schedule record.
    """
    severity = finding.get("severity", "medium")
    config = SEVERITY_FOLLOW_UP.get(severity, SEVERITY_FOLLOW_UP["medium"])

    target_date_str = finding.get("target_date", "")
    if target_date_str:
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()
    else:
        target_date = datetime.now().date()

    follow_up_date = target_date + timedelta(days=config["follow_up_days"])

    return {
        "finding_id": finding.get("finding_id", ""),
        "severity": severity,
        "original_target_date": target_date_str,
        "follow_up_date": follow_up_date.strftime("%Y-%m-%d"),
        "retest_interval_days": config["retest_days"],
        "max_extensions": config["max_extensions"],
        "extensions_used": 0,
        "verification_attempts": 0,
        "status": "scheduled",
    }


def record_verification(
    finding_id: str,
    verification_owner: str,
    method: str,
    tests_performed: list[dict[str, Any]],
    outcome: str,
    evidence_refs: list[str],
    notes: str = "",
) -> dict[str, Any]:
    """
    Record the results of a verification testing event.

    Args:
        finding_id: The finding being verified.
        verification_owner: Auditor performing the verification.
        method: Primary verification method (reperformance, inspection, observation, analytics, inquiry).
        tests_performed: List of test records with procedure, result, and evidence.
        outcome: Verification outcome (pass, partial_pass, fail).
        evidence_refs: List of evidence reference IDs reviewed.
        notes: Additional verification notes.

    Returns:
        Verification record.
    """
    if outcome not in VERIFICATION_OUTCOMES:
        outcome = "fail"

    tests_passed = sum(1 for t in tests_performed if t.get("result") == "pass")
    tests_total = len(tests_performed)

    return {
        "finding_id": finding_id,
        "verification_date": datetime.now().strftime("%Y-%m-%d"),
        "verification_owner": verification_owner,
        "method": method,
        "tests_performed": tests_total,
        "tests_passed": tests_passed,
        "pass_rate": round(tests_passed / tests_total * 100, 1) if tests_total > 0 else 0,
        "outcome": outcome,
        "evidence_refs": evidence_refs,
        "notes": notes,
        "test_details": tests_performed,
    }


def evaluate_closure(
    finding: dict[str, Any],
    verification: dict[str, Any],
) -> dict[str, Any]:
    """
    Evaluate whether a finding meets closure criteria based on verification results.

    Args:
        finding: The audit finding record.
        verification: The verification result record.

    Returns:
        Closure evaluation with recommendation.
    """
    outcome = verification.get("outcome", "fail")

    closure_criteria = {
        "remediation_complete": outcome in ("pass", "partial_pass"),
        "evidence_provided": len(verification.get("evidence_refs", [])) > 0,
        "independent_verification": verification.get("verification_owner", "") != finding.get("remediation_owner", "UNKNOWN"),
        "root_cause_addressed": outcome == "pass",
        "sustainable": outcome == "pass" and verification.get("pass_rate", 0) == 100,
    }

    all_met = all(closure_criteria.values())

    if all_met:
        recommendation = "close"
        next_action = "Prepare closure memo and archive evidence"
    elif outcome == "partial_pass":
        recommendation = "targeted_remediation"
        failed_criteria = [k for k, v in closure_criteria.items() if not v]
        next_action = f"Re-remediate gaps: {', '.join(failed_criteria)}"
    else:
        recommendation = "reopen_and_escalate"
        next_action = "Reopen finding, conduct root cause review, require revised plan"

    target_date_str = finding.get("target_date", "")
    registered_str = finding.get("registered_date", "")
    days_to_close = None
    within_target = None

    if outcome == "pass" and registered_str:
        try:
            reg_date = datetime.strptime(registered_str, "%Y-%m-%d").date()
            days_to_close = (datetime.now().date() - reg_date).days
        except ValueError:
            pass

    if outcome == "pass" and target_date_str:
        try:
            target_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()
            within_target = datetime.now().date() <= target_date
        except ValueError:
            pass

    return {
        "finding_id": finding.get("finding_id", ""),
        "verification_date": verification.get("verification_date", ""),
        "closure_criteria": closure_criteria,
        "all_criteria_met": all_met,
        "recommendation": recommendation,
        "next_action": next_action,
        "days_to_close": days_to_close,
        "within_target": within_target,
    }


def check_escalation_needed(
    finding: dict[str, Any],
    verification_history: list[dict[str, Any]],
) -> dict[str, Any] | None:
    """
    Determine if a finding requires escalation based on overdue status or repeated failures.

    Args:
        finding: The audit finding record.
        verification_history: List of prior verification records for this finding.

    Returns:
        Escalation action if needed, None otherwise.
    """
    severity = finding.get("severity", "medium")
    config = SEVERITY_FOLLOW_UP.get(severity, SEVERITY_FOLLOW_UP["medium"])

    target_str = finding.get("target_date", "")
    if not target_str:
        return None

    try:
        target_date = datetime.strptime(target_str, "%Y-%m-%d").date()
        days_overdue = (datetime.now().date() - target_date).days
    except ValueError:
        return None

    if days_overdue <= 0:
        return None

    failure_count = sum(
        1 for v in verification_history if v.get("outcome") == "fail"
    )

    escalation = None

    if failure_count >= 2:
        escalation = {
            "finding_id": finding.get("finding_id", ""),
            "severity": severity,
            "trigger": f"Verification failed {failure_count} times",
            "days_overdue": days_overdue,
            "escalate_to": "DPO and CPO — root cause review required",
            "urgency": "immediate",
        }
    elif days_overdue > config["escalation_overdue_days"]:
        if severity == "critical":
            escalate_to = "CPO, CISO, and Board Audit Committee"
        elif severity == "high":
            escalate_to = "DPO, CPO, and Audit Committee"
        else:
            escalate_to = "Management"

        escalation = {
            "finding_id": finding.get("finding_id", ""),
            "severity": severity,
            "trigger": f"Overdue by {days_overdue} days (threshold: {config['escalation_overdue_days']})",
            "days_overdue": days_overdue,
            "escalate_to": escalate_to,
            "urgency": "within 5 business days" if severity in ("critical", "high") else "next monthly report",
        }

    return escalation


def generate_follow_up_report(
    findings: list[dict[str, Any]],
    verifications: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Generate a periodic follow-up status report.

    Args:
        findings: List of all open audit findings.
        verifications: List of all verification records.

    Returns:
        Follow-up summary report.
    """
    today = datetime.now().date()

    total_open = len(findings)
    overdue = 0
    by_severity = {"critical": 0, "high": 0, "medium": 0, "low": 0}

    for f in findings:
        sev = f.get("severity", "medium")
        by_severity[sev] = by_severity.get(sev, 0) + 1

        target = f.get("target_date", "")
        if target:
            try:
                if datetime.strptime(target, "%Y-%m-%d").date() < today:
                    overdue += 1
            except ValueError:
                pass

    this_month_verifications = []
    for v in verifications:
        vdate = v.get("verification_date", "")
        if vdate:
            try:
                vd = datetime.strptime(vdate, "%Y-%m-%d").date()
                if vd.month == today.month and vd.year == today.year:
                    this_month_verifications.append(v)
            except ValueError:
                pass

    closures = sum(1 for v in this_month_verifications if v.get("outcome") == "pass")
    partial = sum(1 for v in this_month_verifications if v.get("outcome") == "partial_pass")
    failures = sum(1 for v in this_month_verifications if v.get("outcome") == "fail")

    pass_rate = round(
        closures / len(this_month_verifications) * 100, 1
    ) if this_month_verifications else 0

    return {
        "report_date": today.isoformat(),
        "reporting_period": f"{today.strftime('%B %Y')}",
        "summary": {
            "total_open_findings": total_open,
            "by_severity": by_severity,
            "overdue": overdue,
        },
        "verification_activity": {
            "verifications_this_month": len(this_month_verifications),
            "closures": closures,
            "partial_passes": partial,
            "failures": failures,
            "pass_rate": pass_rate,
        },
    }


if __name__ == "__main__":
    finding = {
        "finding_id": "RA-2025-017",
        "title": "Incomplete vendor sub-processor notification",
        "severity": "high",
        "status": "pending_verification",
        "registered_date": "2025-09-15",
        "target_date": "2025-11-14",
        "remediation_owner": "Vendor Manager",
    }

    schedule = schedule_follow_up(finding)
    print(f"Follow-up scheduled: {schedule['follow_up_date']}")

    verification = record_verification(
        finding_id="RA-2025-017",
        verification_owner="Senior Auditor",
        method="inspection",
        tests_performed=[
            {"test": "Review updated DPAs for sub-processor clauses", "result": "pass", "evidence": "EV-2026-101"},
            {"test": "Verify notification workflow in vendor management system", "result": "pass", "evidence": "EV-2026-102"},
            {"test": "Sample 10 recent sub-processor changes for notification evidence", "result": "pass", "evidence": "EV-2026-103"},
        ],
        outcome="pass",
        evidence_refs=["EV-2026-101", "EV-2026-102", "EV-2026-103"],
        notes="All sub-processor notification workflows verified operational",
    )

    print(f"Verification outcome: {verification['outcome']}")
    print(f"Tests passed: {verification['tests_passed']}/{verification['tests_performed']}")

    closure = evaluate_closure(finding, verification)
    print(f"Closure recommendation: {closure['recommendation']}")
    print(f"Next action: {closure['next_action']}")
