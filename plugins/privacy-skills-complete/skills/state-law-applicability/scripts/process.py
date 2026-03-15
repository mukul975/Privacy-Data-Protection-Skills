#!/usr/bin/env python3
"""
US State Privacy Law Applicability Assessment Tool

Comprehensive assessment engine evaluating applicability across all
major US state privacy laws based on revenue thresholds, consumer
counts, entity exemptions, data exemptions, and SBA size standards.
"""

import json
from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class EntityType(Enum):
    FOR_PROFIT = "for_profit"
    NONPROFIT = "nonprofit"
    GOVERNMENT = "government"
    GLBA_FINANCIAL = "glba_financial_institution"
    HIPAA_COVERED = "hipaa_covered_entity"
    HIGHER_EDUCATION = "higher_education"
    AIR_CARRIER = "air_carrier"


class ExemptionType(Enum):
    ENTITY_LEVEL = "entity_level"
    DATA_LEVEL = "data_level"
    SMALL_BUSINESS = "small_business"
    NONE = "none"


STATE_CONFIGS = {
    "california": {
        "law": "CCPA/CPRA",
        "citation": "Cal. Civ. Code §1798.140(d)",
        "effective": "2020-01-01",
        "threshold_1": {"type": "consumer_count", "value": 100_000, "exclude_payment": False},
        "threshold_2": {"type": "revenue_pct", "value": 50, "min_consumers": None},
        "threshold_3": {"type": "revenue", "value": 25_000_000},
        "exemptions": {
            EntityType.GOVERNMENT: ExemptionType.NONE,  # CA is for-profit only
            EntityType.GLBA_FINANCIAL: ExemptionType.DATA_LEVEL,
            EntityType.HIPAA_COVERED: ExemptionType.DATA_LEVEL,
            EntityType.NONPROFIT: ExemptionType.NONE,  # Not exempt in CA (for-profit only requirement)
            EntityType.HIGHER_EDUCATION: ExemptionType.NONE,
            EntityType.AIR_CARRIER: ExemptionType.NONE,
        },
        "for_profit_only": True,
        "employee_data": "fully_covered",
    },
    "virginia": {
        "law": "VCDPA",
        "citation": "Va. Code §59.1-576",
        "effective": "2023-01-01",
        "threshold_1": {"type": "consumer_count", "value": 100_000, "exclude_payment": False},
        "threshold_2": {"type": "consumer_revenue", "consumers": 25_000, "revenue_pct": 50},
        "exemptions": {
            EntityType.GOVERNMENT: ExemptionType.ENTITY_LEVEL,
            EntityType.GLBA_FINANCIAL: ExemptionType.ENTITY_LEVEL,
            EntityType.HIPAA_COVERED: ExemptionType.ENTITY_LEVEL,
            EntityType.NONPROFIT: ExemptionType.ENTITY_LEVEL,
            EntityType.HIGHER_EDUCATION: ExemptionType.ENTITY_LEVEL,
            EntityType.AIR_CARRIER: ExemptionType.NONE,
        },
        "for_profit_only": False,
        "employee_data": "rights_exempt",
    },
    "colorado": {
        "law": "CPA",
        "citation": "C.R.S. §6-1-1304",
        "effective": "2023-07-01",
        "threshold_1": {"type": "consumer_count", "value": 100_000, "exclude_payment": False},
        "threshold_2": {"type": "consumer_revenue", "consumers": 25_000, "revenue_pct": 0},
        "exemptions": {
            EntityType.GOVERNMENT: ExemptionType.ENTITY_LEVEL,
            EntityType.GLBA_FINANCIAL: ExemptionType.ENTITY_LEVEL,
            EntityType.HIPAA_COVERED: ExemptionType.ENTITY_LEVEL,
            EntityType.NONPROFIT: ExemptionType.ENTITY_LEVEL,
            EntityType.HIGHER_EDUCATION: ExemptionType.ENTITY_LEVEL,
            EntityType.AIR_CARRIER: ExemptionType.NONE,
        },
        "for_profit_only": False,
        "employee_data": "rights_exempt",
    },
    "connecticut": {
        "law": "CTDPA",
        "citation": "Conn. Gen. Stat. §42-516",
        "effective": "2023-07-01",
        "threshold_1": {"type": "consumer_count", "value": 100_000, "exclude_payment": True},
        "threshold_2": {"type": "consumer_revenue", "consumers": 25_000, "revenue_pct": 25},
        "exemptions": {
            EntityType.GOVERNMENT: ExemptionType.ENTITY_LEVEL,
            EntityType.GLBA_FINANCIAL: ExemptionType.ENTITY_LEVEL,
            EntityType.HIPAA_COVERED: ExemptionType.ENTITY_LEVEL,
            EntityType.NONPROFIT: ExemptionType.ENTITY_LEVEL,
            EntityType.HIGHER_EDUCATION: ExemptionType.ENTITY_LEVEL,
            EntityType.AIR_CARRIER: ExemptionType.NONE,
        },
        "for_profit_only": False,
        "employee_data": "rights_exempt",
    },
    "texas": {
        "law": "TDPSA",
        "citation": "Tex. Bus. & Com. Code §541.002",
        "effective": "2024-07-01",
        "threshold_1": {"type": "sba_small_business", "value": None},
        "exemptions": {
            EntityType.GOVERNMENT: ExemptionType.ENTITY_LEVEL,
            EntityType.GLBA_FINANCIAL: ExemptionType.ENTITY_LEVEL,
            EntityType.HIPAA_COVERED: ExemptionType.ENTITY_LEVEL,
            EntityType.NONPROFIT: ExemptionType.ENTITY_LEVEL,
            EntityType.HIGHER_EDUCATION: ExemptionType.ENTITY_LEVEL,
            EntityType.AIR_CARRIER: ExemptionType.NONE,
        },
        "for_profit_only": False,
        "employee_data": "rights_exempt",
    },
    "oregon": {
        "law": "OCPA",
        "citation": "ORS §646A.572",
        "effective": "2024-07-01",
        "threshold_1": {"type": "consumer_count", "value": 100_000, "exclude_payment": True},
        "threshold_2": {"type": "consumer_revenue", "consumers": 25_000, "revenue_pct": 25},
        "exemptions": {
            EntityType.GOVERNMENT: ExemptionType.ENTITY_LEVEL,
            EntityType.GLBA_FINANCIAL: ExemptionType.ENTITY_LEVEL,
            EntityType.HIPAA_COVERED: ExemptionType.ENTITY_LEVEL,
            EntityType.NONPROFIT: ExemptionType.NONE,  # NOT exempt in Oregon
            EntityType.HIGHER_EDUCATION: ExemptionType.NONE,
            EntityType.AIR_CARRIER: ExemptionType.NONE,
        },
        "for_profit_only": False,
        "employee_data": "partial_exemption",
    },
    "montana": {
        "law": "MTDPA",
        "citation": "MCA §30-14-2803",
        "effective": "2024-10-01",
        "threshold_1": {"type": "consumer_count", "value": 50_000, "exclude_payment": True},
        "threshold_2": {"type": "consumer_revenue", "consumers": 25_000, "revenue_pct": 25},
        "exemptions": {
            EntityType.GOVERNMENT: ExemptionType.ENTITY_LEVEL,
            EntityType.GLBA_FINANCIAL: ExemptionType.ENTITY_LEVEL,
            EntityType.HIPAA_COVERED: ExemptionType.ENTITY_LEVEL,
            EntityType.NONPROFIT: ExemptionType.ENTITY_LEVEL,
            EntityType.HIGHER_EDUCATION: ExemptionType.ENTITY_LEVEL,
            EntityType.AIR_CARRIER: ExemptionType.ENTITY_LEVEL,  # Unique to Montana
        },
        "for_profit_only": False,
        "employee_data": "rights_exempt",
    },
    "kentucky": {
        "law": "KPPA",
        "citation": "KRS §367.405",
        "effective": "2026-01-01",
        "threshold_1": {"type": "consumer_count", "value": 100_000, "exclude_payment": False},
        "threshold_2": {"type": "consumer_revenue", "consumers": 25_000, "revenue_pct": 50},
        "exemptions": {
            EntityType.GOVERNMENT: ExemptionType.ENTITY_LEVEL,
            EntityType.GLBA_FINANCIAL: ExemptionType.ENTITY_LEVEL,
            EntityType.HIPAA_COVERED: ExemptionType.ENTITY_LEVEL,
            EntityType.NONPROFIT: ExemptionType.ENTITY_LEVEL,
            EntityType.HIGHER_EDUCATION: ExemptionType.ENTITY_LEVEL,
            EntityType.AIR_CARRIER: ExemptionType.NONE,
        },
        "for_profit_only": False,
        "employee_data": "rights_exempt",
    },
}

SBA_SIZE_STANDARDS = {
    "454110": {"industry": "Electronic shopping and mail-order houses", "threshold": 40_000_000, "metric": "revenue"},
    "519130": {"industry": "Internet publishing and web search portals", "threshold": 47_000_000, "metric": "revenue"},
    "518210": {"industry": "Data processing, hosting, and related services", "threshold": 35_000_000, "metric": "revenue"},
    "511210": {"industry": "Software publishers", "threshold": 47_000_000, "metric": "revenue"},
    "541511": {"industry": "Custom computer programming services", "threshold": 34_000_000, "metric": "revenue"},
    "541512": {"industry": "Computer systems design services", "threshold": 34_000_000, "metric": "revenue"},
    "522110": {"industry": "Commercial banking", "threshold": 750_000_000, "metric": "assets"},
    "621111": {"industry": "Offices of physicians", "threshold": 16_000_000, "metric": "revenue"},
}


@dataclass
class OrganizationProfile:
    """Organization data needed for applicability assessment."""
    name: str
    annual_revenue: float
    entity_types: list[EntityType] = field(default_factory=list)
    naics_code: str = ""
    employee_count: int = 0
    is_for_profit: bool = True
    state_consumer_counts: dict = field(default_factory=dict)
    state_consumer_counts_excl_payment: dict = field(default_factory=dict)
    revenue_from_data_sale_pct: float = 0.0
    derives_revenue_from_sale: bool = False
    has_federal_data: dict = field(default_factory=dict)  # {"glba": True, "hipaa": False, ...}


def assess_sba_small_business(naics_code: str, annual_revenue: float, employee_count: int) -> dict:
    """Determine SBA small business status for Texas TDPSA."""
    standard = SBA_SIZE_STANDARDS.get(naics_code)
    if not standard:
        return {
            "naics_code": naics_code,
            "determination": "manual_review_required",
            "note": f"NAICS code {naics_code} not in lookup table. Check 13 CFR §121.201.",
        }

    if standard["metric"] == "revenue":
        is_small = annual_revenue <= standard["threshold"]
        return {
            "naics_code": naics_code,
            "industry": standard["industry"],
            "metric": "annual_receipts",
            "threshold": f"${standard['threshold']:,}",
            "organization_value": f"${annual_revenue:,.0f}",
            "is_small_business": is_small,
        }
    elif standard["metric"] == "assets":
        return {
            "naics_code": naics_code,
            "industry": standard["industry"],
            "metric": "total_assets",
            "threshold": f"${standard['threshold']:,}",
            "note": "Asset-based threshold — manual verification required",
            "is_small_business": None,
        }
    return {"naics_code": naics_code, "determination": "unknown_metric"}


def assess_state(state: str, org: OrganizationProfile) -> dict:
    """Assess applicability for a single state."""
    config = STATE_CONFIGS.get(state)
    if not config:
        return {"state": state, "error": "State not configured"}

    result = {
        "state": state,
        "law": config["law"],
        "citation": config["citation"],
        "effective": config["effective"],
        "applicable": False,
        "basis": [],
        "exemptions_checked": [],
        "employee_data_status": config.get("employee_data", "unknown"),
    }

    # Check for-profit requirement (California)
    if config.get("for_profit_only") and not org.is_for_profit:
        result["applicable"] = False
        result["basis"].append("Not a for-profit entity (California requires for-profit)")
        return result

    # Check entity-level exemptions
    for entity_type in org.entity_types:
        exemption = config["exemptions"].get(entity_type)
        if exemption == ExemptionType.ENTITY_LEVEL:
            result["applicable"] = False
            result["basis"].append(f"Entity-level exemption: {entity_type.value}")
            result["exemptions_checked"].append({
                "type": entity_type.value,
                "exemption": "entity_level",
            })
            return result
        elif exemption == ExemptionType.DATA_LEVEL:
            result["exemptions_checked"].append({
                "type": entity_type.value,
                "exemption": "data_level",
                "note": "Entity subject to law for non-exempt data",
            })

    # Check thresholds
    consumer_count = org.state_consumer_counts.get(state, 0)
    consumer_count_excl_payment = org.state_consumer_counts_excl_payment.get(state, consumer_count)

    # Threshold 1
    t1 = config.get("threshold_1", {})
    if t1.get("type") == "consumer_count":
        count = consumer_count_excl_payment if t1.get("exclude_payment") else consumer_count
        if count >= t1["value"]:
            result["applicable"] = True
            result["basis"].append(f"Threshold 1: {count:,} consumers >= {t1['value']:,}")

    elif t1.get("type") == "sba_small_business":
        sba = assess_sba_small_business(org.naics_code, org.annual_revenue, org.employee_count)
        if sba.get("is_small_business") is False:
            result["applicable"] = True
            result["basis"].append("Non-SBA small business — no consumer/revenue threshold")
        elif sba.get("is_small_business") is True:
            result["applicable"] = False
            result["basis"].append("SBA small business — most provisions exempt")
            result["note"] = "§541.107(b) prohibition on selling sensitive data still applies"
        result["sba_analysis"] = sba

    # Threshold 2 (consumer + revenue)
    t2 = config.get("threshold_2", {})
    if t2 and not result["applicable"]:
        if t2.get("type") == "consumer_revenue":
            min_consumers = t2.get("consumers", 25_000)
            min_revenue_pct = t2.get("revenue_pct", 0)
            if consumer_count >= min_consumers:
                if min_revenue_pct == 0 and org.derives_revenue_from_sale:
                    result["applicable"] = True
                    result["basis"].append(f"Threshold 2: {consumer_count:,} consumers >= {min_consumers:,} + derives revenue from sale")
                elif org.revenue_from_data_sale_pct > min_revenue_pct:
                    result["applicable"] = True
                    result["basis"].append(f"Threshold 2: {consumer_count:,} consumers >= {min_consumers:,} + {org.revenue_from_data_sale_pct}% > {min_revenue_pct}% revenue")

        elif t2.get("type") == "revenue_pct":
            if org.revenue_from_data_sale_pct >= t2["value"]:
                result["applicable"] = True
                result["basis"].append(f"Revenue threshold: {org.revenue_from_data_sale_pct}% >= {t2['value']}% revenue from sale")

    # Threshold 3 (California revenue alternative)
    t3 = config.get("threshold_3", {})
    if t3 and not result["applicable"]:
        if t3.get("type") == "revenue" and org.annual_revenue > t3["value"]:
            result["applicable"] = True
            result["basis"].append(f"Revenue alternative: ${org.annual_revenue:,.0f} > ${t3['value']:,}")

    if not result["applicable"] and not result["basis"]:
        result["basis"].append("Below all applicable thresholds")

    return result


def full_assessment(org: OrganizationProfile) -> dict:
    """Run full applicability assessment across all states."""
    results = []
    applicable_states = []
    non_applicable_states = []

    for state in STATE_CONFIGS:
        state_result = assess_state(state, org)
        results.append(state_result)
        if state_result["applicable"]:
            applicable_states.append(state)
        else:
            non_applicable_states.append(state)

    return {
        "organization": org.name,
        "assessment_date": datetime.now(timezone.utc).isoformat(),
        "total_states": len(STATE_CONFIGS),
        "applicable_count": len(applicable_states),
        "applicable_states": applicable_states,
        "non_applicable_states": non_applicable_states,
        "state_results": results,
    }


if __name__ == "__main__":
    # Liberty Commerce Inc. assessment
    org = OrganizationProfile(
        name="Liberty Commerce Inc.",
        annual_revenue=48_000_000,
        entity_types=[],
        naics_code="454110",
        employee_count=320,
        is_for_profit=True,
        state_consumer_counts={
            "california": 320_000, "virginia": 145_000, "colorado": 98_000,
            "connecticut": 87_000, "texas": 410_000, "oregon": 72_000,
            "montana": 28_000, "kentucky": 68_000,
        },
        state_consumer_counts_excl_payment={
            "california": 320_000, "virginia": 145_000, "colorado": 98_000,
            "connecticut": 87_000, "texas": 410_000, "oregon": 72_000,
            "montana": 28_000, "kentucky": 68_000,
        },
        revenue_from_data_sale_pct=12.0,
        derives_revenue_from_sale=True,
    )

    report = full_assessment(org)
    print("=== Full Applicability Assessment ===")
    print(f"Organization: {report['organization']}")
    print(f"Applicable in {report['applicable_count']}/{report['total_states']} states: {', '.join(report['applicable_states'])}")
    print(f"Not applicable: {', '.join(report['non_applicable_states'])}")

    print("\n=== State-by-State Results ===")
    for sr in report["state_results"]:
        status = "APPLICABLE" if sr["applicable"] else "NOT APPLICABLE"
        print(f"\n  {sr['state'].upper()} ({sr['law']}): {status}")
        for basis in sr["basis"]:
            print(f"    - {basis}")
        if sr.get("exemptions_checked"):
            for exc in sr["exemptions_checked"]:
                print(f"    - Exemption: {exc['type']} → {exc['exemption']}")
        if sr.get("sba_analysis"):
            sba = sr["sba_analysis"]
            print(f"    - SBA: {sba.get('industry', 'N/A')} | Small business: {sba.get('is_small_business')}")
        print(f"    - Employee data: {sr['employee_data_status']}")
