"""
LINDDUN Privacy Threat Modeling — Automated Threat Assessment

Implements systematic privacy threat identification using the LINDDUN
methodology: Linking, Identifying, Non-repudiation, Detecting,
Data Disclosure, Unawareness, Non-compliance.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
import json
import uuid


class ThreatCategory(Enum):
    LINKING = "L"
    IDENTIFYING = "I"
    NON_REPUDIATION = "N"
    DETECTING = "D_detect"
    DATA_DISCLOSURE = "D_disclose"
    UNAWARENESS = "U"
    NON_COMPLIANCE = "N_comply"


class DFDElementType(Enum):
    DATA_FLOW = "data_flow"
    DATA_STORE = "data_store"
    PROCESS = "process"
    EXTERNAL_ENTITY = "external_entity"


class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class MitigationStatus(Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    IMPLEMENTED = "implemented"
    ACCEPTED = "accepted"


# Mapping of which threat categories apply to which DFD element types
THREAT_APPLICABILITY = {
    DFDElementType.DATA_FLOW: [
        ThreatCategory.LINKING,
        ThreatCategory.IDENTIFYING,
        ThreatCategory.DETECTING,
        ThreatCategory.DATA_DISCLOSURE,
    ],
    DFDElementType.DATA_STORE: [
        ThreatCategory.LINKING,
        ThreatCategory.IDENTIFYING,
        ThreatCategory.DATA_DISCLOSURE,
        ThreatCategory.NON_COMPLIANCE,
    ],
    DFDElementType.PROCESS: [
        ThreatCategory.LINKING,
        ThreatCategory.IDENTIFYING,
        ThreatCategory.NON_REPUDIATION,
        ThreatCategory.DETECTING,
        ThreatCategory.DATA_DISCLOSURE,
        ThreatCategory.UNAWARENESS,
        ThreatCategory.NON_COMPLIANCE,
    ],
    DFDElementType.EXTERNAL_ENTITY: [
        ThreatCategory.IDENTIFYING,
        ThreatCategory.DETECTING,
        ThreatCategory.DATA_DISCLOSURE,
        ThreatCategory.UNAWARENESS,
        ThreatCategory.NON_COMPLIANCE,
    ],
}

MITIGATION_CATALOG = {
    ThreatCategory.LINKING: [
        "Data minimization — collect only necessary attributes",
        "Pseudonymization — replace identifiers with tokens",
        "Session unlinkability — rotate session tokens",
        "Aggregation — enforce minimum group sizes for queries",
        "Mix networks — obscure communication patterns",
    ],
    ThreatCategory.IDENTIFYING: [
        "Anonymization — remove direct identifiers",
        "k-Anonymity — generalize quasi-identifiers",
        "Differential privacy — add calibrated noise",
        "Data masking — replace with synthetic values",
        "Access control — restrict who can see raw data",
    ],
    ThreatCategory.NON_REPUDIATION: [
        "Group signatures — hide individual in group",
        "Minimal logging — log only legally required events",
        "Aggregate reporting — report at group level",
        "Configurable receipts — allow opt-out of confirmations",
    ],
    ThreatCategory.DETECTING: [
        "Traffic padding — generate dummy traffic",
        "Constant-time operations — prevent timing analysis",
        "Differential privacy — prevent membership inference",
        "Oblivious RAM — hide access patterns",
    ],
    ThreatCategory.DATA_DISCLOSURE: [
        "Encryption at rest — AES-256 for stored PII",
        "Encryption in transit — TLS 1.3",
        "Access control — enforce least privilege",
        "DLP — deploy data loss prevention tools",
        "API field filtering — return only requested fields",
    ],
    ThreatCategory.UNAWARENESS: [
        "Layered privacy notices — progressive disclosure",
        "Privacy dashboard — centralized data visibility",
        "Consent management — granular, informed consent",
        "Explainable AI — algorithmic transparency",
        "Self-service portal — easy rights exercise",
    ],
    ThreatCategory.NON_COMPLIANCE: [
        "Legal basis mapping — document basis per processing activity",
        "Automated retention — enforce deletion schedules",
        "DPIA process — mandatory for high-risk processing",
        "Regulatory monitoring — track legal developments",
        "Compliance audits — annual verification",
    ],
}


@dataclass
class DFDElement:
    element_id: str
    name: str
    element_type: DFDElementType
    description: str
    data_types: list[str]
    trust_boundary: str


@dataclass
class PrivacyThreat:
    threat_id: str
    category: ThreatCategory
    element: DFDElement
    description: str
    likelihood: int  # 1-5
    impact: int  # 1-5
    risk_score: int = 0
    risk_level: RiskLevel = RiskLevel.LOW
    mitigations: list[str] = field(default_factory=list)
    mitigation_status: MitigationStatus = MitigationStatus.NOT_STARTED
    owner: Optional[str] = None

    def __post_init__(self):
        self.risk_score = self.likelihood * self.impact
        if self.risk_score >= 20:
            self.risk_level = RiskLevel.CRITICAL
        elif self.risk_score >= 12:
            self.risk_level = RiskLevel.HIGH
        elif self.risk_score >= 6:
            self.risk_level = RiskLevel.MEDIUM
        else:
            self.risk_level = RiskLevel.LOW


@dataclass
class ThreatModel:
    model_id: str
    system_name: str
    version: str
    created_by: str
    created_at: datetime
    elements: list[DFDElement] = field(default_factory=list)
    threats: list[PrivacyThreat] = field(default_factory=list)


class LINDDUNAnalyzer:
    """
    Perform LINDDUN privacy threat analysis on a system model.
    """

    def __init__(self, system_name: str, analyst: str):
        self.model = ThreatModel(
            model_id=str(uuid.uuid4()),
            system_name=system_name,
            version="1.0",
            created_by=analyst,
            created_at=datetime.now(timezone.utc),
        )

    def add_element(
        self,
        name: str,
        element_type: DFDElementType,
        description: str,
        data_types: list[str],
        trust_boundary: str = "internal",
    ) -> DFDElement:
        """Add a DFD element to the threat model."""
        element = DFDElement(
            element_id=str(uuid.uuid4()),
            name=name,
            element_type=element_type,
            description=description,
            data_types=data_types,
            trust_boundary=trust_boundary,
        )
        self.model.elements.append(element)
        return element

    def identify_threats(self) -> list[PrivacyThreat]:
        """
        Systematically identify threats by mapping LINDDUN categories
        to each DFD element based on applicability rules.
        """
        threats = []

        for element in self.model.elements:
            applicable = THREAT_APPLICABILITY.get(element.element_type, [])

            for category in applicable:
                threat = self._create_threat(element, category)
                if threat:
                    threats.append(threat)

        self.model.threats = threats
        return threats

    def _create_threat(
        self, element: DFDElement, category: ThreatCategory
    ) -> Optional[PrivacyThreat]:
        """Create a threat instance for an element and category."""
        category_names = {
            ThreatCategory.LINKING: "Linking",
            ThreatCategory.IDENTIFYING: "Identifying",
            ThreatCategory.NON_REPUDIATION: "Non-repudiation",
            ThreatCategory.DETECTING: "Detecting",
            ThreatCategory.DATA_DISCLOSURE: "Data Disclosure",
            ThreatCategory.UNAWARENESS: "Unawareness",
            ThreatCategory.NON_COMPLIANCE: "Non-compliance",
        }

        # Base likelihood and impact adjusted by data sensitivity
        base_likelihood = 3
        base_impact = 3

        sensitive_types = {"health_data", "financial_data", "biometric_data", "genetic_data", "location_data"}
        has_sensitive = bool(set(element.data_types) & sensitive_types)

        if has_sensitive:
            base_impact = min(5, base_impact + 1)

        if element.trust_boundary == "external":
            base_likelihood = min(5, base_likelihood + 1)

        description = (
            f"{category_names[category]} threat on {element.element_type.value} "
            f"'{element.name}': potential {category_names[category].lower()} "
            f"of {', '.join(element.data_types)}"
        )

        return PrivacyThreat(
            threat_id=str(uuid.uuid4()),
            category=category,
            element=element,
            description=description,
            likelihood=base_likelihood,
            impact=base_impact,
            mitigations=MITIGATION_CATALOG.get(category, [])[:3],
        )

    def prioritize_threats(self) -> list[PrivacyThreat]:
        """Return threats sorted by risk score (highest first)."""
        return sorted(self.model.threats, key=lambda t: t.risk_score, reverse=True)

    def generate_report(self) -> dict:
        """Generate the LINDDUN threat model report."""
        prioritized = self.prioritize_threats()

        by_category = {}
        for t in self.model.threats:
            cat = t.category.value
            by_category[cat] = by_category.get(cat, 0) + 1

        by_risk = {}
        for t in self.model.threats:
            level = t.risk_level.value
            by_risk[level] = by_risk.get(level, 0) + 1

        return {
            "model_id": self.model.model_id,
            "system": self.model.system_name,
            "analyst": self.model.created_by,
            "date": self.model.created_at.isoformat(),
            "summary": {
                "total_elements": len(self.model.elements),
                "total_threats": len(self.model.threats),
                "by_category": by_category,
                "by_risk_level": by_risk,
            },
            "top_threats": [
                {
                    "id": t.threat_id[:8],
                    "category": t.category.value,
                    "element": t.element.name,
                    "description": t.description,
                    "risk_score": t.risk_score,
                    "risk_level": t.risk_level.value,
                    "recommended_mitigations": t.mitigations,
                }
                for t in prioritized[:10]
            ],
        }


if __name__ == "__main__":
    analyzer = LINDDUNAnalyzer("Privacy Analytics Platform", "Privacy Engineering Team")

    analyzer.add_element(
        "User Registration Flow", DFDElementType.DATA_FLOW,
        "Personal data submitted during account creation",
        ["contact_information", "credentials"], "external"
    )
    analyzer.add_element(
        "Customer Database", DFDElementType.DATA_STORE,
        "Primary store for customer personal data",
        ["contact_information", "financial_data", "usage_data"], "internal"
    )
    analyzer.add_element(
        "Analytics Engine", DFDElementType.PROCESS,
        "Processes user behavior data for product analytics",
        ["usage_data", "location_data", "device_data"], "internal"
    )
    analyzer.add_element(
        "Third-Party Analytics", DFDElementType.EXTERNAL_ENTITY,
        "External analytics provider receiving aggregated data",
        ["usage_data"], "external"
    )

    analyzer.identify_threats()
    report = analyzer.generate_report()
    print(json.dumps(report, indent=2))
