---
name: consent-receipt-spec
description: >-
  Implement the Kantara Initiative consent receipt specification including
  machine-readable receipt structure, JWT-based verification mechanisms, receipt
  lifecycle management, and integration patterns for consent management
  platforms. Supports ISO/IEC 27560 consent record information structure.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-engineering
  tags: "consent-receipt, kantara-initiative, consent-management, jwt-verification, iso-27560"
---

# Kantara Initiative Consent Receipt Specification

## Overview

A consent receipt is a record of a consent transaction provided to the individual (data subject) as evidence that consent was given. The Kantara Initiative Consent Receipt Specification v1.1 defines a standard, machine-readable format that enables individuals to track and manage their consent across multiple organizations. This skill covers the implementation of consent receipts aligned with the Kantara specification and ISO/IEC 27560:2023.

## Consent Receipt Structure

### Core Fields (Kantara v1.1)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| version | String | Yes | Specification version (e.g., "KI-CR-v1.1.0") |
| jurisdiction | String | Yes | Legal jurisdiction (ISO 3166-1 alpha-2) |
| consentTimestamp | DateTime | Yes | UTC timestamp of consent grant |
| collectionMethod | String | Yes | How consent was collected (web form, verbal, paper) |
| consentReceiptID | UUID | Yes | Unique identifier for this receipt |
| publicKey | String | No | Public key for receipt verification |
| language | String | Yes | Language of the consent interaction (BCP 47) |
| piiPrincipalId | String | Yes | Identifier for the data subject |
| piiControllers | Array | Yes | List of data controllers |
| policyUrl | URL | Yes | Link to the privacy policy |
| services | Array | Yes | Services for which consent is given |
| sensitive | Boolean | Yes | Whether special category data is involved |
| spiCat | Array | No | Special categories of data processed |

### PII Controller Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| piiController | String | Yes | Name of the controller organization |
| onBehalf | Boolean | No | Whether acting on behalf of another controller |
| contact | String | Yes | Contact information for the controller |
| address | Object | Yes | Physical address of the controller |
| email | String | Yes | Contact email address |
| phone | String | No | Contact phone number |
| piiControllerUrl | URL | No | URL of the controller's website |

### Service Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| service | String | Yes | Name of the service |
| purposes | Array | Yes | List of processing purposes |

### Purpose Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| purpose | String | Yes | Description of the processing purpose |
| purposeCategory | Array | Yes | Category codes for the purpose |
| consentType | String | Yes | "explicit" or "implicit" |
| piiCategory | Array | Yes | Categories of PII processed |
| primaryPurpose | Boolean | Yes | Whether this is the primary purpose |
| termination | String | Yes | How consent can be withdrawn |
| thirdPartyDisclosure | Boolean | Yes | Whether data is shared with third parties |
| thirdPartyName | String | No | Name of third party (if applicable) |

## Machine-Readable Receipt Format

### JSON Consent Receipt

```json
{
  "version": "KI-CR-v1.1.0",
  "jurisdiction": "EU",
  "consentTimestamp": "2026-03-14T10:30:00.000Z",
  "collectionMethod": "web_form",
  "consentReceiptID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "language": "en",
  "piiPrincipalId": "user-98765",
  "piiControllers": [
    {
      "piiController": "Cipher Engineering Labs",
      "onBehalf": false,
      "contact": "Data Protection Officer",
      "address": {
        "streetAddress": "100 Technology Drive",
        "locality": "London",
        "region": "Greater London",
        "postalCode": "EC2A 1NT",
        "country": "GB"
      },
      "email": "dpo@cipherengineeringlabs.com",
      "phone": "+44-20-7946-0958",
      "piiControllerUrl": "https://www.cipherengineeringlabs.com"
    }
  ],
  "policyUrl": "https://www.cipherengineeringlabs.com/privacy-policy",
  "services": [
    {
      "service": "Privacy Analytics Platform",
      "purposes": [
        {
          "purpose": "Provide personalized privacy compliance recommendations",
          "purposeCategory": ["core_service"],
          "consentType": "explicit",
          "piiCategory": ["contact_information", "professional_information"],
          "primaryPurpose": true,
          "termination": "Account settings > Privacy > Withdraw consent",
          "thirdPartyDisclosure": false
        },
        {
          "purpose": "Send product updates and feature announcements",
          "purposeCategory": ["marketing"],
          "consentType": "explicit",
          "piiCategory": ["contact_information"],
          "primaryPurpose": false,
          "termination": "Unsubscribe link in email or Account settings",
          "thirdPartyDisclosure": false
        },
        {
          "purpose": "Aggregate usage analytics to improve platform features",
          "purposeCategory": ["analytics"],
          "consentType": "explicit",
          "piiCategory": ["usage_data", "device_information"],
          "primaryPurpose": false,
          "termination": "Account settings > Privacy > Analytics opt-out",
          "thirdPartyDisclosure": true,
          "thirdPartyName": "Cipher Analytics Processing Ltd"
        }
      ]
    }
  ],
  "sensitive": false,
  "spiCat": []
}
```

## JWT-Based Verification Mechanism

### Signed Consent Receipt Implementation

```python
"""
Consent receipt generation and verification using JWT (JSON Web Tokens).
Implements Kantara Initiative Consent Receipt Specification v1.1
with cryptographic verification.
"""

import json
import uuid
from datetime import datetime, timezone
from typing import Optional
import jwt  # PyJWT
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend


class ConsentReceiptIssuer:
    """
    Issue and sign consent receipts as JWTs.
    Uses RS256 (RSA with SHA-256) for signing.
    """

    def __init__(self, private_key_pem: bytes, issuer_name: str):
        """
        Args:
            private_key_pem: PEM-encoded RSA private key
            issuer_name: Name of the issuing organization
        """
        self.private_key = serialization.load_pem_private_key(
            private_key_pem, password=None, backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        self.issuer_name = issuer_name

    def issue_receipt(
        self,
        principal_id: str,
        services: list[dict],
        jurisdiction: str,
        collection_method: str,
        policy_url: str,
        sensitive: bool = False,
        language: str = "en",
        controller_info: dict = None
    ) -> tuple[str, str]:
        """
        Generate a signed consent receipt.

        Args:
            principal_id: Data subject identifier
            services: List of service/purpose objects
            jurisdiction: Legal jurisdiction code
            collection_method: How consent was collected
            policy_url: URL of the privacy policy
            sensitive: Whether special categories are involved
            language: Language of consent interaction
            controller_info: PII controller details

        Returns:
            Tuple of (receipt_id, signed_jwt_string)
        """
        receipt_id = str(uuid.uuid4())

        if controller_info is None:
            controller_info = {
                "piiController": self.issuer_name,
                "onBehalf": False,
                "contact": "Data Protection Officer",
                "email": f"dpo@{self.issuer_name.lower().replace(' ', '')}.com"
            }

        receipt_payload = {
            "version": "KI-CR-v1.1.0",
            "jurisdiction": jurisdiction,
            "consentTimestamp": datetime.now(timezone.utc).isoformat(),
            "collectionMethod": collection_method,
            "consentReceiptID": receipt_id,
            "language": language,
            "piiPrincipalId": principal_id,
            "piiControllers": [controller_info],
            "policyUrl": policy_url,
            "services": services,
            "sensitive": sensitive,
            "spiCat": [],
            # JWT standard claims
            "iss": self.issuer_name,
            "sub": principal_id,
            "iat": int(datetime.now(timezone.utc).timestamp()),
            "jti": receipt_id,
        }

        # Sign the receipt as a JWT
        signed_token = jwt.encode(
            receipt_payload,
            self.private_key,
            algorithm="RS256",
            headers={"kid": f"{self.issuer_name}-consent-key-1"}
        )

        return receipt_id, signed_token

    def get_public_key_pem(self) -> str:
        """Export the public key for verification by data subjects."""
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode("utf-8")


class ConsentReceiptVerifier:
    """
    Verify signed consent receipts.
    Used by data subjects or auditors to confirm receipt authenticity.
    """

    def __init__(self):
        self.trusted_keys: dict[str, bytes] = {}

    def register_issuer_key(self, issuer_name: str, public_key_pem: str):
        """Register a trusted issuer's public key."""
        self.trusted_keys[issuer_name] = public_key_pem.encode("utf-8")

    def verify_receipt(self, token: str) -> tuple[bool, Optional[dict], Optional[str]]:
        """
        Verify a signed consent receipt JWT.

        Returns:
            Tuple of (is_valid, decoded_payload_or_None, error_message_or_None)
        """
        try:
            # Decode without verification first to get the issuer
            unverified = jwt.decode(token, options={"verify_signature": False})
            issuer = unverified.get("iss")

            if issuer not in self.trusted_keys:
                return (False, None, f"Unknown issuer: {issuer}")

            public_key = serialization.load_pem_public_key(
                self.trusted_keys[issuer],
                backend=default_backend()
            )

            # Verify the signature
            decoded = jwt.decode(
                token,
                public_key,
                algorithms=["RS256"],
                issuer=issuer
            )

            # Validate required Kantara fields
            required_fields = [
                "version", "jurisdiction", "consentTimestamp",
                "collectionMethod", "consentReceiptID", "piiPrincipalId",
                "piiControllers", "policyUrl", "services", "sensitive"
            ]

            missing = [f for f in required_fields if f not in decoded]
            if missing:
                return (False, decoded, f"Missing required fields: {missing}")

            return (True, decoded, None)

        except jwt.ExpiredSignatureError:
            return (False, None, "Receipt JWT has expired")
        except jwt.InvalidSignatureError:
            return (False, None, "Invalid signature — receipt may have been tampered with")
        except jwt.DecodeError as e:
            return (False, None, f"Failed to decode JWT: {str(e)}")
```

## Receipt Lifecycle Management

### Lifecycle States

```
ISSUED --> ACTIVE --> WITHDRAWN
  |          |           |
  |          v           v
  |       UPDATED    ARCHIVED
  |          |
  v          v
EXPIRED   ACTIVE (new version)
```

### Lifecycle Manager

```python
"""
Manage the lifecycle of consent receipts including
updates, withdrawals, and expiration tracking.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum


class ReceiptStatus(Enum):
    ISSUED = "issued"
    ACTIVE = "active"
    UPDATED = "updated"
    WITHDRAWN = "withdrawn"
    EXPIRED = "expired"
    ARCHIVED = "archived"


@dataclass
class ReceiptRecord:
    receipt_id: str
    principal_id: str
    status: ReceiptStatus
    issued_at: datetime
    last_updated: datetime
    withdrawn_at: datetime | None
    jwt_token: str
    version: int
    superseded_by: str | None
    purposes: list[str]


class ConsentReceiptLifecycle:
    """
    Manage consent receipt state transitions and history.
    """

    def __init__(self, receipt_store, issuer: ConsentReceiptIssuer):
        self.store = receipt_store
        self.issuer = issuer

    def activate_receipt(self, receipt_id: str) -> bool:
        """Transition a receipt from ISSUED to ACTIVE."""
        record = self.store.get(receipt_id)
        if record and record.status == ReceiptStatus.ISSUED:
            record.status = ReceiptStatus.ACTIVE
            record.last_updated = datetime.now(timezone.utc)
            self.store.update(record)
            return True
        return False

    def update_receipt(
        self,
        receipt_id: str,
        updated_services: list[dict],
        jurisdiction: str,
        policy_url: str
    ) -> str | None:
        """
        Update an existing receipt by issuing a new version.
        The old receipt is marked as UPDATED and linked to the new one.

        Returns the new receipt ID or None if update failed.
        """
        old_record = self.store.get(receipt_id)
        if not old_record or old_record.status not in [
            ReceiptStatus.ACTIVE, ReceiptStatus.ISSUED
        ]:
            return None

        # Issue new receipt
        new_receipt_id, new_jwt = self.issuer.issue_receipt(
            principal_id=old_record.principal_id,
            services=updated_services,
            jurisdiction=jurisdiction,
            collection_method="consent_update",
            policy_url=policy_url
        )

        # Create new record
        new_record = ReceiptRecord(
            receipt_id=new_receipt_id,
            principal_id=old_record.principal_id,
            status=ReceiptStatus.ACTIVE,
            issued_at=datetime.now(timezone.utc),
            last_updated=datetime.now(timezone.utc),
            withdrawn_at=None,
            jwt_token=new_jwt,
            version=old_record.version + 1,
            superseded_by=None,
            purposes=[p["purpose"] for s in updated_services for p in s.get("purposes", [])]
        )
        self.store.save(new_record)

        # Mark old receipt as updated
        old_record.status = ReceiptStatus.UPDATED
        old_record.superseded_by = new_receipt_id
        old_record.last_updated = datetime.now(timezone.utc)
        self.store.update(old_record)

        return new_receipt_id

    def withdraw_consent(self, receipt_id: str, reason: str = "") -> bool:
        """
        Withdraw consent and mark the receipt accordingly.

        Returns True if withdrawal was successful.
        """
        record = self.store.get(receipt_id)
        if not record or record.status not in [
            ReceiptStatus.ACTIVE, ReceiptStatus.ISSUED
        ]:
            return False

        record.status = ReceiptStatus.WITHDRAWN
        record.withdrawn_at = datetime.now(timezone.utc)
        record.last_updated = datetime.now(timezone.utc)
        self.store.update(record)

        return True

    def get_active_receipts(self, principal_id: str) -> list[ReceiptRecord]:
        """Get all active consent receipts for a data subject."""
        return self.store.find_by_principal(
            principal_id, status=ReceiptStatus.ACTIVE
        )

    def get_receipt_history(self, principal_id: str) -> list[ReceiptRecord]:
        """Get the complete consent receipt history for a data subject."""
        return self.store.find_by_principal(principal_id)
```

## ISO/IEC 27560:2023 Alignment

| Kantara CR Field | ISO 27560 Equivalent | Notes |
|-----------------|---------------------|-------|
| consentReceiptID | Consent Record Identifier | Unique identifier for the record |
| consentTimestamp | Date and time of consent | When consent was collected |
| piiPrincipalId | PII Principal Identifier | Data subject identifier |
| piiControllers | PII Controller | Organization processing data |
| services.purposes | Purpose(s) | Processing purposes |
| services.purposes.piiCategory | PII Categories | Types of personal data |
| sensitive | Sensitive PII indicator | Special category flag |
| jurisdiction | Jurisdiction | Applicable legal framework |
| collectionMethod | Mechanism of consent | How consent was obtained |
| policyUrl | Privacy notice reference | Link to privacy notice |

## References

- Kantara Initiative Consent Receipt Specification v1.1.0 (2018)
- ISO/IEC 27560:2023 — Privacy Technologies — Consent Record Information Structure
- ISO/IEC 29184:2020 — Guidelines for Online Privacy Notices and Consent
- RFC 7519 — JSON Web Token (JWT)
- W3C Data Privacy Vocabularies and Controls Community Group
- IEEE P7012 — Standard for Machine Readable Personal Privacy Terms
