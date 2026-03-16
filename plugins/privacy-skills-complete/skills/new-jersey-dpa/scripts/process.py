"""
New Jersey Data Privacy Act (NJDPA) compliance assessment engine.
Evaluates organizational compliance against NJDPA requirements including
applicability, consumer rights, sensitive data handling, and DPA obligations.
"""

import json
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional


class ComplianceStatus(Enum):
    COMPLIANT = "compliant"
    PARTIAL = "partially_compliant"
    NON_COMPLIANT = "non_compliant"
    NOT_APPLICABLE = "not_applicable"
    UNKNOWN = "unknown"


class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


NJDPA_SENSITIVE_CATEGORIES = [
    "racial_ethnic_origin",
    "religious_beliefs",
    "mental_physical_health",
    "financial_information",
    "sex_life_sexual_orientation",
    "citizenship_immigration_status",
    "transgender_nonbinary_status",
    "genetic_data",
    "biometric_data",
    "child_data_under_13",
    "precise_geolocation",
]

NJDPA_CONSUMER_RIGHTS = [
    "access",
    "correction",
    "deletion",
    "portability",
    "opt_out_sale",
    "opt_out_targeted_advertising",
    "opt_out_profiling",
    "non_discrimination",
    "appeal",
]

EXEMPT_ENTITY_TYPES = [
    "government_agency",
    "hipaa_covered_entity",
    "hipaa_business_associate",
    "glba_financial_institution",
    "higher_education_institution",
    "nonprofit_organization",
]

DPA_TRIGGER_ACTIVITIES = [
    "targeted_advertising",
    "sale_of_personal_data",
    "profiling_legal_significant_effects",
    "sensitive_data_processing",
    "heightened_risk_processing",
]


@dataclass
class ConsumerRightsRequest:
    request_id: str
    request_type: str
    received_date: datetime
    response_date: Optional[datetime] = None
    status: str = "pending"
    appeal_filed: bool = False
    appeal_date: Optional[datetime] = None

    @property
    def sla_days(self) -> int:
        if self.request_type in ("opt_out_sale", "opt_out_targeted_advertising", "opt_out_profiling"):
            return 15  # business days
        return 45  # calendar days

    @property
    def is_overdue(self) -> bool:
        if self.response_date:
            return False
        if self.request_type in ("opt_out_sale", "opt_out_targeted_advertising", "opt_out_profiling"):
            business_days = 0
            current = self.received_date
            while business_days < 15:
                current += timedelta(days=1)
                if current.weekday() < 5:
                    business_days += 1
            return datetime.now() > current
        return datetime.now() > self.received_date + timedelta(days=45)


@dataclass
class DataProtectionAssessment:
    assessment_id: str
    processing_activity: str
    trigger_category: str
    date_conducted: datetime
    benefits_analysis: str = ""
    risk_analysis: str = ""
    safeguards: list = field(default_factory=list)
    residual_risk: RiskLevel = RiskLevel.UNKNOWN
    retained_until: Optional[datetime] = None


@dataclass
class NJDPAComplianceAssessment:
    organization_name: str
    assessment_date: datetime = field(default_factory=datetime.now)
    nj_consumer_count: int = 0
    derives_revenue_from_data_sale: bool = False
    entity_type: str = ""
    sensitive_data_categories: list = field(default_factory=list)
    consent_mechanism_implemented: bool = False
    universal_opt_out_supported: bool = False
    privacy_notice_updated: bool = False
    consumer_rights_channels: list = field(default_factory=list)
    identity_verification_process: bool = False
    dpa_activities: list = field(default_factory=list)
    dpas_conducted: list = field(default_factory=list)
    requests: list = field(default_factory=list)
    findings: list = field(default_factory=list)

    def assess_applicability(self) -> dict:
        """Determine if the NJDPA applies to this organization."""
        if self.entity_type in EXEMPT_ENTITY_TYPES:
            return {
                "applicable": False,
                "reason": f"Entity type '{self.entity_type}' is exempt from NJDPA",
                "status": ComplianceStatus.NOT_APPLICABLE.value,
            }

        threshold_met = False
        reason = ""

        if self.nj_consumer_count >= 100000:
            threshold_met = True
            reason = f"Processes data of {self.nj_consumer_count:,} NJ consumers (>=100,000 threshold)"
        elif self.nj_consumer_count >= 25000 and self.derives_revenue_from_data_sale:
            threshold_met = True
            reason = (
                f"Processes data of {self.nj_consumer_count:,} NJ consumers (>=25,000) "
                "and derives revenue from data sale"
            )

        if not threshold_met:
            return {
                "applicable": False,
                "reason": "Does not meet processing volume thresholds",
                "status": ComplianceStatus.NOT_APPLICABLE.value,
            }

        return {
            "applicable": True,
            "reason": reason,
            "status": ComplianceStatus.UNKNOWN.value,
        }

    def assess_sensitive_data_compliance(self) -> dict:
        """Evaluate compliance with NJDPA sensitive data requirements."""
        findings = []
        status = ComplianceStatus.COMPLIANT

        processed_sensitive = [
            cat for cat in self.sensitive_data_categories if cat in NJDPA_SENSITIVE_CATEGORIES
        ]

        if not processed_sensitive:
            return {
                "status": ComplianceStatus.NOT_APPLICABLE.value,
                "findings": ["No NJDPA-defined sensitive data categories processed"],
                "categories_processed": [],
            }

        if not self.consent_mechanism_implemented:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append(
                "CRITICAL: Opt-in consent mechanism not implemented for sensitive data "
                f"processing. Affected categories: {', '.join(processed_sensitive)}"
            )

        njdpa_unique = {"financial_information", "citizenship_immigration_status", "transgender_nonbinary_status"}
        unique_sensitive = [cat for cat in processed_sensitive if cat in njdpa_unique]
        if unique_sensitive:
            findings.append(
                f"Note: Processing NJDPA-unique sensitive categories: {', '.join(unique_sensitive)}. "
                "These may not be classified as sensitive under other state laws."
            )

        if "child_data_under_13" in processed_sensitive:
            findings.append(
                "Processing known child data (under 13): ensure COPPA compliance in addition "
                "to NJDPA consent requirement."
            )

        return {
            "status": status.value,
            "findings": findings,
            "categories_processed": processed_sensitive,
        }

    def assess_consumer_rights(self) -> dict:
        """Evaluate consumer rights request handling compliance."""
        findings = []
        status = ComplianceStatus.COMPLIANT

        if not self.consumer_rights_channels:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append("CRITICAL: No consumer rights request intake channels established")

        if not self.identity_verification_process:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append("CRITICAL: No identity verification process for consumer requests")

        if not self.universal_opt_out_supported:
            if status != ComplianceStatus.NON_COMPLIANT:
                status = ComplianceStatus.PARTIAL
            findings.append(
                "Universal opt-out mechanism (e.g., GPC) not yet supported. "
                "Required by July 15, 2025."
            )

        overdue_requests = [r for r in self.requests if r.is_overdue]
        if overdue_requests:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append(
                f"CRITICAL: {len(overdue_requests)} consumer rights requests are overdue"
            )

        total_requests = len(self.requests)
        if total_requests > 0:
            completed = sum(1 for r in self.requests if r.response_date is not None)
            findings.append(
                f"Request metrics: {completed}/{total_requests} completed "
                f"({completed / total_requests * 100:.1f}%)"
            )

        return {
            "status": status.value,
            "findings": findings,
            "total_requests": total_requests,
            "overdue_requests": len(overdue_requests) if self.requests else 0,
        }

    def assess_dpa_obligations(self) -> dict:
        """Evaluate data protection assessment obligations."""
        findings = []
        status = ComplianceStatus.COMPLIANT

        activities_requiring_dpa = [
            act for act in self.dpa_activities if act in DPA_TRIGGER_ACTIVITIES
        ]

        if not activities_requiring_dpa:
            return {
                "status": ComplianceStatus.NOT_APPLICABLE.value,
                "findings": ["No processing activities triggering DPA requirement identified"],
            }

        conducted_for = {dpa.trigger_category for dpa in self.dpas_conducted}
        missing_dpas = [act for act in activities_requiring_dpa if act not in conducted_for]

        if missing_dpas:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append(
                f"CRITICAL: DPAs not conducted for: {', '.join(missing_dpas)}"
            )

        for dpa in self.dpas_conducted:
            if not dpa.benefits_analysis or not dpa.risk_analysis:
                if status == ComplianceStatus.COMPLIANT:
                    status = ComplianceStatus.PARTIAL
                findings.append(
                    f"DPA '{dpa.assessment_id}' missing benefits or risk analysis"
                )
            if not dpa.safeguards:
                if status == ComplianceStatus.COMPLIANT:
                    status = ComplianceStatus.PARTIAL
                findings.append(
                    f"DPA '{dpa.assessment_id}' has no safeguards documented"
                )

        return {
            "status": status.value,
            "findings": findings,
            "activities_requiring_dpa": activities_requiring_dpa,
            "dpas_conducted": len(self.dpas_conducted),
            "missing_dpas": missing_dpas,
        }

    def assess_privacy_notice(self) -> dict:
        """Evaluate privacy notice compliance."""
        findings = []
        status = ComplianceStatus.COMPLIANT

        if not self.privacy_notice_updated:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append(
                "CRITICAL: Privacy notice not updated to meet NJDPA Section 7 requirements"
            )

        return {
            "status": status.value,
            "findings": findings,
        }

    def run_full_assessment(self) -> dict:
        """Execute complete NJDPA compliance assessment."""
        applicability = self.assess_applicability()

        if not applicability["applicable"]:
            return {
                "organization": self.organization_name,
                "assessment_date": self.assessment_date.isoformat(),
                "applicability": applicability,
                "overall_status": ComplianceStatus.NOT_APPLICABLE.value,
                "message": "NJDPA does not apply to this organization",
            }

        sensitive_data = self.assess_sensitive_data_compliance()
        consumer_rights = self.assess_consumer_rights()
        dpa_obligations = self.assess_dpa_obligations()
        privacy_notice = self.assess_privacy_notice()

        all_statuses = [
            sensitive_data["status"],
            consumer_rights["status"],
            dpa_obligations["status"],
            privacy_notice["status"],
        ]

        if ComplianceStatus.NON_COMPLIANT.value in all_statuses:
            overall = ComplianceStatus.NON_COMPLIANT
        elif ComplianceStatus.PARTIAL.value in all_statuses:
            overall = ComplianceStatus.PARTIAL
        else:
            overall = ComplianceStatus.COMPLIANT

        all_findings = []
        for section in [sensitive_data, consumer_rights, dpa_obligations, privacy_notice]:
            all_findings.extend(section.get("findings", []))

        risk = RiskLevel.LOW
        critical_count = sum(1 for f in all_findings if f.startswith("CRITICAL"))
        if critical_count >= 3:
            risk = RiskLevel.CRITICAL
        elif critical_count >= 1:
            risk = RiskLevel.HIGH
        elif ComplianceStatus.PARTIAL.value in all_statuses:
            risk = RiskLevel.MEDIUM

        return {
            "organization": self.organization_name,
            "assessment_date": self.assessment_date.isoformat(),
            "applicability": applicability,
            "sensitive_data_compliance": sensitive_data,
            "consumer_rights_compliance": consumer_rights,
            "dpa_obligations": dpa_obligations,
            "privacy_notice": privacy_notice,
            "overall_status": overall.value,
            "risk_level": risk.value,
            "total_findings": len(all_findings),
            "critical_findings": critical_count,
        }


def generate_compliance_report(assessment_result: dict) -> str:
    """Generate a formatted NJDPA compliance report."""
    lines = [
        "=" * 70,
        "NEW JERSEY DATA PRIVACY ACT (NJDPA) COMPLIANCE REPORT",
        "=" * 70,
        f"Organization: {assessment_result['organization']}",
        f"Assessment Date: {assessment_result['assessment_date']}",
        f"Overall Status: {assessment_result['overall_status'].upper()}",
        f"Risk Level: {assessment_result.get('risk_level', 'N/A').upper()}",
        "",
    ]

    if not assessment_result["applicability"]["applicable"]:
        lines.append(f"Applicability: NOT APPLICABLE — {assessment_result['applicability']['reason']}")
        return "\n".join(lines)

    lines.append(f"Applicability: APPLICABLE — {assessment_result['applicability']['reason']}")
    lines.append("")

    sections = [
        ("Sensitive Data Compliance", "sensitive_data_compliance"),
        ("Consumer Rights Compliance", "consumer_rights_compliance"),
        ("Data Protection Assessments", "dpa_obligations"),
        ("Privacy Notice", "privacy_notice"),
    ]

    for title, key in sections:
        section = assessment_result.get(key, {})
        lines.append(f"--- {title} ---")
        lines.append(f"Status: {section.get('status', 'N/A').upper()}")
        for finding in section.get("findings", []):
            lines.append(f"  - {finding}")
        lines.append("")

    lines.append(f"Total Findings: {assessment_result.get('total_findings', 0)}")
    lines.append(f"Critical Findings: {assessment_result.get('critical_findings', 0)}")
    lines.append("=" * 70)

    return "\n".join(lines)


if __name__ == "__main__":
    assessment = NJDPAComplianceAssessment(
        organization_name="Example Corp",
        nj_consumer_count=150000,
        derives_revenue_from_data_sale=True,
        sensitive_data_categories=["financial_information", "precise_geolocation"],
        consent_mechanism_implemented=True,
        universal_opt_out_supported=False,
        privacy_notice_updated=True,
        consumer_rights_channels=["web_form", "email", "toll_free"],
        identity_verification_process=True,
        dpa_activities=["targeted_advertising", "sale_of_personal_data"],
        dpas_conducted=[
            DataProtectionAssessment(
                assessment_id="DPA-001",
                processing_activity="Targeted advertising program",
                trigger_category="targeted_advertising",
                date_conducted=datetime(2025, 1, 10),
                benefits_analysis="Revenue generation through personalized ads",
                risk_analysis="Consumer profiling based on browsing behaviour",
                safeguards=["opt-out mechanism", "data minimisation", "30-day retention"],
                residual_risk=RiskLevel.MEDIUM,
            )
        ],
    )

    result = assessment.run_full_assessment()
    print(generate_compliance_report(result))
    print("\nJSON Output:")
    print(json.dumps(result, indent=2, default=str))
