#!/usr/bin/env python3
"""
Breach Risk Assessment Engine

Implements the EDPB-aligned breach risk assessment methodology for determining
GDPR Art. 33 and Art. 34 notification requirements. Supports factor-by-factor
scoring, threshold determination, and assessment report generation.
"""

import json
import sys
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class BreachType(Enum):
    CONFIDENTIALITY = "confidentiality"
    INTEGRITY = "integrity"
    AVAILABILITY = "availability"
    COMBINED = "combined"


class RiskLevel(Enum):
    NO_RISK = "unlikely_to_result_in_risk"
    RISK = "likely_to_result_in_risk"
    APPROACHING_HIGH = "approaching_high_risk"
    HIGH_RISK = "likely_to_result_in_high_risk"


class NotificationDecision(Enum):
    NO_NOTIFICATION = "no_notification_required"
    SA_ONLY = "supervisory_authority_only"
    SA_AND_DS_RECOMMENDED = "sa_required_ds_recommended"
    SA_AND_DS_REQUIRED = "sa_and_ds_required"


FACTOR_DESCRIPTIONS = {
    "data_sensitivity": {
        1: "Non-sensitive data, publicly available or easily obtainable (business contacts, public directory info)",
        2: "Personal identifiers or behavioral data (email, phone, purchase history, browsing data)",
        3: "Financial data, government IDs, employment records, precise location data",
        4: "Art. 9 special categories, Art. 10 criminal data, authentication credentials, data enabling physical harm",
    },
    "volume": {
        1: "Fewer than 100 data subjects affected",
        2: "100 to 1,000 data subjects affected",
        3: "1,000 to 100,000 data subjects affected",
        4: "More than 100,000 data subjects affected",
    },
    "identifiability": {
        1: "Data pseudonymized or encrypted with key integrity maintained",
        2: "Indirect identifiers only; re-identification requires additional datasets",
        3: "Direct identifiers present (name combined with one additional element)",
        4: "Multiple direct identifiers, photographs, or biometric data exposed",
    },
    "consequences": {
        1: "Minor inconvenience (unsolicited marketing, password change needed)",
        2: "Moderate impact (phishing risk, minor financial exposure, reputational inconvenience)",
        3: "Significant impact (identity theft risk, substantial financial loss, discrimination risk)",
        4: "Severe impact (physical safety threat, significant fraud, denial of essential services)",
    },
    "vulnerable_subjects": {
        1: "General adult population with no heightened vulnerability",
        2: "Includes individuals in dependent relationships (employees, tenants)",
        3: "Includes elderly, financially vulnerable, or unequal power dynamic populations",
        4: "Includes minors, patients, asylum seekers, or safety-dependent individuals",
    },
    "controller_specific": {
        1: "Personal data processing is ancillary to core business (office admin)",
        2: "Personal data processing is core to service delivery",
        3: "Controller holds position of trust (financial, healthcare, education)",
        4: "Large-scale data processing as core business (payment processor, data broker)",
    },
}

EDPB_SCENARIOS = [
    {
        "id": 1,
        "title": "Ransomware with backup — hospital patient data",
        "breach_type": "availability",
        "description": "Hospital hit by ransomware. 2,500 patient records encrypted. Clean backup restored within 24 hours. No evidence of exfiltration.",
        "scores": {"data_sensitivity": 4, "volume": 3, "identifiability": 4, "consequences": 3, "vulnerable_subjects": 4, "controller_specific": 3},
        "total": 21,
        "sa_notification": True,
        "ds_notification": True,
        "edpb_rationale": "Temporary unavailability of health data poses risk to patient safety even with backup restoration. High risk confirmed.",
    },
    {
        "id": 2,
        "title": "Ransomware without backup — small company payroll",
        "breach_type": "availability",
        "description": "Manufacturing company ransomware. 45 employee payroll records permanently lost. No backup.",
        "scores": {"data_sensitivity": 3, "volume": 1, "identifiability": 4, "consequences": 3, "vulnerable_subjects": 2, "controller_specific": 2},
        "total": 15,
        "sa_notification": True,
        "ds_notification": True,
        "edpb_rationale": "Permanent loss of payroll data directly impacts employees financial interests.",
    },
    {
        "id": 3,
        "title": "Data exfiltration — e-commerce platform",
        "breach_type": "confidentiality",
        "description": "SQL injection extracts usernames, hashed passwords, and emails of 1.2 million users.",
        "scores": {"data_sensitivity": 2, "volume": 4, "identifiability": 3, "consequences": 2, "vulnerable_subjects": 1, "controller_specific": 3},
        "total": 15,
        "sa_notification": True,
        "ds_notification": True,
        "edpb_rationale": "Email + hashed password combination enables credential-stuffing attacks at scale.",
    },
    {
        "id": 4,
        "title": "Misdirected email — single salary slip",
        "breach_type": "confidentiality",
        "description": "Single employee salary slip emailed to wrong internal colleague. Discovered in 10 minutes, recipient confirms deletion.",
        "scores": {"data_sensitivity": 3, "volume": 1, "identifiability": 4, "consequences": 1, "vulnerable_subjects": 2, "controller_specific": 1},
        "total": 12,
        "sa_notification": True,
        "ds_notification": False,
        "edpb_rationale": "Marginal SA notification. Breach contained, recipient cooperative, limited exposure.",
    },
    {
        "id": 5,
        "title": "Lost unencrypted USB — pension scheme members",
        "breach_type": "confidentiality",
        "description": "Unencrypted USB lost with names, addresses, and NI numbers of 3,500 pension members.",
        "scores": {"data_sensitivity": 3, "volume": 3, "identifiability": 4, "consequences": 3, "vulnerable_subjects": 3, "controller_specific": 3},
        "total": 19,
        "sa_notification": True,
        "ds_notification": True,
        "edpb_rationale": "Government IDs + vulnerable elderly population creates high identity theft risk.",
    },
    {
        "id": 6,
        "title": "Accidental publication — student grades",
        "breach_type": "confidentiality",
        "description": "University publishes 800 students exam results with names on public webpage for 36 hours.",
        "scores": {"data_sensitivity": 2, "volume": 2, "identifiability": 4, "consequences": 2, "vulnerable_subjects": 2, "controller_specific": 3},
        "total": 15,
        "sa_notification": True,
        "ds_notification": True,
        "edpb_rationale": "Academic performance linked to names, 36h public exposure, impact on academic prospects.",
    },
]


def assess_risk(
    data_sensitivity: int,
    volume: int,
    identifiability: int,
    consequences: int,
    vulnerable_subjects: int,
    controller_specific: int,
    breach_type: str = "confidentiality",
    breach_description: str = "",
    assessor_name: str = "",
    breach_reference: str = "",
) -> dict:
    """
    Perform a complete breach risk assessment.

    Args:
        data_sensitivity: Score 1-4 for data sensitivity.
        volume: Score 1-4 for volume of affected subjects.
        identifiability: Score 1-4 for ease of identification.
        consequences: Score 1-4 for consequence severity.
        vulnerable_subjects: Score 1-4 for vulnerable individual presence.
        controller_specific: Score 1-4 for controller role amplification.
        breach_type: CIA classification.
        breach_description: Narrative description of the breach.
        assessor_name: Name of person conducting the assessment.
        breach_reference: Internal breach reference number.

    Returns:
        Complete assessment record with scores, determination, and rationale.
    """
    factors = {
        "data_sensitivity": data_sensitivity,
        "volume": volume,
        "identifiability": identifiability,
        "consequences": consequences,
        "vulnerable_subjects": vulnerable_subjects,
        "controller_specific": controller_specific,
    }

    for name, value in factors.items():
        if not 1 <= value <= 4:
            raise ValueError(f"{name} must be between 1 and 4, got {value}")

    total_score = sum(factors.values())

    if total_score <= 8:
        risk_level = RiskLevel.NO_RISK
        notification = NotificationDecision.NO_NOTIFICATION
    elif total_score <= 12:
        risk_level = RiskLevel.RISK
        notification = NotificationDecision.SA_ONLY
    elif total_score <= 18:
        risk_level = RiskLevel.APPROACHING_HIGH
        notification = NotificationDecision.SA_AND_DS_RECOMMENDED
    else:
        risk_level = RiskLevel.HIGH_RISK
        notification = NotificationDecision.SA_AND_DS_REQUIRED

    factor_details = {}
    for name, score in factors.items():
        factor_details[name] = {
            "score": score,
            "max_score": 4,
            "description": FACTOR_DESCRIPTIONS[name][score],
        }

    return {
        "assessment_metadata": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "assessor": assessor_name or "DPO Office",
            "breach_reference": breach_reference,
            "methodology": "EDPB Guidelines 9/2022 Section 3.1",
            "version": 1,
        },
        "breach_classification": {
            "type": breach_type,
            "description": breach_description,
        },
        "factor_scores": factor_details,
        "aggregate_score": total_score,
        "max_possible_score": 24,
        "risk_percentage": round((total_score / 24) * 100, 1),
        "risk_level": risk_level.value,
        "notification_decision": notification.value,
        "obligations": {
            "art_33_5_documentation": True,
            "art_33_sa_notification": notification != NotificationDecision.NO_NOTIFICATION,
            "art_34_ds_notification": notification in (
                NotificationDecision.SA_AND_DS_RECOMMENDED,
                NotificationDecision.SA_AND_DS_REQUIRED,
            ),
            "art_34_ds_notification_mandatory": notification == NotificationDecision.SA_AND_DS_REQUIRED,
        },
        "reassessment_triggers": [
            "Scope of breach increases (additional data subjects or categories identified)",
            "Data exfiltration confirmed or ruled out",
            "Evidence of compromised data misuse emerges",
            "Supplementary forensic report changes breach understanding",
            "Supervisory authority requests additional assessment detail",
        ],
    }


def find_comparable_edpb_scenarios(breach_type: str, total_score: int) -> list:
    """
    Find EDPB guideline scenarios comparable to the current breach.

    Args:
        breach_type: CIA classification of the breach.
        total_score: Aggregate risk assessment score.

    Returns:
        List of comparable EDPB scenarios with relevance notes.
    """
    comparable = []
    for scenario in EDPB_SCENARIOS:
        relevance_score = 0

        if scenario["breach_type"] == breach_type:
            relevance_score += 3

        score_diff = abs(scenario["total"] - total_score)
        if score_diff <= 3:
            relevance_score += 3
        elif score_diff <= 6:
            relevance_score += 1

        if relevance_score >= 1:
            comparable.append({
                "scenario_id": scenario["id"],
                "title": scenario["title"],
                "breach_type": scenario["breach_type"],
                "total_score": scenario["total"],
                "sa_notification": scenario["sa_notification"],
                "ds_notification": scenario["ds_notification"],
                "edpb_rationale": scenario["edpb_rationale"],
                "relevance_score": relevance_score,
            })

    comparable.sort(key=lambda x: x["relevance_score"], reverse=True)
    return comparable[:3]


def generate_assessment_report(assessment: dict, comparable_scenarios: list) -> str:
    """Generate a formatted text report of the risk assessment."""
    lines = []
    lines.append("=" * 70)
    lines.append("BREACH RISK ASSESSMENT REPORT")
    lines.append("=" * 70)
    lines.append("")

    meta = assessment["assessment_metadata"]
    lines.append(f"Reference:    {meta['breach_reference']}")
    lines.append(f"Assessor:     {meta['assessor']}")
    lines.append(f"Timestamp:    {meta['timestamp']}")
    lines.append(f"Methodology:  {meta['methodology']}")
    lines.append("")

    breach = assessment["breach_classification"]
    lines.append(f"Breach Type:  {breach['type'].upper()}")
    if breach["description"]:
        lines.append(f"Description:  {breach['description']}")
    lines.append("")

    lines.append("-" * 70)
    lines.append("FACTOR SCORES")
    lines.append("-" * 70)
    for name, detail in assessment["factor_scores"].items():
        display_name = name.replace("_", " ").title()
        lines.append(f"  {display_name}: {detail['score']}/{detail['max_score']}")
        lines.append(f"    {detail['description']}")
    lines.append("")
    lines.append(f"  AGGREGATE SCORE: {assessment['aggregate_score']}/{assessment['max_possible_score']} ({assessment['risk_percentage']}%)")
    lines.append("")

    lines.append("-" * 70)
    lines.append("DETERMINATION")
    lines.append("-" * 70)
    lines.append(f"  Risk Level:     {assessment['risk_level'].replace('_', ' ').upper()}")
    lines.append(f"  Decision:       {assessment['notification_decision'].replace('_', ' ').upper()}")
    lines.append("")

    obligations = assessment["obligations"]
    lines.append("  Obligations:")
    lines.append(f"    Art. 33(5) Breach Register:  REQUIRED (always)")
    lines.append(f"    Art. 33 SA Notification:     {'REQUIRED' if obligations['art_33_sa_notification'] else 'Not required'}")
    lines.append(f"    Art. 34 DS Notification:     {'REQUIRED' if obligations['art_34_ds_notification_mandatory'] else 'Recommended' if obligations['art_34_ds_notification'] else 'Not required'}")
    lines.append("")

    if comparable_scenarios:
        lines.append("-" * 70)
        lines.append("COMPARABLE EDPB SCENARIOS")
        lines.append("-" * 70)
        for s in comparable_scenarios:
            lines.append(f"  Scenario {s['scenario_id']}: {s['title']}")
            lines.append(f"    Type: {s['breach_type']} | Score: {s['total_score']}/24")
            lines.append(f"    SA: {'Yes' if s['sa_notification'] else 'No'} | DS: {'Yes' if s['ds_notification'] else 'No'}")
            lines.append(f"    EDPB: {s['edpb_rationale']}")
            lines.append("")

    lines.append("-" * 70)
    lines.append("RE-ASSESSMENT TRIGGERS")
    lines.append("-" * 70)
    for trigger in assessment["reassessment_triggers"]:
        lines.append(f"  - {trigger}")

    return "\n".join(lines)


def main():
    print("Scenario A: Ransomware attack on Stellar Payments Group customer database")
    print("=" * 70)

    assessment_a = assess_risk(
        data_sensitivity=3,
        volume=3,
        identifiability=4,
        consequences=3,
        vulnerable_subjects=1,
        controller_specific=4,
        breach_type="availability",
        breach_description=(
            "LockBit 3.0 ransomware encrypted 48,720 customer records across "
            "the production database cluster. 15,230 data subjects affected. "
            "Backup restoration initiated. No exfiltration evidence at time of assessment."
        ),
        assessor_name="Dr. Elena Vasquez",
        breach_reference="SPG-BREACH-2026-003",
    )

    comparable_a = find_comparable_edpb_scenarios("availability", assessment_a["aggregate_score"])
    print(generate_assessment_report(assessment_a, comparable_a))

    print("\n\n")
    print("Scenario B: Misdirected email containing customer invoices")
    print("=" * 70)

    assessment_b = assess_risk(
        data_sensitivity=2,
        volume=1,
        identifiability=3,
        consequences=1,
        vulnerable_subjects=1,
        controller_specific=2,
        breach_type="confidentiality",
        breach_description=(
            "Customer service representative sent an email containing 8 customer "
            "invoices (names, addresses, purchase amounts) to an incorrect external "
            "email address. The recipient has been contacted and confirmed deletion."
        ),
        assessor_name="Dr. Elena Vasquez",
        breach_reference="SPG-BREACH-2026-004",
    )

    comparable_b = find_comparable_edpb_scenarios("confidentiality", assessment_b["aggregate_score"])
    print(generate_assessment_report(assessment_b, comparable_b))

    print("\n\n")
    print("Scenario C: Health data breach — employee wellness records")
    print("=" * 70)

    assessment_c = assess_risk(
        data_sensitivity=4,
        volume=2,
        identifiability=4,
        consequences=3,
        vulnerable_subjects=2,
        controller_specific=2,
        breach_type="confidentiality",
        breach_description=(
            "Unauthorized access by IT employee to occupational health database "
            "containing health screening results and sick leave records for 340 "
            "employees enrolled in the company wellness programme."
        ),
        assessor_name="Dr. Elena Vasquez",
        breach_reference="SPG-BREACH-2026-005",
    )

    comparable_c = find_comparable_edpb_scenarios("confidentiality", assessment_c["aggregate_score"])
    print(generate_assessment_report(assessment_c, comparable_c))


if __name__ == "__main__":
    main()
