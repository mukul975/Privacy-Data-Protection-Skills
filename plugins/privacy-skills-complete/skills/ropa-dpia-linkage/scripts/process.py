#!/usr/bin/env python3
"""
RoPA-DPIA Linkage Checker

Validates cross-references between RoPA entries and DPIA register.
Identifies orphaned DPIAs, missing DPIA references, and cascade
triggers from recent RoPA changes.
"""

import json
import sys
from datetime import datetime
from typing import Any


DPIA_CRITERIA = [
    {"id": "C1", "name": "Evaluation or scoring (including profiling)", "article": "Art. 35(3)(a) / WP29"},
    {"id": "C2", "name": "Automated decision-making with legal/significant effects", "article": "Art. 22 / WP29"},
    {"id": "C3", "name": "Systematic monitoring", "article": "Art. 35(3)(c) / WP29"},
    {"id": "C4", "name": "Sensitive data or highly personal data", "article": "Art. 35(3)(b) / WP29"},
    {"id": "C5", "name": "Large-scale processing", "article": "Art. 35(3)(b) / WP29"},
    {"id": "C6", "name": "Matching or combining datasets", "article": "WP29"},
    {"id": "C7", "name": "Vulnerable data subjects", "article": "WP29"},
    {"id": "C8", "name": "Innovative use or new technology", "article": "WP29"},
    {"id": "C9", "name": "Processing preventing exercise of a right", "article": "WP29"},
]


def check_linkage_integrity(ropa: dict, dpia_register: dict) -> dict:
    """Check cross-reference integrity between RoPA and DPIA registers."""
    ropa_records = ropa.get("records", [])
    dpias = dpia_register.get("dpias", [])

    dpia_by_ref = {d["reference"]: d for d in dpias}
    ropa_by_id = {r["record_id"]: r for r in ropa_records}

    issues = []

    # Check RoPA entries that require DPIA
    for record in ropa_records:
        record_id = record.get("record_id", "UNKNOWN")
        dpia_required = record.get("dpia_required", False)
        dpia_ref = record.get("dpia_reference")

        if dpia_required and not dpia_ref:
            issues.append({
                "type": "missing_dpia_reference",
                "severity": "Critical",
                "record_id": record_id,
                "description": f"RoPA entry {record_id} requires DPIA but no DPIA reference is recorded",
            })

        if dpia_ref and dpia_ref not in dpia_by_ref:
            issues.append({
                "type": "invalid_dpia_reference",
                "severity": "Critical",
                "record_id": record_id,
                "dpia_reference": dpia_ref,
                "description": f"RoPA entry {record_id} references DPIA {dpia_ref} which does not exist in the DPIA register",
            })

        if dpia_ref and dpia_ref in dpia_by_ref:
            dpia = dpia_by_ref[dpia_ref]
            dpia_status = dpia.get("status", "")
            if dpia_status in ("Expired", "Rejected"):
                issues.append({
                    "type": "invalid_dpia_status",
                    "severity": "Critical",
                    "record_id": record_id,
                    "dpia_reference": dpia_ref,
                    "dpia_status": dpia_status,
                    "description": f"DPIA {dpia_ref} linked to {record_id} has status '{dpia_status}'",
                })

            review_date = dpia.get("next_review_date")
            if review_date:
                try:
                    rd = datetime.strptime(review_date, "%Y-%m-%d")
                    if rd < datetime.now():
                        days_overdue = (datetime.now() - rd).days
                        issues.append({
                            "type": "dpia_review_overdue",
                            "severity": "Major",
                            "record_id": record_id,
                            "dpia_reference": dpia_ref,
                            "description": f"DPIA {dpia_ref} review is {days_overdue} days overdue (due: {review_date})",
                        })
                except ValueError:
                    pass

    # Check for orphaned DPIAs (no linked RoPA entry)
    ropa_dpia_refs = {r.get("dpia_reference") for r in ropa_records if r.get("dpia_reference")}
    for dpia in dpias:
        dpia_ref = dpia.get("reference")
        linked_ropa = dpia.get("linked_ropa_entries", [])
        if not linked_ropa and dpia_ref not in ropa_dpia_refs:
            issues.append({
                "type": "orphaned_dpia",
                "severity": "Major",
                "dpia_reference": dpia_ref,
                "description": f"DPIA {dpia_ref} has no linked RoPA entry — may indicate unrecorded processing or stale DPIA",
            })

    # Check for high-risk indicators in RoPA entries without DPIA
    for record in ropa_records:
        record_id = record.get("record_id", "UNKNOWN")
        if record.get("dpia_required"):
            continue

        special = record.get("special_category_data", "")
        if isinstance(special, str) and special.lower() not in ("none", "none detected", "no", ""):
            issues.append({
                "type": "potential_dpia_needed",
                "severity": "Major",
                "record_id": record_id,
                "description": f"RoPA entry {record_id} processes special category data but DPIA not required is set. Verify DPIA necessity assessment.",
            })

    return {
        "audit_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ropa_entries_checked": len(ropa_records),
        "dpias_checked": len(dpias),
        "issues_found": len(issues),
        "critical_issues": sum(1 for i in issues if i["severity"] == "Critical"),
        "major_issues": sum(1 for i in issues if i["severity"] == "Major"),
        "issues": issues,
    }


def assess_dpia_necessity(record: dict) -> dict:
    """Assess whether a RoPA entry requires a DPIA based on WP29 criteria."""
    record_id = record.get("record_id", "UNKNOWN")
    criteria_met = []

    purposes = " ".join(record.get("purposes", [])).lower() if isinstance(record.get("purposes"), list) else str(record.get("purposes", "")).lower()
    special = str(record.get("special_category_data", "")).lower()
    data_subjects = " ".join(record.get("data_subject_categories", [])).lower() if isinstance(record.get("data_subject_categories"), list) else ""

    # C1: Evaluation or scoring
    if any(term in purposes for term in ["profiling", "scoring", "evaluation", "assessment", "rating", "ranking"]):
        criteria_met.append("C1")

    # C2: Automated decision-making
    if any(term in purposes for term in ["automated decision", "automated processing", "algorithmic"]):
        criteria_met.append("C2")

    # C3: Systematic monitoring
    if any(term in purposes for term in ["monitoring", "surveillance", "cctv", "tracking", "observation"]):
        criteria_met.append("C3")

    # C4: Sensitive data
    if special not in ("none", "none detected", "no", ""):
        criteria_met.append("C4")

    # C5: Large scale
    if any(term in purposes for term in ["large-scale", "large scale", "organisation-wide", "all employees", "all customers"]):
        criteria_met.append("C5")

    # C6: Matching/combining datasets
    if any(term in purposes for term in ["matching", "combining", "cross-referenc", "merging", "linking"]):
        criteria_met.append("C6")

    # C7: Vulnerable data subjects
    if any(term in data_subjects for term in ["children", "patient", "employee", "elderly", "minor", "student"]):
        criteria_met.append("C7")

    # C8: Innovative use / new technology
    if any(term in purposes for term in ["ai", "machine learning", "biometric", "iot", "blockchain", "novel", "innovative"]):
        criteria_met.append("C8")

    dpia_required = len(criteria_met) >= 2

    return {
        "record_id": record_id,
        "processing_activity": record.get("processing_activity", "N/A"),
        "criteria_assessed": len(DPIA_CRITERIA),
        "criteria_met": criteria_met,
        "criteria_met_count": len(criteria_met),
        "dpia_required": dpia_required,
        "recommendation": "DPIA REQUIRED — two or more criteria met" if dpia_required else "DPIA not required based on automated assessment. DPO should verify.",
        "criteria_details": [c for c in DPIA_CRITERIA if c["id"] in criteria_met],
    }


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python process.py check <ropa.json> <dpia_register.json> [--output report.json]")
        print("  python process.py assess <ropa.json> [--record RPA-002]")
        print("  python process.py demo")
        sys.exit(1)

    command = sys.argv[1]

    if command == "demo":
        sample_ropa = {
            "records": [
                {"record_id": "RPA-001", "processing_activity": "Payroll", "dpia_required": False, "dpia_reference": None, "special_category_data": "Church tax (religion)", "purposes": ["Payroll calculation"], "data_subject_categories": ["Employees"]},
                {"record_id": "RPA-002", "processing_activity": "Clinical trial", "dpia_required": True, "dpia_reference": "DPIA-2024-ONC-04", "special_category_data": "Health data, genetic data", "purposes": ["Clinical data management for Phase III oncology trial"], "data_subject_categories": ["Patients"]},
                {"record_id": "RPA-003", "processing_activity": "Analytics", "dpia_required": False, "dpia_reference": None, "special_category_data": "None", "purposes": ["Website analytics"], "data_subject_categories": ["Website visitors"]},
                {"record_id": "RPA-004", "processing_activity": "Performance profiling", "dpia_required": True, "dpia_reference": None, "special_category_data": "None", "purposes": ["Employee performance scoring and profiling"], "data_subject_categories": ["Employees"]},
            ],
        }
        sample_dpia = {
            "dpias": [
                {"reference": "DPIA-2024-ONC-04", "title": "Oncology Trial", "status": "Approved", "linked_ropa_entries": ["RPA-002"], "next_review_date": "2025-02-28"},
                {"reference": "DPIA-2024-OLD-001", "title": "Legacy System", "status": "Approved", "linked_ropa_entries": [], "next_review_date": "2024-06-01"},
            ],
        }

        print("LINKAGE INTEGRITY CHECK:")
        result = check_linkage_integrity(sample_ropa, sample_dpia)
        print(json.dumps(result, indent=2))

        print("\nDPIA NECESSITY ASSESSMENT:")
        for record in sample_ropa["records"]:
            assessment = assess_dpia_necessity(record)
            print(f"\n  {assessment['record_id']}: {assessment['processing_activity']}")
            print(f"    Criteria met: {assessment['criteria_met_count']} — {assessment['criteria_met']}")
            print(f"    {assessment['recommendation']}")

    elif command == "check":
        if len(sys.argv) < 4:
            print("ERROR: Provide both RoPA and DPIA register JSON files.")
            sys.exit(1)
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            ropa = json.load(f)
        with open(sys.argv[3], "r", encoding="utf-8") as f:
            dpia_register = json.load(f)

        result = check_linkage_integrity(ropa, dpia_register)
        output = json.dumps(result, indent=2)

        if "--output" in sys.argv:
            idx = sys.argv.index("--output")
            if idx + 1 < len(sys.argv):
                with open(sys.argv[idx + 1], "w", encoding="utf-8") as f:
                    f.write(output)
                print(f"Report written to {sys.argv[idx + 1]}")
                sys.exit(0)
        print(output)

    elif command == "assess":
        if len(sys.argv) < 3:
            print("ERROR: Provide the RoPA JSON file.")
            sys.exit(1)
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            ropa = json.load(f)

        target_record = None
        if "--record" in sys.argv:
            idx = sys.argv.index("--record")
            if idx + 1 < len(sys.argv):
                target_record = sys.argv[idx + 1]

        for record in ropa.get("records", []):
            if target_record and record.get("record_id") != target_record:
                continue
            assessment = assess_dpia_necessity(record)
            print(json.dumps(assessment, indent=2))
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
