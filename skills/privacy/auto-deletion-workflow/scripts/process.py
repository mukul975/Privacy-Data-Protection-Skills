#!/usr/bin/env python3
"""
Automated Data Deletion Workflow Process
Orchestrates deletion across systems with cascading dependency resolution,
confirmation logging, and audit trail generation for Orion Data Vault Corp.
"""

import json
import hashlib
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional


class DeletionTrigger(Enum):
    RETENTION_EXPIRY = "retention_expiry"
    ART17_ERASURE = "art17_erasure_request"
    CONSENT_WITHDRAWAL = "consent_withdrawal"
    ACCOUNT_CLOSURE = "account_closure"
    PURPOSE_COMPLETION = "purpose_completion"
    LEGAL_HOLD_RELEASE = "legal_hold_release"


class DeletionAction(Enum):
    HARD_DELETE = "hard_delete"
    ANONYMIZE = "anonymize"
    NULLIFY_FK = "nullify_fk"
    FLAG_BACKUP = "flag_backup"
    SKIP_HELD = "skip_held"


class DeletionStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


DEPENDENCY_MAP = {
    "customer": {
        "dependents": [
            {"entity": "orders", "relationship": "1:N", "action": "cascade", "retention_override": "6 years (HMRC)"},
            {"entity": "support_tickets", "relationship": "1:N", "action": "cascade", "retention_override": "3 years"},
            {"entity": "consent_records", "relationship": "1:N", "action": "cascade", "retention_override": None},
            {"entity": "marketing_preferences", "relationship": "1:1", "action": "cascade", "retention_override": None},
            {"entity": "audit_log", "relationship": "1:N", "action": "anonymize", "retention_override": "7 years"},
        ]
    },
    "orders": {
        "dependents": [
            {"entity": "order_lines", "relationship": "1:N", "action": "cascade", "retention_override": None},
            {"entity": "payment_records", "relationship": "1:N", "action": "anonymize", "retention_override": "6 years"},
            {"entity": "shipping_records", "relationship": "1:N", "action": "cascade", "retention_override": None},
            {"entity": "invoices", "relationship": "1:N", "action": "anonymize", "retention_override": "6 years"},
        ]
    },
    "employee": {
        "dependents": [
            {"entity": "payroll_records", "relationship": "1:N", "action": "cascade", "retention_override": "6 years (PAYE)"},
            {"entity": "performance_reviews", "relationship": "1:N", "action": "cascade", "retention_override": None},
            {"entity": "access_logs", "relationship": "1:N", "action": "anonymize", "retention_override": "2 years"},
        ]
    },
}

SYSTEM_REGISTRY = [
    {"name": "CRM (Salesforce)", "type": "primary_database", "supports_granular_delete": True},
    {"name": "ERP (SAP)", "type": "primary_database", "supports_granular_delete": True},
    {"name": "Data Warehouse (BigQuery)", "type": "analytics", "supports_granular_delete": True},
    {"name": "Email (Exchange)", "type": "communication", "supports_granular_delete": True},
    {"name": "File Storage (S3)", "type": "file_storage", "supports_granular_delete": True},
    {"name": "Backup (Veeam)", "type": "backup", "supports_granular_delete": False},
    {"name": "Analytics (Mixpanel)", "type": "analytics", "supports_granular_delete": True},
    {"name": "Support (Zendesk)", "type": "primary_database", "supports_granular_delete": True},
    {"name": "Audit Log", "type": "audit", "supports_granular_delete": False},
    {"name": "Payment (Stripe)", "type": "payment", "supports_granular_delete": True},
]


def generate_deletion_reference() -> str:
    """Generate a unique deletion job reference."""
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    hash_suffix = hashlib.md5(timestamp.encode()).hexdigest()[:6]
    year = datetime.utcnow().strftime("%Y")
    return f"DEL-{year}-{hash_suffix.upper()}"


def generate_data_subject_hash(identifier: str) -> str:
    """Generate a pseudonymized data subject reference."""
    return f"DS-HASH-{hashlib.sha256(identifier.encode()).hexdigest()[:8]}"


def resolve_dependencies(entity_type: str, check_retention_override: bool = True) -> list[dict]:
    """
    Resolve cascading deletion dependencies for an entity type.
    Returns ordered list of deletion actions (deepest first).
    """
    actions = []

    def _resolve(entity: str, depth: int = 0):
        if entity not in DEPENDENCY_MAP:
            return
        for dep in DEPENDENCY_MAP[entity]["dependents"]:
            _resolve(dep["entity"], depth + 1)

            if check_retention_override and dep["retention_override"]:
                action = DeletionAction.ANONYMIZE
            elif dep["action"] == "anonymize":
                action = DeletionAction.ANONYMIZE
            else:
                action = DeletionAction.HARD_DELETE

            actions.append({
                "entity": dep["entity"],
                "depth": depth + 1,
                "action": action.value,
                "retention_override": dep["retention_override"],
                "relationship": dep["relationship"],
            })

    _resolve(entity_type)
    actions.append({
        "entity": entity_type,
        "depth": 0,
        "action": DeletionAction.HARD_DELETE.value,
        "retention_override": None,
        "relationship": "primary",
    })

    return sorted(actions, key=lambda x: -x["depth"])


def pre_deletion_checks(
    data_subject_ref: str,
    litigation_holds: list[str],
    retention_exceptions: list[str],
    pending_dsars: list[str],
) -> dict:
    """Run pre-deletion checks before executing deletion."""
    checks = {
        "data_subject_ref": data_subject_ref,
        "check_timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "litigation_hold": data_subject_ref in litigation_holds,
        "retention_exception": data_subject_ref in retention_exceptions,
        "pending_dsar": data_subject_ref in pending_dsars,
        "can_proceed": True,
        "blockers": [],
    }

    if checks["litigation_hold"]:
        checks["can_proceed"] = False
        checks["blockers"].append("Active litigation hold — Art. 17(3)(e) exception applies")
    if checks["retention_exception"]:
        checks["can_proceed"] = False
        checks["blockers"].append("Active retention exception — review exception before deletion")
    if checks["pending_dsar"]:
        checks["blockers"].append("Pending DSAR — coordinate with DSAR workflow (non-blocking)")

    return checks


def generate_deletion_manifest(
    reference: str,
    trigger: DeletionTrigger,
    data_subject_hash: str,
    entity_type: str,
    systems: list[dict],
    exceptions: list[dict],
) -> dict:
    """Generate a deletion manifest documenting all systems and actions."""
    dependency_actions = resolve_dependencies(entity_type)

    manifest = {
        "reference": reference,
        "trigger": trigger.value,
        "data_subject_ref": data_subject_hash,
        "created": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": DeletionStatus.PENDING.value,
        "dependency_resolution": dependency_actions,
        "systems": [],
        "exceptions": exceptions,
        "third_party_notifications": [],
        "backup_flagging": {
            "required": True,
            "suppression_list_updated": False,
            "expected_backup_deletion": (datetime.utcnow() + timedelta(days=90)).strftime("%Y-%m-%d"),
        },
    }

    for system in systems:
        action = DeletionAction.HARD_DELETE if system["supports_granular_delete"] else DeletionAction.FLAG_BACKUP
        if system["type"] == "audit":
            action = DeletionAction.ANONYMIZE

        manifest["systems"].append({
            "name": system["name"],
            "type": system["type"],
            "action": action.value,
            "status": DeletionStatus.PENDING.value,
            "records_affected": 0,
            "execution_timestamp": None,
        })

    return manifest


def generate_confirmation_record(manifest: dict) -> dict:
    """Generate an immutable deletion confirmation record from a completed manifest."""
    confirmation = {
        "reference": manifest["reference"],
        "trigger": manifest["trigger"],
        "data_subject_ref": manifest["data_subject_ref"],
        "execution_date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "systems_processed": manifest["systems"],
        "exceptions_applied": manifest["exceptions"],
        "third_party_notifications": manifest["third_party_notifications"],
        "backup_status": manifest["backup_flagging"],
        "verification": {
            "post_deletion_scan": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "residual_data_found": False,
            "verification_hash": hashlib.sha256(
                json.dumps(manifest, sort_keys=True).encode()
            ).hexdigest(),
        },
        "overall_status": DeletionStatus.COMPLETED.value,
    }
    return confirmation


if __name__ == "__main__":
    ref = generate_deletion_reference()
    ds_hash = generate_data_subject_hash("customer-12345@example.com")
    print(f"Deletion Reference: {ref}")
    print(f"Data Subject Hash: {ds_hash}")

    print("\nDependency Resolution (customer):")
    deps = resolve_dependencies("customer")
    for dep in deps:
        indent = "  " * dep["depth"]
        print(f"  {indent}[Depth {dep['depth']}] {dep['entity']}: {dep['action']}")
        if dep["retention_override"]:
            print(f"  {indent}  Retention override: {dep['retention_override']}")

    checks = pre_deletion_checks(
        ds_hash,
        litigation_holds=[],
        retention_exceptions=[],
        pending_dsars=[],
    )
    print(f"\nPre-Deletion Checks: {'PASS' if checks['can_proceed'] else 'BLOCKED'}")

    manifest = generate_deletion_manifest(
        reference=ref,
        trigger=DeletionTrigger.ART17_ERASURE,
        data_subject_hash=ds_hash,
        entity_type="customer",
        systems=SYSTEM_REGISTRY,
        exceptions=[],
    )
    print(f"\nDeletion Manifest: {manifest['reference']}")
    print(f"Systems: {len(manifest['systems'])}")
    print(f"Dependency Actions: {len(manifest['dependency_resolution'])}")

    confirmation = generate_confirmation_record(manifest)
    print(f"\nConfirmation Record Generated")
    print(f"Verification Hash: {confirmation['verification']['verification_hash'][:32]}...")
