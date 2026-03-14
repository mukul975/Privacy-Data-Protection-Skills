#!/usr/bin/env python3
"""AI System Privacy Assessment Engine.

Implements combined GDPR DPIA and AI Act conformity assessment for AI systems,
including training data lawfulness checks, Art. 22 analysis, bias testing
framework, and NIST AI RMF MAP function integration.
"""

import json
from datetime import datetime, timedelta
from typing import Any

# ---------------------------------------------------------------------------
# AI Act Risk Classification
# ---------------------------------------------------------------------------

AI_ACT_PROHIBITED = [
    {
        "id": "P1",
        "reference": "Art. 5(1)(a)",
        "description": (
            "AI systems that deploy subliminal techniques beyond a person's "
            "consciousness to materially distort behaviour causing physical "
            "or psychological harm."
        ),
    },
    {
        "id": "P2",
        "reference": "Art. 5(1)(b)",
        "description": (
            "AI systems that exploit vulnerabilities of specific groups "
            "(age, disability, social/economic situation) to materially "
            "distort behaviour causing harm."
        ),
    },
    {
        "id": "P3",
        "reference": "Art. 5(1)(c)",
        "description": (
            "AI-based social scoring by or on behalf of public authorities "
            "leading to detrimental or unfavourable treatment."
        ),
    },
    {
        "id": "P4",
        "reference": "Art. 5(1)(d)",
        "description": (
            "Real-time remote biometric identification in publicly accessible "
            "spaces for law enforcement (with limited exceptions)."
        ),
    },
    {
        "id": "P5",
        "reference": "Art. 5(1)(e)",
        "description": (
            "Untargeted scraping of facial images from internet or CCTV "
            "for facial recognition databases."
        ),
    },
    {
        "id": "P6",
        "reference": "Art. 5(1)(f)",
        "description": (
            "Emotion recognition in workplace and educational settings "
            "(except for medical or safety reasons)."
        ),
    },
]

AI_ACT_HIGH_RISK_CATEGORIES = [
    {"id": "HR1", "annex": "Annex III(1)", "category": "Biometric identification and categorisation"},
    {"id": "HR2", "annex": "Annex III(2)", "category": "Critical infrastructure management and operation"},
    {"id": "HR3", "annex": "Annex III(3)", "category": "Education and vocational training"},
    {"id": "HR4", "annex": "Annex III(4)", "category": "Employment, worker management, self-employment access"},
    {"id": "HR5", "annex": "Annex III(5)", "category": "Essential private and public services access"},
    {"id": "HR6", "annex": "Annex III(6)", "category": "Law enforcement"},
    {"id": "HR7", "annex": "Annex III(7)", "category": "Migration, asylum, border control"},
    {"id": "HR8", "annex": "Annex III(8)", "category": "Administration of justice and democratic processes"},
]

FAIRNESS_METRICS = [
    {
        "id": "FM1",
        "name": "Demographic Parity Difference",
        "threshold": 0.10,
        "description": (
            "Difference in positive outcome rates between groups. "
            "Values closer to 0 indicate greater parity."
        ),
    },
    {
        "id": "FM2",
        "name": "Equalized Odds Difference",
        "threshold": 0.10,
        "description": (
            "Maximum difference in true positive rate and false positive "
            "rate between groups."
        ),
    },
    {
        "id": "FM3",
        "name": "Disparate Impact Ratio",
        "threshold": 0.80,
        "description": (
            "Ratio of positive outcome rate for disadvantaged group to "
            "positive outcome rate for advantaged group. Four-fifths "
            "rule: ratio below 0.80 indicates disparate impact."
        ),
    },
    {
        "id": "FM4",
        "name": "Predictive Parity Ratio",
        "threshold": 0.80,
        "description": (
            "Ratio of positive predictive value between groups. "
            "Values closer to 1.0 indicate greater parity."
        ),
    },
]


def classify_ai_system(
    prohibited_check: dict[str, bool],
    high_risk_check: dict[str, bool],
    has_transparency_obligation: bool,
) -> dict[str, Any]:
    """Classify AI system under EU AI Act risk categories.

    Args:
        prohibited_check: dict mapping prohibited practice IDs to True/False
        high_risk_check: dict mapping high-risk category IDs to True/False
        has_transparency_obligation: Whether Art. 50 transparency obligations apply

    Returns:
        AI Act classification result
    """
    matched_prohibited = [
        p for p in AI_ACT_PROHIBITED if prohibited_check.get(p["id"], False)
    ]
    if matched_prohibited:
        return {
            "risk_category": "Unacceptable",
            "can_deploy": False,
            "matched_prohibitions": matched_prohibited,
            "assessment": (
                "AI system falls within Art. 5 prohibited practices and cannot "
                "be deployed in the EU/EEA."
            ),
        }

    matched_high_risk = [
        hr for hr in AI_ACT_HIGH_RISK_CATEGORIES if high_risk_check.get(hr["id"], False)
    ]
    if matched_high_risk:
        return {
            "risk_category": "High",
            "can_deploy": True,
            "requires_conformity_assessment": True,
            "matched_categories": matched_high_risk,
            "requirements": [
                "Risk management system (Art. 9)",
                "Data governance (Art. 10)",
                "Technical documentation (Art. 11)",
                "Record-keeping (Art. 12)",
                "Transparency to deployers (Art. 13)",
                "Human oversight (Art. 14)",
                "Accuracy, robustness, cybersecurity (Art. 15)",
                "EU database registration (Art. 71)",
            ],
            "assessment": (
                "AI system classified as high-risk under Annex III. Full conformity "
                "assessment and ongoing compliance obligations apply."
            ),
        }

    if has_transparency_obligation:
        return {
            "risk_category": "Limited",
            "can_deploy": True,
            "requires_conformity_assessment": False,
            "requirements": [
                "Transparency obligation: notify users of AI interaction (Art. 50)",
            ],
            "assessment": "AI system classified as limited-risk. Art. 50 transparency obligations apply.",
        }

    return {
        "risk_category": "Minimal",
        "can_deploy": True,
        "requires_conformity_assessment": False,
        "requirements": [],
        "assessment": "AI system classified as minimal-risk. No specific AI Act obligations beyond voluntary codes.",
    }


def assess_art22_applicability(
    makes_decisions_about_individuals: bool,
    solely_automated: bool,
    legal_or_significant_effect: bool,
    exception_type: str | None = None,
) -> dict[str, Any]:
    """Assess whether GDPR Art. 22 automated decision-making applies.

    Args:
        makes_decisions_about_individuals: Whether the AI makes individual decisions
        solely_automated: Whether decisions are solely automated (no meaningful human involvement)
        legal_or_significant_effect: Whether decisions produce legal or similarly significant effects
        exception_type: Art. 22(2) exception if applicable: "contract", "law", "consent", or None

    Returns:
        Art. 22 applicability assessment
    """
    if not makes_decisions_about_individuals:
        return {
            "art22_applies": False,
            "reason": "AI system does not make decisions about individuals.",
        }

    if not solely_automated:
        return {
            "art22_applies": False,
            "reason": (
                "Decisions involve meaningful human involvement. Art. 22(1) does not "
                "apply, but Art. 13-14 transparency obligations regarding the logic "
                "of automated processing still apply."
            ),
            "human_involvement_warning": (
                "Human involvement must be genuine and meaningful. A human who simply "
                "rubber-stamps AI outputs without independent assessment does not "
                "constitute meaningful human involvement."
            ),
        }

    if not legal_or_significant_effect:
        return {
            "art22_applies": False,
            "reason": (
                "Decisions do not produce legal effects or similarly significantly "
                "affect data subjects. Art. 22(1) does not apply."
            ),
        }

    exception_map = {
        "contract": {
            "reference": "Art. 22(2)(a)",
            "description": "Necessary for entering into or performing a contract",
        },
        "law": {
            "reference": "Art. 22(2)(b)",
            "description": "Authorised by Union or Member State law with suitable safeguards",
        },
        "consent": {
            "reference": "Art. 22(2)(c)",
            "description": "Based on the data subject's explicit consent",
        },
    }

    if exception_type and exception_type in exception_map:
        return {
            "art22_applies": True,
            "exception_available": True,
            "exception": exception_map[exception_type],
            "required_safeguards": [
                "Right to obtain human intervention (Art. 22(3))",
                "Right to express point of view (Art. 22(3))",
                "Right to contest the decision (Art. 22(3))",
                "Meaningful information about the logic involved (Art. 13(2)(f))",
            ],
            "reason": (
                f"Art. 22(1) applies but exception under {exception_map[exception_type]['reference']} "
                f"is available. Art. 22(3) safeguards must be implemented."
            ),
        }

    return {
        "art22_applies": True,
        "exception_available": False,
        "reason": (
            "Art. 22(1) applies and no exception is available. Data subjects have "
            "the right not to be subject to this automated decision. The processing "
            "must be restructured to include meaningful human involvement or an "
            "Art. 22(2) exception must be established."
        ),
        "action_required": "Restructure processing or establish Art. 22(2) exception.",
    }


def assess_bias(
    group_outcomes: dict[str, dict[str, float]],
) -> dict[str, Any]:
    """Assess algorithmic bias using fairness metrics.

    Args:
        group_outcomes: dict mapping group names to outcome metrics:
            {"positive_rate": float, "true_positive_rate": float,
             "false_positive_rate": float, "positive_predictive_value": float}

    Returns:
        Bias assessment with fairness metrics and disparate impact analysis
    """
    if len(group_outcomes) < 2:
        return {"error": "At least two groups required for bias assessment."}

    groups = list(group_outcomes.keys())
    rates = {g: group_outcomes[g]["positive_rate"] for g in groups}

    max_rate_group = max(rates, key=rates.get)
    max_rate = rates[max_rate_group]

    disparate_impact = {}
    bias_detected = False
    for group, rate in rates.items():
        if group == max_rate_group:
            ratio = 1.0
        else:
            ratio = rate / max_rate if max_rate > 0 else 0.0
        di_flag = ratio < 0.80
        if di_flag:
            bias_detected = True
        disparate_impact[group] = {
            "positive_rate": round(rate, 4),
            "disparate_impact_ratio": round(ratio, 4),
            "four_fifths_rule_violated": di_flag,
        }

    demographic_parity_diff = max(rates.values()) - min(rates.values())

    tpr_values = {
        g: group_outcomes[g].get("true_positive_rate", 0.0) for g in groups
    }
    fpr_values = {
        g: group_outcomes[g].get("false_positive_rate", 0.0) for g in groups
    }
    eq_odds_tpr_diff = max(tpr_values.values()) - min(tpr_values.values())
    eq_odds_fpr_diff = max(fpr_values.values()) - min(fpr_values.values())
    equalized_odds_diff = max(eq_odds_tpr_diff, eq_odds_fpr_diff)

    return {
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "groups_assessed": groups,
        "reference_group": max_rate_group,
        "disparate_impact_analysis": disparate_impact,
        "fairness_metrics": {
            "demographic_parity_difference": round(demographic_parity_diff, 4),
            "demographic_parity_flag": demographic_parity_diff > 0.10,
            "equalized_odds_difference": round(equalized_odds_diff, 4),
            "equalized_odds_flag": equalized_odds_diff > 0.10,
        },
        "bias_detected": bias_detected,
        "recommendation": (
            "Disparate impact detected. Investigate root cause (training data "
            "imbalance, proxy variables, label bias). Implement bias mitigation "
            "and re-test before deployment."
            if bias_detected
            else "No disparate impact detected under the four-fifths rule. "
            "Continue monitoring post-deployment."
        ),
    }


def generate_ai_privacy_assessment(
    reference: str,
    org_name: str,
    ai_system_name: str,
    ai_system_description: str,
    ai_act_classification: dict[str, Any],
    art22_assessment: dict[str, Any],
    bias_assessment: dict[str, Any],
    training_data_sources: list[dict[str, str]],
    risks: list[dict[str, Any]],
) -> dict[str, Any]:
    """Generate a combined AI privacy assessment report."""

    return {
        "metadata": {
            "reference": reference,
            "organisation": org_name,
            "ai_system": ai_system_name,
            "version": "1.0",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "next_review": (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d"),
            "framework": "Combined GDPR Art. 35 DPIA + EU AI Act Conformity + NIST AI RMF",
        },
        "ai_system_description": ai_system_description,
        "ai_act_classification": ai_act_classification,
        "training_data_assessment": {
            "sources": training_data_sources,
            "total_sources": len(training_data_sources),
        },
        "art22_assessment": art22_assessment,
        "bias_assessment": bias_assessment,
        "risk_register": risks,
        "total_risks": len(risks),
        "high_risks": len([r for r in risks if r.get("level") in ("High", "Very High")]),
    }


def run_example_assessment() -> dict[str, Any]:
    """Run an example AI privacy assessment for QuantumLeap Health Technologies."""

    ai_classification = classify_ai_system(
        prohibited_check={"P1": False, "P2": False, "P3": False, "P4": False, "P5": False, "P6": False},
        high_risk_check={
            "HR1": False, "HR2": False, "HR3": False,
            "HR4": True,  # Employment — AI used for candidate screening
            "HR5": False, "HR6": False, "HR7": False, "HR8": False,
        },
        has_transparency_obligation=False,
    )

    art22 = assess_art22_applicability(
        makes_decisions_about_individuals=True,
        solely_automated=False,  # HR reviews all AI recommendations
        legal_or_significant_effect=True,
    )

    bias = assess_bias({
        "Male": {
            "positive_rate": 0.32,
            "true_positive_rate": 0.85,
            "false_positive_rate": 0.12,
            "positive_predictive_value": 0.78,
        },
        "Female": {
            "positive_rate": 0.28,
            "true_positive_rate": 0.82,
            "false_positive_rate": 0.14,
            "positive_predictive_value": 0.75,
        },
        "Non-binary": {
            "positive_rate": 0.30,
            "true_positive_rate": 0.80,
            "false_positive_rate": 0.13,
            "positive_predictive_value": 0.74,
        },
    })

    return generate_ai_privacy_assessment(
        reference="AIPA-QLH-2026-0002",
        org_name="QuantumLeap Health Technologies",
        ai_system_name="TalentMatch AI Recruitment Screening System",
        ai_system_description=(
            "TalentMatch is a machine learning system that screens job applications "
            "for QuantumLeap Health Technologies. It processes CVs, cover letters, "
            "and application form responses to generate a suitability score (0-100) "
            "and a shortlist recommendation for each candidate. HR recruiters review "
            "all AI recommendations before making interview decisions. The system "
            "processes approximately 12,000 applications per year across 180 open "
            "positions in software engineering, data science, clinical research, "
            "and regulatory affairs roles. The model was trained on 45,000 historical "
            "applications from 2019-2025 with labelled outcomes (hired/not hired)."
        ),
        ai_act_classification=ai_classification,
        art22_assessment=art22,
        bias_assessment=bias,
        training_data_sources=[
            {
                "source": "QuantumLeap HR application database (2019-2025)",
                "data_categories": "CV text, cover letter text, application form responses, interview outcomes",
                "data_subjects": "45,000 historical job applicants",
                "lawful_basis": "Art. 6(1)(b) — necessary for the recruitment contract process",
                "art6_4_compatibility": (
                    "Compatible further processing: AI training directly serves the "
                    "recruitment purpose; data subjects reasonably expect applications "
                    "to be used for recruitment process improvement."
                ),
                "special_categories": "No special category data — disability and ethnicity fields excluded from training data",
            },
        ],
        risks=[
            {
                "id": "AIPA-QLH-2026-0002-R01",
                "description": (
                    "Historical bias in training data: if past hiring decisions "
                    "reflected unconscious bias, the model may perpetuate discriminatory "
                    "patterns in shortlist recommendations."
                ),
                "likelihood": "Possible",
                "severity": "Significant",
                "level": "High",
                "mitigation": (
                    "Quarterly bias audits against protected characteristics; "
                    "adversarial debiasing applied during training; human review "
                    "of all shortlist decisions with authority to override."
                ),
            },
            {
                "id": "AIPA-QLH-2026-0002-R02",
                "description": (
                    "Proxy variable discrimination: features such as university name, "
                    "postcode, or years of experience gap may correlate with protected "
                    "characteristics (socioeconomic background, gender, disability)."
                ),
                "likelihood": "Likely",
                "severity": "Significant",
                "level": "High",
                "mitigation": (
                    "Feature importance analysis to identify proxy variables; "
                    "counterfactual fairness testing; removal of university name "
                    "from feature set; gap year analysis replaced with skills-based "
                    "assessment only."
                ),
            },
            {
                "id": "AIPA-QLH-2026-0002-R03",
                "description": (
                    "Insufficient explanation of AI recommendations: candidates "
                    "unable to understand or contest the basis for rejection."
                ),
                "likelihood": "Possible",
                "severity": "Limited",
                "level": "Medium",
                "mitigation": (
                    "SHAP (SHapley Additive exPlanations) values generated for "
                    "each recommendation; top-5 contributing factors disclosed to "
                    "HR reviewers; candidate feedback mechanism providing general "
                    "explanation of assessment criteria upon request."
                ),
            },
        ],
    )


if __name__ == "__main__":
    result = run_example_assessment()
    print(json.dumps(result, indent=2, default=str))
