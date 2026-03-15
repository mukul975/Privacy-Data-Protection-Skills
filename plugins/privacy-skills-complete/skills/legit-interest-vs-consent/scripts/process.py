#!/usr/bin/env python3
"""
Legitimate Interest vs Consent Decision Engine

Implements the decision framework for choosing between consent and
legitimate interest as the lawful basis, including power imbalance
detection and three-part LIA scoring.
"""

import json
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class LawfulBasis(Enum):
    CONSENT = "consent"
    EXPLICIT_CONSENT = "explicit_consent"
    LEGITIMATE_INTEREST = "legitimate_interest"
    CONTRACT = "contract_performance"
    LEGAL_OBLIGATION = "legal_obligation"
    PUBLIC_TASK = "public_task"
    VITAL_INTEREST = "vital_interest"


class RecommendationStrength(Enum):
    MANDATORY = "mandatory"  # law requires this basis
    STRONG = "strong"  # clear best choice
    MODERATE = "moderate"  # good choice but alternative possible
    WEAK = "weak"  # marginal; consider alternatives


@dataclass
class ProcessingActivity:
    """Description of a data processing activity to assess."""
    activity_id: str = ""
    name: str = ""
    purpose: str = ""
    data_categories: list[str] = field(default_factory=list)
    data_subject_type: str = ""  # "customer", "employee", "prospect", "child"
    involves_cookies: bool = False
    involves_email_marketing: bool = False
    involves_special_categories: bool = False
    involves_automated_decisions: bool = False
    involves_international_transfer: bool = False
    involves_third_party_sharing: bool = False
    existing_customer_relationship: bool = False
    controller_is_public_authority: bool = False
    employment_context: bool = False
    service_conditional_on_processing: bool = False
    data_subject_has_alternatives: bool = True
    processing_expected_by_subject: bool = True
    withdrawal_operationally_feasible: bool = True

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class LIAScore:
    """Three-part Legitimate Interest Assessment scoring."""
    purpose_test_pass: bool = False
    purpose_test_notes: str = ""
    necessity_test_pass: bool = False
    necessity_test_notes: str = ""
    balancing_factors: dict = field(default_factory=dict)
    balancing_test_pass: bool = False
    balancing_test_notes: str = ""
    overall_pass: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


def check_mandatory_consent(activity: ProcessingActivity) -> Optional[dict]:
    """
    Check if specific legislation mandates consent for this activity.

    Returns:
        Mandate details if consent is required, None otherwise.
    """
    mandates = []

    if activity.involves_cookies:
        mandates.append({
            "regulation": "ePrivacy Directive Article 5(3)",
            "reason": "Non-essential cookies require consent",
            "basis": LawfulBasis.CONSENT.value,
        })

    if activity.involves_email_marketing and not activity.existing_customer_relationship:
        mandates.append({
            "regulation": "ePrivacy Directive Article 13(1)",
            "reason": "Unsolicited electronic marketing requires prior consent",
            "basis": LawfulBasis.CONSENT.value,
        })

    if activity.involves_special_categories:
        mandates.append({
            "regulation": "GDPR Article 9(2)(a)",
            "reason": "Special category data processing requires explicit consent",
            "basis": LawfulBasis.EXPLICIT_CONSENT.value,
        })

    if activity.involves_automated_decisions:
        mandates.append({
            "regulation": "GDPR Article 22(2)(c)",
            "reason": "Automated decision-making with legal effects requires explicit consent",
            "basis": LawfulBasis.EXPLICIT_CONSENT.value,
        })

    if mandates:
        return {"mandatory_consent": True, "mandates": mandates}
    return None


def assess_power_imbalance(activity: ProcessingActivity) -> dict:
    """
    Assess whether a power imbalance exists that would undermine consent validity.

    Per EDPB Guidelines 05/2020 and Recital 43.
    """
    indicators = []
    imbalance_score = 0

    if activity.employment_context:
        indicators.append({
            "indicator": "Employment relationship",
            "impact": "HIGH",
            "reference": "WP29 Opinion 2/2017, Recital 43",
            "note": "Employee consent generally invalid due to power imbalance",
        })
        imbalance_score += 4

    if activity.controller_is_public_authority:
        indicators.append({
            "indicator": "Controller is public authority",
            "impact": "HIGH",
            "reference": "Recital 43",
            "note": "Public authority processing should use legal obligation or public task basis",
        })
        imbalance_score += 4

    if activity.service_conditional_on_processing:
        indicators.append({
            "indicator": "Processing conditional on service",
            "impact": "HIGH",
            "reference": "Article 7(4)",
            "note": "Consent bundled with service access is presumed not freely given",
        })
        imbalance_score += 3

    if not activity.data_subject_has_alternatives:
        indicators.append({
            "indicator": "No reasonable alternatives for data subject",
            "impact": "MEDIUM",
            "reference": "EDPB Guidelines 05/2020 para 14",
            "note": "Monopoly or limited market reduces freedom of choice",
        })
        imbalance_score += 2

    if activity.data_subject_type == "child":
        indicators.append({
            "indicator": "Data subjects are children",
            "impact": "MEDIUM",
            "reference": "Recital 38, Article 8",
            "note": "Children are a vulnerable group requiring extra protection",
        })
        imbalance_score += 2

    has_imbalance = imbalance_score >= 3

    return {
        "has_power_imbalance": has_imbalance,
        "imbalance_score": imbalance_score,
        "consent_validity": "likely_invalid" if has_imbalance else "likely_valid",
        "indicators": indicators,
    }


def perform_lia(activity: ProcessingActivity, stated_interest: str) -> LIAScore:
    """
    Perform a three-part Legitimate Interest Assessment.

    Args:
        activity: The processing activity to assess.
        stated_interest: The articulated legitimate interest.

    Returns:
        LIAScore with results for each test.
    """
    lia = LIAScore()

    # Part 1: Purpose Test
    lia.purpose_test_pass = bool(stated_interest and len(stated_interest) > 20)
    lia.purpose_test_notes = (
        f"Stated interest: '{stated_interest}'. "
        f"{'Interest is clearly articulated.' if lia.purpose_test_pass else 'Interest needs clearer articulation.'}"
    )

    # Part 2: Necessity Test
    lia.necessity_test_pass = not activity.involves_special_categories
    lia.necessity_test_notes = (
        "Processing appears necessary for the stated interest. "
        "No less intrusive alternative identified."
        if lia.necessity_test_pass
        else "Processing involves special categories; heightened necessity scrutiny required."
    )

    # Part 3: Balancing Test
    factors = {
        "data_sensitivity": "low" if not activity.involves_special_categories else "high",
        "reasonable_expectation": "expected" if activity.processing_expected_by_subject else "unexpected",
        "existing_relationship": "yes" if activity.existing_customer_relationship else "no",
        "impact_level": "minimal" if activity.data_subject_has_alternatives else "significant",
        "vulnerable_groups": "yes" if activity.data_subject_type == "child" else "no",
        "third_party_sharing": "yes" if activity.involves_third_party_sharing else "no",
    }

    positive_factors = sum(1 for v in factors.values() if v in ("low", "expected", "yes", "minimal", "no"))
    total_factors = len(factors)

    lia.balancing_factors = factors
    lia.balancing_test_pass = positive_factors >= total_factors * 0.6
    lia.balancing_test_notes = (
        f"{positive_factors}/{total_factors} factors favor the controller. "
        f"{'Balance tips toward controller interest.' if lia.balancing_test_pass else 'Balance tips toward data subject rights.'}"
    )

    lia.overall_pass = all([lia.purpose_test_pass, lia.necessity_test_pass, lia.balancing_test_pass])
    return lia


def recommend_lawful_basis(activity: ProcessingActivity) -> dict:
    """
    Recommend the appropriate lawful basis for a processing activity.

    Returns:
        Recommendation with basis, strength, and reasoning.
    """
    # Step 1: Check mandatory consent
    mandate = check_mandatory_consent(activity)
    if mandate:
        return {
            "recommended_basis": mandate["mandates"][0]["basis"],
            "strength": RecommendationStrength.MANDATORY.value,
            "reasoning": f"Consent is legally required: {mandate['mandates'][0]['regulation']}",
            "mandates": mandate["mandates"],
        }

    # Step 2: Check power imbalance
    imbalance = assess_power_imbalance(activity)
    if imbalance["has_power_imbalance"]:
        return {
            "recommended_basis": LawfulBasis.LEGITIMATE_INTEREST.value,
            "strength": RecommendationStrength.STRONG.value,
            "reasoning": f"Power imbalance detected (score: {imbalance['imbalance_score']}). Consent likely invalid. Legitimate interest recommended with documented LIA.",
            "power_imbalance": imbalance,
        }

    # Step 3: Evaluate both options
    if activity.processing_expected_by_subject and not activity.involves_third_party_sharing:
        return {
            "recommended_basis": LawfulBasis.LEGITIMATE_INTEREST.value,
            "strength": RecommendationStrength.MODERATE.value,
            "reasoning": "Processing is reasonably expected by data subjects and involves no third-party sharing. LI is appropriate with opt-out mechanism.",
        }

    return {
        "recommended_basis": LawfulBasis.CONSENT.value,
        "strength": RecommendationStrength.MODERATE.value,
        "reasoning": "Processing is optional and may not be expected by data subjects. Consent provides appropriate user control.",
    }


if __name__ == "__main__":
    scenarios = [
        ProcessingActivity(
            activity_id="act_001",
            name="Analytics Cookies",
            purpose="Track user behavior on website for analytics",
            involves_cookies=True,
            data_subject_type="customer",
        ),
        ProcessingActivity(
            activity_id="act_002",
            name="Fraud Detection",
            purpose="Detect fraudulent account creation patterns",
            data_subject_type="customer",
            existing_customer_relationship=True,
            processing_expected_by_subject=True,
            withdrawal_operationally_feasible=False,
        ),
        ProcessingActivity(
            activity_id="act_003",
            name="Employee Monitoring",
            purpose="Monitor employee productivity metrics",
            data_subject_type="employee",
            employment_context=True,
            service_conditional_on_processing=True,
        ),
        ProcessingActivity(
            activity_id="act_004",
            name="Third-Party Data Sharing",
            purpose="Share data with Datalytics Partners Ltd. for benchmarking",
            data_subject_type="customer",
            involves_third_party_sharing=True,
            processing_expected_by_subject=False,
            existing_customer_relationship=True,
        ),
    ]

    for activity in scenarios:
        print(f"\n=== {activity.name} ===")
        rec = recommend_lawful_basis(activity)
        print(f"Recommended: {rec['recommended_basis']}")
        print(f"Strength: {rec['strength']}")
        print(f"Reasoning: {rec['reasoning']}")
