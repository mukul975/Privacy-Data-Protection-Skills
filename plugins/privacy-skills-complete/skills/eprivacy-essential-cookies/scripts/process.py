"""
Essential Cookie Classifier

Classifies cookies as strictly necessary (exempt) or consent-required
based on Article 29 Working Party Opinion 04/2012 (WP 194) criteria.

Requirements:
    No external dependencies (uses standard library only)
"""

import json
import os
from datetime import datetime, timezone


# WP 194 exemption categories and their criteria
WP194_CATEGORIES = {
    "A": {
        "name": "User Input Cookies",
        "description": "Track user input during multi-step process (forms, shopping cart)",
        "duration_requirement": "Session-only or short-lived (few hours)",
        "scope_requirement": "First-party only",
    },
    "B": {
        "name": "Authentication Cookies",
        "description": "Authenticate user to provide access to authenticated services",
        "duration_requirement": "Session for session auth; persistent only if user chose 'remember me'",
        "scope_requirement": "First-party only",
    },
    "C": {
        "name": "User Security Cookies",
        "description": "Ensure security of service explicitly requested by user",
        "duration_requirement": "Limited to what is necessary",
        "scope_requirement": "First-party only",
    },
    "D": {
        "name": "Multimedia Player Session Cookies",
        "description": "Store technical data for media playback",
        "duration_requirement": "Session-only",
        "scope_requirement": "First-party only",
    },
    "E": {
        "name": "Load Balancing Cookies",
        "description": "Distribute traffic across multiple servers",
        "duration_requirement": "Session-only",
        "scope_requirement": "First-party only",
    },
    "F": {
        "name": "UI Customisation Cookies (Session)",
        "description": "Store UI preferences explicitly set by user during session",
        "duration_requirement": "Session-only (persistent requires consent)",
        "scope_requirement": "First-party only",
    },
}

# Cookie classification rules
CLASSIFICATION_RULES = {
    # Category A: User Input
    "cart_session": {"exempt": True, "category": "A", "reason": "Shopping cart state during session"},
    "cart_items": {"exempt": True, "category": "A", "reason": "Shopping cart contents"},
    "checkout_step": {"exempt": True, "category": "A", "reason": "Checkout flow position"},
    "form_data_temp": {"exempt": True, "category": "A", "reason": "Form input preservation"},

    # Category B: Authentication
    "auth_token": {"exempt": True, "category": "B", "reason": "User authentication state"},
    "session_id": {"exempt": True, "category": "B", "reason": "Server session identification"},
    "refresh_token": {"exempt": True, "category": "B", "reason": "Persistent login (user-requested)"},

    # Category C: Security
    "csrf_token": {"exempt": True, "category": "C", "reason": "CSRF protection for form submissions"},
    "login_attempts": {"exempt": True, "category": "C", "reason": "Brute-force login protection"},
    "device_verified": {"exempt": True, "category": "C", "reason": "2FA device verification"},
    "__cf_bm": {"exempt": True, "category": "C", "reason": "Cloudflare bot management (session)"},

    # Category E: Load Balancing
    "SERVERID": {"exempt": True, "category": "E", "reason": "HAProxy server affinity"},
    "load_balancer": {"exempt": True, "category": "E", "reason": "Load balancer routing"},
    "lb_route": {"exempt": True, "category": "E", "reason": "Internal load balancer routing"},

    # Category F: UI Customisation (session only)
    "locale_session": {"exempt": True, "category": "F", "reason": "Language selection (current session)"},
    "currency_session": {"exempt": True, "category": "F", "reason": "Currency selection (current session)"},

    # Consent cookie (special case: strictly necessary for consent management)
    "consent_state": {"exempt": True, "category": "consent_management", "reason": "Records user consent choice"},
    "pinnacle_consent_eu": {"exempt": True, "category": "consent_management", "reason": "EU consent state"},
    "pinnacle_consent_uk": {"exempt": True, "category": "consent_management", "reason": "UK consent state"},
    "pinnacle_consent_ccpa": {"exempt": True, "category": "consent_management", "reason": "CCPA opt-out state"},

    # NON-EXEMPT: Analytics
    "_ga": {"exempt": False, "category": "analytics", "reason": "Google Analytics client ID — serves operator, not user"},
    "_gid": {"exempt": False, "category": "analytics", "reason": "GA session distinction — serves operator"},
    "_hj": {"exempt": False, "category": "analytics", "reason": "Hotjar tracking — serves operator"},

    # NON-EXEMPT: Advertising
    "_fbp": {"exempt": False, "category": "advertising", "reason": "Meta Pixel tracking — advertising purpose"},
    "_fbc": {"exempt": False, "category": "advertising", "reason": "Meta click tracking — advertising purpose"},
    "_gcl_au": {"exempt": False, "category": "advertising", "reason": "Google Ads conversion — advertising purpose"},
    "IDE": {"exempt": False, "category": "advertising", "reason": "DoubleClick ad serving — advertising purpose"},

    # NON-EXEMPT: Persistent preferences (exceed session scope)
    "locale": {"exempt": False, "category": "functionality", "reason": "Persistent language preference — exceeds session scope"},
    "currency": {"exempt": False, "category": "functionality", "reason": "Persistent currency preference — exceeds session scope"},
    "recently_viewed": {"exempt": False, "category": "functionality", "reason": "Enhancement, not strictly necessary"},
}


def classify_cookie(cookie_name: str, is_session: bool = False,
                    is_first_party: bool = True, duration_days: int = 0) -> dict:
    """Classify a single cookie as exempt or consent-required."""
    # Check known classifications
    for prefix, classification in CLASSIFICATION_RULES.items():
        if cookie_name == prefix or cookie_name.startswith(prefix):
            result = {
                "cookie_name": cookie_name,
                "classification_source": "known_rule",
                **classification,
            }
            # Additional validation for exempt cookies
            if classification["exempt"]:
                wp_cat = classification.get("category", "")
                if wp_cat in WP194_CATEGORIES:
                    cat_info = WP194_CATEGORIES[wp_cat]
                    # Check duration requirements
                    if "session" in cat_info["duration_requirement"].lower() and not is_session and duration_days > 1:
                        result["warning"] = f"Category {wp_cat} requires session-only, but cookie is persistent ({duration_days} days)"
                    # Check scope requirements
                    if not is_first_party:
                        result["warning"] = f"Category {wp_cat} requires first-party, but cookie is third-party"

            return result

    # Unknown cookie
    return {
        "cookie_name": cookie_name,
        "exempt": False,
        "category": "unknown",
        "reason": "Not in classification database — default to consent-required",
        "classification_source": "default_deny",
        "action_required": "Manual classification needed",
    }


def classify_cookie_inventory(cookies: list[dict]) -> dict:
    """Classify an entire cookie inventory."""
    results = {
        "classification_date": datetime.now(timezone.utc).isoformat(),
        "total_cookies": len(cookies),
        "exempt_cookies": [],
        "consent_required_cookies": [],
        "unknown_cookies": [],
        "warnings": [],
    }

    for cookie in cookies:
        classification = classify_cookie(
            cookie_name=cookie.get("name", ""),
            is_session=cookie.get("is_session", False),
            is_first_party=cookie.get("is_first_party", True),
            duration_days=cookie.get("duration_days", 0),
        )

        if classification.get("exempt"):
            results["exempt_cookies"].append(classification)
        elif classification.get("category") == "unknown":
            results["unknown_cookies"].append(classification)
        else:
            results["consent_required_cookies"].append(classification)

        if "warning" in classification:
            results["warnings"].append(classification)

    results["summary"] = {
        "exempt": len(results["exempt_cookies"]),
        "consent_required": len(results["consent_required_cookies"]),
        "unknown": len(results["unknown_cookies"]),
        "warnings": len(results["warnings"]),
    }

    return results


def main():
    """Run essential cookie classification for Pinnacle E-Commerce Ltd."""
    # Sample cookie inventory
    cookies = [
        {"name": "session_id", "is_session": True, "is_first_party": True, "duration_days": 0},
        {"name": "auth_token", "is_session": True, "is_first_party": True, "duration_days": 0},
        {"name": "csrf_token", "is_session": True, "is_first_party": True, "duration_days": 0},
        {"name": "cart_session", "is_session": True, "is_first_party": True, "duration_days": 0},
        {"name": "consent_state", "is_session": False, "is_first_party": True, "duration_days": 180},
        {"name": "load_balancer", "is_session": True, "is_first_party": True, "duration_days": 0},
        {"name": "_ga", "is_session": False, "is_first_party": True, "duration_days": 730},
        {"name": "_gid", "is_session": False, "is_first_party": True, "duration_days": 1},
        {"name": "_fbp", "is_session": False, "is_first_party": True, "duration_days": 90},
        {"name": "_gcl_au", "is_session": False, "is_first_party": True, "duration_days": 90},
        {"name": "locale", "is_session": False, "is_first_party": True, "duration_days": 365},
        {"name": "currency", "is_session": False, "is_first_party": True, "duration_days": 365},
        {"name": "recently_viewed", "is_session": False, "is_first_party": True, "duration_days": 30},
        {"name": "unknown_cookie_xyz", "is_session": False, "is_first_party": True, "duration_days": 90},
    ]

    results = classify_cookie_inventory(cookies)

    output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "reports")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "essential_cookie_classification.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("=== Essential Cookie Classification ===")
    print(f"Total cookies: {results['total_cookies']}")
    print(f"Exempt (strictly necessary): {results['summary']['exempt']}")
    print(f"Consent required: {results['summary']['consent_required']}")
    print(f"Unknown (needs manual review): {results['summary']['unknown']}")
    print(f"Warnings: {results['summary']['warnings']}")

    print("\nExempt cookies:")
    for c in results["exempt_cookies"]:
        print(f"  {c['cookie_name']} — Category {c['category']}: {c['reason']}")

    print(f"\nReport saved to {output_path}")


if __name__ == "__main__":
    main()
