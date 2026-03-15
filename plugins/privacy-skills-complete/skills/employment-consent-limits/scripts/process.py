"""
Employment Consent Limits Assessment Engine

Evaluates whether consent is a valid lawful basis for specific employment
processing activities. Implements WP29 Opinion 2/2017, EDPB Guidelines
05/2020, and national Art. 88 derogation checks.
"""

import json
from datetime import datetime
from typing import Optional


# Lawful basis hierarchy for employment processing
LAWFUL_BASES = {
    "art_6_1_c": {
        "name": "Art. 6(1)(c) — Legal Obligation",
        "priority": 1,
        "description": "Processing required by EU or Member State law",
    },
    "art_6_1_b": {
        "name": "Art. 6(1)(b) — Contract Performance",
        "priority": 2,
        "description": "Processing necessary for performance of the employment contract",
    },
    "art_6_1_e": {
        "name": "Art. 6(1)(e) — Public Interest",
        "priority": 3,
        "description": "Processing for a public task (public sector employers)",
    },
    "art_6_1_f": {
        "name": "Art. 6(1)(f) — Legitimate Interest",
        "priority": 4,
        "description": "Processing necessary for employer legitimate interest, subject to balancing test",
    },
    "art_6_1_a": {
        "name": "Art. 6(1)(a) — Consent",
        "priority": 5,
        "description": "Freely given, specific, informed consent (rarely valid in employment)",
    },
}

# Common employment processing activities and their recommended lawful bases
PROCESSING_ACTIVITIES = {
    "payroll": {
        "description": "Payroll processing and salary payments",
        "recommended_basis": "art_6_1_b",
        "consent_valid": False,
        "reason": "Payroll is necessary for contract performance — consent is unnecessary and inappropriate.",
    },
    "tax_reporting": {
        "description": "Tax withholding and reporting to tax authorities",
        "recommended_basis": "art_6_1_c",
        "consent_valid": False,
        "reason": "Tax reporting is a legal obligation — no lawful basis choice exists.",
    },
    "social_security": {
        "description": "Social security contributions and reporting",
        "recommended_basis": "art_6_1_c",
        "consent_valid": False,
        "reason": "Social security is a legal obligation.",
    },
    "working_time_recording": {
        "description": "Recording employee working hours",
        "recommended_basis": "art_6_1_c",
        "consent_valid": False,
        "reason": "CJEU C-55/18 (CCOO v Deutsche Bank) confirms working time recording is a legal obligation under Working Time Directive.",
    },
    "performance_management": {
        "description": "Performance reviews and objective setting",
        "recommended_basis": "art_6_1_b",
        "consent_valid": False,
        "reason": "Performance management is necessary for the employment contract.",
    },
    "absence_management": {
        "description": "Recording and managing employee absences",
        "recommended_basis": "art_6_1_b",
        "consent_valid": False,
        "reason": "Absence management is necessary for contract performance and statutory sick pay.",
    },
    "right_to_work": {
        "description": "Immigration right-to-work verification",
        "recommended_basis": "art_6_1_c",
        "consent_valid": False,
        "reason": "Right-to-work checks are a legal obligation under immigration law.",
    },
    "employee_monitoring": {
        "description": "Email, internet, CCTV, or productivity monitoring",
        "recommended_basis": "art_6_1_f",
        "consent_valid": False,
        "reason": "Monitoring cannot be based on consent due to power imbalance. Legitimate interest with balancing test is the appropriate basis.",
    },
    "background_check_criminal": {
        "description": "Criminal record background checks",
        "recommended_basis": "art_6_1_c",
        "consent_valid": False,
        "reason": "Art. 10 requires national law authorisation for criminal data processing.",
    },
    "wellness_programme": {
        "description": "Voluntary employee wellness programme with health data",
        "recommended_basis": "art_6_1_a",
        "consent_valid": True,
        "reason": "Wellness programmes are genuinely voluntary with no employment consequences. Consent may be valid if safeguards are in place.",
    },
    "employee_photo_directory": {
        "description": "Optional employee photo directory / intranet profile",
        "recommended_basis": "art_6_1_a",
        "consent_valid": True,
        "reason": "Participation is genuinely optional. Consent is valid if non-participation has no consequences.",
    },
    "social_media_screening": {
        "description": "Screening candidate social media profiles during recruitment",
        "recommended_basis": "art_6_1_f",
        "consent_valid": False,
        "reason": "Candidates cannot freely consent during recruitment. If justified at all, legitimate interest with strict balancing test.",
    },
    "reference_request": {
        "description": "Employee-initiated reference letter request",
        "recommended_basis": "art_6_1_a",
        "consent_valid": True,
        "reason": "Employee initiates the processing for their own benefit. Genuine free choice exists.",
    },
    "biometric_timekeeping": {
        "description": "Fingerprint or facial recognition for time and attendance",
        "recommended_basis": "art_6_1_f",
        "consent_valid": False,
        "reason": "Art. 9 special category data. Consent in employment is rarely valid. Use Art. 9(2)(b) with national law authorisation.",
    },
    "gps_vehicle_tracking": {
        "description": "GPS tracking of company vehicles used by employees",
        "recommended_basis": "art_6_1_f",
        "consent_valid": False,
        "reason": "Employees cannot freely refuse vehicle tracking while performing driving duties. Legitimate interest is the appropriate basis.",
    },
}

# National Art. 88 derogation rules
NATIONAL_DEROGATIONS = {
    "DE": {
        "name": "Germany",
        "law": "BDSG Section 26",
        "consent_rule": "Consent valid only if employee derives legal or economic advantage or shared interest. Must be in writing.",
        "works_council": True,
        "works_council_law": "Section 87(1)(6) BetrVG",
    },
    "FR": {
        "name": "France",
        "law": "Labour Code Art. L.1121-1, L.1222-4",
        "consent_rule": "Proportionality principle. Monitoring requires prior notification. CNIL guidance restricts consent for monitoring.",
        "works_council": True,
        "works_council_law": "CSE consultation required",
    },
    "NL": {
        "name": "Netherlands",
        "law": "UAVG Art. 30",
        "consent_rule": "Employee consent deemed not freely given due to dependency unless clearly in employee interest.",
        "works_council": True,
        "works_council_law": "Art. 27(1)(k) and (l) WOR",
    },
    "ES": {
        "name": "Spain",
        "law": "LOPDGDD Art. 87-91",
        "consent_rule": "Digital rights in employment. Right to digital privacy at work. Prior notification required for monitoring.",
        "works_council": False,
        "works_council_law": None,
    },
    "IT": {
        "name": "Italy",
        "law": "Workers' Statute Art. 4, D.Lgs. 151/2015",
        "consent_rule": "Remote monitoring requires trade union agreement or labour inspectorate authorisation.",
        "works_council": True,
        "works_council_law": "Trade union agreement under Art. 4",
    },
    "UK": {
        "name": "United Kingdom",
        "law": "DPA 2018, Schedule 1",
        "consent_rule": "No specific consent restriction but ICO Employment Practices Code emphasises power imbalance.",
        "works_council": False,
        "works_council_law": None,
    },
}


def assess_consent_validity(
    activity_key: str,
    jurisdiction: str = "DE",
    voluntary: bool = False,
    consequences_for_refusal: bool = True,
    easy_withdrawal: bool = False,
    specific_purpose: bool = True,
    informed: bool = True,
) -> dict:
    """
    Assess whether consent is a valid lawful basis for a specific employment
    processing activity.

    Args:
        activity_key: Key from PROCESSING_ACTIVITIES.
        jurisdiction: ISO 2-letter country code.
        voluntary: Whether participation is genuinely voluntary.
        consequences_for_refusal: Whether refusal has any adverse consequences.
        easy_withdrawal: Whether withdrawal is easy and consequence-free.
        specific_purpose: Whether consent is for a specific purpose.
        informed: Whether consent form provides required information.

    Returns:
        Assessment result with recommendation.
    """
    activity = PROCESSING_ACTIVITIES.get(activity_key)
    if not activity:
        return {"error": f"Unknown activity: {activity_key}"}

    national = NATIONAL_DEROGATIONS.get(jurisdiction, {})

    # Consent validity checks
    checks = {
        "power_imbalance": {
            "check": "Employment relationship creates inherent power imbalance (WP29 Opinion 2/2017, Section 5.1)",
            "passed": False,
            "note": "Power imbalance is presumed in all employment relationships. Can be overcome only in exceptional circumstances.",
        },
        "freely_given": {
            "check": "Consent is freely given — no consequences for refusal",
            "passed": voluntary and not consequences_for_refusal,
            "note": "Freely given requires zero consequences for refusal or withdrawal (Recital 43).",
        },
        "specific": {
            "check": "Consent is specific to one purpose",
            "passed": specific_purpose,
            "note": "Bundled consent for multiple purposes is invalid (Art. 7(2)).",
        },
        "informed": {
            "check": "Consent form includes all required information",
            "passed": informed,
            "note": "Must include: controller identity, purpose, data types, right to withdraw, automated decisions.",
        },
        "easy_withdrawal": {
            "check": "Withdrawal is as easy as giving consent",
            "passed": easy_withdrawal,
            "note": "Art. 7(3) — withdrawal must be as easy as giving consent.",
        },
    }

    # Override: if the activity is inherently non-voluntary, consent fails
    if not activity["consent_valid"]:
        checks["activity_nature"] = {
            "check": f"Activity '{activity['description']}' is inherently non-voluntary in employment",
            "passed": False,
            "note": activity["reason"],
        }

    all_passed = all(c["passed"] for c in checks.values())
    consent_valid = all_passed and activity["consent_valid"]

    recommended_basis = LAWFUL_BASES[activity["recommended_basis"]]

    result = {
        "assessment_date": datetime.now().isoformat(),
        "activity": activity["description"],
        "jurisdiction": national.get("name", jurisdiction),
        "national_law": national.get("law", "Not specified"),
        "national_consent_rule": national.get("consent_rule", "Not specified"),
        "works_council_required": national.get("works_council", False),
        "consent_validity_checks": checks,
        "consent_valid": consent_valid,
        "recommended_lawful_basis": recommended_basis["name"],
        "recommended_basis_description": recommended_basis["description"],
        "recommendation": (
            f"Consent is valid for '{activity['description']}' in this context. "
            f"Ensure documented safeguards: no consequence for refusal, easy withdrawal, specific purpose."
            if consent_valid
            else f"Consent is NOT valid for '{activity['description']}'. "
            f"Recommended lawful basis: {recommended_basis['name']}. "
            f"Reason: {activity['reason']}"
        ),
    }

    return result


def audit_all_processing(jurisdiction: str = "DE") -> list[dict]:
    """
    Audit all standard employment processing activities for consent validity.

    Args:
        jurisdiction: ISO 2-letter country code.

    Returns:
        List of assessment results for all activities.
    """
    results = []
    for key, activity in PROCESSING_ACTIVITIES.items():
        result = assess_consent_validity(
            activity_key=key,
            jurisdiction=jurisdiction,
            voluntary=activity["consent_valid"],
            consequences_for_refusal=not activity["consent_valid"],
            easy_withdrawal=activity["consent_valid"],
        )
        results.append(result)
    return results


def main():
    """Example: Audit Atlas Manufacturing Group employment processing."""
    print("=== Employment Consent Validity Audit ===")
    print("Organisation: Atlas Manufacturing Group")
    print("Jurisdiction: Germany (BDSG Section 26)")
    print()

    results = audit_all_processing(jurisdiction="DE")

    valid_count = sum(1 for r in results if r["consent_valid"])
    invalid_count = sum(1 for r in results if not r["consent_valid"])

    for r in results:
        status = "VALID" if r["consent_valid"] else "INVALID"
        print(f"[{status}] {r['activity']}")
        print(f"  Recommended basis: {r['recommended_lawful_basis']}")
        print()

    print(f"--- Summary ---")
    print(f"Total activities assessed: {len(results)}")
    print(f"Consent valid: {valid_count}")
    print(f"Consent invalid: {invalid_count}")
    print(f"Activities requiring alternative lawful basis: {invalid_count}")

    # Detailed example
    print("\n=== Detailed Assessment: Employee Monitoring ===")
    monitoring = assess_consent_validity(
        activity_key="employee_monitoring",
        jurisdiction="DE",
        voluntary=False,
        consequences_for_refusal=True,
        easy_withdrawal=False,
    )
    print(json.dumps(monitoring, indent=2))


if __name__ == "__main__":
    main()
