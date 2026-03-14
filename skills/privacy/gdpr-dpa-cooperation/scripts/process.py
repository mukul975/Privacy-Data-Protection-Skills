#!/usr/bin/env python3
"""
Supervisory Authority Request Tracker

Tracks and manages supervisory authority correspondence, ensuring
timely responses and complete documentation.
"""

import json
import sys
from datetime import datetime, timedelta


def calculate_deadline(request_date: str, days: int = 28) -> str:
    dt = datetime.strptime(request_date, "%Y-%m-%d")
    deadline = dt + timedelta(days=days)
    return deadline.strftime("%Y-%m-%d")


def assess_urgency(request: dict) -> str:
    deadline_str = request.get("deadline")
    if not deadline_str:
        return "UNKNOWN"

    try:
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
        days_remaining = (deadline - datetime.now()).days
    except ValueError:
        return "UNKNOWN"

    if days_remaining < 0:
        return "OVERDUE"
    elif days_remaining <= 3:
        return "CRITICAL"
    elif days_remaining <= 7:
        return "HIGH"
    elif days_remaining <= 14:
        return "MEDIUM"
    return "LOW"


def validate_response_completeness(request: dict) -> dict:
    issues = []
    items_requested = request.get("items_requested", [])
    items_provided = request.get("items_provided", [])

    missing_items = [item for item in items_requested if item not in items_provided]
    if missing_items:
        issues.append({
            "severity": "Critical",
            "issue": f"{len(missing_items)} requested items not yet provided",
            "missing": missing_items,
        })

    if not request.get("dpo_reviewed", False):
        issues.append({
            "severity": "Major",
            "issue": "Response has not been reviewed by the DPO",
        })

    if not request.get("legal_reviewed", False):
        issues.append({
            "severity": "Major",
            "issue": "Response has not been reviewed by legal counsel",
        })

    if not request.get("privilege_check", False):
        issues.append({
            "severity": "Major",
            "issue": "Legal privilege review has not been conducted",
        })

    return {
        "complete": len(issues) == 0,
        "issues": issues,
    }


def process_request_log(requests: list) -> dict:
    report = {
        "report_date": datetime.now().strftime("%Y-%m-%d"),
        "total_requests": len(requests),
        "by_status": {},
        "by_urgency": {},
        "overdue": [],
        "details": [],
    }

    for req in requests:
        req_id = req.get("request_id", "UNKNOWN")
        status = req.get("status", "received")
        urgency = assess_urgency(req)
        completeness = None
        if status == "in_progress":
            completeness = validate_response_completeness(req)

        report["by_status"][status] = report["by_status"].get(status, 0) + 1
        report["by_urgency"][urgency] = report["by_urgency"].get(urgency, 0) + 1

        detail = {
            "request_id": req_id,
            "authority": req.get("authority", ""),
            "request_type": req.get("request_type", ""),
            "received_date": req.get("received_date", ""),
            "deadline": req.get("deadline", ""),
            "status": status,
            "urgency": urgency,
        }

        if completeness:
            detail["completeness"] = completeness

        if urgency == "OVERDUE":
            report["overdue"].append(detail)

        report["details"].append(detail)

    return report


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <requests.json>")
        print("\nExpected JSON: list of request objects")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        requests = json.load(f)

    report = process_request_log(requests)
    print(json.dumps(report, indent=2))

    overdue_count = len(report["overdue"])
    sys.exit(2 if overdue_count > 0 else 0)


if __name__ == "__main__":
    main()
