#!/usr/bin/env python3
"""
Thailand PDPA Compliance Assessment Tool

Assesses compliance with Thailand's Personal Data Protection Act B.E. 2562 (2019),
manages consent, cross-border transfers, and data subject rights.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


PDPA_LAWFUL_BASES = {
    "consent": {"section": "Section 19", "name": "Explicit consent"},
    "contract": {"section": "Section 24(3)", "name": "Contract performance"},
    "vital_interests": {"section": "Section 24(4)", "name": "Vital interests"},
    "public_task": {"section": "Section 24(4)", "name": "Public task or official authority"},
    "legitimate_interest": {"section": "Section 24(5)", "name": "Legitimate interest"},
    "legal_obligation": {"section": "Section 24(6)", "name": "Legal obligation"},
    "archiving_research": {"section": "Section 24(1)", "name": "Archiving, research, or statistics"},
}

SENSITIVE_DATA_BASES = {
    "explicit_consent": {"section": "Section 26", "name": "Explicit consent for sensitive data"},
    "vital_interests": {"section": "Section 26(1)", "name": "Prevent danger to life, body, or health"},
    "nonprofit_activities": {"section": "Section 26(2)", "name": "Lawful non-profit activities"},
    "manifestly_public": {"section": "Section 26(3)", "name": "Data manifestly made public"},
    "legal_claims": {"section": "Section 26(4)", "name": "Legal claims"},
    "employment_law": {"section": "Section 26(5)", "name": "Employment law compliance"},
}

CBT_CONDITIONS = {
    "adequacy": {"section": "Section 28(1)", "name": "Adequate protection (PDPC determination)"},
    "group_rules": {"section": "Section 28(3)", "name": "OPDPC-certified group data protection rules"},
    "contract_necessity": {"section": "Section 28(4)(a)", "name": "Contract performance with data subject"},
    "consent": {"section": "Section 28(4)(b)", "name": "Consent with inadequacy disclosure"},
    "vital_interests": {"section": "Section 28(4)(c)", "name": "Vital interests"},
    "public_interest": {"section": "Section 28(4)(d)", "name": "Important public interest"},
    "legal_claims": {"section": "Section 28(4)(e)", "name": "Legal claims"},
    "appropriate_safeguards": {"section": "Section 28(2)", "name": "PDPC-prescribed appropriate safeguards"},
}


def assess_lawful_basis(
    processing_activity: str,
    includes_sensitive: bool,
    proposed_basis: str,
    proposed_sensitive_basis: Optional[str] = None,
) -> dict:
    """Assess whether the proposed lawful basis is valid under the PDPA."""
    basis_info = PDPA_LAWFUL_BASES.get(proposed_basis)
    if not basis_info:
        return {"error": f"Unknown basis: {proposed_basis}", "valid_bases": list(PDPA_LAWFUL_BASES.keys())}

    issues = []
    if includes_sensitive:
        if proposed_sensitive_basis:
            sens_info = SENSITIVE_DATA_BASES.get(proposed_sensitive_basis)
            if not sens_info:
                issues.append(f"Unknown sensitive data basis: {proposed_sensitive_basis}")
        else:
            issues.append("Sensitive data processing requires a specific Section 26 basis")

    return {
        "processing_activity": processing_activity,
        "general_basis": basis_info,
        "sensitive_basis": SENSITIVE_DATA_BASES.get(proposed_sensitive_basis) if proposed_sensitive_basis else None,
        "includes_sensitive": includes_sensitive,
        "valid": len(issues) == 0,
        "issues": issues,
        "assessment_date": datetime.utcnow().isoformat(),
    }


def assess_cbt_mechanism(
    destination_country: str,
    transfer_purpose: str,
    has_adequacy: bool = False,
    has_group_rules: bool = False,
    is_contract_necessity: bool = False,
    has_consent: bool = False,
) -> dict:
    """Assess cross-border transfer mechanism under Section 28."""
    mechanism = None
    if has_adequacy:
        mechanism = CBT_CONDITIONS["adequacy"]
    elif is_contract_necessity:
        mechanism = CBT_CONDITIONS["contract_necessity"]
    elif has_group_rules:
        mechanism = CBT_CONDITIONS["group_rules"]
    elif has_consent:
        mechanism = CBT_CONDITIONS["consent"]

    return {
        "destination": destination_country,
        "purpose": transfer_purpose,
        "selected_mechanism": mechanism,
        "valid": mechanism is not None,
        "note": "PDPC has not published adequacy determinations as of March 2026" if not has_adequacy else None,
        "assessment_date": datetime.utcnow().isoformat(),
    }


def calculate_penalty_exposure(violation_count: int = 1) -> dict:
    """Calculate potential PDPA penalty exposure."""
    return {
        "administrative_fine": {
            "max_per_violation_thb": 5_000_000,
            "max_per_violation_usd_approx": 140_000,
            "total_exposure_thb": 5_000_000 * violation_count,
        },
        "criminal_penalties": {
            "max_imprisonment": "1 year",
            "max_fine_thb": 1_000_000,
            "applies_to": "Natural persons responsible for the violation",
        },
        "punitive_damages": {
            "max_multiplier": "2x actual damages",
            "court_awarded": True,
        },
        "violation_count": violation_count,
        "assessment_date": datetime.utcnow().isoformat(),
    }


def create_dsr_request(
    request_type: str,
    data_subject_name: str,
    request_date: Optional[str] = None,
) -> dict:
    """Create a data subject rights request under PDPA Sections 30-36."""
    dsr_types = {
        "access": {"section": "Section 30", "deadline_days": 30},
        "portability": {"section": "Section 31", "deadline_days": 30},
        "objection": {"section": "Section 32", "deadline_days": 30},
        "erasure": {"section": "Section 33", "deadline_days": 30},
        "restriction": {"section": "Section 34", "deadline_days": 30},
        "rectification": {"section": "Section 35", "deadline_days": 30},
    }

    dsr_info = dsr_types.get(request_type)
    if not dsr_info:
        return {"error": f"Unknown type: {request_type}", "valid_types": list(dsr_types.keys())}

    req_date = datetime.strptime(request_date, "%Y-%m-%d") if request_date else datetime.utcnow()
    deadline = req_date + timedelta(days=dsr_info["deadline_days"])

    return {
        "request_id": f"DSR-TH-{req_date.strftime('%Y')}-{abs(hash(data_subject_name)) % 10000:04d}",
        "request_type": request_type,
        "section": dsr_info["section"],
        "data_subject": data_subject_name,
        "request_date": req_date.strftime("%Y-%m-%d"),
        "response_deadline": deadline.strftime("%Y-%m-%d"),
        "status": "received",
    }


if __name__ == "__main__":
    print("=== Lawful Basis Assessment ===")
    result = assess_lawful_basis("Customer freight processing", False, "contract")
    print(json.dumps(result, indent=2))

    print("\n=== Cross-Border Transfer ===")
    cbt = assess_cbt_mechanism("Germany", "Transfer to EU HQ", has_consent=True)
    print(json.dumps(cbt, indent=2))

    print("\n=== Penalty Exposure ===")
    penalty = calculate_penalty_exposure(2)
    print(json.dumps(penalty, indent=2))
