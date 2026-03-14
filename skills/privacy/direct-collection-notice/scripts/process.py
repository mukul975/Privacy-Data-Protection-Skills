#!/usr/bin/env python3
"""
Direct Collection Information Generator

Generates Art. 13 compliant just-in-time notices and compliance
checklists for data collection points.
"""

import argparse
import json
from datetime import datetime
from typing import Optional


LEGAL_BASES = {
    "consent": "Art. 6(1)(a) — Consent",
    "contract": "Art. 6(1)(b) — Performance of a contract",
    "legal_obligation": "Art. 6(1)(c) — Legal obligation",
    "vital_interests": "Art. 6(1)(d) — Vital interests",
    "public_interest": "Art. 6(1)(e) — Public interest",
    "legitimate_interests": "Art. 6(1)(f) — Legitimate interests",
}

ART_13_CHECKLIST = {
    "13_1_a": {
        "article": "Art. 13(1)(a)",
        "element": "Controller identity and contact details",
        "required": True,
        "layer": 1,
    },
    "13_1_b": {
        "article": "Art. 13(1)(b)",
        "element": "DPO contact details",
        "required": True,
        "layer": 2,
    },
    "13_1_c": {
        "article": "Art. 13(1)(c)",
        "element": "Purposes and legal basis",
        "required": True,
        "layer": 1,
    },
    "13_1_d": {
        "article": "Art. 13(1)(d)",
        "element": "Legitimate interests (if Art. 6(1)(f))",
        "required": False,  # Only if LI is the legal basis
        "layer": 2,
    },
    "13_1_e": {
        "article": "Art. 13(1)(e)",
        "element": "Recipients or categories of recipients",
        "required": True,
        "layer": 2,
    },
    "13_1_f": {
        "article": "Art. 13(1)(f)",
        "element": "International transfers and safeguards",
        "required": False,  # Only if transfers occur
        "layer": 2,
    },
    "13_2_a": {
        "article": "Art. 13(2)(a)",
        "element": "Retention period or criteria",
        "required": True,
        "layer": 2,
    },
    "13_2_b": {
        "article": "Art. 13(2)(b)",
        "element": "Data subject rights (access, rectification, erasure, restriction, object, portability)",
        "required": True,
        "layer": 2,
    },
    "13_2_c": {
        "article": "Art. 13(2)(c)",
        "element": "Right to withdraw consent",
        "required": False,  # Only if consent is the legal basis
        "layer": 2,
    },
    "13_2_d": {
        "article": "Art. 13(2)(d)",
        "element": "Right to complain to supervisory authority",
        "required": True,
        "layer": 2,
    },
    "13_2_e": {
        "article": "Art. 13(2)(e)",
        "element": "Whether provision is statutory/contractual requirement + consequences of non-provision",
        "required": True,
        "layer": 2,
    },
    "13_2_f": {
        "article": "Art. 13(2)(f)",
        "element": "Automated decision-making (existence, logic, significance, consequences)",
        "required": False,  # Only if ADM/profiling is used
        "layer": 2,
    },
    "13_2_g": {
        "article": "Art. 13(2)(g)",
        "element": "Further processing for different purpose",
        "required": False,  # Only if further processing is intended
        "layer": 2,
    },
}


def generate_collection_point_config(
    collection_point_name: str,
    data_fields: list,
    purposes: list,
    legal_basis: str,
    legitimate_interest: Optional[str] = None,
    recipients: list = None,
    international_transfers: bool = False,
    retention_period: str = "Duration of service + 6 years",
    automated_decisions: bool = False,
    consent_based: bool = False,
) -> dict:
    """
    Generate an Art. 13 compliance configuration for a collection point.

    Args:
        collection_point_name: Name of the collection point.
        data_fields: List of data fields collected.
        purposes: List of processing purposes.
        legal_basis: Key from LEGAL_BASES.
        legitimate_interest: Description of legitimate interest (if Art. 6(1)(f)).
        recipients: List of data recipients.
        international_transfers: Whether data is transferred internationally.
        retention_period: Data retention period.
        automated_decisions: Whether automated decision-making is used.
        consent_based: Whether processing is based on consent.
    """
    config = {
        "collection_point": collection_point_name,
        "generated_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "controller": {
            "name": "Meridian Analytics Ltd",
            "address": "47 Canary Wharf Tower, London E14 5AB",
            "registration": "Company number 09847362 (England and Wales)",
        },
        "dpo": {
            "name": "Dr Sarah Chen",
            "email": "dpo@meridiananalytics.co.uk",
        },
        "data_fields": data_fields,
        "purposes": purposes,
        "legal_basis": {
            "key": legal_basis,
            "description": LEGAL_BASES.get(legal_basis, "Unknown"),
        },
        "recipients": recipients or [],
        "international_transfers": international_transfers,
        "retention_period": retention_period,
        "automated_decisions": automated_decisions,
    }

    if legal_basis == "legitimate_interests" and legitimate_interest:
        config["legitimate_interest_description"] = legitimate_interest

    # Generate checklist
    checklist = []
    for item_id, item in ART_13_CHECKLIST.items():
        required = item["required"]

        # Conditional requirements
        if item_id == "13_1_d" and legal_basis == "legitimate_interests":
            required = True
        if item_id == "13_1_f" and international_transfers:
            required = True
        if item_id == "13_2_c" and consent_based:
            required = True
        if item_id == "13_2_f" and automated_decisions:
            required = True

        checklist.append({
            "id": item_id,
            "article": item["article"],
            "element": item["element"],
            "required": required,
            "layer": item["layer"],
            "status": "pending",
        })

    config["compliance_checklist"] = checklist

    # Generate just-in-time notice
    purposes_text = ", ".join(purposes[:3])
    if len(purposes) > 3:
        purposes_text += f", and {len(purposes) - 3} other purposes"

    jit_notice = (
        f"{config['controller']['name']} will use the information you provide "
        f"to {purposes_text}. "
    )

    if consent_based:
        jit_notice += "You can withdraw your consent at any time. "

    if recipients:
        jit_notice += f"We may share your data with {', '.join(recipients[:2])}. "

    jit_notice += (
        f"Read our full privacy notice for complete details on how we use your data, "
        f"who we share it with, and your rights."
    )

    config["just_in_time_notice"] = {
        "text": jit_notice,
        "word_count": len(jit_notice.split()),
        "compliant_length": len(jit_notice.split()) <= 150,
    }

    return config


def audit_collection_point(
    collection_point_name: str,
    elements_present: dict,
    legal_basis: str = "contract",
    international_transfers: bool = False,
    automated_decisions: bool = False,
    consent_based: bool = False,
) -> dict:
    """
    Audit an existing collection point for Art. 13 compliance.

    Args:
        collection_point_name: Name of the collection point.
        elements_present: Dict mapping checklist item IDs to True/False.
        legal_basis: The legal basis used.
        international_transfers: Whether international transfers occur.
        automated_decisions: Whether ADM is used.
        consent_based: Whether consent is the legal basis.
    """
    results = []
    required_count = 0
    present_count = 0

    for item_id, item in ART_13_CHECKLIST.items():
        required = item["required"]
        if item_id == "13_1_d" and legal_basis == "legitimate_interests":
            required = True
        if item_id == "13_1_f" and international_transfers:
            required = True
        if item_id == "13_2_c" and consent_based:
            required = True
        if item_id == "13_2_f" and automated_decisions:
            required = True

        present = elements_present.get(item_id, False)

        if required:
            required_count += 1
            if present:
                present_count += 1

        results.append({
            "id": item_id,
            "article": item["article"],
            "element": item["element"],
            "required": required,
            "present": present,
            "status": "COMPLIANT" if (present or not required) else "GAP",
        })

    compliance_rate = (present_count / required_count * 100) if required_count > 0 else 100

    return {
        "collection_point": collection_point_name,
        "audit_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "required_elements": required_count,
        "present_elements": present_count,
        "compliance_rate": round(compliance_rate, 1),
        "overall_status": "COMPLIANT" if compliance_rate >= 100 else "GAPS_FOUND",
        "elements": results,
        "gaps": [r for r in results if r["status"] == "GAP"],
    }


def main():
    parser = argparse.ArgumentParser(
        description="GDPR Art. 13 direct collection information generator"
    )
    subparsers = parser.add_subparsers(dest="command")

    gen_p = subparsers.add_parser("generate", help="Generate collection point config")
    gen_p.add_argument("--name", required=True, help="Collection point name")
    gen_p.add_argument("--field", action="append", required=True, help="Data field collected")
    gen_p.add_argument("--purpose", action="append", required=True, help="Processing purpose")
    gen_p.add_argument("--legal-basis", required=True, choices=list(LEGAL_BASES.keys()))
    gen_p.add_argument("--recipient", action="append", default=[])
    gen_p.add_argument("--international-transfers", action="store_true")
    gen_p.add_argument("--automated-decisions", action="store_true")
    gen_p.add_argument("--consent-based", action="store_true")

    args = parser.parse_args()

    if args.command == "generate":
        result = generate_collection_point_config(
            collection_point_name=args.name,
            data_fields=args.field,
            purposes=args.purpose,
            legal_basis=args.legal_basis,
            recipients=args.recipient,
            international_transfers=args.international_transfers,
            automated_decisions=args.automated_decisions,
            consent_based=args.consent_based,
        )
        print(json.dumps(result, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
