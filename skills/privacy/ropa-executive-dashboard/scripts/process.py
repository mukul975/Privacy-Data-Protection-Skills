#!/usr/bin/env python3
"""
RoPA Executive Dashboard Generator

Calculates compliance metrics, risk indicators, and operational KPIs
from RoPA data. Generates structured dashboard reports for executive
and board-level consumption.
"""

import json
import sys
from datetime import datetime
from typing import Any
from collections import Counter


def is_populated(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str) and value.strip() in ("", "N/A", "n/a", "None", "TBD"):
        return False
    if isinstance(value, (list, dict)) and len(value) == 0:
        return False
    return True


def calculate_compliance_metrics(records: list[dict]) -> dict:
    """Calculate Tier 1 compliance metrics."""
    total = len(records)
    if total == 0:
        return {"error": "No records to analyze"}

    mandatory_fields = [
        "controller_identity", "purposes", "data_subject_categories",
        "personal_data_categories", "recipient_categories",
        "international_transfers", "retention_periods", "security_measures",
    ]

    # Completeness
    complete_entries = 0
    for record in records:
        all_present = all(is_populated(record.get(f)) for f in mandatory_fields)
        if all_present:
            complete_entries += 1
    completeness = (complete_entries / total) * 100

    # Staleness
    stale_count = 0
    now = datetime.now()
    for record in records:
        lr = record.get("last_reviewed_date")
        if not lr:
            stale_count += 1
            continue
        try:
            rd = datetime.strptime(lr, "%Y-%m-%d")
            if (now - rd).days > 365:
                stale_count += 1
        except ValueError:
            stale_count += 1
    staleness_rate = (stale_count / total) * 100

    # DPA coverage
    total_processors = 0
    processors_with_dpa = 0
    for record in records:
        recipients = record.get("recipient_categories", [])
        if isinstance(recipients, list):
            for r in recipients:
                if isinstance(r, dict) and "processor" in r.get("type", "").lower():
                    total_processors += 1
                    if is_populated(r.get("dpa_reference")):
                        processors_with_dpa += 1
    dpa_coverage = (processors_with_dpa / total_processors * 100) if total_processors > 0 else 100

    # Transfer mechanism coverage
    total_transfers = 0
    transfers_with_mechanism = 0
    for record in records:
        transfers = record.get("international_transfers", [])
        if isinstance(transfers, list):
            for t in transfers:
                if isinstance(t, dict):
                    total_transfers += 1
                    if is_populated(t.get("safeguard_mechanism")):
                        transfers_with_mechanism += 1
    transfer_coverage = (transfers_with_mechanism / total_transfers * 100) if total_transfers > 0 else 100

    # DPIA linkage
    dpia_required = sum(1 for r in records if r.get("dpia_required"))
    dpia_linked = sum(1 for r in records if r.get("dpia_required") and is_populated(r.get("dpia_reference")))
    dpia_linkage = (dpia_linked / dpia_required * 100) if dpia_required > 0 else 100

    return {
        "completeness_score": round(completeness, 1),
        "staleness_rate": round(staleness_rate, 1),
        "dpa_coverage": round(dpa_coverage, 1),
        "transfer_mechanism_coverage": round(transfer_coverage, 1),
        "dpia_linkage": round(dpia_linkage, 1),
        "total_records": total,
        "complete_entries": complete_entries,
        "stale_entries": stale_count,
        "processors_total": total_processors,
        "processors_with_dpa": processors_with_dpa,
        "transfers_total": total_transfers,
        "transfers_with_mechanism": transfers_with_mechanism,
        "dpia_required_count": dpia_required,
        "dpia_linked_count": dpia_linked,
    }


def calculate_risk_metrics(records: list[dict]) -> dict:
    """Calculate Tier 2 risk metrics."""
    total = len(records)

    # Special category count
    special_cat_count = 0
    for record in records:
        sc = str(record.get("special_category_data", "")).lower()
        if sc not in ("none", "none detected", "no", ""):
            special_cat_count += 1

    # High-risk ratio
    dpia_required = sum(1 for r in records if r.get("dpia_required"))
    high_risk_ratio = (dpia_required / total * 100) if total > 0 else 0

    # Transfer counts
    transfer_count = 0
    non_adequate_transfers = 0
    transfer_destinations = Counter()

    adequacy_countries = {
        "united kingdom", "switzerland", "japan", "south korea", "canada",
        "new zealand", "israel", "argentina", "uruguay", "andorra",
        "faroe islands", "guernsey", "isle of man", "jersey",
    }

    for record in records:
        transfers = record.get("international_transfers", [])
        if isinstance(transfers, list):
            for t in transfers:
                if isinstance(t, dict):
                    transfer_count += 1
                    country = t.get("destination_country", "Unknown").lower()
                    transfer_destinations[t.get("destination_country", "Unknown")] += 1
                    mechanism = str(t.get("safeguard_mechanism", "")).lower()
                    if "adequacy" not in mechanism and "data privacy framework" not in mechanism:
                        if country not in adequacy_countries:
                            non_adequate_transfers += 1

    # Processor count
    processors = set()
    for record in records:
        recipients = record.get("recipient_categories", [])
        if isinstance(recipients, list):
            for r in recipients:
                if isinstance(r, dict) and "processor" in r.get("type", "").lower():
                    processors.add(r.get("recipient", "Unknown"))

    # Average entry age
    now = datetime.now()
    total_age = 0
    aged_count = 0
    for record in records:
        lr = record.get("last_reviewed_date")
        if lr:
            try:
                rd = datetime.strptime(lr, "%Y-%m-%d")
                total_age += (now - rd).days
                aged_count += 1
            except ValueError:
                pass
    avg_age = total_age / aged_count if aged_count > 0 else 0

    return {
        "special_category_count": special_cat_count,
        "high_risk_ratio": round(high_risk_ratio, 1),
        "international_transfer_count": transfer_count,
        "non_adequate_transfers": non_adequate_transfers,
        "transfer_destinations": dict(transfer_destinations),
        "unique_processor_count": len(processors),
        "average_entry_age_days": round(avg_age),
    }


def calculate_department_distribution(records: list[dict]) -> dict:
    """Calculate processing activity distribution by department."""
    dept_counts = Counter()
    dept_risk = {}

    for record in records:
        dept = record.get("department", "Unassigned")
        dept_counts[dept] += 1
        if dept not in dept_risk:
            dept_risk[dept] = {"low": 0, "medium": 0, "high": 0, "critical": 0}

        risk = "low"
        has_special = str(record.get("special_category_data", "")).lower() not in ("none", "none detected", "no", "")
        has_dpia = record.get("dpia_required", False)
        has_transfers = len(record.get("international_transfers", [])) > 0

        if has_dpia and has_special and has_transfers:
            risk = "critical"
        elif has_dpia or has_special:
            risk = "high"
        elif has_transfers:
            risk = "medium"

        dept_risk[dept][risk] += 1

    return {
        "department_counts": dict(dept_counts),
        "department_risk_heatmap": dept_risk,
    }


def determine_sa_readiness(compliance: dict) -> dict:
    """Determine supervisory authority readiness traffic lights."""
    def traffic_light(value, green_threshold, amber_threshold, invert=False):
        if invert:
            if value <= green_threshold:
                return "GREEN"
            elif value <= amber_threshold:
                return "AMBER"
            return "RED"
        if value >= green_threshold:
            return "GREEN"
        elif value >= amber_threshold:
            return "AMBER"
        return "RED"

    return {
        "completeness": traffic_light(compliance["completeness_score"], 95, 85),
        "staleness": traffic_light(compliance["staleness_rate"], 5, 15, invert=True),
        "dpa_coverage": traffic_light(compliance["dpa_coverage"], 100, 90),
        "transfer_coverage": traffic_light(compliance["transfer_mechanism_coverage"], 100, 90),
        "dpia_linkage": traffic_light(compliance["dpia_linkage"], 100, 80),
    }


def generate_dashboard_report(ropa: dict) -> str:
    """Generate a full executive dashboard report."""
    records = ropa.get("records", [])
    org = ropa.get("organisation", "Unknown")

    compliance = calculate_compliance_metrics(records)
    risk = calculate_risk_metrics(records)
    dept = calculate_department_distribution(records)
    readiness = determine_sa_readiness(compliance)

    lines = []
    lines.append("=" * 80)
    lines.append(f"RoPA EXECUTIVE DASHBOARD — {org}")
    lines.append(f"Report Date: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append(f"Total Processing Activities: {len(records)}")
    lines.append("=" * 80)

    # SA Readiness
    lines.append(f"\n{'━' * 40}")
    lines.append("SUPERVISORY AUTHORITY READINESS")
    lines.append(f"{'━' * 40}")
    for metric, status in readiness.items():
        indicator = {"GREEN": "[OK]", "AMBER": "[!!]", "RED": "[XX]"}.get(status, "[??]")
        lines.append(f"  {indicator} {metric.replace('_', ' ').title()}: {status}")

    overall_green = sum(1 for s in readiness.values() if s == "GREEN")
    overall_total = len(readiness)
    if overall_green == overall_total:
        lines.append(f"\n  OVERALL: READY FOR SA INSPECTION")
    elif overall_green >= overall_total - 1:
        lines.append(f"\n  OVERALL: LARGELY READY — address amber items")
    else:
        lines.append(f"\n  OVERALL: NOT READY — remediation required")

    # Compliance Metrics
    lines.append(f"\n{'━' * 40}")
    lines.append("COMPLIANCE METRICS (Tier 1)")
    lines.append(f"{'━' * 40}")
    lines.append(f"  Completeness Score:       {compliance['completeness_score']}%")
    lines.append(f"  Staleness Rate:           {compliance['staleness_rate']}% ({compliance['stale_entries']} of {compliance['total_records']} entries)")
    lines.append(f"  DPA Coverage:             {compliance['dpa_coverage']}% ({compliance['processors_with_dpa']}/{compliance['processors_total']} processors)")
    lines.append(f"  Transfer Mech. Coverage:  {compliance['transfer_mechanism_coverage']}% ({compliance['transfers_with_mechanism']}/{compliance['transfers_total']} transfers)")
    lines.append(f"  DPIA Linkage:             {compliance['dpia_linkage']}% ({compliance['dpia_linked_count']}/{compliance['dpia_required_count']} high-risk entries)")

    # Risk Metrics
    lines.append(f"\n{'━' * 40}")
    lines.append("RISK METRICS (Tier 2)")
    lines.append(f"{'━' * 40}")
    lines.append(f"  Special Category Processing: {risk['special_category_count']} activities")
    lines.append(f"  High-Risk Ratio:             {risk['high_risk_ratio']}%")
    lines.append(f"  International Transfers:     {risk['international_transfer_count']} total ({risk['non_adequate_transfers']} to non-adequate countries)")
    lines.append(f"  Unique Processors:           {risk['unique_processor_count']}")
    lines.append(f"  Average Entry Age:           {risk['average_entry_age_days']} days")

    if risk["transfer_destinations"]:
        lines.append(f"\n  Transfer Destinations:")
        for country, count in sorted(risk["transfer_destinations"].items(), key=lambda x: -x[1]):
            lines.append(f"    {country}: {count} transfer(s)")

    # Department Distribution
    lines.append(f"\n{'━' * 40}")
    lines.append("RISK HEATMAP BY DEPARTMENT")
    lines.append(f"{'━' * 40}")
    lines.append(f"  {'Department':<25} {'Low':>5} {'Med':>5} {'High':>5} {'Crit':>5} {'Total':>6}")
    lines.append(f"  {'─' * 51}")
    for dept_name, risks in dept["department_risk_heatmap"].items():
        total_dept = sum(risks.values())
        lines.append(f"  {dept_name:<25} {risks['low']:>5} {risks['medium']:>5} {risks['high']:>5} {risks['critical']:>5} {total_dept:>6}")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python process.py dashboard <ropa.json> [--output report.txt]")
        print("  python process.py metrics <ropa.json> [--output metrics.json]")
        print("  python process.py readiness <ropa.json>")
        sys.exit(1)

    command = sys.argv[1]

    if command in ("dashboard", "metrics", "readiness"):
        if len(sys.argv) < 3:
            print("ERROR: Provide the RoPA JSON file.")
            sys.exit(1)

        with open(sys.argv[2], "r", encoding="utf-8") as f:
            ropa = json.load(f)

        if command == "dashboard":
            report = generate_dashboard_report(ropa)
            output = None
            if "--output" in sys.argv:
                idx = sys.argv.index("--output")
                if idx + 1 < len(sys.argv):
                    output = sys.argv[idx + 1]
            if output:
                with open(output, "w", encoding="utf-8") as f:
                    f.write(report)
                print(f"Dashboard report written to {output}")
            else:
                print(report)

        elif command == "metrics":
            records = ropa.get("records", [])
            metrics = {
                "compliance": calculate_compliance_metrics(records),
                "risk": calculate_risk_metrics(records),
                "departments": calculate_department_distribution(records),
                "readiness": determine_sa_readiness(calculate_compliance_metrics(records)),
                "generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            output_json = json.dumps(metrics, indent=2)
            output = None
            if "--output" in sys.argv:
                idx = sys.argv.index("--output")
                if idx + 1 < len(sys.argv):
                    output = sys.argv[idx + 1]
            if output:
                with open(output, "w", encoding="utf-8") as f:
                    f.write(output_json)
                print(f"Metrics written to {output}")
            else:
                print(output_json)

        elif command == "readiness":
            records = ropa.get("records", [])
            compliance = calculate_compliance_metrics(records)
            readiness = determine_sa_readiness(compliance)
            print("SA READINESS STATUS:")
            all_green = True
            for metric, status in readiness.items():
                print(f"  {metric}: {status}")
                if status != "GREEN":
                    all_green = False
            print(f"\nOverall: {'READY' if all_green else 'NOT READY'}")
            sys.exit(0 if all_green else 1)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
