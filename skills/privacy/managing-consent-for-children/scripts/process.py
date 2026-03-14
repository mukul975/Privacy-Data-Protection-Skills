#!/usr/bin/env python3
"""
Children's Consent Management System

Implements age verification, parental consent workflows, and country-specific
threshold management per GDPR Article 8 and COPPA requirements.
"""

import json
import hashlib
import hmac
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional


# GDPR Article 8 age thresholds by country (ISO 3166-1 alpha-2)
AGE_THRESHOLDS = {
    "AT": {"threshold": 14, "law": "Austrian DSG Section 4(4)"},
    "BE": {"threshold": 13, "law": "Law of 30 July 2018, Art. 7"},
    "BG": {"threshold": 14, "law": "Personal Data Protection Act Art. 25b"},
    "HR": {"threshold": 16, "law": "GDPR default"},
    "CY": {"threshold": 14, "law": "Law 125(I)/2018"},
    "CZ": {"threshold": 15, "law": "Act No. 110/2019, Section 7"},
    "DK": {"threshold": 13, "law": "Danish DPA Section 12"},
    "EE": {"threshold": 13, "law": "Personal Data Protection Act Section 8"},
    "FI": {"threshold": 13, "law": "Data Protection Act 1050/2018, Section 5"},
    "FR": {"threshold": 15, "law": "Loi Informatique et Libertés, Art. 45"},
    "DE": {"threshold": 16, "law": "GDPR default"},
    "GR": {"threshold": 15, "law": "Law 4624/2019, Art. 21"},
    "HU": {"threshold": 16, "law": "GDPR default"},
    "IE": {"threshold": 16, "law": "Data Protection Act 2018, Section 31"},
    "IT": {"threshold": 14, "law": "Legislative Decree 101/2018, Art. 2-quinquies"},
    "LV": {"threshold": 13, "law": "Personal Data Processing Law, Section 9"},
    "LT": {"threshold": 14, "law": "Law on Legal Protection of Personal Data, Art. 5"},
    "LU": {"threshold": 16, "law": "GDPR default"},
    "MT": {"threshold": 13, "law": "Data Protection Act Chapter 586, Art. 8"},
    "NL": {"threshold": 16, "law": "GDPR default"},
    "PL": {"threshold": 16, "law": "GDPR default"},
    "PT": {"threshold": 13, "law": "Law 58/2019, Art. 16"},
    "RO": {"threshold": 16, "law": "GDPR default"},
    "SK": {"threshold": 16, "law": "GDPR default"},
    "SI": {"threshold": 16, "law": "GDPR default"},
    "ES": {"threshold": 14, "law": "Organic Law 3/2018, Art. 7"},
    "SE": {"threshold": 13, "law": "Data Protection Act (2018:218), Ch. 2 Sec. 4"},
    "GB": {"threshold": 13, "law": "UK Data Protection Act 2018, Section 9"},
    "US": {"threshold": 13, "law": "COPPA (15 U.S.C. Section 6501-6506)"},
}


class VerificationMethod:
    EMAIL_LINK = "email_link"
    CREDIT_CARD = "credit_card_micro_transaction"
    GOVERNMENT_ID = "government_id"
    SIGNED_FORM = "signed_consent_form"
    VIDEO_CALL = "video_call"
    KNOWLEDGE_BASED = "knowledge_based"


@dataclass
class AgeCheckResult:
    """Result of age verification for a user registration."""
    user_date_of_birth: str
    user_country: str
    calculated_age: int
    applicable_threshold: int
    applicable_law: str
    requires_parental_consent: bool
    is_coppa_applicable: bool

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ParentalConsentRequest:
    """A parental consent request sent to a parent/guardian."""
    request_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    child_id: str = ""
    child_first_name: str = ""
    parent_email: str = ""
    parent_name: str = ""
    relationship: str = "parent"  # "parent" or "legal_guardian"
    verification_link: str = ""
    link_expiry: str = ""
    purposes: list = field(default_factory=list)
    status: str = "pending"  # "pending", "approved", "declined", "expired"
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    responded_at: Optional[str] = None
    verification_method: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ParentalConsentRecord:
    """Recorded parental consent after verification."""
    record_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    request_id: str = ""
    child_id: str = ""
    parent_identifier: str = ""  # hashed email
    relationship: str = "parent"
    verification_method: str = ""
    per_purpose_decisions: dict = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    consent_text_version: str = ""
    country: str = ""
    applicable_law: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


def calculate_age(date_of_birth: str, reference_date: str = "2026-03-14") -> int:
    """
    Calculate age in years from a date of birth.

    Args:
        date_of_birth: Date of birth in YYYY-MM-DD format.
        reference_date: Date to calculate age against (YYYY-MM-DD).

    Returns:
        Age in complete years.
    """
    dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
    ref = datetime.strptime(reference_date, "%Y-%m-%d")
    age = ref.year - dob.year
    if (ref.month, ref.day) < (dob.month, dob.day):
        age -= 1
    return age


def check_age_threshold(date_of_birth: str, country_code: str) -> AgeCheckResult:
    """
    Check if a user requires parental consent based on their age and country.

    Args:
        date_of_birth: User's date of birth (YYYY-MM-DD).
        country_code: ISO 3166-1 alpha-2 country code.

    Returns:
        AgeCheckResult with determination.
    """
    age = calculate_age(date_of_birth)
    country_info = AGE_THRESHOLDS.get(country_code, {"threshold": 16, "law": "GDPR default (Art. 8)"})

    return AgeCheckResult(
        user_date_of_birth=date_of_birth,
        user_country=country_code,
        calculated_age=age,
        applicable_threshold=country_info["threshold"],
        applicable_law=country_info["law"],
        requires_parental_consent=age < country_info["threshold"],
        is_coppa_applicable=(country_code == "US" and age < 13),
    )


def generate_verification_link(
    child_id: str,
    parent_email: str,
    secret_key: str = "cloudvault-parental-consent-hmac-key-2026",
    base_url: str = "https://app.cloudvault-saas.eu/consent/parental",
) -> tuple[str, str]:
    """
    Generate an HMAC-signed verification link for parental consent.

    Args:
        child_id: Child's account identifier.
        parent_email: Parent's email address.
        secret_key: HMAC signing key.
        base_url: Base URL for the consent form.

    Returns:
        Tuple of (verification_url, expiry_timestamp).
    """
    expiry = datetime.now(timezone.utc) + timedelta(hours=48)
    expiry_str = expiry.isoformat()

    payload = f"{child_id}:{parent_email}:{expiry_str}"
    signature = hmac.new(
        secret_key.encode("utf-8"),
        payload.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

    token = f"{child_id}:{expiry_str}:{signature}"
    # In production, token would be base64url-encoded
    url = f"{base_url}?token={hashlib.sha256(token.encode()).hexdigest()[:32]}"

    return url, expiry_str


def create_parental_consent_request(
    child_id: str,
    child_first_name: str,
    parent_email: str,
    parent_name: str,
    country_code: str,
    purposes: list[dict],
) -> ParentalConsentRequest:
    """
    Create a parental consent request to be sent via email.

    Args:
        child_id: Child's account identifier.
        child_first_name: Child's first name (data minimization — no surname).
        parent_email: Parent's email address.
        parent_name: Parent's name.
        country_code: Country for applicable law reference.
        purposes: List of processing purposes requiring consent.

    Returns:
        ParentalConsentRequest ready for email dispatch.
    """
    url, expiry = generate_verification_link(child_id, parent_email)

    return ParentalConsentRequest(
        child_id=child_id,
        child_first_name=child_first_name,
        parent_email=parent_email,
        parent_name=parent_name,
        verification_link=url,
        link_expiry=expiry,
        purposes=purposes,
    )


def determine_verification_requirements(country_code: str, purposes: list[dict]) -> list[str]:
    """
    Determine which verification methods are required based on country and purpose risk.

    Args:
        country_code: ISO country code.
        purposes: List of processing purposes.

    Returns:
        List of required verification methods.
    """
    methods = [VerificationMethod.EMAIL_LINK]  # Always required as baseline

    has_high_risk = any(p.get("risk_level") == "high" for p in purposes)
    has_profiling = any(p.get("involves_profiling", False) for p in purposes)
    has_data_sharing = any(p.get("involves_third_party", False) for p in purposes)

    if country_code == "US":
        # COPPA requires verifiable parental consent — email alone may be insufficient
        # for data sharing or profiling (FTC COPPA Rule 16 CFR 312.5(b))
        if has_data_sharing or has_profiling:
            methods.append(VerificationMethod.CREDIT_CARD)

    if has_high_risk or has_profiling:
        methods.append(VerificationMethod.CREDIT_CARD)

    return methods


if __name__ == "__main__":
    # Demonstrate age checking for various countries
    print("=== Age Threshold Checks ===")
    test_cases = [
        ("2014-06-15", "IE", "11-year-old in Ireland (threshold 16)"),
        ("2014-06-15", "GB", "11-year-old in UK (threshold 13)"),
        ("2012-01-10", "FR", "14-year-old in France (threshold 15)"),
        ("2012-01-10", "ES", "14-year-old in Spain (threshold 14)"),
        ("2015-09-20", "US", "10-year-old in US (COPPA threshold 13)"),
        ("2010-03-14", "DE", "16-year-old in Germany (threshold 16)"),
    ]

    for dob, country, description in test_cases:
        result = check_age_threshold(dob, country)
        status = "REQUIRES PARENTAL CONSENT" if result.requires_parental_consent else "CAN SELF-CONSENT"
        coppa = " [COPPA APPLIES]" if result.is_coppa_applicable else ""
        print(f"  {description}: Age {result.calculated_age}, Threshold {result.applicable_threshold} -> {status}{coppa}")
        print(f"    Law: {result.applicable_law}")

    # Demonstrate parental consent request creation
    print("\n=== Parental Consent Request ===")
    purposes = [
        {"purpose_id": "pur_account_001", "name": "Account Management", "required": True, "risk_level": "low"},
        {"purpose_id": "pur_analytics_002", "name": "Service Improvement Analytics", "required": False, "risk_level": "medium", "involves_profiling": False},
        {"purpose_id": "pur_benchmarking_003", "name": "Industry Benchmarking", "required": False, "risk_level": "high", "involves_third_party": True},
    ]

    request = create_parental_consent_request(
        child_id="usr_child_abc123",
        child_first_name="Emma",
        parent_email="parent@protonmail.com",
        parent_name="Sarah Johnson",
        country_code="IE",
        purposes=purposes,
    )
    print(json.dumps(request.to_dict(), indent=2, default=str))

    # Determine verification requirements
    print("\n=== Verification Requirements ===")
    for country in ["IE", "US", "DE"]:
        methods = determine_verification_requirements(country, purposes)
        country_name = AGE_THRESHOLDS.get(country, {}).get("law", country)
        print(f"  {country}: {', '.join(methods)}")
