"""
Cookie-less Alternatives Comparison Tool

Evaluates and compares cookie-less tracking alternatives based on
privacy properties, browser support, data quality, and consent requirements.

Requirements:
    No external dependencies (uses standard library only)
"""

import json
import os
from datetime import datetime, timezone


ALTERNATIVES = {
    "topics_api": {
        "name": "Topics API",
        "category": "interest_targeting",
        "provider": "Google (Chrome Privacy Sandbox)",
        "browser_support": {"chrome": True, "firefox": False, "safari": False, "edge": True},
        "uses_cookies": False,
        "uses_device_storage": True,
        "cross_site_tracking": False,
        "data_granularity": "~470 topic categories",
        "noise_level": "5% random topic substitution",
        "latency": "Real-time",
        "consent_required": "Likely (stores data on device; jurisdiction-dependent)",
        "production_ready": True,
        "privacy_score": 8,
        "data_quality_score": 5,
    },
    "attribution_reporting": {
        "name": "Attribution Reporting API",
        "category": "conversion_measurement",
        "provider": "Google (Chrome Privacy Sandbox)",
        "browser_support": {"chrome": True, "firefox": False, "safari": False, "edge": True},
        "uses_cookies": False,
        "uses_device_storage": True,
        "cross_site_tracking": False,
        "data_granularity": "Event-level: 3 bits; Aggregate: histograms with noise",
        "noise_level": "Randomized trigger rate + Laplace noise",
        "latency": "2 days (clicks), 1 day (views)",
        "consent_required": "Likely (stores data on device; jurisdiction-dependent)",
        "production_ready": True,
        "privacy_score": 9,
        "data_quality_score": 6,
    },
    "protected_audiences": {
        "name": "Protected Audiences API (FLEDGE)",
        "category": "remarketing",
        "provider": "Google (Chrome Privacy Sandbox)",
        "browser_support": {"chrome": True, "firefox": False, "safari": False, "edge": True},
        "uses_cookies": False,
        "uses_device_storage": True,
        "cross_site_tracking": False,
        "data_granularity": "Interest group-level targeting",
        "noise_level": "K-anonymity on creatives",
        "latency": "Real-time (on-device auction)",
        "consent_required": "Likely (stores interest groups on device)",
        "production_ready": True,
        "privacy_score": 9,
        "data_quality_score": 6,
    },
    "plausible_analytics": {
        "name": "Plausible Analytics",
        "category": "web_analytics",
        "provider": "Plausible Insights OÜ (Estonia)",
        "browser_support": {"chrome": True, "firefox": True, "safari": True, "edge": True},
        "uses_cookies": False,
        "uses_device_storage": False,
        "cross_site_tracking": False,
        "data_granularity": "Aggregate (daily unique via rotated hash)",
        "noise_level": "None (aggregate by design)",
        "latency": "Real-time",
        "consent_required": "Varies by jurisdiction (no cookies, no PII)",
        "production_ready": True,
        "privacy_score": 10,
        "data_quality_score": 6,
    },
    "fathom_analytics": {
        "name": "Fathom Analytics",
        "category": "web_analytics",
        "provider": "Conva Ventures Inc. (Canada)",
        "browser_support": {"chrome": True, "firefox": True, "safari": True, "edge": True},
        "uses_cookies": False,
        "uses_device_storage": False,
        "cross_site_tracking": False,
        "data_granularity": "Aggregate",
        "noise_level": "None (aggregate by design)",
        "latency": "Real-time",
        "consent_required": "Varies by jurisdiction (no cookies, no PII)",
        "production_ready": True,
        "privacy_score": 10,
        "data_quality_score": 6,
    },
    "matomo_cookieless": {
        "name": "Matomo (cookieless mode)",
        "category": "web_analytics",
        "provider": "InnoCraft Ltd (self-hosted)",
        "browser_support": {"chrome": True, "firefox": True, "safari": True, "edge": True},
        "uses_cookies": False,
        "uses_device_storage": False,
        "cross_site_tracking": False,
        "data_granularity": "Per-visit (fingerprint hash, rotated daily)",
        "noise_level": "None",
        "latency": "Real-time",
        "consent_required": "Check with local DPA (fingerprinting concerns)",
        "production_ready": True,
        "privacy_score": 8,
        "data_quality_score": 7,
    },
    "server_log_analysis": {
        "name": "Server-side log analysis",
        "category": "web_analytics",
        "provider": "Self-hosted",
        "browser_support": {"chrome": True, "firefox": True, "safari": True, "edge": True},
        "uses_cookies": False,
        "uses_device_storage": False,
        "cross_site_tracking": False,
        "data_granularity": "Per-request (IP anonymized)",
        "noise_level": "Bot traffic (~30-50%)",
        "latency": "Batch processing",
        "consent_required": "No (operational necessity for server infrastructure)",
        "production_ready": True,
        "privacy_score": 10,
        "data_quality_score": 4,
    },
}


def generate_comparison_report(org_name: str, use_cases: list[str]) -> dict:
    """Generate comparison report for specified use cases."""
    relevant_alternatives = {}
    for alt_id, alt in ALTERNATIVES.items():
        if alt["category"] in use_cases or "all" in use_cases:
            relevant_alternatives[alt_id] = alt

    # Cross-browser support analysis
    cross_browser = {
        alt_id: all(alt["browser_support"].values())
        for alt_id, alt in relevant_alternatives.items()
    }

    return {
        "metadata": {
            "organization": org_name,
            "analysis_date": datetime.now(timezone.utc).isoformat(),
            "use_cases_evaluated": use_cases,
        },
        "alternatives": relevant_alternatives,
        "cross_browser_support": cross_browser,
        "recommendations": {
            "web_analytics": {
                "primary": "plausible_analytics",
                "reason": "Cross-browser, no cookies, no PII, EU-hosted option",
                "fallback": "server_log_analysis",
            },
            "conversion_measurement": {
                "primary": "attribution_reporting",
                "reason": "Privacy-preserving conversion data with noise/delay tradeoff",
                "limitation": "Chrome-only; no Safari/Firefox support",
            },
            "remarketing": {
                "primary": "protected_audiences",
                "reason": "On-device auction prevents cross-site tracking",
                "limitation": "Chrome-only; requires advertiser JS integration",
            },
            "interest_targeting": {
                "primary": "topics_api",
                "reason": "Coarse-grained interest categories with privacy noise",
                "limitation": "Chrome-only; ~470 topics vs granular cookie audiences",
            },
        },
    }


def main():
    """Generate cookie-less alternatives comparison for Pinnacle E-Commerce Ltd."""
    report = generate_comparison_report(
        org_name="Pinnacle E-Commerce Ltd",
        use_cases=["all"],
    )

    output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "reports")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "cookieless_comparison.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("=== Cookie-less Alternatives Comparison ===")
    print(f"Organization: {report['metadata']['organization']}")
    print(f"Alternatives evaluated: {len(report['alternatives'])}")

    print("\nCross-browser support:")
    for alt_id, supported in report["cross_browser_support"].items():
        alt = report["alternatives"][alt_id]
        tag = "All browsers" if supported else "Chrome/Edge only"
        print(f"  {alt['name']}: {tag}")

    print("\nRecommendations:")
    for use_case, rec in report["recommendations"].items():
        alt = ALTERNATIVES.get(rec["primary"], {})
        print(f"  {use_case}: {alt.get('name', rec['primary'])}")
        print(f"    Reason: {rec['reason']}")

    print(f"\nReport saved to {output_path}")


if __name__ == "__main__":
    main()
