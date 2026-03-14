"""
Consent Receipt Specification — Receipt Generator and Validator

Implements Kantara Initiative Consent Receipt Specification v1.1
with JSON structure generation and field validation.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
import json
import uuid
import hashlib


class ConsentType(Enum):
    EXPLICIT = "explicit"
    IMPLICIT = "implicit"


class ReceiptStatus(Enum):
    ISSUED = "issued"
    ACTIVE = "active"
    UPDATED = "updated"
    WITHDRAWN = "withdrawn"
    EXPIRED = "expired"


REQUIRED_FIELDS = [
    "version", "jurisdiction", "consentTimestamp", "collectionMethod",
    "consentReceiptID", "language", "piiPrincipalId", "piiControllers",
    "policyUrl", "services", "sensitive",
]


@dataclass
class Purpose:
    purpose: str
    purpose_category: list[str]
    consent_type: ConsentType
    pii_category: list[str]
    primary_purpose: bool
    termination: str
    third_party_disclosure: bool
    third_party_name: Optional[str] = None


@dataclass
class Service:
    service: str
    purposes: list[Purpose]


@dataclass
class Controller:
    name: str
    contact: str
    email: str
    address: dict
    phone: Optional[str] = None
    url: Optional[str] = None
    on_behalf: bool = False


class ConsentReceiptGenerator:
    """Generate Kantara-compliant consent receipts."""

    def __init__(self, controller: Controller):
        self.controller = controller

    def generate(
        self,
        principal_id: str,
        services: list[Service],
        jurisdiction: str,
        collection_method: str,
        policy_url: str,
        sensitive: bool = False,
        language: str = "en",
    ) -> dict:
        """Generate a consent receipt per Kantara v1.1 specification."""
        receipt_id = str(uuid.uuid4())

        receipt = {
            "version": "KI-CR-v1.1.0",
            "jurisdiction": jurisdiction,
            "consentTimestamp": datetime.now(timezone.utc).isoformat(),
            "collectionMethod": collection_method,
            "consentReceiptID": receipt_id,
            "language": language,
            "piiPrincipalId": principal_id,
            "piiControllers": [
                {
                    "piiController": self.controller.name,
                    "onBehalf": self.controller.on_behalf,
                    "contact": self.controller.contact,
                    "address": self.controller.address,
                    "email": self.controller.email,
                    "phone": self.controller.phone,
                    "piiControllerUrl": self.controller.url,
                }
            ],
            "policyUrl": policy_url,
            "services": [
                {
                    "service": svc.service,
                    "purposes": [
                        {
                            "purpose": p.purpose,
                            "purposeCategory": p.purpose_category,
                            "consentType": p.consent_type.value,
                            "piiCategory": p.pii_category,
                            "primaryPurpose": p.primary_purpose,
                            "termination": p.termination,
                            "thirdPartyDisclosure": p.third_party_disclosure,
                            **({"thirdPartyName": p.third_party_name} if p.third_party_name else {}),
                        }
                        for p in svc.purposes
                    ],
                }
                for svc in services
            ],
            "sensitive": sensitive,
            "spiCat": [],
        }

        return receipt

    def generate_fingerprint(self, receipt: dict) -> str:
        """Generate a SHA-256 fingerprint of the receipt for integrity verification."""
        canonical = json.dumps(receipt, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


class ConsentReceiptValidator:
    """Validate consent receipts against Kantara specification."""

    def validate(self, receipt: dict) -> tuple[bool, list[str]]:
        """
        Validate a consent receipt against required fields.

        Returns (is_valid, list_of_errors).
        """
        errors = []

        # Check required fields
        for field_name in REQUIRED_FIELDS:
            if field_name not in receipt:
                errors.append(f"Missing required field: {field_name}")

        # Validate version
        if receipt.get("version") and not receipt["version"].startswith("KI-CR"):
            errors.append(f"Invalid version format: {receipt['version']}")

        # Validate controllers
        controllers = receipt.get("piiControllers", [])
        if not controllers:
            errors.append("At least one PII controller is required")
        for ctrl in controllers:
            if "piiController" not in ctrl:
                errors.append("Controller missing 'piiController' name")
            if "email" not in ctrl:
                errors.append("Controller missing 'email'")

        # Validate services and purposes
        services = receipt.get("services", [])
        if not services:
            errors.append("At least one service is required")
        for svc in services:
            if "service" not in svc:
                errors.append("Service missing 'service' name")
            purposes = svc.get("purposes", [])
            if not purposes:
                errors.append(f"Service '{svc.get('service', 'unknown')}' has no purposes")
            for p in purposes:
                if "purpose" not in p:
                    errors.append("Purpose missing 'purpose' description")
                if "consentType" not in p:
                    errors.append("Purpose missing 'consentType'")
                elif p["consentType"] not in ("explicit", "implicit"):
                    errors.append(f"Invalid consentType: {p['consentType']}")

        return (len(errors) == 0, errors)


class ReceiptLifecycleManager:
    """Manage consent receipt state transitions."""

    def __init__(self):
        self.receipts: dict[str, dict] = {}
        self.statuses: dict[str, ReceiptStatus] = {}

    def store(self, receipt: dict):
        rid = receipt["consentReceiptID"]
        self.receipts[rid] = receipt
        self.statuses[rid] = ReceiptStatus.ISSUED

    def activate(self, receipt_id: str) -> bool:
        if self.statuses.get(receipt_id) == ReceiptStatus.ISSUED:
            self.statuses[receipt_id] = ReceiptStatus.ACTIVE
            return True
        return False

    def withdraw(self, receipt_id: str) -> bool:
        if self.statuses.get(receipt_id) in (ReceiptStatus.ACTIVE, ReceiptStatus.ISSUED):
            self.statuses[receipt_id] = ReceiptStatus.WITHDRAWN
            return True
        return False

    def get_status(self, receipt_id: str) -> Optional[str]:
        status = self.statuses.get(receipt_id)
        return status.value if status else None

    def get_active_receipts(self, principal_id: str) -> list[dict]:
        active = []
        for rid, receipt in self.receipts.items():
            if (receipt.get("piiPrincipalId") == principal_id
                    and self.statuses.get(rid) == ReceiptStatus.ACTIVE):
                active.append(receipt)
        return active


if __name__ == "__main__":
    controller = Controller(
        name="Cipher Engineering Labs",
        contact="Data Protection Officer",
        email="dpo@cipherengineeringlabs.com",
        address={
            "streetAddress": "100 Technology Drive",
            "locality": "London",
            "postalCode": "EC2A 1NT",
            "country": "GB",
        },
        url="https://www.cipherengineeringlabs.com",
    )

    generator = ConsentReceiptGenerator(controller)

    services = [
        Service(
            service="Privacy Analytics Platform",
            purposes=[
                Purpose(
                    "Provide personalized compliance recommendations",
                    ["core_service"], ConsentType.EXPLICIT,
                    ["contact_information", "professional_information"],
                    True, "Account settings > Withdraw consent", False,
                ),
                Purpose(
                    "Send product updates",
                    ["marketing"], ConsentType.EXPLICIT,
                    ["contact_information"],
                    False, "Unsubscribe link in email", False,
                ),
            ],
        )
    ]

    receipt = generator.generate(
        "user-98765", services, "EU", "web_form",
        "https://www.cipherengineeringlabs.com/privacy",
    )

    validator = ConsentReceiptValidator()
    valid, errors = validator.validate(receipt)
    print(f"Valid: {valid}, Errors: {errors}")
    print(json.dumps(receipt, indent=2))
