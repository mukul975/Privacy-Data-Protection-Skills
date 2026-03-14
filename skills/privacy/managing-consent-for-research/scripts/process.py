#!/usr/bin/env python3
"""
Research Consent Management System

Manages broad consent for scientific research per GDPR Article 89
and Recital 33, including ethics review tracking, purpose evolution
assessment, and safeguard compliance verification.
"""

import json
import uuid
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class ResearchScopeAssessment(Enum):
    WITHIN_SCOPE = "within_broad_consent_scope"
    OUTSIDE_SCOPE = "outside_scope_new_consent_required"
    BORDERLINE = "borderline_ethics_committee_decision"


class EthicsDecision(Enum):
    APPROVED = "approved"
    APPROVED_WITH_CONDITIONS = "approved_with_conditions"
    REJECTED = "rejected"
    PENDING = "pending_review"


@dataclass
class ResearchProject:
    """A scientific research project using user data."""
    project_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    principal_investigator: str = ""
    research_area: str = ""
    description: str = ""
    data_categories_needed: list[str] = field(default_factory=list)
    safeguards: list[str] = field(default_factory=list)
    ethics_reference: str = ""
    ethics_decision: str = EthicsDecision.PENDING.value
    ethics_conditions: Optional[str] = None
    dpo_approved: bool = False
    dpia_completed: bool = False
    scope_assessment: str = ""
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    status: str = "proposed"  # proposed, active, completed, suspended
    subjects_count: int = 0
    publications: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


# Broad consent research areas defined for CloudVault SaaS Inc.
BROAD_CONSENT_AREAS = {
    "cloud_storage_optimization": {
        "description": "Research into cloud storage efficiency, compression, deduplication, and access pattern optimization",
        "data_categories": ["file_metadata", "storage_patterns", "access_frequency", "storage_tier"],
        "ethics_committee": "CloudVault Research Ethics Committee (CREC)",
    },
    "file_system_design": {
        "description": "Research into file system architecture, indexing, and retrieval mechanisms for cloud environments",
        "data_categories": ["file_metadata", "directory_structure", "access_patterns"],
        "ethics_committee": "CloudVault Research Ethics Committee (CREC)",
    },
    "data_management_behaviors": {
        "description": "Research into how users organize, share, and manage files in cloud storage systems",
        "data_categories": ["usage_patterns", "sharing_behaviors", "collaboration_metrics"],
        "ethics_committee": "CloudVault Research Ethics Committee (CREC)",
    },
}

# Article 89(1) required safeguards
REQUIRED_SAFEGUARDS = [
    "pseudonymization",
    "data_minimization",
    "access_controls",
    "retention_limitation",
    "no_re_identification",
    "audit_trail",
]


def assess_research_scope(project: ResearchProject) -> dict:
    """
    Assess whether a research project falls within the broad consent scope.

    Per Recital 33, broad consent covers "certain areas of scientific research
    when in keeping with recognised ethical standards."

    Returns:
        Assessment result with determination and reasoning.
    """
    matching_areas = []
    data_covered = True

    for area_id, area in BROAD_CONSENT_AREAS.items():
        # Check if the project's research area overlaps
        project_area_lower = project.research_area.lower()
        area_desc_lower = area["description"].lower()

        overlap_keywords = set(project_area_lower.split()) & set(area_desc_lower.split())
        if len(overlap_keywords) >= 3:
            matching_areas.append(area_id)

        # Check if needed data categories are within consented categories
        for cat in project.data_categories_needed:
            if cat not in area["data_categories"]:
                # Check if it's in ANY broad consent area
                all_cats = set()
                for a in BROAD_CONSENT_AREAS.values():
                    all_cats.update(a["data_categories"])
                if cat not in all_cats:
                    data_covered = False

    if matching_areas and data_covered:
        assessment = ResearchScopeAssessment.WITHIN_SCOPE.value
        reasoning = f"Project falls within broad consent area(s): {', '.join(matching_areas)}. All required data categories are covered."
    elif matching_areas and not data_covered:
        assessment = ResearchScopeAssessment.BORDERLINE.value
        reasoning = f"Project area matches {', '.join(matching_areas)} but requires data categories beyond broad consent scope."
    else:
        assessment = ResearchScopeAssessment.OUTSIDE_SCOPE.value
        reasoning = "Project does not fall within any defined broad consent research area. New specific consent required."

    return {
        "project_id": project.project_id,
        "project_title": project.title,
        "assessment": assessment,
        "matching_areas": matching_areas,
        "data_categories_covered": data_covered,
        "reasoning": reasoning,
    }


def verify_safeguards(project: ResearchProject) -> dict:
    """
    Verify Article 89(1) safeguards are in place for a research project.

    Returns:
        Safeguard compliance report.
    """
    results = []
    for safeguard in REQUIRED_SAFEGUARDS:
        present = safeguard in project.safeguards
        results.append({
            "safeguard": safeguard,
            "required": True,
            "present": present,
            "status": "PASS" if present else "FAIL",
        })

    pass_count = sum(1 for r in results if r["present"])
    total = len(REQUIRED_SAFEGUARDS)

    return {
        "project_id": project.project_id,
        "safeguard_results": results,
        "compliance_rate": round(pass_count / total * 100, 1) if total > 0 else 0,
        "all_safeguards_met": pass_count == total,
    }


def assess_withdrawal_impact(
    subject_id: str,
    active_projects: list[ResearchProject],
) -> dict:
    """
    Assess the impact of a consent withdrawal on active research projects.

    Considers Article 17(3)(d) exemption and Article 89(2) derogations.

    Returns:
        Impact assessment with per-project actions.
    """
    impacts = []

    for project in active_projects:
        if project.status == "completed":
            impacts.append({
                "project_id": project.project_id,
                "title": project.title,
                "status": "completed",
                "data_identifiable": False,
                "action": "no_action_required",
                "reasoning": "Research completed. Results are aggregated/anonymized. Art. 17(3)(d) exemption applies.",
            })
        elif project.status == "active":
            impacts.append({
                "project_id": project.project_id,
                "title": project.title,
                "status": "active",
                "data_identifiable": True,
                "action": "remove_from_dataset",
                "reasoning": "Active research. Subject's pseudonymized data will be removed from research dataset.",
            })
        elif project.status == "proposed":
            impacts.append({
                "project_id": project.project_id,
                "title": project.title,
                "status": "proposed",
                "data_identifiable": False,
                "action": "exclude_from_future",
                "reasoning": "Research not yet started. Subject will be excluded from data extraction.",
            })

    return {
        "subject_id": subject_id,
        "withdrawal_timestamp": datetime.now(timezone.utc).isoformat(),
        "projects_affected": len(impacts),
        "impacts": impacts,
    }


if __name__ == "__main__":
    # Create a research project
    project = ResearchProject(
        title="Impact of File Deduplication Algorithms on User Storage Efficiency",
        principal_investigator="Dr. Aoife Murphy, Trinity College Dublin",
        research_area="Cloud storage optimization and deduplication algorithms",
        description="Analyzing how content-defined chunking algorithms affect storage efficiency across different user file types and access patterns",
        data_categories_needed=["file_metadata", "storage_patterns", "access_frequency"],
        safeguards=["pseudonymization", "data_minimization", "access_controls", "retention_limitation", "no_re_identification", "audit_trail"],
        ethics_reference="CREC-2026-007",
        subjects_count=15000,
    )

    # Assess scope
    print("=== Research Scope Assessment ===")
    scope = assess_research_scope(project)
    print(f"Assessment: {scope['assessment']}")
    print(f"Matching areas: {scope['matching_areas']}")
    print(f"Reasoning: {scope['reasoning']}")

    # Verify safeguards
    print("\n=== Safeguard Verification ===")
    safeguards = verify_safeguards(project)
    print(f"Compliance: {safeguards['compliance_rate']}%")
    print(f"All met: {safeguards['all_safeguards_met']}")
    for s in safeguards["safeguard_results"]:
        print(f"  {s['safeguard']}: {s['status']}")

    # Assess withdrawal impact
    print("\n=== Withdrawal Impact Assessment ===")
    completed_project = ResearchProject(
        title="Cloud Storage Usage Patterns 2025",
        status="completed",
        publications=["DOI:10.1145/example-2025-001"],
    )
    active_project = ResearchProject(
        title="Real-Time File Access Prediction",
        status="active",
    )

    impact = assess_withdrawal_impact(
        "usr_7f3a9b2e-41d8-4c76-b5e3-9a8d1c2f4e60",
        [completed_project, active_project, project],
    )
    print(f"Projects affected: {impact['projects_affected']}")
    for i in impact["impacts"]:
        print(f"  {i['title']}: {i['action']}")
        print(f"    Reasoning: {i['reasoning']}")
