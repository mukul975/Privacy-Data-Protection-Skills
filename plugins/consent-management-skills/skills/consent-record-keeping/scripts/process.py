#!/usr/bin/env python3
"""
Consent Record-Keeping System

Implements immutable consent record storage with chain hashing,
Kantara Consent Receipt generation, and audit integrity verification
per GDPR Article 7(1) requirements.
"""

import json
import hashlib
import uuid
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class ConsentRecord:
    """An immutable consent decision record per Art. 7(1)."""
    consent_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    subject_id: str = ""
    purpose_id: str = ""
    purpose_description: str = ""
    decision: str = "granted"
    mechanism: str = "checkbox_tick"
    consent_text_version: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    session_id: Optional[str] = None
    source: str = "signup_flow"
    controller_name: str = "CloudVault SaaS Inc."
    record_hash: str = ""
    previous_hash: Optional[str] = None

    def compute_hash(self, previous_hash: Optional[str] = None) -> str:
        """Compute SHA-256 hash for tamper-evident chain."""
        self.previous_hash = previous_hash
        payload = (
            f"{self.consent_id}:{self.subject_id}:{self.purpose_id}:"
            f"{self.decision}:{self.timestamp}:{self.consent_text_version}:"
            f"{self.previous_hash or 'genesis'}"
        )
        self.record_hash = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        return self.record_hash

    def to_dict(self) -> dict:
        return asdict(self)


def generate_kantara_receipt(record: ConsentRecord, consent_text: str) -> dict:
    """
    Generate a Kantara Initiative Consent Receipt (v1.1.0) from a consent record.

    Args:
        record: The consent decision record.
        consent_text: The full consent text that was displayed.

    Returns:
        Kantara-formatted consent receipt dictionary.
    """
    return {
        "version": "KI-CR-v1.1.0",
        "jurisdiction": "EU/GDPR",
        "consentTimestamp": record.timestamp,
        "collectionMethod": f"web form ({record.mechanism.replace('_', ' ')})",
        "consentReceiptID": f"cr_{record.consent_id}",
        "language": "en",
        "piiPrincipalId": record.subject_id,
        "piiControllers": [
            {
                "piiController": "CloudVault SaaS Inc.",
                "onBehalf": False,
                "contact": "42 Innovation Drive, Dublin, D02 YX88, Ireland",
                "phone": "+353-1-555-0142",
                "email": "privacy@cloudvault-saas.eu",
                "piiControllerUrl": "https://cloudvault-saas.eu",
            }
        ],
        "policyUrl": "https://cloudvault-saas.eu/privacy-policy",
        "services": [
            {
                "service": "CloudVault Cloud Storage",
                "purposes": [
                    {
                        "purpose": record.purpose_description,
                        "purposeId": record.purpose_id,
                        "consentType": "explicit",
                        "termination": "https://app.cloudvault-saas.eu/settings/privacy",
                        "thirdPartyDisclosure": "benchmarking" in record.purpose_id.lower(),
                    }
                ],
            }
        ],
        "sensitive": False,
        "spiCat": [],
        "consentText": consent_text,
        "consentTextHash": record.consent_text_version,
    }


class ConsentRecordStore:
    """
    Append-only consent record store with chain integrity.
    """

    def __init__(self):
        self.records: list[ConsentRecord] = []
        self.text_versions: dict[str, dict] = {}

    def register_consent_text(self, purpose_id: str, text: str, approved_by: str) -> str:
        """Register a consent text version and return its hash."""
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        self.text_versions[text_hash] = {
            "purpose_id": purpose_id,
            "text": text,
            "text_hash": text_hash,
            "approved_by": approved_by,
            "effective_from": datetime.now(timezone.utc).isoformat(),
        }
        return text_hash

    def append_record(self, record: ConsentRecord) -> ConsentRecord:
        """Append a consent record to the immutable store."""
        # Get the last record's hash for chain linking
        subject_records = [r for r in self.records if r.subject_id == record.subject_id]
        previous_hash = subject_records[-1].record_hash if subject_records else None

        record.compute_hash(previous_hash)
        self.records.append(record)
        return record

    def get_subject_records(self, subject_id: str) -> list[ConsentRecord]:
        """Get all consent records for a subject."""
        return [r for r in self.records if r.subject_id == subject_id]

    def get_current_state(self, subject_id: str) -> dict[str, str]:
        """Get current consent state per purpose for a subject."""
        state: dict[str, str] = {}
        for r in self.records:
            if r.subject_id == subject_id:
                state[r.purpose_id] = r.decision
        return state

    def verify_chain_integrity(self, subject_id: str) -> dict:
        """
        Verify the integrity of the record chain for a subject.

        Returns:
            Verification report with chain status.
        """
        subject_records = self.get_subject_records(subject_id)
        if not subject_records:
            return {"subject_id": subject_id, "status": "no_records", "verified": True}

        results = []
        for i, record in enumerate(subject_records):
            expected_previous = subject_records[i - 1].record_hash if i > 0 else None

            # Recompute hash
            payload = (
                f"{record.consent_id}:{record.subject_id}:{record.purpose_id}:"
                f"{record.decision}:{record.timestamp}:{record.consent_text_version}:"
                f"{expected_previous or 'genesis'}"
            )
            expected_hash = hashlib.sha256(payload.encode("utf-8")).hexdigest()

            is_valid = (
                record.record_hash == expected_hash
                and record.previous_hash == expected_previous
            )

            results.append({
                "consent_id": record.consent_id,
                "position": i,
                "stored_hash": record.record_hash[:16] + "...",
                "computed_hash": expected_hash[:16] + "...",
                "hash_valid": record.record_hash == expected_hash,
                "chain_valid": record.previous_hash == expected_previous,
                "overall_valid": is_valid,
            })

        all_valid = all(r["overall_valid"] for r in results)

        return {
            "subject_id": subject_id,
            "total_records": len(results),
            "all_valid": all_valid,
            "status": "intact" if all_valid else "broken",
            "details": results,
        }

    def audit_completeness(self, start_date: str, end_date: str) -> dict:
        """
        Audit record completeness for a date range.

        Checks all mandatory fields are populated per Art. 7(1).
        """
        period_records = [
            r for r in self.records
            if start_date <= r.timestamp <= end_date
        ]

        mandatory_fields = [
            "consent_id", "subject_id", "purpose_id", "purpose_description",
            "decision", "mechanism", "consent_text_version", "timestamp",
            "source", "controller_name",
        ]

        field_completeness: dict[str, int] = {f: 0 for f in mandatory_fields}
        incomplete_records = []

        for record in period_records:
            record_dict = record.to_dict()
            missing = []
            for f in mandatory_fields:
                if record_dict.get(f):
                    field_completeness[f] += 1
                else:
                    missing.append(f)
            if missing:
                incomplete_records.append({
                    "consent_id": record.consent_id,
                    "missing_fields": missing,
                })

        total = len(period_records)
        return {
            "period": {"start": start_date, "end": end_date},
            "total_records": total,
            "field_completeness": {
                f: {"populated": count, "total": total, "rate": round(count / total * 100, 1) if total > 0 else 0}
                for f, count in field_completeness.items()
            },
            "incomplete_records": incomplete_records,
            "overall_completeness": round(
                sum(field_completeness.values()) / (total * len(mandatory_fields)) * 100, 1
            ) if total > 0 else 0,
        }


if __name__ == "__main__":
    store = ConsentRecordStore()

    # Register consent text versions
    analytics_hash = store.register_consent_text(
        "pur_analytics_001",
        "I allow CloudVault SaaS Inc. to analyze my file usage patterns (file sizes, types, and access frequency) to provide personalized storage optimization recommendations. I can withdraw this consent anytime in Settings > Privacy.",
        "Marta Kowalski, DPO",
    )

    marketing_hash = store.register_consent_text(
        "pur_marketing_002",
        "I allow CloudVault SaaS Inc. to send me emails about product updates and new features, no more than twice per month. I can unsubscribe from any email or withdraw consent in Settings > Privacy.",
        "Marta Kowalski, DPO",
    )

    subject = "usr_7f3a9b2e-41d8-4c76-b5e3-9a8d1c2f4e60"

    # Record consent decisions
    r1 = store.append_record(ConsentRecord(
        subject_id=subject,
        purpose_id="pur_analytics_001",
        purpose_description="Service Improvement Analytics",
        decision="granted",
        mechanism="checkbox_tick",
        consent_text_version=analytics_hash,
        source="signup_flow",
        ip_address="198.51.100.42",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    ))

    r2 = store.append_record(ConsentRecord(
        subject_id=subject,
        purpose_id="pur_marketing_002",
        purpose_description="Product Update Emails",
        decision="granted",
        mechanism="checkbox_tick",
        consent_text_version=marketing_hash,
        source="signup_flow",
        ip_address="198.51.100.42",
    ))

    r3 = store.append_record(ConsentRecord(
        subject_id=subject,
        purpose_id="pur_marketing_002",
        purpose_description="Product Update Emails",
        decision="withdrawn",
        mechanism="toggle_switch",
        consent_text_version=marketing_hash,
        source="preference_center",
        ip_address="198.51.100.42",
    ))

    # Display records
    print("=== Consent Records ===")
    for r in store.get_subject_records(subject):
        print(f"  {r.purpose_id}: {r.decision} via {r.source} ({r.mechanism})")
        print(f"    Hash: {r.record_hash[:32]}...")

    # Verify chain integrity
    print("\n=== Chain Integrity Verification ===")
    integrity = store.verify_chain_integrity(subject)
    print(f"  Status: {integrity['status']}")
    print(f"  Records: {integrity['total_records']}")
    for d in integrity["details"]:
        status = "VALID" if d["overall_valid"] else "BROKEN"
        print(f"    Record {d['position']}: {status}")

    # Generate Kantara receipt
    print("\n=== Kantara Consent Receipt (first record) ===")
    receipt = generate_kantara_receipt(
        r1,
        store.text_versions[analytics_hash]["text"],
    )
    print(json.dumps(receipt, indent=2)[:500] + "...")

    # Audit completeness
    print("\n=== Completeness Audit ===")
    audit = store.audit_completeness("2026-01-01T00:00:00Z", "2026-12-31T23:59:59Z")
    print(f"  Overall Completeness: {audit['overall_completeness']}%")
    print(f"  Total Records: {audit['total_records']}")
