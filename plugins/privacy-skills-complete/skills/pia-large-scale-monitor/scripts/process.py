"""
Large-Scale Monitoring Privacy Impact Assessment engine.
Evaluates monitoring systems against GDPR Article 35(3)(c), EDPB Guidelines
3/2019, and workplace monitoring requirements.
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


class MonitoringType(Enum):
    CCTV = "cctv_video_surveillance"
    EMPLOYEE_EMAIL = "employee_email_monitoring"
    EMPLOYEE_INTERNET = "employee_internet_monitoring"
    KEYSTROKE = "keystroke_logging"
    SCREEN_RECORDING = "screen_recording"
    GPS_TRACKING = "gps_vehicle_tracking"
    BADGE_ACCESS = "badge_access_tracking"
    BEHAVIOURAL_ANALYTICS = "behavioural_analytics"
    FACIAL_RECOGNITION = "facial_recognition"
    WIFI_TRACKING = "wifi_bluetooth_tracking"


PUBLICLY_ACCESSIBLE_TYPES = {
    MonitoringType.CCTV,
    MonitoringType.FACIAL_RECOGNITION,
    MonitoringType.WIFI_TRACKING,
    MonitoringType.BEHAVIOURAL_ANALYTICS,
}


@dataclass
class MonitoringSystem:
    system_id: str
    name: str
    monitoring_type: MonitoringType
    purpose: str
    publicly_accessible_area: bool = False
    subject_count: int = 0
    continuous: bool = False
    retention_hours: int = 72
    lawful_basis: str = ""
    transparency_signage: bool = False
    privacy_notice_accessible: bool = False
    access_controls_documented: bool = False
    facial_recognition: bool = False
    employee_policy_distributed: bool = False
    works_council_consulted: bool = False
    proportionality_assessed: bool = False
    automated_deletion: bool = False
    alternative_measures_assessed: bool = False


@dataclass
class LargeScaleMonitoringPIA:
    organisation_name: str
    assessment_date: datetime = field(default_factory=datetime.now)
    monitoring_systems: list = field(default_factory=list)
    dpia_documented: bool = False
    dpo_consulted: bool = False
    review_schedule: str = ""

    def assess_dpia_trigger(self, system: MonitoringSystem) -> dict:
        """Determine if a monitoring system triggers mandatory DPIA."""
        triggers = []

        if system.publicly_accessible_area:
            triggers.append("Art. 35(3)(c): systematic monitoring of publicly accessible area")

        if system.subject_count > 10000:
            triggers.append("WP248 C4: large scale processing")

        if system.continuous:
            triggers.append("WP248 C3: systematic monitoring")

        if system.facial_recognition:
            triggers.append("WP248 C5: special category data (biometric)")
            triggers.append("WP248 C8: innovative technology")

        if system.monitoring_type in (MonitoringType.KEYSTROKE, MonitoringType.SCREEN_RECORDING):
            triggers.append("WP248 C7: vulnerable data subjects (employees in power imbalance)")

        return {
            "system_id": system.system_id,
            "dpia_mandatory": len(triggers) >= 1,
            "trigger_count": len(triggers),
            "triggers": triggers,
        }

    def assess_cctv_compliance(self) -> dict:
        """Assess CCTV systems against EDPB Guidelines 3/2019."""
        findings = []
        status = ComplianceStatus.COMPLIANT

        cctv_systems = [
            s for s in self.monitoring_systems
            if s.monitoring_type in (MonitoringType.CCTV, MonitoringType.FACIAL_RECOGNITION)
        ]

        if not cctv_systems:
            return {
                "status": ComplianceStatus.NOT_APPLICABLE.value,
                "findings": ["No CCTV/video surveillance systems identified"],
            }

        for system in cctv_systems:
            if not system.lawful_basis:
                status = ComplianceStatus.NON_COMPLIANT
                findings.append(
                    f"CRITICAL: System '{system.system_id}' has no documented lawful basis"
                )

            if system.publicly_accessible_area and not system.transparency_signage:
                status = ComplianceStatus.NON_COMPLIANT
                findings.append(
                    f"CRITICAL: System '{system.system_id}' monitors publicly accessible area "
                    "without transparency signage (EDPB Guidelines 3/2019 requirement)"
                )

            if not system.privacy_notice_accessible:
                if status == ComplianceStatus.COMPLIANT:
                    status = ComplianceStatus.PARTIAL
                findings.append(
                    f"System '{system.system_id}': full privacy notice not accessible "
                    "to monitored individuals"
                )

            if system.retention_hours > 72 and not system.proportionality_assessed:
                if status == ComplianceStatus.COMPLIANT:
                    status = ComplianceStatus.PARTIAL
                findings.append(
                    f"System '{system.system_id}': retention ({system.retention_hours}h) "
                    "exceeds EDPB 72h default without documented proportionality assessment"
                )

            if system.facial_recognition:
                findings.append(
                    f"System '{system.system_id}': facial recognition in use — "
                    "verify explicit consent or substantial public interest basis; "
                    "biometric data DPIA mandatory"
                )

        return {"status": status.value, "findings": findings}

    def assess_employee_monitoring(self) -> dict:
        """Assess employee monitoring against Barbulescu criteria."""
        findings = []
        status = ComplianceStatus.COMPLIANT

        employee_systems = [
            s for s in self.monitoring_systems
            if s.monitoring_type in (
                MonitoringType.EMPLOYEE_EMAIL,
                MonitoringType.EMPLOYEE_INTERNET,
                MonitoringType.KEYSTROKE,
                MonitoringType.SCREEN_RECORDING,
                MonitoringType.GPS_TRACKING,
                MonitoringType.BADGE_ACCESS,
            )
        ]

        if not employee_systems:
            return {
                "status": ComplianceStatus.NOT_APPLICABLE.value,
                "findings": ["No employee monitoring systems identified"],
            }

        for system in employee_systems:
            if not system.employee_policy_distributed:
                status = ComplianceStatus.NON_COMPLIANT
                findings.append(
                    f"CRITICAL: System '{system.system_id}' — employee monitoring policy "
                    "not distributed (Barbulescu criterion: prior notification)"
                )

            if not system.proportionality_assessed:
                if status == ComplianceStatus.COMPLIANT:
                    status = ComplianceStatus.PARTIAL
                findings.append(
                    f"System '{system.system_id}': proportionality assessment not conducted "
                    "(Barbulescu v Romania, Grand Chamber, 2017)"
                )

            if not system.alternative_measures_assessed:
                if status == ComplianceStatus.COMPLIANT:
                    status = ComplianceStatus.PARTIAL
                findings.append(
                    f"System '{system.system_id}': less intrusive alternatives not assessed"
                )

            if system.monitoring_type in (MonitoringType.KEYSTROKE, MonitoringType.SCREEN_RECORDING):
                findings.append(
                    f"System '{system.system_id}': {system.monitoring_type.value} is highly "
                    "intrusive — requires strong justification and strict proportionality "
                    "(CNIL vs Amazon France Logistique, 2024: EUR 32M fine)"
                )

            if system.monitoring_type == MonitoringType.GPS_TRACKING and system.continuous:
                findings.append(
                    f"System '{system.system_id}': continuous GPS tracking — ensure "
                    "tracking disabled outside working hours "
                    "(Romanian DPA vs Raiffeisen Bank, 2020: EUR 150K fine)"
                )

        return {"status": status.value, "findings": findings}

    def assess_retention_and_deletion(self) -> dict:
        """Assess retention periods and automated deletion."""
        findings = []
        status = ComplianceStatus.COMPLIANT

        for system in self.monitoring_systems:
            if not system.automated_deletion:
                if status == ComplianceStatus.COMPLIANT:
                    status = ComplianceStatus.PARTIAL
                findings.append(
                    f"System '{system.system_id}': automated deletion not implemented; "
                    "manual deletion increases risk of over-retention"
                )

            if system.retention_hours > 720:  # > 30 days
                findings.append(
                    f"System '{system.system_id}': retention of {system.retention_hours}h "
                    f"({system.retention_hours / 24:.0f} days) — ensure documented justification"
                )

        return {"status": status.value, "findings": findings}

    def calculate_risk(self) -> dict:
        """Calculate overall monitoring risk level."""
        findings = []
        max_risk_score = 0

        for system in self.monitoring_systems:
            score = 0
            if system.publicly_accessible_area:
                score += 3
            if system.continuous:
                score += 2
            if system.facial_recognition:
                score += 4
            if system.subject_count > 100000:
                score += 3
            elif system.subject_count > 10000:
                score += 2
            elif system.subject_count > 1000:
                score += 1
            if system.monitoring_type in (MonitoringType.KEYSTROKE, MonitoringType.SCREEN_RECORDING):
                score += 3

            risk = RiskLevel.LOW
            if score >= 8:
                risk = RiskLevel.CRITICAL
            elif score >= 5:
                risk = RiskLevel.HIGH
            elif score >= 3:
                risk = RiskLevel.MEDIUM

            max_risk_score = max(max_risk_score, score)
            findings.append(
                f"System '{system.system_id}' ({system.monitoring_type.value}): "
                f"risk score {score} — {risk.value.upper()}"
            )

        overall = RiskLevel.LOW
        if max_risk_score >= 8:
            overall = RiskLevel.CRITICAL
        elif max_risk_score >= 5:
            overall = RiskLevel.HIGH
        elif max_risk_score >= 3:
            overall = RiskLevel.MEDIUM

        return {"overall_risk": overall.value, "findings": findings}

    def run_full_assessment(self) -> dict:
        dpia_triggers = [self.assess_dpia_trigger(s) for s in self.monitoring_systems]
        cctv = self.assess_cctv_compliance()
        employee = self.assess_employee_monitoring()
        retention = self.assess_retention_and_deletion()
        risk = self.calculate_risk()

        all_statuses = [cctv["status"], employee["status"], retention["status"]]
        active = [s for s in all_statuses if s != ComplianceStatus.NOT_APPLICABLE.value]

        if ComplianceStatus.NON_COMPLIANT.value in active:
            overall = ComplianceStatus.NON_COMPLIANT
        elif ComplianceStatus.PARTIAL.value in active:
            overall = ComplianceStatus.PARTIAL
        else:
            overall = ComplianceStatus.COMPLIANT

        all_findings = []
        for section in [cctv, employee, retention, risk]:
            all_findings.extend(section.get("findings", []))
        critical = sum(1 for f in all_findings if f.startswith("CRITICAL"))

        return {
            "organisation": self.organisation_name,
            "assessment_date": self.assessment_date.isoformat(),
            "monitoring_systems_count": len(self.monitoring_systems),
            "dpia_triggers": dpia_triggers,
            "cctv_compliance": cctv,
            "employee_monitoring": employee,
            "retention_deletion": retention,
            "risk_assessment": risk,
            "overall_status": overall.value,
            "overall_risk": risk["overall_risk"],
            "total_findings": len(all_findings),
            "critical_findings": critical,
        }


def generate_report(result: dict) -> str:
    lines = [
        "=" * 70,
        "LARGE-SCALE MONITORING PRIVACY IMPACT ASSESSMENT REPORT",
        "=" * 70,
        f"Organisation: {result['organisation']}",
        f"Assessment Date: {result['assessment_date']}",
        f"Monitoring Systems: {result['monitoring_systems_count']}",
        f"Overall Status: {result['overall_status'].upper()}",
        f"Overall Risk: {result.get('overall_risk', 'N/A').upper()}",
        "",
    ]

    lines.append("--- DPIA Trigger Analysis ---")
    for trigger in result.get("dpia_triggers", []):
        mandatory = "MANDATORY" if trigger["dpia_mandatory"] else "NOT REQUIRED"
        lines.append(f"  {trigger['system_id']}: DPIA {mandatory} ({trigger['trigger_count']} triggers)")
        for t in trigger.get("triggers", []):
            lines.append(f"    - {t}")
    lines.append("")

    sections = [
        ("CCTV Compliance", "cctv_compliance"),
        ("Employee Monitoring", "employee_monitoring"),
        ("Retention and Deletion", "retention_deletion"),
        ("Risk Assessment", "risk_assessment"),
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
    pia = LargeScaleMonitoringPIA(
        organisation_name="Metro Shopping Centre Ltd",
        monitoring_systems=[
            MonitoringSystem(
                system_id="MON-001",
                name="Main Floor CCTV",
                monitoring_type=MonitoringType.CCTV,
                purpose="Loss prevention and customer safety",
                publicly_accessible_area=True,
                subject_count=50000,
                continuous=True,
                retention_hours=168,
                lawful_basis="legitimate_interests",
                transparency_signage=True,
                privacy_notice_accessible=True,
                access_controls_documented=True,
                proportionality_assessed=True,
                automated_deletion=True,
            ),
            MonitoringSystem(
                system_id="MON-002",
                name="Employee Email Monitoring",
                monitoring_type=MonitoringType.EMPLOYEE_EMAIL,
                purpose="Data loss prevention",
                subject_count=500,
                continuous=True,
                retention_hours=720,
                lawful_basis="legitimate_interests",
                employee_policy_distributed=True,
                proportionality_assessed=True,
                alternative_measures_assessed=True,
                automated_deletion=False,
            ),
            MonitoringSystem(
                system_id="MON-003",
                name="Delivery Vehicle GPS",
                monitoring_type=MonitoringType.GPS_TRACKING,
                purpose="Fleet management and delivery optimisation",
                subject_count=120,
                continuous=True,
                retention_hours=2160,
                lawful_basis="legitimate_interests",
                employee_policy_distributed=True,
                proportionality_assessed=False,
                alternative_measures_assessed=False,
                automated_deletion=False,
            ),
        ],
        dpia_documented=True,
        dpo_consulted=True,
        review_schedule="annual",
    )

    result = pia.run_full_assessment()
    print(generate_report(result))
    print("\nJSON Output:")
    print(json.dumps(result, indent=2, default=str))
