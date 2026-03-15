"""
Backup Retention and Erasure Management Process
Manages backup data under retention schedules, suppression lists, and restore-and-delete procedures.
"""

import json
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional


class BackupTier(Enum):
    DAILY_INCREMENTAL = "daily_incremental"
    WEEKLY_FULL = "weekly_full"
    MONTHLY_FULL = "monthly_full"
    QUARTERLY_ARCHIVE = "quarterly_archive"
    ANNUAL_ARCHIVE = "annual_archive"


class ErasureAction(Enum):
    AWAIT_ROTATION = "await_rotation"
    RESTORE_AND_DELETE = "restore_and_delete"
    BEYOND_USE = "beyond_use_controls"


BACKUP_RETENTION_CONFIG = {
    BackupTier.DAILY_INCREMENTAL: {"retention_days": 30, "rotation_cycle": "Oldest daily deleted after 30 days"},
    BackupTier.WEEKLY_FULL: {"retention_days": 90, "rotation_cycle": "Oldest weekly deleted after 90 days"},
    BackupTier.MONTHLY_FULL: {"retention_days": 365, "rotation_cycle": "Oldest monthly deleted after 12 months"},
    BackupTier.QUARTERLY_ARCHIVE: {"retention_days": 730, "rotation_cycle": "Oldest quarterly deleted after 24 months"},
    BackupTier.ANNUAL_ARCHIVE: {"retention_days": 2555, "rotation_cycle": "Oldest annual deleted after 7 years"},
}


class SuppressionList:
    """Manages the suppression list for data subjects deleted from primary systems."""

    def __init__(self):
        self.entries: list[dict] = []

    def add_entry(
        self,
        data_subject_hash: str,
        deletion_date: str,
        erasure_reference: str,
        data_categories: list[str],
    ) -> None:
        """Add a data subject to the suppression list."""
        self.entries.append({
            "data_subject_hash": data_subject_hash,
            "primary_deletion_date": deletion_date,
            "erasure_reference": erasure_reference,
            "data_categories": data_categories,
            "added_at": datetime.utcnow().isoformat(),
        })

    def check(self, data_subject_hash: str) -> Optional[dict]:
        """Check if a data subject is on the suppression list."""
        for entry in self.entries:
            if entry["data_subject_hash"] == data_subject_hash:
                return entry
        return None

    def get_entries_since(self, since_date: str) -> list[dict]:
        """Get all entries added since a specific date (for restoration compliance)."""
        since = datetime.fromisoformat(since_date)
        return [
            e for e in self.entries
            if datetime.fromisoformat(e["added_at"]) >= since
        ]

    def export(self) -> dict:
        return {
            "suppression_list": self.entries,
            "total_entries": len(self.entries),
            "exported_at": datetime.utcnow().isoformat(),
        }


class BackupErasureManager:
    """Manages erasure obligations for backup systems."""

    def __init__(self, suppression_list: SuppressionList):
        self.suppression_list = suppression_list
        self.pending_actions: list[dict] = []

    def assess_backup_erasure(
        self,
        data_subject_hash: str,
        erasure_reference: str,
        backup_tiers_affected: list[BackupTier],
    ) -> dict:
        """
        Assess the erasure approach for a data subject's data in backup systems.
        Returns the recommended action for each affected backup tier.
        """
        assessments = []

        for tier in backup_tiers_affected:
            config = BACKUP_RETENTION_CONFIG[tier]
            days_to_rotation = config["retention_days"]  # Simplified — actual would check backup date

            if days_to_rotation <= 90:
                action = ErasureAction.AWAIT_ROTATION
                timeline = f"Expected deletion within {days_to_rotation} days via rotation"
            else:
                action = ErasureAction.RESTORE_AND_DELETE
                timeline = "Restore-and-delete recommended (rotation > 90 days)"

            assessments.append({
                "backup_tier": tier.value,
                "retention_days": config["retention_days"],
                "action": action.value,
                "timeline": timeline,
                "interim_controls": "Beyond-use controls applied",
            })

        self.pending_actions.append({
            "data_subject_hash": data_subject_hash,
            "erasure_reference": erasure_reference,
            "assessments": assessments,
            "created_at": datetime.utcnow().isoformat(),
        })

        return {
            "erasure_reference": erasure_reference,
            "data_subject_hash": data_subject_hash,
            "backup_assessments": assessments,
        }

    def generate_restore_and_delete_plan(
        self,
        backup_tier: BackupTier,
        backup_date: str,
        data_subject_hash: str,
        estimated_size_gb: float,
    ) -> dict:
        """Generate a restore-and-delete execution plan."""
        return {
            "procedure": "BKP-RAD-001",
            "organization": "Orion Data Vault Corp",
            "backup_tier": backup_tier.value,
            "backup_date": backup_date,
            "data_subject_hash": data_subject_hash,
            "estimated_backup_size_gb": estimated_size_gb,
            "steps": [
                {"step": 1, "action": "Identify relevant backup sets", "estimated_hours": 1},
                {"step": 2, "action": "Provision isolated restore environment", "estimated_hours": 2},
                {"step": 3, "action": "Restore backup to isolated environment", "estimated_hours": max(1, estimated_size_gb / 100)},
                {"step": 4, "action": "Execute granular deletion of data subject records", "estimated_hours": 1},
                {"step": 5, "action": "Create replacement backup", "estimated_hours": max(1, estimated_size_gb / 100)},
                {"step": 6, "action": "Destroy original backup", "estimated_hours": 1},
                {"step": 7, "action": "Decommission restore environment", "estimated_hours": 1},
                {"step": 8, "action": "Documentation and confirmation", "estimated_hours": 1},
            ],
            "estimated_total_hours": 8 + max(2, estimated_size_gb / 50),
            "estimated_business_days": max(5, int(estimated_size_gb / 200) + 5),
            "prerequisites": [
                "Primary system deletion confirmed complete",
                "Backup granular deletion confirmed infeasible",
                "DPO has approved restore-and-delete",
                "Isolated network segment available",
                "Sufficient temporary storage provisioned",
            ],
        }

    def check_restoration_compliance(self, backup_date: str) -> dict:
        """
        Check what suppression list entries must be applied after restoring
        a backup from a given date.
        """
        entries = self.suppression_list.get_entries_since(backup_date)
        return {
            "backup_date": backup_date,
            "data_subjects_to_re_delete": len(entries),
            "entries": entries,
            "action_required": len(entries) > 0,
            "instruction": (
                "Run automated deletion script against these data subject hashes "
                "immediately after restoration completes."
                if entries else "No re-deletion required."
            ),
        }


def audit_backup_retention_alignment(
    data_categories: list[dict],
    backup_config: dict,
) -> list[dict]:
    """
    Audit whether backup retention periods align with data category retention periods.
    """
    findings = []

    for tier, config in backup_config.items():
        backup_days = config["retention_days"]
        for category in data_categories:
            cat_days = category["retention_period_days"]
            if backup_days > cat_days:
                findings.append({
                    "finding": "COMPLIANCE_GAP",
                    "severity": "HIGH",
                    "backup_tier": tier,
                    "backup_retention_days": backup_days,
                    "data_category": category["name"],
                    "category_retention_days": cat_days,
                    "overshoot_days": backup_days - cat_days,
                    "remediation": (
                        "Segregate this data category into a separate backup set "
                        "with retention matching the category period, or apply "
                        "beyond-use controls for the overshoot period."
                    ),
                })

    if not findings:
        findings.append({
            "finding": "COMPLIANT",
            "severity": "INFO",
            "description": "All backup tiers align with data category retention periods",
        })

    return findings


if __name__ == "__main__":
    suppression = SuppressionList()
    suppression.add_entry("DS-HASH-abc123", "2026-03-10", "DEL-2026-0142", ["CAT-002", "CAT-003"])
    suppression.add_entry("DS-HASH-def456", "2026-03-12", "DEL-2026-0143", ["CAT-002"])

    manager = BackupErasureManager(suppression)

    assessment = manager.assess_backup_erasure(
        "DS-HASH-abc123",
        "DEL-2026-0142",
        [BackupTier.DAILY_INCREMENTAL, BackupTier.WEEKLY_FULL, BackupTier.ANNUAL_ARCHIVE],
    )
    print("Backup erasure assessment:")
    print(json.dumps(assessment, indent=2))

    compliance = manager.check_restoration_compliance("2026-03-01")
    print("\nRestoration compliance check:")
    print(json.dumps(compliance, indent=2))
