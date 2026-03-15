#!/usr/bin/env python3
"""
Art. 30(5) Exemption Assessor

Assesses whether an organisation qualifies for the GDPR Article 30(5)
exemption from RoPA obligations. Evaluates the three exception conditions:
risk to rights, non-occasional processing, and special category data.
"""

import json
import sys
from datetime import datetime
from typing import Any


SPECIAL_CATEGORY_KEYWORDS = [
    "health", "medical", "sick", "illness", "disability", "diagnosis",
    "genetic", "dna", "genome", "biomarker",
    "biometric", "fingerprint", "facial recognition", "iris",
    "racial", "ethnic", "ethnicity", "race",
    "religion", "religious", "church", "faith", "belief",
    "political", "party affiliation",
    "trade union", "union membership",
    "sexual orientation", "sex life",
]

CRIMINAL_DATA_KEYWORDS = [
    "criminal", "conviction", "offence", "arrest", "sentence",
    "background check", "police check", "CRB", "DBS",
]

NON_OCCASIONAL_INDICATORS = [
    "daily", "weekly", "monthly", "quarterly", "annually", "annual",
    "ongoing", "continuous", "regular", "recurring", "systematic",
    "routine", "standard", "normal business", "core business",
]

RISK_INDICATORS = [
    "financial", "bank", "payment", "salary", "credit card",
    "identity", "passport", "national id", "social security", "tax id",
    "location", "tracking", "monitoring", "surveillance",
    "children", "minor", "vulnerable",
    "profiling", "scoring", "automated decision",
    "large scale", "large-scale",
]


def assess_exemption(organisation: dict) -> dict:
    """Assess whether an organisation qualifies for the Art. 30(5) exemption."""
    employee_count = organisation.get("employee_count", 0)
    processing_activities = organisation.get("processing_activities", [])

    result = {
        "organisation": organisation.get("name", "Unknown"),
        "employee_count": employee_count,
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "threshold_met": employee_count < 250,
        "activities_assessed": len(processing_activities),
        "activity_results": [],
        "overall_exemption_available": False,
        "recommendation": "",
    }

    if employee_count >= 250:
        result["overall_exemption_available"] = False
        result["recommendation"] = (
            f"Organisation has {employee_count} employees (>=250). "
            "Art. 30(5) exemption does NOT apply. Full RoPA required."
        )
        return result

    # Assess each processing activity
    any_non_exempt = False
    for activity in processing_activities:
        activity_name = activity.get("name", "Unknown")
        description = activity.get("description", "").lower()
        data_categories = " ".join(activity.get("data_categories", [])).lower()
        frequency = activity.get("frequency", "").lower()
        all_text = f"{description} {data_categories} {frequency}"

        # Condition 1: Risk to rights and freedoms
        risk_found = False
        risk_reasons = []
        for indicator in RISK_INDICATORS:
            if indicator in all_text:
                risk_found = True
                risk_reasons.append(f"Contains risk indicator: '{indicator}'")

        if activity.get("involves_financial_data"):
            risk_found = True
            risk_reasons.append("Involves financial data")

        if activity.get("involves_identification_data"):
            risk_found = True
            risk_reasons.append("Involves identification data")

        # Condition 2: Not occasional
        not_occasional = False
        occasional_reasons = []
        for indicator in NON_OCCASIONAL_INDICATORS:
            if indicator in all_text:
                not_occasional = True
                occasional_reasons.append(f"Frequency indicator: '{indicator}'")

        if activity.get("is_core_business", False):
            not_occasional = True
            occasional_reasons.append("Marked as core business activity")

        if frequency in ("daily", "weekly", "monthly", "continuous", "ongoing"):
            not_occasional = True
            occasional_reasons.append(f"Frequency: {frequency}")

        # Condition 3: Special category or criminal data
        special_category = False
        special_reasons = []
        for keyword in SPECIAL_CATEGORY_KEYWORDS:
            if keyword in all_text:
                special_category = True
                special_reasons.append(f"Special category indicator: '{keyword}'")

        for keyword in CRIMINAL_DATA_KEYWORDS:
            if keyword in all_text:
                special_category = True
                special_reasons.append(f"Criminal data indicator: '{keyword}'")

        if activity.get("involves_special_category", False):
            special_category = True
            special_reasons.append("Explicitly marked as special category")

        # Determine exemption for this activity
        exempt = not (risk_found or not_occasional or special_category)
        if not exempt:
            any_non_exempt = True

        activity_result = {
            "activity": activity_name,
            "condition_1_risk": risk_found,
            "condition_1_reasons": risk_reasons,
            "condition_2_not_occasional": not_occasional,
            "condition_2_reasons": occasional_reasons,
            "condition_3_special_category": special_category,
            "condition_3_reasons": special_reasons,
            "conditions_met": sum([risk_found, not_occasional, special_category]),
            "exempt": exempt,
            "ropa_required": not exempt or True,  # Always recommended
        }
        result["activity_results"].append(activity_result)

    # Overall assessment
    exempt_activities = sum(1 for a in result["activity_results"] if a["exempt"])
    non_exempt_activities = sum(1 for a in result["activity_results"] if not a["exempt"])

    result["exempt_activities"] = exempt_activities
    result["non_exempt_activities"] = non_exempt_activities

    if non_exempt_activities == 0 and exempt_activities > 0:
        result["overall_exemption_available"] = True
        result["recommendation"] = (
            "All assessed processing activities qualify for the Art. 30(5) exemption. "
            "However, the EDPB recommends maintaining RoPA regardless of size for accountability purposes. "
            "Recommendation: maintain a simplified RoPA."
        )
    else:
        result["overall_exemption_available"] = False
        result["recommendation"] = (
            f"{non_exempt_activities} of {len(processing_activities)} processing activities "
            "do NOT qualify for the Art. 30(5) exemption. RoPA is required for these activities. "
            "Recommendation: maintain a complete RoPA for all processing activities."
        )

    return result


def create_sample_assessment() -> dict:
    """Create a sample assessment for Helix Biotech Diagnostics S.A.S."""
    return {
        "name": "Helix Biotech Diagnostics S.A.S.",
        "employee_count": 45,
        "country": "France",
        "processing_activities": [
            {
                "name": "Employee payroll processing",
                "description": "Monthly calculation and disbursement of employee salaries, tax reporting to Direction Generale des Finances Publiques",
                "data_categories": ["Name", "Tax ID", "Bank account IBAN", "Salary", "Social security number"],
                "frequency": "monthly",
                "is_core_business": True,
                "involves_financial_data": True,
                "involves_identification_data": True,
                "involves_special_category": False,
            },
            {
                "name": "Employee HR records",
                "description": "Maintenance of employee personnel files including sick leave records, annual leave, performance reviews",
                "data_categories": ["Name", "Date of birth", "Address", "Sick leave records", "Health certificate"],
                "frequency": "ongoing",
                "is_core_business": True,
                "involves_financial_data": False,
                "involves_identification_data": True,
                "involves_special_category": True,
            },
            {
                "name": "Diagnostic service customer management",
                "description": "Processing of customer orders for diagnostic laboratory services including sample tracking and health result reporting",
                "data_categories": ["Patient name", "Date of birth", "Diagnosis codes", "Laboratory results", "Medical history"],
                "frequency": "daily",
                "is_core_business": True,
                "involves_financial_data": False,
                "involves_identification_data": True,
                "involves_special_category": True,
            },
            {
                "name": "Supplier management",
                "description": "Processing of supplier contact details and payment information for laboratory reagent procurement",
                "data_categories": ["Supplier contact name", "Email", "Phone", "Bank account for payment"],
                "frequency": "weekly",
                "is_core_business": True,
                "involves_financial_data": True,
                "involves_identification_data": False,
                "involves_special_category": False,
            },
            {
                "name": "Website contact form",
                "description": "Collection of enquiries via website contact form on helix-diagnostics.fr",
                "data_categories": ["Name", "Email", "Phone", "Message content"],
                "frequency": "daily",
                "is_core_business": False,
                "involves_financial_data": False,
                "involves_identification_data": False,
                "involves_special_category": False,
            },
            {
                "name": "One-time office relocation data collection",
                "description": "One-time collection of employee home addresses for office relocation commute impact assessment",
                "data_categories": ["Employee name", "Home address"],
                "frequency": "one-time",
                "is_core_business": False,
                "involves_financial_data": False,
                "involves_identification_data": False,
                "involves_special_category": False,
            },
        ],
    }


def generate_report(assessment: dict) -> str:
    """Generate a formatted assessment report."""
    lines = []
    lines.append("=" * 70)
    lines.append("ART. 30(5) EXEMPTION ASSESSMENT REPORT")
    lines.append(f"Organisation: {assessment['organisation']}")
    lines.append(f"Employee Count: {assessment['employee_count']}")
    lines.append(f"Assessment Date: {assessment['assessment_date']}")
    lines.append("=" * 70)

    lines.append(f"\nEmployee threshold (<250): {'MET' if assessment['threshold_met'] else 'NOT MET'}")

    if not assessment["threshold_met"]:
        lines.append("\nRESULT: Exemption NOT available. Full RoPA required.")
        lines.append(f"\n{assessment['recommendation']}")
        return "\n".join(lines)

    lines.append(f"\nProcessing activities assessed: {assessment['activities_assessed']}")
    lines.append(f"Activities qualifying for exemption: {assessment.get('exempt_activities', 0)}")
    lines.append(f"Activities NOT qualifying: {assessment.get('non_exempt_activities', 0)}")

    lines.append(f"\n{'─' * 70}")
    lines.append("PER-ACTIVITY ASSESSMENT")
    lines.append(f"{'─' * 70}")

    for result in assessment["activity_results"]:
        status = "EXEMPT" if result["exempt"] else "NOT EXEMPT"
        lines.append(f"\n  {result['activity']} [{status}]")
        lines.append(f"    Conditions met: {result['conditions_met']} of 3")

        c1 = "MET" if result["condition_1_risk"] else "Not met"
        c2 = "MET" if result["condition_2_not_occasional"] else "Not met"
        c3 = "MET" if result["condition_3_special_category"] else "Not met"

        lines.append(f"    C1 (Risk to rights): {c1}")
        for r in result.get("condition_1_reasons", []):
            lines.append(f"      - {r}")

        lines.append(f"    C2 (Not occasional): {c2}")
        for r in result.get("condition_2_reasons", []):
            lines.append(f"      - {r}")

        lines.append(f"    C3 (Special category): {c3}")
        for r in result.get("condition_3_reasons", []):
            lines.append(f"      - {r}")

    lines.append(f"\n{'=' * 70}")
    lines.append("CONCLUSION")
    lines.append(f"{'=' * 70}")
    lines.append(f"Exemption available: {'YES' if assessment['overall_exemption_available'] else 'NO'}")
    lines.append(f"\n{assessment['recommendation']}")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python process.py assess <organisation.json> [--output report.txt]")
        print("  python process.py demo")
        sys.exit(1)

    command = sys.argv[1]

    if command == "demo":
        sample = create_sample_assessment()
        assessment = assess_exemption(sample)
        report = generate_report(assessment)
        print(report)

    elif command == "assess":
        if len(sys.argv) < 3:
            print("ERROR: Provide the organisation JSON file.")
            sys.exit(1)

        with open(sys.argv[2], "r", encoding="utf-8") as f:
            org_data = json.load(f)

        assessment = assess_exemption(org_data)
        report = generate_report(assessment)

        output = None
        if "--output" in sys.argv:
            idx = sys.argv.index("--output")
            if idx + 1 < len(sys.argv):
                output = sys.argv[idx + 1]

        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"Assessment report written to {output}")

            json_output = output.replace(".txt", ".json")
            with open(json_output, "w", encoding="utf-8") as f:
                json.dump(assessment, f, indent=2)
            print(f"Assessment data written to {json_output}")
        else:
            print(report)

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
