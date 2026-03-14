#!/usr/bin/env python3
"""
Consent Preference Center — Backend Logic

Implements consent management APIs, version tracking, and propagation
per GDPR Article 7 and IAB TCF v2.2 requirements.
"""

import json
import hashlib
import uuid
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class ConsentDecisionType(Enum):
    GRANTED = "granted"
    WITHDRAWN = "withdrawn"


class ConsentSource(Enum):
    SIGNUP_FLOW = "signup_flow"
    PREFERENCE_CENTER = "preference_center"
    COOKIE_BANNER = "cookie_banner"
    API = "api"


class PropagationStatus(Enum):
    PENDING = "pending"
    DELIVERED = "delivered"
    ACKNOWLEDGED = "acknowledged"
    FAILED = "failed"


@dataclass
class ConsentPurpose:
    """A processing purpose registered in the consent system."""
    purpose_id: str
    purpose_name: str
    purpose_description: str
    data_categories: list[str]
    recipients: list[str]
    retention_period: str
    tcf_purpose_id: Optional[int] = None
    is_active: bool = True

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ConsentTextVersion:
    """Immutable record of consent text presented to users."""
    version_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    purpose_id: str = ""
    consent_text: str = ""
    text_hash: str = ""
    effective_from: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    effective_until: Optional[str] = None
    approved_by: str = ""

    def compute_hash(self) -> str:
        self.text_hash = hashlib.sha256(self.consent_text.encode("utf-8")).hexdigest()
        return self.text_hash


@dataclass
class ConsentDecisionRecord:
    """A single consent decision by a data subject."""
    decision_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    subject_id: str = ""
    purpose_id: str = ""
    version_id: str = ""
    decision: str = "granted"
    mechanism: str = "toggle_switch"
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    source: str = "preference_center"

    def to_dict(self) -> dict:
        return asdict(self)


class ConsentPreferenceCenter:
    """
    Core consent preference center logic.

    Manages purposes, consent decisions, version history,
    and downstream propagation tracking.
    """

    def __init__(self):
        self.purposes: dict[str, ConsentPurpose] = {}
        self.text_versions: dict[str, ConsentTextVersion] = {}
        self.decisions: list[ConsentDecisionRecord] = []
        self.propagation_log: list[dict] = []

    def register_purpose(self, purpose: ConsentPurpose) -> str:
        """Register a new processing purpose."""
        self.purposes[purpose.purpose_id] = purpose
        return purpose.purpose_id

    def create_text_version(
        self, purpose_id: str, consent_text: str, approved_by: str
    ) -> ConsentTextVersion:
        """Create a new immutable consent text version."""
        version = ConsentTextVersion(
            purpose_id=purpose_id,
            consent_text=consent_text,
            approved_by=approved_by,
        )
        version.compute_hash()

        # Expire previous version for this purpose
        for v in self.text_versions.values():
            if v.purpose_id == purpose_id and v.effective_until is None:
                v.effective_until = datetime.now(timezone.utc).isoformat()

        self.text_versions[version.version_id] = version
        return version

    def get_current_version(self, purpose_id: str) -> Optional[ConsentTextVersion]:
        """Get the current active consent text version for a purpose."""
        for v in self.text_versions.values():
            if v.purpose_id == purpose_id and v.effective_until is None:
                return v
        return None

    def record_decision(
        self,
        subject_id: str,
        purpose_id: str,
        decision: ConsentDecisionType,
        mechanism: str = "toggle_switch",
        source: ConsentSource = ConsentSource.PREFERENCE_CENTER,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
    ) -> ConsentDecisionRecord:
        """Record a consent decision and trigger propagation."""
        current_version = self.get_current_version(purpose_id)
        version_id = current_version.version_id if current_version else "unknown"

        record = ConsentDecisionRecord(
            subject_id=subject_id,
            purpose_id=purpose_id,
            version_id=version_id,
            decision=decision.value,
            mechanism=mechanism,
            source=source.value,
            ip_address=ip_address,
            user_agent=user_agent,
        )
        self.decisions.append(record)

        # Trigger downstream propagation for withdrawals
        if decision == ConsentDecisionType.WITHDRAWN:
            self._propagate_withdrawal(record)

        return record

    def _propagate_withdrawal(self, decision: ConsentDecisionRecord) -> None:
        """Notify downstream systems of consent withdrawal."""
        purpose = self.purposes.get(decision.purpose_id)
        if not purpose:
            return

        targets = []
        if purpose.recipients:
            targets.extend(purpose.recipients)
        targets.append("internal_data_pipeline")
        targets.append("analytics_service")

        for target in targets:
            self.propagation_log.append({
                "propagation_id": str(uuid.uuid4()),
                "decision_id": decision.decision_id,
                "target_system": target,
                "status": PropagationStatus.PENDING.value,
                "sent_at": datetime.now(timezone.utc).isoformat(),
                "acknowledged_at": None,
            })

    def get_preferences(self, subject_id: str) -> dict:
        """Get current consent state for all purposes for a subject."""
        preferences = []
        for purpose_id, purpose in self.purposes.items():
            if not purpose.is_active:
                continue

            # Find the most recent decision for this subject and purpose
            relevant = [
                d for d in self.decisions
                if d.subject_id == subject_id and d.purpose_id == purpose_id
            ]
            relevant.sort(key=lambda d: d.timestamp, reverse=True)

            if relevant:
                latest = relevant[0]
                preferences.append({
                    "purpose_id": purpose_id,
                    "purpose_name": purpose.purpose_name,
                    "decision": latest.decision,
                    "decided_at": latest.timestamp,
                    "version_id": latest.version_id,
                })
            else:
                preferences.append({
                    "purpose_id": purpose_id,
                    "purpose_name": purpose.purpose_name,
                    "decision": "not_set",
                    "decided_at": None,
                    "version_id": None,
                })

        return {
            "subject_id": subject_id,
            "preferences": preferences,
            "last_updated": max(
                (d.timestamp for d in self.decisions if d.subject_id == subject_id),
                default=None,
            ),
        }

    def get_consent_history(self, subject_id: str, purpose_id: Optional[str] = None) -> list[dict]:
        """Get full consent history for audit per Art. 7(1)."""
        history = []
        for d in self.decisions:
            if d.subject_id != subject_id:
                continue
            if purpose_id and d.purpose_id != purpose_id:
                continue
            entry = d.to_dict()
            version = self.text_versions.get(d.version_id)
            if version:
                entry["consent_text_hash"] = version.text_hash
            history.append(entry)
        history.sort(key=lambda x: x["timestamp"])
        return history

    def generate_audit_report(self, start_date: str, end_date: str) -> dict:
        """Generate consent audit report for a date range."""
        period_decisions = [
            d for d in self.decisions
            if start_date <= d.timestamp <= end_date
        ]

        by_purpose: dict[str, dict] = {}
        for d in period_decisions:
            if d.purpose_id not in by_purpose:
                by_purpose[d.purpose_id] = {"granted": 0, "withdrawn": 0}
            by_purpose[d.purpose_id][d.decision] += 1

        pending_propagations = [
            p for p in self.propagation_log
            if p["status"] == PropagationStatus.PENDING.value
        ]

        return {
            "audit_period": {"start": start_date, "end": end_date},
            "total_decisions": len(period_decisions),
            "by_purpose": by_purpose,
            "pending_propagations": len(pending_propagations),
            "report_generated_at": datetime.now(timezone.utc).isoformat(),
        }


if __name__ == "__main__":
    center = ConsentPreferenceCenter()

    # Register purposes for CloudVault SaaS Inc.
    center.register_purpose(ConsentPurpose(
        purpose_id="pur_analytics_001",
        purpose_name="Service Improvement Analytics",
        purpose_description="Analyze file usage patterns to recommend storage optimization",
        data_categories=["file_metadata", "access_frequency", "storage_patterns"],
        recipients=[],
        retention_period="24 months from collection",
        tcf_purpose_id=7,
    ))

    center.register_purpose(ConsentPurpose(
        purpose_id="pur_marketing_002",
        purpose_name="Product Update Emails",
        purpose_description="Send emails about new CloudVault features and improvements",
        data_categories=["email_address", "name", "product_usage_tier"],
        recipients=[],
        retention_period="Until consent withdrawn",
    ))

    center.register_purpose(ConsentPurpose(
        purpose_id="pur_benchmarking_003",
        purpose_name="Industry Benchmarking with Datalytics Partners Ltd.",
        purpose_description="Share anonymized usage statistics with Datalytics Partners Ltd. for cloud storage industry benchmarking",
        data_categories=["anonymized_usage_metrics", "storage_tier", "region"],
        recipients=["Datalytics Partners Ltd."],
        retention_period="36 months from aggregation",
    ))

    # Create consent text versions
    center.create_text_version(
        "pur_analytics_001",
        "I allow CloudVault SaaS Inc. to analyze my file usage patterns (file sizes, types, and access frequency — not file contents) to provide personalized storage optimization recommendations. I can withdraw this consent anytime in Settings > Privacy.",
        "Marta Kowalski, DPO",
    )

    center.create_text_version(
        "pur_marketing_002",
        "I allow CloudVault SaaS Inc. to send me emails about product updates and new features. Emails will be sent no more than twice per month. I can unsubscribe from any email or withdraw consent in Settings > Privacy.",
        "Marta Kowalski, DPO",
    )

    center.create_text_version(
        "pur_benchmarking_003",
        "I allow CloudVault SaaS Inc. to share my anonymized usage statistics (storage tier, region, aggregated usage metrics — no personal identifiers) with Datalytics Partners Ltd. (Amsterdam, Netherlands) for cloud storage industry benchmarking reports. I can withdraw this consent anytime in Settings > Privacy.",
        "Marta Kowalski, DPO",
    )

    # Simulate user consent flow
    subject = "usr_7f3a9b2e-41d8-4c76-b5e3-9a8d1c2f4e60"

    center.record_decision(subject, "pur_analytics_001", ConsentDecisionType.GRANTED,
                           source=ConsentSource.SIGNUP_FLOW, ip_address="198.51.100.42")
    center.record_decision(subject, "pur_marketing_002", ConsentDecisionType.GRANTED,
                           source=ConsentSource.SIGNUP_FLOW, ip_address="198.51.100.42")
    center.record_decision(subject, "pur_benchmarking_003", ConsentDecisionType.GRANTED,
                           source=ConsentSource.SIGNUP_FLOW, ip_address="198.51.100.42")

    # User later withdraws marketing consent via preference center
    center.record_decision(subject, "pur_marketing_002", ConsentDecisionType.WITHDRAWN,
                           source=ConsentSource.PREFERENCE_CENTER, ip_address="198.51.100.42")

    # Display current preferences
    prefs = center.get_preferences(subject)
    print("=== Current Consent Preferences ===")
    print(json.dumps(prefs, indent=2))

    # Display consent history
    history = center.get_consent_history(subject)
    print(f"\n=== Consent History ({len(history)} records) ===")
    for h in history:
        print(f"  {h['timestamp']}: {h['purpose_id']} -> {h['decision']} via {h['source']}")

    # Check propagation log
    print(f"\n=== Propagation Log ({len(center.propagation_log)} entries) ===")
    for p in center.propagation_log:
        print(f"  Decision {p['decision_id'][:8]}... -> {p['target_system']}: {p['status']}")
