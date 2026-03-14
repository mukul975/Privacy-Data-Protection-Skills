"""
Data Retention Schedule Management Process
Automates retention schedule creation, review, and enforcement for Orion Data Vault Corp.
"""

import json
from datetime import datetime, timedelta
from typing import Optional


# Statutory retention periods by regulatory source
STATUTORY_PERIODS = {
    "hmrc_tax": {"years": 6, "source": "HMRC; TMA 1970 s.34"},
    "companies_act": {"years": 6, "source": "Companies Act 2006 s.388"},
    "paye_regulations": {"years": 6, "source": "Income Tax (PAYE) Regulations 2003"},
    "vat_regulations": {"years": 6, "source": "VAT Regulations 1995 reg.31"},
    "limitation_contract": {"years": 6, "source": "Limitation Act 1980 s.5"},
    "limitation_tort": {"years": 3, "source": "Limitation Act 1980 s.11"},
    "limitation_deed": {"years": 12, "source": "Limitation Act 1980 s.8"},
    "aml_mlr": {"years": 5, "source": "Money Laundering Regulations 2017 reg.40"},
    "mifid_ii_base": {"years": 5, "source": "MiFID II Art. 16(6)"},
    "mifid_ii_extended": {"years": 7, "source": "MiFID II Art. 16(7) — competent authority extension"},
    "coshh": {"years": 40, "source": "COSHH Regulations 2002"},
    "ionising_radiation": {"years": 50, "source": "Ionising Radiations Regulations 2017"},
    "equality_act": {"months": 6, "source": "Equality Act 2010 s.123"},
    "working_time": {"years": 2, "source": "Working Time Regulations 1998 reg.9"},
    "sox_audit": {"years": 7, "source": "SOX Section 802 (18 U.S.C. §1520)"},
    "sec_17a4": {"years": 6, "source": "SEC Rule 17a-4 (17 CFR §240.17a-4)"},
    "ico_cctv": {"days": 30, "source": "ICO CCTV Code of Practice"},
    "ico_analytics": {"months": 26, "source": "ICO/CNIL recommendation"},
}


class DataCategory:
    """Represents a data category in the retention schedule."""

    def __init__(
        self,
        category_id: str,
        name: str,
        data_elements: list[str],
        processing_purpose: str,
        legal_basis: str,
        retention_period_days: int,
        retention_source: str,
        trigger_event: str,
        review_frequency: str = "Annual",
    ):
        self.category_id = category_id
        self.name = name
        self.data_elements = data_elements
        self.processing_purpose = processing_purpose
        self.legal_basis = legal_basis
        self.retention_period_days = retention_period_days
        self.retention_source = retention_source
        self.trigger_event = trigger_event
        self.review_frequency = review_frequency

    def calculate_deletion_date(self, trigger_date: datetime) -> datetime:
        """Calculate the deletion date based on trigger event and retention period."""
        return trigger_date + timedelta(days=self.retention_period_days)

    def is_expired(self, trigger_date: datetime, reference_date: Optional[datetime] = None) -> bool:
        """Check if the retention period has expired."""
        if reference_date is None:
            reference_date = datetime.utcnow()
        deletion_date = self.calculate_deletion_date(trigger_date)
        return reference_date >= deletion_date

    def days_until_expiry(self, trigger_date: datetime, reference_date: Optional[datetime] = None) -> int:
        """Calculate days remaining until retention period expires."""
        if reference_date is None:
            reference_date = datetime.utcnow()
        deletion_date = self.calculate_deletion_date(trigger_date)
        delta = deletion_date - reference_date
        return max(0, delta.days)

    def to_dict(self) -> dict:
        return {
            "category_id": self.category_id,
            "name": self.name,
            "data_elements": self.data_elements,
            "processing_purpose": self.processing_purpose,
            "legal_basis": self.legal_basis,
            "retention_period_days": self.retention_period_days,
            "retention_source": self.retention_source,
            "trigger_event": self.trigger_event,
            "review_frequency": self.review_frequency,
        }


def build_default_schedule() -> list[DataCategory]:
    """Build the default retention schedule for Orion Data Vault Corp."""
    return [
        DataCategory(
            category_id="CAT-001",
            name="Employee HR Records",
            data_elements=["name", "address", "NI number", "salary", "performance reviews"],
            processing_purpose="Employment administration",
            legal_basis="Art. 6(1)(b) Contract + Art. 6(1)(c) Legal obligation",
            retention_period_days=6 * 365,  # employment + 6 years (trigger = termination)
            retention_source="Limitation Act 1980 s.5; Employment Rights Act 1996",
            trigger_event="Employment termination date",
        ),
        DataCategory(
            category_id="CAT-002",
            name="Customer Account Data",
            data_elements=["name", "email", "phone", "address", "account preferences"],
            processing_purpose="Service delivery",
            legal_basis="Art. 6(1)(b) Contract",
            retention_period_days=2 * 365,  # account closure + 2 years
            retention_source="Contractual necessity; limitation period buffer",
            trigger_event="Account closure date",
        ),
        DataCategory(
            category_id="CAT-003",
            name="Customer Transaction Records",
            data_elements=["purchase history", "payment details", "invoices"],
            processing_purpose="Contract performance and legal obligation",
            legal_basis="Art. 6(1)(b) Contract + Art. 6(1)(c) Legal obligation",
            retention_period_days=6 * 365,
            retention_source="HMRC record-keeping; Companies Act 2006 s.386; Limitation Act 1980",
            trigger_event="Transaction completion date",
        ),
        DataCategory(
            category_id="CAT-004",
            name="Marketing Contact Data",
            data_elements=["name", "email", "consent records", "campaign interactions"],
            processing_purpose="Direct marketing",
            legal_basis="Art. 6(1)(a) Consent",
            retention_period_days=30,  # consent withdrawal + 30 days processing
            retention_source="Consent-based; deletion upon withdrawal",
            trigger_event="Consent withdrawal date or 24 months since last engagement",
        ),
        DataCategory(
            category_id="CAT-005",
            name="Website Analytics",
            data_elements=["IP address", "device data", "browsing behaviour", "cookies"],
            processing_purpose="Website optimization",
            legal_basis="Art. 6(1)(f) Legitimate interest",
            retention_period_days=26 * 30,  # 26 months
            retention_source="ICO guidance; CNIL recommendation on analytics cookies",
            trigger_event="Data collection date",
        ),
        DataCategory(
            category_id="CAT-006",
            name="Job Applicant Data (Unsuccessful)",
            data_elements=["CV", "cover letter", "interview notes", "references"],
            processing_purpose="Recruitment",
            legal_basis="Art. 6(1)(b) Pre-contractual steps",
            retention_period_days=6 * 30,  # 6 months
            retention_source="ICO Employment Practices Code; Equality Act limitation",
            trigger_event="Recruitment decision date",
        ),
        DataCategory(
            category_id="CAT-007",
            name="CCTV Footage",
            data_elements=["video recordings of premises"],
            processing_purpose="Security and safety",
            legal_basis="Art. 6(1)(f) Legitimate interest",
            retention_period_days=30,
            retention_source="ICO CCTV Code of Practice; proportionality principle",
            trigger_event="Recording date",
        ),
        DataCategory(
            category_id="CAT-008",
            name="Supplier Contact Data",
            data_elements=["name", "email", "phone", "company", "contract terms"],
            processing_purpose="Vendor management",
            legal_basis="Art. 6(1)(b) Contract",
            retention_period_days=6 * 365,
            retention_source="Limitation Act 1980; contractual necessity",
            trigger_event="Contract termination date",
        ),
        DataCategory(
            category_id="CAT-009",
            name="Customer Support Records",
            data_elements=["tickets", "correspondence", "complaint records"],
            processing_purpose="Service delivery and quality",
            legal_basis="Art. 6(1)(b) Contract + Art. 6(1)(f) Legitimate interest",
            retention_period_days=3 * 365,
            retention_source="Legitimate interest; limitation period for service-related claims",
            trigger_event="Case closure date",
        ),
        DataCategory(
            category_id="CAT-010",
            name="Financial and Tax Records",
            data_elements=["accounts", "tax filings", "audit reports", "bank statements"],
            processing_purpose="Legal compliance",
            legal_basis="Art. 6(1)(c) Legal obligation",
            retention_period_days=6 * 365,
            retention_source="HMRC requirements; Companies Act 2006 s.388; Limitation Act 1980 s.8",
            trigger_event="End of relevant financial year",
        ),
    ]


def determine_retention_period(
    statutory_requirements: list[str],
    contractual_period_days: int = 0,
    additional_buffer_days: int = 0,
) -> dict:
    """
    Determine the appropriate retention period based on applicable statutory
    requirements, contractual obligations, and limitation periods.

    Returns the longest applicable period with its source.
    """
    max_days = 0
    governing_source = "None"

    for req_key in statutory_requirements:
        if req_key in STATUTORY_PERIODS:
            period = STATUTORY_PERIODS[req_key]
            days = 0
            if "years" in period:
                days = period["years"] * 365
            elif "months" in period:
                days = period["months"] * 30
            elif "days" in period:
                days = period["days"]

            if days > max_days:
                max_days = days
                governing_source = period["source"]

    if contractual_period_days + additional_buffer_days > max_days:
        max_days = contractual_period_days + additional_buffer_days
        governing_source = "Contractual obligation + buffer"

    return {
        "retention_period_days": max_days,
        "governing_source": governing_source,
        "statutory_requirements_checked": statutory_requirements,
    }


def generate_retention_review_report(
    schedule: list[DataCategory],
    reference_date: Optional[datetime] = None,
) -> dict:
    """Generate a retention schedule review report."""
    if reference_date is None:
        reference_date = datetime.utcnow()

    report = {
        "report_date": reference_date.isoformat(),
        "organization": "Orion Data Vault Corp",
        "total_categories": len(schedule),
        "categories": [],
    }

    for category in schedule:
        report["categories"].append({
            "category_id": category.category_id,
            "name": category.name,
            "retention_period_days": category.retention_period_days,
            "retention_source": category.retention_source,
            "trigger_event": category.trigger_event,
            "review_frequency": category.review_frequency,
            "status": "Active",
        })

    return report


def export_schedule_json(schedule: list[DataCategory], output_path: str) -> None:
    """Export the retention schedule to JSON format."""
    data = {
        "organization": "Orion Data Vault Corp",
        "generated_date": datetime.utcnow().isoformat(),
        "categories": [cat.to_dict() for cat in schedule],
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    schedule = build_default_schedule()
    report = generate_retention_review_report(schedule)
    print(json.dumps(report, indent=2))
