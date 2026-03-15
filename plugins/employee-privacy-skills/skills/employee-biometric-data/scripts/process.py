"""
Employee Biometric Data Compliance Engine

Assesses the necessity and proportionality of biometric data processing in the
workplace. Evaluates Art. 9(2) exception applicability and generates compliance
reports per CNIL Règlement Type Biométrie and national law requirements.
"""

import json
from datetime import datetime
from typing import Optional


BIOMETRIC_TECHNOLOGIES = {
    "fingerprint": {
        "name": "Fingerprint Recognition",
        "intrusiveness": "medium",
        "active_passive": "active",
        "revocable": False,
        "affected_by_conditions": True,
        "common_use_cases": ["timekeeping", "physical_access", "device_auth"],
    },
    "facial_recognition": {
        "name": "Facial Recognition",
        "intrusiveness": "high",
        "active_passive": "passive",
        "revocable": False,
        "affected_by_conditions": True,
        "common_use_cases": ["physical_access", "contactless_id", "security_zones"],
    },
    "iris_scan": {
        "name": "Iris Scanning",
        "intrusiveness": "high",
        "active_passive": "active",
        "revocable": False,
        "affected_by_conditions": False,
        "common_use_cases": ["high_security_access"],
    },
    "voice_recognition": {
        "name": "Voice Recognition",
        "intrusiveness": "medium",
        "active_passive": "active",
        "revocable": False,
        "affected_by_conditions": True,
        "common_use_cases": ["telephone_auth", "call_centre"],
    },
    "behavioural_biometrics": {
        "name": "Behavioural Biometrics (keystroke dynamics, gait)",
        "intrusiveness": "high",
        "active_passive": "passive",
        "revocable": False,
        "affected_by_conditions": True,
        "common_use_cases": ["continuous_auth", "anomaly_detection"],
    },
}

STORAGE_METHODS = {
    "individual_device": {
        "name": "Individual Device (badge/token held by employee)",
        "risk_level": "low",
        "cnil_preference": 1,
        "description": "Template stored on smart card or token controlled by employee",
    },
    "centralised_employee_key": {
        "name": "Centralised Database with Employee-Controlled Access Key",
        "risk_level": "medium",
        "cnil_preference": 2,
        "description": "Template in central database but access requires employee key/PIN",
    },
    "centralised_no_control": {
        "name": "Centralised Database without Employee Control",
        "risk_level": "high",
        "cnil_preference": 3,
        "description": "Template in central database under employer control only",
    },
}

LESS_INTRUSIVE_ALTERNATIVES = {
    "timekeeping": [
        {"alternative": "Badge/proximity card clock-in", "effectiveness": "high"},
        {"alternative": "PIN code entry", "effectiveness": "high"},
        {"alternative": "Supervisor sign-off", "effectiveness": "medium"},
        {"alternative": "Self-reporting with audit", "effectiveness": "medium"},
    ],
    "physical_access": [
        {"alternative": "Smart card + PIN", "effectiveness": "high"},
        {"alternative": "Proximity badge", "effectiveness": "medium"},
        {"alternative": "Key lock", "effectiveness": "low"},
    ],
    "device_auth": [
        {"alternative": "Password/passphrase", "effectiveness": "high"},
        {"alternative": "Smart card/security key", "effectiveness": "high"},
        {"alternative": "Certificate-based auth", "effectiveness": "high"},
    ],
    "high_security_access": [
        {"alternative": "Dual smart card + PIN", "effectiveness": "medium"},
        {"alternative": "Multi-factor (card + PIN + OTP)", "effectiveness": "high"},
    ],
    "contactless_id": [
        {"alternative": "Contactless smart card", "effectiveness": "high"},
        {"alternative": "Proximity badge with airlock", "effectiveness": "medium"},
    ],
}


def assess_necessity(
    technology: str,
    use_case: str,
    documented_security_concern: bool = False,
    alternatives_insufficient_reason: Optional[str] = None,
) -> dict:
    """
    Assess whether biometric processing is necessary for the stated use case.

    Args:
        technology: Key from BIOMETRIC_TECHNOLOGIES.
        use_case: The intended use case (timekeeping, physical_access, etc.).
        documented_security_concern: Whether there is a documented security issue alternatives cannot address.
        alternatives_insufficient_reason: Why less intrusive alternatives are insufficient.

    Returns:
        Necessity assessment result.
    """
    tech = BIOMETRIC_TECHNOLOGIES.get(technology)
    if not tech:
        return {"error": f"Unknown technology: {technology}"}

    alternatives = LESS_INTRUSIVE_ALTERNATIVES.get(use_case, [])
    high_effectiveness_alternatives = [a for a in alternatives if a["effectiveness"] == "high"]

    biometric_necessary = (
        documented_security_concern
        and alternatives_insufficient_reason is not None
        and len(alternatives_insufficient_reason) > 10
    )

    if tech["intrusiveness"] == "high" and use_case == "timekeeping":
        biometric_necessary = False
        override_reason = (
            "High-intrusiveness biometric technology is disproportionate for timekeeping. "
            "Multiple high-effectiveness alternatives exist (badge, PIN, supervisor sign-off)."
        )
    else:
        override_reason = None

    return {
        "assessment_date": datetime.now().isoformat(),
        "technology": tech["name"],
        "intrusiveness": tech["intrusiveness"],
        "active_passive": tech["active_passive"],
        "use_case": use_case,
        "alternatives_available": alternatives,
        "high_effectiveness_alternatives": len(high_effectiveness_alternatives),
        "documented_security_concern": documented_security_concern,
        "alternatives_insufficient_reason": alternatives_insufficient_reason,
        "biometric_necessary": biometric_necessary,
        "override_reason": override_reason,
        "recommendation": (
            override_reason if override_reason
            else (
                f"Biometric processing ({tech['name']}) is necessary for {use_case}. "
                f"Proceed to Art. 9(2) exception assessment and DPIA."
                if biometric_necessary
                else (
                    f"Biometric processing ({tech['name']}) is NOT necessary for {use_case}. "
                    f"{len(high_effectiveness_alternatives)} high-effectiveness alternatives available. "
                    f"Use less intrusive method."
                )
            )
        ),
    }


def assess_storage_compliance(
    storage_method: str,
    justification: Optional[str] = None,
) -> dict:
    """
    Assess biometric template storage method against CNIL hierarchy.

    Args:
        storage_method: Key from STORAGE_METHODS.
        justification: Required if not using individual device storage.

    Returns:
        Storage compliance assessment.
    """
    method = STORAGE_METHODS.get(storage_method)
    if not method:
        return {"error": f"Unknown storage method: {storage_method}"}

    compliant = True
    notes = []

    if method["cnil_preference"] > 1:
        if justification and len(justification) > 10:
            notes.append(
                f"Non-preferred storage method ({method['name']}) justified: {justification}"
            )
        else:
            compliant = False
            notes.append(
                f"Non-preferred storage method ({method['name']}) requires documented justification. "
                f"CNIL Règlement Type Biométrie requires individual device storage as default."
            )

    if method["risk_level"] == "high":
        notes.append(
            "Centralised storage without employee control carries highest risk. "
            "Requires strongest justification and enhanced security measures."
        )

    return {
        "storage_method": method["name"],
        "risk_level": method["risk_level"],
        "cnil_preference_rank": method["cnil_preference"],
        "justification": justification,
        "compliant": compliant,
        "notes": notes,
        "required_safeguards": [
            "AES-256 encryption at rest",
            "TLS 1.3 encryption in transit",
            "No raw biometric data stored (templates only)",
            "System-specific template format",
            "Anti-spoofing / liveness detection",
            "Immediate deletion on termination / objection",
            "Audit logging of all template access",
        ],
    }


def generate_biometric_compliance_report(
    organisation: str,
    technology: str,
    use_case: str,
    storage_method: str,
    employee_count: int,
    jurisdiction: str,
    alternative_method_available: bool,
    documented_security_concern: bool,
    security_concern_detail: Optional[str] = None,
) -> dict:
    """Generate a complete biometric data compliance assessment report."""
    necessity = assess_necessity(
        technology=technology,
        use_case=use_case,
        documented_security_concern=documented_security_concern,
        alternatives_insufficient_reason=security_concern_detail,
    )

    storage = assess_storage_compliance(
        storage_method=storage_method,
        justification=security_concern_detail,
    )

    overall_compliant = (
        necessity["biometric_necessary"]
        and storage["compliant"]
        and alternative_method_available
    )

    return {
        "report_date": datetime.now().isoformat(),
        "organisation": organisation,
        "jurisdiction": jurisdiction,
        "employees_in_scope": employee_count,
        "necessity_assessment": necessity,
        "storage_assessment": storage,
        "alternative_method_available": alternative_method_available,
        "overall_compliant": overall_compliant,
        "dpia_required": True,
        "recommendation": (
            "Biometric processing may proceed subject to DPIA completion, "
            "works council consultation (where applicable), and implementation of all safeguards."
            if overall_compliant
            else "Biometric processing should NOT proceed. Address compliance gaps before deployment."
        ),
    }


def main():
    """Example: Atlas Manufacturing Group R&D lab biometric access."""
    report = generate_biometric_compliance_report(
        organisation="Atlas Manufacturing Group",
        technology="fingerprint",
        use_case="physical_access",
        storage_method="individual_device",
        employee_count=45,
        jurisdiction="DE",
        alternative_method_available=True,
        documented_security_concern=True,
        security_concern_detail=(
            "R&D laboratory contains proprietary chemical formulations valued at EUR 12M. "
            "Badge-sharing incidents documented 3 times in the past 12 months. "
            "Dual-factor access (biometric + badge) is necessary to prevent unauthorized access."
        ),
    )

    print(json.dumps(report, indent=2))

    print("\n--- Summary ---")
    print(f"Organisation: {report['organisation']}")
    print(f"Technology: {report['necessity_assessment']['technology']}")
    print(f"Use Case: {report['necessity_assessment']['use_case']}")
    print(f"Biometric Necessary: {report['necessity_assessment']['biometric_necessary']}")
    print(f"Storage Compliant: {report['storage_assessment']['compliant']}")
    print(f"Alternative Available: {report['alternative_method_available']}")
    print(f"Overall Compliant: {report['overall_compliant']}")


if __name__ == "__main__":
    main()
