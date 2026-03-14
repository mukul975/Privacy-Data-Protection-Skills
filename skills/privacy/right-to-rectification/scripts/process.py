#!/usr/bin/env python3
"""
Right to Rectification Processor

Manages GDPR Article 16 rectification requests including verification,
multi-system update tracking, and Art. 19 notification generation.
"""

import argparse
import json
from datetime import datetime, timedelta
from typing import Optional


VERIFICATION_METHODS = {
    "name": {"method": "Accept data subject assertion", "evidence_required": False},
    "date_of_birth": {"method": "Documentary evidence required", "evidence_required": True, "examples": ["Passport", "Birth certificate", "Driving licence"]},
    "address": {"method": "Accept assertion for current address", "evidence_required": False, "examples": ["Utility bill", "Bank statement"]},
    "email": {"method": "Verify via confirmation email to new address", "evidence_required": False},
    "phone": {"method": "Verify via confirmation SMS/call to new number", "evidence_required": False},
    "employment": {"method": "Accept assertion or verify with employer (with consent)", "evidence_required": False},
    "financial": {"method": "Cross-reference against source records", "evidence_required": True, "examples": ["Bank statement", "Invoice", "Payment receipt"]},
    "technical": {"method": "Assess factual correctability — system-generated data may not be rectifiable", "evidence_required": True},
}


def create_rectification_request(
    request_date: str,
    data_subject_id: str,
    corrections: list,
    systems: list,
    recipients: list,
) -> dict:
    """
    Create a rectification request record.

    Args:
        request_date: Date request received (YYYY-MM-DD).
        data_subject_id: Pseudonymised subject ID.
        corrections: List of dicts with keys: field, category, current_value, requested_value.
        systems: List of systems where data resides.
        recipients: List of third parties who received the data.
    """
    req_date = datetime.strptime(request_date, "%Y-%m-%d")
    reference = f"REC-{req_date.strftime('%Y')}-{req_date.strftime('%m%d')}"
    response_deadline = req_date + timedelta(days=30)
    implementation_target = req_date + timedelta(days=5)

    request_record = {
        "reference": reference,
        "request_date": request_date,
        "data_subject_id": data_subject_id,
        "response_deadline": response_deadline.strftime("%Y-%m-%d"),
        "implementation_target": implementation_target.strftime("%Y-%m-%d"),
        "corrections": [],
        "systems_affected": systems,
        "recipients_to_notify": recipients,
        "status": "pending_verification",
    }

    for correction in corrections:
        category = correction.get("category", "unknown")
        verification = VERIFICATION_METHODS.get(category, {
            "method": "Manual assessment required",
            "evidence_required": True,
        })

        request_record["corrections"].append({
            "field": correction["field"],
            "category": category,
            "current_value": correction["current_value"],
            "requested_value": correction["requested_value"],
            "verification_method": verification["method"],
            "evidence_required": verification.get("evidence_required", False),
            "evidence_examples": verification.get("examples", []),
            "status": "pending",
        })

    return request_record


def process_verification(
    request_record: dict,
    verification_results: list,
) -> dict:
    """
    Process verification results and determine rectification actions.

    Args:
        request_record: The rectification request record.
        verification_results: List of dicts with keys: field, verified (bool), notes.
    """
    for result in verification_results:
        for correction in request_record["corrections"]:
            if correction["field"] == result["field"]:
                if result["verified"]:
                    correction["status"] = "verified_inaccurate"
                    correction["action"] = "rectify"
                elif result.get("inconclusive", False):
                    correction["status"] = "inconclusive"
                    correction["action"] = "restrict_pending_investigation"
                else:
                    correction["status"] = "verified_accurate"
                    correction["action"] = "no_rectification"
                correction["verification_notes"] = result.get("notes", "")

    # Determine overall status
    actions = [c["action"] for c in request_record["corrections"]]
    if all(a == "rectify" for a in actions):
        request_record["status"] = "approved_full"
        request_record["decision"] = "Full rectification approved"
    elif any(a == "rectify" for a in actions):
        request_record["status"] = "approved_partial"
        request_record["decision"] = "Partial rectification — some items verified, others not"
    elif any(a == "restrict_pending_investigation" for a in actions):
        request_record["status"] = "pending_investigation"
        request_record["decision"] = "Restriction applied under Art. 18(1)(a) while accuracy investigation continues"
    else:
        request_record["status"] = "declined"
        request_record["decision"] = "Data verified as accurate — no rectification required"

    return request_record


def generate_update_plan(request_record: dict) -> dict:
    """Generate a multi-system update plan for approved rectifications."""
    corrections_to_apply = [
        c for c in request_record["corrections"] if c.get("action") == "rectify"
    ]

    if not corrections_to_apply:
        return {"plan": "No rectifications to apply", "updates": []}

    updates = []
    for system in request_record.get("systems_affected", []):
        for correction in corrections_to_apply:
            updates.append({
                "system": system,
                "field": correction["field"],
                "old_value": correction["current_value"],
                "new_value": correction["requested_value"],
                "status": "pending",
            })

    notifications = []
    for recipient in request_record.get("recipients_to_notify", []):
        notifications.append({
            "recipient": recipient,
            "notification_type": "Art. 19 Rectification Notification",
            "fields_corrected": [c["field"] for c in corrections_to_apply],
            "confirmation_deadline_days": 14,
            "status": "pending",
        })

    return {
        "reference": request_record["reference"],
        "updates": updates,
        "notifications": notifications,
        "backup_correction": {
            "status": "scheduled",
            "expected_completion": "Next backup rotation cycle (max 90 days)",
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Process GDPR Art. 16 rectification requests"
    )
    parser.add_argument("request_date", help="Date of request (YYYY-MM-DD)")
    parser.add_argument("--subject-id", default="DS-0001")
    parser.add_argument("--field", action="append", required=True, help="Field to correct (format: field:category:current:requested)")
    parser.add_argument("--system", action="append", default=["CRM", "data-warehouse"])
    parser.add_argument("--recipient", action="append", default=[])
    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    corrections = []
    for field_spec in args.field:
        parts = field_spec.split(":")
        if len(parts) >= 4:
            corrections.append({
                "field": parts[0],
                "category": parts[1],
                "current_value": parts[2],
                "requested_value": parts[3],
            })

    record = create_rectification_request(
        request_date=args.request_date,
        data_subject_id=args.subject_id,
        corrections=corrections,
        systems=args.system,
        recipients=args.recipient,
    )

    if args.json:
        print(json.dumps(record, indent=2))
    else:
        print("=" * 60)
        print("RECTIFICATION REQUEST RECORD")
        print("=" * 60)
        print(f"Reference:       {record['reference']}")
        print(f"Request Date:    {record['request_date']}")
        print(f"Subject ID:      {record['data_subject_id']}")
        print(f"Response Due:    {record['response_deadline']}")
        print(f"Implement By:    {record['implementation_target']}")
        print(f"Status:          {record['status']}")
        print()
        print("Corrections Requested:")
        for c in record["corrections"]:
            print(f"  Field: {c['field']} ({c['category']})")
            print(f"    Current:    {c['current_value']}")
            print(f"    Requested:  {c['requested_value']}")
            print(f"    Verify:     {c['verification_method']}")
            print(f"    Evidence:   {'Required' if c['evidence_required'] else 'Not required'}")
            print()
        print(f"Systems:         {', '.join(record['systems_affected'])}")
        print(f"Recipients:      {', '.join(record['recipients_to_notify']) or 'None'}")
        print("=" * 60)


if __name__ == "__main__":
    main()
