#!/usr/bin/env python3
"""
Combined DPIA + AI Act Conformity Assessment Scoring Engine

Calculates weighted risk scores across GDPR and AI Act dimensions,
generating combined compliance reports.
"""

import json
import datetime
from dataclasses import dataclass, field
from enum import Enum


class RiskClassification(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    VERY_HIGH = "Very High"
    CRITICAL = "Critical"


DIMENSION_WEIGHTS = {
    "privacy_risk": 0.30,
    "fundamental_rights": 0.25,
    "accuracy_reliability": 0.20,
    "transparency_gap": 0.15,
    "oversight_adequacy": 0.10,
}


@dataclass
class RiskDimension:
    name: str
    score: int  # 1-5
    weight: float
    findings: list[str] = field(default_factory=list)
    mitigations: list[str] = field(default_factory=list)


@dataclass
class CombinedAssessment:
    system_name: str
    date: str
    dimensions: list[RiskDimension]
    weighted_score: float
    classification: RiskClassification
    gdpr_compliant: bool
    ai_act_compliant: bool
    prior_consultation: bool
    recommendations: list[str]


def classify_risk(score: float) -> RiskClassification:
    if score <= 1.5:
        return RiskClassification.LOW
    elif score <= 2.5:
        return RiskClassification.MEDIUM
    elif score <= 3.5:
        return RiskClassification.HIGH
    elif score <= 4.5:
        return RiskClassification.VERY_HIGH
    return RiskClassification.CRITICAL


def run_assessment(
    system_name: str,
    privacy_score: int,
    privacy_findings: list[str],
    rights_score: int,
    rights_findings: list[str],
    accuracy_score: int,
    accuracy_findings: list[str],
    transparency_score: int,
    transparency_findings: list[str],
    oversight_score: int,
    oversight_findings: list[str],
) -> CombinedAssessment:
    today = datetime.date.today().isoformat()

    dimensions = [
        RiskDimension("Privacy Risk", privacy_score, DIMENSION_WEIGHTS["privacy_risk"], privacy_findings),
        RiskDimension("Fundamental Rights", rights_score, DIMENSION_WEIGHTS["fundamental_rights"], rights_findings),
        RiskDimension("Accuracy & Reliability", accuracy_score, DIMENSION_WEIGHTS["accuracy_reliability"], accuracy_findings),
        RiskDimension("Transparency Gap", transparency_score, DIMENSION_WEIGHTS["transparency_gap"], transparency_findings),
        RiskDimension("Oversight Adequacy", oversight_score, DIMENSION_WEIGHTS["oversight_adequacy"], oversight_findings),
    ]

    weighted = sum(d.score * d.weight for d in dimensions)
    classification = classify_risk(weighted)

    prior_consultation = classification in [RiskClassification.VERY_HIGH, RiskClassification.CRITICAL]
    gdpr_ok = privacy_score <= 3 and transparency_score <= 3
    ai_act_ok = accuracy_score <= 3 and oversight_score <= 3

    recommendations = []
    if prior_consultation:
        recommendations.append("Art. 36 prior consultation required — residual risk remains high")
    if not gdpr_ok:
        recommendations.append("GDPR compliance gaps identified — remediate privacy and transparency risks")
    if not ai_act_ok:
        recommendations.append("AI Act compliance gaps — address accuracy and oversight deficiencies")
    if classification == RiskClassification.CRITICAL:
        recommendations.append("CRITICAL: Do not deploy until fundamental risks are addressed")

    return CombinedAssessment(
        system_name=system_name,
        date=today,
        dimensions=dimensions,
        weighted_score=weighted,
        classification=classification,
        gdpr_compliant=gdpr_ok,
        ai_act_compliant=ai_act_ok,
        prior_consultation=prior_consultation,
        recommendations=recommendations,
    )


def format_report(a: CombinedAssessment) -> str:
    lines = [f"{'='*80}", "COMBINED DPIA + AI ACT CONFORMITY ASSESSMENT",
             f"System: {a.system_name}", f"Date: {a.date}", f"{'='*80}"]
    lines.append(f"\nWeighted Score: {a.weighted_score:.2f}/5.00")
    lines.append(f"Classification: {a.classification.value}")
    lines.append(f"GDPR Compliant: {'Yes' if a.gdpr_compliant else 'No'}")
    lines.append(f"AI Act Compliant: {'Yes' if a.ai_act_compliant else 'No'}")
    lines.append(f"Prior Consultation: {'Required' if a.prior_consultation else 'Not Required'}")

    lines.append(f"\n## RISK DIMENSIONS")
    for d in a.dimensions:
        lines.append(f"\n  {d.name}: {d.score}/5 (weight: {d.weight:.0%})")
        for f in d.findings:
            lines.append(f"    - {f}")

    if a.recommendations:
        lines.append(f"\n## RECOMMENDATIONS")
        for r in a.recommendations:
            lines.append(f"  - {r}")
    return "\n".join(lines)


def demo_cerebrum_ai_labs():
    assessment = run_assessment(
        system_name="Cerebrum AI Labs — Patient Triage Classifier",
        privacy_score=3, privacy_findings=["Health data processing", "Model memorization risk moderate"],
        rights_score=4, rights_findings=["Healthcare triage decisions affect patient safety", "Potential discrimination by demographic"],
        accuracy_score=3, accuracy_findings=["93% accuracy overall but 85% for elderly patients"],
        transparency_score=2, transparency_findings=["Model card available", "Patient notification implemented"],
        oversight_score=3, oversight_findings=["Physician review required but time-pressured"],
    )
    print(format_report(assessment))


if __name__ == "__main__":
    demo_cerebrum_ai_labs()
