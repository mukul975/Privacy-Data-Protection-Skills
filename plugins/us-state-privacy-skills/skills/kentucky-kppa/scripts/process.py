#!/usr/bin/env python3
"""
Kentucky KPPA Compliance Tool

Assesses KPPA applicability under KRS §367.405, generates readiness
assessment for the January 1, 2026 effective date, and tracks
consumer rights requests.
"""

import json
from datetime import datetime, timezone, timedelta, date
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class KPPARight(Enum):
    ACCESS = "access"
    CORRECT = "correct"
    DELETE = "delete"
    PORTABILITY = "portability"
    OPT_OUT_TARGETED_ADS = "opt_out_targeted_advertising"
    OPT_OUT_SALE = "opt_out_sale"
    OPT_OUT_PROFILING = "opt_out_profiling"


KPPA_EFFECTIVE_DATE = date(2026, 1, 1)

READINESS_CHECKLIST = [
    {"id": "KY-01", "item": "Applicability determination documented", "section": "§367.405", "category": "legal"},
    {"id": "KY-02", "item": "Privacy notice updated with KPPA requirements", "section": "§367.413(2)", "category": "legal"},
    {"id": "KY-03", "item": "Consumer rights portal deployed", "section": "§367.415", "category": "technical"},
    {"id": "KY-04", "item": "Opt-out mechanisms for targeted ads, sale, profiling", "section": "§367.415(1)(e)", "category": "technical"},
    {"id": "KY-05", "item": "Sensitive data consent mechanisms deployed", "section": "§367.413(5)", "category": "technical"},
    {"id": "KY-06", "item": "45-day SLA monitoring for consumer requests", "section": "§367.417", "category": "operations"},
    {"id": "KY-07", "item": "Appeal process with 60-day SLA", "section": "§367.417", "category": "operations"},
    {"id": "KY-08", "item": "Processor contracts updated with KPPA terms", "section": "§367.421", "category": "legal"},
    {"id": "KY-09", "item": "DPIAs completed for applicable processing", "section": "§367.419", "category": "legal"},
    {"id": "KY-10", "item": "Staff training completed", "section": "general", "category": "operations"},
    {"id": "KY-11", "item": "Data minimization controls reviewed", "section": "§367.413(1)", "category": "technical"},
    {"id": "KY-12", "item": "De-identified data procedures documented", "section": "§367.411", "category": "technical"},
]


@dataclass
class KPPAApplicability:
    """Assess KPPA applicability under KRS §367.405."""
    organization_name: str
    conducts_business_in_kentucky: bool
    targets_kentucky_residents: bool
    kentucky_consumer_count: int
    revenue_from_sale_pct: float
    is_government: bool = False
    is_glba: bool = False
    is_hipaa: bool = False
    is_nonprofit: bool = False

    def assess(self) -> dict:
        exemptions = []
        if self.is_government:
            exemptions.append({"name": "Government entity", "section": "§367.407(1)"})
        if self.is_glba:
            exemptions.append({"name": "GLBA institution", "section": "§367.407(2)"})
        if self.is_hipaa:
            exemptions.append({"name": "HIPAA entity", "section": "§367.407(3)"})
        if self.is_nonprofit:
            exemptions.append({"name": "Nonprofit", "section": "§367.407(4)"})

        if exemptions:
            return {"organization": self.organization_name, "applicable": False, "exemptions": exemptions}

        if not (self.conducts_business_in_kentucky or self.targets_kentucky_residents):
            return {"organization": self.organization_name, "applicable": False, "reason": "No Kentucky nexus"}

        thresholds_met = []
        if self.kentucky_consumer_count >= 100_000:
            thresholds_met.append({
                "threshold": "option_1",
                "description": f"{self.kentucky_consumer_count:,} consumers >= 100,000",
                "section": "§367.405(1)",
            })
        if self.kentucky_consumer_count >= 25_000 and self.revenue_from_sale_pct > 50:
            thresholds_met.append({
                "threshold": "option_2",
                "description": f"{self.kentucky_consumer_count:,} consumers >= 25,000 AND {self.revenue_from_sale_pct}% > 50% revenue",
                "section": "§367.405(2)",
            })

        days_to_effective = (KPPA_EFFECTIVE_DATE - date.today()).days
        return {
            "organization": self.organization_name,
            "applicable": len(thresholds_met) > 0,
            "thresholds_met": thresholds_met,
            "effective_date": KPPA_EFFECTIVE_DATE.isoformat(),
            "days_until_effective": max(days_to_effective, 0),
            "assessment_date": datetime.now(timezone.utc).isoformat(),
        }


def generate_readiness_report(responses: dict[str, str]) -> dict:
    """Generate KPPA readiness report for January 1, 2026 effective date."""
    results = []
    complete_count = 0
    incomplete_count = 0

    for item in READINESS_CHECKLIST:
        status = responses.get(item["id"], "not_started")
        if status == "complete":
            complete_count += 1
        else:
            incomplete_count += 1
        results.append({
            "check_id": item["id"],
            "item": item["item"],
            "section": item["section"],
            "category": item["category"],
            "status": status,
        })

    total = len(READINESS_CHECKLIST)
    readiness_pct = (complete_count / total * 100) if total > 0 else 0
    days_remaining = (KPPA_EFFECTIVE_DATE - date.today()).days

    return {
        "report_title": "KPPA Readiness Assessment",
        "effective_date": KPPA_EFFECTIVE_DATE.isoformat(),
        "days_until_effective": max(days_remaining, 0),
        "readiness_percentage": round(readiness_pct, 1),
        "complete": complete_count,
        "incomplete": incomplete_count,
        "total_items": total,
        "results": results,
        "incomplete_items": [r for r in results if r["status"] != "complete"],
    }


if __name__ == "__main__":
    # Applicability
    print("=== KPPA Applicability Assessment ===")
    assessment = KPPAApplicability(
        organization_name="Liberty Commerce Inc.",
        conducts_business_in_kentucky=True,
        targets_kentucky_residents=True,
        kentucky_consumer_count=68_000,
        revenue_from_sale_pct=12.0,
    )
    print(json.dumps(assessment.assess(), indent=2))

    # Readiness report
    print("\n=== KPPA Readiness Report ===")
    responses = {
        "KY-01": "complete", "KY-02": "in_progress", "KY-03": "not_started",
        "KY-04": "not_started", "KY-05": "not_started", "KY-06": "not_started",
        "KY-07": "not_started", "KY-08": "in_progress", "KY-09": "in_progress",
        "KY-10": "not_started", "KY-11": "complete", "KY-12": "complete",
    }
    report = generate_readiness_report(responses)
    print(f"Readiness: {report['readiness_percentage']}%")
    print(f"Days until effective: {report['days_until_effective']}")
    print(f"Complete: {report['complete']}/{report['total_items']}")
    print(f"\nIncomplete items:")
    for item in report["incomplete_items"]:
        print(f"  [{item['status']}] {item['check_id']}: {item['item']}")
