#!/usr/bin/env python3
"""
Cookie Consent A/B Test Dark Pattern Auditor

Detects dark patterns in consent banner variants by analyzing
visual asymmetry, interaction asymmetry, language manipulation,
timing delays, and repeated prompting per CNIL guidelines.
"""

import json
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class ButtonMetrics:
    """Measured properties of a consent banner button."""
    label: str = ""
    width_px: int = 0
    height_px: int = 0
    font_size_px: int = 0
    font_weight: str = "normal"  # "normal", "bold", "600", etc.
    background_color: str = ""  # hex color
    text_color: str = ""  # hex color
    border: bool = False
    shadow: bool = False
    position: str = ""  # "primary_left", "primary_right", "secondary", "footer_link"
    above_fold: bool = True


@dataclass
class ConsentVariant:
    """A single A/B test variant of a consent banner."""
    variant_id: str = ""
    variant_name: str = ""
    traffic_percentage: float = 0.0
    accept_button: ButtonMetrics = field(default_factory=ButtonMetrics)
    reject_button: Optional[ButtonMetrics] = None
    manage_button: Optional[ButtonMetrics] = None
    accept_clicks: int = 1
    reject_clicks: int = 1
    accept_language_neutral: bool = True
    reject_language_neutral: bool = True
    accept_text: str = ""
    reject_text: str = ""
    both_buttons_render_simultaneously: bool = True
    reject_delay_ms: int = 0
    banner_reappears_after_reject: bool = False
    reconsent_interval_days: int = 180
    pre_selected_purposes: bool = False
    cookie_wall: bool = False
    dismiss_defaults_to_accept: bool = False
    consent_rate: Optional[float] = None
    sample_size: Optional[int] = None

    def to_dict(self) -> dict:
        return asdict(self)


DARK_PATTERN_CATEGORIES = {
    "visual_asymmetry": {"weight": 0.25, "max_score": 10},
    "interaction_asymmetry": {"weight": 0.30, "max_score": 10},
    "language_manipulation": {"weight": 0.20, "max_score": 10},
    "timing_delay": {"weight": 0.15, "max_score": 10},
    "repeated_prompting": {"weight": 0.10, "max_score": 10},
}


def assess_visual_asymmetry(variant: ConsentVariant) -> dict:
    """Assess visual asymmetry between accept and reject buttons."""
    score = 0
    findings = []

    if variant.reject_button is None:
        score = 10
        findings.append("No reject button present on first layer (CNIL violation)")
        return {"score": score, "findings": findings}

    accept = variant.accept_button
    reject = variant.reject_button

    # Size comparison
    accept_area = accept.width_px * accept.height_px
    reject_area = reject.width_px * reject.height_px
    if accept_area > 0 and reject_area > 0:
        size_ratio = reject_area / accept_area
        if size_ratio < 0.5:
            score += 4
            findings.append(f"Reject button area is {size_ratio:.0%} of accept button area")
        elif size_ratio < 0.8:
            score += 2
            findings.append(f"Reject button slightly smaller ({size_ratio:.0%} of accept)")

    # Font comparison
    if accept.font_size_px > reject.font_size_px:
        score += 2
        findings.append(f"Accept font ({accept.font_size_px}px) larger than reject ({reject.font_size_px}px)")

    if accept.font_weight == "bold" and reject.font_weight == "normal":
        score += 1
        findings.append("Accept is bold, reject is normal weight")

    # Color/visibility
    if accept.background_color and not reject.background_color:
        score += 2
        findings.append("Accept has background color, reject does not (text link style)")

    # Position
    if accept.above_fold and not reject.above_fold:
        score += 2
        findings.append("Accept is above fold, reject is below fold")

    if not findings:
        findings.append("Accept and reject buttons are visually symmetric")

    return {"score": min(score, 10), "findings": findings}


def assess_interaction_asymmetry(variant: ConsentVariant) -> dict:
    """Assess click/interaction asymmetry between accept and reject paths."""
    score = 0
    findings = []

    click_diff = variant.reject_clicks - variant.accept_clicks
    if click_diff > 0:
        score = min(click_diff * 3, 10)
        findings.append(
            f"Reject requires {variant.reject_clicks} clicks vs {variant.accept_clicks} "
            f"for accept ({click_diff} extra clicks)"
        )
    elif click_diff == 0:
        findings.append("Equal click count for accept and reject")

    if variant.pre_selected_purposes:
        score = min(score + 3, 10)
        findings.append("Purposes are pre-selected (user must deselect to reject)")

    if variant.cookie_wall:
        score = 10
        findings.append("Cookie wall blocks content access (CNIL/EDPB prohibition)")

    if variant.dismiss_defaults_to_accept:
        score = min(score + 3, 10)
        findings.append("Dismissing banner (X button) defaults to accepting cookies")

    if not findings:
        findings.append("No interaction asymmetry detected")

    return {"score": min(score, 10), "findings": findings}


def assess_language_manipulation(variant: ConsentVariant) -> dict:
    """Assess language neutrality of accept and reject options."""
    score = 0
    findings = []

    manipulative_accept_phrases = [
        "enjoy", "personalized", "best experience", "continue enjoying",
        "recommended", "unlock", "enhance",
    ]
    discouraging_reject_phrases = [
        "limited", "basic", "don't want", "miss out",
        "less relevant", "generic", "reduced",
    ]

    accept_lower = variant.accept_text.lower()
    reject_lower = variant.reject_text.lower()

    for phrase in manipulative_accept_phrases:
        if phrase in accept_lower:
            score += 2
            findings.append(f"Accept text contains encouraging language: '{phrase}'")

    for phrase in discouraging_reject_phrases:
        if phrase in reject_lower:
            score += 2
            findings.append(f"Reject text contains discouraging language: '{phrase}'")

    if not variant.accept_language_neutral:
        score += 2
        findings.append("Accept language flagged as non-neutral")

    if not variant.reject_language_neutral:
        score += 2
        findings.append("Reject language flagged as non-neutral")

    if not findings:
        findings.append("Language is neutral for both options")

    return {"score": min(score, 10), "findings": findings}


def assess_timing_delay(variant: ConsentVariant) -> dict:
    """Assess timing and delay manipulation."""
    score = 0
    findings = []

    if not variant.both_buttons_render_simultaneously:
        score += 3
        findings.append("Accept and reject buttons do not render simultaneously")

    if variant.reject_delay_ms > 0:
        if variant.reject_delay_ms > 2000:
            score += 5
            findings.append(f"Reject path has {variant.reject_delay_ms}ms artificial delay")
        elif variant.reject_delay_ms > 500:
            score += 3
            findings.append(f"Reject path has {variant.reject_delay_ms}ms delay")

    if not findings:
        findings.append("No timing manipulation detected")

    return {"score": min(score, 10), "findings": findings}


def assess_repeated_prompting(variant: ConsentVariant) -> dict:
    """Assess whether the banner nags users after rejection."""
    score = 0
    findings = []

    if variant.banner_reappears_after_reject:
        score += 5
        findings.append("Banner reappears after user rejects cookies")

    if variant.reconsent_interval_days < 30:
        score += 3
        findings.append(f"Reconsent interval is {variant.reconsent_interval_days} days (too frequent)")
    elif variant.reconsent_interval_days < 90:
        score += 1
        findings.append(f"Reconsent interval is {variant.reconsent_interval_days} days (below CNIL 6-month recommendation)")

    if not findings:
        findings.append("No repeated prompting issues")

    return {"score": min(score, 10), "findings": findings}


def audit_variant(variant: ConsentVariant) -> dict:
    """
    Run full dark pattern audit on a consent banner variant.

    Returns:
        Audit result with per-category scores and overall risk score.
    """
    assessments = {
        "visual_asymmetry": assess_visual_asymmetry(variant),
        "interaction_asymmetry": assess_interaction_asymmetry(variant),
        "language_manipulation": assess_language_manipulation(variant),
        "timing_delay": assess_timing_delay(variant),
        "repeated_prompting": assess_repeated_prompting(variant),
    }

    weighted_score = sum(
        assessments[cat]["score"] * DARK_PATTERN_CATEGORIES[cat]["weight"]
        for cat in assessments
    )

    if weighted_score <= 1.0:
        risk_level = "LOW"
        recommendation = "Compliant — no action required"
    elif weighted_score <= 3.0:
        risk_level = "MEDIUM"
        recommendation = "Minor issues — remediate within 30 days"
    elif weighted_score <= 5.0:
        risk_level = "HIGH"
        recommendation = "Significant issues — remediate within 7 days"
    else:
        risk_level = "CRITICAL"
        recommendation = "Severe violations — remove variant immediately"

    return {
        "variant_id": variant.variant_id,
        "variant_name": variant.variant_name,
        "audit_date": datetime.now(timezone.utc).isoformat(),
        "assessments": assessments,
        "overall_score": round(weighted_score, 2),
        "risk_level": risk_level,
        "recommendation": recommendation,
    }


def compare_consent_rates(variants: list[ConsentVariant]) -> dict:
    """Analyze consent rates across variants for manipulation signals."""
    if not variants or not all(v.consent_rate is not None for v in variants):
        return {"analysis": "Insufficient data for consent rate comparison"}

    rates = [(v.variant_name, v.consent_rate, v.sample_size or 0) for v in variants]
    min_rate = min(r[1] for r in rates)
    max_rate = max(r[1] for r in rates)
    spread = max_rate - min_rate

    return {
        "variants": [{"name": r[0], "rate": r[1], "n": r[2]} for r in rates],
        "min_rate": min_rate,
        "max_rate": max_rate,
        "spread_percentage_points": round(spread * 100, 1),
        "red_flag": spread > 0.20,
        "note": "Spread > 20 percentage points with asymmetric design warrants investigation"
        if spread > 0.20 else "Consent rate spread within acceptable range",
    }


if __name__ == "__main__":
    # Compliant variant
    compliant = ConsentVariant(
        variant_id="exp_2026q1_001_A",
        variant_name="Control: Symmetric Banner",
        traffic_percentage=50.0,
        accept_button=ButtonMetrics(
            label="Accept All Cookies", width_px=240, height_px=48,
            font_size_px=16, font_weight="bold", background_color="#2563EB",
            text_color="#FFFFFF", position="primary_left", above_fold=True,
        ),
        reject_button=ButtonMetrics(
            label="Reject All Cookies", width_px=240, height_px=48,
            font_size_px=16, font_weight="bold", background_color="#2563EB",
            text_color="#FFFFFF", position="primary_right", above_fold=True,
        ),
        accept_clicks=1,
        reject_clicks=1,
        accept_text="Accept All Cookies",
        reject_text="Reject All Cookies",
        consent_rate=0.672,
        sample_size=50000,
    )

    # Non-compliant variant (mimics CNIL Google violation pattern)
    non_compliant = ConsentVariant(
        variant_id="exp_2026q1_001_B",
        variant_name="Test: Asymmetric (CNIL violation pattern)",
        traffic_percentage=50.0,
        accept_button=ButtonMetrics(
            label="Accept and enjoy personalized content", width_px=300, height_px=56,
            font_size_px=18, font_weight="bold", background_color="#22C55E",
            text_color="#FFFFFF", position="primary_left", above_fold=True,
        ),
        reject_button=None,  # No reject button on first layer
        manage_button=ButtonMetrics(
            label="Manage preferences", width_px=160, height_px=36,
            font_size_px=12, font_weight="normal", background_color="",
            text_color="#6B7280", position="footer_link", above_fold=False,
        ),
        accept_clicks=1,
        reject_clicks=3,  # Manage → toggle off each → Save
        accept_text="Accept and enjoy personalized content",
        reject_text="",
        accept_language_neutral=False,
        consent_rate=0.891,
        sample_size=50000,
    )

    # Audit both variants
    print("=== Compliant Variant Audit ===")
    result_a = audit_variant(compliant)
    print(f"Score: {result_a['overall_score']} ({result_a['risk_level']})")
    print(f"Recommendation: {result_a['recommendation']}")
    for cat, assessment in result_a["assessments"].items():
        print(f"  {cat}: {assessment['score']}/10")
        for f in assessment["findings"]:
            print(f"    - {f}")

    print("\n=== Non-Compliant Variant Audit ===")
    result_b = audit_variant(non_compliant)
    print(f"Score: {result_b['overall_score']} ({result_b['risk_level']})")
    print(f"Recommendation: {result_b['recommendation']}")
    for cat, assessment in result_b["assessments"].items():
        print(f"  {cat}: {assessment['score']}/10")
        for f in assessment["findings"]:
            print(f"    - {f}")

    # Compare consent rates
    print("\n=== Consent Rate Analysis ===")
    comparison = compare_consent_rates([compliant, non_compliant])
    print(f"Spread: {comparison['spread_percentage_points']} percentage points")
    print(f"Red Flag: {comparison['red_flag']}")
    print(f"Note: {comparison['note']}")
