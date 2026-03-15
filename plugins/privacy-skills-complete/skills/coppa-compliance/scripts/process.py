#!/usr/bin/env python3
"""
COPPA Compliance Audit Tool

Audits online services against COPPA requirements under 16 CFR Part 312,
including notice, consent, access, security, and data minimisation obligations.
"""

import json
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional

COPPA_AUDIT_CHECKLIST = [
    {
        "id": 1,
        "section": "Notice",
        "item": "Online privacy notice posted prominently",
        "reference": "312.4(b)",
        "criteria": "Clear link to notice on home page and each collection point",
    },
    {
        "id": 2,
        "section": "Notice",
        "item": "Notice includes operator identification",
        "reference": "312.4(b)(1)",
        "criteria": "Name, address, email, and phone of all operators listed",
    },
    {
        "id": 3,
        "section": "Notice",
        "item": "Notice describes information collected",
        "reference": "312.4(b)(2)",
        "criteria": "Types of personal information and collection methods stated",
    },
    {
        "id": 4,
        "section": "Notice",
        "item": "Notice describes use of information",
        "reference": "312.4(b)(3)",
        "criteria": "How collected information is used and may be used",
    },
    {
        "id": 5,
        "section": "Notice",
        "item": "Notice discloses third-party sharing",
        "reference": "312.4(b)(4)",
        "criteria": "Third-party types, purposes, and confidentiality commitment stated",
    },
    {
        "id": 6,
        "section": "Notice",
        "item": "Notice describes parental rights",
        "reference": "312.4(b)(5)",
        "criteria": "Right to review, delete, and refuse further collection stated",
    },
    {
        "id": 7,
        "section": "Notice",
        "item": "Direct notice sent to parent before collection",
        "reference": "312.4(c)",
        "criteria": "Direct notice with required content sent before any collection",
    },
    {
        "id": 8,
        "section": "Consent",
        "item": "Verifiable parental consent obtained",
        "reference": "312.5(a)",
        "criteria": "Consent obtained before collection, use, or disclosure",
    },
    {
        "id": 9,
        "section": "Consent",
        "item": "Consent method appropriate for data use",
        "reference": "312.5(b)",
        "criteria": "Email Plus for internal use only; higher methods for disclosure",
    },
    {
        "id": 10,
        "section": "Consent",
        "item": "Age screen is neutral",
        "reference": "312.2, FTC guidance",
        "criteria": "Age prompt does not reveal threshold or encourage false declaration",
    },
    {
        "id": 11,
        "section": "Access",
        "item": "Parent can review collected information",
        "reference": "312.6(a)",
        "criteria": "Mechanism to view all personal information collected from child",
    },
    {
        "id": 12,
        "section": "Access",
        "item": "Parent can delete child's information",
        "reference": "312.6(a)",
        "criteria": "Mechanism to direct deletion within reasonable time",
    },
    {
        "id": 13,
        "section": "Access",
        "item": "Parent can refuse further collection",
        "reference": "312.6(a)",
        "criteria": "Mechanism to opt out of further collection and use",
    },
    {
        "id": 14,
        "section": "Minimisation",
        "item": "No excess data conditioning",
        "reference": "312.7",
        "criteria": "Participation not conditioned on excess personal information",
    },
    {
        "id": 15,
        "section": "Security",
        "item": "Reasonable security procedures",
        "reference": "312.8",
        "criteria": "Procedures to protect confidentiality, security, and integrity",
    },
    {
        "id": 16,
        "section": "Retention",
        "item": "Data retained only as necessary",
        "reference": "312.10",
        "criteria": "Retention limited to reasonably necessary period",
    },
    {
        "id": 17,
        "section": "Retention",
        "item": "Secure deletion procedures",
        "reference": "312.10",
        "criteria": "Reasonable measures to protect against unauthorised access during deletion",
    },
    {
        "id": 18,
        "section": "Safe Harbor",
        "item": "Safe harbor membership (if applicable)",
        "reference": "312.11",
        "criteria": "Membership in FTC-approved safe harbor program",
    },
]

CONSENT_METHODS = {
    "signed_form": {
        "name": "Signed Consent Form",
        "assurance": "high",
        "suitable_for": ["internal_use", "third_party_disclosure", "public_posting"],
    },
    "credit_card": {
        "name": "Credit Card Transaction",
        "assurance": "high",
        "suitable_for": ["internal_use", "third_party_disclosure", "public_posting"],
    },
    "toll_free_call": {
        "name": "Toll-Free Telephone / Video Conference",
        "assurance": "high",
        "suitable_for": ["internal_use", "third_party_disclosure", "public_posting"],
    },
    "government_id": {
        "name": "Government-Issued ID",
        "assurance": "high",
        "suitable_for": ["internal_use", "third_party_disclosure", "public_posting"],
    },
    "knowledge_based": {
        "name": "Knowledge-Based Authentication",
        "assurance": "high",
        "suitable_for": ["internal_use", "third_party_disclosure", "public_posting"],
    },
    "facial_recognition": {
        "name": "Facial Recognition Comparison",
        "assurance": "high",
        "suitable_for": ["internal_use", "third_party_disclosure", "public_posting"],
    },
    "email_plus": {
        "name": "Email Plus",
        "assurance": "basic",
        "suitable_for": ["internal_use"],
    },
}


def run_coppa_audit(responses: dict[int, str]) -> dict:
    """
    Run the COPPA compliance audit.

    Args:
        responses: Dictionary mapping checklist item ID to "pass", "fail", or "na".

    Returns:
        Audit report dictionary with results and compliance summary.
    """
    results = []
    section_results: dict[str, dict] = {}
    pass_count = 0
    fail_count = 0
    na_count = 0

    for item in COPPA_AUDIT_CHECKLIST:
        item_id = item["id"]
        section = item["section"]
        status = responses.get(item_id, "not_assessed")

        if status == "pass":
            pass_count += 1
        elif status == "fail":
            fail_count += 1
        elif status == "na":
            na_count += 1

        if section not in section_results:
            section_results[section] = {"pass": 0, "fail": 0, "na": 0}
        if status in ("pass", "fail", "na"):
            section_results[section][status] += 1

        results.append({
            "id": item_id,
            "section": section,
            "item": item["item"],
            "reference": item["reference"],
            "status": status,
        })

    total_applicable = pass_count + fail_count
    compliance_rate = (pass_count / total_applicable * 100) if total_applicable > 0 else 0.0

    return {
        "audit_date": datetime.now(timezone.utc).isoformat(),
        "controller": "BrightPath Learning Inc.",
        "framework": "COPPA — 16 CFR Part 312",
        "results": results,
        "section_summary": {
            section: {
                "passed": data["pass"],
                "failed": data["fail"],
                "not_applicable": data["na"],
                "section_rate": round(
                    data["pass"] / (data["pass"] + data["fail"]) * 100, 1
                )
                if (data["pass"] + data["fail"]) > 0
                else 0.0,
            }
            for section, data in section_results.items()
        },
        "summary": {
            "total_items": len(COPPA_AUDIT_CHECKLIST),
            "passed": pass_count,
            "failed": fail_count,
            "not_applicable": na_count,
            "not_assessed": len(COPPA_AUDIT_CHECKLIST) - pass_count - fail_count - na_count,
            "compliance_rate_percent": round(compliance_rate, 1),
        },
    }


def validate_consent_method(method: str, data_use: str) -> dict:
    """
    Validate whether a consent method is appropriate for the intended data use.

    Args:
        method: Consent method key (e.g., "email_plus", "credit_card")
        data_use: Intended use ("internal_use", "third_party_disclosure", "public_posting")

    Returns:
        Validation result with recommendation.
    """
    if method not in CONSENT_METHODS:
        return {
            "valid": False,
            "reason": f"Unknown consent method: {method}",
        }

    method_info = CONSENT_METHODS[method]

    if data_use not in method_info["suitable_for"]:
        return {
            "valid": False,
            "reason": (
                f"Method '{method_info['name']}' ({method_info['assurance']} assurance) "
                f"is not suitable for '{data_use}'. "
                f"Suitable for: {', '.join(method_info['suitable_for'])}."
            ),
            "recommendation": (
                "Use a high-assurance method: signed form, credit card, "
                "toll-free call, government ID, or knowledge-based authentication."
            ),
        }

    return {
        "valid": True,
        "reason": (
            f"Method '{method_info['name']}' ({method_info['assurance']} assurance) "
            f"is appropriate for '{data_use}'."
        ),
    }


if __name__ == "__main__":
    print("=== COPPA Compliance Audit ===")
    sample_responses = {
        1: "pass", 2: "pass", 3: "pass", 4: "pass", 5: "pass",
        6: "pass", 7: "pass", 8: "pass", 9: "pass", 10: "pass",
        11: "pass", 12: "pass", 13: "pass", 14: "pass", 15: "pass",
        16: "pass", 17: "pass", 18: "pass",
    }

    report = run_coppa_audit(sample_responses)
    print(f"Overall Compliance: {report['summary']['compliance_rate_percent']}%")
    print(f"Passed: {report['summary']['passed']}, Failed: {report['summary']['failed']}")
    print("\nSection Summary:")
    for section, data in report["section_summary"].items():
        print(f"  {section}: {data['section_rate']}% ({data['passed']} pass, {data['failed']} fail)")

    print("\n=== Consent Method Validation ===")
    test_cases = [
        ("email_plus", "internal_use"),
        ("email_plus", "third_party_disclosure"),
        ("credit_card", "third_party_disclosure"),
    ]

    for method, use in test_cases:
        result = validate_consent_method(method, use)
        status = "VALID" if result["valid"] else "INVALID"
        print(f"  {status}: {result['reason']}")
