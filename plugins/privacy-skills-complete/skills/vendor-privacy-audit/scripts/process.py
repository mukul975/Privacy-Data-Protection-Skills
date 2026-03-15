#!/usr/bin/env python3
"""
Vendor Privacy Audit — Audit Management and Finding Tracking Engine

Implements audit planning, checklist execution, finding classification,
remediation tracking, and audit report generation per GDPR Article 28(3)(h).
"""

import json
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class AuditType(Enum):
    DOCUMENTATION = "documentation_review"
    REMOTE = "remote_technical"
    ON_SITE = "on_site_inspection"


class AuditTrigger(Enum):
    SCHEDULED = "annual_schedule"
    BREACH = "vendor_breach"
    COMPLAINT = "data_subject_complaint"
    CERT_LAPSE = "certification_lapse"
    SUB_PROCESSOR = "sub_processor_concern"
    REGULATORY = "regulatory_inquiry"


class AuditStatus(Enum):
    PLANNED = "planned"
    NOTIFIED = "notified"
    IN_PROGRESS = "in_progress"
    DRAFT_REPORT = "draft_report"
    FINAL_REPORT = "final_report"
    REMEDIATION = "remediation_tracking"
    CLOSED = "closed"


class FindingSeverity(Enum):
    CRITICAL = "critical"
    MAJOR = "major"
    MINOR = "minor"
    OBSERVATION = "observation"


class FindingStatus(Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    REMEDIATED = "remediated"
    VERIFIED = "verified"
    OVERDUE = "overdue"
    ESCALATED = "escalated"


REMEDIATION_DAYS = {
    FindingSeverity.CRITICAL: 7,
    FindingSeverity.MAJOR: 30,
    FindingSeverity.MINOR: 90,
    FindingSeverity.OBSERVATION: 365,
}

AUDIT_CHECKLIST = {
    "A": {
        "name": "DPA Compliance",
        "items": [
            {"id": "A1", "description": "Processing limited to documented controller instructions", "article": "28(3)(a)"},
            {"id": "A2", "description": "All authorized personnel bound by confidentiality", "article": "28(3)(b)"},
            {"id": "A3", "description": "Article 32 security measures implemented per DPA", "article": "28(3)(c)"},
            {"id": "A4", "description": "Sub-processors authorized and DPAs in place", "article": "28(3)(d)"},
            {"id": "A5", "description": "DSR assistance capability demonstrated", "article": "28(3)(e)"},
            {"id": "A6", "description": "Compliance assistance for Art. 32-36", "article": "28(3)(f)"},
            {"id": "A7", "description": "Deletion/return capabilities verified", "article": "28(3)(g)"},
            {"id": "A8", "description": "Audit information and access provided", "article": "28(3)(h)"},
        ],
    },
    "B": {
        "name": "Technical Controls",
        "items": [
            {"id": "B1", "description": "Encryption at rest per DPA specifications", "article": "Art. 32"},
            {"id": "B2", "description": "Encryption in transit per DPA specifications", "article": "Art. 32"},
            {"id": "B3", "description": "Access controls — principle of least privilege", "article": "Art. 32"},
            {"id": "B4", "description": "MFA for administrative access", "article": "Art. 32"},
            {"id": "B5", "description": "Logging enabled and retained per schedule", "article": "Art. 32"},
            {"id": "B6", "description": "Vulnerability scanning per schedule", "article": "Art. 32"},
            {"id": "B7", "description": "Penetration testing per schedule", "article": "Art. 32"},
            {"id": "B8", "description": "Backup and recovery tested", "article": "Art. 32"},
        ],
    },
    "C": {
        "name": "Organizational Controls",
        "items": [
            {"id": "C1", "description": "Privacy training delivered to all staff", "article": "Art. 32/39"},
            {"id": "C2", "description": "Incident response plan documented and tested", "article": "Art. 33"},
            {"id": "C3", "description": "Change management process followed", "article": "Art. 32"},
            {"id": "C4", "description": "Data retention and deletion operational", "article": "Art. 5(1)(e)"},
            {"id": "C5", "description": "Records of processing maintained", "article": "Art. 30(2)"},
        ],
    },
    "D": {
        "name": "Breach Notification Readiness",
        "items": [
            {"id": "D1", "description": "Breach detection capabilities operational", "article": "Art. 33"},
            {"id": "D2", "description": "Notification procedure with DPA-compliant timeframe", "article": "Art. 33(2)"},
            {"id": "D3", "description": "Notification contact details current", "article": "Art. 33(2)"},
            {"id": "D4", "description": "Breach register maintained", "article": "Art. 33(5)"},
        ],
    },
}


@dataclass
class ChecklistResult:
    """Result for a single audit checklist item."""
    item_id: str = ""
    description: str = ""
    article: str = ""
    status: str = "not_assessed"  # compliant, non_compliant, partially_compliant, not_applicable
    evidence: str = ""
    notes: str = ""


@dataclass
class AuditFinding:
    """An audit finding requiring remediation."""
    finding_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    audit_id: str = ""
    vendor_name: str = ""
    checklist_item: str = ""
    severity: str = FindingSeverity.MINOR.value
    description: str = ""
    root_cause: str = ""
    recommendation: str = ""
    remediation_plan: str = ""
    deadline: str = ""
    evidence_required: str = ""
    status: str = FindingStatus.OPEN.value
    status_history: list[dict] = field(default_factory=list)
    verified_date: Optional[str] = None
    verified_by: str = ""


@dataclass
class VendorAudit:
    """A complete vendor privacy audit record."""
    audit_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_id: str = ""
    vendor_name: str = ""
    audit_type: str = AuditType.DOCUMENTATION.value
    trigger: str = AuditTrigger.SCHEDULED.value
    status: str = AuditStatus.PLANNED.value
    audit_team_lead: str = ""
    audit_team_members: list[str] = field(default_factory=list)
    planned_date: str = ""
    notification_date: Optional[str] = None
    execution_dates: list[str] = field(default_factory=list)
    checklist_results: list[dict] = field(default_factory=list)
    findings: list[str] = field(default_factory=list)  # finding IDs
    overall_assessment: str = ""
    report_date: Optional[str] = None
    previous_audit_id: Optional[str] = None
    notes: list[str] = field(default_factory=list)


class VendorAuditEngine:
    """
    Manages the vendor privacy audit lifecycle including planning,
    execution, finding tracking, and remediation verification.
    """

    def __init__(self):
        self.audits: dict[str, VendorAudit] = {}
        self.findings: dict[str, AuditFinding] = {}

    def plan_audit(
        self,
        vendor_id: str,
        vendor_name: str,
        audit_type: AuditType,
        trigger: AuditTrigger,
        planned_date: str,
        team_lead: str,
        team_members: list[str] = None,
    ) -> VendorAudit:
        """Create a new audit plan."""
        audit = VendorAudit(
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            audit_type=audit_type.value,
            trigger=trigger.value,
            planned_date=planned_date,
            audit_team_lead=team_lead,
            audit_team_members=team_members or [],
        )
        self.audits[audit.audit_id] = audit
        return audit

    def notify_vendor(self, audit_id: str) -> str:
        """Record vendor notification of upcoming audit."""
        audit = self.audits.get(audit_id)
        if not audit:
            raise ValueError(f"Audit {audit_id} not found")
        audit.notification_date = datetime.now(timezone.utc).isoformat()
        audit.status = AuditStatus.NOTIFIED.value
        return audit.notification_date

    def start_audit(self, audit_id: str) -> str:
        """Mark audit as in progress."""
        audit = self.audits.get(audit_id)
        if not audit:
            raise ValueError(f"Audit {audit_id} not found")
        audit.status = AuditStatus.IN_PROGRESS.value
        audit.execution_dates.append(datetime.now(timezone.utc).isoformat())
        return audit.status

    def record_checklist_result(
        self, audit_id: str, result: ChecklistResult
    ) -> None:
        """Record the result of a single checklist item assessment."""
        audit = self.audits.get(audit_id)
        if not audit:
            raise ValueError(f"Audit {audit_id} not found")
        audit.checklist_results.append(asdict(result))

    def create_finding(
        self,
        audit_id: str,
        checklist_item: str,
        severity: FindingSeverity,
        description: str,
        root_cause: str = "",
        recommendation: str = "",
        evidence_required: str = "",
    ) -> AuditFinding:
        """Create an audit finding linked to a checklist item."""
        audit = self.audits.get(audit_id)
        if not audit:
            raise ValueError(f"Audit {audit_id} not found")

        deadline = (
            datetime.now(timezone.utc) + timedelta(days=REMEDIATION_DAYS[severity])
        ).isoformat()

        finding = AuditFinding(
            audit_id=audit_id,
            vendor_name=audit.vendor_name,
            checklist_item=checklist_item,
            severity=severity.value,
            description=description,
            root_cause=root_cause,
            recommendation=recommendation,
            deadline=deadline,
            evidence_required=evidence_required,
        )
        finding.status_history.append({
            "status": FindingStatus.OPEN.value,
            "date": datetime.now(timezone.utc).isoformat(),
            "note": "Finding created during audit",
        })

        self.findings[finding.finding_id] = finding
        audit.findings.append(finding.finding_id)
        return finding

    def update_finding_status(
        self, finding_id: str, new_status: FindingStatus, note: str = "",
        verified_by: str = ""
    ) -> str:
        """Update the status of an audit finding."""
        finding = self.findings.get(finding_id)
        if not finding:
            raise ValueError(f"Finding {finding_id} not found")

        finding.status = new_status.value
        finding.status_history.append({
            "status": new_status.value,
            "date": datetime.now(timezone.utc).isoformat(),
            "note": note,
        })

        if new_status == FindingStatus.VERIFIED:
            finding.verified_date = datetime.now(timezone.utc).isoformat()
            finding.verified_by = verified_by

        return finding.status

    def generate_audit_report(self, audit_id: str) -> dict:
        """Generate the audit report summary."""
        audit = self.audits.get(audit_id)
        if not audit:
            raise ValueError(f"Audit {audit_id} not found")

        audit_findings = [
            self.findings[fid] for fid in audit.findings if fid in self.findings
        ]

        severity_dist = {s.value: 0 for s in FindingSeverity}
        for f in audit_findings:
            severity_dist[f.severity] += 1

        total_checks = len(audit.checklist_results)
        compliant = len([r for r in audit.checklist_results if r["status"] == "compliant"])
        compliance_rate = round(compliant / total_checks * 100, 1) if total_checks > 0 else 0

        if severity_dist["critical"] > 0:
            overall = "Non-Compliant — Critical findings require immediate remediation"
        elif severity_dist["major"] > 0:
            overall = "Partially Compliant — Major findings require remediation within 30 days"
        elif severity_dist["minor"] > 0:
            overall = "Substantially Compliant — Minor findings noted"
        else:
            overall = "Compliant — No significant findings"

        audit.overall_assessment = overall
        audit.report_date = datetime.now(timezone.utc).isoformat()
        audit.status = AuditStatus.FINAL_REPORT.value

        return {
            "audit_id": audit.audit_id,
            "vendor_name": audit.vendor_name,
            "audit_type": audit.audit_type,
            "trigger": audit.trigger,
            "audit_team_lead": audit.audit_team_lead,
            "execution_dates": audit.execution_dates,
            "checklist_items_assessed": total_checks,
            "compliance_rate": f"{compliance_rate}%",
            "total_findings": len(audit_findings),
            "severity_distribution": severity_dist,
            "overall_assessment": overall,
            "findings_detail": [
                {
                    "finding_id": f.finding_id,
                    "severity": f.severity,
                    "checklist_item": f.checklist_item,
                    "description": f.description,
                    "deadline": f.deadline,
                    "status": f.status,
                }
                for f in audit_findings
            ],
            "report_date": audit.report_date,
        }

    def get_overdue_findings(self) -> list[dict]:
        """Return all findings past their remediation deadline."""
        now = datetime.now(timezone.utc).isoformat()
        overdue = []
        for finding in self.findings.values():
            if (
                finding.status in [FindingStatus.OPEN.value, FindingStatus.IN_PROGRESS.value]
                and finding.deadline < now
            ):
                finding.status = FindingStatus.OVERDUE.value
                overdue.append({
                    "finding_id": finding.finding_id,
                    "vendor_name": finding.vendor_name,
                    "severity": finding.severity,
                    "description": finding.description,
                    "deadline": finding.deadline,
                    "days_overdue": (
                        datetime.now(timezone.utc)
                        - datetime.fromisoformat(finding.deadline.replace("Z", "+00:00"))
                    ).days,
                })
        return overdue


if __name__ == "__main__":
    engine = VendorAuditEngine()

    # Plan an annual audit for NimbusAnalytics
    audit = engine.plan_audit(
        vendor_id="nimbus-001",
        vendor_name="NimbusAnalytics GmbH",
        audit_type=AuditType.REMOTE,
        trigger=AuditTrigger.SCHEDULED,
        planned_date="2026-04-15",
        team_lead="Sarah Chen, Privacy Analyst",
        team_members=["James Park, InfoSec Analyst", "Lisa Muller, Privacy Specialist"],
    )
    print(f"Audit planned: {audit.audit_id}")

    # Notify vendor and start audit
    engine.notify_vendor(audit.audit_id)
    engine.start_audit(audit.audit_id)

    # Record checklist results
    results = [
        ChecklistResult("A1", "Processing limited to documented instructions", "28(3)(a)",
                        "compliant", "Instruction register reviewed — all processing within scope", ""),
        ChecklistResult("A2", "Personnel bound by confidentiality", "28(3)(b)",
                        "compliant", "100% of staff have signed NDAs; annual renewal tracked", ""),
        ChecklistResult("A3", "Art. 32 security measures implemented", "28(3)(c)",
                        "compliant", "AES-256-GCM at rest, TLS 1.3 in transit verified", ""),
        ChecklistResult("A4", "Sub-processors authorized and DPAs in place", "28(3)(d)",
                        "partially_compliant", "2 of 2 sub-processors have DPAs; one DPA missing updated annex", ""),
        ChecklistResult("B1", "Encryption at rest per DPA", "Art. 32",
                        "compliant", "AES-256-GCM via AWS KMS confirmed via console screenshot", ""),
        ChecklistResult("B3", "Access controls — least privilege", "Art. 32",
                        "non_compliant", "3 developer accounts have unnecessary production database access", ""),
        ChecklistResult("B4", "MFA for administrative access", "Art. 32",
                        "compliant", "MFA enforced for all admin accounts — enrollment at 100%", ""),
        ChecklistResult("C1", "Privacy training delivered", "Art. 32/39",
                        "partially_compliant", "Training completion at 88% — 12% of new hires pending", ""),
        ChecklistResult("D2", "Breach notification procedure with DPA timeframe", "Art. 33(2)",
                        "compliant", "IRP specifies 24-hour notification — matches DPA requirement", ""),
    ]
    for r in results:
        engine.record_checklist_result(audit.audit_id, r)

    # Create findings for non-compliant and partially-compliant items
    finding1 = engine.create_finding(
        audit.audit_id,
        checklist_item="B3",
        severity=FindingSeverity.MAJOR,
        description="Three developer accounts retain production database read access that is not required for their current role assignments.",
        root_cause="Quarterly access review did not include developer role-to-access mapping validation.",
        recommendation="Immediately revoke unnecessary production access. Enhance quarterly access review to include role-based access validation.",
        evidence_required="Updated access control list showing revoked access; revised access review procedure document.",
    )

    finding2 = engine.create_finding(
        audit.audit_id,
        checklist_item="A4",
        severity=FindingSeverity.MINOR,
        description="Sub-processor DPA for Elastic Cloud B.V. references outdated Annex I (data categories from 2025 version, not reflecting 2026 processing changes).",
        root_cause="DPA amendment process not triggered after processing scope change in January 2026.",
        recommendation="Execute DPA amendment to update Annex I with current data categories.",
        evidence_required="Executed DPA amendment with updated Annex I.",
    )

    finding3 = engine.create_finding(
        audit.audit_id,
        checklist_item="C1",
        severity=FindingSeverity.MINOR,
        description="Privacy training completion at 88% — 12% of personnel hired in Q1 2026 have not completed mandatory training.",
        root_cause="Onboarding process allows 60-day training window; some hires are within this window.",
        recommendation="Verify all pending completions are within 60-day onboarding window. Consider reducing training deadline to 30 days.",
        evidence_required="Training completion records showing 100% coverage or documented onboarding timeline.",
    )

    # Generate audit report
    report = engine.generate_audit_report(audit.audit_id)
    print("\n=== Vendor Privacy Audit Report ===")
    print(json.dumps(report, indent=2))
