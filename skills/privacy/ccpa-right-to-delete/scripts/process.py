"""
CCPA/CPRA Right to Delete Process
Manages consumer deletion requests, verification, exceptions, and service provider flow-down.
"""

import json
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional


class RequestStatus(Enum):
    RECEIVED = "received"
    ACKNOWLEDGED = "acknowledged"
    VERIFYING = "verifying"
    VERIFIED = "verified"
    PROCESSING = "processing"
    COMPLETED = "completed"
    PARTIALLY_COMPLETED = "partially_completed"
    DENIED = "denied"
    APPEALED = "appealed"


class VerificationLevel(Enum):
    REASONABLE = "reasonable_degree_of_certainty"
    REASONABLY_HIGH = "reasonably_high_degree_of_certainty"


class CCPAException(Enum):
    COMPLETE_TRANSACTION = "d1_complete_transaction"
    SECURITY = "d2_security"
    DEBUG = "d3_debug"
    FREE_SPEECH = "d4_free_speech"
    RESEARCH = "d5_research"
    INTERNAL_USE_ALIGNED = "d6_internal_use_aligned"
    LEGAL_OBLIGATION = "d7_legal_obligation"
    INTERNAL_USE_LAWFUL = "d8_internal_use_lawful"
    COMPLY_LAW = "d9_comply_other_law"


EXCEPTION_DESCRIPTIONS = {
    CCPAException.COMPLETE_TRANSACTION: "Complete the transaction for which PI was collected; fulfill warranty; provide requested service",
    CCPAException.SECURITY: "Detect security incidents; protect against malicious, deceptive, fraudulent, or illegal activity",
    CCPAException.DEBUG: "Debug to identify and repair errors impairing existing intended functionality",
    CCPAException.FREE_SPEECH: "Exercise free speech or ensure another consumer's right to free speech",
    CCPAException.RESEARCH: "Engage in public/peer-reviewed research in the public interest",
    CCPAException.INTERNAL_USE_ALIGNED: "Solely internal uses reasonably aligned with consumer expectations",
    CCPAException.LEGAL_OBLIGATION: "Comply with a legal obligation",
    CCPAException.INTERNAL_USE_LAWFUL: "Lawful internal use compatible with context of information provided",
    CCPAException.COMPLY_LAW: "Comply with federal, state, or local laws",
}


class DeletionRequest:
    """Manages a CCPA consumer deletion request."""

    def __init__(
        self,
        consumer_reference: str,
        request_channel: str,
        has_account: bool,
        is_logged_in: bool = False,
    ):
        self.reference = f"DEL-CA-{datetime.utcnow().strftime('%Y')}-{hash(consumer_reference) % 10000:04d}"
        self.consumer_reference = consumer_reference
        self.request_channel = request_channel
        self.has_account = has_account
        self.is_logged_in = is_logged_in
        self.status = RequestStatus.RECEIVED
        self.received_date = datetime.utcnow()
        self.acknowledged_date: Optional[datetime] = None
        self.verified_date: Optional[datetime] = None
        self.completed_date: Optional[datetime] = None
        self.verification_level = VerificationLevel.REASONABLE
        self.verification_method: Optional[str] = None
        self.data_points_matched: int = 0
        self.pi_categories_found: list[str] = []
        self.categories_deleted: list[str] = []
        self.categories_retained: list[dict] = []
        self.service_provider_directives: list[dict] = []
        self.third_party_notifications: list[dict] = []
        self.timeline_extended = False
        self.extension_reason: Optional[str] = None

    def acknowledge(self) -> None:
        """Acknowledge receipt within 10 business days."""
        self.acknowledged_date = datetime.utcnow()
        self.status = RequestStatus.ACKNOWLEDGED

    def get_deadline(self) -> datetime:
        """Get the response deadline (45 or 90 days)."""
        base = self.verified_date or self.received_date
        days = 90 if self.timeline_extended else 45
        return base + timedelta(days=days)

    def extend_timeline(self, reason: str) -> None:
        """Extend the response timeline by 45 days (total 90)."""
        self.timeline_extended = True
        self.extension_reason = reason

    def verify_account_holder(self) -> None:
        """Verify identity for account holders (logged in)."""
        if self.has_account and self.is_logged_in:
            self.verification_method = "account_login"
            self.data_points_matched = 0  # Account login is sufficient
            self.verified_date = datetime.utcnow()
            self.status = RequestStatus.VERIFIED

    def verify_with_data_points(self, data_points_matched: int, signed_declaration: bool = False) -> dict:
        """Verify identity using data point matching."""
        required_points = 2
        if self.verification_level == VerificationLevel.REASONABLY_HIGH:
            required_points = 3

        self.data_points_matched = data_points_matched
        verified = data_points_matched >= required_points

        if self.verification_level == VerificationLevel.REASONABLY_HIGH and not signed_declaration:
            verified = False

        if verified:
            self.verified_date = datetime.utcnow()
            self.status = RequestStatus.VERIFIED
            self.verification_method = (
                f"{data_points_matched} data points matched"
                + (" + signed declaration" if signed_declaration else "")
            )

        return {
            "verified": verified,
            "data_points_matched": data_points_matched,
            "required_points": required_points,
            "signed_declaration": signed_declaration,
            "verification_level": self.verification_level.value,
        }

    def assess_exceptions(self, pi_category: str, exceptions: list[CCPAException]) -> dict:
        """Assess exceptions for a specific PI category."""
        applicable_exceptions = []
        for exc in exceptions:
            applicable_exceptions.append({
                "exception": exc.value,
                "description": EXCEPTION_DESCRIPTIONS[exc],
                "applies": True,
            })

        if applicable_exceptions:
            self.categories_retained.append({
                "category": pi_category,
                "exceptions": [e["exception"] for e in applicable_exceptions],
            })
        else:
            self.categories_deleted.append(pi_category)

        return {
            "pi_category": pi_category,
            "action": "retain" if applicable_exceptions else "delete",
            "exceptions": applicable_exceptions,
        }

    def direct_service_provider(
        self, provider_name: str, directed_date: Optional[str] = None
    ) -> None:
        """Direct a service provider to delete."""
        self.service_provider_directives.append({
            "provider_name": provider_name,
            "directed_date": directed_date or datetime.utcnow().isoformat(),
            "confirmed_date": None,
            "status": "directed",
        })

    def confirm_service_provider(self, provider_name: str) -> None:
        """Record service provider deletion confirmation."""
        for sp in self.service_provider_directives:
            if sp["provider_name"] == provider_name:
                sp["confirmed_date"] = datetime.utcnow().isoformat()
                sp["status"] = "confirmed"
                return

    def notify_third_party(self, third_party_name: str) -> None:
        """Notify a third party to whom PI was sold/shared."""
        self.third_party_notifications.append({
            "third_party_name": third_party_name,
            "notified_date": datetime.utcnow().isoformat(),
            "status": "notified",
        })

    def complete(self) -> None:
        """Complete the deletion request."""
        self.completed_date = datetime.utcnow()
        if self.categories_retained:
            self.status = RequestStatus.PARTIALLY_COMPLETED
        else:
            self.status = RequestStatus.COMPLETED

    def generate_response(self) -> dict:
        """Generate the consumer response."""
        return {
            "reference": self.reference,
            "organization": "Orion Data Vault Corp",
            "request_date": self.received_date.isoformat(),
            "verification_date": self.verified_date.isoformat() if self.verified_date else None,
            "response_date": datetime.utcnow().isoformat(),
            "status": self.status.value,
            "categories_deleted": self.categories_deleted,
            "categories_retained": self.categories_retained,
            "service_providers_directed": self.service_provider_directives,
            "third_parties_notified": self.third_party_notifications,
            "consumer_rights": {
                "appeal": "Contact privacy@oriondatavault.corp or call +1-888-555-0147",
                "cppa_complaint": "California Privacy Protection Agency — cppa.ca.gov",
                "other_rights": "Right to know, right to opt-out remain available",
            },
        }


def generate_ccpa_metrics(requests: list[DeletionRequest], quarter: str) -> dict:
    """Generate quarterly CCPA deletion request metrics."""
    total = len(requests)
    completed = sum(1 for r in requests if r.status in (RequestStatus.COMPLETED, RequestStatus.PARTIALLY_COMPLETED))
    denied = sum(1 for r in requests if r.status == RequestStatus.DENIED)
    extended = sum(1 for r in requests if r.timeline_extended)

    response_times = []
    for r in requests:
        if r.completed_date and r.verified_date:
            delta = (r.completed_date - r.verified_date).days
            response_times.append(delta)

    median_time = sorted(response_times)[len(response_times) // 2] if response_times else 0

    return {
        "quarter": quarter,
        "organization": "Orion Data Vault Corp",
        "requests_received": total,
        "requests_completed": completed,
        "requests_denied": denied,
        "requests_requiring_extension": extended,
        "median_response_days": median_time,
        "completion_within_45_days": sum(1 for t in response_times if t <= 45),
        "completion_rate_pct": round(completed / total * 100, 1) if total > 0 else 0,
    }


if __name__ == "__main__":
    request = DeletionRequest(
        consumer_reference="consumer-12345",
        request_channel="online_form",
        has_account=True,
        is_logged_in=True,
    )
    request.acknowledge()
    request.verify_account_holder()
    request.assess_exceptions("browsing_history", [])
    request.assess_exceptions("transaction_records", [CCPAException.LEGAL_OBLIGATION])
    request.direct_service_provider("Analytics SaaS Provider")
    request.complete()

    print(json.dumps(request.generate_response(), indent=2))
