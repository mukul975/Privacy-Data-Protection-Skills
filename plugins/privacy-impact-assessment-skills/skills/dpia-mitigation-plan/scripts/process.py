#!/usr/bin/env python3
"""DPIA Mitigation Planning and Tracking Tool.

Structures risk mitigation planning for DPIAs under Art. 35(7)(d),
tracks implementation progress, calculates residual risk after
mitigation, and flags Art. 36 prior consultation triggers.
"""

import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class MeasureStatus(Enum):
    PROPOSED = "Proposed"
    APPROVED = "Approved"
    IN_PROGRESS = "In Progress"
    IMPLEMENTED = "Implemented"
    VERIFIED = "Verified"


class MeasureType(Enum):
    TECHNICAL = "Technical"
    ORGANISATIONAL = "Organisational"


class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    VERY_HIGH = "Very High"


def score_to_level(score: int) -> RiskLevel:
    if score <= 3:
        return RiskLevel.LOW
    elif score <= 6:
        return RiskLevel.MEDIUM
    elif score <= 9:
        return RiskLevel.HIGH
    return RiskLevel.VERY_HIGH


@dataclass
class MitigationMeasure:
    measure_id: str
    description: str
    measure_type: MeasureType
    risk_references: list  # Risk IDs this measure addresses
    reduces_likelihood: bool
    reduces_severity: bool
    expected_reduction: int  # Points of risk score reduction
    owner: str
    budget_eur: float
    start_date: str
    target_date: str
    status: MeasureStatus
    verification_method: str
    verification_result: str = ""


@dataclass
class Risk:
    risk_id: str
    description: str
    inherent_severity: int
    inherent_likelihood: int
    residual_severity: Optional[int] = None
    residual_likelihood: Optional[int] = None

    @property
    def inherent_score(self) -> int:
        return self.inherent_severity * self.inherent_likelihood

    @property
    def inherent_level(self) -> RiskLevel:
        return score_to_level(self.inherent_score)

    @property
    def residual_score(self) -> int:
        s = self.residual_severity if self.residual_severity else self.inherent_severity
        l = self.residual_likelihood if self.residual_likelihood else self.inherent_likelihood
        return s * l

    @property
    def residual_level(self) -> RiskLevel:
        return score_to_level(self.residual_score)


@dataclass
class MitigationPlan:
    dpia_reference: str
    processing_activity: str
    controller: str
    plan_date: str
    plan_owner: str
    risk_appetite_threshold: int
    risks: list = field(default_factory=list)
    measures: list = field(default_factory=list)


def calculate_residual_risks(plan: MitigationPlan) -> MitigationPlan:
    """Calculate residual risk for each risk based on applicable measures."""
    for risk in plan.risks:
        applicable_measures = [
            m for m in plan.measures
            if risk.risk_id in m.risk_references
            and m.status in (MeasureStatus.IMPLEMENTED, MeasureStatus.VERIFIED, MeasureStatus.IN_PROGRESS, MeasureStatus.APPROVED)
        ]

        total_likelihood_reduction = sum(
            m.expected_reduction for m in applicable_measures
            if m.reduces_likelihood
        )
        total_severity_reduction = sum(
            m.expected_reduction for m in applicable_measures
            if m.reduces_severity
        )

        risk.residual_likelihood = max(1, risk.inherent_likelihood - total_likelihood_reduction)
        risk.residual_severity = max(1, risk.inherent_severity - total_severity_reduction)

    return plan


def assess_plan_completeness(plan: MitigationPlan) -> dict:
    """Assess completeness of the mitigation plan."""
    findings = []

    # Check all high/very high risks have measures
    for risk in plan.risks:
        if risk.inherent_level in (RiskLevel.HIGH, RiskLevel.VERY_HIGH):
            applicable = [m for m in plan.measures if risk.risk_id in m.risk_references]
            if not applicable:
                findings.append({
                    "severity": "Critical",
                    "finding": f"{risk.risk_id}: High/Very High inherent risk with no mitigation measures",
                })

    # Check for overdue measures
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for m in plan.measures:
        if m.target_date < today and m.status in (MeasureStatus.PROPOSED, MeasureStatus.APPROVED, MeasureStatus.IN_PROGRESS):
            findings.append({
                "severity": "High",
                "finding": f"{m.measure_id}: Overdue (target: {m.target_date}, status: {m.status.value})",
            })

    # Check verification status
    unverified = [m for m in plan.measures if m.status == MeasureStatus.IMPLEMENTED]
    if unverified:
        findings.append({
            "severity": "Medium",
            "finding": f"{len(unverified)} measure(s) implemented but not yet verified",
        })

    # Check Art. 36 prior consultation need
    prior_consultation = False
    for risk in plan.risks:
        if risk.residual_level in (RiskLevel.HIGH, RiskLevel.VERY_HIGH):
            prior_consultation = True
            findings.append({
                "severity": "Critical",
                "finding": f"{risk.risk_id}: Residual risk {risk.residual_level.value} -- Art. 36 prior consultation required",
            })

    # Budget summary
    total_budget = sum(m.budget_eur for m in plan.measures)
    implemented_budget = sum(m.budget_eur for m in plan.measures if m.status in (MeasureStatus.IMPLEMENTED, MeasureStatus.VERIFIED))

    return {
        "total_measures": len(plan.measures),
        "verified": sum(1 for m in plan.measures if m.status == MeasureStatus.VERIFIED),
        "implemented": sum(1 for m in plan.measures if m.status == MeasureStatus.IMPLEMENTED),
        "in_progress": sum(1 for m in plan.measures if m.status == MeasureStatus.IN_PROGRESS),
        "pending": sum(1 for m in plan.measures if m.status in (MeasureStatus.PROPOSED, MeasureStatus.APPROVED)),
        "total_budget_eur": total_budget,
        "spent_budget_eur": implemented_budget,
        "prior_consultation_required": prior_consultation,
        "findings": findings,
    }


def generate_report(plan: MitigationPlan) -> str:
    """Generate the mitigation plan report."""
    lines = [
        "=" * 75,
        "DPIA MITIGATION PLAN",
        "=" * 75,
        f"DPIA Reference:      {plan.dpia_reference}",
        f"Processing Activity: {plan.processing_activity}",
        f"Controller:          {plan.controller}",
        f"Plan Date:           {plan.plan_date}",
        f"Plan Owner:          {plan.plan_owner}",
        f"Risk Appetite:       Score <= {plan.risk_appetite_threshold}",
        "",
    ]

    # Risk summary with inherent vs residual
    lines.extend(["-" * 75, "RISK SUMMARY (INHERENT vs RESIDUAL)", "-" * 75])
    for risk in plan.risks:
        lines.append(f"\n  {risk.risk_id}: {risk.description}")
        lines.append(
            f"    Inherent:  {risk.inherent_score:>2} ({risk.inherent_level.value})"
            f"  |  Residual: {risk.residual_score:>2} ({risk.residual_level.value})"
            f"  |  Reduction: {risk.inherent_score - risk.residual_score} points"
        )
        within = risk.residual_score <= plan.risk_appetite_threshold
        lines.append(f"    Within Appetite: {'Yes' if within else 'NO -- ESCALATION REQUIRED'}")

    # Mitigation measures
    lines.extend(["", "-" * 75, "MITIGATION MEASURES", "-" * 75])

    for m in plan.measures:
        lines.append(f"\n  {m.measure_id}: {m.description}")
        lines.append(f"    Type:          {m.measure_type.value}")
        lines.append(f"    Addresses:     {', '.join(m.risk_references)}")
        lines.append(f"    Effect:        {'Likelihood' if m.reduces_likelihood else ''}"
                     f"{'+ Severity' if m.reduces_severity else ''}"
                     f" (reduction: {m.expected_reduction})")
        lines.append(f"    Owner:         {m.owner}")
        lines.append(f"    Budget:        EUR {m.budget_eur:,.0f}")
        lines.append(f"    Timeline:      {m.start_date} to {m.target_date}")
        lines.append(f"    Status:        {m.status.value}")
        lines.append(f"    Verification:  {m.verification_method}")
        if m.verification_result:
            lines.append(f"    Result:        {m.verification_result}")

    # Plan assessment
    assessment = assess_plan_completeness(plan)
    lines.extend([
        "",
        "-" * 75,
        "PLAN ASSESSMENT",
        "-" * 75,
        f"  Total Measures:     {assessment['total_measures']}",
        f"  Verified:           {assessment['verified']}",
        f"  Implemented:        {assessment['implemented']}",
        f"  In Progress:        {assessment['in_progress']}",
        f"  Pending:            {assessment['pending']}",
        f"  Total Budget:       EUR {assessment['total_budget_eur']:,.0f}",
        f"  Spent Budget:       EUR {assessment['spent_budget_eur']:,.0f}",
        f"  Prior Consultation: {'REQUIRED' if assessment['prior_consultation_required'] else 'Not Required'}",
    ])

    if assessment["findings"]:
        lines.append("\n  Findings:")
        for f in assessment["findings"]:
            lines.append(f"    [{f['severity']:>8}] {f['finding']}")

    lines.extend(["", "=" * 75])
    return "\n".join(lines)


if __name__ == "__main__":
    plan = MitigationPlan(
        dpia_reference="DPIA-QLH-2026-012",
        processing_activity="Patient Genomic Profiling Platform",
        controller="QuantumLeap Health Technologies",
        plan_date="2026-03-14",
        plan_owner="Dr. Elena Vasquez, DPO",
        risk_appetite_threshold=6,
        risks=[
            Risk("R1", "Unauthorised access to genomic datasets", 4, 3),
            Risk("R2", "Algorithmic bias in genomic risk scores", 4, 3),
            Risk("R3", "Purpose creep by insurance partners", 3, 2),
            Risk("R4", "Platform unavailability during critical treatment", 3, 2),
            Risk("R5", "Re-identification via research database linkage", 4, 2),
        ],
        measures=[
            MitigationMeasure("M1", "AES-256 encryption at rest and TLS 1.3 in transit for all genomic data", MeasureType.TECHNICAL, ["R1"], True, False, 1, "CISO", 45000, "2026-01-15", "2026-03-01", MeasureStatus.VERIFIED, "Penetration test by Cure53", "Passed: no unencrypted data exposure found"),
            MitigationMeasure("M2", "RBAC with MFA and CyberArk PAM for privileged access", MeasureType.TECHNICAL, ["R1"], True, False, 1, "IT Security Lead", 35000, "2026-02-01", "2026-03-15", MeasureStatus.IMPLEMENTED, "Access control audit", ""),
            MitigationMeasure("M3", "Bias audit using diverse validation cohorts (12 ethnic groups)", MeasureType.TECHNICAL, ["R2"], True, False, 1, "Head of AI Research", 80000, "2026-03-01", "2026-06-30", MeasureStatus.IN_PROGRESS, "Statistical bias metrics across cohorts", ""),
            MitigationMeasure("M4", "Clinical review board for high-impact recommendations", MeasureType.ORGANISATIONAL, ["R2"], True, False, 1, "Chief Medical Officer", 25000, "2026-04-01", "2026-05-15", MeasureStatus.APPROVED, "Board meeting minutes and override rate tracking", ""),
            MitigationMeasure("M5", "Art. 28 DPA with insurance partners restricting purpose", MeasureType.ORGANISATIONAL, ["R3"], True, False, 1, "Legal Counsel", 15000, "2026-01-01", "2026-02-28", MeasureStatus.VERIFIED, "Legal review of executed DPA terms", "DPA executed with all 3 insurance partners; GenDG clause included"),
            MitigationMeasure("M6", "Multi-region deployment with automated failover", MeasureType.TECHNICAL, ["R4"], True, False, 1, "Infrastructure Lead", 60000, "2025-11-01", "2026-02-01", MeasureStatus.VERIFIED, "Failover drill with RTO measurement", "RTO measured at 47 seconds; RPO 3.8 hours"),
            MitigationMeasure("M7", "Clinical fallback protocols for manual pathway selection", MeasureType.ORGANISATIONAL, ["R4"], True, False, 1, "Clinical Operations", 10000, "2026-01-15", "2026-03-01", MeasureStatus.IMPLEMENTED, "Tabletop exercise with clinical staff", ""),
            MitigationMeasure("M8", "Differential privacy (epsilon=1.0) for research exports", MeasureType.TECHNICAL, ["R5"], True, False, 1, "Privacy Engineering", 40000, "2026-04-01", "2026-07-31", MeasureStatus.APPROVED, "Privacy budget verification and re-identification testing", ""),
        ],
    )

    plan = calculate_residual_risks(plan)
    report = generate_report(plan)
    print(report)
