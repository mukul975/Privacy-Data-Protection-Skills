#!/usr/bin/env python3
"""
GDPR Parental Consent Verification Tool

Manages parental consent verification for children's data processing
under GDPR Article 8, including age threshold determination by EU/EEA
Member State, consent record creation, and verification tracking.
"""

import json
import hashlib
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional

# EU/EEA Member State age thresholds for Art. 8(1)
AGE_THRESHOLDS = {
    "AT": 14, "BE": 13, "BG": 14, "HR": 16, "CY": 14,
    "CZ": 15, "DK": 13, "EE": 13, "FI": 13, "FR": 15,
    "DE": 16, "GR": 15, "HU": 16, "IE": 16, "IT": 14,
    "LV": 13, "LT": 14, "LU": 16, "MT": 13, "NL": 16,
    "NO": 13, "PL": 16, "PT": 13, "RO": 16, "SK": 16,
    "SI": 16, "ES": 14, "SE": 13, "GB": 13,
}

VERIFICATION_TIERS = {
    "tier_1_high": [
        "electronic_id_eidas",
        "video_call_verification",
        "credit_card_transaction",
        "government_id_upload",
    ],
    "tier_2_medium": [
        "email_plus_verification",
        "sms_verification_callback",
        "parental_account_linking",
        "digital_signature",
    ],
    "tier_3_basic": [
        "email_verification",
        "checkbox_declaration",
    ],
}


@dataclass
class ParentalConsentRecord:
    """Represents a parental consent record per GDPR Art. 7(1) and Art. 8."""

    consent_id: str
    child_identifier: str
    child_age_at_consent: int
    applicable_threshold: int
    applicable_country: str
    parent_identifier: str
    verification_method: str
    verification_outcome: str  # "verified", "failed", "expired"
    purposes: list[dict]
    data_categories: list[str]
    consent_text_version: str
    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    withdrawal_mechanism: str = "parental_dashboard"
    expiry_date: str = field(
        default_factory=lambda: (
            datetime.now(timezone.utc) + timedelta(days=365)
        ).strftime("%Y-%m-%d")
    )
    controller_name: str = "BrightPath Learning Inc."
    controller_address: str = "200 Education Lane, Amsterdam, 1012 AB, Netherlands"

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)


def get_age_threshold(country_code: str) -> int:
    """Return the Art. 8 age threshold for a given EU/EEA country code."""
    return AGE_THRESHOLDS.get(country_code.upper(), 16)


def calculate_age(date_of_birth: str) -> int:
    """Calculate age from a date of birth string (YYYY-MM-DD format)."""
    dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    today = datetime.now(timezone.utc).date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


def requires_parental_consent(date_of_birth: str, country_code: str) -> dict:
    """
    Determine whether parental consent is required for a child in a given country.

    Returns a dictionary with the determination result and details.
    """
    age = calculate_age(date_of_birth)
    threshold = get_age_threshold(country_code)
    requires_consent = age < threshold

    return {
        "age": age,
        "country_code": country_code.upper(),
        "threshold": threshold,
        "requires_parental_consent": requires_consent,
        "determination": (
            f"Child aged {age} in {country_code.upper()} (threshold: {threshold}). "
            f"Parental consent {'REQUIRED' if requires_consent else 'NOT required'}."
        ),
    }


def recommend_verification_tier(
    data_sensitivity: str, has_social_features: bool, has_messaging: bool
) -> dict:
    """
    Recommend a parental verification tier based on processing risk.

    Args:
        data_sensitivity: "standard", "sensitive", or "special_category"
        has_social_features: Whether the service includes social features
        has_messaging: Whether the service enables direct messaging
    """
    if data_sensitivity == "special_category" or has_messaging:
        tier = "tier_1_high"
        rationale = (
            "High assurance required: "
            + ("special category data processing" if data_sensitivity == "special_category" else "")
            + ("; " if data_sensitivity == "special_category" and has_messaging else "")
            + ("direct messaging with strangers" if has_messaging else "")
        )
    elif data_sensitivity == "sensitive" or has_social_features:
        tier = "tier_2_medium"
        rationale = (
            "Medium assurance required: "
            + ("sensitive data processing" if data_sensitivity == "sensitive" else "")
            + ("; " if data_sensitivity == "sensitive" and has_social_features else "")
            + ("social features present" if has_social_features else "")
        )
    else:
        tier = "tier_3_basic"
        rationale = "Basic assurance: standard data processing with no social features"

    return {
        "recommended_tier": tier,
        "available_methods": VERIFICATION_TIERS[tier],
        "rationale": rationale,
    }


def compute_consent_text_version(consent_text: str) -> str:
    """Generate SHA-256 hash of consent text for version tracking."""
    return hashlib.sha256(consent_text.encode("utf-8")).hexdigest()


def validate_parental_consent_record(record: dict) -> list[str]:
    """
    Validate a parental consent record for Art. 7(1) and Art. 8 compliance.

    Returns a list of validation errors. Empty list means the record is valid.
    """
    required_fields = [
        "consent_id",
        "child_identifier",
        "child_age_at_consent",
        "applicable_threshold",
        "applicable_country",
        "parent_identifier",
        "verification_method",
        "verification_outcome",
        "purposes",
        "consent_text_version",
        "timestamp",
    ]

    errors = []

    for f in required_fields:
        if f not in record or record[f] is None:
            errors.append(f"Missing required field: {f}")

    if record.get("child_age_at_consent") is not None:
        age = record["child_age_at_consent"]
        threshold = record.get("applicable_threshold", 16)
        if age >= threshold:
            errors.append(
                f"Child age ({age}) is at or above threshold ({threshold}); "
                "parental consent record should not exist"
            )

    country = record.get("applicable_country", "")
    if country and country.upper() not in AGE_THRESHOLDS:
        errors.append(f"Unknown country code: {country}")

    if record.get("verification_outcome") not in ("verified", "failed", "expired"):
        errors.append(
            "Field 'verification_outcome' must be 'verified', 'failed', or 'expired'"
        )

    all_methods = []
    for methods in VERIFICATION_TIERS.values():
        all_methods.extend(methods)
    if record.get("verification_method") and record["verification_method"] not in all_methods:
        errors.append(f"Unknown verification method: {record['verification_method']}")

    purposes = record.get("purposes", [])
    if not isinstance(purposes, list) or len(purposes) == 0:
        errors.append("Field 'purposes' must be a non-empty list")
    else:
        for i, purpose in enumerate(purposes):
            if not isinstance(purpose, dict):
                errors.append(f"Purpose at index {i} must be a dictionary")
            elif "purpose_id" not in purpose or "description" not in purpose:
                errors.append(
                    f"Purpose at index {i} must have 'purpose_id' and 'description'"
                )

    if record.get("consent_text_version"):
        version = record["consent_text_version"]
        if len(version) != 64 or not all(c in "0123456789abcdef" for c in version):
            errors.append(
                "Field 'consent_text_version' must be a valid SHA-256 hex digest"
            )

    return errors


def check_consent_renewal_needed(consent_record: dict) -> dict:
    """Check whether a parental consent record needs renewal."""
    expiry = consent_record.get("expiry_date", "")
    if not expiry:
        return {"renewal_needed": True, "reason": "No expiry date set"}

    expiry_date = datetime.strptime(expiry, "%Y-%m-%d").date()
    today = datetime.now(timezone.utc).date()
    days_until_expiry = (expiry_date - today).days

    if days_until_expiry < 0:
        return {
            "renewal_needed": True,
            "reason": f"Consent expired {abs(days_until_expiry)} days ago",
            "days_expired": abs(days_until_expiry),
        }
    elif days_until_expiry <= 30:
        return {
            "renewal_needed": True,
            "reason": f"Consent expires in {days_until_expiry} days",
            "days_until_expiry": days_until_expiry,
        }
    else:
        return {
            "renewal_needed": False,
            "reason": f"Consent valid for {days_until_expiry} more days",
            "days_until_expiry": days_until_expiry,
        }


if __name__ == "__main__":
    # Demonstrate age threshold determination
    print("=== Age Threshold Determination ===")
    test_cases = [
        ("2014-06-15", "FR"),  # 11-year-old in France (threshold 15)
        ("2012-03-20", "BE"),  # 14-year-old in Belgium (threshold 13)
        ("2010-09-01", "DE"),  # 15-year-old in Germany (threshold 16)
        ("2008-01-10", "GB"),  # 18-year-old in UK (threshold 13)
    ]

    for dob, country in test_cases:
        result = requires_parental_consent(dob, country)
        print(f"  {result['determination']}")

    # Demonstrate verification tier recommendation
    print("\n=== Verification Tier Recommendations ===")
    scenarios = [
        ("special_category", False, True),
        ("standard", True, False),
        ("standard", False, False),
    ]

    for sensitivity, social, messaging in scenarios:
        rec = recommend_verification_tier(sensitivity, social, messaging)
        print(f"  {rec['recommended_tier']}: {rec['rationale']}")
        print(f"    Methods: {', '.join(rec['available_methods'])}")

    # Demonstrate consent record creation and validation
    print("\n=== Consent Record Validation ===")
    consent_text = (
        "I, as the parent or legal guardian, consent to BrightPath Learning Inc. "
        "collecting and processing my child's name, age, and learning progress data "
        "for the purpose of providing educational gaming content. I understand I can "
        "withdraw this consent at any time through the parental dashboard."
    )

    record = ParentalConsentRecord(
        consent_id="PC-2026-0003891",
        child_identifier="child_bp_8f3a2d",
        child_age_at_consent=12,
        applicable_threshold=15,
        applicable_country="FR",
        parent_identifier="parent_bp_c7e4f1",
        verification_method="credit_card_transaction",
        verification_outcome="verified",
        purposes=[
            {
                "purpose_id": "edu_content_delivery",
                "description": "Deliver educational gaming content",
                "consented": True,
            },
            {
                "purpose_id": "progress_tracking",
                "description": "Track learning progress for parent reports",
                "consented": True,
            },
        ],
        data_categories=["name", "age", "learning_progress", "game_interactions"],
        consent_text_version=compute_consent_text_version(consent_text),
    )

    errors = validate_parental_consent_record(record.to_dict())
    if not errors:
        print("  Record is valid per Art. 7(1) and Art. 8 requirements.")
    else:
        for err in errors:
            print(f"  ERROR: {err}")

    # Demonstrate consent renewal check
    print("\n=== Consent Renewal Check ===")
    renewal = check_consent_renewal_needed(record.to_dict())
    print(f"  Renewal needed: {renewal['renewal_needed']}")
    print(f"  Reason: {renewal['reason']}")
