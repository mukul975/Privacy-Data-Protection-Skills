#!/usr/bin/env python3
"""
Right to Object Processing Manager

Manages GDPR Article 21(1) objection requests including compelling
legitimate grounds assessment and decision documentation.
"""

import argparse
import json
from datetime import datetime, timedelta


LEGAL_BASES_OBJECTABLE = {
    "legitimate_interests": "Art. 6(1)(f)",
    "public_interest": "Art. 6(1)(e)",
}

ASSESSMENT_FACTORS = [
    "nature_and_sensitivity_of_data",
    "criticality_to_operations",
    "impact_of_cessation_on_controller",
    "impact_of_cessation_on_others",
    "safeguards_in_place",
    "subject_particular_situation",
    "subject_privacy_impact",
    "subject_vulnerability",
    "subject_specific_harm",
]


def create_objection_record(
    request_date: str,
    data_subject_id: str,
    processing_activities: list,
    legal_basis: str,
    subject_grounds: str,
) -> dict:
    """Create an objection record and initiate the assessment process."""
    req_date = datetime.strptime(request_date, "%Y-%m-%d")
    reference = f"OBJ-{req_date.strftime('%Y')}-{req_date.strftime('%m%d')}"
    response_deadline = req_date + timedelta(days=30)

    if legal_basis not in LEGAL_BASES_OBJECTABLE:
        return {
            "reference": reference,
            "decision": "NOT_APPLICABLE",
            "reasoning": (
                f"The right to object under Art. 21(1) applies only to processing "
                f"based on Art. 6(1)(e) or Art. 6(1)(f). The legal basis for this "
                f"processing is '{legal_basis}', which is not objectable under Art. 21(1)."
            ),
            "alternative_rights": [
                "If processing is based on consent: right to withdraw consent (Art. 7(3))",
                "If processing is for direct marketing: absolute right to object (Art. 21(2))",
                "Right to erasure may still be available under other Art. 17(1) grounds",
            ],
        }

    record = {
        "reference": reference,
        "request_date": request_date,
        "data_subject_id": data_subject_id,
        "response_deadline": response_deadline.strftime("%Y-%m-%d"),
        "processing_activities": processing_activities,
        "legal_basis": {
            "key": legal_basis,
            "article": LEGAL_BASES_OBJECTABLE[legal_basis],
        },
        "subject_grounds": subject_grounds,
        "status": "processing_ceased_pending_assessment",
        "immediate_actions": [
            "Cease all objected-to processing activities immediately",
            "Apply restriction under Art. 18(1)(d)",
            "Initiate compelling legitimate grounds assessment",
        ],
        "assessment_required": {
            "factors_to_evaluate": ASSESSMENT_FACTORS,
            "standard": "Compelling legitimate grounds — higher bar than standard LIA",
            "burden_of_proof": "Controller must demonstrate compelling grounds",
        },
    }

    return record


def conduct_assessment(
    reference: str,
    controller_factors: dict,
    subject_factors: dict,
    legal_claims_needed: bool = False,
) -> dict:
    """
    Conduct the compelling legitimate grounds assessment.

    Args:
        reference: Objection reference.
        controller_factors: Dict with scores (1-5) for controller position factors.
        subject_factors: Dict with scores (1-5) for data subject position factors.
        legal_claims_needed: Whether data is needed for legal claims.
    """
    controller_score = sum(controller_factors.values())
    subject_score = sum(subject_factors.values())

    assessment = {
        "reference": reference,
        "assessment_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "controller_position": {
            "factors": controller_factors,
            "total_score": controller_score,
        },
        "subject_position": {
            "factors": subject_factors,
            "total_score": subject_score,
        },
        "legal_claims_exception": legal_claims_needed,
    }

    # The compelling grounds standard requires the controller's grounds
    # to clearly override the subject's interests
    if legal_claims_needed:
        assessment["decision"] = "PARTIAL_OVERRIDE"
        assessment["reasoning"] = (
            "Processing may continue solely for the purpose of establishing, "
            "exercising, or defending legal claims. All other processing must cease."
        )
        assessment["actions"] = [
            "Continue processing only for legal claims purpose",
            "Cease all other objected-to processing",
            "Notify data subject of partial outcome",
            "Restrict data access to Legal team only for legal claims processing",
        ]
    elif controller_score > subject_score * 1.5:
        # Compelling requires a clear override — we use 1.5x threshold
        assessment["decision"] = "COMPELLING_GROUNDS_ESTABLISHED"
        assessment["reasoning"] = (
            f"Controller's compelling legitimate grounds (score: {controller_score}) "
            f"override the data subject's interests (score: {subject_score}). "
            f"The compelling standard is met."
        )
        assessment["actions"] = [
            "Resume objected-to processing",
            "Notify data subject: compelling grounds found + right to complain (Art. 77) + judicial remedy (Art. 79)",
            "Document full assessment in objection register",
        ]
    else:
        assessment["decision"] = "OBJECTION_UPHELD"
        assessment["reasoning"] = (
            f"Controller's grounds (score: {controller_score}) do not meet the "
            f"compelling standard to override the data subject's interests "
            f"(score: {subject_score}). The objection is upheld."
        )
        assessment["actions"] = [
            "Cease all objected-to processing permanently",
            "Notify data subject: objection upheld",
            "Inform subject of right to erasure under Art. 17(1)(c)",
            "Notify third-party recipients under Art. 19",
            "Update records of processing and privacy notices",
        ]

    return assessment


def main():
    parser = argparse.ArgumentParser(
        description="Manage GDPR Art. 21(1) right to object requests"
    )
    subparsers = parser.add_subparsers(dest="command")

    create_p = subparsers.add_parser("create", help="Create objection record")
    create_p.add_argument("request_date", help="Date of objection (YYYY-MM-DD)")
    create_p.add_argument("--subject-id", default="DS-0001")
    create_p.add_argument("--activity", action="append", required=True, help="Processing activity objected to")
    create_p.add_argument("--legal-basis", required=True, choices=list(LEGAL_BASES_OBJECTABLE.keys()) + ["consent", "contract", "legal_obligation"])
    create_p.add_argument("--grounds", required=True, help="Data subject's grounds for objection")

    assess_p = subparsers.add_parser("assess", help="Conduct compelling grounds assessment")
    assess_p.add_argument("--reference", required=True)
    assess_p.add_argument("--controller-score", type=int, required=True, help="Total controller position score (sum of factor scores 1-5)")
    assess_p.add_argument("--subject-score", type=int, required=True, help="Total subject position score")
    assess_p.add_argument("--legal-claims", action="store_true", help="Data needed for legal claims")

    args = parser.parse_args()

    if args.command == "create":
        result = create_objection_record(
            request_date=args.request_date,
            data_subject_id=args.subject_id,
            processing_activities=args.activity,
            legal_basis=args.legal_basis,
            subject_grounds=args.grounds,
        )
    elif args.command == "assess":
        result = conduct_assessment(
            reference=args.reference,
            controller_factors={"combined_score": args.controller_score},
            subject_factors={"combined_score": args.subject_score},
            legal_claims_needed=args.legal_claims,
        )
    else:
        parser.print_help()
        return

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
