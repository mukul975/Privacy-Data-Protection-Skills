#!/usr/bin/env python3
"""
DPA Drafting — Contract Generation and Compliance Verification

Implements DPA template population, mandatory provision checking,
and compliance scoring per GDPR Article 28(3).
"""

import json
import uuid
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class DPAStatus(Enum):
    DRAFT = "draft"
    LEGAL_REVIEW = "legal_review"
    VENDOR_NEGOTIATION = "vendor_negotiation"
    DPO_APPROVAL = "dpo_approval"
    EXECUTED = "executed"
    AMENDMENT_PENDING = "amendment_pending"
    TERMINATED = "terminated"


MANDATORY_PROVISIONS = [
    {"id": "MP01", "article": "28(3)", "description": "Subject-matter and duration of processing"},
    {"id": "MP02", "article": "28(3)", "description": "Nature and purpose of processing"},
    {"id": "MP03", "article": "28(3)", "description": "Type of personal data"},
    {"id": "MP04", "article": "28(3)", "description": "Categories of data subjects"},
    {"id": "MP05", "article": "28(3)", "description": "Controller obligations and rights"},
    {"id": "MP06", "article": "28(3)(a)", "description": "Process only on documented instructions"},
    {"id": "MP07", "article": "28(3)(b)", "description": "Confidentiality of authorized personnel"},
    {"id": "MP08", "article": "28(3)(c)", "description": "Article 32 security measures"},
    {"id": "MP09", "article": "28(3)(d)", "description": "Sub-processor authorization and conditions"},
    {"id": "MP10", "article": "28(3)(e)", "description": "Assistance with data subject rights (Ch. III)"},
    {"id": "MP11", "article": "28(3)(f)", "description": "Assistance with Art. 32-36 obligations"},
    {"id": "MP12", "article": "28(3)(g)", "description": "Deletion or return upon termination"},
    {"id": "MP13", "article": "28(3)(h)", "description": "Audit rights and compliance information"},
    {"id": "MP14", "article": "28(4)", "description": "Sub-processor flow-down obligations"},
    {"id": "MP15", "article": "Ch. V", "description": "International transfer mechanism (if applicable)"},
    {"id": "MP16", "article": "33(2)", "description": "Breach notification to controller"},
    {"id": "MP17", "article": "28(9)", "description": "Written form (including electronic)"},
]


@dataclass
class ProcessingDescription:
    """Annex I — Description of Processing."""
    subject_matter: str = ""
    duration: str = ""
    nature_of_processing: list[str] = field(default_factory=list)
    purpose_of_processing: str = ""
    data_categories: list[dict] = field(default_factory=list)
    data_subject_categories: list[dict] = field(default_factory=list)
    processing_locations: list[str] = field(default_factory=list)


@dataclass
class SecurityMeasures:
    """Annex II — Technical and Organisational Measures."""
    encryption_at_rest: str = ""
    encryption_in_transit: str = ""
    access_control: str = ""
    network_security: str = ""
    physical_security: str = ""
    incident_response: str = ""
    business_continuity: str = ""
    personnel_security: str = ""
    logging_monitoring: str = ""
    vulnerability_management: str = ""


@dataclass
class SubProcessor:
    """Annex III — Approved Sub-Processor."""
    name: str = ""
    location: str = ""
    processing_description: str = ""
    transfer_mechanism: str = "N/A — within EEA"


@dataclass
class DPA:
    """Complete Data Processing Agreement record."""
    dpa_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    controller_name: str = ""
    processor_name: str = ""
    status: str = DPAStatus.DRAFT.value
    template_used: str = "summit_standard"
    processing_description: Optional[dict] = None
    security_measures: Optional[dict] = None
    sub_processors: list[dict] = field(default_factory=list)
    breach_notification_hours: int = 24
    sub_processor_notification_days: int = 30
    audit_frequency: str = "annual"
    termination_data_handling: str = "return_then_delete"
    deletion_certification_required: bool = True
    international_transfers: bool = False
    transfer_mechanism: str = ""
    provision_compliance: dict = field(default_factory=dict)
    compliance_score: float = 0.0
    created_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    executed_date: Optional[str] = None
    expiry_date: Optional[str] = None
    amendments: list[dict] = field(default_factory=list)
    drafting_notes: list[str] = field(default_factory=list)


class DPADraftingEngine:
    """
    Manages DPA drafting, compliance verification, and lifecycle.

    Handles template selection, annex population, mandatory provision
    checking, and amendment tracking.
    """

    def __init__(self):
        self.dpas: dict[str, DPA] = {}

    def create_dpa(
        self,
        controller_name: str,
        processor_name: str,
        processing: ProcessingDescription,
        security: SecurityMeasures,
        sub_processors: list[SubProcessor],
    ) -> DPA:
        """Create a new DPA with populated annexes."""
        dpa = DPA(
            controller_name=controller_name,
            processor_name=processor_name,
            processing_description=asdict(processing),
            security_measures=asdict(security),
            sub_processors=[asdict(sp) for sp in sub_processors],
            international_transfers=any(
                sp.transfer_mechanism != "N/A — within EEA" for sp in sub_processors
            ),
        )

        if dpa.international_transfers:
            dpa.transfer_mechanism = "Standard Contractual Clauses (Commission Decision 2021/914)"

        self.dpas[dpa.dpa_id] = dpa
        return dpa

    def verify_mandatory_provisions(self, dpa_id: str) -> dict:
        """Check DPA against all 17 mandatory provisions."""
        dpa = self.dpas.get(dpa_id)
        if not dpa:
            raise ValueError(f"DPA {dpa_id} not found")

        results = {}
        pd = dpa.processing_description or {}
        sm = dpa.security_measures or {}

        checks = {
            "MP01": bool(pd.get("subject_matter") and pd.get("duration")),
            "MP02": bool(pd.get("nature_of_processing") and pd.get("purpose_of_processing")),
            "MP03": bool(pd.get("data_categories")),
            "MP04": bool(pd.get("data_subject_categories")),
            "MP05": True,  # Included in standard template
            "MP06": True,  # Included in standard template — documented instructions clause
            "MP07": True,  # Included in standard template — confidentiality clause
            "MP08": bool(sm.get("encryption_at_rest") and sm.get("access_control")),
            "MP09": bool(dpa.sub_processors is not None and dpa.sub_processor_notification_days > 0),
            "MP10": True,  # Included in standard template — DSR assistance clause
            "MP11": True,  # Included in standard template — Art. 32-36 assistance clause
            "MP12": bool(dpa.termination_data_handling),
            "MP13": bool(dpa.audit_frequency),
            "MP14": bool(dpa.sub_processors is not None),
            "MP15": not dpa.international_transfers or bool(dpa.transfer_mechanism),
            "MP16": dpa.breach_notification_hours > 0,
            "MP17": True,  # DPA is in written/electronic form
        }

        for provision in MANDATORY_PROVISIONS:
            pid = provision["id"]
            results[pid] = {
                "article": provision["article"],
                "description": provision["description"],
                "compliant": checks.get(pid, False),
            }

        dpa.provision_compliance = results
        compliant_count = sum(1 for r in results.values() if r["compliant"])
        dpa.compliance_score = round(compliant_count / len(MANDATORY_PROVISIONS) * 100, 1)

        return results

    def get_compliance_summary(self, dpa_id: str) -> dict:
        """Generate compliance summary for a DPA."""
        dpa = self.dpas.get(dpa_id)
        if not dpa:
            raise ValueError(f"DPA {dpa_id} not found")

        if not dpa.provision_compliance:
            self.verify_mandatory_provisions(dpa_id)

        non_compliant = [
            {"id": pid, **details}
            for pid, details in dpa.provision_compliance.items()
            if not details["compliant"]
        ]

        return {
            "dpa_id": dpa.dpa_id,
            "controller": dpa.controller_name,
            "processor": dpa.processor_name,
            "status": dpa.status,
            "compliance_score": dpa.compliance_score,
            "total_provisions": len(MANDATORY_PROVISIONS),
            "compliant_provisions": len(MANDATORY_PROVISIONS) - len(non_compliant),
            "non_compliant_provisions": non_compliant,
            "international_transfers": dpa.international_transfers,
            "transfer_mechanism": dpa.transfer_mechanism,
            "breach_notification_hours": dpa.breach_notification_hours,
            "sub_processor_count": len(dpa.sub_processors),
        }

    def record_amendment(
        self, dpa_id: str, description: str, affected_provisions: list[str],
        amended_by: str
    ) -> dict:
        """Record a DPA amendment."""
        dpa = self.dpas.get(dpa_id)
        if not dpa:
            raise ValueError(f"DPA {dpa_id} not found")

        amendment = {
            "amendment_id": str(uuid.uuid4()),
            "date": datetime.now(timezone.utc).isoformat(),
            "description": description,
            "affected_provisions": affected_provisions,
            "amended_by": amended_by,
        }
        dpa.amendments.append(amendment)
        dpa.status = DPAStatus.AMENDMENT_PENDING.value
        return amendment

    def advance_status(self, dpa_id: str, new_status: DPAStatus) -> str:
        """Advance DPA through the drafting lifecycle."""
        dpa = self.dpas.get(dpa_id)
        if not dpa:
            raise ValueError(f"DPA {dpa_id} not found")

        valid_transitions = {
            DPAStatus.DRAFT: [DPAStatus.LEGAL_REVIEW],
            DPAStatus.LEGAL_REVIEW: [DPAStatus.VENDOR_NEGOTIATION, DPAStatus.DRAFT],
            DPAStatus.VENDOR_NEGOTIATION: [DPAStatus.DPO_APPROVAL, DPAStatus.LEGAL_REVIEW],
            DPAStatus.DPO_APPROVAL: [DPAStatus.EXECUTED, DPAStatus.VENDOR_NEGOTIATION],
            DPAStatus.EXECUTED: [DPAStatus.AMENDMENT_PENDING, DPAStatus.TERMINATED],
            DPAStatus.AMENDMENT_PENDING: [DPAStatus.EXECUTED, DPAStatus.TERMINATED],
        }

        current = DPAStatus(dpa.status)
        if new_status not in valid_transitions.get(current, []):
            raise ValueError(
                f"Cannot transition from {current.value} to {new_status.value}"
            )

        dpa.status = new_status.value
        if new_status == DPAStatus.EXECUTED:
            dpa.executed_date = datetime.now(timezone.utc).isoformat()
        return dpa.status


if __name__ == "__main__":
    engine = DPADraftingEngine()

    # Define processing details for Summit Cloud Partners <-> NimbusAnalytics GmbH
    processing = ProcessingDescription(
        subject_matter="Cloud-hosted customer behavior analytics platform providing product usage insights",
        duration="Co-terminus with Master Services Agreement dated 2026-01-15, plus 90-day data return/deletion period",
        nature_of_processing=[
            "Collection via API ingestion",
            "Storage in encrypted database",
            "Automated behavioral analysis",
            "Aggregated reporting and dashboard generation",
            "Deletion upon contract termination or controller instruction",
        ],
        purpose_of_processing=(
            "To provide Summit Cloud Partners with customer behavior analytics "
            "enabling data-driven product improvement decisions, feature prioritization, "
            "and customer experience optimization"
        ),
        data_categories=[
            {"category": "Contact information", "types": "Name, email address", "sensitivity": "Standard"},
            {"category": "Account identifiers", "types": "User ID, tenant ID", "sensitivity": "Standard"},
            {"category": "Usage data", "types": "Feature usage logs, session duration, click paths", "sensitivity": "Standard"},
            {"category": "Device information", "types": "IP address, browser type, OS version", "sensitivity": "Standard"},
            {"category": "Location data", "types": "City/region from IP geolocation", "sensitivity": "Elevated"},
        ],
        data_subject_categories=[
            {"category": "Enterprise customers", "volume": 50000},
            {"category": "Trial users", "volume": 15000},
            {"category": "API consumers", "volume": 5000},
        ],
        processing_locations=["Frankfurt, Germany", "Dublin, Ireland"],
    )

    security = SecurityMeasures(
        encryption_at_rest="AES-256-GCM via AWS KMS with customer-managed keys option",
        encryption_in_transit="TLS 1.3 for all API communications; mTLS for inter-service communication",
        access_control="RBAC with MFA enforced; quarterly access reviews; principle of least privilege",
        network_security="VPC isolation, WAF, network segmentation, DDoS protection",
        physical_security="AWS EU data centers — ISO 27001, SOC 2 certified facilities",
        incident_response="24/7 SOC, documented IRP, mean time to detect < 30 minutes",
        business_continuity="Multi-AZ deployment, RPO < 1 hour, RTO < 4 hours, annual DR testing",
        personnel_security="Background checks, annual privacy training, confidentiality agreements",
        logging_monitoring="Centralized SIEM, access logging with 12-month retention, real-time alerting",
        vulnerability_management="Weekly automated scanning, monthly manual review, annual penetration testing",
    )

    sub_processors = [
        SubProcessor(
            name="Amazon Web Services EMEA SARL (Frankfurt Region)",
            location="Frankfurt, Germany",
            processing_description="Infrastructure hosting and managed database services",
            transfer_mechanism="N/A — within EEA",
        ),
        SubProcessor(
            name="Elastic Cloud B.V.",
            location="Amsterdam, Netherlands",
            processing_description="Log analytics and search indexing",
            transfer_mechanism="N/A — within EEA",
        ),
    ]

    # Create the DPA
    dpa = engine.create_dpa(
        controller_name="Summit Cloud Partners",
        processor_name="NimbusAnalytics GmbH",
        processing=processing,
        security=security,
        sub_processors=sub_processors,
    )
    print(f"DPA created: {dpa.dpa_id}")
    print(f"Status: {dpa.status}")

    # Verify mandatory provisions
    results = engine.verify_mandatory_provisions(dpa.dpa_id)
    print(f"\nCompliance Score: {dpa.compliance_score}%")

    # Get full compliance summary
    summary = engine.get_compliance_summary(dpa.dpa_id)
    print("\n=== DPA Compliance Summary ===")
    print(json.dumps(summary, indent=2))

    # Advance through lifecycle
    engine.advance_status(dpa.dpa_id, DPAStatus.LEGAL_REVIEW)
    engine.advance_status(dpa.dpa_id, DPAStatus.VENDOR_NEGOTIATION)
    engine.advance_status(dpa.dpa_id, DPAStatus.DPO_APPROVAL)
    engine.advance_status(dpa.dpa_id, DPAStatus.EXECUTED)
    print(f"\nFinal Status: {dpa.status}")
    print(f"Executed Date: {dpa.executed_date}")
