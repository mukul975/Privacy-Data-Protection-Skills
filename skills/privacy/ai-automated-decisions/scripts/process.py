#!/usr/bin/env python3
"""
AI Automated Decision-Making Assessment Engine

Evaluates Art. 22 applicability, human oversight effectiveness,
and contestation mechanism compliance for AI decision systems.
"""

import json
import datetime
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Art22Status(Enum):
    TRIGGERED = "Art. 22 Triggered"
    NOT_TRIGGERED = "Art. 22 Not Triggered"
    UNCERTAIN = "Requires Further Assessment"


class OversightLevel(Enum):
    HITL = "Human-in-the-loop"
    HOTL = "Human-on-the-loop"
    HIC = "Human-in-command"
    AUTONOMOUS = "Fully autonomous"


class OversightEffectiveness(Enum):
    EFFECTIVE = "Effective — meaningful human intervention"
    NOMINAL = "Nominal — intervention exists but may not be meaningful"
    INSUFFICIENT = "Insufficient — does not meet Art. 22 requirements"
    ABSENT = "Absent — no human oversight"


class DecisionCategory(Enum):
    CREDIT_FINANCIAL = "Credit and Financial Decisions"
    EMPLOYMENT = "Employment Decisions"
    HEALTHCARE = "Healthcare Decisions"
    PUBLIC_ADMIN = "Public Administration"
    INSURANCE = "Insurance Decisions"
    EDUCATION = "Education Admission"
    LAW_ENFORCEMENT = "Law Enforcement"
    MARKETING = "Marketing and Advertising"
    CONTENT_MODERATION = "Content Moderation"
    OTHER = "Other"


@dataclass
class HumanOversightProfile:
    oversight_level: OversightLevel
    reviewer_has_authority: bool = False
    reviewer_has_competence: bool = False
    reviewer_has_information: bool = False
    reviewer_has_sufficient_time: bool = False
    reviewer_exercises_discretion: bool = False
    override_rate: Optional[float] = None  # percentage
    average_review_time_seconds: Optional[int] = None
    daily_decision_volume_per_reviewer: Optional[int] = None
    automation_bias_countermeasures: bool = False
    training_provided: bool = False
    monitoring_in_place: bool = False


@dataclass
class ContestationMechanism:
    exists: bool = False
    accessible: bool = False
    response_timeframe_days: Optional[int] = None
    independent_reviewer: bool = False
    accepts_evidence: bool = False
    provides_written_outcome: bool = False
    indicates_further_appeal: bool = False
    contestation_rate: Optional[float] = None
    overturn_rate: Optional[float] = None


@dataclass
class AIDecisionSystem:
    system_name: str
    description: str
    category: DecisionCategory
    is_decision: bool = True
    is_solely_automated: bool = True
    has_legal_effects: bool = False
    has_significant_effects: bool = False
    uses_special_category_data: bool = False
    special_category_types: list[str] = field(default_factory=list)
    art22_exception: Optional[str] = None  # "contract", "law", "consent"
    human_oversight: Optional[HumanOversightProfile] = None
    contestation: Optional[ContestationMechanism] = None
    data_subjects_affected: str = ""
    decision_volume_monthly: int = 0


@dataclass
class Art22Assessment:
    system: AIDecisionSystem
    art22_status: Art22Status
    art22_exception_valid: bool
    oversight_effectiveness: OversightEffectiveness
    safeguards_compliant: bool
    contestation_compliant: bool
    issues: list[str]
    recommendations: list[str]
    risk_level: str  # "low", "medium", "high", "critical"


def assess_art22_applicability(system: AIDecisionSystem) -> tuple[Art22Status, list[str]]:
    issues = []

    if not system.is_decision:
        return Art22Status.NOT_TRIGGERED, ["AI output is advisory — no decision is made"]

    if not system.is_solely_automated:
        if system.human_oversight:
            ho = system.human_oversight
            meaningful = all([
                ho.reviewer_has_authority,
                ho.reviewer_has_competence,
                ho.reviewer_has_information,
                ho.reviewer_has_sufficient_time,
                ho.reviewer_exercises_discretion,
            ])
            if meaningful:
                return Art22Status.NOT_TRIGGERED, [
                    "Meaningful human intervention present — Art. 22 not triggered"
                ]
            else:
                issues.append(
                    "Human involvement exists but may not be 'meaningful' per EDPB criteria"
                )
                return Art22Status.TRIGGERED, issues
        else:
            issues.append("Claimed not solely automated but no oversight profile documented")
            return Art22Status.UNCERTAIN, issues

    if not (system.has_legal_effects or system.has_significant_effects):
        return Art22Status.NOT_TRIGGERED, [
            "Decision does not produce legal or similarly significant effects"
        ]

    issues.append("Decision is solely automated with legal or significant effects")
    return Art22Status.TRIGGERED, issues


def assess_oversight_effectiveness(oversight: Optional[HumanOversightProfile]) -> tuple[OversightEffectiveness, list[str]]:
    if not oversight:
        return OversightEffectiveness.ABSENT, ["No human oversight documented"]

    issues = []

    if oversight.oversight_level == OversightLevel.AUTONOMOUS:
        return OversightEffectiveness.ABSENT, ["System operates autonomously"]

    criteria_met = 0
    criteria_total = 5

    if oversight.reviewer_has_authority:
        criteria_met += 1
    else:
        issues.append("Reviewer lacks formal authority to override AI decisions")

    if oversight.reviewer_has_competence:
        criteria_met += 1
    else:
        issues.append("Reviewer lacks domain expertise to evaluate AI decisions")

    if oversight.reviewer_has_information:
        criteria_met += 1
    else:
        issues.append("Reviewer does not have access to all relevant information")

    if oversight.reviewer_has_sufficient_time:
        criteria_met += 1
    else:
        issues.append("Insufficient time allocated for genuine decision review")

    if oversight.reviewer_exercises_discretion:
        criteria_met += 1
    else:
        issues.append("Reviewer does not exercise genuine discretion")

    if oversight.override_rate is not None and oversight.override_rate < 1.0:
        issues.append(
            f"Override rate is {oversight.override_rate}% — very low rate suggests rubber-stamping (ICO recommends investigating < 5%)"
        )

    if oversight.daily_decision_volume_per_reviewer and oversight.daily_decision_volume_per_reviewer > 200:
        issues.append(
            f"Reviewer processes {oversight.daily_decision_volume_per_reviewer} decisions/day — volume may prevent meaningful review"
        )

    if not oversight.automation_bias_countermeasures:
        issues.append("No automation bias countermeasures implemented")

    if not oversight.training_provided:
        issues.append("Reviewers not trained on AI system capabilities and limitations")

    if criteria_met == criteria_total:
        effectiveness = OversightEffectiveness.EFFECTIVE
    elif criteria_met >= 3:
        effectiveness = OversightEffectiveness.NOMINAL
    else:
        effectiveness = OversightEffectiveness.INSUFFICIENT

    return effectiveness, issues


def assess_contestation(contestation: Optional[ContestationMechanism]) -> tuple[bool, list[str]]:
    if not contestation or not contestation.exists:
        return False, ["No contestation mechanism exists — required by Art. 22(3)"]

    issues = []
    compliant = True

    if not contestation.accessible:
        compliant = False
        issues.append("Contestation mechanism is not easily accessible to data subjects")

    if contestation.response_timeframe_days and contestation.response_timeframe_days > 30:
        issues.append(
            f"Response timeframe is {contestation.response_timeframe_days} days — Art. 12 requires one month"
        )

    if not contestation.independent_reviewer:
        compliant = False
        issues.append("Contestation reviewer is not independent from original decision")

    if not contestation.accepts_evidence:
        compliant = False
        issues.append("Mechanism does not accept supporting evidence from data subject")

    if not contestation.provides_written_outcome:
        compliant = False
        issues.append("Written contestation outcome not provided to data subject")

    if not contestation.indicates_further_appeal:
        issues.append("Data subject not informed of further appeal options (DPA complaint, judicial remedy)")

    return compliant, issues


def assess_art22_exception(system: AIDecisionSystem) -> tuple[bool, list[str]]:
    if not system.art22_exception:
        return False, ["No Art. 22(2) exception relied upon"]

    issues = []

    if system.art22_exception == "contract":
        issues.append("Art. 22(2)(a) contract necessity: verify automated decision is genuinely necessary for contract performance")
    elif system.art22_exception == "law":
        issues.append("Art. 22(2)(b) legal authorisation: identify specific Union/Member State law with suitable measures")
    elif system.art22_exception == "consent":
        issues.append("Art. 22(2)(c) explicit consent: verify consent is specific, informed, and withdrawable")
    else:
        return False, [f"Invalid exception: {system.art22_exception}"]

    if system.uses_special_category_data:
        if system.art22_exception in ["contract", "law"]:
            issues.append(
                "Art. 22(4): Special category data in automated decisions requires Art. 9(2)(a) explicit consent or Art. 9(2)(g) substantial public interest"
            )

    return True, issues


def run_assessment(system: AIDecisionSystem) -> Art22Assessment:
    all_issues = []
    all_recommendations = []

    art22_status, art22_issues = assess_art22_applicability(system)
    all_issues.extend(art22_issues)

    exception_valid = False
    if art22_status == Art22Status.TRIGGERED:
        exception_valid, exception_issues = assess_art22_exception(system)
        all_issues.extend(exception_issues)

        if not exception_valid:
            all_recommendations.append(
                "Identify valid Art. 22(2) exception or redesign process to include meaningful human intervention"
            )

    oversight_effectiveness, oversight_issues = assess_oversight_effectiveness(system.human_oversight)
    all_issues.extend(oversight_issues)

    if oversight_effectiveness in [OversightEffectiveness.NOMINAL, OversightEffectiveness.INSUFFICIENT]:
        all_recommendations.append(
            "Strengthen human oversight: ensure reviewers have authority, competence, information, time, and exercise discretion"
        )
    if oversight_effectiveness == OversightEffectiveness.ABSENT and art22_status == Art22Status.TRIGGERED:
        all_recommendations.append(
            "Implement human oversight mechanism — currently no human involvement in decision process"
        )

    contestation_compliant, contestation_issues = assess_contestation(system.contestation)
    all_issues.extend(contestation_issues)

    if not contestation_compliant and art22_status == Art22Status.TRIGGERED:
        all_recommendations.append(
            "Implement Art. 22(3) contestation mechanism: accessible, independent reviewer, evidence acceptance, written outcome"
        )

    safeguards_met = all([
        oversight_effectiveness in [OversightEffectiveness.EFFECTIVE, OversightEffectiveness.NOMINAL],
        contestation_compliant,
    ])

    if system.uses_special_category_data:
        all_recommendations.append(
            "Art. 22(4): Verify Art. 9(2)(a) explicit consent or Art. 9(2)(g) substantial public interest for special category data in automated decisions"
        )

    if art22_status == Art22Status.TRIGGERED and not exception_valid:
        risk = "critical"
    elif art22_status == Art22Status.TRIGGERED and not safeguards_met:
        risk = "high"
    elif oversight_effectiveness == OversightEffectiveness.NOMINAL:
        risk = "medium"
    else:
        risk = "low"

    return Art22Assessment(
        system=system,
        art22_status=art22_status,
        art22_exception_valid=exception_valid,
        oversight_effectiveness=oversight_effectiveness,
        safeguards_compliant=safeguards_met,
        contestation_compliant=contestation_compliant,
        issues=all_issues,
        recommendations=all_recommendations,
        risk_level=risk,
    )


def format_report(assessment: Art22Assessment) -> str:
    lines = []
    today = datetime.date.today().isoformat()
    lines.append(f"{'='*80}")
    lines.append("AI AUTOMATED DECISION-MAKING ASSESSMENT")
    lines.append(f"System: {assessment.system.system_name}")
    lines.append(f"Category: {assessment.system.category.value}")
    lines.append(f"Date: {today}")
    lines.append(f"{'='*80}")

    lines.append(f"\n## ART. 22 STATUS: {assessment.art22_status.value}")
    lines.append(f"Exception Valid: {'YES' if assessment.art22_exception_valid else 'NO'}")
    lines.append(f"Oversight: {assessment.oversight_effectiveness.value}")
    lines.append(f"Contestation: {'COMPLIANT' if assessment.contestation_compliant else 'NON-COMPLIANT'}")
    lines.append(f"Safeguards: {'MET' if assessment.safeguards_compliant else 'NOT MET'}")
    lines.append(f"Risk Level: {assessment.risk_level.upper()}")

    if assessment.issues:
        lines.append(f"\n## ISSUES ({len(assessment.issues)})")
        for issue in assessment.issues:
            lines.append(f"  - {issue}")

    if assessment.recommendations:
        lines.append(f"\n## RECOMMENDATIONS")
        for rec in assessment.recommendations:
            lines.append(f"  - {rec}")

    return "\n".join(lines)


def demo_cerebrum_ai_labs():
    oversight = HumanOversightProfile(
        oversight_level=OversightLevel.HOTL,
        reviewer_has_authority=True,
        reviewer_has_competence=True,
        reviewer_has_information=False,
        reviewer_has_sufficient_time=False,
        reviewer_exercises_discretion=False,
        override_rate=0.8,
        average_review_time_seconds=15,
        daily_decision_volume_per_reviewer=350,
        automation_bias_countermeasures=False,
        training_provided=True,
        monitoring_in_place=True,
    )

    contestation = ContestationMechanism(
        exists=True,
        accessible=True,
        response_timeframe_days=30,
        independent_reviewer=False,
        accepts_evidence=True,
        provides_written_outcome=True,
        indicates_further_appeal=False,
        contestation_rate=2.1,
        overturn_rate=15.0,
    )

    system = AIDecisionSystem(
        system_name="Cerebrum AI Labs — Automated Credit Pre-Screening",
        description="ML model that pre-screens loan applications and auto-declines applications below score threshold",
        category=DecisionCategory.CREDIT_FINANCIAL,
        is_decision=True,
        is_solely_automated=False,
        has_legal_effects=True,
        has_significant_effects=True,
        uses_special_category_data=False,
        art22_exception="contract",
        human_oversight=oversight,
        contestation=contestation,
        data_subjects_affected="EU/EEA loan applicants",
        decision_volume_monthly=45_000,
    )

    assessment = run_assessment(system)
    report = format_report(assessment)
    print(report)


if __name__ == "__main__":
    demo_cerebrum_ai_labs()
