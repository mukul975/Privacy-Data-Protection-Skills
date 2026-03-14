#!/usr/bin/env python3
"""
Regulatory Complaint Response Manager

Manages the lifecycle of GDPR Article 77 regulatory complaints,
including triage, investigation tracking, response drafting support,
and remediation management.
"""

import argparse
import json
from datetime import datetime, timedelta
from typing import Optional


SEVERITY_LEVELS = {
    "routine": {
        "description": "Individual rights exercise issue",
        "escalation": ["DPO"],
        "response_lead": "Privacy Analyst",
        "board_notification": False,
        "external_counsel": False,
    },
    "significant": {
        "description": "Systemic compliance issue",
        "escalation": ["DPO", "General Counsel"],
        "response_lead": "DPO",
        "board_notification": False,
        "external_counsel": True,
        "briefing_deadline_hours": 48,
    },
    "critical": {
        "description": "Potential enforcement action or fine",
        "escalation": ["DPO", "General Counsel", "CEO"],
        "response_lead": "DPO + External Counsel",
        "board_notification": True,
        "external_counsel": True,
        "briefing_deadline_hours": 24,
    },
}

DPA_PROFILES = {
    "ICO": {
        "name": "Information Commissioner's Office",
        "country": "United Kingdom",
        "standard_response_days": 28,
        "language": "English",
        "portal": "ICO online case management portal",
    },
    "CNIL": {
        "name": "Commission Nationale de l'Informatique et des Libertés",
        "country": "France",
        "standard_response_days": 30,
        "language": "French",
        "portal": "CNIL online portal",
    },
    "DPC": {
        "name": "Data Protection Commission",
        "country": "Ireland",
        "standard_response_days": 28,
        "language": "English",
        "portal": "DPC correspondence",
    },
    "BfDI": {
        "name": "Bundesbeauftragter für den Datenschutz und die Informationsfreiheit",
        "country": "Germany",
        "standard_response_days": 30,
        "language": "German",
        "portal": "BfDI correspondence",
    },
}


def create_complaint_record(
    receipt_date: str,
    dpa: str,
    dpa_reference: str,
    complaint_summary: str,
    severity: str,
    response_deadline: Optional[str] = None,
    complainant_name: Optional[str] = None,
) -> dict:
    """Create a regulatory complaint record with triage information."""
    recv_date = datetime.strptime(receipt_date, "%Y-%m-%d")
    reference = f"REG-{recv_date.strftime('%Y')}-{recv_date.strftime('%m%d')}"

    severity_info = SEVERITY_LEVELS.get(severity, SEVERITY_LEVELS["routine"])
    dpa_info = DPA_PROFILES.get(dpa, {"standard_response_days": 28})

    if response_deadline:
        resp_deadline = datetime.strptime(response_deadline, "%Y-%m-%d")
    else:
        resp_deadline = recv_date + timedelta(days=dpa_info.get("standard_response_days", 28))

    # Internal milestones
    days_available = (resp_deadline - recv_date).days
    investigation_deadline = recv_date + timedelta(days=min(14, int(days_available * 0.5)))
    draft_deadline = recv_date + timedelta(days=min(21, int(days_available * 0.75)))
    review_deadline = recv_date + timedelta(days=min(25, int(days_available * 0.9)))

    record = {
        "reference": reference,
        "receipt_date": receipt_date,
        "dpa": {
            "code": dpa,
            "details": dpa_info,
        },
        "dpa_reference": dpa_reference,
        "complaint_summary": complaint_summary,
        "complainant": complainant_name or "Not disclosed by DPA",
        "severity": {
            "level": severity,
            "details": severity_info,
        },
        "deadlines": {
            "dpa_response": resp_deadline.strftime("%Y-%m-%d"),
            "internal_investigation": investigation_deadline.strftime("%Y-%m-%d"),
            "draft_response": draft_deadline.strftime("%Y-%m-%d"),
            "review_approval": review_deadline.strftime("%Y-%m-%d"),
        },
        "immediate_actions": [],
        "status": "open",
    }

    # Immediate actions based on severity
    record["immediate_actions"].append("Notify DPO immediately")
    if severity_info.get("external_counsel"):
        record["immediate_actions"].append("Engage external legal counsel")
    if severity_info.get("board_notification"):
        hours = severity_info.get("briefing_deadline_hours", 24)
        record["immediate_actions"].append(
            f"Notify the board within {hours} hours"
        )
    record["immediate_actions"].extend([
        "Preserve all relevant records and correspondence",
        "Assign investigation team",
        f"Begin internal investigation (complete by {investigation_deadline.strftime('%Y-%m-%d')})",
    ])

    return record


def create_remediation_action(
    complaint_reference: str,
    gap_description: str,
    root_cause: str,
    corrective_action: str,
    owner: str,
    target_date: str,
) -> dict:
    """Create a remediation action for a compliance gap identified during investigation."""
    return {
        "complaint_reference": complaint_reference,
        "created_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "gap_description": gap_description,
        "root_cause": root_cause,
        "corrective_action": corrective_action,
        "owner": owner,
        "target_date": target_date,
        "status": "open",
        "verification_method": "DPO review of implementation evidence",
    }


def main():
    parser = argparse.ArgumentParser(
        description="Manage GDPR Art. 77 regulatory complaint responses"
    )
    subparsers = parser.add_subparsers(dest="command")

    create_p = subparsers.add_parser("create", help="Create complaint record")
    create_p.add_argument("receipt_date", help="Date DPA correspondence received (YYYY-MM-DD)")
    create_p.add_argument("--dpa", required=True, choices=list(DPA_PROFILES.keys()))
    create_p.add_argument("--dpa-ref", required=True, help="DPA reference number")
    create_p.add_argument("--summary", required=True, help="Complaint summary")
    create_p.add_argument("--severity", required=True, choices=list(SEVERITY_LEVELS.keys()))
    create_p.add_argument("--deadline", help="Response deadline (YYYY-MM-DD)")
    create_p.add_argument("--complainant", help="Complainant name (if disclosed)")

    remediate_p = subparsers.add_parser("remediate", help="Create remediation action")
    remediate_p.add_argument("--complaint-ref", required=True)
    remediate_p.add_argument("--gap", required=True, help="Gap description")
    remediate_p.add_argument("--root-cause", required=True)
    remediate_p.add_argument("--action", required=True, help="Corrective action")
    remediate_p.add_argument("--owner", required=True)
    remediate_p.add_argument("--target-date", required=True)

    args = parser.parse_args()

    if args.command == "create":
        result = create_complaint_record(
            receipt_date=args.receipt_date,
            dpa=args.dpa,
            dpa_reference=args.dpa_ref,
            complaint_summary=args.summary,
            severity=args.severity,
            response_deadline=args.deadline,
            complainant_name=args.complainant,
        )
    elif args.command == "remediate":
        result = create_remediation_action(
            complaint_reference=args.complaint_ref,
            gap_description=args.gap,
            root_cause=args.root_cause,
            corrective_action=args.action,
            owner=args.owner,
            target_date=args.target_date,
        )
    else:
        parser.print_help()
        return

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
