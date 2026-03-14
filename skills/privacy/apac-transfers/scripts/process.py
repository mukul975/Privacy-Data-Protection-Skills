#!/usr/bin/env python3
"""
APAC Cross-Border Transfer Compliance Engine

Manages transfer mechanism selection across APAC jurisdictions,
tracks multi-jurisdiction transfer chains, and generates compliance reports.
"""

import json
from datetime import datetime
from typing import Optional


APAC_JURISDICTIONS = {
    "JP": {
        "country": "Japan",
        "law": "APPI (Act No. 57 of 2003, as amended 2022)",
        "transfer_article": "Art. 28",
        "adequate_countries": ["EU/EEA", "UK"],
        "mechanisms": ["adequate_country", "equivalent_measures", "consent"],
        "cbpr_participant": True,
    },
    "KR": {
        "country": "South Korea",
        "law": "PIPA (as amended 2023)",
        "transfer_article": "Art. 28-2",
        "adequate_countries": ["EU/EEA"],
        "mechanisms": ["adequacy_recognition", "consent", "contractual_safeguards", "certification"],
        "cbpr_participant": True,
    },
    "TH": {
        "country": "Thailand",
        "law": "PDPA B.E. 2562 (2019)",
        "transfer_article": "Section 28",
        "adequate_countries": [],
        "mechanisms": ["adequate_country", "bcr", "contractual_safeguards", "consent", "derogation"],
        "cbpr_participant": False,
    },
    "SG": {
        "country": "Singapore",
        "law": "PDPA 2012 (as amended 2021)",
        "transfer_article": "Section 26",
        "adequate_countries": [],
        "mechanisms": ["contractual_arrangements", "cbpr_certification", "consent", "exceptions"],
        "cbpr_participant": True,
    },
    "HK": {
        "country": "Hong Kong SAR",
        "law": "PDPO (Cap. 486)",
        "transfer_article": "Section 33 (not yet commenced)",
        "adequate_countries": [],
        "mechanisms": ["contractual_arrangements", "consent"],
        "cbpr_participant": False,
        "note": "Section 33 not in force; transfers governed by contractual arrangements",
    },
    "PH": {
        "country": "Philippines",
        "law": "Data Privacy Act 2012 (RA 10173)",
        "transfer_article": "Section 21",
        "adequate_countries": [],
        "mechanisms": ["consent", "contractual_safeguards", "binding_corporate_rules", "adequacy"],
        "cbpr_participant": True,
    },
    "AU": {
        "country": "Australia",
        "law": "Privacy Act 1988 (as amended)",
        "transfer_article": "APP 8",
        "adequate_countries": [],
        "mechanisms": ["reasonable_steps", "consent", "contractual_arrangements"],
        "cbpr_participant": True,
    },
    "VN": {
        "country": "Vietnam",
        "law": "Decree 13/2023/ND-CP",
        "transfer_article": "Art. 25-26",
        "adequate_countries": [],
        "mechanisms": ["impact_assessment", "consent"],
        "cbpr_participant": False,
    },
}

CBPR_ACCOUNTABILITY_AGENTS = {
    "US": "TRUSTe / TrustArc",
    "JP": "JIPDEC (Japan Institute for Promotion of Digital Economy and Community)",
    "SG": "IMDA (Infocomm Media Development Authority)",
    "KR": "KCC (Korea Communications Commission)",
    "PH": "NPC (National Privacy Commission)",
}


def determine_apac_mechanism(
    source_country: str,
    destination_country: str,
    has_contractual_safeguards: bool = False,
    has_consent: bool = False,
    recipient_cbpr_certified: bool = False,
    recipient_has_equivalent_measures: bool = False,
) -> dict:
    """Determine the appropriate transfer mechanism for an APAC transfer."""
    source = APAC_JURISDICTIONS.get(source_country.upper())
    if not source:
        return {"error": f"Source jurisdiction '{source_country}' not found in APAC database"}

    dest_name = APAC_JURISDICTIONS.get(destination_country.upper(), {}).get("country", destination_country)

    # Check if destination is adequate under source country's rules
    is_adequate = any(
        dest_name in adeq or destination_country.upper() in adeq
        for adeq in source["adequate_countries"]
    )
    if destination_country.upper() in ("DE", "FR", "NL", "IT", "ES", "AT", "BE", "IE"):
        is_adequate = "EU/EEA" in source["adequate_countries"]

    if is_adequate:
        return {
            "source": source["country"],
            "destination": dest_name,
            "mechanism": "adequate_country",
            "description": f"{dest_name} is recognised as adequate under {source['law']}",
            "additional_required": "Document adequacy reliance in transfer register",
            "compliant": True,
        }

    mechanisms_available = []

    if recipient_has_equivalent_measures and source_country.upper() == "JP":
        mechanisms_available.append({
            "mechanism": "equivalent_measures",
            "description": "Recipient has established APPI-equivalent measures (internal rules + oversight)",
            "strength": "high",
        })

    if has_contractual_safeguards:
        mechanisms_available.append({
            "mechanism": "contractual_safeguards",
            "description": f"Contractual arrangements binding recipient to {source['law']}-equivalent standards",
            "strength": "high",
        })

    if recipient_cbpr_certified and source.get("cbpr_participant"):
        mechanisms_available.append({
            "mechanism": "cbpr_certification",
            "description": "Recipient holds APEC CBPR certification",
            "strength": "medium-high",
        })

    if has_consent:
        mechanisms_available.append({
            "mechanism": "consent",
            "description": f"Data subject consent obtained per {source['transfer_article']}",
            "strength": "medium",
        })

    if mechanisms_available:
        best = max(mechanisms_available, key=lambda m: {"high": 3, "medium-high": 2, "medium": 1}.get(m["strength"], 0))
        return {
            "source": source["country"],
            "destination": dest_name,
            "mechanism": best["mechanism"],
            "description": best["description"],
            "all_available_mechanisms": mechanisms_available,
            "compliant": True,
        }

    return {
        "source": source["country"],
        "destination": dest_name,
        "mechanism": None,
        "compliant": False,
        "recommendation": f"No transfer mechanism available. Options: (1) execute contractual safeguards; "
        f"(2) obtain data subject consent per {source['transfer_article']}; "
        f"(3) pursue CBPR certification for the recipient",
    }


def assess_transfer_chain(chain: list) -> dict:
    """Assess compliance of a multi-jurisdiction transfer chain."""
    legs = []
    all_compliant = True

    for i in range(len(chain) - 1):
        source = chain[i]
        dest = chain[i + 1]
        leg = determine_apac_mechanism(
            source_country=source["country_code"],
            destination_country=dest["country_code"],
            has_contractual_safeguards=dest.get("has_contract", False),
            has_consent=dest.get("has_consent", False),
            recipient_cbpr_certified=dest.get("cbpr_certified", False),
            recipient_has_equivalent_measures=dest.get("equivalent_measures", False),
        )
        leg["leg_number"] = i + 1
        leg["source_entity"] = source.get("entity", "")
        leg["destination_entity"] = dest.get("entity", "")
        legs.append(leg)
        if not leg.get("compliant", False):
            all_compliant = False

    return {
        "assessment_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "total_legs": len(legs),
        "all_legs_compliant": all_compliant,
        "legs": legs,
        "recommendation": "All legs of the transfer chain are compliant"
        if all_compliant
        else "One or more legs lack a valid mechanism — resolve before proceeding",
    }


def generate_apac_compliance_dashboard(transfers: list) -> dict:
    """Generate a dashboard of APAC transfer compliance status."""
    by_jurisdiction = {}
    total = len(transfers)
    compliant = 0

    for t in transfers:
        source = t.get("source_country", "unknown")
        if source not in by_jurisdiction:
            by_jurisdiction[source] = {"total": 0, "compliant": 0, "non_compliant": 0}
        by_jurisdiction[source]["total"] += 1

        if t.get("mechanism"):
            by_jurisdiction[source]["compliant"] += 1
            compliant += 1
        else:
            by_jurisdiction[source]["non_compliant"] += 1

    return {
        "dashboard_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "total_apac_transfers": total,
        "compliant": compliant,
        "non_compliant": total - compliant,
        "compliance_rate": round(compliant / total * 100, 1) if total else 100,
        "by_source_jurisdiction": by_jurisdiction,
    }


if __name__ == "__main__":
    print("=== Japan to Singapore Transfer ===")
    result = determine_apac_mechanism(
        source_country="JP",
        destination_country="SG",
        has_contractual_safeguards=True,
        recipient_has_equivalent_measures=True,
    )
    print(json.dumps(result, indent=2))

    print("\n=== Transfer Chain Assessment ===")
    chain = [
        {"country_code": "DE", "entity": "Athena Global Logistics GmbH"},
        {"country_code": "JP", "entity": "Athena Logistics Japan KK", "has_contract": True, "equivalent_measures": True},
        {"country_code": "SG", "entity": "CloudVault Asia Pte Ltd", "has_contract": True, "cbpr_certified": True},
    ]
    chain_result = assess_transfer_chain(chain)
    print(json.dumps(chain_result, indent=2))
