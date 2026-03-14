#!/usr/bin/env python3
"""
HIPAA Breach Notification Manager

Implements the four-factor breach risk assessment per 45 CFR §164.402(2),
calculates notification deadlines, determines notification obligations
based on breach size and geographic distribution, and generates
notification tracking records.
"""

import json
from datetime import datetime, timezone, timedelta
from enum import Enum
from typing import Optional


class BreachAssessmentOutcome(Enum):
    LOW_PROBABILITY = "low_probability_not_reportable"
    REPORTABLE = "reportable_breach"
    PRESUMED_BREACH = "presumed_breach_assessment_inconclusive"


class NotificationTier(Enum):
    TIER_500_PLUS = "500_plus_immediate_hhs"
    TIER_UNDER_500 = "under_500_annual_log"


def four_factor_assessment(
    phi_types: list,
    includes_ssn: bool,
    includes_financial: bool,
    includes_clinical: bool,
    unauthorized_person_known: bool,
    unauthorized_person_hipaa_covered: bool,
    phi_actually_viewed: bool,
    phi_acquired_or_copied: bool,
    risk_mitigated: bool,
    phi_returned_or_destroyed: bool,
    written_attestation_obtained: bool,
) -> dict:
    """
    Perform the HIPAA four-factor breach risk assessment.

    Returns assessment outcome determining whether notification is required.
    """
    factor_1_score = 0
    if includes_ssn:
        factor_1_score += 3
    if includes_financial:
        factor_1_score += 2
    if includes_clinical:
        factor_1_score += 3
    if len(phi_types) > 5:
        factor_1_score += 2
    elif len(phi_types) > 2:
        factor_1_score += 1

    factor_2_score = 0
    if not unauthorized_person_known:
        factor_2_score += 3
    elif unauthorized_person_hipaa_covered:
        factor_2_score += 0
    else:
        factor_2_score += 2

    factor_3_score = 0
    if phi_acquired_or_copied:
        factor_3_score += 3
    elif phi_actually_viewed:
        factor_3_score += 2
    else:
        factor_3_score += 0

    factor_4_score = 0
    if not risk_mitigated:
        factor_4_score += 2
    if not phi_returned_or_destroyed:
        factor_4_score += 2
    if not written_attestation_obtained:
        factor_4_score += 1

    total = factor_1_score + factor_2_score + factor_3_score + factor_4_score
    max_score = 10 + 3 + 3 + 5

    if total <= 4:
        outcome = BreachAssessmentOutcome.LOW_PROBABILITY
    elif total <= 8:
        outcome = BreachAssessmentOutcome.PRESUMED_BREACH
    else:
        outcome = BreachAssessmentOutcome.REPORTABLE

    return {
        "assessment_date": datetime.now(timezone.utc).isoformat(),
        "factors": {
            "factor_1_nature_extent": {
                "score": factor_1_score,
                "max": 10,
                "phi_types": phi_types,
                "includes_ssn": includes_ssn,
                "includes_financial": includes_financial,
                "includes_clinical": includes_clinical,
            },
            "factor_2_unauthorized_person": {
                "score": factor_2_score,
                "max": 3,
                "person_known": unauthorized_person_known,
                "hipaa_covered": unauthorized_person_hipaa_covered,
            },
            "factor_3_actual_access": {
                "score": factor_3_score,
                "max": 3,
                "actually_viewed": phi_actually_viewed,
                "acquired_or_copied": phi_acquired_or_copied,
            },
            "factor_4_mitigation": {
                "score": factor_4_score,
                "max": 5,
                "risk_mitigated": risk_mitigated,
                "phi_returned_destroyed": phi_returned_or_destroyed,
                "written_attestation": written_attestation_obtained,
            },
        },
        "total_score": total,
        "max_score": max_score,
        "outcome": outcome.value,
        "notification_required": outcome != BreachAssessmentOutcome.LOW_PROBABILITY,
        "rationale": (
            f"Four-factor assessment score: {total}/{max_score}. "
            f"{'Low probability of compromise — not a reportable breach.' if outcome == BreachAssessmentOutcome.LOW_PROBABILITY else ''}"
            f"{'Assessment inconclusive — presumed reportable breach under burden of proof standard.' if outcome == BreachAssessmentOutcome.PRESUMED_BREACH else ''}"
            f"{'Reportable breach — notification required.' if outcome == BreachAssessmentOutcome.REPORTABLE else ''}"
        ),
    }


def calculate_hipaa_deadlines(
    discovery_date: str,
    affected_count: int,
    state_distribution: dict,
) -> dict:
    """
    Calculate all HIPAA breach notification deadlines.

    Args:
        discovery_date: ISO 8601 date of breach discovery.
        affected_count: Total number of affected individuals.
        state_distribution: Dict mapping state abbreviations to affected counts.

    Returns:
        Complete deadline schedule with notification obligations.
    """
    discovery_dt = datetime.fromisoformat(discovery_date)
    if discovery_dt.tzinfo is None:
        discovery_dt = discovery_dt.replace(tzinfo=timezone.utc)

    individual_deadline = discovery_dt + timedelta(days=60)

    if affected_count >= 500:
        hhs_tier = NotificationTier.TIER_500_PLUS
        hhs_deadline = individual_deadline
    else:
        hhs_tier = NotificationTier.TIER_UNDER_500
        year_end = datetime(discovery_dt.year, 12, 31, tzinfo=timezone.utc)
        hhs_deadline = datetime(discovery_dt.year + 1, 3, 1, tzinfo=timezone.utc)

    media_states = [
        state for state, count in state_distribution.items() if count >= 500
    ]

    ag_states = list(state_distribution.keys())

    return {
        "discovery_date": discovery_dt.isoformat(),
        "affected_count": affected_count,
        "deadlines": {
            "individual_notification": {
                "deadline": individual_deadline.isoformat(),
                "requirement": "45 CFR §164.404(b) — no later than 60 days from discovery",
                "recommended_dispatch": (individual_deadline - timedelta(days=5)).isoformat(),
            },
            "hhs_notification": {
                "tier": hhs_tier.value,
                "deadline": hhs_deadline.isoformat(),
                "requirement": (
                    "45 CFR §164.408(b) — 60 days from discovery (500+ breach)"
                    if hhs_tier == NotificationTier.TIER_500_PLUS
                    else "45 CFR §164.408(c) — March 1 following calendar year (under 500)"
                ),
                "portal": "ocrportal.hhs.gov",
            },
            "state_ag_notification": {
                "states": ag_states,
                "deadline": "Before or concurrent with individual notification",
                "requirement": "45 CFR §164.412",
            },
            "media_notification": {
                "required": len(media_states) > 0,
                "states_requiring_media": media_states,
                "deadline": individual_deadline.isoformat() if media_states else None,
                "requirement": "45 CFR §164.406 — 500+ individuals in a single state",
            },
        },
        "substitute_notice": {
            "required": False,
            "note": "Required if 10+ individuals have insufficient contact information (§164.404(d))",
            "web_posting_duration_days": 90,
            "toll_free_active_days": 90,
        },
    }


def main():
    print("=" * 70)
    print("HIPAA FOUR-FACTOR BREACH RISK ASSESSMENT")
    print("=" * 70)

    print("\nScenario A: Laptop theft with encrypted PHI")
    assessment_a = four_factor_assessment(
        phi_types=["patient_names", "dates_of_birth", "diagnosis_codes", "insurance_ids"],
        includes_ssn=False,
        includes_financial=False,
        includes_clinical=True,
        unauthorized_person_known=False,
        unauthorized_person_hipaa_covered=False,
        phi_actually_viewed=False,
        phi_acquired_or_copied=False,
        risk_mitigated=True,
        phi_returned_or_destroyed=False,
        written_attestation_obtained=False,
    )
    print(json.dumps(assessment_a, indent=2))

    print("\nScenario B: Phishing attack exposing patient records")
    assessment_b = four_factor_assessment(
        phi_types=["patient_names", "ssn", "dates_of_birth", "diagnosis_codes", "treatment_records", "insurance_ids", "addresses"],
        includes_ssn=True,
        includes_financial=True,
        includes_clinical=True,
        unauthorized_person_known=False,
        unauthorized_person_hipaa_covered=False,
        phi_actually_viewed=True,
        phi_acquired_or_copied=True,
        risk_mitigated=False,
        phi_returned_or_destroyed=False,
        written_attestation_obtained=False,
    )
    print(json.dumps(assessment_b, indent=2))

    print("\n" + "=" * 70)
    print("HIPAA NOTIFICATION DEADLINES")
    print("=" * 70)

    deadlines = calculate_hipaa_deadlines(
        discovery_date="2026-03-13T14:30:00+00:00",
        affected_count=8420,
        state_distribution={
            "CA": 2100,
            "TX": 1850,
            "FL": 920,
            "NY": 780,
            "IL": 650,
            "PA": 540,
            "OH": 430,
            "GA": 380,
            "NC": 350,
            "MI": 270,
            "Other": 150,
        },
    )
    print(json.dumps(deadlines, indent=2))


if __name__ == "__main__":
    main()
