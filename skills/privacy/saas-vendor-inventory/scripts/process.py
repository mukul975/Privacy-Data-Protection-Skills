#!/usr/bin/env python3
"""
SaaS Vendor Inventory — Discovery, Tracking, and Reconciliation Engine

Implements SaaS application inventory management, shadow IT detection,
data flow mapping, and contract status tracking.
"""

import json
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class InventoryTier(Enum):
    TIER_1_SANCTIONED = "sanctioned"
    TIER_2_UNSANCTIONED = "unsanctioned"
    TIER_3_EXCLUDED = "excluded"


class DPAStatus(Enum):
    EXECUTED = "executed"
    IN_NEGOTIATION = "in_negotiation"
    NOT_REQUIRED = "not_required"
    PENDING = "pending"
    EXPIRED = "expired"


class ContractStatus(Enum):
    ACTIVE_COMPLIANT = "active_compliant"
    ACTIVE_DPA_PENDING = "active_dpa_pending"
    ACTIVE_REVIEW_OVERDUE = "active_review_overdue"
    EXPIRING = "expiring"
    EXPIRED = "expired"
    SUSPENDED = "suspended"
    TERMINATED = "terminated"


class DetectionMethod(Enum):
    CASB = "casb"
    DNS_ANALYSIS = "dns_analysis"
    SSO_LOG = "sso_log"
    EXPENSE_REVIEW = "expense_review"
    API_AUDIT = "api_audit"
    MANUAL_REPORT = "manual_report"


class RemediationStatus(Enum):
    UNDER_REVIEW = "under_review"
    SANCTIONING = "sanctioning_in_progress"
    BLOCKED = "blocked"
    ACCEPTED = "accepted_and_sanctioned"


class SaaSCategory(Enum):
    CRM = "crm"
    HR = "hr"
    ANALYTICS = "analytics"
    COMMUNICATION = "communication"
    DEVOPS = "devops"
    PROJECT_MANAGEMENT = "project_management"
    FINANCE = "finance"
    MARKETING = "marketing"
    SECURITY = "security"
    PRODUCTIVITY = "productivity"
    OTHER = "other"


@dataclass
class SaaSApplication:
    """A SaaS application in the inventory."""
    app_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_name: str = ""
    product_name: str = ""
    category: str = SaaSCategory.OTHER.value
    tier: str = InventoryTier.TIER_1_SANCTIONED.value
    business_owner: str = ""
    department: str = ""
    procurement_date: Optional[str] = None
    dpa_status: str = DPAStatus.PENDING.value
    dpa_reference: str = ""
    privacy_review_date: Optional[str] = None
    risk_tier: str = "standard"
    personal_data_categories: list[str] = field(default_factory=list)
    data_subject_categories: list[str] = field(default_factory=list)
    processing_purposes: list[str] = field(default_factory=list)
    processing_locations: list[str] = field(default_factory=list)
    integration_method: str = ""
    data_flow_direction: str = "bidirectional"
    contract_expiry: Optional[str] = None
    auto_renewal_date: Optional[str] = None
    annual_cost: float = 0.0
    license_count: int = 0
    contract_status: str = ContractStatus.ACTIVE_COMPLIANT.value
    active: bool = True
    added_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class ShadowITDetection:
    """A shadow IT detection event."""
    detection_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    application_name: str = ""
    vendor_name: str = ""
    detection_method: str = DetectionMethod.CASB.value
    detection_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    estimated_users: int = 0
    departments: list[str] = field(default_factory=list)
    likely_data_categories: list[str] = field(default_factory=list)
    risk_level: str = "standard"
    remediation_status: str = RemediationStatus.UNDER_REVIEW.value
    remediation_decision: str = ""
    remediation_date: Optional[str] = None
    notes: str = ""


@dataclass
class DataFlowRecord:
    """Data flow mapping for a SaaS application."""
    flow_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    app_id: str = ""
    integration_type: str = ""
    authentication: str = ""
    encryption_in_transit: str = ""
    data_sent: list[str] = field(default_factory=list)
    data_received: list[str] = field(default_factory=list)
    data_stored_by_vendor: list[str] = field(default_factory=list)
    vendor_processing_locations: list[str] = field(default_factory=list)
    vendor_sub_processors: list[str] = field(default_factory=list)
    retention_at_vendor: str = ""
    deletion_capability: bool = True


class SaaSInventoryEngine:
    """
    Manages the SaaS vendor data processing inventory including
    discovery, tracking, reconciliation, and contract management.
    """

    def __init__(self):
        self.applications: dict[str, SaaSApplication] = {}
        self.shadow_it_detections: list[ShadowITDetection] = []
        self.data_flows: dict[str, DataFlowRecord] = {}

    def add_application(self, app: SaaSApplication) -> str:
        """Add a SaaS application to the inventory."""
        self.applications[app.app_id] = app
        return app.app_id

    def record_shadow_it(self, detection: ShadowITDetection) -> str:
        """Record a shadow IT detection event."""
        self.shadow_it_detections.append(detection)
        return detection.detection_id

    def remediate_shadow_it(
        self, detection_id: str, decision: RemediationStatus,
        notes: str = ""
    ) -> str:
        """Record remediation decision for a shadow IT detection."""
        for d in self.shadow_it_detections:
            if d.detection_id == detection_id:
                d.remediation_status = decision.value
                d.remediation_date = datetime.now(timezone.utc).isoformat()
                d.remediation_decision = notes

                if decision == RemediationStatus.ACCEPTED:
                    app = SaaSApplication(
                        vendor_name=d.vendor_name,
                        product_name=d.application_name,
                        tier=InventoryTier.TIER_1_SANCTIONED.value,
                        department=d.departments[0] if d.departments else "",
                        personal_data_categories=d.likely_data_categories,
                        dpa_status=DPAStatus.PENDING.value,
                        contract_status=ContractStatus.ACTIVE_DPA_PENDING.value,
                    )
                    self.add_application(app)
                return d.remediation_status

        raise ValueError(f"Detection {detection_id} not found")

    def map_data_flow(self, flow: DataFlowRecord) -> str:
        """Record data flow mapping for a SaaS application."""
        self.data_flows[flow.flow_id] = flow
        return flow.flow_id

    def update_contract_status(self, app_id: str) -> str:
        """Recalculate contract status based on current state."""
        app = self.applications.get(app_id)
        if not app:
            raise ValueError(f"Application {app_id} not found")

        now = datetime.now(timezone.utc).isoformat()
        ninety_days = (datetime.now(timezone.utc) + timedelta(days=90)).isoformat()

        if app.contract_expiry and app.contract_expiry < now:
            app.contract_status = ContractStatus.EXPIRED.value
        elif app.contract_expiry and app.contract_expiry < ninety_days:
            app.contract_status = ContractStatus.EXPIRING.value
        elif app.dpa_status in [DPAStatus.PENDING.value, DPAStatus.IN_NEGOTIATION.value]:
            app.contract_status = ContractStatus.ACTIVE_DPA_PENDING.value
        elif (
            app.privacy_review_date
            and (
                datetime.fromisoformat(app.privacy_review_date.replace("Z", "+00:00"))
                + timedelta(days=365)
            ).isoformat() < now
        ):
            app.contract_status = ContractStatus.ACTIVE_REVIEW_OVERDUE.value
        else:
            app.contract_status = ContractStatus.ACTIVE_COMPLIANT.value

        return app.contract_status

    def reconcile(self, discovered_apps: list[str]) -> dict:
        """Reconcile discovered applications against inventory."""
        sanctioned = {
            app.product_name: app
            for app in self.applications.values()
            if app.tier == InventoryTier.TIER_1_SANCTIONED.value and app.active
        }

        discovered_set = set(discovered_apps)
        sanctioned_set = set(sanctioned.keys())

        new_apps = discovered_set - sanctioned_set
        removed_apps = sanctioned_set - discovered_set
        continuing_apps = discovered_set & sanctioned_set

        return {
            "reconciliation_date": datetime.now(timezone.utc).isoformat(),
            "total_discovered": len(discovered_apps),
            "total_sanctioned": len(sanctioned),
            "new_unsanctioned": sorted(new_apps),
            "possibly_removed": sorted(removed_apps),
            "continuing": sorted(continuing_apps),
            "action_items": {
                "investigate_new": len(new_apps),
                "verify_removals": len(removed_apps),
                "routine_monitoring": len(continuing_apps),
            },
        }

    def get_dpa_coverage(self) -> dict:
        """Calculate DPA coverage across the inventory."""
        active_apps = [
            app for app in self.applications.values()
            if app.tier == InventoryTier.TIER_1_SANCTIONED.value and app.active
        ]

        if not active_apps:
            return {"total": 0, "coverage": "N/A"}

        executed = len([a for a in active_apps if a.dpa_status == DPAStatus.EXECUTED.value])
        in_negotiation = len([a for a in active_apps if a.dpa_status == DPAStatus.IN_NEGOTIATION.value])
        not_required = len([a for a in active_apps if a.dpa_status == DPAStatus.NOT_REQUIRED.value])
        pending = len([a for a in active_apps if a.dpa_status == DPAStatus.PENDING.value])

        coverage = round((executed + not_required) / len(active_apps) * 100, 1)

        return {
            "total_sanctioned": len(active_apps),
            "dpa_executed": executed,
            "dpa_in_negotiation": in_negotiation,
            "dpa_not_required": not_required,
            "dpa_pending": pending,
            "coverage_rate": f"{coverage}%",
        }

    def get_inventory_dashboard(self) -> dict:
        """Generate inventory dashboard summary."""
        all_apps = list(self.applications.values())
        active = [a for a in all_apps if a.active]

        by_category = {}
        for a in active:
            cat = a.category
            by_category[cat] = by_category.get(cat, 0) + 1

        by_status = {}
        for a in active:
            st = a.contract_status
            by_status[st] = by_status.get(st, 0) + 1

        shadow_it_open = len([
            d for d in self.shadow_it_detections
            if d.remediation_status == RemediationStatus.UNDER_REVIEW.value
        ])

        return {
            "total_applications": len(active),
            "by_tier": {
                "sanctioned": len([a for a in active if a.tier == InventoryTier.TIER_1_SANCTIONED.value]),
                "unsanctioned": len([a for a in active if a.tier == InventoryTier.TIER_2_UNSANCTIONED.value]),
                "excluded": len([a for a in active if a.tier == InventoryTier.TIER_3_EXCLUDED.value]),
            },
            "by_category": by_category,
            "by_contract_status": by_status,
            "dpa_coverage": self.get_dpa_coverage(),
            "shadow_it_pending_review": shadow_it_open,
            "total_shadow_it_detections": len(self.shadow_it_detections),
            "as_of": datetime.now(timezone.utc).isoformat(),
        }


if __name__ == "__main__":
    engine = SaaSInventoryEngine()

    # Add sanctioned SaaS applications for Summit Cloud Partners
    apps = [
        SaaSApplication(
            vendor_name="Salesforce, Inc.", product_name="Salesforce CRM",
            category=SaaSCategory.CRM.value, business_owner="VP Sales",
            department="Sales", procurement_date="2024-03-01",
            dpa_status=DPAStatus.EXECUTED.value, dpa_reference="DPA-2024-SF-001",
            privacy_review_date="2025-06-15", risk_tier="standard",
            personal_data_categories=["name", "email", "phone", "company", "deal_value"],
            data_subject_categories=["prospects", "customers"],
            processing_purposes=["sales_pipeline_management", "customer_relationship"],
            processing_locations=["Frankfurt, Germany"],
            integration_method="SAML SSO + REST API", annual_cost=48000.0,
            license_count=50, contract_expiry="2027-03-01",
            contract_status=ContractStatus.ACTIVE_COMPLIANT.value,
        ),
        SaaSApplication(
            vendor_name="Workday, Inc.", product_name="Workday HCM",
            category=SaaSCategory.HR.value, business_owner="VP People",
            department="Human Resources", procurement_date="2023-01-15",
            dpa_status=DPAStatus.EXECUTED.value, dpa_reference="DPA-2023-WD-001",
            privacy_review_date="2025-01-20", risk_tier="high",
            personal_data_categories=["name", "address", "salary", "bank_account", "tax_id", "health_insurance"],
            data_subject_categories=["employees", "contractors"],
            processing_purposes=["payroll", "benefits", "performance_management"],
            processing_locations=["Dublin, Ireland", "Amsterdam, Netherlands"],
            integration_method="SAML SSO + SFTP", annual_cost=96000.0,
            license_count=200, contract_expiry="2026-01-15",
            contract_status=ContractStatus.ACTIVE_COMPLIANT.value,
        ),
        SaaSApplication(
            vendor_name="Slack Technologies, LLC", product_name="Slack Enterprise Grid",
            category=SaaSCategory.COMMUNICATION.value, business_owner="VP Engineering",
            department="Engineering", procurement_date="2024-06-01",
            dpa_status=DPAStatus.EXECUTED.value, dpa_reference="DPA-2024-SL-001",
            privacy_review_date="2025-08-10", risk_tier="standard",
            personal_data_categories=["name", "email", "message_content", "file_uploads"],
            data_subject_categories=["employees", "contractors", "guests"],
            processing_purposes=["internal_communication", "collaboration"],
            processing_locations=["Frankfurt, Germany"],
            integration_method="SAML SSO + API", annual_cost=24000.0,
            license_count=200, contract_expiry="2027-06-01",
            contract_status=ContractStatus.ACTIVE_COMPLIANT.value,
        ),
    ]

    for app in apps:
        engine.add_application(app)

    # Detect shadow IT
    shadow1 = ShadowITDetection(
        application_name="Notion", vendor_name="Notion Labs, Inc.",
        detection_method=DetectionMethod.SSO_LOG.value,
        estimated_users=12, departments=["Product"],
        likely_data_categories=["name", "email", "project_notes", "customer_feedback"],
        risk_level="standard",
    )
    shadow2 = ShadowITDetection(
        application_name="Airtable", vendor_name="Formagrid Inc.",
        detection_method=DetectionMethod.CASB.value,
        estimated_users=5, departments=["Marketing"],
        likely_data_categories=["name", "email", "campaign_data"],
        risk_level="standard",
    )

    engine.record_shadow_it(shadow1)
    engine.record_shadow_it(shadow2)

    # Remediate — sanction Notion, block Airtable
    engine.remediate_shadow_it(
        shadow1.detection_id, RemediationStatus.ACCEPTED,
        "Product team requires; initiating formal DPA negotiation"
    )
    engine.remediate_shadow_it(
        shadow2.detection_id, RemediationStatus.BLOCKED,
        "Asana (sanctioned) provides equivalent functionality"
    )

    # Run reconciliation
    discovered = ["Salesforce CRM", "Workday HCM", "Slack Enterprise Grid", "Notion", "Canva"]
    reconciliation = engine.reconcile(discovered)
    print("=== Reconciliation Results ===")
    print(json.dumps(reconciliation, indent=2))

    # Dashboard
    dashboard = engine.get_inventory_dashboard()
    print("\n=== SaaS Vendor Inventory Dashboard ===")
    print(json.dumps(dashboard, indent=2))
