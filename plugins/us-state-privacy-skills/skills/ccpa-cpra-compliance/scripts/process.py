#!/usr/bin/env python3
"""
CCPA/CPRA Compliance Assessment and Consumer Request Tracker

Assesses business applicability under Cal. Civ. Code §1798.140(d),
tracks consumer request metrics per CPPA Regulations §7101, and
generates compliance status reports.
"""

import json
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class RequestType(Enum):
    KNOW_CATEGORIES = "know_categories"
    KNOW_SPECIFIC = "know_specific_pieces"
    DELETE = "delete"
    CORRECT = "correct"
    OPT_OUT_SALE_SHARING = "opt_out_sale_sharing"
    LIMIT_SENSITIVE_PI = "limit_sensitive_pi"


class RequestStatus(Enum):
    RECEIVED = "received"
    VERIFIED = "verified"
    IN_PROGRESS = "in_progress"
    FULFILLED = "fulfilled"
    PARTIALLY_FULFILLED = "partially_fulfilled"
    DENIED = "denied"
    EXTENSION = "extension"


APPLICABILITY_THRESHOLDS = {
    "revenue": 25_000_000,
    "consumer_count": 100_000,
    "revenue_from_sale_pct": 50,
}

RESPONSE_DEADLINE_DAYS = 45
EXTENSION_DAYS = 45
MAX_RESPONSE_DAYS = RESPONSE_DEADLINE_DAYS + EXTENSION_DAYS  # 90 days

VERIFICATION_REQUIREMENTS = {
    RequestType.KNOW_CATEGORIES: {"data_points": 2, "description": "Match at least two data points"},
    RequestType.KNOW_SPECIFIC: {"data_points": 3, "description": "Match at least three data points plus signed declaration under penalty of perjury"},
    RequestType.DELETE: {"data_points": 2, "description": "Match at least two data points"},
    RequestType.CORRECT: {"data_points": 2, "description": "Match at least two data points"},
    RequestType.OPT_OUT_SALE_SHARING: {"data_points": 0, "description": "No verification required beyond reasonable belief"},
    RequestType.LIMIT_SENSITIVE_PI: {"data_points": 0, "description": "No verification required beyond reasonable belief"},
}

SENSITIVE_PI_CATEGORIES = [
    "Social Security number, driver's license number, state ID, or passport number",
    "Account log-in, financial account, debit card, or credit card number with required security/access code",
    "Precise geolocation",
    "Racial or ethnic origin",
    "Religious or philosophical beliefs",
    "Union membership",
    "Contents of mail, email, and text messages (where business is not the intended recipient)",
    "Genetic data",
    "Biometric information for identification purposes",
    "Health information",
    "Sex life or sexual orientation data",
]


@dataclass
class ApplicabilityAssessment:
    """Determines CCPA/CPRA applicability under §1798.140(d)."""
    business_name: str
    does_business_in_california: bool
    annual_gross_revenue: float
    california_consumers_count: int
    revenue_from_sale_sharing_pct: float
    is_for_profit: bool = True

    def assess(self) -> dict:
        if not self.does_business_in_california:
            return {
                "applicable": False,
                "reason": "Business does not do business in California",
                "thresholds_met": [],
            }

        if not self.is_for_profit:
            return {
                "applicable": False,
                "reason": "CCPA/CPRA applies only to for-profit entities (§1798.140(d))",
                "thresholds_met": [],
            }

        thresholds_met = []

        if self.annual_gross_revenue > APPLICABILITY_THRESHOLDS["revenue"]:
            thresholds_met.append({
                "threshold": "revenue",
                "description": f"Annual gross revenue (${self.annual_gross_revenue:,.0f}) exceeds ${APPLICABILITY_THRESHOLDS['revenue']:,}",
                "section": "§1798.140(d)(1)(A)",
            })

        if self.california_consumers_count >= APPLICABILITY_THRESHOLDS["consumer_count"]:
            thresholds_met.append({
                "threshold": "consumer_count",
                "description": f"Processes PI of {self.california_consumers_count:,} consumers (threshold: {APPLICABILITY_THRESHOLDS['consumer_count']:,})",
                "section": "§1798.140(d)(1)(B)",
            })

        if self.revenue_from_sale_sharing_pct >= APPLICABILITY_THRESHOLDS["revenue_from_sale_pct"]:
            thresholds_met.append({
                "threshold": "revenue_from_sale_sharing",
                "description": f"Derives {self.revenue_from_sale_sharing_pct}% of revenue from selling/sharing PI (threshold: {APPLICABILITY_THRESHOLDS['revenue_from_sale_pct']}%)",
                "section": "§1798.140(d)(1)(C)",
            })

        return {
            "business_name": self.business_name,
            "applicable": len(thresholds_met) > 0,
            "thresholds_met": thresholds_met,
            "thresholds_not_met": [
                t for t in ["revenue", "consumer_count", "revenue_from_sale_sharing"]
                if t not in [m["threshold"] for m in thresholds_met]
            ],
            "assessment_date": datetime.now(timezone.utc).isoformat(),
        }


@dataclass
class ConsumerRequest:
    """Tracks a single consumer privacy request per CCPA/CPRA requirements."""
    request_id: str
    request_type: RequestType
    consumer_id: str
    received_date: str
    status: RequestStatus = RequestStatus.RECEIVED
    verified_date: Optional[str] = None
    completed_date: Optional[str] = None
    extension_granted: bool = False
    extension_reason: Optional[str] = None
    denial_reason: Optional[str] = None
    authorized_agent: bool = False
    agent_authorization_type: Optional[str] = None  # "signed_permission" or "power_of_attorney"

    @property
    def deadline(self) -> str:
        received = datetime.fromisoformat(self.received_date)
        days = MAX_RESPONSE_DAYS if self.extension_granted else RESPONSE_DEADLINE_DAYS
        return (received + timedelta(days=days)).isoformat()

    @property
    def days_elapsed(self) -> int:
        received = datetime.fromisoformat(self.received_date)
        now = datetime.now(timezone.utc)
        return (now - received).days

    @property
    def is_overdue(self) -> bool:
        return datetime.now(timezone.utc) > datetime.fromisoformat(self.deadline)

    def to_dict(self) -> dict:
        return {
            "request_id": self.request_id,
            "request_type": self.request_type.value,
            "consumer_id": self.consumer_id,
            "received_date": self.received_date,
            "status": self.status.value,
            "verified_date": self.verified_date,
            "completed_date": self.completed_date,
            "extension_granted": self.extension_granted,
            "deadline": self.deadline,
            "days_elapsed": self.days_elapsed,
            "is_overdue": self.is_overdue,
            "authorized_agent": self.authorized_agent,
        }


class ComplianceMetrics:
    """Generates annual metrics per CPPA Regulations §7101."""

    def __init__(self, business_name: str, reporting_year: int):
        self.business_name = business_name
        self.reporting_year = reporting_year
        self.requests: list[ConsumerRequest] = []

    def add_request(self, request: ConsumerRequest):
        self.requests.append(request)

    def generate_report(self) -> dict:
        metrics_by_type = {}

        for req_type in RequestType:
            type_requests = [r for r in self.requests if r.request_type == req_type]
            fulfilled = [r for r in type_requests if r.status == RequestStatus.FULFILLED]
            partially = [r for r in type_requests if r.status == RequestStatus.PARTIALLY_FULFILLED]
            denied = [r for r in type_requests if r.status == RequestStatus.DENIED]

            response_days = []
            for r in fulfilled + partially:
                if r.completed_date:
                    received = datetime.fromisoformat(r.received_date)
                    completed = datetime.fromisoformat(r.completed_date)
                    response_days.append((completed - received).days)

            median_days = 0
            if response_days:
                sorted_days = sorted(response_days)
                mid = len(sorted_days) // 2
                median_days = sorted_days[mid] if len(sorted_days) % 2 != 0 else (sorted_days[mid - 1] + sorted_days[mid]) / 2

            metrics_by_type[req_type.value] = {
                "received": len(type_requests),
                "fulfilled_whole_or_part": len(fulfilled) + len(partially),
                "denied": len(denied),
                "median_days_to_respond": median_days,
            }

        return {
            "business_name": self.business_name,
            "reporting_year": self.reporting_year,
            "report_generated": datetime.now(timezone.utc).isoformat(),
            "total_requests": len(self.requests),
            "metrics_by_type": metrics_by_type,
            "regulation_reference": "CPPA Regulations §7101",
        }


def generate_privacy_notice_checklist() -> list[dict]:
    """Generate privacy notice content checklist per §1798.100(a) and §1798.130(a)(5)."""
    return [
        {"id": 1, "item": "Categories of PI collected in preceding 12 months", "section": "§1798.100(a)(1)", "status": ""},
        {"id": 2, "item": "Categories of sensitive PI collected", "section": "§1798.100(a)(1)", "status": ""},
        {"id": 3, "item": "Purposes for which each PI category is collected/used", "section": "§1798.100(a)(1)", "status": ""},
        {"id": 4, "item": "Whether PI is sold or shared, per category", "section": "§1798.100(a)(1)", "status": ""},
        {"id": 5, "item": "Retention period or criteria for each PI category", "section": "§1798.100(a)(3)", "status": ""},
        {"id": 6, "item": "Categories of sources of PI", "section": "§1798.110(c)(2)", "status": ""},
        {"id": 7, "item": "Categories of third parties to which PI is disclosed", "section": "§1798.110(c)(4)", "status": ""},
        {"id": 8, "item": "Consumer request submission instructions", "section": "§1798.130(a)(1)", "status": ""},
        {"id": 9, "item": "Two or more methods for submitting requests", "section": "§1798.130(a)(1)", "status": ""},
        {"id": 10, "item": "Do Not Sell or Share link on homepage", "section": "§1798.135(a)(1)", "status": ""},
        {"id": 11, "item": "Limit Use of Sensitive PI link (if applicable)", "section": "§1798.135(a)(2)", "status": ""},
        {"id": 12, "item": "Notice of financial incentive programs (if applicable)", "section": "§1798.125(b)(2)", "status": ""},
        {"id": 13, "item": "Date of last update", "section": "CPPA Regs §7011(e)", "status": ""},
        {"id": 14, "item": "Annual metrics (if 10M+ consumers)", "section": "CPPA Regs §7101", "status": ""},
    ]


if __name__ == "__main__":
    # Demonstrate applicability assessment for Liberty Commerce Inc.
    assessment = ApplicabilityAssessment(
        business_name="Liberty Commerce Inc.",
        does_business_in_california=True,
        annual_gross_revenue=48_000_000,
        california_consumers_count=320_000,
        revenue_from_sale_sharing_pct=12.0,
        is_for_profit=True,
    )

    result = assessment.assess()
    print("=== CCPA/CPRA Applicability Assessment ===")
    print(json.dumps(result, indent=2))

    # Demonstrate consumer request tracking
    print("\n=== Consumer Request Tracking ===")
    request = ConsumerRequest(
        request_id="REQ-2026-00142",
        request_type=RequestType.DELETE,
        consumer_id="CONS-7f3a9b2e",
        received_date="2026-03-01T14:30:00+00:00",
        status=RequestStatus.IN_PROGRESS,
        verified_date="2026-03-03T09:15:00+00:00",
    )
    print(json.dumps(request.to_dict(), indent=2))

    verification = VERIFICATION_REQUIREMENTS[request.request_type]
    print(f"\nVerification requirement: {verification['description']}")
    print(f"Data points to match: {verification['data_points']}")

    # Demonstrate annual metrics
    print("\n=== Annual Metrics Report ===")
    metrics = ComplianceMetrics("Liberty Commerce Inc.", 2025)

    sample_requests = [
        ConsumerRequest("REQ-001", RequestType.KNOW_CATEGORIES, "C001", "2025-02-15T10:00:00+00:00",
                        RequestStatus.FULFILLED, completed_date="2025-03-01T10:00:00+00:00"),
        ConsumerRequest("REQ-002", RequestType.DELETE, "C002", "2025-03-01T10:00:00+00:00",
                        RequestStatus.FULFILLED, completed_date="2025-03-20T10:00:00+00:00"),
        ConsumerRequest("REQ-003", RequestType.OPT_OUT_SALE_SHARING, "C003", "2025-04-10T10:00:00+00:00",
                        RequestStatus.FULFILLED, completed_date="2025-04-11T10:00:00+00:00"),
        ConsumerRequest("REQ-004", RequestType.KNOW_SPECIFIC, "C004", "2025-05-01T10:00:00+00:00",
                        RequestStatus.DENIED, denial_reason="Unable to verify identity"),
        ConsumerRequest("REQ-005", RequestType.LIMIT_SENSITIVE_PI, "C005", "2025-06-15T10:00:00+00:00",
                        RequestStatus.FULFILLED, completed_date="2025-06-16T10:00:00+00:00"),
        ConsumerRequest("REQ-006", RequestType.CORRECT, "C006", "2025-07-01T10:00:00+00:00",
                        RequestStatus.FULFILLED, completed_date="2025-07-25T10:00:00+00:00"),
    ]

    for req in sample_requests:
        metrics.add_request(req)

    report = metrics.generate_report()
    print(json.dumps(report, indent=2))

    # Privacy notice checklist
    print("\n=== Privacy Notice Checklist ===")
    checklist = generate_privacy_notice_checklist()
    for item in checklist:
        print(f"  [{item['status'] or ' '}] {item['id']}. {item['item']} ({item['section']})")
