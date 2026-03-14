#!/usr/bin/env python3
"""
Joint Controller Arrangement Validator

Validates a joint controller arrangement JSON against GDPR Art. 26 requirements,
checking for mandatory elements and producing a compliance assessment.
"""

import json
import sys
from datetime import datetime


REQUIRED_SECTIONS = {
    "parties": {
        "article": "Art. 26(1)",
        "description": "Identity of all joint controllers with legal entity details",
        "required_fields": ["controller_1", "controller_2"],
    },
    "scope": {
        "article": "Art. 26(1)",
        "description": "Scope of joint processing activities covered by the arrangement",
        "required_fields": ["processing_activities", "data_categories", "data_subject_categories"],
    },
    "purpose_determination": {
        "article": "Art. 26(1)",
        "description": "How purposes of processing are jointly determined",
        "required_fields": ["joint_purposes"],
    },
    "means_determination": {
        "article": "Art. 26(1)",
        "description": "How means of processing are jointly determined",
        "required_fields": ["essential_means_allocation"],
    },
    "responsibilities": {
        "article": "Art. 26(1)",
        "description": "Allocation of GDPR compliance responsibilities between controllers",
        "required_fields": [
            "lawful_basis_responsibility",
            "transparency_responsibility",
            "data_subject_rights_responsibility",
            "security_responsibility",
            "breach_notification_responsibility",
            "dpia_responsibility",
            "ropa_responsibility",
        ],
    },
    "contact_point": {
        "article": "Art. 26(1)-(2)",
        "description": "Designated contact point for data subjects",
        "required_fields": ["designated_controller", "contact_details"],
    },
    "transparency": {
        "article": "Art. 26(2)",
        "description": "How the essence of the arrangement is made available to data subjects",
        "required_fields": ["essence_publication_method"],
    },
    "security": {
        "article": "Art. 26(1), Art. 32",
        "description": "Minimum security standards committed by both controllers",
        "required_fields": ["security_standards"],
    },
    "breach_management": {
        "article": "Art. 26(1), Art. 33-34",
        "description": "Breach notification procedures between joint controllers and to authorities",
        "required_fields": ["internal_notification_timeline", "authority_notification_responsibility"],
    },
    "liability": {
        "article": "Art. 82(4)-(5)",
        "description": "Internal liability allocation (noting joint and several liability to data subjects)",
        "required_fields": ["internal_allocation"],
    },
    "term_and_termination": {
        "article": "Art. 26(1)",
        "description": "Duration, exit provisions, and data handling upon termination",
        "required_fields": ["duration", "termination_provisions"],
    },
}


def validate_arrangement(arrangement: dict) -> dict:
    findings = []
    sections_present = 0
    total_sections = len(REQUIRED_SECTIONS)

    for section_key, section_spec in REQUIRED_SECTIONS.items():
        section_data = arrangement.get(section_key)

        if not section_data:
            findings.append({
                "severity": "Critical",
                "section": section_key,
                "article": section_spec["article"],
                "issue": f"Section '{section_key}' is entirely missing from the arrangement",
                "description": section_spec["description"],
            })
            continue

        sections_present += 1

        for field in section_spec["required_fields"]:
            value = section_data.get(field) if isinstance(section_data, dict) else None
            if not value:
                findings.append({
                    "severity": "Major",
                    "section": section_key,
                    "field": field,
                    "article": section_spec["article"],
                    "issue": f"Required field '{field}' is missing in section '{section_key}'",
                    "description": section_spec["description"],
                })

    # Check Art. 26(3) acknowledgment
    art_26_3 = arrangement.get("art_26_3_acknowledgment", False)
    if not art_26_3:
        findings.append({
            "severity": "Major",
            "section": "art_26_3_acknowledgment",
            "article": "Art. 26(3)",
            "issue": "Arrangement does not acknowledge that data subjects may exercise rights against any controller",
            "description": "Art. 26(3) requires that data subjects can exercise rights against each joint controller regardless of the arrangement",
        })

    completeness = (sections_present / total_sections * 100) if total_sections > 0 else 0

    severity_counts = {"Critical": 0, "Major": 0, "Minor": 0}
    for f in findings:
        severity_counts[f["severity"]] = severity_counts.get(f["severity"], 0) + 1

    return {
        "validation_date": datetime.now().strftime("%Y-%m-%d"),
        "arrangement_completeness": round(completeness, 1),
        "sections_present": sections_present,
        "total_sections": total_sections,
        "total_findings": len(findings),
        "severity_summary": severity_counts,
        "compliant": len(findings) == 0,
        "findings": findings,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <arrangement.json>")
        print("\nExpected JSON structure with these top-level sections:")
        for key, spec in REQUIRED_SECTIONS.items():
            fields = ", ".join(spec["required_fields"])
            print(f"  {key}: {{ {fields} }}  ({spec['article']})")
        print(f"  art_26_3_acknowledgment: true/false  (Art. 26(3))")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        arrangement = json.load(f)

    result = validate_arrangement(arrangement)
    print(json.dumps(result, indent=2))

    if result["severity_summary"]["Critical"] > 0:
        sys.exit(2)
    sys.exit(0 if result["compliant"] else 1)


if __name__ == "__main__":
    main()
