#!/usr/bin/env python3
"""
GDPR Article 30 RoPA Validator

Validates Records of Processing Activities JSON against mandatory fields
required by GDPR Art. 30(1) for controllers and Art. 30(2) for processors.
Produces an audit findings report with severity classifications.
"""

import json
import sys
from datetime import datetime, timedelta
from typing import Any


CONTROLLER_REQUIRED_FIELDS = {
    "controller_identity": {
        "article": "Art. 30(1)(a)",
        "description": "Name and contact details of the controller and DPO",
        "sub_fields": ["legal_entity_name", "contact_email", "dpo_name", "dpo_email"],
    },
    "purposes": {
        "article": "Art. 30(1)(b)",
        "description": "Purposes of the processing",
        "sub_fields": [],
    },
    "data_subject_categories": {
        "article": "Art. 30(1)(c)",
        "description": "Categories of data subjects",
        "sub_fields": [],
    },
    "personal_data_categories": {
        "article": "Art. 30(1)(c)",
        "description": "Categories of personal data",
        "sub_fields": [],
    },
    "recipient_categories": {
        "article": "Art. 30(1)(d)",
        "description": "Categories of recipients",
        "sub_fields": [],
    },
    "international_transfers": {
        "article": "Art. 30(1)(e)",
        "description": "Transfers to third countries or international organisations",
        "sub_fields": [],
    },
    "retention_periods": {
        "article": "Art. 30(1)(f)",
        "description": "Envisaged time limits for erasure",
        "sub_fields": [],
    },
    "security_measures": {
        "article": "Art. 30(1)(g)",
        "description": "General description of technical and organisational security measures",
        "sub_fields": [],
    },
}

PROCESSOR_REQUIRED_FIELDS = {
    "processor_identity": {
        "article": "Art. 30(2)(a)",
        "description": "Name and contact details of the processor and each controller",
        "sub_fields": ["legal_entity_name", "contact_email", "controller_names"],
    },
    "processing_categories": {
        "article": "Art. 30(2)(b)",
        "description": "Categories of processing carried out on behalf of each controller",
        "sub_fields": [],
    },
    "international_transfers": {
        "article": "Art. 30(2)(c)",
        "description": "Transfers to third countries or international organisations",
        "sub_fields": [],
    },
    "security_measures": {
        "article": "Art. 30(2)(d)",
        "description": "General description of technical and organisational security measures",
        "sub_fields": [],
    },
}

VAGUE_PURPOSE_TERMS = [
    "business purposes",
    "business operations",
    "general purposes",
    "various purposes",
    "as needed",
    "other purposes",
    "internal use",
    "operational purposes",
]

VAGUE_RETENTION_TERMS = [
    "as long as necessary",
    "indefinitely",
    "until no longer needed",
    "as required",
    "in accordance with policy",
    "per policy",
    "not determined",
    "tbd",
    "n/a",
]


def validate_non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str) and value.strip() == "":
        return False
    if isinstance(value, list) and len(value) == 0:
        return False
    if isinstance(value, dict) and len(value) == 0:
        return False
    return True


def check_vague_terms(value: Any, vague_list: list[str]) -> list[str]:
    issues = []
    text = ""
    if isinstance(value, str):
        text = value.lower()
    elif isinstance(value, list):
        text = " ".join(str(v).lower() for v in value)
    elif isinstance(value, dict):
        text = " ".join(str(v).lower() for v in value.values())

    for term in vague_list:
        if term in text:
            issues.append(f"Vague term detected: '{term}'")
    return issues


def check_staleness(record: dict, max_age_days: int = 365) -> list[str]:
    issues = []
    last_reviewed = record.get("last_reviewed_date")
    if not last_reviewed:
        issues.append("No last_reviewed_date field — cannot verify currency")
        return issues

    try:
        review_date = datetime.strptime(last_reviewed, "%Y-%m-%d")
        age = (datetime.now() - review_date).days
        if age > max_age_days:
            issues.append(
                f"Record last reviewed {age} days ago (threshold: {max_age_days} days)"
            )
    except ValueError:
        issues.append(f"Invalid date format for last_reviewed_date: '{last_reviewed}'")
    return issues


def validate_controller_record(record: dict, record_id: str) -> list[dict]:
    findings = []

    for field_name, field_spec in CONTROLLER_REQUIRED_FIELDS.items():
        value = record.get(field_name)

        if not validate_non_empty(value):
            findings.append(
                {
                    "record_id": record_id,
                    "severity": "Critical",
                    "field": field_name,
                    "article": field_spec["article"],
                    "issue": f"Mandatory field '{field_name}' is missing or empty",
                    "description": field_spec["description"],
                }
            )
            continue

        for sub_field in field_spec.get("sub_fields", []):
            if isinstance(value, dict) and not validate_non_empty(value.get(sub_field)):
                findings.append(
                    {
                        "record_id": record_id,
                        "severity": "Major",
                        "field": f"{field_name}.{sub_field}",
                        "article": field_spec["article"],
                        "issue": f"Sub-field '{sub_field}' is missing within '{field_name}'",
                        "description": field_spec["description"],
                    }
                )

        if field_name == "purposes":
            vague_issues = check_vague_terms(value, VAGUE_PURPOSE_TERMS)
            for issue in vague_issues:
                findings.append(
                    {
                        "record_id": record_id,
                        "severity": "Major",
                        "field": field_name,
                        "article": "Art. 30(1)(b)",
                        "issue": issue,
                        "description": "Purpose description must be specific and granular per Art. 5(1)(b)",
                    }
                )

        if field_name == "retention_periods":
            vague_issues = check_vague_terms(value, VAGUE_RETENTION_TERMS)
            for issue in vague_issues:
                findings.append(
                    {
                        "record_id": record_id,
                        "severity": "Major",
                        "field": field_name,
                        "article": "Art. 30(1)(f)",
                        "issue": issue,
                        "description": "Retention periods must specify concrete durations or criteria",
                    }
                )

        if field_name == "international_transfers":
            if isinstance(value, list):
                for idx, transfer in enumerate(value):
                    if isinstance(transfer, dict):
                        if not transfer.get("safeguard_mechanism"):
                            findings.append(
                                {
                                    "record_id": record_id,
                                    "severity": "Major",
                                    "field": f"international_transfers[{idx}]",
                                    "article": "Art. 30(1)(e)",
                                    "issue": "Transfer missing safeguard mechanism (SCCs/BCRs/adequacy decision)",
                                    "description": "Each international transfer must specify the Art. 46 safeguard relied upon",
                                }
                            )

    staleness_issues = check_staleness(record)
    for issue in staleness_issues:
        findings.append(
            {
                "record_id": record_id,
                "severity": "Major" if "last reviewed" in issue else "Minor",
                "field": "last_reviewed_date",
                "article": "Art. 5(2) / Art. 24",
                "issue": issue,
                "description": "Accountability requires records to be kept current",
            }
        )

    return findings


def validate_processor_record(record: dict, record_id: str) -> list[dict]:
    findings = []

    for field_name, field_spec in PROCESSOR_REQUIRED_FIELDS.items():
        value = record.get(field_name)

        if not validate_non_empty(value):
            findings.append(
                {
                    "record_id": record_id,
                    "severity": "Critical",
                    "field": field_name,
                    "article": field_spec["article"],
                    "issue": f"Mandatory field '{field_name}' is missing or empty",
                    "description": field_spec["description"],
                }
            )
            continue

        for sub_field in field_spec.get("sub_fields", []):
            if isinstance(value, dict) and not validate_non_empty(value.get(sub_field)):
                findings.append(
                    {
                        "record_id": record_id,
                        "severity": "Major",
                        "field": f"{field_name}.{sub_field}",
                        "article": field_spec["article"],
                        "issue": f"Sub-field '{sub_field}' is missing within '{field_name}'",
                        "description": field_spec["description"],
                    }
                )

    staleness_issues = check_staleness(record)
    for issue in staleness_issues:
        findings.append(
            {
                "record_id": record_id,
                "severity": "Major" if "last reviewed" in issue else "Minor",
                "field": "last_reviewed_date",
                "article": "Art. 5(2) / Art. 24",
                "issue": issue,
                "description": "Accountability requires records to be kept current",
            }
        )

    return findings


def generate_report(findings: list[dict], output_path: str | None = None) -> str:
    report_lines = []
    report_lines.append("=" * 80)
    report_lines.append("GDPR ARTICLE 30 RoPA AUDIT REPORT")
    report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("=" * 80)

    severity_counts = {"Critical": 0, "Major": 0, "Minor": 0}
    for f in findings:
        severity_counts[f["severity"]] = severity_counts.get(f["severity"], 0) + 1

    report_lines.append(f"\nTotal findings: {len(findings)}")
    for severity, count in severity_counts.items():
        report_lines.append(f"  {severity}: {count}")

    report_lines.append(f"\n{'─' * 80}")
    report_lines.append("DETAILED FINDINGS")
    report_lines.append(f"{'─' * 80}")

    for i, f in enumerate(findings, 1):
        report_lines.append(f"\n[{f['severity'].upper()}] Finding #{i}")
        report_lines.append(f"  Record:      {f['record_id']}")
        report_lines.append(f"  Field:       {f['field']}")
        report_lines.append(f"  Article:     {f['article']}")
        report_lines.append(f"  Issue:       {f['issue']}")
        report_lines.append(f"  Description: {f['description']}")

        if f["severity"] == "Critical":
            deadline = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        elif f["severity"] == "Major":
            deadline = (datetime.now() + timedelta(days=60)).strftime("%Y-%m-%d")
        else:
            deadline = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
        report_lines.append(f"  Remediation Deadline: {deadline}")

    report = "\n".join(report_lines)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)

    return report


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <ropa_file.json> [--output report.txt]")
        print("\nExpected JSON structure:")
        print(json.dumps(
            {
                "organisation": "Nexus Technologies GmbH",
                "records": [
                    {
                        "record_id": "RPA-001",
                        "record_type": "controller",
                        "controller_identity": {
                            "legal_entity_name": "Nexus Technologies GmbH",
                            "contact_email": "privacy@nexus-tech.eu",
                            "dpo_name": "Dr. Katharina Weiss",
                            "dpo_email": "dpo@nexus-tech.eu",
                        },
                        "purposes": ["Payroll processing for employment contract performance"],
                        "data_subject_categories": ["Employees", "Contractors"],
                        "personal_data_categories": ["Name", "Bank account", "Tax ID", "Salary"],
                        "recipient_categories": ["Payroll processor", "Tax authority"],
                        "international_transfers": [],
                        "retention_periods": "7 years from end of employment per Section 257 HGB",
                        "security_measures": "AES-256 encryption at rest, TLS 1.3 in transit, RBAC, annual penetration testing",
                        "last_reviewed_date": "2025-11-15",
                    }
                ],
            },
            indent=2,
        ))
        sys.exit(1)

    ropa_path = sys.argv[1]
    output_path = None
    if "--output" in sys.argv:
        output_idx = sys.argv.index("--output")
        if output_idx + 1 < len(sys.argv):
            output_path = sys.argv[output_idx + 1]

    with open(ropa_path, "r", encoding="utf-8") as f:
        ropa_data = json.load(f)

    records = ropa_data.get("records", [])
    if not records:
        print("ERROR: No records found in the RoPA file.")
        sys.exit(1)

    all_findings = []
    for record in records:
        record_id = record.get("record_id", "UNKNOWN")
        record_type = record.get("record_type", "controller")

        if record_type == "processor":
            findings = validate_processor_record(record, record_id)
        else:
            findings = validate_controller_record(record, record_id)

        all_findings.extend(findings)

    report = generate_report(all_findings, output_path)
    print(report)

    critical_count = sum(1 for f in all_findings if f["severity"] == "Critical")
    if critical_count > 0:
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
