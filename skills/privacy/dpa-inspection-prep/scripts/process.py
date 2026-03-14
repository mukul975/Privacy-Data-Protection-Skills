#!/usr/bin/env python3
"""
DPA Inspection Preparation Processor

Manages document readiness tracking, interview preparation scheduling,
and inspection response protocol execution for supervisory authority inspections.
"""

import json
import os
from datetime import datetime, timedelta
from typing import Any

CORE_DOCUMENTS = [
    {"id": 1, "name": "Records of Processing Activities (Controller)", "gdpr_ref": "Art. 30(1)", "category": "core"},
    {"id": 2, "name": "Records of Processing Activities (Processor)", "gdpr_ref": "Art. 30(2)", "category": "core"},
    {"id": 3, "name": "Privacy Policy (all versions)", "gdpr_ref": "Art. 13-14", "category": "core"},
    {"id": 4, "name": "Data Protection Impact Assessments", "gdpr_ref": "Art. 35", "category": "core"},
    {"id": 5, "name": "Data Processing Agreements", "gdpr_ref": "Art. 28", "category": "core"},
    {"id": 6, "name": "Legitimate Interest Assessments", "gdpr_ref": "Art. 6(1)(f)", "category": "core"},
    {"id": 7, "name": "International Transfer Mechanisms", "gdpr_ref": "Art. 44-49", "category": "core"},
    {"id": 8, "name": "Breach Notification Records", "gdpr_ref": "Art. 33-34", "category": "core"},
    {"id": 9, "name": "DSAR Records", "gdpr_ref": "Art. 12-22", "category": "core"},
    {"id": 10, "name": "Consent Records", "gdpr_ref": "Art. 7", "category": "core"},
    {"id": 11, "name": "DPO Appointment Documentation", "gdpr_ref": "Art. 37-39", "category": "core"},
    {"id": 12, "name": "Privacy Training Records", "gdpr_ref": "Art. 39(1)(b)", "category": "core"},
    {"id": 13, "name": "Data Protection Policy Manual", "gdpr_ref": "Art. 24(2)", "category": "core"},
    {"id": 14, "name": "Information Security Policy", "gdpr_ref": "Art. 32", "category": "core"},
    {"id": 15, "name": "Vendor Risk Assessment Records", "gdpr_ref": "Art. 28(1)", "category": "core"},
]

SUPPORTING_DOCUMENTS = [
    {"id": 16, "name": "Data Flow Diagrams", "gdpr_ref": "Art. 30, 35(7)(a)", "category": "supporting"},
    {"id": 17, "name": "Data Classification Inventory", "gdpr_ref": "Art. 5(1)(c),(e)", "category": "supporting"},
    {"id": 18, "name": "Retention Schedule", "gdpr_ref": "Art. 5(1)(e)", "category": "supporting"},
    {"id": 19, "name": "Privacy Committee Minutes", "gdpr_ref": "Art. 24(1)", "category": "supporting"},
    {"id": 20, "name": "Internal Audit Reports", "gdpr_ref": "Art. 24(1)", "category": "supporting"},
    {"id": 21, "name": "Privacy Risk Register", "gdpr_ref": "Art. 24(1), 32(1)", "category": "supporting"},
    {"id": 22, "name": "Employee Privacy Policy", "gdpr_ref": "Art. 13-14", "category": "supporting"},
    {"id": 23, "name": "Cookie Audit Results", "gdpr_ref": "ePrivacy Art. 5(3)", "category": "supporting"},
    {"id": 24, "name": "Sub-processor Lists", "gdpr_ref": "Art. 28(2)", "category": "supporting"},
    {"id": 25, "name": "Privacy by Design Documentation", "gdpr_ref": "Art. 25", "category": "supporting"},
]

READINESS_SCORES = {
    "green": {"label": "Ready", "score": 3, "description": "Current, complete, easily retrievable"},
    "yellow": {"label": "Partially Ready", "score": 2, "description": "Exists but overdue/incomplete"},
    "red": {"label": "Not Ready", "score": 1, "description": "Missing, significantly outdated, or unretrievable"},
}


def assess_document_readiness(
    documents: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Assess document readiness for DPA inspection.

    Args:
        documents: List of document assessments with 'id', 'name', 'status' (green/yellow/red),
                  'last_reviewed', 'location', 'owner'.

    Returns:
        Document readiness assessment.
    """
    all_docs = CORE_DOCUMENTS + SUPPORTING_DOCUMENTS
    doc_map = {d["id"]: d for d in all_docs}

    results = []
    green_count = 0
    yellow_count = 0
    red_count = 0

    for doc in documents:
        doc_id = doc.get("id")
        ref_doc = doc_map.get(doc_id, {})
        status = doc.get("status", "red")

        score_info = READINESS_SCORES.get(status, READINESS_SCORES["red"])

        if status == "green":
            green_count += 1
        elif status == "yellow":
            yellow_count += 1
        else:
            red_count += 1

        results.append({
            "id": doc_id,
            "name": ref_doc.get("name", doc.get("name", "Unknown")),
            "gdpr_ref": ref_doc.get("gdpr_ref", ""),
            "category": ref_doc.get("category", ""),
            "status": score_info["label"],
            "status_color": status,
            "score": score_info["score"],
            "last_reviewed": doc.get("last_reviewed", "Unknown"),
            "location": doc.get("location", "Unknown"),
            "owner": doc.get("owner", "Unassigned"),
        })

    total_assessed = len(results)
    max_score = total_assessed * 3
    actual_score = sum(r["score"] for r in results)
    readiness_percentage = round(actual_score / max_score * 100, 1) if max_score > 0 else 0
    green_percentage = round(green_count / total_assessed * 100, 1) if total_assessed > 0 else 0

    return {
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "summary": {
            "total_documents": total_assessed,
            "green": green_count,
            "yellow": yellow_count,
            "red": red_count,
            "readiness_score": readiness_percentage,
            "green_percentage": green_percentage,
            "target": 90.0,
            "meets_target": green_percentage >= 90.0,
        },
        "documents": results,
        "action_items": [
            {
                "document": r["name"],
                "current_status": r["status"],
                "action": "Update and review" if r["status_color"] == "yellow" else "Create or locate",
                "owner": r["owner"],
            }
            for r in results if r["status_color"] != "green"
        ],
    }


def generate_interview_prep(
    interviewees: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Generate interview preparation briefs for key personnel.

    Args:
        interviewees: List of personnel with 'name', 'role', 'topics'.

    Returns:
        Interview preparation briefs.
    """
    role_guidance = {
        "DPO": {
            "key_topics": ["DPO independence", "Privacy program overview", "Risk management", "DPIA program",
                          "Data subject rights", "International transfers", "Supervisory authority cooperation"],
            "principles": [
                "Answer factually and precisely",
                "Reference documented policies and procedures",
                "Acknowledge gaps honestly; describe remediation plans",
                "Do not volunteer information beyond what is asked",
            ],
        },
        "CISO": {
            "key_topics": ["Art. 32 security measures", "Encryption", "Access controls", "Breach detection",
                          "Incident response", "Logging and monitoring", "Vulnerability management"],
            "principles": [
                "Demonstrate technical controls with evidence",
                "Reference security standards (ISO 27001, NIST CSF)",
                "Be prepared for live demonstrations",
                "Have system administrators available for technical questions",
            ],
        },
        "Business Owner": {
            "key_topics": ["Processing purpose and lawful basis", "Data minimisation", "Data subject information",
                          "Retention periods", "Third-party sharing"],
            "principles": [
                "Clearly articulate why data is collected",
                "Know the lawful basis for your processing",
                "Have your RoPA entry available for reference",
                "Describe data subject rights facilitation",
            ],
        },
    }

    briefs = []
    for person in interviewees:
        role = person.get("role", "Business Owner")
        guidance = role_guidance.get(role, role_guidance["Business Owner"])

        briefs.append({
            "name": person["name"],
            "role": role,
            "topics": person.get("topics", guidance["key_topics"]),
            "preparation_principles": guidance["principles"],
            "documents_to_have_ready": person.get("documents", []),
            "preparation_status": person.get("prepared", False),
        })

    return briefs


if __name__ == "__main__":
    sample_docs = [
        {"id": i, "status": "green" if i <= 12 else "yellow" if i <= 14 else "red",
         "last_reviewed": "2025-01-15", "location": "OneTrust", "owner": "DPO"}
        for i in range(1, 26)
    ]

    readiness = assess_document_readiness(sample_docs)
    print(f"Document Readiness: {readiness['summary']['readiness_score']}%")
    print(f"Green: {readiness['summary']['green']}, Yellow: {readiness['summary']['yellow']}, Red: {readiness['summary']['red']}")
    print(f"Meets Target (90%): {readiness['summary']['meets_target']}")
    print(f"Action Items: {len(readiness['action_items'])}")
