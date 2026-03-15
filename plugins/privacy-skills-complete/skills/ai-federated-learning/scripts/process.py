#!/usr/bin/env python3
"""
Federated Learning GDPR Compliance Assessment Engine

Evaluates federated learning architecture configurations for GDPR
compliance, privacy guarantees, and recommends appropriate privacy
measures.
"""

import json
import datetime
import math
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class FLPattern(Enum):
    CROSS_DEVICE = "Cross-Device FL"
    CROSS_SILO = "Cross-Silo FL"
    VERTICAL = "Vertical FL"


class AggregationProtocol(Enum):
    PLAINTEXT = "Plaintext Aggregation (no protection)"
    SECURE_AGGREGATION = "Masking-Based Secure Aggregation"
    HOMOMORPHIC = "Homomorphic Encryption"
    TEE = "Trusted Execution Environment"


class DPType(Enum):
    NONE = "No Differential Privacy"
    LOCAL = "Local Differential Privacy"
    CENTRAL = "Central Differential Privacy"


class PrivacyLevel(Enum):
    STRONG = "Strong (epsilon <= 1)"
    MODERATE = "Moderate (epsilon 1-8)"
    BASIC = "Basic (epsilon 8-16)"
    WEAK = "Weak (epsilon > 16)"
    NONE = "No DP guarantee"


class ComplianceLevel(Enum):
    FULLY_COMPLIANT = "Fully Compliant"
    PARTIALLY_COMPLIANT = "Partially Compliant"
    NON_COMPLIANT = "Non-Compliant"


class ControllerRole(Enum):
    INDEPENDENT_CONTROLLER = "Independent Controller"
    JOINT_CONTROLLER = "Joint Controller"
    PROCESSOR = "Processor"


@dataclass
class FLConfiguration:
    name: str
    pattern: FLPattern
    num_participants: int
    data_sensitivity: str  # "general", "special_category", "highly_sensitive"
    aggregation_protocol: AggregationProtocol
    dp_type: DPType
    dp_epsilon: Optional[float] = None
    dp_delta: Optional[float] = None
    clip_norm: Optional[float] = None
    training_rounds: int = 100
    participants_per_round: int = 10
    total_data_size: int = 0
    cross_border: bool = False
    aggregator_trusted: bool = False
    joint_controller_agreement: bool = False
    dpa_in_place: bool = False
    privacy_notice_updated: bool = False
    dpia_conducted: bool = False


@dataclass
class PrivacyAssessment:
    configuration: FLConfiguration
    privacy_level: PrivacyLevel
    aggregation_secure: bool
    gradient_leakage_risk: str
    model_memorization_risk: str
    transfer_risk: str
    controller_determination: list[dict]
    compliance_level: ComplianceLevel
    issues: list[str]
    recommendations: list[str]


def assess_privacy_level(config: FLConfiguration) -> PrivacyLevel:
    if config.dp_type == DPType.NONE:
        return PrivacyLevel.NONE
    if config.dp_epsilon is None:
        return PrivacyLevel.NONE
    if config.dp_epsilon <= 1:
        return PrivacyLevel.STRONG
    elif config.dp_epsilon <= 8:
        return PrivacyLevel.MODERATE
    elif config.dp_epsilon <= 16:
        return PrivacyLevel.BASIC
    else:
        return PrivacyLevel.WEAK


def assess_gradient_leakage(config: FLConfiguration) -> tuple[str, list[str]]:
    issues = []

    if config.aggregation_protocol == AggregationProtocol.PLAINTEXT:
        risk = "high"
        issues.append(
            "Plaintext aggregation — aggregator can see individual gradient updates, enabling reconstruction attacks"
        )
        issues.append("Gradient leakage research (Zhu et al. 2019) shows pixel-perfect reconstruction from plaintext gradients")
    elif config.aggregation_protocol in [AggregationProtocol.SECURE_AGGREGATION, AggregationProtocol.HOMOMORPHIC]:
        if config.dp_type != DPType.NONE:
            risk = "low"
        else:
            risk = "medium"
            issues.append("Secure aggregation protects individual updates but model may still memorize — add DP for stronger guarantee")
    elif config.aggregation_protocol == AggregationProtocol.TEE:
        risk = "low" if config.dp_type != DPType.NONE else "medium"
        if risk == "medium":
            issues.append("TEE protects updates in transit and aggregation but does not prevent model memorization")
    else:
        risk = "high"
        issues.append("Unknown aggregation protocol — cannot assess gradient leakage risk")

    return risk, issues


def assess_transfer_risk(config: FLConfiguration) -> tuple[str, list[str]]:
    issues = []

    if not config.cross_border:
        return "not_applicable", []

    if config.aggregation_protocol in [AggregationProtocol.SECURE_AGGREGATION, AggregationProtocol.HOMOMORPHIC]:
        if config.dp_type != DPType.NONE:
            risk = "low"
            issues.append(
                "With secure aggregation + DP, model updates may not constitute personal data transfer — document assessment"
            )
        else:
            risk = "medium"
            issues.append("Secure aggregation without DP — model updates may still constitute personal data requiring transfer safeguards")
    elif config.aggregation_protocol == AggregationProtocol.PLAINTEXT:
        risk = "high"
        issues.append("Plaintext gradient transfer across borders constitutes personal data transfer — Chapter V safeguards required")
    else:
        risk = "medium"
        issues.append("Assess whether model updates constitute personal data transfer under applicable DPA guidance")

    return risk, issues


def determine_controller_roles(config: FLConfiguration) -> list[dict]:
    roles = []

    if config.pattern == FLPattern.CROSS_DEVICE:
        roles.append({
            "entity": "Platform operator (aggregator)",
            "role": ControllerRole.INDEPENDENT_CONTROLLER.value,
            "justification": "Determines purpose and means of FL training; participants are data subjects",
        })
    elif config.pattern == FLPattern.CROSS_SILO:
        roles.append({
            "entity": "Each participating organisation",
            "role": ControllerRole.JOINT_CONTROLLER.value,
            "justification": "Jointly determine purpose of training; each controls local data processing",
        })
        roles.append({
            "entity": "Aggregator",
            "role": ControllerRole.PROCESSOR.value if config.aggregator_trusted else ControllerRole.JOINT_CONTROLLER.value,
            "justification": "Aggregator acts on joint controller instructions" if config.aggregator_trusted else "Aggregator has discretion over aggregation method",
        })
    elif config.pattern == FLPattern.VERTICAL:
        roles.append({
            "entity": "All participating organisations",
            "role": ControllerRole.JOINT_CONTROLLER.value,
            "justification": "Jointly processing overlapping data subjects' different features for common training purpose",
        })

    return roles


def run_assessment(config: FLConfiguration) -> PrivacyAssessment:
    issues = []
    recommendations = []

    privacy_level = assess_privacy_level(config)
    aggregation_secure = config.aggregation_protocol != AggregationProtocol.PLAINTEXT

    gradient_risk, gradient_issues = assess_gradient_leakage(config)
    issues.extend(gradient_issues)

    memorization_risk = "low" if privacy_level in [PrivacyLevel.STRONG, PrivacyLevel.MODERATE] else "medium"
    if privacy_level == PrivacyLevel.NONE:
        memorization_risk = "high"
        issues.append("No differential privacy — model memorization of individual records is a significant risk")

    transfer_risk, transfer_issues = assess_transfer_risk(config)
    issues.extend(transfer_issues)

    controller_roles = determine_controller_roles(config)

    if config.pattern in [FLPattern.CROSS_SILO, FLPattern.VERTICAL]:
        if not config.joint_controller_agreement:
            issues.append("Joint controller agreement (Art. 26) not in place")
            recommendations.append("Establish Art. 26 joint controller agreement defining responsibilities")
        if not config.dpa_in_place and any(r["role"] == ControllerRole.PROCESSOR.value for r in controller_roles):
            issues.append("Data processing agreement (Art. 28) not in place for processor")
            recommendations.append("Execute Art. 28 DPA with aggregator/processor")

    if not config.privacy_notice_updated:
        issues.append("Privacy notice not updated to cover federated learning participation")
        recommendations.append("Update privacy notices to inform data subjects about FL processing per Arts. 13-14")

    if not config.dpia_conducted:
        issues.append("DPIA not conducted for federated learning processing")
        recommendations.append("Conduct AI DPIA covering FL architecture, gradient leakage, and memorization risks")

    if config.aggregation_protocol == AggregationProtocol.PLAINTEXT:
        recommendations.append("Upgrade to secure aggregation — plaintext gradient transfer exposes individual updates")

    if config.dp_type == DPType.NONE:
        recommendations.append("Implement differential privacy — FL without DP does not prevent model memorization")

    if config.dp_type == DPType.LOCAL and config.dp_epsilon and config.dp_epsilon > 8:
        recommendations.append(f"Current local DP epsilon ({config.dp_epsilon}) is high — consider tightening for {config.data_sensitivity} data")

    if config.data_sensitivity == "special_category" and privacy_level not in [PrivacyLevel.STRONG]:
        recommendations.append("Special category data requires strong DP (epsilon <= 1) — current privacy level insufficient")

    critical_issues = sum(1 for i in issues if "not in place" in i or "not conducted" in i or "not updated" in i)
    if critical_issues > 2:
        compliance = ComplianceLevel.NON_COMPLIANT
    elif critical_issues > 0 or gradient_risk == "high":
        compliance = ComplianceLevel.PARTIALLY_COMPLIANT
    else:
        compliance = ComplianceLevel.FULLY_COMPLIANT

    return PrivacyAssessment(
        configuration=config,
        privacy_level=privacy_level,
        aggregation_secure=aggregation_secure,
        gradient_leakage_risk=gradient_risk,
        model_memorization_risk=memorization_risk,
        transfer_risk=transfer_risk,
        controller_determination=controller_roles,
        compliance_level=compliance,
        issues=issues,
        recommendations=recommendations,
    )


def format_report(assessment: PrivacyAssessment) -> str:
    lines = []
    today = datetime.date.today().isoformat()
    lines.append(f"{'='*80}")
    lines.append("FEDERATED LEARNING GDPR COMPLIANCE ASSESSMENT")
    lines.append(f"Configuration: {assessment.configuration.name}")
    lines.append(f"Date: {today}")
    lines.append(f"{'='*80}")

    lines.append(f"\n## ARCHITECTURE")
    lines.append(f"Pattern: {assessment.configuration.pattern.value}")
    lines.append(f"Participants: {assessment.configuration.num_participants}")
    lines.append(f"Aggregation: {assessment.configuration.aggregation_protocol.value}")
    lines.append(f"DP: {assessment.configuration.dp_type.value}")
    if assessment.configuration.dp_epsilon:
        lines.append(f"Epsilon: {assessment.configuration.dp_epsilon}")

    lines.append(f"\n## PRIVACY ASSESSMENT")
    lines.append(f"Privacy Level: {assessment.privacy_level.value}")
    lines.append(f"Secure Aggregation: {'Yes' if assessment.aggregation_secure else 'No'}")
    lines.append(f"Gradient Leakage Risk: {assessment.gradient_leakage_risk}")
    lines.append(f"Memorization Risk: {assessment.model_memorization_risk}")
    lines.append(f"Transfer Risk: {assessment.transfer_risk}")

    lines.append(f"\n## CONTROLLER DETERMINATION")
    for role in assessment.controller_determination:
        lines.append(f"  {role['entity']}: {role['role']}")
        lines.append(f"    Justification: {role['justification']}")

    lines.append(f"\n## COMPLIANCE: {assessment.compliance_level.value}")

    if assessment.issues:
        lines.append(f"\n## ISSUES ({len(assessment.issues)})")
        for issue in assessment.issues:
            lines.append(f"  - {issue}")

    if assessment.recommendations:
        lines.append(f"\n## RECOMMENDATIONS")
        for rec in assessment.recommendations:
            lines.append(f"  - {rec}")

    return "\n".join(lines)


def demo_cerebrum_ai_labs():
    config = FLConfiguration(
        name="Cerebrum AI Labs — Multi-Hospital Diagnostic Model",
        pattern=FLPattern.CROSS_SILO,
        num_participants=12,
        data_sensitivity="special_category",
        aggregation_protocol=AggregationProtocol.SECURE_AGGREGATION,
        dp_type=DPType.CENTRAL,
        dp_epsilon=4.0,
        dp_delta=1e-7,
        clip_norm=1.0,
        training_rounds=200,
        participants_per_round=8,
        total_data_size=2_000_000,
        cross_border=True,
        aggregator_trusted=True,
        joint_controller_agreement=True,
        dpa_in_place=True,
        privacy_notice_updated=False,
        dpia_conducted=False,
    )

    assessment = run_assessment(config)
    report = format_report(assessment)
    print(report)


if __name__ == "__main__":
    demo_cerebrum_ai_labs()
