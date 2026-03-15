#!/usr/bin/env python3
"""AI Data Retention and Unlearning Management Engine."""

import json
import datetime
from dataclasses import dataclass, field
from enum import Enum


class DataCategory(Enum):
    RAW_TRAINING = "Raw Training Data"
    PROCESSED_TRAINING = "Processed Training Data"
    VALIDATION = "Validation/Test Data"
    MODEL_WEIGHTS = "Model Weights"
    INFERENCE_LOGS = "Inference Logs"
    EMBEDDINGS = "Embedding Vectors"
    METADATA = "Model Metadata"


class RetentionAction(Enum):
    RETAIN = "Retain"
    DELETE = "Delete"
    PSEUDONYMISE = "Pseudonymise and Retain"
    ARCHIVE = "Archive with Controls"


class UnlearningMethod(Enum):
    FULL_RETRAINING = "Full Retraining"
    SISA = "SISA Shard Retraining"
    GRADIENT_ASCENT = "Gradient-Based Unlearning"
    INFLUENCE_FUNCTION = "Influence Function Unlearning"
    NOT_NEEDED = "Not Needed"


@dataclass
class DataAsset:
    name: str
    category: DataCategory
    record_count: int
    contains_pii: bool
    sensitivity: str  # "general", "special_category"
    retraining_planned: bool = False
    needed_for_validation: bool = False
    needed_for_rights: bool = False
    legal_retention_obligation: bool = False
    current_retention_days: int = 0
    recommended_action: RetentionAction = RetentionAction.RETAIN
    justification: str = ""


@dataclass
class UnlearningTask:
    model_name: str
    records_to_delete: int
    data_sensitivity: str
    recommended_method: UnlearningMethod
    estimated_cost: str  # "low", "medium", "high"
    verification_required: bool = True
    notes: str = ""


def assess_retention(asset: DataAsset) -> DataAsset:
    if asset.retraining_planned:
        asset.recommended_action = RetentionAction.RETAIN
        asset.justification = "Retained for planned model retraining"
    elif asset.needed_for_validation:
        asset.recommended_action = RetentionAction.PSEUDONYMISE
        asset.justification = "Pseudonymised and retained for model validation and audit"
    elif asset.needed_for_rights:
        asset.recommended_action = RetentionAction.ARCHIVE
        asset.justification = "Archived for data subject rights exercise"
    elif asset.legal_retention_obligation:
        asset.recommended_action = RetentionAction.ARCHIVE
        asset.justification = "Retained per legal obligation"
    else:
        asset.recommended_action = RetentionAction.DELETE
        asset.justification = "No retention justification — delete per Art. 5(1)(e)"
    return asset


def recommend_unlearning(
    model_name: str,
    records_to_delete: int,
    total_training_records: int,
    model_parameters: int,
    sensitivity: str,
    sisa_available: bool = False,
) -> UnlearningTask:
    deletion_ratio = records_to_delete / total_training_records if total_training_records > 0 else 0

    if deletion_ratio > 0.1 or sensitivity == "special_category":
        method = UnlearningMethod.FULL_RETRAINING
        cost = "high"
        notes = "High deletion ratio or sensitive data — full retraining recommended for strongest guarantee"
    elif sisa_available:
        method = UnlearningMethod.SISA
        cost = "medium"
        notes = "SISA architecture available — retrain affected shard only"
    elif deletion_ratio > 0.01:
        method = UnlearningMethod.GRADIENT_ASCENT
        cost = "low"
        notes = "Approximate unlearning via gradient ascent + fine-tuning"
    elif model_parameters < 10_000_000:
        method = UnlearningMethod.INFLUENCE_FUNCTION
        cost = "medium"
        notes = "Small model — influence function unlearning feasible"
    else:
        method = UnlearningMethod.GRADIENT_ASCENT
        cost = "low"
        notes = "Low deletion ratio — gradient-based approximate unlearning"

    return UnlearningTask(
        model_name=model_name,
        records_to_delete=records_to_delete,
        data_sensitivity=sensitivity,
        recommended_method=method,
        estimated_cost=cost,
        notes=notes,
    )


def format_retention_report(assets: list[DataAsset], org_name: str) -> str:
    today = datetime.date.today().isoformat()
    lines = [f"{'='*80}", "AI DATA RETENTION ASSESSMENT", f"Organisation: {org_name}",
             f"Date: {today}", f"{'='*80}"]

    delete_count = sum(1 for a in assets if a.recommended_action == RetentionAction.DELETE)
    retain_count = sum(1 for a in assets if a.recommended_action == RetentionAction.RETAIN)

    lines.append(f"\nAssets assessed: {len(assets)}")
    lines.append(f"Recommended for deletion: {delete_count}")
    lines.append(f"Recommended for retention: {retain_count}")

    for asset in assets:
        lines.append(f"\n  {asset.name} [{asset.category.value}]")
        lines.append(f"  Records: {asset.record_count:,} | PII: {'Yes' if asset.contains_pii else 'No'}")
        lines.append(f"  Action: {asset.recommended_action.value}")
        lines.append(f"  Justification: {asset.justification}")

    return "\n".join(lines)


def demo_cerebrum_ai_labs():
    assets = [
        DataAsset("Customer Support Transcripts", DataCategory.RAW_TRAINING, 850_000, True, "general", retraining_planned=True),
        DataAsset("Web Scraped Reviews", DataCategory.RAW_TRAINING, 10_000_000, True, "general"),
        DataAsset("Validation Dataset", DataCategory.VALIDATION, 50_000, True, "general", needed_for_validation=True),
        DataAsset("Intent Model v2 Weights", DataCategory.MODEL_WEIGHTS, 1, True, "general"),
        DataAsset("Inference Logs (90 days)", DataCategory.INFERENCE_LOGS, 5_000_000, True, "general", needed_for_rights=True),
    ]

    for asset in assets:
        assess_retention(asset)

    print(format_retention_report(assets, "Cerebrum AI Labs"))

    task = recommend_unlearning("cerebrum-intent-v2", 500, 850_000, 110_000_000, "general")
    print(f"\n\nUNLEARNING RECOMMENDATION:")
    print(f"  Model: {task.model_name}")
    print(f"  Records to delete: {task.records_to_delete}")
    print(f"  Method: {task.recommended_method.value}")
    print(f"  Cost: {task.estimated_cost}")
    print(f"  Notes: {task.notes}")


if __name__ == "__main__":
    demo_cerebrum_ai_labs()
