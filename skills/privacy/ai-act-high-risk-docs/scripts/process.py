"""
EU AI Act High-Risk AI System Documentation — Classification and Compliance Tracker

Automates high-risk classification assessment, documentation completeness
checking, and conformity assessment tracking for Cerebrum AI Labs.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
import json
import uuid


class RiskClassification(Enum):
    HIGH_RISK_ANNEX_III = "high_risk_annex_iii"
    HIGH_RISK_ANNEX_I = "high_risk_annex_i"
    GPAI_SYSTEMIC = "gpai_systemic_risk"
    GPAI_STANDARD = "gpai_standard"
    LIMITED_RISK = "limited_risk"
    MINIMAL_RISK = "minimal_risk"


class ConformityType(Enum):
    INTERNAL = "internal_assessment"
    THIRD_PARTY = "third_party_notified_body"


class DocumentStatus(Enum):
    NOT_STARTED = "not_started"
    DRAFT = "draft"
    REVIEW = "in_review"
    APPROVED = "approved"
    EXPIRED = "expired"


ANNEX_III_CATEGORIES = {
    "1a": "Biometric identification and categorisation of natural persons",
    "1b": "Emotion recognition",
    "2": "Management and operation of critical infrastructure",
    "3a": "Education and vocational training — admissions and assessment",
    "3b": "Education — monitoring and detecting prohibited behaviour",
    "4a": "Employment — recruitment and selection",
    "4b": "Employment — promotion, termination, task allocation, monitoring",
    "5a": "Essential services — eligibility for public benefits",
    "5b": "Essential services — creditworthiness assessment",
    "5c": "Essential services — risk assessment and pricing for insurance",
    "6a": "Law enforcement — risk of offending or reoffending",
    "6b": "Law enforcement — polygraphs and similar tools",
    "6c": "Law enforcement — profiling in criminal investigations",
    "7a": "Migration — polygraphs and risk assessment",
    "7b": "Migration — examination of applications",
    "8a": "Administration of justice — research and interpretation of facts and law",
}

ANNEX_IV_SECTIONS = [
    "general_description",
    "intended_purpose",
    "system_elements_detail",
    "development_methodology",
    "training_data_governance",
    "validation_and_testing",
    "input_data_specifications",
    "output_description",
    "human_oversight_measures",
    "accuracy_robustness_cybersecurity",
    "risk_management_system",
    "change_management_log",
    "eu_declaration_reference",
]


@dataclass
class AISystem:
    system_id: str
    name: str
    version: str
    intended_purpose: str
    deployer: str
    classification: Optional[RiskClassification] = None
    annex_iii_category: Optional[str] = None
    conformity_type: Optional[ConformityType] = None


@dataclass
class DocumentationItem:
    section: str
    status: DocumentStatus
    owner: str
    last_updated: Optional[datetime] = None
    notes: str = ""


@dataclass
class ComplianceRecord:
    system: AISystem
    documentation: list[DocumentationItem] = field(default_factory=list)
    conformity_date: Optional[datetime] = None
    ce_marking_applied: bool = False
    eu_database_registered: bool = False


class HighRiskClassifier:
    """Classify AI systems under the EU AI Act risk framework."""

    def classify(
        self,
        system_name: str,
        intended_purpose: str,
        annex_iii_match: Optional[str],
        is_safety_component: bool,
        is_biometric: bool,
        affects_fundamental_rights: bool,
    ) -> tuple[RiskClassification, Optional[ConformityType]]:
        """
        Determine risk classification and conformity assessment type.

        Returns (classification, conformity_type).
        """
        if annex_iii_match:
            classification = RiskClassification.HIGH_RISK_ANNEX_III
            if is_biometric:
                conformity = ConformityType.THIRD_PARTY
            else:
                conformity = ConformityType.INTERNAL
            return (classification, conformity)

        if is_safety_component:
            return (RiskClassification.HIGH_RISK_ANNEX_I, ConformityType.THIRD_PARTY)

        if affects_fundamental_rights:
            return (RiskClassification.LIMITED_RISK, None)

        return (RiskClassification.MINIMAL_RISK, None)


class DocumentationTracker:
    """Track Annex IV documentation completeness for high-risk AI systems."""

    def __init__(self):
        self.records: dict[str, ComplianceRecord] = {}

    def create_record(self, system: AISystem) -> ComplianceRecord:
        """Initialize a compliance record with all required documentation sections."""
        docs = [
            DocumentationItem(
                section=section,
                status=DocumentStatus.NOT_STARTED,
                owner="",
            )
            for section in ANNEX_IV_SECTIONS
        ]

        record = ComplianceRecord(system=system, documentation=docs)
        self.records[system.system_id] = record
        return record

    def update_section(
        self, system_id: str, section: str, status: DocumentStatus, owner: str, notes: str = ""
    ) -> bool:
        """Update documentation section status."""
        record = self.records.get(system_id)
        if not record:
            return False

        for doc in record.documentation:
            if doc.section == section:
                doc.status = status
                doc.owner = owner
                doc.last_updated = datetime.now(timezone.utc)
                doc.notes = notes
                return True
        return False

    def completeness_report(self, system_id: str) -> dict:
        """Generate documentation completeness report."""
        record = self.records.get(system_id)
        if not record:
            return {"error": "System not found"}

        total = len(record.documentation)
        by_status = {}
        for doc in record.documentation:
            by_status[doc.status.value] = by_status.get(doc.status.value, 0) + 1

        approved = by_status.get("approved", 0)
        completion_rate = approved / total if total > 0 else 0

        missing = [
            doc.section for doc in record.documentation
            if doc.status == DocumentStatus.NOT_STARTED
        ]

        return {
            "system_id": record.system.system_id,
            "system_name": record.system.name,
            "classification": record.system.classification.value if record.system.classification else "unclassified",
            "total_sections": total,
            "completion_rate": f"{completion_rate*100:.0f}%",
            "status_breakdown": by_status,
            "missing_sections": missing,
            "ce_marking": record.ce_marking_applied,
            "eu_registered": record.eu_database_registered,
            "ready_for_conformity": completion_rate == 1.0,
        }


if __name__ == "__main__":
    # Classify Cerebrum AI Labs systems
    classifier = HighRiskClassifier()

    cv_class, cv_conformity = classifier.classify(
        "CV Screening AI", "Automated filtering of job applications",
        "4a", False, False, True,
    )
    print(f"CV Screening AI: {cv_class.value}, Conformity: {cv_conformity.value}")

    facial_class, facial_conformity = classifier.classify(
        "Facial Verification AI", "Identity verification at onboarding",
        "1a", False, True, True,
    )
    print(f"Facial Verification AI: {facial_class.value}, Conformity: {facial_conformity.value}")

    # Track documentation
    tracker = DocumentationTracker()

    cv_system = AISystem(
        system_id="CAL-AI-001",
        name="CV Screening AI",
        version="v2.4.1",
        intended_purpose="Automated screening and ranking of job applications",
        deployer="Cerebrum AI Labs",
        classification=cv_class,
        annex_iii_category="4a",
        conformity_type=cv_conformity,
    )

    tracker.create_record(cv_system)
    tracker.update_section("CAL-AI-001", "general_description", DocumentStatus.APPROVED, "ML Engineering")
    tracker.update_section("CAL-AI-001", "intended_purpose", DocumentStatus.APPROVED, "Product Team")
    tracker.update_section("CAL-AI-001", "training_data_governance", DocumentStatus.REVIEW, "Data Team")
    tracker.update_section("CAL-AI-001", "risk_management_system", DocumentStatus.DRAFT, "Risk Team")

    report = tracker.completeness_report("CAL-AI-001")
    print(json.dumps(report, indent=2))
