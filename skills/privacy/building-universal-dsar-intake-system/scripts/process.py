#!/usr/bin/env python3
"""
Universal DSAR Intake System

Multi-channel data subject rights request intake, identity verification,
routing, SLA tracking, and response management.
"""

import argparse
import json
import re
from datetime import datetime, timedelta
from typing import Optional


REQUEST_TYPES = {
    "dsar": {"label": "Data Subject Access Request", "article": "Art. 15 GDPR", "deadline_days": 30, "jurisdiction": "GDPR"},
    "erasure": {"label": "Right to Erasure", "article": "Art. 17 GDPR", "deadline_days": 30, "jurisdiction": "GDPR"},
    "portability": {"label": "Right to Data Portability", "article": "Art. 20 GDPR", "deadline_days": 30, "jurisdiction": "GDPR"},
    "restriction": {"label": "Right to Restriction", "article": "Art. 18 GDPR", "deadline_days": 30, "jurisdiction": "GDPR"},
    "rectification": {"label": "Right to Rectification", "article": "Art. 16 GDPR", "deadline_days": 30, "jurisdiction": "GDPR"},
    "objection": {"label": "Right to Object", "article": "Art. 21 GDPR", "deadline_days": 30, "jurisdiction": "GDPR"},
    "marketing_optout": {"label": "Marketing Opt-Out", "article": "Art. 21(2) GDPR", "deadline_days": 1, "jurisdiction": "GDPR"},
    "adm_contestation": {"label": "Automated Decision Contestation", "article": "Art. 22 GDPR", "deadline_days": 30, "jurisdiction": "GDPR"},
    "ccpa_know": {"label": "CCPA Right to Know", "article": "Section 1798.110", "deadline_days": 45, "jurisdiction": "CCPA"},
    "ccpa_delete": {"label": "CCPA Right to Delete", "article": "Section 1798.105", "deadline_days": 45, "jurisdiction": "CCPA"},
    "ccpa_optout": {"label": "CCPA Opt-Out of Sale", "article": "Section 1798.120", "deadline_days": 15, "jurisdiction": "CCPA"},
}

CHANNELS = ["web_form", "email", "telephone", "postal", "in_person"]

VERIFICATION_TIERS = {
    1: {"label": "Low Risk", "description": "Authenticated account", "data_points_required": 0},
    2: {"label": "Medium Risk", "description": "Known identifier, not authenticated", "data_points_required": 2},
    3: {"label": "High Risk", "description": "Unknown channel or third-party request", "data_points_required": 3},
}

ROUTING_MATRIX = {
    "dsar": {"assignee_role": "Privacy Analyst", "priority": "standard"},
    "erasure": {"assignee_role": "Privacy Analyst", "priority": "standard"},
    "portability": {"assignee_role": "Data Engineer + Privacy Analyst", "priority": "standard"},
    "restriction": {"assignee_role": "Senior Privacy Analyst", "priority": "standard"},
    "rectification": {"assignee_role": "Privacy Analyst", "priority": "standard"},
    "objection": {"assignee_role": "DPO", "priority": "complex"},
    "marketing_optout": {"assignee_role": "Marketing Operations", "priority": "urgent"},
    "adm_contestation": {"assignee_role": "DPO + Technical Lead", "priority": "complex"},
    "ccpa_know": {"assignee_role": "Privacy Analyst", "priority": "standard"},
    "ccpa_delete": {"assignee_role": "Privacy Analyst", "priority": "standard"},
    "ccpa_optout": {"assignee_role": "Marketing Operations", "priority": "urgent"},
}

EMAIL_KEYWORDS = {
    "dsar": ["access", "copy of my data", "subject access", "what data", "personal data you hold"],
    "erasure": ["delete", "erase", "remove", "forget", "right to be forgotten"],
    "rectification": ["correct", "update", "wrong", "inaccurate", "change my"],
    "marketing_optout": ["unsubscribe", "stop emailing", "stop marketing", "opt out of marketing", "remove from mailing"],
    "portability": ["export", "transfer my data", "portability", "download my data"],
    "ccpa_optout": ["do not sell", "opt out of sale", "stop selling", "ccpa opt"],
    "ccpa_know": ["ccpa", "california", "what information", "right to know"],
    "ccpa_delete": ["ccpa delete", "california delete"],
}


def classify_email_request(email_body: str) -> dict:
    """Classify a request type from email body text using keyword matching."""
    body_lower = email_body.lower()
    scores = {}

    for req_type, keywords in EMAIL_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in body_lower)
        if score > 0:
            scores[req_type] = score

    if not scores:
        return {"classified_type": None, "confidence": "low", "scores": {}}

    best_match = max(scores, key=scores.get)
    max_score = scores[best_match]

    confidence = "high" if max_score >= 2 else "medium" if max_score == 1 else "low"

    return {
        "classified_type": best_match,
        "classified_label": REQUEST_TYPES.get(best_match, {}).get("label", "Unknown"),
        "confidence": confidence,
        "scores": scores,
    }


def create_intake_record(
    request_date: str,
    channel: str,
    request_type: str,
    subject_name: str,
    subject_email: str,
    subject_identifiers: dict = None,
    authenticated: bool = False,
    third_party: bool = False,
) -> dict:
    """Create a universal intake record for a data subject rights request."""
    req_date = datetime.strptime(request_date, "%Y-%m-%d")
    req_info = REQUEST_TYPES.get(request_type)

    if not req_info:
        return {"error": f"Unknown request type: {request_type}"}

    # Generate reference
    type_prefix = {
        "dsar": "DSAR", "erasure": "ERA", "portability": "PORT",
        "restriction": "RST", "rectification": "REC", "objection": "OBJ",
        "marketing_optout": "MKT", "adm_contestation": "ADM",
        "ccpa_know": "CCPA", "ccpa_delete": "CCPA", "ccpa_optout": "CCPA",
    }
    prefix = type_prefix.get(request_type, "REQ")
    reference = f"{prefix}-{req_date.strftime('%Y')}-{req_date.strftime('%m%d')}"

    # Determine verification tier
    if authenticated:
        verification_tier = 1
    elif third_party:
        verification_tier = 3
    else:
        verification_tier = 2

    tier_info = VERIFICATION_TIERS[verification_tier]

    # Calculate deadline
    deadline = req_date + timedelta(days=req_info["deadline_days"])

    # Calculate acknowledgement deadline (3 business days)
    ack_date = req_date
    biz_days = 0
    while biz_days < 3:
        ack_date += timedelta(days=1)
        if ack_date.weekday() < 5:
            biz_days += 1

    # Get routing info
    routing = ROUTING_MATRIX.get(request_type, {"assignee_role": "Privacy Analyst", "priority": "standard"})

    record = {
        "reference": reference,
        "receipt_date": request_date,
        "receipt_timestamp": req_date.strftime("%Y-%m-%dT09:00:00Z"),
        "channel": channel,
        "request_type": {
            "key": request_type,
            "label": req_info["label"],
            "article": req_info["article"],
            "jurisdiction": req_info["jurisdiction"],
        },
        "data_subject": {
            "name": subject_name,
            "email": subject_email,
            "additional_identifiers": subject_identifiers or {},
        },
        "verification": {
            "tier": verification_tier,
            "tier_label": tier_info["label"],
            "description": tier_info["description"],
            "data_points_required": tier_info["data_points_required"],
            "status": "verified" if verification_tier == 1 else "pending",
        },
        "routing": {
            "assignee_role": routing["assignee_role"],
            "priority": routing["priority"],
        },
        "deadlines": {
            "acknowledgement": ack_date.strftime("%Y-%m-%d"),
            "response": deadline.strftime("%Y-%m-%d"),
        },
        "status": "received",
        "sla": {
            "deadline_days": req_info["deadline_days"],
            "days_elapsed": 0,
            "days_remaining": req_info["deadline_days"],
            "status": "green",
        },
    }

    return record


def check_sla_status(records: list) -> dict:
    """Check SLA status for a list of open request records."""
    today = datetime.utcnow()
    summary = {
        "check_date": today.strftime("%Y-%m-%d"),
        "total_open": len(records),
        "green": 0,
        "amber": 0,
        "red": 0,
        "critical": 0,
        "overdue": 0,
        "alerts": [],
    }

    for record in records:
        req_date = datetime.strptime(record["receipt_date"], "%Y-%m-%d")
        days_elapsed = (today - req_date).days
        deadline_days = record["sla"]["deadline_days"]
        days_remaining = deadline_days - days_elapsed

        if days_elapsed < 20:
            status = "green"
            summary["green"] += 1
        elif days_elapsed < 25:
            status = "amber"
            summary["amber"] += 1
            summary["alerts"].append({
                "reference": record["reference"],
                "status": "amber",
                "days_elapsed": days_elapsed,
                "action": "Alert assignee and team lead",
            })
        elif days_elapsed < 28:
            status = "red"
            summary["red"] += 1
            summary["alerts"].append({
                "reference": record["reference"],
                "status": "red",
                "days_elapsed": days_elapsed,
                "action": "Alert DPO",
            })
        elif days_elapsed <= deadline_days:
            status = "critical"
            summary["critical"] += 1
            summary["alerts"].append({
                "reference": record["reference"],
                "status": "critical",
                "days_elapsed": days_elapsed,
                "action": "Alert DPO + General Counsel — emergency priority",
            })
        else:
            status = "overdue"
            summary["overdue"] += 1
            summary["alerts"].append({
                "reference": record["reference"],
                "status": "overdue",
                "days_elapsed": days_elapsed,
                "days_overdue": days_elapsed - deadline_days,
                "action": "COMPLIANCE BREACH — Alert DPO + GC + CEO, document and remediate",
            })

    return summary


def main():
    parser = argparse.ArgumentParser(
        description="Universal DSAR intake system"
    )
    subparsers = parser.add_subparsers(dest="command")

    intake_p = subparsers.add_parser("intake", help="Create intake record")
    intake_p.add_argument("request_date", help="Date of request (YYYY-MM-DD)")
    intake_p.add_argument("--channel", required=True, choices=CHANNELS)
    intake_p.add_argument("--type", required=True, choices=list(REQUEST_TYPES.keys()))
    intake_p.add_argument("--name", required=True, help="Data subject name")
    intake_p.add_argument("--email", required=True, help="Data subject email")
    intake_p.add_argument("--authenticated", action="store_true")
    intake_p.add_argument("--third-party", action="store_true")

    classify_p = subparsers.add_parser("classify", help="Classify email request")
    classify_p.add_argument("--body", required=True, help="Email body text")

    args = parser.parse_args()

    if args.command == "intake":
        result = create_intake_record(
            request_date=args.request_date,
            channel=args.channel,
            request_type=args.type,
            subject_name=args.name,
            subject_email=args.email,
            authenticated=args.authenticated,
            third_party=args.third_party,
        )
    elif args.command == "classify":
        result = classify_email_request(args.body)
    else:
        parser.print_help()
        return

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
