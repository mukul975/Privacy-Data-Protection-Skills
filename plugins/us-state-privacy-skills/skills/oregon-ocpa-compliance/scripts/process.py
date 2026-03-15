#!/usr/bin/env python3
"""
Oregon OCPA Compliance Tool

Assesses OCPA applicability, evaluates de-identified data compliance
per §646A.586, tracks third-party disclosure requests, and manages
employee data partial exemption assessment.
"""

import json
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class OCPARight(Enum):
    ACCESS = "access"
    CORRECT = "correct"
    DELETE = "delete"
    PORTABILITY = "portability"
    OPT_OUT_TARGETED_ADS = "opt_out_targeted_advertising"
    OPT_OUT_SALE = "opt_out_sale"
    OPT_OUT_PROFILING = "opt_out_profiling"
    THIRD_PARTY_LIST = "third_party_disclosure_list"


DEIDENTIFICATION_CHECKLIST = [
    {"id": "DI-01", "item": "Direct identifiers removed", "section": "§646A.586(1)", "description": "Names, SSN, email, phone, address removed or masked"},
    {"id": "DI-02", "item": "Technical safeguards applied", "section": "§646A.586(1)", "description": "K-anonymity, differential privacy, or equivalent applied"},
    {"id": "DI-03", "item": "Public commitment posted", "section": "§646A.586(2)", "description": "Public statement committing to maintain de-identified form"},
    {"id": "DI-04", "item": "Recipient contracts executed", "section": "§646A.586(3)", "description": "Data use agreements prohibiting re-identification"},
    {"id": "DI-05", "item": "Oversight mechanism in place", "section": "§646A.586(4)", "description": "Monitoring of recipient compliance"},
    {"id": "DI-06", "item": "Risk assessment conducted", "section": "§646A.586(5)", "description": "Regular assessment of re-identification risk"},
    {"id": "DI-07", "item": "Remediation process defined", "section": "§646A.586(5)", "description": "Process to address re-identification incidents"},
    {"id": "DI-08", "item": "Access controls implemented", "section": "§646A.586(1)", "description": "Restricted access to de-identified datasets"},
    {"id": "DI-09", "item": "Re-identification keys separated", "section": "§646A.586(1)", "description": "Keys stored separately with restricted access"},
    {"id": "DI-10", "item": "Destruction policy defined", "section": "§646A.586(5)", "description": "Policy to destroy data if de-identification fails"},
]

EMPLOYEE_DATA_PROVISIONS = {
    "exempt": [
        {"provision": "Consumer rights (access, correct, delete, portability, opt-out)", "section": "§646A.578"},
        {"provision": "Consumer request processing procedures", "section": "§646A.580"},
    ],
    "not_exempt": [
        {"provision": "Controller duties (privacy notice, minimization, security)", "section": "§646A.576"},
        {"provision": "Processor contracts", "section": "§646A.582"},
        {"provision": "Data protection assessments", "section": "§646A.584"},
        {"provision": "De-identified data requirements", "section": "§646A.586"},
        {"provision": "Sensitive data consent", "section": "§646A.576(8)"},
    ],
}

SENSITIVE_DATA_CATEGORIES = [
    "Racial or ethnic origin",
    "Religious beliefs",
    "Mental or physical health diagnosis",
    "Sexual orientation",
    "Citizenship or immigration status",
    "Genetic or biometric data for identification",
    "Known child's personal data",
    "Precise geolocation data",
    "Transgender or nonbinary status",  # Unique to Oregon
]


@dataclass
class OCPAApplicability:
    """Assess OCPA applicability."""
    organization_name: str
    conducts_business_in_oregon: bool
    targets_oregon_residents: bool
    oregon_consumer_count: int
    oregon_consumer_count_excl_payment: int
    revenue_from_sale_pct: float
    is_nonprofit: bool = False
    is_government: bool = False
    is_glba: bool = False
    is_hipaa: bool = False

    def assess(self) -> dict:
        exemptions = []
        if self.is_government:
            exemptions.append({"name": "Government body", "section": "§646A.572(2)(a)"})
        if self.is_glba:
            exemptions.append({"name": "GLBA institution", "section": "§646A.572(2)(b)"})
        if self.is_hipaa:
            exemptions.append({"name": "HIPAA covered entity/BA", "section": "§646A.572(2)(c)"})

        # Note: Nonprofits are NOT exempt under OCPA
        if self.is_nonprofit:
            note = "OCPA applies to nonprofit organizations — no nonprofit exemption"
        else:
            note = ""

        if exemptions:
            return {
                "organization": self.organization_name,
                "applicable": False,
                "exemptions": exemptions,
            }

        if not (self.conducts_business_in_oregon or self.targets_oregon_residents):
            return {"organization": self.organization_name, "applicable": False, "reason": "No Oregon nexus"}

        thresholds_met = []
        if self.oregon_consumer_count_excl_payment >= 100_000:
            thresholds_met.append({
                "threshold": "option_1",
                "description": f"{self.oregon_consumer_count_excl_payment:,} consumers (excl. payment) >= 100,000",
                "section": "§646A.572(1)(a)",
            })
        if self.oregon_consumer_count_excl_payment >= 25_000 and self.revenue_from_sale_pct >= 25:
            thresholds_met.append({
                "threshold": "option_2",
                "description": f"{self.oregon_consumer_count_excl_payment:,} consumers >= 25,000 AND {self.revenue_from_sale_pct}% >= 25% revenue from sale",
                "section": "§646A.572(1)(b)",
            })

        result = {
            "organization": self.organization_name,
            "applicable": len(thresholds_met) > 0,
            "thresholds_met": thresholds_met,
            "is_nonprofit": self.is_nonprofit,
            "assessment_date": datetime.now(timezone.utc).isoformat(),
        }
        if note:
            result["note"] = note
        return result


@dataclass
class DeIdentificationAssessment:
    """Assess de-identified data compliance per §646A.586."""
    dataset_name: str
    assessment_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    results: list = field(default_factory=list)

    def run_assessment(self, responses: dict[str, str]) -> dict:
        pass_count = 0
        fail_count = 0
        gaps = []

        for check in DEIDENTIFICATION_CHECKLIST:
            status = responses.get(check["id"], "not_assessed")
            if status == "pass":
                pass_count += 1
            elif status == "fail":
                fail_count += 1
                gaps.append({"check_id": check["id"], "item": check["item"], "section": check["section"]})

            self.results.append({"check_id": check["id"], "item": check["item"], "status": status})

        compliant = fail_count == 0
        return {
            "dataset": self.dataset_name,
            "assessment_date": self.assessment_date,
            "passed": pass_count,
            "failed": fail_count,
            "compliant": compliant,
            "gaps": gaps,
        }


@dataclass
class ThirdPartyDisclosure:
    """Track a specific third-party disclosure for the Oregon third-party list right."""
    third_party_name: str
    disclosure_date: str
    data_categories: list
    purpose: str
    consumer_id: str

    def to_dict(self) -> dict:
        return asdict(self)


def generate_third_party_report(consumer_id: str, disclosures: list[ThirdPartyDisclosure]) -> dict:
    """Generate the specific third-party list per §646A.578(1)(f)."""
    consumer_disclosures = [d for d in disclosures if d.consumer_id == consumer_id]
    return {
        "consumer_id": consumer_id,
        "report_date": datetime.now(timezone.utc).isoformat(),
        "section": "§646A.578(1)(f)",
        "lookback_period": "12 months",
        "third_parties": [d.to_dict() for d in consumer_disclosures],
        "total_disclosures": len(consumer_disclosures),
    }


if __name__ == "__main__":
    # Applicability
    print("=== OCPA Applicability Assessment ===")
    assessment = OCPAApplicability(
        organization_name="Liberty Commerce Inc.",
        conducts_business_in_oregon=True,
        targets_oregon_residents=True,
        oregon_consumer_count=72_000,
        oregon_consumer_count_excl_payment=72_000,
        revenue_from_sale_pct=12.0,
    )
    print(json.dumps(assessment.assess(), indent=2))

    # De-identification assessment
    print("\n=== De-Identification Assessment ===")
    di_assessment = DeIdentificationAssessment(dataset_name="Customer analytics aggregate")
    responses = {
        "DI-01": "pass", "DI-02": "pass", "DI-03": "pass",
        "DI-04": "pass", "DI-05": "fail", "DI-06": "pass",
        "DI-07": "pass", "DI-08": "pass", "DI-09": "pass", "DI-10": "pass",
    }
    print(json.dumps(di_assessment.run_assessment(responses), indent=2))

    # Third-party disclosure report
    print("\n=== Third-Party Disclosure Report ===")
    disclosures = [
        ThirdPartyDisclosure("PaySecure Corp.", "2026-01-15", ["transaction_data"], "Payment processing", "OR-CONS-1234"),
        ThirdPartyDisclosure("SwiftShip Logistics", "2026-02-01", ["shipping_address", "name"], "Order fulfillment", "OR-CONS-1234"),
        ThirdPartyDisclosure("DataInsight Analytics", "2026-01-20", ["browsing_history", "purchase_patterns"], "Analytics", "OR-CONS-1234"),
    ]
    report = generate_third_party_report("OR-CONS-1234", disclosures)
    print(json.dumps(report, indent=2))

    # Sensitive data categories (including Oregon-unique)
    print("\n=== Oregon Sensitive Data Categories ===")
    for i, cat in enumerate(SENSITIVE_DATA_CATEGORIES, 1):
        unique = " (UNIQUE TO OREGON)" if "transgender" in cat.lower() else ""
        print(f"  {i}. {cat}{unique}")

    # Employee data exemption
    print("\n=== Employee Data Partial Exemption ===")
    print("EXEMPT from:")
    for p in EMPLOYEE_DATA_PROVISIONS["exempt"]:
        print(f"  - {p['provision']} ({p['section']})")
    print("NOT EXEMPT from:")
    for p in EMPLOYEE_DATA_PROVISIONS["not_exempt"]:
        print(f"  - {p['provision']} ({p['section']})")
