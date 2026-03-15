"""
Cross-Jurisdiction Cookie Compliance Configuration Generator

Generates consent configuration profiles for different jurisdictions
and creates a compliance requirements matrix.

Requirements:
    No external dependencies (uses standard library only)
"""

import json
import os
from datetime import datetime, timezone


JURISDICTIONS = {
    "EU": {
        "name": "European Union (ePrivacy + GDPR)",
        "consent_model": "opt-in",
        "default_cookie_state": "denied",
        "banner_type": "opt-in with equal accept/reject",
        "essential_exemption": True,
        "cookie_wall_allowed": False,
        "gpc_required": False,
        "gpc_recommended": True,
        "max_cookie_lifetime_days": 395,
        "reconsent_interval_months": 6,
        "consent_record_required": True,
        "child_age_threshold": 16,
        "countries": [
            "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR",
            "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL",
            "PL", "PT", "RO", "SK", "SI", "ES", "SE",
        ],
        "key_law": "ePrivacy Directive 2002/58/EC Art. 5(3) + GDPR",
    },
    "EEA_NON_EU": {
        "name": "EEA (non-EU)",
        "consent_model": "opt-in",
        "default_cookie_state": "denied",
        "banner_type": "opt-in with equal accept/reject",
        "essential_exemption": True,
        "cookie_wall_allowed": False,
        "gpc_required": False,
        "gpc_recommended": True,
        "max_cookie_lifetime_days": 395,
        "reconsent_interval_months": 6,
        "consent_record_required": True,
        "child_age_threshold": 16,
        "countries": ["IS", "LI", "NO"],
        "key_law": "EEA Agreement + national transposition",
    },
    "UK": {
        "name": "United Kingdom",
        "consent_model": "opt-in",
        "default_cookie_state": "denied",
        "banner_type": "opt-in with clear accept/reject",
        "essential_exemption": True,
        "cookie_wall_allowed": False,
        "gpc_required": False,
        "gpc_recommended": True,
        "max_cookie_lifetime_days": None,
        "reconsent_interval_months": 12,
        "consent_record_required": True,
        "child_age_threshold": 13,
        "countries": ["GB"],
        "key_law": "PECR (SI 2003/2426) Reg. 6 + UK GDPR",
    },
    "US_CA": {
        "name": "California, USA",
        "consent_model": "opt-out",
        "default_cookie_state": "granted",
        "banner_type": "notice with Do Not Sell/Share link",
        "essential_exemption": False,
        "cookie_wall_allowed": False,
        "gpc_required": True,
        "gpc_recommended": True,
        "max_cookie_lifetime_days": None,
        "reconsent_interval_months": 12,
        "consent_record_required": False,
        "child_age_threshold": 16,
        "countries": ["US-CA"],
        "key_law": "CCPA/CPRA (Cal. Civ. Code §1798.100 et seq.)",
    },
    "US_CO": {
        "name": "Colorado, USA",
        "consent_model": "opt-out",
        "default_cookie_state": "granted",
        "banner_type": "notice with opt-out mechanism",
        "essential_exemption": False,
        "cookie_wall_allowed": False,
        "gpc_required": True,
        "gpc_recommended": True,
        "max_cookie_lifetime_days": None,
        "reconsent_interval_months": 12,
        "consent_record_required": False,
        "child_age_threshold": 13,
        "countries": ["US-CO"],
        "key_law": "CPA (C.R.S. §6-1-1301 et seq.)",
    },
    "US_CT": {
        "name": "Connecticut, USA",
        "consent_model": "opt-out",
        "default_cookie_state": "granted",
        "banner_type": "notice with opt-out mechanism",
        "essential_exemption": False,
        "cookie_wall_allowed": False,
        "gpc_required": True,
        "gpc_recommended": True,
        "max_cookie_lifetime_days": None,
        "reconsent_interval_months": 12,
        "consent_record_required": False,
        "child_age_threshold": 13,
        "countries": ["US-CT"],
        "key_law": "CTDPA (P.A. 22-15)",
    },
    "BR": {
        "name": "Brazil",
        "consent_model": "legal_basis_required",
        "default_cookie_state": "denied",
        "banner_type": "consent banner (opt-in recommended)",
        "essential_exemption": False,
        "cookie_wall_allowed": False,
        "gpc_required": False,
        "gpc_recommended": False,
        "max_cookie_lifetime_days": None,
        "reconsent_interval_months": 12,
        "consent_record_required": True,
        "child_age_threshold": 12,
        "countries": ["BR"],
        "key_law": "LGPD (Lei 13.709/2018)",
    },
}


def generate_requirements_matrix() -> list[dict]:
    """Generate a comparison matrix of all jurisdictions."""
    matrix = []
    for jur_id, jur in JURISDICTIONS.items():
        matrix.append({
            "jurisdiction": jur["name"],
            "code": jur_id,
            "consent_model": jur["consent_model"],
            "default_state": jur["default_cookie_state"],
            "gpc_required": jur["gpc_required"],
            "max_cookie_lifetime": f"{jur['max_cookie_lifetime_days']} days" if jur["max_cookie_lifetime_days"] else "Not specified",
            "reconsent_interval": f"{jur['reconsent_interval_months']} months",
            "cookie_wall_allowed": jur["cookie_wall_allowed"],
            "consent_record_required": jur["consent_record_required"],
        })
    return matrix


def generate_consent_config(jurisdiction_id: str) -> dict:
    """Generate consent configuration for a specific jurisdiction."""
    jur = JURISDICTIONS.get(jurisdiction_id)
    if not jur:
        raise ValueError(f"Unknown jurisdiction: {jurisdiction_id}")

    config = {
        "jurisdiction": jur["name"],
        "consent_mode_defaults": {
            "ad_storage": "denied" if jur["consent_model"] == "opt-in" else "granted",
            "ad_user_data": "denied" if jur["consent_model"] == "opt-in" else "granted",
            "ad_personalization": "denied" if jur["consent_model"] == "opt-in" else "granted",
            "analytics_storage": "denied" if jur["consent_model"] == "opt-in" else "granted",
        },
        "banner_configuration": {
            "type": jur["banner_type"],
            "show_reject_button": jur["consent_model"] == "opt-in",
            "show_do_not_sell_link": jur["consent_model"] == "opt-out" and jur_id in ["US_CA"],
            "honor_gpc": jur["gpc_required"] or jur["gpc_recommended"],
        },
        "consent_storage": {
            "cookie_name": f"pinnacle_consent_{jurisdiction_id.lower()}",
            "max_age_seconds": jur["reconsent_interval_months"] * 30 * 24 * 60 * 60,
        },
    }

    return config


def main():
    """Generate cross-jurisdiction compliance configuration."""
    output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "reports")
    os.makedirs(output_dir, exist_ok=True)

    # Generate requirements matrix
    matrix = generate_requirements_matrix()

    # Generate per-jurisdiction configs
    configs = {}
    for jur_id in JURISDICTIONS:
        configs[jur_id] = generate_consent_config(jur_id)

    report = {
        "metadata": {
            "organization": "Pinnacle E-Commerce Ltd",
            "generated_date": datetime.now(timezone.utc).isoformat(),
            "jurisdictions_covered": len(JURISDICTIONS),
        },
        "requirements_matrix": matrix,
        "jurisdiction_configs": configs,
    }

    output_path = os.path.join(output_dir, "cross_jurisdiction_config.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("=== Cross-Jurisdiction Cookie Compliance Configuration ===")
    print(f"Jurisdictions configured: {len(JURISDICTIONS)}")
    for jur_id, jur in JURISDICTIONS.items():
        print(f"  {jur_id}: {jur['name']} — {jur['consent_model']} model")

    print(f"\nConfiguration saved to {output_path}")


if __name__ == "__main__":
    main()
