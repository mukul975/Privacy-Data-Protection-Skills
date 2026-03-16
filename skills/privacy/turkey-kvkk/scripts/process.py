#!/usr/bin/env python3
"""
Turkey KVKK Compliance — Assessment and Tracking Engine

Implements KVKK (Law No. 6698) compliance assessment including
legal basis mapping, VERBIS registration tracking, cross-border
transfer evaluation, data subject rights management, and breach
notification coordination.
"""

import json
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class LegalBasis(Enum):
    EXPLICIT_CONSENT = "explicit_consent"
    PROVIDED_BY_LAW = "expressly_provided_by_law"
    VITAL_INTERESTS = "protection_of_life_physical_integrity"
    CONTRACT = "contract_performance"
    LEGAL_OBLIGATION = "legal_obligation"
    MADE_PUBLIC = "made_public_by_data_subject"
    LEGAL_CLAIMS = "establishment_exercise_defence_of_right"
    LEGITIMATE_INTEREST = "legitimate_interest"


class SpecialCategoryBasis(Enum):
    EXPLICIT_CONSENT = "explicit_consent"
    EXPRESS_LAW = "express_authorisation_by_law"
    HEALTH_AUTHORISED = "authorised_persons_health_sexual_life"


class TransferMechanism(Enum):
    ADEQUACY = "board_adequacy_decision"
    SCC = "standard_contractual_clauses"
    BCR = "binding_corporate_rules"
    WRITTEN_UNDERTAKING = "written_undertaking_board_approved"
    EXPLICIT_CONSENT = "explicit_consent"


class VERBISStatus(Enum):
    REQUIRED = "required"
    REGISTERED = "registered"
    EXEMPT = "exempt"
    PENDING = "pending"


class ComplianceStatus(Enum):
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PARTIAL = "partially_compliant"
    NOT_ASSESSED = "not_assessed"


SPECIAL_CATEGORIES = [
    "race_ethnic_origin",
    "political_opinion",
    "philosophical_belief",
    "religion_sect_belief",
    "appearance_dressing",
    "association_union_membership",
    "health",
    "sexual_life",
    "criminal_conviction",
    "biometric",
    "genetic",
]

BOARD_NOTIFICATION_HOURS = 72


@dataclass
class ProcessingActivity:
    """A single data processing activity mapped to KVKK legal basis."""
    activity_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    activity_name: str = ""
    description: str = ""
    data_categories: list[str] = field(default_factory=list)
    data_subjects: list[str] = field(default_factory=list)
    legal_basis: str = LegalBasis.EXPLICIT_CONSENT.value
    involves_special_category: bool = False
    special_category_basis: Optional[str] = None
    retention_period: str = ""
    recipients: list[str] = field(default_factory=list)
    cross_border: bool = False


@dataclass
class CrossBorderTransfer:
    """Record of a cross-border transfer under Article 9."""
    transfer_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    recipient: str = ""
    country: str = ""
    mechanism: str = TransferMechanism.EXPLICIT_CONSENT.value
    board_approval_required: bool = False
    board_approval_status: str = "not_submitted"
    board_approval_date: Optional[str] = None
    data_categories: list[str] = field(default_factory=list)
    active: bool = True


@dataclass
class DataSubjectRequest:
    """Article 11 data subject rights request."""
    request_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    received_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    data_subject_name: str = ""
    right_exercised: str = ""
    description: str = ""
    response_deadline: str = ""
    response_date: Optional[str] = None
    outcome: str = "pending"
    refusal_reason: Optional[str] = None


@dataclass
class BreachRecord:
    """Article 12(5) breach notification record."""
    breach_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    discovered_date: str = ""
    nature: str = ""
    data_categories: list[str] = field(default_factory=list)
    data_subjects_affected: int = 0
    board_notified: bool = False
    board_notification_date: Optional[str] = None
    within_72_hours: Optional[bool] = None
    data_subjects_notified: bool = False
    remediation_measures: list[str] = field(default_factory=list)


@dataclass
class KVKKComplianceRecord:
    """Complete KVKK compliance assessment record."""
    record_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    organisation_name: str = ""
    tax_id: str = ""
    verbis_status: str = VERBISStatus.REQUIRED.value
    verbis_registration_number: str = ""
    employee_count: int = 0
    annual_turnover_try: float = 0.0
    processing_activities: list[dict] = field(default_factory=list)
    cross_border_transfers: list[dict] = field(default_factory=list)
    data_subject_requests: list[dict] = field(default_factory=list)
    breaches: list[dict] = field(default_factory=list)
    overall_status: str = ComplianceStatus.NOT_ASSESSED.value
    assessment_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    assessor: str = ""


class KVKKComplianceEngine:
    """
    Manages KVKK compliance assessment including VERBIS registration
    determination, legal basis mapping, cross-border transfer evaluation,
    data subject rights tracking, and breach notification coordination.
    """

    def __init__(self):
        self.records: dict[str, KVKKComplianceRecord] = {}

    def create_assessment(
        self, organisation_name: str, tax_id: str,
        employee_count: int, annual_turnover_try: float,
        assessor: str
    ) -> KVKKComplianceRecord:
        """Create a new KVKK compliance assessment."""
        record = KVKKComplianceRecord(
            organisation_name=organisation_name,
            tax_id=tax_id,
            employee_count=employee_count,
            annual_turnover_try=annual_turnover_try,
            assessor=assessor,
        )
        self.records[record.record_id] = record
        return record

    def assess_verbis_obligation(self, record_id: str, core_activity_special: bool = False) -> dict:
        """Determine VERBIS registration obligation."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        required = False
        reasons = []

        if record.employee_count >= 50:
            required = True
            reasons.append(f"Employee count ({record.employee_count}) meets 50+ threshold")

        if record.annual_turnover_try >= 100_000_000:
            required = True
            reasons.append(f"Annual turnover (TRY {record.annual_turnover_try:,.0f}) meets TRY 100M threshold")

        if core_activity_special:
            required = True
            reasons.append("Core activity involves special category data processing")

        record.verbis_status = VERBISStatus.REQUIRED.value if required else VERBISStatus.EXEMPT.value

        return {
            "record_id": record_id,
            "verbis_required": required,
            "reasons": reasons,
            "status": record.verbis_status,
        }

    def add_processing_activity(
        self, record_id: str, name: str, description: str,
        data_categories: list[str], data_subjects: list[str],
        legal_basis: LegalBasis, retention_period: str,
        involves_special_category: bool = False,
        special_category_basis: Optional[SpecialCategoryBasis] = None,
    ) -> ProcessingActivity:
        """Add a processing activity with legal basis mapping."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        activity = ProcessingActivity(
            activity_name=name,
            description=description,
            data_categories=data_categories,
            data_subjects=data_subjects,
            legal_basis=legal_basis.value,
            retention_period=retention_period,
            involves_special_category=involves_special_category,
            special_category_basis=special_category_basis.value if special_category_basis else None,
        )
        record.processing_activities.append(asdict(activity))
        return activity

    def evaluate_cross_border_transfer(
        self, record_id: str, recipient: str, country: str,
        mechanism: TransferMechanism, data_categories: list[str]
    ) -> CrossBorderTransfer:
        """Evaluate and record a cross-border transfer under Article 9."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        board_required = mechanism in (
            TransferMechanism.BCR,
            TransferMechanism.WRITTEN_UNDERTAKING,
        )

        transfer = CrossBorderTransfer(
            recipient=recipient,
            country=country,
            mechanism=mechanism.value,
            board_approval_required=board_required,
            data_categories=data_categories,
        )
        record.cross_border_transfers.append(asdict(transfer))
        return transfer

    def handle_data_subject_request(
        self, record_id: str, data_subject_name: str,
        right_exercised: str, description: str
    ) -> DataSubjectRequest:
        """Process an Article 11 data subject request."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        received = datetime.now(timezone.utc)
        deadline = received + timedelta(days=30)

        request = DataSubjectRequest(
            received_date=received.isoformat(),
            data_subject_name=data_subject_name,
            right_exercised=right_exercised,
            description=description,
            response_deadline=deadline.isoformat(),
        )
        record.data_subject_requests.append(asdict(request))
        return request

    def record_breach(
        self, record_id: str, nature: str,
        data_categories: list[str], subjects_affected: int
    ) -> BreachRecord:
        """Record a data breach under Article 12(5)."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        breach = BreachRecord(
            discovered_date=datetime.now(timezone.utc).isoformat(),
            nature=nature,
            data_categories=data_categories,
            data_subjects_affected=subjects_affected,
        )
        record.breaches.append(asdict(breach))
        return breach

    def generate_compliance_summary(self, record_id: str) -> dict:
        """Generate KVKK compliance summary."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        special_processing = [
            a for a in record.processing_activities
            if a.get("involves_special_category")
        ]
        pending_requests = [
            r for r in record.data_subject_requests
            if r.get("outcome") == "pending"
        ]
        board_pending_transfers = [
            t for t in record.cross_border_transfers
            if t.get("board_approval_required") and t.get("board_approval_status") != "approved"
        ]

        return {
            "record_id": record_id,
            "organisation": record.organisation_name,
            "verbis_status": record.verbis_status,
            "total_processing_activities": len(record.processing_activities),
            "special_category_activities": len(special_processing),
            "cross_border_transfers": len(record.cross_border_transfers),
            "transfers_pending_board_approval": len(board_pending_transfers),
            "data_subject_requests_total": len(record.data_subject_requests),
            "data_subject_requests_pending": len(pending_requests),
            "breaches_recorded": len(record.breaches),
            "assessment_date": record.assessment_date,
            "assessor": record.assessor,
        }


if __name__ == "__main__":
    engine = KVKKComplianceEngine()

    # Create assessment for a Turkish technology company
    record = engine.create_assessment(
        organisation_name="Anatolian Digital Hizmetler A.S.",
        tax_id="1234567890",
        employee_count=180,
        annual_turnover_try=250_000_000,
        assessor="Av. Elif Yilmaz, Data Protection Counsel",
    )
    print(f"Assessment ID: {record.record_id}")

    # Assess VERBIS obligation
    verbis = engine.assess_verbis_obligation(record.record_id, core_activity_special=False)
    print(f"\nVERBIS Assessment:")
    print(json.dumps(verbis, indent=2))

    # Add processing activity
    activity = engine.add_processing_activity(
        record.record_id,
        name="Customer Account Management",
        description="Processing customer personal data for account creation, authentication, and service delivery",
        data_categories=["name", "email", "phone", "address", "national_id"],
        data_subjects=["customers"],
        legal_basis=LegalBasis.CONTRACT,
        retention_period="Duration of customer relationship plus 10 years per Turkish Commercial Code",
    )
    print(f"\nActivity: {activity.activity_name}")

    # Add special category processing
    engine.add_processing_activity(
        record.record_id,
        name="Employee Health Records",
        description="Occupational health assessments and sick leave tracking",
        data_categories=["health_reports", "sick_leave_records", "disability_status"],
        data_subjects=["employees"],
        legal_basis=LegalBasis.LEGAL_OBLIGATION,
        retention_period="Duration of employment plus 15 years per Labour Law",
        involves_special_category=True,
        special_category_basis=SpecialCategoryBasis.HEALTH_AUTHORISED,
    )

    # Evaluate cross-border transfer
    transfer = engine.evaluate_cross_border_transfer(
        record.record_id,
        recipient="AWS EMEA SARL",
        country="Germany",
        mechanism=TransferMechanism.SCC,
        data_categories=["customer_data", "usage_analytics"],
    )
    print(f"\nTransfer to {transfer.country}: mechanism={transfer.mechanism}")

    # Generate summary
    summary = engine.generate_compliance_summary(record.record_id)
    print(f"\n=== KVKK Compliance Summary ===")
    print(json.dumps(summary, indent=2))
