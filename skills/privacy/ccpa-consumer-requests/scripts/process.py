#!/usr/bin/env python3
"""
CCPA Consumer Request Manager

Manages California Consumer Privacy Act (CCPA) consumer rights
requests including right to know, delete, correct, opt-out of
sale, and non-discrimination compliance.
"""

import argparse
import json
from datetime import datetime, timedelta
from typing import Optional


CCPA_REQUEST_TYPES = {
    "know_categories": {
        "right": "Right to Know — Categories",
        "section": "Cal. Civ. Code Section 1798.110(a)(1)-(4)",
        "verification": "reasonable",
        "response_days": 45,
        "extendable_days": 45,
    },
    "know_specific": {
        "right": "Right to Know — Specific Pieces",
        "section": "Cal. Civ. Code Section 1798.110(a)(5)",
        "verification": "reasonably_high",
        "response_days": 45,
        "extendable_days": 45,
    },
    "delete": {
        "right": "Right to Delete",
        "section": "Cal. Civ. Code Section 1798.105",
        "verification": "reasonable",
        "response_days": 45,
        "extendable_days": 45,
    },
    "correct": {
        "right": "Right to Correct",
        "section": "Cal. Civ. Code Section 1798.106",
        "verification": "reasonable",
        "response_days": 45,
        "extendable_days": 45,
    },
    "opt_out_sale": {
        "right": "Right to Opt-Out of Sale/Sharing",
        "section": "Cal. Civ. Code Section 1798.120",
        "verification": "none",
        "response_days": 15,
        "extendable_days": 0,
        "response_days_type": "business",
    },
    "limit_sensitive": {
        "right": "Right to Limit Use of Sensitive PI",
        "section": "Cal. Civ. Code Section 1798.121",
        "verification": "none",
        "response_days": 15,
        "extendable_days": 0,
        "response_days_type": "business",
    },
}

CCPA_CATEGORIES = [
    "Identifiers (name, address, email, SSN, IP address, account name)",
    "Customer records (financial, insurance, education, employment information)",
    "Protected classification characteristics (age, race, sex, disability)",
    "Commercial information (purchase history, consumption tendencies)",
    "Biometric information",
    "Internet or electronic network activity (browsing, search, interaction history)",
    "Geolocation data",
    "Audio, electronic, visual, thermal, olfactory, or similar information",
    "Professional or employment-related information",
    "Non-FERPA education information",
    "Inferences drawn to create a consumer profile",
    "Sensitive personal information (SSN, financial accounts, precise geolocation, racial/ethnic origin, health data)",
]

DELETION_EXCEPTIONS = [
    {"code": "1798.105(d)(1)", "description": "Complete a transaction or provide requested service"},
    {"code": "1798.105(d)(2)", "description": "Detect security incidents or protect against fraud"},
    {"code": "1798.105(d)(3)", "description": "Debug to identify and repair errors"},
    {"code": "1798.105(d)(4)", "description": "Exercise free speech or another legal right"},
    {"code": "1798.105(d)(5)", "description": "Comply with California Electronic Communications Privacy Act"},
    {"code": "1798.105(d)(6)", "description": "Engage in public interest research (with consent)"},
    {"code": "1798.105(d)(7)", "description": "Internal use aligned with consumer expectations"},
    {"code": "1798.105(d)(8)", "description": "Comply with a legal obligation"},
    {"code": "1798.105(d)(9)", "description": "Lawful internal use compatible with collection context"},
]


def create_ccpa_request(
    request_date: str,
    consumer_id: str,
    request_type: str,
    channel: str = "web_form",
    is_california_resident: bool = True,
) -> dict:
    """Create a CCPA consumer request record."""
    if request_type not in CCPA_REQUEST_TYPES:
        return {"error": f"Unknown request type: {request_type}"}

    req_date = datetime.strptime(request_date, "%Y-%m-%d")
    req_info = CCPA_REQUEST_TYPES[request_type]
    reference = f"CCPA-{req_date.strftime('%Y')}-{req_date.strftime('%m%d')}"

    # Calculate acknowledgement deadline (10 business days)
    ack_date = req_date
    biz_days = 0
    while biz_days < 10:
        ack_date += timedelta(days=1)
        if ack_date.weekday() < 5:
            biz_days += 1

    # Calculate response deadline
    if req_info.get("response_days_type") == "business":
        resp_date = req_date
        biz_days = 0
        while biz_days < req_info["response_days"]:
            resp_date += timedelta(days=1)
            if resp_date.weekday() < 5:
                biz_days += 1
    else:
        resp_date = req_date + timedelta(days=req_info["response_days"])

    record = {
        "reference": reference,
        "request_date": request_date,
        "consumer_id": consumer_id,
        "is_california_resident": is_california_resident,
        "request_type": {
            "key": request_type,
            "right": req_info["right"],
            "section": req_info["section"],
        },
        "channel": channel,
        "verification": {
            "standard": req_info["verification"],
            "status": "pending" if req_info["verification"] != "none" else "not_required",
        },
        "deadlines": {
            "acknowledgement": ack_date.strftime("%Y-%m-%d"),
            "response": resp_date.strftime("%Y-%m-%d"),
        },
        "status": "received",
    }

    if req_info["extendable_days"] > 0:
        ext_date = resp_date + timedelta(days=req_info["extendable_days"])
        record["deadlines"]["maximum_extended"] = ext_date.strftime("%Y-%m-%d")
        record["extension_available"] = True
    else:
        record["extension_available"] = False

    # Add type-specific information
    if request_type in ("know_categories", "know_specific"):
        record["response_must_cover"] = "Preceding 12 months from request date"
        record["ccpa_categories"] = CCPA_CATEGORIES
    elif request_type == "delete":
        record["deletion_exceptions"] = DELETION_EXCEPTIONS
        record["obligations"] = [
            "Delete from business records",
            "Direct service providers and contractors to delete",
            "Direct third parties who purchased/received the information to delete",
        ]
    elif request_type == "opt_out_sale":
        record["obligations"] = [
            "Cease selling and sharing consumer's personal information",
            "Do not sell/share for at least 12 months",
            "Only re-enable with subsequent consumer authorization",
            "Notify downstream third parties",
        ]

    record["non_discrimination"] = {
        "section": "Cal. Civ. Code Section 1798.125",
        "obligations": [
            "Do not deny goods or services",
            "Do not charge different prices or rates",
            "Do not provide different level or quality of goods/services",
            "Do not suggest consumer will receive different treatment",
        ],
    }

    return record


def main():
    parser = argparse.ArgumentParser(
        description="Manage CCPA consumer rights requests"
    )
    parser.add_argument("request_date", help="Date of request (YYYY-MM-DD)")
    parser.add_argument("--consumer-id", default="CA-0001")
    parser.add_argument(
        "--type",
        required=True,
        choices=list(CCPA_REQUEST_TYPES.keys()),
        help="Type of CCPA request",
    )
    parser.add_argument("--channel", default="web_form", choices=["web_form", "email", "phone", "postal"])
    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    result = create_ccpa_request(
        request_date=args.request_date,
        consumer_id=args.consumer_id,
        request_type=args.type,
        channel=args.channel,
    )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
