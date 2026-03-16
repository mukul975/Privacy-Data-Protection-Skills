"""
Health Data Privacy Impact Assessment engine.
Evaluates health data processing compliance against GDPR Article 9,
HIPAA Privacy Rule, and sector-specific health privacy regulations.
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


class SensitivityTier(Enum):
    TIER_1 = "routine_clinical"
    TIER_2 = "sensitive_diagnoses"
    TIER_3 = "genetic_genomic"


ARTICLE_9_EXCEPTIONS = [
    "explicit_consent",
    "employment_obligations",
    "vital_interests",
    "health_care_provision",
    "public_health",
    "scientific_research",
    "substantial_public_interest",
    "legal_claims",
]

HIPAA_SAFE_HARBOR_IDENTIFIERS = [
    "names", "geographic_subdivisions", "dates", "phone_numbers",
    "fax_numbers", "email_addresses", "ssn", "medical_record_numbers",
    "health_plan_beneficiary_numbers", "account_numbers",
    "certificate_license_numbers", "vehicle_identifiers",
    "device_identifiers", "web_urls", "ip_addresses",
    "biometric_identifiers", "full_face_photos", "any_other_unique_number",
]


@dataclass
class HealthDataActivity:
    activity_id: str
    description: str
    data_categories: list = field(default_factory=list)
    sensitivity_tier: SensitivityTier = SensitivityTier.TIER_1
    article_6_basis: str = ""
    article_9_exception: str = ""
    hipaa_applicable: bool = False
    baa_in_place: bool = False
    subject_count: int = 0
    access_controls: dict = field(default_factory=dict)
    de_identified: bool = False
    de_identification_method: str = ""
    cross_border: bool = False


@dataclass
class AccessControlAssessment:
    rbac_implemented: bool = False
    two_factor_auth: bool = False
    audit_logging: bool = False
    break_glass_procedure: bool = False
    log_monitoring_frequency: str = ""
    anomaly_detection: bool = False


@dataclass
class HealthDataPIA:
    organisation_name: str
    assessment_date: datetime = field(default_factory=datetime.now)
    activities: list = field(default_factory=list)
    access_controls: Optional[AccessControlAssessment] = None
    dpia_documented: bool = False
    dpo_sign_off: bool = False
    caldicott_guardian_sign_off: bool = False
    review_schedule: str = ""
    findings: list = field(default_factory=list)

    def assess_lawful_basis(self) -> dict:
        findings = []
        status = ComplianceStatus.COMPLIANT

        for activity in self.activities:
            if not activity.article_6_basis:
                status = ComplianceStatus.NON_COMPLIANT
                findings.append(
                    f"CRITICAL: Activity '{activity.activity_id}' has no GDPR Art. 6 lawful basis"
                )

            if not activity.article_9_exception:
                status = ComplianceStatus.NON_COMPLIANT
                findings.append(
                    f"CRITICAL: Activity '{activity.activity_id}' processes health data "
                    "without Art. 9(2) exception"
                )
            elif activity.article_9_exception not in ARTICLE_9_EXCEPTIONS:
                status = ComplianceStatus.NON_COMPLIANT
                findings.append(
                    f"CRITICAL: Activity '{activity.activity_id}' has invalid Art. 9(2) "
                    f"exception: '{activity.article_9_exception}'"
                )

            if activity.article_9_exception == "health_care_provision":
                findings.append(
                    f"Activity '{activity.activity_id}': verify processing is by or under "
                    "responsibility of health professional subject to secrecy obligations"
                )

            if activity.article_9_exception == "scientific_research":
                findings.append(
                    f"Activity '{activity.activity_id}': verify Art. 89(1) safeguards "
                    "(pseudonymisation, data minimisation, ethics approval)"
                )

        return {"status": status.value, "findings": findings}

    def assess_hipaa_compliance(self) -> dict:
        findings = []
        status = ComplianceStatus.COMPLIANT

        hipaa_activities = [a for a in self.activities if a.hipaa_applicable]

        if not hipaa_activities:
            return {
                "status": ComplianceStatus.NOT_APPLICABLE.value,
                "findings": ["No HIPAA-applicable processing activities identified"],
            }

        for activity in hipaa_activities:
            if not activity.baa_in_place:
                status = ComplianceStatus.NON_COMPLIANT
                findings.append(
                    f"CRITICAL: Activity '{activity.activity_id}' involves HIPAA PHI "
                    "but no BAA in place with processor"
                )

            if activity.de_identified:
                if activity.de_identification_method not in ("safe_harbor", "expert_determination"):
                    if status == ComplianceStatus.COMPLIANT:
                        status = ComplianceStatus.PARTIAL
                    findings.append(
                        f"Activity '{activity.activity_id}' claims de-identification but "
                        "method not specified as Safe Harbor or Expert Determination"
                    )

        return {"status": status.value, "findings": findings}

    def assess_access_controls(self) -> dict:
        findings = []
        status = ComplianceStatus.COMPLIANT

        if self.access_controls is None:
            return {
                "status": ComplianceStatus.NON_COMPLIANT.value,
                "findings": ["CRITICAL: No access control assessment conducted for health data systems"],
            }

        ac = self.access_controls

        if not ac.rbac_implemented:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append(
                "CRITICAL: Role-based access control not implemented for health data systems"
            )

        if not ac.two_factor_auth:
            if status == ComplianceStatus.COMPLIANT:
                status = ComplianceStatus.PARTIAL
            findings.append(
                "Two-factor authentication not implemented for health data access "
                "(recommended by Dutch DPA enforcement action against OLVG Hospital)"
            )

        if not ac.audit_logging:
            status = ComplianceStatus.NON_COMPLIANT
            findings.append(
                "CRITICAL: Audit logging not implemented for health data access"
            )

        if not ac.break_glass_procedure:
            if status == ComplianceStatus.COMPLIANT:
                status = ComplianceStatus.PARTIAL
            findings.append(
                "Break-glass emergency access procedure not documented"
            )

        if not ac.anomaly_detection:
            findings.append(
                "Anomaly detection for unusual access patterns not implemented"
            )

        return {"status": status.value, "findings": findings}

    def assess_sensitivity_risks(self) -> dict:
        findings = []
        risk_scores = []

        for activity in self.activities:
            base_risk = {
                SensitivityTier.TIER_1: 2,
                SensitivityTier.TIER_2: 4,
                SensitivityTier.TIER_3: 5,
            }.get(activity.sensitivity_tier, 2)

            volume_factor = 1
            if activity.subject_count > 100000:
                volume_factor = 3
            elif activity.subject_count > 10000:
                volume_factor = 2

            cross_border_factor = 1.5 if activity.cross_border else 1.0

            risk_score = base_risk * volume_factor * cross_border_factor
            risk_scores.append(risk_score)

            risk_level = RiskLevel.LOW
            if risk_score >= 15:
                risk_level = RiskLevel.CRITICAL
            elif risk_score >= 10:
                risk_level = RiskLevel.HIGH
            elif risk_score >= 5:
                risk_level = RiskLevel.MEDIUM

            findings.append(
                f"Activity '{activity.activity_id}': {activity.sensitivity_tier.value}, "
                f"{activity.subject_count:,} subjects, "
                f"{'cross-border' if activity.cross_border else 'domestic'} — "
                f"risk level: {risk_level.value.upper()}"
            )

        max_risk = max(risk_scores) if risk_scores else 0
        overall_risk = RiskLevel.LOW
        if max_risk >= 15:
            overall_risk = RiskLevel.CRITICAL
        elif max_risk >= 10:
            overall_risk = RiskLevel.HIGH
        elif max_risk >= 5:
            overall_risk = RiskLevel.MEDIUM

        return {
            "overall_risk": overall_risk.value,
            "findings": findings,
        }

    def run_full_assessment(self) -> dict:
        lawful_basis = self.assess_lawful_basis()
        hipaa = self.assess_hipaa_compliance()
        access = self.assess_access_controls()
        sensitivity = self.assess_sensitivity_risks()

        all_statuses = [
            lawful_basis["status"],
            hipaa["status"],
            access["status"],
        ]
        active = [s for s in all_statuses if s != ComplianceStatus.NOT_APPLICABLE.value]

        if ComplianceStatus.NON_COMPLIANT.value in active:
            overall = ComplianceStatus.NON_COMPLIANT
        elif ComplianceStatus.PARTIAL.value in active:
            overall = ComplianceStatus.PARTIAL
        else:
            overall = ComplianceStatus.COMPLIANT

        all_findings = []
        for section in [lawful_basis, hipaa, access, sensitivity]:
            all_findings.extend(section.get("findings", []))

        critical_count = sum(1 for f in all_findings if f.startswith("CRITICAL"))

        documentation_findings = []
        if not self.dpia_documented:
            documentation_findings.append("DPIA not formally documented per Art. 35(7)")
        if not self.dpo_sign_off:
            documentation_findings.append("DPO sign-off not obtained")
        if not self.review_schedule:
            documentation_findings.append("Periodic review schedule not defined")

        return {
            "organisation": self.organisation_name,
            "assessment_date": self.assessment_date.isoformat(),
            "lawful_basis": lawful_basis,
            "hipaa_compliance": hipaa,
            "access_controls": access,
            "sensitivity_risk": sensitivity,
            "documentation": {
                "dpia_documented": self.dpia_documented,
                "dpo_sign_off": self.dpo_sign_off,
                "findings": documentation_findings,
            },
            "overall_status": overall.value,
            "overall_risk": sensitivity.get("overall_risk", "unknown"),
            "total_findings": len(all_findings) + len(documentation_findings),
            "critical_findings": critical_count,
        }


def generate_report(result: dict) -> str:
    lines = [
        "=" * 70,
        "HEALTH DATA PRIVACY IMPACT ASSESSMENT REPORT",
        "=" * 70,
        f"Organisation: {result['organisation']}",
        f"Assessment Date: {result['assessment_date']}",
        f"Overall Status: {result['overall_status'].upper()}",
        f"Overall Risk: {result.get('overall_risk', 'N/A').upper()}",
        "",
    ]

    sections = [
        ("Lawful Basis and Art. 9 Exceptions", "lawful_basis"),
        ("HIPAA Compliance", "hipaa_compliance"),
        ("Access Controls", "access_controls"),
        ("Sensitivity Risk Assessment", "sensitivity_risk"),
        ("Documentation", "documentation"),
    ]

    for title, key in sections:
        section = result.get(key, {})
        lines.append(f"--- {title} ---")
        if "status" in section:
            lines.append(f"Status: {section['status'].upper()}")
        for finding in section.get("findings", []):
            lines.append(f"  - {finding}")
        lines.append("")

    lines.append(f"Total Findings: {result.get('total_findings', 0)}")
    lines.append(f"Critical Findings: {result.get('critical_findings', 0)}")
    lines.append("=" * 70)

    return "\n".join(lines)


if __name__ == "__main__":
    pia = HealthDataPIA(
        organisation_name="City Hospital NHS Trust",
        activities=[
            HealthDataActivity(
                activity_id="HA-001",
                description="Electronic Health Records",
                data_categories=["medical_history", "diagnoses", "medications", "lab_results"],
                sensitivity_tier=SensitivityTier.TIER_1,
                article_6_basis="public_interest",
                article_9_exception="health_care_provision",
                subject_count=250000,
            ),
            HealthDataActivity(
                activity_id="HA-002",
                description="Mental health treatment records",
                data_categories=["psychiatric_diagnoses", "therapy_notes", "medication"],
                sensitivity_tier=SensitivityTier.TIER_2,
                article_6_basis="public_interest",
                article_9_exception="health_care_provision",
                subject_count=15000,
            ),
            HealthDataActivity(
                activity_id="HA-003",
                description="Genomic research study",
                data_categories=["dna_sequence", "genetic_test_results", "family_history"],
                sensitivity_tier=SensitivityTier.TIER_3,
                article_6_basis="public_interest",
                article_9_exception="scientific_research",
                subject_count=5000,
                cross_border=True,
            ),
        ],
        access_controls=AccessControlAssessment(
            rbac_implemented=True,
            two_factor_auth=True,
            audit_logging=True,
            break_glass_procedure=True,
            log_monitoring_frequency="daily",
            anomaly_detection=False,
        ),
        dpia_documented=True,
        dpo_sign_off=True,
        review_schedule="annual",
    )

    result = pia.run_full_assessment()
    print(generate_report(result))
    print("\nJSON Output:")
    print(json.dumps(result, indent=2, default=str))
