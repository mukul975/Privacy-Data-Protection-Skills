#!/usr/bin/env python3
"""
Search Engine Erasure (Right to Be Forgotten) Process
Implements the EDPB 13-point assessment framework for delisting requests.
"""

import json
from datetime import datetime
from enum import Enum


class DelistingDecision(Enum):
    APPROVE = "approve_delisting"
    REFUSE = "refuse_delisting"
    PARTIAL = "partial_delisting"
    FURTHER_REVIEW = "further_review_required"


EDPB_CRITERIA = [
    {"id": 1, "name": "Role in public life", "weight": "high", "description": "Does the data subject play a role in public life?"},
    {"id": 2, "name": "Nature of information", "weight": "high", "description": "What type of personal data is involved?"},
    {"id": 3, "name": "Accuracy", "weight": "high", "description": "Is the information accurate and up-to-date?"},
    {"id": 4, "name": "Relevance", "weight": "medium", "description": "Is the information still relevant to public interest?"},
    {"id": 5, "name": "Age of information", "weight": "medium", "description": "How old is the information?"},
    {"id": 6, "name": "Source", "weight": "medium", "description": "Who published the original content?"},
    {"id": 7, "name": "Context of publication", "weight": "low", "description": "Was it published voluntarily by the data subject?"},
    {"id": 8, "name": "Sensitivity", "weight": "high", "description": "How sensitive is the information?"},
    {"id": 9, "name": "Impact on data subject", "weight": "high", "description": "What impact does continued indexing have?"},
    {"id": 10, "name": "Access context", "weight": "medium", "description": "In what context do users access this via search?"},
    {"id": 11, "name": "Minor", "weight": "high", "description": "Is the data subject a minor or was data published when they were?"},
    {"id": 12, "name": "Criminal data", "weight": "high", "description": "Does the information relate to criminal proceedings?"},
    {"id": 13, "name": "Legal obligation", "weight": "medium", "description": "Is there a legal obligation to index the information?"},
]


def generate_delisting_reference() -> str:
    """Generate a unique delisting case reference."""
    year = datetime.utcnow().strftime("%Y")
    seq = datetime.utcnow().strftime("%m%d%H")
    return f"DELIST-{year}-{seq}"


def assess_delisting_request(
    criteria_scores: dict[int, dict],
) -> dict:
    """
    Assess a delisting request using the EDPB 13-point framework.

    criteria_scores: dict mapping criterion ID to:
        {"score": int (1-5, where 1 favours refusal and 5 favours delisting),
         "notes": str}
    """
    reference = generate_delisting_reference()
    assessment = {
        "reference": reference,
        "assessment_date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "criteria_evaluations": [],
        "score_summary": {"total": 0, "max_possible": 0, "weighted_score": 0},
    }

    weight_map = {"high": 3, "medium": 2, "low": 1}
    total_weighted = 0
    max_weighted = 0

    for criterion in EDPB_CRITERIA:
        cid = criterion["id"]
        score_data = criteria_scores.get(cid, {"score": 3, "notes": "Not assessed"})
        weight = weight_map[criterion["weight"]]
        weighted = score_data["score"] * weight

        total_weighted += weighted
        max_weighted += 5 * weight

        assessment["criteria_evaluations"].append({
            "criterion_id": cid,
            "criterion_name": criterion["name"],
            "weight": criterion["weight"],
            "score": score_data["score"],
            "weighted_score": weighted,
            "notes": score_data["notes"],
        })

    assessment["score_summary"]["total"] = total_weighted
    assessment["score_summary"]["max_possible"] = max_weighted
    percentage = round((total_weighted / max_weighted) * 100, 1) if max_weighted > 0 else 0
    assessment["score_summary"]["weighted_score"] = percentage

    if percentage >= 70:
        decision = DelistingDecision.APPROVE
        reasoning = "Privacy rights clearly prevail over public interest in continued indexing."
    elif percentage >= 50:
        decision = DelistingDecision.FURTHER_REVIEW
        reasoning = "Borderline case requiring detailed written balancing assessment and DPO/Legal consultation."
    elif percentage >= 35:
        decision = DelistingDecision.PARTIAL
        reasoning = "Some URLs may qualify for delisting while others do not. Per-URL assessment needed."
    else:
        decision = DelistingDecision.REFUSE
        reasoning = "Public interest in access to information outweighs data subject's privacy rights."

    assessment["decision"] = decision.value
    assessment["reasoning"] = reasoning

    return assessment


def generate_delisting_request_template(
    data_subject_name: str,
    search_engine: str,
    urls: list[dict],
    grounds: list[str],
    relationship_to_org: str,
    impact_description: str,
) -> dict:
    """Generate a delisting request template for submission."""
    reference = generate_delisting_reference()
    return {
        "reference": reference,
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "data_subject": data_subject_name,
        "search_engine": search_engine,
        "urls_for_delisting": urls,
        "grounds_cited": grounds,
        "relationship_to_organization": relationship_to_org,
        "impact_of_continued_indexing": impact_description,
        "identity_verification": "Government-issued ID attached (for search engine submission only)",
        "status": "draft",
    }


def track_delisting_response(
    reference: str,
    search_engine: str,
    response_type: str,
    urls_delisted: list[str],
    urls_refused: list[str],
    reasoning: str,
) -> dict:
    """Track the search engine's response to a delisting request."""
    return {
        "reference": reference,
        "search_engine": search_engine,
        "response_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "response_type": response_type,
        "urls_delisted": urls_delisted,
        "urls_refused": urls_refused,
        "reasoning": reasoning,
        "next_action": (
            "Verify delisting effectiveness"
            if response_type == "approved"
            else "Assess DPA complaint escalation"
            if response_type == "refused"
            else "Review partial outcome; consider resubmission for refused URLs"
        ),
    }


if __name__ == "__main__":
    sample_scores = {
        1: {"score": 5, "notes": "Private individual, no public role"},
        2: {"score": 4, "notes": "Employment history — standard personal data"},
        3: {"score": 4, "notes": "Information partially outdated (5 years old)"},
        4: {"score": 4, "notes": "No current relevance to public interest"},
        5: {"score": 4, "notes": "Published 5 years ago; significant passage of time"},
        6: {"score": 3, "notes": "Published by local news outlet"},
        7: {"score": 5, "notes": "Not self-published by data subject"},
        8: {"score": 3, "notes": "Standard sensitivity — employment information"},
        9: {"score": 5, "notes": "Significant impact — preventing employment due to outdated article"},
        10: {"score": 4, "notes": "Appears in name-based search (highly intrusive)"},
        11: {"score": 3, "notes": "Adult at time of publication"},
        12: {"score": 3, "notes": "No criminal data involved"},
        13: {"score": 4, "notes": "No legal obligation to index"},
    }

    assessment = assess_delisting_request(sample_scores)
    print(f"Assessment Reference: {assessment['reference']}")
    print(f"Weighted Score: {assessment['score_summary']['weighted_score']}%")
    print(f"Decision: {assessment['decision']}")
    print(f"Reasoning: {assessment['reasoning']}")
