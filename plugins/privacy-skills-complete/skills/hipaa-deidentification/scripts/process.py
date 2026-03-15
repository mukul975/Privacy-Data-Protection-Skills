#!/usr/bin/env python3
"""HIPAA de-identification processor — safe harbor validation and re-identification risk assessment."""

import json
import os
import re
from datetime import datetime
from typing import Any


SAFE_HARBOR_IDENTIFIERS = {
    "names": {"category": 1, "description": "Names"},
    "geographic_subdivision": {"category": 2, "description": "Geographic data smaller than state"},
    "dates": {"category": 3, "description": "Dates related to individual (except year)"},
    "telephone": {"category": 4, "description": "Telephone numbers"},
    "fax": {"category": 5, "description": "Fax numbers"},
    "email": {"category": 6, "description": "Email addresses"},
    "ssn": {"category": 7, "description": "Social Security numbers"},
    "mrn": {"category": 8, "description": "Medical record numbers"},
    "health_plan_id": {"category": 9, "description": "Health plan beneficiary numbers"},
    "account_numbers": {"category": 10, "description": "Account numbers"},
    "certificate_license": {"category": 11, "description": "Certificate/license numbers"},
    "vehicle_identifiers": {"category": 12, "description": "Vehicle identifiers/serial numbers"},
    "device_identifiers": {"category": 13, "description": "Device identifiers/serial numbers"},
    "web_urls": {"category": 14, "description": "Web URLs"},
    "ip_addresses": {"category": 15, "description": "IP addresses"},
    "biometric": {"category": 16, "description": "Biometric identifiers"},
    "photographs": {"category": 17, "description": "Full-face photographs"},
    "other_unique": {"category": 18, "description": "Any other unique identifying number/characteristic/code"},
}

# 3-digit ZIP codes with populations <=20,000 that must be set to 000
# This is a representative sample; the full list is derived from Census Bureau data
LOW_POPULATION_ZIP3 = {
    "036", "059", "063", "102", "203", "556",
    "692", "790", "821", "823", "830", "831",
    "878", "879", "884", "890", "893",
}

IDENTIFIER_PATTERNS = {
    "ssn": re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
    "phone": re.compile(r'\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'),
    "email": re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
    "ip_address": re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b'),
    "url": re.compile(r'https?://\S+'),
    "mrn_pattern": re.compile(r'\b(?:MRN|MR#|Medical Record)\s*:?\s*\d+\b', re.IGNORECASE),
    "date_full": re.compile(r'\b\d{1,2}/\d{1,2}/\d{2,4}\b'),
}

LIMITED_DATASET_REMOVED = [
    "names", "street_address", "telephone", "fax", "email",
    "ssn", "mrn", "health_plan_id", "account_numbers",
    "certificate_license", "vehicle_identifiers", "device_identifiers",
    "web_urls", "ip_addresses", "biometric", "photographs",
]

LIMITED_DATASET_RETAINED = [
    "dates_all", "city", "state", "zip_code", "ages_over_89",
]


def validate_safe_harbor(
    dataset_fields: dict[str, Any],
    zip_codes: list[str] | None = None,
    max_age: int | None = None,
) -> dict[str, Any]:
    """Validate that a dataset meets HIPAA safe harbor de-identification requirements.

    Args:
        dataset_fields: Dictionary mapping identifier categories to removal status.
        zip_codes: List of 3-digit ZIP code prefixes in the dataset.
        max_age: Maximum age value in the dataset.

    Returns:
        Validation result with compliance status per identifier.
    """
    result = {
        "validation_date": datetime.now().isoformat(),
        "method": "safe_harbor",
        "compliant": True,
        "identifiers": [],
        "zip_code_issues": [],
        "age_issues": [],
        "summary": {
            "total_identifiers": len(SAFE_HARBOR_IDENTIFIERS),
            "removed": 0,
            "not_removed": 0,
            "not_assessed": 0,
        },
    }

    for id_key, id_info in SAFE_HARBOR_IDENTIFIERS.items():
        status = dataset_fields.get(id_key, "not_assessed")
        identifier_result = {
            "category": id_info["category"],
            "identifier": id_info["description"],
            "status": status,
        }
        result["identifiers"].append(identifier_result)

        if status == "removed":
            result["summary"]["removed"] += 1
        elif status == "not_removed":
            result["summary"]["not_removed"] += 1
            result["compliant"] = False
        else:
            result["summary"]["not_assessed"] += 1
            result["compliant"] = False

    if zip_codes:
        for zip3 in zip_codes:
            if zip3 in LOW_POPULATION_ZIP3:
                result["zip_code_issues"].append({
                    "zip3": zip3,
                    "issue": f"3-digit ZIP {zip3} has population <=20,000; must be replaced with 000",
                    "compliant": False,
                })
                result["compliant"] = False

    if max_age is not None and max_age > 89:
        result["age_issues"].append({
            "max_age": max_age,
            "issue": "Ages over 89 must be aggregated into 90+ category",
            "compliant": False,
        })
        result["compliant"] = False

    no_actual_knowledge = dataset_fields.get("no_actual_knowledge_of_identification", False)
    result["no_actual_knowledge_confirmed"] = no_actual_knowledge
    if not no_actual_knowledge:
        result["compliant"] = False

    return result


def scan_text_for_identifiers(text: str) -> dict[str, Any]:
    """Scan free text for potential identifiers using pattern matching.

    Args:
        text: Text string to scan for identifiers.

    Returns:
        Scan results with identified patterns and locations.
    """
    findings = {
        "scan_date": datetime.now().isoformat(),
        "text_length": len(text),
        "identifiers_found": [],
        "total_findings": 0,
        "risk_level": "low",
    }

    for pattern_name, pattern in IDENTIFIER_PATTERNS.items():
        matches = pattern.finditer(text)
        for match in matches:
            findings["identifiers_found"].append({
                "type": pattern_name,
                "value": match.group()[:4] + "***" if pattern_name == "ssn" else "[REDACTED]",
                "position": match.start(),
                "length": len(match.group()),
            })
            findings["total_findings"] += 1

    if findings["total_findings"] > 10:
        findings["risk_level"] = "high"
    elif findings["total_findings"] > 0:
        findings["risk_level"] = "medium"

    return findings


def assess_reidentification_risk(
    dataset_properties: dict[str, Any],
) -> dict[str, Any]:
    """Assess re-identification risk of a de-identified dataset.

    Args:
        dataset_properties: Properties of the de-identified dataset.

    Returns:
        Re-identification risk assessment.
    """
    result = {
        "assessment_date": datetime.now().isoformat(),
        "risk_factors": [],
        "overall_risk": "low",
        "recommendations": [],
    }

    record_count = dataset_properties.get("record_count", 0)
    if record_count < 100:
        result["risk_factors"].append({
            "factor": "Small dataset",
            "detail": f"Only {record_count} records — higher uniqueness probability",
            "risk_contribution": "high",
        })

    has_rare_conditions = dataset_properties.get("rare_conditions", False)
    if has_rare_conditions:
        result["risk_factors"].append({
            "factor": "Rare conditions present",
            "detail": "Rare diseases or procedures increase record uniqueness",
            "risk_contribution": "high",
        })
        result["recommendations"].append(
            "Consider suppressing records with rare conditions or generalizing diagnoses"
        )

    geographic_specificity = dataset_properties.get("geographic_specificity", "state")
    if geographic_specificity in ("zip5", "zip3_small", "census_tract"):
        result["risk_factors"].append({
            "factor": "Fine geographic granularity",
            "detail": f"Geographic level: {geographic_specificity} — increases linkage risk",
            "risk_contribution": "medium",
        })

    temporal_specificity = dataset_properties.get("temporal_specificity", "year")
    if temporal_specificity in ("exact_date", "week"):
        result["risk_factors"].append({
            "factor": "Temporal specificity",
            "detail": f"Date precision: {temporal_specificity} — increases linkage risk with news/public records",
            "risk_contribution": "high",
        })

    quasi_identifiers = dataset_properties.get("quasi_identifier_count", 0)
    if quasi_identifiers > 5:
        result["risk_factors"].append({
            "factor": "Many quasi-identifiers",
            "detail": f"{quasi_identifiers} quasi-identifiers increase combination uniqueness",
            "risk_contribution": "medium",
        })

    publicly_available_linkage = dataset_properties.get("linkage_sources_available", [])
    if len(publicly_available_linkage) > 2:
        result["risk_factors"].append({
            "factor": "Multiple linkage sources available",
            "detail": f"Identified linkage sources: {', '.join(publicly_available_linkage)}",
            "risk_contribution": "high",
        })

    high_factors = sum(1 for f in result["risk_factors"] if f["risk_contribution"] == "high")
    medium_factors = sum(1 for f in result["risk_factors"] if f["risk_contribution"] == "medium")

    if high_factors >= 2:
        result["overall_risk"] = "high"
        result["recommendations"].append("Engage expert for formal expert determination analysis")
        result["recommendations"].append("Consider additional transformations (generalization, suppression)")
    elif high_factors >= 1 or medium_factors >= 2:
        result["overall_risk"] = "medium"
        result["recommendations"].append("Apply additional safeguards (data use agreement, access controls)")
    else:
        result["overall_risk"] = "low"

    return result


def validate_limited_dataset(
    dataset_fields: dict[str, Any],
    purpose: str,
    has_dua: bool,
) -> dict[str, Any]:
    """Validate a limited data set and its usage conditions.

    Args:
        dataset_fields: Dictionary mapping identifier categories to removal status.
        purpose: Stated purpose for the limited data set.
        has_dua: Whether a Data Use Agreement is in place.

    Returns:
        Validation result.
    """
    permitted_purposes = ["research", "public_health", "healthcare_operations"]

    result = {
        "validation_date": datetime.now().isoformat(),
        "method": "limited_data_set",
        "compliant": True,
        "purpose_permitted": purpose in permitted_purposes,
        "dua_in_place": has_dua,
        "identifiers_removed": [],
        "issues": [],
    }

    if not result["purpose_permitted"]:
        result["compliant"] = False
        result["issues"].append(
            f"Purpose '{purpose}' is not permitted for limited data sets (must be research, public health, or healthcare operations)"
        )

    if not has_dua:
        result["compliant"] = False
        result["issues"].append("Data Use Agreement required but not in place")

    for identifier in LIMITED_DATASET_REMOVED:
        status = dataset_fields.get(identifier, "not_assessed")
        result["identifiers_removed"].append({
            "identifier": identifier,
            "status": status,
        })
        if status != "removed":
            result["compliant"] = False
            result["issues"].append(f"Direct identifier '{identifier}' must be removed from limited data set")

    return result


if __name__ == "__main__":
    print("=== HIPAA De-Identification Assessment ===\n")

    fields = {id_key: "removed" for id_key in SAFE_HARBOR_IDENTIFIERS}
    fields["no_actual_knowledge_of_identification"] = True

    safe_harbor_result = validate_safe_harbor(
        fields,
        zip_codes=["021", "100", "900", "036"],
        max_age=85,
    )
    print(f"Safe Harbor Validation: Compliant = {safe_harbor_result['compliant']}")
    print(f"  Identifiers removed: {safe_harbor_result['summary']['removed']}/{safe_harbor_result['summary']['total_identifiers']}")
    if safe_harbor_result["zip_code_issues"]:
        for issue in safe_harbor_result["zip_code_issues"]:
            print(f"  ZIP Issue: {issue['issue']}")
    print()

    sample_text = "Patient John Smith, DOB 03/15/1975, SSN 123-45-6789, called from 555-123-4567"
    scan_result = scan_text_for_identifiers(sample_text)
    print(f"Text Scan: {scan_result['total_findings']} identifiers found (risk: {scan_result['risk_level']})")
    for finding in scan_result["identifiers_found"]:
        print(f"  {finding['type']}: {finding['value']}")
    print()

    risk = assess_reidentification_risk({
        "record_count": 50,
        "rare_conditions": True,
        "geographic_specificity": "zip3_small",
        "temporal_specificity": "year",
        "quasi_identifier_count": 4,
        "linkage_sources_available": ["voter_registration", "news_reports", "social_media"],
    })
    print(f"Re-identification Risk: {risk['overall_risk']}")
    for rec in risk["recommendations"]:
        print(f"  Recommendation: {rec}")
