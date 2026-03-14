#!/usr/bin/env python3
"""
Transfer Records and Documentation Management Engine

Manages cross-border transfer registers, audit trails, compliance
documentation packages, and review cycles under GDPR Chapter V.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


TRANSFER_MECHANISMS = {
    "adequacy": {
        "name": "Adequacy Decision (Art. 45)",
        "requires_tia": False,
        "requires_supplementary_measures": False,
        "documentation": ["adequacy_decision_reference", "scope_assessment", "monitoring_log"],
    },
    "sccs": {
        "name": "Standard Contractual Clauses (Art. 46(2)(c))",
        "requires_tia": True,
        "requires_supplementary_measures": True,
        "documentation": [
            "executed_sccs", "tia_document", "supplementary_measures_record",
            "due_diligence_record", "annex_review_log", "sub_processor_list",
        ],
    },
    "bcr": {
        "name": "Binding Corporate Rules (Art. 47)",
        "requires_tia": True,
        "requires_supplementary_measures": True,
        "documentation": [
            "approved_bcr_text", "bcr_member_list", "compliance_audit_reports",
            "training_records", "complaint_handling_log", "update_log",
        ],
    },
    "derogation": {
        "name": "Art. 49 Derogation",
        "requires_tia": False,
        "requires_supplementary_measures": False,
        "documentation": [
            "derogation_assessment", "necessity_analysis",
            "data_subject_information", "dpa_notification", "transfer_log",
        ],
    },
    "dpf": {
        "name": "EU-US Data Privacy Framework (Adequacy Decision 2023/1795)",
        "requires_tia": False,
        "requires_supplementary_measures": False,
        "documentation": [
            "dpf_certification_verification", "scope_assessment",
            "monitoring_log", "contingency_plan",
        ],
    },
}

RISK_WEIGHTS = {
    "special_category_data": 2.0,
    "large_volume": 1.5,
    "non_adequate_country": 2.0,
    "government_access_risk": 2.5,
    "no_tia": 3.0,
    "stale_tia": 1.5,
    "no_supplementary_measures": 2.0,
    "derogation_basis": 1.5,
}


def create_transfer_entry(
    transfer_id: str,
    exporter_name: str,
    exporter_country: str,
    importer_name: str,
    importer_country: str,
    data_subjects: list,
    data_categories: list,
    special_category: bool,
    purpose: str,
    legal_basis: str,
    mechanism: str,
    mechanism_reference: str,
    tia_reference: Optional[str] = None,
    supplementary_measures: Optional[list] = None,
    retention_period: str = "Duration of contract + 1 year",
    review_months: int = 12,
) -> dict:
    """Create a new transfer register entry with all mandatory fields."""
    mech_info = TRANSFER_MECHANISMS.get(mechanism)
    if not mech_info:
        return {"error": f"Unknown mechanism '{mechanism}'. Valid: {list(TRANSFER_MECHANISMS.keys())}"}

    now = datetime.utcnow()
    review_date = now + timedelta(days=review_months * 30)

    entry = {
        "transfer_id": transfer_id,
        "exporter": {"name": exporter_name, "country": exporter_country},
        "importer": {"name": importer_name, "country": importer_country},
        "data_subjects": data_subjects,
        "data_categories": data_categories,
        "special_category_data": special_category,
        "purpose": purpose,
        "legal_basis": legal_basis,
        "mechanism": {
            "type": mechanism,
            "name": mech_info["name"],
            "reference": mechanism_reference,
        },
        "tia_reference": tia_reference,
        "supplementary_measures": supplementary_measures or [],
        "retention_period": retention_period,
        "review_date": review_date.strftime("%Y-%m-%d"),
        "status": "Active",
        "created_date": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "created_by": "system",
    }

    # Validate completeness
    gaps = []
    if mech_info["requires_tia"] and not tia_reference:
        gaps.append("TIA required but not provided")
    if mech_info["requires_supplementary_measures"] and not supplementary_measures:
        gaps.append("Supplementary measures required but not documented")

    entry["completeness"] = {
        "mandatory_fields_complete": len(gaps) == 0,
        "gaps": gaps,
        "required_documentation": mech_info["documentation"],
    }

    return entry


def assess_risk_rating(
    special_category: bool = False,
    volume_above_threshold: bool = False,
    adequate_country: bool = True,
    government_access_risk: bool = False,
    tia_completed: bool = True,
    tia_current: bool = True,
    supplementary_measures_in_place: bool = True,
    derogation_basis: bool = False,
) -> dict:
    """Calculate a risk rating for a transfer based on weighted risk factors."""
    score = 0.0
    factors = []

    if special_category:
        score += RISK_WEIGHTS["special_category_data"]
        factors.append("Special category data involved")
    if volume_above_threshold:
        score += RISK_WEIGHTS["large_volume"]
        factors.append("Large volume of data subjects")
    if not adequate_country:
        score += RISK_WEIGHTS["non_adequate_country"]
        factors.append("Destination is non-adequate country")
    if government_access_risk:
        score += RISK_WEIGHTS["government_access_risk"]
        factors.append("Significant government access risk in destination")
    if not tia_completed:
        score += RISK_WEIGHTS["no_tia"]
        factors.append("No TIA completed")
    elif not tia_current:
        score += RISK_WEIGHTS["stale_tia"]
        factors.append("TIA is stale (not refreshed after material change)")
    if not supplementary_measures_in_place and not adequate_country:
        score += RISK_WEIGHTS["no_supplementary_measures"]
        factors.append("No supplementary measures despite non-adequate destination")
    if derogation_basis:
        score += RISK_WEIGHTS["derogation_basis"]
        factors.append("Transfer relies on Art. 49 derogation")

    if score <= 2.0:
        rating = "Low"
    elif score <= 5.0:
        rating = "Medium"
    elif score <= 8.0:
        rating = "High"
    else:
        rating = "Critical"

    recommended_review = {
        "Low": 12,
        "Medium": 6,
        "High": 3,
        "Critical": 1,
    }

    return {
        "risk_score": round(score, 1),
        "risk_rating": rating,
        "risk_factors": factors,
        "recommended_review_months": recommended_review[rating],
    }


def create_audit_entry(
    transfer_id: str,
    event_type: str,
    details: dict,
    actor: str,
) -> dict:
    """Create an immutable audit trail entry for a transfer record change."""
    valid_event_types = [
        "transfer_created", "transfer_modified", "mechanism_changed",
        "tia_completed", "tia_updated", "review_conducted",
        "transfer_suspended", "transfer_terminated", "document_attached",
        "sa_inquiry_received", "supplementary_measure_added",
        "supplementary_measure_removed", "risk_rating_changed",
    ]

    if event_type not in valid_event_types:
        return {"error": f"Invalid event type '{event_type}'. Valid: {valid_event_types}"}

    entry = {
        "audit_id": f"AUD-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{transfer_id}",
        "transfer_id": transfer_id,
        "event_type": event_type,
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "actor": actor,
        "details": details,
        "immutable": True,
    }

    return entry


def conduct_register_review(transfers: list, review_date: Optional[str] = None) -> dict:
    """Conduct a periodic review of the transfer register and identify gaps."""
    if review_date is None:
        review_date = datetime.utcnow().strftime("%Y-%m-%d")

    review_date_dt = datetime.strptime(review_date, "%Y-%m-%d")

    total = len(transfers)
    active = 0
    overdue_reviews = []
    missing_tia = []
    missing_measures = []
    incomplete_fields = []
    high_risk = []

    for t in transfers:
        if t.get("status") != "Active":
            continue
        active += 1

        tid = t.get("transfer_id", "unknown")

        # Check review date
        entry_review = t.get("review_date")
        if entry_review:
            rd = datetime.strptime(entry_review, "%Y-%m-%d")
            if rd < review_date_dt:
                overdue_reviews.append({"transfer_id": tid, "review_due": entry_review})

        # Check TIA
        mechanism_type = t.get("mechanism", {}).get("type", "")
        mech_info = TRANSFER_MECHANISMS.get(mechanism_type, {})
        if mech_info.get("requires_tia") and not t.get("tia_reference"):
            missing_tia.append(tid)

        # Check supplementary measures
        if mech_info.get("requires_supplementary_measures") and not t.get("supplementary_measures"):
            missing_measures.append(tid)

        # Check completeness
        gaps = t.get("completeness", {}).get("gaps", [])
        if gaps:
            incomplete_fields.append({"transfer_id": tid, "gaps": gaps})

        # Check risk
        risk = t.get("risk_rating", "")
        if risk in ("High", "Critical"):
            high_risk.append({"transfer_id": tid, "risk_rating": risk})

    return {
        "review_date": review_date,
        "total_entries": total,
        "active_transfers": active,
        "overdue_reviews": {
            "count": len(overdue_reviews),
            "transfers": overdue_reviews,
        },
        "missing_tia": {
            "count": len(missing_tia),
            "transfers": missing_tia,
        },
        "missing_supplementary_measures": {
            "count": len(missing_measures),
            "transfers": missing_measures,
        },
        "incomplete_entries": {
            "count": len(incomplete_fields),
            "transfers": incomplete_fields,
        },
        "high_risk_transfers": {
            "count": len(high_risk),
            "transfers": high_risk,
        },
        "overall_health": "Healthy" if not (overdue_reviews or missing_tia or missing_measures) else "Action Required",
        "actions_required": (
            [f"Review overdue for {len(overdue_reviews)} transfer(s)"] if overdue_reviews else []
        ) + (
            [f"TIA missing for {len(missing_tia)} transfer(s)"] if missing_tia else []
        ) + (
            [f"Supplementary measures missing for {len(missing_measures)} transfer(s)"] if missing_measures else []
        ),
    }


def generate_documentation_package(transfer: dict) -> dict:
    """Generate a documentation package checklist for a specific transfer."""
    mechanism_type = transfer.get("mechanism", {}).get("type", "")
    mech_info = TRANSFER_MECHANISMS.get(mechanism_type)

    if not mech_info:
        return {"error": f"Unknown mechanism type '{mechanism_type}'"}

    required_docs = mech_info["documentation"]
    provided_docs = transfer.get("documentation_provided", [])

    checklist = []
    for doc in required_docs:
        status = "Provided" if doc in provided_docs else "Missing"
        checklist.append({"document": doc, "status": status})

    complete = all(item["status"] == "Provided" for item in checklist)

    package = {
        "transfer_id": transfer.get("transfer_id", ""),
        "mechanism": mech_info["name"],
        "documentation_checklist": checklist,
        "package_complete": complete,
        "sa_ready": complete and transfer.get("tia_reference") is not None,
    }

    if not complete:
        missing = [item["document"] for item in checklist if item["status"] == "Missing"]
        package["missing_documents"] = missing
        package["remediation"] = f"Obtain and file the following documents: {', '.join(missing)}"

    return package


def generate_sa_response_package(transfers: list, scope: str = "all") -> dict:
    """Generate a supervisory authority response package covering requested transfers."""
    now = datetime.utcnow()

    if scope == "all":
        in_scope = transfers
    else:
        in_scope = [t for t in transfers if t.get("importer", {}).get("country", "").lower() == scope.lower()]

    entries = []
    all_complete = True

    for t in in_scope:
        doc_package = generate_documentation_package(t)
        if not doc_package.get("package_complete", False):
            all_complete = False
        entries.append({
            "transfer_id": t.get("transfer_id"),
            "exporter": t.get("exporter", {}).get("name"),
            "importer": t.get("importer", {}).get("name"),
            "destination": t.get("importer", {}).get("country"),
            "mechanism": t.get("mechanism", {}).get("name"),
            "tia_reference": t.get("tia_reference"),
            "documentation_complete": doc_package.get("package_complete", False),
            "missing_documents": doc_package.get("missing_documents", []),
        })

    return {
        "generated_date": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "scope": scope,
        "total_transfers_in_scope": len(entries),
        "all_documentation_complete": all_complete,
        "transfers": entries,
        "response_readiness": "Ready for submission" if all_complete else "Gaps must be resolved before submission",
    }


if __name__ == "__main__":
    print("=== Create Transfer Register Entry ===")
    entry = create_transfer_entry(
        transfer_id="ATH-INT-001",
        exporter_name="Athena Global Logistics GmbH",
        exporter_country="Germany (EU)",
        importer_name="TransPacific Freight Solutions Ltd",
        importer_country="Hong Kong SAR",
        data_subjects=["employees", "logistics contacts"],
        data_categories=["name", "email", "phone", "shipment data"],
        special_category=False,
        purpose="Freight logistics coordination for APAC operations",
        legal_basis="Art. 6(1)(b) — performance of contract",
        mechanism="sccs",
        mechanism_reference="SCCs Module 2 executed 15 March 2024",
        tia_reference="TIA-2024-003",
        supplementary_measures=["encryption in transit (TLS 1.3)", "pseudonymisation of employee IDs", "contractual audit rights"],
    )
    print(json.dumps(entry, indent=2))

    print("\n=== Risk Assessment ===")
    risk = assess_risk_rating(
        special_category=False,
        volume_above_threshold=False,
        adequate_country=False,
        government_access_risk=True,
        tia_completed=True,
        tia_current=True,
        supplementary_measures_in_place=True,
        derogation_basis=False,
    )
    print(json.dumps(risk, indent=2))

    print("\n=== Audit Trail Entry ===")
    audit = create_audit_entry(
        transfer_id="ATH-INT-001",
        event_type="review_conducted",
        details={
            "reviewer": "Elisa Brandt (DPO)",
            "outcome": "Compliant — no changes required",
            "next_review": "2025-06-30",
        },
        actor="elisa.brandt@athena-logistics.eu",
    )
    print(json.dumps(audit, indent=2))

    print("\n=== Register Review ===")
    sample_transfers = [
        {
            "transfer_id": "ATH-INT-001",
            "status": "Active",
            "mechanism": {"type": "sccs", "name": "SCCs Module 2"},
            "tia_reference": "TIA-2024-003",
            "supplementary_measures": ["encryption", "pseudonymisation"],
            "review_date": "2025-06-30",
            "completeness": {"mandatory_fields_complete": True, "gaps": []},
            "risk_rating": "Medium",
        },
        {
            "transfer_id": "ATH-INT-004",
            "status": "Active",
            "mechanism": {"type": "sccs", "name": "SCCs Module 1"},
            "tia_reference": None,
            "supplementary_measures": [],
            "review_date": "2024-12-31",
            "completeness": {"mandatory_fields_complete": False, "gaps": ["TIA required but not provided"]},
            "risk_rating": "High",
        },
        {
            "transfer_id": "ATH-INT-003",
            "status": "Active",
            "mechanism": {"type": "adequacy", "name": "EU Adequacy Decision"},
            "tia_reference": None,
            "supplementary_measures": [],
            "review_date": "2025-12-31",
            "completeness": {"mandatory_fields_complete": True, "gaps": []},
            "risk_rating": "Low",
        },
    ]
    review = conduct_register_review(sample_transfers, review_date="2025-03-14")
    print(json.dumps(review, indent=2))

    print("\n=== Documentation Package ===")
    doc_pkg = generate_documentation_package({
        "transfer_id": "ATH-INT-001",
        "mechanism": {"type": "sccs", "name": "SCCs Module 2"},
        "tia_reference": "TIA-2024-003",
        "documentation_provided": ["executed_sccs", "tia_document", "supplementary_measures_record"],
    })
    print(json.dumps(doc_pkg, indent=2))
