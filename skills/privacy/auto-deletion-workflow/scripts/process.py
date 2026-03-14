"""
Automated Data Deletion Workflow Process
Implements deletion orchestration for retention expiry and Art. 17 erasure requests.
"""

import json
import hashlib
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional


class DeletionTrigger(Enum):
    RETENTION_EXPIRY = "retention_expiry"
    ART17_ERASURE = "art17_erasure"
    CONSENT_WITHDRAWAL = "consent_withdrawal"
    ACCOUNT_CLOSURE = "account_closure"
    PURPOSE_COMPLETION = "purpose_completion"
    LEGAL_HOLD_RELEASE = "legal_hold_release"


class DeletionPriority(Enum):
    STANDARD = "standard"
    HIGH = "high"
    URGENT = "urgent"


class DeletionStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    PARTIAL = "partial"
    FAILED = "failed"
    HELD = "held"


class SystemDeletionResult:
    """Result of deletion from a single system."""

    def __init__(
        self,
        system_name: str,
        records_deleted: int,
        action: str,
        status: DeletionStatus,
        timestamp: Optional[datetime] = None,
        error_message: Optional[str] = None,
    ):
        self.system_name = system_name
        self.records_deleted = records_deleted
        self.action = action
        self.status = status
        self.timestamp = timestamp or datetime.utcnow()
        self.error_message = error_message

    def to_dict(self) -> dict:
        result = {
            "system_name": self.system_name,
            "records_deleted": self.records_deleted,
            "action": self.action,
            "status": self.status.value,
            "timestamp": self.timestamp.isoformat(),
        }
        if self.error_message:
            result["error_message"] = self.error_message
        return result


class DeletionJob:
    """Represents a single deletion job for one data subject or data batch."""

    def __init__(
        self,
        trigger: DeletionTrigger,
        data_subject_hash: str,
        data_categories: list[str],
        priority: DeletionPriority = DeletionPriority.STANDARD,
    ):
        self.reference = f"DEL-{datetime.utcnow().strftime('%Y')}-{hash(data_subject_hash) % 10000:04d}"
        self.trigger = trigger
        self.data_subject_hash = data_subject_hash
        self.data_categories = data_categories
        self.priority = priority
        self.status = DeletionStatus.PENDING
        self.created_at = datetime.utcnow()
        self.completed_at: Optional[datetime] = None
        self.system_results: list[SystemDeletionResult] = []
        self.exceptions_applied: list[dict] = []
        self.third_party_notifications: list[dict] = []

    def add_system_result(self, result: SystemDeletionResult) -> None:
        self.system_results.append(result)

    def add_exception(self, category: str, exception_basis: str, retention_until: str) -> None:
        self.exceptions_applied.append({
            "category": category,
            "exception_basis": exception_basis,
            "retention_until": retention_until,
        })

    def add_third_party_notification(
        self, processor_name: str, notified_date: str, confirmed_date: Optional[str] = None
    ) -> None:
        self.third_party_notifications.append({
            "processor_name": processor_name,
            "notified_date": notified_date,
            "confirmed_date": confirmed_date,
            "status": "confirmed" if confirmed_date else "pending",
        })

    def complete(self) -> None:
        self.completed_at = datetime.utcnow()
        failed = [r for r in self.system_results if r.status == DeletionStatus.FAILED]
        if failed:
            self.status = DeletionStatus.PARTIAL
        else:
            self.status = DeletionStatus.COMPLETED

    def generate_confirmation_record(self) -> dict:
        """Generate an immutable deletion confirmation record."""
        record = {
            "reference": self.reference,
            "trigger": self.trigger.value,
            "data_subject_reference": self.data_subject_hash,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "status": self.status.value,
            "systems_processed": [r.to_dict() for r in self.system_results],
            "exceptions_applied": self.exceptions_applied,
            "third_party_notifications": self.third_party_notifications,
            "verification_hash": self._compute_verification_hash(),
        }
        return record

    def _compute_verification_hash(self) -> str:
        """Compute a SHA-256 hash of the confirmation record for integrity verification."""
        data = json.dumps({
            "reference": self.reference,
            "data_subject_reference": self.data_subject_hash,
            "systems": [r.to_dict() for r in self.system_results],
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
        }, sort_keys=True)
        return hashlib.sha256(data.encode()).hexdigest()


def check_litigation_hold(data_subject_hash: str, hold_register: list[dict]) -> Optional[dict]:
    """Check if a data subject's data is under litigation hold."""
    for hold in hold_register:
        if hold.get("status") == "active":
            if data_subject_hash in hold.get("affected_data_subjects", []):
                return hold
    return None


def check_retention_exception(data_category: str, exception_register: list[dict]) -> Optional[dict]:
    """Check if a data category has an active retention exception."""
    for exception in exception_register:
        if exception.get("status") == "active" and exception.get("data_category") == data_category:
            expiry = datetime.fromisoformat(exception["extended_deletion_date"])
            if datetime.utcnow() < expiry:
                return exception
    return None


def resolve_dependencies(
    primary_entity: str,
    dependency_map: list[dict],
) -> list[dict]:
    """
    Resolve cascading deletion dependencies using depth-first traversal.
    Returns an ordered list of entities to delete (deepest first).
    """
    deletion_order = []
    visited = set()

    def _traverse(entity: str, depth: int) -> None:
        if entity in visited:
            return
        visited.add(entity)
        dependents = [
            dep for dep in dependency_map if dep["primary_entity"] == entity
        ]
        for dep in dependents:
            _traverse(dep["dependent_entity"], depth + 1)
        deletion_order.append({"entity": entity, "depth": depth})

    _traverse(primary_entity, 0)
    deletion_order.sort(key=lambda x: x["depth"], reverse=True)
    return deletion_order


def build_dependency_map() -> list[dict]:
    """Build the default dependency map for Orion Data Vault Corp."""
    return [
        {"primary_entity": "Customer", "dependent_entity": "Orders", "relationship": "1:N", "action": "cascade_delete", "retention_override": "6 years — HMRC"},
        {"primary_entity": "Customer", "dependent_entity": "Support Tickets", "relationship": "1:N", "action": "cascade_delete", "retention_override": "3 years"},
        {"primary_entity": "Customer", "dependent_entity": "Consent Records", "relationship": "1:N", "action": "cascade_delete", "retention_override": None},
        {"primary_entity": "Customer", "dependent_entity": "Marketing Preferences", "relationship": "1:1", "action": "cascade_delete", "retention_override": None},
        {"primary_entity": "Customer", "dependent_entity": "Account Audit Log", "relationship": "1:N", "action": "anonymize", "retention_override": "7 years"},
        {"primary_entity": "Orders", "dependent_entity": "Order Lines", "relationship": "1:N", "action": "cascade_delete", "retention_override": None},
        {"primary_entity": "Orders", "dependent_entity": "Payment Records", "relationship": "1:N", "action": "anonymize", "retention_override": "6 years"},
        {"primary_entity": "Orders", "dependent_entity": "Invoices", "relationship": "1:N", "action": "anonymize", "retention_override": "6 years"},
    ]


def generate_deletion_metrics(jobs: list[DeletionJob]) -> dict:
    """Generate deletion metrics for quarterly compliance reporting."""
    total = len(jobs)
    completed = sum(1 for j in jobs if j.status == DeletionStatus.COMPLETED)
    partial = sum(1 for j in jobs if j.status == DeletionStatus.PARTIAL)
    failed = sum(1 for j in jobs if j.status == DeletionStatus.FAILED)
    held = sum(1 for j in jobs if j.status == DeletionStatus.HELD)

    trigger_breakdown = {}
    for job in jobs:
        trigger = job.trigger.value
        trigger_breakdown[trigger] = trigger_breakdown.get(trigger, 0) + 1

    return {
        "report_date": datetime.utcnow().isoformat(),
        "organization": "Orion Data Vault Corp",
        "total_jobs": total,
        "completed": completed,
        "partial": partial,
        "failed": failed,
        "held": held,
        "completion_rate": f"{(completed / total * 100):.1f}%" if total > 0 else "N/A",
        "trigger_breakdown": trigger_breakdown,
    }


if __name__ == "__main__":
    ds_hash = hashlib.sha256(b"ds-20251201-orion-crm-4827").hexdigest()[:16]
    job = DeletionJob(
        trigger=DeletionTrigger.RETENTION_EXPIRY,
        data_subject_hash=f"DS-HASH-{ds_hash}",
        data_categories=["CAT-002", "CAT-003", "CAT-009"],
    )
    job.add_system_result(SystemDeletionResult("CRM", 1, "hard_delete", DeletionStatus.COMPLETED))
    job.add_system_result(SystemDeletionResult("ERP", 47, "hard_delete", DeletionStatus.COMPLETED))
    job.add_system_result(SystemDeletionResult("Data Warehouse", 312, "hard_delete", DeletionStatus.COMPLETED))
    job.add_exception("Invoices", "Art. 17(3)(b) — HMRC statutory retention", "2032-03-14")
    job.add_third_party_notification("Analytics SaaS", "2026-03-14", "2026-03-16")
    job.complete()

    record = job.generate_confirmation_record()
    print(json.dumps(record, indent=2))
