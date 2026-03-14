#!/usr/bin/env python3
"""
Global Privacy Control (GPC) Detection and Processing

Server-side implementation for detecting and honoring GPC signals
per CPRA Section 1798.135(e) and multi-state requirements.
"""

import json
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class GPCAction(Enum):
    OPT_OUT_APPLIED = "opt_out_applied"
    CONFLICT_RESOLVED = "conflict_resolved"
    ALREADY_OPTED_OUT = "already_opted_out"
    NO_GPC_SIGNAL = "no_gpc_signal"


# US states requiring GPC signal recognition with effective dates
GPC_STATE_REQUIREMENTS = {
    "CA": {
        "state": "California",
        "law": "California Privacy Rights Act (CPRA)",
        "statute": "Cal. Civ. Code Section 1798.135(e)",
        "effective_date": "2023-01-01",
        "scope": "sale_and_sharing",
        "notes": "AG Regulation 11 CCR 7025 provides implementation details. Sephora enforcement (Aug 2022) confirmed GPC must be honored.",
    },
    "CO": {
        "state": "Colorado",
        "law": "Colorado Privacy Act (CPA)",
        "statute": "C.R.S. Section 6-1-1306(1)(a)(IV)(A)",
        "effective_date": "2024-07-01",
        "scope": "sale_and_targeted_advertising",
        "notes": "CPA Rules 4.6 require recognition of universal opt-out mechanisms.",
    },
    "CT": {
        "state": "Connecticut",
        "law": "Connecticut Data Privacy Act (CTDPA)",
        "statute": "Public Act 22-15, Section 42-520(b)(5)",
        "effective_date": "2025-01-01",
        "scope": "sale_and_targeted_advertising",
        "notes": "Effective January 1, 2025 for universal opt-out mechanism recognition.",
    },
    "MT": {
        "state": "Montana",
        "law": "Montana Consumer Data Privacy Act (MCDPA)",
        "statute": "MCA Section 30-14-2807",
        "effective_date": "2024-10-01",
        "scope": "sale_and_targeted_advertising",
        "notes": "Applies to sale of personal data and targeted advertising.",
    },
    "TX": {
        "state": "Texas",
        "law": "Texas Data Privacy and Security Act (TDPSA)",
        "statute": "Tex. Bus. & Com. Code Section 541.055",
        "effective_date": "2025-01-01",
        "scope": "sale_and_targeted_advertising",
        "notes": "Universal opt-out mechanism recognition required from January 1, 2025.",
    },
    "OR": {
        "state": "Oregon",
        "law": "Oregon Consumer Privacy Act (OCPA)",
        "statute": "ORS Section 646A.578",
        "effective_date": "2024-07-01",
        "scope": "sale_and_targeted_advertising",
        "notes": "Controllers shall recognize opt-out preference signals.",
    },
}

# Processing purposes affected by GPC opt-out at CloudVault SaaS Inc.
GPC_AFFECTED_PURPOSES = [
    {
        "purpose_id": "pur_benchmarking_003",
        "purpose_name": "Industry Benchmarking with Datalytics Partners Ltd.",
        "reason": "Constitutes sharing of personal information with a third party",
    },
    {
        "purpose_id": "pur_advertising_004",
        "purpose_name": "Targeted Advertising",
        "reason": "Constitutes sale/sharing for cross-context behavioral advertising",
    },
]

# Purposes NOT affected by GPC (internal use only, not sale/sharing)
GPC_UNAFFECTED_PURPOSES = [
    {
        "purpose_id": "pur_analytics_001",
        "purpose_name": "Service Improvement Analytics",
        "reason": "Internal first-party analytics; does not constitute sale or sharing",
    },
    {
        "purpose_id": "pur_marketing_002",
        "purpose_name": "Product Update Emails",
        "reason": "Direct marketing by controller; not sale or sharing of data",
    },
]


@dataclass
class GPCSignalEvent:
    """Record of a GPC signal detection event."""
    event_id: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    source: str = "http_header"  # "http_header" or "javascript_api"
    user_id: Optional[str] = None
    session_id: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    action_taken: str = ""
    purposes_affected: list = field(default_factory=list)
    conflict_detected: bool = False
    conflict_resolution: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)


def detect_gpc_from_headers(headers: dict) -> bool:
    """
    Detect GPC signal from HTTP request headers.

    Per GPC specification, the signal is transmitted as:
        Sec-GPC: 1

    The header is absent (not set to "0") when GPC is not enabled.

    Args:
        headers: Dictionary of HTTP request headers (case-insensitive keys).

    Returns:
        True if GPC signal is detected, False otherwise.
    """
    normalized = {k.lower(): v for k, v in headers.items()}
    gpc_value = normalized.get("sec-gpc", "").strip()
    return gpc_value == "1"


GPC_JS_DETECTION_CODE = """
// GPC Detection — runs before any tracking scripts
// Per CPRA Section 1798.135(e) and GPC Specification
(function() {
    'use strict';

    var gpcEnabled = (navigator.globalPrivacyControl === true);

    // Store GPC state globally for consent management
    window.__cloudvault_privacy = window.__cloudvault_privacy || {};
    window.__cloudvault_privacy.gpcDetected = gpcEnabled;

    if (gpcEnabled) {
        // Block sale/sharing purposes
        window.__cloudvault_privacy.saleOptOut = true;
        window.__cloudvault_privacy.sharingOptOut = true;

        // Prevent loading of third-party tracking scripts
        window.__cloudvault_privacy.blockThirdPartyTracking = true;

        // Set first-party cookie to persist GPC detection
        document.cookie = 'cv_gpc_detected=1; SameSite=Strict; Secure; Path=/; Max-Age=86400';

        // Log GPC detection event
        if (window.__cloudvault_privacy.consentAPI) {
            window.__cloudvault_privacy.consentAPI.logGPCDetection({
                source: 'javascript_api',
                timestamp: new Date().toISOString(),
                userAgent: navigator.userAgent
            });
        }

        console.log('[CloudVault Privacy] Global Privacy Control signal detected. '
            + 'Opt-out of sale/sharing applied per CPRA Section 1798.135(e).');
    }
})();
"""


def process_gpc_signal(
    user_id: Optional[str],
    session_id: str,
    ip_address: str,
    user_agent: str,
    existing_consents: Optional[dict] = None,
) -> GPCSignalEvent:
    """
    Process a detected GPC signal and determine appropriate actions.

    Args:
        user_id: Authenticated user ID (None for anonymous sessions).
        session_id: Current session identifier.
        ip_address: Request IP address.
        user_agent: Request user agent string.
        existing_consents: Dict of purpose_id -> "granted"/"withdrawn" for the user.

    Returns:
        GPCSignalEvent with actions taken and affected purposes.
    """
    import uuid
    event = GPCSignalEvent(
        event_id=str(uuid.uuid4()),
        user_id=user_id,
        session_id=session_id,
        ip_address=ip_address,
        user_agent=user_agent,
    )

    affected_purpose_ids = []
    conflict_detected = False

    for purpose in GPC_AFFECTED_PURPOSES:
        pid = purpose["purpose_id"]
        affected_purpose_ids.append(pid)

        if existing_consents and existing_consents.get(pid) == "granted":
            conflict_detected = True

    event.purposes_affected = affected_purpose_ids
    event.conflict_detected = conflict_detected

    if conflict_detected:
        event.action_taken = GPCAction.CONFLICT_RESOLVED.value
        event.conflict_resolution = (
            "GPC signal overrides manual opt-in per AG Regulation 11 CCR 7025(c). "
            "User will be notified of the conflict and given the option to re-confirm "
            "participation in any applicable financial incentive program."
        )
    else:
        if existing_consents:
            all_already_out = all(
                existing_consents.get(pid) == "withdrawn"
                for pid in affected_purpose_ids
            )
            if all_already_out:
                event.action_taken = GPCAction.ALREADY_OPTED_OUT.value
            else:
                event.action_taken = GPCAction.OPT_OUT_APPLIED.value
        else:
            event.action_taken = GPCAction.OPT_OUT_APPLIED.value

    return event


def check_state_compliance(states_served: list[str], reference_date: str = "2026-03-14") -> dict:
    """
    Check GPC compliance requirements for states where the business operates.

    Args:
        states_served: List of US state abbreviations where the business has consumers.
        reference_date: Date to check against effective dates (YYYY-MM-DD).

    Returns:
        Compliance report dictionary.
    """
    report = {
        "reference_date": reference_date,
        "states_checked": [],
        "gpc_required": False,
        "applicable_laws": [],
    }

    for state_code in states_served:
        state_info = GPC_STATE_REQUIREMENTS.get(state_code)
        if state_info and reference_date >= state_info["effective_date"]:
            report["gpc_required"] = True
            report["applicable_laws"].append({
                "state": state_info["state"],
                "law": state_info["law"],
                "statute": state_info["statute"],
                "scope": state_info["scope"],
            })
            report["states_checked"].append({
                "code": state_code,
                "state": state_info["state"],
                "gpc_required": True,
                "effective_date": state_info["effective_date"],
            })
        elif state_info:
            report["states_checked"].append({
                "code": state_code,
                "state": state_info["state"],
                "gpc_required": False,
                "effective_date": state_info["effective_date"],
                "note": "Not yet effective as of reference date",
            })
        else:
            report["states_checked"].append({
                "code": state_code,
                "state": state_code,
                "gpc_required": False,
                "note": "No GPC-specific requirement identified in this state",
            })

    return report


if __name__ == "__main__":
    # Demonstrate GPC header detection
    print("=== GPC Header Detection ===")
    headers_with_gpc = {"Sec-GPC": "1", "User-Agent": "Mozilla/5.0", "Accept": "text/html"}
    headers_without_gpc = {"User-Agent": "Mozilla/5.0", "Accept": "text/html"}

    print(f"Headers with GPC: {detect_gpc_from_headers(headers_with_gpc)}")
    print(f"Headers without GPC: {detect_gpc_from_headers(headers_without_gpc)}")

    # Demonstrate GPC signal processing with conflict
    print("\n=== GPC Signal Processing (Conflict Scenario) ===")
    event = process_gpc_signal(
        user_id="usr_7f3a9b2e-41d8-4c76-b5e3-9a8d1c2f4e60",
        session_id="sess_abc123",
        ip_address="198.51.100.42",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Brave/1.62",
        existing_consents={
            "pur_benchmarking_003": "granted",
            "pur_advertising_004": "granted",
        },
    )
    print(json.dumps(event.to_dict(), indent=2))

    # Demonstrate state compliance check
    print("\n=== State Compliance Check ===")
    cloudvault_states = ["CA", "CO", "CT", "TX", "NY", "FL"]
    compliance = check_state_compliance(cloudvault_states)
    print(f"GPC Required: {compliance['gpc_required']}")
    print(f"Applicable Laws: {len(compliance['applicable_laws'])}")
    for law in compliance["applicable_laws"]:
        print(f"  - {law['state']}: {law['law']} ({law['statute']})")

    print("\n=== JavaScript Detection Code (First 5 Lines) ===")
    for line in GPC_JS_DETECTION_CODE.strip().split("\n")[:5]:
        print(f"  {line}")
    print("  ...")
