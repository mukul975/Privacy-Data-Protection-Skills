#!/usr/bin/env python3
"""
Right to Restriction Processing Manager

Manages the lifecycle of GDPR Article 18 restriction requests,
including ground assessment, technical flag generation, permitted
processing evaluation, and lifting procedures.
"""

import argparse
import json
from datetime import datetime, timedelta
from typing import Optional


RESTRICTION_GROUNDS = {
    "accuracy_contested": {
        "article": "Art. 18(1)(a)",
        "description": "Data subject contests the accuracy of the personal data",
        "duration": "Until accuracy is verified by the controller",
        "review_period_days": 15,
        "resolution_options": [
            "Data verified as accurate — lift restriction, notify subject",
            "Data verified as inaccurate — rectify under Art. 16, lift restriction",
        ],
    },
    "unlawful_opposed": {
        "article": "Art. 18(1)(b)",
        "description": "Processing is unlawful and data subject opposes erasure, requesting restriction instead",
        "duration": "Indefinite — until subject consents to erasure or processing becomes lawful",
        "review_period_days": 90,
        "resolution_options": [
            "Data subject requests erasure — proceed under Art. 17",
            "Lawful basis for processing established — lift restriction with notice",
        ],
    },
    "legal_claims": {
        "article": "Art. 18(1)(c)",
        "description": "Controller no longer needs data but subject requires it for legal claims",
        "duration": "Duration of legal proceedings",
        "review_period_days": 90,
        "resolution_options": [
            "Legal proceedings concluded — lift restriction with notice",
            "Data subject confirms data no longer needed — lift restriction",
        ],
    },
    "objection_pending": {
        "article": "Art. 18(1)(d)",
        "description": "Data subject objected under Art. 21(1), pending legitimate grounds assessment",
        "duration": "Until Art. 21 assessment is complete",
        "review_period_days": 20,
        "resolution_options": [
            "Controller's legitimate grounds override — lift restriction, inform subject of right to complain",
            "Subject's grounds prevail — erase data under Art. 17(1)(c)",
        ],
    },
}

PERMITTED_PURPOSES = {
    "consent": "Data subject has provided specific consent for this processing during restriction",
    "legal_claims": "Processing necessary for establishment, exercise, or defence of legal claims",
    "protection_of_rights": "Processing necessary to protect rights of another natural or legal person",
    "public_interest": "Processing required for reasons of important public interest of the EU or Member State",
}


def assess_restriction_request(
    request_date: str,
    data_subject_id: str,
    ground: str,
    data_categories: list,
    systems: list,
) -> dict:
    """Assess a restriction request and generate the restriction order."""
    if ground not in RESTRICTION_GROUNDS:
        return {
            "decision": "INVALID",
            "error": f"Ground '{ground}' is not a recognised Art. 18(1) ground",
        }

    req_date = datetime.strptime(request_date, "%Y-%m-%d")
    ground_info = RESTRICTION_GROUNDS[ground]

    response_deadline = req_date + timedelta(days=30)
    implementation_deadline = req_date + timedelta(days=3)  # 72-hour technical deadline
    review_date = req_date + timedelta(days=ground_info["review_period_days"])

    reference = f"RST-{req_date.strftime('%Y')}-{req_date.strftime('%m%d')}"

    restriction_order = {
        "reference": reference,
        "request_date": request_date,
        "data_subject_id": data_subject_id,
        "decision": "RESTRICT",
        "ground": {
            "key": ground,
            "article": ground_info["article"],
            "description": ground_info["description"],
        },
        "duration": ground_info["duration"],
        "deadlines": {
            "response_to_subject": response_deadline.strftime("%Y-%m-%d"),
            "technical_implementation": implementation_deadline.strftime("%Y-%m-%d"),
            "first_review": review_date.strftime("%Y-%m-%d"),
        },
        "data_categories_restricted": data_categories,
        "systems_affected": systems,
        "technical_measures": {
            "database_flags": {
                "restriction_flag": True,
                "restriction_date": req_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "restriction_ground": ground,
                "restriction_reference": reference,
            },
            "application_controls": [
                "Exclude restricted records from standard queries",
                "Return HTTP 423 for restricted data via API",
                "Add batch processing exclusion rules",
                "Enable UI masking in internal tools",
            ],
            "access_restrictions": [
                "Limit access to DPO and Legal team",
                "Enable audit logging for all access to restricted data",
            ],
        },
        "permitted_processing": list(PERMITTED_PURPOSES.values()),
        "resolution_options": ground_info["resolution_options"],
        "notification_required": {
            "art_19_third_parties": True,
            "pre_lifting_notice_days": 7,
        },
    }

    return restriction_order


def evaluate_permitted_processing(
    restriction_reference: str,
    requested_purpose: str,
    justification: str,
    requestor: str,
) -> dict:
    """Evaluate whether a request to process restricted data is permitted."""
    if requested_purpose not in PERMITTED_PURPOSES:
        return {
            "restriction_reference": restriction_reference,
            "decision": "DENIED",
            "reason": f"Purpose '{requested_purpose}' is not one of the four permitted processing purposes under Art. 18(2)",
            "permitted_purposes": list(PERMITTED_PURPOSES.keys()),
        }

    return {
        "restriction_reference": restriction_reference,
        "decision": "PERMITTED",
        "purpose": PERMITTED_PURPOSES[requested_purpose],
        "justification": justification,
        "requestor": requestor,
        "conditions": [
            "Processing must be minimised to what is strictly necessary",
            "All access must be logged with timestamp, user, and purpose",
            "Processing must cease immediately once the specific purpose is fulfilled",
        ],
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def generate_lifting_notice(
    restriction_reference: str,
    data_subject_id: str,
    lifting_reason: str,
    lifting_date: str,
) -> dict:
    """Generate a pre-lifting notification under Art. 18(3)."""
    lift_date = datetime.strptime(lifting_date, "%Y-%m-%d")
    notice_date = lift_date - timedelta(days=7)

    return {
        "restriction_reference": restriction_reference,
        "data_subject_id": data_subject_id,
        "notice_type": "Pre-Lifting Notification under Art. 18(3) GDPR",
        "notice_date": notice_date.strftime("%Y-%m-%d"),
        "planned_lifting_date": lifting_date,
        "reason_for_lifting": lifting_reason,
        "data_subject_rights": [
            "Right to object to the lifting",
            "Right to request erasure under Art. 17",
            "Right to lodge a complaint with the supervisory authority under Art. 77",
        ],
        "response_deadline": lift_date.strftime("%Y-%m-%d"),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Manage GDPR Art. 18 restriction of processing requests"
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Assess command
    assess_parser = subparsers.add_parser("assess", help="Assess a restriction request")
    assess_parser.add_argument("request_date", help="Date of request (YYYY-MM-DD)")
    assess_parser.add_argument("--subject-id", default="DS-0001", help="Data subject ID")
    assess_parser.add_argument(
        "--ground",
        choices=list(RESTRICTION_GROUNDS.keys()),
        required=True,
        help="Restriction ground",
    )
    assess_parser.add_argument(
        "--data-category", action="append", default=["identity", "contact", "financial"],
        help="Data categories to restrict",
    )
    assess_parser.add_argument(
        "--system", action="append", default=["CRM", "data-warehouse", "analytics"],
        help="Systems holding the data",
    )

    # Permitted processing command
    permit_parser = subparsers.add_parser("permit", help="Evaluate permitted processing request")
    permit_parser.add_argument("--reference", required=True, help="Restriction reference")
    permit_parser.add_argument(
        "--purpose",
        choices=list(PERMITTED_PURPOSES.keys()),
        required=True,
        help="Requested processing purpose",
    )
    permit_parser.add_argument("--justification", required=True, help="Justification for processing")
    permit_parser.add_argument("--requestor", required=True, help="Name of person requesting access")

    # Lifting notice command
    lift_parser = subparsers.add_parser("lift", help="Generate pre-lifting notification")
    lift_parser.add_argument("--reference", required=True, help="Restriction reference")
    lift_parser.add_argument("--subject-id", required=True, help="Data subject ID")
    lift_parser.add_argument("--reason", required=True, help="Reason for lifting restriction")
    lift_parser.add_argument("--date", required=True, help="Planned lifting date (YYYY-MM-DD)")

    args = parser.parse_args()

    if args.command == "assess":
        result = assess_restriction_request(
            request_date=args.request_date,
            data_subject_id=args.subject_id,
            ground=args.ground,
            data_categories=args.data_category,
            systems=args.system,
        )
    elif args.command == "permit":
        result = evaluate_permitted_processing(
            restriction_reference=args.reference,
            requested_purpose=args.purpose,
            justification=args.justification,
            requestor=args.requestor,
        )
    elif args.command == "lift":
        result = generate_lifting_notice(
            restriction_reference=args.reference,
            data_subject_id=args.subject_id,
            lifting_reason=args.reason,
            lifting_date=args.date,
        )
    else:
        parser.print_help()
        return

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
