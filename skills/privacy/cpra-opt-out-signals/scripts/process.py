#!/usr/bin/env python3
"""
CPRA Opt-Out Preference Signal Manager

Manages Global Privacy Control (GPC) signal detection, automated
honoring, cross-device consistency, and compliance auditing for
CPRA Section 1798.135.
"""

import argparse
import json
import hashlib
from datetime import datetime, timedelta
from typing import Optional


GPC_SIGNAL_SOURCES = {
    "http_header": {
        "header": "Sec-GPC",
        "value": "1",
        "detection_point": "Server-side (middleware/reverse proxy)",
    },
    "javascript_api": {
        "api": "navigator.globalPrivacyControl",
        "value": True,
        "detection_point": "Client-side (before third-party script loading)",
    },
}

SUPPORTED_BROWSERS = {
    "firefox": {"gpc_support": "built-in", "since_version": "120"},
    "brave": {"gpc_support": "built-in", "since_version": "1.0"},
    "duckduckgo": {"gpc_support": "built-in", "since_version": "all"},
    "chrome": {"gpc_support": "extension", "extension": "Privacy Badger, OptMeowt"},
    "edge": {"gpc_support": "extension", "extension": "Privacy Badger"},
    "safari": {"gpc_support": "extension", "extension": "DuckDuckGo Privacy Essentials"},
}

AUTOMATED_ACTIONS = [
    {
        "action": "suppress_tracking_scripts",
        "description": "Block loading of third-party advertising and tracking scripts",
        "systems": ["Google Ads tag", "Meta Pixel", "LinkedIn Insight Tag"],
    },
    {
        "action": "block_advertising_cookies",
        "description": "Prevent setting or reading advertising and cross-site tracking cookies",
        "systems": ["_fbp", "_gcl_au", "IDE", "fr"],
    },
    {
        "action": "exclude_from_sharing",
        "description": "Remove from data-sharing feeds with advertising partners",
        "systems": ["Customer match uploads", "Lookalike audiences", "Data broker feeds"],
    },
    {
        "action": "update_cmp",
        "description": "Set consent management platform sale/sharing status to opted-out",
        "systems": ["OneTrust", "Cookiebot", "Custom CMP"],
    },
]


def process_gpc_signal(
    timestamp: str,
    signal_source: str,
    consumer_authenticated: bool,
    consumer_id: Optional[str] = None,
    device_hash: Optional[str] = None,
    existing_business_setting: Optional[str] = None,
) -> dict:
    """
    Process a detected GPC signal and determine the appropriate actions.

    Args:
        timestamp: Detection timestamp (ISO format).
        signal_source: 'http_header' or 'javascript_api'.
        consumer_authenticated: Whether the consumer is logged in.
        consumer_id: Authenticated consumer ID (if known).
        device_hash: Hashed device/browser identifier.
        existing_business_setting: Consumer's explicit business setting ('opt_in', 'opt_out', or None).
    """
    detection = {
        "timestamp": timestamp,
        "signal_source": signal_source,
        "signal_details": GPC_SIGNAL_SOURCES.get(signal_source, {}),
        "consumer_authenticated": consumer_authenticated,
        "consumer_id": consumer_id,
        "device_hash": device_hash,
    }

    # Determine scope
    if consumer_authenticated and consumer_id:
        scope = "account_level"
        scope_description = "Opt-out applied to consumer account across all devices"
    elif device_hash:
        scope = "device_level"
        scope_description = "Opt-out applied to this browser/device only"
    else:
        scope = "session_level"
        scope_description = "Opt-out applied to this browsing session"

    # Conflict detection
    conflict = False
    conflict_resolution = None
    if existing_business_setting == "opt_in":
        conflict = True
        conflict_resolution = {
            "conflict_type": "GPC opt-out vs. explicit business opt-in",
            "resolution": "GPC signal takes precedence per 11 CCR Section 7025(d)",
            "action": "Apply opt-out. Optionally notify consumer of conflict.",
            "consumer_can_override": True,
            "override_method": "Explicit re-confirmation through business privacy settings",
        }

    result = {
        "detection": detection,
        "scope": {
            "level": scope,
            "description": scope_description,
        },
        "conflict": {
            "detected": conflict,
            "resolution": conflict_resolution,
        },
        "actions_executed": AUTOMATED_ACTIONS,
        "compliance_log": {
            "signal_honored": True,
            "legal_basis": "CPRA Section 1798.135(b)(1)",
            "regulation": "11 CCR Section 7025",
            "timestamp": timestamp,
            "scope": scope,
        },
    }

    return result


def generate_compliance_report(
    period_start: str,
    period_end: str,
    total_signals_detected: int,
    signals_honored: int,
    conflicts_detected: int,
    conflicts_consumer_overrode: int,
    authenticated_signals: int,
    anonymous_signals: int,
) -> dict:
    """Generate a GPC compliance audit report."""
    honor_rate = (signals_honored / total_signals_detected * 100) if total_signals_detected > 0 else 0

    report = {
        "report_type": "CPRA Opt-Out Preference Signal Compliance Report",
        "period": {
            "start": period_start,
            "end": period_end,
        },
        "generated_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "metrics": {
            "total_gpc_signals_detected": total_signals_detected,
            "signals_honored": signals_honored,
            "honor_rate": f"{honor_rate:.1f}%",
            "conflicts_detected": conflicts_detected,
            "conflicts_consumer_overrode": conflicts_consumer_overrode,
            "authenticated_signals": authenticated_signals,
            "anonymous_signals": anonymous_signals,
        },
        "compliance_status": "COMPLIANT" if honor_rate >= 99.9 else "REVIEW_REQUIRED",
        "supported_browsers": SUPPORTED_BROWSERS,
        "detection_mechanisms": list(GPC_SIGNAL_SOURCES.keys()),
        "automated_actions": [a["action"] for a in AUTOMATED_ACTIONS],
    }

    if honor_rate < 99.9:
        unprocessed = total_signals_detected - signals_honored
        report["remediation_required"] = {
            "signals_not_honored": unprocessed,
            "action": "Investigate why signals were not honored and implement fixes",
            "deadline": (datetime.utcnow() + timedelta(days=14)).strftime("%Y-%m-%d"),
        }

    return report


def main():
    parser = argparse.ArgumentParser(
        description="CPRA opt-out preference signal (GPC) management"
    )
    subparsers = parser.add_subparsers(dest="command")

    detect_p = subparsers.add_parser("detect", help="Process a detected GPC signal")
    detect_p.add_argument("--source", required=True, choices=list(GPC_SIGNAL_SOURCES.keys()))
    detect_p.add_argument("--authenticated", action="store_true")
    detect_p.add_argument("--consumer-id", default=None)
    detect_p.add_argument("--device-hash", default=None)
    detect_p.add_argument("--existing-setting", choices=["opt_in", "opt_out"], default=None)

    report_p = subparsers.add_parser("report", help="Generate compliance report")
    report_p.add_argument("--start", required=True, help="Period start (YYYY-MM-DD)")
    report_p.add_argument("--end", required=True, help="Period end (YYYY-MM-DD)")
    report_p.add_argument("--total-signals", type=int, required=True)
    report_p.add_argument("--honored", type=int, required=True)
    report_p.add_argument("--conflicts", type=int, default=0)
    report_p.add_argument("--overrides", type=int, default=0)
    report_p.add_argument("--authenticated", type=int, default=0)
    report_p.add_argument("--anonymous", type=int, default=0)

    args = parser.parse_args()

    if args.command == "detect":
        result = process_gpc_signal(
            timestamp=datetime.utcnow().isoformat() + "Z",
            signal_source=args.source,
            consumer_authenticated=args.authenticated,
            consumer_id=args.consumer_id,
            device_hash=args.device_hash,
            existing_business_setting=args.existing_setting,
        )
    elif args.command == "report":
        result = generate_compliance_report(
            period_start=args.start,
            period_end=args.end,
            total_signals_detected=args.total_signals,
            signals_honored=args.honored,
            conflicts_detected=args.conflicts,
            conflicts_consumer_overrode=args.overrides,
            authenticated_signals=args.authenticated,
            anonymous_signals=args.anonymous,
        )
    else:
        parser.print_help()
        return

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
