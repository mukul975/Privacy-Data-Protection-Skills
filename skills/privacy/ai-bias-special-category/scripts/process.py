#!/usr/bin/env python3
"""
AI Bias Assessment Engine for Special Category Data

Computes fairness metrics, identifies bias patterns, and generates
compliance reports for AI systems processing Art. 9 special categories.
"""

import json
import datetime
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class FairnessMetric(Enum):
    DEMOGRAPHIC_PARITY = "Demographic Parity"
    EQUALIZED_ODDS = "Equalized Odds"
    EQUAL_OPPORTUNITY = "Equal Opportunity"
    CALIBRATION = "Calibration"
    PREDICTIVE_PARITY = "Predictive Parity"


class BiasLevel(Enum):
    NONE = "No significant bias detected"
    LOW = "Low bias — within acceptable thresholds"
    MODERATE = "Moderate bias — mitigation recommended"
    HIGH = "High bias — mitigation required"
    CRITICAL = "Critical bias — deployment should be paused"


class MitigationStrategy(Enum):
    RESAMPLING = "Data resampling"
    REWEIGHTING = "Sample reweighting"
    ADVERSARIAL_DEBIASING = "Adversarial debiasing"
    FAIRNESS_CONSTRAINTS = "Fairness constraints in training"
    THRESHOLD_ADJUSTMENT = "Per-group threshold adjustment"
    SCORE_CALIBRATION = "Per-group score calibration"


@dataclass
class GroupMetrics:
    group_name: str
    sample_size: int
    positive_rate: float  # P(positive outcome)
    true_positive_rate: float  # TPR / recall
    false_positive_rate: float  # FPR
    positive_predictive_value: float  # PPV / precision
    calibration_score: float  # P(Y=1 | score=s)


@dataclass
class FairnessMeasurement:
    metric: FairnessMetric
    group_a: str
    group_b: str
    group_a_value: float
    group_b_value: float
    disparity: float  # absolute difference or ratio
    threshold: float
    passes: bool


@dataclass
class BiasAssessment:
    system_name: str
    date: str
    protected_attributes: list[str]
    group_metrics: list[GroupMetrics]
    fairness_measurements: list[FairnessMeasurement]
    overall_bias_level: BiasLevel
    findings: list[str]
    mitigations_recommended: list[dict]
    art10_5_processing: bool
    art10_5_safeguards: list[str]


def compute_demographic_parity(group_a: GroupMetrics, group_b: GroupMetrics, threshold: float = 0.1) -> FairnessMeasurement:
    disparity = abs(group_a.positive_rate - group_b.positive_rate)
    return FairnessMeasurement(
        metric=FairnessMetric.DEMOGRAPHIC_PARITY,
        group_a=group_a.group_name,
        group_b=group_b.group_name,
        group_a_value=group_a.positive_rate,
        group_b_value=group_b.positive_rate,
        disparity=disparity,
        threshold=threshold,
        passes=disparity <= threshold,
    )


def compute_equalized_odds(group_a: GroupMetrics, group_b: GroupMetrics, threshold: float = 0.1) -> list[FairnessMeasurement]:
    tpr_disparity = abs(group_a.true_positive_rate - group_b.true_positive_rate)
    fpr_disparity = abs(group_a.false_positive_rate - group_b.false_positive_rate)
    max_disparity = max(tpr_disparity, fpr_disparity)

    return [
        FairnessMeasurement(
            metric=FairnessMetric.EQUALIZED_ODDS,
            group_a=group_a.group_name,
            group_b=group_b.group_name,
            group_a_value=group_a.true_positive_rate,
            group_b_value=group_b.true_positive_rate,
            disparity=tpr_disparity,
            threshold=threshold,
            passes=tpr_disparity <= threshold,
        ),
        FairnessMeasurement(
            metric=FairnessMetric.EQUALIZED_ODDS,
            group_a=group_a.group_name,
            group_b=group_b.group_name,
            group_a_value=group_a.false_positive_rate,
            group_b_value=group_b.false_positive_rate,
            disparity=fpr_disparity,
            threshold=threshold,
            passes=fpr_disparity <= threshold,
        ),
    ]


def compute_equal_opportunity(group_a: GroupMetrics, group_b: GroupMetrics, threshold: float = 0.1) -> FairnessMeasurement:
    disparity = abs(group_a.true_positive_rate - group_b.true_positive_rate)
    return FairnessMeasurement(
        metric=FairnessMetric.EQUAL_OPPORTUNITY,
        group_a=group_a.group_name,
        group_b=group_b.group_name,
        group_a_value=group_a.true_positive_rate,
        group_b_value=group_b.true_positive_rate,
        disparity=disparity,
        threshold=threshold,
        passes=disparity <= threshold,
    )


def assess_overall_bias(measurements: list[FairnessMeasurement]) -> BiasLevel:
    failing = [m for m in measurements if not m.passes]
    if not failing:
        return BiasLevel.NONE
    max_disparity = max(m.disparity for m in failing)
    if max_disparity > 0.3:
        return BiasLevel.CRITICAL
    elif max_disparity > 0.2:
        return BiasLevel.HIGH
    elif max_disparity > 0.1:
        return BiasLevel.MODERATE
    else:
        return BiasLevel.LOW


def recommend_mitigations(bias_level: BiasLevel, measurements: list[FairnessMeasurement]) -> list[dict]:
    if bias_level in [BiasLevel.NONE, BiasLevel.LOW]:
        return []

    recommendations = []
    failing_metrics = set(m.metric.value for m in measurements if not m.passes)

    if FairnessMetric.DEMOGRAPHIC_PARITY.value in failing_metrics:
        recommendations.append({
            "strategy": MitigationStrategy.RESAMPLING.value,
            "description": "Resample training data to balance positive outcome rates across groups",
            "priority": "High" if bias_level in [BiasLevel.HIGH, BiasLevel.CRITICAL] else "Medium",
        })

    if FairnessMetric.EQUALIZED_ODDS.value in failing_metrics:
        recommendations.append({
            "strategy": MitigationStrategy.ADVERSARIAL_DEBIASING.value,
            "description": "Apply adversarial debiasing to equalise TPR and FPR across groups",
            "priority": "High",
        })
        recommendations.append({
            "strategy": MitigationStrategy.THRESHOLD_ADJUSTMENT.value,
            "description": "Adjust decision thresholds per group to equalise error rates",
            "priority": "Medium",
        })

    if bias_level == BiasLevel.CRITICAL:
        recommendations.insert(0, {
            "strategy": "Pause deployment",
            "description": "Critical bias detected — pause deployment until mitigation is validated",
            "priority": "Critical",
        })

    return recommendations


def run_bias_assessment(
    system_name: str,
    group_metrics: list[GroupMetrics],
    metrics_to_compute: list[FairnessMetric],
    protected_attribute: str,
    art10_5: bool = False,
) -> BiasAssessment:
    today = datetime.date.today().isoformat()
    measurements = []
    findings = []

    for i, group_a in enumerate(group_metrics):
        for group_b in group_metrics[i + 1:]:
            for metric in metrics_to_compute:
                if metric == FairnessMetric.DEMOGRAPHIC_PARITY:
                    measurements.append(compute_demographic_parity(group_a, group_b))
                elif metric == FairnessMetric.EQUALIZED_ODDS:
                    measurements.extend(compute_equalized_odds(group_a, group_b))
                elif metric == FairnessMetric.EQUAL_OPPORTUNITY:
                    measurements.append(compute_equal_opportunity(group_a, group_b))

    for m in measurements:
        if not m.passes:
            findings.append(
                f"{m.metric.value} violation: {m.group_a} vs {m.group_b} — disparity {m.disparity:.3f} exceeds threshold {m.threshold}"
            )

    size_imbalances = []
    max_size = max(g.sample_size for g in group_metrics)
    for g in group_metrics:
        if g.sample_size < max_size * 0.1:
            size_imbalances.append(g.group_name)
    if size_imbalances:
        findings.append(f"Underrepresented groups in training data: {', '.join(size_imbalances)}")

    overall = assess_overall_bias(measurements)
    mitigations = recommend_mitigations(overall, measurements)

    art10_safeguards = []
    if art10_5:
        art10_safeguards = [
            "Special category data pseudonymised for bias analysis",
            "Access restricted to bias assessment team",
            "Data not used for any purpose other than bias detection",
            "Data to be deleted after bias assessment completion",
        ]

    return BiasAssessment(
        system_name=system_name,
        date=today,
        protected_attributes=[protected_attribute],
        group_metrics=group_metrics,
        fairness_measurements=measurements,
        overall_bias_level=overall,
        findings=findings,
        mitigations_recommended=mitigations,
        art10_5_processing=art10_5,
        art10_5_safeguards=art10_safeguards,
    )


def format_report(assessment: BiasAssessment) -> str:
    lines = []
    lines.append(f"{'='*80}")
    lines.append("AI BIAS ASSESSMENT — SPECIAL CATEGORY DATA")
    lines.append(f"System: {assessment.system_name}")
    lines.append(f"Date: {assessment.date}")
    lines.append(f"{'='*80}")

    lines.append(f"\nOverall Bias Level: {assessment.overall_bias_level.value}")
    lines.append(f"Protected Attributes: {', '.join(assessment.protected_attributes)}")

    lines.append(f"\n## GROUP METRICS")
    for g in assessment.group_metrics:
        lines.append(f"  {g.group_name} (n={g.sample_size:,}): positive_rate={g.positive_rate:.3f}, TPR={g.true_positive_rate:.3f}, FPR={g.false_positive_rate:.3f}")

    lines.append(f"\n## FAIRNESS MEASUREMENTS")
    for m in assessment.fairness_measurements:
        status = "PASS" if m.passes else "FAIL"
        lines.append(f"  [{status}] {m.metric.value}: {m.group_a}={m.group_a_value:.3f} vs {m.group_b}={m.group_b_value:.3f} (disparity={m.disparity:.3f}, threshold={m.threshold})")

    if assessment.findings:
        lines.append(f"\n## FINDINGS")
        for f in assessment.findings:
            lines.append(f"  - {f}")

    if assessment.mitigations_recommended:
        lines.append(f"\n## RECOMMENDED MITIGATIONS")
        for m in assessment.mitigations_recommended:
            lines.append(f"  [{m['priority']}] {m['strategy']}: {m['description']}")

    if assessment.art10_5_processing:
        lines.append(f"\n## ART. 10(5) SAFEGUARDS")
        for s in assessment.art10_5_safeguards:
            lines.append(f"  - {s}")

    return "\n".join(lines)


def demo_cerebrum_ai_labs():
    groups = [
        GroupMetrics("Male", 50000, 0.42, 0.85, 0.12, 0.78, 0.82),
        GroupMetrics("Female", 45000, 0.31, 0.72, 0.08, 0.81, 0.79),
        GroupMetrics("Non-binary", 2000, 0.28, 0.65, 0.15, 0.68, 0.71),
    ]

    assessment = run_bias_assessment(
        system_name="Cerebrum AI Labs — Hiring Candidate Ranker",
        group_metrics=groups,
        metrics_to_compute=[
            FairnessMetric.DEMOGRAPHIC_PARITY,
            FairnessMetric.EQUALIZED_ODDS,
            FairnessMetric.EQUAL_OPPORTUNITY,
        ],
        protected_attribute="gender",
        art10_5=True,
    )

    report = format_report(assessment)
    print(report)


if __name__ == "__main__":
    demo_cerebrum_ai_labs()
