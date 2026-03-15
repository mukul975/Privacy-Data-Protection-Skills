"""
NIST Privacy Framework GOVERN Function — Governance Assessment Tool

Evaluates the maturity of privacy governance structures across
GV.AT (Awareness/Training), GV.MT (Monitoring/Review),
GV.PO (Policy), and GV.RR (Roles/Responsibilities).
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import json


class MaturityLevel(Enum):
    INITIAL = 1
    MANAGED = 2
    DEFINED = 3
    QUANTITATIVELY_MANAGED = 4
    OPTIMIZING = 5


@dataclass
class GovernanceControl:
    subcategory: str
    description: str
    maturity: MaturityLevel
    evidence: str
    gaps: list[str]
    recommendations: list[str]


@dataclass
class TrainingMetrics:
    total_staff: int
    trained_staff: int
    specialist_certified: int
    total_specialists: int
    avg_quiz_score: float
    new_hire_avg_days: float


@dataclass
class PolicyInventory:
    policy_name: str
    owner: str
    last_reviewed: datetime
    review_cycle_months: int
    acknowledgment_rate: float
    status: str  # current, overdue, draft


class GovernFunctionAssessor:
    """
    Assess and score the GOVERN function implementation maturity.
    """

    def __init__(self, organization: str):
        self.organization = organization
        self.controls: list[GovernanceControl] = []
        self.training_metrics: TrainingMetrics | None = None
        self.policies: list[PolicyInventory] = []

    def assess_awareness_training(
        self, metrics: TrainingMetrics
    ) -> list[GovernanceControl]:
        """Assess GV.AT subcategories."""
        self.training_metrics = metrics
        controls = []

        # GV.AT-P1: Workforce training
        completion_rate = metrics.trained_staff / metrics.total_staff if metrics.total_staff > 0 else 0
        if completion_rate >= 0.95 and metrics.avg_quiz_score >= 85:
            maturity = MaturityLevel.OPTIMIZING
        elif completion_rate >= 0.90:
            maturity = MaturityLevel.QUANTITATIVELY_MANAGED
        elif completion_rate >= 0.80:
            maturity = MaturityLevel.DEFINED
        elif completion_rate >= 0.50:
            maturity = MaturityLevel.MANAGED
        else:
            maturity = MaturityLevel.INITIAL

        gaps = []
        recs = []
        if completion_rate < 0.95:
            gaps.append(f"Training completion rate is {completion_rate*100:.1f}% (target: 95%)")
            recs.append("Implement automated training reminders and escalation")
        if metrics.new_hire_avg_days > 30:
            gaps.append(f"New hire training takes {metrics.new_hire_avg_days:.0f} days (target: <30)")
            recs.append("Add privacy training to onboarding checklist with 14-day deadline")

        controls.append(GovernanceControl(
            subcategory="GV.AT-P1",
            description="Workforce informed and trained on privacy roles",
            maturity=maturity,
            evidence=f"Completion: {completion_rate*100:.1f}%, Avg score: {metrics.avg_quiz_score:.1f}%",
            gaps=gaps,
            recommendations=recs,
        ))

        # GV.AT-P3: Privacy personnel specialization
        cert_rate = metrics.specialist_certified / metrics.total_specialists if metrics.total_specialists > 0 else 0
        if cert_rate >= 0.80:
            maturity = MaturityLevel.OPTIMIZING
        elif cert_rate >= 0.60:
            maturity = MaturityLevel.DEFINED
        elif cert_rate >= 0.30:
            maturity = MaturityLevel.MANAGED
        else:
            maturity = MaturityLevel.INITIAL

        controls.append(GovernanceControl(
            subcategory="GV.AT-P3",
            description="Privacy personnel understand roles and have certifications",
            maturity=maturity,
            evidence=f"Certification rate: {cert_rate*100:.1f}% ({metrics.specialist_certified}/{metrics.total_specialists})",
            gaps=[f"Certification rate {cert_rate*100:.1f}% below 80% target"] if cert_rate < 0.80 else [],
            recommendations=["Fund CIPP/CIPM/CIPT certifications for privacy team"] if cert_rate < 0.80 else [],
        ))

        self.controls.extend(controls)
        return controls

    def assess_policies(self, policies: list[PolicyInventory]) -> list[GovernanceControl]:
        """Assess GV.PO subcategories."""
        self.policies = policies
        controls = []

        overdue = [p for p in policies if p.status == "overdue"]
        low_ack = [p for p in policies if p.acknowledgment_rate < 0.95]

        if not overdue and not low_ack:
            maturity = MaturityLevel.OPTIMIZING
        elif len(overdue) <= 1 and len(low_ack) <= 2:
            maturity = MaturityLevel.QUANTITATIVELY_MANAGED
        elif len(overdue) <= 3:
            maturity = MaturityLevel.DEFINED
        else:
            maturity = MaturityLevel.MANAGED

        gaps = []
        recs = []
        if overdue:
            gaps.append(f"{len(overdue)} policies overdue for review: {', '.join(p.policy_name for p in overdue)}")
            recs.append("Schedule immediate review for overdue policies")
        if low_ack:
            gaps.append(f"{len(low_ack)} policies with acknowledgment rate below 95%")
            recs.append("Send reminder campaigns for policy acknowledgment")

        controls.append(GovernanceControl(
            subcategory="GV.PO-P1",
            description="Privacy values and policies established and communicated",
            maturity=maturity,
            evidence=f"Total policies: {len(policies)}, Overdue: {len(overdue)}, Low acknowledgment: {len(low_ack)}",
            gaps=gaps,
            recommendations=recs,
        ))

        self.controls.extend(controls)
        return controls

    def generate_governance_report(self) -> dict:
        """Generate comprehensive governance assessment report."""
        avg_maturity = (
            sum(c.maturity.value for c in self.controls) / len(self.controls)
            if self.controls else 0
        )

        all_gaps = []
        all_recs = []
        for c in self.controls:
            all_gaps.extend(c.gaps)
            all_recs.extend(c.recommendations)

        return {
            "organization": self.organization,
            "assessment_date": datetime.now(timezone.utc).isoformat(),
            "overall_maturity": round(avg_maturity, 1),
            "maturity_label": MaturityLevel(round(avg_maturity)).name if avg_maturity > 0 else "NOT_ASSESSED",
            "subcategory_scores": [
                {
                    "subcategory": c.subcategory,
                    "description": c.description,
                    "maturity_level": c.maturity.value,
                    "maturity_name": c.maturity.name,
                    "evidence": c.evidence,
                }
                for c in self.controls
            ],
            "total_gaps": len(all_gaps),
            "gaps": all_gaps,
            "recommendations": all_recs,
        }


if __name__ == "__main__":
    assessor = GovernFunctionAssessor("Cipher Engineering Labs")

    training = TrainingMetrics(
        total_staff=500,
        trained_staff=472,
        specialist_certified=8,
        total_specialists=12,
        avg_quiz_score=87.5,
        new_hire_avg_days=18.0,
    )
    assessor.assess_awareness_training(training)

    policies = [
        PolicyInventory("Enterprise Privacy Policy", "CPO", datetime(2025, 6, 1, tzinfo=timezone.utc), 12, 0.97, "current"),
        PolicyInventory("Data Retention Policy", "CPO", datetime(2025, 3, 15, tzinfo=timezone.utc), 12, 0.94, "current"),
        PolicyInventory("Cookie Policy", "CPO", datetime(2024, 8, 1, tzinfo=timezone.utc), 6, 0.91, "overdue"),
        PolicyInventory("Incident Response Policy", "CISO", datetime(2025, 9, 1, tzinfo=timezone.utc), 6, 0.98, "current"),
    ]
    assessor.assess_policies(policies)

    report = assessor.generate_governance_report()
    print(json.dumps(report, indent=2))
