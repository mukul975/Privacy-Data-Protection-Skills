#!/usr/bin/env python3
"""
Automated RoPA Generator

Generates draft RoPA entries from IT system inventory data including
database schemas, cloud service catalogs, and application registrations.
Applies PII detection patterns to identify personal data categories
and flags fields requiring human review.
"""

import json
import re
import sys
from datetime import datetime
from typing import Any


PII_PATTERNS = {
    "name": {
        "patterns": [r"(?i)(first_?name|last_?name|full_?name|sur_?name|given_?name|family_?name|display_?name|contact_?name|person_?name)"],
        "data_category": "Name",
        "special_category": False,
    },
    "email": {
        "patterns": [r"(?i)(e_?mail|email_?addr|mail_?address)"],
        "data_category": "Email address",
        "special_category": False,
    },
    "phone": {
        "patterns": [r"(?i)(phone|mobile|telephone|fax|cell_?phone)"],
        "data_category": "Phone number",
        "special_category": False,
    },
    "address": {
        "patterns": [r"(?i)(street|postal_?code|zip_?code|city|country|address_?line|postcode|house_?number)"],
        "data_category": "Postal address",
        "special_category": False,
    },
    "dob": {
        "patterns": [r"(?i)(date_?of_?birth|birth_?date|dob|birthday)"],
        "data_category": "Date of birth",
        "special_category": False,
    },
    "national_id": {
        "patterns": [r"(?i)(ssn|social_?security|tax_?id|national_?id|passport|id_?number|personal_?number|bsn|nif|steuer)"],
        "data_category": "National identification number",
        "special_category": False,
    },
    "financial": {
        "patterns": [r"(?i)(salary|bank_?account|iban|bic|swift|compensation|wage|credit_?card|debit_?card|payment)"],
        "data_category": "Financial data",
        "special_category": False,
    },
    "ip_address": {
        "patterns": [r"(?i)(ip_?addr|ip_?address|remote_?addr|client_?ip|source_?ip)"],
        "data_category": "IP address",
        "special_category": False,
    },
    "health": {
        "patterns": [r"(?i)(diagnosis|medical|health|condition|symptom|treatment|medication|allergy|blood_?type|patient)"],
        "data_category": "Health data",
        "special_category": True,
    },
    "genetic": {
        "patterns": [r"(?i)(genetic|dna|genome|genotype|biomarker|brca|her2|mutation)"],
        "data_category": "Genetic data",
        "special_category": True,
    },
    "biometric": {
        "patterns": [r"(?i)(biometric|fingerprint|facial|retina|iris|voice_?print)"],
        "data_category": "Biometric data",
        "special_category": True,
    },
    "ethnicity": {
        "patterns": [r"(?i)(ethnic|race|racial|ethnicity)"],
        "data_category": "Racial or ethnic origin",
        "special_category": True,
    },
    "religion": {
        "patterns": [r"(?i)(religion|religious|belief|church|faith)"],
        "data_category": "Religious or philosophical beliefs",
        "special_category": True,
    },
    "political": {
        "patterns": [r"(?i)(political|party_?affiliation)"],
        "data_category": "Political opinions",
        "special_category": True,
    },
    "union": {
        "patterns": [r"(?i)(trade_?union|union_?member)"],
        "data_category": "Trade union membership",
        "special_category": True,
    },
    "criminal": {
        "patterns": [r"(?i)(criminal|conviction|offence|arrest|sentence)"],
        "data_category": "Criminal conviction data (Art. 10)",
        "special_category": True,
    },
}


def scan_schema(schema: dict) -> list[dict]:
    """Scan a database schema for personal data columns.

    Expected schema format:
    {
        "database": "hr_db",
        "tables": [
            {
                "name": "employees",
                "columns": [
                    {"name": "employee_id", "type": "INTEGER"},
                    {"name": "first_name", "type": "VARCHAR(100)"},
                    ...
                ]
            }
        ]
    }
    """
    findings = []
    database = schema.get("database", "unknown")

    for table in schema.get("tables", []):
        table_name = table.get("name", "unknown")
        for column in table.get("columns", []):
            col_name = column.get("name", "")
            col_type = column.get("type", "")

            for category_key, category_info in PII_PATTERNS.items():
                for pattern in category_info["patterns"]:
                    if re.search(pattern, col_name):
                        findings.append({
                            "database": database,
                            "table": table_name,
                            "column": col_name,
                            "column_type": col_type,
                            "data_category": category_info["data_category"],
                            "special_category": category_info["special_category"],
                            "pattern_matched": category_key,
                            "confidence": "High" if len(col_name) > 5 else "Medium",
                        })
                        break

    return findings


def infer_data_subjects(table_name: str) -> list[str]:
    """Infer data subject categories from table name."""
    table_lower = table_name.lower()
    subjects = []

    subject_patterns = {
        "employee": "Employees",
        "staff": "Employees",
        "worker": "Employees",
        "personnel": "Employees",
        "contractor": "Contractors",
        "consultant": "Consultants",
        "applicant": "Job applicants",
        "candidate": "Job applicants",
        "customer": "Customers",
        "client": "Clients",
        "patient": "Patients",
        "participant": "Clinical trial participants",
        "subject": "Research subjects",
        "visitor": "Website visitors",
        "user": "System users",
        "supplier": "Supplier contacts",
        "vendor": "Vendor contacts",
        "subscriber": "Subscribers",
        "member": "Members",
        "student": "Students",
        "intern": "Interns",
    }

    for pattern, subject in subject_patterns.items():
        if pattern in table_lower:
            subjects.append(subject)

    return subjects if subjects else ["Unknown — requires manual classification"]


def detect_transfers(services: list[dict]) -> list[dict]:
    """Detect potential international transfers from cloud service configurations."""
    eea_regions = {
        "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "eu-south-1", "eu-south-2",
        "westeurope", "northeurope", "francecentral", "francesouth", "germanywestcentral",
        "germanynorth", "swedencentral", "norwayeast", "switzerlandnorth", "switzerlandwest",
        "europe-west1", "europe-west2", "europe-west3", "europe-west4", "europe-north1",
    }

    transfers = []
    for service in services:
        region = service.get("region", "").lower()
        if region and region not in eea_regions:
            region_country = map_region_to_country(region)
            transfers.append({
                "service": service.get("name", "Unknown"),
                "region": service.get("region", "Unknown"),
                "country": region_country,
                "data_indicator": service.get("data_classification", "Unknown"),
                "safeguard_mechanism": "REQUIRED — determine appropriate transfer mechanism",
                "status": "DRAFT — requires DPO review",
            })

    return transfers


def map_region_to_country(region: str) -> str:
    """Map cloud region identifiers to country names."""
    region_map = {
        "us-east-1": "United States", "us-east-2": "United States",
        "us-west-1": "United States", "us-west-2": "United States",
        "ap-southeast-1": "Singapore", "ap-southeast-2": "Australia",
        "ap-northeast-1": "Japan", "ap-northeast-2": "South Korea",
        "ap-south-1": "India", "sa-east-1": "Brazil",
        "ca-central-1": "Canada", "me-south-1": "Bahrain",
        "af-south-1": "South Africa",
        "eastus": "United States", "westus": "United States",
        "eastasia": "Hong Kong", "southeastasia": "Singapore",
        "japaneast": "Japan", "australiaeast": "Australia",
        "brazilsouth": "Brazil", "canadacentral": "Canada",
        "centralindia": "India", "koreacentral": "South Korea",
        "uksouth": "United Kingdom", "ukwest": "United Kingdom",
    }
    return region_map.get(region.lower(), f"Unknown ({region})")


def generate_draft_ropa_from_schema(schema: dict, org_config: dict) -> dict:
    """Generate a draft RoPA entry from a database schema scan."""
    findings = scan_schema(schema)
    database = schema.get("database", "unknown")

    data_categories = list(set(f["data_category"] for f in findings))
    special_categories = [f["data_category"] for f in findings if f["special_category"]]

    all_subjects = set()
    for table in schema.get("tables", []):
        subjects = infer_data_subjects(table["name"])
        all_subjects.update(subjects)

    return {
        "record_id": f"RPA-AUTO-{database.upper()[:10]}",
        "record_type": "controller",
        "processing_activity": f"DRAFT — Processing in {database} database",
        "status": "DRAFT — requires DPO and processing owner review",
        "auto_generated": True,
        "generation_date": datetime.now().strftime("%Y-%m-%d"),
        "controller_identity": org_config.get("controller_identity", {}),
        "purposes": ["DRAFT — purpose must be articulated by processing owner. Cannot be determined from technical metadata."],
        "lawful_basis": "DRAFT — lawful basis must be determined by DPO",
        "data_subject_categories": sorted(all_subjects),
        "personal_data_categories": sorted(data_categories),
        "special_category_data": f"Art. 9 special categories detected: {', '.join(special_categories)}" if special_categories else "None detected",
        "recipient_categories": ["DRAFT — identify recipients from AD security groups and API integrations"],
        "international_transfers": [],
        "retention_periods": "DRAFT — determine retention policy. Actual data age can be assessed from database statistics.",
        "security_measures": "DRAFT — extract from cloud and infrastructure security configuration",
        "schema_scan_results": {
            "database": database,
            "tables_scanned": len(schema.get("tables", [])),
            "pii_columns_detected": len(findings),
            "special_category_detected": len(special_categories) > 0,
            "detailed_findings": findings,
        },
    }


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python process.py scan-schema <schema.json> [--org-config org.json] [--output draft_ropa.json]")
        print("  python process.py detect-transfers <services.json>")
        print("  python process.py demo")
        sys.exit(1)

    command = sys.argv[1]

    if command == "demo":
        # Demonstrate with Helix Biotech sample schema
        sample_schema = {
            "database": "helix_hr_db",
            "tables": [
                {
                    "name": "employees",
                    "columns": [
                        {"name": "employee_id", "type": "INTEGER"},
                        {"name": "first_name", "type": "VARCHAR(100)"},
                        {"name": "last_name", "type": "VARCHAR(100)"},
                        {"name": "email_address", "type": "VARCHAR(255)"},
                        {"name": "phone_number", "type": "VARCHAR(20)"},
                        {"name": "date_of_birth", "type": "DATE"},
                        {"name": "tax_id", "type": "VARCHAR(20)"},
                        {"name": "social_security_number", "type": "VARCHAR(20)"},
                        {"name": "bank_account_iban", "type": "VARCHAR(34)"},
                        {"name": "salary_amount", "type": "DECIMAL(10,2)"},
                        {"name": "department", "type": "VARCHAR(100)"},
                        {"name": "hire_date", "type": "DATE"},
                        {"name": "religion_indicator", "type": "VARCHAR(50)"},
                    ],
                },
                {
                    "name": "clinical_participants",
                    "columns": [
                        {"name": "participant_id", "type": "VARCHAR(20)"},
                        {"name": "date_of_birth", "type": "DATE"},
                        {"name": "diagnosis_code", "type": "VARCHAR(10)"},
                        {"name": "medical_history", "type": "TEXT"},
                        {"name": "genetic_biomarker", "type": "VARCHAR(50)"},
                        {"name": "treatment_allocation", "type": "VARCHAR(50)"},
                        {"name": "ethnicity_code", "type": "VARCHAR(10)"},
                        {"name": "adverse_event_description", "type": "TEXT"},
                    ],
                },
            ],
        }

        org_config = {
            "controller_identity": {
                "legal_entity_name": "Helix Biotech Solutions GmbH",
                "registered_address": "Leopoldstrasse 42, 80802 Munich, Germany",
                "contact_email": "privacy@helix-biotech.eu",
                "dpo_name": "Dr. Elena Voss",
                "dpo_email": "dpo@helix-biotech.eu",
            }
        }

        print("=" * 70)
        print("AUTOMATED RoPA GENERATION — DEMO")
        print("=" * 70)

        # Schema scan
        findings = scan_schema(sample_schema)
        print(f"\nSchema Scan Results for '{sample_schema['database']}':")
        print(f"  Tables scanned: {len(sample_schema['tables'])}")
        print(f"  PII columns detected: {len(findings)}")
        print(f"  Special category columns: {sum(1 for f in findings if f['special_category'])}")

        print("\nDetailed PII Findings:")
        for f in findings:
            special = " [ART. 9 SPECIAL CATEGORY]" if f["special_category"] else ""
            print(f"  {f['table']}.{f['column']} -> {f['data_category']}{special}")

        # Generate draft RoPA
        draft = generate_draft_ropa_from_schema(sample_schema, org_config)
        print(f"\n{'=' * 70}")
        print("DRAFT RoPA ENTRY GENERATED")
        print(f"{'=' * 70}")
        print(json.dumps(draft, indent=2, default=str))

    elif command == "scan-schema":
        if len(sys.argv) < 3:
            print("ERROR: Provide the schema JSON file path.")
            sys.exit(1)

        with open(sys.argv[2], "r", encoding="utf-8") as f:
            schema = json.load(f)

        org_config = {}
        if "--org-config" in sys.argv:
            idx = sys.argv.index("--org-config")
            if idx + 1 < len(sys.argv):
                with open(sys.argv[idx + 1], "r", encoding="utf-8") as f:
                    org_config = json.load(f)

        draft = generate_draft_ropa_from_schema(schema, org_config)

        output = None
        if "--output" in sys.argv:
            idx = sys.argv.index("--output")
            if idx + 1 < len(sys.argv):
                output = sys.argv[idx + 1]

        draft_json = json.dumps(draft, indent=2, default=str)
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(draft_json)
            print(f"Draft RoPA written to {output}")
        else:
            print(draft_json)

    elif command == "detect-transfers":
        if len(sys.argv) < 3:
            print("ERROR: Provide the services JSON file path.")
            sys.exit(1)

        with open(sys.argv[2], "r", encoding="utf-8") as f:
            services = json.load(f)

        transfers = detect_transfers(services)
        if transfers:
            print(f"POTENTIAL INTERNATIONAL TRANSFERS DETECTED: {len(transfers)}\n")
            for t in transfers:
                print(f"  Service: {t['service']}")
                print(f"  Region: {t['region']} -> {t['country']}")
                print(f"  Status: {t['status']}")
                print()
        else:
            print("No non-EEA deployments detected.")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
