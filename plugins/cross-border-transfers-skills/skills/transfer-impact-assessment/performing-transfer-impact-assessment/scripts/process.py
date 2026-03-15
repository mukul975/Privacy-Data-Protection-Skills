#!/usr/bin/env python3
"""Transfer Impact Assessment (TIA) Scoring Engine.

Implements the EDPB Recommendations 01/2020 six-step methodology and
TIA scoring rubric for evaluating international data transfers post-Schrems II.
"""

import json
from datetime import datetime, timedelta
from typing import Any

# ---------------------------------------------------------------------------
# European Essential Guarantees Assessment Factors
# ---------------------------------------------------------------------------

ESSENTIAL_GUARANTEES = [
    {
        "id": "EG1",
        "name": "Clear, Precise, and Accessible Rules",
        "weight": 0.25,
        "description": (
            "Surveillance powers must be defined by publicly available law with "
            "sufficient clarity regarding conditions, scope, and limitations."
        ),
        "scoring_guide": {
            1: "Surveillance powers defined by detailed, publicly available statute with clear limitations",
            2: "Surveillance powers defined by law but with some ambiguity in scope",
            3: "Surveillance powers defined by law but with broad discretionary scope",
            4: "Surveillance powers partly defined by law, partly by executive decree",
            5: "Surveillance powers not clearly defined by law or exercised under secret directives",
        },
    },
    {
        "id": "EG2",
        "name": "Necessity and Proportionality",
        "weight": 0.25,
        "description": (
            "Government access must be limited to what is strictly necessary and "
            "proportionate. Bulk or indiscriminate collection must have adequate "
            "safeguards and limitations."
        ),
        "scoring_guide": {
            1: "Access strictly limited to targeted individuals with judicial determination of necessity",
            2: "Access generally targeted with some bulk collection subject to safeguards",
            3: "Mix of targeted and bulk access; proportionality requirements exist but enforcement is uneven",
            4: "Broad access powers with limited proportionality safeguards",
            5: "Bulk or indiscriminate access with no meaningful proportionality requirements",
        },
    },
    {
        "id": "EG3",
        "name": "Independent Oversight",
        "weight": 0.25,
        "description": (
            "Surveillance activities must be subject to prior authorisation and "
            "ongoing oversight by a body independent from the executive branch."
        ),
        "scoring_guide": {
            1: "Judicial authorisation required for all access; independent oversight body with enforcement powers",
            2: "Judicial authorisation for most access; independent oversight with review powers",
            3: "Judicial authorisation for some access types; administrative authorisation for others",
            4: "Primarily administrative authorisation with limited independent review",
            5: "No independent oversight; self-authorisation by executive or intelligence agencies",
        },
    },
    {
        "id": "EG4",
        "name": "Effective Remedies",
        "weight": 0.25,
        "description": (
            "Data subjects, including foreign nationals, must have access to "
            "effective legal remedies before an independent and impartial body."
        ),
        "scoring_guide": {
            1: "Independent court with full review powers accessible to foreign nationals; binding remedies available",
            2: "Independent tribunal with review powers; foreign nationals have access with some limitations",
            3: "Administrative review body with limited powers; foreign national access restricted",
            4: "Review mechanism exists but with significant limitations on scope or foreign national access",
            5: "No effective remedy available to foreign nationals",
        },
    },
]

GOVERNMENT_ACCESS_FACTORS = [
    {
        "id": "GA1",
        "name": "Surveillance Legislation Scope",
        "weight": 0.25,
        "scoring_guide": {
            1: "Targeted access only, strictly necessary and proportionate",
            3: "Mix of targeted and bulk powers with proportionality limitations",
            5: "Bulk/indiscriminate access without proportionality requirements",
        },
    },
    {
        "id": "GA2",
        "name": "Independent Prior Authorisation",
        "weight": 0.20,
        "scoring_guide": {
            1: "Judicial authorisation required for all access",
            3: "Judicial for some; administrative for others",
            5: "No independent authorisation; self-authorisation",
        },
    },
    {
        "id": "GA3",
        "name": "Effective Remedies",
        "weight": 0.20,
        "scoring_guide": {
            1: "Independent court with full review, accessible to foreign nationals",
            3: "Administrative review with limited powers",
            5: "No effective remedy for foreign nationals",
        },
    },
    {
        "id": "GA4",
        "name": "Transparency and Notification",
        "weight": 0.15,
        "scoring_guide": {
            1: "Mandatory notification and public transparency reporting",
            3: "Partial transparency; notification in some cases",
            5: "No notification; limited or no transparency",
        },
    },
    {
        "id": "GA5",
        "name": "Rule of Law and Judicial Independence",
        "weight": 0.20,
        "scoring_guide": {
            1: "Strong constitutional protections; independent judiciary; CoE 108+ ratified",
            3: "Some constitutional protections; judiciary generally independent",
            5: "Weak/absent constitutional protections; executive influence over judiciary",
        },
    },
]

SUPPLEMENTARY_MEASURES_CATALOGUE = {
    "technical": [
        {
            "id": "TM1",
            "name": "End-to-end encryption with exporter-held key",
            "effectiveness": "High",
            "description": (
                "Data encrypted before transfer using keys held exclusively by the "
                "data exporter in the EEA. Data importer has no access to decryption "
                "keys and cannot provide clear text data to government authorities."
            ),
            "limitations": (
                "Only effective when processing purpose does not require importer "
                "to access data in clear text (e.g., backup, archival, transport)."
            ),
        },
        {
            "id": "TM2",
            "name": "Pseudonymisation with exporter-held mapping table",
            "effectiveness": "High",
            "description": (
                "Personal data pseudonymised before transfer. The mapping table "
                "enabling re-identification is held exclusively by the data exporter "
                "in the EEA and not transferred."
            ),
            "limitations": (
                "Only effective when the pseudonymised data cannot be re-identified "
                "by the importer using other means available to it."
            ),
        },
        {
            "id": "TM3",
            "name": "Split processing across jurisdictions",
            "effectiveness": "High",
            "description": (
                "Processing split so that no single third-country entity has access "
                "to the complete dataset. Re-assembly requires cooperation of "
                "entities in multiple jurisdictions."
            ),
            "limitations": "Operationally complex; requires careful data architecture design.",
        },
        {
            "id": "TM4",
            "name": "Transport encryption (TLS 1.3 / IPsec)",
            "effectiveness": "Low",
            "description": (
                "Data encrypted during transit between exporter and importer "
                "using state-of-the-art transport encryption."
            ),
            "limitations": (
                "Protects only against interception during transit. Does not protect "
                "against access at rest or government compulsion to the importer."
            ),
        },
        {
            "id": "TM5",
            "name": "Encryption at rest (importer-held key)",
            "effectiveness": "Low",
            "description": (
                "Data encrypted at rest in the destination country using keys "
                "held by the data importer."
            ),
            "limitations": (
                "Importer holds decryption key and can be compelled by government "
                "to provide access. Does not protect against government compulsion."
            ),
        },
    ],
    "contractual": [
        {
            "id": "CM1",
            "name": "Obligation to challenge government access",
            "effectiveness": "Medium",
            "description": (
                "Contractual obligation on the importer to use all available "
                "legal remedies to challenge government access requests that "
                "conflict with EU data protection law."
            ),
        },
        {
            "id": "CM2",
            "name": "Transparency and notification obligations",
            "effectiveness": "Medium",
            "description": (
                "Obligation to notify exporter of government access requests "
                "where legally permitted, and to publish annual transparency "
                "reports on government access volume."
            ),
        },
        {
            "id": "CM3",
            "name": "Audit rights",
            "effectiveness": "Medium",
            "description": (
                "Contractual right for the exporter to audit the importer's "
                "handling of government access requests and compliance with "
                "supplementary measures."
            ),
        },
    ],
    "organisational": [
        {
            "id": "OM1",
            "name": "Government access response procedures",
            "effectiveness": "Medium",
            "description": (
                "Documented internal policies for assessing and responding to "
                "government access requests, including escalation to legal counsel "
                "and notification to the data exporter."
            ),
        },
        {
            "id": "OM2",
            "name": "Staff training on government access handling",
            "effectiveness": "Low",
            "description": (
                "Regular training for relevant staff on procedures for handling "
                "government access requests and obligations under the SCCs."
            ),
        },
    ],
}

RISK_LEVELS = {
    (1.0, 2.0): {
        "level": "Low",
        "recommendation": (
            "Transfer may proceed with the standard transfer tool. "
            "No additional supplementary measures required beyond "
            "the transfer mechanism itself."
        ),
    },
    (2.1, 3.0): {
        "level": "Medium",
        "recommendation": (
            "Transfer may proceed with appropriate supplementary measures. "
            "Contractual and organisational measures may suffice if the "
            "specific risks are addressable contractually."
        ),
    },
    (3.1, 4.0): {
        "level": "High",
        "recommendation": (
            "Transfer may proceed only with robust technical supplementary "
            "measures such as end-to-end encryption with exporter-held key "
            "or pseudonymisation with exporter-held mapping table."
        ),
    },
    (4.1, 5.0): {
        "level": "Very High",
        "recommendation": (
            "Transfer should not proceed unless data is encrypted with "
            "exporter-held key and the importer has no access to clear "
            "text data. If processing requires clear text access, the "
            "transfer must not proceed."
        ),
    },
}


def calculate_tia_score(factor_scores: dict[str, int]) -> dict[str, Any]:
    """Calculate overall TIA government access risk score.

    Args:
        factor_scores: dict mapping factor IDs (GA1-GA5) to scores (1-5)

    Returns:
        TIA scoring result with weighted score and risk level
    """
    weighted_sum = 0.0
    factor_details = []

    for factor in GOVERNMENT_ACCESS_FACTORS:
        fid = factor["id"]
        score = factor_scores.get(fid, 3)
        if score < 1 or score > 5:
            raise ValueError(f"Score for {fid} must be between 1 and 5, got {score}")
        weighted_contribution = score * factor["weight"]
        weighted_sum += weighted_contribution
        factor_details.append({
            "factor_id": fid,
            "factor_name": factor["name"],
            "weight": factor["weight"],
            "raw_score": score,
            "weighted_score": round(weighted_contribution, 2),
        })

    risk_level = "Unknown"
    recommendation = ""
    for (low, high), info in RISK_LEVELS.items():
        if low <= round(weighted_sum, 1) <= high:
            risk_level = info["level"]
            recommendation = info["recommendation"]
            break

    return {
        "overall_weighted_score": round(weighted_sum, 2),
        "risk_level": risk_level,
        "recommendation": recommendation,
        "factor_details": factor_details,
    }


def assess_essential_guarantees(
    guarantee_scores: dict[str, int],
) -> dict[str, Any]:
    """Assess the four European Essential Guarantees per EDPB Recommendations 02/2020.

    Args:
        guarantee_scores: dict mapping guarantee IDs (EG1-EG4) to scores (1-5)

    Returns:
        Essential guarantees assessment with individual and overall scores
    """
    weighted_sum = 0.0
    guarantee_details = []

    for guarantee in ESSENTIAL_GUARANTEES:
        gid = guarantee["id"]
        score = guarantee_scores.get(gid, 3)
        if score < 1 or score > 5:
            raise ValueError(f"Score for {gid} must be between 1 and 5, got {score}")
        weighted_contribution = score * guarantee["weight"]
        weighted_sum += weighted_contribution
        guarantee_details.append({
            "guarantee_id": gid,
            "guarantee_name": guarantee["name"],
            "weight": guarantee["weight"],
            "raw_score": score,
            "weighted_score": round(weighted_contribution, 2),
            "assessment": guarantee["scoring_guide"].get(
                score, f"Score {score} — interpolated between defined levels"
            ),
        })

    meets_standard = weighted_sum <= 2.5

    return {
        "overall_score": round(weighted_sum, 2),
        "meets_essential_guarantees": meets_standard,
        "guarantee_details": guarantee_details,
        "assessment": (
            "The third country legal framework meets the European Essential "
            "Guarantees. Standard transfer tool may be sufficient."
            if meets_standard
            else "The third country legal framework does not fully meet the "
            "European Essential Guarantees. Supplementary measures are required."
        ),
    }


def recommend_supplementary_measures(
    tia_risk_level: str,
    processing_requires_clear_text: bool,
) -> dict[str, Any]:
    """Recommend supplementary measures based on TIA risk level.

    Args:
        tia_risk_level: Risk level from TIA scoring (Low, Medium, High, Very High)
        processing_requires_clear_text: Whether the importer needs clear text data access

    Returns:
        Recommended supplementary measures with feasibility assessment
    """
    recommended = []

    if tia_risk_level == "Low":
        return {
            "measures_required": False,
            "recommendation": (
                "No supplementary measures beyond the standard transfer tool are required."
            ),
            "recommended_measures": [],
        }

    if tia_risk_level == "Medium":
        recommended.extend([
            SUPPLEMENTARY_MEASURES_CATALOGUE["contractual"][0],  # CM1: Challenge obligation
            SUPPLEMENTARY_MEASURES_CATALOGUE["contractual"][1],  # CM2: Transparency
            SUPPLEMENTARY_MEASURES_CATALOGUE["contractual"][2],  # CM3: Audit rights
            SUPPLEMENTARY_MEASURES_CATALOGUE["organisational"][0],  # OM1: Procedures
        ])

    elif tia_risk_level == "High":
        if not processing_requires_clear_text:
            recommended.append(
                SUPPLEMENTARY_MEASURES_CATALOGUE["technical"][0]  # TM1: E2E encryption
            )
        else:
            recommended.append(
                SUPPLEMENTARY_MEASURES_CATALOGUE["technical"][1]  # TM2: Pseudonymisation
            )
        recommended.extend([
            SUPPLEMENTARY_MEASURES_CATALOGUE["contractual"][0],
            SUPPLEMENTARY_MEASURES_CATALOGUE["contractual"][1],
            SUPPLEMENTARY_MEASURES_CATALOGUE["contractual"][2],
            SUPPLEMENTARY_MEASURES_CATALOGUE["organisational"][0],
        ])

    elif tia_risk_level == "Very High":
        if processing_requires_clear_text:
            return {
                "measures_required": True,
                "transfer_blocked": True,
                "recommendation": (
                    "Transfer must not proceed. The processing requires clear text "
                    "data access by the importer, and no supplementary measures can "
                    "ensure essentially equivalent protection given the Very High "
                    "risk level of the destination country."
                ),
                "recommended_measures": [],
                "alternative": (
                    "Process data within the EEA using an EEA-based processor, or "
                    "restructure processing to eliminate clear text access requirement."
                ),
            }
        recommended.append(
            SUPPLEMENTARY_MEASURES_CATALOGUE["technical"][0]  # TM1: E2E encryption
        )
        recommended.extend([
            SUPPLEMENTARY_MEASURES_CATALOGUE["contractual"][0],
            SUPPLEMENTARY_MEASURES_CATALOGUE["contractual"][1],
            SUPPLEMENTARY_MEASURES_CATALOGUE["contractual"][2],
            SUPPLEMENTARY_MEASURES_CATALOGUE["organisational"][0],
            SUPPLEMENTARY_MEASURES_CATALOGUE["organisational"][1],
        ])

    return {
        "measures_required": True,
        "transfer_blocked": False,
        "recommendation": (
            f"Supplementary measures are required for {tia_risk_level} risk transfer. "
            f"The following {len(recommended)} measures are recommended."
        ),
        "recommended_measures": recommended,
    }


def generate_tia_report(
    reference: str,
    org_name: str,
    data_exporter: str,
    data_importer: str,
    importer_country: str,
    transfer_mechanism: str,
    data_categories: list[str],
    data_subjects: list[str],
    transfer_purpose: str,
    factor_scores: dict[str, int],
    guarantee_scores: dict[str, int],
    processing_requires_clear_text: bool,
) -> dict[str, Any]:
    """Generate a complete TIA report.

    Returns:
        Complete TIA report as structured data
    """
    tia_score = calculate_tia_score(factor_scores)
    eg_assessment = assess_essential_guarantees(guarantee_scores)
    measures = recommend_supplementary_measures(
        tia_score["risk_level"],
        processing_requires_clear_text,
    )

    return {
        "metadata": {
            "tia_reference": reference,
            "organisation": org_name,
            "version": "1.0",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "next_review": (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d"),
        },
        "step_1_transfer_mapping": {
            "data_exporter": data_exporter,
            "data_importer": data_importer,
            "importer_country": importer_country,
            "data_categories": data_categories,
            "data_subjects": data_subjects,
            "transfer_purpose": transfer_purpose,
        },
        "step_2_transfer_mechanism": transfer_mechanism,
        "step_3_country_assessment": {
            "government_access_score": tia_score,
            "essential_guarantees": eg_assessment,
        },
        "step_4_supplementary_measures": measures,
        "step_5_implementation": {
            "status": "Pending implementation",
            "measures_count": len(measures.get("recommended_measures", [])),
        },
        "step_6_review_schedule": {
            "next_review_date": (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d"),
            "review_triggers": [
                "New surveillance legislation in destination country",
                "Court decision affecting government access powers",
                "Government access request received by data importer",
                "Data breach involving transferred data",
                "Adequacy decision adopted or withdrawn for destination country",
            ],
        },
        "conclusion": {
            "transfer_permitted": not measures.get("transfer_blocked", False),
            "risk_level": tia_score["risk_level"],
            "conditions": tia_score["recommendation"],
        },
    }


def run_example_tia() -> dict[str, Any]:
    """Execute an example TIA for QuantumLeap Health Technologies transfer to India."""
    return generate_tia_report(
        reference="TIA-QLH-2026-0003",
        org_name="QuantumLeap Health Technologies",
        data_exporter=(
            "QuantumLeap Health Technologies GmbH, Friedrichstrasse 112, "
            "10117 Berlin, Germany"
        ),
        data_importer=(
            "QuantumLeap Health Technologies India Pvt. Ltd., "
            "Tower B, Manyata Embassy Business Park, Outer Ring Road, "
            "Bangalore 560045, Karnataka, India"
        ),
        importer_country="India",
        transfer_mechanism=(
            "Standard Contractual Clauses (Commission Implementing Decision "
            "2021/914), Module 2 (Controller-to-Processor)"
        ),
        data_categories=[
            "Employee identifiers (name, employee ID, email address)",
            "IT support ticket data (device information, error logs, user actions)",
            "Application usage metadata (timestamps, feature usage counts)",
        ],
        data_subjects=[
            "QuantumLeap Health Technologies employees in EU/EEA (2,847 employees)",
        ],
        transfer_purpose=(
            "IT helpdesk support services and application monitoring provided "
            "by the Bangalore-based IT support team during extended business hours "
            "(IST timezone coverage for after-hours EU support)."
        ),
        factor_scores={
            "GA1": 3,  # IT Act Section 69 and Telegraph Act are broad
            "GA2": 4,  # Limited judicial oversight for intelligence access
            "GA3": 4,  # No effective remedy for foreign nationals under current framework
            "GA4": 3,  # Limited transparency requirements
            "GA5": 3,  # Constitutional protections exist but surveillance oversight weak
        },
        guarantee_scores={
            "EG1": 3,  # Laws exist but with broad discretionary scope
            "EG2": 4,  # Broad access powers with limited proportionality
            "EG3": 4,  # Limited independent oversight of surveillance
            "EG4": 4,  # No effective remedy for foreign nationals
        },
        processing_requires_clear_text=True,
    )


if __name__ == "__main__":
    result = run_example_tia()
    print(json.dumps(result, indent=2, default=str))
