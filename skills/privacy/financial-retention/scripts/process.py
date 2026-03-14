"""
Financial Records Retention Process
Maps financial data categories to statutory retention periods across jurisdictions.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


# Financial retention requirements by category
FINANCIAL_CATEGORIES = {
    "FIN-001": {
        "name": "General Ledger",
        "records": "Journal entries, trial balances, chart of accounts",
        "uk_period_years": 6, "uk_source": "Companies Act 2006 s.388",
        "eu_period_years": 10, "eu_source": "EU Accounting Directive 2013/34/EU (varies by MS)",
        "us_period_years": 7, "us_source": "SOX Section 802",
        "trigger": "Financial year end",
    },
    "FIN-002": {
        "name": "Accounts Payable",
        "records": "Purchase invoices, supplier statements, payment records",
        "uk_period_years": 6, "uk_source": "Companies Act 2006; HMRC VAT",
        "eu_period_years": 10, "eu_source": "EU Accounting Directive",
        "us_period_years": 7, "us_source": "IRS requirements",
        "trigger": "Financial year end",
    },
    "FIN-003": {
        "name": "Accounts Receivable",
        "records": "Sales invoices, credit notes, debit notes",
        "uk_period_years": 6, "uk_source": "Companies Act 2006; HMRC VAT",
        "eu_period_years": 10, "eu_source": "EU Accounting Directive",
        "us_period_years": 7, "us_source": "IRS requirements",
        "trigger": "Financial year end",
    },
    "FIN-005": {
        "name": "Payroll",
        "records": "Pay slips, P45s, P60s, P11Ds, NI records",
        "uk_period_years": 6, "uk_source": "Income Tax (PAYE) Regulations 2003",
        "eu_period_years": 6, "eu_source": "Varies by member state",
        "us_period_years": 4, "us_source": "IRS employment tax records",
        "trigger": "Tax year end (5 April)",
    },
    "FIN-009": {
        "name": "AML Records",
        "records": "CDD documentation, EDD records, risk assessments, SARs",
        "uk_period_years": 5, "uk_source": "MLR 2017 reg.40",
        "eu_period_years": 5, "eu_source": "AMLD5 Art. 40",
        "us_period_years": 5, "us_source": "Bank Secrecy Act / 31 CFR §1010.430",
        "trigger": "End of business relationship or transaction",
    },
    "FIN-010": {
        "name": "Audit Files",
        "records": "External audit workpapers, internal audit reports",
        "uk_period_years": 6, "uk_source": "Companies Act 2006",
        "eu_period_years": 6, "eu_source": "EU Audit Directive",
        "us_period_years": 7, "us_source": "SOX Section 802 (18 U.S.C. §1520)",
        "trigger": "Audit completion date",
    },
    "FIN-011": {
        "name": "Investment Records",
        "records": "Client orders, execution reports, suitability assessments",
        "uk_period_years": 5, "uk_source": "MiFID II Art. 16(6); FCA COBS",
        "eu_period_years": 5, "eu_source": "MiFID II Art. 16(6)",
        "us_period_years": 6, "us_source": "SEC Rule 17a-4",
        "trigger": "Record creation date",
    },
    "FIN-012": {
        "name": "Communications (Investment)",
        "records": "Recorded telephone conversations, electronic communications",
        "uk_period_years": 5, "uk_source": "MiFID II Art. 16(7)",
        "eu_period_years": 5, "eu_source": "MiFID II Art. 16(7)",
        "us_period_years": 6, "us_source": "SEC Rule 17a-4",
        "trigger": "Recording date",
    },
    "FIN-013": {
        "name": "Payment Records",
        "records": "Card transactions, direct debits, BACS/CHAPS records",
        "uk_period_years": 6, "uk_source": "Limitation Act 1980 s.5; PSD2",
        "eu_period_years": 5, "eu_source": "PSD2",
        "us_period_years": 7, "us_source": "IRS; state tax requirements",
        "trigger": "Transaction date",
    },
    "FIN-015": {
        "name": "Contracts (Financial)",
        "records": "Loan agreements, facility letters, guarantees",
        "uk_period_years": 12, "uk_source": "Limitation Act 1980 s.8 (deeds: 12 years)",
        "eu_period_years": 10, "eu_source": "Varies by member state",
        "us_period_years": 7, "us_source": "SOX; state UCC requirements",
        "trigger": "Contract termination",
    },
}


def get_governing_period(
    category_id: str,
    jurisdictions: list[str],
) -> dict:
    """
    Determine the governing retention period for a financial data category
    across the specified jurisdictions. The longest period governs.
    """
    if category_id not in FINANCIAL_CATEGORIES:
        raise ValueError(f"Unknown financial category: {category_id}")

    cat = FINANCIAL_CATEGORIES[category_id]
    periods = {}

    if "uk" in jurisdictions:
        periods["uk"] = {"years": cat["uk_period_years"], "source": cat["uk_source"]}
    if "eu" in jurisdictions:
        periods["eu"] = {"years": cat["eu_period_years"], "source": cat["eu_source"]}
    if "us" in jurisdictions:
        periods["us"] = {"years": cat["us_period_years"], "source": cat["us_source"]}

    if not periods:
        return {"error": "No valid jurisdictions specified"}

    max_jurisdiction = max(periods, key=lambda j: periods[j]["years"])
    governing = periods[max_jurisdiction]

    return {
        "category_id": category_id,
        "category_name": cat["name"],
        "jurisdictions_assessed": jurisdictions,
        "jurisdiction_periods": periods,
        "governing_jurisdiction": max_jurisdiction,
        "governing_period_years": governing["years"],
        "governing_source": governing["source"],
        "trigger_event": cat["trigger"],
    }


def calculate_financial_deletion_date(
    category_id: str,
    trigger_date: str,
    jurisdictions: list[str],
) -> dict:
    """Calculate the deletion date for a financial record."""
    governing = get_governing_period(category_id, jurisdictions)
    if "error" in governing:
        return governing

    trigger = datetime.strptime(trigger_date, "%Y-%m-%d")
    deletion_date = trigger + timedelta(days=governing["governing_period_years"] * 365)

    return {
        "category_id": category_id,
        "category_name": governing["category_name"],
        "trigger_date": trigger_date,
        "trigger_event": governing["trigger_event"],
        "governing_period_years": governing["governing_period_years"],
        "governing_source": governing["governing_source"],
        "calculated_deletion_date": deletion_date.strftime("%Y-%m-%d"),
    }


def assess_art17_financial_exception(
    category_id: str,
    trigger_date: str,
    jurisdictions: list[str],
    request_date: Optional[str] = None,
) -> dict:
    """
    Assess whether a financial record is subject to Art. 17(3)(b) exception
    (legal obligation to retain) when an erasure request is received.
    """
    if request_date is None:
        request_date = datetime.utcnow().strftime("%Y-%m-%d")

    deletion_info = calculate_financial_deletion_date(category_id, trigger_date, jurisdictions)
    if "error" in deletion_info:
        return deletion_info

    deletion_date = datetime.strptime(deletion_info["calculated_deletion_date"], "%Y-%m-%d")
    req_date = datetime.strptime(request_date, "%Y-%m-%d")

    exception_applies = req_date < deletion_date

    return {
        "category_id": category_id,
        "category_name": deletion_info["category_name"],
        "erasure_request_date": request_date,
        "statutory_retention_expires": deletion_info["calculated_deletion_date"],
        "exception_applies": exception_applies,
        "exception_basis": "Art. 17(3)(b) — legal obligation" if exception_applies else "No exception — statutory period expired",
        "governing_statute": deletion_info["governing_source"],
        "action": (
            f"Retain under statutory obligation until {deletion_info['calculated_deletion_date']}. "
            f"Apply data minimization. Restrict access to compliance team."
        ) if exception_applies else "Delete per normal erasure workflow",
    }


def generate_retention_calendar() -> list[dict]:
    """Generate the annual retention calendar for financial records."""
    return [
        {"month": "April", "activity": "Tax year end — trigger payroll records retention countdown (FIN-005)"},
        {"month": "May", "activity": "Annual financial statement preparation — trigger prior year ledger retention (FIN-001)"},
        {"month": "June", "activity": "Annual external audit completion — trigger audit files retention (FIN-010)"},
        {"month": "September", "activity": "Companies House filing deadline — archive annual accounts"},
        {"month": "October", "activity": "Annual retention review — review all financial categories against current statutes"},
        {"month": "December/January", "activity": "Financial year end — trigger accounting records retention countdown"},
        {"month": "Quarterly", "activity": "VAT return filing — archive returns and supporting records"},
        {"month": "Monthly", "activity": "AML transaction monitoring — archive alerts and dispositions (FIN-009)"},
    ]


if __name__ == "__main__":
    result = get_governing_period("FIN-010", ["uk", "eu", "us"])
    print("Governing period:", json.dumps(result, indent=2))

    deletion = calculate_financial_deletion_date("FIN-010", "2025-06-30", ["uk", "us"])
    print("Deletion date:", json.dumps(deletion, indent=2))

    exception = assess_art17_financial_exception("FIN-009", "2024-01-15", ["uk", "eu"], "2026-03-14")
    print("Art. 17 assessment:", json.dumps(exception, indent=2))
