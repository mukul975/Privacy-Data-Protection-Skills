#!/usr/bin/env python3
"""
LGPD Compliance Assessment and Management Tool

Assesses compliance with Brazil's Lei Geral de Proteção de Dados (Lei 13.709/2018),
tracks lawful basis determinations, manages data subject rights requests,
and monitors ANPD enforcement requirements.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


LGPD_LAWFUL_BASES_ART7 = {
    "consent": {
        "article": "Art. 7, I",
        "name": "Consent of the data subject",
        "requires_consent_record": True,
        "requires_ripd": False,
        "applies_to_sensitive": True,
        "sensitive_article": "Art. 11, I",
        "key_requirements": [
            "Free, informed, and unequivocal expression of will",
            "Written consent in a separate clause from other contractual terms (Art. 8, §1)",
            "Burden of proof on the controller (Art. 8, §2)",
            "Must be specific to each processing purpose",
            "Revocable at any time via facilitated procedure (Art. 8, §5)",
        ],
    },
    "legal_obligation": {
        "article": "Art. 7, II",
        "name": "Compliance with legal or regulatory obligation",
        "requires_consent_record": False,
        "requires_ripd": False,
        "applies_to_sensitive": True,
        "sensitive_article": "Art. 11, II(a)",
        "key_requirements": [
            "Specific Brazilian law or regulation mandating the processing",
            "Document the legal provision requiring processing",
            "Processing limited to what the law requires",
        ],
    },
    "public_policy": {
        "article": "Art. 7, III",
        "name": "Execution of public policies (public administration only)",
        "requires_consent_record": False,
        "requires_ripd": False,
        "applies_to_sensitive": True,
        "sensitive_article": "Art. 11, II(b)",
        "key_requirements": [
            "Only available to public administration bodies",
            "Must be provided in laws, regulations, or supported by contracts",
            "Not applicable to private-sector controllers",
        ],
    },
    "research": {
        "article": "Art. 7, IV",
        "name": "Research by research bodies",
        "requires_consent_record": False,
        "requires_ripd": False,
        "applies_to_sensitive": True,
        "sensitive_article": "Art. 11, II(c)",
        "key_requirements": [
            "Conducted by a recognized research body",
            "Anonymisation of personal data whenever possible",
            "Subject to ethics committee oversight",
        ],
    },
    "contract_performance": {
        "article": "Art. 7, V",
        "name": "Contract performance or preliminary procedures",
        "requires_consent_record": False,
        "requires_ripd": False,
        "applies_to_sensitive": False,
        "sensitive_article": None,
        "key_requirements": [
            "Data subject is a party to the contract",
            "Processing is necessary for contract execution",
            "At the request of the data subject",
        ],
    },
    "exercise_of_rights": {
        "article": "Art. 7, VI",
        "name": "Exercise of rights in proceedings",
        "requires_consent_record": False,
        "requires_ripd": False,
        "applies_to_sensitive": True,
        "sensitive_article": "Art. 11, II(d)",
        "key_requirements": [
            "Judicial, administrative, or arbitration proceedings",
            "Processing is necessary for the regular exercise of rights",
            "Data retained only for the duration needed for the proceedings",
        ],
    },
    "protection_of_life": {
        "article": "Art. 7, VII",
        "name": "Protection of life or physical safety",
        "requires_consent_record": False,
        "requires_ripd": False,
        "applies_to_sensitive": True,
        "sensitive_article": "Art. 11, II(e)",
        "key_requirements": [
            "Genuine emergency situation",
            "Consent cannot reasonably be obtained",
            "Processing limited to what is necessary for protection",
        ],
    },
    "health_protection": {
        "article": "Art. 7, VIII",
        "name": "Health protection",
        "requires_consent_record": False,
        "requires_ripd": False,
        "applies_to_sensitive": True,
        "sensitive_article": "Art. 11, II(f)",
        "key_requirements": [
            "Exclusively in procedures by health professionals or health authorities",
            "Must be carried out by health services or health authorities",
            "Not available to non-health-sector controllers",
        ],
    },
    "legitimate_interest": {
        "article": "Art. 7, IX",
        "name": "Legitimate interest of controller or third party",
        "requires_consent_record": False,
        "requires_ripd": True,
        "applies_to_sensitive": False,
        "sensitive_article": None,
        "key_requirements": [
            "Based on concrete situations (Art. 10)",
            "Only strictly necessary data processed",
            "Transparency measures required",
            "Four-step balancing test: purpose, necessity, balance, safeguards",
            "RIPD recommended and may be requested by ANPD (Art. 10, §3)",
        ],
    },
    "credit_protection": {
        "article": "Art. 7, X",
        "name": "Credit protection",
        "requires_consent_record": False,
        "requires_ripd": False,
        "applies_to_sensitive": False,
        "sensitive_article": None,
        "key_requirements": [
            "Processing relates to credit risk assessment",
            "Compliance with Lei 12.414/2011 (Positive Credit Registry)",
            "No equivalent in GDPR — unique to LGPD",
        ],
    },
}

DSR_TYPES = {
    "confirmation": {
        "article": "Art. 18, I",
        "deadline_days": 15,
        "description": "Confirmation of the existence of processing",
    },
    "access": {
        "article": "Art. 18, II",
        "deadline_days": 15,
        "description": "Access to personal data",
    },
    "correction": {
        "article": "Art. 18, III",
        "deadline_days": 15,
        "description": "Correction of incomplete, inaccurate, or out-of-date data",
    },
    "anonymisation_blocking_deletion": {
        "article": "Art. 18, IV",
        "deadline_days": 15,
        "description": "Anonymisation, blocking, or deletion of unnecessary or excessive data",
    },
    "portability": {
        "article": "Art. 18, V",
        "deadline_days": 15,
        "description": "Portability of data to another service provider",
    },
    "deletion_consent": {
        "article": "Art. 18, VI",
        "deadline_days": 15,
        "description": "Deletion of data processed with consent",
    },
    "sharing_info": {
        "article": "Art. 18, VII",
        "deadline_days": 15,
        "description": "Information about entities with which data was shared",
    },
    "consent_denial_info": {
        "article": "Art. 18, VIII",
        "deadline_days": 0,
        "description": "Information about consequences of denying consent",
    },
    "consent_revocation": {
        "article": "Art. 18, IX",
        "deadline_days": 0,
        "description": "Revocation of consent",
    },
    "automated_decision_review": {
        "article": "Art. 20",
        "deadline_days": 15,
        "description": "Review of automated decision-making",
    },
}

ANPD_SANCTIONS = {
    "warning": {
        "severity": 1,
        "description": "Warning with deadline for corrective measures",
        "financial_impact": 0,
    },
    "simple_fine": {
        "severity": 2,
        "description": "Up to 2% of revenue in Brazil per violation, max R$50M",
        "max_amount_brl": 50_000_000,
        "max_percentage": 2.0,
    },
    "daily_fine": {
        "severity": 3,
        "description": "Daily fine to compel compliance, subject to R$50M cap",
        "max_amount_brl": 50_000_000,
    },
    "public_disclosure": {
        "severity": 4,
        "description": "Public disclosure of the violation after confirmation",
        "financial_impact": "reputational",
    },
    "data_blocking": {
        "severity": 5,
        "description": "Blocking of personal data until regularisation",
        "financial_impact": "operational",
    },
    "data_deletion": {
        "severity": 6,
        "description": "Deletion of personal data related to the violation",
        "financial_impact": "operational",
    },
    "database_suspension": {
        "severity": 7,
        "description": "Partial suspension of database operation for up to 6 months",
        "financial_impact": "operational",
    },
    "processing_suspension": {
        "severity": 8,
        "description": "Suspension of processing activity for up to 6 months",
        "financial_impact": "operational",
    },
    "processing_prohibition": {
        "severity": 9,
        "description": "Partial or total prohibition of processing activities",
        "financial_impact": "operational_critical",
    },
}


def assess_lawful_basis(
    processing_activity: str,
    data_categories: list,
    includes_sensitive_data: bool,
    proposed_basis: str,
    is_public_administration: bool = False,
) -> dict:
    """Assess whether the proposed lawful basis is valid for the processing activity."""
    basis_info = LGPD_LAWFUL_BASES_ART7.get(proposed_basis)
    if not basis_info:
        return {
            "valid": False,
            "error": f"Unknown lawful basis: {proposed_basis}",
            "available_bases": list(LGPD_LAWFUL_BASES_ART7.keys()),
        }

    issues = []
    warnings = []
    recommendations = []

    if proposed_basis == "public_policy" and not is_public_administration:
        issues.append(
            "Art. 7, III (public policy) is available only to public administration bodies. "
            "Private-sector controllers must select an alternative basis."
        )

    if proposed_basis == "health_protection":
        warnings.append(
            "Art. 7, VIII (health protection) is restricted to procedures by health "
            "professionals, health services, or health authorities. Verify the processing "
            "entity qualifies under this restriction."
        )

    if includes_sensitive_data and not basis_info["applies_to_sensitive"]:
        issues.append(
            f"The proposed basis ({basis_info['article']}) does not support sensitive data "
            f"processing under Art. 11. Sensitive data requires one of the bases enumerated "
            f"in Art. 11."
        )

    if proposed_basis == "legitimate_interest" and includes_sensitive_data:
        issues.append(
            "Legitimate interest (Art. 7, IX) cannot be used for sensitive data processing. "
            "Select an Art. 11 basis instead."
        )

    if proposed_basis == "credit_protection" and includes_sensitive_data:
        issues.append(
            "Credit protection (Art. 7, X) cannot be used for sensitive data processing. "
            "Select an Art. 11 basis instead."
        )

    if basis_info["requires_ripd"]:
        recommendations.append(
            "This lawful basis triggers a recommendation to prepare a RIPD (Relatório de "
            "Impacto à Proteção de Dados Pessoais) per Art. 10, §3 and Art. 38."
        )

    if basis_info["requires_consent_record"]:
        recommendations.append(
            "Implement a consent management mechanism with: standalone consent clause, "
            "timestamp recording, purpose-specific granularity, and facilitated revocation."
        )

    if proposed_basis == "legitimate_interest":
        recommendations.append(
            "Conduct and document the four-step legitimate interest assessment per ANPD "
            "guidance: (1) purpose identification, (2) necessity test, (3) balancing test, "
            "(4) safeguards implementation."
        )

    return {
        "processing_activity": processing_activity,
        "proposed_basis": proposed_basis,
        "basis_name": basis_info["name"],
        "article": basis_info["article"],
        "valid": len(issues) == 0,
        "includes_sensitive_data": includes_sensitive_data,
        "sensitive_basis": basis_info["sensitive_article"] if includes_sensitive_data else None,
        "issues": issues,
        "warnings": warnings,
        "recommendations": recommendations,
        "key_requirements": basis_info["key_requirements"],
        "assessment_date": datetime.utcnow().isoformat(),
    }


def create_dsr_request(
    request_type: str,
    data_subject_name: str,
    data_subject_email: str,
    description: str,
    request_date: Optional[str] = None,
) -> dict:
    """Create and track a data subject rights request under LGPD Arts. 17-22."""
    dsr_info = DSR_TYPES.get(request_type)
    if not dsr_info:
        return {
            "error": f"Unknown DSR type: {request_type}",
            "available_types": list(DSR_TYPES.keys()),
        }

    if request_date:
        req_date = datetime.strptime(request_date, "%Y-%m-%d")
    else:
        req_date = datetime.utcnow()

    deadline_days = dsr_info["deadline_days"]
    if deadline_days > 0:
        deadline = req_date + timedelta(days=deadline_days)
    else:
        deadline = req_date

    request_id = f"DSR-BR-{req_date.strftime('%Y')}-{abs(hash(data_subject_email + str(req_date)))  % 10000:04d}"

    return {
        "request_id": request_id,
        "request_type": request_type,
        "lgpd_article": dsr_info["article"],
        "description": dsr_info["description"],
        "data_subject": {
            "name": data_subject_name,
            "email": data_subject_email,
        },
        "request_details": description,
        "request_date": req_date.strftime("%Y-%m-%d"),
        "response_deadline": deadline.strftime("%Y-%m-%d"),
        "deadline_days": deadline_days,
        "status": "received",
        "identity_verified": False,
        "workflow_steps": _generate_dsr_workflow(request_type),
        "created_at": datetime.utcnow().isoformat(),
    }


def _generate_dsr_workflow(request_type: str) -> list:
    """Generate the workflow steps for a DSR type."""
    base_steps = [
        {"step": 1, "action": "Verify data subject identity", "status": "pending"},
        {"step": 2, "action": "Search all systems for subject data", "status": "pending"},
        {"step": 3, "action": "Assess exemptions (legal retention, proceedings)", "status": "pending"},
    ]

    type_specific = {
        "confirmation": [
            {"step": 4, "action": "Generate confirmation of processing existence", "status": "pending"},
        ],
        "access": [
            {"step": 4, "action": "Compile complete data export from all systems", "status": "pending"},
            {"step": 5, "action": "Format in structured format (JSON/PDF)", "status": "pending"},
        ],
        "correction": [
            {"step": 4, "action": "Validate correction request against source records", "status": "pending"},
            {"step": 5, "action": "Update records across all systems", "status": "pending"},
            {"step": 6, "action": "Notify third-party recipients of correction", "status": "pending"},
        ],
        "deletion_consent": [
            {"step": 4, "action": "Identify data processed under consent basis", "status": "pending"},
            {"step": 5, "action": "Execute deletion workflows", "status": "pending"},
            {"step": 6, "action": "Document retained data under legal obligation exemption", "status": "pending"},
            {"step": 7, "action": "Notify third-party recipients per Art. 18, §6", "status": "pending"},
        ],
        "portability": [
            {"step": 4, "action": "Export data in machine-readable format (JSON/CSV)", "status": "pending"},
            {"step": 5, "action": "Transfer to designated recipient controller or provide to subject", "status": "pending"},
        ],
        "automated_decision_review": [
            {"step": 4, "action": "Identify the automated decision and model used", "status": "pending"},
            {"step": 5, "action": "Prepare explanation of decision criteria", "status": "pending"},
            {"step": 6, "action": "Conduct human review of the decision", "status": "pending"},
            {"step": 7, "action": "Communicate reviewed or confirmed decision", "status": "pending"},
        ],
    }

    specific = type_specific.get(request_type, [
        {"step": 4, "action": f"Fulfil {request_type} request", "status": "pending"},
    ])

    final_steps = [
        {"step": len(base_steps) + len(specific) + 1, "action": "Deliver response to data subject", "status": "pending"},
        {"step": len(base_steps) + len(specific) + 2, "action": "Record response in DSR register", "status": "pending"},
    ]

    return base_steps + specific + final_steps


def calculate_fine_exposure(
    annual_revenue_brl: float,
    violation_count: int = 1,
    severity: str = "medium",
    has_privacy_programme: bool = False,
    timely_corrective_action: bool = False,
    recidivist: bool = False,
) -> dict:
    """Calculate potential ANPD fine exposure under Art. 52 and dosimetry regulation."""
    max_percentage = 2.0
    max_fine_per_violation = 50_000_000.0

    severity_multipliers = {
        "light": 0.25,
        "medium": 0.50,
        "severe": 0.75,
        "very_severe": 1.0,
    }

    multiplier = severity_multipliers.get(severity, 0.50)

    base_fine = annual_revenue_brl * (max_percentage / 100) * multiplier

    if has_privacy_programme:
        base_fine *= 0.80
    if timely_corrective_action:
        base_fine *= 0.85
    if recidivist:
        base_fine *= 1.50

    fine_per_violation = min(base_fine, max_fine_per_violation)
    total_exposure = fine_per_violation * violation_count
    total_capped = min(total_exposure, max_fine_per_violation * violation_count)

    return {
        "annual_revenue_brl": annual_revenue_brl,
        "severity": severity,
        "violation_count": violation_count,
        "severity_multiplier": multiplier,
        "mitigating_factors": {
            "privacy_programme": has_privacy_programme,
            "corrective_action": timely_corrective_action,
        },
        "aggravating_factors": {
            "recidivist": recidivist,
        },
        "fine_per_violation_brl": round(fine_per_violation, 2),
        "total_exposure_brl": round(total_capped, 2),
        "statutory_cap_per_violation_brl": max_fine_per_violation,
        "percentage_of_revenue": round(
            (fine_per_violation / annual_revenue_brl) * 100, 4
        ) if annual_revenue_brl > 0 else 0,
        "assessment_date": datetime.utcnow().isoformat(),
    }


def assess_transfer_mechanism(
    destination_country: str,
    data_categories: list,
    transfer_purpose: str,
    has_adequacy_decision: bool = False,
    has_sccs: bool = False,
    has_bcr: bool = False,
    has_specific_consent: bool = False,
) -> dict:
    """Assess the appropriate international transfer mechanism under Art. 33."""
    mechanisms_available = []
    recommended_mechanism = None
    issues = []

    if has_adequacy_decision:
        mechanisms_available.append({
            "mechanism": "Adequacy decision (Art. 33, I)",
            "status": "available",
            "note": "Verify the ANPD adequacy determination covers the relevant data categories",
        })
        recommended_mechanism = "Adequacy decision"

    if has_sccs:
        mechanisms_available.append({
            "mechanism": "ANPD-approved standard contractual clauses (Art. 33, II(b))",
            "status": "available",
            "note": "Ensure SCCs conform to ANPD Resolution CD/ANPD No. 19/2024",
        })
        if not recommended_mechanism:
            recommended_mechanism = "Standard contractual clauses"

    if has_bcr:
        mechanisms_available.append({
            "mechanism": "Global corporate rules (Art. 33, II(c))",
            "status": "available",
            "note": "ANPD BCR approval mechanism is pending formal establishment as of March 2026",
        })
        if not recommended_mechanism:
            recommended_mechanism = "Global corporate rules"

    if has_specific_consent:
        mechanisms_available.append({
            "mechanism": "Specific consent (Art. 33, VIII)",
            "status": "available",
            "note": "Data subject must be specifically informed about the international nature of the transfer",
        })
        if not recommended_mechanism:
            recommended_mechanism = "Specific consent"

    if not mechanisms_available:
        issues.append(
            "No valid transfer mechanism identified under Art. 33. The international "
            "transfer cannot proceed without an adequate legal basis."
        )

    if not has_adequacy_decision:
        issues.append(
            "The ANPD has not issued any adequacy decisions as of March 2026. "
            "Alternative mechanisms under Art. 33, II-VIII must be used."
        )

    return {
        "destination_country": destination_country,
        "data_categories": data_categories,
        "transfer_purpose": transfer_purpose,
        "mechanisms_available": mechanisms_available,
        "recommended_mechanism": recommended_mechanism,
        "issues": issues,
        "requires_tia": True,
        "tia_note": "A transfer impact assessment is recommended for all international transfers regardless of mechanism",
        "assessment_date": datetime.utcnow().isoformat(),
    }


def generate_compliance_dashboard(
    processing_activities: list,
    dsr_requests: list,
    transfer_records: list,
    ripd_records: list,
) -> dict:
    """Generate an LGPD compliance dashboard summary."""
    basis_distribution = {}
    for activity in processing_activities:
        basis = activity.get("lawful_basis", "unspecified")
        basis_distribution[basis] = basis_distribution.get(basis, 0) + 1

    total_dsr = len(dsr_requests)
    dsr_by_type = {}
    dsr_overdue = 0
    for req in dsr_requests:
        req_type = req.get("request_type", "unknown")
        dsr_by_type[req_type] = dsr_by_type.get(req_type, 0) + 1
        if req.get("status") != "completed":
            deadline = datetime.strptime(req["response_deadline"], "%Y-%m-%d")
            if deadline < datetime.utcnow():
                dsr_overdue += 1

    transfers_by_country = {}
    transfers_by_mechanism = {}
    for transfer in transfer_records:
        country = transfer.get("destination_country", "unknown")
        transfers_by_country[country] = transfers_by_country.get(country, 0) + 1
        mechanism = transfer.get("mechanism", "unknown")
        transfers_by_mechanism[mechanism] = transfers_by_mechanism.get(mechanism, 0) + 1

    ripd_by_status = {"current": 0, "overdue_review": 0}
    for ripd in ripd_records:
        review_date = datetime.strptime(ripd.get("next_review", "2099-01-01"), "%Y-%m-%d")
        if review_date < datetime.utcnow():
            ripd_by_status["overdue_review"] += 1
        else:
            ripd_by_status["current"] += 1

    return {
        "dashboard_date": datetime.utcnow().isoformat(),
        "processing_activities": {
            "total": len(processing_activities),
            "by_lawful_basis": basis_distribution,
        },
        "data_subject_requests": {
            "total": total_dsr,
            "by_type": dsr_by_type,
            "overdue": dsr_overdue,
            "compliance_rate": round(
                ((total_dsr - dsr_overdue) / total_dsr) * 100, 1
            ) if total_dsr > 0 else 100.0,
        },
        "international_transfers": {
            "total": len(transfer_records),
            "by_country": transfers_by_country,
            "by_mechanism": transfers_by_mechanism,
        },
        "ripd_status": ripd_by_status,
        "overall_health": _calculate_health_score(dsr_overdue, total_dsr, ripd_by_status),
    }


def _calculate_health_score(dsr_overdue: int, total_dsr: int, ripd_status: dict) -> str:
    """Calculate overall compliance health score."""
    issues = 0
    if dsr_overdue > 0:
        issues += 2
    if ripd_status.get("overdue_review", 0) > 0:
        issues += 1
    if total_dsr == 0:
        issues += 0

    if issues == 0:
        return "GREEN — All compliance indicators within acceptable parameters"
    elif issues <= 1:
        return "AMBER — Minor compliance gaps identified; remediation recommended within 30 days"
    else:
        return "RED — Significant compliance gaps; immediate remediation required"


if __name__ == "__main__":
    print("=== LGPD Lawful Basis Assessment ===")
    result = assess_lawful_basis(
        processing_activity="Customer credit scoring for trade credit applications",
        data_categories=["name", "cpf", "payment_history", "credit_score"],
        includes_sensitive_data=False,
        proposed_basis="credit_protection",
    )
    print(json.dumps(result, indent=2))

    print("\n=== Data Subject Rights Request ===")
    dsr = create_dsr_request(
        request_type="access",
        data_subject_name="João Silva",
        data_subject_email="joao.silva@zenithglobal.com.br",
        description="Request for access to all personal data processed by Zenith Global Enterprises",
    )
    print(json.dumps(dsr, indent=2))

    print("\n=== ANPD Fine Exposure Calculation ===")
    fine = calculate_fine_exposure(
        annual_revenue_brl=500_000_000,
        violation_count=1,
        severity="severe",
        has_privacy_programme=True,
        timely_corrective_action=False,
        recidivist=False,
    )
    print(json.dumps(fine, indent=2))

    print("\n=== International Transfer Assessment ===")
    transfer = assess_transfer_mechanism(
        destination_country="Germany",
        data_categories=["customer_name", "shipping_address", "contact_details"],
        transfer_purpose="Transfer to EU headquarters for global logistics coordination",
        has_sccs=True,
    )
    print(json.dumps(transfer, indent=2))
