#!/usr/bin/env python3
"""
Data Portability Export Generator

Generates a structured portability export package with manifest,
schema documentation, and sample data structure compliant with
GDPR Article 20 requirements.
"""

import argparse
import hashlib
import json
import csv
import io
import os
import zipfile
from datetime import datetime
from typing import Optional


SUPPORTED_FORMATS = {"json", "csv", "xml"}

PORTABLE_LEGAL_BASES = {
    "consent": "Art. 6(1)(a) GDPR — Consent",
    "explicit_consent": "Art. 9(2)(a) GDPR — Explicit consent for special category data",
    "contract": "Art. 6(1)(b) GDPR — Performance of a contract",
}

NON_PORTABLE_LEGAL_BASES = {
    "legal_obligation": "Art. 6(1)(c) GDPR — Legal obligation",
    "vital_interests": "Art. 6(1)(d) GDPR — Vital interests",
    "public_interest": "Art. 6(1)(e) GDPR — Public interest",
    "legitimate_interests": "Art. 6(1)(f) GDPR — Legitimate interests",
}


def assess_portability_scope(data_categories: list) -> dict:
    """
    Assess which data categories are in scope for portability.

    Each category is a dict with keys: name, source, legal_basis, automated.
    """
    in_scope = []
    out_of_scope = []

    for cat in data_categories:
        reasons = []
        portable = True

        # Check source: provided/observed vs inferred
        if cat.get("source") == "inferred":
            reasons.append("Inferred/derived data is not portable (WP242 rev.01)")
            portable = False

        # Check legal basis
        if cat.get("legal_basis") not in PORTABLE_LEGAL_BASES:
            reasons.append(
                f"Legal basis '{cat.get('legal_basis')}' does not qualify for portability"
            )
            portable = False

        # Check automated processing
        if not cat.get("automated", True):
            reasons.append("Manual processing — Art. 20(1)(b) requires automated means")
            portable = False

        entry = {
            "name": cat["name"],
            "source": cat.get("source", "provided"),
            "legal_basis": cat.get("legal_basis", "unknown"),
            "automated": cat.get("automated", True),
            "portable": portable,
        }
        if not portable:
            entry["exclusion_reasons"] = reasons
            out_of_scope.append(entry)
        else:
            in_scope.append(entry)

    return {"in_scope": in_scope, "out_of_scope": out_of_scope}


def generate_manifest(
    reference: str,
    data_subject_id: str,
    files: list,
    export_format: str,
    export_date: str,
) -> dict:
    """Generate a portability export manifest."""
    return {
        "manifest_version": "1.0",
        "reference": reference,
        "data_subject_id": data_subject_id,
        "export_date": export_date,
        "export_format": export_format,
        "controller": {
            "name": "Meridian Analytics Ltd",
            "address": "47 Canary Wharf Tower, London E14 5AB",
            "dpo_contact": "dpo@meridiananalytics.co.uk",
        },
        "legal_basis": "GDPR Article 20 — Right to data portability",
        "files": files,
        "schema_version": "2.1",
        "encoding": "UTF-8",
        "checksum_algorithm": "SHA-256",
    }


def generate_sample_export(
    reference: str,
    data_subject_id: str,
    export_format: str = "json",
    output_dir: Optional[str] = None,
) -> dict:
    """
    Generate a sample portability export structure.

    In production, this would query actual databases. This implementation
    generates the complete file structure and manifest.
    """
    export_date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Define the data categories to export
    account_data = {
        "data_subject_id": data_subject_id,
        "account": {
            "registration_date": "2023-06-03T10:24:00Z",
            "account_type": "professional",
            "subscription_plan": "enterprise",
        },
        "identity": {
            "full_name": "[DATA SUBJECT NAME]",
            "date_of_birth": "[DATE OF BIRTH]",
            "job_title": "Head of Data Science",
            "organisation": "Northgate Financial Services Ltd",
        },
        "contact": {
            "email": "[EMAIL ADDRESS]",
            "phone": "[PHONE NUMBER]",
            "address": {
                "line_1": "[ADDRESS LINE 1]",
                "city": "[CITY]",
                "postcode": "[POSTCODE]",
                "country": "United Kingdom",
            },
        },
        "preferences": {
            "language": "en-GB",
            "timezone": "Europe/London",
            "notification_email": True,
            "notification_sms": False,
            "marketing_consent": False,
            "analytics_consent": True,
        },
    }

    transactions = [
        {
            "transaction_id": "TXN-2024-001847",
            "date": "2024-01-15T09:30:00Z",
            "type": "subscription_payment",
            "amount": 299.00,
            "currency": "GBP",
            "description": "Enterprise plan — monthly subscription",
        },
        {
            "transaction_id": "TXN-2024-002103",
            "date": "2024-02-15T09:30:00Z",
            "type": "subscription_payment",
            "amount": 299.00,
            "currency": "GBP",
            "description": "Enterprise plan — monthly subscription",
        },
    ]

    activity_logs = [
        {
            "timestamp": "2024-03-10T14:22:00Z",
            "action": "dashboard_view",
            "resource": "revenue-analytics-q1",
            "ip_address": "[IP ADDRESS]",
            "device": "Chrome 122 / Windows 11",
        },
        {
            "timestamp": "2024-03-10T14:35:00Z",
            "action": "report_generated",
            "resource": "custom-report-0847",
            "ip_address": "[IP ADDRESS]",
            "device": "Chrome 122 / Windows 11",
        },
    ]

    files_list = []

    if export_format == "json":
        files_list = [
            {
                "filename": "account_data.json",
                "description": "Account information, identity, contact, and preferences",
                "record_count": 1,
                "checksum": hashlib.sha256(
                    json.dumps(account_data).encode()
                ).hexdigest(),
            },
            {
                "filename": "transactions.json",
                "description": "Payment and subscription transaction history",
                "record_count": len(transactions),
                "checksum": hashlib.sha256(
                    json.dumps(transactions).encode()
                ).hexdigest(),
            },
            {
                "filename": "activity_logs.json",
                "description": "Platform usage activity (observed data)",
                "record_count": len(activity_logs),
                "checksum": hashlib.sha256(
                    json.dumps(activity_logs).encode()
                ).hexdigest(),
            },
        ]
    elif export_format == "csv":
        files_list = [
            {
                "filename": "account_data.csv",
                "description": "Account information (flattened)",
                "record_count": 1,
                "checksum": "computed_at_generation",
            },
            {
                "filename": "transactions.csv",
                "description": "Payment and subscription transaction history",
                "record_count": len(transactions),
                "checksum": "computed_at_generation",
            },
            {
                "filename": "activity_logs.csv",
                "description": "Platform usage activity (observed data)",
                "record_count": len(activity_logs),
                "checksum": "computed_at_generation",
            },
        ]

    manifest = generate_manifest(
        reference=reference,
        data_subject_id=data_subject_id,
        files=files_list,
        export_format=export_format,
        export_date=export_date,
    )

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

        # Write manifest
        manifest_path = os.path.join(output_dir, "manifest.json")
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)

        if export_format == "json":
            with open(os.path.join(output_dir, "account_data.json"), "w", encoding="utf-8") as f:
                json.dump(account_data, f, indent=2)
            with open(os.path.join(output_dir, "transactions.json"), "w", encoding="utf-8") as f:
                json.dump(transactions, f, indent=2)
            with open(os.path.join(output_dir, "activity_logs.json"), "w", encoding="utf-8") as f:
                json.dump(activity_logs, f, indent=2)

        elif export_format == "csv":
            # Transactions CSV
            txn_path = os.path.join(output_dir, "transactions.csv")
            with open(txn_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f, fieldnames=["transaction_id", "date", "type", "amount", "currency", "description"]
                )
                writer.writeheader()
                writer.writerows(transactions)

            # Activity logs CSV
            log_path = os.path.join(output_dir, "activity_logs.csv")
            with open(log_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f, fieldnames=["timestamp", "action", "resource", "ip_address", "device"]
                )
                writer.writeheader()
                writer.writerows(activity_logs)

        print(f"Export files written to: {output_dir}")

    return {
        "manifest": manifest,
        "scope_summary": {
            "categories_exported": ["account_data", "transactions", "activity_logs"],
            "categories_excluded": ["profiling_scores", "internal_risk_assessments"],
            "exclusion_reason": "Inferred/derived data not portable under WP242 rev.01",
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Generate GDPR Art. 20 data portability export"
    )
    parser.add_argument("--reference", default="PORT-2026-0314", help="Request reference")
    parser.add_argument("--subject-id", default="DS-0001", help="Data subject ID")
    parser.add_argument(
        "--format",
        choices=list(SUPPORTED_FORMATS),
        default="json",
        help="Export format",
    )
    parser.add_argument("--output-dir", help="Directory to write export files")
    parser.add_argument("--json", action="store_true", help="Output summary as JSON")

    args = parser.parse_args()

    result = generate_sample_export(
        reference=args.reference,
        data_subject_id=args.subject_id,
        export_format=args.format,
        output_dir=args.output_dir,
    )

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        manifest = result["manifest"]
        print("=" * 60)
        print("DATA PORTABILITY EXPORT SUMMARY")
        print("=" * 60)
        print(f"Reference:       {manifest['reference']}")
        print(f"Subject ID:      {manifest['data_subject_id']}")
        print(f"Export Date:     {manifest['export_date']}")
        print(f"Format:          {manifest['export_format']}")
        print(f"Controller:      {manifest['controller']['name']}")
        print()
        print("Files:")
        for f in manifest["files"]:
            print(f"  {f['filename']} — {f['description']} ({f['record_count']} records)")
        print()
        scope = result["scope_summary"]
        print(f"Categories exported:  {', '.join(scope['categories_exported'])}")
        print(f"Categories excluded:  {', '.join(scope['categories_excluded'])}")
        print(f"Exclusion reason:     {scope['exclusion_reason']}")
        print("=" * 60)


if __name__ == "__main__":
    main()
