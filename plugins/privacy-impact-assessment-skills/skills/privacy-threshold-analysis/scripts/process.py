#!/usr/bin/env python3
"""Privacy Threshold Analysis Screening Engine.

Implements the PTA quick-screen questionnaire and decision matrix
for determining whether a full DPIA is required.
"""

import json
from datetime import datetime
from typing import Any


def conduct_pta(
    reference: str,
    processing_name: str,
    processing_owner: str,
    section_a: dict[str, bool],
    section_b: dict[str, bool],
    section_c: dict[str, bool],
) -> dict[str, Any]:
    """Conduct a Privacy Threshold Analysis.

    Args:
        reference: PTA reference number
        processing_name: Name of the processing activity
        processing_owner: Name and role of the processing owner
        section_a: Art. 35(3) mandatory triggers (A1-A4)
        section_b: WP248 criteria (B1-B9)
        section_c: Additional risk factors (C1-C4)

    Returns:
        PTA result with determination
    """
    # Section A: Mandatory triggers
    a_triggers = [k for k, v in section_a.items() if v]
    mandatory_dpia = len(a_triggers) > 0

    # Section B: EDPB criteria
    b_criteria = [k for k, v in section_b.items() if v]
    b_count = len(b_criteria)

    # Section C: Additional factors
    c_factors = [k for k, v in section_c.items() if v]
    c_count = len(c_factors)

    # Determination
    if mandatory_dpia:
        determination = "DPIA mandatory"
        rationale = f"Art. 35(3) mandatory trigger(s) met: {', '.join(a_triggers)}"
    elif b_count >= 2:
        determination = "DPIA strongly recommended"
        rationale = f"{b_count} EDPB WP248rev.01 criteria met (threshold: 2): {', '.join(b_criteria)}"
    elif b_count == 1 and c_count >= 1:
        determination = "DPIA recommended"
        rationale = f"1 EDPB criterion met ({b_criteria[0]}) plus {c_count} additional risk factor(s)"
    elif b_count == 1:
        determination = "DPO consultation recommended"
        rationale = f"1 EDPB criterion met ({b_criteria[0]}) with no additional risk factors"
    elif c_count >= 1:
        determination = "Document screening; monitor"
        rationale = f"No EDPB criteria met but {c_count} additional risk factor(s) present"
    else:
        determination = "DPIA not required"
        rationale = "No Art. 35(3) triggers, no EDPB criteria, and no additional risk factors"

    return {
        "reference": reference,
        "processing_name": processing_name,
        "processing_owner": processing_owner,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "section_a": {
            "triggers_met": a_triggers,
            "mandatory_dpia": mandatory_dpia,
        },
        "section_b": {
            "criteria_met": b_criteria,
            "criteria_count": b_count,
        },
        "section_c": {
            "factors_present": c_factors,
            "factor_count": c_count,
        },
        "determination": determination,
        "rationale": rationale,
        "next_steps": (
            "Initiate full DPIA process. Processing must not commence until DPIA is completed."
            if "mandatory" in determination.lower() or "strongly recommended" in determination.lower()
            else "DPO to review and make final determination."
            if "recommended" in determination.lower() or "consultation" in determination.lower()
            else "Document PTA outcome. Processing may proceed subject to standard controls."
        ),
    }


def run_example() -> dict[str, Any]:
    """Run example PTA for QuantumLeap Health Technologies."""
    return conduct_pta(
        reference="PTA-QLH-2026-0015",
        processing_name="Patient Satisfaction Survey Analytics Dashboard",
        processing_owner="Dr. Lisa Bergmann, Head of Clinical Operations",
        section_a={
            "A1": False,  # No systematic profiling with significant effects
            "A2": False,  # No large-scale special category (survey is pseudonymised)
            "A3": False,  # No public area monitoring
            "A4": False,  # Not on national SA list
        },
        section_b={
            "B1": False,  # No evaluation/scoring of patients
            "B2": False,  # No automated decisions
            "B3": False,  # No systematic monitoring
            "B4": False,  # Survey responses are not special category (satisfaction ratings)
            "B5": False,  # 4,000 surveys/year — not large scale
            "B6": False,  # Single data source (survey platform)
            "B7": True,   # Patients are vulnerable data subjects
            "B8": False,  # Standard survey technology
            "B9": False,  # Does not prevent exercise of rights
        },
        section_c={
            "C1": False,  # No international transfers
            "C2": True,   # New processing activity
            "C3": False,  # No enforcement against similar processing
            "C4": False,  # No real-time processing
        },
    )


if __name__ == "__main__":
    result = run_example()
    print(json.dumps(result, indent=2, default=str))
