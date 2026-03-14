#!/usr/bin/env python3
"""AI Deployment Privacy Checklist Assessment Engine."""

import json
import datetime
from dataclasses import dataclass, field
from enum import Enum


class CheckStatus(Enum):
    PASSED = "Passed"
    FAILED = "Failed"
    NOT_APPLICABLE = "N/A"
    IN_PROGRESS = "In Progress"


class GateDecision(Enum):
    APPROVE = "Approved for Deployment"
    CONDITIONAL = "Conditional — Deploy with Remediation Plan"
    REJECT = "Rejected — Return to Development"


class CheckCategory(Enum):
    LEGAL = "Legal and Compliance"
    TECHNICAL = "Technical Privacy"
    TRANSPARENCY = "Transparency"
    OVERSIGHT = "Human Oversight"
    RIGHTS = "Data Subject Rights"
    OPERATIONAL = "Operational Readiness"


@dataclass
class CheckItem:
    id: int
    category: CheckCategory
    description: str
    reference: str
    status: CheckStatus = CheckStatus.IN_PROGRESS
    critical: bool = True
    notes: str = ""


@dataclass
class DeploymentAssessment:
    system_name: str
    date: str
    checks: list[CheckItem]
    gate_decision: GateDecision
    passed_count: int
    failed_count: int
    total_checks: int
    critical_failures: int
    recommendations: list[str]


CHECKLIST_TEMPLATE = [
    CheckItem(1, CheckCategory.LEGAL, "DPIA completed and approved", "GDPR Art. 35", critical=True),
    CheckItem(2, CheckCategory.LEGAL, "AI Act classification determined", "AI Act Art. 6", critical=True),
    CheckItem(3, CheckCategory.LEGAL, "Lawful basis for training data", "GDPR Art. 6(1)", critical=True),
    CheckItem(4, CheckCategory.LEGAL, "Lawful basis for inference", "GDPR Art. 6(1)", critical=True),
    CheckItem(5, CheckCategory.LEGAL, "Art. 22 assessment (automated decisions)", "GDPR Art. 22", critical=True),
    CheckItem(6, CheckCategory.LEGAL, "Vendor DPA/JCA executed", "GDPR Art. 28/26", critical=True),
    CheckItem(7, CheckCategory.TECHNICAL, "Model privacy audit completed", "Best practice", critical=True),
    CheckItem(8, CheckCategory.TECHNICAL, "Bias assessment completed", "AI Act Art. 10", critical=True),
    CheckItem(9, CheckCategory.TECHNICAL, "Input/output PII filtering", "Data minimisation", critical=False),
    CheckItem(10, CheckCategory.TECHNICAL, "Encryption at rest and transit", "GDPR Art. 32", critical=True),
    CheckItem(11, CheckCategory.TECHNICAL, "Access controls configured", "GDPR Art. 32", critical=True),
    CheckItem(12, CheckCategory.TECHNICAL, "Inference logging operational", "AI Act Art. 12", critical=False),
    CheckItem(13, CheckCategory.TRANSPARENCY, "Privacy notice updated for AI", "GDPR Arts. 13-14", critical=True),
    CheckItem(14, CheckCategory.TRANSPARENCY, "AI interaction notification", "AI Act Art. 50", critical=True),
    CheckItem(15, CheckCategory.TRANSPARENCY, "Model card documented", "Best practice", critical=False),
    CheckItem(16, CheckCategory.TRANSPARENCY, "Explainability mechanism deployed", "GDPR Art. 13(2)(f)", critical=True),
    CheckItem(17, CheckCategory.OVERSIGHT, "Human oversight implemented", "AI Act Art. 14", critical=True),
    CheckItem(18, CheckCategory.OVERSIGHT, "Reviewer training completed", "AI Act Art. 14", critical=True),
    CheckItem(19, CheckCategory.OVERSIGHT, "Contestation mechanism operational", "GDPR Art. 22(3)", critical=True),
    CheckItem(20, CheckCategory.RIGHTS, "AI explanation mechanism", "GDPR Art. 15(1)(h)", critical=True),
    CheckItem(21, CheckCategory.RIGHTS, "Training data access/deletion", "GDPR Arts. 15, 17", critical=True),
    CheckItem(22, CheckCategory.RIGHTS, "Opt-out from AI training", "GDPR Art. 21", critical=False),
    CheckItem(23, CheckCategory.OPERATIONAL, "AI incident response documented", "GDPR Art. 33-34", critical=True),
    CheckItem(24, CheckCategory.OPERATIONAL, "Monitoring dashboard deployed", "AI Act Art. 9", critical=False),
    CheckItem(25, CheckCategory.OPERATIONAL, "Drift detection configured", "AI Act Art. 15", critical=False),
]


def run_gate_review(system_name: str, check_results: dict[int, CheckStatus]) -> DeploymentAssessment:
    today = datetime.date.today().isoformat()
    checks = []

    for template_check in CHECKLIST_TEMPLATE:
        check = CheckItem(
            id=template_check.id,
            category=template_check.category,
            description=template_check.description,
            reference=template_check.reference,
            status=check_results.get(template_check.id, CheckStatus.IN_PROGRESS),
            critical=template_check.critical,
        )
        checks.append(check)

    passed = sum(1 for c in checks if c.status == CheckStatus.PASSED)
    failed = sum(1 for c in checks if c.status == CheckStatus.FAILED)
    na = sum(1 for c in checks if c.status == CheckStatus.NOT_APPLICABLE)
    total = len(checks) - na
    critical_fails = sum(1 for c in checks if c.status == CheckStatus.FAILED and c.critical)

    recommendations = []
    if critical_fails > 0:
        gate = GateDecision.REJECT
        recommendations.append(f"{critical_fails} critical check(s) failed — deployment blocked")
        for c in checks:
            if c.status == CheckStatus.FAILED and c.critical:
                recommendations.append(f"  CRITICAL: #{c.id} {c.description} ({c.reference})")
    elif failed > 0:
        gate = GateDecision.CONDITIONAL
        recommendations.append(f"{failed} non-critical check(s) failed — deploy with remediation plan")
    else:
        gate = GateDecision.APPROVE
        recommendations.append("All checks passed — approved for deployment")

    return DeploymentAssessment(
        system_name=system_name,
        date=today,
        checks=checks,
        gate_decision=gate,
        passed_count=passed,
        failed_count=failed,
        total_checks=total,
        critical_failures=critical_fails,
        recommendations=recommendations,
    )


def format_report(assessment: DeploymentAssessment) -> str:
    lines = [f"{'='*80}", "AI DEPLOYMENT PRIVACY GATE REVIEW",
             f"System: {assessment.system_name}", f"Date: {assessment.date}", f"{'='*80}"]
    lines.append(f"\nGATE DECISION: {assessment.gate_decision.value}")
    lines.append(f"Passed: {assessment.passed_count}/{assessment.total_checks}")
    lines.append(f"Failed: {assessment.failed_count} (Critical: {assessment.critical_failures})")

    for category in CheckCategory:
        cat_checks = [c for c in assessment.checks if c.category == category]
        if cat_checks:
            lines.append(f"\n## {category.value}")
            for c in cat_checks:
                icon = {"Passed": "OK", "Failed": "FAIL", "N/A": "N/A", "In Progress": "PEND"}[c.status.value]
                crit = " [CRITICAL]" if c.critical and c.status == CheckStatus.FAILED else ""
                lines.append(f"  [{icon}] #{c.id}: {c.description}{crit}")

    lines.append(f"\n## RECOMMENDATIONS")
    for r in assessment.recommendations:
        lines.append(f"  {r}")
    return "\n".join(lines)


def demo_cerebrum_ai_labs():
    results = {
        1: CheckStatus.PASSED, 2: CheckStatus.PASSED, 3: CheckStatus.PASSED,
        4: CheckStatus.PASSED, 5: CheckStatus.PASSED, 6: CheckStatus.PASSED,
        7: CheckStatus.PASSED, 8: CheckStatus.PASSED, 9: CheckStatus.FAILED,
        10: CheckStatus.PASSED, 11: CheckStatus.PASSED, 12: CheckStatus.PASSED,
        13: CheckStatus.FAILED, 14: CheckStatus.PASSED, 15: CheckStatus.FAILED,
        16: CheckStatus.PASSED, 17: CheckStatus.PASSED, 18: CheckStatus.PASSED,
        19: CheckStatus.PASSED, 20: CheckStatus.PASSED, 21: CheckStatus.PASSED,
        22: CheckStatus.PASSED, 23: CheckStatus.PASSED, 24: CheckStatus.PASSED,
        25: CheckStatus.IN_PROGRESS,
    }
    assessment = run_gate_review("Cerebrum AI Labs — Customer Intent Classifier v2", results)
    print(format_report(assessment))


if __name__ == "__main__":
    demo_cerebrum_ai_labs()
