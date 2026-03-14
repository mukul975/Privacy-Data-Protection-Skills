#!/usr/bin/env python3
"""
Transfer Impact Assessment (TIA) Engine

Implements the EDPB six-step methodology for assessing international
data transfers. Evaluates destination country laws against European
Essential Guarantees and determines supplementary measure requirements.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


EUROPEAN_ESSENTIAL_GUARANTEES = [
    {
        "id": "eeg_1",
        "name": "Clear, Precise, and Accessible Rules",
        "criteria": [
            "Government access based on published legislation",
            "Scope of access clearly defined in law",
            "Categories of data and persons specified",
            "Conditions and limitations for access stated",
        ],
    },
    {
        "id": "eeg_2",
        "name": "Necessity and Proportionality",
        "criteria": [
            "Necessity requirement for each access request",
            "Proportionality of access scope to stated objective",
            "Safeguards against bulk or untargeted access",
            "Data minimisation and retention limits for accessed data",
        ],
    },
    {
        "id": "eeg_3",
        "name": "Independent Oversight",
        "criteria": [
            "Prior judicial or independent authorisation required",
            "Ongoing independent oversight of access activities",
            "Oversight body genuinely independent from executive",
        ],
    },
    {
        "id": "eeg_4",
        "name": "Effective Remedies",
        "criteria": [
            "Individuals can challenge access in court or before independent body",
            "Notification mechanism exists (even if delayed)",
            "Effective remedies available (compensation, deletion, injunction)",
        ],
    },
]

COUNTRY_RISK_PROFILES = {
    "US": {
        "name": "United States",
        "surveillance_laws": [
            "FISA Section 702",
            "Executive Order 12333",
            "CLOUD Act",
            "National Security Letters (18 USC 2709)",
        ],
        "baseline_risk": "medium",
        "dpf_available": True,
        "notes": "EO 14086 and DPRC address Schrems II concerns for DPF-certified orgs; "
        "non-DPF transfers require supplementary measures",
    },
    "CN": {
        "name": "People's Republic of China",
        "surveillance_laws": [
            "National Intelligence Law (Art. 7, 14)",
            "Cybersecurity Law (Art. 28, 37)",
            "Data Security Law (Art. 35-36)",
            "Counter-Espionage Law (2023 revision)",
            "Cryptography Law",
        ],
        "baseline_risk": "high",
        "dpf_available": False,
        "notes": "Broad government access powers with limited independent oversight; "
        "strong encryption with EU-held keys essential",
    },
    "IN": {
        "name": "India",
        "surveillance_laws": [
            "IT Act 2000 Section 69 (interception powers)",
            "Telegraph Act 1885 Section 5",
            "DPDP Act 2023 Section 36 (government exemptions)",
            "CMS (Central Monitoring System)",
        ],
        "baseline_risk": "medium-high",
        "dpf_available": False,
        "notes": "Ministerial authorisation for interception without prior judicial review; "
        "DPDP Act exemptions for state security are broad",
    },
    "HK": {
        "name": "Hong Kong SAR",
        "surveillance_laws": [
            "Interception of Communications and Surveillance Ordinance (Cap. 589)",
            "National Security Law (2020)",
            "Safeguarding National Security Ordinance (2024)",
        ],
        "baseline_risk": "medium",
        "dpf_available": False,
        "notes": "Cap. 589 provides judicial oversight for interception; NSL introduces broader "
        "powers with limited proportionality review",
    },
    "RU": {
        "name": "Russian Federation",
        "surveillance_laws": [
            "Federal Law No. 144-FZ on Operative-Investigative Activity",
            "SORM system (System of Operative-Investigative Measures)",
            "Yarovaya Law (Federal Law No. 374-FZ)",
            "Federal Law No. 242-FZ (data localisation)",
        ],
        "baseline_risk": "very-high",
        "dpf_available": False,
        "notes": "SORM requires ISPs to install surveillance equipment; Yarovaya Law mandates "
        "data retention; very limited independent oversight and remedies",
    },
    "BR": {
        "name": "Brazil",
        "surveillance_laws": [
            "Lei Geral de Protecao de Dados (LGPD)",
            "Marco Civil da Internet (Law 12.965/2014)",
            "Interception Law (Law 9.296/1996)",
        ],
        "baseline_risk": "low-medium",
        "dpf_available": False,
        "notes": "LGPD provides strong data protection framework; interception requires "
        "judicial authorisation; ANPD established as independent authority",
    },
    "SG": {
        "name": "Singapore",
        "surveillance_laws": [
            "Computer Misuse Act",
            "Official Secrets Act",
            "Internal Security Act",
        ],
        "baseline_risk": "low-medium",
        "dpf_available": False,
        "notes": "Strong rule of law; PDPA provides data protection framework; "
        "internal security powers exist but used sparingly in commercial context",
    },
}

SUPPLEMENTARY_MEASURES_CATALOGUE = {
    "technical": [
        {
            "id": "T1",
            "name": "End-to-end encryption with EU-held keys",
            "effectiveness": "high",
            "addresses": ["eeg_2", "eeg_3"],
            "applicable_when": "Importer does not need access to plaintext data",
        },
        {
            "id": "T2",
            "name": "Pseudonymisation with EU-held mapping table",
            "effectiveness": "high",
            "addresses": ["eeg_1", "eeg_2"],
            "applicable_when": "Importer can process data without identifying individuals",
        },
        {
            "id": "T3",
            "name": "Split processing across jurisdictions",
            "effectiveness": "high",
            "addresses": ["eeg_2"],
            "applicable_when": "Processing can be divided so no single jurisdiction holds complete dataset",
        },
        {
            "id": "T4",
            "name": "Transport-layer encryption (TLS 1.3)",
            "effectiveness": "medium",
            "addresses": ["eeg_2"],
            "applicable_when": "Baseline measure for all transfers; insufficient alone for high-risk jurisdictions",
        },
    ],
    "contractual": [
        {
            "id": "C1",
            "name": "Obligation to challenge disproportionate government requests",
            "effectiveness": "medium",
            "addresses": ["eeg_2", "eeg_4"],
            "applicable_when": "Importer has legal standing to challenge requests",
        },
        {
            "id": "C2",
            "name": "Transparency obligation for government access requests",
            "effectiveness": "medium",
            "addresses": ["eeg_1", "eeg_4"],
            "applicable_when": "Not prohibited by local law gag orders",
        },
        {
            "id": "C3",
            "name": "Exporter audit rights over importer compliance",
            "effectiveness": "medium",
            "addresses": ["eeg_3"],
            "applicable_when": "All transfers",
        },
        {
            "id": "C4",
            "name": "Warrant canary in regular transparency reports",
            "effectiveness": "low-medium",
            "addresses": ["eeg_1"],
            "applicable_when": "Jurisdictions where gag orders may apply",
        },
    ],
    "organisational": [
        {
            "id": "O1",
            "name": "Strict internal access policies at importer",
            "effectiveness": "medium",
            "addresses": ["eeg_2"],
            "applicable_when": "All transfers",
        },
        {
            "id": "O2",
            "name": "Regular transparency reports on government requests",
            "effectiveness": "medium",
            "addresses": ["eeg_1", "eeg_4"],
            "applicable_when": "All transfers",
        },
        {
            "id": "O3",
            "name": "Importer ISO 27001/27701 certification",
            "effectiveness": "medium",
            "addresses": ["eeg_2", "eeg_3"],
            "applicable_when": "Provides independent verification of controls",
        },
    ],
}


def conduct_eeg_assessment(country_code: str, eeg_scores: dict) -> dict:
    """Assess a destination country against the four European Essential Guarantees."""
    country = COUNTRY_RISK_PROFILES.get(country_code.upper())
    if not country:
        return {"error": f"Country code '{country_code}' not found in profiles"}

    results = {
        "country": country["name"],
        "country_code": country_code.upper(),
        "assessment_date": datetime.utcnow().isoformat(),
        "surveillance_laws": country["surveillance_laws"],
        "guarantees": {},
        "overall_risk": country["baseline_risk"],
        "gaps": [],
    }

    total_criteria = 0
    met_criteria = 0

    for eeg in EUROPEAN_ESSENTIAL_GUARANTEES:
        eeg_id = eeg["id"]
        scores = eeg_scores.get(eeg_id, {})
        eeg_met = 0
        eeg_gaps = []

        for criterion in eeg["criteria"]:
            total_criteria += 1
            if scores.get(criterion, False):
                eeg_met += 1
                met_criteria += 1
            else:
                eeg_gaps.append(criterion)
                results["gaps"].append(
                    {"guarantee": eeg["name"], "criterion": criterion}
                )

        results["guarantees"][eeg_id] = {
            "name": eeg["name"],
            "total_criteria": len(eeg["criteria"]),
            "met": eeg_met,
            "gaps": eeg_gaps,
            "score_pct": round(eeg_met / len(eeg["criteria"]) * 100, 1),
        }

    results["overall_score_pct"] = (
        round(met_criteria / total_criteria * 100, 1) if total_criteria else 0
    )

    if results["overall_score_pct"] >= 80:
        results["preliminary_conclusion"] = "green"
        results["conclusion_text"] = (
            "Legal framework provides essentially equivalent protection; "
            "supplementary measures may not be necessary"
        )
    elif results["overall_score_pct"] >= 40:
        results["preliminary_conclusion"] = "amber"
        results["conclusion_text"] = (
            "Protection gaps exist that may be bridged with supplementary measures; "
            "proceed to Step 4"
        )
    else:
        results["preliminary_conclusion"] = "red"
        results["conclusion_text"] = (
            "Significant protection gaps identified; supplementary measures "
            "unlikely to be effective — consider suspending the transfer"
        )

    return results


def recommend_supplementary_measures(eeg_gaps: list, data_sensitivity: str) -> dict:
    """Recommend supplementary measures based on identified EEG gaps."""
    gap_eegs = set()
    for gap in eeg_gaps:
        for eeg in EUROPEAN_ESSENTIAL_GUARANTEES:
            if gap.get("criterion") in eeg["criteria"]:
                gap_eegs.add(eeg["id"])

    recommended = {"technical": [], "contractual": [], "organisational": []}

    for category, measures in SUPPLEMENTARY_MEASURES_CATALOGUE.items():
        for measure in measures:
            if any(addr in gap_eegs for addr in measure["addresses"]):
                if data_sensitivity == "high" and measure["effectiveness"] in (
                    "low-medium",
                ):
                    continue
                recommended[category].append(measure)

    total_measures = sum(len(v) for v in recommended.values())
    return {
        "assessment_date": datetime.utcnow().isoformat(),
        "data_sensitivity": data_sensitivity,
        "identified_gaps": len(eeg_gaps),
        "gap_eeg_areas": list(gap_eegs),
        "recommended_measures": recommended,
        "total_recommended": total_measures,
        "recommendation": "Implement all recommended measures before proceeding with transfer"
        if total_measures > 0
        else "No supplementary measures identified — review assessment for completeness",
    }


def generate_tia_record(
    transfer_ref: str,
    exporter: str,
    importer: str,
    destination_country: str,
    mechanism: str,
    data_categories: list,
    eeg_conclusion: str,
    supplementary_measures: list,
    assessed_by: str,
    review_interval_months: int = 12,
) -> dict:
    """Generate a formal TIA record."""
    now = datetime.utcnow()
    next_review = now + timedelta(days=review_interval_months * 30)

    conclusion_map = {
        "green": "Transfer may proceed; no supplementary measures required",
        "amber": "Transfer may proceed with supplementary measures implemented",
        "red": "Transfer must be suspended; supplementary measures insufficient",
    }

    return {
        "tia_reference": transfer_ref,
        "assessment_date": now.strftime("%Y-%m-%d"),
        "exporter": exporter,
        "importer": importer,
        "destination_country": destination_country,
        "transfer_mechanism": mechanism,
        "data_categories": data_categories,
        "eeg_conclusion": eeg_conclusion,
        "conclusion_text": conclusion_map.get(eeg_conclusion, "Unknown"),
        "supplementary_measures": supplementary_measures,
        "assessed_by": assessed_by,
        "next_review_date": next_review.strftime("%Y-%m-%d"),
        "review_triggers": [
            "New surveillance legislation in destination country",
            "Court ruling affecting privacy protections",
            "EDPB or SA updated guidance",
            "Material change in transfer scope or sensitivity",
            "Government access request received by importer",
        ],
        "status": "active",
        "version": "1.0",
    }


def assess_transfer_portfolio(tia_records: list) -> dict:
    """Generate a portfolio-level view of all TIA statuses."""
    total = len(tia_records)
    by_conclusion = {"green": 0, "amber": 0, "red": 0}
    by_country = {}
    overdue_reviews = []

    now = datetime.utcnow()

    for record in tia_records:
        conclusion = record.get("eeg_conclusion", "unknown")
        by_conclusion[conclusion] = by_conclusion.get(conclusion, 0) + 1

        country = record.get("destination_country", "unknown")
        by_country[country] = by_country.get(country, 0) + 1

        review_date = datetime.strptime(record["next_review_date"], "%Y-%m-%d")
        if review_date < now:
            overdue_reviews.append(
                {
                    "tia_reference": record["tia_reference"],
                    "destination_country": record["destination_country"],
                    "days_overdue": (now - review_date).days,
                }
            )

    return {
        "portfolio_date": now.strftime("%Y-%m-%d"),
        "total_tias": total,
        "by_conclusion": by_conclusion,
        "by_destination_country": by_country,
        "overdue_reviews": overdue_reviews,
        "action_items": _generate_portfolio_actions(by_conclusion, overdue_reviews),
    }


def _generate_portfolio_actions(by_conclusion: dict, overdue: list) -> list:
    """Generate action items from portfolio assessment."""
    actions = []
    if by_conclusion.get("red", 0) > 0:
        actions.append(
            f"CRITICAL: {by_conclusion['red']} transfer(s) concluded RED — "
            "verify transfers are suspended and SA notified"
        )
    if overdue:
        actions.append(
            f"MAJOR: {len(overdue)} TIA(s) overdue for review — "
            "initiate re-evaluation immediately"
        )
    if by_conclusion.get("amber", 0) > 0:
        actions.append(
            f"MONITOR: {by_conclusion['amber']} transfer(s) rely on supplementary measures — "
            "verify ongoing effectiveness"
        )
    if not actions:
        actions.append("No immediate action items — all TIAs current and green")
    return actions


if __name__ == "__main__":
    print("=== EEG Assessment — Hong Kong ===")
    hk_scores = {
        "eeg_1": {
            "Government access based on published legislation": True,
            "Scope of access clearly defined in law": True,
            "Categories of data and persons specified": False,
            "Conditions and limitations for access stated": True,
        },
        "eeg_2": {
            "Necessity requirement for each access request": True,
            "Proportionality of access scope to stated objective": False,
            "Safeguards against bulk or untargeted access": True,
            "Data minimisation and retention limits for accessed data": False,
        },
        "eeg_3": {
            "Prior judicial or independent authorisation required": True,
            "Ongoing independent oversight of access activities": True,
            "Oversight body genuinely independent from executive": False,
        },
        "eeg_4": {
            "Individuals can challenge access in court or before independent body": True,
            "Notification mechanism exists (even if delayed)": False,
            "Effective remedies available (compensation, deletion, injunction)": True,
        },
    }
    eeg_result = conduct_eeg_assessment("HK", hk_scores)
    print(json.dumps(eeg_result, indent=2))

    print("\n=== Supplementary Measures Recommendation ===")
    measures = recommend_supplementary_measures(eeg_result["gaps"], "medium")
    print(json.dumps(measures, indent=2))

    print("\n=== TIA Record Generation ===")
    tia = generate_tia_record(
        transfer_ref="TIA-2025-HK-001",
        exporter="Athena Global Logistics GmbH",
        importer="TransPacific Freight Solutions Ltd",
        destination_country="Hong Kong SAR",
        mechanism="SCCs Module 2 (Commission Decision 2021/914)",
        data_categories=["customer names", "shipping addresses", "customs IDs"],
        eeg_conclusion="amber",
        supplementary_measures=["T1: End-to-end encryption", "C1: Challenge obligation", "C2: Transparency"],
        assessed_by="Elisa Brandt, Head of Data Protection",
    )
    print(json.dumps(tia, indent=2))
