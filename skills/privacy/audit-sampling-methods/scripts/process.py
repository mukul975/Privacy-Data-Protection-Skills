#!/usr/bin/env python3
"""
Privacy Audit Sampling Methods Tool

Calculates sample sizes, evaluates sampling results, and supports
stratified sampling for privacy audit engagements.
"""

import json
import math
from typing import Optional


SAMPLE_SIZE_TABLE = {
    (90, 5): {50: 29, 100: 38, 250: 42, 500: 44, 1000: 45, 5000: 46, 10000: 46},
    (95, 5): {50: 33, 100: 45, 250: 50, 500: 54, 1000: 57, 5000: 59, 10000: 59},
    (95, 2): {50: 42, 100: 64, 250: 100, 500: 131, 1000: 154, 5000: 176, 10000: 181},
    (90, 2): {50: 38, 100: 55, 250: 82, 500: 105, 1000: 121, 5000: 138, 10000: 142},
}


def calculate_sample_size(
    population_size: int,
    confidence_level: int = 95,
    tolerable_deviation_rate: int = 5,
    expected_deviation_rate: float = 1.0,
) -> dict:
    """Calculate attribute sampling sample size using standard tables and formulas."""
    if confidence_level not in [90, 95]:
        raise ValueError("Confidence level must be 90 or 95")
    if tolerable_deviation_rate not in [2, 5]:
        raise ValueError("Tolerable deviation rate must be 2 or 5 (percent)")

    z_scores = {90: 1.645, 95: 1.960}
    z = z_scores[confidence_level]
    p = expected_deviation_rate / 100.0
    e = tolerable_deviation_rate / 100.0

    if p >= e:
        raise ValueError("Expected deviation rate must be less than tolerable deviation rate")

    n_infinite = math.ceil((z ** 2 * p * (1 - p)) / (e ** 2))
    n_adjusted = math.ceil(n_infinite / (1 + (n_infinite - 1) / population_size))

    table_key = (confidence_level, tolerable_deviation_rate)
    table_n = None
    if table_key in SAMPLE_SIZE_TABLE:
        table = SAMPLE_SIZE_TABLE[table_key]
        for threshold in sorted(table.keys()):
            if population_size <= threshold:
                table_n = table[threshold]
                break
        if table_n is None:
            table_n = table[max(table.keys())]

    recommended = max(n_adjusted, table_n or 0, 25)

    return {
        "population_size": population_size,
        "confidence_level_pct": confidence_level,
        "tolerable_deviation_rate_pct": tolerable_deviation_rate,
        "expected_deviation_rate_pct": expected_deviation_rate,
        "formula_sample_size": n_adjusted,
        "table_sample_size": table_n,
        "recommended_sample_size": recommended,
        "sampling_fraction_pct": round(recommended / population_size * 100, 1),
    }


def evaluate_sample_results(
    sample_size: int,
    deviations_found: int,
    population_size: int,
    tolerable_deviation_rate: float = 5.0,
) -> dict:
    """Evaluate attribute sampling results and determine conclusion."""
    sample_deviation_rate = round(deviations_found / sample_size * 100, 2) if sample_size > 0 else 0

    projected_deviations = round(sample_deviation_rate / 100 * population_size)

    if sample_deviation_rate < tolerable_deviation_rate * 0.5:
        conclusion = "compliant"
        finding_required = False
        recommendation = "No material finding. Population is likely compliant."
    elif sample_deviation_rate < tolerable_deviation_rate:
        conclusion = "compliant_with_observations"
        finding_required = False
        recommendation = "Population is likely compliant but deviations noted. Consider targeted follow-up."
    elif sample_deviation_rate == tolerable_deviation_rate:
        conclusion = "borderline"
        finding_required = True
        recommendation = "Borderline result. Expand sample or raise as medium finding."
    else:
        conclusion = "non_compliant"
        finding_required = True
        recommendation = f"Material non-compliance detected. Projected {projected_deviations} deviations in population of {population_size}."

    return {
        "sample_size": sample_size,
        "deviations_found": deviations_found,
        "sample_deviation_rate_pct": sample_deviation_rate,
        "tolerable_deviation_rate_pct": tolerable_deviation_rate,
        "population_size": population_size,
        "projected_population_deviations": projected_deviations,
        "conclusion": conclusion,
        "finding_required": finding_required,
        "recommendation": recommendation,
    }


def design_stratified_sample(
    strata: list,
    total_sample_size: int,
    allocation_method: str = "proportional",
) -> dict:
    """Design a stratified sample with proportional or risk-weighted allocation."""
    total_population = sum(s["population"] for s in strata)

    result_strata = []
    allocated = 0

    for i, stratum in enumerate(strata):
        if allocation_method == "proportional":
            fraction = stratum["population"] / total_population
        elif allocation_method == "risk_weighted":
            risk_weight = stratum.get("risk_weight", 1)
            total_weight = sum(s.get("risk_weight", 1) * s["population"] for s in strata)
            fraction = (risk_weight * stratum["population"]) / total_weight
        else:
            raise ValueError(f"Unknown allocation method: {allocation_method}")

        if i == len(strata) - 1:
            sample_n = total_sample_size - allocated
        else:
            sample_n = round(total_sample_size * fraction)

        allocated += sample_n

        result_strata.append({
            "stratum_name": stratum["name"],
            "population": stratum["population"],
            "sample_size": sample_n,
            "sampling_fraction_pct": round(sample_n / stratum["population"] * 100, 1) if stratum["population"] > 0 else 0,
        })

    return {
        "total_population": total_population,
        "total_sample_size": total_sample_size,
        "allocation_method": allocation_method,
        "strata": result_strata,
    }


def recommend_sampling_approach(
    population_size: int,
    is_critical_control: bool,
    regulatory_facing: bool,
) -> dict:
    """Recommend sampling approach and parameters based on context."""
    if population_size <= 20:
        approach = "100% testing"
        confidence = None
        tolerable = None
        rationale = "Population is small enough for complete testing"
    elif population_size <= 50 and not regulatory_facing:
        approach = "non-statistical"
        confidence = None
        tolerable = None
        rationale = "Small population; judgemental selection appropriate for internal purposes"
    else:
        approach = "statistical"
        confidence = 95 if (is_critical_control or regulatory_facing) else 90
        tolerable = 2 if is_critical_control else 5
        rationale = "Large population requires statistical sampling for defensible conclusions"

    return {
        "population_size": population_size,
        "is_critical_control": is_critical_control,
        "regulatory_facing": regulatory_facing,
        "recommended_approach": approach,
        "confidence_level": confidence,
        "tolerable_deviation_rate": tolerable,
        "rationale": rationale,
    }


if __name__ == "__main__":
    print("=== Sample Size Calculation ===")
    size = calculate_sample_size(
        population_size=1000,
        confidence_level=95,
        tolerable_deviation_rate=5,
        expected_deviation_rate=1.0,
    )
    print(json.dumps(size, indent=2))

    print("\n=== Sample Results Evaluation ===")
    results = evaluate_sample_results(
        sample_size=57,
        deviations_found=5,
        population_size=1000,
        tolerable_deviation_rate=5.0,
    )
    print(json.dumps(results, indent=2))

    print("\n=== Stratified Sample Design ===")
    strata = [
        {"name": "EU vendors", "population": 500, "risk_weight": 3},
        {"name": "US vendors", "population": 450, "risk_weight": 2},
        {"name": "APAC vendors", "population": 250, "risk_weight": 1},
    ]
    stratified = design_stratified_sample(strata, total_sample_size=60, allocation_method="risk_weighted")
    print(json.dumps(stratified, indent=2))

    print("\n=== Sampling Approach Recommendation ===")
    rec = recommend_sampling_approach(
        population_size=500,
        is_critical_control=True,
        regulatory_facing=True,
    )
    print(json.dumps(rec, indent=2))
