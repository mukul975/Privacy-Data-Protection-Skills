#!/usr/bin/env python3
"""
Third-Country Adequacy Assessment Engine

Checks adequacy status, manages partial adequacy verification,
and monitors adequacy decision review schedules.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


ADEQUACY_DECISIONS = {
    "AD": {"country": "Andorra", "decision": "Decision 2010/625/EU", "date": "2010-10-19", "scope": "full", "review_due": "2026-12-31", "sunset": None},
    "AR": {"country": "Argentina", "decision": "Decision 2003/490/EC", "date": "2003-06-30", "scope": "full", "review_due": "2026-12-31", "sunset": None},
    "CA": {"country": "Canada", "decision": "Decision 2002/2/EC", "date": "2001-12-20", "scope": "partial", "scope_detail": "Commercial organisations subject to PIPEDA only", "review_due": "2026-12-31", "sunset": None},
    "FO": {"country": "Faroe Islands", "decision": "Decision 2010/146/EU", "date": "2010-03-05", "scope": "full", "review_due": "2026-12-31", "sunset": None},
    "GG": {"country": "Guernsey", "decision": "Decision 2003/821/EC", "date": "2003-11-21", "scope": "full", "review_due": "2026-12-31", "sunset": None},
    "IL": {"country": "Israel", "decision": "Decision 2011/61/EU", "date": "2011-01-31", "scope": "full", "review_due": "2026-12-31", "sunset": None},
    "IM": {"country": "Isle of Man", "decision": "Decision 2004/411/EC", "date": "2004-04-28", "scope": "full", "review_due": "2026-12-31", "sunset": None},
    "JP": {"country": "Japan", "decision": "Decision (EU) 2019/419", "date": "2019-01-23", "scope": "partial", "scope_detail": "Commercial sector subject to APPI with supplementary rules", "review_due": "2025-12-31", "sunset": None},
    "JE": {"country": "Jersey", "decision": "Decision 2008/393/EC", "date": "2008-05-08", "scope": "full", "review_due": "2026-12-31", "sunset": None},
    "NZ": {"country": "New Zealand", "decision": "Decision 2013/65/EU", "date": "2012-12-19", "scope": "full", "review_due": "2026-12-31", "sunset": None},
    "KR": {"country": "South Korea", "decision": "Decision (EU) 2022/254", "date": "2021-12-17", "scope": "partial", "scope_detail": "Commercial and public sector subject to PIPA; excludes intelligence agencies", "review_due": "2026-12-31", "sunset": None},
    "CH": {"country": "Switzerland", "decision": "Decision 2000/518/EC", "date": "2000-07-26", "scope": "full", "review_due": "2026-12-31", "sunset": None},
    "GB": {"country": "United Kingdom", "decision": "Decision (EU) 2021/1772", "date": "2021-06-28", "scope": "full", "review_due": "2025-06-27", "sunset": "2025-06-27"},
    "UY": {"country": "Uruguay", "decision": "Decision 2012/484/EU", "date": "2012-08-21", "scope": "full", "review_due": "2026-12-31", "sunset": None},
    "US": {"country": "United States (DPF)", "decision": "Decision (EU) 2023/1795", "date": "2023-07-10", "scope": "partial", "scope_detail": "Self-certified organisations under EU-US DPF subject to FTC/DoT jurisdiction", "review_due": "2025-10-31", "sunset": None},
}


def check_adequacy(country_code: str) -> dict:
    """Check whether a country has an EC adequacy decision."""
    decision = ADEQUACY_DECISIONS.get(country_code.upper())
    if not decision:
        return {
            "country_code": country_code.upper(),
            "has_adequacy": False,
            "recommendation": "No adequacy decision exists; use Art. 46 safeguards (SCCs/BCRs) or Art. 49 derogations",
        }

    now = datetime.utcnow()
    result = {
        "country_code": country_code.upper(),
        "country": decision["country"],
        "has_adequacy": True,
        "decision_reference": decision["decision"],
        "adoption_date": decision["date"],
        "scope": decision["scope"],
        "review_due": decision["review_due"],
    }

    if decision["scope"] == "partial":
        result["scope_detail"] = decision.get("scope_detail", "Partial scope — verify coverage")
        result["partial_adequacy_warning"] = (
            "This adequacy decision has partial scope. Verify that the specific "
            "recipient falls within the covered sector or category before relying on adequacy."
        )

    if decision.get("sunset"):
        sunset_date = datetime.strptime(decision["sunset"], "%Y-%m-%d")
        days_to_sunset = (sunset_date - now).days
        result["sunset_date"] = decision["sunset"]
        result["days_to_sunset"] = days_to_sunset
        if days_to_sunset < 0:
            result["sunset_status"] = "EXPIRED — adequacy decision no longer in force unless renewed"
        elif days_to_sunset < 90:
            result["sunset_status"] = f"IMMINENT — expires in {days_to_sunset} days; prepare backup mechanism"
        else:
            result["sunset_status"] = f"Active — {days_to_sunset} days until sunset"

    review_date = datetime.strptime(decision["review_due"], "%Y-%m-%d")
    days_to_review = (review_date - now).days
    result["days_to_review"] = days_to_review
    if days_to_review < 90:
        result["review_alert"] = f"Periodic review due in {days_to_review} days — monitor EC announcements"

    return result


def verify_partial_adequacy(
    country_code: str,
    recipient_name: str,
    recipient_sector: str,
    subject_to_law: str,
    additional_conditions_met: bool = True,
) -> dict:
    """Verify whether a specific recipient falls within partial adequacy scope."""
    decision = ADEQUACY_DECISIONS.get(country_code.upper())
    if not decision:
        return {"error": f"No adequacy decision for {country_code}"}

    if decision["scope"] != "partial":
        return {
            "country_code": country_code.upper(),
            "country": decision["country"],
            "scope": "full",
            "verification_needed": False,
            "covered": True,
            "note": "Full adequacy — no sector-specific verification needed",
        }

    scope_rules = {
        "CA": {
            "required_law": "PIPEDA",
            "alternative_laws": ["Alberta PIPA", "British Columbia PIPA", "Quebec Private Sector Act"],
            "excluded_sectors": ["public sector", "health information"],
        },
        "JP": {
            "required_law": "APPI",
            "conditions": ["PPC supplementary rules implemented"],
            "excluded_sectors": ["non-commercial"],
        },
        "US": {
            "required_law": "FTC Act Section 5",
            "alternative_laws": ["DoT jurisdiction"],
            "conditions": ["Active DPF self-certification"],
            "excluded_sectors": ["banking (OCC)", "telecommunications (FCC)", "insurance (state commissioners)"],
        },
        "KR": {
            "required_law": "PIPA",
            "excluded_sectors": ["intelligence agencies"],
        },
    }

    rules = scope_rules.get(country_code.upper(), {})
    required_law = rules.get("required_law", "")
    alternative_laws = rules.get("alternative_laws", [])
    excluded_sectors = rules.get("excluded_sectors", [])

    is_subject = subject_to_law.lower() in [required_law.lower()] + [a.lower() for a in alternative_laws]
    is_excluded = recipient_sector.lower() in [s.lower() for s in excluded_sectors]
    covered = is_subject and not is_excluded and additional_conditions_met

    return {
        "country_code": country_code.upper(),
        "country": decision["country"],
        "recipient": recipient_name,
        "recipient_sector": recipient_sector,
        "subject_to_law": subject_to_law,
        "is_within_scope": is_subject,
        "is_excluded_sector": is_excluded,
        "additional_conditions_met": additional_conditions_met,
        "covered_by_adequacy": covered,
        "recommendation": "Transfer may proceed under adequacy decision"
        if covered
        else "Recipient NOT covered by adequacy decision — establish Art. 46 safeguards",
    }


def monitor_adequacy_schedule(as_of_date: Optional[str] = None) -> dict:
    """Generate an adequacy decision monitoring report."""
    if as_of_date:
        check_date = datetime.strptime(as_of_date, "%Y-%m-%d")
    else:
        check_date = datetime.utcnow()

    expiring_soon = []
    review_due_soon = []
    stable = []

    for code, decision in ADEQUACY_DECISIONS.items():
        entry = {
            "country_code": code,
            "country": decision["country"],
            "decision": decision["decision"],
        }

        if decision.get("sunset"):
            sunset = datetime.strptime(decision["sunset"], "%Y-%m-%d")
            days = (sunset - check_date).days
            if days < 180:
                entry["sunset_date"] = decision["sunset"]
                entry["days_to_sunset"] = days
                entry["urgency"] = "critical" if days < 90 else "high"
                expiring_soon.append(entry)
                continue

        review = datetime.strptime(decision["review_due"], "%Y-%m-%d")
        days_review = (review - check_date).days
        if days_review < 180:
            entry["review_due"] = decision["review_due"]
            entry["days_to_review"] = days_review
            review_due_soon.append(entry)
        else:
            entry["status"] = "stable"
            stable.append(entry)

    return {
        "monitoring_date": check_date.strftime("%Y-%m-%d"),
        "total_adequacy_decisions": len(ADEQUACY_DECISIONS),
        "expiring_soon": expiring_soon,
        "review_due_soon": review_due_soon,
        "stable": stable,
        "action_items": _generate_monitoring_actions(expiring_soon, review_due_soon),
    }


def _generate_monitoring_actions(expiring: list, review_due: list) -> list:
    """Generate action items from monitoring results."""
    actions = []
    for e in expiring:
        actions.append(
            f"CRITICAL: {e['country']} adequacy expires {e.get('sunset_date', 'soon')} "
            f"({e.get('days_to_sunset', '?')} days). Prepare backup SCCs for all transfers."
        )
    for r in review_due:
        actions.append(
            f"MONITOR: {r['country']} adequacy review due {r['review_due']}. "
            "Monitor EC announcements for review outcome."
        )
    if not actions:
        actions.append("No immediate action items — all adequacy decisions stable.")
    return actions


if __name__ == "__main__":
    print("=== Adequacy Check — Japan ===")
    print(json.dumps(check_adequacy("JP"), indent=2))

    print("\n=== Adequacy Check — United Kingdom ===")
    print(json.dumps(check_adequacy("GB"), indent=2))

    print("\n=== Partial Adequacy Verification — Canada ===")
    verification = verify_partial_adequacy(
        country_code="CA",
        recipient_name="Northern Freight Services Inc",
        recipient_sector="commercial logistics",
        subject_to_law="PIPEDA",
    )
    print(json.dumps(verification, indent=2))

    print("\n=== Adequacy Monitoring Report ===")
    monitoring = monitor_adequacy_schedule("2025-03-14")
    print(json.dumps(monitoring, indent=2))
