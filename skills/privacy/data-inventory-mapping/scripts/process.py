"""
Data Inventory and Mapping Engine
Builds and maintains GDPR Art. 30 compliant data inventories.
"""

import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from datetime import date


class ClassificationTier(Enum):
    PUBLIC = "Public"
    INTERNAL = "Internal"
    CONFIDENTIAL = "Confidential"
    RESTRICTED = "Restricted"


class DataCategory(Enum):
    PERSONAL_DIRECT = "personal_direct"
    PERSONAL_INDIRECT = "personal_indirect"
    SPECIAL_CATEGORY = "special_category"
    CRIMINAL_DATA = "criminal_data"
    PSEUDONYMISED = "pseudonymised"
    ANONYMISED = "anonymised"
    NON_PERSONAL = "non_personal"


class LawfulBasis(Enum):
    CONSENT = "Art. 6(1)(a) — Consent"
    CONTRACT = "Art. 6(1)(b) — Contract performance"
    LEGAL_OBLIGATION = "Art. 6(1)(c) — Legal obligation"
    VITAL_INTERESTS = "Art. 6(1)(d) — Vital interests"
    PUBLIC_TASK = "Art. 6(1)(e) — Public task"
    LEGITIMATE_INTERESTS = "Art. 6(1)(f) — Legitimate interests"


@dataclass
class DataElement:
    """A single data element within a system."""
    element_id: str
    field_name: str
    data_type: str
    description: str
    category: DataCategory
    classification_tier: ClassificationTier
    source: str
    data_subjects: list[str]
    lawful_basis: LawfulBasis
    art9_condition: str = ""
    art10_basis: str = ""
    retention_period: str = ""
    notes: str = ""


@dataclass
class DataFlow:
    """A data flow between two systems or entities."""
    flow_id: str
    source_system: str
    destination_system: str
    data_categories: list[str]
    transfer_mechanism: str
    is_international_transfer: bool = False
    destination_country: str = ""
    safeguard_mechanism: str = ""
    legal_basis: str = ""
    frequency: str = ""
    volume: str = ""


@dataclass
class SystemRecord:
    """A system record in the data inventory."""
    system_id: str
    system_name: str
    system_type: str
    department: str
    vendor: str
    hosting_location: str
    data_elements: list[DataElement] = field(default_factory=list)
    inbound_flows: list[DataFlow] = field(default_factory=list)
    outbound_flows: list[DataFlow] = field(default_factory=list)
    data_subjects: list[str] = field(default_factory=list)
    processing_purposes: list[str] = field(default_factory=list)
    dpia_reference: str = ""
    system_owner: str = ""
    last_reviewed: str = ""


@dataclass
class ProcessingActivity:
    """An Art. 30 processing activity record."""
    activity_id: str
    activity_name: str
    controller: str
    purposes: list[str]
    data_subject_categories: list[str]
    personal_data_categories: list[str]
    recipients: list[str]
    international_transfers: list[dict]
    retention_periods: dict
    security_measures: list[str]
    lawful_basis: str
    art9_condition: str = ""
    dpia_reference: str = ""
    systems_involved: list[str] = field(default_factory=list)


class DataInventoryManager:
    """
    Manages the enterprise data inventory for GDPR Art. 30 compliance.
    """

    def __init__(self, organisation: str):
        self.organisation = organisation
        self.systems: dict[str, SystemRecord] = {}
        self.processing_activities: dict[str, ProcessingActivity] = {}
        self.data_flows: list[DataFlow] = []

    def register_system(self, system: SystemRecord) -> str:
        """Register a system in the inventory."""
        self.systems[system.system_id] = system
        return system.system_id

    def add_data_element(self, system_id: str, element: DataElement) -> bool:
        """Add a data element to a registered system."""
        if system_id not in self.systems:
            return False
        self.systems[system_id].data_elements.append(element)
        return True

    def add_data_flow(self, flow: DataFlow) -> str:
        """Register a data flow between systems."""
        self.data_flows.append(flow)
        if flow.source_system in self.systems:
            self.systems[flow.source_system].outbound_flows.append(flow)
        if flow.destination_system in self.systems:
            self.systems[flow.destination_system].inbound_flows.append(flow)
        return flow.flow_id

    def register_processing_activity(self, activity: ProcessingActivity) -> str:
        """Register an Art. 30 processing activity."""
        self.processing_activities[activity.activity_id] = activity
        return activity.activity_id

    def get_inventory_summary(self) -> dict:
        """Generate a summary of the data inventory."""
        total_elements = sum(len(s.data_elements) for s in self.systems.values())
        category_counts: dict[str, int] = {}
        tier_counts: dict[str, int] = {}
        special_cat_systems: list[str] = []

        for system in self.systems.values():
            for elem in system.data_elements:
                cat = elem.category.value
                category_counts[cat] = category_counts.get(cat, 0) + 1
                tier = elem.classification_tier.value
                tier_counts[tier] = tier_counts.get(tier, 0) + 1
                if elem.category in (DataCategory.SPECIAL_CATEGORY, DataCategory.CRIMINAL_DATA):
                    if system.system_name not in special_cat_systems:
                        special_cat_systems.append(system.system_name)

        international_flows = [
            f for f in self.data_flows if f.is_international_transfer
        ]

        return {
            "organisation": self.organisation,
            "report_date": date.today().isoformat(),
            "total_systems": len(self.systems),
            "total_data_elements": total_elements,
            "total_processing_activities": len(self.processing_activities),
            "total_data_flows": len(self.data_flows),
            "international_transfers": len(international_flows),
            "elements_by_category": category_counts,
            "elements_by_tier": tier_counts,
            "systems_with_special_category": special_cat_systems,
        }

    def reconcile_with_discovery(
        self, discovered_elements: list[dict]
    ) -> dict:
        """
        Reconcile manual inventory with automated discovery results.

        Args:
            discovered_elements: List of dicts with keys:
                system_name, field_name, category

        Returns:
            Reconciliation report with gaps in both directions
        """
        inventory_elements = set()
        for system in self.systems.values():
            for elem in system.data_elements:
                inventory_elements.add((system.system_name, elem.field_name))

        discovered_set = set()
        for d in discovered_elements:
            discovered_set.add((d["system_name"], d["field_name"]))

        in_inventory_not_discovered = inventory_elements - discovered_set
        discovered_not_in_inventory = discovered_set - inventory_elements

        return {
            "reconciliation_date": date.today().isoformat(),
            "inventory_elements": len(inventory_elements),
            "discovered_elements": len(discovered_set),
            "matching": len(inventory_elements & discovered_set),
            "in_inventory_not_discovered": [
                {"system": s, "field": f} for s, f in in_inventory_not_discovered
            ],
            "discovered_not_in_inventory": [
                {"system": s, "field": f} for s, f in discovered_not_in_inventory
            ],
            "inventory_completeness": (
                len(inventory_elements & discovered_set) / len(discovered_set) * 100
                if discovered_set else 100
            ),
        }

    def generate_ropa_export(self) -> list[dict]:
        """Export processing activities in Art. 30 RoPA format."""
        ropa_records = []
        for activity in self.processing_activities.values():
            ropa_records.append({
                "controller": activity.controller,
                "activity_name": activity.activity_name,
                "purposes": activity.purposes,
                "data_subject_categories": activity.data_subject_categories,
                "personal_data_categories": activity.personal_data_categories,
                "recipients": activity.recipients,
                "international_transfers": activity.international_transfers,
                "retention_periods": activity.retention_periods,
                "security_measures": activity.security_measures,
                "lawful_basis": activity.lawful_basis,
            })
        return ropa_records


def run_vanguard_example():
    """Build a sample data inventory for Vanguard Financial Services."""
    mgr = DataInventoryManager("Vanguard Financial Services")

    crm = SystemRecord(
        system_id="SYS-CRM-001",
        system_name="Salesforce CRM",
        system_type="SaaS",
        department="Sales / Customer Service",
        vendor="Salesforce Inc.",
        hosting_location="EU (Frankfurt)",
        data_subjects=["Customers", "Prospects"],
        processing_purposes=["Customer relationship management", "Sales pipeline", "Service delivery"],
        system_owner="Head of Sales Operations",
        last_reviewed=date.today().isoformat(),
    )
    mgr.register_system(crm)

    mgr.add_data_element("SYS-CRM-001", DataElement(
        element_id="DE-CRM-001",
        field_name="customer_full_name",
        data_type="VARCHAR(255)",
        description="Customer legal name",
        category=DataCategory.PERSONAL_DIRECT,
        classification_tier=ClassificationTier.CONFIDENTIAL,
        source="Collected from data subject",
        data_subjects=["Customers"],
        lawful_basis=LawfulBasis.CONTRACT,
        retention_period="Duration of relationship + 7 years",
    ))

    mgr.add_data_element("SYS-CRM-001", DataElement(
        element_id="DE-CRM-002",
        field_name="customer_email",
        data_type="VARCHAR(255)",
        description="Customer primary email address",
        category=DataCategory.PERSONAL_DIRECT,
        classification_tier=ClassificationTier.CONFIDENTIAL,
        source="Collected from data subject",
        data_subjects=["Customers"],
        lawful_basis=LawfulBasis.CONTRACT,
        retention_period="Duration of relationship + 7 years",
    ))

    mgr.add_data_element("SYS-CRM-001", DataElement(
        element_id="DE-CRM-003",
        field_name="customer_account_number",
        data_type="VARCHAR(14)",
        description="Vanguard customer account reference (VFS-XXXXXXXXXX)",
        category=DataCategory.PERSONAL_INDIRECT,
        classification_tier=ClassificationTier.CONFIDENTIAL,
        source="System generated",
        data_subjects=["Customers"],
        lawful_basis=LawfulBasis.CONTRACT,
        retention_period="Duration of relationship + 7 years",
    ))

    hr = SystemRecord(
        system_id="SYS-HR-001",
        system_name="Workday HR",
        system_type="SaaS",
        department="Human Resources",
        vendor="Workday Inc.",
        hosting_location="EU (Dublin)",
        data_subjects=["Employees", "Candidates"],
        processing_purposes=["HR management", "Recruitment", "Diversity monitoring"],
        system_owner="Head of Human Resources",
        last_reviewed=date.today().isoformat(),
    )
    mgr.register_system(hr)

    mgr.add_data_element("SYS-HR-001", DataElement(
        element_id="DE-HR-001",
        field_name="employee_ethnicity",
        data_type="VARCHAR(50)",
        description="Self-reported ethnicity for diversity monitoring",
        category=DataCategory.SPECIAL_CATEGORY,
        classification_tier=ClassificationTier.RESTRICTED,
        source="Collected from data subject (voluntary survey)",
        data_subjects=["Employees"],
        lawful_basis=LawfulBasis.CONSENT,
        art9_condition="Art. 9(2)(a) — Explicit consent",
        retention_period="3 years from collection",
    ))

    mgr.add_data_flow(DataFlow(
        flow_id="DF-001",
        source_system="Salesforce CRM",
        destination_system="Oracle Data Warehouse",
        data_categories=["customer_name", "customer_email", "account_number", "transaction_history"],
        transfer_mechanism="ETL pipeline (Azure Data Factory)",
        is_international_transfer=False,
        frequency="Daily at 02:00 UTC",
        volume="~50,000 records/day (incremental)",
    ))

    mgr.add_data_flow(DataFlow(
        flow_id="DF-002",
        source_system="Salesforce CRM",
        destination_system="Salesforce Inc. (US)",
        data_categories=["customer_name", "customer_email", "account_number"],
        transfer_mechanism="SaaS platform hosting",
        is_international_transfer=True,
        destination_country="United States",
        safeguard_mechanism="EU-US Data Privacy Framework (adequacy decision 10 July 2023)",
        frequency="Continuous (SaaS)",
    ))

    mgr.register_processing_activity(ProcessingActivity(
        activity_id="PA-CRM-001",
        activity_name="Customer Relationship Management",
        controller="Vanguard Financial Services Ltd",
        purposes=["Manage customer accounts", "Provide financial services", "Customer communications"],
        data_subject_categories=["Customers", "Prospects"],
        personal_data_categories=["Name", "Email", "Address", "Phone", "Account number", "Transaction history"],
        recipients=["Salesforce Inc. (processor)", "Oracle (processor)", "HMRC (legal obligation)"],
        international_transfers=[
            {"recipient": "Salesforce Inc.", "country": "US", "safeguard": "EU-US DPF"}
        ],
        retention_periods={"customer_data": "Relationship + 7 years", "prospect_data": "2 years from last contact"},
        security_measures=["Encryption at rest (AES-256)", "TLS 1.3 in transit", "RBAC", "Audit logging", "MFA"],
        lawful_basis="Art. 6(1)(b) — Contract performance",
        systems_involved=["Salesforce CRM", "Oracle Data Warehouse"],
    ))

    summary = mgr.get_inventory_summary()
    print("=" * 70)
    print("VANGUARD FINANCIAL SERVICES — DATA INVENTORY SUMMARY")
    print("=" * 70)
    print(json.dumps(summary, indent=2))

    discovered = [
        {"system_name": "Salesforce CRM", "field_name": "customer_full_name"},
        {"system_name": "Salesforce CRM", "field_name": "customer_email"},
        {"system_name": "Salesforce CRM", "field_name": "customer_account_number"},
        {"system_name": "Salesforce CRM", "field_name": "customer_ip_address"},
        {"system_name": "Workday HR", "field_name": "employee_ethnicity"},
        {"system_name": "Workday HR", "field_name": "employee_health_notes"},
    ]
    recon = mgr.reconcile_with_discovery(discovered)
    print(f"\n{'='*70}")
    print("DISCOVERY RECONCILIATION")
    print("=" * 70)
    print(json.dumps(recon, indent=2))

    ropa = mgr.generate_ropa_export()
    print(f"\n{'='*70}")
    print("ART. 30 RoPA EXPORT")
    print("=" * 70)
    print(json.dumps(ropa, indent=2))


if __name__ == "__main__":
    run_vanguard_example()
