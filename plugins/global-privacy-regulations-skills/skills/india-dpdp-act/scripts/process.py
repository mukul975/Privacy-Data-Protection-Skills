#!/usr/bin/env python3
"""
DPDP Act Compliance Assessment and Management Tool

Assesses compliance with India's Digital Personal Data Protection Act 2023,
manages consent and legitimate use determinations, tracks SDF obligations,
and handles data principal rights requests.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


LEGITIMATE_USES = {
    "voluntary_provision": {
        "section": "Section 7(a)",
        "name": "Specified purpose for voluntarily provided data",
        "scope": "Data principal voluntarily provides data for a specified purpose",
    },
    "state_functions": {
        "section": "Section 7(b)",
        "name": "State functions",
        "scope": "Processing by the State for subsidies, benefits, services, licences, permits",
    },
    "legal_obligation": {
        "section": "Section 7(c)",
        "name": "Compliance with legal obligation",
        "scope": "Processing under any law for compliance with judgement or order",
    },
    "medical_emergency": {
        "section": "Section 7(d)",
        "name": "Medical emergency",
        "scope": "Responding to a medical emergency involving threat to life or health",
    },
    "epidemic_disaster": {
        "section": "Section 7(e)",
        "name": "Epidemic or disaster response",
        "scope": "Processing during epidemic, outbreak, or public health threat; disaster or public order breakdown",
    },
    "employment": {
        "section": "Section 7(f)",
        "name": "Employment purposes",
        "scope": "Processing by employer for prevention of espionage, confidentiality, recruitment, attendance, assessment",
    },
    "public_interest": {
        "section": "Section 7(g)",
        "name": "Public interest (as prescribed)",
        "scope": "Processing for purposes prescribed by the Central Government",
    },
}

PENALTY_SCHEDULE = {
    "security_safeguard_failure": {
        "violation": "Failure to take reasonable security safeguards resulting in breach",
        "max_penalty_inr": 2_500_000_000,
        "max_penalty_usd_approx": 30_000_000,
    },
    "breach_notification_failure": {
        "violation": "Failure to notify Board and data principals of a breach",
        "max_penalty_inr": 2_000_000_000,
        "max_penalty_usd_approx": 24_000_000,
    },
    "children_obligation_failure": {
        "violation": "Non-fulfilment of obligations related to children",
        "max_penalty_inr": 2_000_000_000,
        "max_penalty_usd_approx": 24_000_000,
    },
    "sdf_obligation_failure": {
        "violation": "Non-fulfilment of additional SDF obligations",
        "max_penalty_inr": 1_500_000_000,
        "max_penalty_usd_approx": 18_000_000,
    },
    "other_breach": {
        "violation": "Other breaches by data fiduciary or processor",
        "max_penalty_inr": 500_000_000,
        "max_penalty_usd_approx": 6_000_000,
    },
    "data_principal_duty_breach": {
        "violation": "Breach of data principal duties",
        "max_penalty_inr": 10_000,
        "max_penalty_usd_approx": 120,
    },
}

SDF_CRITERIA = [
    "volume_of_data",
    "sensitivity_of_data",
    "risk_to_rights",
    "sovereignty_impact",
    "electoral_democracy_risk",
    "state_security_risk",
    "public_order_risk",
]


def assess_processing_ground(
    processing_activity: str,
    has_consent: bool,
    legitimate_use_type: Optional[str] = None,
    is_state_entity: bool = False,
) -> dict:
    """Assess the lawful ground for processing under Sections 6-7."""
    if has_consent:
        return {
            "processing_activity": processing_activity,
            "ground": "Consent (Section 6)",
            "valid": True,
            "requirements": [
                "Notice provided per Section 5 before consent collection",
                "Consent is free, specific, informed, unconditional, unambiguous",
                "Clear affirmative action obtained",
                "Withdrawal mechanism available (as easy as giving consent)",
                "Purpose-specific consent (no bundling)",
            ],
            "consent_manager_recommended": True,
            "assessment_date": datetime.utcnow().isoformat(),
        }

    if legitimate_use_type:
        use_info = LEGITIMATE_USES.get(legitimate_use_type)
        if not use_info:
            return {
                "valid": False,
                "error": f"Unknown legitimate use type: {legitimate_use_type}",
                "available_types": list(LEGITIMATE_USES.keys()),
            }

        if legitimate_use_type == "state_functions" and not is_state_entity:
            return {
                "valid": False,
                "error": "Section 7(b) state functions is only available to the State or its instrumentalities",
                "recommendation": "Use consent (Section 6) or another applicable legitimate use",
            }

        return {
            "processing_activity": processing_activity,
            "ground": f"Legitimate use — {use_info['name']} ({use_info['section']})",
            "valid": True,
            "scope": use_info["scope"],
            "notice_still_required": True,
            "note": "Section 5 notice requirements apply even for legitimate uses",
            "assessment_date": datetime.utcnow().isoformat(),
        }

    return {
        "valid": False,
        "error": "No valid processing ground identified. Either consent or a legitimate use must be established.",
        "recommendation": "Obtain consent per Section 6 or identify an applicable Section 7 legitimate use.",
    }


def assess_sdf_designation(
    total_data_principals: int,
    processes_sensitive_data: bool,
    risk_to_rights: str,
    sovereignty_impact: str,
) -> dict:
    """Assess likelihood of Significant Data Fiduciary designation under Section 10."""
    risk_scores = {"low": 1, "medium": 2, "high": 3}

    volume_score = 3 if total_data_principals >= 1_000_000 else (2 if total_data_principals >= 100_000 else 1)
    sensitivity_score = 3 if processes_sensitive_data else 1
    rights_score = risk_scores.get(risk_to_rights, 1)
    sovereignty_score = risk_scores.get(sovereignty_impact, 1)

    total_score = volume_score + sensitivity_score + rights_score + sovereignty_score
    max_score = 12

    if total_score >= 9:
        designation_likelihood = "HIGH"
        recommendation = "Prepare for SDF obligations: appoint DPO (India-based), engage independent auditor, initiate DPIA programme"
    elif total_score >= 6:
        designation_likelihood = "MEDIUM"
        recommendation = "Monitor Central Government notifications; begin preliminary DPO and auditor identification"
    else:
        designation_likelihood = "LOW"
        recommendation = "Continue standard data fiduciary compliance; monitor for designation criteria changes"

    return {
        "total_data_principals": total_data_principals,
        "processes_sensitive_data": processes_sensitive_data,
        "risk_to_rights": risk_to_rights,
        "sovereignty_impact": sovereignty_impact,
        "score": f"{total_score}/{max_score}",
        "designation_likelihood": designation_likelihood,
        "recommendation": recommendation,
        "sdf_obligations_if_designated": [
            "Appoint DPO based in India (Section 10(2)(a))",
            "Appoint independent data auditor (Section 10(2)(b))",
            "Conduct periodic DPIAs (Section 10(2)(c))",
            "Submit audit reports to the Board",
        ],
        "assessment_date": datetime.utcnow().isoformat(),
    }


def create_dsr_request(
    request_type: str,
    data_principal_name: str,
    data_principal_email: str,
    description: str,
    request_date: Optional[str] = None,
) -> dict:
    """Create a data principal rights request under DPDP Act."""
    dsr_types = {
        "access": {"section": "Section 11", "deadline_days": 30},
        "correction": {"section": "Section 12", "deadline_days": 30},
        "erasure": {"section": "Section 12", "deadline_days": 30},
        "grievance": {"section": "Section 13", "deadline_days": 30},
        "nomination": {"section": "Section 14", "deadline_days": 30},
    }

    dsr_info = dsr_types.get(request_type)
    if not dsr_info:
        return {"error": f"Unknown DSR type: {request_type}", "valid_types": list(dsr_types.keys())}

    req_date = datetime.strptime(request_date, "%Y-%m-%d") if request_date else datetime.utcnow()
    deadline = req_date + timedelta(days=dsr_info["deadline_days"])

    return {
        "request_id": f"DPR-IN-{req_date.strftime('%Y')}-{abs(hash(data_principal_email + str(req_date))) % 10000:04d}",
        "request_type": request_type,
        "section": dsr_info["section"],
        "data_principal": {"name": data_principal_name, "email": data_principal_email},
        "description": description,
        "request_date": req_date.strftime("%Y-%m-%d"),
        "response_deadline": deadline.strftime("%Y-%m-%d"),
        "status": "received",
        "assessment_date": datetime.utcnow().isoformat(),
    }


def calculate_penalty_exposure(
    violation_type: str,
    violation_count: int = 1,
) -> dict:
    """Calculate potential DPBI penalty exposure under the DPDP Act Schedule."""
    penalty_info = PENALTY_SCHEDULE.get(violation_type)
    if not penalty_info:
        return {
            "error": f"Unknown violation type: {violation_type}",
            "available_types": list(PENALTY_SCHEDULE.keys()),
        }

    return {
        "violation_type": violation_type,
        "violation_description": penalty_info["violation"],
        "violation_count": violation_count,
        "max_penalty_per_violation_inr": penalty_info["max_penalty_inr"],
        "max_penalty_per_violation_usd": penalty_info["max_penalty_usd_approx"],
        "total_exposure_inr": penalty_info["max_penalty_inr"] * violation_count,
        "total_exposure_usd": penalty_info["max_penalty_usd_approx"] * violation_count,
        "note": "Actual penalty determined by Board considering: nature, gravity, significance, repetitive nature, and financial gain",
        "appeals_to": "Telecom Disputes Settlement and Appellate Tribunal (TDSAT)",
        "assessment_date": datetime.utcnow().isoformat(),
    }


def assess_children_compliance(
    processes_children_data: bool,
    has_age_verification: bool,
    has_parental_consent: bool,
    has_tracking_profiling: bool,
    has_targeted_advertising: bool,
) -> dict:
    """Assess compliance with Section 9 children's data requirements."""
    issues = []
    if processes_children_data:
        if not has_age_verification:
            issues.append("Age verification mechanism not implemented (Section 9 requirement)")
        if not has_parental_consent:
            issues.append("Verifiable parental consent mechanism not in place (Section 9(1))")
        if has_tracking_profiling:
            issues.append("Tracking or behavioural monitoring of children is prohibited (Section 9(3))")
        if has_targeted_advertising:
            issues.append("Targeted advertising directed at children is prohibited (Section 9(3))")

    return {
        "processes_children_data": processes_children_data,
        "age_threshold": 18,
        "compliant": len(issues) == 0,
        "issues": issues,
        "requirements": [
            "Verifiable parental consent before processing child's data",
            "No tracking, behavioural monitoring, or targeted advertising to children",
            "No processing detrimental to child's well-being",
            "Age verification at data collection points",
        ] if processes_children_data else ["No children's data processed — requirements not applicable"],
        "assessment_date": datetime.utcnow().isoformat(),
    }


if __name__ == "__main__":
    print("=== Processing Ground Assessment ===")
    result = assess_processing_ground(
        processing_activity="Employee payroll processing",
        has_consent=False,
        legitimate_use_type="employment",
    )
    print(json.dumps(result, indent=2))

    print("\n=== SDF Designation Assessment ===")
    sdf = assess_sdf_designation(
        total_data_principals=500_000,
        processes_sensitive_data=True,
        risk_to_rights="medium",
        sovereignty_impact="low",
    )
    print(json.dumps(sdf, indent=2))

    print("\n=== Penalty Exposure ===")
    penalty = calculate_penalty_exposure("security_safeguard_failure", 1)
    print(json.dumps(penalty, indent=2))

    print("\n=== Children's Compliance Assessment ===")
    children = assess_children_compliance(
        processes_children_data=False,
        has_age_verification=False,
        has_parental_consent=False,
        has_tracking_profiling=False,
        has_targeted_advertising=False,
    )
    print(json.dumps(children, indent=2))
