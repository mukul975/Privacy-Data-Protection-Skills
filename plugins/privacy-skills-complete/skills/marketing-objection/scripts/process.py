#!/usr/bin/env python3
"""
Direct Marketing Objection Manager

Manages GDPR Article 21(2)-(3) direct marketing objections including
suppression list management, cross-channel enforcement, and pre-campaign
screening.
"""

import argparse
import hashlib
import json
from datetime import datetime, timedelta
from typing import Optional


MARKETING_CHANNELS = {
    "email": "Email marketing communications",
    "sms": "SMS/text message marketing",
    "telephone": "Telephone marketing calls",
    "postal": "Postal direct mail",
    "online_ads": "Online targeted advertising (remarketing, customer match)",
    "profiling": "Marketing profiling and segmentation",
}

MARKETING_SYSTEMS = {
    "email_platform": {"name": "Mailchimp", "action": "Unsubscribe + add to suppression segment"},
    "sms_platform": {"name": "Twilio", "action": "Opt-out + add to suppression list"},
    "crm": {"name": "Salesforce", "action": "Set marketing_opt_out = TRUE"},
    "google_ads": {"name": "Google Ads", "action": "Remove from customer match and remarketing"},
    "meta_ads": {"name": "Meta Ads Manager", "action": "Remove from custom audiences"},
    "analytics": {"name": "Google Analytics", "action": "Exclude from marketing attribution"},
    "data_warehouse": {"name": "BigQuery", "action": "Update marketing consent flag"},
}


def hash_identifier(value: str) -> str:
    """Hash an identifier using SHA-256 for suppression list storage."""
    return hashlib.sha256(value.strip().lower().encode("utf-8")).hexdigest()


def process_marketing_objection(
    request_date: str,
    data_subject_id: str,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    postal_address: Optional[str] = None,
    scope: str = "full",
    channels_specified: Optional[list] = None,
    channel_received: str = "email",
) -> dict:
    """
    Process a direct marketing objection.

    Args:
        request_date: Date of objection (YYYY-MM-DD).
        data_subject_id: Data subject identifier.
        email: Email address to suppress.
        phone: Phone number to suppress.
        postal_address: Postal address to suppress.
        scope: 'full' for all channels or 'partial' for specific channels.
        channels_specified: List of specific channels to suppress (if partial).
        channel_received: Channel through which objection was received.
    """
    req_date = datetime.strptime(request_date, "%Y-%m-%d")
    reference = f"MKT-{req_date.strftime('%Y')}-{req_date.strftime('%m%d')}"
    cessation_deadline = req_date + timedelta(hours=24)
    confirmation_deadline = req_date + timedelta(days=14)

    # Determine channels to suppress
    if scope == "full":
        channels_suppressed = list(MARKETING_CHANNELS.keys())
    elif channels_specified:
        channels_suppressed = [c for c in channels_specified if c in MARKETING_CHANNELS]
    else:
        channels_suppressed = list(MARKETING_CHANNELS.keys())

    # Build suppression record
    suppression_record = {
        "data_subject_id": data_subject_id,
        "suppression_date": request_date,
        "scope": scope,
        "channels_suppressed": channels_suppressed,
        "identifiers_hashed": {},
    }

    if email:
        suppression_record["identifiers_hashed"]["email_sha256"] = hash_identifier(email)
    if phone:
        suppression_record["identifiers_hashed"]["phone_sha256"] = hash_identifier(phone)
    if postal_address:
        suppression_record["identifiers_hashed"]["postal_sha256"] = hash_identifier(postal_address)

    # Build system update actions
    system_actions = []
    for sys_key, sys_info in MARKETING_SYSTEMS.items():
        system_actions.append({
            "system": sys_info["name"],
            "action": sys_info["action"],
            "status": "pending",
            "deadline": cessation_deadline.strftime("%Y-%m-%dT%H:%M:%SZ"),
        })

    result = {
        "reference": reference,
        "request_date": request_date,
        "channel_received": channel_received,
        "right_type": "Absolute — Art. 21(2) GDPR",
        "assessment_required": False,
        "can_refuse": False,
        "cessation_deadline": cessation_deadline.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "confirmation_deadline": confirmation_deadline.strftime("%Y-%m-%d"),
        "suppression_record": suppression_record,
        "system_actions": system_actions,
        "channels_detail": [
            {
                "channel": ch,
                "description": MARKETING_CHANNELS[ch],
                "action": "SUPPRESS",
            }
            for ch in channels_suppressed
        ],
        "ongoing_obligations": [
            "Check suppression list before every marketing campaign",
            "Screen new data imports against suppression list",
            "Retain suppression record indefinitely (until subject re-consents)",
            "Quarterly audit of suppression list effectiveness",
        ],
    }

    return result


def screen_campaign_list(
    suppression_list: list,
    campaign_recipients: list,
) -> dict:
    """
    Screen a campaign recipient list against the suppression list.

    Args:
        suppression_list: List of hashed identifiers to suppress.
        campaign_recipients: List of dicts with 'email' and 'id' keys.
    """
    total = len(campaign_recipients)
    suppressed = []
    approved = []

    for recipient in campaign_recipients:
        email_hash = hash_identifier(recipient.get("email", ""))
        if email_hash in suppression_list:
            suppressed.append(recipient["id"])
        else:
            approved.append(recipient["id"])

    return {
        "screening_date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_recipients": total,
        "suppressed_count": len(suppressed),
        "approved_count": len(approved),
        "suppression_rate": f"{(len(suppressed) / total * 100):.1f}%" if total > 0 else "0%",
        "suppressed_ids": suppressed,
        "status": "screened",
    }


def main():
    parser = argparse.ArgumentParser(
        description="Manage GDPR Art. 21(2) direct marketing objections"
    )
    parser.add_argument("request_date", help="Date of objection (YYYY-MM-DD)")
    parser.add_argument("--subject-id", default="DS-0001")
    parser.add_argument("--email", help="Email address to suppress")
    parser.add_argument("--phone", help="Phone number to suppress")
    parser.add_argument("--scope", choices=["full", "partial"], default="full")
    parser.add_argument("--channel", action="append", help="Specific channel to suppress (if partial)")
    parser.add_argument("--received-via", default="email", help="Channel objection was received through")
    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    result = process_marketing_objection(
        request_date=args.request_date,
        data_subject_id=args.subject_id,
        email=args.email,
        phone=args.phone,
        scope=args.scope,
        channels_specified=args.channel,
        channel_received=args.received_via,
    )

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("=" * 60)
        print("DIRECT MARKETING OBJECTION — ABSOLUTE RIGHT")
        print("=" * 60)
        print(f"Reference:           {result['reference']}")
        print(f"Request Date:        {result['request_date']}")
        print(f"Right Type:          {result['right_type']}")
        print(f"Can Refuse:          {result['can_refuse']}")
        print(f"Cessation Deadline:  {result['cessation_deadline']}")
        print(f"Confirm By:          {result['confirmation_deadline']}")
        print()
        print("Channels Suppressed:")
        for ch in result["channels_detail"]:
            print(f"  [{ch['action']}] {ch['channel']}: {ch['description']}")
        print()
        print("System Actions Required:")
        for action in result["system_actions"]:
            print(f"  {action['system']}: {action['action']}")
        print()
        print("Suppression Identifiers (hashed):")
        for key, val in result["suppression_record"]["identifiers_hashed"].items():
            print(f"  {key}: {val[:16]}...")
        print("=" * 60)


if __name__ == "__main__":
    main()
