#!/usr/bin/env python3
"""
Privacy Design Pattern Selection Engine

Implements Hoepman's eight privacy design patterns with automated
pattern selection based on processing activity characteristics.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class GDPRPrinciple(Enum):
    LAWFULNESS = ("Article 5(1)(a)", "Lawfulness, fairness and transparency")
    PURPOSE_LIMITATION = ("Article 5(1)(b)", "Purpose limitation")
    DATA_MINIMIZATION = ("Article 5(1)(c)", "Data minimisation")
    ACCURACY = ("Article 5(1)(d)", "Accuracy")
    STORAGE_LIMITATION = ("Article 5(1)(e)", "Storage limitation")
    INTEGRITY_CONFIDENTIALITY = ("Article 5(1)(f)", "Integrity and confidentiality")
    ACCOUNTABILITY = ("Article 5(2)", "Accountability")

    def __init__(self, article: str, description: str):
        self.article = article
        self.description = description


class PatternCategory(Enum):
    DATA_ORIENTED = "data-oriented"
    PROCESS_ORIENTED = "process-oriented"


@dataclass
class PrivacyPattern:
    """One of the eight privacy design patterns per Hoepman."""
    name: str
    category: PatternCategory
    description: str
    gdpr_principles: list[GDPRPrinciple]
    sub_patterns: list[str]
    implementation_examples: list[str]


@dataclass
class ProcessingActivity:
    """A data processing activity to evaluate for pattern selection."""
    name: str
    purpose: str
    lawful_basis: str
    data_categories: list[str]
    data_subjects: str
    involves_special_categories: bool = False
    involves_profiling: bool = False
    involves_cross_border: bool = False
    involves_third_parties: bool = False
    data_volume: str = "medium"  # low, medium, high
    sensitivity_level: int = 3  # 1-5


PATTERNS = {
    "MINIMIZE": PrivacyPattern(
        name="MINIMIZE",
        category=PatternCategory.DATA_ORIENTED,
        description="Limit the processing of personal data as much as possible",
        gdpr_principles=[GDPRPrinciple.DATA_MINIMIZATION, GDPRPrinciple.STORAGE_LIMITATION],
        sub_patterns=["Select before collect", "Exclude", "Strip", "Destroy"],
        implementation_examples=[
            "API allowlist validation rejecting non-required fields",
            "Pseudonymization at ingestion boundary",
            "TTL-based automated deletion",
            "Progressive collection tied to feature activation",
        ],
    ),
    "HIDE": PrivacyPattern(
        name="HIDE",
        category=PatternCategory.DATA_ORIENTED,
        description="Protect personal data, make it unlinkable or unobservable",
        gdpr_principles=[GDPRPrinciple.INTEGRITY_CONFIDENTIALITY, GDPRPrinciple.DATA_MINIMIZATION],
        sub_patterns=["Encrypt", "Hash", "Mix", "Obfuscate", "Dissociate"],
        implementation_examples=[
            "AES-256-GCM field-level encryption",
            "HMAC-SHA256 pseudonymization with HSM key storage",
            "Differential privacy noise injection",
            "Dynamic data masking for support agents",
        ],
    ),
    "SEPARATE": PrivacyPattern(
        name="SEPARATE",
        category=PatternCategory.DATA_ORIENTED,
        description="Process personal data in a distributed fashion, preventing correlation",
        gdpr_principles=[GDPRPrinciple.PURPOSE_LIMITATION, GDPRPrinciple.DATA_MINIMIZATION],
        sub_patterns=["Isolate", "Distribute"],
        implementation_examples=[
            "Purpose-partitioned databases",
            "Microservice isolation per processing purpose",
            "Federated learning for distributed ML",
            "Cross-purpose join prohibition without compatibility assessment",
        ],
    ),
    "ABSTRACT": PrivacyPattern(
        name="ABSTRACT",
        category=PatternCategory.DATA_ORIENTED,
        description="Limit the detail of personal data as much as possible",
        gdpr_principles=[GDPRPrinciple.DATA_MINIMIZATION],
        sub_patterns=["Summarize", "Group", "Perturb"],
        implementation_examples=[
            "Age brackets instead of exact dates of birth",
            "Region-level geographic data instead of postal codes",
            "Minimum group size enforcement (11 records) in analytics",
            "k-anonymity with generalization hierarchies",
        ],
    ),
    "INFORM": PrivacyPattern(
        name="INFORM",
        category=PatternCategory.PROCESS_ORIENTED,
        description="Inform data subjects about the processing of their personal data",
        gdpr_principles=[GDPRPrinciple.LAWFULNESS],
        sub_patterns=["Supply", "Notify", "Explain"],
        implementation_examples=[
            "Layered privacy notices (plain-language first layer, full Art. 13 second layer)",
            "Just-in-time notifications at new data collection points",
            "Data breach notification within 72 hours (Art. 33)",
            "Explainable AI output descriptions for automated decisions",
        ],
    ),
    "CONTROL": PrivacyPattern(
        name="CONTROL",
        category=PatternCategory.PROCESS_ORIENTED,
        description="Provide data subjects with control over their personal data",
        gdpr_principles=[GDPRPrinciple.LAWFULNESS, GDPRPrinciple.ACCURACY],
        sub_patterns=["Consent", "Choose", "Update", "Retract"],
        implementation_examples=[
            "Granular consent toggles with unticked defaults",
            "Privacy preference center with per-purpose controls",
            "Self-service profile editing for accuracy corrections",
            "One-click consent withdrawal with 24-hour processing cessation",
        ],
    ),
    "ENFORCE": PrivacyPattern(
        name="ENFORCE",
        category=PatternCategory.PROCESS_ORIENTED,
        description="Commit to and technically enforce privacy-friendly processing",
        gdpr_principles=[GDPRPrinciple.PURPOSE_LIMITATION, GDPRPrinciple.ACCOUNTABILITY],
        sub_patterns=["Create", "Maintain", "Uphold"],
        implementation_examples=[
            "OPA policy-as-code for purpose-based access control",
            "CI/CD privacy gate blocking non-compliant deployments",
            "Automated retention enforcement with TTL scanning",
            "Processor contract management with SCC compliance checks",
        ],
    ),
    "DEMONSTRATE": PrivacyPattern(
        name="DEMONSTRATE",
        category=PatternCategory.PROCESS_ORIENTED,
        description="Demonstrate compliance with privacy policies and regulations",
        gdpr_principles=[GDPRPrinciple.ACCOUNTABILITY],
        sub_patterns=["Record", "Audit", "Report"],
        implementation_examples=[
            "Immutable audit trail for all data access events",
            "Article 30 records of processing activities",
            "Quarterly privacy audits with documented findings",
            "DPO quarterly compliance reports",
        ],
    ),
}


class PatternSelector:
    """Selects applicable privacy design patterns for a processing activity."""

    def __init__(self):
        self.patterns = PATTERNS

    def evaluate(self, activity: ProcessingActivity) -> list[dict]:
        """Score all patterns for a given processing activity."""
        results = []

        for name, pattern in self.patterns.items():
            score = self._score_pattern(pattern, activity)
            results.append({
                "pattern": name,
                "category": pattern.category.value,
                "score": score,
                "max_score": 25,
                "description": pattern.description,
                "applicable_sub_patterns": self._select_sub_patterns(pattern, activity),
                "gdpr_articles": [p.article for p in pattern.gdpr_principles],
                "priority": "HIGH" if score >= 18 else "MEDIUM" if score >= 12 else "LOW",
            })

        results.sort(key=lambda x: x["score"], reverse=True)
        return results

    def _score_pattern(self, pattern: PrivacyPattern, activity: ProcessingActivity) -> int:
        score = 0

        # Base relevance (all patterns have baseline applicability)
        score += 5

        # Sensitivity amplifier
        if activity.sensitivity_level >= 4:
            if pattern.name in ("HIDE", "MINIMIZE", "SEPARATE"):
                score += 5
        if activity.sensitivity_level >= 3:
            if pattern.name in ("HIDE", "ENFORCE"):
                score += 3

        # Special categories
        if activity.involves_special_categories:
            if pattern.name in ("HIDE", "MINIMIZE", "SEPARATE", "ENFORCE"):
                score += 4

        # Profiling
        if activity.involves_profiling:
            if pattern.name in ("INFORM", "CONTROL", "ABSTRACT"):
                score += 4

        # Cross-border
        if activity.involves_cross_border:
            if pattern.name in ("SEPARATE", "HIDE", "ENFORCE"):
                score += 3

        # Third parties
        if activity.involves_third_parties:
            if pattern.name in ("ENFORCE", "DEMONSTRATE", "HIDE"):
                score += 3

        # High volume
        if activity.data_volume == "high":
            if pattern.name in ("MINIMIZE", "ABSTRACT", "HIDE"):
                score += 2

        # Universal patterns (always important)
        if pattern.name in ("INFORM", "DEMONSTRATE"):
            score += 3

        return min(score, 25)

    def _select_sub_patterns(self, pattern: PrivacyPattern, activity: ProcessingActivity) -> list[str]:
        """Select the most applicable sub-patterns."""
        # Return all sub-patterns for simplicity; in practice, filter based on activity
        return pattern.sub_patterns

    def generate_report(self, activity: ProcessingActivity) -> dict:
        evaluations = self.evaluate(activity)
        high_priority = [e for e in evaluations if e["priority"] == "HIGH"]
        medium_priority = [e for e in evaluations if e["priority"] == "MEDIUM"]

        return {
            "activity": activity.name,
            "purpose": activity.purpose,
            "assessment_date": datetime.now(timezone.utc).isoformat(),
            "total_patterns_evaluated": len(evaluations),
            "high_priority_patterns": len(high_priority),
            "medium_priority_patterns": len(medium_priority),
            "recommended_patterns": evaluations[:5],
            "all_evaluations": evaluations,
        }


def run_example():
    """Demonstrate pattern selection for Prism Data Systems AG."""

    selector = PatternSelector()

    activities = [
        ProcessingActivity(
            name="Customer behavior analytics pipeline",
            purpose="Analyze feature usage patterns for product improvement",
            lawful_basis="Article 6(1)(f) legitimate interest",
            data_categories=["pseudonymized_user_id", "feature_events", "session_duration"],
            data_subjects="Prism Data Systems AG customers",
            sensitivity_level=3,
            data_volume="high",
        ),
        ProcessingActivity(
            name="Health insurance claims processing",
            purpose="Adjudicate health insurance claims",
            lawful_basis="Article 6(1)(b) contract + Article 9(2)(f) legal claims",
            data_categories=["patient_name", "diagnosis_codes", "treatment_history", "provider_id"],
            data_subjects="Insurance policyholders",
            involves_special_categories=True,
            sensitivity_level=5,
            data_volume="medium",
        ),
        ProcessingActivity(
            name="Automated credit scoring",
            purpose="Assess creditworthiness using automated profiling",
            lawful_basis="Article 6(1)(b) contract + Article 22(2)(a) explicit consent",
            data_categories=["financial_history", "employment_data", "payment_behavior"],
            data_subjects="Loan applicants",
            involves_profiling=True,
            involves_third_parties=True,
            sensitivity_level=4,
        ),
    ]

    for activity in activities:
        print(f"=== Pattern Selection: {activity.name} ===")
        print(f"Purpose: {activity.purpose}")
        print(f"Lawful basis: {activity.lawful_basis}")
        if activity.involves_special_categories:
            print("  [Special categories: YES]")
        if activity.involves_profiling:
            print("  [Profiling: YES]")
        print()

        report = selector.generate_report(activity)

        print(f"Recommended patterns (top 5):")
        for i, ev in enumerate(report["recommended_patterns"]):
            print(f"  #{i+1} {ev['pattern']} [{ev['category']}] — "
                  f"Score: {ev['score']}/{ev['max_score']} ({ev['priority']})")
            print(f"      {ev['description']}")
            print(f"      GDPR: {', '.join(ev['gdpr_articles'])}")
            print(f"      Sub-patterns: {', '.join(ev['applicable_sub_patterns'])}")
            print()

        print("-" * 70)
        print()


if __name__ == "__main__":
    run_example()
