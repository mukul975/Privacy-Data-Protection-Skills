#!/usr/bin/env python3
"""
UK International Data Transfer Compliance Engine

Manages UK IDTA and Addendum implementation, ICO Transfer Risk
Assessment, and dual EU-UK transfer tracking.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


UK_ADEQUATE_COUNTRIES = {
    "EU_EEA": {"name": "EU/EEA Member States", "regulation": "Data Protection (Adequacy) (EEA and Gibraltar) Regulations 2019", "effective": "2021-01-01"},
    "AD": {"name": "Andorra", "regulation": "Data Protection (Adequacy) Regulations 2023", "effective": "2023-10-12"},
    "AR": {"name": "Argentina", "regulation": "Data Protection (Adequacy) Regulations 2023", "effective": "2023-10-12"},
    "CA": {"name": "Canada (PIPEDA)", "regulation": "Data Protection (Adequacy) Regulations 2023", "effective": "2023-10-12"},
    "FO": {"name": "Faroe Islands", "regulation": "Data Protection (Adequacy) Regulations 2023", "effective": "2023-10-12"},
    "GG": {"name": "Guernsey", "regulation": "Data Protection (Adequacy) Regulations 2023", "effective": "2023-10-12"},
    "IL": {"name": "Israel", "regulation": "Data Protection (Adequacy) Regulations 2023", "effective": "2023-10-12"},
    "IM": {"name": "Isle of Man", "regulation": "Data Protection (Adequacy) Regulations 2023", "effective": "2023-10-12"},
    "JP": {"name": "Japan", "regulation": "Data Protection (Adequacy) Regulations 2023", "effective": "2023-10-12"},
    "JE": {"name": "Jersey", "regulation": "Data Protection (Adequacy) Regulations 2023", "effective": "2023-10-12"},
    "NZ": {"name": "New Zealand", "regulation": "Data Protection (Adequacy) Regulations 2023", "effective": "2023-10-12"},
    "KR": {"name": "South Korea", "regulation": "Data Protection (Adequacy) Regulations 2024", "effective": "2024-01-01"},
    "CH": {"name": "Switzerland", "regulation": "Data Protection (Adequacy) Regulations 2023", "effective": "2023-10-12"},
    "UY": {"name": "Uruguay", "regulation": "Data Protection (Adequacy) Regulations 2023", "effective": "2023-10-12"},
    "US_DATA_BRIDGE": {"name": "United States (UK-US Data Bridge)", "regulation": "Data Protection (Adequacy) Regulations 2023", "effective": "2023-10-12"},
}

TRA_RISK_FACTORS = {
    "rule_of_law": {"weight": 3, "description": "Rule of law, independent judiciary, and human rights record"},
    "data_protection_law": {"weight": 3, "description": "Comprehensive data protection legislation with individual rights"},
    "government_access": {"weight": 4, "description": "Government access laws, necessity, proportionality, oversight"},
    "enforcement_redress": {"weight": 3, "description": "Enforcement mechanisms and individual redress availability"},
    "data_sensitivity": {"weight": 2, "description": "Sensitivity of the specific data being transferred"},
    "transfer_volume": {"weight": 1, "description": "Volume and frequency of the transfer"},
    "importer_profile": {"weight": 2, "description": "Importer sector, size, and government access history"},
    "technical_measures": {"weight": 3, "description": "Technical protections applied to the transfer"},
}


def check_uk_adequacy(country_code: str) -> dict:
    """Check whether a country has UK adequacy regulations."""
    country = UK_ADEQUATE_COUNTRIES.get(country_code.upper())
    if country:
        return {
            "country_code": country_code.upper(),
            "country_name": country["name"],
            "has_adequacy": True,
            "regulation": country["regulation"],
            "effective_date": country["effective"],
            "transfer_mechanism": "UK adequacy regulations — no additional mechanism required",
            "note": "Verify adequacy regulations remain in force at time of transfer",
        }
    return {
        "country_code": country_code.upper(),
        "has_adequacy": False,
        "transfer_mechanism": "IDTA or UK Addendum to EU SCCs required",
        "note": "Conduct ICO Transfer Risk Assessment before transfer",
    }


def conduct_uk_tra(
    destination_country: str,
    risk_scores: dict,
    data_categories: list,
    includes_special_category: bool = False,
) -> dict:
    """Conduct an ICO-aligned Transfer Risk Assessment."""
    total_weighted_score = 0
    max_weighted_score = 0
    factor_results = {}

    for factor_key, factor_info in TRA_RISK_FACTORS.items():
        score = risk_scores.get(factor_key, 0)  # 0-5 scale: 0=very poor, 5=equivalent to UK
        weight = factor_info["weight"]
        weighted = score * weight
        total_weighted_score += weighted
        max_weighted_score += 5 * weight

        factor_results[factor_key] = {
            "description": factor_info["description"],
            "score": score,
            "weight": weight,
            "weighted_score": weighted,
        }

    overall_pct = round(total_weighted_score / max_weighted_score * 100, 1) if max_weighted_score else 0

    if includes_special_category:
        overall_pct = max(0, overall_pct - 10)

    if overall_pct >= 75:
        risk_level = "low"
        conclusion = "Transfer likely provides essentially equivalent protection; IDTA/Addendum sufficient"
        extra_protection_needed = False
    elif overall_pct >= 50:
        risk_level = "medium"
        conclusion = "Protection gaps identified; Extra Protection Clauses (supplementary measures) required"
        extra_protection_needed = True
    elif overall_pct >= 25:
        risk_level = "high"
        conclusion = "Significant protection gaps; strong supplementary measures essential; consider feasibility"
        extra_protection_needed = True
    else:
        risk_level = "very-high"
        conclusion = "Fundamental protection gaps; transfer may not be possible with sufficient safeguards"
        extra_protection_needed = True

    return {
        "tra_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "destination_country": destination_country,
        "data_categories": data_categories,
        "includes_special_category": includes_special_category,
        "factor_results": factor_results,
        "overall_score_pct": overall_pct,
        "risk_level": risk_level,
        "conclusion": conclusion,
        "extra_protection_clauses_needed": extra_protection_needed,
    }


def generate_idta_record(
    exporter_name: str,
    exporter_address: str,
    importer_name: str,
    importer_address: str,
    importer_country: str,
    transfer_purpose: str,
    data_categories: list,
    data_subjects: list,
    frequency: str,
    retention: str,
    tra_reference: str,
    extra_protection_clauses: Optional[list] = None,
) -> dict:
    """Generate an IDTA documentation record."""
    return {
        "instrument": "International Data Transfer Agreement (IDTA)",
        "effective_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "table_1_parties": {
            "exporter": {
                "name": exporter_name,
                "address": exporter_address,
                "role": "Exporter",
            },
            "importer": {
                "name": importer_name,
                "address": importer_address,
                "country": importer_country,
                "role": "Importer",
            },
        },
        "table_2_transfer_details": {
            "purpose": transfer_purpose,
            "data_categories": data_categories,
            "data_subjects": data_subjects,
            "frequency": frequency,
            "retention": retention,
        },
        "table_4_extra_protection": extra_protection_clauses or [],
        "tra_reference": tra_reference,
        "review_date": (datetime.utcnow() + timedelta(days=365)).strftime("%Y-%m-%d"),
    }


def generate_addendum_record(
    eu_scc_reference: str,
    eu_scc_module: str,
    eu_scc_date: str,
    uk_exporter: str,
    importer: str,
    tra_reference: str,
) -> dict:
    """Generate a UK Addendum record linked to existing EU SCCs."""
    return {
        "instrument": "UK Addendum to EU Standard Contractual Clauses",
        "addendum_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "table_1": {
            "eu_scc_reference": eu_scc_reference,
            "parties": f"{uk_exporter} (Exporter) and {importer} (Importer)",
        },
        "table_2": {
            "eu_scc_version": "Commission Implementing Decision (EU) 2021/914",
            "selected_module": eu_scc_module,
            "eu_scc_execution_date": eu_scc_date,
        },
        "table_3": "Appendix information as per EU SCC Annexes I-III",
        "table_4": {
            "ending_approach": "The parties may end the Addendum as set out in Section 19 of the Mandatory Clauses",
            "alternative": "Neither party may end the Addendum if the Approved Addendum is changed",
        },
        "tra_reference": tra_reference,
        "review_date": (datetime.utcnow() + timedelta(days=365)).strftime("%Y-%m-%d"),
    }


def dual_transfer_register(
    eu_exporter: str,
    uk_exporter: str,
    importer: str,
    importer_country: str,
    eu_mechanism: str,
    uk_mechanism: str,
    eu_tia_ref: str,
    uk_tra_ref: str,
) -> dict:
    """Generate dual EU-UK transfer register entries."""
    return {
        "eu_transfer": {
            "exporter": eu_exporter,
            "importer": importer,
            "country": importer_country,
            "mechanism": eu_mechanism,
            "tia_reference": eu_tia_ref,
            "governing_law": "EU GDPR",
        },
        "uk_transfer": {
            "exporter": uk_exporter,
            "importer": importer,
            "country": importer_country,
            "mechanism": uk_mechanism,
            "tra_reference": uk_tra_ref,
            "governing_law": "UK GDPR",
        },
        "common_review_date": (datetime.utcnow() + timedelta(days=365)).strftime("%Y-%m-%d"),
    }


if __name__ == "__main__":
    print("=== UK Adequacy Check ===")
    print(json.dumps(check_uk_adequacy("JP"), indent=2))
    print(json.dumps(check_uk_adequacy("HK"), indent=2))

    print("\n=== UK Transfer Risk Assessment ===")
    tra = conduct_uk_tra(
        destination_country="Hong Kong SAR",
        risk_scores={
            "rule_of_law": 4,
            "data_protection_law": 3,
            "government_access": 2,
            "enforcement_redress": 3,
            "data_sensitivity": 4,
            "transfer_volume": 3,
            "importer_profile": 4,
            "technical_measures": 4,
        },
        data_categories=["customer names", "shipping addresses", "customs IDs"],
    )
    print(json.dumps(tra, indent=2))

    print("\n=== Dual EU-UK Register ===")
    dual = dual_transfer_register(
        eu_exporter="Athena Global Logistics GmbH",
        uk_exporter="Athena Logistics (UK) Ltd",
        importer="TransPacific Freight Solutions Ltd",
        importer_country="Hong Kong SAR",
        eu_mechanism="EU SCCs Module 2 (Decision 2021/914)",
        uk_mechanism="UK Addendum to EU SCCs",
        eu_tia_ref="TIA-2025-HK-001",
        uk_tra_ref="TRA-2025-HK-001",
    )
    print(json.dumps(dual, indent=2))
