"""
AI Privacy Inference and Derived Data — Inference Registry and Compliance Tracker

Manages the Cerebrum AI Labs Inference Registry: classifies AI-generated inferences,
tracks Art. 22 profiling assessments, monitors inference accuracy across demographic
groups, and handles data subject requests for inference access, explanation,
rectification, and objection.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
import json


class InferenceType(Enum):
    OBSERVED = "observed_data"
    DERIVED = "derived_data"
    INFERRED = "inferred_data"
    AGGREGATED = "aggregated_data"


class ProfilingLevel(Enum):
    PROFILING_ONLY = "profiling_only"
    PROFILING_HUMAN_DECISION = "profiling_informing_human_decision"
    SOLELY_AUTOMATED = "solely_automated_decision"


class Art22Exception(Enum):
    CONTRACT = "art_22_2_a_contract"
    LAW = "art_22_2_b_law"
    EXPLICIT_CONSENT = "art_22_2_c_explicit_consent"
    NOT_APPLICABLE = "not_applicable"


class SpecialCategoryRisk(Enum):
    NONE = "no_art9_risk"
    PROXY_LOW = "proxy_low_correlation"
    PROXY_HIGH = "proxy_high_correlation"
    DIRECT = "direct_art9_inference"


class RequestType(Enum):
    ACCESS = "art_15_access"
    RECTIFICATION = "art_16_rectification"
    OBJECTION = "art_21_objection"
    CONTESTATION = "art_22_3_contestation"


class RequestStatus(Enum):
    RECEIVED = "received"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    REFUSED = "refused"


@dataclass
class InferenceRegistryEntry:
    system_id: str
    system_name: str
    inference_name: str
    inference_type: InferenceType
    description: str
    data_subjects: str
    estimated_volume: int
    input_features: list[str]
    output_format: str
    profiling_level: ProfilingLevel
    art22_exception: Art22Exception
    special_category_risk: SpecialCategoryRisk
    lawful_basis: str
    dpia_reference: str
    retention_days: int
    accuracy_precision: Optional[float] = None
    accuracy_recall: Optional[float] = None
    accuracy_f1: Optional[float] = None
    disparate_impact_ratio: Optional[float] = None
    registered_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    last_reviewed: Optional[datetime] = None
    dpo_approved: bool = False


@dataclass
class Art22Safeguard:
    system_id: str
    human_intervention_available: bool = False
    trained_reviewers: int = 0
    expression_of_views_channel: str = ""
    contestation_sla_days: int = 15
    explanation_method: str = ""
    privacy_notice_updated: bool = False


@dataclass
class AccuracyMetric:
    system_id: str
    inference_name: str
    group: str
    precision: float
    recall: float
    f1: float
    sample_size: int
    measured_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class DataSubjectRequest:
    request_id: str
    data_subject_id: str
    request_type: RequestType
    system_id: str
    inference_name: str
    status: RequestStatus
    description: str
    received_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: Optional[datetime] = None
    outcome: str = ""


class InferenceRegistry:
    """Central registry for all AI-generated inferences about individuals."""

    def __init__(self):
        self.entries: dict[str, InferenceRegistryEntry] = {}
        self.safeguards: dict[str, Art22Safeguard] = {}
        self.accuracy_history: list[AccuracyMetric] = []
        self.requests: dict[str, DataSubjectRequest] = {}

    def register_inference(self, entry: InferenceRegistryEntry) -> str:
        key = f"{entry.system_id}:{entry.inference_name}"
        self.entries[key] = entry
        return key

    def classify_inference(
        self,
        produces_individual_evaluation: bool,
        feeds_automated_decision: bool,
        human_meaningfully_involved: bool,
        decision_has_legal_effects: bool,
        predicts_art9_characteristic: bool,
        proxy_correlation: Optional[float] = None,
    ) -> tuple[ProfilingLevel, SpecialCategoryRisk]:
        """Classify an inference's profiling level and special category risk."""
        if feeds_automated_decision and decision_has_legal_effects:
            if human_meaningfully_involved:
                level = ProfilingLevel.PROFILING_HUMAN_DECISION
            else:
                level = ProfilingLevel.SOLELY_AUTOMATED
        elif produces_individual_evaluation:
            level = ProfilingLevel.PROFILING_ONLY
        else:
            level = ProfilingLevel.PROFILING_ONLY

        if predicts_art9_characteristic:
            risk = SpecialCategoryRisk.DIRECT
        elif proxy_correlation is not None and proxy_correlation > 0.3:
            risk = SpecialCategoryRisk.PROXY_HIGH
        elif proxy_correlation is not None and proxy_correlation > 0.15:
            risk = SpecialCategoryRisk.PROXY_LOW
        else:
            risk = SpecialCategoryRisk.NONE

        return (level, risk)

    def register_safeguards(self, safeguard: Art22Safeguard) -> None:
        self.safeguards[safeguard.system_id] = safeguard

    def record_accuracy(self, metric: AccuracyMetric) -> None:
        self.accuracy_history.append(metric)

    def check_fairness(self, system_id: str, inference_name: str) -> dict:
        """Check disparate impact across groups for a specific inference."""
        key = f"{system_id}:{inference_name}"
        relevant = [
            m for m in self.accuracy_history
            if m.system_id == system_id and m.inference_name == inference_name
        ]

        if not relevant:
            return {"status": "no_data", "message": "No accuracy metrics recorded"}

        groups = {}
        for m in relevant:
            if m.group not in groups or m.measured_at > groups[m.group].measured_at:
                groups[m.group] = m

        if len(groups) < 2:
            return {"status": "insufficient_groups", "message": "Need at least 2 groups for comparison"}

        max_f1 = max(m.f1 for m in groups.values())
        results = []
        violations = []
        for group_name, metric in groups.items():
            ratio = metric.f1 / max_f1 if max_f1 > 0 else 0
            result = {
                "group": group_name,
                "f1": metric.f1,
                "ratio_to_best": round(ratio, 3),
                "four_fifths_pass": ratio >= 0.8,
                "sample_size": metric.sample_size,
            }
            results.append(result)
            if ratio < 0.8:
                violations.append(group_name)

        return {
            "system_id": system_id,
            "inference_name": inference_name,
            "groups_evaluated": len(groups),
            "four_fifths_violations": violations,
            "overall_pass": len(violations) == 0,
            "group_details": results,
        }

    def submit_request(self, request: DataSubjectRequest) -> str:
        self.requests[request.request_id] = request
        return request.request_id

    def process_access_request(self, data_subject_id: str) -> dict:
        """Compile all inferences held about a data subject for Art. 15 response."""
        relevant_systems = []
        for key, entry in self.entries.items():
            relevant_systems.append({
                "system": entry.system_name,
                "inference": entry.inference_name,
                "type": entry.inference_type.value,
                "description": entry.description,
                "input_features_categories": entry.input_features,
                "output_format": entry.output_format,
                "profiling_level": entry.profiling_level.value,
                "art22_applicable": entry.profiling_level == ProfilingLevel.SOLELY_AUTOMATED,
                "retention_days": entry.retention_days,
            })

        return {
            "data_subject_id": data_subject_id,
            "response_type": "art_15_profiling_information",
            "inferences_held": relevant_systems,
            "art_15_1_h_information": {
                "automated_decision_making_exists": any(
                    e.profiling_level == ProfilingLevel.SOLELY_AUTOMATED
                    for e in self.entries.values()
                ),
                "meaningful_logic_explanation": "Individual explanations available on request using SHAP feature attribution",
                "significance_and_consequences": "Inferences may affect service personalisation, credit decisions, and customer retention interventions",
            },
        }

    def compliance_report(self) -> dict:
        """Generate compliance summary across all registered inferences."""
        total = len(self.entries)
        solely_automated = sum(
            1 for e in self.entries.values()
            if e.profiling_level == ProfilingLevel.SOLELY_AUTOMATED
        )
        art9_risk = sum(
            1 for e in self.entries.values()
            if e.special_category_risk in (SpecialCategoryRisk.DIRECT, SpecialCategoryRisk.PROXY_HIGH)
        )
        unapproved = sum(1 for e in self.entries.values() if not e.dpo_approved)
        missing_safeguards = sum(
            1 for e in self.entries.values()
            if e.profiling_level == ProfilingLevel.SOLELY_AUTOMATED
            and e.system_id not in self.safeguards
        )
        pending_requests = sum(
            1 for r in self.requests.values()
            if r.status in (RequestStatus.RECEIVED, RequestStatus.IN_PROGRESS)
        )

        return {
            "total_registered_inferences": total,
            "solely_automated_decisions": solely_automated,
            "art9_special_category_risk": art9_risk,
            "pending_dpo_approval": unapproved,
            "missing_art22_safeguards": missing_safeguards,
            "pending_data_subject_requests": pending_requests,
            "compliant": unapproved == 0 and missing_safeguards == 0 and pending_requests == 0,
        }


if __name__ == "__main__":
    registry = InferenceRegistry()

    # Register churn prediction inference
    churn_entry = InferenceRegistryEntry(
        system_id="CAL-AI-003",
        system_name="Customer Churn Prediction Model",
        inference_name="churn_probability",
        inference_type=InferenceType.INFERRED,
        description="Predicts probability that customer will close account within 6 months",
        data_subjects="Cerebrum AI Labs retail customers",
        estimated_volume=1_500_000,
        input_features=["transaction_count", "account_tenure", "product_holdings",
                        "channel_preference", "complaint_flag", "credit_score", "postcode"],
        output_format="probability_score_0_to_1",
        profiling_level=ProfilingLevel.PROFILING_HUMAN_DECISION,
        art22_exception=Art22Exception.NOT_APPLICABLE,
        special_category_risk=SpecialCategoryRisk.PROXY_HIGH,
        lawful_basis="Art. 6(1)(f) legitimate interests — LIA-ML-CHURN-2026-001",
        dpia_reference="DPIA-ML-CHURN-2026-001",
        retention_days=90,
        accuracy_precision=0.82,
        accuracy_recall=0.78,
        accuracy_f1=0.80,
        disparate_impact_ratio=0.84,
        dpo_approved=True,
    )
    registry.register_inference(churn_entry)

    # Register credit scoring inference (solely automated)
    credit_entry = InferenceRegistryEntry(
        system_id="CAL-AI-004",
        system_name="Credit Scoring AI",
        inference_name="credit_risk_score",
        inference_type=InferenceType.DERIVED,
        description="Calculates credit risk score for loan application decisions",
        data_subjects="Cerebrum AI Labs loan applicants",
        estimated_volume=200_000,
        input_features=["income", "employment_duration", "existing_debt",
                        "payment_history", "credit_utilisation"],
        output_format="risk_score_0_to_1000_with_category",
        profiling_level=ProfilingLevel.SOLELY_AUTOMATED,
        art22_exception=Art22Exception.CONTRACT,
        special_category_risk=SpecialCategoryRisk.PROXY_LOW,
        lawful_basis="Art. 6(1)(b) contract performance",
        dpia_reference="DPIA-AI-CREDIT-2026-001",
        retention_days=180,
        accuracy_precision=0.89,
        accuracy_recall=0.85,
        accuracy_f1=0.87,
        disparate_impact_ratio=0.82,
        dpo_approved=True,
    )
    registry.register_inference(credit_entry)

    # Register Art. 22 safeguards for credit scoring
    safeguard = Art22Safeguard(
        system_id="CAL-AI-004",
        human_intervention_available=True,
        trained_reviewers=8,
        expression_of_views_channel="Customer portal contestation form",
        contestation_sla_days=15,
        explanation_method="SHAP feature attribution — top 5 factors",
        privacy_notice_updated=True,
    )
    registry.register_safeguards(safeguard)

    # Record accuracy metrics by demographic group
    for group, f1 in [("White British", 0.88), ("Asian", 0.85), ("Black", 0.81), ("Other", 0.83)]:
        registry.record_accuracy(AccuracyMetric(
            system_id="CAL-AI-003",
            inference_name="churn_probability",
            group=group,
            precision=f1 + 0.02,
            recall=f1 - 0.02,
            f1=f1,
            sample_size=50000,
        ))

    # Check fairness
    fairness = registry.check_fairness("CAL-AI-003", "churn_probability")
    print("=== Fairness Report ===")
    print(json.dumps(fairness, indent=2))

    # Process access request
    access_response = registry.process_access_request("CUST-123456")
    print("\n=== Art. 15 Access Response ===")
    print(json.dumps(access_response, indent=2))

    # Compliance report
    report = registry.compliance_report()
    print("\n=== Compliance Report ===")
    print(json.dumps(report, indent=2))
