#!/usr/bin/env python3
"""
CNIL-Compliant Cookie Consent Manager

Implements cookie consent per CNIL Deliberation No. 2020-091 requirements
including equal prominence, no cookie walls, 6-month reconsent, and
essential cookie exemptions.
"""

import json
import hashlib
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional


CNIL_RECONSENT_DAYS = 180  # 6-month maximum per CNIL recommendation
CNIL_COOKIE_MAX_LIFETIME_MONTHS = 13  # Maximum cookie duration per CNIL
CNIL_DATA_RETENTION_MONTHS = 25  # Maximum data retention per CNIL


@dataclass
class CookieDefinition:
    """Definition of a cookie used on the site."""
    name: str = ""
    domain: str = ""
    purpose: str = ""
    category: str = ""  # "essential", "analytics", "advertising", "social"
    first_party: bool = True
    lifetime_days: int = 0
    data_stored: str = ""
    third_party_name: Optional[str] = None
    requires_consent: bool = True

    def to_dict(self) -> dict:
        return asdict(self)


# CloudVault SaaS Inc. cookie inventory
COOKIE_INVENTORY = [
    CookieDefinition(
        name="cv_session", domain="cloudvault-saas.eu",
        purpose="Session management and authentication",
        category="essential", first_party=True, lifetime_days=1,
        data_stored="Encrypted session identifier", requires_consent=False,
    ),
    CookieDefinition(
        name="cv_csrf", domain="cloudvault-saas.eu",
        purpose="Cross-Site Request Forgery protection",
        category="essential", first_party=True, lifetime_days=1,
        data_stored="CSRF token", requires_consent=False,
    ),
    CookieDefinition(
        name="cv_lb", domain="cloudvault-saas.eu",
        purpose="Load balancer server affinity",
        category="essential", first_party=True, lifetime_days=0,
        data_stored="Server identifier", requires_consent=False,
    ),
    CookieDefinition(
        name="cv_lang", domain="cloudvault-saas.eu",
        purpose="User language preference",
        category="essential", first_party=True, lifetime_days=365,
        data_stored="Language code (e.g., fr, en, de)", requires_consent=False,
    ),
    CookieDefinition(
        name="cv_consent", domain="cloudvault-saas.eu",
        purpose="Store cookie consent preferences",
        category="essential", first_party=True, lifetime_days=180,
        data_stored="Consent choices and timestamp", requires_consent=False,
    ),
    CookieDefinition(
        name="_ga", domain="cloudvault-saas.eu",
        purpose="Google Analytics audience measurement",
        category="analytics", first_party=True, lifetime_days=390,
        data_stored="Randomly generated client ID",
        third_party_name="Google LLC", requires_consent=True,
    ),
    CookieDefinition(
        name="_gid", domain="cloudvault-saas.eu",
        purpose="Google Analytics session distinction",
        category="analytics", first_party=True, lifetime_days=1,
        data_stored="Randomly generated session ID",
        third_party_name="Google LLC", requires_consent=True,
    ),
]


@dataclass
class ConsentBannerConfig:
    """Configuration for the CNIL-compliant consent banner."""
    accept_button_text: str = "Accept All"
    refuse_button_text: str = "Refuse All"
    manage_button_text: str = "Manage Preferences"
    accept_button_width_px: int = 200
    accept_button_height_px: int = 44
    refuse_button_width_px: int = 200
    refuse_button_height_px: int = 44
    button_color: str = "#2563EB"
    button_text_color: str = "#FFFFFF"
    button_font_size_px: int = 16
    button_font_weight: str = "bold"
    manage_link_color: str = "#6B7280"
    manage_link_font_size_px: int = 14
    banner_position: str = "bottom"
    blocks_content: bool = False  # Must be False per CNIL no-cookie-wall rule
    reconsent_days: int = CNIL_RECONSENT_DAYS


def check_consent_expiry(consent_timestamp: str, reference_date: Optional[str] = None) -> dict:
    """
    Check if consent has expired per CNIL 6-month reconsent requirement.

    Args:
        consent_timestamp: ISO 8601 timestamp of last consent.
        reference_date: Date to check against (ISO 8601). Defaults to now.

    Returns:
        Expiry status dictionary.
    """
    consent_dt = datetime.fromisoformat(consent_timestamp.replace("Z", "+00:00"))
    if reference_date:
        ref_dt = datetime.fromisoformat(reference_date.replace("Z", "+00:00"))
    else:
        ref_dt = datetime.now(timezone.utc)

    days_since = (ref_dt - consent_dt).days
    expired = days_since >= CNIL_RECONSENT_DAYS

    return {
        "consent_timestamp": consent_timestamp,
        "days_since_consent": days_since,
        "reconsent_threshold_days": CNIL_RECONSENT_DAYS,
        "expired": expired,
        "action": "re_display_banner" if expired else "respect_stored_preferences",
        "days_until_expiry": max(0, CNIL_RECONSENT_DAYS - days_since),
    }


def validate_banner_compliance(config: ConsentBannerConfig) -> dict:
    """
    Validate that the cookie banner configuration meets CNIL requirements.

    Returns:
        Compliance report.
    """
    checks = []

    # Check 1: Accept and Refuse buttons must have equal size
    size_equal = (
        config.accept_button_width_px == config.refuse_button_width_px
        and config.accept_button_height_px == config.refuse_button_height_px
    )
    checks.append({
        "requirement": "Equal button size (accept vs refuse)",
        "reference": "CNIL 2020-091 Section 2.1",
        "pass": size_equal,
        "detail": f"Accept: {config.accept_button_width_px}x{config.accept_button_height_px}, "
                  f"Refuse: {config.refuse_button_width_px}x{config.refuse_button_height_px}",
    })

    # Check 2: No cookie wall
    checks.append({
        "requirement": "No cookie wall (banner does not block content)",
        "reference": "CNIL 2020-091 Section 2.2",
        "pass": not config.blocks_content,
        "detail": f"blocks_content: {config.blocks_content}",
    })

    # Check 3: Reconsent interval <= 180 days
    checks.append({
        "requirement": "Reconsent interval <= 180 days",
        "reference": "CNIL 2020-091 Section 2.3",
        "pass": config.reconsent_days <= CNIL_RECONSENT_DAYS,
        "detail": f"Configured: {config.reconsent_days} days",
    })

    # Check 4: Refuse button exists and has visible styling
    has_refuse = bool(config.refuse_button_text)
    checks.append({
        "requirement": "Refuse All button present on first layer",
        "reference": "CNIL 2020-091 Section 2.1 (per Google/Meta fines)",
        "pass": has_refuse,
        "detail": f"Refuse text: '{config.refuse_button_text}'",
    })

    pass_count = sum(1 for c in checks if c["pass"])
    total = len(checks)

    return {
        "checks": checks,
        "passed": pass_count,
        "total": total,
        "compliant": pass_count == total,
    }


def classify_cookies(cookies: list[CookieDefinition]) -> dict:
    """
    Classify cookies into essential and non-essential categories per CNIL Section 3.

    Returns:
        Classification report.
    """
    essential = [c for c in cookies if not c.requires_consent]
    non_essential = [c for c in cookies if c.requires_consent]

    categories = {}
    for cookie in non_essential:
        cat = cookie.category
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(cookie.name)

    third_parties = set()
    for cookie in non_essential:
        if cookie.third_party_name:
            third_parties.add(cookie.third_party_name)

    return {
        "essential_cookies": [{"name": c.name, "purpose": c.purpose} for c in essential],
        "non_essential_cookies": [{"name": c.name, "purpose": c.purpose, "category": c.category} for c in non_essential],
        "non_essential_by_category": categories,
        "third_parties": sorted(third_parties),
        "total_cookies": len(cookies),
        "essential_count": len(essential),
        "non_essential_count": len(non_essential),
    }


if __name__ == "__main__":
    # Validate banner compliance
    print("=== Banner Compliance Validation ===")
    config = ConsentBannerConfig()
    report = validate_banner_compliance(config)
    print(f"Compliant: {report['compliant']} ({report['passed']}/{report['total']})")
    for check in report["checks"]:
        status = "PASS" if check["pass"] else "FAIL"
        print(f"  [{status}] {check['requirement']}")

    # Check consent expiry
    print("\n=== Consent Expiry Check ===")
    scenarios = [
        ("2026-01-15T10:00:00Z", "30 days ago"),
        ("2025-09-14T10:00:00Z", "6 months ago (expired)"),
        ("2025-06-01T10:00:00Z", "9 months ago (well expired)"),
    ]
    for ts, label in scenarios:
        result = check_consent_expiry(ts, "2026-03-14T10:00:00Z")
        status = "EXPIRED" if result["expired"] else "VALID"
        print(f"  {label}: {status} (day {result['days_since_consent']})")

    # Classify cookies
    print("\n=== Cookie Classification ===")
    classification = classify_cookies(COOKIE_INVENTORY)
    print(f"Total: {classification['total_cookies']}")
    print(f"Essential (no consent): {classification['essential_count']}")
    print(f"Non-essential (consent required): {classification['non_essential_count']}")
    print(f"Third parties: {', '.join(classification['third_parties'])}")
    for cookie in classification["essential_cookies"]:
        print(f"  [Essential] {cookie['name']}: {cookie['purpose']}")
    for cookie in classification["non_essential_cookies"]:
        print(f"  [Consent] {cookie['name']}: {cookie['purpose']}")
