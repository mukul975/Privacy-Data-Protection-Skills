#!/usr/bin/env python3
"""
BCR Compliance and Approval Tracker

Tracks BCR application progress, entity compliance status,
audit schedules, and referential gap analysis.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


WP256_REFERENTIAL = {
    "section_1_binding_nature": {
        "label": "Binding Nature of the BCR",
        "elements": [
            "Intra-group agreement executed by all bound entities",
            "Board resolution adopting BCR as corporate policy",
            "Third-party beneficiary clause for data subjects",
            "Acceptance of jurisdiction of EU courts and SAs",
        ],
    },
    "section_2_scope": {
        "label": "Scope of the BCR",
        "elements": [
            "Entity list (Annex A) with legal names and jurisdictions",
            "Transfer scope (Annex B) — data categories, purposes, data subjects",
            "Destination country register",
            "Processing activities covered",
        ],
    },
    "section_3_principles": {
        "label": "Data Protection Principles",
        "elements": [
            "Purpose limitation with compatibility assessment procedure",
            "Data minimisation standards",
            "Storage limitation with retention schedules",
            "Accuracy and data quality procedures",
            "Security measures (Annex C minimum standards)",
            "Lawful basis documentation for each transfer category",
            "Special category data handling procedures",
            "Data protection by design and by default",
        ],
    },
    "section_4_rights": {
        "label": "Data Subject Rights",
        "elements": [
            "Right of access procedure",
            "Right to rectification procedure",
            "Right to erasure procedure",
            "Right to restriction procedure",
            "Right to data portability procedure",
            "Right to object procedure",
            "Automated decision-making safeguards",
        ],
    },
    "section_5_liability": {
        "label": "Liability and Jurisdiction",
        "elements": [
            "BCR Lead identified and accepts liability for non-EU entity breaches",
            "Burden of proof on BCR Lead to demonstrate non-responsibility",
            "Insurance or financial guarantee for BCR claims",
            "Submission to jurisdiction of competent SA",
            "Local law conflict reporting mechanism",
            "Government access transparency and challenge procedures",
        ],
    },
    "section_6_complaints": {
        "label": "Complaint Handling",
        "elements": [
            "Complaint submission mechanism accessible to data subjects",
            "30-day response timeline",
            "Escalation pathway to DPO and then to SA",
            "Alternative dispute resolution mechanism",
            "Right to judicial remedy information",
        ],
    },
    "section_7_compliance": {
        "label": "Training and Audit Programme",
        "elements": [
            "Mandatory onboarding training for data-handling staff",
            "Annual refresher training programme",
            "Role-specific training modules",
            "Internal audit programme with three-year rolling coverage",
            "Annual compliance self-assessments by bound entities",
            "DPO or privacy officer network across bound entities",
            "Audit findings reporting to management and SA",
        ],
    },
    "section_8_updates": {
        "label": "Update and Change Management",
        "elements": [
            "Amendment procedure requiring BCR Lead approval",
            "SA notification for material changes",
            "Communication procedure to all bound entities",
            "Annual entity list review and update",
            "Periodic BCR full review (at least every three years)",
        ],
    },
}

BCR_APPROVAL_PHASES = [
    {
        "phase": 1,
        "name": "Preparation and Drafting",
        "typical_duration_weeks": 16,
        "milestones": [
            "Corporate group mapping completed",
            "Intra-group data flow mapping completed",
            "Gap analysis against referential completed",
            "BCR document drafted",
            "Annexes A, B, C drafted",
            "Intra-group agreement drafted",
            "Internal legal review completed",
            "Board approval obtained",
        ],
    },
    {
        "phase": 2,
        "name": "Lead SA Submission and Review",
        "typical_duration_weeks": 22,
        "milestones": [
            "Standard application form completed",
            "Submission package compiled",
            "Submitted to lead SA",
            "Receipt acknowledged by lead SA",
            "First round of SA questions received",
            "First round responses submitted",
            "Second round of SA questions received (if any)",
            "Second round responses submitted (if any)",
            "Lead SA preliminary positive assessment",
        ],
    },
    {
        "phase": 3,
        "name": "Cooperation Procedure",
        "typical_duration_weeks": 12,
        "milestones": [
            "BCR circulated to concerned SAs",
            "Comment period opened",
            "Comments received from concerned SAs",
            "Comments consolidated by lead SA",
            "Amendments prepared (if needed)",
            "Consensus reached among SAs",
        ],
    },
    {
        "phase": 4,
        "name": "EDPB Consistency and Formal Approval",
        "typical_duration_weeks": 12,
        "milestones": [
            "EDPB referral (if triggered)",
            "EDPB opinion received (if triggered)",
            "Lead SA issues formal approval decision",
            "Conditions implemented (if any)",
            "Final unconditional approval received",
        ],
    },
    {
        "phase": 5,
        "name": "Rollout and Implementation",
        "typical_duration_weeks": 10,
        "milestones": [
            "Intra-group agreement executed by all entities",
            "BCR published on website and EDPB register",
            "Privacy notices updated",
            "Transfer register updated",
            "Training deployed to all bound entities",
            "Audit programme activated",
        ],
    },
]


def conduct_referential_gap_analysis(
    current_compliance: dict,
) -> dict:
    """Assess BCR readiness against the WP256 referential."""
    results = {
        "analysis_date": datetime.utcnow().isoformat(),
        "sections": {},
        "overall_score": 0.0,
        "total_elements": 0,
        "compliant_elements": 0,
        "gaps": [],
    }

    for section_key, section_data in WP256_REFERENTIAL.items():
        section_compliance = current_compliance.get(section_key, {})
        section_elements = section_data["elements"]
        compliant = 0
        section_gaps = []

        for element in section_elements:
            element_status = section_compliance.get(element, False)
            if element_status:
                compliant += 1
            else:
                section_gaps.append(element)
                results["gaps"].append(
                    {
                        "section": section_data["label"],
                        "element": element,
                        "severity": "critical"
                        if section_key in ["section_1_binding_nature", "section_5_liability"]
                        else "major",
                    }
                )

        results["total_elements"] += len(section_elements)
        results["compliant_elements"] += compliant
        results["sections"][section_key] = {
            "label": section_data["label"],
            "total": len(section_elements),
            "compliant": compliant,
            "gaps": section_gaps,
            "completion_pct": round(compliant / len(section_elements) * 100, 1)
            if section_elements
            else 100.0,
        }

    if results["total_elements"] > 0:
        results["overall_score"] = round(
            results["compliant_elements"] / results["total_elements"] * 100, 1
        )

    return results


def create_approval_timeline(
    start_date: str,
    lead_sa: str = "BlnBDI",
) -> dict:
    """Generate a projected BCR approval timeline."""
    start = datetime.strptime(start_date, "%Y-%m-%d")
    timeline = {
        "start_date": start_date,
        "lead_sa": lead_sa,
        "phases": [],
        "projected_completion": None,
    }

    current_start = start
    for phase in BCR_APPROVAL_PHASES:
        phase_end = current_start + timedelta(weeks=phase["typical_duration_weeks"])
        timeline["phases"].append(
            {
                "phase": phase["phase"],
                "name": phase["name"],
                "start_date": current_start.strftime("%Y-%m-%d"),
                "end_date": phase_end.strftime("%Y-%m-%d"),
                "duration_weeks": phase["typical_duration_weeks"],
                "milestones": phase["milestones"],
            }
        )
        current_start = phase_end

    timeline["projected_completion"] = current_start.strftime("%Y-%m-%d")
    total_weeks = sum(p["typical_duration_weeks"] for p in BCR_APPROVAL_PHASES)
    timeline["total_duration_weeks"] = total_weeks
    timeline["total_duration_months"] = round(total_weeks / 4.33, 1)

    return timeline


def track_entity_compliance(entities: list) -> dict:
    """Track BCR compliance status across all bound entities."""
    results = {
        "assessment_date": datetime.utcnow().isoformat(),
        "total_entities": len(entities),
        "compliant": 0,
        "partially_compliant": 0,
        "non_compliant": 0,
        "entities": [],
    }

    for entity in entities:
        compliance_items = [
            entity.get("iga_signed", False),
            entity.get("training_completed", False),
            entity.get("self_assessment_submitted", False),
            entity.get("security_standards_met", False),
            entity.get("complaint_procedure_operational", False),
        ]
        score = sum(1 for item in compliance_items if item)
        total = len(compliance_items)
        pct = round(score / total * 100, 1) if total else 0

        if pct == 100:
            status = "compliant"
            results["compliant"] += 1
        elif pct >= 60:
            status = "partially_compliant"
            results["partially_compliant"] += 1
        else:
            status = "non_compliant"
            results["non_compliant"] += 1

        results["entities"].append(
            {
                "entity_name": entity["name"],
                "jurisdiction": entity["jurisdiction"],
                "compliance_score": pct,
                "status": status,
                "missing_items": [
                    item_name
                    for item_name, item_val in zip(
                        [
                            "IGA signed",
                            "Training completed",
                            "Self-assessment submitted",
                            "Security standards met",
                            "Complaint procedure operational",
                        ],
                        compliance_items,
                    )
                    if not item_val
                ],
            }
        )

    results["group_compliance_rate"] = round(
        results["compliant"] / results["total_entities"] * 100, 1
    ) if results["total_entities"] else 0

    return results


def generate_audit_plan(
    entities: list, cycle_years: int = 3, start_date: Optional[str] = None
) -> dict:
    """Generate a rolling BCR audit plan covering all entities within the cycle period."""
    if start_date:
        start = datetime.strptime(start_date, "%Y-%m-%d")
    else:
        start = datetime.utcnow()

    total_entities = len(entities)
    audits_per_year = -(-total_entities // cycle_years)  # ceiling division

    plan = {
        "cycle_years": cycle_years,
        "total_entities": total_entities,
        "audits_per_year": audits_per_year,
        "schedule": [],
    }

    for i, entity in enumerate(entities):
        year_slot = i // audits_per_year
        position_in_year = i % audits_per_year
        audit_date = start + timedelta(days=365 * year_slot + 30 * position_in_year)
        plan["schedule"].append(
            {
                "entity_name": entity["name"],
                "jurisdiction": entity["jurisdiction"],
                "planned_audit_date": audit_date.strftime("%Y-%m-%d"),
                "audit_year": year_slot + 1,
                "audit_type": "full" if year_slot == 0 else "follow-up",
            }
        )

    return plan


if __name__ == "__main__":
    print("=== BCR Approval Timeline ===")
    timeline = create_approval_timeline("2025-04-01", "BlnBDI")
    print(json.dumps(timeline, indent=2))

    print("\n=== Referential Gap Analysis (Sample) ===")
    sample_compliance = {
        "section_1_binding_nature": {
            "Intra-group agreement executed by all bound entities": True,
            "Board resolution adopting BCR as corporate policy": True,
            "Third-party beneficiary clause for data subjects": False,
            "Acceptance of jurisdiction of EU courts and SAs": True,
        },
        "section_2_scope": {
            "Entity list (Annex A) with legal names and jurisdictions": True,
            "Transfer scope (Annex B) — data categories, purposes, data subjects": True,
            "Destination country register": True,
            "Processing activities covered": False,
        },
    }
    gap_result = conduct_referential_gap_analysis(sample_compliance)
    print(json.dumps(gap_result, indent=2))

    print("\n=== Entity Compliance Tracking ===")
    sample_entities = [
        {
            "name": "Athena Global Logistics GmbH",
            "jurisdiction": "Germany",
            "iga_signed": True,
            "training_completed": True,
            "self_assessment_submitted": True,
            "security_standards_met": True,
            "complaint_procedure_operational": True,
        },
        {
            "name": "Athena Logistics (Hong Kong) Ltd",
            "jurisdiction": "Hong Kong SAR",
            "iga_signed": True,
            "training_completed": True,
            "self_assessment_submitted": False,
            "security_standards_met": True,
            "complaint_procedure_operational": True,
        },
        {
            "name": "Athena Freight Services India Pvt Ltd",
            "jurisdiction": "India",
            "iga_signed": True,
            "training_completed": False,
            "self_assessment_submitted": False,
            "security_standards_met": False,
            "complaint_procedure_operational": False,
        },
    ]
    entity_result = track_entity_compliance(sample_entities)
    print(json.dumps(entity_result, indent=2))
