#!/usr/bin/env python3
"""
California Consumer Rights Request Processing Engine

Manages the lifecycle of consumer privacy requests under CCPA/CPRA,
including identity verification, exception handling, and response tracking.
"""

import json
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class RightType(Enum):
    KNOW_CATEGORIES = "know_categories"
    KNOW_SPECIFIC = "know_specific_pieces"
    DELETE = "delete"
    CORRECT = "correct"
    OPT_OUT = "opt_out_sale_sharing"
    LIMIT_SENSITIVE = "limit_sensitive_pi"


class VerificationLevel(Enum):
    NONE = "none"
    STANDARD = "standard_2_points"
    HEIGHTENED = "heightened_3_points_declaration"


class RequestChannel(Enum):
    WEB_PORTAL = "web_portal"
    EMAIL = "email"
    TOLL_FREE = "toll_free"
    MAIL = "postal_mail"
    IN_STORE = "in_store"
    AUTHORIZED_AGENT = "authorized_agent"


VERIFICATION_MAP = {
    RightType.KNOW_CATEGORIES: VerificationLevel.STANDARD,
    RightType.KNOW_SPECIFIC: VerificationLevel.HEIGHTENED,
    RightType.DELETE: VerificationLevel.STANDARD,
    RightType.CORRECT: VerificationLevel.STANDARD,
    RightType.OPT_OUT: VerificationLevel.NONE,
    RightType.LIMIT_SENSITIVE: VerificationLevel.NONE,
}

RESPONSE_DEADLINES = {
    RightType.KNOW_CATEGORIES: 45,
    RightType.KNOW_SPECIFIC: 45,
    RightType.DELETE: 45,
    RightType.CORRECT: 45,
    RightType.OPT_OUT: 15,  # 15 business days
    RightType.LIMIT_SENSITIVE: 15,  # 15 business days
}

DELETION_EXCEPTIONS = [
    {
        "id": "DEX-01",
        "section": "§1798.105(d)(1)",
        "description": "Complete the transaction for which the PI was collected",
        "example": "Open order, pending return, active subscription",
    },
    {
        "id": "DEX-02",
        "section": "§1798.105(d)(2)",
        "description": "Detect security incidents; protect against malicious, deceptive, fraudulent, or illegal activity; prosecute responsible persons",
        "example": "Active fraud investigation, account compromise case",
    },
    {
        "id": "DEX-03",
        "section": "§1798.105(d)(3)",
        "description": "Debug to identify and repair errors that impair existing intended functionality",
        "example": "Error logs needed for ongoing software debugging",
    },
    {
        "id": "DEX-04",
        "section": "§1798.105(d)(4)",
        "description": "Exercise free speech, ensure another consumer's exercise of free speech, or exercise another right provided for by law",
        "example": "Product review authored by consumer, publicly posted content",
    },
    {
        "id": "DEX-05",
        "section": "§1798.105(d)(5)",
        "description": "Comply with the California Electronic Communications Privacy Act (Cal. Penal Code §1546 et seq.)",
        "example": "Electronic communications subject to legal process",
    },
    {
        "id": "DEX-06",
        "section": "§1798.105(d)(6)",
        "description": "Engage in public or peer-reviewed scientific, historical, or statistical research in the public interest",
        "example": "Anonymized data in published research dataset",
    },
    {
        "id": "DEX-07",
        "section": "§1798.105(d)(7)",
        "description": "Enable solely internal uses reasonably aligned with consumer expectations based on the consumer's relationship with the business",
        "example": "Purchase history for product recall notifications",
    },
    {
        "id": "DEX-08",
        "section": "§1798.105(d)(8)",
        "description": "Comply with a legal obligation",
        "example": "Tax records per 26 U.S.C. §6001 (7-year retention), litigation hold",
    },
    {
        "id": "DEX-09",
        "section": "§1798.105(d)(9)",
        "description": "Otherwise use the consumer's PI, internally, in a lawful manner that is compatible with the context in which the consumer provided the information",
        "example": "Warranty records for duration of warranty period",
    },
]


@dataclass
class VerificationResult:
    """Result of consumer identity verification."""
    verified: bool
    method: str
    data_points_matched: int
    data_points_required: int
    declaration_signed: bool = False
    verification_timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    notes: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class DeletionExceptionAssessment:
    """Assessment of deletion exceptions for a specific consumer."""
    consumer_id: str
    exceptions_found: list = field(default_factory=list)
    data_to_retain: list = field(default_factory=list)
    data_to_delete: list = field(default_factory=list)
    assessment_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def add_exception(self, exception_id: str, data_category: str, retention_duration: str, justification: str):
        exception_detail = next((e for e in DELETION_EXCEPTIONS if e["id"] == exception_id), None)
        if exception_detail:
            self.exceptions_found.append({
                "exception_id": exception_id,
                "section": exception_detail["section"],
                "description": exception_detail["description"],
                "data_category": data_category,
                "retention_duration": retention_duration,
                "justification": justification,
            })
            self.data_to_retain.append(data_category)

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ConsumerRightsRequest:
    """Full lifecycle tracking for a consumer rights request."""
    request_id: str
    right_type: RightType
    consumer_id: str
    channel: RequestChannel
    received_date: str
    consumer_name: str = ""
    consumer_email: str = ""
    is_authorized_agent: bool = False
    agent_name: Optional[str] = None
    agent_authorization_type: Optional[str] = None
    verification: Optional[VerificationResult] = None
    deletion_exceptions: Optional[DeletionExceptionAssessment] = None
    status: str = "received"
    acknowledged_date: Optional[str] = None
    completed_date: Optional[str] = None
    extension_granted: bool = False
    denial_reason: Optional[str] = None

    @property
    def deadline_days(self) -> int:
        base = RESPONSE_DEADLINES[self.right_type]
        if self.extension_granted and self.right_type not in (RightType.OPT_OUT, RightType.LIMIT_SENSITIVE):
            return base + 45
        return base

    @property
    def deadline_date(self) -> str:
        received = datetime.fromisoformat(self.received_date)
        return (received + timedelta(days=self.deadline_days)).isoformat()

    @property
    def days_remaining(self) -> int:
        deadline = datetime.fromisoformat(self.deadline_date)
        now = datetime.now(timezone.utc)
        return (deadline - now).days

    @property
    def verification_required(self) -> VerificationLevel:
        return VERIFICATION_MAP[self.right_type]

    def verify_identity(self, method: str, data_points_matched: int, declaration_signed: bool = False) -> VerificationResult:
        required = VERIFICATION_MAP[self.right_type]

        if required == VerificationLevel.NONE:
            result = VerificationResult(
                verified=True, method="not_required", data_points_matched=0,
                data_points_required=0, notes="No verification required for opt-out/limit requests"
            )
        elif required == VerificationLevel.STANDARD:
            result = VerificationResult(
                verified=data_points_matched >= 2, method=method,
                data_points_matched=data_points_matched, data_points_required=2,
                notes="Standard verification: 2+ data points required"
            )
        elif required == VerificationLevel.HEIGHTENED:
            result = VerificationResult(
                verified=data_points_matched >= 3 and declaration_signed,
                method=method, data_points_matched=data_points_matched,
                data_points_required=3, declaration_signed=declaration_signed,
                notes="Heightened verification: 3+ data points plus signed declaration under penalty of perjury"
            )
        else:
            result = VerificationResult(
                verified=False, method=method, data_points_matched=data_points_matched,
                data_points_required=0, notes="Unknown verification level"
            )

        self.verification = result
        if result.verified:
            self.status = "verified"
        else:
            self.status = "verification_failed"
        return result

    def to_summary(self) -> dict:
        return {
            "request_id": self.request_id,
            "right_type": self.right_type.value,
            "consumer_id": self.consumer_id,
            "channel": self.channel.value,
            "status": self.status,
            "received_date": self.received_date,
            "deadline_date": self.deadline_date,
            "days_remaining": self.days_remaining,
            "verification_required": self.verification_required.value,
            "verified": self.verification.verified if self.verification else None,
            "extension_granted": self.extension_granted,
            "is_authorized_agent": self.is_authorized_agent,
        }


def generate_deletion_exception_report(assessment: DeletionExceptionAssessment) -> str:
    """Generate human-readable deletion exception report for consumer notification."""
    lines = [
        f"Deletion Exception Report for Consumer: {assessment.consumer_id}",
        f"Assessment Date: {assessment.assessment_date}",
        "",
    ]

    if not assessment.exceptions_found:
        lines.append("No exceptions apply. All personal information will be deleted.")
    else:
        lines.append(f"Exceptions Found: {len(assessment.exceptions_found)}")
        lines.append("")
        for exc in assessment.exceptions_found:
            lines.append(f"  Exception: {exc['exception_id']} ({exc['section']})")
            lines.append(f"  Basis: {exc['description']}")
            lines.append(f"  Data Category: {exc['data_category']}")
            lines.append(f"  Retention Duration: {exc['retention_duration']}")
            lines.append(f"  Justification: {exc['justification']}")
            lines.append("")

    lines.append("Data Categories to Delete:")
    for cat in assessment.data_to_delete:
        lines.append(f"  - {cat}")

    lines.append("")
    lines.append("Data Categories Retained (with exception):")
    for cat in assessment.data_to_retain:
        lines.append(f"  - {cat}")

    return "\n".join(lines)


if __name__ == "__main__":
    # Demonstrate consumer rights request processing
    request = ConsumerRightsRequest(
        request_id="REQ-2026-00247",
        right_type=RightType.DELETE,
        consumer_id="CONS-a8b4c912",
        channel=RequestChannel.WEB_PORTAL,
        received_date="2026-03-01T10:30:00+00:00",
        consumer_name="Jane Doe",
        consumer_email="jane.doe@example.com",
    )

    print("=== Consumer Rights Request ===")
    print(json.dumps(request.to_summary(), indent=2))

    # Verify identity
    print("\n=== Identity Verification ===")
    result = request.verify_identity(
        method="account_reauthentication",
        data_points_matched=2,
    )
    print(json.dumps(result.to_dict(), indent=2))

    # Assess deletion exceptions
    print("\n=== Deletion Exception Assessment ===")
    assessment = DeletionExceptionAssessment(consumer_id="CONS-a8b4c912")
    assessment.add_exception(
        exception_id="DEX-08",
        data_category="Transaction records (invoices, receipts)",
        retention_duration="7 years from transaction date",
        justification="IRS tax record retention per 26 U.S.C. §6001",
    )
    assessment.add_exception(
        exception_id="DEX-01",
        data_category="Shipping information for open order #ORD-98712",
        retention_duration="Until order delivery + 30 days",
        justification="Open order pending shipment, cannot delete until fulfilled",
    )
    assessment.data_to_delete = [
        "Browsing history",
        "Search history",
        "Marketing preferences",
        "Loyalty program profile",
        "Device identifiers",
        "IP address logs",
    ]

    report = generate_deletion_exception_report(assessment)
    print(report)

    # Show all deletion exceptions
    print("\n=== All Available Deletion Exceptions (§1798.105(d)) ===")
    for exc in DELETION_EXCEPTIONS:
        print(f"  {exc['id']}: {exc['section']}")
        print(f"    {exc['description']}")
        print(f"    Example: {exc['example']}")
        print()
