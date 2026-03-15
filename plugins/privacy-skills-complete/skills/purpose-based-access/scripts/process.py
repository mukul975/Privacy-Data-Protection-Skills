"""
Purpose-Based Access Control — Purpose Registry and Policy Evaluator

Implements purpose ontology management and access decision evaluation
for PBAC systems enforcing GDPR Article 5(1)(b) purpose limitation.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
import json
import uuid


class LegalBasis(Enum):
    CONSENT = "consent"
    CONTRACT = "contract"
    LEGAL_OBLIGATION = "legal_obligation"
    VITAL_INTEREST = "vital_interest"
    PUBLIC_INTEREST = "public_interest"
    LEGITIMATE_INTEREST = "legitimate_interest"


class Decision(Enum):
    PERMIT = "PERMIT"
    DENY = "DENY"


@dataclass
class Purpose:
    purpose_id: str
    name: str
    description: str
    parent_id: Optional[str]
    legal_bases: list[LegalBasis]
    allowed_data_categories: list[str]
    retention_days: int
    requires_consent: bool
    active: bool = True


@dataclass
class AccessRequest:
    requester_id: str
    roles: list[str]
    resource: str
    data_category: str
    action: str
    purpose_id: str
    justification: str


@dataclass
class AccessDecision:
    decision: Decision
    reason: str
    obligations: list[str]
    timestamp: str


class PurposeRegistry:
    """Manage the purpose ontology for PBAC."""

    def __init__(self):
        self.purposes: dict[str, Purpose] = {}

    def register_purpose(self, purpose: Purpose):
        self.purposes[purpose.purpose_id] = purpose

    def get_purpose(self, purpose_id: str) -> Optional[Purpose]:
        return self.purposes.get(purpose_id)

    def get_children(self, parent_id: str) -> list[Purpose]:
        return [p for p in self.purposes.values() if p.parent_id == parent_id]

    def is_data_category_allowed(self, purpose_id: str, data_category: str) -> bool:
        purpose = self.get_purpose(purpose_id)
        if not purpose:
            return False
        return data_category in purpose.allowed_data_categories

    def export_ontology(self) -> dict:
        tree = {}
        roots = [p for p in self.purposes.values() if p.parent_id is None]
        for root in roots:
            tree[root.purpose_id] = self._build_tree(root)
        return tree

    def _build_tree(self, purpose: Purpose) -> dict:
        children = self.get_children(purpose.purpose_id)
        return {
            "name": purpose.name,
            "legal_bases": [lb.value for lb in purpose.legal_bases],
            "data_categories": purpose.allowed_data_categories,
            "active": purpose.active,
            "children": {
                c.purpose_id: self._build_tree(c) for c in children
            },
        }


class PBACEvaluator:
    """Evaluate access requests against purpose-based policies."""

    ROLE_PURPOSE_MAPPING = {
        "customer_support": ["service_delivery.support", "service_delivery.account_mgmt"],
        "marketing_analyst": ["marketing.analytics", "marketing.segmentation"],
        "data_engineer": ["analytics.product", "analytics.bi"],
        "legal_counsel": ["legal.compliance", "legal.dsr"],
        "privacy_officer": ["legal.compliance", "legal.dsr", "legal.audit"],
    }

    def __init__(self, registry: PurposeRegistry):
        self.registry = registry
        self.audit_log: list[dict] = []

    def evaluate(self, request: AccessRequest) -> AccessDecision:
        """Evaluate an access request through the PBAC pipeline."""
        now = datetime.now(timezone.utc).isoformat()

        # Stage 1: Validate purpose exists and is active
        purpose = self.registry.get_purpose(request.purpose_id)
        if not purpose:
            return self._log_decision(request, Decision.DENY, "Purpose not found", now)

        if not purpose.active:
            return self._log_decision(request, Decision.DENY, "Purpose is inactive", now)

        # Stage 2: Check data category alignment
        if not self.registry.is_data_category_allowed(request.purpose_id, request.data_category):
            return self._log_decision(
                request, Decision.DENY,
                f"Data category '{request.data_category}' not allowed for purpose '{purpose.name}'",
                now,
            )

        # Stage 3: Check role-purpose alignment
        allowed_purposes = []
        for role in request.roles:
            allowed_purposes.extend(self.ROLE_PURPOSE_MAPPING.get(role, []))

        if request.purpose_id not in allowed_purposes:
            return self._log_decision(
                request, Decision.DENY,
                f"Roles {request.roles} not authorized for purpose '{purpose.name}'",
                now,
            )

        # Stage 4: Grant with obligations
        obligations = [
            f"RETENTION_{purpose.retention_days}_DAYS",
            "LOG_ACCESS",
        ]
        if request.action == "export":
            obligations.append("ENCRYPT_EXPORT")
        if request.data_category in ("health_data", "financial_data"):
            obligations.append("MASK_SENSITIVE_FIELDS")

        return self._log_decision(
            request, Decision.PERMIT,
            f"Access granted for purpose '{purpose.name}'",
            now, obligations,
        )

    def _log_decision(
        self, request: AccessRequest, decision: Decision,
        reason: str, timestamp: str, obligations: list[str] = None,
    ) -> AccessDecision:
        entry = {
            "timestamp": timestamp,
            "requester": request.requester_id,
            "resource": request.resource,
            "data_category": request.data_category,
            "purpose": request.purpose_id,
            "decision": decision.value,
            "reason": reason,
        }
        self.audit_log.append(entry)

        return AccessDecision(
            decision=decision,
            reason=reason,
            obligations=obligations or [],
            timestamp=timestamp,
        )


if __name__ == "__main__":
    registry = PurposeRegistry()

    registry.register_purpose(Purpose(
        "service_delivery", "Service Delivery", "Core service purposes",
        None, [LegalBasis.CONTRACT], ["contact_info", "account_data"], 1095, False,
    ))
    registry.register_purpose(Purpose(
        "service_delivery.support", "Customer Support", "Resolve support tickets",
        "service_delivery", [LegalBasis.CONTRACT], ["contact_info", "account_data", "ticket_data"], 1095, False,
    ))
    registry.register_purpose(Purpose(
        "marketing.analytics", "Marketing Analytics", "Analyze marketing performance",
        None, [LegalBasis.CONSENT], ["usage_data", "marketing_data"], 730, True,
    ))

    evaluator = PBACEvaluator(registry)

    # Should permit
    result = evaluator.evaluate(AccessRequest(
        "user-001", ["customer_support"], "customer-db",
        "contact_info", "read", "service_delivery.support", "Resolving ticket #1234",
    ))
    print(f"Decision: {result.decision.value} — {result.reason}")

    # Should deny (wrong data category)
    result = evaluator.evaluate(AccessRequest(
        "user-002", ["marketing_analyst"], "customer-db",
        "financial_data", "read", "marketing.analytics", "Campaign analysis",
    ))
    print(f"Decision: {result.decision.value} — {result.reason}")
