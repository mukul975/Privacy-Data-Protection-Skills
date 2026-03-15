#!/usr/bin/env python3
"""Healthcare AI privacy assessment — training data governance, model privacy testing, and bias monitoring."""

import json
import os
from datetime import datetime
from typing import Any


AI_RISK_CLASSIFICATIONS = {
    "unacceptable": {
        "ai_act_ref": "Art. 5",
        "description": "Prohibited AI practices",
        "examples": ["Social scoring", "Real-time biometric identification in public spaces (with limited exceptions)"],
        "action": "Must not deploy",
    },
    "high_risk": {
        "ai_act_ref": "Art. 6 + Annex III",
        "description": "High-risk AI systems requiring conformity assessment",
        "examples": ["AI diagnostic imaging", "AI-assisted surgery planning", "AI companion diagnostics"],
        "action": "Full AI Act compliance required: risk management, data governance, transparency, human oversight",
    },
    "limited_risk": {
        "ai_act_ref": "Art. 50",
        "description": "Transparency obligations",
        "examples": ["AI chatbots for patient triage", "AI-generated health content"],
        "action": "Disclose AI interaction to users",
    },
    "minimal_risk": {
        "ai_act_ref": "N/A",
        "description": "No specific AI Act obligations",
        "examples": ["AI-powered scheduling optimization", "Supply chain AI"],
        "action": "Standard HIPAA compliance; voluntary AI ethics practices",
    },
}

PRIVACY_ATTACK_TYPES = [
    {
        "attack": "membership_inference",
        "description": "Determines if specific patient's data was in training set",
        "risk_level": "high",
        "mitigation": ["Differential privacy", "Model regularization", "Output perturbation"],
    },
    {
        "attack": "training_data_extraction",
        "description": "Extracts verbatim training data from the model",
        "risk_level": "critical",
        "mitigation": ["DP-SGD training", "Training data deduplication", "Output filtering"],
    },
    {
        "attack": "model_inversion",
        "description": "Reconstructs patient features from model outputs",
        "risk_level": "high",
        "mitigation": ["Limit output granularity", "Add noise to confidence scores", "Restrict API access"],
    },
    {
        "attack": "attribute_inference",
        "description": "Reveals sensitive attributes not provided as input",
        "risk_level": "high",
        "mitigation": ["Feature correlation analysis", "Fairness-aware training", "Output filtering"],
    },
    {
        "attack": "explanation_leakage",
        "description": "SHAP/LIME explanations reveal individual patient contributions",
        "risk_level": "medium",
        "mitigation": ["Aggregate explanations", "Synthetic examples for patient-facing explanations"],
    },
]

TRAINING_DATA_LAWFUL_BASES = {
    "tpo_treatment": {"ref": "§164.506(c)(1)", "description": "Treatment — AI directly supports patient care"},
    "tpo_operations": {"ref": "§164.506(c)(4)", "description": "Healthcare operations — quality, CDS development"},
    "research_irb_waiver": {"ref": "§164.512(i)", "description": "Research with IRB/Privacy Board waiver"},
    "research_authorization": {"ref": "§164.508", "description": "Research with individual authorization"},
    "deidentified": {"ref": "§164.514(a)", "description": "De-identified data — HIPAA does not apply"},
    "limited_dataset": {"ref": "§164.514(e)", "description": "Limited data set with DUA"},
}


def classify_healthcare_ai(
    system: dict[str, Any],
) -> dict[str, Any]:
    """Classify a healthcare AI system under relevant regulatory frameworks.

    Args:
        system: Dictionary describing the AI system.

    Returns:
        Classification results under AI Act, FDA, and HIPAA.
    """
    result = {
        "system_name": system.get("name", ""),
        "classification_date": datetime.now().isoformat(),
        "ai_act_classification": "",
        "fda_classification": "",
        "hipaa_requirements": [],
        "cures_act_cds_exempt": False,
    }

    processes_images = system.get("processes_medical_images", False)
    makes_autonomous_decisions = system.get("autonomous_decisions", False)
    is_medical_device = system.get("is_medical_device", False)

    if is_medical_device or processes_images:
        result["ai_act_classification"] = "high_risk"
    elif system.get("patient_facing"):
        result["ai_act_classification"] = "limited_risk"
    else:
        result["ai_act_classification"] = "minimal_risk"

    result["ai_act_details"] = AI_RISK_CLASSIFICATIONS.get(
        result["ai_act_classification"], {}
    )

    if processes_images or makes_autonomous_decisions:
        result["fda_classification"] = "likely_samd"
        result["cures_act_cds_exempt"] = False
    else:
        cds_criteria = [
            not processes_images,
            system.get("displays_analyzes_prints_info", False),
            system.get("provides_recommendations_to_hcp", False),
            system.get("hcp_can_review_basis", False),
        ]
        if all(cds_criteria):
            result["fda_classification"] = "cds_exempt"
            result["cures_act_cds_exempt"] = True
        else:
            result["fda_classification"] = "likely_samd"

    if system.get("processes_phi", True):
        result["hipaa_requirements"].append("Security Rule compliance for ePHI")
        result["hipaa_requirements"].append("Access controls and audit logging")
        result["hipaa_requirements"].append("BAA with AI vendor if cloud-based")
        result["hipaa_requirements"].append("Minimum necessary for input data")
        result["hipaa_requirements"].append("Include in enterprise risk analysis")

    return result


def assess_training_data_governance(
    request: dict[str, Any],
) -> dict[str, Any]:
    """Assess an AI training data request for HIPAA compliance.

    Args:
        request: Dictionary describing the training data request.

    Returns:
        Governance assessment with approval/denial recommendation.
    """
    result = {
        "request_id": request.get("request_id", ""),
        "model_name": request.get("model_name", ""),
        "assessment_date": datetime.now().isoformat(),
        "lawful_basis": None,
        "approved": False,
        "conditions": [],
        "risks": [],
    }

    basis_code = request.get("lawful_basis_code", "")
    if basis_code in TRAINING_DATA_LAWFUL_BASES:
        result["lawful_basis"] = TRAINING_DATA_LAWFUL_BASES[basis_code]
    else:
        result["conditions"].append("No valid lawful basis identified — request cannot be approved")
        return result

    if basis_code == "deidentified":
        result["approved"] = True
        result["conditions"].append("Verify de-identification meets safe harbor or expert determination")
        result["conditions"].append("Assess model memorization risk post-training")
        return result

    requested_fields = request.get("phi_fields_requested", [])
    necessary_fields = request.get("phi_fields_necessary", [])
    excess_fields = [f for f in requested_fields if f not in necessary_fields]
    if excess_fields:
        result["conditions"].append(
            f"Minimum necessary: remove {len(excess_fields)} unnecessary fields: {', '.join(excess_fields)}"
        )

    if not request.get("encrypted_storage"):
        result["risks"].append("Training data storage must be encrypted (AES-256)")
    if not request.get("access_controlled"):
        result["risks"].append("Training environment must have role-based access controls")
    if not request.get("audit_logging"):
        result["risks"].append("All data access must be audit-logged")

    if request.get("data_retention_days", 999) > 90:
        result["conditions"].append("Training data copies must be deleted within 90 days of model finalization")

    if not request.get("memorization_testing_planned"):
        result["conditions"].append("Membership inference and data extraction testing required before deployment")

    if not result["risks"]:
        result["approved"] = True
    else:
        result["approved"] = False
        result["conditions"].append("Address all security risks before approval")

    return result


def assess_model_privacy_risks(
    model: dict[str, Any],
) -> dict[str, Any]:
    """Assess privacy risks of a deployed healthcare AI model.

    Args:
        model: Dictionary describing the AI model.

    Returns:
        Privacy risk assessment with attack surface analysis.
    """
    result = {
        "model_name": model.get("name", ""),
        "assessment_date": datetime.now().isoformat(),
        "attack_surface": [],
        "overall_risk": "low",
        "recommendations": [],
    }

    model_type = model.get("model_type", "")
    training_data_size = model.get("training_data_records", 0)
    parameter_count = model.get("parameter_count", 0)
    output_type = model.get("output_type", "classification")

    for attack in PRIVACY_ATTACK_TYPES:
        risk = attack["risk_level"]

        if attack["attack"] == "training_data_extraction":
            if model_type in ("transformer", "llm", "generative") and parameter_count > 1_000_000:
                risk = "critical"
            elif training_data_size < 10000:
                risk = "high"
            else:
                risk = "medium"

        elif attack["attack"] == "membership_inference":
            if training_data_size < 10000:
                risk = "high"
            else:
                risk = "medium"

        elif attack["attack"] == "model_inversion":
            if output_type in ("confidence_scores", "embeddings"):
                risk = "high"
            else:
                risk = "medium"

        result["attack_surface"].append({
            "attack_type": attack["attack"],
            "description": attack["description"],
            "assessed_risk": risk,
            "mitigation_options": attack["mitigation"],
        })

    risk_levels = [a["assessed_risk"] for a in result["attack_surface"]]
    if "critical" in risk_levels:
        result["overall_risk"] = "critical"
    elif risk_levels.count("high") >= 2:
        result["overall_risk"] = "high"
    elif "high" in risk_levels:
        result["overall_risk"] = "medium"
    else:
        result["overall_risk"] = "low"

    if result["overall_risk"] in ("critical", "high"):
        result["recommendations"].append("Apply differential privacy during training (DP-SGD)")
        result["recommendations"].append("Conduct formal privacy attack testing before deployment")
        result["recommendations"].append("Implement output perturbation for inference API")

    if not model.get("differential_privacy_applied"):
        result["recommendations"].append("Consider differential privacy for training")
    if not model.get("memorization_tested"):
        result["recommendations"].append("Run membership inference and extraction tests")

    return result


def generate_model_card_privacy_section(
    model: dict[str, Any],
) -> dict[str, Any]:
    """Generate the privacy section of a model card.

    Args:
        model: Dictionary containing model details.

    Returns:
        Privacy section content for model card.
    """
    return {
        "model_name": model.get("name", ""),
        "privacy_section": {
            "training_data": {
                "source": model.get("training_data_source", ""),
                "lawful_basis": model.get("lawful_basis", ""),
                "deidentification_method": model.get("deidentification_method", ""),
                "patient_count_approximate": model.get("patient_count", ""),
                "date_range": model.get("training_date_range", ""),
                "geographic_scope": model.get("geographic_scope", ""),
            },
            "privacy_protections": {
                "differential_privacy": model.get("differential_privacy_applied", False),
                "dp_epsilon": model.get("dp_epsilon", "N/A"),
                "data_minimization": model.get("data_minimization_applied", False),
                "encryption": model.get("data_encrypted", False),
                "access_controls": model.get("access_controls", False),
            },
            "privacy_testing": {
                "membership_inference_tested": model.get("membership_inference_tested", False),
                "extraction_tested": model.get("extraction_tested", False),
                "inversion_tested": model.get("inversion_tested", False),
                "test_results_summary": model.get("privacy_test_summary", ""),
            },
            "deployment_privacy": {
                "phi_at_inference": model.get("phi_at_inference", []),
                "outputs_stored_in_ehr": model.get("outputs_in_ehr", False),
                "patient_notification": model.get("patient_notification", ""),
                "human_oversight": model.get("human_oversight_level", ""),
            },
        },
        "generated_date": datetime.now().isoformat(),
    }


if __name__ == "__main__":
    print("=== Healthcare AI Privacy Assessment ===\n")

    ai_system = {
        "name": "Asclepius Radiology AI - Chest X-Ray Pneumonia Detection",
        "processes_medical_images": True,
        "autonomous_decisions": False,
        "is_medical_device": True,
        "patient_facing": False,
        "displays_analyzes_prints_info": True,
        "provides_recommendations_to_hcp": True,
        "hcp_can_review_basis": True,
        "processes_phi": True,
    }
    classification = classify_healthcare_ai(ai_system)
    print(f"AI System: {classification['system_name']}")
    print(f"  AI Act: {classification['ai_act_classification']}")
    print(f"  FDA: {classification['fda_classification']}")
    print(f"  Cures Act exempt: {classification['cures_act_cds_exempt']}")
    print(f"  HIPAA requirements: {len(classification['hipaa_requirements'])}")
    print()

    model_risks = assess_model_privacy_risks({
        "name": "Chest X-Ray Pneumonia Detector v2.1",
        "model_type": "cnn",
        "training_data_records": 50000,
        "parameter_count": 25_000_000,
        "output_type": "classification",
        "differential_privacy_applied": False,
        "memorization_tested": False,
    })
    print(f"Model Privacy Risk: {model_risks['overall_risk']}")
    for attack in model_risks["attack_surface"]:
        print(f"  {attack['attack_type']}: {attack['assessed_risk']}")
    for rec in model_risks["recommendations"]:
        print(f"  Recommendation: {rec}")
