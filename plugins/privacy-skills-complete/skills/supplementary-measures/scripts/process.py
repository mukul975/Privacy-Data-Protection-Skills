#!/usr/bin/env python3
"""
Supplementary Measures Selection and Effectiveness Engine

Selects appropriate supplementary measures based on TIA gap analysis,
assesses combined effectiveness, and tracks implementation status.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


MEASURES_CATALOGUE = {
    "T1": {
        "id": "T1",
        "category": "technical",
        "name": "End-to-end encryption with EU-held keys",
        "effectiveness": "high",
        "addresses_eegs": ["eeg_2", "eeg_3"],
        "prevents_compelled_disclosure": True,
        "prevents_bulk_surveillance": True,
        "requires_importer_plaintext": False,
        "implementation_effort": "high",
        "description": "AES-256-GCM encryption with CMK in EU KMS; importer receives ciphertext only",
    },
    "T2": {
        "id": "T2",
        "category": "technical",
        "name": "Pseudonymisation with EU-held mapping",
        "effectiveness": "high",
        "addresses_eegs": ["eeg_1", "eeg_2"],
        "prevents_compelled_disclosure": True,
        "prevents_bulk_surveillance": True,
        "requires_importer_plaintext": False,
        "implementation_effort": "medium",
        "description": "HMAC-SHA256 pseudonymisation; mapping table in EU PostgreSQL instance",
    },
    "T3": {
        "id": "T3",
        "category": "technical",
        "name": "Split processing across jurisdictions",
        "effectiveness": "high",
        "addresses_eegs": ["eeg_2"],
        "prevents_compelled_disclosure": True,
        "prevents_bulk_surveillance": True,
        "requires_importer_plaintext": False,
        "implementation_effort": "very-high",
        "description": "Identity data stays in EU; only operational data transferred",
    },
    "T4": {
        "id": "T4",
        "category": "technical",
        "name": "Transport-layer encryption (TLS 1.3)",
        "effectiveness": "medium",
        "addresses_eegs": ["eeg_2"],
        "prevents_compelled_disclosure": False,
        "prevents_bulk_surveillance": True,
        "requires_importer_plaintext": True,
        "implementation_effort": "low",
        "description": "TLS 1.3 with strong cipher suites; mTLS for endpoint authentication",
    },
    "T5": {
        "id": "T5",
        "category": "technical",
        "name": "Anonymisation before transfer",
        "effectiveness": "complete",
        "addresses_eegs": ["eeg_1", "eeg_2", "eeg_3", "eeg_4"],
        "prevents_compelled_disclosure": True,
        "prevents_bulk_surveillance": True,
        "requires_importer_plaintext": True,
        "implementation_effort": "medium",
        "description": "k-anonymity + l-diversity; data no longer personal after transformation",
    },
    "C1": {
        "id": "C1",
        "category": "contractual",
        "name": "Obligation to challenge disproportionate requests",
        "effectiveness": "medium",
        "addresses_eegs": ["eeg_2", "eeg_4"],
        "prevents_compelled_disclosure": False,
        "prevents_bulk_surveillance": False,
        "requires_importer_plaintext": True,
        "implementation_effort": "low",
        "description": "Contractual duty to exhaust legal remedies before disclosure",
    },
    "C2": {
        "id": "C2",
        "category": "contractual",
        "name": "Transparency obligation for government access",
        "effectiveness": "medium",
        "addresses_eegs": ["eeg_1", "eeg_4"],
        "prevents_compelled_disclosure": False,
        "prevents_bulk_surveillance": False,
        "requires_importer_plaintext": True,
        "implementation_effort": "low",
        "description": "48-hour notification to exporter upon government request receipt",
    },
    "C3": {
        "id": "C3",
        "category": "contractual",
        "name": "Audit rights for data exporter",
        "effectiveness": "medium",
        "addresses_eegs": ["eeg_3"],
        "prevents_compelled_disclosure": False,
        "prevents_bulk_surveillance": False,
        "requires_importer_plaintext": True,
        "implementation_effort": "low",
        "description": "Annual on-site or remote audit right with 30-day notice",
    },
    "C4": {
        "id": "C4",
        "category": "contractual",
        "name": "Warrant canary",
        "effectiveness": "low-medium",
        "addresses_eegs": ["eeg_1"],
        "prevents_compelled_disclosure": False,
        "prevents_bulk_surveillance": False,
        "requires_importer_plaintext": True,
        "implementation_effort": "low",
        "description": "Monthly statement confirming no undisclosable government orders received",
    },
    "O1": {
        "id": "O1",
        "category": "organisational",
        "name": "Strict internal access policies",
        "effectiveness": "medium",
        "addresses_eegs": ["eeg_2"],
        "prevents_compelled_disclosure": False,
        "prevents_bulk_surveillance": False,
        "requires_importer_plaintext": True,
        "implementation_effort": "low",
        "description": "Named personnel access list; quarterly reviews; 24h revocation SLA",
    },
    "O2": {
        "id": "O2",
        "category": "organisational",
        "name": "Transparency reports on government requests",
        "effectiveness": "medium",
        "addresses_eegs": ["eeg_1", "eeg_4"],
        "prevents_compelled_disclosure": False,
        "prevents_bulk_surveillance": False,
        "requires_importer_plaintext": True,
        "implementation_effort": "low",
        "description": "Annual public transparency report on government data requests",
    },
    "O3": {
        "id": "O3",
        "category": "organisational",
        "name": "ISO 27001/27701 certification",
        "effectiveness": "medium",
        "addresses_eegs": ["eeg_2", "eeg_3"],
        "prevents_compelled_disclosure": False,
        "prevents_bulk_surveillance": False,
        "requires_importer_plaintext": True,
        "implementation_effort": "high",
        "description": "Independent third-party certification of security and privacy controls",
    },
}

EFFECTIVENESS_WEIGHTS = {
    "complete": 5,
    "high": 4,
    "medium": 2,
    "low-medium": 1,
    "low": 0.5,
}


def select_measures(
    eeg_gaps: list,
    importer_needs_plaintext: bool,
    data_sensitivity: str,
    risk_level: str,
) -> dict:
    """Select supplementary measures based on TIA gap analysis."""
    gap_eegs = set()
    for gap in eeg_gaps:
        gap_eegs.add(gap["eeg_id"])

    selected = []
    excluded = []

    for measure_id, measure in MEASURES_CATALOGUE.items():
        addresses_gap = any(eeg in gap_eegs for eeg in measure["addresses_eegs"])
        if not addresses_gap:
            continue

        if importer_needs_plaintext and not measure["requires_importer_plaintext"]:
            if measure["category"] == "technical" and measure["effectiveness"] == "high":
                excluded.append(
                    {
                        "id": measure_id,
                        "name": measure["name"],
                        "reason": "Importer requires plaintext access for processing",
                    }
                )
                continue

        if data_sensitivity == "low" and measure["implementation_effort"] == "very-high":
            excluded.append(
                {
                    "id": measure_id,
                    "name": measure["name"],
                    "reason": "Implementation effort disproportionate to data sensitivity",
                }
            )
            continue

        selected.append(measure)

    by_category = {"technical": [], "contractual": [], "organisational": []}
    for m in selected:
        by_category[m["category"]].append(m)

    combined_score = sum(
        EFFECTIVENESS_WEIGHTS.get(m["effectiveness"], 0) for m in selected
    )
    max_possible = sum(
        EFFECTIVENESS_WEIGHTS.get(m["effectiveness"], 0)
        for m in MEASURES_CATALOGUE.values()
        if any(eeg in gap_eegs for eeg in m["addresses_eegs"])
    )

    has_technical = len(by_category["technical"]) > 0
    has_high_effectiveness = any(
        m["effectiveness"] in ("high", "complete") for m in selected
    )

    if risk_level in ("high", "very-high") and not has_high_effectiveness:
        sufficient = False
        conclusion = (
            "INSUFFICIENT: High-risk jurisdiction requires at least one high-effectiveness "
            "technical measure. Consider encryption with EU-held keys or pseudonymisation."
        )
    elif not has_technical and risk_level != "low":
        sufficient = False
        conclusion = (
            "INSUFFICIENT: No technical measures selected. At minimum, transport-layer "
            "encryption must be implemented."
        )
    else:
        sufficient = True
        conclusion = (
            "Selected measures provide a reasonable combination of technical, contractual, "
            "and organisational safeguards to bridge the identified protection gaps."
        )

    return {
        "selection_date": datetime.utcnow().isoformat(),
        "identified_gaps": len(eeg_gaps),
        "gap_eegs": list(gap_eegs),
        "data_sensitivity": data_sensitivity,
        "risk_level": risk_level,
        "importer_needs_plaintext": importer_needs_plaintext,
        "selected_measures": by_category,
        "excluded_measures": excluded,
        "total_selected": len(selected),
        "combined_effectiveness_score": combined_score,
        "max_possible_score": max_possible,
        "sufficient": sufficient,
        "conclusion": conclusion,
    }


def track_implementation(measures_plan: list) -> dict:
    """Track implementation status of selected supplementary measures."""
    total = len(measures_plan)
    implemented = 0
    in_progress = 0
    not_started = 0
    overdue = []

    now = datetime.utcnow()

    for m in measures_plan:
        status = m.get("status", "not_started")
        if status == "implemented":
            implemented += 1
        elif status == "in_progress":
            in_progress += 1
        else:
            not_started += 1

        target_date = m.get("target_date")
        if target_date and status != "implemented":
            target = datetime.strptime(target_date, "%Y-%m-%d")
            if target < now:
                overdue.append(
                    {
                        "measure_id": m["id"],
                        "name": m["name"],
                        "target_date": target_date,
                        "days_overdue": (now - target).days,
                    }
                )

    return {
        "tracking_date": now.strftime("%Y-%m-%d"),
        "total_measures": total,
        "implemented": implemented,
        "in_progress": in_progress,
        "not_started": not_started,
        "completion_pct": round(implemented / total * 100, 1) if total else 0,
        "overdue": overdue,
        "transfer_permitted": implemented == total,
        "recommendation": "All measures implemented — transfer may proceed"
        if implemented == total
        else f"{total - implemented} measure(s) remaining — transfer must not proceed until complete",
    }


def assess_combined_effectiveness(
    selected_measures: list, destination_risk: str
) -> dict:
    """Assess the combined effectiveness of the selected supplementary measures package."""
    score = sum(
        EFFECTIVENESS_WEIGHTS.get(m.get("effectiveness", "low"), 0)
        for m in selected_measures
    )

    risk_threshold = {
        "low": 2,
        "low-medium": 4,
        "medium": 6,
        "medium-high": 10,
        "high": 14,
        "very-high": 20,
    }

    threshold = risk_threshold.get(destination_risk, 10)
    meets_threshold = score >= threshold

    prevents_disclosure = any(
        m.get("prevents_compelled_disclosure", False) for m in selected_measures
    )

    return {
        "assessment_date": datetime.utcnow().isoformat(),
        "total_measures": len(selected_measures),
        "combined_score": score,
        "risk_threshold": threshold,
        "destination_risk": destination_risk,
        "meets_threshold": meets_threshold,
        "prevents_compelled_disclosure": prevents_disclosure,
        "verdict": "EFFECTIVE"
        if meets_threshold and prevents_disclosure
        else "EFFECTIVE (with residual risk)"
        if meets_threshold
        else "INEFFECTIVE — transfer must be suspended",
    }


if __name__ == "__main__":
    print("=== Measure Selection ===")
    gaps = [
        {"eeg_id": "eeg_2", "criterion": "Proportionality of access scope"},
        {"eeg_id": "eeg_3", "criterion": "Oversight body independence"},
        {"eeg_id": "eeg_4", "criterion": "Notification mechanism"},
    ]
    selection = select_measures(
        eeg_gaps=gaps,
        importer_needs_plaintext=True,
        data_sensitivity="medium",
        risk_level="medium",
    )
    print(json.dumps(selection, indent=2))

    print("\n=== Implementation Tracking ===")
    plan = [
        {"id": "T4", "name": "TLS 1.3", "status": "implemented", "target_date": "2025-03-01"},
        {"id": "C1", "name": "Challenge obligation", "status": "implemented", "target_date": "2025-03-15"},
        {"id": "C2", "name": "Transparency", "status": "in_progress", "target_date": "2025-03-20"},
        {"id": "O1", "name": "Access policies", "status": "not_started", "target_date": "2025-04-01"},
    ]
    tracking = track_implementation(plan)
    print(json.dumps(tracking, indent=2))
