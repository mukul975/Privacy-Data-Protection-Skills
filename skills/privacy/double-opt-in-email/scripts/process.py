#!/usr/bin/env python3
"""
Double Opt-In Email Consent System

Implements ePrivacy Directive compliant double opt-in workflow
with token management, suppression list, and multi-jurisdiction compliance.
"""

import json
import hashlib
import secrets
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class SubscriptionStatus(Enum):
    PENDING = "pending_confirmation"
    CONFIRMED = "confirmed"
    UNSUBSCRIBED = "unsubscribed"
    BOUNCED = "bounced"
    EXPIRED = "expired"


class SuppressionReason(Enum):
    UNSUBSCRIBED = "unsubscribed"
    HARD_BOUNCE = "hard_bounce"
    SPAM_COMPLAINT = "spam_complaint"
    DSAR_ERASURE = "dsar_erasure"


@dataclass
class DOIRequest:
    """A double opt-in subscription request."""
    request_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    email: str = ""
    email_hash: str = ""
    token: str = ""
    token_expiry: str = ""
    status: str = SubscriptionStatus.PENDING.value
    purpose: str = "product_updates_newsletter"
    consent_text_version: str = ""
    initial_request: dict = field(default_factory=dict)
    confirmation: Optional[dict] = None
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class SuppressionEntry:
    """An entry in the email suppression list."""
    email_hash: str = ""
    reason: str = ""
    added_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    source: str = ""


class DoubleOptInSystem:
    """
    Manages the double opt-in email consent lifecycle.
    """

    def __init__(self):
        self.requests: dict[str, DOIRequest] = {}  # token -> request
        self.subscriptions: dict[str, DOIRequest] = {}  # email_hash -> confirmed request
        self.suppression_list: dict[str, SuppressionEntry] = {}  # email_hash -> entry
        self.consent_texts: dict[str, str] = {}

    def _hash_email(self, email: str) -> str:
        """Hash email for suppression list storage (data minimization)."""
        return hashlib.sha256(email.lower().strip().encode("utf-8")).hexdigest()

    def _generate_token(self) -> str:
        """Generate cryptographically random URL-safe token."""
        return secrets.token_urlsafe(32)

    def register_consent_text(self, text: str) -> str:
        """Register a consent text version."""
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        self.consent_texts[text_hash] = text
        return text_hash

    def is_suppressed(self, email: str) -> bool:
        """Check if an email is on the suppression list."""
        return self._hash_email(email) in self.suppression_list

    def is_confirmed(self, email: str) -> bool:
        """Check if an email has an active subscription."""
        return self._hash_email(email) in self.subscriptions

    def create_doi_request(
        self,
        email: str,
        ip_address: str,
        user_agent: str,
        consent_text_version: str,
    ) -> dict:
        """
        Create a new double opt-in request (Step 1).

        Returns:
            Result dictionary indicating success or failure reason.
        """
        email_hash = self._hash_email(email)

        # Check suppression list
        if email_hash in self.suppression_list:
            return {
                "success": False,
                "reason": "suppressed",
                "user_message": "Please check your email for a confirmation link.",
                "internal_note": "Email is on suppression list. No confirmation sent.",
            }

        # Check if already confirmed
        if email_hash in self.subscriptions:
            return {
                "success": False,
                "reason": "already_subscribed",
                "user_message": "You're already subscribed!",
            }

        # Check for pending request (rate limiting)
        for req in self.requests.values():
            if req.email_hash == email_hash and req.status == SubscriptionStatus.PENDING.value:
                expiry = datetime.fromisoformat(req.token_expiry)
                if expiry > datetime.now(timezone.utc):
                    return {
                        "success": False,
                        "reason": "pending_exists",
                        "user_message": "Please check your email for a confirmation link.",
                        "internal_note": "Pending DOI request already exists.",
                    }

        # Create new DOI request
        token = self._generate_token()
        expiry = (datetime.now(timezone.utc) + timedelta(hours=48)).isoformat()

        request = DOIRequest(
            email=email,
            email_hash=email_hash,
            token=token,
            token_expiry=expiry,
            consent_text_version=consent_text_version,
            initial_request={
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "ip_address": ip_address,
                "user_agent": user_agent,
            },
        )

        self.requests[token] = request

        return {
            "success": True,
            "token": token,
            "confirmation_url": f"https://app.cloudvault-saas.eu/newsletter/confirm?token={token}",
            "expiry": expiry,
            "user_message": "Please check your email for a confirmation link.",
        }

    def confirm_subscription(
        self,
        token: str,
        ip_address: str,
        user_agent: str,
    ) -> dict:
        """
        Confirm a subscription via token click (Step 2).

        Returns:
            Result dictionary.
        """
        request = self.requests.get(token)

        if not request:
            return {"success": False, "reason": "invalid_token"}

        if request.status == SubscriptionStatus.CONFIRMED.value:
            return {"success": False, "reason": "already_confirmed"}

        expiry = datetime.fromisoformat(request.token_expiry)
        if datetime.now(timezone.utc) > expiry:
            request.status = SubscriptionStatus.EXPIRED.value
            return {"success": False, "reason": "token_expired"}

        # Confirm subscription
        request.status = SubscriptionStatus.CONFIRMED.value
        request.confirmation = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "ip_address": ip_address,
            "user_agent": user_agent,
        }

        # Remove from suppression list if re-subscribing
        if request.email_hash in self.suppression_list:
            del self.suppression_list[request.email_hash]

        self.subscriptions[request.email_hash] = request

        return {
            "success": True,
            "email": request.email,
            "consent_record": {
                "initial_request": request.initial_request,
                "confirmation": request.confirmation,
                "consent_text_version": request.consent_text_version,
                "purpose": request.purpose,
            },
        }

    def unsubscribe(self, email: str, method: str = "one_click_rfc8058") -> dict:
        """
        Process an unsubscribe request.

        Args:
            email: Email address to unsubscribe.
            method: How the unsubscribe was initiated.

        Returns:
            Result dictionary.
        """
        email_hash = self._hash_email(email)

        # Remove from active subscriptions
        if email_hash in self.subscriptions:
            del self.subscriptions[email_hash]

        # Add to suppression list
        self.suppression_list[email_hash] = SuppressionEntry(
            email_hash=email_hash,
            reason=SuppressionReason.UNSUBSCRIBED.value,
            source=method,
        )

        return {
            "success": True,
            "action": "unsubscribed_and_suppressed",
            "method": method,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def get_consent_evidence(self, email: str) -> Optional[dict]:
        """
        Retrieve consent evidence for an email (for Art. 7(1) compliance).

        Returns:
            Full consent evidence if subscribed, None if not found.
        """
        email_hash = self._hash_email(email)
        request = self.subscriptions.get(email_hash)

        if not request:
            return None

        return {
            "email": request.email,
            "purpose": request.purpose,
            "initial_opt_in": request.initial_request,
            "doi_confirmation": request.confirmation,
            "consent_text_version": request.consent_text_version,
            "consent_text": self.consent_texts.get(request.consent_text_version, ""),
            "status": request.status,
        }


if __name__ == "__main__":
    system = DoubleOptInSystem()

    # Register consent text
    text_hash = system.register_consent_text(
        "I'd like to receive product updates, tips, and news from CloudVault SaaS Inc. "
        "Emails sent max 2 times per month. Unsubscribe anytime."
    )

    # Step 1: Create DOI request
    print("=== Step 1: Create DOI Request ===")
    result = system.create_doi_request(
        email="sarah.murphy@protonmail.com",
        ip_address="198.51.100.42",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        consent_text_version=text_hash,
    )
    print(json.dumps(result, indent=2))

    # Step 2: Confirm subscription
    print("\n=== Step 2: Confirm Subscription ===")
    confirm_result = system.confirm_subscription(
        token=result["token"],
        ip_address="198.51.100.42",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    )
    print(json.dumps(confirm_result, indent=2))

    # Retrieve consent evidence
    print("\n=== Consent Evidence (Art. 7(1)) ===")
    evidence = system.get_consent_evidence("sarah.murphy@protonmail.com")
    if evidence:
        print(f"Email: {evidence['email']}")
        print(f"Initial opt-in: {evidence['initial_opt_in']['timestamp']}")
        print(f"DOI confirmation: {evidence['doi_confirmation']['timestamp']}")

    # Unsubscribe
    print("\n=== Unsubscribe ===")
    unsub = system.unsubscribe("sarah.murphy@protonmail.com")
    print(json.dumps(unsub, indent=2))

    # Verify suppression
    print(f"\nIs suppressed: {system.is_suppressed('sarah.murphy@protonmail.com')}")
    print(f"Is confirmed: {system.is_confirmed('sarah.murphy@protonmail.com')}")
