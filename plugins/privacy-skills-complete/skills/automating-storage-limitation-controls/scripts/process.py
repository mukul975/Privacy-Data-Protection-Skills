#!/usr/bin/env python3
"""
Storage Limitation Automation Engine

Implements GDPR Article 5(1)(e) automated retention enforcement with
TTL-based deletion, legal hold management, and lifecycle transitions.
"""

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from enum import Enum
from typing import Optional
from uuid import uuid4


class RetentionTrigger(Enum):
    ACCOUNT_CLOSURE = "account_closure"
    TRANSACTION_DATE = "transaction_date"
    CONSENT_WITHDRAWAL = "consent_withdrawal"
    TICKET_CLOSURE = "ticket_closure"
    LOG_CREATION = "log_creation"
    EMPLOYMENT_END = "employment_end"
    DATA_COLLECTION = "data_collection"
    PROCESSING_CESSATION = "processing_cessation"


class StorageTier(Enum):
    HOT = "hot"
    WARM = "warm"
    COLD = "cold"
    DELETED = "deleted"


class LifecycleAction(Enum):
    RETAIN = "retain"
    ARCHIVE = "archive_to_warm"
    COLD_ARCHIVE = "archive_to_cold"
    DELETE = "delete"
    HOLD = "legal_hold"


@dataclass
class RetentionPolicy:
    """Retention policy for a specific data category."""
    policy_id: str
    data_category: str
    purpose: str
    lawful_basis: str
    retention_period_days: int
    retention_trigger: RetentionTrigger
    archive_before_delete: bool = True
    warm_duration_days: int = 90
    legal_reference: str = ""


@dataclass
class LegalHold:
    """A legal hold that suspends automated deletion."""
    hold_id: str
    matter_reference: str
    data_categories: list[str]
    date_range_start: Optional[datetime] = None
    date_range_end: Optional[datetime] = None
    subject_identifiers: list[str] = field(default_factory=list)
    issued_by: str = ""
    issued_date: str = ""
    review_cadence_days: int = 30
    last_reviewed: str = ""
    active: bool = True


@dataclass
class DataRecord:
    """A personal data record with retention lifecycle metadata."""
    record_id: str
    data_category: str
    subject_id: str
    created_at: datetime
    retention_trigger_date: Optional[datetime] = None
    ttl_expiry_date: Optional[datetime] = None
    legal_hold_id: Optional[str] = None
    current_tier: StorageTier = StorageTier.HOT
    deleted: bool = False


class RetentionPolicyEngine:
    """
    Automated retention policy enforcement engine.

    Manages retention policies, legal holds, and lifecycle transitions
    for GDPR Article 5(1)(e) compliance.
    """

    def __init__(self, organization: str = "Prism Data Systems AG"):
        self.organization = organization
        self.policies: dict[str, RetentionPolicy] = {}
        self.legal_holds: dict[str, LegalHold] = {}
        self.records: list[DataRecord] = []
        self.audit_log: list[dict] = []
        self.deletion_count = 0
        self.archive_count = 0
        self.hold_count = 0

    def register_policy(self, policy: RetentionPolicy) -> None:
        self.policies[policy.data_category] = policy

    def register_legal_hold(self, hold: LegalHold) -> None:
        self.legal_holds[hold.hold_id] = hold
        affected = 0
        for record in self.records:
            if self._record_matches_hold(record, hold):
                record.legal_hold_id = hold.hold_id
                affected += 1

        self._log("legal_hold_registered", {
            "hold_id": hold.hold_id,
            "matter_reference": hold.matter_reference,
            "affected_records": affected,
        })

    def release_legal_hold(self, hold_id: str, released_by: str) -> dict:
        hold = self.legal_holds.get(hold_id)
        if hold is None:
            return {"status": "error", "message": f"Hold {hold_id} not found"}

        hold.active = False
        released_count = 0
        for record in self.records:
            if record.legal_hold_id == hold_id:
                record.legal_hold_id = None
                released_count += 1

        self._log("legal_hold_released", {
            "hold_id": hold_id,
            "released_by": released_by,
            "records_released": released_count,
        })

        return {
            "status": "success",
            "records_released": released_count,
            "hold_id": hold_id,
        }

    def add_record(self, record: DataRecord) -> None:
        policy = self.policies.get(record.data_category)
        if policy and record.retention_trigger_date:
            record.ttl_expiry_date = (
                record.retention_trigger_date + timedelta(days=policy.retention_period_days)
            )
        self.records.append(record)

    def trigger_retention_event(self, record_id: str, trigger_date: datetime) -> None:
        for record in self.records:
            if record.record_id == record_id:
                record.retention_trigger_date = trigger_date
                policy = self.policies.get(record.data_category)
                if policy:
                    record.ttl_expiry_date = trigger_date + timedelta(days=policy.retention_period_days)
                self._log("retention_triggered", {
                    "record_id": record_id,
                    "trigger_date": trigger_date.isoformat(),
                    "ttl_expiry": record.ttl_expiry_date.isoformat() if record.ttl_expiry_date else None,
                })
                break

    def run_lifecycle_scan(self, scan_date: Optional[datetime] = None) -> dict:
        """
        Execute a lifecycle scan to identify and process expired records.

        Returns:
            Summary of actions taken during the scan.
        """
        now = scan_date or datetime.now(timezone.utc)
        results = {
            "scan_date": now.isoformat(),
            "records_scanned": 0,
            "records_deleted": 0,
            "records_archived": 0,
            "records_held": 0,
            "records_retained": 0,
            "overdue_records": 0,
            "actions": [],
        }

        for record in self.records:
            if record.deleted:
                continue

            results["records_scanned"] += 1
            action = self._determine_action(record, now)

            if action == LifecycleAction.DELETE:
                record.deleted = True
                record.current_tier = StorageTier.DELETED
                self.deletion_count += 1
                results["records_deleted"] += 1
                results["actions"].append({
                    "record_id": record.record_id,
                    "action": "deleted",
                    "data_category": record.data_category,
                    "reason": "TTL expired, no legal hold",
                })
                self._log("record_deleted", {
                    "record_id": record.record_id,
                    "data_category": record.data_category,
                    "ttl_expiry": record.ttl_expiry_date.isoformat() if record.ttl_expiry_date else None,
                })

            elif action == LifecycleAction.ARCHIVE:
                record.current_tier = StorageTier.WARM
                self.archive_count += 1
                results["records_archived"] += 1
                results["actions"].append({
                    "record_id": record.record_id,
                    "action": "archived_to_warm",
                    "data_category": record.data_category,
                })

            elif action == LifecycleAction.HOLD:
                self.hold_count += 1
                results["records_held"] += 1
                results["actions"].append({
                    "record_id": record.record_id,
                    "action": "held",
                    "hold_id": record.legal_hold_id,
                    "data_category": record.data_category,
                })

            else:
                results["records_retained"] += 1

            # Check for overdue records (TTL exceeded by 7+ days)
            if (record.ttl_expiry_date
                    and not record.deleted
                    and record.legal_hold_id is None
                    and (now - record.ttl_expiry_date).days > 7):
                results["overdue_records"] += 1

        self._log("lifecycle_scan_completed", {
            "scan_date": now.isoformat(),
            "deleted": results["records_deleted"],
            "archived": results["records_archived"],
            "held": results["records_held"],
            "overdue": results["overdue_records"],
        })

        return results

    def _determine_action(self, record: DataRecord, now: datetime) -> LifecycleAction:
        # Legal hold takes priority
        if record.legal_hold_id is not None:
            hold = self.legal_holds.get(record.legal_hold_id)
            if hold and hold.active:
                return LifecycleAction.HOLD

        # No TTL set yet (trigger event has not occurred)
        if record.ttl_expiry_date is None:
            return LifecycleAction.RETAIN

        # TTL expired
        if now >= record.ttl_expiry_date:
            policy = self.policies.get(record.data_category)
            if policy and policy.archive_before_delete and record.current_tier == StorageTier.HOT:
                return LifecycleAction.ARCHIVE
            return LifecycleAction.DELETE

        # Check if archival transition is due (trigger date + warm duration)
        if record.retention_trigger_date:
            policy = self.policies.get(record.data_category)
            if policy and policy.archive_before_delete:
                archive_date = record.retention_trigger_date + timedelta(days=policy.warm_duration_days)
                if now >= archive_date and record.current_tier == StorageTier.HOT:
                    return LifecycleAction.ARCHIVE

        return LifecycleAction.RETAIN

    def _record_matches_hold(self, record: DataRecord, hold: LegalHold) -> bool:
        if record.data_category not in hold.data_categories:
            return False
        if hold.subject_identifiers and record.subject_id not in hold.subject_identifiers:
            return False
        if hold.date_range_start and record.created_at < hold.date_range_start:
            return False
        if hold.date_range_end and record.created_at > hold.date_range_end:
            return False
        return True

    def _log(self, event: str, details: dict) -> None:
        self.audit_log.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event": event,
            "organization": self.organization,
            **details,
        })

    def get_retention_report(self) -> dict:
        active_records = [r for r in self.records if not r.deleted]
        held_records = [r for r in active_records if r.legal_hold_id is not None]

        by_category = {}
        for r in active_records:
            cat = r.data_category
            if cat not in by_category:
                by_category[cat] = {"count": 0, "held": 0}
            by_category[cat]["count"] += 1
            if r.legal_hold_id:
                by_category[cat]["held"] += 1

        by_tier = {}
        for r in active_records:
            tier = r.current_tier.value
            by_tier[tier] = by_tier.get(tier, 0) + 1

        return {
            "organization": self.organization,
            "report_date": datetime.now(timezone.utc).isoformat(),
            "total_active_records": len(active_records),
            "total_deleted_records": self.deletion_count,
            "total_held_records": len(held_records),
            "active_legal_holds": sum(1 for h in self.legal_holds.values() if h.active),
            "by_category": by_category,
            "by_tier": by_tier,
        }


def run_example():
    """Demonstrate storage limitation automation for Prism Data Systems AG."""

    engine = RetentionPolicyEngine()

    # Register retention policies
    engine.register_policy(RetentionPolicy(
        policy_id="RET-ACCT-001",
        data_category="customer_account",
        purpose="Service delivery",
        lawful_basis="Article 6(1)(b)",
        retention_period_days=90,
        retention_trigger=RetentionTrigger.ACCOUNT_CLOSURE,
        archive_before_delete=True,
        warm_duration_days=30,
        legal_reference="Art. 5(1)(e), Art. 17(1)(a)",
    ))

    engine.register_policy(RetentionPolicy(
        policy_id="RET-TX-001",
        data_category="transaction_record",
        purpose="Tax compliance",
        lawful_basis="Article 6(1)(c)",
        retention_period_days=3650,
        retention_trigger=RetentionTrigger.TRANSACTION_DATE,
        archive_before_delete=True,
        warm_duration_days=365,
        legal_reference="Swiss CO Art. 958f",
    ))

    engine.register_policy(RetentionPolicy(
        policy_id="RET-LOG-001",
        data_category="server_log",
        purpose="Security monitoring",
        lawful_basis="Article 6(1)(f)",
        retention_period_days=365,
        retention_trigger=RetentionTrigger.LOG_CREATION,
        archive_before_delete=False,
        legal_reference="Art. 5(1)(e), ENISA recommendation",
    ))

    # Add sample records
    now = datetime.now(timezone.utc)

    records = [
        DataRecord(
            record_id="REC-001",
            data_category="customer_account",
            subject_id="SUBJ-12847",
            created_at=now - timedelta(days=400),
            retention_trigger_date=now - timedelta(days=120),
        ),
        DataRecord(
            record_id="REC-002",
            data_category="customer_account",
            subject_id="SUBJ-55901",
            created_at=now - timedelta(days=200),
            retention_trigger_date=now - timedelta(days=50),
        ),
        DataRecord(
            record_id="REC-003",
            data_category="transaction_record",
            subject_id="SUBJ-12847",
            created_at=now - timedelta(days=400),
            retention_trigger_date=now - timedelta(days=400),
        ),
        DataRecord(
            record_id="REC-004",
            data_category="server_log",
            subject_id="SUBJ-12847",
            created_at=now - timedelta(days=500),
            retention_trigger_date=now - timedelta(days=500),
        ),
        DataRecord(
            record_id="REC-005",
            data_category="server_log",
            subject_id="SUBJ-33210",
            created_at=now - timedelta(days=100),
            retention_trigger_date=now - timedelta(days=100),
        ),
    ]

    for rec in records:
        engine.add_record(rec)

    print("=== Storage Limitation Automation Demo ===")
    print(f"Organization: {engine.organization}")
    print(f"Registered Policies: {len(engine.policies)}")
    print(f"Active Records: {len(engine.records)}")
    print()

    # Print record status before scan
    print("--- Records Before Lifecycle Scan ---")
    for r in engine.records:
        days_to_expiry = (r.ttl_expiry_date - now).days if r.ttl_expiry_date else None
        status = "EXPIRED" if days_to_expiry is not None and days_to_expiry < 0 else f"{days_to_expiry}d remaining"
        print(f"  {r.record_id} [{r.data_category}] Tier={r.current_tier.value} TTL={status}")
    print()

    # Register a legal hold
    engine.register_legal_hold(LegalHold(
        hold_id="HOLD-2026-0023",
        matter_reference="Regulatory inquiry RA-2026-CH-0089",
        data_categories=["customer_account", "transaction_record"],
        date_range_start=now - timedelta(days=450),
        date_range_end=now - timedelta(days=100),
        issued_by="Dr. Eva Hartmann (General Counsel)",
        issued_date=now.strftime("%Y-%m-%d"),
    ))

    print("--- Legal Hold Registered ---")
    print(f"  Hold ID: HOLD-2026-0023")
    print(f"  Matter: Regulatory inquiry RA-2026-CH-0089")
    print()

    # Run lifecycle scan
    scan_results = engine.run_lifecycle_scan(now)
    print("--- Lifecycle Scan Results ---")
    print(f"  Records Scanned: {scan_results['records_scanned']}")
    print(f"  Records Deleted: {scan_results['records_deleted']}")
    print(f"  Records Archived: {scan_results['records_archived']}")
    print(f"  Records Held: {scan_results['records_held']}")
    print(f"  Records Retained: {scan_results['records_retained']}")
    print(f"  Overdue Records: {scan_results['overdue_records']}")
    print()

    for action in scan_results["actions"]:
        print(f"  Action: {action['record_id']} -> {action['action']} ({action['data_category']})")
        if "hold_id" in action:
            print(f"    Hold: {action['hold_id']}")
        if "reason" in action:
            print(f"    Reason: {action['reason']}")
    print()

    # Release legal hold and run catch-up
    print("--- Releasing Legal Hold ---")
    release = engine.release_legal_hold("HOLD-2026-0023", "Dr. Eva Hartmann / Dr. Lukas Meier (dual approval)")
    print(f"  Records released: {release['records_released']}")
    print()

    # Run catch-up scan
    catchup = engine.run_lifecycle_scan(now)
    print("--- Catch-Up Scan After Hold Release ---")
    print(f"  Records Deleted: {catchup['records_deleted']}")
    print(f"  Records Archived: {catchup['records_archived']}")
    print()

    # Print retention report
    report = engine.get_retention_report()
    print("--- Retention Report ---")
    print(f"  Active Records: {report['total_active_records']}")
    print(f"  Deleted Records: {report['total_deleted_records']}")
    print(f"  Held Records: {report['total_held_records']}")
    print(f"  Active Holds: {report['active_legal_holds']}")
    print(f"  By Tier: {json.dumps(report['by_tier'], indent=4)}")


if __name__ == "__main__":
    run_example()
