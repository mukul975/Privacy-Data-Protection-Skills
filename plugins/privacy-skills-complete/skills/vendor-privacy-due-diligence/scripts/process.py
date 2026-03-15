#!/usr/bin/env python3
"""
Vendor Privacy Due Diligence — Assessment Engine

Implements vendor privacy risk scoring, questionnaire management,
and sufficiency determination per GDPR Article 28(1).
"""

import json
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class RiskTier(Enum):
    HIGH = "high"
    STANDARD = "standard"
    LOW = "low"


class AssessmentStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    AWAITING_VENDOR = "awaiting_vendor"
    UNDER_REVIEW = "under_review"
    COMPLETED = "completed"


class SufficiencyDecision(Enum):
    APPROVED = "approved"
    CONDITIONALLY_APPROVED = "conditionally_approved"
    REJECTED = "rejected"


class TriggerType(Enum):
    INITIAL = "initial"
    ANNUAL_REASSESSMENT = "annual_reassessment"
    VENDOR_BREACH = "vendor_breach"
    REGULATORY_ACTION = "regulatory_action"
    CERTIFICATION_CHANGE = "certification_change"
    SERVICE_CHANGE = "material_service_change"
    MEDIA_REPORT = "media_report"


SCORING_WEIGHTS = {
    "legal_governance": 0.15,
    "technical_security": 0.25,
    "data_handling": 0.20,
    "certifications": 0.15,
    "breach_history": 0.10,
    "sub_processor_mgmt": 0.10,
    "transfer_safeguards": 0.05,
}

DECISION_THRESHOLDS = {
    SufficiencyDecision.APPROVED: 4.0,
    SufficiencyDecision.CONDITIONALLY_APPROVED: 3.0,
}


@dataclass
class VendorProfile:
    """Prospective or existing vendor being assessed."""
    vendor_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_name: str = ""
    jurisdiction: str = ""
    dpo_name: str = ""
    dpo_contact: str = ""
    processing_locations: list[str] = field(default_factory=list)
    certifications: list[str] = field(default_factory=list)
    sub_processors: list[dict] = field(default_factory=list)
    risk_tier: str = RiskTier.STANDARD.value
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class DataFlowRecord:
    """Documents data flow between controller and vendor."""
    flow_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_id: str = ""
    data_categories: list[str] = field(default_factory=list)
    data_subject_categories: list[str] = field(default_factory=list)
    approximate_volume: int = 0
    transfer_method: str = ""
    encryption_protocol: str = ""
    processing_locations: list[str] = field(default_factory=list)
    retention_period: str = ""
    special_category_data: bool = False


@dataclass
class QuestionnaireResponse:
    """Vendor response to a due diligence questionnaire section."""
    section: str = ""
    question_id: str = ""
    question_text: str = ""
    vendor_response: str = ""
    evidence_provided: bool = False
    evidence_description: str = ""
    score: int = 0  # 1-5
    assessor_notes: str = ""


@dataclass
class DueDiligenceAssessment:
    """Complete due diligence assessment for a vendor."""
    assessment_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_id: str = ""
    trigger: str = TriggerType.INITIAL.value
    status: str = AssessmentStatus.PENDING.value
    initiated_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    questionnaire_sent_date: Optional[str] = None
    questionnaire_received_date: Optional[str] = None
    responses: list[dict] = field(default_factory=list)
    data_flow: Optional[dict] = None
    domain_scores: dict = field(default_factory=dict)
    weighted_score: float = 0.0
    decision: Optional[str] = None
    decision_rationale: str = ""
    conditions: list[str] = field(default_factory=list)
    assessor: str = ""
    approver: str = ""
    completed_date: Optional[str] = None
    next_reassessment_date: Optional[str] = None


class VendorDueDiligenceEngine:
    """
    Manages the vendor privacy due diligence lifecycle.

    Handles vendor profiling, questionnaire management, risk scoring,
    sufficiency determinations, and reassessment scheduling.
    """

    def __init__(self):
        self.vendors: dict[str, VendorProfile] = {}
        self.assessments: list[DueDiligenceAssessment] = []
        self.data_flows: dict[str, DataFlowRecord] = {}

    def register_vendor(self, vendor: VendorProfile) -> str:
        """Register a new vendor for due diligence tracking."""
        self.vendors[vendor.vendor_id] = vendor
        return vendor.vendor_id

    def classify_risk_tier(self, vendor_id: str, data_flow: DataFlowRecord) -> RiskTier:
        """Determine vendor risk tier based on data flow characteristics."""
        risk_factors = 0

        if data_flow.approximate_volume > 10000:
            risk_factors += 2
        elif data_flow.approximate_volume > 1000:
            risk_factors += 1

        if data_flow.special_category_data:
            risk_factors += 3

        eea_countries = {
            "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
            "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
            "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta",
            "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia",
            "Spain", "Sweden", "Iceland", "Liechtenstein", "Norway",
        }
        for location in data_flow.processing_locations:
            if location not in eea_countries:
                risk_factors += 2
                break

        if len(data_flow.data_categories) > 5:
            risk_factors += 1

        if risk_factors >= 4:
            tier = RiskTier.HIGH
        elif risk_factors >= 2:
            tier = RiskTier.STANDARD
        else:
            tier = RiskTier.LOW

        vendor = self.vendors.get(vendor_id)
        if vendor:
            vendor.risk_tier = tier.value

        self.data_flows[data_flow.flow_id] = data_flow
        return tier

    def initiate_assessment(
        self, vendor_id: str, trigger: TriggerType = TriggerType.INITIAL, assessor: str = ""
    ) -> DueDiligenceAssessment:
        """Create a new due diligence assessment for a vendor."""
        assessment = DueDiligenceAssessment(
            vendor_id=vendor_id,
            trigger=trigger.value,
            status=AssessmentStatus.IN_PROGRESS.value,
            assessor=assessor,
        )
        self.assessments.append(assessment)
        return assessment

    def record_questionnaire_response(
        self, assessment_id: str, response: QuestionnaireResponse
    ) -> None:
        """Record a vendor's response to a questionnaire question."""
        for assessment in self.assessments:
            if assessment.assessment_id == assessment_id:
                assessment.responses.append(asdict(response))
                return
        raise ValueError(f"Assessment {assessment_id} not found")

    def calculate_domain_score(self, responses: list[dict], section: str) -> float:
        """Calculate average score for a questionnaire section."""
        section_responses = [r for r in responses if r["section"] == section]
        if not section_responses:
            return 0.0
        scores = [r["score"] for r in section_responses if r["score"] > 0]
        return sum(scores) / len(scores) if scores else 0.0

    def calculate_sufficiency_score(self, assessment_id: str) -> float:
        """Calculate weighted sufficiency score across all domains."""
        assessment = None
        for a in self.assessments:
            if a.assessment_id == assessment_id:
                assessment = a
                break

        if not assessment:
            raise ValueError(f"Assessment {assessment_id} not found")

        domain_scores = {
            "legal_governance": self.calculate_domain_score(assessment.responses, "A"),
            "technical_security": self.calculate_domain_score(assessment.responses, "B"),
            "data_handling": self.calculate_domain_score(assessment.responses, "C"),
            "certifications": self.calculate_domain_score(assessment.responses, "D"),
            "breach_history": assessment.domain_scores.get("breach_history", 3.0),
            "sub_processor_mgmt": assessment.domain_scores.get("sub_processor_mgmt", 3.0),
            "transfer_safeguards": assessment.domain_scores.get("transfer_safeguards", 3.0),
        }

        weighted_score = sum(
            domain_scores[domain] * weight
            for domain, weight in SCORING_WEIGHTS.items()
        )

        assessment.domain_scores = domain_scores
        assessment.weighted_score = round(weighted_score, 2)
        return assessment.weighted_score

    def make_sufficiency_decision(
        self, assessment_id: str, approver: str, rationale: str = "",
        conditions: list[str] = None
    ) -> SufficiencyDecision:
        """Issue sufficiency decision based on weighted score."""
        assessment = None
        for a in self.assessments:
            if a.assessment_id == assessment_id:
                assessment = a
                break

        if not assessment:
            raise ValueError(f"Assessment {assessment_id} not found")

        if assessment.weighted_score == 0.0:
            self.calculate_sufficiency_score(assessment_id)

        score = assessment.weighted_score
        if score >= DECISION_THRESHOLDS[SufficiencyDecision.APPROVED]:
            decision = SufficiencyDecision.APPROVED
        elif score >= DECISION_THRESHOLDS[SufficiencyDecision.CONDITIONALLY_APPROVED]:
            decision = SufficiencyDecision.CONDITIONALLY_APPROVED
        else:
            decision = SufficiencyDecision.REJECTED

        vendor = self.vendors.get(assessment.vendor_id)
        risk_tier = vendor.risk_tier if vendor else RiskTier.STANDARD.value
        reassessment_months = 12 if risk_tier == RiskTier.HIGH.value else 24

        assessment.decision = decision.value
        assessment.decision_rationale = rationale
        assessment.conditions = conditions or []
        assessment.approver = approver
        assessment.completed_date = datetime.now(timezone.utc).isoformat()
        assessment.status = AssessmentStatus.COMPLETED.value
        assessment.next_reassessment_date = (
            datetime.now(timezone.utc) + timedelta(days=reassessment_months * 30)
        ).isoformat()

        return decision

    def get_assessment_summary(self, assessment_id: str) -> dict:
        """Generate a summary of the due diligence assessment."""
        assessment = None
        for a in self.assessments:
            if a.assessment_id == assessment_id:
                assessment = a
                break

        if not assessment:
            raise ValueError(f"Assessment {assessment_id} not found")

        vendor = self.vendors.get(assessment.vendor_id)

        return {
            "assessment_id": assessment.assessment_id,
            "vendor_name": vendor.vendor_name if vendor else "Unknown",
            "vendor_jurisdiction": vendor.jurisdiction if vendor else "Unknown",
            "trigger": assessment.trigger,
            "status": assessment.status,
            "domain_scores": assessment.domain_scores,
            "weighted_score": assessment.weighted_score,
            "decision": assessment.decision,
            "decision_rationale": assessment.decision_rationale,
            "conditions": assessment.conditions,
            "assessor": assessment.assessor,
            "approver": assessment.approver,
            "initiated_date": assessment.initiated_date,
            "completed_date": assessment.completed_date,
            "next_reassessment_date": assessment.next_reassessment_date,
            "total_questions_answered": len(assessment.responses),
        }

    def get_vendors_due_reassessment(self) -> list[dict]:
        """Return vendors whose reassessment date has passed or is approaching."""
        now = datetime.now(timezone.utc).isoformat()
        due = []
        for assessment in self.assessments:
            if (
                assessment.status == AssessmentStatus.COMPLETED.value
                and assessment.next_reassessment_date
                and assessment.next_reassessment_date <= now
            ):
                vendor = self.vendors.get(assessment.vendor_id)
                due.append({
                    "vendor_id": assessment.vendor_id,
                    "vendor_name": vendor.vendor_name if vendor else "Unknown",
                    "last_assessment_date": assessment.completed_date,
                    "reassessment_due_date": assessment.next_reassessment_date,
                    "risk_tier": vendor.risk_tier if vendor else "unknown",
                })
        return due


if __name__ == "__main__":
    engine = VendorDueDiligenceEngine()

    # Register a prospective vendor
    vendor = VendorProfile(
        vendor_name="NimbusAnalytics GmbH",
        jurisdiction="Germany",
        dpo_name="Dr. Klaus Weber",
        dpo_contact="dpo@nimbusanalytics.de",
        processing_locations=["Germany", "Ireland"],
        certifications=["ISO 27001:2022", "SOC 2 Type II"],
        sub_processors=[
            {"name": "AWS EU (Frankfurt)", "function": "Cloud hosting", "location": "Germany"},
            {"name": "Elastic Cloud EU", "function": "Log analytics", "location": "Netherlands"},
        ],
    )
    engine.register_vendor(vendor)

    # Classify risk tier based on data flow
    data_flow = DataFlowRecord(
        vendor_id=vendor.vendor_id,
        data_categories=["email_address", "usage_metrics", "account_id", "ip_address"],
        data_subject_categories=["Summit Cloud Partners enterprise customers"],
        approximate_volume=25000,
        transfer_method="REST API over TLS 1.3",
        encryption_protocol="AES-256-GCM at rest, TLS 1.3 in transit",
        processing_locations=["Germany", "Ireland"],
        retention_period="18 months from collection",
        special_category_data=False,
    )
    tier = engine.classify_risk_tier(vendor.vendor_id, data_flow)
    print(f"Risk Tier: {tier.value}")

    # Initiate assessment
    assessment = engine.initiate_assessment(
        vendor.vendor_id,
        trigger=TriggerType.INITIAL,
        assessor="Sarah Chen, Privacy Analyst",
    )

    # Record questionnaire responses (Section A — Legal Governance)
    section_a_responses = [
        QuestionnaireResponse(
            section="A", question_id="A1",
            question_text="Does your organization have a designated DPO?",
            vendor_response="Yes — Dr. Klaus Weber, appointed 2021, reports directly to the management board.",
            evidence_provided=True,
            evidence_description="DPO appointment letter and organizational chart provided",
            score=5, assessor_notes="Clear DPO appointment with board-level reporting line",
        ),
        QuestionnaireResponse(
            section="A", question_id="A2",
            question_text="In which jurisdictions is your organization established?",
            vendor_response="Headquartered in Munich, Germany. Subsidiary in Dublin, Ireland.",
            evidence_provided=True,
            evidence_description="Company registration documents provided",
            score=5, assessor_notes="EEA-only establishment, no third-country presence",
        ),
        QuestionnaireResponse(
            section="A", question_id="A3",
            question_text="GDPR compliance governance structure?",
            vendor_response="Privacy Office of 4 staff, annual training, documented privacy program since 2018.",
            evidence_provided=True,
            evidence_description="Privacy program charter and org chart provided",
            score=4, assessor_notes="Mature program, could improve documentation of privacy metrics",
        ),
    ]

    # Record questionnaire responses (Section B — Technical Security)
    section_b_responses = [
        QuestionnaireResponse(
            section="B", question_id="B1",
            question_text="Encryption approach for data at rest and in transit?",
            vendor_response="AES-256-GCM at rest via AWS KMS. TLS 1.3 for all API communications. Customer-managed keys available.",
            evidence_provided=True,
            evidence_description="Architecture documentation and AWS KMS policy provided",
            score=5, assessor_notes="Strong encryption with customer-managed key option",
        ),
        QuestionnaireResponse(
            section="B", question_id="B2",
            question_text="Access control and authentication model?",
            vendor_response="RBAC with quarterly access reviews. MFA enforced for all employees. SSO via SAML 2.0.",
            evidence_provided=True,
            evidence_description="IAM policy document and latest access review report provided",
            score=4, assessor_notes="Solid access controls, quarterly review cadence is appropriate",
        ),
    ]

    # Record questionnaire responses (Section C — Data Handling)
    section_c_responses = [
        QuestionnaireResponse(
            section="C", question_id="C1",
            question_text="Client data segregation approach?",
            vendor_response="Logical segregation at the database level with tenant-specific encryption keys.",
            evidence_provided=True,
            evidence_description="Multi-tenancy architecture document provided",
            score=4, assessor_notes="Logical segregation with per-tenant keys is adequate",
        ),
    ]

    # Record questionnaire responses (Section D — Certifications)
    section_d_responses = [
        QuestionnaireResponse(
            section="D", question_id="D1",
            question_text="ISO 27001 certification?",
            vendor_response="ISO 27001:2022 certified. Certification body: TUV Rheinland. Scope: All cloud analytics services.",
            evidence_provided=True,
            evidence_description="Certificate PDF provided, valid through 2027-06-15",
            score=5, assessor_notes="Verified on TUV Rheinland registry. Full scope coverage.",
        ),
        QuestionnaireResponse(
            section="D", question_id="D3",
            question_text="SOC 2 Type II attestation?",
            vendor_response="SOC 2 Type II covering Security, Availability, and Confidentiality. Period: 2025-01-01 to 2025-12-31.",
            evidence_provided=True,
            evidence_description="SOC 2 Type II report provided under NDA",
            score=4, assessor_notes="No qualified opinions. One minor finding on access review timeliness — remediated.",
        ),
    ]

    for response in section_a_responses + section_b_responses + section_c_responses + section_d_responses:
        engine.record_questionnaire_response(assessment.assessment_id, response)

    # Set manually assessed domain scores
    assessment.domain_scores["breach_history"] = 4.5  # No breaches reported
    assessment.domain_scores["sub_processor_mgmt"] = 4.0  # Good sub-processor controls
    assessment.domain_scores["transfer_safeguards"] = 5.0  # EEA-only processing

    # Calculate sufficiency score
    score = engine.calculate_sufficiency_score(assessment.assessment_id)
    print(f"Weighted Sufficiency Score: {score}")

    # Make sufficiency decision
    decision = engine.make_sufficiency_decision(
        assessment.assessment_id,
        approver="Dr. Maria Santos, DPO — Summit Cloud Partners",
        rationale="NimbusAnalytics GmbH demonstrates strong technical controls, appropriate certifications, "
                  "and EEA-only processing. ISO 27001 and SOC 2 Type II verified. Minor gap in privacy-specific "
                  "certification (no ISO 27701) — not blocking given overall control maturity.",
        conditions=["Recommend vendor pursue ISO 27701 certification within 18 months"],
    )
    print(f"Decision: {decision.value}")

    # Print full summary
    summary = engine.get_assessment_summary(assessment.assessment_id)
    print("\n=== Due Diligence Assessment Summary ===")
    print(json.dumps(summary, indent=2))
