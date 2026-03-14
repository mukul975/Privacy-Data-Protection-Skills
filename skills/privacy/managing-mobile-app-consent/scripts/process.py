#!/usr/bin/env python3
"""
Mobile App Consent Management

Manages consent for mobile applications including ATT framework
integration, SDK consent propagation, and IDFA/GAID handling.
"""

import json
import uuid
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class Platform(Enum):
    IOS = "ios"
    ANDROID = "android"


class ATTStatus(Enum):
    NOT_DETERMINED = "notDetermined"
    AUTHORIZED = "authorized"
    DENIED = "denied"
    RESTRICTED = "restricted"


class SDKConsentState(Enum):
    ENABLED = "enabled"
    DISABLED = "disabled"
    NOT_INITIALIZED = "not_initialized"


# SDK registry for CloudVault mobile app
SDK_REGISTRY = {
    "firebase_analytics": {
        "name": "Firebase Analytics",
        "vendor": "Google LLC",
        "purpose": "Usage analytics",
        "required_consent": "pur_analytics_001",
        "data_collected": ["screen_views", "events", "device_info", "app_version"],
        "ios_disable": "FirebaseAnalytics.setAnalyticsCollectionEnabled(false)",
        "android_disable": "FirebaseAnalytics.setAnalyticsCollectionEnabled(false)",
    },
    "crashlytics": {
        "name": "Firebase Crashlytics",
        "vendor": "Google LLC",
        "purpose": "Crash reporting",
        "required_consent": "pur_crash_003",
        "data_collected": ["stack_traces", "device_state", "os_version", "app_version"],
        "ios_disable": "Crashlytics.setCrashlyticsCollectionEnabled(false)",
        "android_disable": "Crashlytics.setCrashlyticsCollectionEnabled(false)",
    },
    "appsflyer": {
        "name": "AppsFlyer",
        "vendor": "AppsFlyer Ltd.",
        "purpose": "Attribution and advertising measurement",
        "required_consent": "pur_advertising_002",
        "data_collected": ["idfa_gaid", "install_referrer", "in_app_events"],
        "ios_disable": "AppsFlyerLib.shared().isStopped = true",
        "android_disable": "AppsFlyerLib.getInstance().stop(true, context)",
        "requires_att": True,
    },
}


@dataclass
class MobileConsentRecord:
    """Consent record with mobile-specific fields."""
    consent_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    subject_id: str = ""
    purpose_id: str = ""
    decision: str = "granted"
    mechanism: str = "toggle_switch"
    platform: str = ""
    os_version: str = ""
    app_version: str = ""
    device_model: str = ""
    att_status: Optional[str] = None  # iOS only
    gaid_available: Optional[bool] = None  # Android only
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    ip_address: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class SDKState:
    """Current state of an SDK's consent and initialization."""
    sdk_id: str = ""
    sdk_name: str = ""
    consent_required: str = ""
    consent_granted: bool = False
    att_required: bool = False
    att_granted: bool = False
    initialized: bool = False
    data_collection_active: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


def determine_sdk_states(
    consent_decisions: dict[str, str],
    platform: str,
    att_status: Optional[str] = None,
) -> list[SDKState]:
    """
    Determine which SDKs should be enabled based on consent state.

    Args:
        consent_decisions: Dict of purpose_id -> "granted" or "not_granted".
        platform: "ios" or "android".
        att_status: ATT authorization status (iOS only).

    Returns:
        List of SDKState objects indicating what should be initialized.
    """
    states = []

    for sdk_id, sdk_info in SDK_REGISTRY.items():
        consent_purpose = sdk_info["required_consent"]
        consent_granted = consent_decisions.get(consent_purpose) == "granted"

        att_required = sdk_info.get("requires_att", False) and platform == "ios"
        att_granted = att_status == ATTStatus.AUTHORIZED.value if att_required else True

        should_initialize = consent_granted and (not att_required or att_granted)

        states.append(SDKState(
            sdk_id=sdk_id,
            sdk_name=sdk_info["name"],
            consent_required=consent_purpose,
            consent_granted=consent_granted,
            att_required=att_required,
            att_granted=att_granted,
            initialized=should_initialize,
            data_collection_active=should_initialize,
        ))

    return states


def audit_sdk_compliance(
    consent_decisions: dict[str, str],
    platform: str,
    att_status: Optional[str],
    actual_sdk_states: dict[str, bool],
) -> dict:
    """
    Audit whether SDKs are correctly gated by consent.

    Args:
        consent_decisions: Current consent state.
        platform: "ios" or "android".
        att_status: Current ATT status.
        actual_sdk_states: Dict of sdk_id -> whether it is currently collecting data.

    Returns:
        Audit report with compliance findings.
    """
    expected = determine_sdk_states(consent_decisions, platform, att_status)
    findings = []

    for sdk_state in expected:
        actual_active = actual_sdk_states.get(sdk_state.sdk_id, False)
        expected_active = sdk_state.data_collection_active

        if actual_active and not expected_active:
            findings.append({
                "sdk": sdk_state.sdk_name,
                "severity": "CRITICAL",
                "finding": f"{sdk_state.sdk_name} is collecting data without consent",
                "expected": "disabled",
                "actual": "active",
            })
        elif not actual_active and expected_active:
            findings.append({
                "sdk": sdk_state.sdk_name,
                "severity": "LOW",
                "finding": f"{sdk_state.sdk_name} is disabled despite having consent",
                "expected": "active",
                "actual": "disabled",
            })
        else:
            findings.append({
                "sdk": sdk_state.sdk_name,
                "severity": "NONE",
                "finding": "SDK state matches consent",
                "expected": "active" if expected_active else "disabled",
                "actual": "active" if actual_active else "disabled",
            })

    critical_count = sum(1 for f in findings if f["severity"] == "CRITICAL")

    return {
        "audit_date": datetime.now(timezone.utc).isoformat(),
        "platform": platform,
        "att_status": att_status,
        "findings": findings,
        "critical_issues": critical_count,
        "compliant": critical_count == 0,
    }


if __name__ == "__main__":
    # Demonstrate SDK state determination
    print("=== iOS: User consents to analytics and advertising, ATT authorized ===")
    ios_states = determine_sdk_states(
        consent_decisions={
            "pur_analytics_001": "granted",
            "pur_advertising_002": "granted",
            "pur_crash_003": "not_granted",
        },
        platform="ios",
        att_status="authorized",
    )
    for state in ios_states:
        status = "ACTIVE" if state.data_collection_active else "DISABLED"
        print(f"  {state.sdk_name}: {status}")
        if state.att_required:
            print(f"    ATT required: {state.att_required}, ATT granted: {state.att_granted}")

    print("\n=== iOS: User consents to advertising, but ATT denied ===")
    ios_denied = determine_sdk_states(
        consent_decisions={
            "pur_analytics_001": "not_granted",
            "pur_advertising_002": "granted",
            "pur_crash_003": "granted",
        },
        platform="ios",
        att_status="denied",
    )
    for state in ios_denied:
        status = "ACTIVE" if state.data_collection_active else "DISABLED"
        att_note = " (ATT denied)" if state.att_required and not state.att_granted else ""
        print(f"  {state.sdk_name}: {status}{att_note}")

    # SDK compliance audit
    print("\n=== SDK Compliance Audit ===")
    audit = audit_sdk_compliance(
        consent_decisions={"pur_analytics_001": "not_granted", "pur_advertising_002": "not_granted", "pur_crash_003": "granted"},
        platform="ios",
        att_status="denied",
        actual_sdk_states={"firebase_analytics": True, "crashlytics": True, "appsflyer": False},
    )
    print(f"Compliant: {audit['compliant']}")
    for f in audit["findings"]:
        print(f"  [{f['severity']}] {f['sdk']}: {f['finding']}")
