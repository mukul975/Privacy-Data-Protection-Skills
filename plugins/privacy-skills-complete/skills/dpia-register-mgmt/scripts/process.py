#!/usr/bin/env python3
"""DPIA Register Management Tool.

Manages the organisational DPIA register tracking all Data Protection Impact
Assessments. Handles lifecycle management, review scheduling per Art. 35(11),
status tracking, overdue detection, and supervisory authority reporting.
"""

import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Optional


class DPIAStatus(Enum):
    SCREENING = "Screening"
    DRAFT = "Draft"
    DPO_REVIEW = "DPO Review"
    PRIOR_CONSULTATION = "Prior Consultation Pending"
    APPROVED = "Approved"
    ACTIVE_MONITORING = "Active Monitoring"
    REQUIRES_UPDATE = "Requires Update"
    REVISED = "Revised"
    RE_APPROVED = "Re-approved"
    ARCHIVED = "Archived"


class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    VERY_HIGH = "Very High"


class ReviewTrigger(Enum):
    SCHEDULED = "Scheduled periodic review"
    SCOPE_CHANGE = "Processing scope change"
    TECHNOLOGY_CHANGE = "Technology or system change"
    LEGAL_CHANGE = "Legal or regulatory change"
    INCIDENT = "Data breach or incident"
    ORGANISATIONAL_CHANGE = "Organisational change (merger, acquisition)"
    COMPLAINT = "Data subject complaint pattern"
    AUDIT_FINDING = "Internal or external audit finding"
    DPO_RECOMMENDATION = "DPO recommendation"


# Review frequency in days based on risk level
REVIEW_FREQUENCY = {
    RiskLevel.VERY_HIGH: 180,   # 6 months
    RiskLevel.HIGH: 365,        # 12 months
    RiskLevel.MEDIUM: 548,      # 18 months
    RiskLevel.LOW: 730,         # 24 months
}


@dataclass
class PriorConsultation:
    required: bool
    submission_date: Optional[str] = None
    sa_reference: Optional[str] = None
    response_date: Optional[str] = None
    outcome: Optional[str] = None  # Approved, Approved with conditions, Objected
    conditions: Optional[str] = None
    conditions_met: bool = False


@dataclass
class DPIAEntry:
    reference: str
    processing_activity: str
    department: str
    controller: str
    dpo_consulted: bool
    dpia_lead: str
    assessment_date: str
    status: DPIAStatus
    risk_level: RiskLevel
    ropa_reference: str
    mitigation_plan_ref: str
    approval_authority: str
    approval_date: Optional[str] = None
    review_date: Optional[str] = None
    prior_consultation: Optional[PriorConsultation] = None
    last_review_date: Optional[str] = None
    review_trigger: Optional[ReviewTrigger] = None
    archive_date: Optional[str] = None
    archive_reason: Optional[str] = None
    notes: str = ""


@dataclass
class DPIARegister:
    organisation: str
    register_owner: str
    entries: list = field(default_factory=list)
    created_date: str = ""
    last_updated: str = ""


def calculate_review_date(assessment_date: str, risk_level: RiskLevel) -> str:
    """Calculate next review date based on risk level."""
    base = datetime.strptime(assessment_date, "%Y-%m-%d")
    days = REVIEW_FREQUENCY[risk_level]
    review = base + timedelta(days=days)
    return review.strftime("%Y-%m-%d")


def find_overdue_reviews(register: DPIARegister, as_of: str) -> list:
    """Identify DPIAs with overdue reviews."""
    overdue = []
    for entry in register.entries:
        if entry.status in (DPIAStatus.ARCHIVED, DPIAStatus.SCREENING, DPIAStatus.DRAFT):
            continue
        if entry.review_date and entry.review_date < as_of:
            days_overdue = (
                datetime.strptime(as_of, "%Y-%m-%d")
                - datetime.strptime(entry.review_date, "%Y-%m-%d")
            ).days
            overdue.append({
                "reference": entry.reference,
                "processing_activity": entry.processing_activity,
                "review_date": entry.review_date,
                "days_overdue": days_overdue,
                "risk_level": entry.risk_level.value,
                "dpia_lead": entry.dpia_lead,
            })
    return sorted(overdue, key=lambda x: x["days_overdue"], reverse=True)


def get_status_summary(register: DPIARegister) -> dict:
    """Generate status distribution summary."""
    summary = {}
    for status in DPIAStatus:
        count = sum(1 for e in register.entries if e.status == status)
        if count > 0:
            summary[status.value] = count
    return summary


def get_risk_distribution(register: DPIARegister) -> dict:
    """Generate risk level distribution for active DPIAs."""
    active_statuses = {
        DPIAStatus.APPROVED, DPIAStatus.ACTIVE_MONITORING,
        DPIAStatus.RE_APPROVED, DPIAStatus.REQUIRES_UPDATE,
    }
    distribution = {}
    for level in RiskLevel:
        count = sum(
            1 for e in register.entries
            if e.status in active_statuses and e.risk_level == level
        )
        if count > 0:
            distribution[level.value] = count
    return distribution


def get_prior_consultation_summary(register: DPIARegister) -> dict:
    """Summarise Art. 36 prior consultation status."""
    consultations = [
        e for e in register.entries
        if e.prior_consultation and e.prior_consultation.required
    ]
    return {
        "total_required": len(consultations),
        "submitted": sum(1 for c in consultations if c.prior_consultation.submission_date),
        "responded": sum(1 for c in consultations if c.prior_consultation.response_date),
        "pending": sum(
            1 for c in consultations
            if c.prior_consultation.submission_date and not c.prior_consultation.response_date
        ),
        "conditions_met": sum(
            1 for c in consultations
            if c.prior_consultation.conditions and c.prior_consultation.conditions_met
        ),
        "conditions_outstanding": sum(
            1 for c in consultations
            if c.prior_consultation.conditions and not c.prior_consultation.conditions_met
        ),
    }


def assess_register_completeness(register: DPIARegister) -> dict:
    """Assess completeness and quality of the DPIA register."""
    findings = []

    for entry in register.entries:
        # Check DPO consultation
        if not entry.dpo_consulted and entry.status not in (DPIAStatus.SCREENING, DPIAStatus.DRAFT):
            findings.append({
                "severity": "Critical",
                "reference": entry.reference,
                "finding": "DPIA approved without DPO consultation (Art. 35(2) breach)",
            })

        # Check review date set for active DPIAs
        active = entry.status in (
            DPIAStatus.APPROVED, DPIAStatus.ACTIVE_MONITORING,
            DPIAStatus.RE_APPROVED,
        )
        if active and not entry.review_date:
            findings.append({
                "severity": "High",
                "reference": entry.reference,
                "finding": "Active DPIA with no review date (Art. 35(11) non-compliance)",
            })

        # Check RoPA linkage
        if not entry.ropa_reference:
            findings.append({
                "severity": "Medium",
                "reference": entry.reference,
                "finding": "DPIA not linked to RoPA entry (Art. 30 cross-reference missing)",
            })

        # Check mitigation plan linkage for high-risk
        if entry.risk_level in (RiskLevel.HIGH, RiskLevel.VERY_HIGH) and not entry.mitigation_plan_ref:
            findings.append({
                "severity": "High",
                "reference": entry.reference,
                "finding": "High/Very High risk DPIA without linked mitigation plan",
            })

        # Check prior consultation for very high residual risk
        if entry.risk_level == RiskLevel.VERY_HIGH:
            if not entry.prior_consultation or not entry.prior_consultation.required:
                findings.append({
                    "severity": "Critical",
                    "reference": entry.reference,
                    "finding": "Very High residual risk without Art. 36 prior consultation assessment",
                })

    return {
        "total_entries": len(register.entries),
        "findings_count": len(findings),
        "critical": sum(1 for f in findings if f["severity"] == "Critical"),
        "high": sum(1 for f in findings if f["severity"] == "High"),
        "medium": sum(1 for f in findings if f["severity"] == "Medium"),
        "findings": findings,
    }


def generate_report(register: DPIARegister, report_date: str) -> str:
    """Generate the DPIA register management report."""
    lines = [
        "=" * 78,
        "DPIA REGISTER MANAGEMENT REPORT",
        "=" * 78,
        f"Organisation:     {register.organisation}",
        f"Register Owner:   {register.register_owner}",
        f"Report Date:      {report_date}",
        f"Total Entries:    {len(register.entries)}",
        "",
    ]

    # Status summary
    status_summary = get_status_summary(register)
    lines.extend(["-" * 78, "STATUS DISTRIBUTION", "-" * 78])
    for status, count in status_summary.items():
        lines.append(f"  {status:<30} {count:>3}")

    # Risk distribution
    risk_dist = get_risk_distribution(register)
    lines.extend(["", "-" * 78, "RISK LEVEL DISTRIBUTION (Active DPIAs)", "-" * 78])
    for level, count in risk_dist.items():
        lines.append(f"  {level:<30} {count:>3}")

    # Overdue reviews
    overdue = find_overdue_reviews(register, report_date)
    lines.extend(["", "-" * 78, "OVERDUE REVIEWS", "-" * 78])
    if overdue:
        for o in overdue:
            lines.append(
                f"  {o['reference']}: {o['processing_activity'][:40]}"
                f"  | Due: {o['review_date']} | {o['days_overdue']} days overdue"
                f"  | Risk: {o['risk_level']}"
            )
    else:
        lines.append("  No overdue reviews.")

    # Prior consultation summary
    consultation = get_prior_consultation_summary(register)
    lines.extend(["", "-" * 78, "ART. 36 PRIOR CONSULTATION SUMMARY", "-" * 78])
    lines.append(f"  Total Required:         {consultation['total_required']}")
    lines.append(f"  Submitted:              {consultation['submitted']}")
    lines.append(f"  Responses Received:     {consultation['responded']}")
    lines.append(f"  Pending Response:       {consultation['pending']}")
    lines.append(f"  Conditions Met:         {consultation['conditions_met']}")
    lines.append(f"  Conditions Outstanding: {consultation['conditions_outstanding']}")

    # Register entries detail
    lines.extend(["", "-" * 78, "REGISTER ENTRIES", "-" * 78])
    for e in register.entries:
        lines.append(f"\n  {e.reference}: {e.processing_activity}")
        lines.append(f"    Department:    {e.department}")
        lines.append(f"    Status:        {e.status.value}")
        lines.append(f"    Risk Level:    {e.risk_level.value}")
        lines.append(f"    Assessed:      {e.assessment_date}")
        lines.append(f"    Next Review:   {e.review_date or 'Not set'}")
        lines.append(f"    RoPA Ref:      {e.ropa_reference}")
        lines.append(f"    DPO Consulted: {'Yes' if e.dpo_consulted else 'No'}")
        if e.prior_consultation and e.prior_consultation.required:
            lines.append(f"    Prior Consult:  Required -- {e.prior_consultation.outcome or 'Pending'}")

    # Register completeness assessment
    completeness = assess_register_completeness(register)
    lines.extend([
        "",
        "-" * 78,
        "REGISTER COMPLETENESS ASSESSMENT",
        "-" * 78,
        f"  Total Findings:  {completeness['findings_count']}",
        f"  Critical:        {completeness['critical']}",
        f"  High:            {completeness['high']}",
        f"  Medium:          {completeness['medium']}",
    ])
    if completeness["findings"]:
        lines.append("\n  Findings:")
        for f in completeness["findings"]:
            lines.append(f"    [{f['severity']:>8}] {f['reference']}: {f['finding']}")

    lines.extend(["", "=" * 78])
    return "\n".join(lines)


if __name__ == "__main__":
    register = DPIARegister(
        organisation="Meridian Financial Services AG",
        register_owner="Dr. Laura Engel, Group DPO",
        created_date="2024-01-15",
        last_updated="2026-03-16",
        entries=[
            DPIAEntry(
                reference="DPIA-RISK-2025-001",
                processing_activity="Customer Credit Scoring Algorithm v3.2",
                department="Risk Analytics",
                controller="Meridian Financial Services AG",
                dpo_consulted=True,
                dpia_lead="Markus Bauer, Head of Privacy Engineering",
                assessment_date="2025-06-15",
                status=DPIAStatus.ACTIVE_MONITORING,
                risk_level=RiskLevel.HIGH,
                ropa_reference="RoPA-RISK-042",
                mitigation_plan_ref="MIT-RISK-2025-001",
                approval_authority="CFO, Dr. Stefan Keller",
                approval_date="2025-07-01",
                review_date="2026-06-15",
                prior_consultation=PriorConsultation(required=False),
            ),
            DPIAEntry(
                reference="DPIA-HR-2025-003",
                processing_activity="Employee Biometric Access Control (Fingerprint)",
                department="Human Resources",
                controller="Meridian Financial Services AG",
                dpo_consulted=True,
                dpia_lead="Anna Schmidt, HR Privacy Lead",
                assessment_date="2025-09-01",
                status=DPIAStatus.ACTIVE_MONITORING,
                risk_level=RiskLevel.MEDIUM,
                ropa_reference="RoPA-HR-018",
                mitigation_plan_ref="MIT-HR-2025-003",
                approval_authority="CHRO, Petra Zimmermann",
                approval_date="2025-09-20",
                review_date="2027-03-01",
            ),
            DPIAEntry(
                reference="DPIA-MKTG-2025-007",
                processing_activity="Real-Time Customer Profiling for Personalised Offers",
                department="Marketing",
                controller="Meridian Financial Services AG",
                dpo_consulted=True,
                dpia_lead="Felix Hartmann, Marketing Privacy Lead",
                assessment_date="2025-04-01",
                status=DPIAStatus.REQUIRES_UPDATE,
                risk_level=RiskLevel.HIGH,
                ropa_reference="RoPA-MKTG-023",
                mitigation_plan_ref="MIT-MKTG-2025-007",
                approval_authority="CMO, Sandra Richter",
                approval_date="2025-04-20",
                review_date="2026-04-01",
                review_trigger=ReviewTrigger.TECHNOLOGY_CHANGE,
                notes="Vendor migrating to new ML platform; requires reassessment of automated decision-making safeguards",
            ),
            DPIAEntry(
                reference="DPIA-COMP-2026-001",
                processing_activity="AML Transaction Monitoring Enhancement (AI-Based)",
                department="Compliance",
                controller="Meridian Financial Services AG",
                dpo_consulted=True,
                dpia_lead="Dr. Thomas Weiss, Compliance Privacy Lead",
                assessment_date="2026-02-15",
                status=DPIAStatus.PRIOR_CONSULTATION,
                risk_level=RiskLevel.VERY_HIGH,
                ropa_reference="RoPA-COMP-031",
                mitigation_plan_ref="MIT-COMP-2026-001",
                approval_authority="CEO, Dr. Michael Braun",
                prior_consultation=PriorConsultation(
                    required=True,
                    submission_date="2026-03-01",
                    sa_reference="BfDI-2026-PC-0847",
                    response_date=None,
                    outcome=None,
                ),
            ),
            DPIAEntry(
                reference="DPIA-OPS-2024-012",
                processing_activity="Customer Call Recording and Sentiment Analysis",
                department="Operations",
                controller="Meridian Financial Services AG",
                dpo_consulted=True,
                dpia_lead="Julia Braun, Operations Privacy Lead",
                assessment_date="2024-11-01",
                status=DPIAStatus.ACTIVE_MONITORING,
                risk_level=RiskLevel.HIGH,
                ropa_reference="RoPA-OPS-015",
                mitigation_plan_ref="MIT-OPS-2024-012",
                approval_authority="COO, Andreas Fischer",
                approval_date="2024-11-20",
                review_date="2025-11-01",
                last_review_date="2025-11-01",
                notes="Reviewed 2025-11-01; no changes to processing; next review set for 2026-11-01",
            ),
            DPIAEntry(
                reference="DPIA-IT-2026-002",
                processing_activity="Cloud Migration of Customer Database to AWS Frankfurt",
                department="IT Infrastructure",
                controller="Meridian Financial Services AG",
                dpo_consulted=False,
                dpia_lead="Robert Klein, Cloud Architect",
                assessment_date="2026-03-10",
                status=DPIAStatus.DRAFT,
                risk_level=RiskLevel.MEDIUM,
                ropa_reference="",
                mitigation_plan_ref="",
                approval_authority="CTO, Dr. Katrin Neumann",
            ),
            DPIAEntry(
                reference="DPIA-LEGACY-2023-001",
                processing_activity="Legacy CRM System (Decommissioned)",
                department="IT",
                controller="Meridian Financial Services AG",
                dpo_consulted=True,
                dpia_lead="Former DPO",
                assessment_date="2023-03-01",
                status=DPIAStatus.ARCHIVED,
                risk_level=RiskLevel.LOW,
                ropa_reference="RoPA-IT-009 (archived)",
                mitigation_plan_ref="MIT-IT-2023-001 (archived)",
                approval_authority="CTO",
                approval_date="2023-03-15",
                archive_date="2025-12-31",
                archive_reason="CRM system decommissioned; all data migrated to new platform",
            ),
        ],
    )

    report = generate_report(register, "2026-03-16")
    print(report)
