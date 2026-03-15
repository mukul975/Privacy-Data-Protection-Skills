#!/usr/bin/env python3
"""
LINDDUN Privacy Threat Modeling Engine

Implements the LINDDUN methodology for systematic privacy threat
identification, risk assessment, and mitigation mapping.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class LINDDUNCategory(Enum):
    LINKING = ("L", "Linking", "Associating data items with each other or with an individual")
    IDENTIFYING = ("I", "Identifying", "Learning the identity of a data subject")
    NON_REPUDIATION = ("N", "Non-repudiation", "Unable to deny an action or association")
    DETECTING = ("D", "Detecting", "Deducing an individual is involved in a process")
    DATA_DISCLOSURE = ("DD", "Data Disclosure", "Exposing personal data to unauthorized parties")
    UNAWARENESS = ("U", "Unawareness", "Data subjects unaware of processing")
    NON_COMPLIANCE = ("NC", "Non-compliance", "Failing to comply with privacy regulations")

    def __init__(self, code: str, label: str, description: str):
        self.code = code
        self.label = label
        self._description = description


class DFDElementType(Enum):
    EXTERNAL_ENTITY = "external_entity"
    PROCESS = "process"
    DATA_STORE = "data_store"
    DATA_FLOW = "data_flow"


class RiskLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


# Mapping of which LINDDUN categories apply to which DFD element types
APPLICABILITY_MATRIX = {
    DFDElementType.EXTERNAL_ENTITY: [LINDDUNCategory.IDENTIFYING, LINDDUNCategory.UNAWARENESS],
    DFDElementType.PROCESS: [
        LINDDUNCategory.LINKING, LINDDUNCategory.IDENTIFYING, LINDDUNCategory.NON_REPUDIATION,
        LINDDUNCategory.DETECTING, LINDDUNCategory.DATA_DISCLOSURE, LINDDUNCategory.NON_COMPLIANCE,
    ],
    DFDElementType.DATA_STORE: [
        LINDDUNCategory.LINKING, LINDDUNCategory.IDENTIFYING, LINDDUNCategory.NON_REPUDIATION,
        LINDDUNCategory.DATA_DISCLOSURE, LINDDUNCategory.NON_COMPLIANCE,
    ],
    DFDElementType.DATA_FLOW: [
        LINDDUNCategory.LINKING, LINDDUNCategory.IDENTIFYING, LINDDUNCategory.NON_REPUDIATION,
        LINDDUNCategory.DETECTING, LINDDUNCategory.DATA_DISCLOSURE, LINDDUNCategory.NON_COMPLIANCE,
    ],
}


@dataclass
class DFDElement:
    """A Data Flow Diagram element."""
    element_id: str
    name: str
    element_type: DFDElementType
    data_categories: list[str] = field(default_factory=list)
    trust_boundary: str = "internal"


@dataclass
class PrivacyThreat:
    """An identified privacy threat."""
    threat_id: str
    category: LINDDUNCategory
    dfd_element: DFDElement
    description: str
    attack_scenario: str
    likelihood: int  # 1-5
    impact: int      # 1-5
    mitigation_pattern: str = ""
    mitigation_control: str = ""
    status: str = "open"

    @property
    def risk_score(self) -> int:
        return self.likelihood * self.impact

    @property
    def risk_level(self) -> RiskLevel:
        score = self.risk_score
        if score <= 6:
            return RiskLevel.LOW
        elif score <= 12:
            return RiskLevel.MEDIUM
        elif score <= 19:
            return RiskLevel.HIGH
        else:
            return RiskLevel.CRITICAL


MITIGATION_MAP = {
    LINDDUNCategory.LINKING: {
        "pattern": "HIDE + SEPARATE",
        "controls": [
            "HMAC-SHA256 pseudonymization with context-separated keys",
            "Purpose-partitioned data stores preventing cross-purpose joins",
            "Differential privacy on query outputs",
        ],
    },
    LINDDUNCategory.IDENTIFYING: {
        "pattern": "HIDE + MINIMIZE + ABSTRACT",
        "controls": [
            "Field-level encryption for direct identifiers",
            "k-anonymity (k >= 5) on published datasets",
            "Pseudonymization at analytics boundary",
        ],
    },
    LINDDUNCategory.NON_REPUDIATION: {
        "pattern": "HIDE (Mix)",
        "controls": [
            "Group signatures for authenticating actions without individual attribution",
            "Aggregated audit logs (action counts without individual linkage)",
        ],
    },
    LINDDUNCategory.DETECTING: {
        "pattern": "HIDE (Mix, Obfuscate)",
        "controls": [
            "Cover traffic to mask real communication patterns",
            "Differential privacy on membership queries",
            "Oblivious RAM for access pattern protection",
        ],
    },
    LINDDUNCategory.DATA_DISCLOSURE: {
        "pattern": "HIDE (Encrypt)",
        "controls": [
            "AES-256-GCM field-level encryption at rest",
            "TLS 1.3 for data in transit",
            "Role-based access control with purpose enforcement",
            "Dynamic data masking for non-privileged access",
        ],
    },
    LINDDUNCategory.UNAWARENESS: {
        "pattern": "INFORM",
        "controls": [
            "Layered privacy notices at all collection points",
            "Just-in-time notifications for new processing activities",
            "Privacy dashboard showing data subjects their processed data",
        ],
    },
    LINDDUNCategory.NON_COMPLIANCE: {
        "pattern": "ENFORCE + DEMONSTRATE",
        "controls": [
            "OPA policy-as-code for automated compliance enforcement",
            "Automated retention policy engine with TTL scanning",
            "Article 30 records maintained as living document",
            "Quarterly privacy audits with documented findings",
        ],
    },
}


class LINDDUNAssessment:
    """Conducts a LINDDUN privacy threat modeling assessment."""

    def __init__(self, system_name: str, organization: str = "Prism Data Systems AG"):
        self.system_name = system_name
        self.organization = organization
        self.dfd_elements: list[DFDElement] = []
        self.threats: list[PrivacyThreat] = []
        self.assessment_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    def add_dfd_element(self, element: DFDElement) -> None:
        self.dfd_elements.append(element)

    def identify_threats(self) -> list[PrivacyThreat]:
        """
        Systematically identify threats by mapping LINDDUN categories to DFD elements.
        """
        threat_counter = 0

        for element in self.dfd_elements:
            applicable_categories = APPLICABILITY_MATRIX.get(element.element_type, [])
            for category in applicable_categories:
                threat_counter += 1
                threat = self._generate_threat(
                    threat_id=f"T-{threat_counter:03d}",
                    category=category,
                    element=element,
                )
                self.threats.append(threat)

        return self.threats

    def _generate_threat(self, threat_id: str, category: LINDDUNCategory,
                         element: DFDElement) -> PrivacyThreat:
        """Generate a contextual threat based on the category and element."""
        descriptions = {
            (LINDDUNCategory.LINKING, DFDElementType.DATA_STORE):
                f"Records in {element.name} can be linked to the same individual via quasi-identifier combinations ({', '.join(element.data_categories[:3])})",
            (LINDDUNCategory.LINKING, DFDElementType.DATA_FLOW):
                f"Data flowing through {element.name} can be correlated with other data flows to link activities to individuals",
            (LINDDUNCategory.LINKING, DFDElementType.PROCESS):
                f"Process {element.name} combines data from multiple sources enabling individual-level linkage",
            (LINDDUNCategory.IDENTIFYING, DFDElementType.EXTERNAL_ENTITY):
                f"External entity {element.name} can be identified through data associated with their interactions",
            (LINDDUNCategory.IDENTIFYING, DFDElementType.DATA_STORE):
                f"Direct or quasi-identifiers in {element.name} enable re-identification of data subjects",
            (LINDDUNCategory.DATA_DISCLOSURE, DFDElementType.DATA_FLOW):
                f"Personal data in {element.name} may be exposed if transmission is not encrypted or access is unauthorized",
            (LINDDUNCategory.DATA_DISCLOSURE, DFDElementType.DATA_STORE):
                f"Personal data in {element.name} may be disclosed through unauthorized access or insufficient access controls",
            (LINDDUNCategory.UNAWARENESS, DFDElementType.EXTERNAL_ENTITY):
                f"Data subject {element.name} may be unaware of processing activities performed on their data",
            (LINDDUNCategory.NON_COMPLIANCE, DFDElementType.PROCESS):
                f"Process {element.name} may not comply with GDPR requirements for data handling",
        }

        description = descriptions.get(
            (category, element.element_type),
            f"{category.label} threat on {element.name} ({element.element_type.value})"
        )

        # Default risk scores (would be refined during assessment)
        has_special = any(cat in element.data_categories for cat in ["health_data", "biometric", "genetic"])
        base_likelihood = 3
        base_impact = 4 if has_special else 3

        mitigation_info = MITIGATION_MAP.get(category, {})

        return PrivacyThreat(
            threat_id=threat_id,
            category=category,
            dfd_element=element,
            description=description,
            attack_scenario=f"An adversary exploits {category.label.lower()} vulnerability on {element.name}",
            likelihood=base_likelihood,
            impact=base_impact,
            mitigation_pattern=mitigation_info.get("pattern", ""),
            mitigation_control=mitigation_info.get("controls", [""])[0] if mitigation_info.get("controls") else "",
        )

    def get_risk_summary(self) -> dict:
        by_level = {level: 0 for level in RiskLevel}
        by_category = {cat: 0 for cat in LINDDUNCategory}

        for threat in self.threats:
            by_level[threat.risk_level] += 1
            by_category[threat.category] += 1

        return {
            "system": self.system_name,
            "organization": self.organization,
            "assessment_date": self.assessment_date,
            "total_threats": len(self.threats),
            "by_risk_level": {level.value: count for level, count in by_level.items()},
            "by_category": {cat.code: count for cat, count in by_category.items()},
            "critical_threats": [t.threat_id for t in self.threats if t.risk_level == RiskLevel.CRITICAL],
            "high_threats": [t.threat_id for t in self.threats if t.risk_level == RiskLevel.HIGH],
        }


def run_example():
    """Demonstrate LINDDUN assessment for Prism Data Systems AG."""

    assessment = LINDDUNAssessment(
        system_name="Customer Analytics Platform",
        organization="Prism Data Systems AG",
    )

    # Define DFD elements
    elements = [
        DFDElement("EE-01", "Customer (Data Subject)", DFDElementType.EXTERNAL_ENTITY,
                   ["email", "display_name"], "external"),
        DFDElement("P-01", "API Gateway", DFDElementType.PROCESS,
                   ["email", "session_token"], "dmz"),
        DFDElement("P-02", "Analytics Engine", DFDElementType.PROCESS,
                   ["pseudonymized_id", "feature_events"], "internal"),
        DFDElement("DS-01", "Customer Database", DFDElementType.DATA_STORE,
                   ["email", "display_name", "country_code"], "internal"),
        DFDElement("DS-02", "Analytics Warehouse", DFDElementType.DATA_STORE,
                   ["pseudonymized_id", "feature_events", "session_duration"], "internal"),
        DFDElement("DF-01", "Customer -> API Gateway", DFDElementType.DATA_FLOW,
                   ["email", "credentials"], "external-to-dmz"),
        DFDElement("DF-02", "API Gateway -> Customer DB", DFDElementType.DATA_FLOW,
                   ["email", "display_name"], "dmz-to-internal"),
        DFDElement("DF-03", "Customer DB -> Analytics Engine", DFDElementType.DATA_FLOW,
                   ["pseudonymized_id", "feature_events"], "internal"),
    ]

    for elem in elements:
        assessment.add_dfd_element(elem)

    print("=== LINDDUN Privacy Threat Model ===")
    print(f"System: {assessment.system_name}")
    print(f"Organization: {assessment.organization}")
    print(f"DFD Elements: {len(assessment.dfd_elements)}")
    print()

    # Identify threats
    threats = assessment.identify_threats()
    print(f"Total threats identified: {len(threats)}")
    print()

    # Display threats sorted by risk
    sorted_threats = sorted(threats, key=lambda t: t.risk_score, reverse=True)

    print("--- Top 10 Threats by Risk Score ---")
    for threat in sorted_threats[:10]:
        print(f"  [{threat.threat_id}] {threat.category.code} - {threat.risk_level.value} "
              f"(Risk: {threat.risk_score})")
        print(f"    Element: {threat.dfd_element.name}")
        print(f"    Threat: {threat.description}")
        print(f"    Mitigation: {threat.mitigation_pattern} — {threat.mitigation_control}")
        print()

    # Risk summary
    summary = assessment.get_risk_summary()
    print("--- Risk Summary ---")
    print(f"  Total: {summary['total_threats']}")
    for level, count in summary["by_risk_level"].items():
        print(f"  {level}: {count}")
    print()
    print("  By LINDDUN category:")
    for code, count in summary["by_category"].items():
        print(f"    {code}: {count} threats")


if __name__ == "__main__":
    run_example()
