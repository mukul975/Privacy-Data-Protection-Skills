#!/usr/bin/env python3
"""
Controller RoPA Generator

Generates GDPR Article 30(1) compliant Records of Processing Activities
for data controllers. Outputs structured JSON and formatted Markdown reports.
Validates all seven mandatory fields before generating the record.
"""

import json
import sys
from datetime import datetime, date
from typing import Any


CONTROLLER_MANDATORY_FIELDS = {
    "controller_identity": {
        "article": "Art. 30(1)(a)",
        "description": "Name and contact details of controller, joint controller, representative, and DPO",
        "required_sub_fields": ["legal_entity_name", "registered_address", "contact_email", "dpo_name", "dpo_email"],
    },
    "purposes": {
        "article": "Art. 30(1)(b)",
        "description": "Purposes of the processing",
        "required_sub_fields": [],
    },
    "data_subject_categories": {
        "article": "Art. 30(1)(c)",
        "description": "Categories of data subjects",
        "required_sub_fields": [],
    },
    "personal_data_categories": {
        "article": "Art. 30(1)(c)",
        "description": "Categories of personal data",
        "required_sub_fields": [],
    },
    "recipient_categories": {
        "article": "Art. 30(1)(d)",
        "description": "Categories of recipients including third-country recipients",
        "required_sub_fields": [],
    },
    "international_transfers": {
        "article": "Art. 30(1)(e)",
        "description": "Transfers to third countries or international organisations",
        "required_sub_fields": [],
    },
    "retention_periods": {
        "article": "Art. 30(1)(f)",
        "description": "Envisaged time limits for erasure of different categories of data",
        "required_sub_fields": [],
    },
    "security_measures": {
        "article": "Art. 30(1)(g)",
        "description": "General description of technical and organisational security measures per Art. 32(1)",
        "required_sub_fields": [],
    },
}

VAGUE_PURPOSE_TERMS = [
    "business purposes", "business operations", "general purposes",
    "various purposes", "as needed", "other purposes", "internal use",
    "operational purposes", "miscellaneous", "general use",
]

VAGUE_RETENTION_TERMS = [
    "as long as necessary", "indefinitely", "until no longer needed",
    "as required", "in accordance with policy", "per policy",
    "not determined", "tbd", "n/a", "to be confirmed",
]


def validate_non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str) and value.strip() == "":
        return False
    if isinstance(value, (list, dict)) and len(value) == 0:
        return False
    return True


def validate_entry(entry: dict) -> list[dict]:
    """Validate a single RoPA entry against Art. 30(1) requirements."""
    issues = []
    record_id = entry.get("record_id", "UNKNOWN")

    for field_name, spec in CONTROLLER_MANDATORY_FIELDS.items():
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

        if field_name == "purposes":
            text = " ".join(value) if isinstance(value, list) else str(value)
            for term in VAGUE_PURPOSE_TERMS:
                if term in text.lower():
                    issues.append({
                        "record_id": record_id,
                        "severity": "Major",
                        "field": "purposes",
                        "article": "Art. 30(1)(b) / Art. 5(1)(b)",
                        "issue": f"Vague purpose term detected: '{term}'. Purposes must be specific and explicit.",
                    })

        if field_name == "retention_periods":
            text = ""
            if isinstance(value, str):
                text = value.lower()
            elif isinstance(value, list):
                text = " ".join(str(v).lower() for v in value)
            elif isinstance(value, dict):
                text = " ".join(str(v).lower() for v in value.values())
            for term in VAGUE_RETENTION_TERMS:
                if term in text:
                    issues.append({
                        "record_id": record_id,
                        "severity": "Major",
                        "field": "retention_periods",
                        "article": "Art. 30(1)(f) / Art. 5(1)(e)",
                        "issue": f"Vague retention term detected: '{term}'. Specify concrete duration or criteria.",
                    })

        if field_name == "international_transfers" and isinstance(value, list):
            for idx, transfer in enumerate(value):
                if isinstance(transfer, dict):
                    if not transfer.get("destination_country"):
                        issues.append({
                            "record_id": record_id,
                            "severity": "Major",
                            "field": f"international_transfers[{idx}]",
                            "article": "Art. 30(1)(e)",
                            "issue": "Transfer missing destination country identification",
                        })
                    if not transfer.get("safeguard_mechanism"):
                        issues.append({
                            "record_id": record_id,
                            "severity": "Major",
                            "field": f"international_transfers[{idx}]",
                            "article": "Art. 30(1)(e) / Chapter V",
                            "issue": "Transfer missing safeguard mechanism (SCCs, adequacy decision, BCRs, or Art. 49 derogation)",
                        })

    return issues


def create_sample_ropa() -> dict:
    """Generate a sample controller RoPA for Helix Biotech Solutions."""
    return {
        "organisation": "Helix Biotech Solutions GmbH",
        "ropa_version": "3.1",
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "prepared_by": "Dr. Elena Voss, Data Protection Officer",
        "records": [
            {
                "record_id": "RPA-001",
                "record_type": "controller",
                "processing_activity": "Employee payroll processing",
                "department": "Human Resources",
                "controller_identity": {
                    "legal_entity_name": "Helix Biotech Solutions GmbH",
                    "registered_address": "Leopoldstrasse 42, 80802 Munich, Germany",
                    "registration_number": "HRB 267891, Amtsgericht Munich",
                    "contact_email": "privacy@helix-biotech.eu",
                    "dpo_name": "Dr. Elena Voss",
                    "dpo_email": "dpo@helix-biotech.eu",
                    "dpo_phone": "+49 89 7654 3210",
                    "joint_controllers": None,
                    "eu_representative": "Not applicable (established in EEA)",
                },
                "purposes": [
                    "Calculation and disbursement of monthly salaries, bonuses, and statutory deductions for employees under employment contract obligation",
                    "Reporting of employee income and social security contributions to Finanzamt Munich and statutory health insurance providers under German tax and social security law",
                ],
                "lawful_basis": "Art. 6(1)(b) — performance of employment contract; Art. 6(1)(c) — compliance with legal obligations under EStG, SGB IV",
                "data_subject_categories": [
                    "Permanent employees",
                    "Fixed-term employees",
                    "Working students (Werkstudenten)",
                    "Interns",
                ],
                "personal_data_categories": [
                    "Full name",
                    "Employee ID",
                    "Date of birth",
                    "Tax identification number (Steuerliche Identifikationsnummer)",
                    "Social security number (Sozialversicherungsnummer)",
                    "Bank account details (IBAN, BIC)",
                    "Salary grade and compensation details",
                    "Working hours and overtime records",
                    "Tax class (Steuerklasse)",
                    "Church tax indicator",
                    "Health insurance provider",
                ],
                "special_category_data": "Church tax indicator reveals religious affiliation (Art. 9(1)). Processed under Art. 9(2)(b) — necessary for employment law obligations.",
                "recipient_categories": [
                    {
                        "recipient": "ADP Employer Services GmbH",
                        "type": "Processor",
                        "purpose": "Payroll calculation and payslip generation",
                        "dpa_reference": "DPA-2023-ADP-002, executed 2023-09-01",
                    },
                    {
                        "recipient": "Finanzamt Munich (Tax Authority)",
                        "type": "Public authority",
                        "purpose": "Statutory income tax reporting under Section 41a EStG",
                        "dpa_reference": "Legal obligation — no DPA required",
                    },
                    {
                        "recipient": "AOK Bayern",
                        "type": "Other controller (statutory insurer)",
                        "purpose": "Social security contribution reporting under SGB IV",
                        "dpa_reference": "Legal obligation — no DPA required",
                    },
                    {
                        "recipient": "Deutsche Rentenversicherung Bund",
                        "type": "Other controller (pension authority)",
                        "purpose": "Pension contribution reporting",
                        "dpa_reference": "Legal obligation — no DPA required",
                    },
                ],
                "international_transfers": [],
                "retention_periods": {
                    "payroll_records": "10 years from end of financial year in which created, per Section 257 HGB and Section 147 AO",
                    "tax_documents": "6 years from end of financial year per Section 147(1) No. 1 AO",
                    "social_security_records": "5 years from end of employment per Section 28f(1) SGB IV",
                },
                "security_measures": "AES-256 encryption at rest in ADP hosted environment (ISO 27001 certified, SOC 2 Type II audited). TLS 1.3 for all data transmission. Role-based access restricted to HR Payroll team (4 named users) with quarterly access reviews. Multi-factor authentication required. Payroll data segregated from general HR systems. Daily encrypted backups with 30-day retention. Annual penetration testing of payroll interface. Staff with access have completed enhanced background checks and signed confidentiality agreements.",
                "dpia_required": False,
                "dpia_reference": None,
                "created_date": "2024-01-15",
                "last_reviewed_date": "2025-11-20",
                "next_review_date": "2026-11-20",
                "processing_owner": "Markus Bauer, Head of Human Resources",
            },
            {
                "record_id": "RPA-002",
                "record_type": "controller",
                "processing_activity": "Clinical trial participant data management",
                "department": "Clinical Operations",
                "controller_identity": {
                    "legal_entity_name": "Helix Biotech Solutions GmbH",
                    "registered_address": "Leopoldstrasse 42, 80802 Munich, Germany",
                    "registration_number": "HRB 267891, Amtsgericht Munich",
                    "contact_email": "privacy@helix-biotech.eu",
                    "dpo_name": "Dr. Elena Voss",
                    "dpo_email": "dpo@helix-biotech.eu",
                    "dpo_phone": "+49 89 7654 3210",
                    "joint_controllers": None,
                    "eu_representative": "Not applicable (established in EEA)",
                },
                "purposes": [
                    "Collection and management of participant clinical data including vital signs, adverse events, laboratory results, and treatment outcomes for Phase III oncology trial HBX-2025-ONC-04 as specified in approved clinical trial protocol",
                    "Monitoring of participant safety and reporting of Suspected Unexpected Serious Adverse Reactions (SUSARs) to the European Medicines Agency and national competent authorities under EU Clinical Trials Regulation 536/2014",
                ],
                "lawful_basis": "Art. 6(1)(a) — explicit consent of clinical trial participant; Art. 9(2)(a) — explicit consent for processing of health data and genetic data",
                "data_subject_categories": [
                    "Clinical trial participants (enrolled patients)",
                    "Screen failures (patients who consented but did not meet eligibility criteria)",
                ],
                "personal_data_categories": [
                    "Participant ID (pseudonymised)",
                    "Date of birth",
                    "Sex",
                    "Ethnicity (for pharmacogenomic analysis)",
                    "Medical history",
                    "Current medications",
                    "Vital signs (blood pressure, heart rate, temperature, weight)",
                    "Laboratory results (haematology, biochemistry, tumour markers)",
                    "Genetic biomarker data (BRCA1/2, HER2 status)",
                    "Treatment allocation and dosing records",
                    "Adverse event reports",
                    "Informed consent documentation",
                    "Contact details (held separately by trial site, not by sponsor)",
                ],
                "special_category_data": "Health data, genetic data (Art. 9(1)). Processed under Art. 9(2)(a) — explicit informed consent obtained per ICH E6(R2) GCP and EU CTR 536/2014.",
                "recipient_categories": [
                    {
                        "recipient": "Veeva Systems Inc. (Veeva Vault CDMS)",
                        "type": "Processor",
                        "purpose": "Clinical data management system hosting and processing",
                        "dpa_reference": "DPA-2024-VEEVA-001, executed 2024-03-10",
                    },
                    {
                        "recipient": "Parexel International GmbH",
                        "type": "Processor",
                        "purpose": "Contract research organisation — trial monitoring and data verification",
                        "dpa_reference": "DPA-2024-PAR-003, executed 2024-04-22",
                    },
                    {
                        "recipient": "European Medicines Agency (EMA)",
                        "type": "Public authority",
                        "purpose": "SUSAR reporting and clinical trial results submission under EU CTR 536/2014",
                        "dpa_reference": "Legal obligation — no DPA required",
                    },
                    {
                        "recipient": "Bundesinstitut fuer Arzneimittel und Medizinprodukte (BfArM)",
                        "type": "Public authority",
                        "purpose": "National competent authority notification and safety reporting",
                        "dpa_reference": "Legal obligation — no DPA required",
                    },
                ],
                "international_transfers": [
                    {
                        "destination_country": "United States",
                        "recipient": "Veeva Systems Inc.",
                        "data_transferred": "Pseudonymised clinical trial data",
                        "safeguard_mechanism": "EU-US Data Privacy Framework adequacy decision (10 July 2023) — Veeva Systems Inc. is listed on the Data Privacy Framework List",
                        "tia_reference": "TIA-2024-VEEVA-001",
                    },
                ],
                "retention_periods": {
                    "clinical_trial_data": "25 years from trial completion per Section 13(10) GCP-Verordnung and ICH E6(R2) Section 4.9.5",
                    "informed_consent_forms": "25 years from trial completion, held at investigator site with sponsor retaining copies",
                    "screen_failure_data": "15 years from screening date per ICH E6(R2)",
                },
                "security_measures": "Pseudonymisation of all participant data at point of collection (participant ID only, no direct identifiers held by sponsor). AES-256 encryption at rest in Veeva Vault. TLS 1.3 for all data transmission. Role-based access with named-user accounts and quarterly access reviews. Audit trail logging of all data access and modifications (21 CFR Part 11 compliant). Physical security: ISO 27001 certified data centres. Network segmentation isolating clinical systems. Annual penetration testing. All staff with clinical data access have completed GCP training and signed enhanced confidentiality agreements.",
                "dpia_required": True,
                "dpia_reference": "DPIA-2024-ONC-04, approved 2024-02-28",
                "created_date": "2024-03-01",
                "last_reviewed_date": "2025-09-15",
                "next_review_date": "2026-03-15",
                "processing_owner": "Dr. Katrin Schreiber, VP Clinical Operations",
            },
            {
                "record_id": "RPA-003",
                "record_type": "controller",
                "processing_activity": "Website analytics and cookie processing",
                "department": "Digital Marketing",
                "controller_identity": {
                    "legal_entity_name": "Helix Biotech Solutions GmbH",
                    "registered_address": "Leopoldstrasse 42, 80802 Munich, Germany",
                    "registration_number": "HRB 267891, Amtsgericht Munich",
                    "contact_email": "privacy@helix-biotech.eu",
                    "dpo_name": "Dr. Elena Voss",
                    "dpo_email": "dpo@helix-biotech.eu",
                    "dpo_phone": "+49 89 7654 3210",
                    "joint_controllers": None,
                    "eu_representative": "Not applicable (established in EEA)",
                },
                "purposes": [
                    "Analysis of aggregate website visitor behaviour on helix-biotech.eu to optimise user experience, measure content engagement, and improve site navigation based on legitimate interest",
                    "Collection of analytics cookies (with prior consent via CMP) to track page views, session duration, referral sources, and conversion events for marketing effectiveness measurement",
                ],
                "lawful_basis": "Art. 6(1)(f) — legitimate interest for anonymised analytics; Art. 6(1)(a) — consent for analytics cookies per Section 25 TDDDG (Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz)",
                "data_subject_categories": [
                    "Website visitors (helix-biotech.eu)",
                    "Registered portal users (customer and partner portals)",
                ],
                "personal_data_categories": [
                    "IP address (truncated to /24 for analytics)",
                    "Cookie identifiers",
                    "Browser type and version",
                    "Operating system",
                    "Screen resolution",
                    "Page views and navigation path",
                    "Session duration",
                    "Referral URL",
                    "Geographic location (city-level, derived from IP)",
                ],
                "special_category_data": "None",
                "recipient_categories": [
                    {
                        "recipient": "Google LLC (Google Analytics 4)",
                        "type": "Processor",
                        "purpose": "Web analytics data processing and reporting",
                        "dpa_reference": "Google Ads Data Processing Terms, accepted 2024-01-20",
                    },
                    {
                        "recipient": "Cookiebot (Cybot A/S)",
                        "type": "Processor",
                        "purpose": "Consent management platform for cookie consent collection and documentation",
                        "dpa_reference": "DPA-2024-CB-001, executed 2024-02-01",
                    },
                ],
                "international_transfers": [
                    {
                        "destination_country": "United States",
                        "recipient": "Google LLC",
                        "data_transferred": "Truncated IP addresses, cookie identifiers, browsing behaviour",
                        "safeguard_mechanism": "EU-US Data Privacy Framework adequacy decision (10 July 2023) — Google LLC listed on DPF List",
                        "tia_reference": "TIA-2024-GOOGLE-002",
                    },
                ],
                "retention_periods": {
                    "analytics_data": "14 months from collection (GA4 data retention setting configured to 14 months)",
                    "consent_records": "3 years from consent action per documentation obligations",
                    "server_logs": "90 days rolling deletion",
                },
                "security_measures": "IP anonymisation enabled in GA4 configuration (last octet truncation). Analytics data accessed via SSO-protected Google Workspace accounts with MFA. Consent management platform hosted in EU (Cybot, Denmark). TLS 1.3 for all website traffic. Content Security Policy (CSP) headers preventing unauthorised script injection. Quarterly review of active cookies against consent categories. Annual cookie audit by DPO office.",
                "dpia_required": False,
                "dpia_reference": None,
                "created_date": "2024-02-01",
                "last_reviewed_date": "2025-10-10",
                "next_review_date": "2026-04-10",
                "processing_owner": "Julia Richter, Head of Digital Marketing",
            },
        ],
    }


def generate_markdown_report(ropa: dict) -> str:
    """Generate a formatted Markdown RoPA report from structured data."""
    lines = []
    org = ropa.get("organisation", "Unknown Organisation")
    lines.append(f"# Record of Processing Activities — {org}")
    lines.append(f"\n**RoPA Version**: {ropa.get('ropa_version', 'N/A')}")
    lines.append(f"**Last Updated**: {ropa.get('last_updated', 'N/A')}")
    lines.append(f"**Prepared By**: {ropa.get('prepared_by', 'N/A')}")
    lines.append(f"**Record Type**: Controller (GDPR Art. 30(1))")
    lines.append(f"\n---\n")

    for record in ropa.get("records", []):
        rid = record.get("record_id", "N/A")
        activity = record.get("processing_activity", "N/A")
        dept = record.get("department", "N/A")

        lines.append(f"## {rid}: {activity}")
        lines.append(f"\n**Department**: {dept}")
        lines.append(f"**Processing Owner**: {record.get('processing_owner', 'N/A')}")
        lines.append(f"**Created**: {record.get('created_date', 'N/A')} | **Last Reviewed**: {record.get('last_reviewed_date', 'N/A')} | **Next Review**: {record.get('next_review_date', 'N/A')}")

        # Controller Identity
        ci = record.get("controller_identity", {})
        lines.append(f"\n### Art. 30(1)(a) — Controller Identity and Contact Details\n")
        lines.append(f"| Field | Value |")
        lines.append(f"|-------|-------|")
        lines.append(f"| Legal entity | {ci.get('legal_entity_name', 'N/A')} |")
        lines.append(f"| Registered address | {ci.get('registered_address', 'N/A')} |")
        lines.append(f"| Registration | {ci.get('registration_number', 'N/A')} |")
        lines.append(f"| Contact email | {ci.get('contact_email', 'N/A')} |")
        lines.append(f"| DPO | {ci.get('dpo_name', 'N/A')}, {ci.get('dpo_email', 'N/A')}, {ci.get('dpo_phone', 'N/A')} |")
        lines.append(f"| Joint controllers | {ci.get('joint_controllers', 'None')} |")
        lines.append(f"| EU representative | {ci.get('eu_representative', 'N/A')} |")

        # Purposes
        lines.append(f"\n### Art. 30(1)(b) — Purposes of Processing\n")
        for purpose in record.get("purposes", []):
            lines.append(f"- {purpose}")
        lines.append(f"\n**Lawful Basis**: {record.get('lawful_basis', 'N/A')}")

        # Data Subject Categories
        lines.append(f"\n### Art. 30(1)(c) — Categories of Data Subjects\n")
        for cat in record.get("data_subject_categories", []):
            lines.append(f"- {cat}")

        # Personal Data Categories
        lines.append(f"\n### Art. 30(1)(c) — Categories of Personal Data\n")
        for cat in record.get("personal_data_categories", []):
            lines.append(f"- {cat}")
        if record.get("special_category_data"):
            lines.append(f"\n**Special Category Data (Art. 9)**: {record['special_category_data']}")

        # Recipients
        lines.append(f"\n### Art. 30(1)(d) — Categories of Recipients\n")
        lines.append(f"| Recipient | Type | Purpose | Agreement |")
        lines.append(f"|-----------|------|---------|-----------|")
        for r in record.get("recipient_categories", []):
            if isinstance(r, dict):
                lines.append(f"| {r.get('recipient', 'N/A')} | {r.get('type', 'N/A')} | {r.get('purpose', 'N/A')} | {r.get('dpa_reference', 'N/A')} |")
            else:
                lines.append(f"| {r} | — | — | — |")

        # International Transfers
        transfers = record.get("international_transfers", [])
        lines.append(f"\n### Art. 30(1)(e) — International Transfers\n")
        if not transfers:
            lines.append("No transfers to third countries or international organisations.")
        else:
            lines.append(f"| Destination | Recipient | Data | Safeguard | TIA Ref |")
            lines.append(f"|-------------|-----------|------|-----------|---------|")
            for t in transfers:
                if isinstance(t, dict):
                    lines.append(f"| {t.get('destination_country', 'N/A')} | {t.get('recipient', 'N/A')} | {t.get('data_transferred', 'N/A')} | {t.get('safeguard_mechanism', 'N/A')} | {t.get('tia_reference', 'N/A')} |")

        # Retention Periods
        lines.append(f"\n### Art. 30(1)(f) — Retention Periods\n")
        retention = record.get("retention_periods", {})
        if isinstance(retention, dict):
            lines.append(f"| Data Category | Retention Period |")
            lines.append(f"|---------------|-----------------|")
            for category, period in retention.items():
                display_cat = category.replace("_", " ").title()
                lines.append(f"| {display_cat} | {period} |")
        elif isinstance(retention, str):
            lines.append(f"**Retention**: {retention}")

        # Security Measures
        lines.append(f"\n### Art. 30(1)(g) — Technical and Organisational Security Measures\n")
        lines.append(record.get("security_measures", "Not specified"))

        # DPIA
        if record.get("dpia_required"):
            lines.append(f"\n### DPIA Reference\n")
            lines.append(f"DPIA required: Yes — {record.get('dpia_reference', 'Reference pending')}")

        lines.append(f"\n---\n")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python process.py generate [--output ropa.json] [--markdown report.md]")
        print("  python process.py validate <ropa_file.json>")
        print("  python process.py report <ropa_file.json> [--output report.md]")
        print()
        print("Commands:")
        print("  generate  — Generate a sample controller RoPA for Helix Biotech Solutions")
        print("  validate  — Validate a RoPA JSON file against Art. 30(1) requirements")
        print("  report    — Generate a formatted Markdown report from RoPA JSON")
        sys.exit(1)

    command = sys.argv[1]

    if command == "generate":
        ropa = create_sample_ropa()

        json_output = None
        md_output = None
        for i, arg in enumerate(sys.argv):
            if arg == "--output" and i + 1 < len(sys.argv):
                json_output = sys.argv[i + 1]
            if arg == "--markdown" and i + 1 < len(sys.argv):
                md_output = sys.argv[i + 1]

        ropa_json = json.dumps(ropa, indent=2, default=str)

        if json_output:
            with open(json_output, "w", encoding="utf-8") as f:
                f.write(ropa_json)
            print(f"RoPA JSON written to {json_output}")
        else:
            print(ropa_json)

        if md_output:
            report = generate_markdown_report(ropa)
            with open(md_output, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"Markdown report written to {md_output}")

    elif command == "validate":
        if len(sys.argv) < 3:
            print("ERROR: Provide the path to the RoPA JSON file.")
            sys.exit(1)

        ropa_path = sys.argv[2]
        with open(ropa_path, "r", encoding="utf-8") as f:
            ropa_data = json.load(f)

        records = ropa_data.get("records", [])
        if not records:
            print("ERROR: No records found in the RoPA file.")
            sys.exit(1)

        all_issues = []
        for record in records:
            issues = validate_entry(record)
            all_issues.extend(issues)

        if not all_issues:
            print("PASS: All records comply with Art. 30(1) mandatory field requirements.")
            sys.exit(0)

        print(f"VALIDATION RESULTS: {len(all_issues)} issue(s) found across {len(records)} record(s)\n")
        for issue in all_issues:
            print(f"[{issue['severity']}] {issue['record_id']} — {issue['field']}")
            print(f"  {issue['article']}: {issue['issue']}")
            print()

        critical_count = sum(1 for i in all_issues if i["severity"] == "Critical")
        major_count = sum(1 for i in all_issues if i["severity"] == "Major")
        print(f"Summary: {critical_count} Critical, {major_count} Major")
        sys.exit(2 if critical_count > 0 else 1)

    elif command == "report":
        if len(sys.argv) < 3:
            print("ERROR: Provide the path to the RoPA JSON file.")
            sys.exit(1)

        ropa_path = sys.argv[2]
        with open(ropa_path, "r", encoding="utf-8") as f:
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
