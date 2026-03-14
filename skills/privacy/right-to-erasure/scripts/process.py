#!/usr/bin/env python3
"""
Right to Erasure Assessment Engine

Evaluates erasure requests against GDPR Article 17 grounds and exceptions,
producing a documented decision with audit trail.
"""

import argparse
import json
from datetime import datetime, timedelta
from typing import Optional


ERASURE_GROUNDS = {
    "purpose_fulfilled": {
        "article": "Art. 17(1)(a)",
        "description": "Personal data no longer necessary for the purposes for which they were collected or processed",
        "assessment_question": "Is the data still necessary for any current processing purpose?",
    },
    "consent_withdrawn": {
        "article": "Art. 17(1)(b)",
        "description": "Data subject withdraws consent and there is no other legal ground for processing",
        "assessment_question": "Was processing based solely on consent, and has consent been withdrawn?",
    },
    "successful_objection": {
        "article": "Art. 17(1)(c)",
        "description": "Data subject has objected under Art. 21 and no overriding legitimate grounds exist",
        "assessment_question": "Has the objection been assessed and found to override the controller's interests?",
    },
    "unlawful_processing": {
        "article": "Art. 17(1)(d)",
        "description": "The personal data have been unlawfully processed",
        "assessment_question": "Has processing been identified as lacking a valid legal basis?",
    },
    "legal_obligation_erase": {
        "article": "Art. 17(1)(e)",
        "description": "Erasure required to comply with a legal obligation under EU or Member State law",
        "assessment_question": "Is there a specific legal obligation requiring deletion of this data?",
    },
    "child_data_iss": {
        "article": "Art. 17(1)(f)",
        "description": "Data collected from a child in relation to information society services under Art. 8(1)",
        "assessment_question": "Was data collected from a child in relation to an online service?",
    },
}

ERASURE_EXCEPTIONS = {
    "freedom_expression": {
        "article": "Art. 17(3)(a)",
        "description": "Exercising the right of freedom of expression and information",
        "assessment_question": "Is this data necessary for the exercise of freedom of expression or information (e.g., journalism)?",
    },
    "legal_obligation_retain": {
        "article": "Art. 17(3)(b)",
        "description": "Compliance with a legal obligation or performance of a task in the public interest",
        "assessment_question": "Is there a statutory retention requirement (e.g., Companies Act 2006 — 6 years, HMRC — 6 years, MLR 2017 — 5 years)?",
        "common_retention_periods": {
            "Companies Act 2006": "6 years",
            "HMRC tax records": "6 years from end of accounting period",
            "Money Laundering Regulations 2017": "5 years from end of business relationship",
            "Financial Conduct Authority records": "varies by record type, typically 3-6 years",
        },
    },
    "public_health": {
        "article": "Art. 17(3)(c)",
        "description": "Public interest in the area of public health per Art. 9(2)(h) and (i)",
        "assessment_question": "Is this data necessary for public health purposes?",
    },
    "archiving_research": {
        "article": "Art. 17(3)(d)",
        "description": "Archiving in the public interest, scientific/historical research, or statistical purposes under Art. 89(1)",
        "assessment_question": "Would erasure render impossible or seriously impair the achievement of archiving or research objectives?",
    },
    "legal_claims": {
        "article": "Art. 17(3)(e)",
        "description": "Establishment, exercise, or defence of legal claims",
        "assessment_question": "Are there pending or anticipated legal proceedings, regulatory investigations, or litigation holds involving this data?",
    },
}


def assess_erasure_request(
    request_date: str,
    data_subject_id: str,
    ground: str,
    ground_established: bool,
    exceptions_assessed: dict,
    data_categories: list,
    systems_holding_data: list,
    third_party_recipients: list,
) -> dict:
    """
    Assess an erasure request and produce a documented decision.

    Args:
        request_date: Date the request was received (YYYY-MM-DD).
        data_subject_id: Pseudonymised identifier for the data subject.
        ground: Key from ERASURE_GROUNDS indicating the claimed ground.
        ground_established: Whether the ground has been verified as applicable.
        exceptions_assessed: Dict mapping exception keys to True/False.
        data_categories: List of data categories held (e.g., ["identity", "financial"]).
        systems_holding_data: List of systems where data resides.
        third_party_recipients: List of third parties who received the data.

    Returns:
        Assessment decision dictionary.
    """
    req_date = datetime.strptime(request_date, "%Y-%m-%d")
    deadline = req_date + timedelta(days=30)

    assessment = {
        "reference": f"ERA-{req_date.strftime('%Y')}-{req_date.strftime('%m%d')}",
        "request_date": request_date,
        "data_subject_id": data_subject_id,
        "response_deadline": deadline.strftime("%Y-%m-%d"),
        "ground_claimed": {},
        "exceptions_assessment": [],
        "decision": "",
        "actions_required": [],
    }

    # Validate ground
    if ground not in ERASURE_GROUNDS:
        assessment["decision"] = "INVALID_GROUND"
        assessment["reasoning"] = f"Ground '{ground}' is not a recognised Art. 17(1) ground"
        return assessment

    ground_info = ERASURE_GROUNDS[ground]
    assessment["ground_claimed"] = {
        "key": ground,
        "article": ground_info["article"],
        "description": ground_info["description"],
        "established": ground_established,
    }

    if not ground_established:
        assessment["decision"] = "REFUSE"
        assessment["reasoning"] = (
            f"The ground under {ground_info['article']} has not been established. "
            f"Assessment question: {ground_info['assessment_question']}"
        )
        assessment["actions_required"] = [
            "Notify data subject of refusal with reasons",
            "Inform of right to lodge complaint with supervisory authority (Art. 77)",
            "Inform of right to judicial remedy (Art. 79)",
        ]
        return assessment

    # Assess exceptions
    any_full_exception = False
    partial_exceptions = []

    for exc_key, exc_applies in exceptions_assessed.items():
        if exc_key in ERASURE_EXCEPTIONS:
            exc_info = ERASURE_EXCEPTIONS[exc_key]
            exc_record = {
                "key": exc_key,
                "article": exc_info["article"],
                "description": exc_info["description"],
                "applies": exc_applies,
            }
            assessment["exceptions_assessment"].append(exc_record)

            if exc_applies:
                partial_exceptions.append(exc_info["article"])

    # Determine decision
    if len(partial_exceptions) > 0:
        # Check if exception covers all data or only some
        if len(partial_exceptions) >= len(data_categories):
            any_full_exception = True

    if any_full_exception:
        assessment["decision"] = "REFUSE_EXCEPTION"
        assessment["reasoning"] = (
            f"Erasure refused due to applicable exception(s): "
            f"{', '.join(partial_exceptions)}"
        )
        assessment["actions_required"] = [
            "Notify data subject of refusal citing specific exception(s)",
            "Inform of right to lodge complaint with supervisory authority (Art. 77)",
            "Inform of right to judicial remedy (Art. 79)",
        ]
    elif len(partial_exceptions) > 0:
        assessment["decision"] = "PARTIAL_ERASURE"
        assessment["reasoning"] = (
            f"Partial erasure: exception(s) {', '.join(partial_exceptions)} apply "
            f"to some data categories. Non-excepted data will be erased."
        )
        assessment["actions_required"] = build_erasure_actions(
            systems_holding_data, third_party_recipients, partial=True
        )
    else:
        assessment["decision"] = "ERASE"
        assessment["reasoning"] = (
            f"Ground {ground_info['article']} established, no exceptions apply. "
            f"Full erasure required."
        )
        assessment["actions_required"] = build_erasure_actions(
            systems_holding_data, third_party_recipients, partial=False
        )

    assessment["data_categories"] = data_categories
    assessment["systems_affected"] = systems_holding_data
    assessment["third_parties_to_notify"] = third_party_recipients

    return assessment


def build_erasure_actions(
    systems: list, third_parties: list, partial: bool
) -> list:
    """Build the list of required erasure actions."""
    prefix = "Erase non-excepted" if partial else "Erase all"
    actions = []

    for system in systems:
        actions.append(f"{prefix} personal data from {system}")

    actions.append("Flag data in backup systems for deletion at next rotation cycle (max 90 days)")
    actions.append("Purge application caches and temporary storage")

    for tp in third_parties:
        actions.append(
            f"Send Art. 19 erasure notification to {tp} — request confirmation within 14 days"
        )

    actions.extend([
        "Run verification sweep across all systems to confirm erasure",
        "Compile erasure completion record",
        "Send confirmation to data subject within response deadline",
        "Retain erasure processing record for 3 years (metadata only, no personal data)",
    ])

    if partial:
        actions.append(
            "Document which data categories are retained under exception, with legal basis"
        )

    return actions


def main():
    parser = argparse.ArgumentParser(
        description="Assess a GDPR Art. 17 erasure request"
    )
    parser.add_argument("request_date", help="Date of request (YYYY-MM-DD)")
    parser.add_argument("--subject-id", default="DS-0001", help="Data subject pseudonymised ID")
    parser.add_argument(
        "--ground",
        choices=list(ERASURE_GROUNDS.keys()),
        required=True,
        help="Erasure ground claimed",
    )
    parser.add_argument(
        "--ground-established",
        action="store_true",
        help="Flag that the erasure ground has been verified",
    )
    parser.add_argument(
        "--exception",
        action="append",
        default=[],
        help="Exception that applies (can specify multiple times)",
    )
    parser.add_argument(
        "--data-category",
        action="append",
        default=["identity", "contact", "financial", "technical"],
        help="Data category held",
    )
    parser.add_argument(
        "--system",
        action="append",
        default=["CRM", "data-warehouse", "analytics-platform"],
        help="System holding data",
    )
    parser.add_argument(
        "--third-party",
        action="append",
        default=[],
        help="Third-party recipient",
    )
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    exceptions_assessed = {}
    for exc in args.exception:
        if exc in ERASURE_EXCEPTIONS:
            exceptions_assessed[exc] = True
    for exc_key in ERASURE_EXCEPTIONS:
        if exc_key not in exceptions_assessed:
            exceptions_assessed[exc_key] = False

    result = assess_erasure_request(
        request_date=args.request_date,
        data_subject_id=args.subject_id,
        ground=args.ground,
        ground_established=args.ground_established,
        exceptions_assessed=exceptions_assessed,
        data_categories=args.data_category,
        systems_holding_data=args.system,
        third_party_recipients=args.third_party,
    )

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("=" * 60)
        print("ERASURE REQUEST ASSESSMENT")
        print("=" * 60)
        print(f"Reference:       {result['reference']}")
        print(f"Request Date:    {result['request_date']}")
        print(f"Subject ID:      {result['data_subject_id']}")
        print(f"Deadline:        {result['response_deadline']}")
        print()
        print(f"Ground:          {result['ground_claimed'].get('article', 'N/A')} — {result['ground_claimed'].get('description', 'N/A')}")
        print(f"Established:     {result['ground_claimed'].get('established', 'N/A')}")
        print()
        print(f"DECISION:        {result['decision']}")
        print(f"Reasoning:       {result['reasoning']}")
        print()
        if result.get("exceptions_assessment"):
            print("Exceptions Assessed:")
            for exc in result["exceptions_assessment"]:
                status = "APPLIES" if exc["applies"] else "Does not apply"
                print(f"  {exc['article']}: {status}")
        print()
        print("Actions Required:")
        for i, action in enumerate(result.get("actions_required", []), 1):
            print(f"  {i}. {action}")
        print("=" * 60)


if __name__ == "__main__":
    main()
