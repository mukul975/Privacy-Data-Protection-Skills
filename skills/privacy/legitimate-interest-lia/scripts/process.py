#!/usr/bin/env python3
"""
Legitimate Interest Assessment (LIA) Tool

Implements the three-part LIA test under GDPR Art. 6(1)(f):
1. Purpose test — Is the interest legitimate?
2. Necessity test — Is the processing necessary?
3. Balancing test — Do data subject rights override?
"""

import json
import sys
from datetime import datetime
from typing import Any


IMPACT_SCORES = {
    "negligible": 1,
    "minor": 2,
    "moderate": 3,
    "significant": 4,
    "severe": 5,
}

INTEREST_STRENGTH = {
    "low": 1,
    "moderate": 2,
    "high": 3,
    "essential": 4,
}

RECOGNISED_INTERESTS = [
    "fraud prevention",
    "direct marketing to existing customers",
    "network and information security",
    "intra-group administrative transfers",
    "physical security",
    "reporting criminal acts",
    "exercise of freedom of expression",
    "research and statistics",
    "debt recovery",
    "employee monitoring for security",
]


def run_purpose_test(lia_input: dict) -> dict:
    purpose = lia_input.get("purpose_test", {})
    result = {
        "test": "Purpose Test",
        "outcome": "FAIL",
        "rationale": "",
        "issues": [],
    }

    interest = purpose.get("interest_description", "")
    if not interest or len(interest.strip()) < 10:
        result["issues"].append(
            "The legitimate interest has not been articulated or is too vague. "
            "Provide a clear, specific description of the interest pursued."
        )
        result["rationale"] = "No legitimate interest identified."
        return result

    is_lawful = purpose.get("interest_is_lawful", True)
    if not is_lawful:
        result["issues"].append("The stated interest is prohibited by applicable law.")
        result["rationale"] = "Interest is unlawful and cannot form the basis of Art. 6(1)(f)."
        return result

    vague_terms = ["improve business", "general purposes", "various needs", "business operations"]
    for term in vague_terms:
        if term.lower() in interest.lower():
            result["issues"].append(
                f"Interest description contains vague language: '{term}'. "
                f"The interest must be specific and concrete."
            )

    if result["issues"]:
        result["rationale"] = "Interest articulation needs improvement before the purpose test can pass."
        return result

    recognised = any(ri in interest.lower() for ri in RECOGNISED_INTERESTS)
    recognition_note = ""
    if recognised:
        recognition_note = " This interest is recognised in GDPR recitals/case law, strengthening the position."

    result["outcome"] = "PASS"
    result["rationale"] = (
        f"A legitimate interest has been clearly identified: '{interest}'. "
        f"The interest is lawful, specific, and present.{recognition_note}"
    )
    return result


def run_necessity_test(lia_input: dict) -> dict:
    necessity = lia_input.get("necessity_test", {})
    result = {
        "test": "Necessity Test",
        "outcome": "FAIL",
        "rationale": "",
        "issues": [],
    }

    can_achieve_without_data = necessity.get("can_achieve_without_personal_data", False)
    if can_achieve_without_data:
        result["issues"].append(
            "The interest can be achieved without processing personal data. "
            "Processing fails the necessity test."
        )
        result["rationale"] = "Processing is not necessary — the interest can be achieved without personal data."
        return result

    less_intrusive_available = necessity.get("less_intrusive_alternative_available", False)
    alternative_desc = necessity.get("alternative_description", "")
    if less_intrusive_available:
        result["issues"].append(
            f"A less intrusive alternative is available: {alternative_desc}. "
            f"Processing cannot be justified when a less invasive means exists."
        )
        result["rationale"] = f"Less intrusive alternative available: {alternative_desc}."
        return result

    data_minimised = necessity.get("data_minimised", False)
    if not data_minimised:
        result["issues"].append(
            "Data minimisation has not been confirmed. Verify that only the minimum "
            "necessary personal data is processed."
        )

    proportionate = necessity.get("processing_proportionate", True)
    if not proportionate:
        result["issues"].append(
            "Processing scope is disproportionate to the stated interest. "
            "Reduce the volume, granularity, or duration of processing."
        )

    if result["issues"]:
        result["rationale"] = "Necessity test has outstanding issues that must be resolved."
        return result

    result["outcome"] = "PASS"
    result["rationale"] = (
        "Processing is necessary for the stated legitimate interest. "
        "No less intrusive alternative achieves the same result. "
        "Data minimisation principles have been applied."
    )
    return result


def run_balancing_test(lia_input: dict) -> dict:
    balancing = lia_input.get("balancing_test", {})
    result = {
        "test": "Balancing Test",
        "outcome": "FAIL",
        "rationale": "",
        "issues": [],
        "score_detail": {},
    }

    interest_strength = balancing.get("interest_strength", "moderate")
    controller_score = INTEREST_STRENGTH.get(interest_strength, 2)

    impact_ratings = balancing.get("data_subject_impact", {})
    impact_scores = []
    for impact_type, rating in impact_ratings.items():
        score = IMPACT_SCORES.get(rating, 3)
        impact_scores.append(score)

    avg_impact = sum(impact_scores) / len(impact_scores) if impact_scores else 3

    vulnerability_factor = 0
    involves_children = balancing.get("involves_children", False)
    involves_vulnerable = balancing.get("involves_vulnerable_persons", False)
    involves_sensitive = balancing.get("involves_sensitive_data", False)

    if involves_children:
        vulnerability_factor += 2
        result["issues"].append(
            "Processing involves children's data — Art. 6(1)(f) provides heightened protection for minors."
        )
    if involves_vulnerable:
        vulnerability_factor += 1
        result["issues"].append(
            "Processing involves vulnerable persons — additional weight given to data subject interests."
        )
    if involves_sensitive:
        vulnerability_factor += 1.5
        result["issues"].append(
            "Processing involves sensitive data categories — strong presumption in favour of data subject."
        )

    reasonable_expectation = balancing.get("data_subjects_expect_processing", True)
    expectation_factor = 0 if reasonable_expectation else 1

    safeguards = balancing.get("safeguards", [])
    safeguard_mitigation = min(len(safeguards) * 0.3, 2.0)

    has_opt_out = balancing.get("opt_out_available", False)
    opt_out_factor = 0.5 if has_opt_out else 0

    adjusted_impact = avg_impact + vulnerability_factor + expectation_factor - safeguard_mitigation - opt_out_factor

    result["score_detail"] = {
        "controller_interest_score": controller_score,
        "average_impact_score": round(avg_impact, 2),
        "vulnerability_adjustment": vulnerability_factor,
        "expectation_adjustment": expectation_factor,
        "safeguard_mitigation": round(safeguard_mitigation, 2),
        "opt_out_mitigation": opt_out_factor,
        "adjusted_impact_score": round(adjusted_impact, 2),
        "interpretation": (
            f"Controller interest ({interest_strength}={controller_score}) vs "
            f"Adjusted data subject impact ({round(adjusted_impact, 2)})"
        ),
    }

    if controller_score >= adjusted_impact:
        result["outcome"] = "PASS"
        result["rationale"] = (
            f"The controller's legitimate interest (strength: {interest_strength}) "
            f"is not overridden by the data subject's interests after accounting for "
            f"{len(safeguards)} safeguard(s) and impact assessment. "
            f"Balance: controller score {controller_score} >= adjusted impact {round(adjusted_impact, 2)}."
        )
    else:
        result["outcome"] = "FAIL"
        result["rationale"] = (
            f"The data subject's interests, rights, and freedoms override the controller's "
            f"legitimate interest. Adjusted impact score ({round(adjusted_impact, 2)}) exceeds "
            f"controller interest score ({controller_score}). Consider additional safeguards, "
            f"consent as an alternative basis, or do not process."
        )

    return result


def run_lia(lia_input: dict) -> dict:
    assessment = {
        "activity_name": lia_input.get("activity_name", "Unnamed"),
        "ropa_reference": lia_input.get("ropa_reference", ""),
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "assessor": lia_input.get("assessor", ""),
        "tests": [],
        "overall_outcome": "FAIL",
        "overall_rationale": "",
        "safeguards_committed": lia_input.get("balancing_test", {}).get("safeguards", []),
    }

    purpose_result = run_purpose_test(lia_input)
    assessment["tests"].append(purpose_result)

    if purpose_result["outcome"] == "FAIL":
        assessment["overall_rationale"] = (
            "LIA failed at the purpose test. No legitimate interest could be established. "
            "Art. 6(1)(f) cannot be relied upon."
        )
        return assessment

    necessity_result = run_necessity_test(lia_input)
    assessment["tests"].append(necessity_result)

    if necessity_result["outcome"] == "FAIL":
        assessment["overall_rationale"] = (
            "LIA failed at the necessity test. The processing is not necessary for the "
            "stated legitimate interest. Art. 6(1)(f) cannot be relied upon."
        )
        return assessment

    balancing_result = run_balancing_test(lia_input)
    assessment["tests"].append(balancing_result)

    if balancing_result["outcome"] == "FAIL":
        assessment["overall_rationale"] = (
            "LIA failed at the balancing test. Data subject rights override the controller's "
            "interest. Consider consent or do not process."
        )
        return assessment

    assessment["overall_outcome"] = "PASS"
    assessment["overall_rationale"] = (
        "All three LIA tests passed. Art. 6(1)(f) legitimate interests can be relied upon "
        "as the lawful basis, subject to implementation of committed safeguards and ongoing "
        "facilitation of the Art. 21 right to object."
    )
    return assessment


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <lia_input.json>")
        print("\nExample input:")
        example = {
            "activity_name": "Website analytics using first-party cookies",
            "ropa_reference": "RPA-034",
            "assessor": "Dr. Katharina Weiss",
            "purpose_test": {
                "interest_description": "Analysis of aggregate website visitor behaviour to optimise user experience and conversion rates",
                "interest_is_lawful": True,
            },
            "necessity_test": {
                "can_achieve_without_personal_data": False,
                "less_intrusive_alternative_available": False,
                "data_minimised": True,
                "processing_proportionate": True,
            },
            "balancing_test": {
                "interest_strength": "moderate",
                "data_subject_impact": {
                    "financial": "negligible",
                    "emotional": "negligible",
                    "social": "negligible",
                    "loss_of_control": "minor",
                },
                "involves_children": False,
                "involves_vulnerable_persons": False,
                "involves_sensitive_data": False,
                "data_subjects_expect_processing": True,
                "opt_out_available": True,
                "safeguards": [
                    "IP anonymisation enabled",
                    "No cross-site tracking",
                    "Data retained for 14 months only",
                    "Server-side processing in EU",
                    "Cookie consent banner with opt-out",
                ],
            },
        }
        print(json.dumps(example, indent=2))
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        lia_input = json.load(f)

    result = run_lia(lia_input)
    print(json.dumps(result, indent=2))

    sys.exit(0 if result["overall_outcome"] == "PASS" else 2)


if __name__ == "__main__":
    main()
