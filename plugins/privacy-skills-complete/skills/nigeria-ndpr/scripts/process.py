"""
Nigeria Data Protection Regulation (NDPR) and Nigeria Data Protection Act (NDPA)
compliance assessment engine. Evaluates organisational compliance against
NDPA requirements including registration, lawful basis, data subject rights,
cross-border transfers, DPCO audit obligations, and breach notification.
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


class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


NDPA_LAWFUL_BASES = [
    "consent",
    "contract",
    "legal_obligation",
    "vital_interests",
    "public_interest",
    "legitimate_interests",
]

NDPA_SENSITIVE_CATEGORIES = [
    "racial_ethnic_origin",
    "political_opinions",
    "religious_philosophical_beliefs",
    "trade_union_membership",
    "genetic_data",
    "biometric_data",
    "health_data",
    "sex_life_sexual_orientation",
    "criminal_convictions",
]

NDPA_DATA_SUBJECT_RIGHTS = [
    "right_to_be_informed",
    "right_of_access",
    "right_to_rectification",
    "right_to_erasure",
    "right_to_restrict_processing",
    "right_to_data_portability",
    "right_to_object",
    "right_automated_decisions",
]

DPIA_TRIGGERS = [
    "systematic_extensive_profiling",
    "large_scale_sensitive_data",
    "systematic_monitoring_public_area",
    "new_technology_processing",
]


@dataclass
class ProcessingActivity:
    activity_id: str
    description: str
    lawful_basis: str
    data_categories: list = field(default_factory=list)
    sensitive_data: bool = False
    cross_border_transfer: bool = False
    transfer_destination: str = ""
    transfer_safeguard: str = ""
    consent_documented: bool = False
    lia_conducted: bool = False


@dataclass
class BreachRecord:
    breach_id: str
    detected_date: datetime
    ndpc_notified_date: Optional[datetime] = None
    subjects_notified_date: Optional[datetime] = None
    high_risk: bool = False
    categories_affected: list = field(default_factory=list)
    subjects_affected_count: int = 0
    documented: bool = False

    @property
    def ndpc_notification_timely(self) -> bool:
        if self.ndpc_notified_date is None:
            return False
        return (self.ndpc_notified_date - self.detected_date) <= timedelta(hours=72)


@dataclass
class NDPAComplianceAssessment:
    organisation_name: str
    assessment_date: datetime = field(default_factory=datetime.now)
    registered_with_ndpc: bool = False
    data_subjects_count: int = 0
    dpco_engaged: bool = False
    dpco_audit_filed: bool = False
    last_audit_date: Optional[datetime] = None
    processing_activities: list = field(default_factory=list)
    breaches: list = field(default_factory=list)
    dpia_conducted_for: list = field(default_factory=list)
    privacy_notice_provided: bool = False
    dpo_appointed: bool = False
    findings: list = field(default_factory=list)

    def assess_registration(self) -> dict:
        findings = []
        status = ComplianceStatus.COMPLIANT

        if not self.registered_with_ndpc:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append(
                "CRITICAL: Organisation not registered with the NDPC as required under NDPA"
            )

        return {"status": status.value, "findings": findings}

    def assess_dpco_obligations(self) -> dict:
        findings = []
        status = ComplianceStatus.COMPLIANT

        if self.data_subjects_count <= 2000:
            return {
                "status": ComplianceStatus.NOT_APPLICABLE.value,
                "findings": ["Data subject count below 2,000 threshold; DPCO engagement not required"],
            }

        if not self.dpco_engaged:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append(
                "CRITICAL: DPCO not engaged despite processing data of "
                f"{self.data_subjects_count:,} data subjects (threshold: 2,000)"
            )

        if not self.dpco_audit_filed:
            if status == ComplianceStatus.COMPLIANT:
                status = ComplianceStatus.NON_COMPLIANT
            findings.append("CRITICAL: Annual DPCO audit report not filed with NDPC")

        if self.last_audit_date:
            months_since_audit = (self.assessment_date - self.last_audit_date).days / 30.44
            if months_since_audit > 12:
                if status == ComplianceStatus.COMPLIANT:
                    status = ComplianceStatus.PARTIAL
                findings.append(
                    f"Annual audit overdue: last audit was {months_since_audit:.0f} months ago"
                )

        return {"status": status.value, "findings": findings}

    def assess_lawful_basis(self) -> dict:
        findings = []
        status = ComplianceStatus.COMPLIANT

        if not self.processing_activities:
            return {
                "status": ComplianceStatus.PARTIAL.value,
                "findings": ["No processing activities documented; unable to assess lawful basis"],
            }

        for activity in self.processing_activities:
            if activity.lawful_basis not in NDPA_LAWFUL_BASES:
                status = ComplianceStatus.NON_COMPLIANT
                findings.append(
                    f"CRITICAL: Activity '{activity.activity_id}' has invalid lawful basis: "
                    f"'{activity.lawful_basis}'"
                )

            if activity.lawful_basis == "consent" and not activity.consent_documented:
                if status == ComplianceStatus.COMPLIANT:
                    status = ComplianceStatus.PARTIAL
                findings.append(
                    f"Activity '{activity.activity_id}' relies on consent but consent "
                    "records not documented"
                )

            if activity.lawful_basis == "legitimate_interests" and not activity.lia_conducted:
                if status == ComplianceStatus.COMPLIANT:
                    status = ComplianceStatus.PARTIAL
                findings.append(
                    f"Activity '{activity.activity_id}' relies on legitimate interests "
                    "but no LIA conducted"
                )

            if activity.sensitive_data and activity.lawful_basis != "consent":
                findings.append(
                    f"Activity '{activity.activity_id}' processes sensitive data without "
                    "explicit consent — verify applicable derogation"
                )

        return {"status": status.value, "findings": findings}

    def assess_cross_border_transfers(self) -> dict:
        findings = []
        status = ComplianceStatus.COMPLIANT

        transfer_activities = [a for a in self.processing_activities if a.cross_border_transfer]

        if not transfer_activities:
            return {
                "status": ComplianceStatus.NOT_APPLICABLE.value,
                "findings": ["No cross-border transfers identified"],
            }

        for activity in transfer_activities:
            if not activity.transfer_safeguard:
                status = ComplianceStatus.NON_COMPLIANT
                findings.append(
                    f"CRITICAL: Activity '{activity.activity_id}' transfers data to "
                    f"'{activity.transfer_destination}' without documented transfer safeguard"
                )
            else:
                findings.append(
                    f"Activity '{activity.activity_id}': transfer to "
                    f"'{activity.transfer_destination}' using {activity.transfer_safeguard}"
                )

        return {
            "status": status.value,
            "findings": findings,
            "transfer_count": len(transfer_activities),
        }

    def assess_breach_management(self) -> dict:
        findings = []
        status = ComplianceStatus.COMPLIANT

        if not self.breaches:
            return {
                "status": ComplianceStatus.COMPLIANT.value,
                "findings": ["No breaches recorded during assessment period"],
            }

        for breach in self.breaches:
            if not breach.documented:
                status = ComplianceStatus.NON_COMPLIANT
                findings.append(
                    f"CRITICAL: Breach '{breach.breach_id}' not documented in breach register"
                )

            if not breach.ndpc_notification_timely:
                status = ComplianceStatus.NON_COMPLIANT
                findings.append(
                    f"CRITICAL: Breach '{breach.breach_id}' — NDPC not notified within 72 hours"
                )

            if breach.high_risk and breach.subjects_notified_date is None:
                status = ComplianceStatus.NON_COMPLIANT
                findings.append(
                    f"CRITICAL: High-risk breach '{breach.breach_id}' — data subjects not notified"
                )

        return {
            "status": status.value,
            "findings": findings,
            "total_breaches": len(self.breaches),
        }

    def assess_dpia_obligations(self) -> dict:
        findings = []
        status = ComplianceStatus.COMPLIANT

        activities_needing_dpia = []
        for activity in self.processing_activities:
            if activity.sensitive_data:
                activities_needing_dpia.append(activity.activity_id)

        if not activities_needing_dpia:
            return {
                "status": ComplianceStatus.NOT_APPLICABLE.value,
                "findings": ["No processing activities identified as requiring DPIA"],
            }

        missing_dpias = [
            a for a in activities_needing_dpia if a not in self.dpia_conducted_for
        ]

        if missing_dpias:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append(
                f"CRITICAL: DPIAs not conducted for: {', '.join(missing_dpias)}"
            )

        return {
            "status": status.value,
            "findings": findings,
            "activities_requiring_dpia": activities_needing_dpia,
            "dpias_missing": missing_dpias,
        }

    def run_full_assessment(self) -> dict:
        registration = self.assess_registration()
        dpco = self.assess_dpco_obligations()
        lawful_basis = self.assess_lawful_basis()
        transfers = self.assess_cross_border_transfers()
        breaches = self.assess_breach_management()
        dpia = self.assess_dpia_obligations()

        all_statuses = [
            registration["status"],
            dpco["status"],
            lawful_basis["status"],
            transfers["status"],
            breaches["status"],
            dpia["status"],
        ]

        active_statuses = [s for s in all_statuses if s != ComplianceStatus.NOT_APPLICABLE.value]

        if ComplianceStatus.NON_COMPLIANT.value in active_statuses:
            overall = ComplianceStatus.NON_COMPLIANT
        elif ComplianceStatus.PARTIAL.value in active_statuses:
            overall = ComplianceStatus.PARTIAL
        else:
            overall = ComplianceStatus.COMPLIANT

        all_findings = []
        for section in [registration, dpco, lawful_basis, transfers, breaches, dpia]:
            all_findings.extend(section.get("findings", []))

        critical_count = sum(1 for f in all_findings if f.startswith("CRITICAL"))
        risk = RiskLevel.LOW
        if critical_count >= 3:
            risk = RiskLevel.CRITICAL
        elif critical_count >= 1:
            risk = RiskLevel.HIGH
        elif ComplianceStatus.PARTIAL.value in active_statuses:
            risk = RiskLevel.MEDIUM

        return {
            "organisation": self.organisation_name,
            "assessment_date": self.assessment_date.isoformat(),
            "registration": registration,
            "dpco_obligations": dpco,
            "lawful_basis": lawful_basis,
            "cross_border_transfers": transfers,
            "breach_management": breaches,
            "dpia_obligations": dpia,
            "overall_status": overall.value,
            "risk_level": risk.value,
            "total_findings": len(all_findings),
            "critical_findings": critical_count,
        }


def generate_report(result: dict) -> str:
    lines = [
        "=" * 70,
        "NIGERIA DATA PROTECTION ACT (NDPA) COMPLIANCE REPORT",
        "=" * 70,
        f"Organisation: {result['organisation']}",
        f"Assessment Date: {result['assessment_date']}",
        f"Overall Status: {result['overall_status'].upper()}",
        f"Risk Level: {result.get('risk_level', 'N/A').upper()}",
        "",
    ]

    sections = [
        ("NDPC Registration", "registration"),
        ("DPCO Obligations", "dpco_obligations"),
        ("Lawful Basis", "lawful_basis"),
        ("Cross-Border Transfers", "cross_border_transfers"),
        ("Breach Management", "breach_management"),
        ("DPIA Obligations", "dpia_obligations"),
    ]

    for title, key in sections:
        section = result.get(key, {})
        lines.append(f"--- {title} ---")
        lines.append(f"Status: {section.get('status', 'N/A').upper()}")
        for finding in section.get("findings", []):
            lines.append(f"  - {finding}")
        lines.append("")

    lines.append(f"Total Findings: {result.get('total_findings', 0)}")
    lines.append(f"Critical Findings: {result.get('critical_findings', 0)}")
    lines.append("=" * 70)

    return "\n".join(lines)


if __name__ == "__main__":
    assessment = NDPAComplianceAssessment(
        organisation_name="Lagos Tech Ltd",
        registered_with_ndpc=True,
        data_subjects_count=50000,
        dpco_engaged=True,
        dpco_audit_filed=True,
        last_audit_date=datetime(2025, 6, 15),
        privacy_notice_provided=True,
        dpo_appointed=True,
        processing_activities=[
            ProcessingActivity(
                activity_id="PA-001",
                description="Customer account management",
                lawful_basis="contract",
                data_categories=["name", "email", "phone", "address"],
            ),
            ProcessingActivity(
                activity_id="PA-002",
                description="Marketing communications",
                lawful_basis="consent",
                consent_documented=True,
                data_categories=["name", "email", "preferences"],
            ),
            ProcessingActivity(
                activity_id="PA-003",
                description="Cloud analytics processing",
                lawful_basis="legitimate_interests",
                lia_conducted=True,
                cross_border_transfer=True,
                transfer_destination="EU (Ireland)",
                transfer_safeguard="standard_contractual_clauses",
            ),
        ],
    )

    result = assessment.run_full_assessment()
    print(generate_report(result))
    print("\nJSON Output:")
    print(json.dumps(result, indent=2, default=str))
