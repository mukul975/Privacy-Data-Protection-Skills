#!/usr/bin/env python3
"""
Vendor Termination Data — Return and Deletion Management Engine

Implements data return tracking, deletion verification, certification
management, and transition planning per GDPR Article 28(3)(g).
"""

import json
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class TerminationTrigger(Enum):
    CONTRACT_EXPIRY = "contract_expiry"
    CONVENIENCE = "termination_for_convenience"
    CAUSE = "termination_for_cause"
    MIGRATION = "service_migration"
    INSOLVENCY = "vendor_insolvency"
    REGULATORY = "regulatory_order"


class DataElection(Enum):
    RETURN = "return_only"
    DELETE = "delete_only"
    RETURN_THEN_DELETE = "return_then_delete"


class TerminationPhase(Enum):
    INITIATED = "initiated"
    SCOPE_CONFIRMED = "scope_confirmed"
    DATA_RETURN_IN_PROGRESS = "data_return_in_progress"
    DATA_RETURN_COMPLETE = "data_return_complete"
    DELETION_IN_PROGRESS = "deletion_in_progress"
    DELETION_COMPLETE = "deletion_complete"
    CERTIFICATION_RECEIVED = "certification_received"
    VERIFIED = "verified"
    CLOSED = "closed"


class DeletionMethod(Enum):
    DATABASE_DELETE = "database_delete_vacuum"
    OBJECT_DELETE = "object_storage_delete"
    SECURE_OVERWRITE = "nist_800_88_clear"
    CRYPTO_ERASE = "crypto_erase"
    PHYSICAL_DESTRUCTION = "physical_destruction"
    CACHE_FLUSH = "cache_flush_ttl"
    LOG_EXPIRY = "log_retention_expiry"


@dataclass
class DataInventoryItem:
    """A data location identified for return/deletion."""
    item_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    data_category: str = ""
    location: str = ""
    data_format: str = ""
    volume: str = ""
    deletion_method: str = ""
    deletion_date: Optional[str] = None
    deletion_verified: bool = False
    legal_retention: bool = False
    legal_retention_basis: str = ""
    legal_retention_until: Optional[str] = None


@dataclass
class DataReturnRecord:
    """Record of data returned to the controller."""
    return_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    data_categories: list[str] = field(default_factory=list)
    format: str = ""
    transfer_method: str = ""
    record_count: int = 0
    checksum: str = ""
    transfer_date: str = ""
    validated: bool = False
    validation_date: Optional[str] = None
    validation_notes: str = ""


@dataclass
class DeletionCertification:
    """Processor's deletion certification document."""
    cert_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    certifying_officer: str = ""
    certifying_title: str = ""
    certification_date: str = ""
    data_locations_covered: list[str] = field(default_factory=list)
    deletion_methods_used: list[str] = field(default_factory=list)
    sub_processors_confirmed: list[str] = field(default_factory=list)
    exceptions: list[dict] = field(default_factory=list)
    accepted: bool = False
    review_notes: str = ""


@dataclass
class VendorTermination:
    """Complete vendor termination data management record."""
    termination_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_id: str = ""
    vendor_name: str = ""
    dpa_reference: str = ""
    trigger: str = TerminationTrigger.CONTRACT_EXPIRY.value
    data_election: str = DataElection.RETURN_THEN_DELETE.value
    phase: str = TerminationPhase.INITIATED.value
    initiated_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    data_inventory: list[dict] = field(default_factory=list)
    data_returns: list[dict] = field(default_factory=list)
    deletion_certification: Optional[dict] = None
    return_deadline: str = ""
    deletion_deadline: str = ""
    certification_deadline: str = ""
    phase_history: list[dict] = field(default_factory=list)
    closed_date: Optional[str] = None


class VendorTerminationEngine:
    """
    Manages the vendor termination data lifecycle including
    data return, deletion tracking, and certification verification.
    """

    def __init__(self, return_days: int = 30, deletion_days: int = 90):
        self.terminations: dict[str, VendorTermination] = {}
        self.return_days = return_days
        self.deletion_days = deletion_days

    def initiate_termination(
        self, vendor_id: str, vendor_name: str, dpa_reference: str,
        trigger: TerminationTrigger, election: DataElection,
    ) -> VendorTermination:
        """Initiate a vendor termination data process."""
        now = datetime.now(timezone.utc)

        term = VendorTermination(
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            dpa_reference=dpa_reference,
            trigger=trigger.value,
            data_election=election.value,
            return_deadline=(now + timedelta(days=self.return_days)).isoformat(),
            deletion_deadline=(now + timedelta(days=self.deletion_days)).isoformat(),
            certification_deadline=(now + timedelta(days=self.deletion_days)).isoformat(),
        )
        term.phase_history.append({
            "phase": TerminationPhase.INITIATED.value,
            "date": now.isoformat(),
        })

        self.terminations[term.termination_id] = term
        return term

    def record_data_inventory(
        self, termination_id: str, items: list[DataInventoryItem]
    ) -> int:
        """Record the data inventory for termination scope."""
        term = self.terminations.get(termination_id)
        if not term:
            raise ValueError(f"Termination {termination_id} not found")

        term.data_inventory = [asdict(item) for item in items]
        self.advance_phase(termination_id, TerminationPhase.SCOPE_CONFIRMED)
        return len(items)

    def record_data_return(
        self, termination_id: str, return_record: DataReturnRecord
    ) -> str:
        """Record a data return event."""
        term = self.terminations.get(termination_id)
        if not term:
            raise ValueError(f"Termination {termination_id} not found")

        term.data_returns.append(asdict(return_record))
        if term.phase == TerminationPhase.SCOPE_CONFIRMED.value:
            self.advance_phase(termination_id, TerminationPhase.DATA_RETURN_IN_PROGRESS)
        return return_record.return_id

    def validate_return(
        self, termination_id: str, return_id: str, valid: bool, notes: str = ""
    ) -> bool:
        """Validate a data return against expected scope."""
        term = self.terminations.get(termination_id)
        if not term:
            raise ValueError(f"Termination {termination_id} not found")

        for r in term.data_returns:
            if r["return_id"] == return_id:
                r["validated"] = valid
                r["validation_date"] = datetime.now(timezone.utc).isoformat()
                r["validation_notes"] = notes
                break

        all_validated = all(r.get("validated") for r in term.data_returns)
        if all_validated and term.data_returns:
            self.advance_phase(termination_id, TerminationPhase.DATA_RETURN_COMPLETE)

        return valid

    def record_deletion_certification(
        self, termination_id: str, cert: DeletionCertification
    ) -> bool:
        """Record and review a deletion certification from the vendor."""
        term = self.terminations.get(termination_id)
        if not term:
            raise ValueError(f"Termination {termination_id} not found")

        # Verify coverage
        inventory_locations = {
            item["location"] for item in term.data_inventory
            if not item.get("legal_retention")
        }
        cert_locations = set(cert.data_locations_covered)

        uncovered = inventory_locations - cert_locations
        if uncovered:
            cert.accepted = False
            cert.review_notes = f"Incomplete — locations not covered: {', '.join(uncovered)}"
        else:
            cert.accepted = True
            cert.review_notes = "All known data locations covered by certification"

        term.deletion_certification = asdict(cert)
        if cert.accepted:
            self.advance_phase(termination_id, TerminationPhase.CERTIFICATION_RECEIVED)

        return cert.accepted

    def advance_phase(self, termination_id: str, new_phase: TerminationPhase) -> str:
        """Advance the termination process to a new phase."""
        term = self.terminations.get(termination_id)
        if not term:
            raise ValueError(f"Termination {termination_id} not found")

        term.phase = new_phase.value
        term.phase_history.append({
            "phase": new_phase.value,
            "date": datetime.now(timezone.utc).isoformat(),
        })

        if new_phase == TerminationPhase.CLOSED:
            term.closed_date = datetime.now(timezone.utc).isoformat()

        return new_phase.value

    def get_termination_summary(self, termination_id: str) -> dict:
        """Generate a termination process summary."""
        term = self.terminations.get(termination_id)
        if not term:
            raise ValueError(f"Termination {termination_id} not found")

        inventory_count = len(term.data_inventory)
        legal_holds = len([i for i in term.data_inventory if i.get("legal_retention")])
        returns_validated = len([r for r in term.data_returns if r.get("validated")])
        cert_accepted = (
            term.deletion_certification.get("accepted") if term.deletion_certification else None
        )

        return {
            "termination_id": term.termination_id,
            "vendor": term.vendor_name,
            "trigger": term.trigger,
            "election": term.data_election,
            "current_phase": term.phase,
            "data_locations_inventoried": inventory_count,
            "legal_retention_holds": legal_holds,
            "data_returns_received": len(term.data_returns),
            "returns_validated": returns_validated,
            "deletion_certification_received": term.deletion_certification is not None,
            "certification_accepted": cert_accepted,
            "return_deadline": term.return_deadline,
            "deletion_deadline": term.deletion_deadline,
            "initiated": term.initiated_date,
            "closed": term.closed_date,
        }


if __name__ == "__main__":
    engine = VendorTerminationEngine(return_days=30, deletion_days=90)

    # Initiate termination for NimbusAnalytics
    term = engine.initiate_termination(
        vendor_id="nimbus-001",
        vendor_name="NimbusAnalytics GmbH",
        dpa_reference="DPA-2026-NA-001",
        trigger=TerminationTrigger.MIGRATION,
        election=DataElection.RETURN_THEN_DELETE,
    )
    print(f"Termination initiated: {term.termination_id}")
    print(f"Return deadline: {term.return_deadline}")
    print(f"Deletion deadline: {term.deletion_deadline}")

    # Record data inventory
    inventory = [
        DataInventoryItem(
            data_category="Customer analytics data",
            location="Primary PostgreSQL database (Frankfurt)",
            data_format="Structured SQL", volume="2.3 GB",
            deletion_method=DeletionMethod.DATABASE_DELETE.value,
        ),
        DataInventoryItem(
            data_category="Analytics event logs",
            location="Elasticsearch cluster (Frankfurt)",
            data_format="JSON documents", volume="15 GB",
            deletion_method=DeletionMethod.DATABASE_DELETE.value,
        ),
        DataInventoryItem(
            data_category="Encrypted backups",
            location="AWS S3 (Frankfurt) — daily backups, 30-day retention",
            data_format="Encrypted backup files", volume="8 GB",
            deletion_method=DeletionMethod.OBJECT_DELETE.value,
        ),
        DataInventoryItem(
            data_category="Application access logs",
            location="CloudWatch Logs (Frankfurt)",
            data_format="Log entries", volume="500 MB",
            deletion_method=DeletionMethod.LOG_EXPIRY.value,
        ),
        DataInventoryItem(
            data_category="Sub-processor data (Elastic Cloud)",
            location="Elastic Cloud B.V. (Amsterdam)",
            data_format="Search indices", volume="3 GB",
            deletion_method=DeletionMethod.DATABASE_DELETE.value,
        ),
    ]
    engine.record_data_inventory(term.termination_id, inventory)

    # Record data return
    return_record = DataReturnRecord(
        data_categories=["customer_analytics", "event_logs"],
        format="CSV + JSONL (gzip compressed)",
        transfer_method="SFTP with PGP encryption",
        record_count=2450000,
        checksum="sha256:a1b2c3d4e5f6...",
        transfer_date=datetime.now(timezone.utc).isoformat(),
    )
    engine.record_data_return(term.termination_id, return_record)
    engine.validate_return(
        term.termination_id, return_record.return_id, True,
        "Record count matches. Checksums verified. Sample review passed."
    )

    # Record deletion certification
    cert = DeletionCertification(
        certifying_officer="Dr. Klaus Weber",
        certifying_title="Data Protection Officer, NimbusAnalytics GmbH",
        certification_date=datetime.now(timezone.utc).isoformat(),
        data_locations_covered=[
            "Primary PostgreSQL database (Frankfurt)",
            "Elasticsearch cluster (Frankfurt)",
            "AWS S3 (Frankfurt) — daily backups, 30-day retention",
            "CloudWatch Logs (Frankfurt)",
            "Elastic Cloud B.V. (Amsterdam)",
        ],
        deletion_methods_used=[
            "Database DELETE + VACUUM (PostgreSQL)",
            "Index deletion (Elasticsearch)",
            "S3 object lifecycle deletion",
            "CloudWatch log group deletion",
            "Sub-processor cascade deletion confirmed",
        ],
        sub_processors_confirmed=["Elastic Cloud B.V."],
        exceptions=[],
    )
    accepted = engine.record_deletion_certification(term.termination_id, cert)
    print(f"\nDeletion certification accepted: {accepted}")

    # Close termination
    engine.advance_phase(term.termination_id, TerminationPhase.CLOSED)

    # Summary
    summary = engine.get_termination_summary(term.termination_id)
    print("\n=== Vendor Termination Summary ===")
    print(json.dumps(summary, indent=2))
