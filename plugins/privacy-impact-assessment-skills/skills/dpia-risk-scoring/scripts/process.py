#!/usr/bin/env python3
"""DPIA Risk Scoring Tool.

Implements a structured risk scoring methodology for Data Protection Impact
Assessments aligned with ENISA threat taxonomy and ISO 29134. Calculates
inherent and residual risk scores using a 4x4 severity-likelihood matrix.
"""

import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    VERY_HIGH = "Very High"


class SeverityLevel(Enum):
    NEGLIGIBLE = 1
    LIMITED = 2
    SIGNIFICANT = 3
    MAXIMUM = 4


class LikelihoodLevel(Enum):
    NEGLIGIBLE = 1
    LIMITED = 2
    SIGNIFICANT = 3
    MAXIMUM = 4


RIGHTS_CATEGORIES = [
    "Loss of confidentiality",
    "Loss of integrity",
    "Loss of availability",
    "Loss of purpose limitation",
    "Discrimination",
    "Identity theft or fraud",
    "Financial loss",
    "Reputational damage",
    "Physical harm",
    "Loss of autonomy",
]


def score_to_risk_level(score: int) -> RiskLevel:
    """Map numeric risk score to risk level."""
    if score <= 3:
        return RiskLevel.LOW
    elif score <= 6:
        return RiskLevel.MEDIUM
    elif score <= 9:
        return RiskLevel.HIGH
    else:
        return RiskLevel.VERY_HIGH


@dataclass
class MitigationMeasure:
    description: str
    measure_type: str  # "technical" or "organisational"
    likelihood_reduction: int  # How many levels likelihood is reduced (0-3)
    status: str  # "implemented", "planned", "proposed"


@dataclass
class PrivacyRisk:
    risk_id: str
    description: str
    rights_category: str
    risk_source: str
    inherent_severity: int
    inherent_likelihood: int
    mitigation_measures: list = field(default_factory=list)
    residual_severity: Optional[int] = None
    residual_likelihood: Optional[int] = None

    @property
    def inherent_score(self) -> int:
        return self.inherent_severity * self.inherent_likelihood

    @property
    def inherent_level(self) -> RiskLevel:
        return score_to_risk_level(self.inherent_score)

    @property
    def residual_score(self) -> int:
        sev = self.residual_severity or self.inherent_severity
        lik = self.residual_likelihood or self.inherent_likelihood
        return sev * lik

    @property
    def residual_level(self) -> RiskLevel:
        return score_to_risk_level(self.residual_score)

    @property
    def risk_reduction(self) -> int:
        return self.inherent_score - self.residual_score


@dataclass
class RiskAssessment:
    assessment_id: str
    processing_activity: str
    controller: str
    assessment_date: str
    assessor: str
    risk_appetite_threshold: int  # Maximum acceptable residual risk score
    risks: list = field(default_factory=list)


def calculate_residual_risk(risk: PrivacyRisk) -> PrivacyRisk:
    """Calculate residual risk after applying mitigation measures."""
    # Severity typically remains the same (worst-case impact unchanged)
    risk.residual_severity = risk.inherent_severity

    # Likelihood reduced by effective mitigation measures
    total_reduction = sum(
        m.likelihood_reduction
        for m in risk.mitigation_measures
        if m.status in ("implemented", "planned")
    )

    adjusted_likelihood = max(1, risk.inherent_likelihood - total_reduction)
    risk.residual_likelihood = min(adjusted_likelihood, 4)

    return risk


def assess_prior_consultation_need(assessment: RiskAssessment) -> dict:
    """Determine if Art. 36 prior consultation is required."""
    high_residual_risks = [
        r for r in assessment.risks
        if r.residual_level in (RiskLevel.HIGH, RiskLevel.VERY_HIGH)
    ]

    above_appetite = [
        r for r in assessment.risks
        if r.residual_score > assessment.risk_appetite_threshold
    ]

    return {
        "prior_consultation_required": len(high_residual_risks) > 0,
        "high_residual_count": len(high_residual_risks),
        "above_appetite_count": len(above_appetite),
        "high_residual_risks": [r.risk_id for r in high_residual_risks],
        "above_appetite_risks": [r.risk_id for r in above_appetite],
    }


def generate_risk_matrix_display(risks: list) -> str:
    """Generate a visual risk matrix showing risk distribution."""
    matrix = {}
    for sev in range(1, 5):
        for lik in range(1, 5):
            matrix[(sev, lik)] = {"inherent": [], "residual": []}

    for r in risks:
        matrix[(r.inherent_severity, r.inherent_likelihood)]["inherent"].append(r.risk_id)
        rs = r.residual_severity or r.inherent_severity
        rl = r.residual_likelihood or r.inherent_likelihood
        matrix[(rs, rl)]["residual"].append(r.risk_id)

    sev_labels = ["Negligible", "Limited", "Significant", "Maximum"]
    lik_labels = ["Negligible", "Limited", "Significant", "Maximum"]

    lines = ["INHERENT RISK MATRIX", "=" * 60]
    lines.append(f"{'':>14} | {'Sev=1':^10} | {'Sev=2':^10} | {'Sev=3':^10} | {'Sev=4':^10}")
    lines.append("-" * 60)

    for lik in range(4, 0, -1):
        row_items = []
        for sev in range(1, 5):
            ids = matrix[(sev, lik)]["inherent"]
            cell = ",".join(ids) if ids else "."
            row_items.append(f"{cell:^10}")
        lines.append(f"Lik={lik:<9} | {' | '.join(row_items)}")

    lines.append("")
    lines.append("RESIDUAL RISK MATRIX")
    lines.append("=" * 60)
    lines.append(f"{'':>14} | {'Sev=1':^10} | {'Sev=2':^10} | {'Sev=3':^10} | {'Sev=4':^10}")
    lines.append("-" * 60)

    for lik in range(4, 0, -1):
        row_items = []
        for sev in range(1, 5):
            ids = matrix[(sev, lik)]["residual"]
            cell = ",".join(ids) if ids else "."
            row_items.append(f"{cell:^10}")
        lines.append(f"Lik={lik:<9} | {' | '.join(row_items)}")

    return "\n".join(lines)


def generate_report(assessment: RiskAssessment) -> str:
    """Generate a formatted risk scoring report."""
    lines = [
        "=" * 75,
        "DPIA RISK SCORING REPORT",
        "=" * 75,
        f"Assessment ID:       {assessment.assessment_id}",
        f"Processing Activity: {assessment.processing_activity}",
        f"Controller:          {assessment.controller}",
        f"Assessment Date:     {assessment.assessment_date}",
        f"Assessor:            {assessment.assessor}",
        f"Risk Appetite:       Score <= {assessment.risk_appetite_threshold} "
        f"({score_to_risk_level(assessment.risk_appetite_threshold).value})",
        "",
    ]

    # Risk register
    lines.extend(["-" * 75, "RISK REGISTER", "-" * 75])

    for risk in assessment.risks:
        lines.append(f"\n  Risk: {risk.risk_id}")
        lines.append(f"  Description:      {risk.description}")
        lines.append(f"  Rights Category:  {risk.rights_category}")
        lines.append(f"  Risk Source:       {risk.risk_source}")
        lines.append(
            f"  Inherent Risk:    Severity={risk.inherent_severity} x "
            f"Likelihood={risk.inherent_likelihood} = "
            f"{risk.inherent_score} ({risk.inherent_level.value})"
        )

        if risk.mitigation_measures:
            lines.append("  Mitigation Measures:")
            for m in risk.mitigation_measures:
                lines.append(
                    f"    - [{m.measure_type.upper():^15}] [{m.status:^11}] "
                    f"{m.description} (reduction: -{m.likelihood_reduction})"
                )

        lines.append(
            f"  Residual Risk:    Severity={risk.residual_severity} x "
            f"Likelihood={risk.residual_likelihood} = "
            f"{risk.residual_score} ({risk.residual_level.value})"
        )
        lines.append(f"  Risk Reduction:   {risk.risk_reduction} points")

        within = risk.residual_score <= assessment.risk_appetite_threshold
        lines.append(
            f"  Within Appetite:  {'Yes' if within else 'NO -- ESCALATION REQUIRED'}"
        )

    # Summary statistics
    lines.extend(["", "-" * 75, "SUMMARY STATISTICS", "-" * 75])

    total = len(assessment.risks)
    inherent_dist = {}
    residual_dist = {}
    for r in assessment.risks:
        il = r.inherent_level.value
        rl = r.residual_level.value
        inherent_dist[il] = inherent_dist.get(il, 0) + 1
        residual_dist[rl] = residual_dist.get(rl, 0) + 1

    lines.append(f"  Total Risks Assessed: {total}")
    lines.append("  Inherent Risk Distribution:")
    for level in ["Very High", "High", "Medium", "Low"]:
        count = inherent_dist.get(level, 0)
        bar = "#" * (count * 3)
        lines.append(f"    {level:>10}: {count:>2} {bar}")

    lines.append("  Residual Risk Distribution:")
    for level in ["Very High", "High", "Medium", "Low"]:
        count = residual_dist.get(level, 0)
        bar = "#" * (count * 3)
        lines.append(f"    {level:>10}: {count:>2} {bar}")

    avg_reduction = (
        sum(r.risk_reduction for r in assessment.risks) / total if total else 0
    )
    lines.append(f"  Average Risk Reduction: {avg_reduction:.1f} points")

    # Risk matrix
    lines.extend(["", "-" * 75])
    lines.append(generate_risk_matrix_display(assessment.risks))

    # Prior consultation assessment
    pc = assess_prior_consultation_need(assessment)
    lines.extend([
        "",
        "-" * 75,
        "ART. 36 PRIOR CONSULTATION ASSESSMENT",
        "-" * 75,
        f"  Prior Consultation Required: {'YES' if pc['prior_consultation_required'] else 'No'}",
        f"  High/Very High Residual Risks: {pc['high_residual_count']}",
        f"  Risks Above Appetite: {pc['above_appetite_count']}",
    ])

    if pc["high_residual_risks"]:
        lines.append(f"  Affected Risks: {', '.join(pc['high_residual_risks'])}")

    lines.extend(["", "=" * 75])

    return "\n".join(lines)


def run_assessment(config: dict) -> str:
    """Execute the full risk scoring assessment."""
    assessment = RiskAssessment(
        assessment_id=config.get("assessment_id", "DPIA-RISK-001"),
        processing_activity=config.get("processing_activity", ""),
        controller=config.get("controller", ""),
        assessment_date=config.get(
            "assessment_date",
            datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        ),
        assessor=config.get("assessor", "DPO"),
        risk_appetite_threshold=config.get("risk_appetite_threshold", 6),
    )

    for risk_data in config.get("risks", []):
        risk = PrivacyRisk(
            risk_id=risk_data["risk_id"],
            description=risk_data["description"],
            rights_category=risk_data.get("rights_category", ""),
            risk_source=risk_data.get("risk_source", ""),
            inherent_severity=risk_data["inherent_severity"],
            inherent_likelihood=risk_data["inherent_likelihood"],
        )

        for m_data in risk_data.get("mitigation_measures", []):
            risk.mitigation_measures.append(
                MitigationMeasure(
                    description=m_data["description"],
                    measure_type=m_data.get("measure_type", "technical"),
                    likelihood_reduction=m_data.get("likelihood_reduction", 1),
                    status=m_data.get("status", "planned"),
                )
            )

        risk = calculate_residual_risk(risk)
        assessment.risks.append(risk)

    return generate_report(assessment)


if __name__ == "__main__":
    sample = {
        "assessment_id": "DPIA-QLH-2026-012-RISK",
        "processing_activity": "Patient Genomic Profiling Platform",
        "controller": "QuantumLeap Health Technologies",
        "assessment_date": "2026-03-14",
        "assessor": "Dr. Elena Vasquez, DPO",
        "risk_appetite_threshold": 6,
        "risks": [
            {
                "risk_id": "R1",
                "description": "Unauthorised access to genomic datasets enabling re-identification of patients",
                "rights_category": "Loss of confidentiality",
                "risk_source": "External attacker; insider threat",
                "inherent_severity": 4,
                "inherent_likelihood": 3,
                "mitigation_measures": [
                    {"description": "AES-256 encryption at rest and TLS 1.3 in transit", "measure_type": "technical", "likelihood_reduction": 1, "status": "implemented"},
                    {"description": "Role-based access with MFA and privileged access management", "measure_type": "technical", "likelihood_reduction": 1, "status": "implemented"},
                ],
            },
            {
                "risk_id": "R2",
                "description": "Algorithmic bias in genomic risk scores causing discriminatory treatment recommendations",
                "rights_category": "Discrimination",
                "risk_source": "Training data bias; model design",
                "inherent_severity": 4,
                "inherent_likelihood": 3,
                "mitigation_measures": [
                    {"description": "Bias audit using diverse validation cohorts across ethnicities", "measure_type": "technical", "likelihood_reduction": 1, "status": "planned"},
                    {"description": "Clinical review board oversight of all high-impact recommendations", "measure_type": "organisational", "likelihood_reduction": 1, "status": "planned"},
                ],
            },
            {
                "risk_id": "R3",
                "description": "Genomic data used by insurance partners beyond agreed purposes",
                "rights_category": "Loss of purpose limitation",
                "risk_source": "Data recipient; contractual failure",
                "inherent_severity": 3,
                "inherent_likelihood": 2,
                "mitigation_measures": [
                    {"description": "Art. 28 DPA with insurance partners limiting purpose to coverage assessment", "measure_type": "organisational", "likelihood_reduction": 1, "status": "implemented"},
                ],
            },
            {
                "risk_id": "R4",
                "description": "Platform unavailability during critical treatment decisions",
                "rights_category": "Loss of availability",
                "risk_source": "System failure; ransomware",
                "inherent_severity": 3,
                "inherent_likelihood": 2,
                "mitigation_measures": [
                    {"description": "Multi-region deployment with automated failover", "measure_type": "technical", "likelihood_reduction": 1, "status": "implemented"},
                    {"description": "Clinical fallback protocols for manual treatment pathway selection", "measure_type": "organisational", "likelihood_reduction": 1, "status": "implemented"},
                ],
            },
            {
                "risk_id": "R5",
                "description": "Patient re-identification through genomic data linkage with public research databases",
                "rights_category": "Identity theft or fraud",
                "risk_source": "Research data linkage; genealogy databases",
                "inherent_severity": 4,
                "inherent_likelihood": 2,
                "mitigation_measures": [
                    {"description": "Differential privacy applied to any research exports", "measure_type": "technical", "likelihood_reduction": 1, "status": "planned"},
                ],
            },
        ],
    }

    report = run_assessment(sample)
    print(report)
