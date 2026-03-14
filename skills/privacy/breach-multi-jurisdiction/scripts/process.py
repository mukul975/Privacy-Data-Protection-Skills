#!/usr/bin/env python3
"""
Multi-Jurisdiction Breach Notification Coordinator

Maps breach impact to applicable notification laws, calculates jurisdiction-specific
deadlines, and generates a coordinated notification plan.
"""

import json
from datetime import datetime, timezone, timedelta
from typing import Optional


JURISDICTION_RULES = {
    "EU_GDPR": {
        "name": "EU General Data Protection Regulation",
        "authority": "Lead Supervisory Authority (Art. 56)",
        "sa_timeline_hours": 72,
        "sa_timeline_description": "72 hours from awareness",
        "ds_timeline": "Without undue delay when high risk",
        "threshold": "Unless unlikely to result in risk",
        "ag_threshold_count": None,
        "content_requirements": ["nature", "dpo_contact", "consequences", "measures"],
    },
    "UK_GDPR": {
        "name": "UK GDPR + DPA 2018",
        "authority": "ICO",
        "sa_timeline_hours": 72,
        "sa_timeline_description": "72 hours from awareness",
        "ds_timeline": "Without undue delay when high risk",
        "threshold": "Unless unlikely to result in risk",
        "ag_threshold_count": None,
        "content_requirements": ["nature", "dpo_contact", "consequences", "measures"],
    },
    "US_CA": {
        "name": "California — Cal. Civ. Code §1798.82",
        "authority": "California Attorney General",
        "sa_timeline_hours": None,
        "sa_timeline_description": "Most expedient time possible",
        "ds_timeline": "Most expedient time possible, no unreasonable delay",
        "threshold": "Name + specified data element",
        "ag_threshold_count": 500,
        "content_requirements": ["nature", "contact", "remedial_actions"],
    },
    "US_NY": {
        "name": "New York — GBL §899-aa + SHIELD Act",
        "authority": "NY AG + DFS + DOS",
        "sa_timeline_hours": None,
        "sa_timeline_description": "Most expedient time possible",
        "ds_timeline": "Most expedient time possible, no unreasonable delay",
        "threshold": "Private information (name + data element)",
        "ag_threshold_count": None,
        "content_requirements": ["nature", "contact", "remedial_actions", "toll_free_number"],
    },
    "US_TX": {
        "name": "Texas — Bus. & Com. Code §521.053",
        "authority": "Texas Attorney General",
        "sa_timeline_hours": 1440,
        "sa_timeline_description": "60 days from determination",
        "ds_timeline": "60 days from determination",
        "threshold": "Name + sensitive personal information",
        "ag_threshold_count": 250,
        "content_requirements": ["nature", "contact", "remedial_actions"],
    },
    "US_FL": {
        "name": "Florida — Fla. Stat. §501.171",
        "authority": "FDLE",
        "sa_timeline_hours": 720,
        "sa_timeline_description": "30 days from determination",
        "ds_timeline": "30 days from determination",
        "threshold": "Name + specified data element",
        "ag_threshold_count": 500,
        "content_requirements": ["nature", "contact", "remedial_actions"],
    },
    "US_CO": {
        "name": "Colorado — Rev. Stat. §6-1-716",
        "authority": "Colorado Attorney General",
        "sa_timeline_hours": 720,
        "sa_timeline_description": "30 days from determination",
        "ds_timeline": "30 days from determination",
        "threshold": "Name + specified data element",
        "ag_threshold_count": 500,
        "content_requirements": ["nature", "contact", "remedial_actions"],
    },
    "US_MA": {
        "name": "Massachusetts — G.L. c. 93H §3",
        "authority": "MA AG + OCABR",
        "sa_timeline_hours": None,
        "sa_timeline_description": "As soon as practicable",
        "ds_timeline": "As soon as practicable",
        "threshold": "Name + specified data element",
        "ag_threshold_count": None,
        "content_requirements": ["nature", "contact", "remedial_services"],
    },
    "CA_PIPEDA": {
        "name": "Canada — PIPEDA",
        "authority": "OPC (Office of the Privacy Commissioner)",
        "sa_timeline_hours": None,
        "sa_timeline_description": "As soon as feasible",
        "ds_timeline": "As soon as feasible",
        "threshold": "Real risk of significant harm (RROSH)",
        "ag_threshold_count": None,
        "content_requirements": ["nature", "contact", "consequences", "measures", "complaint_process"],
    },
    "AU_NDB": {
        "name": "Australia — Privacy Act NDB Scheme",
        "authority": "OAIC",
        "sa_timeline_hours": 720,
        "sa_timeline_description": "30 days from determination",
        "ds_timeline": "As soon as practicable",
        "threshold": "Eligible data breach (serious harm likely)",
        "ag_threshold_count": None,
        "content_requirements": ["nature", "contact", "steps_to_take"],
    },
    "BR_LGPD": {
        "name": "Brazil — LGPD Art. 48",
        "authority": "ANPD",
        "sa_timeline_hours": 72,
        "sa_timeline_description": "3 business days per ANPD Resolution",
        "ds_timeline": "Reasonable time",
        "threshold": "Risk or relevant damage to data subjects",
        "ag_threshold_count": None,
        "content_requirements": ["nature", "contact", "consequences", "measures"],
    },
    "KR_PIPA": {
        "name": "South Korea — PIPA Art. 34",
        "authority": "PIPC",
        "sa_timeline_hours": 72,
        "sa_timeline_description": "72 hours",
        "ds_timeline": "Without delay",
        "threshold": "1,000+ subjects or sensitive data",
        "ag_threshold_count": 1000,
        "content_requirements": ["nature", "contact", "measures"],
    },
}


def map_affected_jurisdictions(
    data_subject_distribution: dict,
    breach_awareness_timestamp: str,
    includes_financial_data: bool = False,
    includes_health_data: bool = False,
    includes_ssn: bool = False,
) -> dict:
    """
    Map affected jurisdictions and calculate notification deadlines.

    Args:
        data_subject_distribution: Dict mapping jurisdiction codes to affected counts.
        breach_awareness_timestamp: ISO 8601 UTC timestamp of awareness.
        includes_financial_data: Whether financial data is involved.
        includes_health_data: Whether health data is involved.
        includes_ssn: Whether SSN/government IDs are involved.

    Returns:
        Comprehensive notification plan with deadlines per jurisdiction.
    """
    awareness_dt = datetime.fromisoformat(breach_awareness_timestamp)
    if awareness_dt.tzinfo is None:
        awareness_dt = awareness_dt.replace(tzinfo=timezone.utc)

    notification_plan = {
        "breach_awareness": awareness_dt.isoformat(),
        "total_jurisdictions_affected": len(data_subject_distribution),
        "total_data_subjects": sum(data_subject_distribution.values()),
        "jurisdictions": [],
    }

    deadlines = []

    for jurisdiction_code, affected_count in data_subject_distribution.items():
        rule = JURISDICTION_RULES.get(jurisdiction_code)
        if not rule:
            notification_plan["jurisdictions"].append({
                "code": jurisdiction_code,
                "affected_count": affected_count,
                "status": "UNKNOWN_JURISDICTION — manual review required",
            })
            continue

        if rule["sa_timeline_hours"]:
            deadline_dt = awareness_dt + timedelta(hours=rule["sa_timeline_hours"])
        else:
            deadline_dt = awareness_dt + timedelta(days=45)

        ag_required = False
        if rule["ag_threshold_count"] and affected_count >= rule["ag_threshold_count"]:
            ag_required = True

        jurisdiction_entry = {
            "code": jurisdiction_code,
            "law": rule["name"],
            "authority": rule["authority"],
            "affected_count": affected_count,
            "sa_notification_deadline": deadline_dt.isoformat(),
            "sa_timeline_description": rule["sa_timeline_description"],
            "ds_notification_timeline": rule["ds_timeline"],
            "ag_notification_required": ag_required,
            "content_requirements": rule["content_requirements"],
            "special_considerations": [],
        }

        if includes_financial_data and jurisdiction_code.startswith("US_"):
            jurisdiction_entry["special_considerations"].append(
                "Financial data involved — credit monitoring offer required in most US states"
            )
        if includes_health_data and jurisdiction_code.startswith("US_"):
            jurisdiction_entry["special_considerations"].append(
                "Health data involved — check state-specific health data breach requirements"
            )
        if includes_ssn and jurisdiction_code.startswith("US_"):
            jurisdiction_entry["special_considerations"].append(
                "SSN involved — triggers notification in all US states; credit monitoring required"
            )

        notification_plan["jurisdictions"].append(jurisdiction_entry)
        deadlines.append((jurisdiction_code, deadline_dt))

    deadlines.sort(key=lambda x: x[1])
    notification_plan["deadline_priority_order"] = [
        {"jurisdiction": code, "deadline": dt.isoformat()}
        for code, dt in deadlines
    ]

    if deadlines:
        notification_plan["next_deadline"] = {
            "jurisdiction": deadlines[0][0],
            "deadline": deadlines[0][1].isoformat(),
            "remaining_hours": max(0, (deadlines[0][1] - datetime.now(timezone.utc)).total_seconds() / 3600),
        }

    return notification_plan


def main():
    print("=" * 70)
    print("MULTI-JURISDICTION NOTIFICATION PLAN")
    print("=" * 70)

    plan = map_affected_jurisdictions(
        data_subject_distribution={
            "EU_GDPR": 12450,
            "UK_GDPR": 1830,
            "US_CA": 2340,
            "US_NY": 1870,
            "US_TX": 980,
            "US_FL": 620,
            "US_CO": 340,
            "CA_PIPEDA": 890,
            "AU_NDB": 210,
            "BR_LGPD": 150,
            "KR_PIPA": 45,
        },
        breach_awareness_timestamp="2026-03-13T14:30:00+00:00",
        includes_financial_data=True,
        includes_health_data=False,
        includes_ssn=False,
    )

    print(json.dumps(plan, indent=2, default=str))

    print("\n" + "=" * 70)
    print("NOTIFICATION DEADLINE SUMMARY")
    print("=" * 70)

    for deadline in plan["deadline_priority_order"]:
        rule = JURISDICTION_RULES.get(deadline["jurisdiction"], {})
        dt = datetime.fromisoformat(deadline["deadline"])
        print(f"  {deadline['jurisdiction']:12s} | {dt.strftime('%d %b %Y %H:%M UTC')} | {rule.get('sa_timeline_description', 'N/A')}")


if __name__ == "__main__":
    main()
