"""
GPC (Global Privacy Control) Integration Module

Detects GPC signals and applies appropriate opt-out behavior based on
user jurisdiction. Integrates with consent management platforms.

Requirements:
    pip install flask requests
"""

import json
import os
from datetime import datetime, timezone
from typing import Optional

try:
    from flask import Flask, request, jsonify, make_response
except ImportError:
    print("Required packages not installed. Run: pip install flask")
    raise

app = Flask(__name__)

# US states where GPC is legally binding
GPC_MANDATORY_STATES = {
    "CA": {"law": "CCPA/CPRA", "effective": "2023-01-01", "scope": "sale, sharing"},
    "CO": {"law": "CPA", "effective": "2024-07-01", "scope": "targeted advertising, sale"},
    "CT": {"law": "CTDPA", "effective": "2023-07-01", "scope": "targeted advertising, sale, profiling"},
    "MT": {"law": "MCDPA", "effective": "2024-10-01", "scope": "targeted advertising, sale"},
    "TX": {"law": "TDPSA", "effective": "2024-07-01", "scope": "targeted advertising, sale"},
    "OR": {"law": "OCPA", "effective": "2024-07-01", "scope": "targeted advertising, sale"},
    "DE": {"law": "DPDPA", "effective": "2025-01-01", "scope": "targeted advertising, sale"},
    "NH": {"law": "NHPA", "effective": "2025-01-01", "scope": "targeted advertising, sale"},
    "NJ": {"law": "NJDPA", "effective": "2025-01-15", "scope": "targeted advertising, sale"},
}

# GPC opt-out log (in production, use a proper database)
gpc_opt_out_log: list[dict] = []


def detect_gpc(request_obj) -> bool:
    """Detect GPC signal from HTTP headers."""
    gpc_header = request_obj.headers.get("Sec-GPC", "")
    return gpc_header == "1"


def get_user_state(ip_address: str) -> Optional[str]:
    """
    Resolve IP address to US state.
    In production, use MaxMind GeoIP2 or similar service.
    """
    # Uses TEST_USER_STATE env var for testing; in production, integrate
    # MaxMind GeoIP2 database for IP-to-state resolution.
    # Install: pip install geoip2
    # Usage: reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    #        response = reader.city(ip_address)
    #        return response.subdivisions.most_specific.iso_code
    test_state = os.environ.get("TEST_USER_STATE")
    if test_state:
        return test_state

    try:
        import geoip2.database
        db_path = os.environ.get("GEOIP_DB_PATH", "/usr/share/GeoIP/GeoLite2-City.mmdb")
        if os.path.exists(db_path):
            reader = geoip2.database.Reader(db_path)
            response = reader.city(ip_address)
            state_code = response.subdivisions.most_specific.iso_code
            reader.close()
            return state_code
    except (ImportError, Exception):
        pass

    # Default to California (most restrictive US state) when geolocation unavailable
    return "CA"


def process_gpc_signal(ip_address: str, user_agent: str) -> dict:
    """Process GPC signal and determine required actions."""
    user_state = get_user_state(ip_address)

    is_mandatory = user_state in GPC_MANDATORY_STATES
    state_info = GPC_MANDATORY_STATES.get(user_state, {})

    # Determine what to opt out
    opt_out_actions = {
        "sale_of_personal_information": is_mandatory,
        "sharing_for_behavioral_advertising": is_mandatory,
        "targeted_advertising": is_mandatory,
        "profiling": user_state in ["CT"],  # CT specifically includes profiling
    }

    # Consent mode updates
    consent_updates = {
        "ad_storage": "denied" if is_mandatory else "granted",
        "ad_user_data": "denied" if is_mandatory else "granted",
        "ad_personalization": "denied" if is_mandatory else "granted",
        "analytics_storage": "granted",  # GPC does not affect analytics
    }

    # Cookies to remove
    cookies_to_remove = []
    if is_mandatory:
        cookies_to_remove = ["_fbp", "_fbc", "_gcl_au", "_gcl_aw", "IDE", "fr", "NID"]

    result = {
        "gpc_detected": True,
        "user_state": user_state,
        "gpc_legally_binding": is_mandatory,
        "applicable_law": state_info.get("law", "None"),
        "opt_out_scope": state_info.get("scope", "N/A"),
        "opt_out_actions": opt_out_actions,
        "consent_mode_updates": consent_updates,
        "cookies_to_remove": cookies_to_remove,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    # Log the GPC opt-out
    if is_mandatory:
        log_entry = {
            "type": "gpc_auto_optout",
            "state": user_state,
            "law": state_info.get("law"),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "ip_hash": hash(ip_address) % 10**8,  # Pseudonymized
        }
        gpc_opt_out_log.append(log_entry)

    return result


@app.route("/api/gpc/check", methods=["GET"])
def check_gpc():
    """Check if GPC is detected and return required actions."""
    gpc_detected = detect_gpc(request)

    if not gpc_detected:
        return jsonify({
            "gpc_detected": False,
            "message": "No GPC signal detected",
        })

    result = process_gpc_signal(
        ip_address=request.remote_addr,
        user_agent=request.headers.get("User-Agent", ""),
    )

    return jsonify(result)


@app.route("/api/gpc/client-script", methods=["GET"])
def get_client_script():
    """Return JavaScript for client-side GPC detection and CMP integration."""
    script = """
(function() {
  'use strict';

  var GPC_MANDATORY_STATES = ['CA', 'CO', 'CT', 'MT', 'TX', 'OR', 'DE', 'NH', 'NJ'];

  function handleGPC() {
    if (navigator.globalPrivacyControl !== true) return;

    // Fetch user jurisdiction from server
    fetch('/api/gpc/check', {
      headers: { 'Sec-GPC': '1' }
    })
    .then(function(response) { return response.json(); })
    .then(function(data) {
      if (!data.gpc_legally_binding) return;

      // Update Google Consent Mode
      if (typeof gtag === 'function') {
        gtag('consent', 'update', data.consent_mode_updates);
      }

      // Remove advertising cookies
      data.cookies_to_remove.forEach(function(name) {
        document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; domain=.' + location.hostname;
      });

      // Dispatch event for CMP integration
      window.dispatchEvent(new CustomEvent('gpc_optout', { detail: data }));
    })
    .catch(function(err) {
      console.warn('GPC check failed:', err);
    });
  }

  // Run on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', handleGPC);
  } else {
    handleGPC();
  }
})();
"""
    response = make_response(script)
    response.headers["Content-Type"] = "application/javascript"
    response.headers["Cache-Control"] = "public, max-age=3600"
    return response


@app.route("/api/gpc/log", methods=["GET"])
def get_gpc_log():
    """Return GPC opt-out log (for compliance audit)."""
    return jsonify({
        "total_gpc_optouts": len(gpc_opt_out_log),
        "log": gpc_opt_out_log[-100:],  # Last 100 entries
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


def main():
    """Run GPC integration server."""
    port = int(os.environ.get("PORT", 8081))
    print(f"Starting GPC integration server on port {port}")
    print(f"GPC mandatory states: {', '.join(GPC_MANDATORY_STATES.keys())}")
    app.run(host="0.0.0.0", port=port, debug=False)


if __name__ == "__main__":
    main()
