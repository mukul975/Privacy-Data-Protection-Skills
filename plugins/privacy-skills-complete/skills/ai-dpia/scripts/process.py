#!/usr/bin/env python3
"""
AI DPIA Assessment Engine

Automates Data Protection Impact Assessment screening, risk scoring,
and report generation for AI/ML systems per EDPB Guidelines 04/2025
and EU AI Act requirements.
"""

import json
import datetime
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class AIActRiskLevel(Enum):
    UNACCEPTABLE = "unacceptable"
    HIGH = "high"
    LIMITED = "limited"
    MINIMAL = "minimal"


class Likelihood(Enum):
    REMOTE = 1
    POSSIBLE = 2
    LIKELY = 3
    ALMOST_CERTAIN = 4


class Severity(Enum):
    NEGLIGIBLE = 1
    LIMITED = 2
    SIGNIFICANT = 3
    MAXIMUM = 4


class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    VERY_HIGH = "Very High"


class LawfulBasis(Enum):
    CONSENT = "Art. 6(1)(a) - Consent"
    CONTRACT = "Art. 6(1)(b) - Contract"
    LEGAL_OBLIGATION = "Art. 6(1)(c) - Legal Obligation"
    VITAL_INTEREST = "Art. 6(1)(d) - Vital Interest"
    PUBLIC_INTEREST = "Art. 6(1)(e) - Public Interest"
    LEGITIMATE_INTEREST = "Art. 6(1)(f) - Legitimate Interest"


RISK_MATRIX = {
    (Likelihood.REMOTE, Severity.NEGLIGIBLE): RiskLevel.LOW,
    (Likelihood.REMOTE, Severity.LIMITED): RiskLevel.LOW,
    (Likelihood.REMOTE, Severity.SIGNIFICANT): RiskLevel.MEDIUM,
    (Likelihood.REMOTE, Severity.MAXIMUM): RiskLevel.HIGH,
    (Likelihood.POSSIBLE, Severity.NEGLIGIBLE): RiskLevel.LOW,
    (Likelihood.POSSIBLE, Severity.LIMITED): RiskLevel.MEDIUM,
    (Likelihood.POSSIBLE, Severity.SIGNIFICANT): RiskLevel.HIGH,
    (Likelihood.POSSIBLE, Severity.MAXIMUM): RiskLevel.HIGH,
    (Likelihood.LIKELY, Severity.NEGLIGIBLE): RiskLevel.MEDIUM,
    (Likelihood.LIKELY, Severity.LIMITED): RiskLevel.HIGH,
    (Likelihood.LIKELY, Severity.SIGNIFICANT): RiskLevel.HIGH,
    (Likelihood.LIKELY, Severity.MAXIMUM): RiskLevel.VERY_HIGH,
    (Likelihood.ALMOST_CERTAIN, Severity.NEGLIGIBLE): RiskLevel.MEDIUM,
    (Likelihood.ALMOST_CERTAIN, Severity.LIMITED): RiskLevel.HIGH,
    (Likelihood.ALMOST_CERTAIN, Severity.SIGNIFICANT): RiskLevel.VERY_HIGH,
    (Likelihood.ALMOST_CERTAIN, Severity.MAXIMUM): RiskLevel.VERY_HIGH,
}

ANNEX_III_CATEGORIES = [
    "biometric_identification",
    "critical_infrastructure",
    "education_vocational",
    "employment_worker_management",
    "essential_services_access",
    "law_enforcement",
    "migration_border_control",
    "administration_of_justice",
]

WP248_CRITERIA = [
    "evaluation_scoring",
    "automated_decision_legal_effect",
    "systematic_monitoring",
    "sensitive_data",
    "large_scale",
    "matching_combining_datasets",
    "vulnerable_data_subjects",
    "innovative_technology",
    "preventing_exercise_of_rights",
]

AI_RISK_CATEGORIES = [
    {
        "id": "training_data_extraction",
        "name": "Training Data Extraction",
        "description": "Adversary extracts verbatim training data from the model",
        "default_likelihood": Likelihood.POSSIBLE,
        "default_severity": Severity.SIGNIFICANT,
    },
    {
        "id": "membership_inference",
        "name": "Membership Inference",
        "description": "Adversary determines if specific data was in the training set",
        "default_likelihood": Likelihood.LIKELY,
        "default_severity": Severity.LIMITED,
    },
    {
        "id": "model_inversion",
        "name": "Model Inversion",
        "description": "Adversary reconstructs input features from model outputs",
        "default_likelihood": Likelihood.POSSIBLE,
        "default_severity": Severity.SIGNIFICANT,
    },
    {
        "id": "attribute_inference",
        "name": "Attribute Inference",
        "description": "Model reveals sensitive attributes not provided as input",
        "default_likelihood": Likelihood.LIKELY,
        "default_severity": Severity.SIGNIFICANT,
    },
    {
        "id": "bias_amplification",
        "name": "Bias Amplification",
        "description": "Model amplifies biases producing discriminatory outcomes",
        "default_likelihood": Likelihood.LIKELY,
        "default_severity": Severity.MAXIMUM,
    },
    {
        "id": "concept_drift_discrimination",
        "name": "Concept Drift Discrimination",
        "description": "Model performance degrades unequally across demographic groups",
        "default_likelihood": Likelihood.POSSIBLE,
        "default_severity": Severity.SIGNIFICANT,
    },
    {
        "id": "reidentification_via_output",
        "name": "Re-identification via Output",
        "description": "Model outputs enable linking back to specific data subjects",
        "default_likelihood": Likelihood.POSSIBLE,
        "default_severity": Severity.SIGNIFICANT,
    },
    {
        "id": "automated_decision_errors",
        "name": "Automated Decision Errors",
        "description": "Incorrect AI decisions causing material harm",
        "default_likelihood": Likelihood.LIKELY,
        "default_severity": Severity.SIGNIFICANT,
    },
]


@dataclass
class TrainingDataSource:
    name: str
    source_type: str  # first_party, third_party, public_dataset, web_scraped, user_contributed
    data_categories: list[str]
    contains_special_category: bool
    special_category_types: list[str] = field(default_factory=list)
    lawful_basis: Optional[LawfulBasis] = None
    art9_condition: Optional[str] = None
    record_count: int = 0
    geographic_scope: str = ""
    consent_covers_ai_training: Optional[bool] = None
    compatibility_assessed: bool = False
    notes: str = ""


@dataclass
class AISystemProfile:
    system_name: str
    system_description: str
    model_type: str  # e.g., "transformer", "cnn", "ensemble", "decision_tree"
    model_parameters: int = 0
    training_data_sources: list[TrainingDataSource] = field(default_factory=list)
    annex_iii_category: Optional[str] = None
    produces_legal_effects: bool = False
    processes_special_category: bool = False
    performs_surveillance: bool = False
    uses_foundation_model: bool = False
    infers_sensitive_attributes: bool = False
    wp248_criteria_met: list[str] = field(default_factory=list)
    target_data_subjects: str = ""
    deployment_jurisdiction: str = "EU"
    human_oversight_level: str = ""  # none, nominal, meaningful, full


@dataclass
class RiskEntry:
    risk_id: str
    category: str
    description: str
    likelihood: Likelihood
    severity: Severity
    inherent_risk: RiskLevel
    mitigation_measures: list[str] = field(default_factory=list)
    residual_likelihood: Optional[Likelihood] = None
    residual_severity: Optional[Severity] = None
    residual_risk: Optional[RiskLevel] = None


@dataclass
class AIDPIAReport:
    reference_number: str
    system_profile: AISystemProfile
    dpia_required: bool
    dpia_triggers: list[str]
    ai_act_risk_level: AIActRiskLevel
    training_data_assessment: list[dict]
    risk_register: list[RiskEntry]
    prior_consultation_required: bool
    overall_residual_risk: RiskLevel
    human_oversight_assessment: dict
    recommendations: list[str]
    assessment_date: str
    next_review_date: str


def calculate_risk_level(likelihood: Likelihood, severity: Severity) -> RiskLevel:
    return RISK_MATRIX[(likelihood, severity)]


def screen_ai_system(profile: AISystemProfile) -> tuple[bool, list[str]]:
    triggers = []

    if profile.annex_iii_category and profile.annex_iii_category in ANNEX_III_CATEGORIES:
        triggers.append(
            f"AI Act Annex III high-risk category: {profile.annex_iii_category}"
        )

    if profile.produces_legal_effects:
        triggers.append(
            "Art. 35(3)(a): Automated decisions with legal or significant effects"
        )

    if profile.processes_special_category:
        triggers.append(
            "Art. 35(3)(b): Large-scale processing of special category data"
        )

    if profile.performs_surveillance:
        triggers.append(
            "Art. 35(3)(c): Systematic monitoring of publicly accessible area"
        )

    if profile.uses_foundation_model:
        triggers.append(
            "EDPB Guidelines 04/2025: Foundation model processing personal data"
        )

    if profile.infers_sensitive_attributes:
        triggers.append(
            "EDPB Guidelines 04/2025: Inference of sensitive attributes from non-sensitive inputs"
        )

    wp248_count = len(profile.wp248_criteria_met)
    if wp248_count >= 2:
        triggers.append(
            f"WP248rev.01: {wp248_count} criteria met ({', '.join(profile.wp248_criteria_met)})"
        )

    dpia_required = len(triggers) > 0
    return dpia_required, triggers


def classify_ai_act_risk(profile: AISystemProfile) -> AIActRiskLevel:
    prohibited_patterns = [
        "social_scoring",
        "realtime_biometric_public",
        "emotion_recognition_workplace",
        "untargeted_facial_scraping",
    ]

    if profile.annex_iii_category and any(
        p in profile.system_description.lower() for p in prohibited_patterns
    ):
        return AIActRiskLevel.UNACCEPTABLE

    if profile.annex_iii_category and profile.annex_iii_category in ANNEX_III_CATEGORIES:
        return AIActRiskLevel.HIGH

    if profile.produces_legal_effects or profile.processes_special_category:
        return AIActRiskLevel.HIGH

    if profile.uses_foundation_model:
        return AIActRiskLevel.LIMITED

    return AIActRiskLevel.MINIMAL


def assess_training_data_lawfulness(
    source: TrainingDataSource,
) -> dict:
    assessment = {
        "source_name": source.name,
        "source_type": source.source_type,
        "lawful_basis": source.lawful_basis.value if source.lawful_basis else "NOT IDENTIFIED",
        "compliant": False,
        "issues": [],
        "recommendations": [],
    }

    if not source.lawful_basis:
        assessment["issues"].append(
            "No lawful basis identified for AI training processing"
        )
        assessment["recommendations"].append(
            "Identify and document Art. 6(1) lawful basis before using this data source"
        )
        return assessment

    if source.lawful_basis == LawfulBasis.CONSENT:
        if source.consent_covers_ai_training is False:
            assessment["issues"].append(
                "Consent does not specifically cover AI/ML training as a processing purpose"
            )
            assessment["recommendations"].append(
                "Obtain fresh consent specifying AI training as a purpose, or identify alternative lawful basis"
            )
        elif source.consent_covers_ai_training is None:
            assessment["issues"].append(
                "Consent scope for AI training has not been verified"
            )
            assessment["recommendations"].append(
                "Review original consent language to verify AI training is a specified purpose"
            )
        else:
            assessment["compliant"] = True

    elif source.lawful_basis == LawfulBasis.LEGITIMATE_INTEREST:
        if source.source_type == "web_scraped":
            assessment["issues"].append(
                "EDPB Guidelines 04/2025: Web-scraped data for AI training faces heightened scrutiny under legitimate interest"
            )
            assessment["recommendations"].append(
                "Document comprehensive three-part balancing test with specific justification for web scraping necessity"
            )
            assessment["recommendations"].append(
                "Implement maximum safeguards: differential privacy, opt-out mechanism, data subject notification"
            )
        else:
            assessment["compliant"] = True
            assessment["recommendations"].append(
                "Ensure three-part balancing test is documented and reviewed by legal counsel"
            )

    elif source.lawful_basis == LawfulBasis.CONTRACT:
        assessment["compliant"] = True
        assessment["recommendations"].append(
            "Verify that AI training is genuinely necessary for the contracted service delivery"
        )

    else:
        assessment["compliant"] = True

    if source.contains_special_category:
        if not source.art9_condition:
            assessment["compliant"] = False
            assessment["issues"].append(
                f"Special category data ({', '.join(source.special_category_types)}) present without Art. 9(2) condition"
            )
            assessment["recommendations"].append(
                "Identify Art. 9(2) condition or remove special category data from training set"
            )
        else:
            assessment["recommendations"].append(
                f"Verify Art. 9(2) condition '{source.art9_condition}' remains valid for AI training context"
            )

    if not source.compatibility_assessed and source.source_type in [
        "third_party",
        "public_dataset",
    ]:
        assessment["issues"].append(
            "Art. 6(4) compatibility assessment not completed for repurposed data"
        )
        assessment["recommendations"].append(
            "Conduct and document Art. 6(4) compatibility assessment for using this data in AI training"
        )

    return assessment


def assess_ai_risks(
    profile: AISystemProfile, dpia_ref: str
) -> list[RiskEntry]:
    risk_register = []

    for idx, risk_cat in enumerate(AI_RISK_CATEGORIES, 1):
        likelihood = risk_cat["default_likelihood"]
        severity = risk_cat["default_severity"]

        if profile.model_parameters > 1_000_000_000 and risk_cat["id"] == "training_data_extraction":
            likelihood = Likelihood.LIKELY

        if profile.processes_special_category and risk_cat["id"] in [
            "attribute_inference",
            "bias_amplification",
        ]:
            severity = Severity.MAXIMUM

        if profile.produces_legal_effects and risk_cat["id"] == "automated_decision_errors":
            severity = Severity.MAXIMUM

        if profile.human_oversight_level == "none" and risk_cat["id"] == "automated_decision_errors":
            likelihood = Likelihood.ALMOST_CERTAIN

        inherent_risk = calculate_risk_level(likelihood, severity)

        entry = RiskEntry(
            risk_id=f"{dpia_ref}-R{idx:03d}",
            category=risk_cat["name"],
            description=risk_cat["description"],
            likelihood=likelihood,
            severity=severity,
            inherent_risk=inherent_risk,
        )
        risk_register.append(entry)

    return risk_register


def recommend_mitigations(risk_register: list[RiskEntry]) -> list[RiskEntry]:
    mitigation_map = {
        "Training Data Extraction": [
            "Apply differential privacy (DP-SGD) during training with epsilon <= 8",
            "Deduplicate training data to reduce memorization",
            "Apply model distillation to compress and reduce memorization capacity",
            "Implement output perturbation to prevent verbatim extraction",
        ],
        "Membership Inference": [
            "Apply differential privacy during training",
            "Regularize model to reduce overfitting (dropout, weight decay)",
            "Restrict model output to top-k predictions with rounded confidence scores",
            "Conduct pre-deployment membership inference testing",
        ],
        "Model Inversion": [
            "Limit output granularity (coarsen confidence scores)",
            "Apply output perturbation with calibrated noise",
            "Implement rate limiting on model queries",
            "Monitor for systematic probing patterns",
        ],
        "Attribute Inference": [
            "Audit model for attribute leakage using held-out sensitive attributes",
            "Apply fairness constraints to decorrelate outputs from sensitive attributes",
            "Remove proxy features correlated with sensitive attributes where feasible",
            "Implement output filtering for sensitive attribute predictions",
        ],
        "Bias Amplification": [
            "Measure fairness metrics (demographic parity, equalized odds, calibration) pre-deployment",
            "Apply bias mitigation techniques (reweighting, resampling, adversarial debiasing)",
            "Conduct ongoing fairness monitoring post-deployment with automated alerts",
            "Establish bias incident response procedures",
        ],
        "Concept Drift Discrimination": [
            "Implement continuous monitoring of model performance across demographic groups",
            "Set automated alerts for differential performance degradation",
            "Establish regular retraining schedule with updated data",
            "Maintain performance benchmarks per subgroup",
        ],
        "Re-identification via Output": [
            "Implement k-anonymity or l-diversity checks on model outputs",
            "Apply output generalization to reduce specificity",
            "Restrict output combination that could enable re-identification",
            "Audit output uniqueness against population statistics",
        ],
        "Automated Decision Errors": [
            "Implement meaningful human oversight with override capability",
            "Establish error correction and contestation mechanisms for data subjects",
            "Monitor decision accuracy and false positive/negative rates by subgroup",
            "Define and enforce confidence thresholds below which human review is mandatory",
        ],
    }

    for entry in risk_register:
        if entry.category in mitigation_map:
            entry.mitigation_measures = mitigation_map[entry.category]

            if entry.inherent_risk in [RiskLevel.HIGH, RiskLevel.VERY_HIGH]:
                entry.residual_likelihood = Likelihood(max(1, entry.likelihood.value - 1))
                entry.residual_severity = entry.severity
            else:
                entry.residual_likelihood = entry.likelihood
                entry.residual_severity = Severity(max(1, entry.severity.value - 1))

            entry.residual_risk = calculate_risk_level(
                entry.residual_likelihood, entry.residual_severity
            )

    return risk_register


def assess_human_oversight(profile: AISystemProfile) -> dict:
    assessment = {
        "oversight_level": profile.human_oversight_level,
        "art22_applicable": profile.produces_legal_effects
        and profile.human_oversight_level in ["none", "nominal"],
        "ai_act_art14_applicable": profile.annex_iii_category in ANNEX_III_CATEGORIES
        if profile.annex_iii_category
        else False,
        "findings": [],
        "recommendations": [],
    }

    if profile.human_oversight_level == "none":
        assessment["findings"].append(
            "No human oversight in decision pipeline — Art. 22(1) likely triggered"
        )
        assessment["recommendations"].append(
            "Implement meaningful human intervention before final decision"
        )
        assessment["recommendations"].append(
            "If Art. 22(2) exception relied upon, document specific basis and implement Art. 22(3) safeguards"
        )

    elif profile.human_oversight_level == "nominal":
        assessment["findings"].append(
            "Nominal human oversight may not constitute meaningful intervention per EDPB Guidelines 06/2020"
        )
        assessment["recommendations"].append(
            "Ensure reviewer has competence, time, authority, and genuine ability to override AI"
        )
        assessment["recommendations"].append(
            "Implement automation bias countermeasures (e.g., delay before confirmation, mandatory justification for agreement)"
        )

    elif profile.human_oversight_level == "meaningful":
        assessment["findings"].append(
            "Meaningful human oversight in place — verify ongoing effectiveness"
        )
        assessment["recommendations"].append(
            "Audit override rates periodically; very low override rates may indicate automation bias"
        )

    elif profile.human_oversight_level == "full":
        assessment["findings"].append(
            "Full human oversight in place — AI used as decision support only"
        )
        assessment["recommendations"].append(
            "Document that final decisions are genuinely made by the human reviewer"
        )

    return assessment


def generate_ai_dpia(profile: AISystemProfile) -> AIDPIAReport:
    today = datetime.date.today()
    dpia_ref = f"AI-DPIA-{today.year}-{today.strftime('%m%d')}"

    dpia_required, triggers = screen_ai_system(profile)
    ai_act_level = classify_ai_act_risk(profile)

    training_assessments = []
    for source in profile.training_data_sources:
        assessment = assess_training_data_lawfulness(source)
        training_assessments.append(assessment)

    risk_register = assess_ai_risks(profile, dpia_ref)
    risk_register = recommend_mitigations(risk_register)

    human_oversight = assess_human_oversight(profile)

    prior_consultation = any(
        r.residual_risk in [RiskLevel.HIGH, RiskLevel.VERY_HIGH]
        for r in risk_register
        if r.residual_risk is not None
    )

    residual_levels = [
        r.residual_risk for r in risk_register if r.residual_risk is not None
    ]
    if RiskLevel.VERY_HIGH in residual_levels:
        overall_residual = RiskLevel.VERY_HIGH
    elif RiskLevel.HIGH in residual_levels:
        overall_residual = RiskLevel.HIGH
    elif RiskLevel.MEDIUM in residual_levels:
        overall_residual = RiskLevel.MEDIUM
    else:
        overall_residual = RiskLevel.LOW

    recommendations = []
    if ai_act_level == AIActRiskLevel.UNACCEPTABLE:
        recommendations.append(
            "CRITICAL: AI system falls under prohibited practices (AI Act Art. 5). Processing must not proceed."
        )
    if ai_act_level == AIActRiskLevel.HIGH:
        recommendations.append(
            "Complete AI Act conformity assessment in parallel with DPIA."
        )
    if prior_consultation:
        recommendations.append(
            "Art. 36 prior consultation required — residual risk remains High or Very High after mitigation."
        )
    if human_oversight.get("art22_applicable"):
        recommendations.append(
            "Implement Art. 22(3) safeguards: right to human intervention, express views, contest decision."
        )

    non_compliant_sources = [
        a for a in training_assessments if not a["compliant"]
    ]
    if non_compliant_sources:
        recommendations.append(
            f"{len(non_compliant_sources)} training data source(s) have lawfulness issues requiring remediation before deployment."
        )

    review_date = today + datetime.timedelta(days=365)

    return AIDPIAReport(
        reference_number=dpia_ref,
        system_profile=profile,
        dpia_required=dpia_required,
        dpia_triggers=triggers,
        ai_act_risk_level=ai_act_level,
        training_data_assessment=training_assessments,
        risk_register=risk_register,
        prior_consultation_required=prior_consultation,
        overall_residual_risk=overall_residual,
        human_oversight_assessment=human_oversight,
        recommendations=recommendations,
        assessment_date=today.isoformat(),
        next_review_date=review_date.isoformat(),
    )


def format_report(report: AIDPIAReport) -> str:
    lines = []
    lines.append(f"{'='*80}")
    lines.append(f"AI DATA PROTECTION IMPACT ASSESSMENT")
    lines.append(f"Reference: {report.reference_number}")
    lines.append(f"Date: {report.assessment_date}")
    lines.append(f"Next Review: {report.next_review_date}")
    lines.append(f"{'='*80}")

    lines.append(f"\n## 1. AI SYSTEM PROFILE")
    lines.append(f"System: {report.system_profile.system_name}")
    lines.append(f"Description: {report.system_profile.system_description}")
    lines.append(f"Model Type: {report.system_profile.model_type}")
    lines.append(f"Parameters: {report.system_profile.model_parameters:,}")

    lines.append(f"\n## 2. DPIA SCREENING")
    lines.append(f"DPIA Required: {'YES' if report.dpia_required else 'NO'}")
    if report.dpia_triggers:
        lines.append("Triggers:")
        for trigger in report.dpia_triggers:
            lines.append(f"  - {trigger}")

    lines.append(f"\n## 3. AI ACT CLASSIFICATION")
    lines.append(f"Risk Level: {report.ai_act_risk_level.value.upper()}")

    lines.append(f"\n## 4. TRAINING DATA LAWFULNESS")
    for assessment in report.training_data_assessment:
        status = "COMPLIANT" if assessment["compliant"] else "NON-COMPLIANT"
        lines.append(f"\n  Source: {assessment['source_name']} [{status}]")
        lines.append(f"  Type: {assessment['source_type']}")
        lines.append(f"  Lawful Basis: {assessment['lawful_basis']}")
        if assessment["issues"]:
            lines.append("  Issues:")
            for issue in assessment["issues"]:
                lines.append(f"    - {issue}")
        if assessment["recommendations"]:
            lines.append("  Recommendations:")
            for rec in assessment["recommendations"]:
                lines.append(f"    - {rec}")

    lines.append(f"\n## 5. AI RISK REGISTER")
    for risk in report.risk_register:
        lines.append(f"\n  {risk.risk_id}: {risk.category}")
        lines.append(f"  Description: {risk.description}")
        lines.append(
            f"  Inherent Risk: {risk.likelihood.name} x {risk.severity.name} = {risk.inherent_risk.value}"
        )
        if risk.mitigation_measures:
            lines.append("  Mitigations:")
            for m in risk.mitigation_measures:
                lines.append(f"    - {m}")
        if risk.residual_risk:
            lines.append(f"  Residual Risk: {risk.residual_risk.value}")

    lines.append(f"\n## 6. HUMAN OVERSIGHT ASSESSMENT")
    lines.append(f"Oversight Level: {report.human_oversight_assessment['oversight_level']}")
    lines.append(
        f"Art. 22 Applicable: {'YES' if report.human_oversight_assessment['art22_applicable'] else 'NO'}"
    )
    for finding in report.human_oversight_assessment["findings"]:
        lines.append(f"  Finding: {finding}")
    for rec in report.human_oversight_assessment["recommendations"]:
        lines.append(f"  Recommendation: {rec}")

    lines.append(f"\n## 7. OVERALL ASSESSMENT")
    lines.append(f"Overall Residual Risk: {report.overall_residual_risk.value}")
    lines.append(
        f"Prior Consultation Required: {'YES' if report.prior_consultation_required else 'NO'}"
    )

    lines.append(f"\n## 8. RECOMMENDATIONS")
    for rec in report.recommendations:
        lines.append(f"  - {rec}")

    return "\n".join(lines)


def demo_cerebrum_ai_labs():
    customer_churn_data = TrainingDataSource(
        name="Customer Transaction History",
        source_type="first_party",
        data_categories=["purchase_history", "demographics", "contact_details"],
        contains_special_category=False,
        lawful_basis=LawfulBasis.LEGITIMATE_INTEREST,
        record_count=2_500_000,
        geographic_scope="EU/EEA",
        compatibility_assessed=True,
    )

    web_scraped_reviews = TrainingDataSource(
        name="Web-Scraped Product Reviews",
        source_type="web_scraped",
        data_categories=["user_names", "review_text", "ratings"],
        contains_special_category=False,
        lawful_basis=LawfulBasis.LEGITIMATE_INTEREST,
        record_count=10_000_000,
        geographic_scope="Global",
        consent_covers_ai_training=False,
    )

    health_survey_data = TrainingDataSource(
        name="Health and Wellness Survey Responses",
        source_type="third_party",
        data_categories=["health_conditions", "medication_use", "lifestyle"],
        contains_special_category=True,
        special_category_types=["health_data"],
        lawful_basis=LawfulBasis.CONSENT,
        art9_condition="Art. 9(2)(a) - Explicit consent",
        record_count=500_000,
        geographic_scope="EU/EEA",
        consent_covers_ai_training=False,
        compatibility_assessed=False,
    )

    profile = AISystemProfile(
        system_name="Cerebrum AI Labs - Customer Wellness Predictor",
        system_description="ML system predicting customer health-related product preferences and wellness scores for personalized marketing",
        model_type="transformer",
        model_parameters=350_000_000,
        training_data_sources=[
            customer_churn_data,
            web_scraped_reviews,
            health_survey_data,
        ],
        annex_iii_category=None,
        produces_legal_effects=False,
        processes_special_category=True,
        performs_surveillance=False,
        uses_foundation_model=True,
        infers_sensitive_attributes=True,
        wp248_criteria_met=[
            "evaluation_scoring",
            "sensitive_data",
            "large_scale",
            "matching_combining_datasets",
            "innovative_technology",
        ],
        target_data_subjects="EU/EEA consumers",
        deployment_jurisdiction="EU",
        human_oversight_level="nominal",
    )

    report = generate_ai_dpia(profile)
    formatted = format_report(report)
    print(formatted)

    report_data = {
        "reference": report.reference_number,
        "dpia_required": report.dpia_required,
        "triggers_count": len(report.dpia_triggers),
        "ai_act_level": report.ai_act_risk_level.value,
        "training_sources_compliant": sum(
            1 for a in report.training_data_assessment if a["compliant"]
        ),
        "training_sources_total": len(report.training_data_assessment),
        "high_risks": sum(
            1
            for r in report.risk_register
            if r.inherent_risk in [RiskLevel.HIGH, RiskLevel.VERY_HIGH]
        ),
        "prior_consultation": report.prior_consultation_required,
        "overall_residual_risk": report.overall_residual_risk.value,
    }
    print(f"\n\nJSON Summary:\n{json.dumps(report_data, indent=2)}")


if __name__ == "__main__":
    demo_cerebrum_ai_labs()
