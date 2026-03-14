"""
NIST Privacy Framework IDENTIFY Function — Assessment Processor

Automates the privacy risk identification process including data action
inventorying, problematic data action screening, and risk scoring aligned
with NIST Privacy Framework subcategories ID.BE, ID.DA, ID.IM, and ID.RA.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
import json
import uuid


class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ResponseStrategy(Enum):
    MITIGATE = "mitigate"
    TRANSFER = "transfer"
    AVOID = "avoid"
    ACCEPT = "accept"


class OrganizationalRole(Enum):
    CONTROLLER = "controller"
    PROCESSOR = "processor"
    JOINT_CONTROLLER = "joint_controller"


PROBLEMATIC_DATA_ACTIONS = [
    "appropriation",
    "distortion",
    "induced_disclosure",
    "insecurity",
    "re-identification",
    "stigmatization",
    "surveillance",
    "unanticipated_revelation",
    "unwarranted_restriction",
]


@dataclass
class DataAction:
    action_id: str
    name: str
    description: str
    data_categories: list[str]
    data_subjects: list[str]
    systems: list[str]
    owner: str
    legal_basis: str
    retention_period: str
    organizational_role: OrganizationalRole
    third_party_sharing: bool = False
    cross_border_transfer: bool = False


@dataclass
class ProblematicDataAction:
    pda_type: str
    description: str
    affected_data_action: str
    likelihood: int  # 1-5
    impact: int  # 1-5
    risk_score: int = 0
    risk_level: RiskLevel = RiskLevel.LOW

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
class RiskResponse:
    risk_id: str
    strategy: ResponseStrategy
    controls: list[str]
    owner: str
    deadline: datetime
    residual_risk_level: RiskLevel
    rationale: str


@dataclass
class IdentifyAssessment:
    assessment_id: str
    organization: str
    scope: str
    assessed_by: str
    assessment_date: datetime
    data_actions: list[DataAction] = field(default_factory=list)
    problematic_data_actions: list[ProblematicDataAction] = field(default_factory=list)
    risk_responses: list[RiskResponse] = field(default_factory=list)


class IdentifyFunctionProcessor:
    """
    Process NIST Privacy Framework IDENTIFY function assessments.

    Automates:
    - Data action inventory compilation (ID.DA)
    - Problematic data action screening (ID.RA-P1)
    - Risk scoring and prioritization (ID.RA-P3)
    - Business environment analysis (ID.BE)
    """

    def __init__(self, organization: str):
        self.organization = organization

    def create_assessment(self, scope: str, assessed_by: str) -> IdentifyAssessment:
        """Create a new IDENTIFY function assessment."""
        return IdentifyAssessment(
            assessment_id=str(uuid.uuid4()),
            organization=self.organization,
            scope=scope,
            assessed_by=assessed_by,
            assessment_date=datetime.now(timezone.utc),
        )

    def add_data_action(
        self,
        assessment: IdentifyAssessment,
        name: str,
        description: str,
        data_categories: list[str],
        data_subjects: list[str],
        systems: list[str],
        owner: str,
        legal_basis: str,
        retention_period: str,
        role: OrganizationalRole,
        third_party_sharing: bool = False,
        cross_border_transfer: bool = False,
    ) -> DataAction:
        """Add a data action to the assessment inventory (ID.DA-P1)."""
        action = DataAction(
            action_id=str(uuid.uuid4()),
            name=name,
            description=description,
            data_categories=data_categories,
            data_subjects=data_subjects,
            systems=systems,
            owner=owner,
            legal_basis=legal_basis,
            retention_period=retention_period,
            organizational_role=role,
            third_party_sharing=third_party_sharing,
            cross_border_transfer=cross_border_transfer,
        )
        assessment.data_actions.append(action)
        return action

    def screen_problematic_data_actions(
        self, assessment: IdentifyAssessment
    ) -> list[ProblematicDataAction]:
        """
        Screen data actions for problematic data actions (ID.RA-P1).

        Evaluates each data action against the NIST catalog of
        problematic data actions and assigns initial risk scores.
        """
        findings = []

        for action in assessment.data_actions:
            # Check for re-identification risk
            if any(
                cat in action.data_categories
                for cat in ["pseudonymized_data", "anonymized_data", "aggregated_data"]
            ):
                pda = ProblematicDataAction(
                    pda_type="re-identification",
                    description=f"Risk of re-identification in '{action.name}' processing pseudonymized/anonymized data",
                    affected_data_action=action.action_id,
                    likelihood=3,
                    impact=4,
                )
                findings.append(pda)

            # Check for surveillance risk
            if any(
                cat in action.data_categories
                for cat in ["location_data", "device_data", "browsing_history", "biometric_data"]
            ):
                pda = ProblematicDataAction(
                    pda_type="surveillance",
                    description=f"Surveillance risk in '{action.name}' processing tracking-capable data",
                    affected_data_action=action.action_id,
                    likelihood=3,
                    impact=4,
                )
                findings.append(pda)

            # Check for insecurity risk based on third-party sharing
            if action.third_party_sharing:
                pda = ProblematicDataAction(
                    pda_type="insecurity",
                    description=f"Insecurity risk from third-party data sharing in '{action.name}'",
                    affected_data_action=action.action_id,
                    likelihood=3,
                    impact=3,
                )
                findings.append(pda)

            # Check for unanticipated revelation in cross-border transfers
            if action.cross_border_transfer:
                pda = ProblematicDataAction(
                    pda_type="unanticipated_revelation",
                    description=f"Risk of unanticipated data exposure from cross-border transfer in '{action.name}'",
                    affected_data_action=action.action_id,
                    likelihood=2,
                    impact=4,
                )
                findings.append(pda)

            # Check for induced disclosure from data collection
            if any(
                cat in action.data_categories
                for cat in ["health_data", "financial_data", "genetic_data", "biometric_data"]
            ):
                pda = ProblematicDataAction(
                    pda_type="induced_disclosure",
                    description=f"Risk of induced disclosure of sensitive data in '{action.name}'",
                    affected_data_action=action.action_id,
                    likelihood=2,
                    impact=5,
                )
                findings.append(pda)

        assessment.problematic_data_actions = findings
        return findings

    def prioritize_risks(
        self, assessment: IdentifyAssessment
    ) -> list[ProblematicDataAction]:
        """Prioritize identified risks by score (ID.RA-P3)."""
        return sorted(
            assessment.problematic_data_actions,
            key=lambda p: p.risk_score,
            reverse=True,
        )

    def add_risk_response(
        self,
        assessment: IdentifyAssessment,
        pda: ProblematicDataAction,
        strategy: ResponseStrategy,
        controls: list[str],
        owner: str,
        deadline: datetime,
        residual_risk: RiskLevel,
        rationale: str,
    ) -> RiskResponse:
        """Add a risk response for a problematic data action (ID.RA-P3)."""
        response = RiskResponse(
            risk_id=str(uuid.uuid4()),
            strategy=strategy,
            controls=controls,
            owner=owner,
            deadline=deadline,
            residual_risk_level=residual_risk,
            rationale=rationale,
        )
        assessment.risk_responses.append(response)
        return response

    def generate_report(self, assessment: IdentifyAssessment) -> dict:
        """Generate the IDENTIFY function assessment report."""
        prioritized = self.prioritize_risks(assessment)

        return {
            "assessment_id": assessment.assessment_id,
            "organization": assessment.organization,
            "scope": assessment.scope,
            "assessed_by": assessment.assessed_by,
            "date": assessment.assessment_date.isoformat(),
            "summary": {
                "total_data_actions": len(assessment.data_actions),
                "total_problematic_data_actions": len(assessment.problematic_data_actions),
                "risk_distribution": {
                    "critical": sum(1 for p in prioritized if p.risk_level == RiskLevel.CRITICAL),
                    "high": sum(1 for p in prioritized if p.risk_level == RiskLevel.HIGH),
                    "medium": sum(1 for p in prioritized if p.risk_level == RiskLevel.MEDIUM),
                    "low": sum(1 for p in prioritized if p.risk_level == RiskLevel.LOW),
                },
                "total_risk_responses": len(assessment.risk_responses),
            },
            "data_actions": [
                {
                    "id": da.action_id,
                    "name": da.name,
                    "owner": da.owner,
                    "role": da.organizational_role.value,
                    "data_categories": da.data_categories,
                    "third_party_sharing": da.third_party_sharing,
                    "cross_border_transfer": da.cross_border_transfer,
                }
                for da in assessment.data_actions
            ],
            "prioritized_risks": [
                {
                    "type": p.pda_type,
                    "description": p.description,
                    "risk_score": p.risk_score,
                    "risk_level": p.risk_level.value,
                    "likelihood": p.likelihood,
                    "impact": p.impact,
                }
                for p in prioritized
            ],
        }


if __name__ == "__main__":
    processor = IdentifyFunctionProcessor("Cipher Engineering Labs")
    assessment = processor.create_assessment(
        scope="Privacy Analytics Platform",
        assessed_by="Privacy Engineering Team",
    )

    processor.add_data_action(
        assessment,
        name="Customer profile data collection",
        description="Collection of customer profile information during account registration",
        data_categories=["contact_information", "professional_information"],
        data_subjects=["customers"],
        systems=["registration-service", "customer-db"],
        owner="Product Team",
        legal_basis="consent",
        retention_period="Duration of account + 3 years",
        role=OrganizationalRole.CONTROLLER,
    )

    processor.add_data_action(
        assessment,
        name="Usage analytics processing",
        description="Processing of platform usage data for product improvement",
        data_categories=["usage_data", "device_data", "browsing_history"],
        data_subjects=["customers"],
        systems=["analytics-pipeline", "data-warehouse"],
        owner="Data Team",
        legal_basis="legitimate_interest",
        retention_period="26 months",
        role=OrganizationalRole.CONTROLLER,
        third_party_sharing=True,
    )

    findings = processor.screen_problematic_data_actions(assessment)
    report = processor.generate_report(assessment)
    print(json.dumps(report, indent=2))
