#!/usr/bin/env python3
"""
RoPA Tool Integration — Multi-Platform Sync Engine

Provides synchronisation capabilities between local RoPA JSON format
and privacy management platforms (OneTrust, TrustArc, Collibra, DataGrail).
Supports import, export, and bidirectional sync operations.
"""

import json
import sys
import os
import csv
from datetime import datetime
from typing import Any


def load_ropa_json(file_path: str) -> dict:
    """Load a RoPA JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def export_to_onetrust_format(ropa: dict) -> list[dict]:
    """Convert local RoPA format to OneTrust import schema."""
    onetrust_records = []

    for record in ropa.get("records", []):
        ot_record = {
            "name": record.get("processing_activity", record.get("service_name", "Untitled")),
            "description": "",
            "organizationName": ropa.get("organisation", ""),
            "status": "Active",
            "purposes": [],
            "dataSubjectCategories": [],
            "dataElementCategories": [],
            "thirdParties": [],
            "transfers": [],
            "retentionPeriod": "",
            "securityMeasures": "",
            "lastReviewDate": record.get("last_reviewed_date", ""),
            "owner": record.get("processing_owner", record.get("record_owner", "")),
        }

        # Map purposes
        purposes = record.get("purposes", [])
        if isinstance(purposes, list):
            for p in purposes:
                ot_record["purposes"].append({
                    "name": p if isinstance(p, str) else str(p),
                    "legalBasis": record.get("lawful_basis", ""),
                })
        elif isinstance(purposes, str):
            ot_record["purposes"].append({"name": purposes, "legalBasis": record.get("lawful_basis", "")})

        # Map data subjects
        for ds in record.get("data_subject_categories", []):
            ot_record["dataSubjectCategories"].append({"name": ds})

        # Map data categories
        for dc in record.get("personal_data_categories", []):
            ot_record["dataElementCategories"].append({"name": dc})

        # Map recipients
        for r in record.get("recipient_categories", []):
            if isinstance(r, dict):
                ot_record["thirdParties"].append({
                    "name": r.get("recipient", ""),
                    "type": r.get("type", ""),
                    "purpose": r.get("purpose", ""),
                    "dpaReference": r.get("dpa_reference", ""),
                })
            elif isinstance(r, str):
                ot_record["thirdParties"].append({"name": r})

        # Map transfers
        for t in record.get("international_transfers", []):
            if isinstance(t, dict):
                ot_record["transfers"].append({
                    "destinationCountry": t.get("destination_country", ""),
                    "recipient": t.get("recipient", ""),
                    "safeguardMechanism": t.get("safeguard_mechanism", ""),
                    "tiaReference": t.get("tia_reference", ""),
                })

        # Retention
        retention = record.get("retention_periods", "")
        if isinstance(retention, dict):
            ot_record["retentionPeriod"] = "; ".join(f"{k}: {v}" for k, v in retention.items())
        elif isinstance(retention, str):
            ot_record["retentionPeriod"] = retention

        # Security
        ot_record["securityMeasures"] = record.get("security_measures", "")

        onetrust_records.append(ot_record)

    return onetrust_records


def export_to_csv(ropa: dict, output_path: str) -> None:
    """Export RoPA to CSV format suitable for platform import."""
    records = ropa.get("records", [])
    if not records:
        print("No records to export.")
        return

    rows = []
    for record in records:
        row = {
            "Record ID": record.get("record_id", ""),
            "Record Type": record.get("record_type", "controller"),
            "Processing Activity": record.get("processing_activity", record.get("service_name", "")),
            "Department": record.get("department", ""),
            "Processing Owner": record.get("processing_owner", record.get("record_owner", "")),
            "Controller Name": "",
            "Controller Email": "",
            "DPO Name": "",
            "DPO Email": "",
            "Purposes": "",
            "Lawful Basis": record.get("lawful_basis", ""),
            "Data Subject Categories": "",
            "Personal Data Categories": "",
            "Special Category Data": record.get("special_category_data", "None"),
            "Recipient Categories": "",
            "International Transfers": "",
            "Retention Periods": "",
            "Security Measures": record.get("security_measures", ""),
            "DPIA Required": str(record.get("dpia_required", False)),
            "DPIA Reference": record.get("dpia_reference", ""),
            "Created Date": record.get("created_date", ""),
            "Last Reviewed": record.get("last_reviewed_date", ""),
            "Next Review": record.get("next_review_date", ""),
        }

        # Controller identity
        ci = record.get("controller_identity", record.get("processor_identity", {}))
        if isinstance(ci, dict):
            row["Controller Name"] = ci.get("legal_entity_name", "")
            row["Controller Email"] = ci.get("contact_email", "")
            row["DPO Name"] = ci.get("dpo_name", "")
            row["DPO Email"] = ci.get("dpo_email", "")

        # Purposes
        purposes = record.get("purposes", [])
        if isinstance(purposes, list):
            row["Purposes"] = " | ".join(purposes)
        elif isinstance(purposes, str):
            row["Purposes"] = purposes

        # Data subjects
        ds = record.get("data_subject_categories", [])
        row["Data Subject Categories"] = " | ".join(ds) if isinstance(ds, list) else str(ds)

        # Data categories
        dc = record.get("personal_data_categories", [])
        row["Personal Data Categories"] = " | ".join(dc) if isinstance(dc, list) else str(dc)

        # Recipients
        recipients = record.get("recipient_categories", [])
        if isinstance(recipients, list):
            recipient_strs = []
            for r in recipients:
                if isinstance(r, dict):
                    recipient_strs.append(f"{r.get('recipient', '')} ({r.get('type', '')})")
                else:
                    recipient_strs.append(str(r))
            row["Recipient Categories"] = " | ".join(recipient_strs)

        # Transfers
        transfers = record.get("international_transfers", [])
        if isinstance(transfers, list):
            transfer_strs = []
            for t in transfers:
                if isinstance(t, dict):
                    transfer_strs.append(f"{t.get('destination_country', '')} -> {t.get('recipient', '')} ({t.get('safeguard_mechanism', '')})")
            row["International Transfers"] = " | ".join(transfer_strs) if transfer_strs else "None"
        else:
            row["International Transfers"] = "None"

        # Retention
        retention = record.get("retention_periods", "")
        if isinstance(retention, dict):
            row["Retention Periods"] = " | ".join(f"{k}: {v}" for k, v in retention.items())
        elif isinstance(retention, str):
            row["Retention Periods"] = retention

        rows.append(row)

    if rows:
        fieldnames = rows[0].keys()
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Exported {len(rows)} records to {output_path}")


def import_from_csv(csv_path: str) -> dict:
    """Import RoPA records from a CSV file into local JSON format."""
    records = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            record = {
                "record_id": row.get("Record ID", ""),
                "record_type": row.get("Record Type", "controller"),
                "processing_activity": row.get("Processing Activity", ""),
                "department": row.get("Department", ""),
                "processing_owner": row.get("Processing Owner", ""),
                "controller_identity": {
                    "legal_entity_name": row.get("Controller Name", ""),
                    "contact_email": row.get("Controller Email", ""),
                    "dpo_name": row.get("DPO Name", ""),
                    "dpo_email": row.get("DPO Email", ""),
                },
                "purposes": [p.strip() for p in row.get("Purposes", "").split("|") if p.strip()],
                "lawful_basis": row.get("Lawful Basis", ""),
                "data_subject_categories": [d.strip() for d in row.get("Data Subject Categories", "").split("|") if d.strip()],
                "personal_data_categories": [d.strip() for d in row.get("Personal Data Categories", "").split("|") if d.strip()],
                "special_category_data": row.get("Special Category Data", "None"),
                "retention_periods": row.get("Retention Periods", ""),
                "security_measures": row.get("Security Measures", ""),
                "created_date": row.get("Created Date", ""),
                "last_reviewed_date": row.get("Last Reviewed", ""),
                "next_review_date": row.get("Next Review", ""),
            }
            records.append(record)

    return {
        "organisation": "Imported RoPA",
        "ropa_version": "1.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "records": records,
    }


def generate_platform_mapping_report(ropa: dict) -> str:
    """Generate a report showing how RoPA fields map to each platform."""
    lines = []
    lines.append("=" * 80)
    lines.append("RoPA PLATFORM FIELD MAPPING REPORT")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Organisation: {ropa.get('organisation', 'Unknown')}")
    lines.append(f"Records: {len(ropa.get('records', []))}")
    lines.append("=" * 80)

    mappings = {
        "Art. 30(1)(a) Controller Identity": {
            "OneTrust": "Organization > Legal Entity",
            "TrustArc": "Assessment > Controller Details",
            "Collibra": "Business Asset > Organisation",
            "DataGrail": "Organization Settings",
        },
        "Art. 30(1)(b) Purposes": {
            "OneTrust": "Processing Activity > Purposes",
            "TrustArc": "Assessment > Purpose of Processing",
            "Collibra": "Processing Activity > Purpose (attribute)",
            "DataGrail": "Data Map > Purpose",
        },
        "Art. 30(1)(c) Data Subjects": {
            "OneTrust": "Processing Activity > Data Subjects",
            "TrustArc": "Assessment > Data Subject Categories",
            "Collibra": "Related Asset > Data Subject Category",
            "DataGrail": "Data Map > Data Subjects",
        },
        "Art. 30(1)(c) Data Categories": {
            "OneTrust": "Processing Activity > Data Elements",
            "TrustArc": "Assessment > Data Categories",
            "Collibra": "Related Asset > Data Category (glossary)",
            "DataGrail": "Data Map > Data Categories (auto-discovered)",
        },
        "Art. 30(1)(d) Recipients": {
            "OneTrust": "Processing Activity > Third Parties + Vendorpedia",
            "TrustArc": "Assessment > Recipients",
            "Collibra": "Relation > shares data with Organisation/System",
            "DataGrail": "Connected Systems > Vendors",
        },
        "Art. 30(1)(e) Transfers": {
            "OneTrust": "Processing Activity > Cross Border Transfers",
            "TrustArc": "Assessment > International Transfers",
            "Collibra": "Relation > transfers to Geography",
            "DataGrail": "Data Map > Cross-Border Flows",
        },
        "Art. 30(1)(f) Retention": {
            "OneTrust": "Processing Activity > Retention",
            "TrustArc": "Assessment > Retention Period",
            "Collibra": "Processing Activity > Retention (attribute)",
            "DataGrail": "Data Map > Retention Policy",
        },
        "Art. 30(1)(g) Security": {
            "OneTrust": "Processing Activity > Security Measures",
            "TrustArc": "Assessment > Security Measures",
            "Collibra": "Related Asset > Security Control",
            "DataGrail": "Manual entry",
        },
    }

    for field, platforms in mappings.items():
        lines.append(f"\n{field}")
        for platform, mapping in platforms.items():
            lines.append(f"  {platform:15s} -> {mapping}")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python process.py export-csv <ropa.json> --output <output.csv>")
        print("  python process.py export-onetrust <ropa.json> --output <output.json>")
        print("  python process.py import-csv <input.csv> --output <ropa.json>")
        print("  python process.py mapping-report <ropa.json>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "export-csv":
        if len(sys.argv) < 3:
            print("ERROR: Provide the RoPA JSON file path.")
            sys.exit(1)
        ropa = load_ropa_json(sys.argv[2])
        output = "ropa_export.csv"
        if "--output" in sys.argv:
            idx = sys.argv.index("--output")
            if idx + 1 < len(sys.argv):
                output = sys.argv[idx + 1]
        export_to_csv(ropa, output)

    elif command == "export-onetrust":
        if len(sys.argv) < 3:
            print("ERROR: Provide the RoPA JSON file path.")
            sys.exit(1)
        ropa = load_ropa_json(sys.argv[2])
        ot_records = export_to_onetrust_format(ropa)
        output = "onetrust_import.json"
        if "--output" in sys.argv:
            idx = sys.argv.index("--output")
            if idx + 1 < len(sys.argv):
                output = sys.argv[idx + 1]
        with open(output, "w", encoding="utf-8") as f:
            json.dump(ot_records, f, indent=2)
        print(f"OneTrust import file written to {output} ({len(ot_records)} records)")

    elif command == "import-csv":
        if len(sys.argv) < 3:
            print("ERROR: Provide the CSV file path.")
            sys.exit(1)
        ropa = import_from_csv(sys.argv[2])
        output = "imported_ropa.json"
        if "--output" in sys.argv:
            idx = sys.argv.index("--output")
            if idx + 1 < len(sys.argv):
                output = sys.argv[idx + 1]
        with open(output, "w", encoding="utf-8") as f:
            json.dump(ropa, f, indent=2)
        print(f"Imported {len(ropa['records'])} records to {output}")

    elif command == "mapping-report":
        if len(sys.argv) < 3:
            print("ERROR: Provide the RoPA JSON file path.")
            sys.exit(1)
        ropa = load_ropa_json(sys.argv[2])
        report = generate_platform_mapping_report(ropa)
        print(report)

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
