#!/usr/bin/env python3
"""
Data Minimization Assessment and Pseudonymization Engine

Implements GDPR Article 5(1)(c) data minimization scoring and
Article 4(5) pseudonymization using HMAC-SHA256.
"""

import hashlib
import hmac
import json
import os
import secrets
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import IntEnum
from typing import Optional


class SensitivityTier(IntEnum):
    """Data sensitivity classification tiers per Prism Data Systems AG policy."""
    T1_DIRECT_IDENTIFIER = 1    # email, full_name, national_id
    T2_QUASI_IDENTIFIER = 2     # date_of_birth, postal_code
    T3_SENSITIVE_ATTRIBUTE = 3  # health_data, financial_score
    T4_NON_IDENTIFYING = 4     # country_code, language_preference


@dataclass
class DataField:
    """Represents a personal data field subject to minimization assessment."""
    name: str
    purpose: str
    lawful_basis: str
    sensitivity_tier: SensitivityTier
    necessity_score: int = 0         # 0-2: Is field required for purpose?
    proportionality_score: int = 0   # 0-2: Could less identifying alternative work?
    aggregation_score: int = 0       # 0-2: Can field be aggregated?
    pseudonymization_score: int = 0  # 0-2: Can field be pseudonymized?
    temporal_score: int = 0          # 0-2: Is field needed beyond transaction?
    access_score: int = 0            # 0-2: How many roles need raw access?

    @property
    def total_score(self) -> int:
        return (
            self.necessity_score
            + self.proportionality_score
            + self.aggregation_score
            + self.pseudonymization_score
            + self.temporal_score
            + self.access_score
        )

    @property
    def recommendation(self) -> str:
        score = self.total_score
        if score <= 4:
            return "ELIMINATE or AGGREGATE — strong candidate for removal or pseudonymization"
        elif score <= 8:
            return "PROTECT — apply masking, field-level encryption, and access controls"
        else:
            return "RETAIN WITH SAFEGUARDS — justified retention with full technical controls"


class MinimizationAssessor:
    """Conducts data minimization assessments per GDPR Article 5(1)(c)."""

    def __init__(self, organization: str = "Prism Data Systems AG"):
        self.organization = organization
        self.assessment_date = datetime.now(timezone.utc).isoformat()
        self.fields: list[DataField] = []

    def add_field(self, data_field: DataField) -> None:
        self.fields.append(data_field)

    def assess_all(self) -> dict:
        results = {
            "organization": self.organization,
            "assessment_date": self.assessment_date,
            "gdpr_basis": "Article 5(1)(c), Article 25(1)",
            "total_fields_assessed": len(self.fields),
            "fields_to_eliminate": 0,
            "fields_to_protect": 0,
            "fields_to_retain": 0,
            "field_assessments": [],
        }

        for f in self.fields:
            assessment = {
                "field_name": f.name,
                "purpose": f.purpose,
                "lawful_basis": f.lawful_basis,
                "sensitivity_tier": f"T{f.sensitivity_tier}",
                "scores": {
                    "necessity": f.necessity_score,
                    "proportionality": f.proportionality_score,
                    "aggregation_potential": f.aggregation_score,
                    "pseudonymization_feasibility": f.pseudonymization_score,
                    "temporal_scope": f.temporal_score,
                    "access_scope": f.access_score,
                    "total": f.total_score,
                },
                "recommendation": f.recommendation,
            }
            results["field_assessments"].append(assessment)

            if f.total_score <= 4:
                results["fields_to_eliminate"] += 1
            elif f.total_score <= 8:
                results["fields_to_protect"] += 1
            else:
                results["fields_to_retain"] += 1

        return results


class PseudonymizationEngine:
    """
    HMAC-SHA256 pseudonymization engine per ENISA 2019 recommendations.

    Implements keyed pseudonymization with key versioning and rotation support.
    In production, the HMAC key would be stored in an HSM (FIPS 140-2 Level 3).
    """

    def __init__(self, key: Optional[bytes] = None, key_version: str = "v001"):
        self.key = key or secrets.token_bytes(32)
        self.key_version = key_version
        self.pseudonymization_log: list[dict] = []

    def pseudonymize(self, value: str, context: str = "default") -> str:
        """
        Generate a pseudonym for a given value using HMAC-SHA256.

        Args:
            value: The personal data value to pseudonymize.
            context: Processing context (e.g., 'analytics', 'reporting') to enable
                     purpose-separated pseudonyms per Article 5(1)(b).

        Returns:
            A hex-encoded pseudonym prefixed with key version.
        """
        message = f"{context}:{value}".encode("utf-8")
        digest = hmac.new(self.key, message, hashlib.sha256).hexdigest()
        pseudonym = f"PSE-{self.key_version}-{digest[:16]}"

        self.pseudonymization_log.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "context": context,
            "key_version": self.key_version,
            "pseudonym_prefix": pseudonym[:12],
        })

        return pseudonym

    def rotate_key(self) -> "PseudonymizationEngine":
        """
        Create a new engine instance with a rotated key.

        Returns:
            New PseudonymizationEngine with fresh key material.
        """
        version_num = int(self.key_version[1:]) + 1
        new_version = f"v{version_num:03d}"
        return PseudonymizationEngine(
            key=secrets.token_bytes(32),
            key_version=new_version,
        )

    def verify_pseudonym(self, value: str, pseudonym: str, context: str = "default") -> bool:
        """Verify that a pseudonym matches a given value under the current key."""
        expected = self.pseudonymize(value, context)
        return hmac.compare_digest(expected, pseudonym)


class DataMaskingEngine:
    """Dynamic data masking for access minimization."""

    MASKING_RULES = {
        "email": lambda v: v[0] + "***" + v[v.index("@"):] if "@" in v else "***",
        "phone": lambda v: "***-***-" + v[-4:] if len(v) >= 4 else "***",
        "name": lambda v: v[0] + "***" + (" " + v.split()[-1][0] + "***" if " " in v else ""),
        "national_id": lambda v: "***-**-" + v[-4:] if len(v) >= 4 else "***",
        "credit_card": lambda v: "****-****-****-" + v[-4:] if len(v) >= 4 else "***",
        "date_of_birth": lambda _: "****-**-**",
        "postal_code": lambda v: v[:2] + "***" if len(v) >= 2 else "***",
    }

    @classmethod
    def mask(cls, value: str, field_type: str) -> str:
        rule = cls.MASKING_RULES.get(field_type)
        if rule is None:
            return "***"
        return rule(value)

    @classmethod
    def mask_record(cls, record: dict, field_types: dict, role: str, role_permissions: dict) -> dict:
        """
        Apply dynamic masking to a record based on the requester's role.

        Args:
            record: Dictionary of field_name -> value.
            field_types: Dictionary of field_name -> field_type (email, phone, etc.).
            role: The requester's role identifier.
            role_permissions: Dictionary of role -> list of fields allowed unmasked.

        Returns:
            Record with masking applied based on role permissions.
        """
        allowed_fields = role_permissions.get(role, [])
        masked = {}
        for field_name, value in record.items():
            if field_name in allowed_fields:
                masked[field_name] = value
            elif field_name in field_types:
                masked[field_name] = cls.mask(value, field_types[field_name])
            else:
                masked[field_name] = value
        return masked


def run_assessment_example():
    """Run a complete data minimization assessment for Prism Data Systems AG."""

    assessor = MinimizationAssessor()

    assessor.add_field(DataField(
        name="email",
        purpose="Account authentication and transactional notifications",
        lawful_basis="Article 6(1)(b) — contractual necessity",
        sensitivity_tier=SensitivityTier.T1_DIRECT_IDENTIFIER,
        necessity_score=2,
        proportionality_score=2,
        aggregation_score=2,
        pseudonymization_score=1,
        temporal_score=2,
        access_score=1,
    ))

    assessor.add_field(DataField(
        name="browsing_history",
        purpose="Product recommendation engine",
        lawful_basis="Article 6(1)(a) — consent",
        sensitivity_tier=SensitivityTier.T2_QUASI_IDENTIFIER,
        necessity_score=1,
        proportionality_score=0,
        aggregation_score=0,
        pseudonymization_score=0,
        temporal_score=0,
        access_score=0,
    ))

    assessor.add_field(DataField(
        name="ip_address",
        purpose="Fraud detection and geographic access control",
        lawful_basis="Article 6(1)(f) — legitimate interest",
        sensitivity_tier=SensitivityTier.T2_QUASI_IDENTIFIER,
        necessity_score=2,
        proportionality_score=1,
        aggregation_score=1,
        pseudonymization_score=0,
        temporal_score=1,
        access_score=1,
    ))

    assessor.add_field(DataField(
        name="date_of_birth",
        purpose="Age verification for restricted content",
        lawful_basis="Article 6(1)(c) — legal obligation",
        sensitivity_tier=SensitivityTier.T2_QUASI_IDENTIFIER,
        necessity_score=1,
        proportionality_score=0,
        aggregation_score=0,
        pseudonymization_score=0,
        temporal_score=0,
        access_score=0,
    ))

    results = assessor.assess_all()
    print("=== Data Minimization Assessment Report ===")
    print(f"Organization: {results['organization']}")
    print(f"Date: {results['assessment_date']}")
    print(f"GDPR Basis: {results['gdpr_basis']}")
    print(f"Fields Assessed: {results['total_fields_assessed']}")
    print(f"  Eliminate/Aggregate: {results['fields_to_eliminate']}")
    print(f"  Protect (mask/encrypt): {results['fields_to_protect']}")
    print(f"  Retain with safeguards: {results['fields_to_retain']}")
    print()

    for fa in results["field_assessments"]:
        print(f"Field: {fa['field_name']}")
        print(f"  Purpose: {fa['purpose']}")
        print(f"  Score: {fa['scores']['total']}/12")
        print(f"  Recommendation: {fa['recommendation']}")
        print()

    print("=== Pseudonymization Demo ===")
    engine = PseudonymizationEngine(key_version="v003")

    test_values = [
        ("user-12847@prism-data.ch", "analytics"),
        ("user-12847@prism-data.ch", "reporting"),
        ("user-55901@prism-data.ch", "analytics"),
    ]

    for value, context in test_values:
        pseudonym = engine.pseudonymize(value, context)
        print(f"  {value} [{context}] -> {pseudonym}")

    print()
    print("=== Dynamic Masking Demo ===")
    customer_record = {
        "email": "maria.schneider@prism-data.ch",
        "phone": "+41-44-555-7892",
        "full_name": "Maria Schneider",
        "national_id": "756.1234.5678.97",
        "country_code": "CH",
    }

    field_types = {
        "email": "email",
        "phone": "phone",
        "full_name": "name",
        "national_id": "national_id",
    }

    role_permissions = {
        "support_agent": ["country_code"],
        "escalation_agent": ["email", "phone", "country_code"],
        "data_protection_officer": ["email", "phone", "full_name", "national_id", "country_code"],
    }

    for role in ["support_agent", "escalation_agent", "data_protection_officer"]:
        masked = DataMaskingEngine.mask_record(
            customer_record, field_types, role, role_permissions
        )
        print(f"  Role: {role}")
        for k, v in masked.items():
            print(f"    {k}: {v}")
        print()


if __name__ == "__main__":
    run_assessment_example()
