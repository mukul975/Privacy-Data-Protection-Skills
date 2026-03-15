"""
Google Consent Mode v2 Configuration Generator

Generates consent mode configuration snippets for different CMP platforms
and jurisdictions.

Requirements:
    No external dependencies (uses standard library only)
"""

import json
import os
from datetime import datetime, timezone

# EEA country codes (27 EU + 3 EEA)
EEA_COUNTRIES = [
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR",
    "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL",
    "PL", "PT", "RO", "SK", "SI", "ES", "SE", "IS", "LI", "NO",
]

# US states with privacy laws requiring consent/opt-out
US_PRIVACY_STATES = {
    "US-CA": {"law": "CCPA/CPRA", "model": "opt-out", "gpc_required": True},
    "US-CO": {"law": "CPA", "model": "opt-out", "gpc_required": True},
    "US-CT": {"law": "CTDPA", "model": "opt-out", "gpc_required": True},
    "US-VA": {"law": "VCDPA", "model": "opt-out", "gpc_required": False},
    "US-MT": {"law": "MCDPA", "model": "opt-out", "gpc_required": True},
    "US-TX": {"law": "TDPSA", "model": "opt-out", "gpc_required": True},
    "US-OR": {"law": "OCPA", "model": "opt-out", "gpc_required": True},
}

# Consent parameter definitions
CONSENT_PARAMETERS = {
    "ad_storage": {
        "description": "Controls advertising cookies (e.g., _gcl_*, IDE)",
        "default_eea": "denied",
        "default_us": "granted",
        "default_other": "granted",
    },
    "ad_user_data": {
        "description": "Controls sending user data to Google for advertising",
        "default_eea": "denied",
        "default_us": "granted",
        "default_other": "granted",
    },
    "ad_personalization": {
        "description": "Controls ad personalization and remarketing",
        "default_eea": "denied",
        "default_us": "granted",
        "default_other": "granted",
    },
    "analytics_storage": {
        "description": "Controls analytics cookies (e.g., _ga, _gid)",
        "default_eea": "denied",
        "default_us": "granted",
        "default_other": "granted",
    },
    "functionality_storage": {
        "description": "Controls functionality cookies (e.g., language)",
        "default_eea": "granted",
        "default_us": "granted",
        "default_other": "granted",
    },
    "personalization_storage": {
        "description": "Controls personalization cookies",
        "default_eea": "denied",
        "default_us": "granted",
        "default_other": "granted",
    },
    "security_storage": {
        "description": "Controls security cookies (e.g., authentication)",
        "default_eea": "granted",
        "default_us": "granted",
        "default_other": "granted",
    },
}


def generate_gtag_config(
    ga4_measurement_id: str,
    google_ads_id: str = "",
    strict_mode: bool = True,
) -> str:
    """Generate gtag.js consent mode configuration."""
    config = f"""<!-- Google Consent Mode v2 Configuration for Pinnacle E-Commerce Ltd -->
<!-- Generated: {datetime.now(timezone.utc).isoformat()} -->

<script>
// Initialize dataLayer
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}

// === CONSENT DEFAULTS (must load BEFORE Google tag) ===

// EEA: Strict opt-in (all non-essential denied)
gtag('consent', 'default', {{
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied',
  'functionality_storage': 'granted',
  'personalization_storage': 'denied',
  'security_storage': 'granted',
  'wait_for_update': 500,
  'region': {json.dumps(EEA_COUNTRIES)}
}});

// UK: Same as EEA (PECR requires opt-in)
gtag('consent', 'default', {{
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied',
  'functionality_storage': 'granted',
  'personalization_storage': 'denied',
  'security_storage': 'granted',
  'wait_for_update': 500,
  'region': ['GB']
}});

// US: Opt-out model (granted by default, user can opt out)
gtag('consent', 'default', {{
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted',
  'analytics_storage': 'granted',
  'functionality_storage': 'granted',
  'personalization_storage': 'granted',
  'security_storage': 'granted',
  'region': ['US']
}});

// Rest of world: Granted by default (adjust per local law)
gtag('consent', 'default', {{
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted',
  'analytics_storage': 'granted',
  'functionality_storage': 'granted',
  'personalization_storage': 'granted',
  'security_storage': 'granted'
}});

// Enable URL passthrough for cookieless conversion measurement
gtag('set', 'url_passthrough', true);

// Redact ad click identifiers when ad_storage is denied
gtag('set', 'ads_data_redaction', true);
</script>

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={ga4_measurement_id}"></script>
<script>
gtag('js', new Date());
gtag('config', '{ga4_measurement_id}');
"""
    if google_ads_id:
        config += f"gtag('config', '{google_ads_id}');\n"

    config += """</script>

<!-- Consent Update Function (called by CMP on user interaction) -->
<script>
function updateGoogleConsent(consentChoices) {
  /**
   * consentChoices object:
   *   analytics: boolean
   *   advertising: boolean
   *   personalization: boolean
   *   functionality: boolean
   */
  gtag('consent', 'update', {
    'ad_storage': consentChoices.advertising ? 'granted' : 'denied',
    'ad_user_data': consentChoices.advertising ? 'granted' : 'denied',
    'ad_personalization': consentChoices.personalization ? 'granted' : 'denied',
    'analytics_storage': consentChoices.analytics ? 'granted' : 'denied',
    'functionality_storage': consentChoices.functionality ? 'granted' : 'denied',
    'personalization_storage': consentChoices.personalization ? 'granted' : 'denied'
  });
}

// Handle GPC signal for US users
if (navigator.globalPrivacyControl === true) {
  gtag('consent', 'update', {
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied'
  });
}
</script>"""

    return config


def generate_gtm_datalayer_config() -> str:
    """Generate GTM dataLayer consent configuration."""
    return """<!-- GTM Consent Mode v2 — dataLayer Configuration -->
<script>
window.dataLayer = window.dataLayer || [];

// Push consent defaults to dataLayer BEFORE GTM loads
window.dataLayer.push({
  'event': 'consent_default',
  'consent': {
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'analytics_storage': 'denied',
    'functionality_storage': 'granted',
    'personalization_storage': 'denied',
    'security_storage': 'granted',
    'wait_for_update': 500
  }
});

// Function for CMP to call on consent update
function pushConsentUpdate(consentState) {
  window.dataLayer.push({
    'event': 'consent_update',
    'consent': {
      'ad_storage': consentState.advertising ? 'granted' : 'denied',
      'ad_user_data': consentState.advertising ? 'granted' : 'denied',
      'ad_personalization': consentState.personalization ? 'granted' : 'denied',
      'analytics_storage': consentState.analytics ? 'granted' : 'denied',
      'functionality_storage': consentState.functionality ? 'granted' : 'denied',
      'personalization_storage': consentState.personalization ? 'granted' : 'denied'
    }
  });
}
</script>
"""


def generate_consent_parameter_docs() -> str:
    """Generate documentation for consent parameters."""
    docs = "# Consent Mode v2 Parameter Reference\n\n"
    docs += "| Parameter | Description | EEA Default | US Default |\n"
    docs += "|-----------|-------------|-------------|------------|\n"

    for param, info in CONSENT_PARAMETERS.items():
        docs += f"| `{param}` | {info['description']} | {info['default_eea']} | {info['default_us']} |\n"

    return docs


def main():
    """Generate Consent Mode v2 configurations for Pinnacle E-Commerce Ltd."""
    output_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
    os.makedirs(output_dir, exist_ok=True)

    # Generate gtag.js configuration
    gtag_config = generate_gtag_config(
        ga4_measurement_id="G-PINNACLE123",
        google_ads_id="AW-PINNACLE456",
    )
    with open(os.path.join(output_dir, "consent_mode_gtag.html"), "w") as f:
        f.write(gtag_config)

    # Generate GTM dataLayer configuration
    gtm_config = generate_gtm_datalayer_config()
    with open(os.path.join(output_dir, "consent_mode_gtm.html"), "w") as f:
        f.write(gtm_config)

    # Generate parameter documentation
    param_docs = generate_consent_parameter_docs()
    with open(os.path.join(output_dir, "consent_parameters.md"), "w") as f:
        f.write(param_docs)

    print("=== Google Consent Mode v2 Configuration Generated ===")
    print(f"Output directory: {output_dir}")
    print("Files generated:")
    print("  - consent_mode_gtag.html (gtag.js implementation)")
    print("  - consent_mode_gtm.html (GTM dataLayer implementation)")
    print("  - consent_parameters.md (parameter reference)")
    print(f"\nEEA countries configured: {len(EEA_COUNTRIES)}")
    print(f"US privacy states tracked: {len(US_PRIVACY_STATES)}")


if __name__ == "__main__":
    main()
