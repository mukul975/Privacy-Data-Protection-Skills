#!/usr/bin/env python3
"""
UAE PDP Law Compliance — Assessment and Tracking Engine

Implements compliance assessment for Federal Decree-Law No. 45 of 2021
on the Protection of Personal Data including legal basis mapping,
cross-border transfer evaluation, DPIA tracking, data subject rights
management, and breach notification coordination.
"""

import json
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class LawfulBasis(Enum):
    CONSENT = "consent"
    CONTRACT = "contract_performance"
    LEGAL_OBLIGATION = "legal_obligation"
    VITAL_INTERESTS = "vital_interests"
    MADE_PUBLIC = "data_made_public"
    LEGAL_PROCEEDINGS = "legal_proceedings"
    MEDICAL_PURPOSES = "medical_purposes"
    PUBLIC_INTEREST = "public_interest"
    LEGITIMATE_INTEREST = "legitimate_interest"


class TransferMechanism(Enum):
    ADEQUACY = "adequacy_determination"
    SCC = "standard_contractual_clauses"
    BCR = "binding_corporate_rules"
    CERTIFICATION = "approved_certification"
    EXPLICIT_CONSENT = "explicit_consent"
    DEROGATION = "derogation"


class Jurisdiction(Enum):
    MAINLAND = "uae_mainland"
    DIFC = "difc"
    ADGM = "adgm"
    OTHER_FREE_ZONE = "other_free_zone"


class ComplianceStatus(Enum):
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PARTIAL = "partially_compliant"
    NOT_ASSESSED = "not_assessed"


class RiskLevel(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


SENSITIVE_CATEGORIES = [
    "racial_ethnic_origin",
    "political_opinions",
    "religious_beliefs",
    "criminal_records",
    "biometric_data",
    "health_data",
    "genetic_data",
]


@dataclass
class ProcessingActivity:
    """A data processing activity mapped to UAE PDP Law provisions."""
    activity_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    description: str = ""
    data_categories: list[str] = field(default_factory=list)
    data_subjects: list[str] = field(default_factory=list)
    lawful_basis: str = LawfulBasis.CONSENT.value
    involves_sensitive: bool = False
    sensitive_categories: list[str] = field(default_factory=list)
    retention_period: str = ""
    recipients: list[str] = field(default_factory=list)
    cross_border: bool = False
    dpia_required: bool = False
    dpia_conducted: bool = False


@dataclass
class CrossBorderTransfer:
    """Article 22 cross-border transfer record."""
    transfer_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    recipient: str = ""
    country: str = ""
    mechanism: str = TransferMechanism.ADEQUACY.value
    data_categories: list[str] = field(default_factory=list)
    adequacy_assessment: str = ""
    agreement_reference: str = ""
    approved: bool = False
    review_date: Optional[str] = None


@dataclass
class DPIARecord:
    """Data Protection Impact Assessment record."""
    dpia_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    activity_name: str = ""
    risk_level: str = RiskLevel.MEDIUM.value
    conducted_date: str = ""
    assessor: str = ""
    risks_identified: list[str] = field(default_factory=list)
    mitigations: list[str] = field(default_factory=list)
    residual_risk: str = RiskLevel.LOW.value
    approved: bool = False
    approved_by: str = ""


@dataclass
class BreachRecord:
    """Article 12 breach notification record."""
    breach_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    discovered_date: str = ""
    nature: str = ""
    data_categories: list[str] = field(default_factory=list)
    data_subjects_affected: int = 0
    involves_sensitive: bool = False
    risk_to_subjects: str = RiskLevel.MEDIUM.value
    data_office_notified: bool = False
    data_office_notification_date: Optional[str] = None
    subjects_notified: bool = False
    subjects_notification_date: Optional[str] = None
    remediation_measures: list[str] = field(default_factory=list)


@dataclass
class UAEComplianceRecord:
    """Complete UAE PDP Law compliance record."""
    record_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    organisation_name: str = ""
    trade_license: str = ""
    jurisdiction: str = Jurisdiction.MAINLAND.value
    dpo_name: str = ""
    dpo_contact: str = ""
    processing_activities: list[dict] = field(default_factory=list)
    cross_border_transfers: list[dict] = field(default_factory=list)
    dpias: list[dict] = field(default_factory=list)
    breaches: list[dict] = field(default_factory=list)
    overall_status: str = ComplianceStatus.NOT_ASSESSED.value
    assessment_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    assessor: str = ""


class UAEPDPComplianceEngine:
    """
    Manages UAE PDP Law compliance including legal basis mapping,
    cross-border transfer assessment, DPIA management, and breach
    notification coordination.
    """

    def __init__(self):
        self.records: dict[str, UAEComplianceRecord] = {}

    def create_assessment(
        self, organisation_name: str, trade_license: str,
        jurisdiction: Jurisdiction, dpo_name: str, assessor: str
    ) -> UAEComplianceRecord:
        """Create a new UAE PDP Law compliance assessment."""
        record = UAEComplianceRecord(
            organisation_name=organisation_name,
            trade_license=trade_license,
            jurisdiction=jurisdiction.value,
            dpo_name=dpo_name,
            assessor=assessor,
        )
        self.records[record.record_id] = record
        return record

    def add_processing_activity(
        self, record_id: str, name: str, description: str,
        data_categories: list[str], data_subjects: list[str],
        lawful_basis: LawfulBasis, retention_period: str,
        sensitive_categories: list[str] = None,
    ) -> ProcessingActivity:
        """Add a processing activity with legal basis mapping."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        involves_sensitive = bool(sensitive_categories)
        dpia_required = involves_sensitive or len(data_subjects) > 0

        activity = ProcessingActivity(
            name=name,
            description=description,
            data_categories=data_categories,
            data_subjects=data_subjects,
            lawful_basis=lawful_basis.value,
            involves_sensitive=involves_sensitive,
            sensitive_categories=sensitive_categories or [],
            retention_period=retention_period,
            dpia_required=dpia_required,
        )
        record.processing_activities.append(asdict(activity))
        return activity

    def assess_cross_border_transfer(
        self, record_id: str, recipient: str, country: str,
        mechanism: TransferMechanism, data_categories: list[str],
        adequacy_notes: str
    ) -> CrossBorderTransfer:
        """Evaluate a cross-border transfer under Article 22."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        transfer = CrossBorderTransfer(
            recipient=recipient,
            country=country,
            mechanism=mechanism.value,
            data_categories=data_categories,
            adequacy_assessment=adequacy_notes,
            approved=mechanism == TransferMechanism.ADEQUACY,
        )
        record.cross_border_transfers.append(asdict(transfer))
        return transfer

    def conduct_dpia(
        self, record_id: str, activity_name: str,
        risks: list[str], mitigations: list[str],
        assessor: str, approver: str
    ) -> DPIARecord:
        """Conduct and record a DPIA under Article 9."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        initial_risk = RiskLevel.HIGH if len(risks) > 3 else RiskLevel.MEDIUM
        residual = RiskLevel.LOW if len(mitigations) >= len(risks) else RiskLevel.MEDIUM

        dpia = DPIARecord(
            activity_name=activity_name,
            risk_level=initial_risk.value,
            conducted_date=datetime.now(timezone.utc).isoformat(),
            assessor=assessor,
            risks_identified=risks,
            mitigations=mitigations,
            residual_risk=residual.value,
            approved=True,
            approved_by=approver,
        )
        record.dpias.append(asdict(dpia))

        for act in record.processing_activities:
            if act.get("name") == activity_name:
                act["dpia_conducted"] = True

        return dpia

    def record_breach(
        self, record_id: str, nature: str,
        data_categories: list[str], subjects_affected: int,
        involves_sensitive: bool
    ) -> BreachRecord:
        """Record a data breach under Article 12."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        risk = RiskLevel.HIGH if involves_sensitive or subjects_affected > 1000 else RiskLevel.MEDIUM

        breach = BreachRecord(
            discovered_date=datetime.now(timezone.utc).isoformat(),
            nature=nature,
            data_categories=data_categories,
            data_subjects_affected=subjects_affected,
            involves_sensitive=involves_sensitive,
            risk_to_subjects=risk.value,
        )
        record.breaches.append(asdict(breach))
        return breach

    def generate_compliance_summary(self, record_id: str) -> dict:
        """Generate comprehensive compliance summary."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        sensitive_activities = [
            a for a in record.processing_activities
            if a.get("involves_sensitive")
        ]
        dpia_needed = [
            a for a in record.processing_activities
            if a.get("dpia_required") and not a.get("dpia_conducted")
        ]

        return {
            "record_id": record_id,
            "organisation": record.organisation_name,
            "jurisdiction": record.jurisdiction,
            "dpo": record.dpo_name,
            "total_processing_activities": len(record.processing_activities),
            "sensitive_data_activities": len(sensitive_activities),
            "cross_border_transfers": len(record.cross_border_transfers),
            "dpias_conducted": len(record.dpias),
            "dpias_outstanding": len(dpia_needed),
            "breaches_recorded": len(record.breaches),
            "assessment_date": record.assessment_date,
        }


if __name__ == "__main__":
    engine = UAEPDPComplianceEngine()

    # Create assessment for a UAE technology company
    record = engine.create_assessment(
        organisation_name="Gulf Digital Solutions LLC",
        trade_license="DED-987654",
        jurisdiction=Jurisdiction.MAINLAND,
        dpo_name="Ahmed Al-Rashid",
        assessor="Sarah Mahmoud, Privacy Consultant",
    )
    print(f"Assessment ID: {record.record_id}")

    # Add processing activity
    activity = engine.add_processing_activity(
        record.record_id,
        name="Customer Relationship Management",
        description="Processing customer data for account management and service delivery",
        data_categories=["name", "email", "phone", "emirates_id", "transaction_history"],
        data_subjects=["customers"],
        lawful_basis=LawfulBasis.CONTRACT,
        retention_period="Duration of customer relationship plus 5 years per UAE Commercial Companies Law",
    )
    print(f"Activity: {activity.name}")

    # Add sensitive data processing
    engine.add_processing_activity(
        record.record_id,
        name="Employee Health Insurance Administration",
        description="Processing employee health data for insurance enrolment and claims",
        data_categories=["name", "emirates_id", "health_records", "insurance_claims"],
        data_subjects=["employees"],
        lawful_basis=LawfulBasis.LEGAL_OBLIGATION,
        retention_period="Duration of employment plus 8 years",
        sensitive_categories=["health_data"],
    )

    # Cross-border transfer
    transfer = engine.assess_cross_border_transfer(
        record.record_id,
        recipient="Microsoft Ireland Operations Ltd",
        country="Ireland",
        mechanism=TransferMechanism.SCC,
        data_categories=["customer_data", "employee_data"],
        adequacy_notes="EU/EEA — GDPR provides comprehensive data protection framework; SCCs executed",
    )
    print(f"Transfer: {transfer.recipient} ({transfer.country})")

    # Conduct DPIA
    dpia = engine.conduct_dpia(
        record.record_id,
        activity_name="Employee Health Insurance Administration",
        risks=[
            "Unauthorised access to sensitive health data",
            "Data breach exposing employee medical records",
            "Excessive retention of health data",
        ],
        mitigations=[
            "Role-based access control with MFA",
            "Encryption at rest and in transit",
            "Automated retention policy enforcement",
        ],
        assessor="Sarah Mahmoud",
        approver="Ahmed Al-Rashid, DPO",
    )
    print(f"DPIA: {dpia.activity_name} — residual risk: {dpia.residual_risk}")

    # Summary
    summary = engine.generate_compliance_summary(record.record_id)
    print(f"\n=== UAE PDP Compliance Summary ===")
    print(json.dumps(summary, indent=2))
