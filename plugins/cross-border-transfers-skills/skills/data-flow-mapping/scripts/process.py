#!/usr/bin/env python3
"""
International Data Flow Mapping and Gap Analysis Engine

Manages the data flow inventory, assigns transfer mechanisms,
identifies gaps, and generates compliance reports.
"""

import json
from datetime import datetime
from typing import Optional


ADEQUACY_COUNTRIES = [
    "Andorra", "Argentina", "Canada", "Faroe Islands", "Guernsey",
    "Israel", "Isle of Man", "Japan", "Jersey", "New Zealand",
    "South Korea", "Switzerland", "United Kingdom", "Uruguay",
]

DPF_COUNTRIES = ["United States"]

MECHANISM_PRIORITY = [
    "adequacy_decision",
    "dpf",
    "bcrs",
    "sccs",
    "art49_derogation",
]


def create_data_flow_entry(
    flow_id: str,
    source_system: str,
    source_country: str,
    destination_entity: str,
    destination_country: str,
    data_categories: list,
    data_subjects: list,
    purpose: str,
    transfer_method: str,
    frequency: str,
    mechanism: Optional[str] = None,
    tia_reference: Optional[str] = None,
    contract_reference: Optional[str] = None,
) -> dict:
    """Create a data flow register entry."""
    return {
        "flow_id": flow_id,
        "source_system": source_system,
        "source_country": source_country,
        "destination_entity": destination_entity,
        "destination_country": destination_country,
        "data_categories": data_categories,
        "data_subjects": data_subjects,
        "purpose": purpose,
        "transfer_method": transfer_method,
        "frequency": frequency,
        "mechanism": mechanism,
        "tia_reference": tia_reference,
        "contract_reference": contract_reference,
        "last_reviewed": datetime.utcnow().strftime("%Y-%m-%d"),
        "is_cross_border": source_country != destination_country,
    }


def assign_transfer_mechanism(destination_country: str, importer_dpf_certified: bool = False) -> dict:
    """Determine the appropriate transfer mechanism for a destination country."""
    if destination_country in ADEQUACY_COUNTRIES:
        return {
            "mechanism": "adequacy_decision",
            "description": f"EU adequacy decision in force for {destination_country}",
            "additional_required": "None — transfer may proceed under adequacy",
            "tia_required": False,
        }

    if destination_country in DPF_COUNTRIES or (
        destination_country == "United States" and importer_dpf_certified
    ):
        return {
            "mechanism": "eu_us_dpf",
            "description": "EU-US Data Privacy Framework (Decision 2023/1795)",
            "additional_required": "Verify importer DPF certification is active; maintain SCCs as backup",
            "tia_required": False,
        }

    return {
        "mechanism": "sccs_required",
        "description": f"No adequacy decision for {destination_country}; SCCs or BCRs required",
        "additional_required": "Execute SCCs (appropriate module), complete TIA, implement supplementary measures if needed",
        "tia_required": True,
    }


def conduct_gap_analysis(data_flows: list) -> dict:
    """Analyse data flow register for compliance gaps."""
    gaps = {
        "critical": [],
        "high": [],
        "medium": [],
    }
    summary = {
        "total_flows": len(data_flows),
        "cross_border_flows": 0,
        "with_mechanism": 0,
        "without_mechanism": 0,
        "with_tia": 0,
        "without_tia_needed": 0,
    }

    for flow in data_flows:
        if not flow.get("is_cross_border", False):
            continue

        summary["cross_border_flows"] += 1

        if not flow.get("mechanism"):
            summary["without_mechanism"] += 1
            gaps["critical"].append({
                "flow_id": flow["flow_id"],
                "issue": "No transfer mechanism in place",
                "destination": flow["destination_country"],
                "destination_entity": flow["destination_entity"],
                "remediation": "Execute SCCs or establish alternative Art. 46 mechanism within 30 days",
                "priority": "critical",
            })
        else:
            summary["with_mechanism"] += 1

            dest_country = flow["destination_country"]
            needs_tia = dest_country not in ADEQUACY_COUNTRIES and flow["mechanism"] not in (
                "adequacy_decision", "eu_us_dpf"
            )

            if needs_tia and not flow.get("tia_reference"):
                summary["without_tia_needed"] += 1
                gaps["high"].append({
                    "flow_id": flow["flow_id"],
                    "issue": "Transfer mechanism in place but TIA not documented",
                    "destination": dest_country,
                    "mechanism": flow["mechanism"],
                    "remediation": "Complete TIA within 30 days",
                    "priority": "high",
                })
            elif needs_tia:
                summary["with_tia"] += 1

            if not flow.get("contract_reference") and flow["mechanism"] in ("sccs", "bcrs"):
                gaps["medium"].append({
                    "flow_id": flow["flow_id"],
                    "issue": "Contract reference not documented in flow register",
                    "destination": dest_country,
                    "remediation": "Update register with contract reference within 60 days",
                    "priority": "medium",
                })

    return {
        "analysis_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "summary": summary,
        "gaps": gaps,
        "total_gaps": sum(len(v) for v in gaps.values()),
        "compliance_rate": round(
            summary["with_mechanism"] / summary["cross_border_flows"] * 100, 1
        ) if summary["cross_border_flows"] else 100,
    }


def generate_flow_summary_by_country(data_flows: list) -> dict:
    """Generate a summary of data flows grouped by destination country."""
    by_country = {}
    for flow in data_flows:
        if not flow.get("is_cross_border"):
            continue
        country = flow["destination_country"]
        if country not in by_country:
            by_country[country] = {
                "flow_count": 0,
                "mechanisms": set(),
                "entities": set(),
                "data_categories": set(),
            }
        by_country[country]["flow_count"] += 1
        if flow.get("mechanism"):
            by_country[country]["mechanisms"].add(flow["mechanism"])
        by_country[country]["entities"].add(flow["destination_entity"])
        for cat in flow.get("data_categories", []):
            by_country[country]["data_categories"].add(cat)

    result = {}
    for country, info in by_country.items():
        result[country] = {
            "flow_count": info["flow_count"],
            "mechanisms": list(info["mechanisms"]),
            "recipient_entities": list(info["entities"]),
            "data_categories": list(info["data_categories"]),
            "adequacy_status": "adequate" if country in ADEQUACY_COUNTRIES else "not_adequate",
        }

    return {
        "report_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "total_destination_countries": len(result),
        "adequate_countries": sum(1 for v in result.values() if v["adequacy_status"] == "adequate"),
        "non_adequate_countries": sum(1 for v in result.values() if v["adequacy_status"] != "adequate"),
        "by_country": result,
    }


def generate_third_party_register(data_flows: list) -> list:
    """Extract and deduplicate third-party recipients from data flows."""
    parties = {}
    for flow in data_flows:
        entity = flow["destination_entity"]
        if entity not in parties:
            parties[entity] = {
                "entity_name": entity,
                "country": flow["destination_country"],
                "flow_ids": [],
                "data_categories": set(),
                "mechanisms": set(),
                "contract_references": set(),
            }
        parties[entity]["flow_ids"].append(flow["flow_id"])
        for cat in flow.get("data_categories", []):
            parties[entity]["data_categories"].add(cat)
        if flow.get("mechanism"):
            parties[entity]["mechanisms"].add(flow["mechanism"])
        if flow.get("contract_reference"):
            parties[entity]["contract_references"].add(flow["contract_reference"])

    return [
        {
            "entity_name": p["entity_name"],
            "country": p["country"],
            "flow_count": len(p["flow_ids"]),
            "flow_ids": p["flow_ids"],
            "data_categories": list(p["data_categories"]),
            "mechanisms": list(p["mechanisms"]),
            "contract_references": list(p["contract_references"]),
        }
        for p in parties.values()
    ]


if __name__ == "__main__":
    flows = [
        create_data_flow_entry(
            "DF-001", "SAP S/4HANA", "Germany",
            "Athena Logistics (HK) Ltd", "Hong Kong SAR",
            ["customer names", "addresses", "consignment data"],
            ["shipping customers"],
            "Freight operations", "API", "Continuous",
            mechanism="sccs", tia_reference="TIA-2025-HK-001", contract_reference="SCC-2025-APAC-001",
        ),
        create_data_flow_entry(
            "DF-002", "Workday", "Ireland",
            "Workday Inc (US backup)", "United States",
            ["employee HR data"],
            ["employees"],
            "HR platform backup", "Replication", "Continuous",
            mechanism="eu_us_dpf",
        ),
        create_data_flow_entry(
            "DF-003", "Fleetio", "Germany",
            "Fleetio Inc", "United States",
            ["driver names", "licence numbers", "GPS data"],
            ["drivers"],
            "Fleet management", "API", "Continuous",
        ),
        create_data_flow_entry(
            "DF-004", "SAP S/4HANA", "Germany",
            "Athena Freight Services India", "India",
            ["employee payroll", "benefits"],
            ["employees"],
            "Local payroll processing", "SFTP", "Daily",
            mechanism="sccs", contract_reference="SCC-2025-IN-001",
        ),
    ]

    print("=== Gap Analysis ===")
    gaps = conduct_gap_analysis(flows)
    print(json.dumps(gaps, indent=2))

    print("\n=== Flow Summary by Country ===")
    summary = generate_flow_summary_by_country(flows)
    print(json.dumps(summary, indent=2))

    print("\n=== Third-Party Register ===")
    register = generate_third_party_register(flows)
    print(json.dumps(register, indent=2))
