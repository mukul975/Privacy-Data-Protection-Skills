#!/usr/bin/env python3
"""
Sub-Processor Management — Tracking and Compliance Engine

Implements sub-processor authorization workflows, notification tracking,
objection management, and flow-down compliance verification per GDPR Article 28(2)/(4).
"""

import json
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class AuthorizationType(Enum):
    SPECIFIC = "prior_specific"
    GENERAL = "general_written"


class NotificationStatus(Enum):
    RECEIVED = "received"
    UNDER_REVIEW = "under_review"
    NO_OBJECTION = "no_objection"
    CONDITIONAL_APPROVAL = "conditional_approval"
    OBJECTED = "objected"
    NEGOTIATING = "negotiating"
    RESOLVED = "resolved"
    ESCALATED = "escalated"


class FlowDownStatus(Enum):
    COMPLIANT = "compliant"
    PARTIALLY_COMPLIANT = "partially_compliant"
    NON_COMPLIANT = "non_compliant"
    NOT_ASSESSED = "not_assessed"


class ReconciliationFinding(Enum):
    MATCH = "match"
    ADDED_WITHOUT_NOTICE = "added_without_notice"
    REMOVED_WITHOUT_NOTICE = "removed_without_notice"
    DETAILS_CHANGED = "details_changed"
    ADMINISTRATIVE = "administrative"


@dataclass
class SubProcessorRecord:
    """A sub-processor in the processing chain."""
    sub_processor_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    processor_id: str = ""
    processor_name: str = ""
    name: str = ""
    jurisdiction: str = ""
    processing_location: str = ""
    processing_function: str = ""
    data_access_scope: list[str] = field(default_factory=list)
    transfer_mechanism: str = "N/A — within EEA"
    certifications: list[str] = field(default_factory=list)
    authorization_type: str = AuthorizationType.GENERAL.value
    authorization_date: Optional[str] = None
    dpa_executed: bool = False
    dpa_execution_date: Optional[str] = None
    risk_classification: str = "standard"
    last_review_date: Optional[str] = None
    active: bool = True


@dataclass
class ChangeNotification:
    """A sub-processor change notification from a processor."""
    notification_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    processor_id: str = ""
    processor_name: str = ""
    change_type: str = "addition"  # addition, replacement, removal
    sub_processor_name: str = ""
    sub_processor_jurisdiction: str = ""
    sub_processor_location: str = ""
    sub_processor_function: str = ""
    data_access_scope: list[str] = field(default_factory=list)
    transfer_mechanism: str = ""
    certifications: list[str] = field(default_factory=list)
    proposed_engagement_date: str = ""
    notification_received_date: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    objection_deadline: str = ""
    status: str = NotificationStatus.RECEIVED.value
    objection_grounds: str = ""
    conditions: list[str] = field(default_factory=list)
    resolution_notes: str = ""


@dataclass
class FlowDownAssessment:
    """Assessment of flow-down obligation compliance for a sub-processor DPA."""
    assessment_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    sub_processor_id: str = ""
    sub_processor_name: str = ""
    assessment_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    obligations: dict = field(default_factory=dict)
    overall_status: str = FlowDownStatus.NOT_ASSESSED.value
    findings: list[str] = field(default_factory=list)
    remediation_required: bool = False
    remediation_deadline: Optional[str] = None


FLOW_DOWN_OBLIGATIONS = [
    "documented_instructions",
    "confidentiality",
    "security_measures",
    "further_sub_processing",
    "dsr_assistance",
    "compliance_assistance",
    "deletion_return",
    "audit_rights",
    "breach_notification",
]


class SubProcessorManagementEngine:
    """
    Manages the sub-processor lifecycle including authorization,
    notification tracking, objection handling, and flow-down compliance.
    """

    def __init__(self, objection_period_days: int = 30):
        self.sub_processors: dict[str, SubProcessorRecord] = {}
        self.notifications: list[ChangeNotification] = []
        self.flow_down_assessments: list[FlowDownAssessment] = []
        self.objection_period_days = objection_period_days

    def register_sub_processor(self, record: SubProcessorRecord) -> str:
        """Add a sub-processor to the register."""
        self.sub_processors[record.sub_processor_id] = record
        return record.sub_processor_id

    def receive_notification(self, notification: ChangeNotification) -> ChangeNotification:
        """Process an incoming sub-processor change notification."""
        received = datetime.fromisoformat(notification.notification_received_date.replace("Z", "+00:00"))
        notification.objection_deadline = (
            received + timedelta(days=self.objection_period_days)
        ).isoformat()
        notification.status = NotificationStatus.UNDER_REVIEW.value
        self.notifications.append(notification)
        return notification

    def assess_notification_risk(self, notification_id: str) -> dict:
        """Evaluate risk factors for a sub-processor change notification."""
        notification = None
        for n in self.notifications:
            if n.notification_id == notification_id:
                notification = n
                break

        if not notification:
            raise ValueError(f"Notification {notification_id} not found")

        risk_factors = []
        risk_score = 0

        eea_countries = {
            "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
            "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
            "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta",
            "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia",
            "Spain", "Sweden", "Iceland", "Liechtenstein", "Norway",
        }

        if notification.sub_processor_jurisdiction not in eea_countries:
            risk_factors.append("Third-country jurisdiction — transfer mechanism required")
            risk_score += 3

        if not notification.certifications:
            risk_factors.append("No security certifications reported")
            risk_score += 2

        sensitive_categories = {"health_data", "biometric_data", "financial_data", "location_data"}
        if sensitive_categories.intersection(set(notification.data_access_scope)):
            risk_factors.append("Access to sensitive data categories")
            risk_score += 2

        if notification.transfer_mechanism == "" and notification.sub_processor_jurisdiction not in eea_countries:
            risk_factors.append("No transfer mechanism specified for third-country transfer")
            risk_score += 4

        if risk_score >= 5:
            recommendation = "OBJECT — significant data protection concerns"
        elif risk_score >= 3:
            recommendation = "CONDITIONAL APPROVAL — require supplementary measures"
        else:
            recommendation = "NO OBJECTION — acceptable risk level"

        return {
            "notification_id": notification_id,
            "sub_processor": notification.sub_processor_name,
            "risk_score": risk_score,
            "risk_factors": risk_factors,
            "recommendation": recommendation,
            "objection_deadline": notification.objection_deadline,
        }

    def issue_decision(
        self,
        notification_id: str,
        decision: NotificationStatus,
        grounds: str = "",
        conditions: list[str] = None,
    ) -> str:
        """Issue a decision on a sub-processor change notification."""
        notification = None
        for n in self.notifications:
            if n.notification_id == notification_id:
                notification = n
                break

        if not notification:
            raise ValueError(f"Notification {notification_id} not found")

        notification.status = decision.value
        notification.objection_grounds = grounds
        notification.conditions = conditions or []

        if decision == NotificationStatus.NO_OBJECTION:
            record = SubProcessorRecord(
                processor_id=notification.processor_id,
                processor_name=notification.processor_name,
                name=notification.sub_processor_name,
                jurisdiction=notification.sub_processor_jurisdiction,
                processing_location=notification.sub_processor_location,
                processing_function=notification.sub_processor_function,
                data_access_scope=notification.data_access_scope,
                transfer_mechanism=notification.transfer_mechanism,
                certifications=notification.certifications,
                authorization_type=AuthorizationType.GENERAL.value,
                authorization_date=datetime.now(timezone.utc).isoformat(),
            )
            self.register_sub_processor(record)

        return notification.status

    def assess_flow_down(
        self, sub_processor_id: str, obligation_status: dict
    ) -> FlowDownAssessment:
        """Assess flow-down obligation compliance for a sub-processor."""
        sp = self.sub_processors.get(sub_processor_id)
        if not sp:
            raise ValueError(f"Sub-processor {sub_processor_id} not found")

        assessment = FlowDownAssessment(
            sub_processor_id=sub_processor_id,
            sub_processor_name=sp.name,
        )

        findings = []
        non_compliant_count = 0

        for obligation in FLOW_DOWN_OBLIGATIONS:
            status = obligation_status.get(obligation, FlowDownStatus.NOT_ASSESSED.value)
            assessment.obligations[obligation] = status

            if status == FlowDownStatus.NON_COMPLIANT.value:
                non_compliant_count += 1
                findings.append(f"CRITICAL: {obligation} obligation is non-compliant in sub-processor DPA")
            elif status == FlowDownStatus.PARTIALLY_COMPLIANT.value:
                findings.append(f"MAJOR: {obligation} obligation is partially compliant — remediation needed")

        if non_compliant_count > 0:
            assessment.overall_status = FlowDownStatus.NON_COMPLIANT.value
            assessment.remediation_required = True
            assessment.remediation_deadline = (
                datetime.now(timezone.utc) + timedelta(days=30)
            ).isoformat()
        elif any(
            s == FlowDownStatus.PARTIALLY_COMPLIANT.value
            for s in assessment.obligations.values()
        ):
            assessment.overall_status = FlowDownStatus.PARTIALLY_COMPLIANT.value
            assessment.remediation_required = True
            assessment.remediation_deadline = (
                datetime.now(timezone.utc) + timedelta(days=60)
            ).isoformat()
        else:
            assessment.overall_status = FlowDownStatus.COMPLIANT.value

        assessment.findings = findings
        self.flow_down_assessments.append(assessment)
        return assessment

    def reconcile_register(
        self, processor_id: str, processor_reported_list: list[dict]
    ) -> list[dict]:
        """Compare processor-reported sub-processor list against internal register."""
        registered = {
            sp.name: sp
            for sp in self.sub_processors.values()
            if sp.processor_id == processor_id and sp.active
        }
        reported = {item["name"]: item for item in processor_reported_list}

        findings = []

        for name, item in reported.items():
            if name not in registered:
                findings.append({
                    "sub_processor": name,
                    "finding": ReconciliationFinding.ADDED_WITHOUT_NOTICE.value,
                    "severity": "high",
                    "action_required": "Require retrospective notification and assessment",
                })
            else:
                sp = registered[name]
                if (
                    item.get("location") != sp.processing_location
                    or item.get("function") != sp.processing_function
                ):
                    findings.append({
                        "sub_processor": name,
                        "finding": ReconciliationFinding.DETAILS_CHANGED.value,
                        "severity": "medium",
                        "action_required": "Verify change was notified; update register",
                    })
                else:
                    findings.append({
                        "sub_processor": name,
                        "finding": ReconciliationFinding.MATCH.value,
                        "severity": "none",
                        "action_required": "None",
                    })

        for name in registered:
            if name not in reported:
                findings.append({
                    "sub_processor": name,
                    "finding": ReconciliationFinding.REMOVED_WITHOUT_NOTICE.value,
                    "severity": "medium",
                    "action_required": "Confirm removal with processor; verify data deletion",
                })

        return findings

    def get_register_summary(self, processor_id: str = None) -> dict:
        """Generate a summary of the sub-processor register."""
        sps = list(self.sub_processors.values())
        if processor_id:
            sps = [sp for sp in sps if sp.processor_id == processor_id]

        active = [sp for sp in sps if sp.active]
        return {
            "total_sub_processors": len(active),
            "by_risk": {
                "high": len([sp for sp in active if sp.risk_classification == "high"]),
                "standard": len([sp for sp in active if sp.risk_classification == "standard"]),
                "low": len([sp for sp in active if sp.risk_classification == "low"]),
            },
            "with_dpa": len([sp for sp in active if sp.dpa_executed]),
            "without_dpa": len([sp for sp in active if not sp.dpa_executed]),
            "eea_only": len([
                sp for sp in active
                if sp.transfer_mechanism == "N/A — within EEA"
            ]),
            "third_country": len([
                sp for sp in active
                if sp.transfer_mechanism != "N/A — within EEA"
            ]),
            "pending_notifications": len([
                n for n in self.notifications
                if n.status == NotificationStatus.UNDER_REVIEW.value
            ]),
        }


if __name__ == "__main__":
    engine = SubProcessorManagementEngine(objection_period_days=30)

    # Register existing approved sub-processors for NimbusAnalytics
    existing_sps = [
        SubProcessorRecord(
            processor_id="nimbus-001",
            processor_name="NimbusAnalytics GmbH",
            name="AWS EU (Frankfurt)",
            jurisdiction="Germany",
            processing_location="Frankfurt, Germany",
            processing_function="Cloud hosting and managed database services",
            data_access_scope=["all_categories_per_dpa"],
            certifications=["ISO 27001", "SOC 2 Type II", "ISO 27017", "ISO 27018"],
            authorization_date="2026-01-15",
            dpa_executed=True,
            dpa_execution_date="2026-01-10",
        ),
        SubProcessorRecord(
            processor_id="nimbus-001",
            processor_name="NimbusAnalytics GmbH",
            name="Elastic Cloud B.V.",
            jurisdiction="Netherlands",
            processing_location="Amsterdam, Netherlands",
            processing_function="Log analytics and search indexing",
            data_access_scope=["usage_data", "device_information"],
            certifications=["SOC 2 Type II", "ISO 27001"],
            authorization_date="2026-01-15",
            dpa_executed=True,
            dpa_execution_date="2026-01-12",
        ),
    ]

    for sp in existing_sps:
        engine.register_sub_processor(sp)

    # Receive a sub-processor change notification
    notification = ChangeNotification(
        processor_id="nimbus-001",
        processor_name="NimbusAnalytics GmbH",
        change_type="addition",
        sub_processor_name="Datastream Analytics Inc.",
        sub_processor_jurisdiction="United States",
        sub_processor_location="AWS us-east-1, Virginia, USA",
        sub_processor_function="Real-time event processing and aggregation",
        data_access_scope=["usage_data", "device_information", "account_identifiers"],
        transfer_mechanism="EU-US Data Privacy Framework",
        certifications=["SOC 2 Type II"],
        proposed_engagement_date="2026-05-01",
    )
    notification = engine.receive_notification(notification)
    print(f"Notification received: {notification.notification_id}")
    print(f"Objection deadline: {notification.objection_deadline}")

    # Assess risk
    risk = engine.assess_notification_risk(notification.notification_id)
    print(f"\nRisk Assessment:")
    print(json.dumps(risk, indent=2))

    # Issue decision (conditional approval in this case)
    engine.issue_decision(
        notification.notification_id,
        NotificationStatus.CONDITIONAL_APPROVAL,
        grounds="US jurisdiction requires verification of DPF certification and supplementary measures",
        conditions=[
            "Verify active EU-US DPF certification before engagement",
            "Require encryption of all data at rest with AES-256",
            "Require contractual commitment to notify of any DPF certification changes",
        ],
    )

    # Perform flow-down assessment on existing sub-processor
    sp_id = existing_sps[0].sub_processor_id
    flow_down = engine.assess_flow_down(sp_id, {
        "documented_instructions": FlowDownStatus.COMPLIANT.value,
        "confidentiality": FlowDownStatus.COMPLIANT.value,
        "security_measures": FlowDownStatus.COMPLIANT.value,
        "further_sub_processing": FlowDownStatus.COMPLIANT.value,
        "dsr_assistance": FlowDownStatus.COMPLIANT.value,
        "compliance_assistance": FlowDownStatus.COMPLIANT.value,
        "deletion_return": FlowDownStatus.COMPLIANT.value,
        "audit_rights": FlowDownStatus.PARTIALLY_COMPLIANT.value,
        "breach_notification": FlowDownStatus.COMPLIANT.value,
    })
    print(f"\nFlow-Down Assessment: {flow_down.overall_status}")
    for f in flow_down.findings:
        print(f"  {f}")

    # Register summary
    summary = engine.get_register_summary("nimbus-001")
    print(f"\n=== Sub-Processor Register Summary ===")
    print(json.dumps(summary, indent=2))
