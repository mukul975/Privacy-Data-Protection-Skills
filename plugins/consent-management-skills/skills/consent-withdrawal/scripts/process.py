#!/usr/bin/env python3
"""
Consent Withdrawal Processing Engine

Implements GDPR Article 7(3) consent withdrawal with cascading effects,
downstream notification, and equal ease compliance auditing.
"""

import json
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class WithdrawalStatus(Enum):
    INITIATED = "initiated"
    PROCESSING = "processing"
    PROPAGATING = "propagating"
    COMPLETED = "completed"
    FAILED = "failed"


class PropagationStatus(Enum):
    PENDING = "pending"
    SENT = "sent"
    ACKNOWLEDGED = "acknowledged"
    COMPLETED = "completed"
    FAILED = "failed"
    ESCALATED = "escalated"


class EscalationLevel(Enum):
    RETRY = "automated_retry"
    ENGINEERING = "engineering_alert"
    DPO = "dpo_escalation"
    DPA_BREACH = "dpa_breach_process"


@dataclass
class WithdrawalRequest:
    """A consent withdrawal request from a data subject."""
    withdrawal_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    subject_id: str = ""
    purpose_id: str = ""
    purpose_name: str = ""
    mechanism: str = "toggle_switch"
    source: str = "preference_center"
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    status: str = WithdrawalStatus.INITIATED.value
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class PropagationEvent:
    """Tracks notification to a downstream system after consent withdrawal."""
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    withdrawal_id: str = ""
    target_system: str = ""
    target_type: str = "internal"  # "internal" or "third_party"
    notification_payload: dict = field(default_factory=dict)
    status: str = PropagationStatus.PENDING.value
    sent_at: Optional[str] = None
    acknowledged_at: Optional[str] = None
    completed_at: Optional[str] = None
    escalation_level: Optional[str] = None
    sla_deadline: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class EqualEaseMetrics:
    """Metrics for comparing consent-giving vs withdrawal ease."""
    action: str  # "give_consent" or "withdraw_consent"
    purpose_id: str
    path: str  # "signup_flow", "preference_center", "email_unsubscribe", etc.
    click_count: int = 0
    page_navigations: int = 0
    form_fields: int = 0
    estimated_seconds: float = 0.0

    def to_dict(self) -> dict:
        return asdict(self)


# Downstream systems configuration for CloudVault SaaS Inc.
DOWNSTREAM_SYSTEMS = {
    "pur_analytics_001": [
        {
            "system": "analytics_sdk",
            "type": "internal",
            "action": "disable_tracking",
            "sla_hours": 1,
        },
        {
            "system": "analytics_data_warehouse",
            "type": "internal",
            "action": "flag_data_for_review",
            "sla_hours": 24,
        },
    ],
    "pur_marketing_002": [
        {
            "system": "email_marketing_platform",
            "type": "internal",
            "action": "remove_from_lists_and_suppress",
            "sla_hours": 1,
        },
        {
            "system": "campaign_scheduler",
            "type": "internal",
            "action": "cancel_scheduled_campaigns",
            "sla_hours": 1,
        },
    ],
    "pur_benchmarking_003": [
        {
            "system": "data_export_pipeline",
            "type": "internal",
            "action": "stop_export",
            "sla_hours": 1,
        },
        {
            "system": "datalytics_partners_api",
            "type": "third_party",
            "action": "cease_processing_notification",
            "sla_hours": 4,
            "api_endpoint": "https://api.datalytics-partners.nl/v2/consent/withdrawal",
        },
    ],
}


class ConsentWithdrawalEngine:
    """
    Processes consent withdrawals with cascading effects per Art. 7(3).
    """

    def __init__(self):
        self.withdrawals: list[WithdrawalRequest] = []
        self.propagation_events: list[PropagationEvent] = []

    def process_withdrawal(
        self,
        subject_id: str,
        purpose_id: str,
        mechanism: str = "toggle_switch",
        source: str = "preference_center",
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
    ) -> WithdrawalRequest:
        """
        Process a consent withdrawal and trigger cascading effects.

        Args:
            subject_id: Data subject identifier.
            purpose_id: Purpose being withdrawn.
            mechanism: UI mechanism used ("toggle_switch", "unsubscribe_link", "api_call").
            source: Where withdrawal was initiated.
            ip_address: Request IP.
            user_agent: Request user agent.

        Returns:
            WithdrawalRequest with processing status.
        """
        purpose_names = {
            "pur_analytics_001": "Service Improvement Analytics",
            "pur_marketing_002": "Product Update Emails",
            "pur_benchmarking_003": "Industry Benchmarking with Datalytics Partners Ltd.",
        }

        withdrawal = WithdrawalRequest(
            subject_id=subject_id,
            purpose_id=purpose_id,
            purpose_name=purpose_names.get(purpose_id, purpose_id),
            mechanism=mechanism,
            source=source,
            ip_address=ip_address,
            user_agent=user_agent,
            status=WithdrawalStatus.PROCESSING.value,
        )

        self.withdrawals.append(withdrawal)

        # Trigger cascading notifications
        self._propagate_withdrawal(withdrawal)

        withdrawal.status = WithdrawalStatus.PROPAGATING.value
        return withdrawal

    def _propagate_withdrawal(self, withdrawal: WithdrawalRequest) -> None:
        """Dispatch withdrawal notifications to all downstream systems."""
        systems = DOWNSTREAM_SYSTEMS.get(withdrawal.purpose_id, [])

        for system in systems:
            sla_deadline = (
                datetime.now(timezone.utc) + timedelta(hours=system["sla_hours"])
            ).isoformat()

            payload = {
                "notification_type": "consent_withdrawal",
                "subject_id_hash": f"sha256:{withdrawal.subject_id[:8]}...",
                "purpose_id": withdrawal.purpose_id,
                "withdrawal_timestamp": withdrawal.timestamp,
                "required_action": system["action"],
                "action_deadline": sla_deadline,
                "acknowledgment_required": True,
                "controller": "CloudVault SaaS Inc.",
            }

            event = PropagationEvent(
                withdrawal_id=withdrawal.withdrawal_id,
                target_system=system["system"],
                target_type=system["type"],
                notification_payload=payload,
                status=PropagationStatus.SENT.value,
                sent_at=datetime.now(timezone.utc).isoformat(),
                sla_deadline=sla_deadline,
            )

            self.propagation_events.append(event)

    def check_sla_compliance(self) -> list[dict]:
        """
        Check all propagation events for SLA compliance.

        Returns:
            List of SLA violation records.
        """
        now = datetime.now(timezone.utc).isoformat()
        violations = []

        for event in self.propagation_events:
            if event.status in (PropagationStatus.COMPLETED.value, PropagationStatus.ACKNOWLEDGED.value):
                continue

            if event.sla_deadline and now > event.sla_deadline:
                violations.append({
                    "event_id": event.event_id,
                    "withdrawal_id": event.withdrawal_id,
                    "target_system": event.target_system,
                    "target_type": event.target_type,
                    "sla_deadline": event.sla_deadline,
                    "current_status": event.status,
                    "overdue": True,
                })

        return violations

    def acknowledge_propagation(self, event_id: str) -> Optional[PropagationEvent]:
        """Record acknowledgment from a downstream system."""
        for event in self.propagation_events:
            if event.event_id == event_id:
                event.status = PropagationStatus.ACKNOWLEDGED.value
                event.acknowledged_at = datetime.now(timezone.utc).isoformat()
                return event
        return None

    def complete_propagation(self, event_id: str) -> Optional[PropagationEvent]:
        """Record completion of processing cessation by downstream system."""
        for event in self.propagation_events:
            if event.event_id == event_id:
                event.status = PropagationStatus.COMPLETED.value
                event.completed_at = datetime.now(timezone.utc).isoformat()

                # Check if all propagation events for this withdrawal are complete
                withdrawal_id = event.withdrawal_id
                related = [e for e in self.propagation_events if e.withdrawal_id == withdrawal_id]
                if all(e.status == PropagationStatus.COMPLETED.value for e in related):
                    for w in self.withdrawals:
                        if w.withdrawal_id == withdrawal_id:
                            w.status = WithdrawalStatus.COMPLETED.value
                            break
                return event
        return None


def audit_equal_ease(give_metrics: list[EqualEaseMetrics], withdraw_metrics: list[EqualEaseMetrics]) -> dict:
    """
    Audit equal ease compliance per GDPR Article 7(3).

    Compares consent-giving metrics against withdrawal metrics.
    Withdrawal must be equal to or easier than giving consent.

    Returns:
        Audit report with pass/fail per purpose and path.
    """
    results = []

    for give in give_metrics:
        matching_withdrawals = [
            w for w in withdraw_metrics
            if w.purpose_id == give.purpose_id
        ]

        for withdraw in matching_withdrawals:
            checks = {
                "click_count": withdraw.click_count <= give.click_count,
                "page_navigations": withdraw.page_navigations <= give.page_navigations,
                "form_fields": withdraw.form_fields <= give.form_fields,
            }
            overall_pass = all(checks.values())

            results.append({
                "purpose_id": give.purpose_id,
                "give_path": give.path,
                "withdraw_path": withdraw.path,
                "give_clicks": give.click_count,
                "withdraw_clicks": withdraw.click_count,
                "give_pages": give.page_navigations,
                "withdraw_pages": withdraw.page_navigations,
                "checks": checks,
                "compliant": overall_pass,
            })

    compliant_count = sum(1 for r in results if r["compliant"])
    total = len(results)

    return {
        "audit_date": datetime.now(timezone.utc).isoformat(),
        "results": results,
        "summary": {
            "total_comparisons": total,
            "compliant": compliant_count,
            "non_compliant": total - compliant_count,
            "compliance_rate": round(compliant_count / total * 100, 1) if total > 0 else 0.0,
        },
    }


if __name__ == "__main__":
    engine = ConsentWithdrawalEngine()

    # Process a withdrawal for third-party benchmarking
    print("=== Processing Consent Withdrawal ===")
    withdrawal = engine.process_withdrawal(
        subject_id="usr_7f3a9b2e-41d8-4c76-b5e3-9a8d1c2f4e60",
        purpose_id="pur_benchmarking_003",
        mechanism="toggle_switch",
        source="preference_center",
        ip_address="198.51.100.42",
    )
    print(f"Withdrawal ID: {withdrawal.withdrawal_id}")
    print(f"Status: {withdrawal.status}")
    print(f"Purpose: {withdrawal.purpose_name}")

    # Show propagation events
    print(f"\n=== Propagation Events ({len(engine.propagation_events)}) ===")
    for event in engine.propagation_events:
        print(f"  -> {event.target_system} ({event.target_type}): {event.status}")
        print(f"     SLA Deadline: {event.sla_deadline}")

    # Simulate acknowledgment
    if engine.propagation_events:
        first_event = engine.propagation_events[0]
        engine.acknowledge_propagation(first_event.event_id)
        engine.complete_propagation(first_event.event_id)
        print(f"\n  Acknowledged and completed: {first_event.target_system}")

    # Equal ease audit
    print("\n=== Equal Ease Audit ===")
    give_metrics = [
        EqualEaseMetrics("give_consent", "pur_marketing_002", "signup_flow", click_count=1, page_navigations=0, form_fields=0, estimated_seconds=2),
        EqualEaseMetrics("give_consent", "pur_benchmarking_003", "signup_flow", click_count=1, page_navigations=0, form_fields=0, estimated_seconds=2),
    ]
    withdraw_metrics = [
        EqualEaseMetrics("withdraw_consent", "pur_marketing_002", "preference_center", click_count=2, page_navigations=1, form_fields=0, estimated_seconds=5),
        EqualEaseMetrics("withdraw_consent", "pur_marketing_002", "email_unsubscribe", click_count=1, page_navigations=1, form_fields=0, estimated_seconds=3),
        EqualEaseMetrics("withdraw_consent", "pur_benchmarking_003", "preference_center", click_count=2, page_navigations=1, form_fields=0, estimated_seconds=5),
    ]

    audit = audit_equal_ease(give_metrics, withdraw_metrics)
    print(f"Compliance Rate: {audit['summary']['compliance_rate']}%")
    for r in audit["results"]:
        status = "PASS" if r["compliant"] else "FAIL"
        print(f"  {r['purpose_id']} ({r['withdraw_path']}): {status} "
              f"[give={r['give_clicks']} clicks, withdraw={r['withdraw_clicks']} clicks]")
