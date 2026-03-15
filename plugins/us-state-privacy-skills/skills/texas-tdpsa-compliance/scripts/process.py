#!/usr/bin/env python3
"""
Texas TDPSA Compliance Assessment Tool

Assesses TDPSA applicability (including SBA small business determination),
tracks consumer rights requests, and evaluates data broker registration
requirements under Tex. Bus. & Com. Code §541.
"""

import json
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class TDPSARight(Enum):
    ACCESS = "access"
    CORRECT = "correct"
    DELETE = "delete"
    PORTABILITY = "portability"
    OPT_OUT_TARGETED_ADS = "opt_out_targeted_advertising"
    OPT_OUT_SALE = "opt_out_sale"
    OPT_OUT_PROFILING = "opt_out_profiling"


SBA_SIZE_STANDARDS = {
    "454110": {"industry": "Electronic shopping and mail-order houses", "threshold_revenue": 40_000_000},
    "518210": {"industry": "Data processing, hosting, and related services", "threshold_revenue": 35_000_000},
    "541511": {"industry": "Custom computer programming services", "threshold_revenue": 34_000_000},
    "423110": {"industry": "Automobile and motor vehicle merchant wholesalers", "threshold_revenue": 275_000_000},
    "611310": {"industry": "Colleges, universities, and professional schools", "threshold_revenue": 30_000_000},
}

ENTITY_EXEMPTIONS = [
    {"name": "State agency / political subdivision", "section": "§541.003(1)"},
    {"name": "GLBA financial institution", "section": "§541.003(2)"},
    {"name": "HIPAA covered entity / business associate", "section": "§541.003(3)"},
    {"name": "Nonprofit organization", "section": "§541.003(4)"},
    {"name": "Institution of higher education", "section": "§541.003(5)"},
    {"name": "Electric utility (ERCOT)", "section": "§541.003(6)"},
]


@dataclass
class TDPSAApplicability:
    """Assess TDPSA applicability including SBA small business check."""
    organization_name: str
    conducts_business_in_texas: bool
    targets_texas_residents: bool
    processes_personal_data: bool
    naics_code: str
    annual_revenue: float
    employee_count: int
    is_government: bool = False
    is_glba: bool = False
    is_hipaa: bool = False
    is_nonprofit: bool = False
    is_higher_ed: bool = False
    is_electric_utility: bool = False

    def assess(self) -> dict:
        # Entity exemption check
        exemptions = []
        if self.is_government:
            exemptions.append(ENTITY_EXEMPTIONS[0])
        if self.is_glba:
            exemptions.append(ENTITY_EXEMPTIONS[1])
        if self.is_hipaa:
            exemptions.append(ENTITY_EXEMPTIONS[2])
        if self.is_nonprofit:
            exemptions.append(ENTITY_EXEMPTIONS[3])
        if self.is_higher_ed:
            exemptions.append(ENTITY_EXEMPTIONS[4])
        if self.is_electric_utility:
            exemptions.append(ENTITY_EXEMPTIONS[5])

        if exemptions:
            return {
                "organization": self.organization_name,
                "applicable": False,
                "reason": "Entity-level exemption",
                "exemptions": exemptions,
            }

        if not (self.conducts_business_in_texas or self.targets_texas_residents):
            return {"organization": self.organization_name, "applicable": False, "reason": "No Texas nexus"}

        if not self.processes_personal_data:
            return {"organization": self.organization_name, "applicable": False, "reason": "Does not process personal data"}

        # SBA small business check
        sba_standard = SBA_SIZE_STANDARDS.get(self.naics_code)
        is_small_business = False
        sba_analysis = {}

        if sba_standard:
            is_small_business = self.annual_revenue <= sba_standard["threshold_revenue"]
            sba_analysis = {
                "naics_code": self.naics_code,
                "industry": sba_standard["industry"],
                "sba_threshold": f"${sba_standard['threshold_revenue']:,}",
                "annual_revenue": f"${self.annual_revenue:,.0f}",
                "is_small_business": is_small_business,
            }
        else:
            sba_analysis = {
                "naics_code": self.naics_code,
                "note": "NAICS code not in lookup table — manual SBA determination required",
                "is_small_business": None,
            }

        if is_small_business:
            return {
                "organization": self.organization_name,
                "applicable": False,
                "reason": "SBA small business exemption (most provisions)",
                "sba_analysis": sba_analysis,
                "note": "§541.107(b) prohibition on selling sensitive data without consent STILL APPLIES to small businesses",
            }

        return {
            "organization": self.organization_name,
            "applicable": True,
            "reason": "Non-small business that conducts business in Texas and processes personal data",
            "sba_analysis": sba_analysis,
            "note": "No revenue or consumer count threshold — full TDPSA applies",
            "assessment_date": datetime.now(timezone.utc).isoformat(),
        }


@dataclass
class DataBrokerAssessment:
    """Assess whether an organization qualifies as a data broker under §541.201."""
    organization_name: str
    principal_revenue_from_data: bool
    data_collected_directly_from_consumers: bool
    total_revenue: float
    data_related_revenue: float

    def assess(self) -> dict:
        data_revenue_pct = (self.data_related_revenue / self.total_revenue * 100) if self.total_revenue > 0 else 0
        is_data_broker = self.principal_revenue_from_data and not self.data_collected_directly_from_consumers

        result = {
            "organization": self.organization_name,
            "is_data_broker": is_data_broker,
            "section": "§541.201",
            "data_revenue_percentage": round(data_revenue_pct, 1),
            "principal_revenue_from_data": self.principal_revenue_from_data,
            "data_collected_directly": self.data_collected_directly_from_consumers,
        }

        if is_data_broker:
            result["obligations"] = [
                "Register with Texas Secretary of State (§541.202)",
                "Pay registration fee",
                "Disclose data collection practices",
                "Report breach history (preceding 3 years)",
                "Provide consumer opt-out mechanism (§541.203)",
                "Provide access and deletion mechanisms",
            ]
        else:
            result["note"] = "Not a data broker — registration not required"

        return result


@dataclass
class BiometricComplianceCheck:
    """Assess CUBI compliance for biometric data processing."""
    organization_name: str
    captures_biometric_identifiers: bool
    biometric_types: list = field(default_factory=list)
    informed_consent_obtained: bool = False
    storage_protections: bool = False
    destruction_policy: bool = False
    no_sale_or_disclosure: bool = False

    def assess(self) -> dict:
        if not self.captures_biometric_identifiers:
            return {
                "organization": self.organization_name,
                "cubi_applicable": False,
                "note": "Does not capture biometric identifiers — CUBI not applicable",
            }

        checks = {
            "informed_consent": self.informed_consent_obtained,
            "storage_protection": self.storage_protections,
            "destruction_policy": self.destruction_policy,
            "no_unauthorized_disclosure": self.no_sale_or_disclosure,
        }
        compliant = all(checks.values())
        failed = [k for k, v in checks.items() if not v]

        return {
            "organization": self.organization_name,
            "cubi_applicable": True,
            "biometric_types": self.biometric_types,
            "compliant": compliant,
            "checks": checks,
            "failed_checks": failed,
            "penalty_exposure": "Up to $25,000 per violation" if not compliant else "None",
        }


if __name__ == "__main__":
    # TDPSA applicability
    print("=== TDPSA Applicability Assessment ===")
    assessment = TDPSAApplicability(
        organization_name="Liberty Commerce Inc.",
        conducts_business_in_texas=True,
        targets_texas_residents=True,
        processes_personal_data=True,
        naics_code="454110",
        annual_revenue=48_000_000,
        employee_count=320,
    )
    print(json.dumps(assessment.assess(), indent=2))

    # Data broker assessment
    print("\n=== Data Broker Assessment ===")
    broker = DataBrokerAssessment(
        organization_name="Liberty Commerce Inc.",
        principal_revenue_from_data=False,
        data_collected_directly_from_consumers=True,
        total_revenue=48_000_000,
        data_related_revenue=5_760_000,
    )
    print(json.dumps(broker.assess(), indent=2))

    # Biometric compliance
    print("\n=== CUBI Biometric Compliance ===")
    biometric = BiometricComplianceCheck(
        organization_name="Liberty Commerce Inc.",
        captures_biometric_identifiers=False,
    )
    print(json.dumps(biometric.assess(), indent=2))
