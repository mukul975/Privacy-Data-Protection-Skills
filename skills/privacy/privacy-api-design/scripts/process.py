"""
Privacy API Design — API Route Definitions and Request Handlers

Provides reference implementation patterns for privacy API endpoints
including DSAR, consent, deletion, and audit APIs.
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Optional
import json
import uuid


class DSARType(Enum):
    ACCESS = "access"
    DELETION = "deletion"
    PORTABILITY = "portability"
    RECTIFICATION = "rectification"
    RESTRICTION = "restriction"
    OBJECTION = "objection"


class DSARStatus(Enum):
    PENDING = "pending"
    IDENTITY_VERIFICATION = "identity_verification"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    REJECTED = "rejected"


class AuditEventType(Enum):
    DATA_ACCESS = "data_access"
    CONSENT_CHANGE = "consent_change"
    DELETION = "deletion"
    DSAR_SUBMITTED = "dsar_submitted"
    DSAR_COMPLETED = "dsar_completed"
    BREACH_DETECTED = "breach_detected"


@dataclass
class DSARRequest:
    request_id: str
    request_type: DSARType
    subject_email: str
    status: DSARStatus
    submitted_at: datetime
    regulatory_deadline: datetime
    completed_at: Optional[datetime] = None
    details: str = ""
    data_categories: list[str] = field(default_factory=lambda: ["all"])


@dataclass
class ConsentPreference:
    purpose_id: str
    purpose_name: str
    granted: bool
    updated_at: datetime
    channels: list[str] = field(default_factory=list)


@dataclass
class AuditEvent:
    event_id: str
    event_type: AuditEventType
    timestamp: datetime
    actor_id: str
    actor_type: str
    subject_id: Optional[str]
    resource: str
    action: str
    outcome: str
    details: dict = field(default_factory=dict)


class DSARService:
    """Handle Data Subject Access Request operations."""

    DEADLINE_DAYS = {
        "EU": 30,
        "US_CA": 45,
        "US_CO": 45,
        "UK": 30,
        "BR": 15,
    }

    def __init__(self):
        self.requests: dict[str, DSARRequest] = {}
        self.audit_log: list[AuditEvent] = []

    def submit_request(
        self,
        request_type: DSARType,
        subject_email: str,
        jurisdiction: str = "EU",
        details: str = "",
        data_categories: list[str] = None,
    ) -> DSARRequest:
        """Submit a new DSAR request."""
        deadline_days = self.DEADLINE_DAYS.get(jurisdiction, 30)
        now = datetime.now(timezone.utc)

        request = DSARRequest(
            request_id=str(uuid.uuid4()),
            request_type=request_type,
            subject_email=subject_email,
            status=DSARStatus.PENDING,
            submitted_at=now,
            regulatory_deadline=now + timedelta(days=deadline_days),
            details=details,
            data_categories=data_categories or ["all"],
        )
        self.requests[request.request_id] = request

        self._log_event(
            AuditEventType.DSAR_SUBMITTED, "system", "system",
            subject_email, "dsar_service", "submit",
            "success", {"request_id": request.request_id, "type": request_type.value},
        )

        return request

    def get_request(self, request_id: str) -> Optional[DSARRequest]:
        return self.requests.get(request_id)

    def list_requests(
        self, subject_email: str, status: Optional[DSARStatus] = None
    ) -> list[DSARRequest]:
        results = [
            r for r in self.requests.values()
            if r.subject_email == subject_email
        ]
        if status:
            results = [r for r in results if r.status == status]
        return sorted(results, key=lambda r: r.submitted_at, reverse=True)

    def update_status(self, request_id: str, new_status: DSARStatus) -> bool:
        request = self.requests.get(request_id)
        if not request:
            return False

        request.status = new_status
        if new_status == DSARStatus.COMPLETED:
            request.completed_at = datetime.now(timezone.utc)
            self._log_event(
                AuditEventType.DSAR_COMPLETED, "system", "system",
                request.subject_email, "dsar_service", "complete",
                "success", {"request_id": request_id},
            )
        return True

    def _log_event(self, event_type, actor_id, actor_type, subject_id,
                   resource, action, outcome, details):
        self.audit_log.append(AuditEvent(
            event_id=str(uuid.uuid4()),
            event_type=event_type,
            timestamp=datetime.now(timezone.utc),
            actor_id=actor_id,
            actor_type=actor_type,
            subject_id=subject_id,
            resource=resource,
            action=action,
            outcome=outcome,
            details=details,
        ))

    def to_api_response(self, request: DSARRequest) -> dict:
        """Convert a DSAR request to API response format."""
        return {
            "requestId": request.request_id,
            "requestType": request.request_type.value,
            "status": request.status.value,
            "submittedAt": request.submitted_at.isoformat(),
            "regulatoryDeadline": request.regulatory_deadline.isoformat(),
            "completedAt": request.completed_at.isoformat() if request.completed_at else None,
            "dataCategories": request.data_categories,
        }


class ConsentService:
    """Handle consent preference management."""

    def __init__(self):
        self.preferences: dict[str, list[ConsentPreference]] = {}

    def get_preferences(self, subject_id: str) -> list[ConsentPreference]:
        return self.preferences.get(subject_id, [])

    def update_preferences(
        self, subject_id: str, updates: list[dict]
    ) -> list[ConsentPreference]:
        """Update consent preferences for a data subject."""
        current = {p.purpose_id: p for p in self.preferences.get(subject_id, [])}
        now = datetime.now(timezone.utc)

        for update in updates:
            purpose_id = update["purpose_id"]
            if purpose_id in current:
                current[purpose_id].granted = update["granted"]
                current[purpose_id].updated_at = now
                current[purpose_id].channels = update.get("channels", [])
            else:
                current[purpose_id] = ConsentPreference(
                    purpose_id=purpose_id,
                    purpose_name=update.get("purpose_name", purpose_id),
                    granted=update["granted"],
                    updated_at=now,
                    channels=update.get("channels", []),
                )

        self.preferences[subject_id] = list(current.values())
        return self.preferences[subject_id]


class PrivacyAPIRouter:
    """Define privacy API route structure and generate OpenAPI-style documentation."""

    ROUTES = {
        "DSAR": [
            {"method": "POST", "path": "/privacy/v1/dsar/requests", "description": "Submit new DSAR"},
            {"method": "GET", "path": "/privacy/v1/dsar/requests", "description": "List own DSARs"},
            {"method": "GET", "path": "/privacy/v1/dsar/requests/{id}", "description": "Get DSAR status"},
            {"method": "GET", "path": "/privacy/v1/dsar/requests/{id}/download", "description": "Download data package"},
        ],
        "Consent": [
            {"method": "GET", "path": "/privacy/v1/consent/preferences", "description": "Get consent preferences"},
            {"method": "PUT", "path": "/privacy/v1/consent/preferences", "description": "Update preferences"},
            {"method": "GET", "path": "/privacy/v1/consent/purposes", "description": "List available purposes"},
            {"method": "GET", "path": "/privacy/v1/consent/receipts/{id}", "description": "Get consent receipt"},
        ],
        "Deletion": [
            {"method": "POST", "path": "/privacy/v1/deletion/requests", "description": "Submit deletion request"},
            {"method": "GET", "path": "/privacy/v1/deletion/requests/{id}", "description": "Get deletion status"},
            {"method": "POST", "path": "/privacy/v1/deletion/requests/{id}/verify", "description": "Verify deletion"},
        ],
        "Audit": [
            {"method": "GET", "path": "/privacy/v1/audit/events", "description": "Query audit events"},
            {"method": "GET", "path": "/privacy/v1/audit/reports/compliance", "description": "Generate compliance report"},
        ],
    }

    def generate_route_summary(self) -> dict:
        """Generate API route summary for documentation."""
        total_routes = sum(len(routes) for routes in self.ROUTES.values())
        return {
            "api_version": "v1",
            "base_url": "/privacy/v1",
            "total_endpoints": total_routes,
            "categories": {
                category: {
                    "endpoints": len(routes),
                    "routes": routes,
                }
                for category, routes in self.ROUTES.items()
            },
        }


if __name__ == "__main__":
    # DSAR Service demo
    dsar_svc = DSARService()

    request = dsar_svc.submit_request(
        DSARType.ACCESS, "user@cipherengineeringlabs.com", "EU",
        "I want a copy of all my personal data",
        ["profile", "transactions", "communications"],
    )
    print("=== DSAR Submitted ===")
    print(json.dumps(dsar_svc.to_api_response(request), indent=2))

    # Consent Service demo
    consent_svc = ConsentService()
    prefs = consent_svc.update_preferences("user-001", [
        {"purpose_id": "marketing.email", "purpose_name": "Email Marketing", "granted": True, "channels": ["email"]},
        {"purpose_id": "analytics.product", "purpose_name": "Product Analytics", "granted": False},
    ])
    print("\n=== Consent Updated ===")
    for p in prefs:
        print(f"  {p.purpose_name}: {'granted' if p.granted else 'denied'}")

    # API Route Summary
    router = PrivacyAPIRouter()
    summary = router.generate_route_summary()
    print(f"\n=== API Summary: {summary['total_endpoints']} endpoints ===")
    print(json.dumps(summary, indent=2))
