"""
Employee Health Data Compliance Engine

Assesses compliance of employee health data processing against Art. 9 GDPR,
data minimisation requirements, and access control standards.
"""

import json
from datetime import datetime
from typing import Optional


HEALTH_DATA_CATEGORIES = {
    "absence_dates": {
        "description": "Dates of sickness absence",
        "sensitivity": "low",
        "employer_may_hold": True,
        "basis": "Art. 6(1)(b) contract + Art. 9(2)(b) employment obligation",
    },
    "fit_unfit_conclusion": {
        "description": "Fitness-for-work conclusion (fit/unfit/fit with adjustments)",
        "sensitivity": "medium",
        "employer_may_hold": True,
        "basis": "Art. 9(2)(b) employment obligation",
    },
    "workplace_adjustments": {
        "description": "Required workplace adjustments (functional description)",
        "sensitivity": "medium",
        "employer_may_hold": True,
        "basis": "Art. 9(2)(b) disability legislation",
    },
    "oh_referral_correspondence": {
        "description": "Occupational health referral and response correspondence",
        "sensitivity": "medium",
        "employer_may_hold": True,
        "basis": "Art. 9(2)(h) health professional",
    },
    "fitness_certificates": {
        "description": "Fitness-for-work certificates for safety-critical roles",
        "sensitivity": "medium",
        "employer_may_hold": True,
        "basis": "Art. 9(2)(b) health and safety obligation",
    },
    "clinical_diagnosis": {
        "description": "Specific medical diagnosis",
        "sensitivity": "very_high",
        "employer_may_hold": False,
        "basis": "NOT necessary for employment decisions",
    },
    "treatment_details": {
        "description": "Treatment plans, medications, procedures",
        "sensitivity": "very_high",
        "employer_may_hold": False,
        "basis": "NOT necessary; disproportionate intrusion",
    },
    "medication": {
        "description": "Medication information",
        "sensitivity": "very_high",
        "employer_may_hold": False,
        "basis": "NOT necessary; may reveal conditions not relevant to work",
    },
    "mental_health_counselling": {
        "description": "Mental health counselling records",
        "sensitivity": "very_high",
        "employer_may_hold": False,
        "basis": "Processed under professional secrecy by health professional",
    },
    "gp_hospital_records": {
        "description": "GP or hospital medical records",
        "sensitivity": "very_high",
        "employer_may_hold": False,
        "basis": "No lawful basis for employer access",
    },
    "genetic_data": {
        "description": "Genetic test results",
        "sensitivity": "very_high",
        "employer_may_hold": False,
        "basis": "Art. 9(1) + Art. 9(4) national restrictions",
    },
    "covid_test_results": {
        "description": "COVID-19 test results (legacy)",
        "sensitivity": "high",
        "employer_may_hold": False,
        "basis": "Legal basis (Art. 9(2)(b)/(i)) likely expired post-pandemic",
    },
    "vaccination_status": {
        "description": "COVID-19 vaccination records (legacy)",
        "sensitivity": "high",
        "employer_may_hold": False,
        "basis": "Legal basis likely expired unless healthcare sector with ongoing obligation",
    },
}

ACCESS_ROLES = {
    "hr_manager": {
        "name": "HR Manager (Employee Relations)",
        "permitted_data": [
            "absence_dates", "fit_unfit_conclusion", "workplace_adjustments",
            "oh_referral_correspondence", "fitness_certificates",
        ],
    },
    "line_manager": {
        "name": "Line Manager",
        "permitted_data": ["absence_dates"],
    },
    "oh_provider": {
        "name": "Occupational Health Provider",
        "permitted_data": list(HEALTH_DATA_CATEGORIES.keys()),
    },
    "payroll": {
        "name": "Payroll",
        "permitted_data": ["absence_dates"],
    },
    "dpo": {
        "name": "DPO",
        "permitted_data": [],
    },
    "it_admin": {
        "name": "IT Administrator",
        "permitted_data": [],
    },
}


def assess_health_data_compliance(
    data_held: list[str],
    access_config: dict[str, list[str]],
) -> dict:
    """
    Assess whether the organisation's health data holdings and access
    configuration comply with data minimisation and access control requirements.

    Args:
        data_held: List of health data category keys currently held by the employer.
        access_config: Dict mapping role keys to lists of data category keys they can access.

    Returns:
        Compliance assessment with findings.
    """
    findings = []
    critical_issues = []

    # Check data holdings
    for data_key in data_held:
        cat = HEALTH_DATA_CATEGORIES.get(data_key)
        if not cat:
            continue
        if not cat["employer_may_hold"]:
            critical_issues.append({
                "issue": f"Employer holds '{cat['description']}' — NOT permitted",
                "data_category": data_key,
                "reason": cat["basis"],
                "remediation": "Delete this data immediately. It should not be in the employer's possession.",
            })

    # Check access configuration
    for role_key, role_data_access in access_config.items():
        expected_role = ACCESS_ROLES.get(role_key)
        if not expected_role:
            continue
        for data_key in role_data_access:
            if data_key not in expected_role["permitted_data"]:
                cat = HEALTH_DATA_CATEGORIES.get(data_key, {})
                critical_issues.append({
                    "issue": f"Role '{expected_role['name']}' has access to '{cat.get('description', data_key)}' — NOT permitted",
                    "role": role_key,
                    "data_category": data_key,
                    "remediation": f"Remove access for {expected_role['name']} to this data category.",
                })

    compliant = len(critical_issues) == 0

    return {
        "assessment_date": datetime.now().isoformat(),
        "data_categories_held": len(data_held),
        "data_categories_prohibited": len([
            d for d in data_held
            if not HEALTH_DATA_CATEGORIES.get(d, {}).get("employer_may_hold", True)
        ]),
        "access_violations": len([
            i for i in critical_issues if "access to" in i["issue"]
        ]),
        "critical_issues": critical_issues,
        "findings": findings,
        "compliant": compliant,
        "recommendation": (
            "Health data processing is compliant with data minimisation and access control requirements."
            if compliant
            else f"{len(critical_issues)} critical issue(s) identified. Remediate immediately."
        ),
    }


def main():
    """Example: Atlas Manufacturing Group health data audit."""
    print("=== Employee Health Data Compliance Assessment ===")
    print("Organisation: Atlas Manufacturing Group\n")

    # Simulate Atlas holding some data it should not
    result = assess_health_data_compliance(
        data_held=[
            "absence_dates", "fit_unfit_conclusion", "workplace_adjustments",
            "oh_referral_correspondence", "fitness_certificates",
        ],
        access_config={
            "hr_manager": [
                "absence_dates", "fit_unfit_conclusion", "workplace_adjustments",
                "oh_referral_correspondence", "fitness_certificates",
            ],
            "line_manager": ["absence_dates"],
            "payroll": ["absence_dates"],
            "dpo": [],
            "it_admin": [],
        },
    )

    print(json.dumps(result, indent=2))
    print(f"\nCompliant: {result['compliant']}")

    # Simulate non-compliant scenario
    print("\n=== Non-Compliant Scenario ===")
    bad_result = assess_health_data_compliance(
        data_held=[
            "absence_dates", "fit_unfit_conclusion", "clinical_diagnosis",
            "medication", "covid_test_results",
        ],
        access_config={
            "hr_manager": ["absence_dates", "fit_unfit_conclusion", "clinical_diagnosis"],
            "line_manager": ["absence_dates", "fit_unfit_conclusion"],
        },
    )
    print(json.dumps(bad_result, indent=2))


if __name__ == "__main__":
    main()
