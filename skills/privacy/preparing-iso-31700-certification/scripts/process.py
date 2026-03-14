#!/usr/bin/env python3
"""
ISO 31700 Gap Assessment Engine

Automates the gap assessment process for ISO 31700 Privacy by Design
certification, scoring each of the 30 requirements and generating
a prioritized remediation roadmap.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from enum import Enum
from typing import Optional


class LifecyclePhase(Enum):
    DESIGN = "Design"
    PRODUCTION = "Production"
    DISPOSAL = "Disposal"


class MaturityLevel(Enum):
    NON_EXISTENT = (0, "Non-existent", "No awareness of the requirement")
    INITIAL = (1, "Initial", "Awareness exists but no formal implementation")
    DEVELOPING = (2, "Developing", "Partial implementation, ad hoc processes")
    DEFINED = (3, "Defined", "Formal processes documented and communicated")
    MANAGED = (4, "Managed", "Processes monitored, measured, and consistently applied")
    OPTIMIZING = (5, "Optimizing", "Continuous improvement based on metrics")

    def __init__(self, score: int, label: str, description: str):
        self.score = score
        self.label = label
        self._description = description


@dataclass
class Requirement:
    """An ISO 31700 requirement."""
    number: int
    title: str
    phase: LifecyclePhase
    gdpr_mapping: str
    current_score: int = 0
    target_score: int = 3
    evidence: str = ""
    gap_description: str = ""
    remediation_action: str = ""
    owner: str = ""
    target_date: str = ""

    @property
    def is_gap(self) -> bool:
        return self.current_score < self.target_score

    @property
    def gap_severity(self) -> str:
        if self.current_score >= self.target_score:
            return "NONE"
        elif self.current_score <= 1:
            return "CRITICAL"
        elif self.current_score == 2:
            return "MAJOR"
        else:
            return "MINOR"


class ISO31700Assessment:
    """Conducts an ISO 31700 gap assessment."""

    def __init__(self, organization: str = "Prism Data Systems AG",
                 assessor: str = "Dr. Lukas Meier"):
        self.organization = organization
        self.assessor = assessor
        self.assessment_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        self.requirements: list[Requirement] = []
        self._load_requirements()

    def _load_requirements(self):
        """Load all 30 ISO 31700 requirements with Prism Data Systems AG scores."""
        reqs = [
            # Design Phase (1-16)
            (1, "Designing privacy controls", LifecyclePhase.DESIGN, "Art. 25(1), 25(2)", 4,
             "Privacy controls implemented in all consumer products via preference center"),
            (2, "Privacy notice and consent", LifecyclePhase.DESIGN, "Art. 12-14", 4,
             "Layered privacy notices at all collection points; granular consent mechanism"),
            (3, "Consumer PII collection", LifecyclePhase.DESIGN, "Art. 5(1)(c)", 4,
             "API allowlist validation; data minimization assessment for each endpoint"),
            (4, "Creating and managing consumer PII", LifecyclePhase.DESIGN, "Art. 5(1)(d), 5(1)(e)", 4,
             "Automated lifecycle management with TTL-based deletion"),
            (5, "Consumer PII use limitation", LifecyclePhase.DESIGN, "Art. 5(1)(b)", 4,
             "Purpose registry with OPA enforcement; compatibility assessments documented"),
            (6, "Consumer PII disclosure to third parties", LifecyclePhase.DESIGN, "Art. 28, 44-49", 3,
             "DPA with all processors; Art. 30 records updated; SCC for international transfers"),
            (7, "Consumer PII quality", LifecyclePhase.DESIGN, "Art. 5(1)(d)", 3,
             "Self-service profile editing; data validation at ingestion"),
            (8, "Consumer PII security", LifecyclePhase.DESIGN, "Art. 32", 4,
             "Field-level encryption, TLS 1.3, RBAC, SOC 2 Type II certified"),
            (9, "Consumer PII retention", LifecyclePhase.DESIGN, "Art. 5(1)(e)", 4,
             "Automated retention enforcement; retention schedule documented and enforced"),
            (10, "Organizational commitment", LifecyclePhase.DESIGN, "Art. 24", 4,
              "DPO appointed; privacy budget allocated; board-level privacy reporting"),
            (11, "Privacy risk assessment", LifecyclePhase.DESIGN, "Art. 35", 4,
              "DPIA conducted for all high-risk processing; LINDDUN threat modeling"),
            (12, "Designing PII processing rights", LifecyclePhase.DESIGN, "Art. 15-20", 4,
              "Self-service DSAR portal; automated data export; erasure workflow"),
            (13, "Designing ergonomic privacy controls", LifecyclePhase.DESIGN, "Art. 25(2)", 3,
              "Usability testing of privacy preference center; WCAG 2.1 AA compliant"),
            (14, "Designing privacy for vulnerable consumers", LifecyclePhase.DESIGN, "Art. 8", 2,
              "Age verification implemented but no formal design review for elderly users"),
            (15, "Supply chain management", LifecyclePhase.DESIGN, "Art. 28", 3,
              "Privacy requirements in procurement; annual processor audits"),
            (16, "Designing for disposal", LifecyclePhase.DESIGN, "Art. 17", 2,
              "Database deletion automated; IoT device firmware lacks data wipe function"),
            # Production Phase (17-24)
            (17, "Privacy awareness and training", LifecyclePhase.PRODUCTION, "Art. 39(1)(b)", 4,
              "Annual privacy training for all staff; role-specific modules for engineering"),
            (18, "Privacy operations", LifecyclePhase.PRODUCTION, "Art. 24, 25(1)", 4,
              "Privacy operations handbook; daily retention job monitoring"),
            (19, "Privacy breach management", LifecyclePhase.PRODUCTION, "Art. 33, 34", 4,
              "Incident response plan; 72-hour notification procedure; tabletop exercises quarterly"),
            (20, "Communication with consumers", LifecyclePhase.PRODUCTION, "Art. 12(2)", 3,
              "Privacy inbox monitored; FAQ page; DPO contact published"),
            (21, "Third-party management", LifecyclePhase.PRODUCTION, "Art. 28", 3,
              "Processor register maintained; annual DPA review; sub-processor notification"),
            (22, "Consumer PII use", LifecyclePhase.PRODUCTION, "Art. 5(1)(b)", 4,
              "OPA purpose enforcement in production; weekly compliance dashboard review"),
            (23, "Managing privacy inquiries", LifecyclePhase.PRODUCTION, "Art. 12(3)", 3,
              "DSAR response within 25 days (below 30-day limit); tracking system in place"),
            (24, "Privacy performance monitoring", LifecyclePhase.PRODUCTION, "Art. 24(1)", 2,
              "Ad hoc monitoring; formal KPIs and dashboard not yet implemented"),
            # Disposal Phase (25-30)
            (25, "End-of-life PII management", LifecyclePhase.DISPOSAL, "Art. 17", 2,
              "Database records handled; no formal end-of-life process for decommissioned products"),
            (26, "Consumer notification of disposal", LifecyclePhase.DISPOSAL, "Art. 13", 3,
              "Account closure email includes data handling information"),
            (27, "PII disposal", LifecyclePhase.DISPOSAL, "Art. 5(1)(e), 17", 1,
              "Database deletion automated; physical media disposal lacks verification procedure"),
            (28, "Data portability at end of life", LifecyclePhase.DISPOSAL, "Art. 20", 3,
              "Data export available before account closure; JSON and CSV formats"),
            (29, "Supply chain disposal", LifecyclePhase.DISPOSAL, "Art. 28(3)(g)", 2,
              "DPA includes deletion clause; no verification of supplier data deletion"),
            (30, "Disposal documentation", LifecyclePhase.DISPOSAL, "Art. 5(2)", 3,
              "Deletion logs maintained; physical media disposal logs incomplete"),
        ]

        for num, title, phase, gdpr, score, evidence in reqs:
            self.requirements.append(Requirement(
                number=num,
                title=title,
                phase=phase,
                gdpr_mapping=gdpr,
                current_score=score,
                evidence=evidence,
            ))

    def identify_gaps(self) -> list[Requirement]:
        """Identify all requirements scoring below the target."""
        gaps = [r for r in self.requirements if r.is_gap]

        # Add remediation details for Prism Data Systems AG
        remediation_map = {
            14: ("Document formal accessibility and child safety design review stage gate",
                 "UX Engineering", "2026-06-15"),
            16: ("Add data wipe functionality to IoT device firmware; test remotely",
                 "Firmware Engineering", "2026-07-01"),
            24: ("Define KPIs for each privacy control; implement monitoring dashboard",
                 "Privacy Engineering", "2026-06-01"),
            25: ("Define end-of-life procedures for each product line",
                 "Product Management", "2026-05-15"),
            27: ("Implement NIST SP 800-88 media sanitization with certificate of destruction",
                 "IT Operations", "2026-05-01"),
            29: ("Add disposal audit clause to supplier contracts; annual verification",
                 "Procurement", "2026-06-01"),
        }

        for gap in gaps:
            if gap.number in remediation_map:
                action, owner, target = remediation_map[gap.number]
                gap.remediation_action = action
                gap.owner = owner
                gap.target_date = target
                gap.gap_description = f"Requirement {gap.number} ({gap.title}) scores {gap.current_score}/5, below minimum of {gap.target_score}"

        return gaps

    def generate_report(self) -> dict:
        """Generate the full gap assessment report."""
        gaps = self.identify_gaps()

        by_phase = {}
        for phase in LifecyclePhase:
            phase_reqs = [r for r in self.requirements if r.phase == phase]
            avg_score = sum(r.current_score for r in phase_reqs) / len(phase_reqs) if phase_reqs else 0
            phase_gaps = [r for r in phase_reqs if r.is_gap]
            critical_gaps = [r for r in phase_gaps if r.gap_severity == "CRITICAL"]
            by_phase[phase.value] = {
                "requirements_count": len(phase_reqs),
                "average_score": round(avg_score, 1),
                "gaps": len(phase_gaps),
                "critical_gaps": len(critical_gaps),
            }

        overall_avg = sum(r.current_score for r in self.requirements) / len(self.requirements)

        return {
            "organization": self.organization,
            "assessor": self.assessor,
            "assessment_date": self.assessment_date,
            "total_requirements": len(self.requirements),
            "overall_average_score": round(overall_avg, 1),
            "total_gaps": len(gaps),
            "critical_gaps": sum(1 for g in gaps if g.gap_severity == "CRITICAL"),
            "major_gaps": sum(1 for g in gaps if g.gap_severity == "MAJOR"),
            "certification_ready": len(gaps) == 0,
            "by_phase": by_phase,
            "gap_register": [
                {
                    "requirement": g.number,
                    "title": g.title,
                    "phase": g.phase.value,
                    "current_score": g.current_score,
                    "target_score": g.target_score,
                    "severity": g.gap_severity,
                    "remediation": g.remediation_action,
                    "owner": g.owner,
                    "target_date": g.target_date,
                }
                for g in sorted(gaps, key=lambda x: x.current_score)
            ],
        }


def run_example():
    """Demonstrate ISO 31700 gap assessment for Prism Data Systems AG."""

    assessment = ISO31700Assessment()

    print("=== ISO 31700 Gap Assessment Report ===")
    print(f"Organization: {assessment.organization}")
    print(f"Assessor: {assessment.assessor}")
    print(f"Date: {assessment.assessment_date}")
    print()

    report = assessment.generate_report()

    print(f"Total Requirements: {report['total_requirements']}")
    print(f"Overall Average Score: {report['overall_average_score']}/5")
    print(f"Certification Ready: {'Yes' if report['certification_ready'] else 'No'}")
    print(f"Total Gaps: {report['total_gaps']}")
    print(f"  Critical: {report['critical_gaps']}")
    print(f"  Major: {report['major_gaps']}")
    print()

    print("--- By Lifecycle Phase ---")
    for phase, data in report["by_phase"].items():
        print(f"  {phase}: avg={data['average_score']}/5, "
              f"gaps={data['gaps']}, critical={data['critical_gaps']}")
    print()

    print("--- Gap Register (sorted by severity) ---")
    for gap in report["gap_register"]:
        print(f"  Req {gap['requirement']}: {gap['title']}")
        print(f"    Phase: {gap['phase']}, Score: {gap['current_score']}/{gap['target_score']}, "
              f"Severity: {gap['severity']}")
        print(f"    Remediation: {gap['remediation']}")
        print(f"    Owner: {gap['owner']}, Target: {gap['target_date']}")
        print()

    print("--- Requirement Scores ---")
    for req in assessment.requirements:
        status = "GAP" if req.is_gap else "OK"
        bar = "#" * req.current_score + "." * (5 - req.current_score)
        print(f"  Req {req.number:2d} [{bar}] {req.current_score}/5 {status:3s} {req.title}")


if __name__ == "__main__":
    run_example()
