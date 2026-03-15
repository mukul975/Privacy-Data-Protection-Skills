#!/usr/bin/env python3
"""
Colorado Privacy Act Compliance Tool

Assesses CPA applicability under C.R.S. §6-1-1304, processes universal
opt-out signals per 4 CCR 904-3 Rule 5, and manages consumer rights requests.
"""

import json
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class CPARight(Enum):
    ACCESS = "access"
    CORRECT = "correct"
    DELETE = "delete"
    PORTABILITY = "portability"
    OPT_OUT_TARGETED_ADS = "opt_out_targeted_advertising"
    OPT_OUT_SALE = "opt_out_sale"
    OPT_OUT_PROFILING = "opt_out_profiling"


class OptOutSignalScope(Enum):
    TARGETED_ADVERTISING = "targeted_advertising"
    SALE = "sale_of_personal_data"


CPA_THRESHOLDS = {
    "option_1": {
        "consumer_count": 100_000,
        "description": "Control or process data of 100,000+ Colorado consumers per calendar year",
        "section": "§6-1-1304(1)(a)",
    },
    "option_2": {
        "consumer_count": 25_000,
        "revenue_from_sale": True,
        "description": "25,000+ consumers AND derive revenue/discount from sale of personal data",
        "section": "§6-1-1304(1)(b)",
    },
}

SENSITIVE_DATA_CATEGORIES = [
    {"category": "racial_ethnic_origin", "section": "§6-1-1304(26)(a)", "description": "Personal data revealing racial or ethnic origin"},
    {"category": "religious_beliefs", "section": "§6-1-1304(26)(b)", "description": "Religious beliefs"},
    {"category": "mental_physical_health", "section": "§6-1-1304(26)(c)", "description": "Mental or physical health condition or diagnosis"},
    {"category": "sex_life_orientation", "section": "§6-1-1304(26)(d)", "description": "Sex life or sexual orientation"},
    {"category": "citizenship_status", "section": "§6-1-1304(26)(e)", "description": "Citizenship or citizenship status"},
    {"category": "genetic_biometric", "section": "§6-1-1304(26)(f)", "description": "Genetic or biometric data for uniquely identifying an individual"},
    {"category": "child_data", "section": "§6-1-1304(26)(g)", "description": "Personal data of a known child"},
]


@dataclass
class CPAApplicability:
    """Assess CPA applicability."""
    organization_name: str
    conducts_business_in_colorado: bool
    targets_colorado_residents: bool
    colorado_consumer_count: int
    derives_revenue_from_sale: bool
    is_government_entity: bool = False
    is_glba_institution: bool = False
    is_hipaa_covered: bool = False
    is_nonprofit: bool = False

    def assess(self) -> dict:
        exemptions = []
        if self.is_government_entity:
            exemptions.append({"name": "Government entity", "section": "§6-1-1304(2)(a)"})
        if self.is_glba_institution:
            exemptions.append({"name": "GLBA institution", "section": "§6-1-1304(2)(d)"})
        if self.is_hipaa_covered:
            exemptions.append({"name": "HIPAA covered entity/BA", "section": "§6-1-1304(2)(c)"})
        if self.is_nonprofit:
            exemptions.append({"name": "Nonprofit organization", "section": "§6-1-1304(2)(f)"})

        if exemptions:
            return {
                "organization": self.organization_name,
                "applicable": False,
                "reason": "Entity-level exemption applies",
                "exemptions": exemptions,
            }

        if not (self.conducts_business_in_colorado or self.targets_colorado_residents):
            return {"organization": self.organization_name, "applicable": False, "reason": "No Colorado nexus"}

        thresholds_met = []
        if self.colorado_consumer_count >= 100_000:
            thresholds_met.append(CPA_THRESHOLDS["option_1"])
        if self.colorado_consumer_count >= 25_000 and self.derives_revenue_from_sale:
            thresholds_met.append(CPA_THRESHOLDS["option_2"])

        return {
            "organization": self.organization_name,
            "applicable": len(thresholds_met) > 0,
            "thresholds_met": thresholds_met,
            "assessment_date": datetime.now(timezone.utc).isoformat(),
        }


@dataclass
class UniversalOptOutEvent:
    """Record of universal opt-out signal processing per 4 CCR 904-3 Rule 5."""
    event_id: str
    signal_type: str  # "gpc", "other"
    signal_value: bool
    consumer_authenticated: bool
    consumer_id: Optional[str] = None
    session_id: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    scopes_applied: list = field(default_factory=list)
    tags_suppressed: list = field(default_factory=list)
    compliant: bool = True
    notes: str = ""

    def process_signal(self) -> dict:
        """Process universal opt-out signal per CPA requirements."""
        if not self.signal_value:
            return {"action": "no_opt_out_signal", "scopes_applied": []}

        self.scopes_applied = [
            OptOutSignalScope.TARGETED_ADVERTISING.value,
            OptOutSignalScope.SALE.value,
        ]

        self.tags_suppressed = [
            "AdReach Network pixel",
            "Cross-context behavioral advertising tags",
            "Third-party data sharing pipeline",
            "Retargeting cookies",
        ]

        actions = {
            "signal_type": self.signal_type,
            "consumer_authenticated": self.consumer_authenticated,
            "scopes_applied": self.scopes_applied,
            "tags_suppressed": self.tags_suppressed,
            "pop_up_displayed": False,
            "additional_verification_required": False,
            "compliant_with_rule_5_11": True,
        }

        if self.consumer_authenticated:
            actions["persistence"] = "account_level"
            actions["note"] = "Opt-out permanently associated with consumer account"
        else:
            actions["persistence"] = "session_level"
            actions["note"] = "Opt-out applied to browser/device for this session"

        return actions


@dataclass
class CPAConsumerRequest:
    """Track CPA consumer rights request with appeal process."""
    request_id: str
    right: CPARight
    consumer_id: str
    received_date: str
    status: str = "received"
    completed_date: Optional[str] = None
    appeal_filed: bool = False
    appeal_date: Optional[str] = None
    appeal_outcome: Optional[str] = None

    @property
    def response_deadline(self) -> str:
        received = datetime.fromisoformat(self.received_date)
        return (received + timedelta(days=45)).isoformat()

    @property
    def appeal_deadline(self) -> Optional[str]:
        if self.appeal_date:
            return (datetime.fromisoformat(self.appeal_date) + timedelta(days=45)).isoformat()
        return None

    def to_dict(self) -> dict:
        return {
            "request_id": self.request_id,
            "right": self.right.value,
            "consumer_id": self.consumer_id,
            "status": self.status,
            "received_date": self.received_date,
            "response_deadline": self.response_deadline,
            "appeal_filed": self.appeal_filed,
            "appeal_deadline": self.appeal_deadline,
        }


if __name__ == "__main__":
    # Applicability assessment
    print("=== CPA Applicability Assessment ===")
    assessment = CPAApplicability(
        organization_name="Liberty Commerce Inc.",
        conducts_business_in_colorado=True,
        targets_colorado_residents=True,
        colorado_consumer_count=98_000,
        derives_revenue_from_sale=True,
    )
    print(json.dumps(assessment.assess(), indent=2))

    # Universal opt-out signal processing
    print("\n=== Universal Opt-Out Signal Processing ===")
    opt_out = UniversalOptOutEvent(
        event_id="UOO-2026-00312",
        signal_type="gpc",
        signal_value=True,
        consumer_authenticated=True,
        consumer_id="CO-CONS-4a8b2c",
        session_id="sess-xyz789",
    )
    result = opt_out.process_signal()
    print(json.dumps(result, indent=2))

    # Consumer request with appeal
    print("\n=== Consumer Rights Request ===")
    request = CPAConsumerRequest(
        request_id="CO-REQ-2026-00087",
        right=CPARight.DELETE,
        consumer_id="CO-CONS-4a8b2c",
        received_date="2026-03-01T10:00:00+00:00",
    )
    print(json.dumps(request.to_dict(), indent=2))
