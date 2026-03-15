#!/usr/bin/env python3
"""
Age-Gating Implementation Tool

Implements age-gating logic for online services including gate type selection,
neutral prompt validation, circumvention detection, and re-verification triggers.
"""

import json
import hashlib
from datetime import datetime, timezone, timedelta

AGE_THRESHOLDS = {
    "AT": 14, "BE": 13, "BG": 14, "HR": 16, "CY": 14,
    "CZ": 15, "DK": 13, "EE": 13, "FI": 13, "FR": 15,
    "DE": 16, "GR": 15, "HU": 16, "IE": 16, "IT": 14,
    "LV": 13, "LT": 14, "LU": 16, "MT": 13, "NL": 16,
    "NO": 13, "PL": 16, "PT": 13, "RO": 16, "SK": 16,
    "SI": 16, "ES": 14, "SE": 13, "GB": 13, "US": 13,
}

FEATURE_RESTRICTIONS = {
    "under_5": {
        "account_type": "denied",
        "message": "This app is designed for children aged 5 and older.",
    },
    "5_7": {
        "account_type": "parent_managed",
        "profile_visibility": "not_applicable",
        "messaging": "disabled",
        "recommendations": "curated_editorial",
        "advertising": "none",
        "data_sharing": "none",
    },
    "8_12": {
        "account_type": "child_with_oversight",
        "profile_visibility": "private_only",
        "messaging": "preset_messages",
        "recommendations": "content_based",
        "advertising": "none",
        "data_sharing": "none",
    },
    "13_15": {
        "account_type": "child_standard",
        "profile_visibility": "private_default_friends_available",
        "messaging": "moderated_contacts_only",
        "recommendations": "content_based",
        "advertising": "contextual_only",
        "data_sharing": "none_default",
    },
    "16_17": {
        "account_type": "young_adult",
        "profile_visibility": "private_default_public_available",
        "messaging": "unmoderated_contacts",
        "recommendations": "content_based_behavioural_optin",
        "advertising": "contextual_only",
        "data_sharing": "optional_with_consent",
    },
    "18_plus": {
        "account_type": "adult",
        "profile_visibility": "user_choice",
        "messaging": "unrestricted",
        "recommendations": "full_personalisation",
        "advertising": "behavioural_with_consent",
        "data_sharing": "per_privacy_policy",
    },
}


def calculate_age(date_of_birth: str) -> int:
    """Calculate age from YYYY-MM-DD date of birth."""
    dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    today = datetime.now(timezone.utc).date()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


def determine_age_tier(age: int) -> str:
    """Map age to the appropriate feature restriction tier."""
    if age < 5:
        return "under_5"
    elif age <= 7:
        return "5_7"
    elif age <= 12:
        return "8_12"
    elif age <= 15:
        return "13_15"
    elif age <= 17:
        return "16_17"
    else:
        return "18_plus"


def process_age_gate(date_of_birth: str, country_code: str) -> dict:
    """
    Process an age gate submission.

    Args:
        date_of_birth: User's DOB in YYYY-MM-DD format.
        country_code: Two-letter country code.

    Returns:
        Age gate result with routing decision and feature restrictions.
    """
    age = calculate_age(date_of_birth)
    threshold = AGE_THRESHOLDS.get(country_code.upper(), 16)
    tier = determine_age_tier(age)
    restrictions = FEATURE_RESTRICTIONS.get(tier, {})

    requires_parental_consent = age < threshold and tier != "under_5"
    is_denied = tier == "under_5"

    return {
        "age": age,
        "country_code": country_code.upper(),
        "threshold": threshold,
        "age_tier": tier,
        "routing": (
            "denied" if is_denied
            else "parental_consent_required" if requires_parental_consent
            else "independent_registration"
        ),
        "feature_restrictions": restrictions,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def detect_circumvention_signals(attempts: list[dict]) -> dict:
    """
    Analyze age gate attempts for circumvention signals.

    Args:
        attempts: List of dicts with keys: device_id, dob_entered, timestamp, outcome.

    Returns:
        Analysis with flagged signals.
    """
    signals = []

    # Check for multiple attempts from same device
    device_attempts: dict[str, list] = {}
    for attempt in attempts:
        did = attempt.get("device_id", "unknown")
        if did not in device_attempts:
            device_attempts[did] = []
        device_attempts[did].append(attempt)

    for device_id, device_list in device_attempts.items():
        if len(device_list) > 1:
            dobs = [a["dob_entered"] for a in device_list]
            if len(set(dobs)) > 1:
                signals.append({
                    "type": "multiple_dob_same_device",
                    "device_id": device_id,
                    "attempts": len(device_list),
                    "severity": "high",
                    "description": f"Device {device_id} submitted {len(set(dobs))} different DOBs",
                })

    # Check for exact threshold age
    for attempt in attempts:
        age = calculate_age(attempt["dob_entered"])
        country = attempt.get("country_code", "US")
        threshold = AGE_THRESHOLDS.get(country, 13)
        if age == threshold:
            dob = datetime.strptime(attempt["dob_entered"], "%Y-%m-%d").date()
            today = datetime.now(timezone.utc).date()
            days_past = (today - dob).days - (threshold * 365)
            if 0 <= days_past <= 30:
                signals.append({
                    "type": "exact_threshold_age",
                    "dob_entered": attempt["dob_entered"],
                    "severity": "medium",
                    "description": f"DOB results in age exactly at threshold ({threshold})",
                })

    # Check for January 1 DOB (common fake date)
    jan1_count = sum(1 for a in attempts if a["dob_entered"].endswith("-01-01"))
    if jan1_count > len(attempts) * 0.2 and len(attempts) >= 5:
        signals.append({
            "type": "january_1_anomaly",
            "count": jan1_count,
            "severity": "medium",
            "description": f"{jan1_count} of {len(attempts)} attempts used January 1 DOB",
        })

    return {
        "total_attempts": len(attempts),
        "signals_detected": len(signals),
        "signals": signals,
        "recommendation": (
            "No circumvention signals detected." if not signals
            else "Circumvention signals detected. Review flagged accounts."
        ),
    }


if __name__ == "__main__":
    print("=== Age Gate Processing ===")
    test_cases = [
        ("2023-06-15", "FR"),  # 2-year-old in France
        ("2018-03-20", "GB"),  # 8-year-old in UK
        ("2012-09-01", "DE"),  # 13-year-old in Germany
        ("2009-01-10", "BE"),  # 17-year-old in Belgium
    ]

    for dob, country in test_cases:
        result = process_age_gate(dob, country)
        print(f"  Age {result['age']} in {result['country_code']}: "
              f"tier={result['age_tier']}, routing={result['routing']}")

    print("\n=== Circumvention Detection ===")
    attempts = [
        {"device_id": "dev_001", "dob_entered": "2012-03-14", "timestamp": "2026-03-14T10:00:00Z", "outcome": "child", "country_code": "GB"},
        {"device_id": "dev_001", "dob_entered": "2005-03-14", "timestamp": "2026-03-14T10:05:00Z", "outcome": "adult", "country_code": "GB"},
        {"device_id": "dev_002", "dob_entered": "2013-03-14", "timestamp": "2026-03-14T11:00:00Z", "outcome": "child", "country_code": "GB"},
    ]

    analysis = detect_circumvention_signals(attempts)
    print(f"  Signals detected: {analysis['signals_detected']}")
    for signal in analysis["signals"]:
        print(f"    [{signal['severity']}] {signal['type']}: {signal['description']}")
