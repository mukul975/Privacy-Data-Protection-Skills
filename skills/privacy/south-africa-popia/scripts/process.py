#!/usr/bin/env python3
"""
South Africa POPIA Compliance — Assessment and Tracking Engine

Implements POPIA compliance assessment against the eight conditions
for lawful processing, cross-border transfer evaluation, breach
notification tracking, and Information Officer registration management.
"""

import json
import uuid
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class ComplianceStatus(Enum):
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PARTIAL = "partially_compliant"
    NOT_ASSESSED = "not_assessed"


class GapPriority(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class TransferMechanism(Enum):
    ADEQUACY = "adequate_protection"
    BCR = "binding_corporate_rules"
    BINDING_AGREEMENT = "binding_agreement"
    CONSENT = "data_subject_consent"
    CONTRACT_PERFORMANCE = "contract_performance"
    PRE_CONTRACTUAL = "pre_contractual_measures"
    BENEFIT = "benefit_of_data_subject"
    PUBLIC_RECORD = "public_record"


POPIA_CONDITIONS = [
    {"number": 1, "name": "Accountability", "sections": "Section 8"},
    {"number": 2, "name": "Processing Limitation", "sections": "Sections 9-12"},
    {"number": 3, "name": "Purpose Specification", "sections": "Sections 13-14"},
    {"number": 4, "name": "Further Processing Limitation", "sections": "Section 15"},
    {"number": 5, "name": "Information Quality", "sections": "Section 16"},
    {"number": 6, "name": "Openness", "sections": "Sections 17-18"},
    {"number": 7, "name": "Security Safeguards", "sections": "Sections 19-22"},
    {"number": 8, "name": "Data Subject Participation", "sections": "Sections 23-25"},
]

SPECIAL_CATEGORIES = [
    "religious_philosophical_beliefs",
    "race_ethnic_origin",
    "trade_union_membership",
    "political_persuasion",
    "health",
    "sex_life",
    "biometric_information",
    "criminal_behaviour",
]


@dataclass
class ConditionAssessment:
    """Assessment of a single POPIA condition."""
    condition_number: int = 0
    condition_name: str = ""
    sections: str = ""
    status: str = ComplianceStatus.NOT_ASSESSED.value
    findings: list[str] = field(default_factory=list)
    gaps: list[str] = field(default_factory=list)
    evidence_references: list[str] = field(default_factory=list)
    assessed_date: str = ""
    assessor: str = ""


@dataclass
class CrossBorderTransfer:
    """Record of a cross-border transfer under Section 72."""
    transfer_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    recipient: str = ""
    recipient_country: str = ""
    mechanism: str = TransferMechanism.ADEQUACY.value
    data_categories: list[str] = field(default_factory=list)
    adequacy_assessment: str = ""
    agreement_reference: str = ""
    approved: bool = False
    approved_by: str = ""
    approved_date: Optional[str] = None


@dataclass
class SecurityCompromise:
    """Section 22 security compromise notification record."""
    compromise_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    discovered_date: str = ""
    nature_of_compromise: str = ""
    data_categories_affected: list[str] = field(default_factory=list)
    estimated_data_subjects: int = 0
    identity_theft_risk: bool = False
    regulator_notified: bool = False
    regulator_notification_date: Optional[str] = None
    data_subjects_notified: bool = False
    ds_notification_date: Optional[str] = None
    ds_notification_method: str = ""
    police_delay_requested: bool = False
    remediation_measures: list[str] = field(default_factory=list)


@dataclass
class POPIAComplianceRecord:
    """Complete POPIA compliance assessment record."""
    record_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    organisation_name: str = ""
    registration_number: str = ""
    information_officer: str = ""
    io_registered: bool = False
    io_registration_number: str = ""
    deputy_information_officers: list[str] = field(default_factory=list)
    popia_applicable: bool = True
    applicability_rationale: str = ""
    condition_assessments: list[dict] = field(default_factory=list)
    special_categories_processed: list[str] = field(default_factory=list)
    cross_border_transfers: list[dict] = field(default_factory=list)
    security_compromises: list[dict] = field(default_factory=list)
    overall_status: str = ComplianceStatus.NOT_ASSESSED.value
    assessment_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    assessor: str = ""


class POPIAComplianceEngine:
    """
    Manages POPIA compliance assessments including condition-by-condition
    evaluation, cross-border transfer assessment, breach notification
    tracking, and overall compliance scoring.
    """

    def __init__(self):
        self.records: dict[str, POPIAComplianceRecord] = {}

    def create_assessment(
        self, organisation_name: str, registration_number: str,
        information_officer: str, assessor: str
    ) -> POPIAComplianceRecord:
        """Create a new POPIA compliance assessment."""
        record = POPIAComplianceRecord(
            organisation_name=organisation_name,
            registration_number=registration_number,
            information_officer=information_officer,
            assessor=assessor,
        )

        for condition in POPIA_CONDITIONS:
            assessment = ConditionAssessment(
                condition_number=condition["number"],
                condition_name=condition["name"],
                sections=condition["sections"],
            )
            record.condition_assessments.append(asdict(assessment))

        self.records[record.record_id] = record
        return record

    def assess_condition(
        self, record_id: str, condition_number: int,
        status: ComplianceStatus, findings: list[str],
        gaps: list[str], evidence: list[str], assessor: str
    ) -> dict:
        """Assess a specific POPIA condition."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        for ca in record.condition_assessments:
            if ca["condition_number"] == condition_number:
                ca["status"] = status.value
                ca["findings"] = findings
                ca["gaps"] = gaps
                ca["evidence_references"] = evidence
                ca["assessed_date"] = datetime.now(timezone.utc).isoformat()
                ca["assessor"] = assessor
                return ca

        raise ValueError(f"Condition {condition_number} not found")

    def evaluate_cross_border_transfer(
        self, record_id: str, recipient: str, country: str,
        mechanism: TransferMechanism, data_categories: list[str],
        adequacy_notes: str, approver: str
    ) -> CrossBorderTransfer:
        """Evaluate and record a cross-border transfer under Section 72."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        transfer = CrossBorderTransfer(
            recipient=recipient,
            recipient_country=country,
            mechanism=mechanism.value,
            data_categories=data_categories,
            adequacy_assessment=adequacy_notes,
            approved=True,
            approved_by=approver,
            approved_date=datetime.now(timezone.utc).isoformat(),
        )
        record.cross_border_transfers.append(asdict(transfer))
        return transfer

    def record_security_compromise(
        self, record_id: str, nature: str,
        data_categories: list[str], estimated_subjects: int,
        identity_theft_risk: bool
    ) -> SecurityCompromise:
        """Record a security compromise under Section 22."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        compromise = SecurityCompromise(
            discovered_date=datetime.now(timezone.utc).isoformat(),
            nature_of_compromise=nature,
            data_categories_affected=data_categories,
            estimated_data_subjects=estimated_subjects,
            identity_theft_risk=identity_theft_risk,
        )
        record.security_compromises.append(asdict(compromise))
        return compromise

    def calculate_overall_compliance(self, record_id: str) -> dict:
        """Calculate overall POPIA compliance status."""
        record = self.records.get(record_id)
        if not record:
            raise ValueError(f"Record {record_id} not found")

        total = len(record.condition_assessments)
        compliant = sum(
            1 for ca in record.condition_assessments
            if ca["status"] == ComplianceStatus.COMPLIANT.value
        )
        non_compliant = sum(
            1 for ca in record.condition_assessments
            if ca["status"] == ComplianceStatus.NON_COMPLIANT.value
        )
        partial = sum(
            1 for ca in record.condition_assessments
            if ca["status"] == ComplianceStatus.PARTIAL.value
        )
        not_assessed = sum(
            1 for ca in record.condition_assessments
            if ca["status"] == ComplianceStatus.NOT_ASSESSED.value
        )

        all_gaps = []
        for ca in record.condition_assessments:
            for gap in ca.get("gaps", []):
                all_gaps.append({
                    "condition": ca["condition_name"],
                    "gap": gap,
                })

        if non_compliant > 0:
            overall = ComplianceStatus.NON_COMPLIANT.value
        elif partial > 0 or not_assessed > 0:
            overall = ComplianceStatus.PARTIAL.value
        else:
            overall = ComplianceStatus.COMPLIANT.value

        record.overall_status = overall

        return {
            "record_id": record_id,
            "organisation": record.organisation_name,
            "overall_status": overall,
            "conditions_compliant": compliant,
            "conditions_non_compliant": non_compliant,
            "conditions_partial": partial,
            "conditions_not_assessed": not_assessed,
            "total_conditions": total,
            "compliance_percentage": round((compliant / total) * 100, 1) if total > 0 else 0,
            "total_gaps": len(all_gaps),
            "gaps": all_gaps,
            "cross_border_transfers": len(record.cross_border_transfers),
            "security_compromises": len(record.security_compromises),
        }


if __name__ == "__main__":
    engine = POPIAComplianceEngine()

    # Create assessment for a South African financial services firm
    record = engine.create_assessment(
        organisation_name="Protea Financial Holdings (Pty) Ltd",
        registration_number="2019/123456/07",
        information_officer="Advocate Nomsa Dlamini",
        assessor="Thabo Molefe, Privacy Consultant",
    )
    print(f"Assessment ID: {record.record_id}")

    # Assess Condition 1: Accountability
    engine.assess_condition(
        record.record_id,
        condition_number=1,
        status=ComplianceStatus.COMPLIANT,
        findings=[
            "Information Officer designated: Advocate Nomsa Dlamini",
            "IO registered with Information Regulator on 2024-09-15",
            "Two Deputy Information Officers appointed for HR and IT divisions",
            "POPIA compliance programme documented and approved by board",
        ],
        gaps=[],
        evidence=["IO registration certificate", "Board resolution 2024-07-01"],
        assessor="Thabo Molefe",
    )

    # Assess Condition 7: Security Safeguards
    engine.assess_condition(
        record.record_id,
        condition_number=7,
        status=ComplianceStatus.PARTIAL,
        findings=[
            "ISO 27001 certification in place for IT infrastructure",
            "Encryption at rest and in transit implemented",
            "Operator agreements in place with 12 of 15 operators",
        ],
        gaps=[
            "Three operator agreements missing Section 21 mandatory clauses",
            "Breach notification procedure not tested via simulation exercise",
        ],
        evidence=["ISO 27001 certificate", "Operator agreement register"],
        assessor="Thabo Molefe",
    )

    # Record a cross-border transfer
    transfer = engine.evaluate_cross_border_transfer(
        record.record_id,
        recipient="CloudVault EU BV",
        country="Netherlands",
        mechanism=TransferMechanism.ADEQUACY,
        data_categories=["customer_financial_data", "employee_payroll"],
        adequacy_notes="EU/EEA — GDPR provides adequate protection substantially similar to POPIA",
        approver="Advocate Nomsa Dlamini, Information Officer",
    )
    print(f"Transfer ID: {transfer.transfer_id}")

    # Calculate overall compliance
    summary = engine.calculate_overall_compliance(record.record_id)
    print(f"\n=== POPIA Compliance Summary ===")
    print(json.dumps(summary, indent=2))
