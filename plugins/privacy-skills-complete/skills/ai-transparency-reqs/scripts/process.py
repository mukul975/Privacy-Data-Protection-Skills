#!/usr/bin/env python3
"""
AI Transparency Compliance Assessment Engine

Evaluates AI system transparency against GDPR Arts. 13-14 and EU AI Act
Arts. 13, 14, 50 requirements, generating compliance reports and
remediation recommendations.
"""

import json
import datetime
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class AIActClassification(Enum):
    UNACCEPTABLE = "unacceptable"
    HIGH_RISK = "high_risk"
    LIMITED = "limited"
    MINIMAL = "minimal"


class ComplianceLevel(Enum):
    FULLY_COMPLIANT = "Fully Compliant"
    PARTIALLY_COMPLIANT = "Partially Compliant"
    NON_COMPLIANT = "Non-Compliant"
    NOT_ASSESSED = "Not Assessed"


class TransparencyLayer(Enum):
    INITIAL_NOTICE = "Layer 1: Initial AI Notification"
    PRIVACY_NOTICE = "Layer 2: Privacy Notice AI Section"
    DETAILED_DOCS = "Layer 3: Detailed AI Documentation"
    INDIVIDUAL_EXPLANATION = "Layer 4: Individual Decision Explanation"


GDPR_TRANSPARENCY_REQUIREMENTS = [
    {
        "id": "gdpr_purpose",
        "article": "Art. 13(1)(c)/14(1)(c)",
        "description": "Specific AI processing purpose disclosed",
        "mandatory": True,
    },
    {
        "id": "gdpr_lawful_basis",
        "article": "Art. 13(1)(c)/14(1)(c)",
        "description": "Lawful basis for AI training and inference disclosed",
        "mandatory": True,
    },
    {
        "id": "gdpr_legitimate_interest",
        "article": "Art. 13(1)(d)/14(2)(b)",
        "description": "Legitimate interest pursued through AI processing disclosed",
        "mandatory": True,
    },
    {
        "id": "gdpr_recipients",
        "article": "Art. 13(1)(e)/14(1)(e)",
        "description": "AI infrastructure providers and data recipients disclosed",
        "mandatory": True,
    },
    {
        "id": "gdpr_transfers",
        "article": "Art. 13(1)(f)/14(1)(f)",
        "description": "AI processing jurisdictions (training/inference) disclosed",
        "mandatory": True,
    },
    {
        "id": "gdpr_retention",
        "article": "Art. 13(2)(a)/14(2)(a)",
        "description": "Training data and inference log retention periods disclosed",
        "mandatory": True,
    },
    {
        "id": "gdpr_rights",
        "article": "Art. 13(2)(b)/14(2)(c)",
        "description": "AI-specific data subject rights disclosed (explanation, contestation, human review)",
        "mandatory": True,
    },
    {
        "id": "gdpr_automated_logic",
        "article": "Art. 13(2)(f)/14(2)(g)",
        "description": "Meaningful information about AI decision logic, significance, consequences",
        "mandatory": True,
    },
    {
        "id": "gdpr_data_source",
        "article": "Art. 14(2)(f)",
        "description": "Source of training data (categories) disclosed when not collected from data subject",
        "mandatory": True,
    },
]

AI_ACT_TRANSPARENCY_REQUIREMENTS = [
    {
        "id": "aiact_interaction",
        "article": "Art. 50(1)",
        "description": "Persons informed of AI interaction",
        "applies_to": ["high_risk", "limited", "minimal"],
        "condition": "interacts_with_persons",
    },
    {
        "id": "aiact_emotion",
        "article": "Art. 50(2)",
        "description": "Persons informed of emotion recognition/biometric categorisation",
        "applies_to": ["high_risk", "limited"],
        "condition": "emotion_or_biometric",
    },
    {
        "id": "aiact_content_label",
        "article": "Art. 50(3)",
        "description": "AI-generated content labelled in machine-readable format",
        "applies_to": ["high_risk", "limited", "minimal"],
        "condition": "generates_content",
    },
    {
        "id": "aiact_public_text",
        "article": "Art. 50(4)",
        "description": "AI-generated text on public interest matters disclosed",
        "applies_to": ["high_risk", "limited", "minimal"],
        "condition": "public_interest_text",
    },
    {
        "id": "aiact_interpretability",
        "article": "Art. 13(1)",
        "description": "High-risk AI designed for output interpretability",
        "applies_to": ["high_risk"],
        "condition": "always",
    },
    {
        "id": "aiact_instructions",
        "article": "Art. 13(2)",
        "description": "Instructions for use provided to deployers",
        "applies_to": ["high_risk"],
        "condition": "always",
    },
    {
        "id": "aiact_performance",
        "article": "Art. 13(3)(b)",
        "description": "Performance metrics and limitations documented",
        "applies_to": ["high_risk"],
        "condition": "always",
    },
    {
        "id": "aiact_human_oversight",
        "article": "Art. 14",
        "description": "Human oversight design and implementation documented",
        "applies_to": ["high_risk"],
        "condition": "always",
    },
    {
        "id": "aiact_explanation_right",
        "article": "Art. 86",
        "description": "Individual explanation of AI role in decision provided on request",
        "applies_to": ["high_risk"],
        "condition": "always",
    },
]


@dataclass
class AISystemTransparencyProfile:
    system_name: str
    system_description: str
    ai_act_classification: AIActClassification
    interacts_with_persons: bool = False
    emotion_or_biometric: bool = False
    generates_content: bool = False
    public_interest_text: bool = False
    makes_automated_decisions: bool = False
    art22_applicable: bool = False
    gdpr_requirements_met: dict = field(default_factory=dict)
    ai_act_requirements_met: dict = field(default_factory=dict)
    transparency_layers_implemented: dict = field(default_factory=dict)
    model_card_available: bool = False
    explainability_tools_deployed: bool = False
    privacy_notice_updated: bool = False


@dataclass
class TransparencyGap:
    requirement_id: str
    article: str
    description: str
    framework: str  # "GDPR" or "AI Act"
    severity: str  # "critical", "major", "minor"
    remediation: str


@dataclass
class TransparencyAssessment:
    system: AISystemTransparencyProfile
    date: str
    gdpr_compliance: ComplianceLevel
    ai_act_compliance: ComplianceLevel
    overall_compliance: ComplianceLevel
    gaps: list[TransparencyGap]
    recommendations: list[str]
    score: float  # 0-100


def assess_gdpr_transparency(profile: AISystemTransparencyProfile) -> tuple[list[TransparencyGap], float]:
    gaps = []
    met = 0
    total = len(GDPR_TRANSPARENCY_REQUIREMENTS)

    for req in GDPR_TRANSPARENCY_REQUIREMENTS:
        is_met = profile.gdpr_requirements_met.get(req["id"], False)
        if is_met:
            met += 1
        else:
            severity = "critical" if req["id"] in [
                "gdpr_automated_logic", "gdpr_purpose", "gdpr_lawful_basis"
            ] else "major"

            remediation_map = {
                "gdpr_purpose": "Add specific AI processing purpose to privacy notice (not generic 'service improvement')",
                "gdpr_lawful_basis": "Disclose lawful basis for AI training and inference processing separately",
                "gdpr_legitimate_interest": "Disclose the specific legitimate interest pursued through AI processing",
                "gdpr_recipients": "List AI infrastructure providers and model hosting services as recipients",
                "gdpr_transfers": "Disclose jurisdictions where AI training and inference processing occurs",
                "gdpr_retention": "Specify retention periods for training data, inference logs, and model artefacts",
                "gdpr_rights": "Add AI-specific rights: explanation of AI decisions, contestation mechanism, human review request",
                "gdpr_automated_logic": "Provide meaningful information about AI decision logic, key variables, significance, and consequences",
                "gdpr_data_source": "Disclose categories of training data sources when data not collected directly from data subjects",
            }

            gaps.append(TransparencyGap(
                requirement_id=req["id"],
                article=req["article"],
                description=req["description"],
                framework="GDPR",
                severity=severity,
                remediation=remediation_map.get(req["id"], "Address requirement per article"),
            ))

    score = (met / total) * 100 if total > 0 else 0
    return gaps, score


def assess_ai_act_transparency(profile: AISystemTransparencyProfile) -> tuple[list[TransparencyGap], float]:
    gaps = []
    applicable = 0
    met = 0

    for req in AI_ACT_TRANSPARENCY_REQUIREMENTS:
        classification = profile.ai_act_classification.value
        if classification not in req["applies_to"]:
            continue

        condition = req["condition"]
        if condition == "always":
            applies = True
        elif condition == "interacts_with_persons":
            applies = profile.interacts_with_persons
        elif condition == "emotion_or_biometric":
            applies = profile.emotion_or_biometric
        elif condition == "generates_content":
            applies = profile.generates_content
        elif condition == "public_interest_text":
            applies = profile.public_interest_text
        else:
            applies = False

        if not applies:
            continue

        applicable += 1
        is_met = profile.ai_act_requirements_met.get(req["id"], False)

        if is_met:
            met += 1
        else:
            severity = "critical" if classification == "high_risk" else "major"

            remediation_map = {
                "aiact_interaction": "Implement AI interaction notification — inform users they are interacting with AI before first exchange",
                "aiact_emotion": "Deploy prominent notice before emotion recognition/biometric processing begins",
                "aiact_content_label": "Implement machine-readable labelling (C2PA/IPTC) and visible disclosure for AI-generated content",
                "aiact_public_text": "Add disclosure that text on public interest matters is AI-generated",
                "aiact_interpretability": "Design AI system outputs for interpretability — provide confidence levels and contributing factors",
                "aiact_instructions": "Create comprehensive instructions for use covering capabilities, limitations, intended purpose, foreseeable misuse",
                "aiact_performance": "Document and disclose accuracy, robustness, and cybersecurity metrics with known limitation contexts",
                "aiact_human_oversight": "Document human oversight design — how to interpret outputs, override decisions, and stop the system",
                "aiact_explanation_right": "Implement mechanism for individuals to request explanation of AI's role in decisions affecting them",
            }

            gaps.append(TransparencyGap(
                requirement_id=req["id"],
                article=req["article"],
                description=req["description"],
                framework="AI Act",
                severity=severity,
                remediation=remediation_map.get(req["id"], "Address requirement per article"),
            ))

    score = (met / applicable) * 100 if applicable > 0 else 100
    return gaps, score


def assess_transparency_layers(profile: AISystemTransparencyProfile) -> list[str]:
    recommendations = []

    layers = {
        TransparencyLayer.INITIAL_NOTICE: profile.transparency_layers_implemented.get("layer1", False),
        TransparencyLayer.PRIVACY_NOTICE: profile.transparency_layers_implemented.get("layer2", False),
        TransparencyLayer.DETAILED_DOCS: profile.transparency_layers_implemented.get("layer3", False),
        TransparencyLayer.INDIVIDUAL_EXPLANATION: profile.transparency_layers_implemented.get("layer4", False),
    }

    if not layers[TransparencyLayer.INITIAL_NOTICE]:
        recommendations.append(
            "Implement Layer 1 notification: short AI disclosure at point of interaction"
        )

    if not layers[TransparencyLayer.PRIVACY_NOTICE]:
        recommendations.append(
            "Add Layer 2 AI section to privacy notice with purpose, logic, rights, retention"
        )

    if not layers[TransparencyLayer.DETAILED_DOCS]:
        recommendations.append(
            "Create Layer 3 detailed documentation: model card, training data description, fairness metrics"
        )

    if not layers[TransparencyLayer.INDIVIDUAL_EXPLANATION] and profile.art22_applicable:
        recommendations.append(
            "Implement Layer 4 individual explanation mechanism for Art. 22 automated decisions"
        )

    if not profile.model_card_available:
        recommendations.append(
            "Generate and maintain a model card for the deployed AI model"
        )

    if not profile.explainability_tools_deployed and profile.makes_automated_decisions:
        recommendations.append(
            "Deploy explainability tools (SHAP/LIME) for generating individual decision explanations"
        )

    return recommendations


def run_assessment(profile: AISystemTransparencyProfile) -> TransparencyAssessment:
    today = datetime.date.today().isoformat()

    gdpr_gaps, gdpr_score = assess_gdpr_transparency(profile)
    ai_act_gaps, ai_act_score = assess_ai_act_transparency(profile)
    layer_recs = assess_transparency_layers(profile)

    all_gaps = gdpr_gaps + ai_act_gaps
    overall_score = (gdpr_score * 0.5 + ai_act_score * 0.5)

    if gdpr_score >= 90:
        gdpr_compliance = ComplianceLevel.FULLY_COMPLIANT
    elif gdpr_score >= 60:
        gdpr_compliance = ComplianceLevel.PARTIALLY_COMPLIANT
    else:
        gdpr_compliance = ComplianceLevel.NON_COMPLIANT

    if ai_act_score >= 90:
        ai_act_compliance = ComplianceLevel.FULLY_COMPLIANT
    elif ai_act_score >= 60:
        ai_act_compliance = ComplianceLevel.PARTIALLY_COMPLIANT
    else:
        ai_act_compliance = ComplianceLevel.NON_COMPLIANT

    if overall_score >= 90:
        overall = ComplianceLevel.FULLY_COMPLIANT
    elif overall_score >= 60:
        overall = ComplianceLevel.PARTIALLY_COMPLIANT
    else:
        overall = ComplianceLevel.NON_COMPLIANT

    recommendations = layer_recs
    critical_gaps = [g for g in all_gaps if g.severity == "critical"]
    if critical_gaps:
        recommendations.insert(
            0,
            f"PRIORITY: {len(critical_gaps)} critical transparency gaps require immediate remediation"
        )

    return TransparencyAssessment(
        system=profile,
        date=today,
        gdpr_compliance=gdpr_compliance,
        ai_act_compliance=ai_act_compliance,
        overall_compliance=overall,
        gaps=all_gaps,
        recommendations=recommendations,
        score=overall_score,
    )


def format_report(assessment: TransparencyAssessment) -> str:
    lines = []
    lines.append(f"{'='*80}")
    lines.append("AI TRANSPARENCY COMPLIANCE ASSESSMENT")
    lines.append(f"System: {assessment.system.system_name}")
    lines.append(f"Date: {assessment.date}")
    lines.append(f"{'='*80}")

    lines.append(f"\n## COMPLIANCE SUMMARY")
    lines.append(f"Overall Score: {assessment.score:.1f}%")
    lines.append(f"Overall Compliance: {assessment.overall_compliance.value}")
    lines.append(f"GDPR Transparency: {assessment.gdpr_compliance.value}")
    lines.append(f"AI Act Transparency: {assessment.ai_act_compliance.value}")
    lines.append(f"AI Act Classification: {assessment.system.ai_act_classification.value}")

    if assessment.gaps:
        lines.append(f"\n## TRANSPARENCY GAPS ({len(assessment.gaps)} found)")
        for gap in assessment.gaps:
            lines.append(f"\n  [{gap.severity.upper()}] {gap.framework} — {gap.article}")
            lines.append(f"  Requirement: {gap.description}")
            lines.append(f"  Remediation: {gap.remediation}")

    if assessment.recommendations:
        lines.append(f"\n## RECOMMENDATIONS")
        for idx, rec in enumerate(assessment.recommendations, 1):
            lines.append(f"  {idx}. {rec}")

    return "\n".join(lines)


def demo_cerebrum_ai_labs():
    profile = AISystemTransparencyProfile(
        system_name="Cerebrum AI Labs — Customer Intent Classifier",
        system_description="NLP model classifying customer support intents for automated routing and response generation",
        ai_act_classification=AIActClassification.LIMITED,
        interacts_with_persons=True,
        generates_content=True,
        makes_automated_decisions=True,
        art22_applicable=False,
        gdpr_requirements_met={
            "gdpr_purpose": True,
            "gdpr_lawful_basis": True,
            "gdpr_legitimate_interest": True,
            "gdpr_recipients": False,
            "gdpr_transfers": False,
            "gdpr_retention": False,
            "gdpr_rights": False,
            "gdpr_automated_logic": False,
            "gdpr_data_source": True,
        },
        ai_act_requirements_met={
            "aiact_interaction": True,
            "aiact_content_label": False,
        },
        transparency_layers_implemented={
            "layer1": True,
            "layer2": False,
            "layer3": False,
            "layer4": False,
        },
        model_card_available=False,
        explainability_tools_deployed=False,
        privacy_notice_updated=False,
    )

    assessment = run_assessment(profile)
    report = format_report(assessment)
    print(report)

    summary = {
        "system": assessment.system.system_name,
        "score": assessment.score,
        "gdpr_compliance": assessment.gdpr_compliance.value,
        "ai_act_compliance": assessment.ai_act_compliance.value,
        "total_gaps": len(assessment.gaps),
        "critical_gaps": sum(1 for g in assessment.gaps if g.severity == "critical"),
    }
    print(f"\n\nJSON Summary:\n{json.dumps(summary, indent=2)}")


if __name__ == "__main__":
    demo_cerebrum_ai_labs()
