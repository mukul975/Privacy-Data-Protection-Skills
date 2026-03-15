#!/usr/bin/env python3
"""
RoPA Maintenance Monitor

Monitors RoPA entries for staleness, completeness gaps, and pending
review deadlines. Generates maintenance reports and alerts for
overdue reviews, expiring DPAs, and incomplete fields.
"""

import json
import sys
from datetime import datetime, timedelta
from typing import Any


def parse_date(date_str: str) -> datetime | None:
    """Parse a date string in YYYY-MM-DD format."""
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None


def check_staleness(records: list[dict], max_age_days: int = 365) -> list[dict]:
    """Identify records that have not been reviewed within the threshold."""
    stale = []
    now = datetime.now()
    for record in records:
        record_id = record.get("record_id", "UNKNOWN")
        last_reviewed = record.get("last_reviewed_date")
        review_date = parse_date(last_reviewed)

        if not review_date:
            stale.append({
                "record_id": record_id,
                "activity": record.get("processing_activity", "N/A"),
                "issue": "No last_reviewed_date recorded",
                "severity": "Critical",
                "days_overdue": "Unknown",
            })
            continue

        age_days = (now - review_date).days
        if age_days > max_age_days:
            stale.append({
                "record_id": record_id,
                "activity": record.get("processing_activity", record.get("service_name", "N/A")),
                "issue": f"Last reviewed {age_days} days ago (threshold: {max_age_days})",
                "severity": "Major" if age_days <= max_age_days * 1.5 else "Critical",
                "days_overdue": age_days - max_age_days,
            })

    return stale


def check_upcoming_reviews(records: list[dict], horizon_days: int = 30) -> list[dict]:
    """Identify records with reviews due within the specified horizon."""
    upcoming = []
    now = datetime.now()
    horizon = now + timedelta(days=horizon_days)

    for record in records:
        record_id = record.get("record_id", "UNKNOWN")
        next_review = record.get("next_review_date")
        review_date = parse_date(next_review)

        if not review_date:
            upcoming.append({
                "record_id": record_id,
                "activity": record.get("processing_activity", record.get("service_name", "N/A")),
                "issue": "No next_review_date scheduled",
                "severity": "Major",
            })
            continue

        if review_date <= horizon:
            days_until = (review_date - now).days
            if days_until < 0:
                upcoming.append({
                    "record_id": record_id,
                    "activity": record.get("processing_activity", record.get("service_name", "N/A")),
                    "issue": f"Review overdue by {abs(days_until)} days (due: {next_review})",
                    "severity": "Critical",
                })
            else:
                upcoming.append({
                    "record_id": record_id,
                    "activity": record.get("processing_activity", record.get("service_name", "N/A")),
                    "issue": f"Review due in {days_until} days (due: {next_review})",
                    "severity": "Info",
                })

    return upcoming


def check_dpa_expiry(records: list[dict], horizon_days: int = 90) -> list[dict]:
    """Check for DPAs expiring within the horizon across all recipient entries."""
    expiring = []
    now = datetime.now()
    horizon = now + timedelta(days=horizon_days)

    for record in records:
        record_id = record.get("record_id", "UNKNOWN")
        recipients = record.get("recipient_categories", [])
        if not isinstance(recipients, list):
            continue

        for recipient in recipients:
            if not isinstance(recipient, dict):
                continue
            dpa_ref = recipient.get("dpa_reference", "")
            dpa_expiry = recipient.get("dpa_expiry")
            if not dpa_expiry:
                continue

            expiry_date = parse_date(dpa_expiry)
            if not expiry_date:
                continue

            if expiry_date <= horizon:
                days_until = (expiry_date - now).days
                expiring.append({
                    "record_id": record_id,
                    "recipient": recipient.get("recipient", "Unknown"),
                    "dpa_reference": dpa_ref,
                    "expiry_date": dpa_expiry,
                    "days_until_expiry": days_until,
                    "severity": "Critical" if days_until < 0 else ("Major" if days_until < 30 else "Info"),
                })

    return expiring


def check_field_completeness(records: list[dict]) -> list[dict]:
    """Check all records for missing mandatory fields."""
    controller_fields = [
        "controller_identity", "purposes", "data_subject_categories",
        "personal_data_categories", "recipient_categories",
        "international_transfers", "retention_periods", "security_measures",
    ]
    processor_fields = [
        "processor_identity", "controllers", "processing_categories",
        "international_transfers", "security_measures",
    ]

    gaps = []
    for record in records:
        record_id = record.get("record_id", "UNKNOWN")
        record_type = record.get("record_type", "controller")
        fields = processor_fields if record_type == "processor" else controller_fields

        for field in fields:
            value = record.get(field)
            if value is None or value == "" or value == [] or value == {}:
                gaps.append({
                    "record_id": record_id,
                    "field": field,
                    "issue": f"Mandatory field '{field}' is empty or missing",
                    "severity": "Critical",
                })

    return gaps


def generate_maintenance_report(ropa: dict, max_age_days: int = 365, review_horizon: int = 30, dpa_horizon: int = 90) -> str:
    """Generate a comprehensive maintenance status report."""
    records = ropa.get("records", [])
    org = ropa.get("organisation", "Unknown")

    lines = []
    lines.append("=" * 80)
    lines.append(f"RoPA MAINTENANCE STATUS REPORT — {org}")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Total Records: {len(records)}")
    lines.append("=" * 80)

    # Staleness check
    stale = check_staleness(records, max_age_days)
    lines.append(f"\n{'─' * 40}")
    lines.append(f"STALENESS CHECK ({max_age_days}-day threshold)")
    lines.append(f"{'─' * 40}")
    if stale:
        for s in stale:
            lines.append(f"  [{s['severity']}] {s['record_id']}: {s['activity']}")
            lines.append(f"    {s['issue']}")
    else:
        lines.append("  All records are within the review threshold.")

    # Upcoming reviews
    upcoming = check_upcoming_reviews(records, review_horizon)
    lines.append(f"\n{'─' * 40}")
    lines.append(f"UPCOMING REVIEWS (next {review_horizon} days)")
    lines.append(f"{'─' * 40}")
    if upcoming:
        for u in upcoming:
            lines.append(f"  [{u['severity']}] {u['record_id']}: {u['activity']}")
            lines.append(f"    {u['issue']}")
    else:
        lines.append("  No reviews due within the horizon.")

    # DPA expiry
    expiring = check_dpa_expiry(records, dpa_horizon)
    lines.append(f"\n{'─' * 40}")
    lines.append(f"DPA EXPIRY CHECK (next {dpa_horizon} days)")
    lines.append(f"{'─' * 40}")
    if expiring:
        for e in expiring:
            lines.append(f"  [{e['severity']}] {e['record_id']} — {e['recipient']}")
            lines.append(f"    DPA: {e['dpa_reference']}, Expiry: {e['expiry_date']} ({e['days_until_expiry']} days)")
    else:
        lines.append("  No DPAs expiring within the horizon.")

    # Field completeness
    gaps = check_field_completeness(records)
    lines.append(f"\n{'─' * 40}")
    lines.append("FIELD COMPLETENESS CHECK")
    lines.append(f"{'─' * 40}")
    if gaps:
        for g in gaps:
            lines.append(f"  [{g['severity']}] {g['record_id']}: {g['field']}")
            lines.append(f"    {g['issue']}")
    else:
        lines.append("  All mandatory fields are populated.")

    # Summary
    total_issues = len(stale) + len([u for u in upcoming if u["severity"] != "Info"]) + len(expiring) + len(gaps)
    critical = (
        sum(1 for s in stale if s["severity"] == "Critical") +
        sum(1 for u in upcoming if u["severity"] == "Critical") +
        sum(1 for e in expiring if e["severity"] == "Critical") +
        sum(1 for g in gaps if g["severity"] == "Critical")
    )
    lines.append(f"\n{'=' * 80}")
    lines.append(f"SUMMARY: {total_issues} issue(s), {critical} critical")
    lines.append(f"{'=' * 80}")

    # Completeness score
    total_records = len(records)
    if total_records > 0:
        stale_pct = (1 - len(stale) / total_records) * 100
        complete_pct = (1 - len(gaps) / (total_records * 8)) * 100  # 8 fields per controller record
        score = (stale_pct * 0.4 + complete_pct * 0.6)
        lines.append(f"\nCompliance Score: {score:.1f}%")
        if score >= 95:
            lines.append("Status: SUPERVISORY AUTHORITY READY")
        elif score >= 80:
            lines.append("Status: ACCEPTABLE — minor improvements needed")
        else:
            lines.append("Status: REQUIRES ATTENTION — significant gaps detected")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python process.py monitor <ropa_file.json> [--max-age 365] [--review-horizon 30] [--dpa-horizon 90]")
        print("  python process.py staleness <ropa_file.json> [--max-age 365]")
        print("  python process.py completeness <ropa_file.json>")
        sys.exit(1)

    command = sys.argv[1]

    if command in ("monitor", "staleness", "completeness"):
        if len(sys.argv) < 3:
            print("ERROR: Provide the path to the RoPA JSON file.")
            sys.exit(1)

        with open(sys.argv[2], "r", encoding="utf-8") as f:
            ropa_data = json.load(f)

        max_age = 365
        review_horizon = 30
        dpa_horizon = 90
        for i, arg in enumerate(sys.argv):
            if arg == "--max-age" and i + 1 < len(sys.argv):
                max_age = int(sys.argv[i + 1])
            if arg == "--review-horizon" and i + 1 < len(sys.argv):
                review_horizon = int(sys.argv[i + 1])
            if arg == "--dpa-horizon" and i + 1 < len(sys.argv):
                dpa_horizon = int(sys.argv[i + 1])

        if command == "monitor":
            report = generate_maintenance_report(ropa_data, max_age, review_horizon, dpa_horizon)
            print(report)
        elif command == "staleness":
            stale = check_staleness(ropa_data.get("records", []), max_age)
            if stale:
                print(f"STALE RECORDS: {len(stale)} found\n")
                for s in stale:
                    print(f"  [{s['severity']}] {s['record_id']}: {s['issue']}")
                sys.exit(1)
            else:
                print("All records are current.")
        elif command == "completeness":
            gaps = check_field_completeness(ropa_data.get("records", []))
            if gaps:
                print(f"COMPLETENESS GAPS: {len(gaps)} found\n")
                for g in gaps:
                    print(f"  [{g['severity']}] {g['record_id']}: {g['issue']}")
                sys.exit(1)
            else:
                print("All mandatory fields are populated.")
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
