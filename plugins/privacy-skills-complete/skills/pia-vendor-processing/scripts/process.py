"""
Vendor Processing Privacy Impact Assessment engine.
Evaluates vendor/processor data processing arrangements against GDPR Article 28,
DPA requirements, sub-processor management, and cross-border transfer obligations.
"""

import json
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class ComplianceStatus(Enum):
    COMPLIANT = "compliant"
    PARTIAL = "partially_compliant"
    NON_COMPLIANT = "non_compliant"
    NOT_APPLICABLE = "not_applicable"


class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class VendorRiskCategory(Enum):
    CLOUD_INFRASTRUCTURE = "cloud_iaas_paas"
    SAAS_APPLICATION = "saas_application"
    ANALYTICS_PROVIDER = "analytics_provider"
    IT_SUPPORT = "it_managed_services"
    PAYMENT_PROCESSOR = "payment_processor"
    MARKETING_VENDOR = "marketing_vendor"
    HR_VENDOR = "hr_payroll_vendor"
    OTHER = "other"


ART_28_MANDATORY_CLAUSES = [
    "documented_instructions",
    "confidentiality_obligation",
    "security_measures_art32",
    "sub_processor_conditions",
    "data_subject_rights_assistance",
    "security_breach_dpia_assistance",
    "data_deletion_return",
    "audit_information_access",
]


@dataclass
class SubProcessor:
    name: str
    service: str
    location: str
    assessed: bool = False
    dpa_flow_down: bool = False


@dataclass
class VendorAssessment:
    vendor_id: str
    vendor_name: str
    service_description: str
    risk_category: VendorRiskCategory = VendorRiskCategory.OTHER
    data_categories: list = field(default_factory=list)
    special_category_data: bool = False
    data_subject_count: int = 0
    cross_border: bool = False
    transfer_destination: str = ""
    transfer_mechanism: str = ""
    dpa_signed: bool = False
    dpa_clauses_present: list = field(default_factory=list)
    security_certifications: list = field(default_factory=list)
    due_diligence_completed: bool = False
    enforcement_history_checked: bool = False
    sub_processors: list = field(default_factory=list)
    sub_processor_notification_process: bool = False
    last_review_date: Optional[datetime] = None
    audit_conducted: bool = False
    exit_plan_documented: bool = False


@dataclass
class VendorProcessingPIA:
    organisation_name: str
    assessment_date: datetime = field(default_factory=datetime.now)
    vendors: list = field(default_factory=list)

    def assess_dpa_compliance(self, vendor: VendorAssessment) -> dict:
        findings = []
        status = ComplianceStatus.COMPLIANT

        if not vendor.dpa_signed:
            return {
                "status": ComplianceStatus.NON_COMPLIANT.value,
                "findings": [
                    f"CRITICAL: No DPA signed with vendor '{vendor.vendor_name}' "
                    "(Art. 28(3) requirement)"
                ],
            }

        missing_clauses = [
            c for c in ART_28_MANDATORY_CLAUSES
            if c not in vendor.dpa_clauses_present
        ]

        if missing_clauses:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append(
                f"CRITICAL: DPA with '{vendor.vendor_name}' missing mandatory Art. 28(3) "
                f"clauses: {', '.join(missing_clauses)}"
            )

        return {"status": status.value, "findings": findings}

    def assess_due_diligence(self, vendor: VendorAssessment) -> dict:
        findings = []
        status = ComplianceStatus.COMPLIANT

        if not vendor.due_diligence_completed:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append(
                f"CRITICAL: Due diligence not completed for vendor '{vendor.vendor_name}' "
                "(Art. 28(1) sufficient guarantees)"
            )

        if not vendor.security_certifications:
            if status == ComplianceStatus.COMPLIANT:
                status = ComplianceStatus.PARTIAL
            findings.append(
                f"Vendor '{vendor.vendor_name}': no security certifications provided "
                "(ISO 27001, SOC 2, etc.)"
            )

        if not vendor.enforcement_history_checked:
            findings.append(
                f"Vendor '{vendor.vendor_name}': enforcement history not checked "
                "with supervisory authorities"
            )

        return {"status": status.value, "findings": findings}

    def assess_sub_processors(self, vendor: VendorAssessment) -> dict:
        findings = []
        status = ComplianceStatus.COMPLIANT

        if not vendor.sub_processors:
            return {
                "status": ComplianceStatus.COMPLIANT.value,
                "findings": [f"Vendor '{vendor.vendor_name}': no sub-processors identified"],
            }

        if not vendor.sub_processor_notification_process:
            status = ComplianceStatus.PARTIAL
            findings.append(
                f"Vendor '{vendor.vendor_name}': no sub-processor change notification "
                "process in place (Art. 28(2) requirement)"
            )

        for sp in vendor.sub_processors:
            if not sp.assessed:
                if status == ComplianceStatus.COMPLIANT:
                    status = ComplianceStatus.PARTIAL
                findings.append(
                    f"Sub-processor '{sp.name}' ({sp.service}) not assessed"
                )

            if not sp.dpa_flow_down:
                status = ComplianceStatus.NON_COMPLIANT
                findings.append(
                    f"CRITICAL: Sub-processor '{sp.name}' does not have Art. 28(4) "
                    "flow-down DPA obligations"
                )

        return {
            "status": status.value,
            "findings": findings,
            "sub_processor_count": len(vendor.sub_processors),
        }

    def assess_cross_border(self, vendor: VendorAssessment) -> dict:
        findings = []
        status = ComplianceStatus.COMPLIANT

        if not vendor.cross_border:
            return {
                "status": ComplianceStatus.NOT_APPLICABLE.value,
                "findings": [f"Vendor '{vendor.vendor_name}': no cross-border transfers"],
            }

        if not vendor.transfer_mechanism:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append(
                f"CRITICAL: Vendor '{vendor.vendor_name}' transfers data to "
                f"'{vendor.transfer_destination}' without documented transfer mechanism"
            )
        else:
            findings.append(
                f"Vendor '{vendor.vendor_name}': transfer to '{vendor.transfer_destination}' "
                f"using {vendor.transfer_mechanism}"
            )

        return {"status": status.value, "findings": findings}

    def calculate_vendor_risk(self, vendor: VendorAssessment) -> RiskLevel:
        score = 0

        category_scores = {
            VendorRiskCategory.CLOUD_INFRASTRUCTURE: 4,
            VendorRiskCategory.SAAS_APPLICATION: 3,
            VendorRiskCategory.PAYMENT_PROCESSOR: 4,
            VendorRiskCategory.ANALYTICS_PROVIDER: 3,
            VendorRiskCategory.HR_VENDOR: 3,
            VendorRiskCategory.MARKETING_VENDOR: 2,
            VendorRiskCategory.IT_SUPPORT: 2,
            VendorRiskCategory.OTHER: 1,
        }
        score += category_scores.get(vendor.risk_category, 1)

        if vendor.special_category_data:
            score += 3
        if vendor.cross_border:
            score += 2
        if vendor.data_subject_count > 100000:
            score += 3
        elif vendor.data_subject_count > 10000:
            score += 2
        elif vendor.data_subject_count > 1000:
            score += 1
        if len(vendor.sub_processors) > 5:
            score += 2
        elif len(vendor.sub_processors) > 0:
            score += 1

        if score >= 10:
            return RiskLevel.CRITICAL
        elif score >= 7:
            return RiskLevel.HIGH
        elif score >= 4:
            return RiskLevel.MEDIUM
        return RiskLevel.LOW

    def run_full_assessment(self) -> dict:
        vendor_results = []

        for vendor in self.vendors:
            dpa = self.assess_dpa_compliance(vendor)
            dd = self.assess_due_diligence(vendor)
            sp = self.assess_sub_processors(vendor)
            cb = self.assess_cross_border(vendor)
            risk = self.calculate_vendor_risk(vendor)

            vendor_results.append({
                "vendor_id": vendor.vendor_id,
                "vendor_name": vendor.vendor_name,
                "risk_level": risk.value,
                "dpa_compliance": dpa,
                "due_diligence": dd,
                "sub_processor_management": sp,
                "cross_border_transfer": cb,
                "exit_plan": vendor.exit_plan_documented,
                "last_review": vendor.last_review_date.isoformat() if vendor.last_review_date else None,
            })

        all_findings = []
        for vr in vendor_results:
            for section in ["dpa_compliance", "due_diligence", "sub_processor_management", "cross_border_transfer"]:
                all_findings.extend(vr[section].get("findings", []))

        critical = sum(1 for f in all_findings if f.startswith("CRITICAL"))

        all_statuses = []
        for vr in vendor_results:
            for section in ["dpa_compliance", "due_diligence", "sub_processor_management", "cross_border_transfer"]:
                all_statuses.append(vr[section]["status"])

        active = [s for s in all_statuses if s != ComplianceStatus.NOT_APPLICABLE.value]
        if ComplianceStatus.NON_COMPLIANT.value in active:
            overall = ComplianceStatus.NON_COMPLIANT
        elif ComplianceStatus.PARTIAL.value in active:
            overall = ComplianceStatus.PARTIAL
        else:
            overall = ComplianceStatus.COMPLIANT

        risk_levels = [vr["risk_level"] for vr in vendor_results]
        if RiskLevel.CRITICAL.value in risk_levels:
            overall_risk = RiskLevel.CRITICAL
        elif RiskLevel.HIGH.value in risk_levels:
            overall_risk = RiskLevel.HIGH
        elif RiskLevel.MEDIUM.value in risk_levels:
            overall_risk = RiskLevel.MEDIUM
        else:
            overall_risk = RiskLevel.LOW

        return {
            "organisation": self.organisation_name,
            "assessment_date": self.assessment_date.isoformat(),
            "vendor_count": len(self.vendors),
            "vendors": vendor_results,
            "overall_status": overall.value,
            "overall_risk": overall_risk.value,
            "total_findings": len(all_findings),
            "critical_findings": critical,
        }


def generate_report(result: dict) -> str:
    lines = [
        "=" * 70,
        "VENDOR PROCESSING PRIVACY IMPACT ASSESSMENT REPORT",
        "=" * 70,
        f"Organisation: {result['organisation']}",
        f"Assessment Date: {result['assessment_date']}",
        f"Vendors Assessed: {result['vendor_count']}",
        f"Overall Status: {result['overall_status'].upper()}",
        f"Overall Risk: {result.get('overall_risk', 'N/A').upper()}",
        "",
    ]

    for vendor in result.get("vendors", []):
        lines.append(f"=== Vendor: {vendor['vendor_name']} ({vendor['vendor_id']}) ===")
        lines.append(f"Risk Level: {vendor['risk_level'].upper()}")

        for section_name, section_key in [
            ("DPA Compliance", "dpa_compliance"),
            ("Due Diligence", "due_diligence"),
            ("Sub-Processor Management", "sub_processor_management"),
            ("Cross-Border Transfer", "cross_border_transfer"),
        ]:
            section = vendor[section_key]
            lines.append(f"  {section_name}: {section['status'].upper()}")
            for finding in section.get("findings", []):
                lines.append(f"    - {finding}")

        lines.append(f"  Exit Plan: {'Documented' if vendor['exit_plan'] else 'NOT DOCUMENTED'}")
        lines.append("")

    lines.append(f"Total Findings: {result.get('total_findings', 0)}")
    lines.append(f"Critical Findings: {result.get('critical_findings', 0)}")
    lines.append("=" * 70)

    return "\n".join(lines)


if __name__ == "__main__":
    pia = VendorProcessingPIA(
        organisation_name="Acme Financial Services",
        vendors=[
            VendorAssessment(
                vendor_id="V-001",
                vendor_name="CloudCo IaaS",
                service_description="Cloud infrastructure hosting",
                risk_category=VendorRiskCategory.CLOUD_INFRASTRUCTURE,
                data_categories=["customer_pii", "financial_data", "transaction_records"],
                data_subject_count=500000,
                cross_border=True,
                transfer_destination="EU (Ireland), US (Virginia)",
                transfer_mechanism="standard_contractual_clauses",
                dpa_signed=True,
                dpa_clauses_present=ART_28_MANDATORY_CLAUSES.copy(),
                security_certifications=["ISO_27001", "SOC_2_Type_II", "CSA_STAR"],
                due_diligence_completed=True,
                enforcement_history_checked=True,
                sub_processors=[
                    SubProcessor("CDN Corp", "Content delivery", "Global", True, True),
                    SubProcessor("BackupCo", "Backup storage", "EU", True, True),
                ],
                sub_processor_notification_process=True,
                last_review_date=datetime(2025, 9, 1),
                audit_conducted=True,
                exit_plan_documented=True,
            ),
            VendorAssessment(
                vendor_id="V-002",
                vendor_name="MarketingPlatform SaaS",
                service_description="Email marketing and campaign management",
                risk_category=VendorRiskCategory.MARKETING_VENDOR,
                data_categories=["email", "name", "preferences"],
                data_subject_count=200000,
                cross_border=True,
                transfer_destination="US",
                transfer_mechanism="",
                dpa_signed=True,
                dpa_clauses_present=[
                    "documented_instructions",
                    "confidentiality_obligation",
                    "security_measures_art32",
                    "data_deletion_return",
                ],
                security_certifications=["SOC_2_Type_II"],
                due_diligence_completed=True,
                enforcement_history_checked=False,
                sub_processors=[
                    SubProcessor("EmailSend Inc", "Email delivery", "US", False, False),
                ],
                sub_processor_notification_process=False,
                exit_plan_documented=False,
            ),
        ],
    )

    result = pia.run_full_assessment()
    print(generate_report(result))
    print("\nJSON Output:")
    print(json.dumps(result, indent=2, default=str))
