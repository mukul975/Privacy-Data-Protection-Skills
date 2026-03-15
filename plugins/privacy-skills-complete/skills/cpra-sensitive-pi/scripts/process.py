#!/usr/bin/env python3
"""
CPRA Sensitive Personal Information Classification and Limit-Request Processor

Classifies data elements against §1798.140(ae) categories, processes
consumer limit requests under §1798.121, and audits compliance with
permitted purpose restrictions.
"""

import json
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class SensitivePICategory(Enum):
    GOVERNMENT_ID = "government_identifiers"
    ACCOUNT_CREDENTIALS = "account_credentials"
    PRECISE_GEOLOCATION = "precise_geolocation"
    RACIAL_ETHNIC = "racial_ethnic_origin"
    RELIGIOUS_PHILOSOPHICAL = "religious_philosophical_beliefs"
    UNION_MEMBERSHIP = "union_membership"
    PRIVATE_COMMUNICATIONS = "private_communications_content"
    GENETIC_DATA = "genetic_data"
    BIOMETRIC_DATA = "biometric_information"
    HEALTH_INFO = "health_information"
    SEX_LIFE_ORIENTATION = "sex_life_sexual_orientation"


class PermittedPurpose(Enum):
    SERVICE_FULFILLMENT = "perform_services_provide_goods"
    SECURITY_INCIDENTS = "prevent_detect_investigate_security"
    RESIST_MALICIOUS = "resist_malicious_deceptive_illegal"
    PHYSICAL_SAFETY = "ensure_physical_safety"
    SHORT_TERM_TRANSIENT = "short_term_transient_use"
    BUSINESS_SERVICES = "perform_services_on_behalf"
    QUALITY_SAFETY = "verify_maintain_quality_safety"
    UPGRADE_IMPROVE = "upgrade_enhance_improve_services"


SENSITIVE_PI_DEFINITIONS = {
    SensitivePICategory.GOVERNMENT_ID: {
        "section": "§1798.140(ae)(1)",
        "description": "Social Security number, driver's license number, state ID card number, or passport number",
        "examples": ["SSN", "Driver's license", "State ID", "Passport number"],
        "geolocation_threshold": None,
    },
    SensitivePICategory.ACCOUNT_CREDENTIALS: {
        "section": "§1798.140(ae)(2)",
        "description": "Account log-in, financial account, debit/credit card number with required security/access code, password, or credentials",
        "examples": ["Username + password", "Credit card + CVV", "Bank account + PIN"],
        "geolocation_threshold": None,
    },
    SensitivePICategory.PRECISE_GEOLOCATION: {
        "section": "§1798.140(ae)(3)",
        "description": "Data derived from device used to locate consumer within area equal to or less than circle with 1,850-foot radius",
        "examples": ["GPS coordinates", "Wi-Fi triangulation", "Cell tower triangulation"],
        "geolocation_threshold_feet": 1850,
        "geolocation_threshold_meters": 564,
    },
    SensitivePICategory.RACIAL_ETHNIC: {
        "section": "§1798.140(ae)(4)",
        "description": "Racial or ethnic origin",
        "examples": ["Self-reported race/ethnicity", "Diversity survey responses"],
    },
    SensitivePICategory.RELIGIOUS_PHILOSOPHICAL: {
        "section": "§1798.140(ae)(5)",
        "description": "Religious or philosophical beliefs",
        "examples": ["Religious affiliation", "Philosophical views from surveys"],
    },
    SensitivePICategory.UNION_MEMBERSHIP: {
        "section": "§1798.140(ae)(6)",
        "description": "Union membership",
        "examples": ["Trade union membership", "Union dues records"],
    },
    SensitivePICategory.PRIVATE_COMMUNICATIONS: {
        "section": "§1798.140(ae)(7)",
        "description": "Contents of mail, email, text messages (where business is not intended recipient)",
        "examples": ["Intercepted messages", "Forwarded private emails", "Scanned mail contents"],
    },
    SensitivePICategory.GENETIC_DATA: {
        "section": "§1798.140(ae)(8)",
        "description": "Genetic data",
        "examples": ["DNA test results", "Genetic predisposition data", "Genome sequences"],
    },
    SensitivePICategory.BIOMETRIC_DATA: {
        "section": "§1798.140(ae)(9)",
        "description": "Biometric information processed for uniquely identifying a consumer",
        "examples": ["Fingerprint templates", "Facial recognition data", "Iris scans", "Voiceprints"],
    },
    SensitivePICategory.HEALTH_INFO: {
        "section": "§1798.140(ae)(10)",
        "description": "Health information",
        "examples": ["Medical records", "Health conditions", "Prescription data", "Fitness data"],
    },
    SensitivePICategory.SEX_LIFE_ORIENTATION: {
        "section": "§1798.140(ae)(11)",
        "description": "Information concerning sex life or sexual orientation",
        "examples": ["Sexual orientation", "Gender identity", "Dating preferences"],
    },
}

PERMITTED_PURPOSES = {
    PermittedPurpose.SERVICE_FULFILLMENT: {
        "section": "§1798.121(a)(1)",
        "description": "Perform services or provide goods reasonably expected by an average consumer who requests those goods or services",
    },
    PermittedPurpose.SECURITY_INCIDENTS: {
        "section": "§1798.121(a)(2)",
        "description": "Prevent, detect, and investigate security incidents that compromise availability, authenticity, integrity, or confidentiality",
    },
    PermittedPurpose.RESIST_MALICIOUS: {
        "section": "§1798.121(a)(3)",
        "description": "Resist malicious, deceptive, fraudulent, or illegal actions directed at the business",
    },
    PermittedPurpose.PHYSICAL_SAFETY: {
        "section": "§1798.121(a)(4)",
        "description": "Ensure the physical safety of natural persons",
    },
    PermittedPurpose.SHORT_TERM_TRANSIENT: {
        "section": "§1798.121(a)(5)",
        "description": "Short-term, transient use, including non-personalized advertising shown as part of a consumer's current interaction",
    },
    PermittedPurpose.BUSINESS_SERVICES: {
        "section": "§1798.121(a)(6)",
        "description": "Perform services on behalf of the business (customer service, account maintenance, order processing, verification, payment, financing, advertising, marketing, analytics, security, operational improvement)",
    },
    PermittedPurpose.QUALITY_SAFETY: {
        "section": "§1798.121(a)(7)",
        "description": "Verify or maintain the quality or safety of a service or device owned, manufactured, manufactured for, or controlled by the business",
    },
    PermittedPurpose.UPGRADE_IMPROVE: {
        "section": "§1798.121(a)(8)",
        "description": "Upgrade, enhance, or improve the service or device owned, manufactured, manufactured for, or controlled by the business",
    },
}


@dataclass
class DataElementClassification:
    """Classification of a data element against sensitive PI categories."""
    data_element: str
    is_sensitive: bool
    category: Optional[SensitivePICategory] = None
    section: str = ""
    justification: str = ""
    collection_purpose: str = ""
    permitted_purposes_after_limit: list = field(default_factory=list)
    retention_period: str = ""

    def to_dict(self) -> dict:
        result = asdict(self)
        if self.category:
            result["category"] = self.category.value
        result["permitted_purposes_after_limit"] = [p.value if isinstance(p, PermittedPurpose) else p for p in self.permitted_purposes_after_limit]
        return result


@dataclass
class LimitRequest:
    """Consumer limit request under §1798.121."""
    request_id: str
    consumer_id: str
    received_timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    categories_limited: list = field(default_factory=list)
    status: str = "received"
    effective_date: Optional[str] = None
    actions_taken: list = field(default_factory=list)

    def apply_limit(self, categories_processed: list[SensitivePICategory]) -> list[dict]:
        """Apply limit to all sensitive PI categories processed for this consumer."""
        actions = []
        for category in categories_processed:
            cat_def = SENSITIVE_PI_DEFINITIONS.get(category, {})
            action = {
                "category": category.value,
                "section": cat_def.get("section", ""),
                "action": "restricted_to_permitted_purposes",
                "blocked_uses": [],
                "permitted_uses": [],
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }

            if category == SensitivePICategory.PRECISE_GEOLOCATION:
                action["blocked_uses"] = ["targeted_advertising", "location_based_marketing", "sale_to_data_brokers"]
                action["permitted_uses"] = ["delivery_tracking", "store_finder_on_request"]
            elif category == SensitivePICategory.ACCOUNT_CREDENTIALS:
                action["blocked_uses"] = ["profile_enrichment", "cross_referencing"]
                action["permitted_uses"] = ["transaction_processing", "fraud_detection", "authentication"]
            elif category == SensitivePICategory.GOVERNMENT_ID:
                action["blocked_uses"] = ["any_non_original_purpose"]
                action["permitted_uses"] = ["tax_reporting_ssn", "age_verification_dl"]
            elif category == SensitivePICategory.RACIAL_ETHNIC:
                action["blocked_uses"] = ["all_processing"]
                action["permitted_uses"] = ["none_delete_within_30_days"]
            elif category == SensitivePICategory.HEALTH_INFO:
                action["blocked_uses"] = ["behavioral_advertising", "profiling", "sale"]
                action["permitted_uses"] = ["product_recall_notifications"]
            else:
                action["blocked_uses"] = ["all_non_essential_processing"]
                action["permitted_uses"] = ["security_incident_prevention"]

            actions.append(action)

        self.actions_taken = actions
        self.status = "applied"
        self.effective_date = datetime.now(timezone.utc).isoformat()
        self.categories_limited = [c.value for c in categories_processed]
        return actions


def classify_data_element(element_name: str, element_description: str) -> DataElementClassification:
    """Classify a data element against CPRA sensitive PI categories."""
    sensitive_keywords = {
        SensitivePICategory.GOVERNMENT_ID: ["ssn", "social security", "driver's license", "drivers license", "passport", "state id"],
        SensitivePICategory.ACCOUNT_CREDENTIALS: ["password", "credential", "login", "credit card", "debit card", "cvv", "pin", "account number"],
        SensitivePICategory.PRECISE_GEOLOCATION: ["gps", "geolocation", "coordinates", "latitude", "longitude", "precise location"],
        SensitivePICategory.RACIAL_ETHNIC: ["race", "racial", "ethnicity", "ethnic origin"],
        SensitivePICategory.RELIGIOUS_PHILOSOPHICAL: ["religion", "religious", "philosophical", "faith", "belief"],
        SensitivePICategory.UNION_MEMBERSHIP: ["union", "trade union", "labor union"],
        SensitivePICategory.PRIVATE_COMMUNICATIONS: ["mail content", "email content", "message content", "text message content"],
        SensitivePICategory.GENETIC_DATA: ["genetic", "dna", "genome", "genotype"],
        SensitivePICategory.BIOMETRIC_DATA: ["fingerprint", "biometric", "facial recognition", "iris scan", "voiceprint"],
        SensitivePICategory.HEALTH_INFO: ["health", "medical", "diagnosis", "prescription", "treatment", "condition"],
        SensitivePICategory.SEX_LIFE_ORIENTATION: ["sexual orientation", "sex life", "gender identity", "dating preference"],
    }

    combined = f"{element_name} {element_description}".lower()

    for category, keywords in sensitive_keywords.items():
        for keyword in keywords:
            if keyword in combined:
                cat_def = SENSITIVE_PI_DEFINITIONS[category]
                return DataElementClassification(
                    data_element=element_name,
                    is_sensitive=True,
                    category=category,
                    section=cat_def["section"],
                    justification=f"Matches sensitive PI category: {cat_def['description']}",
                )

    return DataElementClassification(
        data_element=element_name,
        is_sensitive=False,
        justification="Does not match any sensitive PI category under §1798.140(ae)",
    )


if __name__ == "__main__":
    # Demonstrate data element classification
    print("=== Sensitive PI Classification ===")
    test_elements = [
        ("GPS Coordinates", "Precise location data from mobile device"),
        ("Email Address", "Consumer's email address for account"),
        ("SSN", "Social Security Number for marketplace seller tax reporting"),
        ("Purchase History", "Record of products purchased"),
        ("Fingerprint Template", "Biometric data for device authentication"),
        ("Ethnicity Survey Response", "Self-reported racial/ethnic origin from diversity survey"),
        ("Credit Card Number", "Payment card with CVV for transaction processing"),
        ("IP Address", "Consumer's IP address from web request"),
    ]

    for name, desc in test_elements:
        result = classify_data_element(name, desc)
        status = f"SENSITIVE ({result.category.value})" if result.is_sensitive else "NOT SENSITIVE"
        print(f"  {name}: {status}")

    # Demonstrate limit request processing
    print("\n=== Limit Request Processing ===")
    limit_req = LimitRequest(
        request_id="LIM-2026-00089",
        consumer_id="CONS-b7e3f142",
    )

    consumer_categories = [
        SensitivePICategory.PRECISE_GEOLOCATION,
        SensitivePICategory.ACCOUNT_CREDENTIALS,
        SensitivePICategory.RACIAL_ETHNIC,
    ]

    actions = limit_req.apply_limit(consumer_categories)
    print(f"Request: {limit_req.request_id}")
    print(f"Status: {limit_req.status}")
    print(f"Categories limited: {limit_req.categories_limited}")
    print(f"\nActions taken:")
    for action in actions:
        print(f"\n  Category: {action['category']}")
        print(f"  Blocked: {', '.join(action['blocked_uses'])}")
        print(f"  Permitted: {', '.join(action['permitted_uses'])}")

    # Print all permitted purposes
    print("\n=== Permitted Purposes After Limit (§1798.121(a)) ===")
    for purpose, details in PERMITTED_PURPOSES.items():
        print(f"  {details['section']}: {details['description']}")
