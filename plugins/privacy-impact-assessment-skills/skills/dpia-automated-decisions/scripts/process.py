"""
DPIA for Automated Decision-Making - Risk Assessment and Bias Analysis Tool

Assesses GDPR Art. 35(3)(a) DPIA requirements for automated decision-making
systems, evaluates Art. 22 compliance, and identifies bias and discrimination risks.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class ADMSystemProfile:
    """Profile of an automated decision-making system for DPIA assessment."""

    def __init__(
        self,
        system_name: str,
        purpose: str,
        decision_types: List[str],
        automation_level: str,
        data_categories: List[str],
        data_subjects_volume: int,
        special_category_data: bool = False,
        profiling: bool = False,
    ):
        self.system_name = system_name
        self.purpose = purpose
        self.decision_types = decision_types
        self.automation_level = automation_level  # fully_automated, semi_automated, human_override
        self.data_categories = data_categories
        self.data_subjects_volume = data_subjects_volume
        self.special_category_data = special_category_data
        self.profiling = profiling


class BiasMetric:
    """Result of a bias assessment for a demographic group."""

    def __init__(
        self,
        protected_attribute: str,
        group_name: str,
        decision_rate: float,
        reference_rate: float,
    ):
        self.protected_attribute = protected_attribute
        self.group_name = group_name
        self.decision_rate = decision_rate
        self.reference_rate = reference_rate
        self.disparate_impact_ratio = (
            decision_rate / reference_rate if reference_rate > 0 else 0
        )
        self.four_fifths_pass = self.disparate_impact_ratio >= 0.8

    def to_dict(self) -> Dict:
        return {
            "protected_attribute": self.protected_attribute,
            "group": self.group_name,
            "decision_rate": round(self.decision_rate, 4),
            "reference_rate": round(self.reference_rate, 4),
            "disparate_impact_ratio": round(self.disparate_impact_ratio, 4),
            "four_fifths_rule_pass": self.four_fifths_pass,
        }


def classify_art22_applicability(profile: ADMSystemProfile) -> Dict:
    """Determine whether GDPR Art. 22 applies to the ADM system."""
    solely_automated = profile.automation_level == "fully_automated"
    has_legal_effect = any(
        dt in [
            "credit_decision", "insurance_pricing", "recruitment_screening",
            "benefit_determination", "loan_approval", "tenancy_decision",
            "employment_termination", "access_to_education",
        ]
        for dt in profile.decision_types
    )
    has_significant_effect = any(
        dt in [
            "fraud_detection", "content_moderation", "service_access",
            "pricing_personalization", "risk_scoring",
        ]
        for dt in profile.decision_types
    )

    art22_applies = solely_automated and (has_legal_effect or has_significant_effect)
    art35_3a_triggered = (
        profile.profiling
        and (has_legal_effect or has_significant_effect)
        and profile.data_subjects_volume > 1000
    )

    result = {
        "system": profile.system_name,
        "solely_automated": solely_automated,
        "legal_effects": has_legal_effect,
        "significant_effects": has_significant_effect,
        "profiling_involved": profile.profiling,
        "art_22_applies": art22_applies,
        "art_35_3a_dpia_required": art35_3a_triggered or art22_applies,
        "special_category_restriction": (
            profile.special_category_data and art22_applies
        ),
    }

    if art22_applies:
        result["required_safeguards"] = [
            "Art. 22(3)(a): Right to obtain human intervention",
            "Art. 22(3)(b): Right to express point of view",
            "Art. 22(3)(c): Right to contest the decision",
        ]
        if profile.special_category_data:
            result["art_22_4_note"] = (
                "Art. 22(4): Special category data processing requires "
                "Art. 9(2)(a) explicit consent or Art. 9(2)(g) substantial "
                "public interest with suitable safeguards"
            )

    return result


def assess_bias_risk(
    decision_rates: Dict[str, Dict[str, float]],
) -> List[BiasMetric]:
    """
    Assess bias using disparate impact analysis (four-fifths rule).

    Args:
        decision_rates: Dict mapping protected attribute to dict of
            group_name -> favorable_decision_rate
            e.g. {"gender": {"male": 0.72, "female": 0.58}}
    """
    metrics = []
    for attribute, groups in decision_rates.items():
        if not groups:
            continue
        reference_rate = max(groups.values())
        for group_name, rate in groups.items():
            metric = BiasMetric(attribute, group_name, rate, reference_rate)
            metrics.append(metric)

    return sorted(metrics, key=lambda m: m.disparate_impact_ratio)


def assess_transparency_compliance(
    has_privacy_notice_adm: bool,
    has_logic_explanation: bool,
    has_significance_description: bool,
    has_consequence_description: bool,
    explanation_depth: str,
    has_contestation_process: bool,
    has_human_intervention: bool,
    response_time_days: int,
) -> Dict:
    """Assess Art. 13(2)(f)/14(2)(g) and Art. 22(3) transparency compliance."""
    issues = []
    score = 0
    max_score = 8

    checks = [
        (has_privacy_notice_adm, "Privacy notice mentions automated decision-making",
         "Add Art. 22 automated decision-making disclosure to privacy notice"),
        (has_logic_explanation, "Meaningful information about logic provided",
         "Implement logic explanation per Art. 13(2)(f) and WP251rev.01 Section IV"),
        (has_significance_description, "Significance of processing described",
         "Describe the significance of the automated processing for individuals"),
        (has_consequence_description, "Envisaged consequences described",
         "Describe the potential consequences of the automated decision"),
        (has_contestation_process, "Contestation mechanism available",
         "Implement Art. 22(3) right to contest the decision"),
        (has_human_intervention, "Human intervention mechanism available",
         "Implement Art. 22(3) right to obtain human intervention"),
        (explanation_depth in ["individual_specific", "key_factors"],
         "Explanation depth is adequate (key factors or individual-specific)",
         "Increase explanation depth beyond general system description"),
        (response_time_days <= 30, "Response to contestation within Art. 12(3) deadline",
         f"Reduce contestation response time from {response_time_days} to max 30 days"),
    ]

    for condition, description, remediation in checks:
        if condition:
            score += 1
        else:
            issues.append({"requirement": description, "remediation": remediation})

    return {
        "transparency_score": f"{score}/{max_score}",
        "compliance_percentage": round(score / max_score * 100, 1),
        "compliant": score == max_score,
        "issues": issues,
    }


def calculate_residual_risk(
    inherent_risks: List[Dict],
    mitigations: List[Dict],
) -> Dict:
    """
    Calculate residual risk after applying mitigation measures.

    Args:
        inherent_risks: List of dicts with keys: risk_id, description, likelihood (1-5), impact (1-5)
        mitigations: List of dicts with keys: risk_id, description, effectiveness (0.0-1.0)
    """
    mitigation_map = {}
    for m in mitigations:
        mitigation_map.setdefault(m["risk_id"], []).append(m)

    residual_risks = []
    for risk in inherent_risks:
        risk_id = risk["risk_id"]
        inherent_score = risk["likelihood"] * risk["impact"]

        applicable_mitigations = mitigation_map.get(risk_id, [])
        combined_effectiveness = 0.0
        for m in applicable_mitigations:
            combined_effectiveness = 1 - (1 - combined_effectiveness) * (1 - m["effectiveness"])

        residual_score = inherent_score * (1 - combined_effectiveness)

        if residual_score <= 4:
            residual_level = "low"
        elif residual_score <= 9:
            residual_level = "medium"
        elif residual_score <= 16:
            residual_level = "high"
        else:
            residual_level = "very_high"

        residual_risks.append({
            "risk_id": risk_id,
            "description": risk["description"],
            "inherent_score": inherent_score,
            "mitigation_effectiveness": round(combined_effectiveness, 2),
            "residual_score": round(residual_score, 2),
            "residual_level": residual_level,
            "mitigations_applied": len(applicable_mitigations),
        })

    overall_max = max(r["residual_score"] for r in residual_risks) if residual_risks else 0
    if overall_max <= 4:
        overall_level = "low"
    elif overall_max <= 9:
        overall_level = "medium"
    elif overall_max <= 16:
        overall_level = "high"
    else:
        overall_level = "very_high"

    prior_consultation = overall_level == "very_high"

    return {
        "assessed_at": datetime.now().isoformat(),
        "risks": sorted(residual_risks, key=lambda r: r["residual_score"], reverse=True),
        "overall_residual_level": overall_level,
        "prior_consultation_required": prior_consultation,
        "recommendation": (
            "Art. 36 prior consultation with supervisory authority required before processing"
            if prior_consultation
            else f"Processing may proceed with {overall_level} residual risk. Review schedule recommended."
        ),
    }


if __name__ == "__main__":
    # Sample assessment for Meridian Analytics Ltd credit scoring system
    profile = ADMSystemProfile(
        system_name="Meridian Credit Risk Scorer v3.2",
        purpose="Automated credit risk assessment for consumer loan applications",
        decision_types=["credit_decision", "risk_scoring"],
        automation_level="fully_automated",
        data_categories=["name", "income", "employment_history", "credit_history", "address"],
        data_subjects_volume=45000,
        special_category_data=False,
        profiling=True,
    )

    print("=" * 70)
    print("DPIA - AUTOMATED DECISION-MAKING ASSESSMENT")
    print("Meridian Analytics Ltd - Credit Risk Scorer v3.2")
    print("=" * 70)

    # Art. 22 classification
    classification = classify_art22_applicability(profile)
    print("\n--- Art. 22 Classification ---")
    print(f"  Art. 22 applies: {classification['art_22_applies']}")
    print(f"  Art. 35(3)(a) DPIA required: {classification['art_35_3a_dpia_required']}")
    if classification.get("required_safeguards"):
        print("  Required safeguards:")
        for s in classification["required_safeguards"]:
            print(f"    - {s}")

    # Bias assessment
    print("\n--- Bias Assessment (Four-Fifths Rule) ---")
    bias_results = assess_bias_risk({
        "gender": {"male": 0.72, "female": 0.61},
        "age_group": {"25-34": 0.78, "35-44": 0.75, "45-54": 0.68, "55-64": 0.52, "65+": 0.41},
        "ethnicity": {"white": 0.74, "asian": 0.71, "black": 0.58, "hispanic": 0.63},
    })
    for metric in bias_results:
        status = "PASS" if metric.four_fifths_pass else "FAIL"
        print(f"  [{status}] {metric.protected_attribute}/{metric.group_name}: "
              f"rate={metric.decision_rate:.2f}, ratio={metric.disparate_impact_ratio:.2f}")

    # Transparency assessment
    print("\n--- Transparency Compliance ---")
    transparency = assess_transparency_compliance(
        has_privacy_notice_adm=True,
        has_logic_explanation=True,
        has_significance_description=True,
        has_consequence_description=True,
        explanation_depth="key_factors",
        has_contestation_process=True,
        has_human_intervention=True,
        response_time_days=14,
    )
    print(f"  Score: {transparency['transparency_score']} ({transparency['compliance_percentage']}%)")
    if transparency["issues"]:
        for issue in transparency["issues"]:
            print(f"  Gap: {issue['requirement']}")

    # Residual risk
    print("\n--- Residual Risk Assessment ---")
    risk_result = calculate_residual_risk(
        inherent_risks=[
            {"risk_id": "R1", "description": "Age discrimination in credit decisions", "likelihood": 4, "impact": 5},
            {"risk_id": "R2", "description": "Ethnic bias from proxy variables", "likelihood": 3, "impact": 5},
            {"risk_id": "R3", "description": "Opacity of decision logic to applicants", "likelihood": 3, "impact": 3},
            {"risk_id": "R4", "description": "Feedback loop amplifying historical bias", "likelihood": 3, "impact": 4},
        ],
        mitigations=[
            {"risk_id": "R1", "description": "Age-group bias testing with four-fifths rule", "effectiveness": 0.6},
            {"risk_id": "R1", "description": "Age removed as direct feature", "effectiveness": 0.3},
            {"risk_id": "R2", "description": "Proxy variable detection and removal", "effectiveness": 0.5},
            {"risk_id": "R2", "description": "Demographic parity constraint in model training", "effectiveness": 0.4},
            {"risk_id": "R3", "description": "SHAP-based individual explanations implemented", "effectiveness": 0.7},
            {"risk_id": "R4", "description": "Training data refresh with external validation", "effectiveness": 0.5},
        ],
    )
    print(f"  Overall residual risk: {risk_result['overall_residual_level']}")
    print(f"  Prior consultation required: {risk_result['prior_consultation_required']}")
    for risk in risk_result["risks"]:
        print(f"  {risk['risk_id']}: inherent={risk['inherent_score']}, "
              f"residual={risk['residual_score']} ({risk['residual_level']})")
