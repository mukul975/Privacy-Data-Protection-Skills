#!/usr/bin/env python3
"""
Indirect Collection Information Manager

Manages GDPR Article 14 notification obligations for personal data
obtained from sources other than the data subject, including timing
calculation, exemption assessment, and notice generation.
"""

import argparse
import json
from datetime import datetime, timedelta
from typing import Optional


ART_14_ELEMENTS = [
    {"id": "14_1_a", "article": "Art. 14(1)(a)", "element": "Controller identity and contact details"},
    {"id": "14_1_b", "article": "Art. 14(1)(b)", "element": "DPO contact details"},
    {"id": "14_1_c", "article": "Art. 14(1)(c)", "element": "Purposes and legal basis"},
    {"id": "14_1_d", "article": "Art. 14(1)(d)", "element": "Categories of personal data concerned"},
    {"id": "14_1_e", "article": "Art. 14(1)(e)", "element": "Recipients or categories of recipients"},
    {"id": "14_1_f", "article": "Art. 14(1)(f)", "element": "International transfers and safeguards"},
    {"id": "14_2_a", "article": "Art. 14(2)(a)", "element": "Retention period or criteria"},
    {"id": "14_2_b", "article": "Art. 14(2)(b)", "element": "Legitimate interests (if Art. 6(1)(f))"},
    {"id": "14_2_c", "article": "Art. 14(2)(c)", "element": "Data subject rights"},
    {"id": "14_2_d", "article": "Art. 14(2)(d)", "element": "Right to withdraw consent (if applicable)"},
    {"id": "14_2_e", "article": "Art. 14(2)(e)", "element": "Right to complain to supervisory authority"},
    {"id": "14_2_f", "article": "Art. 14(2)(f)", "element": "Source of data and whether publicly accessible"},
    {"id": "14_2_g", "article": "Art. 14(2)(g)", "element": "Automated decision-making (if applicable)"},
]

EXEMPTIONS = {
    "already_has_info": {
        "article": "Art. 14(5)(a)",
        "description": "Data subject already has the information",
        "documentation": "Source and date of prior information, confirmation of equivalent content",
    },
    "disproportionate_effort": {
        "article": "Art. 14(5)(b)",
        "description": "Provision is impossible or involves disproportionate effort",
        "documentation": "Written proportionality assessment approved by DPO, compensatory measures implemented",
        "compensatory_measures": [
            "Publish information on controller's website",
            "Make information available on request",
        ],
    },
    "legal_requirement": {
        "article": "Art. 14(5)(c)",
        "description": "Obtaining or disclosure expressly required by law",
        "documentation": "Citation of specific legal provision",
    },
    "professional_secrecy": {
        "article": "Art. 14(5)(d)",
        "description": "Data must remain confidential under statutory professional secrecy",
        "documentation": "Citation of statutory secrecy obligation",
    },
}


def calculate_notification_deadline(
    receipt_date: str,
    used_for_communication: bool = False,
    first_communication_date: Optional[str] = None,
    disclosed_to_recipient: bool = False,
    first_disclosure_date: Optional[str] = None,
) -> dict:
    """Calculate the Art. 14(3) notification deadline."""
    recv_date = datetime.strptime(receipt_date, "%Y-%m-%d")
    default_deadline = recv_date + timedelta(days=30)  # Max 1 month

    deadlines = [
        {
            "rule": "Art. 14(3)(a) — Within reasonable period, max 1 month",
            "deadline": default_deadline.strftime("%Y-%m-%d"),
        }
    ]

    applicable_deadline = default_deadline

    if used_for_communication and first_communication_date:
        comm_date = datetime.strptime(first_communication_date, "%Y-%m-%d")
        deadlines.append({
            "rule": "Art. 14(3)(b) — At or before first communication",
            "deadline": comm_date.strftime("%Y-%m-%d"),
        })
        if comm_date < applicable_deadline:
            applicable_deadline = comm_date

    if disclosed_to_recipient and first_disclosure_date:
        disc_date = datetime.strptime(first_disclosure_date, "%Y-%m-%d")
        deadlines.append({
            "rule": "Art. 14(3)(c) — At or before first disclosure",
            "deadline": disc_date.strftime("%Y-%m-%d"),
        })
        if disc_date < applicable_deadline:
            applicable_deadline = disc_date

    return {
        "receipt_date": receipt_date,
        "deadlines_assessed": deadlines,
        "applicable_deadline": applicable_deadline.strftime("%Y-%m-%d"),
        "days_until_deadline": (applicable_deadline - datetime.utcnow()).days,
    }


def assess_exemption(
    exemption_type: str,
    data_subject_count: int = 0,
    data_age_months: int = 0,
    alternative_contact_available: bool = True,
    justification: str = "",
) -> dict:
    """Assess whether an Art. 14(5) exemption applies."""
    if exemption_type not in EXEMPTIONS:
        return {"valid": False, "error": f"Unknown exemption type: {exemption_type}"}

    exemption = EXEMPTIONS[exemption_type]
    assessment = {
        "exemption": exemption["article"],
        "description": exemption["description"],
        "documentation_required": exemption["documentation"],
        "justification": justification,
    }

    if exemption_type == "disproportionate_effort":
        # Proportionality factors
        factors = {
            "data_subject_count": data_subject_count,
            "data_age_months": data_age_months,
            "alternative_contact_available": alternative_contact_available,
        }

        # Simple scoring: higher score = more likely disproportionate
        score = 0
        if data_subject_count > 10000:
            score += 3
        elif data_subject_count > 1000:
            score += 2
        elif data_subject_count > 100:
            score += 1

        if data_age_months > 24:
            score += 2
        elif data_age_months > 12:
            score += 1

        if not alternative_contact_available:
            score += 2

        assessment["proportionality_factors"] = factors
        assessment["proportionality_score"] = score
        assessment["recommendation"] = (
            "Disproportionate effort likely justified"
            if score >= 5
            else "Disproportionate effort may be justified — requires detailed DPO assessment"
            if score >= 3
            else "Disproportionate effort unlikely to be justified — provide Art. 14 notice"
        )
        assessment["valid"] = score >= 5
        assessment["compensatory_measures"] = exemption.get("compensatory_measures", [])
    else:
        assessment["valid"] = True  # Other exemptions are binary — either they apply or not
        assessment["note"] = "Controller must document that this exemption applies to the specific circumstances"

    return assessment


def generate_art14_notice(
    data_source: str,
    data_source_type: str,
    categories: list,
    purposes: list,
    legal_basis: str,
) -> dict:
    """Generate an Art. 14 notification template."""
    notice = {
        "notice_type": "Art. 14 GDPR — Indirect Collection Information Notice",
        "generated_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "controller": {
            "name": "Meridian Analytics Ltd",
            "address": "47 Canary Wharf Tower, London E14 5AB",
            "registration": "Company number 09847362",
        },
        "dpo": {
            "name": "Dr Sarah Chen",
            "email": "dpo@meridiananalytics.co.uk",
        },
        "source": {
            "identity": data_source,
            "type": data_source_type,
            "publicly_accessible": data_source_type == "public_registry",
        },
        "data_categories": categories,
        "purposes": purposes,
        "legal_basis": legal_basis,
        "elements_included": [e["article"] + " — " + e["element"] for e in ART_14_ELEMENTS],
    }

    return notice


def main():
    parser = argparse.ArgumentParser(
        description="GDPR Art. 14 indirect collection information manager"
    )
    subparsers = parser.add_subparsers(dest="command")

    deadline_p = subparsers.add_parser("deadline", help="Calculate notification deadline")
    deadline_p.add_argument("receipt_date", help="Date data was received (YYYY-MM-DD)")
    deadline_p.add_argument("--communication-date", help="Date of first communication (YYYY-MM-DD)")
    deadline_p.add_argument("--disclosure-date", help="Date of first disclosure (YYYY-MM-DD)")

    exempt_p = subparsers.add_parser("exemption", help="Assess Art. 14(5) exemption")
    exempt_p.add_argument("--type", required=True, choices=list(EXEMPTIONS.keys()))
    exempt_p.add_argument("--subject-count", type=int, default=0)
    exempt_p.add_argument("--data-age-months", type=int, default=0)
    exempt_p.add_argument("--no-contact", action="store_true")
    exempt_p.add_argument("--justification", default="")

    args = parser.parse_args()

    if args.command == "deadline":
        result = calculate_notification_deadline(
            receipt_date=args.receipt_date,
            used_for_communication=bool(args.communication_date),
            first_communication_date=args.communication_date,
            disclosed_to_recipient=bool(args.disclosure_date),
            first_disclosure_date=args.disclosure_date,
        )
    elif args.command == "exemption":
        result = assess_exemption(
            exemption_type=args.type,
            data_subject_count=args.subject_count,
            data_age_months=args.data_age_months,
            alternative_contact_available=not args.no_contact,
            justification=args.justification,
        )
    else:
        parser.print_help()
        return

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
