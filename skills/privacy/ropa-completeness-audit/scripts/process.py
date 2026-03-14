#!/usr/bin/env python3
"""
RoPA Completeness Auditor

Audits RoPA entries against supervisory authority templates (CNIL, ICO, BfDI).
Calculates multi-tier completeness scores, identifies gaps, and generates
audit reports with remediation tracking.
"""

import json
import sys
from datetime import datetime
from typing import Any


SA_TEMPLATES = {
    "cnil": {
        "name": "CNIL (France)",
        "mandatory_fields": [
            "controller_identity", "purposes", "data_subject_categories",
            "personal_data_categories", "recipient_categories",
            "international_transfers", "retention_periods", "security_measures",
        ],
        "sa_required_fields": [
            "controller_identity", "purposes", "data_subject_categories",
            "personal_data_categories", "recipient_categories",
            "international_transfers", "retention_periods", "security_measures",
        ],
        "sa_recommended_fields": [
            "lawful_basis", "special_category_data", "dpia_required",
            "dpia_reference", "last_reviewed_date",
        ],
    },
    "ico": {
        "name": "ICO (United Kingdom)",
        "mandatory_fields": [
            "controller_identity", "purposes", "data_subject_categories",
            "personal_data_categories", "recipient_categories",
            "international_transfers", "retention_periods", "security_measures",
        ],
        "sa_required_fields": [
            "controller_identity", "purposes", "lawful_basis",
            "data_subject_categories", "personal_data_categories",
            "special_category_data", "recipient_categories",
            "international_transfers", "retention_periods", "security_measures",
        ],
        "sa_recommended_fields": [
            "dpia_reference", "last_reviewed_date", "processing_owner",
        ],
    },
    "bfdi": {
        "name": "BfDI (Germany)",
        "mandatory_fields": [
            "controller_identity", "purposes", "data_subject_categories",
            "personal_data_categories", "recipient_categories",
            "international_transfers", "retention_periods", "security_measures",
        ],
        "sa_required_fields": [
            "controller_identity", "purposes", "lawful_basis",
            "data_subject_categories", "personal_data_categories",
            "recipient_categories", "international_transfers",
            "retention_periods", "security_measures",
        ],
        "sa_recommended_fields": [
            "department", "dpia_reference", "last_reviewed_date",
            "processing_owner",
        ],
    },
}

VAGUE_PURPOSE_TERMS = [
    "business purposes", "business operations", "general purposes",
    "various purposes", "as needed", "other purposes", "internal use",
    "operational purposes",
]

VAGUE_RETENTION_TERMS = [
    "as long as necessary", "indefinitely", "until no longer needed",
    "as required", "in accordance with policy", "per policy",
    "not determined", "tbd", "n/a",
]


def is_populated(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str) and value.strip() in ("", "N/A", "n/a", "None", "TBD"):
        return False
    if isinstance(value, (list, dict)) and len(value) == 0:
        return False
    return True


def quality_score(field_name: str, value: Any) -> int:
    """Score field quality on 0-3 scale."""
    if not is_populated(value):
        return 0

    text = ""
    if isinstance(value, str):
        text = value.lower()
    elif isinstance(value, list):
        text = " ".join(str(v).lower() for v in value)
    elif isinstance(value, dict):
        text = " ".join(str(v).lower() for v in value.values())

    if field_name == "purposes":
        for term in VAGUE_PURPOSE_TERMS:
            if term in text:
                return 1
        if len(text) < 20:
            return 1
        return 3 if len(text) > 50 else 2

    if field_name == "retention_periods":
        for term in VAGUE_RETENTION_TERMS:
            if term in text:
                return 1
        if any(c.isdigit() for c in text):
            return 3
        return 2

    if field_name == "security_measures":
        if len(text) < 30:
            return 1
        keywords = ["encryption", "access control", "mfa", "backup", "audit", "training", "iso"]
        found = sum(1 for kw in keywords if kw in text)
        if found >= 4:
            return 3
        elif found >= 2:
            return 2
        return 1

    if field_name == "international_transfers":
        if isinstance(value, list):
            for t in value:
                if isinstance(t, dict) and not t.get("safeguard_mechanism"):
                    return 1
            return 3
        return 2

    if field_name in ("controller_identity", "processor_identity"):
        if isinstance(value, dict):
            sub_fields = ["legal_entity_name", "contact_email", "dpo_name", "dpo_email"]
            populated = sum(1 for sf in sub_fields if is_populated(value.get(sf)))
            if populated >= 4:
                return 3
            elif populated >= 2:
                return 2
            return 1
        return 2

    # Default scoring for other fields
    if isinstance(value, list):
        return 3 if len(value) >= 2 else 2
    if isinstance(value, str) and len(value) > 10:
        return 3 if len(value) > 30 else 2
    return 2


def check_review_currency(record: dict) -> int:
    """Score review currency: 3=<12m, 2=12-18m, 1=18-24m, 0=>24m."""
    last_reviewed = record.get("last_reviewed_date")
    if not last_reviewed:
        return 0
    try:
        review_date = datetime.strptime(last_reviewed, "%Y-%m-%d")
        days = (datetime.now() - review_date).days
        if days <= 365:
            return 3
        elif days <= 548:
            return 2
        elif days <= 730:
            return 1
        return 0
    except ValueError:
        return 0


def audit_entry(record: dict, sa_template: str = "cnil") -> dict:
    """Audit a single RoPA entry against a supervisory authority template."""
    template = SA_TEMPLATES.get(sa_template, SA_TEMPLATES["cnil"])
    record_id = record.get("record_id", "UNKNOWN")

    # Tier 1: Art. 30 mandatory fields
    tier1_results = {}
    for field in template["mandatory_fields"]:
        value = record.get(field)
        present = is_populated(value)
        qual = quality_score(field, value) if present else 0
        tier1_results[field] = {"present": present, "quality": qual}

    tier1_present = sum(1 for r in tier1_results.values() if r["present"])
    tier1_total = len(template["mandatory_fields"])
    tier1_avg_quality = (
        sum(r["quality"] for r in tier1_results.values()) / tier1_total
        if tier1_total > 0 else 0
    )
    tier1_score = (tier1_present / tier1_total) * (tier1_avg_quality / 3) * 100

    # Tier 2: SA-specific fields
    all_sa_fields = template["sa_required_fields"] + template["sa_recommended_fields"]
    tier2_results = {}
    for field in all_sa_fields:
        value = record.get(field)
        present = is_populated(value)
        qual = quality_score(field, value) if present else 0
        tier2_results[field] = {"present": present, "quality": qual}

    tier2_present = sum(1 for r in tier2_results.values() if r["present"])
    tier2_total = len(all_sa_fields)
    tier2_avg_quality = (
        sum(r["quality"] for r in tier2_results.values()) / tier2_total
        if tier2_total > 0 else 0
    )
    tier2_score = (tier2_present / tier2_total) * (tier2_avg_quality / 3) * 100

    # Tier 3: Quality metrics
    purpose_quality = quality_score("purposes", record.get("purposes"))
    retention_quality = quality_score("retention_periods", record.get("retention_periods"))
    security_quality = quality_score("security_measures", record.get("security_measures"))
    transfer_quality = quality_score("international_transfers", record.get("international_transfers"))
    currency = check_review_currency(record)

    tier3_metrics = {
        "purpose_specificity": purpose_quality,
        "retention_concreteness": retention_quality,
        "security_description": security_quality,
        "transfer_documentation": transfer_quality,
        "review_currency": currency,
    }
    tier3_score = (sum(tier3_metrics.values()) / (5 * 3)) * 100

    # Overall score
    overall = (tier1_score * 0.40) + (tier2_score * 0.35) + (tier3_score * 0.25)

    # Rating
    if overall >= 95:
        rating = "Excellent"
    elif overall >= 85:
        rating = "Good"
    elif overall >= 70:
        rating = "Acceptable"
    elif overall >= 50:
        rating = "Poor"
    else:
        rating = "Critical"

    # Gaps
    gaps = []
    for field, result in tier1_results.items():
        if not result["present"]:
            gaps.append({
                "field": field,
                "classification": "Missing",
                "severity": "Critical",
                "tier": 1,
            })
        elif result["quality"] <= 1:
            gaps.append({
                "field": field,
                "classification": "Incomplete" if result["quality"] == 1 else "Vague",
                "severity": "Major",
                "tier": 1,
            })

    for field in template["sa_recommended_fields"]:
        if not is_populated(record.get(field)):
            gaps.append({
                "field": field,
                "classification": "Enhancement",
                "severity": "Low",
                "tier": 2,
            })

    return {
        "record_id": record_id,
        "processing_activity": record.get("processing_activity", record.get("service_name", "N/A")),
        "sa_template": template["name"],
        "tier1_score": round(tier1_score, 1),
        "tier2_score": round(tier2_score, 1),
        "tier3_score": round(tier3_score, 1),
        "overall_score": round(overall, 1),
        "rating": rating,
        "tier1_details": tier1_results,
        "tier3_metrics": tier3_metrics,
        "gaps": gaps,
        "gap_count": {"Critical": 0, "Major": 0, "Low": 0},
    }


def generate_audit_report(ropa: dict, sa_template: str = "cnil") -> str:
    """Generate a full completeness audit report."""
    records = ropa.get("records", [])
    org = ropa.get("organisation", "Unknown")
    template = SA_TEMPLATES.get(sa_template, SA_TEMPLATES["cnil"])

    lines = []
    lines.append("=" * 80)
    lines.append(f"RoPA COMPLETENESS AUDIT REPORT")
    lines.append(f"Organisation: {org}")
    lines.append(f"SA Template: {template['name']}")
    lines.append(f"Audit Date: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append(f"Records Audited: {len(records)}")
    lines.append("=" * 80)

    all_results = []
    for record in records:
        result = audit_entry(record, sa_template)
        all_results.append(result)

    # Aggregate scores
    if all_results:
        avg_overall = sum(r["overall_score"] for r in all_results) / len(all_results)
        avg_tier1 = sum(r["tier1_score"] for r in all_results) / len(all_results)
        avg_tier2 = sum(r["tier2_score"] for r in all_results) / len(all_results)
        avg_tier3 = sum(r["tier3_score"] for r in all_results) / len(all_results)
    else:
        avg_overall = avg_tier1 = avg_tier2 = avg_tier3 = 0

    lines.append(f"\n{'─' * 40}")
    lines.append("AGGREGATE SCORES")
    lines.append(f"{'─' * 40}")
    lines.append(f"  Overall Completeness: {avg_overall:.1f}%")
    lines.append(f"  Tier 1 (Art. 30 Mandatory): {avg_tier1:.1f}%")
    lines.append(f"  Tier 2 (SA Extended): {avg_tier2:.1f}%")
    lines.append(f"  Tier 3 (Quality): {avg_tier3:.1f}%")

    if avg_overall >= 95:
        lines.append(f"\n  VERDICT: SUPERVISORY AUTHORITY READY")
    elif avg_overall >= 85:
        lines.append(f"\n  VERDICT: GOOD — minor improvements recommended")
    elif avg_overall >= 70:
        lines.append(f"\n  VERDICT: ACCEPTABLE — remediation plan required")
    else:
        lines.append(f"\n  VERDICT: REQUIRES URGENT REMEDIATION")

    # Per-entry results
    lines.append(f"\n{'─' * 40}")
    lines.append("PER-ENTRY RESULTS")
    lines.append(f"{'─' * 40}")

    for result in sorted(all_results, key=lambda r: r["overall_score"]):
        lines.append(f"\n  {result['record_id']}: {result['processing_activity']}")
        lines.append(f"    Overall: {result['overall_score']}% ({result['rating']})")
        lines.append(f"    Tier 1: {result['tier1_score']}% | Tier 2: {result['tier2_score']}% | Tier 3: {result['tier3_score']}%")
        if result["gaps"]:
            for gap in result["gaps"]:
                lines.append(f"    [{gap['severity']}] {gap['field']}: {gap['classification']}")

    # Gap summary
    total_critical = sum(len([g for g in r["gaps"] if g["severity"] == "Critical"]) for r in all_results)
    total_major = sum(len([g for g in r["gaps"] if g["severity"] == "Major"]) for r in all_results)
    total_low = sum(len([g for g in r["gaps"] if g["severity"] == "Low"]) for r in all_results)

    lines.append(f"\n{'─' * 40}")
    lines.append("GAP SUMMARY")
    lines.append(f"{'─' * 40}")
    lines.append(f"  Critical gaps: {total_critical}")
    lines.append(f"  Major gaps: {total_major}")
    lines.append(f"  Enhancement opportunities: {total_low}")
    lines.append(f"  Total: {total_critical + total_major + total_low}")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python process.py audit <ropa.json> [--template cnil|ico|bfdi] [--output report.txt]")
        print("  python process.py score <ropa.json> [--template cnil|ico|bfdi]")
        sys.exit(1)

    command = sys.argv[1]
    sa_template = "cnil"
    if "--template" in sys.argv:
        idx = sys.argv.index("--template")
        if idx + 1 < len(sys.argv):
            sa_template = sys.argv[idx + 1].lower()

    if command in ("audit", "score"):
        if len(sys.argv) < 3:
            print("ERROR: Provide the RoPA JSON file path.")
            sys.exit(1)

        with open(sys.argv[2], "r", encoding="utf-8") as f:
            ropa = json.load(f)

        report = generate_audit_report(ropa, sa_template)

        output = None
        if "--output" in sys.argv:
            idx = sys.argv.index("--output")
            if idx + 1 < len(sys.argv):
                output = sys.argv[idx + 1]

        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"Audit report written to {output}")
        else:
            print(report)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
