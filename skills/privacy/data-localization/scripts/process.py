#!/usr/bin/env python3
"""
Data Localization Compliance Engine

Assesses data localization requirements by jurisdiction,
tracks compliance status, and generates architecture recommendations.
"""

import json
from datetime import datetime
from typing import Optional


LOCALIZATION_REQUIREMENTS = {
    "RU": {
        "country": "Russia",
        "law": "Federal Law 152-FZ (amended by 242-FZ)",
        "requirement": "storage",
        "scope": "All personal data of Russian citizens collected via any means",
        "effective": "2015-09-01",
        "transfer_permitted": True,
        "transfer_conditions": "After localization; subject to 152-FZ cross-border rules (adequate country or consent)",
        "filing_required": "Roskomnadzor notification of data processing",
        "penalties": "Website blocking; fines up to RUB 18M for repeated violations",
        "enforcer": "Roskomnadzor",
    },
    "CN": {
        "country": "China",
        "law": "PIPL Art. 40; CSL Art. 37; DSL Art. 31",
        "requirement": "storage_and_assessment",
        "scope": "CIIOs and processors meeting CAC volume thresholds (1M individuals or cumulative 100K/10K sensitive)",
        "effective": "2021-11-01",
        "transfer_permitted": True,
        "transfer_conditions": "CAC security assessment (CIIOs/threshold) or Standard Contract (below threshold); PIIA required",
        "filing_required": "CAC security assessment or Standard Contract filing with provincial CAC",
        "penalties": "Fines up to RMB 50M or 5% of annual revenue; suspension of business",
        "enforcer": "Cyberspace Administration of China (CAC)",
    },
    "IN": {
        "country": "India",
        "law": "DPDP Act 2023 Section 16",
        "requirement": "conditional",
        "scope": "Blacklist model — no current restrictions; future notifications may restrict transfers to specific countries",
        "effective": "2024-01-01",
        "transfer_permitted": True,
        "transfer_conditions": "Permitted unless blacklisted; RBI payment data must remain in India",
        "filing_required": "None currently; monitor for future requirements",
        "penalties": "Up to INR 250 crore (approx. EUR 28M) under DPDP Act",
        "enforcer": "Data Protection Board of India",
    },
    "IN_RBI": {
        "country": "India (Payment Data)",
        "law": "RBI Circular DPSS.CO.OD.No.2785 (April 2018)",
        "requirement": "storage_strict",
        "scope": "All payment system data processed by payment system operators in India",
        "effective": "2018-10-15",
        "transfer_permitted": False,
        "transfer_conditions": "Payment data must be stored exclusively in India; foreign processing not permitted",
        "filing_required": "RBI compliance audit",
        "penalties": "Regulatory action by RBI including licence revocation",
        "enforcer": "Reserve Bank of India",
    },
    "TR": {
        "country": "Turkey",
        "law": "KVKK Law No. 6698 Art. 9",
        "requirement": "approval_based",
        "scope": "All personal data transfers abroad require adequate country status or Board approval",
        "effective": "2016-04-07",
        "transfer_permitted": True,
        "transfer_conditions": "Adequate country (KVKK Board list) or Board approval with written undertaking",
        "filing_required": "Board application for transfers to non-adequate countries",
        "penalties": "Fines up to TRY 9.8M (2024); data processing restrictions",
        "enforcer": "KVKK Board",
    },
    "VN": {
        "country": "Vietnam",
        "law": "Decree 13/2023/ND-CP; Cybersecurity Law 2018 Art. 26(3)",
        "requirement": "assessment_based",
        "scope": "All cross-border transfers require impact assessment; certain data must be stored in Vietnam per Cybersecurity Law",
        "effective": "2023-07-01",
        "transfer_permitted": True,
        "transfer_conditions": "Transfer impact assessment dossier filed with Ministry of Public Security within 60 days",
        "filing_required": "Impact assessment dossier to Ministry of Public Security",
        "penalties": "Administrative fines; business suspension",
        "enforcer": "Ministry of Public Security",
    },
    "ID": {
        "country": "Indonesia",
        "law": "GR 71/2019 Art. 20-21; UU PDP 2024",
        "requirement": "sector_based",
        "scope": "Public electronic system operators: data must be in Indonesia; Private operators: may be abroad with access provisions",
        "effective": "2019-10-10",
        "transfer_permitted": True,
        "transfer_conditions": "Private sector: allowed with supervisory access; Public sector: localization mandatory",
        "filing_required": "None specific",
        "penalties": "Administrative sanctions under UU PDP",
        "enforcer": "Ministry of Communication and Digital",
    },
}


def assess_localization_requirement(
    country_code: str,
    is_ciio: bool = False,
    data_subject_count: int = 0,
    is_payment_data: bool = False,
    is_public_sector: bool = False,
) -> dict:
    """Assess data localization requirements for a specific jurisdiction."""
    if country_code == "IN" and is_payment_data:
        country_code = "IN_RBI"

    req = LOCALIZATION_REQUIREMENTS.get(country_code.upper())
    if not req:
        return {
            "country_code": country_code,
            "localization_required": False,
            "note": "No known data localization requirement for this jurisdiction",
        }

    result = {
        "country_code": country_code.upper(),
        "country": req["country"],
        "law": req["law"],
        "requirement_type": req["requirement"],
        "scope": req["scope"],
        "cross_border_transfer_permitted": req["transfer_permitted"],
        "transfer_conditions": req["transfer_conditions"],
        "filing_required": req["filing_required"],
        "penalties": req["penalties"],
        "enforcer": req["enforcer"],
    }

    if country_code.upper() == "CN":
        if is_ciio or data_subject_count >= 1_000_000:
            result["cac_security_assessment_required"] = True
            result["mechanism"] = "CAC security assessment (mandatory)"
        elif data_subject_count >= 100_000:
            result["cac_security_assessment_required"] = True
            result["mechanism"] = "CAC security assessment (cumulative threshold)"
        else:
            result["cac_security_assessment_required"] = False
            result["mechanism"] = "CAC Standard Contract (below threshold)"

    if country_code.upper() == "ID":
        result["localization_mandatory"] = is_public_sector
        result["note"] = (
            "Localization mandatory for public sector operators"
            if is_public_sector
            else "Private sector may store abroad with supervisory access"
        )

    return result


def generate_localization_compliance_report(operations: list) -> dict:
    """Generate a compliance report across all jurisdictions where the organisation operates."""
    report = {
        "report_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "total_jurisdictions": len(operations),
        "compliant": 0,
        "non_compliant": 0,
        "partial": 0,
        "jurisdictions": [],
    }

    for op in operations:
        status = op.get("compliance_status", "unknown")
        if status == "compliant":
            report["compliant"] += 1
        elif status == "non_compliant":
            report["non_compliant"] += 1
        else:
            report["partial"] += 1

        report["jurisdictions"].append({
            "country": op["country"],
            "requirement": op.get("requirement_type", "unknown"),
            "local_storage_in_place": op.get("local_storage", False),
            "transfer_mechanism_in_place": op.get("transfer_mechanism", False),
            "filing_completed": op.get("filing_completed", False),
            "compliance_status": status,
            "gaps": op.get("gaps", []),
        })

    report["compliance_rate"] = round(
        report["compliant"] / report["total_jurisdictions"] * 100, 1
    ) if report["total_jurisdictions"] else 0

    return report


if __name__ == "__main__":
    print("=== Russia Localization Assessment ===")
    ru = assess_localization_requirement("RU")
    print(json.dumps(ru, indent=2))

    print("\n=== China Assessment (below threshold) ===")
    cn = assess_localization_requirement("CN", is_ciio=False, data_subject_count=15000)
    print(json.dumps(cn, indent=2))

    print("\n=== India Payment Data ===")
    in_pay = assess_localization_requirement("IN", is_payment_data=True)
    print(json.dumps(in_pay, indent=2))

    print("\n=== Compliance Report ===")
    ops = [
        {"country": "Russia", "requirement_type": "storage", "local_storage": True,
         "transfer_mechanism": True, "filing_completed": True, "compliance_status": "compliant"},
        {"country": "China", "requirement_type": "storage_and_assessment", "local_storage": True,
         "transfer_mechanism": True, "filing_completed": True, "compliance_status": "compliant"},
        {"country": "India", "requirement_type": "conditional", "local_storage": True,
         "transfer_mechanism": True, "filing_completed": True, "compliance_status": "compliant"},
        {"country": "Turkey", "requirement_type": "approval_based", "local_storage": False,
         "transfer_mechanism": False, "filing_completed": False, "compliance_status": "non_compliant",
         "gaps": ["KVKK Board application not filed", "No adequate country status"]},
    ]
    report = generate_localization_compliance_report(ops)
    print(json.dumps(report, indent=2))
