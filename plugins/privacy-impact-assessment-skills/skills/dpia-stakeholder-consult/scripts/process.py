#!/usr/bin/env python3
"""DPIA Stakeholder Consultation Management Tool.

Manages the stakeholder consultation process for Data Protection Impact
Assessments under GDPR Art. 35(9). Tracks consultation planning, execution,
response analysis, and integration into DPIA outcomes.
"""

import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class ConsultationStatus(Enum):
    PLANNED = "Planned"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    NOT_REQUIRED = "Not Required (Justified)"


class StakeholderType(Enum):
    DATA_SUBJECT = "Data Subject"
    REPRESENTATIVE_BODY = "Representative Body"
    DPO = "Data Protection Officer"
    PROCESSOR = "Processor Representative"
    INTERNAL = "Internal Stakeholder"
    WORKS_COUNCIL = "Works Council"
    PATIENT_GROUP = "Patient Advisory Group"


class ConsultationMethod(Enum):
    FOCUS_GROUP = "Focus Group"
    ONLINE_SURVEY = "Online Survey"
    WRITTEN_CONSULTATION = "Written Consultation"
    PUBLIC_MEETING = "Public Meeting"
    ADVISORY_PANEL = "Advisory Panel"
    USER_TESTING = "User Testing with Privacy Lens"
    REPRESENTATIVE_MEETING = "Representative Body Meeting"


class FeedbackOutcome(Enum):
    ADOPTED = "Adopted -- DPIA updated"
    PARTIALLY_ADOPTED = "Partially adopted with modifications"
    NOTED = "Noted -- no change required"
    NOT_ADOPTED = "Not adopted -- justification recorded"


@dataclass
class Stakeholder:
    name: str
    stakeholder_type: StakeholderType
    contact_method: str
    consultation_method: ConsultationMethod
    invited: bool = True
    responded: bool = False


@dataclass
class ConsultationResponse:
    stakeholder_name: str
    stakeholder_type: str
    date_received: str
    theme: str
    concern_summary: str
    risk_alignment: str  # Which DPIA risk this relates to, or "New Risk"
    outcome: FeedbackOutcome
    action_taken: str


@dataclass
class ConsultationPlan:
    dpia_reference: str
    processing_activity: str
    controller: str
    consultation_required: bool
    justification_if_not_required: str = ""
    start_date: str = ""
    end_date: str = ""
    status: ConsultationStatus = ConsultationStatus.PLANNED
    stakeholders: list = field(default_factory=list)
    responses: list = field(default_factory=list)
    dpo_advice_received: bool = False
    dpo_advice_date: str = ""
    dpo_advice_summary: str = ""


def assess_consultation_completeness(plan: ConsultationPlan) -> dict:
    """Evaluate whether the consultation process meets Art. 35(9) requirements."""
    findings = []
    score = 0
    max_score = 100

    # DPO involvement (Art. 35(2)) -- mandatory
    if plan.dpo_advice_received:
        score += 25
    else:
        findings.append({
            "severity": "Critical",
            "finding": "DPO advice not received -- Art. 35(2) requires DPO involvement",
        })

    # Data subject consultation assessed
    if not plan.consultation_required:
        if plan.justification_if_not_required:
            score += 20
            findings.append({
                "severity": "Info",
                "finding": f"Data subject consultation not conducted -- justified: {plan.justification_if_not_required}",
            })
        else:
            findings.append({
                "severity": "High",
                "finding": "Data subject consultation not conducted and no justification recorded",
            })
    else:
        # Check stakeholder diversity
        stakeholder_types = set(s.stakeholder_type for s in plan.stakeholders)
        if StakeholderType.DATA_SUBJECT in stakeholder_types or StakeholderType.REPRESENTATIVE_BODY in stakeholder_types:
            score += 20
        else:
            findings.append({
                "severity": "High",
                "finding": "No data subjects or representative bodies included in consultation",
            })

        # Check response rate
        invited = sum(1 for s in plan.stakeholders if s.invited)
        responded = sum(1 for s in plan.stakeholders if s.responded)
        response_rate = (responded / invited * 100) if invited > 0 else 0

        if response_rate >= 50:
            score += 15
        elif response_rate >= 25:
            score += 10
            findings.append({
                "severity": "Medium",
                "finding": f"Low response rate ({response_rate:.0f}%) -- consider additional outreach",
            })
        else:
            findings.append({
                "severity": "High",
                "finding": f"Very low response rate ({response_rate:.0f}%) -- consultation representativeness questionable",
            })

        # Check feedback integration
        if plan.responses:
            adopted = sum(1 for r in plan.responses if r.outcome in (FeedbackOutcome.ADOPTED, FeedbackOutcome.PARTIALLY_ADOPTED))
            not_adopted = sum(1 for r in plan.responses if r.outcome == FeedbackOutcome.NOT_ADOPTED)

            score += 15
            if not_adopted > 0:
                all_justified = all(
                    r.action_taken for r in plan.responses
                    if r.outcome == FeedbackOutcome.NOT_ADOPTED
                )
                if all_justified:
                    score += 10
                else:
                    findings.append({
                        "severity": "Medium",
                        "finding": "Some non-adopted feedback lacks documented justification",
                    })
            else:
                score += 10

            # Feedback loop closure
            score += 15
        else:
            findings.append({
                "severity": "Medium",
                "finding": "No consultation responses recorded",
            })

    return {
        "completeness_score": min(score, max_score),
        "max_score": max_score,
        "findings": findings,
        "art_35_2_compliant": plan.dpo_advice_received,
        "art_35_9_compliant": (
            not plan.consultation_required and bool(plan.justification_if_not_required)
        ) or (plan.consultation_required and len(plan.responses) > 0),
    }


def generate_report(plan: ConsultationPlan) -> str:
    """Generate a consultation process report."""
    lines = [
        "=" * 70,
        "DPIA STAKEHOLDER CONSULTATION REPORT",
        "=" * 70,
        f"DPIA Reference:      {plan.dpia_reference}",
        f"Processing Activity: {plan.processing_activity}",
        f"Controller:          {plan.controller}",
        f"Consultation Status: {plan.status.value}",
        f"Period:              {plan.start_date} to {plan.end_date}",
        "",
    ]

    # DPO Advice
    lines.extend([
        "-" * 70,
        "DPO ADVICE (Art. 35(2))",
        "-" * 70,
        f"  Received: {'Yes' if plan.dpo_advice_received else 'NO -- NON-COMPLIANT'}",
        f"  Date:     {plan.dpo_advice_date}",
        f"  Summary:  {plan.dpo_advice_summary}",
        "",
    ])

    # Stakeholder map
    lines.extend([
        "-" * 70,
        "STAKEHOLDER MAP",
        "-" * 70,
    ])

    for s in plan.stakeholders:
        status = "Responded" if s.responded else ("Invited" if s.invited else "Identified")
        lines.append(
            f"  [{status:>10}] {s.name} ({s.stakeholder_type.value}) "
            f"-- {s.consultation_method.value}"
        )

    invited = sum(1 for s in plan.stakeholders if s.invited)
    responded = sum(1 for s in plan.stakeholders if s.responded)
    rate = (responded / invited * 100) if invited > 0 else 0
    lines.append(f"\n  Response Rate: {responded}/{invited} ({rate:.0f}%)")
    lines.append("")

    # Responses
    if plan.responses:
        lines.extend([
            "-" * 70,
            "CONSULTATION RESPONSES AND OUTCOMES",
            "-" * 70,
        ])

        for i, r in enumerate(plan.responses, 1):
            lines.append(f"\n  Response #{i}")
            lines.append(f"  From:           {r.stakeholder_name} ({r.stakeholder_type})")
            lines.append(f"  Date:           {r.date_received}")
            lines.append(f"  Theme:          {r.theme}")
            lines.append(f"  Concern:        {r.concern_summary}")
            lines.append(f"  Risk Alignment: {r.risk_alignment}")
            lines.append(f"  Outcome:        {r.outcome.value}")
            lines.append(f"  Action:         {r.action_taken}")

    # Completeness assessment
    assessment = assess_consultation_completeness(plan)
    lines.extend([
        "",
        "-" * 70,
        "CONSULTATION COMPLETENESS ASSESSMENT",
        "-" * 70,
        f"  Score: {assessment['completeness_score']}/{assessment['max_score']}",
        f"  Art. 35(2) Compliant (DPO): {'Yes' if assessment['art_35_2_compliant'] else 'NO'}",
        f"  Art. 35(9) Compliant (Consultation): {'Yes' if assessment['art_35_9_compliant'] else 'NO'}",
        "",
    ])

    if assessment["findings"]:
        lines.append("  Findings:")
        for f in assessment["findings"]:
            lines.append(f"    [{f['severity']:>8}] {f['finding']}")

    lines.extend(["", "=" * 70])
    return "\n".join(lines)


if __name__ == "__main__":
    plan = ConsultationPlan(
        dpia_reference="DPIA-QLH-2026-012",
        processing_activity="Patient Genomic Profiling Platform",
        controller="QuantumLeap Health Technologies",
        consultation_required=True,
        start_date="2026-04-01",
        end_date="2026-05-01",
        status=ConsultationStatus.COMPLETED,
        dpo_advice_received=True,
        dpo_advice_date="2026-03-20",
        dpo_advice_summary="DPO recommends patient focus groups and ethics committee review. Genomic data processing requires enhanced transparency measures. Prior consultation with BfDI likely needed given residual risk profile.",
    )

    plan.stakeholders = [
        Stakeholder("Patient Advisory Council (Charite Berlin)", StakeholderType.PATIENT_GROUP, "email", ConsultationMethod.FOCUS_GROUP, True, True),
        Stakeholder("Deutsche Gesellschaft fuer Humangenetik", StakeholderType.REPRESENTATIVE_BODY, "written", ConsultationMethod.WRITTEN_CONSULTATION, True, True),
        Stakeholder("Verbraucherzentrale Bundesverband", StakeholderType.REPRESENTATIVE_BODY, "written", ConsultationMethod.WRITTEN_CONSULTATION, True, True),
        Stakeholder("Patient Sample Group (n=200)", StakeholderType.DATA_SUBJECT, "online", ConsultationMethod.ONLINE_SURVEY, True, True),
        Stakeholder("Hospital IT Directors Group", StakeholderType.INTERNAL, "meeting", ConsultationMethod.ADVISORY_PANEL, True, True),
        Stakeholder("CloudGenomics GmbH (Processor)", StakeholderType.PROCESSOR, "meeting", ConsultationMethod.REPRESENTATIVE_MEETING, True, True),
        Stakeholder("Betriebsrat QuantumLeap", StakeholderType.WORKS_COUNCIL, "meeting", ConsultationMethod.REPRESENTATIVE_MEETING, True, True),
        Stakeholder("Ethics Committee Charite", StakeholderType.REPRESENTATIVE_BODY, "written", ConsultationMethod.WRITTEN_CONSULTATION, True, False),
    ]

    plan.responses = [
        ConsultationResponse(
            "Patient Advisory Council", "Patient Advisory Group", "2026-04-10",
            "Transparency", "Patients want clear explanation of how genomic data influences treatment decisions and who can access their genetic information",
            "R1 (Confidentiality)", FeedbackOutcome.ADOPTED,
            "Enhanced patient information leaflet with genomic data flow diagram; added granular consent options for data sharing with insurance partners"
        ),
        ConsultationResponse(
            "Deutsche Gesellschaft fuer Humangenetik", "Representative Body", "2026-04-15",
            "Genetic discrimination", "Concern about insurance partners using genomic risk scores for underwriting decisions in violation of Gendiagnostikgesetz",
            "R3 (Purpose limitation)", FeedbackOutcome.ADOPTED,
            "Added technical control: only aggregated risk categories (not individual scores) shared with insurance; contractual clause explicitly prohibiting underwriting use"
        ),
        ConsultationResponse(
            "Patient Survey (n=200)", "Data Subject", "2026-04-28",
            "Data retention", "67% of respondents want ability to request deletion of genomic data after treatment completion; 23% want indefinite retention for future research",
            "New Risk", FeedbackOutcome.PARTIALLY_ADOPTED,
            "Implemented tiered retention: active treatment data retained for treatment duration + 10 years (clinical records requirement); research use requires separate explicit consent with deletion option"
        ),
        ConsultationResponse(
            "Verbraucherzentrale", "Representative Body", "2026-04-20",
            "Algorithmic transparency", "Request for public documentation of AI model decision criteria and bias testing results",
            "R2 (Discrimination)", FeedbackOutcome.PARTIALLY_ADOPTED,
            "Model cards published for each algorithm; bias audit summaries made available; full model architecture details withheld as trade secret per Art. 35(9) commercial interests exception"
        ),
        ConsultationResponse(
            "Betriebsrat QuantumLeap", "Works Council", "2026-04-12",
            "Employee data", "Concern that platform usage logs could be used for employee performance monitoring",
            "New Risk", FeedbackOutcome.ADOPTED,
            "Added BetrVG-compliant supplementary agreement; platform usage logs excluded from HR performance reviews; access to employee-identifiable logs restricted to DPO and IT security only"
        ),
    ]

    report = generate_report(plan)
    print(report)
