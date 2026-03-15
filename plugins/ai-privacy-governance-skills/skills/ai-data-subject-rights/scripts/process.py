#!/usr/bin/env python3
"""AI Data Subject Rights Processing Engine for AI systems."""

import json
import datetime
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class RightType(Enum):
    ACCESS = "Right of Access (Art. 15)"
    RECTIFICATION = "Right to Rectification (Art. 16)"
    ERASURE = "Right to Erasure (Art. 17)"
    RESTRICTION = "Right to Restriction (Art. 18)"
    PORTABILITY = "Right to Portability (Art. 20)"
    OBJECTION = "Right to Object (Art. 21)"
    AUTOMATED_DECISION = "Automated Decision Rights (Art. 22)"
    EXPLANATION = "Right to Explanation (Art. 86 AI Act)"


class RequestStatus(Enum):
    RECEIVED = "Received"
    IN_PROGRESS = "In Progress"
    ML_ACTION_REQUIRED = "ML Engineering Action Required"
    COMPLETED = "Completed"
    PARTIALLY_COMPLETED = "Partially Completed"
    REFUSED = "Refused (with justification)"


class AIContext(Enum):
    TRAINING_DATA = "Training Data"
    INFERENCE_INPUT = "Inference Input"
    INFERENCE_OUTPUT = "Inference Output/Decision"
    MODEL_WEIGHTS = "Model Weights (encoded data)"
    GENERATED_CONTENT = "AI-Generated Content"


@dataclass
class RightsRequest:
    request_id: str
    data_subject_id: str
    right_type: RightType
    ai_contexts: list[AIContext]
    description: str
    received_date: str
    deadline: str
    status: RequestStatus = RequestStatus.RECEIVED
    ai_systems_involved: list[str] = field(default_factory=list)
    ml_action_needed: bool = False
    ml_action_description: str = ""
    response_provided: str = ""


@dataclass
class RightsAssessment:
    request: RightsRequest
    feasibility: str  # "fully_feasible", "partially_feasible", "technically_challenging"
    actions: list[dict]
    ml_engineering_tasks: list[str]
    estimated_completion: str
    issues: list[str]


def assess_request(request: RightsRequest) -> RightsAssessment:
    actions = []
    ml_tasks = []
    issues = []

    if request.right_type == RightType.ACCESS:
        if AIContext.TRAINING_DATA in request.ai_contexts:
            actions.append({"action": "Search training data catalogue for data subject records", "owner": "Data team"})
            actions.append({"action": "Compile training data contribution in structured format", "owner": "Data team"})
        if AIContext.INFERENCE_OUTPUT in request.ai_contexts:
            actions.append({"action": "Retrieve inference logs for data subject", "owner": "Platform team"})
            actions.append({"action": "Generate AI decision explanation (SHAP/LIME)", "owner": "ML team"})
            ml_tasks.append("Generate per-decision explanation using explainability tools")
        feasibility = "fully_feasible"

    elif request.right_type == RightType.RECTIFICATION:
        if AIContext.TRAINING_DATA in request.ai_contexts:
            actions.append({"action": "Correct records in training dataset", "owner": "Data team"})
            ml_tasks.append("Assess if model retraining is needed to propagate correction")
            issues.append("Correction may not propagate to model without retraining")
        if AIContext.GENERATED_CONTENT in request.ai_contexts:
            actions.append({"action": "Correct or flag inaccurate AI-generated content", "owner": "Content team"})
        feasibility = "partially_feasible"

    elif request.right_type == RightType.ERASURE:
        if AIContext.TRAINING_DATA in request.ai_contexts:
            actions.append({"action": "Delete records from training dataset and backups", "owner": "Data team"})
            ml_tasks.append("Run membership inference test on deleted records")
            ml_tasks.append("Apply machine unlearning or schedule model retraining")
            ml_tasks.append("Verify erasure effectiveness post-unlearning")
            issues.append("Full erasure from trained model may require retraining — timeline dependent on model complexity")
        if AIContext.INFERENCE_INPUT in request.ai_contexts:
            actions.append({"action": "Purge inference logs linked to data subject", "owner": "Platform team"})
        feasibility = "technically_challenging"

    elif request.right_type == RightType.OBJECTION:
        actions.append({"action": "Assess whether compelling legitimate grounds override objection", "owner": "Legal"})
        actions.append({"action": "Remove data subject from AI training pipeline", "owner": "Data team"})
        ml_tasks.append("Exclude data subject's data from future training runs")
        feasibility = "fully_feasible"

    elif request.right_type == RightType.AUTOMATED_DECISION:
        actions.append({"action": "Generate AI decision explanation", "owner": "ML team"})
        actions.append({"action": "Assign independent human reviewer", "owner": "Operations"})
        actions.append({"action": "Process contestation through review panel", "owner": "Review panel"})
        ml_tasks.append("Generate SHAP/LIME explanation for specific decision")
        feasibility = "fully_feasible"

    elif request.right_type == RightType.EXPLANATION:
        actions.append({"action": "Generate explanation of AI role in decision", "owner": "ML team"})
        actions.append({"action": "Translate technical explanation to plain language", "owner": "Privacy team"})
        ml_tasks.append("Run explainability analysis on the specific decision")
        feasibility = "fully_feasible"

    else:
        actions.append({"action": f"Process {request.right_type.value} request", "owner": "Privacy team"})
        feasibility = "fully_feasible"

    deadline = datetime.date.fromisoformat(request.received_date) + datetime.timedelta(days=30)
    if feasibility == "technically_challenging":
        deadline += datetime.timedelta(days=60)

    return RightsAssessment(
        request=request,
        feasibility=feasibility,
        actions=actions,
        ml_engineering_tasks=ml_tasks,
        estimated_completion=deadline.isoformat(),
        issues=issues,
    )


def format_report(assessment: RightsAssessment) -> str:
    lines = [f"{'='*80}", "AI DATA SUBJECT RIGHTS REQUEST ASSESSMENT",
             f"Request ID: {assessment.request.request_id}",
             f"Right: {assessment.request.right_type.value}",
             f"Received: {assessment.request.received_date}",
             f"Deadline: {assessment.estimated_completion}", f"{'='*80}"]
    lines.append(f"\nFeasibility: {assessment.feasibility}")
    lines.append(f"AI Contexts: {', '.join(c.value for c in assessment.request.ai_contexts)}")

    if assessment.actions:
        lines.append("\n## ACTIONS")
        for a in assessment.actions:
            lines.append(f"  - [{a['owner']}] {a['action']}")

    if assessment.ml_engineering_tasks:
        lines.append("\n## ML ENGINEERING TASKS")
        for t in assessment.ml_engineering_tasks:
            lines.append(f"  - {t}")

    if assessment.issues:
        lines.append("\n## ISSUES")
        for i in assessment.issues:
            lines.append(f"  - {i}")
    return "\n".join(lines)


def demo_cerebrum_ai_labs():
    request = RightsRequest(
        request_id="DSR-AI-2026-0042",
        data_subject_id="DS-EU-12345",
        right_type=RightType.ERASURE,
        ai_contexts=[AIContext.TRAINING_DATA, AIContext.INFERENCE_INPUT],
        description="Data subject requests erasure of all data from AI training sets and inference logs",
        received_date="2026-03-14",
        deadline="2026-04-13",
        ai_systems_involved=["cerebrum-intent-v2", "cerebrum-recommend-v1"],
    )
    assessment = assess_request(request)
    print(format_report(assessment))


if __name__ == "__main__":
    demo_cerebrum_ai_labs()
