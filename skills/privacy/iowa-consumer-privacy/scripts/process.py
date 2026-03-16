#!/usr/bin/env python3
"""
Iowa ICDPA Compliance Tool

Assesses ICDPA applicability under Iowa Code §715D.2, tracks consumer
rights requests with the 90-day response window, and generates
compliance readiness reports.
"""

import json
from datetime import datetime, timezone, timedelta, date
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class ICDPARight(Enum):
    ACCESS = "access"
    DELETE = "delete"
    OPT_OUT_SALE = "opt_out_sale"
    OPT_OUT_TARGETED_ADS = "opt_out_targeted_advertising"


ICDPA_EFFECTIVE_DATE = date(2025, 1, 1)
RESPONSE_WINDOW_DAYS = 90
APPEAL_WINDOW_DAYS = 60
CURE_PERIOD_DAYS = 90

SENSITIVE_DATA_CATEGORIES = [
    "Racial or ethnic origin",
    "Religious beliefs",
    "Mental or physical health diagnosis",
    "Sexual orientation",
    "Citizenship or immigration status",
    "Genetic data",
    "Biometric data for identification",
    "Personal data of a known child",
    "Precise geolocation data",
]

READINESS_CHECKLIST = [
    {"id": "IA-01", "item": "Applicability determination documented", "section": "§715D.2", "category": "legal"},
    {"id": "IA-02", "item": "Privacy notice updated with ICDPA requirements", "section": "§715D.4(6)", "category": "legal"},
    {"id": "IA-03", "item": "Consumer rights portal deployed (access, delete, opt-out)", "section": "§715D.4", "category": "technical"},
    {"id": "IA-04", "item": "Opt-out mechanisms for sale and targeted advertising", "section": "§715D.4(1)(c)", "category": "technical"},
    {"id": "IA-05", "item": "Sensitive data consent mechanisms deployed", "section": "§715D.4(4)", "category": "technical"},
    {"id": "IA-06", "item": "90-day SLA monitoring for consumer requests", "section": "§715D.5", "category": "operations"},
    {"id": "IA-07", "item": "Appeal process with 60-day SLA established", "section": "§715D.5", "category": "operations"},
    {"id": "IA-08", "item": "Processor contracts updated with ICDPA terms", "section": "§715D.5", "category": "legal"},
    {"id": "IA-09", "item": "Staff training completed on ICDPA requirements", "section": "general", "category": "operations"},
    {"id": "IA-10", "item": "Data minimization controls reviewed", "section": "§715D.4(2)", "category": "technical"},
    {"id": "IA-11", "item": "Data security practices documented", "section": "§715D.4(3)", "category": "technical"},
    {"id": "IA-12", "item": "90-day cure period response plan established", "section": "§715D.6(2)", "category": "legal"},
]


@dataclass
class ICDPAApplicability:
    """Assess ICDPA applicability under Iowa Code §715D.2."""
    organization_name: str
    conducts_business_in_iowa: bool
    targets_iowa_consumers: bool
    iowa_consumer_count: int
    revenue_from_sale_pct: float
    is_government: bool = False
    is_glba: bool = False
    is_hipaa: bool = False
    is_nonprofit: bool = False
    is_higher_ed: bool = False

    def assess(self) -> dict:
        exemptions = []
        if self.is_government:
            exemptions.append({"name": "Government entity", "section": "§715D.3(1)"})
        if self.is_glba:
            exemptions.append({"name": "GLBA institution", "section": "§715D.3(2)"})
        if self.is_hipaa:
            exemptions.append({"name": "HIPAA entity", "section": "§715D.3(3)"})
        if self.is_nonprofit:
            exemptions.append({"name": "Nonprofit", "section": "§715D.3(4)"})
        if self.is_higher_ed:
            exemptions.append({"name": "Higher education institution", "section": "§715D.3(5)"})

        if exemptions:
            return {
                "organization": self.organization_name,
                "applicable": False,
                "exemptions": exemptions,
                "assessment_date": datetime.now(timezone.utc).isoformat(),
            }

        if not (self.conducts_business_in_iowa or self.targets_iowa_consumers):
            return {
                "organization": self.organization_name,
                "applicable": False,
                "reason": "No Iowa nexus — does not conduct business in Iowa or target Iowa consumers",
                "assessment_date": datetime.now(timezone.utc).isoformat(),
            }

        thresholds_met = []
        if self.iowa_consumer_count >= 100_000:
            thresholds_met.append({
                "threshold": "option_1",
                "description": f"{self.iowa_consumer_count:,} consumers >= 100,000",
                "section": "§715D.2(1)",
            })
        if self.iowa_consumer_count >= 25_000 and self.revenue_from_sale_pct > 50:
            thresholds_met.append({
                "threshold": "option_2",
                "description": f"{self.iowa_consumer_count:,} consumers >= 25,000 AND {self.revenue_from_sale_pct}% > 50% revenue from sale",
                "section": "§715D.2(2)",
            })

        return {
            "organization": self.organization_name,
            "applicable": len(thresholds_met) > 0,
            "thresholds_met": thresholds_met,
            "effective_date": ICDPA_EFFECTIVE_DATE.isoformat(),
            "assessment_date": datetime.now(timezone.utc).isoformat(),
        }


@dataclass
class ConsumerRequest:
    """Track an Iowa consumer rights request with 90-day SLA."""
    request_id: str
    consumer_id: str
    right_type: ICDPARight
    received_date: date
    status: str = "pending"
    response_date: Optional[date] = None
    appeal_filed: bool = False
    appeal_date: Optional[date] = None
    appeal_response_date: Optional[date] = None

    @property
    def deadline(self) -> date:
        return self.received_date + timedelta(days=RESPONSE_WINDOW_DAYS)

    @property
    def days_remaining(self) -> int:
        if self.status in ("fulfilled", "denied"):
            return 0
        return max((self.deadline - date.today()).days, 0)

    @property
    def is_overdue(self) -> bool:
        return self.status == "pending" and date.today() > self.deadline

    @property
    def appeal_deadline(self) -> Optional[date]:
        if self.appeal_date:
            return self.appeal_date + timedelta(days=APPEAL_WINDOW_DAYS)
        return None

    def to_dict(self) -> dict:
        result = {
            "request_id": self.request_id,
            "consumer_id": self.consumer_id,
            "right_type": self.right_type.value,
            "received_date": self.received_date.isoformat(),
            "deadline": self.deadline.isoformat(),
            "days_remaining": self.days_remaining,
            "status": self.status,
            "is_overdue": self.is_overdue,
        }
        if self.response_date:
            result["response_date"] = self.response_date.isoformat()
        if self.appeal_filed:
            result["appeal_filed"] = True
            result["appeal_date"] = self.appeal_date.isoformat() if self.appeal_date else None
            result["appeal_deadline"] = self.appeal_deadline.isoformat() if self.appeal_deadline else None
        return result


def generate_readiness_report(responses: dict[str, str]) -> dict:
    """Generate ICDPA readiness report."""
    results = []
    complete_count = 0

    for item in READINESS_CHECKLIST:
        status = responses.get(item["id"], "not_started")
        if status == "complete":
            complete_count += 1
        results.append({
            "check_id": item["id"],
            "item": item["item"],
            "section": item["section"],
            "category": item["category"],
            "status": status,
        })

    total = len(READINESS_CHECKLIST)
    readiness_pct = (complete_count / total * 100) if total > 0 else 0

    return {
        "report_title": "ICDPA Compliance Readiness Assessment",
        "effective_date": ICDPA_EFFECTIVE_DATE.isoformat(),
        "law_status": "effective" if date.today() >= ICDPA_EFFECTIVE_DATE else "pre-effective",
        "readiness_percentage": round(readiness_pct, 1),
        "complete": complete_count,
        "incomplete": total - complete_count,
        "total_items": total,
        "results": results,
        "incomplete_items": [r for r in results if r["status"] != "complete"],
        "key_distinctions": [
            "Iowa provides only 3 consumer rights (no correct, no portability)",
            "90-day response window (longest among state privacy laws)",
            "90-day cure period (longest, permanent, no sunset)",
            "No DPIA requirement",
            "No universal opt-out mechanism requirement",
        ],
    }


def compare_with_other_states(iowa_data: dict) -> dict:
    """Compare Iowa ICDPA provisions with other state privacy laws."""
    states = {
        "Iowa ICDPA": {
            "effective": "2025-01-01", "threshold": 100_000,
            "rights": ["access", "delete", "opt-out (sale, targeted ads)"],
            "right_to_correct": False, "right_to_portability": False,
            "dpia_required": False, "universal_opt_out": False,
            "response_days": 90, "cure_days": 90,
        },
        "Virginia VCDPA": {
            "effective": "2023-01-01", "threshold": 100_000,
            "rights": ["access", "correct", "delete", "portability", "opt-out"],
            "right_to_correct": True, "right_to_portability": True,
            "dpia_required": True, "universal_opt_out": False,
            "response_days": 45, "cure_days": 30,
        },
        "Connecticut CTDPA": {
            "effective": "2023-07-01", "threshold": 100_000,
            "rights": ["access", "correct", "delete", "portability", "opt-out"],
            "right_to_correct": True, "right_to_portability": True,
            "dpia_required": True, "universal_opt_out": True,
            "response_days": 45, "cure_days": 60,
        },
        "Colorado CPA": {
            "effective": "2023-07-01", "threshold": 100_000,
            "rights": ["access", "correct", "delete", "portability", "opt-out"],
            "right_to_correct": True, "right_to_portability": True,
            "dpia_required": True, "universal_opt_out": True,
            "response_days": 45, "cure_days": 60,
        },
    }

    return {
        "comparison_title": "Iowa ICDPA Multi-State Comparison",
        "iowa_consumer_count": iowa_data.get("consumer_count", 0),
        "states": states,
        "iowa_advantages": [
            "Longest response window (90 days) reduces operational burden",
            "Longest cure period (90 days) provides maximum remediation time",
            "Fewest consumer rights reduces request processing complexity",
            "No DPIA requirement reduces compliance overhead",
        ],
    }


if __name__ == "__main__":
    print("=== ICDPA Applicability Assessment ===")
    assessment = ICDPAApplicability(
        organization_name="Liberty Commerce Inc.",
        conducts_business_in_iowa=True,
        targets_iowa_consumers=True,
        iowa_consumer_count=52_000,
        revenue_from_sale_pct=12.0,
    )
    result = assessment.assess()
    print(json.dumps(result, indent=2))

    print("\n=== ICDPA Consumer Request Tracking ===")
    request = ConsumerRequest(
        request_id="IA-REQ-2025-00001",
        consumer_id="consumer-8842",
        right_type=ICDPARight.ACCESS,
        received_date=date(2025, 2, 15),
    )
    print(json.dumps(request.to_dict(), indent=2))

    print("\n=== ICDPA Readiness Report ===")
    responses = {
        "IA-01": "complete", "IA-02": "complete", "IA-03": "complete",
        "IA-04": "complete", "IA-05": "complete", "IA-06": "complete",
        "IA-07": "complete", "IA-08": "in_progress", "IA-09": "complete",
        "IA-10": "complete", "IA-11": "complete", "IA-12": "complete",
    }
    report = generate_readiness_report(responses)
    print(f"Readiness: {report['readiness_percentage']}%")
    print(f"Law status: {report['law_status']}")
    print(f"Complete: {report['complete']}/{report['total_items']}")
    if report["incomplete_items"]:
        print("Incomplete items:")
        for item in report["incomplete_items"]:
            print(f"  [{item['status']}] {item['check_id']}: {item['item']}")

    print("\n=== Multi-State Comparison ===")
    comparison = compare_with_other_states({"consumer_count": 52_000})
    print(f"Iowa advantages:")
    for adv in comparison["iowa_advantages"]:
        print(f"  - {adv}")
