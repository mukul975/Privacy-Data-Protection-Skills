#!/usr/bin/env python3
"""
DPA Compliance Checker

Validates a data processing agreement JSON structure against all
GDPR Art. 28(3) mandatory elements and produces a compliance report.
"""

import json
import sys
from datetime import datetime


DPA_REQUIREMENTS = [
    {"id": "R01", "article": "Art. 28(3)", "requirement": "Subject-matter and duration specified", "field": "subject_matter"},
    {"id": "R02", "article": "Art. 28(3)", "requirement": "Nature and purpose of processing defined", "field": "nature_and_purpose"},
    {"id": "R03", "article": "Art. 28(3)", "requirement": "Types of personal data listed", "field": "data_types"},
    {"id": "R04", "article": "Art. 28(3)", "requirement": "Categories of data subjects identified", "field": "data_subject_categories"},
    {"id": "R05", "article": "Art. 28(3)(a)", "requirement": "Processor acts only on documented instructions", "field": "documented_instructions"},
    {"id": "R06", "article": "Art. 28(3)(a)", "requirement": "Law-required processing notification obligation", "field": "law_notification"},
    {"id": "R07", "article": "Art. 28(3)(b)", "requirement": "Confidentiality commitment for personnel", "field": "confidentiality"},
    {"id": "R08", "article": "Art. 28(3)(c)", "requirement": "Art. 32 security measures implemented", "field": "security_measures"},
    {"id": "R09", "article": "Art. 28(2)-(3)(d)", "requirement": "Sub-processor authorisation mechanism", "field": "subprocessor_authorisation"},
    {"id": "R10", "article": "Art. 28(4)", "requirement": "Sub-processor change notification", "field": "subprocessor_notification"},
    {"id": "R11", "article": "Art. 28(2)", "requirement": "Controller objection right to sub-processors", "field": "subprocessor_objection_right"},
    {"id": "R12", "article": "Art. 28(4)", "requirement": "Same obligations imposed on sub-processors", "field": "subprocessor_obligations"},
    {"id": "R13", "article": "Art. 28(3)(e)", "requirement": "Assistance with data subject rights", "field": "dsr_assistance"},
    {"id": "R14", "article": "Art. 28(3)(f)", "requirement": "Assistance with Art. 32-36 obligations", "field": "compliance_assistance"},
    {"id": "R15", "article": "Art. 28(3)(g)", "requirement": "Data return or deletion upon termination", "field": "data_return_deletion"},
    {"id": "R16", "article": "Art. 28(3)(h)", "requirement": "Audit and inspection rights", "field": "audit_rights"},
    {"id": "R17", "article": "Art. 28(3)(h)", "requirement": "Information to demonstrate compliance", "field": "compliance_information"},
    {"id": "R18", "article": "Ch. V", "requirement": "International transfer safeguards", "field": "transfer_safeguards"},
    {"id": "R19", "article": "Art. 28(9)", "requirement": "Written form (including electronic)", "field": "written_form"},
    {"id": "R20", "article": "Art. 33(2)", "requirement": "Breach notification to controller", "field": "breach_notification"},
]


def check_requirement(dpa: dict, req: dict) -> dict:
    field = req["field"]
    value = dpa.get(field)

    status = "missing"
    detail = ""

    if value is None or value == "" or value == [] or value == {}:
        status = "missing"
        detail = f"Field '{field}' is not present in the DPA"
    elif isinstance(value, bool):
        status = "present" if value else "missing"
        detail = f"Field '{field}' is {'confirmed' if value else 'set to false'}"
    elif isinstance(value, str) and len(value.strip()) < 10:
        status = "insufficient"
        detail = f"Field '{field}' contains insufficient detail: '{value}'"
    elif isinstance(value, list) and len(value) == 0:
        status = "missing"
        detail = f"Field '{field}' is an empty list"
    else:
        status = "present"
        detail = f"Field '{field}' is populated"

    severity = "Critical" if status == "missing" else ("Major" if status == "insufficient" else "Compliant")

    return {
        "requirement_id": req["id"],
        "article": req["article"],
        "requirement": req["requirement"],
        "status": status,
        "severity": severity,
        "detail": detail,
    }


def validate_dpa(dpa: dict) -> dict:
    results = []
    for req in DPA_REQUIREMENTS:
        results.append(check_requirement(dpa, req))

    compliant_count = sum(1 for r in results if r["status"] == "present")
    total = len(results)
    compliance_pct = (compliant_count / total * 100) if total > 0 else 0

    severity_counts = {"Critical": 0, "Major": 0, "Compliant": 0}
    for r in results:
        severity_counts[r["severity"]] = severity_counts.get(r["severity"], 0) + 1

    findings = [r for r in results if r["status"] != "present"]

    return {
        "validation_date": datetime.now().strftime("%Y-%m-%d"),
        "processor_name": dpa.get("processor_name", "Unknown"),
        "controller_name": dpa.get("controller_name", "Unknown"),
        "compliance_percentage": round(compliance_pct, 1),
        "total_requirements": total,
        "compliant_requirements": compliant_count,
        "severity_summary": severity_counts,
        "is_compliant": len(findings) == 0,
        "findings": findings,
        "all_results": results,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <dpa.json>")
        print("\nExpected JSON with fields for each Art. 28(3) requirement.")
        print("Fields: subject_matter, nature_and_purpose, data_types, data_subject_categories,")
        print("  documented_instructions, law_notification, confidentiality, security_measures,")
        print("  subprocessor_authorisation, subprocessor_notification, subprocessor_objection_right,")
        print("  subprocessor_obligations, dsr_assistance, compliance_assistance,")
        print("  data_return_deletion, audit_rights, compliance_information,")
        print("  transfer_safeguards, written_form, breach_notification")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        dpa = json.load(f)

    result = validate_dpa(dpa)
    print(json.dumps(result, indent=2))

    if result["severity_summary"]["Critical"] > 0:
        sys.exit(2)
    sys.exit(0 if result["is_compliant"] else 1)


if __name__ == "__main__":
    main()
