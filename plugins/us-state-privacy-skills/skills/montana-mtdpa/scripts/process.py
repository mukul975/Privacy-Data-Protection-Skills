#!/usr/bin/env python3
"""
Montana MTDPA Compliance Assessment Tool

Assesses applicability under MCA §30-14-2803 with the lowest
50,000-consumer threshold, tracks consumer rights requests with
the shorter 15-day extension period, and manages universal opt-out.
"""

import json
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class MTDPARight(Enum):
    ACCESS = "access"
    CORRECT = "correct"
    DELETE = "delete"
    PORTABILITY = "portability"
    OPT_OUT_TARGETED_ADS = "opt_out_targeted_advertising"
    OPT_OUT_SALE = "opt_out_sale"
    OPT_OUT_PROFILING = "opt_out_profiling"


MTDPA_THRESHOLDS = {
    "option_1": {
        "consumer_count": 50_000,
        "description": "50,000+ Montana consumers (excl. payment-only)",
        "section": "§30-14-2803(1)(a)",
    },
    "option_2": {
        "consumer_count": 25_000,
        "revenue_pct": 25,
        "description": "25,000+ consumers AND >25% revenue from sale",
        "section": "§30-14-2803(1)(b)",
    },
}

RESPONSE_DEADLINE_DAYS = 45
EXTENSION_DAYS = 15  # Montana: only 15 days (most states: 45)
MAX_RESPONSE_DAYS = RESPONSE_DEADLINE_DAYS + EXTENSION_DAYS  # 60 days total
APPEAL_RESPONSE_DAYS = 60


@dataclass
class MTDPAApplicability:
    """Assess MTDPA applicability with 50,000-consumer threshold."""
    organization_name: str
    conducts_business_in_montana: bool
    targets_montana_residents: bool
    montana_consumer_count: int
    montana_consumer_count_excl_payment: int
    revenue_from_sale_pct: float
    is_government: bool = False
    is_glba: bool = False
    is_hipaa: bool = False
    is_nonprofit: bool = False
    is_air_carrier: bool = False

    def assess(self) -> dict:
        exemptions = []
        if self.is_government:
            exemptions.append({"name": "Government entity", "section": "§30-14-2805(1)"})
        if self.is_glba:
            exemptions.append({"name": "GLBA institution", "section": "§30-14-2805(2)"})
        if self.is_hipaa:
            exemptions.append({"name": "HIPAA covered entity/BA", "section": "§30-14-2805(3)"})
        if self.is_nonprofit:
            exemptions.append({"name": "Nonprofit organization", "section": "§30-14-2805(4)"})
        if self.is_air_carrier:
            exemptions.append({"name": "Air carrier", "section": "§30-14-2805(6)"})

        if exemptions:
            return {"organization": self.organization_name, "applicable": False, "exemptions": exemptions}

        if not (self.conducts_business_in_montana or self.targets_montana_residents):
            return {"organization": self.organization_name, "applicable": False, "reason": "No Montana nexus"}

        thresholds_met = []
        if self.montana_consumer_count_excl_payment >= 50_000:
            thresholds_met.append(MTDPA_THRESHOLDS["option_1"])
        if self.montana_consumer_count_excl_payment >= 25_000 and self.revenue_from_sale_pct > 25:
            thresholds_met.append(MTDPA_THRESHOLDS["option_2"])

        return {
            "organization": self.organization_name,
            "applicable": len(thresholds_met) > 0,
            "thresholds_met": thresholds_met,
            "note": "Montana has the lowest consumer threshold (50,000) among state privacy laws",
            "assessment_date": datetime.now(timezone.utc).isoformat(),
        }


@dataclass
class MTDPAConsumerRequest:
    """Track MTDPA consumer request with shorter extension period."""
    request_id: str
    right: MTDPARight
    consumer_id: str
    received_date: str
    status: str = "received"
    extension_granted: bool = False
    completed_date: Optional[str] = None

    @property
    def response_deadline(self) -> str:
        received = datetime.fromisoformat(self.received_date)
        days = MAX_RESPONSE_DAYS if self.extension_granted else RESPONSE_DEADLINE_DAYS
        return (received + timedelta(days=days)).isoformat()

    @property
    def days_remaining(self) -> int:
        deadline = datetime.fromisoformat(self.response_deadline)
        return (deadline - datetime.now(timezone.utc)).days

    def to_dict(self) -> dict:
        return {
            "request_id": self.request_id,
            "right": self.right.value,
            "consumer_id": self.consumer_id,
            "status": self.status,
            "received_date": self.received_date,
            "response_deadline": self.response_deadline,
            "days_remaining": self.days_remaining,
            "extension_granted": self.extension_granted,
            "max_total_days": MAX_RESPONSE_DAYS,
            "note": f"Montana allows only {EXTENSION_DAYS}-day extension (total {MAX_RESPONSE_DAYS} days), shorter than most states' 90-day maximum",
        }


def compare_thresholds() -> list[dict]:
    """Compare consumer thresholds across state privacy laws."""
    return [
        {"state": "Montana (MTDPA)", "threshold_1": "50,000", "threshold_2": "25,000 + 25% revenue", "effective": "Oct 1, 2024"},
        {"state": "Virginia (VCDPA)", "threshold_1": "100,000", "threshold_2": "25,000 + 50% revenue", "effective": "Jan 1, 2023"},
        {"state": "Colorado (CPA)", "threshold_1": "100,000", "threshold_2": "25,000 + revenue from sale", "effective": "Jul 1, 2023"},
        {"state": "Connecticut (CTDPA)", "threshold_1": "100,000", "threshold_2": "25,000 + 25% revenue", "effective": "Jul 1, 2023"},
        {"state": "Oregon (OCPA)", "threshold_1": "100,000", "threshold_2": "25,000 + 25% revenue", "effective": "Jul 1, 2024"},
        {"state": "Texas (TDPSA)", "threshold_1": "N/A (non-SBA)", "threshold_2": "N/A", "effective": "Jul 1, 2024"},
        {"state": "California (CCPA/CPRA)", "threshold_1": "100,000", "threshold_2": "$25M revenue OR 50% revenue", "effective": "Jan 1, 2020/2023"},
    ]


if __name__ == "__main__":
    # Applicability
    print("=== MTDPA Applicability Assessment ===")
    assessment = MTDPAApplicability(
        organization_name="Liberty Commerce Inc.",
        conducts_business_in_montana=True,
        targets_montana_residents=True,
        montana_consumer_count=28_000,
        montana_consumer_count_excl_payment=28_000,
        revenue_from_sale_pct=12.0,
    )
    print(json.dumps(assessment.assess(), indent=2))

    # Consumer request with shorter extension
    print("\n=== Consumer Request (Shorter Extension) ===")
    request = MTDPAConsumerRequest(
        request_id="MT-REQ-2026-00019",
        right=MTDPARight.DELETE,
        consumer_id="MT-CONS-5b7a",
        received_date="2026-03-01T10:00:00+00:00",
        extension_granted=True,
    )
    print(json.dumps(request.to_dict(), indent=2))

    # Threshold comparison
    print("\n=== State Threshold Comparison ===")
    for entry in compare_thresholds():
        print(f"  {entry['state']}: {entry['threshold_1']} | {entry['threshold_2']}")
