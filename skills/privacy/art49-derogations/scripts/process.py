#!/usr/bin/env python3
"""
Article 49 Derogation Assessment Engine

Evaluates the applicability of GDPR Article 49 derogation conditions
for international data transfers and generates compliance documentation.
"""

import json
from datetime import datetime
from typing import Optional


DEROGATIONS = {
    "art49_1_a": {
        "name": "Explicit Consent",
        "article": "Art. 49(1)(a)",
        "conditions": [
            "Data subject has explicitly consented to the transfer",
            "Data subject informed of destination country lacking adequacy decision",
            "Data subject informed of absence of appropriate safeguards",
            "Data subject informed of specific risks of the transfer",
            "Consent is specific to the transfer (not general processing consent)",
            "Consent is freely given (no power imbalance, no detriment for refusal)",
            "Withdrawal mechanism is available and as easy as giving consent",
        ],
        "restrictions": [
            "Cannot be used for systematic, repetitive, or large-scale transfers",
            "Not appropriate in employment context due to power imbalance",
            "Cannot substitute for establishing Art. 46 safeguards",
        ],
    },
    "art49_1_b": {
        "name": "Contract Performance with Data Subject",
        "article": "Art. 49(1)(b)",
        "conditions": [
            "Contract exists directly between data subject and controller",
            "Transfer is objectively necessary for contract performance",
            "Close and substantial connection between transfer and contractual obligation",
            "Transfer is occasional, not systematic or continuous",
            "Only data necessary for the specific obligation is transferred",
        ],
        "restrictions": [
            "Contract must be with the data subject, not a third party",
            "Commercial necessity alone is insufficient; must be contractual necessity",
            "Cannot be used if alternative performance methods avoid the transfer",
        ],
    },
    "art49_1_c": {
        "name": "Contract in Interest of Data Subject",
        "article": "Art. 49(1)(c)",
        "conditions": [
            "Contract exists between controller and another person",
            "Contract is concluded in the interest of the data subject",
            "Transfer is objectively necessary for the contract",
            "Transfer is occasional, not systematic",
        ],
        "restrictions": [
            "Must demonstrate the contract genuinely serves the data subject's interests",
            "Controller's commercial interest alone is insufficient",
        ],
    },
    "art49_1_d": {
        "name": "Important Public Interest",
        "article": "Art. 49(1)(d)",
        "conditions": [
            "Public interest recognised in EU or Member State law",
            "Public interest is of important (significant) nature",
            "Transfer is necessary to serve the identified public interest",
            "Transfer is by a public authority or body acting in public capacity",
        ],
        "restrictions": [
            "Private companies cannot invoke for commercial purposes",
            "Public interest must be explicitly recognised in law",
            "Trivial or minor public interests do not qualify",
        ],
    },
    "art49_1_e": {
        "name": "Legal Claims",
        "article": "Art. 49(1)(e)",
        "conditions": [
            "Actual or concretely contemplated legal proceedings exist",
            "Transfer is necessary for establishment, exercise, or defence of the claim",
            "Only data relevant to the legal claim is transferred",
            "Transfer is linked to specific proceedings (occasional)",
        ],
        "restrictions": [
            "Theoretical or speculative possibility of proceedings is insufficient",
            "Cannot be used as a routine transfer basis for ongoing legal operations",
        ],
    },
    "art49_1_f": {
        "name": "Vital Interests",
        "article": "Art. 49(1)(f)",
        "conditions": [
            "Transfer is necessary to protect vital interests (life-threatening situation)",
            "Data subject is physically or legally incapable of giving consent",
            "Only data strictly necessary for protecting vital interests is transferred",
        ],
        "restrictions": [
            "Very narrow application — genuine emergency situations only",
            "Not applicable where consent could be obtained",
        ],
    },
    "art49_1_g": {
        "name": "Public Register",
        "article": "Art. 49(1)(g)",
        "conditions": [
            "Register is established by EU or Member State law for public information",
            "Register is open to public consultation",
            "Conditions for access set by law are fulfilled",
            "Transfer does not involve the entirety of the register",
        ],
        "restrictions": [
            "Only specific entries, not bulk register copies",
            "Consultation conditions must be met by the requester",
        ],
    },
    "art49_1_compelling": {
        "name": "Compelling Legitimate Interests (Last Resort)",
        "article": "Art. 49(1) second subparagraph",
        "conditions": [
            "No other Art. 49 derogation applies",
            "No Art. 45 adequacy decision or Art. 46 safeguards available",
            "Transfer is not repetitive (one-time or very occasional)",
            "Transfer concerns a limited number of data subjects",
            "Compelling legitimate interest identified (higher bar than Art. 6(1)(f))",
            "Balancing test: interests not overridden by data subject rights",
            "Suitable safeguards provided for the transfer",
            "Supervisory authority notified of the transfer",
            "Data subject informed of transfer and compelling interests",
            "Assessment documented in Art. 30 records",
        ],
        "restrictions": [
            "Absolute last resort — all other options exhausted",
            "Not for regular, repeated, or bulk transfers",
            "SA notification is mandatory before transfer",
        ],
    },
}


def assess_derogation_applicability(
    derogation_key: str, condition_assessment: dict
) -> dict:
    """Assess whether a specific Art. 49 derogation is applicable."""
    derogation = DEROGATIONS.get(derogation_key)
    if not derogation:
        return {"error": f"Unknown derogation: {derogation_key}"}

    conditions = derogation["conditions"]
    met_conditions = []
    unmet_conditions = []

    for condition in conditions:
        if condition_assessment.get(condition, False):
            met_conditions.append(condition)
        else:
            unmet_conditions.append(condition)

    all_met = len(unmet_conditions) == 0
    pct = round(len(met_conditions) / len(conditions) * 100, 1) if conditions else 0

    return {
        "derogation": derogation["name"],
        "article": derogation["article"],
        "assessment_date": datetime.utcnow().isoformat(),
        "total_conditions": len(conditions),
        "conditions_met": len(met_conditions),
        "conditions_unmet": len(unmet_conditions),
        "unmet_conditions": unmet_conditions,
        "compliance_pct": pct,
        "applicable": all_met,
        "restrictions": derogation["restrictions"],
        "recommendation": f"Derogation under {derogation['article']} is applicable"
        if all_met
        else f"Derogation under {derogation['article']} is NOT applicable — "
        f"{len(unmet_conditions)} condition(s) not met",
    }


def find_applicable_derogation(transfer_characteristics: dict) -> dict:
    """Determine which Art. 49 derogation(s) may apply to a transfer."""
    results = {
        "assessment_date": datetime.utcnow().isoformat(),
        "transfer_summary": transfer_characteristics,
        "potentially_applicable": [],
        "not_applicable": [],
    }

    is_systematic = transfer_characteristics.get("systematic", False)
    is_large_scale = transfer_characteristics.get("large_scale", False)
    has_ds_contract = transfer_characteristics.get("direct_contract_with_ds", False)
    has_explicit_consent = transfer_characteristics.get("explicit_consent_obtainable", False)
    has_public_interest_law = transfer_characteristics.get("public_interest_in_law", False)
    has_legal_proceedings = transfer_characteristics.get("actual_legal_proceedings", False)
    is_vital_emergency = transfer_characteristics.get("vital_interests_emergency", False)
    is_public_register = transfer_characteristics.get("from_public_register", False)
    has_third_party_contract_for_ds = transfer_characteristics.get(
        "third_party_contract_in_ds_interest", False
    )
    is_employment = transfer_characteristics.get("employment_context", False)

    if is_systematic or is_large_scale:
        results["preliminary_note"] = (
            "WARNING: Transfer appears systematic or large-scale. "
            "Art. 49 derogations are generally NOT available for such transfers. "
            "Establish Art. 46 safeguards instead."
        )

    if has_explicit_consent and not is_employment and not is_systematic:
        results["potentially_applicable"].append(
            {"derogation": "art49_1_a", "name": "Explicit Consent", "article": "Art. 49(1)(a)"}
        )
    else:
        reasons = []
        if is_employment:
            reasons.append("Employment context — consent unlikely to be freely given")
        if is_systematic:
            reasons.append("Systematic transfer — consent derogation not for routine transfers")
        if not has_explicit_consent:
            reasons.append("Explicit consent not obtainable")
        results["not_applicable"].append(
            {"derogation": "art49_1_a", "reasons": reasons}
        )

    if has_ds_contract and not is_systematic:
        results["potentially_applicable"].append(
            {
                "derogation": "art49_1_b",
                "name": "Contract Performance",
                "article": "Art. 49(1)(b)",
            }
        )
    else:
        results["not_applicable"].append(
            {
                "derogation": "art49_1_b",
                "reasons": ["No direct contract with data subject" if not has_ds_contract else "Systematic transfer"],
            }
        )

    if has_third_party_contract_for_ds and not is_systematic:
        results["potentially_applicable"].append(
            {
                "derogation": "art49_1_c",
                "name": "Contract in DS Interest",
                "article": "Art. 49(1)(c)",
            }
        )

    if has_public_interest_law:
        results["potentially_applicable"].append(
            {
                "derogation": "art49_1_d",
                "name": "Important Public Interest",
                "article": "Art. 49(1)(d)",
            }
        )

    if has_legal_proceedings:
        results["potentially_applicable"].append(
            {
                "derogation": "art49_1_e",
                "name": "Legal Claims",
                "article": "Art. 49(1)(e)",
            }
        )

    if is_vital_emergency:
        results["potentially_applicable"].append(
            {
                "derogation": "art49_1_f",
                "name": "Vital Interests",
                "article": "Art. 49(1)(f)",
            }
        )

    if is_public_register:
        results["potentially_applicable"].append(
            {
                "derogation": "art49_1_g",
                "name": "Public Register",
                "article": "Art. 49(1)(g)",
            }
        )

    if not results["potentially_applicable"] and not is_systematic and not is_large_scale:
        results["potentially_applicable"].append(
            {
                "derogation": "art49_1_compelling",
                "name": "Compelling Legitimate Interests (Last Resort)",
                "article": "Art. 49(1) second subparagraph",
                "note": "Last resort — SA notification mandatory",
            }
        )

    return results


def generate_derogation_record(
    transfer_ref: str,
    derogation_key: str,
    exporter: str,
    importer: str,
    destination_country: str,
    data_categories: list,
    justification: str,
    why_art45_46_unavailable: str,
    data_subjects_affected: int,
    assessed_by: str,
) -> dict:
    """Generate a formal Art. 49 derogation documentation record."""
    derogation = DEROGATIONS.get(derogation_key, {})
    return {
        "record_reference": transfer_ref,
        "derogation": derogation.get("name", derogation_key),
        "article": derogation.get("article", "Art. 49"),
        "record_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "exporter": exporter,
        "importer": importer,
        "destination_country": destination_country,
        "data_categories": data_categories,
        "data_subjects_affected": data_subjects_affected,
        "justification": justification,
        "why_art45_46_unavailable": why_art45_46_unavailable,
        "occasional_nature_confirmed": True,
        "data_minimisation_confirmed": True,
        "assessed_by": assessed_by,
        "sa_notification_required": derogation_key == "art49_1_compelling",
        "retain_until": "Duration of data retention plus 5 years for enforcement limitation",
    }


if __name__ == "__main__":
    print("=== Derogation Applicability Assessment ===")
    transfer_chars = {
        "systematic": False,
        "large_scale": False,
        "direct_contract_with_ds": True,
        "explicit_consent_obtainable": True,
        "public_interest_in_law": False,
        "actual_legal_proceedings": False,
        "vital_interests_emergency": False,
        "from_public_register": False,
        "third_party_contract_in_ds_interest": False,
        "employment_context": False,
    }
    result = find_applicable_derogation(transfer_chars)
    print(json.dumps(result, indent=2))

    print("\n=== Specific Derogation Assessment — Contract Necessity ===")
    conditions = {
        "Contract exists directly between data subject and controller": True,
        "Transfer is objectively necessary for contract performance": True,
        "Close and substantial connection between transfer and contractual obligation": True,
        "Transfer is occasional, not systematic or continuous": True,
        "Only data necessary for the specific obligation is transferred": True,
    }
    assessment = assess_derogation_applicability("art49_1_b", conditions)
    print(json.dumps(assessment, indent=2))
