#!/usr/bin/env python3
"""
Transfer Consent Management

Manages explicit consent for international data transfers
per GDPR Article 49(1)(a) requirements.
"""

import json
import hashlib
import uuid
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional


# EU Adequacy decisions as of March 2026
ADEQUACY_DECISIONS = {
    "AD": "Andorra", "AR": "Argentina", "CA": "Canada (commercial)",
    "FO": "Faroe Islands", "GG": "Guernsey", "IL": "Israel",
    "IM": "Isle of Man", "JP": "Japan", "JE": "Jersey",
    "NZ": "New Zealand", "KR": "South Korea", "CH": "Switzerland",
    "GB": "United Kingdom", "UY": "Uruguay", "US": "United States (DPF)",
}


@dataclass
class TransferRiskAssessment:
    """Risk assessment for a specific international transfer."""
    destination_country: str = ""
    destination_country_name: str = ""
    has_adequacy_decision: bool = False
    has_appropriate_safeguards: bool = False
    risk_factors: list[str] = field(default_factory=list)
    risk_level: str = "high"  # "low", "medium", "high"
    explicit_consent_required: bool = True


@dataclass
class TransferConsentRecord:
    """Consent record specifically for international transfers."""
    consent_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    subject_id: str = ""
    destination_country: str = ""
    recipient_name: str = ""
    recipient_address: str = ""
    purpose: str = ""
    data_categories: list[str] = field(default_factory=list)
    has_adequacy_decision: bool = False
    has_appropriate_safeguards: bool = False
    risk_disclosure_version: str = ""
    consent_type: str = "explicit_typed_declaration"
    typed_statement: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    status: str = "granted"  # "granted", "withdrawn"

    def to_dict(self) -> dict:
        return asdict(self)


def assess_transfer_risk(
    destination_country_code: str,
    has_sccs: bool = False,
    has_bcrs: bool = False,
) -> TransferRiskAssessment:
    """
    Assess the risk of transferring data to a specific country.

    Determines whether explicit consent is needed under Article 49(1)(a).
    """
    has_adequacy = destination_country_code in ADEQUACY_DECISIONS
    has_safeguards = has_sccs or has_bcrs

    country_names = {
        "IN": "India", "CN": "China", "BR": "Brazil", "RU": "Russia",
        "NG": "Nigeria", "PH": "Philippines", "UA": "Ukraine",
    }
    country_name = ADEQUACY_DECISIONS.get(
        destination_country_code,
        country_names.get(destination_country_code, destination_country_code)
    )

    risk_factors = []
    if not has_adequacy:
        risk_factors.append(
            f"{country_name} does not have an EU adequacy decision under Article 45"
        )
    if not has_safeguards:
        risk_factors.append(
            "Transfer is not covered by Standard Contractual Clauses (Art. 46(2)(c)) "
            "or Binding Corporate Rules (Art. 47)"
        )

    if has_adequacy:
        risk_level = "low"
        explicit_consent_required = False
    elif has_safeguards:
        risk_level = "medium"
        explicit_consent_required = False
    else:
        risk_level = "high"
        explicit_consent_required = True
        risk_factors.append(
            "Without adequacy or safeguards, transfer relies on Article 49 derogations. "
            "Explicit consent required under Article 49(1)(a)."
        )

    return TransferRiskAssessment(
        destination_country=destination_country_code,
        destination_country_name=country_name,
        has_adequacy_decision=has_adequacy,
        has_appropriate_safeguards=has_safeguards,
        risk_factors=risk_factors,
        risk_level=risk_level,
        explicit_consent_required=explicit_consent_required,
    )


def generate_risk_disclosure(
    destination_country: str,
    recipient_name: str,
    purpose: str,
    data_categories: list[str],
) -> tuple[str, str]:
    """
    Generate the risk disclosure text required before obtaining transfer consent.

    Returns:
        Tuple of (disclosure_text, text_hash).
    """
    risk_assessment = assess_transfer_risk(destination_country)

    disclosure = (
        f"To {purpose}, CloudVault SaaS Inc. may transfer your personal data "
        f"({', '.join(data_categories)}) to {recipient_name} in {risk_assessment.destination_country_name}.\n\n"
        f"{risk_assessment.destination_country_name} does not have an adequacy decision "
        f"from the European Commission, and this transfer is not covered by Standard "
        f"Contractual Clauses or Binding Corporate Rules.\n\n"
        f"This means your data may not receive the same level of protection as under EU law. "
        f"Specifically:\n"
        f"- The data protection framework in {risk_assessment.destination_country_name} may not "
        f"provide equivalent rights and remedies\n"
        f"- Government authorities in {risk_assessment.destination_country_name} may have legal "
        f"powers to access personal data that differ from EU standards\n"
        f"- Judicial remedies available to you may differ from those under EU law\n\n"
        f"You are not required to consent to this transfer. You can withdraw consent "
        f"at any time in Settings > Privacy > Data Transfers."
    )

    text_hash = hashlib.sha256(disclosure.encode("utf-8")).hexdigest()
    return disclosure, text_hash


if __name__ == "__main__":
    # Assess transfer risk for various countries
    print("=== Transfer Risk Assessments ===")
    countries = [
        ("GB", False, False, "United Kingdom (adequacy)"),
        ("US", False, False, "United States (DPF adequacy)"),
        ("IN", False, False, "India (no adequacy, no safeguards)"),
        ("IN", True, False, "India (with SCCs)"),
        ("BR", False, False, "Brazil (no adequacy, no safeguards)"),
    ]

    for code, sccs, bcrs, label in countries:
        assessment = assess_transfer_risk(code, sccs, bcrs)
        print(f"\n  {label}:")
        print(f"    Risk Level: {assessment.risk_level}")
        print(f"    Explicit Consent Required: {assessment.explicit_consent_required}")
        for rf in assessment.risk_factors:
            print(f"    - {rf}")

    # Generate risk disclosure
    print("\n=== Risk Disclosure (India) ===")
    disclosure, text_hash = generate_risk_disclosure(
        "IN",
        "CloudVault India Pvt. Ltd.",
        "provide 24/7 customer support",
        ["name", "email address", "account metadata", "support ticket content"],
    )
    print(disclosure[:300] + "...")
    print(f"\nDisclosure hash: {text_hash[:32]}...")

    # Create transfer consent record
    print("\n=== Transfer Consent Record ===")
    record = TransferConsentRecord(
        subject_id="usr_7f3a9b2e-41d8-4c76-b5e3-9a8d1c2f4e60",
        destination_country="IN",
        recipient_name="CloudVault India Pvt. Ltd.",
        recipient_address="100 MG Road, Bengaluru, Karnataka 560001, India",
        purpose="24/7 customer support ticket handling",
        data_categories=["name", "email", "account_metadata", "support_ticket_content"],
        risk_disclosure_version=text_hash,
        typed_statement="I consent to the transfer",
        ip_address="198.51.100.42",
    )
    print(json.dumps(record.to_dict(), indent=2, default=str))
