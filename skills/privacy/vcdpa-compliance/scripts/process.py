#!/usr/bin/env python3
"""
VCDPA Compliance Assessment Tool

Assesses applicability under Va. Code §59.1-576, tracks consumer rights
requests, evaluates sensitive data consent requirements, and generates
DPIA templates per §59.1-580.
"""

import json
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class VCDPARight(Enum):
    ACCESS = "access"
    CORRECT = "correct"
    DELETE = "delete"
    PORTABILITY = "portability"
    OPT_OUT_TARGETED_ADS = "opt_out_targeted_advertising"
    OPT_OUT_SALE = "opt_out_sale"
    OPT_OUT_PROFILING = "opt_out_profiling"


class SensitiveDataCategory(Enum):
    RACIAL_ETHNIC = "racial_ethnic_origin"
    RELIGIOUS = "religious_beliefs"
    HEALTH = "mental_physical_health_diagnosis"
    SEXUAL_ORIENTATION = "sexual_orientation"
    CITIZENSHIP = "citizenship_immigration_status"
    GENETIC_BIOMETRIC = "genetic_biometric_for_identification"
    PRECISE_GEOLOCATION = "precise_geolocation"
    CHILD_DATA = "known_child_personal_data"


VCDPA_THRESHOLDS = {
    "option_1": {"consumer_count": 100_000, "description": "Control or process data of 100,000+ Virginia consumers"},
    "option_2": {"consumer_count": 25_000, "revenue_pct": 50, "description": "25,000+ consumers AND >50% revenue from sale of personal data"},
}

ENTITY_EXEMPTIONS = [
    {"name": "Virginia government entity", "section": "§59.1-576(B)(1)", "basis": "State/local government bodies"},
    {"name": "GLBA-covered financial institution", "section": "§59.1-576(B)(2)", "basis": "Subject to Title V of Gramm-Leach-Bliley Act (15 U.S.C. §6801 et seq.)"},
    {"name": "HIPAA covered entity/business associate", "section": "§59.1-576(B)(3)", "basis": "Subject to HIPAA (42 U.S.C. §1320d et seq.)"},
    {"name": "Nonprofit organization", "section": "§59.1-576(B)(4)", "basis": "Tax-exempt under IRC §501(c)(3) or §501(c)(6)"},
    {"name": "Institution of higher education", "section": "§59.1-576(B)(5)", "basis": "Public or private institution of higher education"},
]

DPIA_TRIGGERS = [
    {"trigger": "Targeted advertising", "section": "§59.1-580(A)(1)", "required": True},
    {"trigger": "Sale of personal data", "section": "§59.1-580(A)(2)", "required": True},
    {"trigger": "Profiling with risk of significant effects", "section": "§59.1-580(A)(3)", "required": True},
    {"trigger": "Sensitive data processing", "section": "§59.1-580(A)(4)", "required": True},
    {"trigger": "Other heightened risk processing", "section": "§59.1-580(A)(5)", "required": True},
]


@dataclass
class VCDPAApplicability:
    """Assess VCDPA applicability for an organization."""
    organization_name: str
    conducts_business_in_virginia: bool
    targets_virginia_residents: bool
    virginia_consumer_count: int
    revenue_from_data_sale_pct: float
    is_government_entity: bool = False
    is_glba_institution: bool = False
    is_hipaa_covered: bool = False
    is_nonprofit: bool = False
    is_higher_education: bool = False

    def assess(self) -> dict:
        # Check entity-level exemptions first
        exemptions = []
        if self.is_government_entity:
            exemptions.append(ENTITY_EXEMPTIONS[0])
        if self.is_glba_institution:
            exemptions.append(ENTITY_EXEMPTIONS[1])
        if self.is_hipaa_covered:
            exemptions.append(ENTITY_EXEMPTIONS[2])
        if self.is_nonprofit:
            exemptions.append(ENTITY_EXEMPTIONS[3])
        if self.is_higher_education:
            exemptions.append(ENTITY_EXEMPTIONS[4])

        if exemptions:
            return {
                "organization": self.organization_name,
                "applicable": False,
                "reason": "Entity-level exemption applies",
                "exemptions": exemptions,
                "assessment_date": datetime.now(timezone.utc).isoformat(),
            }

        if not (self.conducts_business_in_virginia or self.targets_virginia_residents):
            return {
                "organization": self.organization_name,
                "applicable": False,
                "reason": "Does not conduct business in Virginia or target Virginia residents",
                "assessment_date": datetime.now(timezone.utc).isoformat(),
            }

        thresholds_met = []
        if self.virginia_consumer_count >= 100_000:
            thresholds_met.append({
                "threshold": "option_1",
                "description": f"Processes data of {self.virginia_consumer_count:,} Virginia consumers (≥100,000)",
                "section": "§59.1-576(A)(1)",
            })

        if self.virginia_consumer_count >= 25_000 and self.revenue_from_data_sale_pct > 50:
            thresholds_met.append({
                "threshold": "option_2",
                "description": f"Processes data of {self.virginia_consumer_count:,} consumers (≥25,000) and {self.revenue_from_data_sale_pct}% revenue from sale (>50%)",
                "section": "§59.1-576(A)(2)",
            })

        return {
            "organization": self.organization_name,
            "applicable": len(thresholds_met) > 0,
            "thresholds_met": thresholds_met,
            "assessment_date": datetime.now(timezone.utc).isoformat(),
        }


@dataclass
class ConsumerRightsRequest:
    """Track a VCDPA consumer rights request."""
    request_id: str
    right: VCDPARight
    consumer_id: str
    received_date: str
    status: str = "received"
    authenticated: bool = False
    completed_date: Optional[str] = None
    appeal_filed: bool = False
    appeal_date: Optional[str] = None
    appeal_response_date: Optional[str] = None

    @property
    def response_deadline(self) -> str:
        received = datetime.fromisoformat(self.received_date)
        return (received + timedelta(days=45)).isoformat()

    @property
    def appeal_deadline(self) -> Optional[str]:
        if self.appeal_date:
            appeal = datetime.fromisoformat(self.appeal_date)
            return (appeal + timedelta(days=60)).isoformat()
        return None

    def to_dict(self) -> dict:
        return {
            "request_id": self.request_id,
            "right": self.right.value,
            "consumer_id": self.consumer_id,
            "received_date": self.received_date,
            "status": self.status,
            "response_deadline": self.response_deadline,
            "appeal_filed": self.appeal_filed,
            "appeal_deadline": self.appeal_deadline,
        }


@dataclass
class SensitiveDataConsent:
    """Record of sensitive data processing consent under §59.1-578(A)(5)."""
    consumer_id: str
    category: SensitiveDataCategory
    purpose: str
    consent_granted: bool
    consent_text_version: str
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    mechanism: str = "checkbox_tick"
    withdrawn: bool = False
    withdrawal_date: Optional[str] = None

    def to_dict(self) -> dict:
        result = asdict(self)
        result["category"] = self.category.value
        return result


@dataclass
class DPIARecord:
    """Data Protection Impact Assessment record per §59.1-580."""
    dpia_id: str
    processing_activity: str
    trigger: str
    trigger_section: str
    description: str
    data_categories: list
    consumer_categories: list
    benefits: list
    risks: list
    mitigation_measures: list
    assessment_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    reviewer: str = ""
    approved: bool = False
    next_review_date: str = ""

    def risk_score(self) -> str:
        high_risk_keywords = ["discrimination", "financial injury", "physical harm", "surveillance", "disparate impact"]
        risk_text = " ".join(str(r) for r in self.risks).lower()
        high_count = sum(1 for kw in high_risk_keywords if kw in risk_text)
        if high_count >= 2:
            return "HIGH"
        elif high_count == 1:
            return "MEDIUM"
        return "LOW"

    def to_dict(self) -> dict:
        result = asdict(self)
        result["risk_score"] = self.risk_score()
        return result


def generate_privacy_notice_checklist() -> list[dict]:
    """Generate VCDPA privacy notice compliance checklist per §59.1-578(B)."""
    return [
        {"id": 1, "item": "Categories of personal data processed", "section": "§59.1-578(B)(1)", "status": ""},
        {"id": 2, "item": "Purpose for processing each category", "section": "§59.1-578(B)(2)", "status": ""},
        {"id": 3, "item": "How consumers may exercise rights", "section": "§59.1-578(B)(3)", "status": ""},
        {"id": 4, "item": "Instructions for appeal process", "section": "§59.1-578(B)(3)", "status": ""},
        {"id": 5, "item": "Categories of data shared with third parties", "section": "§59.1-578(B)(4)", "status": ""},
        {"id": 6, "item": "Categories of third parties", "section": "§59.1-578(B)(5)", "status": ""},
        {"id": 7, "item": "Active email or online contact mechanism", "section": "§59.1-578(B)(6)", "status": ""},
        {"id": 8, "item": "Whether personal data is sold", "section": "§59.1-578(B)", "status": ""},
        {"id": 9, "item": "Whether targeted advertising is conducted", "section": "§59.1-578(B)", "status": ""},
        {"id": 10, "item": "Whether profiling is conducted", "section": "§59.1-578(B)", "status": ""},
    ]


if __name__ == "__main__":
    # Demonstrate applicability assessment
    print("=== VCDPA Applicability Assessment ===")
    assessment = VCDPAApplicability(
        organization_name="Liberty Commerce Inc.",
        conducts_business_in_virginia=True,
        targets_virginia_residents=True,
        virginia_consumer_count=145_000,
        revenue_from_data_sale_pct=12.0,
    )
    result = assessment.assess()
    print(json.dumps(result, indent=2))

    # Demonstrate consumer request tracking
    print("\n=== Consumer Rights Request ===")
    request = ConsumerRightsRequest(
        request_id="VA-REQ-2026-00041",
        right=VCDPARight.DELETE,
        consumer_id="VA-CONS-8a2b4c",
        received_date="2026-03-01T10:00:00+00:00",
        authenticated=True,
    )
    print(json.dumps(request.to_dict(), indent=2))

    # Demonstrate sensitive data consent
    print("\n=== Sensitive Data Consent ===")
    consent = SensitiveDataConsent(
        consumer_id="VA-CONS-8a2b4c",
        category=SensitiveDataCategory.PRECISE_GEOLOCATION,
        purpose="Delivery tracking and store finder functionality",
        consent_granted=True,
        consent_text_version="v2.1-sha256abc",
        mechanism="checkbox_tick",
    )
    print(json.dumps(consent.to_dict(), indent=2))

    # Demonstrate DPIA
    print("\n=== Data Protection Impact Assessment ===")
    dpia = DPIARecord(
        dpia_id="DPIA-VA-2026-003",
        processing_activity="Targeted advertising via AdReach Network",
        trigger="Targeted advertising",
        trigger_section="§59.1-580(A)(1)",
        description="Processing of browsing history, purchase patterns, and device identifiers to deliver targeted advertisements through AdReach Network partnership",
        data_categories=["browsing_history", "purchase_patterns", "device_identifiers", "IP_address"],
        consumer_categories=["Virginia e-commerce customers"],
        benefits=["Revenue generation from advertising", "Relevant product recommendations for consumers"],
        risks=["Profiling may create filter bubbles", "Potential for discrimination in ad targeting based on inferred characteristics"],
        mitigation_measures=["Opt-out mechanism for targeted advertising", "Prohibition on use of sensitive data for targeting", "Annual bias audit of advertising algorithms"],
        reviewer="Robert Kim, DPO",
        approved=True,
        next_review_date="2027-03-01",
    )
    print(json.dumps(dpia.to_dict(), indent=2))

    # Privacy notice checklist
    print("\n=== Privacy Notice Checklist ===")
    checklist = generate_privacy_notice_checklist()
    for item in checklist:
        print(f"  [ ] {item['id']}. {item['item']} ({item['section']})")
