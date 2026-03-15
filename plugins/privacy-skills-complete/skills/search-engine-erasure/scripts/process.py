"""
Search Engine Erasure (Right to Be Forgotten) Process
Implements EDPB 13-point assessment and delisting request management.
"""

import json
from datetime import datetime
from enum import Enum
from typing import Optional


class DelistingDecision(Enum):
    APPROVE = "approve"
    REFUSE = "refuse"
    PARTIAL = "partial"
    PENDING = "pending_assessment"


class SearchEngine(Enum):
    GOOGLE = "Google"
    BING = "Microsoft Bing"
    DUCKDUCKGO = "DuckDuckGo"
    YAHOO = "Yahoo"


class EDPBCriterion:
    """Represents one of the 13 EDPB assessment criteria."""

    def __init__(self, number: int, name: str, weight: str):
        self.number = number
        self.name = name
        self.weight = weight
        self.assessment: Optional[str] = None
        self.favours: Optional[str] = None  # "delisting" or "refusal"
        self.strength: Optional[str] = None  # "strong", "moderate", "weak", "neutral"

    def assess(self, assessment: str, favours: str, strength: str) -> None:
        self.assessment = assessment
        self.favours = favours
        self.strength = strength

    def to_dict(self) -> dict:
        return {
            "criterion": self.number,
            "name": self.name,
            "assessment": self.assessment,
            "favours": self.favours,
            "strength": self.strength,
        }


def build_edpb_criteria() -> list[EDPBCriterion]:
    """Build the 13 EDPB assessment criteria."""
    return [
        EDPBCriterion(1, "Role in public life", "Public figures have reduced delisting expectation"),
        EDPBCriterion(2, "Nature of information", "Special category data weighs toward delisting"),
        EDPBCriterion(3, "Accuracy of information", "Inaccurate information favours delisting"),
        EDPBCriterion(4, "Relevance", "Irrelevant information favours delisting"),
        EDPBCriterion(5, "Age of information", "Older information generally favours delisting"),
        EDPBCriterion(6, "Source of information", "Journalistic sources weigh against delisting"),
        EDPBCriterion(7, "Context of publication", "Self-published may weigh against delisting"),
        EDPBCriterion(8, "Sensitivity", "Higher sensitivity favours delisting"),
        EDPBCriterion(9, "Impact on data subject", "Significant harm favours delisting"),
        EDPBCriterion(10, "Access context", "Name-based searches more intrusive"),
        EDPBCriterion(11, "Minor", "Data subjects who were children have strengthened right"),
        EDPBCriterion(12, "Criminal data", "Spent convictions favour delisting"),
        EDPBCriterion(13, "Legal obligation to index", "Legal requirement to maintain weighs against delisting"),
    ]


class DelistingRequest:
    """Manages a delisting request assessment and submission."""

    def __init__(
        self,
        data_subject_name: str,
        urls: list[str],
        grounds: list[str],
        search_engines: list[SearchEngine],
    ):
        self.reference = f"DELIST-{datetime.utcnow().strftime('%Y')}-{hash(data_subject_name) % 10000:04d}"
        self.data_subject_name = data_subject_name
        self.urls = urls
        self.grounds = grounds
        self.search_engines = search_engines
        self.created_at = datetime.utcnow()
        self.criteria = build_edpb_criteria()
        self.decision: Optional[DelistingDecision] = None
        self.decision_reasoning: Optional[str] = None
        self.submissions: list[dict] = []
        self.responses: list[dict] = []

    def assess_criterion(
        self, criterion_number: int, assessment: str, favours: str, strength: str
    ) -> None:
        """Assess a specific EDPB criterion."""
        for c in self.criteria:
            if c.number == criterion_number:
                c.assess(assessment, favours, strength)
                return
        raise ValueError(f"Invalid criterion number: {criterion_number}")

    def compute_balance(self) -> dict:
        """Compute the balance of assessed criteria."""
        assessed = [c for c in self.criteria if c.assessment is not None]
        delisting_factors = [c for c in assessed if c.favours == "delisting"]
        refusal_factors = [c for c in assessed if c.favours == "refusal"]
        neutral_factors = [c for c in assessed if c.favours == "neutral"]

        strong_delisting = sum(1 for c in delisting_factors if c.strength == "strong")
        strong_refusal = sum(1 for c in refusal_factors if c.strength == "strong")

        return {
            "total_assessed": len(assessed),
            "favouring_delisting": len(delisting_factors),
            "favouring_refusal": len(refusal_factors),
            "neutral": len(neutral_factors),
            "strong_delisting_factors": strong_delisting,
            "strong_refusal_factors": strong_refusal,
            "preliminary_indication": "delisting" if len(delisting_factors) > len(refusal_factors) else "refusal",
        }

    def make_decision(self, decision: DelistingDecision, reasoning: str) -> None:
        """Record the decision on the delisting request."""
        self.decision = decision
        self.decision_reasoning = reasoning

    def record_submission(
        self, search_engine: SearchEngine, submission_date: str, reference: Optional[str] = None
    ) -> None:
        """Record submission to a search engine."""
        self.submissions.append({
            "search_engine": search_engine.value,
            "submission_date": submission_date,
            "reference": reference,
            "status": "submitted",
        })

    def record_response(
        self,
        search_engine: SearchEngine,
        response_date: str,
        outcome: str,
        details: Optional[str] = None,
    ) -> None:
        """Record response from a search engine."""
        self.responses.append({
            "search_engine": search_engine.value,
            "response_date": response_date,
            "outcome": outcome,
            "details": details,
        })

    def generate_assessment_report(self) -> dict:
        """Generate the full assessment report."""
        return {
            "reference": self.reference,
            "organization": "Orion Data Vault Corp",
            "created_at": self.created_at.isoformat(),
            "data_subject": self.data_subject_name,
            "urls": self.urls,
            "grounds": self.grounds,
            "edpb_assessment": [c.to_dict() for c in self.criteria],
            "balance": self.compute_balance(),
            "decision": self.decision.value if self.decision else "pending",
            "decision_reasoning": self.decision_reasoning,
            "submissions": self.submissions,
            "responses": self.responses,
        }


if __name__ == "__main__":
    request = DelistingRequest(
        data_subject_name="[Pseudonymised]",
        urls=["https://news-archive.oriondatavault.corp/2019/employee-dispute-filing"],
        grounds=["Art. 17(1)(a) — Data no longer necessary for original purpose"],
        search_engines=[SearchEngine.GOOGLE, SearchEngine.BING],
    )
    request.assess_criterion(1, "Private individual, no public role", "delisting", "strong")
    request.assess_criterion(2, "Standard personal data — employment history", "neutral", "neutral")
    request.assess_criterion(3, "Information is accurate", "refusal", "moderate")
    request.assess_criterion(4, "Information is 8 years old and no longer relevant", "delisting", "strong")
    request.assess_criterion(5, "Published 8 years ago", "delisting", "moderate")
    request.assess_criterion(9, "Employment prospects affected", "delisting", "strong")

    balance = request.compute_balance()
    request.make_decision(
        DelistingDecision.APPROVE,
        "Private individual with no public role. Information is 8 years old and demonstrably affecting employment. Privacy rights outweigh public interest.",
    )

    print(json.dumps(request.generate_assessment_report(), indent=2))
