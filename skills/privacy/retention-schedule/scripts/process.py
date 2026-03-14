#!/usr/bin/env python3
"""
Data Retention Schedule Management Process
Generates, validates, and audits retention schedules for Orion Data Vault Corp.
"""

import json
import hashlib
from datetime import datetime, timedelta
from typing import Optional


RETENTION_CATEGORIES = [
    {
        "category_id": "CAT-001",
        "name": "Employee HR Records",
        "data_elements": ["Name", "Address", "NI number", "Salary", "Performance reviews"],
        "purpose": "Employment administration",
        "legal_basis": "Art. 6(1)(b) Contract + Art. 6(1)(c) Legal obligation",
        "retention_period_years": 6,
        "retention_trigger": "Employment termination date",
        "statutory_basis": "Limitation Act 1980 s.5; Employment Rights Act 1996",
        "review_frequency": "Annual",
    },
    {
        "category_id": "CAT-002",
        "name": "Customer Account Data",
        "data_elements": ["Name", "Email", "Phone", "Address", "Account preferences"],
        "purpose": "Service delivery",
        "legal_basis": "Art. 6(1)(b) Contract",
        "retention_period_years": 2,
        "retention_trigger": "Account closure date",
        "statutory_basis": "Contractual necessity; limitation period buffer",
        "review_frequency": "Annual",
    },
    {
        "category_id": "CAT-003",
        "name": "Customer Transaction Records",
        "data_elements": ["Purchase history", "Payment details", "Invoices"],
        "purpose": "Contract performance and legal obligation",
        "legal_basis": "Art. 6(1)(b) Contract + Art. 6(1)(c) Legal obligation",
        "retention_period_years": 6,
        "retention_trigger": "Transaction completion date",
        "statutory_basis": "HMRC record-keeping; Companies Act 2006 s.386; Limitation Act 1980",
        "review_frequency": "Annual",
    },
    {
        "category_id": "CAT-004",
        "name": "Marketing Contact Data",
        "data_elements": ["Name", "Email", "Consent records", "Campaign interactions"],
        "purpose": "Direct marketing",
        "legal_basis": "Art. 6(1)(a) Consent",
        "retention_period_years": 2,
        "retention_trigger": "Consent withdrawal or 24 months since last engagement",
        "statutory_basis": "Consent-based; deletion upon withdrawal",
        "review_frequency": "Biannual",
    },
    {
        "category_id": "CAT-005",
        "name": "Website Analytics",
        "data_elements": ["IP address", "Device data", "Browsing behaviour", "Cookies"],
        "purpose": "Website optimization",
        "legal_basis": "Art. 6(1)(f) Legitimate interest",
        "retention_period_years": 2,
        "retention_trigger": "Data collection date",
        "statutory_basis": "ICO guidance; CNIL recommendation (26 months)",
        "review_frequency": "Annual",
    },
    {
        "category_id": "CAT-006",
        "name": "Job Applicant Data",
        "data_elements": ["CV", "Cover letter", "Interview notes", "References"],
        "purpose": "Recruitment",
        "legal_basis": "Art. 6(1)(b) Pre-contractual steps",
        "retention_period_years": 0.5,
        "retention_trigger": "Recruitment decision date",
        "statutory_basis": "ICO Employment Practices Code; Equality Act 2010 s.123 (6 months)",
        "review_frequency": "After each recruitment cycle",
    },
    {
        "category_id": "CAT-007",
        "name": "CCTV Footage",
        "data_elements": ["Video recordings of premises"],
        "purpose": "Security and safety",
        "legal_basis": "Art. 6(1)(f) Legitimate interest",
        "retention_period_years": 0.08,
        "retention_trigger": "Recording date",
        "statutory_basis": "ICO CCTV Code of Practice (30 days)",
        "review_frequency": "Monthly",
    },
    {
        "category_id": "CAT-008",
        "name": "Supplier Contact Data",
        "data_elements": ["Name", "Email", "Phone", "Company", "Contract terms"],
        "purpose": "Vendor management",
        "legal_basis": "Art. 6(1)(b) Contract",
        "retention_period_years": 6,
        "retention_trigger": "Contract termination date",
        "statutory_basis": "Limitation Act 1980; contractual necessity",
        "review_frequency": "Annual",
    },
    {
        "category_id": "CAT-009",
        "name": "Customer Support Records",
        "data_elements": ["Tickets", "Correspondence", "Complaint records"],
        "purpose": "Service delivery and quality",
        "legal_basis": "Art. 6(1)(b) Contract + Art. 6(1)(f) Legitimate interest",
        "retention_period_years": 3,
        "retention_trigger": "Case closure date",
        "statutory_basis": "Legitimate interest; limitation period for service-related claims",
        "review_frequency": "Annual",
    },
    {
        "category_id": "CAT-010",
        "name": "Financial and Tax Records",
        "data_elements": ["Accounts", "Tax filings", "Audit reports", "Bank statements"],
        "purpose": "Legal compliance",
        "legal_basis": "Art. 6(1)(c) Legal obligation",
        "retention_period_years": 6,
        "retention_trigger": "End of relevant financial year",
        "statutory_basis": "HMRC requirements; Companies Act 2006 s.388; Limitation Act 1980 s.8",
        "review_frequency": "Annual",
    },
]


def generate_retention_schedule(org_name: str = "Orion Data Vault Corp") -> dict:
    """Generate the complete retention schedule document."""
    schedule = {
        "organization": org_name,
        "generated_date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "version": "1.0",
        "approved_by": "Data Protection Officer",
        "next_review_date": (datetime.utcnow() + timedelta(days=365)).strftime("%Y-%m-%d"),
        "categories": RETENTION_CATEGORIES,
        "total_categories": len(RETENTION_CATEGORIES),
    }
    schedule_json = json.dumps(schedule, sort_keys=True)
    schedule["checksum"] = hashlib.sha256(schedule_json.encode()).hexdigest()[:16]
    return schedule


def calculate_deletion_date(
    trigger_date: str, category_id: str
) -> Optional[str]:
    """Calculate the deletion date for a record based on its category and trigger event."""
    category = next(
        (c for c in RETENTION_CATEGORIES if c["category_id"] == category_id), None
    )
    if not category:
        return None

    trigger = datetime.strptime(trigger_date, "%Y-%m-%d")
    retention_days = int(category["retention_period_years"] * 365.25)
    deletion_date = trigger + timedelta(days=retention_days)
    return deletion_date.strftime("%Y-%m-%d")


def audit_retention_compliance(records: list[dict]) -> dict:
    """
    Audit a list of records for retention compliance.
    Each record should have: category_id, trigger_date, current_status (active/expired).
    """
    today = datetime.utcnow().date()
    results = {
        "audit_date": today.strftime("%Y-%m-%d"),
        "total_records": len(records),
        "compliant": 0,
        "overdue_for_deletion": 0,
        "approaching_expiry": 0,
        "within_retention": 0,
        "overdue_records": [],
        "approaching_records": [],
    }

    for record in records:
        deletion_date_str = calculate_deletion_date(
            record["trigger_date"], record["category_id"]
        )
        if not deletion_date_str:
            continue

        deletion_date = datetime.strptime(deletion_date_str, "%Y-%m-%d").date()
        days_until_deletion = (deletion_date - today).days

        if days_until_deletion < 0 and record.get("current_status") == "active":
            results["overdue_for_deletion"] += 1
            results["overdue_records"].append(
                {
                    "record": record,
                    "deletion_date": deletion_date_str,
                    "days_overdue": abs(days_until_deletion),
                }
            )
        elif 0 <= days_until_deletion <= 30:
            results["approaching_expiry"] += 1
            results["approaching_records"].append(
                {
                    "record": record,
                    "deletion_date": deletion_date_str,
                    "days_remaining": days_until_deletion,
                }
            )
        else:
            results["within_retention"] += 1
            results["compliant"] += 1

    results["compliance_rate"] = (
        round(results["compliant"] / results["total_records"] * 100, 2)
        if results["total_records"] > 0
        else 0
    )
    return results


def generate_retention_justification(
    category_id: str,
    proposed_period_years: float,
    statutory_minimum_years: float,
    justification_text: str,
    data_subjects_affected: int,
    sensitivity: str,
) -> dict:
    """Generate a retention period justification document."""
    category = next(
        (c for c in RETENTION_CATEGORIES if c["category_id"] == category_id), None
    )
    excess_years = proposed_period_years - statutory_minimum_years

    return {
        "category": category["name"] if category else "Unknown",
        "category_id": category_id,
        "proposed_period_years": proposed_period_years,
        "statutory_minimum_years": statutory_minimum_years,
        "excess_period_years": round(excess_years, 2),
        "justification": justification_text,
        "data_subjects_affected": data_subjects_affected,
        "sensitivity": sensitivity,
        "proportionality_assessment": {
            "excess_period": "within acceptable range" if excess_years <= 2 else "requires detailed justification",
            "volume_impact": "low" if data_subjects_affected < 1000 else "medium" if data_subjects_affected < 10000 else "high",
            "sensitivity_level": sensitivity,
        },
        "generated_date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "requires_dpo_approval": excess_years > 0,
    }


if __name__ == "__main__":
    schedule = generate_retention_schedule()
    print(f"Retention Schedule Generated: {schedule['generated_date']}")
    print(f"Total Categories: {schedule['total_categories']}")
    print(f"Next Review: {schedule['next_review_date']}")
    print(f"Checksum: {schedule['checksum']}")
    print()

    for cat in schedule["categories"]:
        print(f"  {cat['category_id']}: {cat['name']}")
        print(f"    Retention: {cat['retention_period_years']} years from {cat['retention_trigger']}")
        print(f"    Basis: {cat['statutory_basis']}")
        print()

    sample_deletion = calculate_deletion_date("2020-06-15", "CAT-003")
    print(f"Sample Deletion Date (CAT-003, triggered 2020-06-15): {sample_deletion}")

    sample_records = [
        {"category_id": "CAT-003", "trigger_date": "2019-01-15", "current_status": "active"},
        {"category_id": "CAT-002", "trigger_date": "2024-06-01", "current_status": "active"},
        {"category_id": "CAT-007", "trigger_date": "2026-02-15", "current_status": "active"},
    ]
    audit = audit_retention_compliance(sample_records)
    print(f"\nRetention Audit: {audit['compliance_rate']}% compliant")
    print(f"  Overdue: {audit['overdue_for_deletion']}")
    print(f"  Approaching: {audit['approaching_expiry']}")
