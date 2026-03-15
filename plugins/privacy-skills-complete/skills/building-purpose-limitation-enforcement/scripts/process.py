#!/usr/bin/env python3
"""
Purpose Limitation Enforcement Engine

Implements GDPR Article 5(1)(b) purpose limitation with purpose-tagged
data stores, Article 6(4) compatibility assessment, and purpose-based
access control enforcement.
"""

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from enum import Enum
from typing import Optional


class LawfulBasis(Enum):
    CONSENT = "Article 6(1)(a)"
    CONTRACT = "Article 6(1)(b)"
    LEGAL_OBLIGATION = "Article 6(1)(c)"
    VITAL_INTERESTS = "Article 6(1)(d)"
    PUBLIC_INTEREST = "Article 6(1)(e)"
    LEGITIMATE_INTEREST = "Article 6(1)(f)"


class CompatibilityResult(Enum):
    COMPATIBLE = "compatible"
    CONDITIONAL = "conditionally_compatible"
    LIKELY_INCOMPATIBLE = "likely_incompatible"
    INCOMPATIBLE = "incompatible"


@dataclass
class ProcessingPurpose:
    """A registered processing purpose per Article 5(1)(b)."""
    purpose_id: str
    name: str
    description: str
    lawful_basis: LawfulBasis
    data_categories: list[str]
    controller: str
    retention_period_days: int
    retention_trigger: str
    compatible_purposes: list[str] = field(default_factory=list)
    incompatible_purposes: list[str] = field(default_factory=list)
    special_categories: bool = False
    created_date: str = ""
    last_reviewed: str = ""
    review_cadence_days: int = 180
    owner: str = ""
    dpo_approved: bool = False


@dataclass
class CompatibilityFactor:
    """One of the five Article 6(4) compatibility assessment factors."""
    name: str
    article_ref: str
    score: int  # 1-5
    justification: str


@dataclass
class CompatibilityAssessment:
    """Article 6(4) compatibility assessment between two purposes."""
    original_purpose_id: str
    proposed_purpose_id: str
    assessor: str
    assessment_date: str
    factors: list[CompatibilityFactor] = field(default_factory=list)
    conditions: list[str] = field(default_factory=list)
    review_date: str = ""

    @property
    def total_score(self) -> int:
        return sum(f.score for f in self.factors)

    @property
    def result(self) -> CompatibilityResult:
        score = self.total_score
        if score >= 20:
            return CompatibilityResult.COMPATIBLE
        elif score >= 15:
            return CompatibilityResult.CONDITIONAL
        elif score >= 10:
            return CompatibilityResult.LIKELY_INCOMPATIBLE
        else:
            return CompatibilityResult.INCOMPATIBLE

    @property
    def result_description(self) -> str:
        result = self.result
        if result == CompatibilityResult.COMPATIBLE:
            return "Compatible — approve with standard documentation"
        elif result == CompatibilityResult.CONDITIONAL:
            return "Conditionally compatible — approve with additional safeguards"
        elif result == CompatibilityResult.LIKELY_INCOMPATIBLE:
            return "Likely incompatible — requires DPO escalation and DPIA consideration"
        else:
            return "Incompatible — denied, new lawful basis or separate consent required"


class PurposeRegistry:
    """Central registry of all processing purposes."""

    def __init__(self, organization: str = "Prism Data Systems AG"):
        self.organization = organization
        self.purposes: dict[str, ProcessingPurpose] = {}
        self.assessments: list[CompatibilityAssessment] = []

    def register_purpose(self, purpose: ProcessingPurpose) -> None:
        self.purposes[purpose.purpose_id] = purpose

    def get_purpose(self, purpose_id: str) -> Optional[ProcessingPurpose]:
        return self.purposes.get(purpose_id)

    def is_compatible(self, source_id: str, target_id: str) -> bool:
        source = self.purposes.get(source_id)
        if source is None:
            return False
        return target_id in source.compatible_purposes

    def is_incompatible(self, source_id: str, target_id: str) -> bool:
        source = self.purposes.get(source_id)
        if source is None:
            return True
        return target_id in source.incompatible_purposes


class AccessDecisionEngine:
    """Purpose-based access control enforcement."""

    def __init__(self, registry: PurposeRegistry):
        self.registry = registry
        self.role_purpose_matrix: dict[str, list[str]] = {}
        self.audit_log: list[dict] = []

    def configure_role(self, role: str, authorized_purposes: list[str]) -> None:
        self.role_purpose_matrix[role] = authorized_purposes

    def evaluate_access(self, requester_role: str, declared_purpose: str,
                        data_purpose_tags: list[str], action: str,
                        requester_id: str) -> dict:
        """
        Evaluate whether an access request is authorized under purpose limitation.

        Args:
            requester_role: The role of the requesting service or user.
            declared_purpose: The purpose declared by the requester.
            data_purpose_tags: Purpose tags attached to the data record.
            action: The requested action (read, write).
            requester_id: Identifier of the requester for audit purposes.

        Returns:
            Access decision with rationale.
        """
        # Check 1: Is the declared purpose registered?
        purpose = self.registry.get_purpose(declared_purpose)
        if purpose is None:
            decision = self._deny("Declared purpose is not registered in the purpose registry")
            self._log(requester_id, requester_role, declared_purpose, data_purpose_tags, action, decision)
            return decision

        # Check 2: Is the role authorized for this purpose?
        authorized = self.role_purpose_matrix.get(requester_role, [])
        if declared_purpose not in authorized:
            decision = self._deny(f"Role '{requester_role}' is not authorized for purpose '{declared_purpose}'")
            self._log(requester_id, requester_role, declared_purpose, data_purpose_tags, action, decision)
            return decision

        # Check 3: Does the data's purpose tag match the declared purpose?
        if declared_purpose in data_purpose_tags:
            decision = self._allow("Direct purpose match — data tag matches declared purpose")
            self._log(requester_id, requester_role, declared_purpose, data_purpose_tags, action, decision)
            return decision

        # Check 4: Is there a registered compatibility relationship?
        for tag in data_purpose_tags:
            if self.registry.is_compatible(tag, declared_purpose):
                decision = self._allow(
                    f"Cross-purpose access allowed — '{tag}' is registered as compatible with '{declared_purpose}'"
                )
                self._log(requester_id, requester_role, declared_purpose, data_purpose_tags, action, decision)
                return decision

        # Check 5: Explicit incompatibility
        for tag in data_purpose_tags:
            if self.registry.is_incompatible(tag, declared_purpose):
                decision = self._deny(
                    f"Cross-purpose access denied — '{tag}' is registered as incompatible with '{declared_purpose}'"
                )
                self._log(requester_id, requester_role, declared_purpose, data_purpose_tags, action, decision)
                return decision

        # Default: deny unassessed cross-purpose access
        decision = self._deny(
            "Cross-purpose access denied — no compatibility assessment exists. "
            "Submit an Article 6(4) compatibility assessment request."
        )
        self._log(requester_id, requester_role, declared_purpose, data_purpose_tags, action, decision)
        return decision

    def _allow(self, reason: str) -> dict:
        return {"decision": "ALLOW", "reason": reason}

    def _deny(self, reason: str) -> dict:
        return {"decision": "DENY", "reason": reason}

    def _log(self, requester_id: str, role: str, purpose: str,
             data_tags: list[str], action: str, decision: dict) -> None:
        self.audit_log.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "requester_id": requester_id,
            "requester_role": role,
            "declared_purpose": purpose,
            "data_purpose_tags": data_tags,
            "action": action,
            "decision": decision["decision"],
            "reason": decision["reason"],
        })


def conduct_compatibility_assessment(
    original_id: str,
    proposed_id: str,
    assessor: str,
    link_score: int,
    link_justification: str,
    context_score: int,
    context_justification: str,
    nature_score: int,
    nature_justification: str,
    consequences_score: int,
    consequences_justification: str,
    safeguards_score: int,
    safeguards_justification: str,
) -> CompatibilityAssessment:
    """Conduct a full Article 6(4) compatibility assessment."""
    assessment = CompatibilityAssessment(
        original_purpose_id=original_id,
        proposed_purpose_id=proposed_id,
        assessor=assessor,
        assessment_date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        review_date=(datetime.now(timezone.utc) + timedelta(days=365)).strftime("%Y-%m-%d"),
    )

    assessment.factors = [
        CompatibilityFactor("Link between purposes", "Art. 6(4)(a)", link_score, link_justification),
        CompatibilityFactor("Context of collection", "Art. 6(4)(b)", context_score, context_justification),
        CompatibilityFactor("Nature of data", "Art. 6(4)(c)", nature_score, nature_justification),
        CompatibilityFactor("Consequences", "Art. 6(4)(d)", consequences_score, consequences_justification),
        CompatibilityFactor("Safeguards", "Art. 6(4)(e)", safeguards_score, safeguards_justification),
    ]

    if assessment.result == CompatibilityResult.CONDITIONAL:
        assessment.conditions = [
            "Data must be pseudonymized before cross-purpose processing",
            "Access must be logged with purpose context in audit trail",
            "Reassessment required within 12 months",
        ]

    return assessment


def run_example():
    """Demonstrate purpose limitation enforcement for Prism Data Systems AG."""

    # Set up purpose registry
    registry = PurposeRegistry()

    registry.register_purpose(ProcessingPurpose(
        purpose_id="PRP-ONBRD-001",
        name="Customer onboarding",
        description="Collection and processing of personal data for account creation and identity verification",
        lawful_basis=LawfulBasis.CONTRACT,
        data_categories=["email", "display_name", "country_code"],
        controller="Prism Data Systems AG",
        retention_period_days=2555,
        retention_trigger="account_closure",
        compatible_purposes=["PRP-SUPRT-001", "PRP-SECUR-001"],
        incompatible_purposes=["PRP-MARKET-001"],
        created_date="2025-06-01",
        last_reviewed="2026-01-15",
        owner="product_team",
        dpo_approved=True,
    ))

    registry.register_purpose(ProcessingPurpose(
        purpose_id="PRP-SUPRT-001",
        name="Customer support",
        description="Processing personal data to respond to customer support requests and resolve issues",
        lawful_basis=LawfulBasis.CONTRACT,
        data_categories=["email", "display_name", "support_ticket_history"],
        controller="Prism Data Systems AG",
        retention_period_days=1095,
        retention_trigger="ticket_closure",
        compatible_purposes=["PRP-ONBRD-001"],
        created_date="2025-06-01",
        last_reviewed="2026-01-15",
        owner="support_team",
        dpo_approved=True,
    ))

    registry.register_purpose(ProcessingPurpose(
        purpose_id="PRP-MARKET-001",
        name="Direct marketing",
        description="Sending promotional communications about Prism Data Systems AG products and services",
        lawful_basis=LawfulBasis.CONSENT,
        data_categories=["email", "display_name", "marketing_preferences"],
        controller="Prism Data Systems AG",
        retention_period_days=730,
        retention_trigger="consent_withdrawal",
        incompatible_purposes=["PRP-ONBRD-001"],
        created_date="2025-06-01",
        last_reviewed="2026-01-15",
        owner="marketing_team",
        dpo_approved=True,
    ))

    registry.register_purpose(ProcessingPurpose(
        purpose_id="PRP-SECUR-001",
        name="Security monitoring",
        description="Processing personal data for fraud detection and security incident investigation",
        lawful_basis=LawfulBasis.LEGITIMATE_INTEREST,
        data_categories=["ip_address", "user_agent", "login_events"],
        controller="Prism Data Systems AG",
        retention_period_days=365,
        retention_trigger="rolling_window",
        compatible_purposes=["PRP-ONBRD-001", "PRP-SUPRT-001"],
        created_date="2025-06-01",
        last_reviewed="2026-01-15",
        owner="security_team",
        dpo_approved=True,
    ))

    # Set up access control engine
    engine = AccessDecisionEngine(registry)
    engine.configure_role("onboarding_service", ["PRP-ONBRD-001"])
    engine.configure_role("support_agent", ["PRP-SUPRT-001", "PRP-ONBRD-001"])
    engine.configure_role("marketing_automation", ["PRP-MARKET-001"])
    engine.configure_role("security_ops", ["PRP-SECUR-001", "PRP-ONBRD-001", "PRP-SUPRT-001"])

    print("=== Purpose Limitation Enforcement Demo ===")
    print(f"Organization: {registry.organization}")
    print(f"Registered Purposes: {len(registry.purposes)}")
    print()

    # Test scenarios
    scenarios = [
        {
            "desc": "Support agent accessing onboarding data (compatible)",
            "role": "support_agent",
            "purpose": "PRP-SUPRT-001",
            "tags": ["PRP-ONBRD-001"],
            "action": "read",
            "requester": "agent_mueller",
        },
        {
            "desc": "Marketing accessing onboarding data (incompatible)",
            "role": "marketing_automation",
            "purpose": "PRP-MARKET-001",
            "tags": ["PRP-ONBRD-001"],
            "action": "read",
            "requester": "marketing_svc_01",
        },
        {
            "desc": "Onboarding service writing with correct purpose",
            "role": "onboarding_service",
            "purpose": "PRP-ONBRD-001",
            "tags": ["PRP-ONBRD-001"],
            "action": "write",
            "requester": "onboarding_svc_01",
        },
        {
            "desc": "Security ops accessing support data (compatible)",
            "role": "security_ops",
            "purpose": "PRP-SECUR-001",
            "tags": ["PRP-SUPRT-001"],
            "action": "read",
            "requester": "secops_analyst_01",
        },
        {
            "desc": "Unauthorized role accessing security data",
            "role": "onboarding_service",
            "purpose": "PRP-SECUR-001",
            "tags": ["PRP-SECUR-001"],
            "action": "read",
            "requester": "onboarding_svc_01",
        },
    ]

    for s in scenarios:
        result = engine.evaluate_access(
            requester_role=s["role"],
            declared_purpose=s["purpose"],
            data_purpose_tags=s["tags"],
            action=s["action"],
            requester_id=s["requester"],
        )
        print(f"Scenario: {s['desc']}")
        print(f"  Decision: {result['decision']}")
        print(f"  Reason: {result['reason']}")
        print()

    # Compatibility assessment example
    print("=== Article 6(4) Compatibility Assessment ===")
    assessment = conduct_compatibility_assessment(
        original_id="PRP-ONBRD-001",
        proposed_id="PRP-ANALYT-001",
        assessor="Dr. Lukas Meier (DPO)",
        link_score=4,
        link_justification="Product analytics directly informs improvements to the onboarding experience that benefits customers",
        context_score=3,
        context_justification="Customers expect their usage data may inform product improvements but may not expect detailed behavioral analysis",
        nature_score=5,
        nature_justification="Data categories are non-sensitive: pseudonymized user ID, feature events, session duration",
        consequences_score=4,
        consequences_justification="Minimal consequences as data is pseudonymized; no individual-level decisions made from analytics",
        safeguards_score=4,
        safeguards_justification="HMAC-SHA256 pseudonymization applied at ingestion boundary; analytics team cannot access raw identifiers",
    )

    print(f"Original Purpose: {assessment.original_purpose_id}")
    print(f"Proposed Purpose: {assessment.proposed_purpose_id}")
    print(f"Assessor: {assessment.assessor}")
    print(f"Assessment Date: {assessment.assessment_date}")
    print()
    for f in assessment.factors:
        print(f"  {f.name} ({f.article_ref}): {f.score}/5")
        print(f"    {f.justification}")
    print()
    print(f"Total Score: {assessment.total_score}/25")
    print(f"Result: {assessment.result_description}")
    if assessment.conditions:
        print("Conditions:")
        for c in assessment.conditions:
            print(f"  - {c}")

    print()
    print(f"=== Audit Log ({len(engine.audit_log)} entries) ===")
    for entry in engine.audit_log:
        print(f"  [{entry['timestamp']}] {entry['requester_id']} ({entry['requester_role']}) "
              f"-> {entry['decision']} ({entry['declared_purpose']})")


if __name__ == "__main__":
    run_example()
