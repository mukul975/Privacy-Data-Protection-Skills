#!/usr/bin/env python3
"""
Processor RoPA Generator

Generates GDPR Article 30(2) compliant Records of Processing Activities
for data processors. Validates all four mandatory fields and produces
structured JSON and formatted Markdown output.
"""

import json
import sys
from datetime import datetime
from typing import Any


PROCESSOR_MANDATORY_FIELDS = {
    "processor_identity": {
        "article": "Art. 30(2)(a)",
        "description": "Name and contact details of processor(s), each controller, representative, and DPO",
        "required_sub_fields": ["legal_entity_name", "registered_address", "contact_email", "dpo_name", "dpo_email"],
    },
    "controllers": {
        "article": "Art. 30(2)(a)",
        "description": "Identity and contact details of each controller on whose behalf the processor acts",
        "required_sub_fields": [],
    },
    "processing_categories": {
        "article": "Art. 30(2)(b)",
        "description": "Categories of processing carried out on behalf of each controller",
        "required_sub_fields": [],
    },
    "international_transfers": {
        "article": "Art. 30(2)(c)",
        "description": "Transfers to third countries or international organisations",
        "required_sub_fields": [],
    },
    "security_measures": {
        "article": "Art. 30(2)(d)",
        "description": "General description of technical and organisational security measures per Art. 32(1)",
        "required_sub_fields": [],
    },
}


def validate_non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str) and value.strip() == "":
        return False
    if isinstance(value, (list, dict)) and len(value) == 0:
        return False
    return True


def validate_processor_entry(entry: dict) -> list[dict]:
    """Validate a single processor RoPA entry against Art. 30(2) requirements."""
    issues = []
    record_id = entry.get("record_id", "UNKNOWN")

    for field_name, spec in PROCESSOR_MANDATORY_FIELDS.items():
        value = entry.get(field_name)

        if not validate_non_empty(value):
            issues.append({
                "record_id": record_id,
                "severity": "Critical",
                "field": field_name,
                "article": spec["article"],
                "issue": f"Mandatory field '{field_name}' is missing or empty",
            })
            continue

        for sub_field in spec.get("required_sub_fields", []):
            if isinstance(value, dict) and not validate_non_empty(value.get(sub_field)):
                issues.append({
                    "record_id": record_id,
                    "severity": "Major",
                    "field": f"{field_name}.{sub_field}",
                    "article": spec["article"],
                    "issue": f"Required sub-field '{sub_field}' is missing within '{field_name}'",
                })

    # Validate per-controller processing categories
    controllers = entry.get("controllers", [])
    processing_cats = entry.get("processing_categories", {})
    if isinstance(controllers, list) and isinstance(processing_cats, dict):
        for controller in controllers:
            c_name = controller.get("controller_name", "Unknown")
            if c_name not in processing_cats and not any(
                c_name in str(k) for k in processing_cats.keys()
            ):
                issues.append({
                    "record_id": record_id,
                    "severity": "Major",
                    "field": "processing_categories",
                    "article": "Art. 30(2)(b)",
                    "issue": f"No processing categories documented for controller '{c_name}'. Art. 30(2)(b) requires per-controller documentation.",
                })

    # Validate transfer documentation
    transfers = entry.get("international_transfers", [])
    if isinstance(transfers, list):
        for idx, transfer in enumerate(transfers):
            if isinstance(transfer, dict):
                if not transfer.get("destination_country"):
                    issues.append({
                        "record_id": record_id,
                        "severity": "Major",
                        "field": f"international_transfers[{idx}]",
                        "article": "Art. 30(2)(c)",
                        "issue": "Transfer missing destination country",
                    })
                if not transfer.get("safeguard_mechanism"):
                    issues.append({
                        "record_id": record_id,
                        "severity": "Major",
                        "field": f"international_transfers[{idx}]",
                        "article": "Art. 30(2)(c) / Chapter V",
                        "issue": "Transfer missing safeguard mechanism",
                    })

    return issues


def create_sample_processor_ropa() -> dict:
    """Generate a sample processor RoPA for Helix Biotech Solutions."""
    return {
        "organisation": "Helix Biotech Solutions GmbH",
        "record_role": "Processor",
        "ropa_version": "2.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "prepared_by": "Dr. Elena Voss, Data Protection Officer",
        "records": [
            {
                "record_id": "RPP-001",
                "record_type": "processor",
                "service_name": "LIMS Cloud Hosting Service",
                "processor_identity": {
                    "legal_entity_name": "Helix Biotech Solutions GmbH",
                    "registered_address": "Leopoldstrasse 42, 80802 Munich, Germany",
                    "registration_number": "HRB 267891, Amtsgericht Munich",
                    "contact_email": "processor-privacy@helix-biotech.eu",
                    "dpo_name": "Dr. Elena Voss",
                    "dpo_email": "dpo@helix-biotech.eu",
                    "dpo_phone": "+49 89 7654 3210",
                },
                "controllers": [
                    {
                        "controller_name": "Meridian Pharma AG",
                        "controller_address": "Bahnhofstrasse 15, 8001 Zurich, Switzerland",
                        "controller_contact": "privacy@meridian-pharma.ch",
                        "controller_dpo": "Thomas Keller, dpo@meridian-pharma.ch",
                        "eu_representative": "Meridian Pharma EU Representative Ltd, 45 Fitzwilliam Square, Dublin 2, Ireland",
                        "dpa_reference": "DPA-2024-MER-001, executed 2024-05-15",
                        "dpa_expiry": "2027-05-14",
                    },
                    {
                        "controller_name": "NovaCure Therapeutics S.A.",
                        "controller_address": "Avenue Louise 54, 1050 Brussels, Belgium",
                        "controller_contact": "gdpr@novacure.eu",
                        "controller_dpo": "Marie Dupont, dpo@novacure.eu",
                        "eu_representative": "Not applicable (established in EEA)",
                        "dpa_reference": "DPA-2024-NOV-002, executed 2024-08-22",
                        "dpa_expiry": "2026-08-21",
                    },
                ],
                "processing_categories": {
                    "Meridian Pharma AG": [
                        {
                            "category": "Data hosting and storage",
                            "description": "Hosting of laboratory test results, sample tracking data, and quality control records on Helix cloud infrastructure (AWS eu-central-1). Includes database management, indexing, and query execution.",
                        },
                        {
                            "category": "Backup and disaster recovery",
                            "description": "Daily automated encrypted backups of all hosted data with cross-region replication (eu-central-1 to eu-west-1). Quarterly disaster recovery testing.",
                        },
                        {
                            "category": "Technical support",
                            "description": "Troubleshooting and resolving LIMS system issues requiring access to data records. All access is ticket-based, logged, and time-limited to resolution window.",
                        },
                    ],
                    "NovaCure Therapeutics S.A.": [
                        {
                            "category": "Data hosting and storage",
                            "description": "Hosting of pre-clinical and Phase I clinical laboratory data on dedicated Helix cloud tenant (AWS eu-central-1). Includes database management, indexing, and query execution.",
                        },
                        {
                            "category": "Backup and disaster recovery",
                            "description": "Daily automated encrypted backups with cross-region replication. Quarterly disaster recovery testing.",
                        },
                        {
                            "category": "Data migration (completed)",
                            "description": "One-time migration of legacy laboratory data from NovaCure on-premises systems to Helix cloud. Migration completed 2024-10-15. Post-migration data access for validation revoked 2024-11-01.",
                        },
                    ],
                },
                "sub_processors": [
                    {
                        "name": "Amazon Web Services EMEA SARL",
                        "location": "Luxembourg (data centres: Frankfurt eu-central-1, Dublin eu-west-1)",
                        "service": "Cloud infrastructure (IaaS) — compute, storage, networking",
                        "controllers_affected": "All controllers",
                        "dpa_reference": "AWS GDPR DPA, accepted 2024-01-10",
                        "authorisation_type": "General written authorisation with 30-day notification obligation",
                    },
                    {
                        "name": "Wipro Ltd",
                        "location": "Bangalore, India",
                        "service": "24x7 infrastructure monitoring and Level 1 support",
                        "controllers_affected": "NovaCure Therapeutics S.A. only (per controller-specific authorisation)",
                        "dpa_reference": "DPA-2024-WIPRO-003, executed 2024-07-01",
                        "authorisation_type": "Specific written authorisation from NovaCure (granted 2024-06-15)",
                    },
                    {
                        "name": "Datadog Inc.",
                        "location": "EU region (Dublin, Ireland)",
                        "service": "Application performance monitoring, log aggregation, alerting",
                        "controllers_affected": "All controllers",
                        "dpa_reference": "Datadog DPA, accepted 2024-03-01",
                        "authorisation_type": "General written authorisation with 30-day notification obligation",
                    },
                ],
                "international_transfers": [
                    {
                        "controller": "Meridian Pharma AG",
                        "destination_country": "Switzerland",
                        "recipient": "Meridian Pharma AG (controller)",
                        "data_transferred": "Laboratory results and QC data returned to controller",
                        "safeguard_mechanism": "Swiss adequacy decision — Commission Decision 2000/518/EC as maintained",
                        "tia_reference": "Not required (adequacy decision)",
                    },
                    {
                        "controller": "NovaCure Therapeutics S.A.",
                        "destination_country": "India",
                        "recipient": "Wipro Ltd (sub-processor)",
                        "data_transferred": "System metadata, incidental access to hosted laboratory data during infrastructure support",
                        "safeguard_mechanism": "EU SCCs Module 3 (processor-to-sub-processor), executed 2024-07-01",
                        "tia_reference": "TIA-2024-WIPRO-004",
                    },
                ],
                "security_measures": "Multi-tenant cloud infrastructure with logical tenant isolation using dedicated database schemas per controller and separate AWS KMS encryption keys. AES-256 encryption at rest. TLS 1.3 for all data in transit. Network segmentation with dedicated VPCs per tenant. Role-based access control with named-user accounts and quarterly access reviews. Multi-factor authentication for all administrative access. Immutable audit logging via AWS CloudTrail with 2-year retention. Daily encrypted backups with cross-region replication and quarterly restore testing. Weekly automated vulnerability scanning (Qualys). Annual penetration testing by NCC Group (latest: 2025-Q2). ISO 27001:2022 certified (cert ref: IS 891245). SOC 2 Type II audit completed annually (latest: 2025-Q3). All staff with data access undergo background checks, sign confidentiality agreements, and complete annual data protection training. Incident response procedure with 24-hour initial assessment and controller notification per Art. 33(2).",
                "created_date": "2024-06-01",
                "last_reviewed_date": "2025-12-01",
                "next_review_date": "2026-06-01",
                "record_owner": "Dr. Elena Voss, DPO",
            },
        ],
    }


def generate_markdown_report(ropa: dict) -> str:
    """Generate a formatted Markdown processor RoPA report."""
    lines = []
    org = ropa.get("organisation", "Unknown Organisation")
    lines.append(f"# Processor Record of Processing Activities — {org}")
    lines.append(f"\n**Record Role**: Processor (GDPR Art. 30(2))")
    lines.append(f"**RoPA Version**: {ropa.get('ropa_version', 'N/A')}")
    lines.append(f"**Last Updated**: {ropa.get('last_updated', 'N/A')}")
    lines.append(f"**Prepared By**: {ropa.get('prepared_by', 'N/A')}")
    lines.append(f"\n---\n")

    for record in ropa.get("records", []):
        rid = record.get("record_id", "N/A")
        service = record.get("service_name", "N/A")
        lines.append(f"## {rid}: {service}")

        # Processor Identity
        pi = record.get("processor_identity", {})
        lines.append(f"\n### Art. 30(2)(a) — Processor Identity\n")
        lines.append(f"| Field | Value |")
        lines.append(f"|-------|-------|")
        lines.append(f"| Legal entity | {pi.get('legal_entity_name', 'N/A')} |")
        lines.append(f"| Registered address | {pi.get('registered_address', 'N/A')} |")
        lines.append(f"| Contact | {pi.get('contact_email', 'N/A')} |")
        lines.append(f"| DPO | {pi.get('dpo_name', 'N/A')}, {pi.get('dpo_email', 'N/A')} |")

        # Controllers
        lines.append(f"\n### Art. 30(2)(a) — Controllers Served\n")
        lines.append(f"| Controller | Address | DPO | DPA Reference |")
        lines.append(f"|-----------|---------|-----|---------------|")
        for c in record.get("controllers", []):
            lines.append(f"| {c.get('controller_name', 'N/A')} | {c.get('controller_address', 'N/A')} | {c.get('controller_dpo', 'N/A')} | {c.get('dpa_reference', 'N/A')} |")

        # Processing Categories per Controller
        lines.append(f"\n### Art. 30(2)(b) — Categories of Processing\n")
        proc_cats = record.get("processing_categories", {})
        for controller_name, categories in proc_cats.items():
            lines.append(f"\n**Controller: {controller_name}**\n")
            lines.append(f"| Category | Description |")
            lines.append(f"|----------|-------------|")
            for cat in categories:
                lines.append(f"| {cat.get('category', 'N/A')} | {cat.get('description', 'N/A')} |")

        # Sub-processors
        subs = record.get("sub_processors", [])
        if subs:
            lines.append(f"\n### Sub-Processors\n")
            lines.append(f"| Sub-Processor | Location | Service | Controllers | DPA | Auth Type |")
            lines.append(f"|--------------|----------|---------|-------------|-----|-----------|")
            for s in subs:
                lines.append(f"| {s.get('name', 'N/A')} | {s.get('location', 'N/A')} | {s.get('service', 'N/A')} | {s.get('controllers_affected', 'N/A')} | {s.get('dpa_reference', 'N/A')} | {s.get('authorisation_type', 'N/A')} |")

        # International Transfers
        transfers = record.get("international_transfers", [])
        lines.append(f"\n### Art. 30(2)(c) — International Transfers\n")
        if not transfers:
            lines.append("No transfers to third countries or international organisations.")
        else:
            lines.append(f"| Controller | Destination | Recipient | Data | Safeguard | TIA |")
            lines.append(f"|-----------|-------------|-----------|------|-----------|-----|")
            for t in transfers:
                lines.append(f"| {t.get('controller', 'N/A')} | {t.get('destination_country', 'N/A')} | {t.get('recipient', 'N/A')} | {t.get('data_transferred', 'N/A')} | {t.get('safeguard_mechanism', 'N/A')} | {t.get('tia_reference', 'N/A')} |")

        # Security Measures
        lines.append(f"\n### Art. 30(2)(d) — Security Measures\n")
        lines.append(record.get("security_measures", "Not specified"))

        lines.append(f"\n---\n")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python process.py generate [--output ropa.json] [--markdown report.md]")
        print("  python process.py validate <ropa_file.json>")
        print("  python process.py report <ropa_file.json> [--output report.md]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "generate":
        ropa = create_sample_processor_ropa()
        ropa_json = json.dumps(ropa, indent=2, default=str)

        json_output = None
        md_output = None
        for i, arg in enumerate(sys.argv):
            if arg == "--output" and i + 1 < len(sys.argv):
                json_output = sys.argv[i + 1]
            if arg == "--markdown" and i + 1 < len(sys.argv):
                md_output = sys.argv[i + 1]

        if json_output:
            with open(json_output, "w", encoding="utf-8") as f:
                f.write(ropa_json)
            print(f"Processor RoPA JSON written to {json_output}")
        else:
            print(ropa_json)

        if md_output:
            report = generate_markdown_report(ropa)
            with open(md_output, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"Markdown report written to {md_output}")

    elif command == "validate":
        if len(sys.argv) < 3:
            print("ERROR: Provide the path to the processor RoPA JSON file.")
            sys.exit(1)

        with open(sys.argv[2], "r", encoding="utf-8") as f:
            ropa_data = json.load(f)

        all_issues = []
        for record in ropa_data.get("records", []):
            all_issues.extend(validate_processor_entry(record))

        if not all_issues:
            print("PASS: All processor records comply with Art. 30(2) requirements.")
            sys.exit(0)

        print(f"VALIDATION: {len(all_issues)} issue(s) found\n")
        for issue in all_issues:
            print(f"[{issue['severity']}] {issue['record_id']} — {issue['field']}")
            print(f"  {issue['article']}: {issue['issue']}\n")

        critical = sum(1 for i in all_issues if i["severity"] == "Critical")
        print(f"Summary: {critical} Critical, {len(all_issues) - critical} Major/Minor")
        sys.exit(2 if critical > 0 else 1)

    elif command == "report":
        if len(sys.argv) < 3:
            print("ERROR: Provide path to processor RoPA JSON.")
            sys.exit(1)

        with open(sys.argv[2], "r", encoding="utf-8") as f:
            ropa_data = json.load(f)

        report = generate_markdown_report(ropa_data)
        output_path = None
        if "--output" in sys.argv:
            idx = sys.argv.index("--output")
            if idx + 1 < len(sys.argv):
                output_path = sys.argv[idx + 1]

        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"Report written to {output_path}")
        else:
            print(report)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
