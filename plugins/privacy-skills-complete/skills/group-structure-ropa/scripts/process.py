#!/usr/bin/env python3
"""
Group Structure RoPA Manager

Manages RoPA across multi-entity corporate groups. Validates intra-group
transfer documentation, checks DPA coverage for intra-group processing,
and generates consolidated group views.
"""

import json
import sys
from datetime import datetime
from typing import Any


def load_group_ropa(file_path: str) -> dict:
    """Load a group RoPA file containing multiple entities."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_intra_group_transfers(group_ropa: dict) -> list[dict]:
    """Validate that intra-group transfers are documented by both parties."""
    entities = group_ropa.get("entities", [])
    entity_names = {e.get("entity_name"): e for e in entities}
    issues = []

    for entity in entities:
        entity_name = entity.get("entity_name", "Unknown")
        for record in entity.get("records", []):
            record_id = record.get("record_id", "UNKNOWN")

            # Check recipients for intra-group entities
            recipients = record.get("recipient_categories", [])
            for recipient in recipients:
                if isinstance(recipient, dict):
                    r_name = recipient.get("recipient", "")
                    r_type = recipient.get("type", "")

                    # Check if recipient is a group entity
                    for group_entity_name in entity_names:
                        if group_entity_name in r_name and group_entity_name != entity_name:
                            # Verify the receiving entity has corresponding documentation
                            receiving_entity = entity_names[group_entity_name]
                            has_corresponding = False

                            if "processor" in r_type.lower():
                                # Check processor records
                                for r_record in receiving_entity.get("processor_records", []):
                                    controllers = r_record.get("controllers", [])
                                    for c in controllers:
                                        if entity_name in str(c.get("controller_name", "")):
                                            has_corresponding = True
                                            break

                            if not has_corresponding:
                                # Check if receiving entity has any reference back
                                for r_record in receiving_entity.get("records", []):
                                    r_recipients = r_record.get("recipient_categories", [])
                                    for rr in r_recipients:
                                        if isinstance(rr, dict) and entity_name in str(rr.get("recipient", "")):
                                            has_corresponding = True
                                            break

                            if not has_corresponding:
                                issues.append({
                                    "type": "unmatched_intra_group_transfer",
                                    "severity": "Major",
                                    "source_entity": entity_name,
                                    "source_record": record_id,
                                    "receiving_entity": group_entity_name,
                                    "description": f"{entity_name} ({record_id}) lists {group_entity_name} as recipient, but {group_entity_name} has no corresponding record",
                                })

                            # Check for DPA if processor relationship
                            if "processor" in r_type.lower():
                                dpa_ref = recipient.get("dpa_reference", "")
                                if not dpa_ref or "no dpa" in dpa_ref.lower():
                                    issues.append({
                                        "type": "missing_intra_group_dpa",
                                        "severity": "Critical",
                                        "source_entity": entity_name,
                                        "source_record": record_id,
                                        "receiving_entity": group_entity_name,
                                        "description": f"Intra-group processor relationship between {entity_name} and {group_entity_name} has no Art. 28 DPA reference",
                                    })

            # Check international transfers for intra-group
            transfers = record.get("international_transfers", [])
            for transfer in transfers:
                if isinstance(transfer, dict):
                    t_recipient = transfer.get("recipient", "")
                    for group_entity_name in entity_names:
                        if group_entity_name in t_recipient:
                            if not transfer.get("safeguard_mechanism"):
                                issues.append({
                                    "type": "missing_transfer_mechanism",
                                    "severity": "Critical",
                                    "source_entity": entity_name,
                                    "source_record": record_id,
                                    "destination_entity": group_entity_name,
                                    "description": f"Intra-group transfer from {entity_name} to {group_entity_name} has no documented transfer mechanism",
                                })

    return issues


def check_joint_controller_consistency(group_ropa: dict) -> list[dict]:
    """Check that joint controller arrangements are consistently documented."""
    entities = group_ropa.get("entities", [])
    jca_refs = {}  # JCA reference -> list of entities referencing it
    issues = []

    for entity in entities:
        entity_name = entity.get("entity_name", "Unknown")
        for record in entity.get("records", []):
            ci = record.get("controller_identity", {})
            jc = ci.get("joint_controllers")
            if jc and jc not in ("None", "none", None):
                jca_ref = ci.get("art_26_reference", "")
                if jca_ref:
                    if jca_ref not in jca_refs:
                        jca_refs[jca_ref] = []
                    jca_refs[jca_ref].append({
                        "entity": entity_name,
                        "record_id": record.get("record_id"),
                    })

    # Each JCA should be referenced by at least 2 entities
    for ref, entities_list in jca_refs.items():
        if len(entities_list) < 2:
            issues.append({
                "type": "unmatched_joint_controller",
                "severity": "Major",
                "jca_reference": ref,
                "entities": [e["entity"] for e in entities_list],
                "description": f"Joint controller arrangement {ref} is only referenced by {entities_list[0]['entity']}. The other joint controller(s) must also reference this arrangement.",
            })

    return issues


def generate_consolidated_view(group_ropa: dict) -> str:
    """Generate a consolidated group RoPA view."""
    entities = group_ropa.get("entities", [])
    group_name = group_ropa.get("group_name", "Unknown Group")

    lines = []
    lines.append("=" * 80)
    lines.append(f"CONSOLIDATED GROUP RoPA — {group_name}")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 80)

    total_controller_records = 0
    total_processor_records = 0

    for entity in entities:
        entity_name = entity.get("entity_name", "Unknown")
        country = entity.get("country", "Unknown")
        controller_records = entity.get("records", [])
        processor_records = entity.get("processor_records", [])

        total_controller_records += len(controller_records)
        total_processor_records += len(processor_records)

        lines.append(f"\n{'─' * 60}")
        lines.append(f"ENTITY: {entity_name} ({country})")
        lines.append(f"{'─' * 60}")
        lines.append(f"  Controller records: {len(controller_records)}")
        lines.append(f"  Processor records: {len(processor_records)}")
        lines.append(f"  DPO: {entity.get('dpo', 'N/A')}")
        lines.append(f"  Lead SA: {entity.get('lead_sa', 'N/A')}")

        if controller_records:
            lines.append(f"\n  Controller Processing Activities:")
            for r in controller_records:
                dpia = "DPIA" if r.get("dpia_required") else "No DPIA"
                lines.append(f"    {r.get('record_id', 'N/A')}: {r.get('processing_activity', 'N/A')} [{dpia}]")

        if processor_records:
            lines.append(f"\n  Processor Records (processing on behalf of):")
            for r in processor_records:
                controllers = r.get("controllers", [])
                c_names = ", ".join(c.get("controller_name", "N/A") for c in controllers)
                lines.append(f"    {r.get('record_id', 'N/A')}: {r.get('service_name', 'N/A')} [For: {c_names}]")

    lines.append(f"\n{'=' * 80}")
    lines.append(f"GROUP SUMMARY")
    lines.append(f"{'=' * 80}")
    lines.append(f"  Total entities: {len(entities)}")
    lines.append(f"  Total controller records: {total_controller_records}")
    lines.append(f"  Total processor records: {total_processor_records}")
    lines.append(f"  Total records: {total_controller_records + total_processor_records}")

    return "\n".join(lines)


def create_sample_group_ropa() -> dict:
    """Create a sample group RoPA for Helix Biotech Solutions."""
    return {
        "group_name": "Helix Biotech Holdings SE Group",
        "group_dpo": "Dr. Elena Voss",
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "entities": [
            {
                "entity_name": "Helix Biotech Solutions GmbH",
                "country": "Germany",
                "registration": "HRB 267891, Amtsgericht Munich",
                "dpo": "Dr. Elena Voss",
                "lead_sa": "BfDI / BayLDA",
                "records": [
                    {"record_id": "DE-RPA-001", "processing_activity": "Employee payroll", "dpia_required": False},
                    {"record_id": "DE-RPA-002", "processing_activity": "Clinical trial data management", "dpia_required": True},
                    {"record_id": "DE-RPA-003", "processing_activity": "Website analytics", "dpia_required": False},
                ],
                "processor_records": [],
            },
            {
                "entity_name": "Helix Biotech Solutions Ltd",
                "country": "United Kingdom",
                "registration": "Company No. 12345678",
                "dpo": "James Walker",
                "lead_sa": "ICO",
                "records": [
                    {"record_id": "UK-RPA-001", "processing_activity": "UK employee payroll", "dpia_required": False},
                    {"record_id": "UK-RPA-002", "processing_activity": "UK clinical trial sites", "dpia_required": True},
                ],
                "processor_records": [],
            },
            {
                "entity_name": "Helix Shared Services B.V.",
                "country": "Netherlands",
                "registration": "KvK 87654321",
                "dpo": "Dr. Elena Voss (group DPO)",
                "lead_sa": "Autoriteit Persoonsgegevens",
                "records": [
                    {"record_id": "NL-RPA-001", "processing_activity": "Own employee data", "dpia_required": False},
                ],
                "processor_records": [
                    {
                        "record_id": "NL-RPP-001",
                        "service_name": "Group IT Infrastructure",
                        "controllers": [
                            {"controller_name": "Helix Biotech Solutions GmbH"},
                            {"controller_name": "Helix Biotech Solutions Ltd"},
                        ],
                    },
                    {
                        "record_id": "NL-RPP-002",
                        "service_name": "Group Payroll Processing",
                        "controllers": [
                            {"controller_name": "Helix Biotech Solutions GmbH"},
                            {"controller_name": "Helix Biotech Solutions Ltd"},
                        ],
                    },
                ],
            },
        ],
    }


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python process.py consolidated <group_ropa.json>")
        print("  python process.py validate-transfers <group_ropa.json>")
        print("  python process.py validate-jca <group_ropa.json>")
        print("  python process.py demo")
        sys.exit(1)

    command = sys.argv[1]

    if command == "demo":
        sample = create_sample_group_ropa()
        print(json.dumps(sample, indent=2, default=str))
        print("\n")
        print(generate_consolidated_view(sample))

    elif command == "consolidated":
        if len(sys.argv) < 3:
            print("ERROR: Provide group RoPA JSON.")
            sys.exit(1)
        group_ropa = load_group_ropa(sys.argv[2])
        print(generate_consolidated_view(group_ropa))

    elif command == "validate-transfers":
        if len(sys.argv) < 3:
            print("ERROR: Provide group RoPA JSON.")
            sys.exit(1)
        group_ropa = load_group_ropa(sys.argv[2])
        issues = validate_intra_group_transfers(group_ropa)
        if issues:
            print(f"INTRA-GROUP TRANSFER ISSUES: {len(issues)}\n")
            for i in issues:
                print(f"  [{i['severity']}] {i['type']}")
                print(f"    {i['description']}\n")
        else:
            print("All intra-group transfers are properly documented.")

    elif command == "validate-jca":
        if len(sys.argv) < 3:
            print("ERROR: Provide group RoPA JSON.")
            sys.exit(1)
        group_ropa = load_group_ropa(sys.argv[2])
        issues = check_joint_controller_consistency(group_ropa)
        if issues:
            print(f"JOINT CONTROLLER ISSUES: {len(issues)}\n")
            for i in issues:
                print(f"  [{i['severity']}] {i['jca_reference']}")
                print(f"    {i['description']}\n")
        else:
            print("All joint controller arrangements are consistently documented.")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
