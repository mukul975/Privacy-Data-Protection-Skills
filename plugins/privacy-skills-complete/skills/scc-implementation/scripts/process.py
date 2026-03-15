#!/usr/bin/env python3
"""
SCC Module Selection and Compliance Tracker

Determines the appropriate SCC module based on party roles,
tracks annex completion status, and generates compliance reports.
"""

import json
import hashlib
from datetime import datetime, timedelta
from typing import Optional


SCC_MODULES = {
    "module_1": {
        "name": "Module 1: Controller to Controller (C2C)",
        "exporter_role": "controller",
        "importer_role": "controller",
        "requires_annex_iii": False,
        "key_clauses": [
            "Clause 8.1 — Data protection safeguards",
            "Clause 8.2 — Purpose limitation",
            "Clause 8.3 — Transparency",
            "Clause 8.4 — Accuracy",
            "Clause 8.5 — Duration and erasure",
            "Clause 8.6 — Security",
            "Clause 8.7 — Onward transfers",
            "Clause 10 — Data subject rights (C2C variant)",
            "Clause 11 — Redress",
            "Clause 14 — Local laws and obligations (TIA required)",
            "Clause 15 — Government access obligations",
        ],
    },
    "module_2": {
        "name": "Module 2: Controller to Processor (C2P)",
        "exporter_role": "controller",
        "importer_role": "processor",
        "requires_annex_iii": True,
        "key_clauses": [
            "Clause 8.1 — Instructions",
            "Clause 8.2 — Purpose limitation",
            "Clause 8.3 — Transparency",
            "Clause 8.5 — Sub-processing",
            "Clause 8.6 — International onward transfers",
            "Clause 8.8 — Security of processing",
            "Clause 8.9 — Documentation and compliance",
            "Clause 9 — Use of sub-processors",
            "Clause 10 — Data subject rights (C2P variant)",
            "Clause 14 — Local laws and obligations (TIA required)",
            "Clause 15 — Government access obligations",
        ],
    },
    "module_3": {
        "name": "Module 3: Processor to Processor (P2P)",
        "exporter_role": "processor",
        "importer_role": "sub-processor",
        "requires_annex_iii": True,
        "key_clauses": [
            "Clause 8.1 — Instructions (chain from controller)",
            "Clause 8.5 — Onward sub-processing",
            "Clause 8.8 — Security measures",
            "Clause 8.9 — Documentation and compliance",
            "Clause 9 — Use of sub-processors",
            "Clause 14 — Local laws and obligations (TIA required)",
            "Clause 15 — Government access obligations",
        ],
    },
    "module_4": {
        "name": "Module 4: Processor to Controller (P2C)",
        "exporter_role": "processor",
        "importer_role": "controller",
        "requires_annex_iii": False,
        "key_clauses": [
            "Clause 8.1 — Importer compliance obligations",
            "Clause 8.2 — Purpose limitation and transparency",
            "Clause 14 — Local laws and obligations (TIA required)",
            "Clause 15 — Government access obligations",
        ],
    },
}

ANNEX_FIELDS = {
    "annex_i_a": [
        "exporter_legal_name",
        "exporter_address",
        "exporter_contact_person",
        "exporter_activities",
        "exporter_role",
        "importer_legal_name",
        "importer_address",
        "importer_contact_person",
        "importer_activities",
        "importer_role",
    ],
    "annex_i_b": [
        "data_subject_categories",
        "personal_data_categories",
        "sensitive_data_transferred",
        "transfer_frequency",
        "processing_nature",
        "transfer_purpose",
        "retention_period",
    ],
    "annex_i_c": [
        "competent_supervisory_authority",
    ],
    "annex_ii": [
        "encryption_in_transit",
        "encryption_at_rest",
        "access_control",
        "data_minimisation",
        "logging_and_monitoring",
        "incident_response",
        "physical_security",
        "business_continuity",
        "staff_measures",
        "sub_processor_management",
    ],
    "annex_iii": [
        "sub_processor_list",
    ],
}


def select_scc_module(exporter_role: str, importer_role: str) -> dict:
    """Determine the correct SCC module based on party roles."""
    exporter_role = exporter_role.lower().strip()
    importer_role = importer_role.lower().strip()

    role_map = {
        ("controller", "controller"): "module_1",
        ("controller", "processor"): "module_2",
        ("processor", "sub-processor"): "module_3",
        ("processor", "processor"): "module_3",
        ("processor", "controller"): "module_4",
    }

    module_key = role_map.get((exporter_role, importer_role))
    if not module_key:
        return {
            "error": f"No SCC module matches exporter={exporter_role}, importer={importer_role}",
            "valid_combinations": list(role_map.keys()),
        }

    module = SCC_MODULES[module_key]
    return {
        "selected_module": module_key,
        "module_name": module["name"],
        "requires_annex_iii": module["requires_annex_iii"],
        "key_clauses": module["key_clauses"],
        "required_annexes": _get_required_annexes(module_key),
    }


def _get_required_annexes(module_key: str) -> list:
    """Return the list of required annexes for a given module."""
    base_annexes = ["annex_i_a", "annex_i_b", "annex_i_c", "annex_ii"]
    if SCC_MODULES[module_key]["requires_annex_iii"]:
        base_annexes.append("annex_iii")
    return base_annexes


def assess_annex_completeness(annex_data: dict, module_key: str) -> dict:
    """Check whether all required annex fields are populated."""
    required_annexes = _get_required_annexes(module_key)
    results = {
        "module": module_key,
        "assessment_date": datetime.utcnow().isoformat(),
        "overall_complete": True,
        "annexes": {},
    }

    for annex_name in required_annexes:
        required_fields = ANNEX_FIELDS.get(annex_name, [])
        provided_data = annex_data.get(annex_name, {})
        missing = []
        populated = []

        for field in required_fields:
            value = provided_data.get(field)
            if value and str(value).strip():
                populated.append(field)
            else:
                missing.append(field)

        is_complete = len(missing) == 0
        if not is_complete:
            results["overall_complete"] = False

        results["annexes"][annex_name] = {
            "total_fields": len(required_fields),
            "populated": len(populated),
            "missing_fields": missing,
            "complete": is_complete,
            "completion_pct": round(len(populated) / len(required_fields) * 100, 1)
            if required_fields
            else 100.0,
        }

    return results


def generate_scc_register_entry(
    exporter_name: str,
    importer_name: str,
    module_key: str,
    execution_date: str,
    importer_country: str,
    tia_completed: bool,
    tia_date: Optional[str] = None,
    supplementary_measures: Optional[list] = None,
    next_review_date: Optional[str] = None,
) -> dict:
    """Generate a standardised SCC register entry."""
    module = SCC_MODULES.get(module_key)
    if not module:
        return {"error": f"Unknown module: {module_key}"}

    exec_date = datetime.strptime(execution_date, "%Y-%m-%d")
    if not next_review_date:
        review_date = exec_date + timedelta(days=365)
        next_review_date = review_date.strftime("%Y-%m-%d")

    entry_id = hashlib.sha256(
        f"{exporter_name}:{importer_name}:{module_key}:{execution_date}".encode()
    ).hexdigest()[:12]

    return {
        "register_id": f"SCC-{entry_id.upper()}",
        "exporter": exporter_name,
        "importer": importer_name,
        "importer_country": importer_country,
        "module": module["name"],
        "module_key": module_key,
        "execution_date": execution_date,
        "scc_version": "Commission Decision 2021/914",
        "tia_completed": tia_completed,
        "tia_date": tia_date,
        "supplementary_measures_applied": supplementary_measures or [],
        "next_review_date": next_review_date,
        "status": "active",
        "created_at": datetime.utcnow().isoformat(),
    }


def check_scc_review_due(register_entries: list, as_of_date: Optional[str] = None) -> dict:
    """Identify SCCs that are due or overdue for review."""
    if as_of_date:
        check_date = datetime.strptime(as_of_date, "%Y-%m-%d")
    else:
        check_date = datetime.utcnow()

    overdue = []
    due_within_30_days = []
    due_within_90_days = []
    current = []

    for entry in register_entries:
        review_date = datetime.strptime(entry["next_review_date"], "%Y-%m-%d")
        days_until_review = (review_date - check_date).days

        entry_summary = {
            "register_id": entry["register_id"],
            "exporter": entry["exporter"],
            "importer": entry["importer"],
            "module": entry["module_key"],
            "next_review_date": entry["next_review_date"],
            "days_until_review": days_until_review,
        }

        if days_until_review < 0:
            overdue.append(entry_summary)
        elif days_until_review <= 30:
            due_within_30_days.append(entry_summary)
        elif days_until_review <= 90:
            due_within_90_days.append(entry_summary)
        else:
            current.append(entry_summary)

    return {
        "check_date": check_date.strftime("%Y-%m-%d"),
        "total_entries": len(register_entries),
        "overdue": overdue,
        "due_within_30_days": due_within_30_days,
        "due_within_90_days": due_within_90_days,
        "current": current,
        "action_required": len(overdue) + len(due_within_30_days),
    }


def generate_compliance_report(
    register_entries: list, annex_assessments: Optional[list] = None
) -> dict:
    """Generate a compliance summary report across all SCCs."""
    total = len(register_entries)
    by_module = {}
    by_country = {}
    tia_complete = 0
    tia_missing = 0

    for entry in register_entries:
        mod = entry.get("module_key", "unknown")
        by_module[mod] = by_module.get(mod, 0) + 1

        country = entry.get("importer_country", "unknown")
        by_country[country] = by_country.get(country, 0) + 1

        if entry.get("tia_completed"):
            tia_complete += 1
        else:
            tia_missing += 1

    annex_summary = None
    if annex_assessments:
        complete_count = sum(1 for a in annex_assessments if a.get("overall_complete"))
        annex_summary = {
            "total_assessed": len(annex_assessments),
            "fully_complete": complete_count,
            "incomplete": len(annex_assessments) - complete_count,
        }

    return {
        "report_date": datetime.utcnow().isoformat(),
        "total_active_sccs": total,
        "by_module": by_module,
        "by_destination_country": by_country,
        "tia_status": {
            "completed": tia_complete,
            "missing": tia_missing,
            "compliance_rate": round(tia_complete / total * 100, 1) if total else 0,
        },
        "annex_completeness": annex_summary,
        "recommendations": _generate_recommendations(tia_missing, annex_summary),
    }


def _generate_recommendations(tia_missing: int, annex_summary: Optional[dict]) -> list:
    """Generate actionable recommendations based on compliance gaps."""
    recs = []
    if tia_missing > 0:
        recs.append(
            f"CRITICAL: {tia_missing} SCC(s) lack a completed Transfer Impact Assessment. "
            "Clause 14 requires a documented TIA before or at the time of transfer. "
            "Prioritise completion within 30 days."
        )
    if annex_summary and annex_summary.get("incomplete", 0) > 0:
        recs.append(
            f"MAJOR: {annex_summary['incomplete']} SCC(s) have incomplete annexes. "
            "Review and populate all required fields to ensure enforceability."
        )
    if not recs:
        recs.append(
            "All SCCs have completed TIAs and fully populated annexes. "
            "Schedule the next periodic review per the review calendar."
        )
    return recs


if __name__ == "__main__":
    print("=== SCC Module Selection ===")
    result = select_scc_module("controller", "processor")
    print(json.dumps(result, indent=2))

    print("\n=== Annex Completeness Assessment ===")
    sample_annex_data = {
        "annex_i_a": {
            "exporter_legal_name": "Athena Global Logistics GmbH",
            "exporter_address": "Friedrichstrasse 112, 10117 Berlin, Germany",
            "exporter_contact_person": "Elisa Brandt, Head of Data Protection",
            "exporter_activities": "International freight forwarding",
            "exporter_role": "Controller",
            "importer_legal_name": "TransPacific Freight Solutions Ltd",
            "importer_address": "88 Harbour Road, Wan Chai, Hong Kong SAR",
            "importer_contact_person": "James Leung, Chief Privacy Officer",
            "importer_activities": "Regional freight consolidation",
            "importer_role": "Processor",
        },
        "annex_i_b": {
            "data_subject_categories": "Shipping customers, employees of customer companies",
            "personal_data_categories": "Full name, business email, phone, shipping address",
            "sensitive_data_transferred": "None",
            "transfer_frequency": "Continuous real-time via API; daily batch at 02:00 UTC",
            "processing_nature": "Storage, retrieval, customs documentation generation",
            "transfer_purpose": "Freight forwarding contract fulfilment",
            "retention_period": "36 months from shipment completion",
        },
        "annex_i_c": {
            "competent_supervisory_authority": "Berliner Beauftragte fuer Datenschutz (BlnBDI)",
        },
        "annex_ii": {
            "encryption_in_transit": "TLS 1.3 for APIs; SFTP with AES-256 for batch",
            "encryption_at_rest": "AES-256 on all storage volumes",
            "access_control": "RBAC with MFA for admin access",
            "data_minimisation": "API payloads stripped of non-essential fields",
            "logging_and_monitoring": "Centralised SIEM with 12-month retention",
            "incident_response": "24-hour initial assessment SLA",
            "physical_security": "ISO 27001-certified data centres",
            "business_continuity": "RPO 4h, RTO 8h, annual DR testing",
            "staff_measures": "Mandatory annual training, background checks",
            "sub_processor_management": "Due diligence before engagement, annual audit",
        },
        "annex_iii": {
            "sub_processor_list": [
                {
                    "name": "CloudVault Asia Pte Ltd",
                    "country": "Singapore",
                    "activity": "Cloud infrastructure hosting",
                    "safeguard": "SCCs Module 3 executed 15 March 2025",
                },
                {
                    "name": "Pinnacle Data Services Co Ltd",
                    "country": "Thailand",
                    "activity": "Data entry and validation for customs",
                    "safeguard": "SCCs Module 3 executed 22 January 2025",
                },
            ],
        },
    }
    completeness = assess_annex_completeness(sample_annex_data, "module_2")
    print(json.dumps(completeness, indent=2))

    print("\n=== SCC Register Entry ===")
    entry = generate_scc_register_entry(
        exporter_name="Athena Global Logistics GmbH",
        importer_name="TransPacific Freight Solutions Ltd",
        module_key="module_2",
        execution_date="2025-03-15",
        importer_country="Hong Kong SAR",
        tia_completed=True,
        tia_date="2025-03-10",
        supplementary_measures=["TLS 1.3 encryption", "SFTP with AES-256"],
    )
    print(json.dumps(entry, indent=2))
