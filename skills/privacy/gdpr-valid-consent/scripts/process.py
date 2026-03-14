#!/usr/bin/env python3
"""
GDPR Valid Consent Audit Tool

Audits consent forms and consent records against GDPR Article 7 conditions,
Article 4(11) definition, and EDPB Guidelines 05/2020.
"""

import json
import hashlib
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class ConsentRecord:
    """Represents a single consent receipt per GDPR Article 7(1) requirements."""
    subject_id: str
    purpose_id: str
    purpose_description: str
    decision: str  # "granted" or "not_granted"
    mechanism: str  # "checkbox_tick", "toggle_switch", "typed_statement", "signature"
    consent_text_version: str
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    controller_name: str = "CloudVault SaaS Inc."
    controller_address: str = "42 Innovation Drive, Dublin, D02 YX88, Ireland"

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)


def compute_consent_text_version(consent_text: str) -> str:
    """Generate SHA-256 hash of consent text for version tracking per Art. 7(1)."""
    return hashlib.sha256(consent_text.encode("utf-8")).hexdigest()


AUDIT_CHECKLIST = [
    {
        "id": 1,
        "item": "Consent is separated from terms of service",
        "gdpr_reference": "Art. 7(2)",
        "criteria": "Consent request is clearly distinguishable from other matters",
    },
    {
        "id": 2,
        "item": "No pre-ticked boxes or default-on toggles",
        "gdpr_reference": "Art. 4(11), Recital 32, CJEU C-673/17",
        "criteria": "All consent mechanisms start in the off state",
    },
    {
        "id": 3,
        "item": "Granular consent per purpose",
        "gdpr_reference": "Recital 32, EDPB Guidelines 05/2020",
        "criteria": "Separate opt-in for each distinct processing purpose",
    },
    {
        "id": 4,
        "item": "Controller identity stated",
        "gdpr_reference": "Art. 7(2), Art. 13(1)(a)",
        "criteria": "Full legal name and contact details of data controller visible",
    },
    {
        "id": 5,
        "item": "Purpose clearly described",
        "gdpr_reference": "Art. 13(1)(c)",
        "criteria": "Each purpose described in plain language without legal jargon",
    },
    {
        "id": 6,
        "item": "Data types specified",
        "gdpr_reference": "Art. 13(1)(d)",
        "criteria": "Categories of personal data listed for each purpose",
    },
    {
        "id": 7,
        "item": "Third-party recipients named",
        "gdpr_reference": "Art. 13(1)(e)",
        "criteria": "Specific third parties identified by name",
    },
    {
        "id": 8,
        "item": "Withdrawal mechanism explained",
        "gdpr_reference": "Art. 7(3)",
        "criteria": "Clear statement that consent can be withdrawn at any time with instructions",
    },
    {
        "id": 9,
        "item": "No detriment for refusal",
        "gdpr_reference": "Art. 7(4), Recital 42",
        "criteria": "Service access not conditional on optional consent",
    },
    {
        "id": 10,
        "item": "Withdrawal as easy as giving",
        "gdpr_reference": "Art. 7(3)",
        "criteria": "Withdrawal requires equal or fewer steps than initial consent",
    },
    {
        "id": 11,
        "item": "Age verification present",
        "gdpr_reference": "Art. 8",
        "criteria": "Age gate or verification for services directed at children",
    },
    {
        "id": 12,
        "item": "Language is plain and clear",
        "gdpr_reference": "Art. 7(2), Recital 42",
        "criteria": "Flesch-Kincaid grade level 8 or below, no legal jargon",
    },
    {
        "id": 13,
        "item": "Consent records stored",
        "gdpr_reference": "Art. 7(1)",
        "criteria": "Timestamp, version, purpose, mechanism, identity recorded",
    },
    {
        "id": 14,
        "item": "Re-consent mechanism for purpose changes",
        "gdpr_reference": "Art. 13(3)",
        "criteria": "Process exists to obtain fresh consent when purposes change",
    },
    {
        "id": 15,
        "item": "No cookie walls blocking access",
        "gdpr_reference": "EDPB Guidelines 05/2020 para 39",
        "criteria": "Content accessible regardless of cookie consent choices",
    },
]


def run_consent_audit(responses: dict[int, str]) -> dict:
    """
    Run the consent form audit checklist.

    Args:
        responses: Dictionary mapping checklist item ID to "pass", "fail", or "na".

    Returns:
        Audit report dictionary with results and summary.
    """
    results = []
    pass_count = 0
    fail_count = 0
    na_count = 0

    for item in AUDIT_CHECKLIST:
        item_id = item["id"]
        status = responses.get(item_id, "not_assessed")

        if status == "pass":
            pass_count += 1
        elif status == "fail":
            fail_count += 1
        elif status == "na":
            na_count += 1

        results.append({
            "id": item_id,
            "item": item["item"],
            "gdpr_reference": item["gdpr_reference"],
            "criteria": item["criteria"],
            "status": status,
        })

    total_applicable = pass_count + fail_count
    compliance_rate = (pass_count / total_applicable * 100) if total_applicable > 0 else 0.0

    return {
        "audit_date": datetime.now(timezone.utc).isoformat(),
        "controller": "CloudVault SaaS Inc.",
        "results": results,
        "summary": {
            "total_items": len(AUDIT_CHECKLIST),
            "passed": pass_count,
            "failed": fail_count,
            "not_applicable": na_count,
            "not_assessed": len(AUDIT_CHECKLIST) - pass_count - fail_count - na_count,
            "compliance_rate_percent": round(compliance_rate, 1),
        },
    }


def validate_consent_record(record: dict) -> list[str]:
    """
    Validate a consent record contains all fields required by Art. 7(1).

    Returns:
        List of validation errors. Empty list means the record is valid.
    """
    required_fields = [
        "subject_id",
        "purpose_id",
        "purpose_description",
        "decision",
        "mechanism",
        "consent_text_version",
        "timestamp",
        "controller_name",
    ]

    errors = []

    for f in required_fields:
        if f not in record or not record[f]:
            errors.append(f"Missing required field: {f}")

    if record.get("decision") not in ("granted", "not_granted"):
        errors.append("Field 'decision' must be 'granted' or 'not_granted'")

    valid_mechanisms = {"checkbox_tick", "toggle_switch", "typed_statement", "signature"}
    if record.get("mechanism") not in valid_mechanisms:
        errors.append(f"Field 'mechanism' must be one of: {', '.join(sorted(valid_mechanisms))}")

    if record.get("timestamp"):
        try:
            datetime.fromisoformat(record["timestamp"])
        except ValueError:
            errors.append("Field 'timestamp' must be ISO 8601 format")

    if record.get("consent_text_version"):
        version = record["consent_text_version"]
        if len(version) != 64 or not all(c in "0123456789abcdef" for c in version):
            errors.append("Field 'consent_text_version' must be a valid SHA-256 hex digest")

    return errors


if __name__ == "__main__":
    # Demonstrate consent record creation
    consent_text = (
        "I agree to allow CloudVault SaaS Inc. to analyze my file usage patterns "
        "to provide personalized storage optimization recommendations. This involves "
        "processing file metadata (size, type, access frequency) but not file contents. "
        "I can withdraw this consent at any time from my Account Settings page."
    )

    version_hash = compute_consent_text_version(consent_text)

    record = ConsentRecord(
        subject_id="usr_7f3a9b2e-41d8-4c76-b5e3-9a8d1c2f4e60",
        purpose_id="purpose_service_improvement_analytics",
        purpose_description="Analyze file usage patterns for storage optimization recommendations",
        decision="granted",
        mechanism="checkbox_tick",
        consent_text_version=version_hash,
        ip_address="198.51.100.42",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    )

    print("=== Consent Record ===")
    print(record.to_json())

    print("\n=== Validation ===")
    validation_errors = validate_consent_record(record.to_dict())
    if not validation_errors:
        print("Record is valid per Art. 7(1) requirements.")
    else:
        for err in validation_errors:
            print(f"  ERROR: {err}")

    # Demonstrate audit
    print("\n=== Consent Form Audit ===")
    sample_responses = {
        1: "pass", 2: "pass", 3: "pass", 4: "pass", 5: "pass",
        6: "pass", 7: "fail", 8: "pass", 9: "pass", 10: "fail",
        11: "na", 12: "pass", 13: "pass", 14: "pass", 15: "pass",
    }
    report = run_consent_audit(sample_responses)
    print(f"Compliance Rate: {report['summary']['compliance_rate_percent']}%")
    print(f"Passed: {report['summary']['passed']}, Failed: {report['summary']['failed']}, "
          f"N/A: {report['summary']['not_applicable']}")

    failed_items = [r for r in report["results"] if r["status"] == "fail"]
    if failed_items:
        print("\nFailed Items:")
        for item in failed_items:
            print(f"  #{item['id']}: {item['item']} ({item['gdpr_reference']})")
