"""
Employee DSAR Response Management Engine

Manages employee Data Subject Access Request processing including data source
identification, timeline tracking, redaction management, and compliance reporting.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


DATA_SOURCES = {
    "hr_system": {
        "name": "HR Information System",
        "custodian": "HR Operations",
        "data_types": "Personal details, employment history, contract, salary, benefits, absence, performance",
        "search_effort": "medium",
    },
    "email": {
        "name": "Email System",
        "custodian": "IT / Privacy Team",
        "data_types": "Emails sent, received, and about the employee",
        "search_effort": "high",
    },
    "cctv": {
        "name": "CCTV System",
        "custodian": "Facilities / Security",
        "data_types": "Video footage where employee is identifiable",
        "search_effort": "high",
    },
    "access_control": {
        "name": "Access Control System",
        "custodian": "Facilities / IT",
        "data_types": "Entry/exit logs, access attempts",
        "search_effort": "low",
    },
    "time_attendance": {
        "name": "Time and Attendance",
        "custodian": "HR Operations",
        "data_types": "Clock-in/out records, attendance patterns",
        "search_effort": "low",
    },
    "payroll": {
        "name": "Payroll System",
        "custodian": "Payroll / Finance",
        "data_types": "Salary history, tax records, pension, benefits",
        "search_effort": "low",
    },
    "performance": {
        "name": "Performance Management",
        "custodian": "HR Business Partner",
        "data_types": "Reviews, objectives, competency assessments, 360 feedback",
        "search_effort": "medium",
    },
    "lms": {
        "name": "Learning Management System",
        "custodian": "L&D / HR",
        "data_types": "Training records, certifications, mandatory training",
        "search_effort": "low",
    },
    "recruitment": {
        "name": "Recruitment System",
        "custodian": "Recruitment / HR",
        "data_types": "Application, interview notes, assessment scores",
        "search_effort": "medium",
    },
    "disciplinary": {
        "name": "Disciplinary and Grievance Files",
        "custodian": "HR Employee Relations",
        "data_types": "Investigation notes, witness statements, outcomes",
        "search_effort": "high",
    },
    "oh_records": {
        "name": "Occupational Health Records",
        "custodian": "OH Provider / HR",
        "data_types": "Fitness reports, referral correspondence",
        "search_effort": "medium",
    },
    "monitoring": {
        "name": "Monitoring Systems",
        "custodian": "IT Security",
        "data_types": "DLP alerts, web proxy logs, MDM data",
        "search_effort": "medium",
    },
    "expenses": {
        "name": "Expenses System",
        "custodian": "Finance",
        "data_types": "Expense claims, receipts, approvals",
        "search_effort": "low",
    },
    "informal_records": {
        "name": "Informal Records (Manager Notes)",
        "custodian": "Line Manager",
        "data_types": "Notes, performance observations, management discussions",
        "search_effort": "high",
    },
}

EXEMPTIONS = {
    "legal_privilege": {
        "name": "Legal Professional Privilege",
        "basis": "UK DPA 2018, Schedule 2, Part 4, Para 19",
        "description": "Communications with legal counsel for obtaining/giving legal advice or litigation",
    },
    "management_planning": {
        "name": "Management Planning",
        "basis": "UK DPA 2018, Schedule 2, Part 4, Para 24",
        "description": "Prejudice to management forecasting or planning (e.g., redundancy selection before announcement)",
    },
    "negotiations": {
        "name": "Negotiations",
        "basis": "UK DPA 2018, Schedule 2, Part 4, Para 25",
        "description": "Controller's intentions regarding negotiations with the data subject",
    },
    "ongoing_investigation": {
        "name": "Ongoing Investigation",
        "basis": "Art. 23(1)(d) GDPR — prevention/detection of offences",
        "description": "Disclosure would prejudice an ongoing disciplinary or regulatory investigation",
    },
    "third_party_rights": {
        "name": "Third-Party Rights",
        "basis": "Art. 15(4) GDPR",
        "description": "Disclosure would adversely affect the rights and freedoms of others",
    },
}


def create_dsar_record(
    employee_name: str,
    employee_id: str,
    request_date: datetime,
    request_scope: str,
    current_employee: bool = True,
) -> dict:
    """Create a new DSAR record with timeline and data source mapping."""
    reference = f"DSAR-EMP-{request_date.year}-{request_date.strftime('%m%d%H%M')}"
    deadline = request_date + timedelta(days=30)
    extended_deadline = request_date + timedelta(days=90)

    sources_to_search = list(DATA_SOURCES.keys())
    if not current_employee:
        sources_to_search = [s for s in sources_to_search if s != "monitoring"]

    high_effort_sources = [
        s for s in sources_to_search
        if DATA_SOURCES[s]["search_effort"] == "high"
    ]

    extension_likely = len(high_effort_sources) >= 2

    return {
        "reference": reference,
        "employee_name": employee_name,
        "employee_id": employee_id,
        "request_date": request_date.isoformat(),
        "request_scope": request_scope,
        "current_employee": current_employee,
        "status": "received",
        "deadline": deadline.strftime("%Y-%m-%d"),
        "extended_deadline": extended_deadline.strftime("%Y-%m-%d") if extension_likely else None,
        "extension_likely": extension_likely,
        "extension_reason": (
            f"Complex request involving {len(high_effort_sources)} high-effort data sources: "
            f"{', '.join(DATA_SOURCES[s]['name'] for s in high_effort_sources)}"
            if extension_likely
            else None
        ),
        "data_sources": [
            {
                "source": DATA_SOURCES[s]["name"],
                "custodian": DATA_SOURCES[s]["custodian"],
                "data_types": DATA_SOURCES[s]["data_types"],
                "search_effort": DATA_SOURCES[s]["search_effort"],
                "status": "pending",
            }
            for s in sources_to_search
        ],
        "redaction_required": True,
        "privilege_review_required": True,
        "timeline": {
            "day_1": "Receipt, identity verification, acknowledgment",
            "days_2_5": "Scoping, custodian notification, collection instructions",
            "days_5_20": "Data collection from all sources",
            "days_15_25": "Review, redaction, privilege assessment",
            "days_25_30": "Quality check, covering letter, secure dispatch",
        },
    }


def assess_exemptions(
    has_legal_proceedings: bool = False,
    has_ongoing_investigation: bool = False,
    has_settlement_negotiations: bool = False,
    has_management_planning: bool = False,
) -> list[dict]:
    """Assess which exemptions may apply to the DSAR."""
    applicable = []

    if has_legal_proceedings:
        applicable.append({
            **EXEMPTIONS["legal_privilege"],
            "applies": True,
            "action": "Route potentially privileged documents to legal counsel for review. Maintain privilege log.",
        })

    if has_ongoing_investigation:
        applicable.append({
            **EXEMPTIONS["ongoing_investigation"],
            "applies": True,
            "action": "May temporarily withhold investigation materials. Must disclose once investigation concludes.",
        })

    if has_settlement_negotiations:
        applicable.append({
            **EXEMPTIONS["negotiations"],
            "applies": True,
            "action": "May withhold employer's settlement strategy and internal negotiation positions.",
        })

    if has_management_planning:
        applicable.append({
            **EXEMPTIONS["management_planning"],
            "applies": True,
            "action": "May temporarily withhold planning documents. Narrow and temporary exemption only.",
        })

    # Third-party rights always applies
    applicable.append({
        **EXEMPTIONS["third_party_rights"],
        "applies": True,
        "action": "Redact third-party personal data unless reasonable to disclose.",
    })

    return applicable


def main():
    """Example: Atlas Manufacturing Group employee DSAR."""
    print("=== Employee DSAR Processing ===")
    print("Organisation: Atlas Manufacturing Group\n")

    dsar = create_dsar_record(
        employee_name="James Harrison",
        employee_id="ATL-2019-0847",
        request_date=datetime(2026, 3, 10),
        request_scope="All personal data held about me",
        current_employee=True,
    )

    print(f"Reference: {dsar['reference']}")
    print(f"Deadline: {dsar['deadline']}")
    print(f"Extension Likely: {dsar['extension_likely']}")
    if dsar['extension_likely']:
        print(f"Extension Reason: {dsar['extension_reason']}")
        print(f"Extended Deadline: {dsar['extended_deadline']}")

    print(f"\nData Sources to Search: {len(dsar['data_sources'])}")
    for src in dsar["data_sources"]:
        print(f"  [{src['search_effort'].upper()}] {src['source']} — Custodian: {src['custodian']}")

    # Assess exemptions (employee on PIP with solicitor involved)
    exemptions = assess_exemptions(
        has_legal_proceedings=True,
        has_ongoing_investigation=False,
        has_settlement_negotiations=True,
    )

    print(f"\nApplicable Exemptions: {len(exemptions)}")
    for ex in exemptions:
        print(f"  - {ex['name']}: {ex['action']}")

    print("\n" + json.dumps(dsar, indent=2, default=str))


if __name__ == "__main__":
    main()
