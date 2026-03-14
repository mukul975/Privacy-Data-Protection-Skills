---
name: purpose-based-access
description: >-
  Design and implement Purpose-Based Access Control (PBAC) architecture including
  purpose ontology definition, policy engine configuration, audit logging of
  purpose verification at query time, and integration with existing IAM systems.
  Enforces GDPR Article 5(1)(b) purpose limitation technically.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-engineering
  tags: "purpose-based-access-control, pbac, purpose-limitation, access-policy-engine, privacy-engineering"
---

# Purpose-Based Access Control (PBAC) Architecture

## Overview

Purpose-Based Access Control (PBAC) extends traditional access control models (RBAC, ABAC) by adding purpose as a mandatory dimension in every access decision. Under PBAC, data access is granted only when the requester can demonstrate a valid, pre-authorized purpose that aligns with the basis under which the data was collected. This directly implements GDPR Article 5(1)(b) purpose limitation, CCPA purpose restrictions, and similar requirements across global privacy regulations.

## PBAC vs Traditional Access Control

| Dimension | RBAC | ABAC | PBAC |
|-----------|------|------|------|
| Access decision based on | Role membership | Attributes (user, resource, environment) | Purpose + attributes |
| Answers the question | "Who can access?" | "Under what conditions?" | "Why is this access needed?" |
| Purpose enforcement | None (implicit) | Possible as attribute | Core requirement |
| Audit trail | Who accessed what | Who, what, when, where | Who, what, when, where, WHY |
| Privacy alignment | Low | Medium | High |
| Consent integration | None | Possible | Native |

## Purpose Ontology

### Purpose Hierarchy

```
Root Purpose
├── Service Delivery
│   ├── Order Fulfillment
│   │   ├── Payment Processing
│   │   ├── Shipping Logistics
│   │   └── Order Confirmation
│   ├── Account Management
│   │   ├── Account Creation
│   │   ├── Account Maintenance
│   │   └── Account Recovery
│   └── Customer Support
│       ├── Ticket Resolution
│       └── Escalation Handling
├── Legal Compliance
│   ├── Regulatory Reporting
│   │   ├── Tax Reporting
│   │   ├── AML Compliance
│   │   └── Regulatory Audit
│   ├── Data Subject Rights
│   │   ├── Access Request
│   │   ├── Deletion Request
│   │   ├── Portability Request
│   │   └── Rectification Request
│   └── Litigation Hold
├── Analytics
│   ├── Product Analytics
│   │   ├── Feature Usage Analysis
│   │   └── UX Research
│   ├── Business Intelligence
│   │   ├── Revenue Reporting
│   │   └── Forecasting
│   └── Aggregate Reporting
│       ├── Board Reporting
│       └── Investor Reporting
├── Marketing
│   ├── Direct Marketing
│   │   ├── Email Campaigns
│   │   └── Personalized Offers
│   ├── Market Research
│   │   └── Survey Analysis
│   └── Advertising
│       ├── Audience Segmentation
│       └── Campaign Measurement
└── Security
    ├── Fraud Detection
    ├── Incident Investigation
    └── Access Auditing
```

### Purpose Definition Schema

```python
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime


class LegalBasis(Enum):
    CONSENT = "consent"
    CONTRACT = "contract"
    LEGAL_OBLIGATION = "legal_obligation"
    VITAL_INTEREST = "vital_interest"
    PUBLIC_INTEREST = "public_interest"
    LEGITIMATE_INTEREST = "legitimate_interest"


class PurposeStatus(Enum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    PENDING_APPROVAL = "pending_approval"


@dataclass
class Purpose:
    purpose_id: str
    name: str
    description: str
    parent_purpose_id: str | None
    legal_bases: list[LegalBasis]
    data_categories_allowed: list[str]
    retention_period_days: int
    requires_consent: bool
    status: PurposeStatus
    owner: str
    created_date: datetime
    review_date: datetime
    jurisdictions: list[str] = field(default_factory=lambda: ["global"])
    compatible_purposes: list[str] = field(default_factory=list)
    incompatible_purposes: list[str] = field(default_factory=list)
```

## Policy Engine Architecture

### System Design

```
Access Request
    |
    v
+-------------------+
| Request Parser    |
| - Identity (who)  |
| - Resource (what) |
| - Action (how)    |
| - Purpose (why)   |
| - Context (when/  |
|   where)          |
+-------------------+
    |
    v
+-------------------+     +--------------------+
| Purpose Validator |---->| Purpose Registry   |
| - Purpose exists  |     | - Ontology tree    |
| - Purpose active  |     | - Legal bases      |
| - Purpose applies |     | - Data categories  |
|   to data category|     +--------------------+
+-------------------+
    |
    v
+-------------------+     +--------------------+
| Consent Checker   |---->| Consent Store      |
| - Consent exists  |     | - Data subject     |
| - Consent active  |     |   preferences      |
| - Scope matches   |     | - Consent records  |
+-------------------+     +--------------------+
    |
    v
+-------------------+     +--------------------+
| ABAC Policy       |---->| Policy Repository  |
| Evaluator         |     | - XACML policies   |
| - Role check      |     | - Purpose-data     |
| - Attribute check  |     |   mappings        |
| - Environment check|     +--------------------+
+-------------------+
    |
    v
+-------------------+
| Decision Engine   |
| - PERMIT / DENY   |
| - Obligations     |
| - Advice          |
+-------------------+
    |
    +------+-------+
    |              |
    v              v
PERMIT          DENY
+ Audit Log     + Audit Log
+ Obligations   + Denial Reason
```

### Policy Engine Implementation

```python
"""
Purpose-Based Access Control policy engine.
Evaluates access requests against purpose definitions,
consent records, and attribute-based policies.
"""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class Decision(Enum):
    PERMIT = "PERMIT"
    DENY = "DENY"


@dataclass
class AccessRequest:
    requester_id: str
    requester_roles: list[str]
    resource_id: str
    data_category: str
    action: str  # read, write, delete, export
    purpose_id: str
    data_subject_id: Optional[str]
    timestamp: datetime
    source_ip: str
    justification: str


@dataclass
class AccessDecision:
    decision: Decision
    reason: str
    obligations: list[str]
    request: AccessRequest
    evaluated_at: datetime
    policy_version: str


class PurposeBasedAccessController:
    """
    Core PBAC engine that evaluates access requests against
    purpose definitions, consent records, and organizational policies.
    """

    def __init__(
        self,
        purpose_registry,
        consent_store,
        policy_repository,
        audit_logger
    ):
        self.purpose_registry = purpose_registry
        self.consent_store = consent_store
        self.policy_repository = policy_repository
        self.audit_logger = audit_logger

    def evaluate(self, request: AccessRequest) -> AccessDecision:
        """
        Evaluate an access request through the PBAC pipeline.

        Pipeline stages:
        1. Purpose validation
        2. Consent verification
        3. Attribute-based policy evaluation
        4. Decision with obligations
        """
        now = datetime.utcnow()

        # Stage 1: Validate purpose
        purpose = self.purpose_registry.get_purpose(request.purpose_id)
        if purpose is None:
            return self._deny(request, "Purpose not found in registry", now)

        if purpose.status != PurposeStatus.ACTIVE:
            return self._deny(request, f"Purpose is {purpose.status.value}", now)

        if request.data_category not in purpose.data_categories_allowed:
            return self._deny(
                request,
                f"Data category '{request.data_category}' not allowed for purpose '{purpose.name}'",
                now
            )

        # Stage 2: Verify consent (if required)
        if purpose.requires_consent and request.data_subject_id:
            consent = self.consent_store.get_active_consent(
                data_subject_id=request.data_subject_id,
                purpose_id=request.purpose_id
            )
            if consent is None:
                return self._deny(
                    request,
                    f"No active consent for purpose '{purpose.name}' from data subject",
                    now
                )

        # Stage 3: Evaluate attribute-based policies
        policy_result = self.policy_repository.evaluate(
            roles=request.requester_roles,
            resource=request.resource_id,
            action=request.action,
            purpose=request.purpose_id,
            data_category=request.data_category,
            context={"source_ip": request.source_ip, "time": now}
        )

        if not policy_result.permitted:
            return self._deny(request, policy_result.denial_reason, now)

        # Stage 4: Permit with obligations
        obligations = self._determine_obligations(purpose, request)
        decision = AccessDecision(
            decision=Decision.PERMIT,
            reason=f"Access permitted for purpose '{purpose.name}'",
            obligations=obligations,
            request=request,
            evaluated_at=now,
            policy_version=self.policy_repository.version
        )

        self.audit_logger.log_access_decision(decision)
        return decision

    def _deny(
        self, request: AccessRequest, reason: str, timestamp: datetime
    ) -> AccessDecision:
        """Create a DENY decision and log it."""
        decision = AccessDecision(
            decision=Decision.DENY,
            reason=reason,
            obligations=[],
            request=request,
            evaluated_at=timestamp,
            policy_version=self.policy_repository.version
        )
        self.audit_logger.log_access_decision(decision)
        return decision

    def _determine_obligations(self, purpose, request: AccessRequest) -> list[str]:
        """Determine post-access obligations based on purpose and context."""
        obligations = []

        if request.action == "export":
            obligations.append("LOG_DATA_EXPORT")
            obligations.append("APPLY_ENCRYPTION_TO_EXPORT")

        if request.action == "read" and request.data_category in [
            "health_data", "financial_data", "biometric_data"
        ]:
            obligations.append("MASK_SENSITIVE_FIELDS")

        obligations.append(f"ENFORCE_RETENTION_{purpose.retention_period_days}_DAYS")
        obligations.append("LOG_PURPOSE_USAGE")

        return obligations
```

## Purpose Verification at Query Time

### SQL Proxy with Purpose Enforcement

```python
"""
SQL proxy that intercepts database queries and enforces
purpose-based access control at the query level.
"""

import re
from datetime import datetime


class PurposeAwareSQLProxy:
    """
    Intercepts SQL queries, validates purpose, and rewrites
    queries to enforce data category restrictions.
    """

    def __init__(self, pbac_controller, column_category_map: dict):
        self.pbac = pbac_controller
        self.column_category_map = column_category_map

    def execute_query(
        self,
        sql: str,
        requester_id: str,
        requester_roles: list[str],
        purpose_id: str,
        justification: str
    ) -> tuple[bool, object]:
        """
        Execute a SQL query with purpose verification.

        Returns (success, result_or_error).
        """
        # Parse referenced columns/tables from SQL
        referenced_columns = self._extract_columns(sql)
        referenced_categories = set()

        for col in referenced_columns:
            category = self.column_category_map.get(col, "general")
            referenced_categories.add(category)

        # Validate access for each data category
        denied_categories = []
        for category in referenced_categories:
            request = AccessRequest(
                requester_id=requester_id,
                requester_roles=requester_roles,
                resource_id="database",
                data_category=category,
                action="read",
                purpose_id=purpose_id,
                data_subject_id=None,
                timestamp=datetime.utcnow(),
                source_ip="internal",
                justification=justification
            )

            decision = self.pbac.evaluate(request)
            if decision.decision == Decision.DENY:
                denied_categories.append((category, decision.reason))

        if denied_categories:
            reasons = "; ".join(
                f"{cat}: {reason}" for cat, reason in denied_categories
            )
            return (False, f"Access denied for categories: {reasons}")

        # Rewrite query to mask unauthorized columns if needed
        rewritten_sql = self._apply_column_masking(sql, purpose_id)

        # Execute the rewritten query (actual DB execution would go here)
        return (True, rewritten_sql)

    def _extract_columns(self, sql: str) -> list[str]:
        """Extract column references from SQL (simplified parser)."""
        select_pattern = re.compile(
            r"SELECT\s+(.+?)\s+FROM", re.IGNORECASE | re.DOTALL
        )
        match = select_pattern.search(sql)
        if not match:
            return []

        columns_str = match.group(1)
        if columns_str.strip() == "*":
            return list(self.column_category_map.keys())

        columns = [
            col.strip().split(".")[-1].split(" ")[0]
            for col in columns_str.split(",")
        ]
        return columns

    def _apply_column_masking(self, sql: str, purpose_id: str) -> str:
        """Rewrite query to mask columns not needed for the given purpose."""
        return sql  # Production implementation would rewrite SELECT columns
```

## Audit Logging for PBAC

### Audit Record Schema

| Field | Type | Description |
|-------|------|-------------|
| audit_id | UUID | Unique audit record identifier |
| timestamp | DateTime | When the access decision was made |
| requester_id | String | Identity of the requester |
| requester_roles | Array[String] | Roles held by requester |
| resource_id | String | Resource being accessed |
| data_category | String | Category of data being accessed |
| action | String | Type of access (read/write/delete/export) |
| purpose_id | String | Stated purpose for access |
| purpose_name | String | Human-readable purpose name |
| decision | Enum | PERMIT or DENY |
| denial_reason | String | Reason for denial (if denied) |
| obligations | Array[String] | Post-access obligations applied |
| justification | String | Free-text justification from requester |
| policy_version | String | Version of policy used for decision |

## Integration with Existing IAM

### PBAC Overlay Architecture

```
Existing IAM (RBAC/ABAC)
    |
    v
+---------------------------+
| PBAC Middleware Layer      |
| (intercepts access calls) |
+---------------------------+
    |
    +-- Purpose verification
    +-- Consent validation
    +-- Data category mapping
    +-- Obligation enforcement
    +-- Enhanced audit logging
    |
    v
Resource (Database / API / File System)
```

## References

- Byun, J. and Li, N. "Purpose Based Access Control of Complex Data for Privacy Protection." ACM SACMAT, 2008.
- GDPR Article 5(1)(b) — Purpose Limitation Principle
- ISO/IEC 29101:2018 — Privacy Architecture Framework
- NIST SP 800-162 — Guide to Attribute Based Access Control Definition and Considerations
- Ni, Q. et al. "Privacy-Aware Role-Based Access Control." ACM TOPS, 2010.
