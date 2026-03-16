#!/usr/bin/env python3
"""
Audit Evidence Collection Processor

Manages evidence planning, collection tracking, sufficiency assessment,
and evidence quality evaluation for privacy audit engagements.
"""

import json
import os
from datetime import datetime, timedelta
from typing import Any


EVIDENCE_TYPES = {
    "documentary": {
        "description": "Policies, records, contracts, training materials, correspondence",
        "reliability": "high",
        "weight": 3,
    },
    "testimonial": {
        "description": "Interviews, declarations, walkthrough explanations",
        "reliability": "medium",
        "weight": 2,
    },
    "observational": {
        "description": "System walkthroughs, physical inspections, process observation",
        "reliability": "high",
        "weight": 3,
    },
    "analytical": {
        "description": "Data analysis, trend analysis, benchmarking",
        "reliability": "high",
        "weight": 3,
    },
}

RELIABILITY_SCORES = {
    "system_generated": 5,
    "third_party_confirmed": 4,
    "internally_verified": 3,
    "self_reported": 2,
    "unverified": 1,
}

SUFFICIENCY_THRESHOLD = 2  # Minimum evidence items per audit criterion


def create_evidence_plan(
    audit_id: str,
    audit_objectives: list[str],
    audit_criteria: dict[str, list[str]],
    sampling_method: str = "risk_based",
) -> dict[str, Any]:
    """
    Create an evidence collection plan for a privacy audit engagement.

    Args:
        audit_id: Unique audit engagement identifier.
        audit_objectives: List of audit objective descriptions.
        audit_criteria: Mapping of objective to specific regulatory criteria.
        sampling_method: Sampling approach (random, stratified, risk_based, key_item).

    Returns:
        Evidence collection plan.
    """
    plan_items = []
    for objective in audit_objectives:
        criteria = audit_criteria.get(objective, [])
        for criterion in criteria:
            plan_items.append({
                "objective": objective,
                "criterion": criterion,
                "evidence_types_required": ["documentary", "testimonial"],
                "sampling_method": sampling_method,
                "status": "planned",
                "evidence_items": [],
            })

    return {
        "audit_id": audit_id,
        "plan_created": datetime.now().strftime("%Y-%m-%d"),
        "sampling_method": sampling_method,
        "total_criteria": len(plan_items),
        "plan_items": plan_items,
    }


def register_evidence(
    evidence_id: str,
    audit_id: str,
    evidence_type: str,
    title: str,
    source: str,
    source_reliability: str,
    audit_criterion: str,
    collected_by: str,
    description: str,
    date_of_evidence: str = "",
) -> dict[str, Any]:
    """
    Register a collected evidence item.

    Args:
        evidence_id: Unique evidence reference number.
        audit_id: Associated audit engagement ID.
        evidence_type: Type (documentary, testimonial, observational, analytical).
        title: Evidence item title.
        source: Who or what provided the evidence.
        source_reliability: Reliability level (system_generated, third_party_confirmed,
                           internally_verified, self_reported, unverified).
        audit_criterion: The specific audit criterion this evidence supports.
        collected_by: Name of the auditor who collected the evidence.
        description: Brief description of the evidence content.
        date_of_evidence: Date the evidence item was created or observed.

    Returns:
        Registered evidence record.
    """
    reliability_score = RELIABILITY_SCORES.get(source_reliability, 1)
    type_config = EVIDENCE_TYPES.get(evidence_type, EVIDENCE_TYPES["documentary"])

    return {
        "evidence_id": evidence_id,
        "audit_id": audit_id,
        "evidence_type": evidence_type,
        "title": title,
        "source": source,
        "source_reliability": source_reliability,
        "reliability_score": reliability_score,
        "type_weight": type_config["weight"],
        "audit_criterion": audit_criterion,
        "collected_by": collected_by,
        "collection_date": datetime.now().strftime("%Y-%m-%d"),
        "date_of_evidence": date_of_evidence or datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "status": "collected",
        "verified": False,
        "cross_references": [],
    }


def assess_sufficiency(
    evidence_items: list[dict[str, Any]],
    audit_criteria: list[str],
) -> dict[str, Any]:
    """
    Assess whether collected evidence is sufficient for each audit criterion.

    Args:
        evidence_items: List of registered evidence records.
        audit_criteria: List of audit criteria to assess.

    Returns:
        Sufficiency assessment with gaps identified.
    """
    criteria_evidence = {}
    for criterion in audit_criteria:
        criteria_evidence[criterion] = {
            "evidence_items": [],
            "evidence_count": 0,
            "types_covered": set(),
            "avg_reliability": 0.0,
            "sufficient": False,
        }

    for item in evidence_items:
        criterion = item.get("audit_criterion", "")
        if criterion in criteria_evidence:
            criteria_evidence[criterion]["evidence_items"].append(item["evidence_id"])
            criteria_evidence[criterion]["evidence_count"] += 1
            criteria_evidence[criterion]["types_covered"].add(item["evidence_type"])

    gaps = []
    for criterion, data in criteria_evidence.items():
        count = data["evidence_count"]
        matching = [
            e for e in evidence_items if e.get("audit_criterion") == criterion
        ]
        if matching:
            avg_rel = sum(e["reliability_score"] for e in matching) / len(matching)
            data["avg_reliability"] = round(avg_rel, 1)

        data["sufficient"] = (
            count >= SUFFICIENCY_THRESHOLD and data["avg_reliability"] >= 2.5
        )
        data["types_covered"] = list(data["types_covered"])

        if not data["sufficient"]:
            gap_reasons = []
            if count < SUFFICIENCY_THRESHOLD:
                gap_reasons.append(
                    f"insufficient quantity ({count}/{SUFFICIENCY_THRESHOLD})"
                )
            if data["avg_reliability"] < 2.5:
                gap_reasons.append(
                    f"low reliability ({data['avg_reliability']}/5.0)"
                )
            gaps.append({
                "criterion": criterion,
                "current_count": count,
                "reasons": gap_reasons,
                "recommended_action": "Collect additional corroborating evidence",
            })

    total = len(audit_criteria)
    sufficient_count = sum(
        1 for d in criteria_evidence.values() if d["sufficient"]
    )

    return {
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "total_criteria": total,
        "sufficient_criteria": sufficient_count,
        "insufficient_criteria": total - sufficient_count,
        "sufficiency_rate": round(sufficient_count / total * 100, 1) if total > 0 else 0,
        "gaps": gaps,
        "criteria_detail": {
            k: {**v, "types_covered": list(v["types_covered"]) if isinstance(v["types_covered"], set) else v["types_covered"]}
            for k, v in criteria_evidence.items()
        },
    }


def generate_evidence_log(
    evidence_items: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Generate a summary evidence log for the audit engagement.

    Args:
        evidence_items: List of registered evidence records.

    Returns:
        Evidence log summary.
    """
    by_type = {}
    by_reliability = {}
    by_criterion = {}

    for item in evidence_items:
        etype = item.get("evidence_type", "unknown")
        by_type[etype] = by_type.get(etype, 0) + 1

        rel = item.get("source_reliability", "unverified")
        by_reliability[rel] = by_reliability.get(rel, 0) + 1

        crit = item.get("audit_criterion", "unlinked")
        by_criterion[crit] = by_criterion.get(crit, 0) + 1

    return {
        "log_date": datetime.now().strftime("%Y-%m-%d"),
        "total_items": len(evidence_items),
        "by_type": by_type,
        "by_reliability": by_reliability,
        "by_criterion": by_criterion,
        "verified_count": sum(1 for e in evidence_items if e.get("verified")),
        "unverified_count": sum(1 for e in evidence_items if not e.get("verified")),
    }


if __name__ == "__main__":
    plan = create_evidence_plan(
        audit_id="PA-2026-003",
        audit_objectives=["Assess DSAR response compliance", "Verify consent mechanisms"],
        audit_criteria={
            "Assess DSAR response compliance": [
                "GDPR Art. 15 — Right of access response within 30 days",
                "GDPR Art. 17 — Erasure request processing",
            ],
            "Verify consent mechanisms": [
                "GDPR Art. 7 — Conditions for consent",
            ],
        },
    )
    print(f"Evidence plan created: {plan['audit_id']}")
    print(f"Total criteria to evidence: {plan['total_criteria']}")

    evidence1 = register_evidence(
        evidence_id="EV-2026-001",
        audit_id="PA-2026-003",
        evidence_type="documentary",
        title="DSAR response log extract (Jan-Mar 2026)",
        source="Privacy management system",
        source_reliability="system_generated",
        audit_criterion="GDPR Art. 15 — Right of access response within 30 days",
        collected_by="Auditor A",
        description="System-generated log of 142 access requests with response timestamps",
    )

    evidence2 = register_evidence(
        evidence_id="EV-2026-002",
        audit_id="PA-2026-003",
        evidence_type="testimonial",
        title="Interview with DSAR team lead",
        source="DSAR Team Lead",
        source_reliability="internally_verified",
        audit_criterion="GDPR Art. 15 — Right of access response within 30 days",
        collected_by="Auditor A",
        description="Structured interview covering DSAR triage, response workflow, and escalation",
    )

    assessment = assess_sufficiency(
        evidence_items=[evidence1, evidence2],
        audit_criteria=[
            "GDPR Art. 15 — Right of access response within 30 days",
            "GDPR Art. 17 — Erasure request processing",
            "GDPR Art. 7 — Conditions for consent",
        ],
    )

    print(f"Sufficiency rate: {assessment['sufficiency_rate']}%")
    print(f"Gaps identified: {len(assessment['gaps'])}")
    for gap in assessment["gaps"]:
        print(f"  - {gap['criterion']}: {', '.join(gap['reasons'])}")
