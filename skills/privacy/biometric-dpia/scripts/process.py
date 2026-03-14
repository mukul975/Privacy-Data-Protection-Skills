#!/usr/bin/env python3
"""Biometric Processing Privacy Assessment Engine.

Implements DPIA methodology for biometric systems covering Art. 9 special
category analysis, proportionality assessment, accuracy evaluation, and
risk scoring for facial recognition, fingerprint, voice, and iris systems.
"""

import json
from datetime import datetime, timedelta
from typing import Any

BIOMETRIC_MODALITIES = {
    "facial_recognition": {
        "name": "Facial Recognition",
        "art9_applicable": True,
        "intrusiveness_score": 5,
        "ambient_capture": True,
        "description": (
            "Processing of facial images to extract geometric or texture features "
            "for identification or verification of individuals."
        ),
        "specific_risks": [
            "Ambient capture without awareness",
            "Demographic accuracy disparities (skin colour, gender, age)",
            "Mass surveillance capability in identification mode",
            "Spoofing via photographs or 3D masks",
        ],
    },
    "fingerprint": {
        "name": "Fingerprint Recognition",
        "art9_applicable": True,
        "intrusiveness_score": 3,
        "ambient_capture": False,
        "description": (
            "Processing of fingerprint ridge patterns (minutiae, pattern type) "
            "for identification or verification."
        ),
        "specific_risks": [
            "Latent fingerprint collection from surfaces",
            "Cannot be changed if compromised",
            "Reduced accuracy for certain populations (manual labourers, elderly)",
            "Hygiene concerns with contact sensors",
        ],
    },
    "iris_scan": {
        "name": "Iris Recognition",
        "art9_applicable": True,
        "intrusiveness_score": 3,
        "ambient_capture": False,
        "description": (
            "Processing of iris patterns (crypts, furrows, collarette) for "
            "highly accurate identification or verification."
        ),
        "specific_risks": [
            "Requires close-range controlled capture",
            "May reveal health conditions (iridology)",
            "High-resolution iris images can be spoofed from photographs",
        ],
    },
    "voice_recognition": {
        "name": "Voice Recognition",
        "art9_applicable": True,
        "intrusiveness_score": 3,
        "ambient_capture": True,
        "description": (
            "Processing of voice characteristics (pitch, cadence, formants) "
            "for speaker identification or verification."
        ),
        "specific_risks": [
            "Remote capture without physical presence",
            "Voice cloning and deepfake audio attacks",
            "Accuracy affected by illness, emotion, ageing",
            "May incidentally capture conversation content",
        ],
    },
    "gait_analysis": {
        "name": "Gait Analysis",
        "art9_applicable": True,
        "intrusiveness_score": 4,
        "ambient_capture": True,
        "description": (
            "Processing of walking patterns and body movement characteristics "
            "for identification at a distance."
        ),
        "specific_risks": [
            "Identification at distance without cooperation",
            "May reveal health conditions (mobility impairments)",
            "Accuracy varies with footwear, load, terrain",
            "Relatively new technology with limited accuracy benchmarks",
        ],
    },
}

PROPORTIONALITY_ALTERNATIVES = [
    {
        "id": "ALT1",
        "name": "Card/badge access control",
        "security_level": "Medium",
        "cost": "Low",
        "privacy_impact": "Low",
        "limitations": "Cards can be lost, stolen, or shared",
    },
    {
        "id": "ALT2",
        "name": "PIN/password authentication",
        "security_level": "Medium",
        "cost": "Low",
        "privacy_impact": "Low",
        "limitations": "PINs can be shared or observed; passwords can be forgotten",
    },
    {
        "id": "ALT3",
        "name": "Multi-factor (card + PIN)",
        "security_level": "High",
        "cost": "Medium",
        "privacy_impact": "Low",
        "limitations": "Two-step process; card dependency",
    },
    {
        "id": "ALT4",
        "name": "Security guard visual identification",
        "security_level": "Medium",
        "cost": "High (ongoing)",
        "privacy_impact": "Medium",
        "limitations": "Human error; scalability issues; inconsistent application",
    },
]

LIKELIHOOD_SCORES = {"remote": 1, "possible": 2, "likely": 3, "almost_certain": 4}
SEVERITY_SCORES = {"negligible": 1, "limited": 2, "significant": 3, "maximum": 4}
RISK_MATRIX = {
    (1, 1): "Low", (1, 2): "Low", (1, 3): "Medium", (1, 4): "Medium",
    (2, 1): "Low", (2, 2): "Medium", (2, 3): "High", (2, 4): "High",
    (3, 1): "Medium", (3, 2): "High", (3, 3): "High", (3, 4): "Very High",
    (4, 1): "Medium", (4, 2): "High", (4, 3): "Very High", (4, 4): "Very High",
}


def assess_biometric_necessity(
    purpose: str,
    modality: str,
    processing_mode: str,
    alternatives_considered: list[str],
    justification_for_biometric: str,
) -> dict[str, Any]:
    """Assess necessity and proportionality of biometric processing.

    Args:
        purpose: Stated purpose of biometric processing
        modality: Biometric modality key
        processing_mode: "verification" (1:1) or "identification" (1:N)
        alternatives_considered: List of alternative IDs considered (ALT1-ALT4)
        justification_for_biometric: Why biometric is necessary over alternatives

    Returns:
        Necessity and proportionality assessment
    """
    mod_info = BIOMETRIC_MODALITIES.get(modality)
    if not mod_info:
        return {"error": f"Unknown modality: {modality}"}

    considered = [
        alt for alt in PROPORTIONALITY_ALTERNATIVES
        if alt["id"] in alternatives_considered
    ]

    mode_proportionality = {
        "verification": "More proportionate — limited to enrolled individuals, 1:1 matching",
        "identification": "Less proportionate — database search, potentially unlimited subjects",
    }

    return {
        "purpose": purpose,
        "modality": mod_info["name"],
        "intrusiveness_score": mod_info["intrusiveness_score"],
        "processing_mode": processing_mode,
        "mode_assessment": mode_proportionality.get(processing_mode, "Unknown mode"),
        "ambient_capture": mod_info["ambient_capture"],
        "alternatives_considered": considered,
        "biometric_justification": justification_for_biometric,
        "proportionality_assessment": (
            "Biometric processing may be proportionate if non-biometric alternatives "
            "are genuinely insufficient for the stated purpose and the least intrusive "
            "biometric modality and mode are selected."
            if len(considered) >= 2
            else "Insufficient alternatives considered. EDPB Guidelines 3/2019 require "
            "demonstration that less intrusive alternatives were evaluated."
        ),
        "art9_exemption_required": mod_info["art9_applicable"],
    }


def assess_biometric_risks(
    modality: str,
    processing_mode: str,
    enrolled_subjects: int,
    centralised_storage: bool,
    has_liveness_detection: bool,
    has_demographic_testing: bool,
    has_fallback_mechanism: bool,
) -> dict[str, Any]:
    """Assess risks specific to biometric processing.

    Returns:
        Biometric risk assessment with risk register
    """
    mod_info = BIOMETRIC_MODALITIES.get(modality, {})
    risks = []

    # BIO-R1: Data breach
    breach_likelihood = "possible" if not centralised_storage else "likely"
    breach_severity = "maximum"  # Biometric data is always maximum severity if breached
    l, s = LIKELIHOOD_SCORES[breach_likelihood], SEVERITY_SCORES[breach_severity]
    risks.append({
        "id": "BIO-R1",
        "name": "Biometric data breach",
        "likelihood": breach_likelihood,
        "severity": breach_severity,
        "level": RISK_MATRIX[(l, s)],
        "mitigation": (
            "Decentralised template storage (on-card/on-device) preferred. "
            "Cancellable biometric templates (BioHashing). AES-256 encryption. "
            "Segregated biometric database network."
        ),
    })

    # BIO-R2: Function creep
    l, s = LIKELIHOOD_SCORES["likely"], SEVERITY_SCORES["significant"]
    risks.append({
        "id": "BIO-R2",
        "name": "Function creep beyond stated purpose",
        "likelihood": "likely",
        "severity": "significant",
        "level": RISK_MATRIX[(l, s)],
        "mitigation": (
            "Purpose limitation enforced through technical access controls. "
            "Biometric templates bound to specific application. "
            "Audit logging of all template access. Annual purpose review."
        ),
    })

    # BIO-R3: Discriminatory accuracy (especially for facial recognition)
    if modality == "facial_recognition":
        disc_likelihood = "likely" if not has_demographic_testing else "possible"
        l, s = LIKELIHOOD_SCORES[disc_likelihood], SEVERITY_SCORES["significant"]
        risks.append({
            "id": "BIO-R3",
            "name": "Discriminatory accuracy across demographic groups",
            "likelihood": disc_likelihood,
            "severity": "significant",
            "level": RISK_MATRIX[(l, s)],
            "mitigation": (
                "Demographic accuracy testing per NIST FRVT methodology. "
                "Performance thresholds set per demographic group. "
                "Quarterly re-evaluation of accuracy metrics."
            ),
        })

    # BIO-R4: False rejection
    fallback_effect = "possible" if has_fallback_mechanism else "likely"
    fallback_sev = "limited" if has_fallback_mechanism else "significant"
    l, s = LIKELIHOOD_SCORES[fallback_effect], SEVERITY_SCORES[fallback_sev]
    risks.append({
        "id": "BIO-R4",
        "name": "False rejection denying legitimate access",
        "likelihood": fallback_effect,
        "severity": fallback_sev,
        "level": RISK_MATRIX[(l, s)],
        "mitigation": (
            "Non-biometric fallback mechanism available (PIN, card, helpdesk). "
            "FRR threshold set to maximise accessibility. "
            "Accessibility assessment for disabled users."
        ),
    })

    # BIO-R5: Spoofing
    spoof_likelihood = "possible" if has_liveness_detection else "likely"
    l, s = LIKELIHOOD_SCORES[spoof_likelihood], SEVERITY_SCORES["significant"]
    risks.append({
        "id": "BIO-R5",
        "name": "Presentation attack / spoofing",
        "likelihood": spoof_likelihood,
        "severity": "significant",
        "level": RISK_MATRIX[(l, s)],
        "mitigation": (
            "ISO 30107 compliant presentation attack detection. "
            "Multi-spectral liveness detection. "
            "Regular penetration testing of biometric system."
        ),
    })

    high_risks = [r for r in risks if r["level"] in ("High", "Very High")]

    return {
        "modality": mod_info.get("name", modality),
        "processing_mode": processing_mode,
        "enrolled_subjects": enrolled_subjects,
        "centralised_storage": centralised_storage,
        "risk_register": risks,
        "total_risks": len(risks),
        "high_or_very_high": len(high_risks),
        "prior_consultation_recommended": any(
            r["level"] == "Very High" for r in risks
        ),
    }


def run_example_assessment() -> dict[str, Any]:
    """Run example biometric DPIA for QuantumLeap Health Technologies."""

    necessity = assess_biometric_necessity(
        purpose=(
            "Physical access control to the Secure Research Laboratory containing "
            "patient clinical trial data, biological samples, and experimental "
            "pharmaceutical compounds. Regulatory requirement under GxP (Good "
            "Practice) guidelines and EU Clinical Trials Regulation 536/2014 "
            "for controlled access to clinical trial materials."
        ),
        modality="fingerprint",
        processing_mode="verification",
        alternatives_considered=["ALT1", "ALT2", "ALT3"],
        justification_for_biometric=(
            "Card-based access (ALT1) was used previously but was identified as "
            "insufficient during the 2025 GxP audit: cards were shared between "
            "researchers, and three incidents of unauthorized card-based access were "
            "recorded. PIN + card (ALT3) was considered but rejected because PIN "
            "sharing was also observed. Fingerprint verification provides non-transferable "
            "authentication ensuring that only the authorized individual can access the "
            "laboratory. This is the least intrusive biometric option as it requires "
            "voluntary placement of finger on the scanner (no ambient capture) and "
            "operates in 1:1 verification mode only."
        ),
    )

    risks = assess_biometric_risks(
        modality="fingerprint",
        processing_mode="verification",
        enrolled_subjects=142,
        centralised_storage=False,
        has_liveness_detection=True,
        has_demographic_testing=True,
        has_fallback_mechanism=True,
    )

    return {
        "reference": "DPIA-QLH-2026-0008",
        "organisation": "QuantumLeap Health Technologies",
        "system": "Secure Research Laboratory Fingerprint Access Control",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "necessity_assessment": necessity,
        "risk_assessment": risks,
        "art9_exemption": {
            "exemption": "Art. 9(2)(b) — employment law",
            "national_law": "BDSG Section 26(3) — biometric processing for access control",
            "safeguards": [
                "Non-biometric fallback (card + PIN) offered without penalty",
                "Explicit information to employees about biometric processing",
                "Template stored on employee's smart card, not in centralised database",
                "Works council agreement obtained (dated 2025-11-20)",
            ],
        },
    }


if __name__ == "__main__":
    result = run_example_assessment()
    print(json.dumps(result, indent=2, default=str))
