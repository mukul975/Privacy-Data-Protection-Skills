"""
Server-Side Tracking Consent Router

Processes incoming tracking events and routes them to appropriate
destinations based on user consent state. Implements IP anonymization
and data minimization before forwarding.

Requirements:
    pip install flask requests
"""

import hashlib
import json
import os
import re
from datetime import datetime, timezone
from typing import Optional
from ipaddress import ip_address, IPv4Address, IPv6Address

try:
    from flask import Flask, request, jsonify
    import requests as http_requests
except ImportError:
    print("Required packages not installed. Run: pip install flask requests")
    raise

app = Flask(__name__)

# Configuration
GA4_MEASUREMENT_ID = os.environ.get("GA4_MEASUREMENT_ID", "G-PINNACLE123")
GA4_API_SECRET = os.environ.get("GA4_API_SECRET", "")
META_PIXEL_ID = os.environ.get("META_PIXEL_ID", "")
META_ACCESS_TOKEN = os.environ.get("META_ACCESS_TOKEN", "")

# Consent parameter mapping
CONSENT_DESTINATIONS = {
    "ga4": {
        "required_consent": ["analytics_storage"],
        "endpoint": f"https://www.google-analytics.com/mp/collect?measurement_id={GA4_MEASUREMENT_ID}&api_secret={GA4_API_SECRET}",
    },
    "google_ads": {
        "required_consent": ["ad_storage", "ad_user_data"],
        "endpoint": "https://www.googleadservices.com/pagead/conversion/",
    },
    "meta_capi": {
        "required_consent": ["ad_storage", "ad_user_data"],
        "endpoint": f"https://graph.facebook.com/v18.0/{META_PIXEL_ID}/events",
    },
}


def anonymize_ip(ip_str: str, level: str = "standard") -> Optional[str]:
    """
    Anonymize an IP address.

    Levels:
        - standard: Zero last octet (IPv4) or last 80 bits (IPv6)
        - full: Return None (remove IP entirely)
        - geo_only: Resolve to country, return None
    """
    if level == "full":
        return None

    try:
        addr = ip_address(ip_str)
        if isinstance(addr, IPv4Address):
            # Zero the last octet: 203.0.113.42 -> 203.0.113.0
            parts = ip_str.split(".")
            parts[3] = "0"
            return ".".join(parts)
        elif isinstance(addr, IPv6Address):
            # Zero the last 80 bits
            full = addr.exploded
            parts = full.split(":")
            # Keep first 3 groups (48 bits), zero the rest
            for i in range(3, 8):
                parts[i] = "0000"
            return ":".join(parts)
    except ValueError:
        return None

    return None


def hash_pii(value: str) -> str:
    """SHA-256 hash for PII (email, phone) before sending to ad platforms."""
    normalized = value.strip().lower()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def minimize_user_agent(ua: str) -> str:
    """Reduce user agent to essential components only."""
    # Extract browser and OS from full UA string
    browser_match = re.search(r"(Chrome|Firefox|Safari|Edge)/[\d.]+", ua)
    os_match = re.search(r"\((Windows|Macintosh|Linux|iPhone|Android)[^)]*\)", ua)

    browser = browser_match.group(0) if browser_match else "Unknown"
    os_info = os_match.group(1) if os_match else "Unknown"

    return f"{os_info}; {browser}"


def minimize_url(url: str) -> str:
    """Strip query parameters from URL, keep path only."""
    from urllib.parse import urlparse
    parsed = urlparse(url)
    return parsed.path


def check_consent(event_consent: dict, required: list[str]) -> bool:
    """Check if all required consent parameters are granted."""
    for param in required:
        if event_consent.get(param) != "granted":
            return False
    return True


def forward_to_ga4(event: dict, client_id: str, anonymized_ip: Optional[str]):
    """Forward event to GA4 Measurement Protocol."""
    if not GA4_API_SECRET:
        return {"status": "skipped", "reason": "GA4 API secret not configured"}

    payload = {
        "client_id": client_id,
        "events": [
            {
                "name": event.get("event_name", "page_view"),
                "params": {
                    k: v
                    for k, v in event.get("event_params", {}).items()
                    if k not in ("email", "phone", "ip_address")
                },
            }
        ],
    }

    # Add minimized page location
    if "page_location" in event.get("event_params", {}):
        payload["events"][0]["params"]["page_location"] = minimize_url(
            event["event_params"]["page_location"]
        )

    try:
        response = http_requests.post(
            CONSENT_DESTINATIONS["ga4"]["endpoint"],
            json=payload,
            timeout=5,
        )
        return {"status": "sent", "response_code": response.status_code}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def forward_to_meta_capi(event: dict, anonymized_ip: Optional[str]):
    """Forward event to Meta Conversions API."""
    if not META_ACCESS_TOKEN:
        return {"status": "skipped", "reason": "Meta access token not configured"}

    # Build Meta event data
    meta_event = {
        "event_name": event.get("event_name", "PageView"),
        "event_time": int(datetime.now(timezone.utc).timestamp()),
        "action_source": "website",
        "event_source_url": minimize_url(
            event.get("event_params", {}).get("page_location", "")
        ),
        "user_data": {},
    }

    # Add hashed email if present and consent granted
    email = event.get("event_params", {}).get("email")
    if email:
        meta_event["user_data"]["em"] = [hash_pii(email)]

    # IP is NOT forwarded to Meta (privacy policy)
    # User agent is minimized
    ua = event.get("user_agent", "")
    if ua:
        meta_event["user_data"]["client_user_agent"] = minimize_user_agent(ua)

    # Event ID for deduplication
    event_id = event.get("event_id")
    if event_id:
        meta_event["event_id"] = event_id

    payload = {
        "data": [meta_event],
        "access_token": META_ACCESS_TOKEN,
    }

    try:
        response = http_requests.post(
            CONSENT_DESTINATIONS["meta_capi"]["endpoint"],
            json=payload,
            timeout=5,
        )
        return {"status": "sent", "response_code": response.status_code}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# Aggregate counters (in production, use a proper database)
aggregate_counters = {}


def increment_aggregate_counter(event_name: str):
    """Increment aggregate event counter (no PII stored)."""
    date_key = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    key = f"{date_key}:{event_name}"
    aggregate_counters[key] = aggregate_counters.get(key, 0) + 1


@app.route("/collect", methods=["POST"])
def collect_event():
    """Main event collection endpoint."""
    try:
        event = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not event:
        return jsonify({"error": "Empty payload"}), 400

    # Extract consent state
    consent_state = event.get("consent_state", {})
    client_id = event.get("client_id", "anonymous")
    source_ip = request.remote_addr

    # Always increment aggregate counter (no consent needed)
    event_name = event.get("event_name", "unknown")
    increment_aggregate_counter(event_name)

    results = {}

    # Anonymize IP
    anonymized_ip = anonymize_ip(source_ip, level="standard")

    # Route to GA4 if analytics consent granted
    if check_consent(consent_state, CONSENT_DESTINATIONS["ga4"]["required_consent"]):
        results["ga4"] = forward_to_ga4(event, client_id, anonymized_ip)
    else:
        results["ga4"] = {"status": "blocked", "reason": "analytics_storage denied"}

    # Route to Meta CAPI if advertising consent granted
    if check_consent(consent_state, CONSENT_DESTINATIONS["meta_capi"]["required_consent"]):
        results["meta_capi"] = forward_to_meta_capi(event, None)  # No IP for Meta
    else:
        results["meta_capi"] = {"status": "blocked", "reason": "ad_storage or ad_user_data denied"}

    return jsonify({
        "status": "processed",
        "event_name": event_name,
        "routing_results": results,
        "ip_anonymized": anonymized_ip is not None,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()})


@app.route("/stats", methods=["GET"])
def get_stats():
    """Return aggregate counters (no PII)."""
    return jsonify({"counters": aggregate_counters})


def main():
    """Run the server-side tracking consent router."""
    port = int(os.environ.get("PORT", 8080))
    print(f"Starting server-side tracking consent router on port {port}")
    print(f"GA4 Measurement ID: {GA4_MEASUREMENT_ID}")
    print(f"Meta Pixel ID: {'configured' if META_PIXEL_ID else 'not configured'}")
    app.run(host="0.0.0.0", port=port, debug=False)


if __name__ == "__main__":
    main()
