"""
Privacy-Preserving Data Sharing — Synthetic Data Quality Assessment

Provides utility and privacy measurement for synthetic datasets
generated with SDV or other synthetic data tools.
"""

from dataclasses import dataclass
from typing import Optional
import json


@dataclass
class QualityMetric:
    metric_name: str
    score: float
    target: float
    passed: bool
    details: str


@dataclass
class PrivacyMetric:
    metric_name: str
    value: float
    threshold: float
    safe: bool
    details: str


class SyntheticDataAssessor:
    """
    Assess synthetic data quality and privacy risk.
    Works with any synthetic data generation method.
    """

    def assess_column_shape_similarity(
        self,
        real_distributions: dict[str, dict],
        synthetic_distributions: dict[str, dict],
    ) -> list[QualityMetric]:
        """
        Compare column distributions between real and synthetic data.

        Args:
            real_distributions: {column: {value: count}} for real data
            synthetic_distributions: {column: {value: count}} for synthetic data
        """
        metrics = []

        for col in real_distributions:
            if col not in synthetic_distributions:
                metrics.append(QualityMetric(
                    metric_name=f"column_shape:{col}",
                    score=0.0,
                    target=0.85,
                    passed=False,
                    details=f"Column {col} missing from synthetic data",
                ))
                continue

            real = real_distributions[col]
            synth = synthetic_distributions[col]

            all_keys = set(real.keys()) | set(synth.keys())
            real_total = sum(real.values())
            synth_total = sum(synth.values())

            if real_total == 0 or synth_total == 0:
                continue

            # Calculate distribution overlap (simplified Bhattacharyya coefficient)
            overlap = 0.0
            for key in all_keys:
                real_prop = real.get(key, 0) / real_total
                synth_prop = synth.get(key, 0) / synth_total
                overlap += min(real_prop, synth_prop)

            metrics.append(QualityMetric(
                metric_name=f"column_shape:{col}",
                score=round(overlap, 3),
                target=0.85,
                passed=overlap >= 0.85,
                details=f"Distribution overlap: {overlap:.1%}",
            ))

        return metrics

    def assess_privacy_risk(
        self,
        exact_match_rate: float,
        nearest_neighbor_distance: float,
        membership_inference_auc: float,
    ) -> list[PrivacyMetric]:
        """Assess privacy risk metrics for synthetic data."""
        return [
            PrivacyMetric(
                metric_name="exact_match_rate",
                value=exact_match_rate,
                threshold=0.01,
                safe=exact_match_rate < 0.01,
                details=f"Exact match rate: {exact_match_rate:.2%} (threshold: <1%)",
            ),
            PrivacyMetric(
                metric_name="nearest_neighbor_distance",
                value=nearest_neighbor_distance,
                threshold=0.1,
                safe=nearest_neighbor_distance > 0.1,
                details=f"Min NN distance: {nearest_neighbor_distance:.4f} (threshold: >0.1)",
            ),
            PrivacyMetric(
                metric_name="membership_inference_auc",
                value=membership_inference_auc,
                threshold=0.55,
                safe=membership_inference_auc < 0.55,
                details=f"MI AUC: {membership_inference_auc:.3f} (threshold: <0.55, random=0.5)",
            ),
        ]

    def generate_assessment_report(
        self,
        quality_metrics: list[QualityMetric],
        privacy_metrics: list[PrivacyMetric],
        dataset_name: str,
        generation_method: str,
    ) -> dict:
        """Generate comprehensive synthetic data assessment report."""
        quality_pass_rate = (
            sum(1 for m in quality_metrics if m.passed) / len(quality_metrics)
            if quality_metrics else 0
        )
        privacy_safe = all(m.safe for m in privacy_metrics)

        return {
            "dataset": dataset_name,
            "method": generation_method,
            "overall_verdict": "APPROVED" if quality_pass_rate >= 0.8 and privacy_safe else "NEEDS_REVIEW",
            "quality": {
                "pass_rate": f"{quality_pass_rate:.1%}",
                "metrics": [
                    {"name": m.metric_name, "score": m.score, "target": m.target, "passed": m.passed}
                    for m in quality_metrics
                ],
            },
            "privacy": {
                "all_safe": privacy_safe,
                "metrics": [
                    {"name": m.metric_name, "value": m.value, "threshold": m.threshold, "safe": m.safe}
                    for m in privacy_metrics
                ],
            },
        }


if __name__ == "__main__":
    assessor = SyntheticDataAssessor()

    real_dist = {
        "age_group": {"18-25": 200, "26-35": 350, "36-45": 250, "46-55": 150, "56+": 50},
        "region": {"North": 300, "South": 250, "East": 200, "West": 250},
    }
    synth_dist = {
        "age_group": {"18-25": 185, "26-35": 360, "36-45": 240, "46-55": 160, "56+": 55},
        "region": {"North": 310, "South": 240, "East": 210, "West": 240},
    }

    quality = assessor.assess_column_shape_similarity(real_dist, synth_dist)
    privacy = assessor.assess_privacy_risk(
        exact_match_rate=0.002,
        nearest_neighbor_distance=0.23,
        membership_inference_auc=0.52,
    )

    report = assessor.generate_assessment_report(quality, privacy, "customer_analytics", "CTGAN")
    print(json.dumps(report, indent=2))
