#!/usr/bin/env python3
"""
PIPEDA Compliance Manager

Manages Personal Information Protection and Electronic Documents Act
(PIPEDA) compliance operations including access requests, consent
tracking, breach assessment, and cross-border transfer evaluation.
"""

import argparse
import json
from datetime import datetime, timedelta
from typing import Optional


FAIR_INFORMATION_PRINCIPLES = {
    "accountability": {
        "clause": "4.1",
        "title": "Accountability",
        "description": "Organization is responsible for PI under its control and must designate a privacy officer.",
    },
    "identifying_purposes": {
        "clause": "4.2",
        "title": "Identifying Purposes",
        "description": "Purposes for collection must be identified at or before time of collection.",
    },
    "consent": {
        "clause": "4.3",
        "title": "Consent",
        "description": "Knowledge and consent of the individual required for collection, use, or disclosure.",
    },
    "limiting_collection": {
        "clause": "4.4",
        "title": "Limiting Collection",
        "description": "Collection limited to what is necessary for identified purposes.",
    },
    "limiting_use_disclosure_retention": {
        "clause": "4.5",
        "title": "Limiting Use, Disclosure, and Retention",
        "description": "PI not used or disclosed for purposes other than those for which it was collected.",
    },
    "accuracy": {
        "clause": "4.6",
        "title": "Accuracy",
        "description": "PI shall be accurate, complete, and up-to-date as necessary for its purposes.",
    },
    "safeguards": {
        "clause": "4.7",
        "title": "Safeguards",
        "description": "PI protected by security safeguards appropriate to sensitivity.",
    },
    "openness": {
        "clause": "4.8",
        "title": "Openness",
        "description": "Organization makes its PI policies and practices readily available.",
    },
    "individual_access": {
        "clause": "4.9",
        "title": "Individual Access",
        "description": "Individual informed of existence, use, and disclosure of their PI and given access.",
    },
    "challenging_compliance": {
        "clause": "4.10",
        "title": "Challenging Compliance",
        "description": "Individual can challenge compliance with principles to designated accountable person.",
    },
}

CONSENT_EXCEPTIONS = [
    {
        "section": "7(1)(a)",
        "description": "Collection clearly in the interest of the individual and consent cannot be obtained in a timely way",
    },
    {
        "section": "7(1)(b)",
        "description": "Collection reasonable for investigation of breach of agreement or law",
    },
    {
        "section": "7(1)(c)",
        "description": "Collection for journalistic, artistic, or literary purpose",
    },
    {
        "section": "7(1)(d)",
        "description": "Information is publicly available as specified in regulations",
    },
    {
        "section": "7(2)(a)",
        "description": "Use for purpose individual would consider reasonable in the circumstances",
    },
    {
        "section": "7(3)(c)",
        "description": "Disclosure required by law (subpoena, warrant, court order)",
    },
    {
        "section": "7(3)(d)",
        "description": "Disclosure to government institution for law enforcement or national security",
    },
    {
        "section": "7(3)(e)",
        "description": "Disclosure for emergency threatening life, health, or security",
    },
]

ACCESS_REFUSAL_GROUNDS = [
    {"section": "9(3)(a)", "description": "Information subject to solicitor-client privilege"},
    {"section": "9(3)(b)", "description": "Disclosure would reveal confidential commercial information"},
    {"section": "9(3)(c)", "description": "Information could threaten life or security of another individual"},
    {
        "section": "9(3)(d)",
        "description": "Information collected for investigation of breach of agreement or law",
    },
    {
        "section": "9(3)(e)",
        "description": "Information generated in formal dispute resolution process",
    },
]

RROSH_HARM_TYPES = [
    "Bodily harm",
    "Humiliation",
    "Damage to reputation or relationships",
    "Loss of employment, business, or professional opportunities",
    "Financial loss",
    "Identity theft",
    "Negative effects on credit record",
    "Damage to or loss of property",
]

SENSITIVITY_LEVELS = {
    "high": {
        "examples": ["health data", "financial information", "children's data", "biometric data", "SIN"],
        "consent_required": "express",
    },
    "medium": {
        "examples": ["employment data", "precise location", "browsing history"],
        "consent_required": "express_or_implied",
    },
    "low": {
        "examples": ["business contact information", "publicly available data", "name and address"],
        "consent_required": "implied_or_opt_out",
    },
}


def create_access_request(
    request_date: str,
    requester_name: str,
    organization: str,
    request_scope: str = "full",
) -> dict:
    """Create a PIPEDA individual access request record."""
    req_date = datetime.strptime(request_date, "%Y-%m-%d")
    deadline = req_date + timedelta(days=30)
    reference = f"PIPEDA-AR-{req_date.strftime('%Y%m%d')}"

    record = {
        "reference": reference,
        "request_date": request_date,
        "requester_name": requester_name,
        "organization": organization,
        "request_scope": request_scope,
        "legal_basis": "PIPEDA Schedule 1, Clause 4.9 (Individual Access)",
        "response_deadline": deadline.strftime("%Y-%m-%d"),
        "response_deadline_days": 30,
        "status": "received",
        "verification": {"status": "pending", "method": "to_be_determined"},
        "cost": "Minimal or no cost (Section 8(3))",
        "format": "Generally understandable form",
        "refusal_grounds_to_check": ACCESS_REFUSAL_GROUNDS,
        "response_must_include": [
            "Existence of personal information held",
            "Account of use and disclosure of personal information",
            "Copy of personal information",
            "Information about any third parties to whom information has been disclosed",
        ],
        "if_refused": {
            "obligations": [
                "Provide written reasons for refusal",
                "Inform individual of right to complain to OPC",
                "Provide OPC contact information",
            ]
        },
    }

    return record


def assess_breach_rrosh(
    breach_date: str,
    information_types: list,
    num_affected: int,
    breach_type: str = "unauthorized_access",
    encryption_at_rest: bool = False,
) -> dict:
    """Assess whether a breach creates a Real Risk of Significant Harm (RROSH)."""
    b_date = datetime.strptime(breach_date, "%Y-%m-%d")
    reference = f"PIPEDA-BR-{b_date.strftime('%Y%m%d')}"

    sensitivity_score = 0
    for info_type in information_types:
        info_lower = info_type.lower()
        if any(term in info_lower for term in ["health", "financial", "sin", "social insurance", "biometric", "child"]):
            sensitivity_score += 3
        elif any(term in info_lower for term in ["employment", "location", "browsing"]):
            sensitivity_score += 2
        else:
            sensitivity_score += 1

    misuse_probability = "high"
    if encryption_at_rest and breach_type == "loss":
        misuse_probability = "low"
    elif breach_type in ("theft", "unauthorized_access"):
        misuse_probability = "high"
    elif breach_type == "accidental_disclosure":
        misuse_probability = "medium"

    rrosh_determination = False
    if sensitivity_score >= 3 and misuse_probability in ("high", "medium"):
        rrosh_determination = True
    if num_affected > 500 and misuse_probability != "low":
        rrosh_determination = True
    if sensitivity_score >= 6:
        rrosh_determination = True

    record = {
        "reference": reference,
        "breach_date": breach_date,
        "breach_type": breach_type,
        "information_types": information_types,
        "num_affected": num_affected,
        "encryption_at_rest": encryption_at_rest,
        "assessment": {
            "sensitivity_score": sensitivity_score,
            "misuse_probability": misuse_probability,
            "rrosh_determination": rrosh_determination,
        },
        "potential_harms": RROSH_HARM_TYPES,
        "record_retention": "24 months from determination date (Section 10.3)",
    }

    if rrosh_determination:
        record["required_actions"] = {
            "report_to_opc": {
                "required": True,
                "section": "10.1",
                "timing": "As soon as feasible",
                "contents": [
                    "Description of circumstances and cause",
                    "Date or period of breach",
                    "Description of personal information involved",
                    "Number of affected individuals",
                    "Steps taken to reduce or mitigate harm",
                    "Whether individuals have been notified",
                    "Contact person for OPC inquiries",
                ],
            },
            "notify_individuals": {
                "required": True,
                "section": "10.1(4)",
                "timing": "As soon as feasible after RROSH determination",
                "contents": [
                    "Description of breach",
                    "Personal information involved",
                    "Steps organization has taken",
                    "Steps individual can take to reduce risk",
                    "Contact information for further inquiries",
                ],
            },
            "notify_other_organizations": {
                "required": "If notification may reduce risk of harm",
                "section": "10.2",
            },
        }
    else:
        record["required_actions"] = {
            "report_to_opc": {"required": False},
            "notify_individuals": {"required": False},
            "maintain_record": {
                "required": True,
                "section": "10.3",
                "duration": "24 months",
            },
        }

    return record


def assess_consent_requirement(
    information_type: str,
    purpose: str,
    is_sensitive: bool = False,
) -> dict:
    """Determine the consent requirement for a given collection scenario."""
    if is_sensitive:
        sensitivity = "high"
    else:
        info_lower = information_type.lower()
        if any(term in info_lower for term in ["health", "financial", "sin", "biometric", "child"]):
            sensitivity = "high"
        elif any(term in info_lower for term in ["employment", "location", "browsing"]):
            sensitivity = "medium"
        else:
            sensitivity = "low"

    level_info = SENSITIVITY_LEVELS[sensitivity]

    result = {
        "information_type": information_type,
        "purpose": purpose,
        "sensitivity_level": sensitivity,
        "consent_type_required": level_info["consent_required"],
        "sensitivity_examples": level_info["examples"],
        "consent_exceptions_to_check": CONSENT_EXCEPTIONS,
        "opc_meaningful_consent_requirements": [
            "Emphasize key elements (what, with whom, for what, risks)",
            "Allow individuals to control level of detail",
            "Provide clear yes/no options",
            "Be innovative about consent mechanisms",
            "Consider consumer perspective",
            "Make consent an ongoing process",
            "Document consent records for accountability",
        ],
        "legal_reference": "PIPEDA Section 6.1, Schedule 1 Clause 4.3",
    }

    return result


def generate_principles_checklist(organization: str) -> dict:
    """Generate a PIPEDA fair information principles compliance checklist."""
    checklist = {
        "organization": organization,
        "generated_date": datetime.now().strftime("%Y-%m-%d"),
        "legal_framework": "PIPEDA Schedule 1 (CSA Model Code CAN/CSA-Q830-96)",
        "principles": {},
    }

    compliance_items = {
        "accountability": [
            "Privacy officer designated with name and contact published",
            "Written privacy policies and procedures in place",
            "Complaint-handling procedures documented",
            "Staff privacy training programme active",
            "Third-party processor agreements include privacy obligations",
        ],
        "identifying_purposes": [
            "Purposes documented before or at time of collection",
            "New purposes identified and fresh consent obtained before use",
            "Purpose limitation documented in data inventory",
        ],
        "consent": [
            "Consent type appropriate to sensitivity of information",
            "Consent mechanism provides clear yes/no choice",
            "Withdrawal mechanism available and equally easy",
            "Consent records maintained with timestamps",
            "OPC meaningful consent guidelines followed",
        ],
        "limiting_collection": [
            "Each data element tied to documented purpose",
            "No indiscriminate or excessive collection",
            "Collection methods fair and lawful",
        ],
        "limiting_use_disclosure_retention": [
            "Use limited to identified purposes or with fresh consent",
            "Retention schedule defined and enforced",
            "Destruction procedures documented and followed",
        ],
        "accuracy": [
            "Information kept accurate for decision-making purposes",
            "Individuals can request correction of inaccuracies",
            "Correction requests processed within 30 days",
        ],
        "safeguards": [
            "Physical safeguards appropriate to sensitivity",
            "Organizational safeguards (access controls, training, NDAs)",
            "Technological safeguards (encryption, firewalls, audit trails)",
            "Regular security assessments conducted",
        ],
        "openness": [
            "Privacy policy publicly available and easily understandable",
            "Policy describes types of PI held and general uses",
            "Privacy officer contact information published",
        ],
        "individual_access": [
            "Access request process documented and publicized",
            "Responses provided within 30 days",
            "Minimal or no cost to individuals",
            "Refusal grounds applied only where permitted under Section 9(3)",
        ],
        "challenging_compliance": [
            "Complaint procedure in place and accessible",
            "All complaints investigated",
            "Corrective measures implemented where warranted",
            "OPC complaint route communicated to individuals",
        ],
    }

    for principle_key, principle_info in FAIR_INFORMATION_PRINCIPLES.items():
        checklist["principles"][principle_key] = {
            "clause": principle_info["clause"],
            "title": principle_info["title"],
            "description": principle_info["description"],
            "compliance_items": [
                {"item": item, "status": "not_assessed"}
                for item in compliance_items.get(principle_key, [])
            ],
        }

    return checklist


def main():
    parser = argparse.ArgumentParser(
        description="PIPEDA compliance operations manager"
    )
    subparsers = parser.add_subparsers(dest="command", help="Operation to perform")

    # Access request subcommand
    access_parser = subparsers.add_parser("access-request", help="Create an access request record")
    access_parser.add_argument("request_date", help="Date of request (YYYY-MM-DD)")
    access_parser.add_argument("--requester", required=True, help="Requester name")
    access_parser.add_argument("--organization", required=True, help="Organization name")
    access_parser.add_argument("--scope", default="full", choices=["full", "specific", "correction"])

    # Breach assessment subcommand
    breach_parser = subparsers.add_parser("breach-assess", help="Assess breach RROSH")
    breach_parser.add_argument("breach_date", help="Date of breach (YYYY-MM-DD)")
    breach_parser.add_argument("--info-types", nargs="+", required=True, help="Types of PI involved")
    breach_parser.add_argument("--num-affected", type=int, required=True, help="Number of individuals affected")
    breach_parser.add_argument("--breach-type", default="unauthorized_access",
                               choices=["unauthorized_access", "theft", "loss", "accidental_disclosure"])
    breach_parser.add_argument("--encrypted", action="store_true", help="Data was encrypted at rest")

    # Consent assessment subcommand
    consent_parser = subparsers.add_parser("consent-assess", help="Assess consent requirements")
    consent_parser.add_argument("--info-type", required=True, help="Type of information")
    consent_parser.add_argument("--purpose", required=True, help="Purpose of collection")
    consent_parser.add_argument("--sensitive", action="store_true", help="Information is sensitive")

    # Checklist subcommand
    checklist_parser = subparsers.add_parser("checklist", help="Generate principles compliance checklist")
    checklist_parser.add_argument("--organization", required=True, help="Organization name")

    args = parser.parse_args()

    if args.command == "access-request":
        result = create_access_request(
            request_date=args.request_date,
            requester_name=args.requester,
            organization=args.organization,
            request_scope=args.scope,
        )
    elif args.command == "breach-assess":
        result = assess_breach_rrosh(
            breach_date=args.breach_date,
            information_types=args.info_types,
            num_affected=args.num_affected,
            breach_type=args.breach_type,
            encryption_at_rest=args.encrypted,
        )
    elif args.command == "consent-assess":
        result = assess_consent_requirement(
            information_type=args.info_type,
            purpose=args.purpose,
            is_sensitive=args.sensitive,
        )
    elif args.command == "checklist":
        result = generate_principles_checklist(organization=args.organization)
    else:
        parser.print_help()
        return

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
