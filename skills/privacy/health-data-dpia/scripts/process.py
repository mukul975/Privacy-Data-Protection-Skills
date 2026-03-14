#!/usr/bin/env python3
"""Health Data Processing Privacy Assessment Engine.

Implements DPIA methodology for health data including Art. 9(2) exemption
analysis, clinical trial assessment, and HIPAA-GDPR crosswalk.
"""

import json
from datetime import datetime
from typing import Any

ART_9_2_EXEMPTIONS = {
    "consent": {"ref": "Art. 9(2)(a)", "name": "Explicit consent", "conditions": ["Consent must be explicit, not implied", "Separate from treatment consent", "Freely given — not a condition of treatment"]},
    "employment": {"ref": "Art. 9(2)(b)", "name": "Employment, social security", "conditions": ["Authorised by Member State law", "Suitable safeguards in place"]},
    "vital_interests": {"ref": "Art. 9(2)(c)", "name": "Vital interests", "conditions": ["Data subject physically or legally incapable of consent", "Protection of life required"]},
    "healthcare": {"ref": "Art. 9(2)(h)", "name": "Healthcare provision", "conditions": ["Necessary for preventive/occupational medicine, diagnosis, treatment, or health system management", "Under responsibility of professional subject to medical secrecy (Art. 9(3))"]},
    "public_health": {"ref": "Art. 9(2)(i)", "name": "Public health", "conditions": ["Necessary for public health purposes", "Protecting against cross-border health threats", "EU or Member State law basis with suitable safeguards"]},
    "research": {"ref": "Art. 9(2)(j)", "name": "Scientific research", "conditions": ["Necessary for scientific research purposes", "Art. 89(1) safeguards: data minimisation, pseudonymisation where possible", "EU or Member State law basis"]},
}

HEALTH_DATA_TYPES = [
    {"id": "HD1", "category": "Direct health data", "examples": "Diagnoses, test results, prescriptions, medical images", "sensitivity": "Very High"},
    {"id": "HD2", "category": "Indirect health data", "examples": "Insurance claims, appointment records, referral letters", "sensitivity": "High"},
    {"id": "HD3", "category": "Inferred health data", "examples": "Wellness app data, fitness tracker data, sleep data", "sensitivity": "High"},
    {"id": "HD4", "category": "Genetic data", "examples": "DNA sequences, genotype data, pharmacogenomic profiles", "sensitivity": "Maximum"},
    {"id": "HD5", "category": "Mental health data", "examples": "Psychiatric assessments, therapy notes, medication records", "sensitivity": "Maximum"},
]


def assess_art9_exemption(
    exemption_type: str,
    conditions_met: dict[str, bool],
) -> dict[str, Any]:
    """Assess whether an Art. 9(2) exemption is validly relied upon."""
    exemption = ART_9_2_EXEMPTIONS.get(exemption_type)
    if not exemption:
        return {"error": f"Unknown exemption type: {exemption_type}"}

    conditions = exemption["conditions"]
    results = []
    for condition in conditions:
        met = conditions_met.get(condition, False)
        results.append({"condition": condition, "met": met})

    all_met = all(r["met"] for r in results)

    return {
        "exemption": exemption["ref"],
        "name": exemption["name"],
        "conditions_assessment": results,
        "valid": all_met,
        "assessment": (
            f"Art. 9(2) exemption {exemption['ref']} is validly relied upon."
            if all_met
            else f"Art. 9(2) exemption {exemption['ref']} cannot be relied upon — "
            f"not all conditions are met."
        ),
    }


def assess_hipaa_gdpr_gap(
    organisation_subject_to_hipaa: bool,
) -> dict[str, Any]:
    """Assess HIPAA-GDPR compliance gaps for transatlantic operations."""
    if not organisation_subject_to_hipaa:
        return {"applicable": False, "message": "HIPAA not applicable — US operations do not involve PHI."}

    gaps = [
        {
            "area": "Consent standard",
            "hipaa": "TPO exception allows processing without consent for treatment, payment, operations",
            "gdpr": "No TPO exception; Art. 9(2)(h) requires processing under professional secrecy",
            "action": "Implement GDPR-compliant consent for all EU data subjects even in TPO contexts",
        },
        {
            "area": "Breach notification timeline",
            "hipaa": "60 days from discovery",
            "gdpr": "72 hours from awareness to SA; without undue delay to data subjects",
            "action": "Align breach notification to GDPR 72-hour standard globally",
        },
        {
            "area": "Data subject rights",
            "hipaa": "Access and amendment rights",
            "gdpr": "Broader: access, rectification, erasure, restriction, portability, objection",
            "action": "Implement full GDPR rights framework for EU data subjects",
        },
        {
            "area": "De-identification vs anonymisation",
            "hipaa": "Safe Harbor (18 identifiers) or Expert Determination",
            "gdpr": "Irreversibility standard (Recital 26) — no specific identifier list",
            "action": "Assess anonymisation against GDPR standard, not just HIPAA Safe Harbor",
        },
    ]

    return {
        "applicable": True,
        "gaps": gaps,
        "total_gaps": len(gaps),
        "recommendation": "Align to GDPR standard (the more restrictive) for all processing involving EU data subjects.",
    }


def run_example() -> dict[str, Any]:
    """Run example health data DPIA for QuantumLeap Health Technologies."""
    exemption = assess_art9_exemption(
        exemption_type="research",
        conditions_met={
            "Necessary for scientific research purposes": True,
            "Art. 89(1) safeguards: data minimisation, pseudonymisation where possible": True,
            "EU or Member State law basis": True,
        },
    )

    hipaa = assess_hipaa_gdpr_gap(organisation_subject_to_hipaa=True)

    return {
        "reference": "DPIA-QLH-2026-0016",
        "organisation": "QuantumLeap Health Technologies",
        "processing": "Phase III Clinical Trial Data Processing — QT-CARDIO-301",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "art9_exemption": exemption,
        "hipaa_crosswalk": hipaa,
        "health_data_categories": [
            {"type": "Direct health data", "elements": "ECG readings, cardiac biomarkers, adverse event reports"},
            {"type": "Genetic data", "elements": "Pharmacogenomic CYP450 enzyme panel for dosing optimization"},
        ],
    }


if __name__ == "__main__":
    result = run_example()
    print(json.dumps(result, indent=2, default=str))
