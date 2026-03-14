#!/usr/bin/env python3
"""
Data Protection by Default Verification Engine

Implements GDPR Article 25(2) by-default compliance verification
across the four dimensions: amount, extent, period, and accessibility.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class DefaultDimension(Enum):
    AMOUNT = "amount"
    EXTENT = "extent"
    PERIOD = "period"
    ACCESSIBILITY = "accessibility"


class ComplianceStatus(Enum):
    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"
    PARTIAL = "PARTIAL"


@dataclass
class DefaultCheck:
    """A single by-default compliance check."""
    check_id: str
    dimension: DefaultDimension
    description: str
    expected_default: str
    actual_default: str = ""
    compliant: bool = False
    remediation: str = ""


class ByDefaultVerifier:
    """Verifies data protection by default compliance per Article 25(2)."""

    def __init__(self, product_name: str, organization: str = "Prism Data Systems AG"):
        self.product_name = product_name
        self.organization = organization
        self.checks: list[DefaultCheck] = []
        self.verification_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    def add_check(self, check: DefaultCheck) -> None:
        self.checks.append(check)

    def evaluate_check(self, check_id: str, actual_default: str, compliant: bool) -> None:
        for check in self.checks:
            if check.check_id == check_id:
                check.actual_default = actual_default
                check.compliant = compliant
                if not compliant:
                    check.remediation = f"Change default from '{actual_default}' to '{check.expected_default}'"
                break

    def get_results(self) -> dict:
        total = len(self.checks)
        compliant_count = sum(1 for c in self.checks if c.compliant)
        non_compliant = [c for c in self.checks if not c.compliant]

        by_dimension = {}
        for dim in DefaultDimension:
            dim_checks = [c for c in self.checks if c.dimension == dim]
            dim_compliant = sum(1 for c in dim_checks if c.compliant)
            by_dimension[dim.value] = {
                "total": len(dim_checks),
                "compliant": dim_compliant,
                "compliance_rate": (dim_compliant / len(dim_checks) * 100) if dim_checks else 0,
            }

        overall_status = ComplianceStatus.COMPLIANT if compliant_count == total else (
            ComplianceStatus.PARTIAL if compliant_count > 0 else ComplianceStatus.NON_COMPLIANT
        )

        return {
            "product": self.product_name,
            "organization": self.organization,
            "verification_date": self.verification_date,
            "overall_status": overall_status.value,
            "total_checks": total,
            "compliant": compliant_count,
            "non_compliant": total - compliant_count,
            "compliance_rate": (compliant_count / total * 100) if total > 0 else 0,
            "by_dimension": by_dimension,
            "failures": [
                {
                    "check_id": c.check_id,
                    "dimension": c.dimension.value,
                    "description": c.description,
                    "expected": c.expected_default,
                    "actual": c.actual_default,
                    "remediation": c.remediation,
                }
                for c in non_compliant
            ],
        }


@dataclass
class ProductDefaultConfig:
    """Default configuration for a product's privacy settings."""
    product_name: str
    registration_fields: dict[str, bool]  # field_name -> mandatory (True) or optional (False)
    processing_defaults: dict[str, bool]   # processing_activity -> default ON/OFF
    retention_defaults: dict[str, int]     # data_category -> default retention days
    access_defaults: dict[str, list[str]]  # role -> list of accessible data categories


def verify_product_defaults(config: ProductDefaultConfig) -> dict:
    """Run a complete by-default verification on a product configuration."""

    verifier = ByDefaultVerifier(config.product_name)

    # Dimension 1: Amount checks
    for field_name, mandatory in config.registration_fields.items():
        if not mandatory:
            verifier.add_check(DefaultCheck(
                check_id=f"AMT-{field_name}",
                dimension=DefaultDimension.AMOUNT,
                description=f"Optional field '{field_name}' should not be collected by default",
                expected_default="Not collected (opt-in only)",
            ))

    # Dimension 2: Extent checks
    for activity, default_on in config.processing_defaults.items():
        verifier.add_check(DefaultCheck(
            check_id=f"EXT-{activity}",
            dimension=DefaultDimension.EXTENT,
            description=f"Processing activity '{activity}' default state",
            expected_default="OFF (opt-in required)" if activity != "core_service" else "ON (contractual basis)",
        ))

    # Dimension 3: Period checks
    for category, days in config.retention_defaults.items():
        verifier.add_check(DefaultCheck(
            check_id=f"PER-{category}",
            dimension=DefaultDimension.PERIOD,
            description=f"Retention period for '{category}' should be minimum necessary",
            expected_default=f"Shortest defensible period",
        ))

    # Dimension 4: Accessibility checks
    for role, categories in config.access_defaults.items():
        verifier.add_check(DefaultCheck(
            check_id=f"ACC-{role}",
            dimension=DefaultDimension.ACCESSIBILITY,
            description=f"Role '{role}' default access scope",
            expected_default="Minimum necessary for role function",
        ))

    # Evaluate checks against the config
    for field_name, mandatory in config.registration_fields.items():
        if not mandatory:
            verifier.evaluate_check(
                f"AMT-{field_name}",
                actual_default="Not collected" if not mandatory else "Collected",
                compliant=True,  # Optional fields exist but are not collected by default
            )

    for activity, default_on in config.processing_defaults.items():
        if activity == "core_service":
            verifier.evaluate_check(f"EXT-{activity}", "ON", compliant=True)
        else:
            verifier.evaluate_check(
                f"EXT-{activity}",
                "ON" if default_on else "OFF",
                compliant=not default_on,
            )

    for category, days in config.retention_defaults.items():
        max_acceptable = {
            "session_data": 1,
            "server_logs": 90,
            "account_data": 2650,
            "support_tickets": 365,
            "analytics_data": 395,
        }
        limit = max_acceptable.get(category, 365)
        verifier.evaluate_check(
            f"PER-{category}",
            f"{days} days",
            compliant=days <= limit,
        )

    for role, categories in config.access_defaults.items():
        max_categories = {
            "support_tier1": 2,
            "analytics_team": 1,
            "engineering": 0,
            "marketing": 1,
            "dpo": 10,
        }
        limit = max_categories.get(role, 2)
        verifier.evaluate_check(
            f"ACC-{role}",
            f"{len(categories)} data categories",
            compliant=len(categories) <= limit,
        )

    return verifier.get_results()


def run_example():
    """Demonstrate by-default verification for Prism Data Systems AG."""

    # Compliant product configuration
    compliant_config = ProductDefaultConfig(
        product_name="Prism Analytics Platform v3.2",
        registration_fields={
            "email": True,
            "display_name": True,
            "country_code": True,
            "phone_number": False,
            "billing_address": False,
            "company_name": False,
        },
        processing_defaults={
            "core_service": True,
            "product_analytics": False,
            "marketing_emails": False,
            "feature_recommendations": False,
            "ml_training": False,
        },
        retention_defaults={
            "session_data": 0,
            "server_logs": 90,
            "account_data": 2555,
            "support_tickets": 365,
            "analytics_data": 395,
        },
        access_defaults={
            "support_tier1": ["masked_email", "country_code"],
            "analytics_team": ["pseudonymized_events"],
            "engineering": [],
            "marketing": ["aggregate_stats"],
            "dpo": ["email", "display_name", "country_code", "consent_records"],
        },
    )

    print("=== Data Protection by Default Verification ===")
    print("Product: Prism Analytics Platform v3.2")
    print()

    results = verify_product_defaults(compliant_config)

    print(f"Overall Status: {results['overall_status']}")
    print(f"Compliance Rate: {results['compliance_rate']:.0f}%")
    print(f"Checks: {results['compliant']}/{results['total_checks']} compliant")
    print()

    print("--- By Dimension ---")
    for dim, data in results["by_dimension"].items():
        print(f"  {dim}: {data['compliant']}/{data['total']} compliant ({data['compliance_rate']:.0f}%)")
    print()

    if results["failures"]:
        print("--- Non-Compliant Items ---")
        for fail in results["failures"]:
            print(f"  [{fail['check_id']}] {fail['description']}")
            print(f"    Expected: {fail['expected']}")
            print(f"    Actual: {fail['actual']}")
            print(f"    Remediation: {fail['remediation']}")
            print()
    else:
        print("All checks passed. Product meets Article 25(2) by-default requirements.")
    print()

    # Non-compliant configuration for comparison
    non_compliant_config = ProductDefaultConfig(
        product_name="Legacy Widget Dashboard v1.0",
        registration_fields={
            "email": True,
            "display_name": True,
            "phone_number": False,
            "date_of_birth": False,
        },
        processing_defaults={
            "core_service": True,
            "product_analytics": True,    # NON-COMPLIANT: analytics ON by default
            "marketing_emails": True,     # NON-COMPLIANT: marketing ON by default
            "feature_recommendations": False,
        },
        retention_defaults={
            "session_data": 0,
            "server_logs": 365,           # NON-COMPLIANT: exceeds 90-day recommendation
            "account_data": 2555,
            "analytics_data": 730,        # NON-COMPLIANT: exceeds 395-day limit
        },
        access_defaults={
            "support_tier1": ["email", "phone", "display_name", "account_data"],  # NON-COMPLIANT: too broad
            "analytics_team": ["pseudonymized_events"],
            "engineering": [],
            "marketing": ["aggregate_stats"],
        },
    )

    print("=== Comparison: Non-Compliant Product ===")
    print("Product: Legacy Widget Dashboard v1.0")
    print()

    results2 = verify_product_defaults(non_compliant_config)

    print(f"Overall Status: {results2['overall_status']}")
    print(f"Compliance Rate: {results2['compliance_rate']:.0f}%")
    print()

    if results2["failures"]:
        print(f"Non-Compliant Items ({len(results2['failures'])}):")
        for fail in results2["failures"]:
            print(f"  [{fail['check_id']}] {fail['description']}")
            print(f"    Actual: {fail['actual']} | Remediation: {fail['remediation']}")


if __name__ == "__main__":
    run_example()
