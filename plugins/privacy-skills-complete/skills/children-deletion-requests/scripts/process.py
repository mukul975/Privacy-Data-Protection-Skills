#!/usr/bin/env python3
"""
Children's Data Deletion Request Management Tool

Manages deletion requests for children's personal data under GDPR Art. 17,
COPPA Section 312.6, and UK AADC Standard 15.
"""

import json
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional

DELETION_SCOPE = {
    "account_data": {"default_include": True, "exception": None},
    "activity_logs": {"default_include": True, "exception": None},
    "content_created": {"default_include": True, "exception": "offer_download_first"},
    "communications": {"default_include": True, "exception": "safeguarding_investigation"},
    "consent_records": {"default_include": False, "exception": "legal_compliance_6_years"},
    "financial_records": {"default_include": False, "exception": "tax_accounting_obligation"},
    "safety_logs": {"default_include": False, "exception": "active_investigation"},
    "backup_copies": {"default_include": True, "exception": "scheduled_purge_30_days"},
}

ART_17_3_EXCEPTIONS = [
    {"ground": "17(3)(a)", "description": "Freedom of expression and information", "applies_to_children": "rarely"},
    {"ground": "17(3)(b)", "description": "Legal obligation requiring processing", "applies_to_children": "sometimes"},
    {"ground": "17(3)(c)", "description": "Public health reasons", "applies_to_children": "sometimes"},
    {"ground": "17(3)(d)", "description": "Archiving in public interest / research", "applies_to_children": "sometimes"},
    {"ground": "17(3)(e)", "description": "Legal claims", "applies_to_children": "sometimes"},
]


@dataclass
class DeletionRequest:
    """Represents a children's data deletion request."""

    reference: str
    child_identifier: str
    requester_identifier: str
    requester_type: str  # "parent", "child", "former_child", "school"
    request_date: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    scope: str = "full_account"  # "full_account" or "partial"
    partial_categories: list[str] = field(default_factory=list)
    verification_status: str = "pending"  # "pending", "verified", "failed"
    verification_method: Optional[str] = None
    deletion_status: str = "received"
    deadline: str = field(
        default_factory=lambda: (
            datetime.now(timezone.utc) + timedelta(days=30)
        ).isoformat()
    )
    exceptions_applied: list[dict] = field(default_factory=list)
    third_party_notifications: list[dict] = field(default_factory=list)
    completion_date: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)


def determine_requester_authority(
    requester_type: str,
    child_age: int,
    country_code: str,
) -> dict:
    """
    Determine whether the requester has authority to request deletion.

    Returns authority assessment.
    """
    thresholds = {
        "GB": 13, "FR": 15, "DE": 16, "BE": 13, "ES": 14, "IT": 14, "NL": 16,
    }
    threshold = thresholds.get(country_code.upper(), 16)

    if requester_type == "parent":
        if child_age < threshold:
            return {
                "authorised": True,
                "reason": f"Parent holds consent authority for child aged {child_age} (threshold: {threshold})",
            }
        else:
            return {
                "authorised": True,
                "reason": "Parent can request deletion on behalf of child (Art. 17(1)(f))",
                "note": "Child above threshold may also request independently",
            }

    elif requester_type == "child":
        if child_age >= threshold:
            return {
                "authorised": True,
                "reason": f"Child aged {child_age} is above threshold ({threshold}); can request independently",
            }
        else:
            return {
                "authorised": False,
                "reason": f"Child aged {child_age} is below threshold ({threshold}); parent must submit request",
                "guidance": "Redirect child to parent and provide instructions for parental request",
            }

    elif requester_type == "former_child":
        return {
            "authorised": True,
            "reason": "Art. 17(1)(f) applies to data collected from a child regardless of current age",
        }

    elif requester_type == "school":
        return {
            "authorised": True,
            "reason": "School authority under FERPA / contractual agreement",
        }

    return {"authorised": False, "reason": f"Unknown requester type: {requester_type}"}


def calculate_deletion_scope(
    scope_type: str,
    exceptions: list[str] | None = None,
) -> dict:
    """
    Calculate what data should be deleted and what should be retained.

    Args:
        scope_type: "full_account" or "partial".
        exceptions: List of active exception grounds (e.g., ["safeguarding_investigation"]).

    Returns:
        Scope determination with deletion and retention lists.
    """
    if exceptions is None:
        exceptions = []

    to_delete = []
    to_retain = []

    for category, config in DELETION_SCOPE.items():
        if scope_type == "full_account" and config["default_include"]:
            if config["exception"] and config["exception"] in exceptions:
                to_retain.append({
                    "category": category,
                    "reason": config["exception"],
                })
            else:
                to_delete.append({"category": category})
        elif not config["default_include"]:
            to_retain.append({
                "category": category,
                "reason": config["exception"] or "legal_retention",
            })

    return {
        "scope_type": scope_type,
        "to_delete": to_delete,
        "to_retain": to_retain,
        "delete_count": len(to_delete),
        "retain_count": len(to_retain),
    }


def process_deletion_request(request: DeletionRequest) -> dict:
    """
    Process a deletion request through the workflow stages.

    Returns processing result with timeline.
    """
    stages = []

    # Stage 1: Acknowledgement
    stages.append({
        "stage": "acknowledgement",
        "status": "completed",
        "action": "Acknowledgement sent to requester",
        "deadline": (datetime.fromisoformat(request.request_date) + timedelta(hours=48)).isoformat(),
    })

    # Stage 2: Verification
    stages.append({
        "stage": "verification",
        "status": request.verification_status,
        "action": f"Identity verified via {request.verification_method or 'pending'}",
        "deadline": (datetime.fromisoformat(request.request_date) + timedelta(days=5)).isoformat(),
    })

    # Stage 3: Scope determination
    scope = calculate_deletion_scope(request.scope)
    stages.append({
        "stage": "scope_determination",
        "status": "completed" if request.verification_status == "verified" else "pending",
        "action": f"Delete {scope['delete_count']} categories, retain {scope['retain_count']}",
    })

    # Stage 4: Primary deletion
    stages.append({
        "stage": "primary_deletion",
        "status": request.deletion_status,
        "action": "Delete from all primary systems",
        "deadline": request.deadline,
    })

    # Stage 5: Third-party notification
    stages.append({
        "stage": "third_party_notification",
        "status": "pending" if not request.third_party_notifications else "completed",
        "action": f"Notify {len(request.third_party_notifications)} third parties",
    })

    # Stage 6: Backup purge
    backup_deadline = (
        datetime.fromisoformat(request.deadline) + timedelta(days=30)
    ).isoformat()
    stages.append({
        "stage": "backup_purge",
        "status": "scheduled",
        "action": "Purge from backup systems",
        "deadline": backup_deadline,
    })

    # Stage 7: Confirmation
    stages.append({
        "stage": "confirmation",
        "status": "pending",
        "action": "Send deletion confirmation to requester",
    })

    return {
        "reference": request.reference,
        "stages": stages,
        "overall_deadline": request.deadline,
        "backup_purge_deadline": backup_deadline,
    }


if __name__ == "__main__":
    print("=== Requester Authority Assessment ===")
    cases = [
        ("parent", 10, "FR"),
        ("child", 14, "BE"),
        ("child", 14, "DE"),
        ("former_child", 22, "GB"),
    ]

    for rtype, age, country in cases:
        result = determine_requester_authority(rtype, age, country)
        auth = "AUTHORISED" if result["authorised"] else "NOT AUTHORISED"
        print(f"  {rtype} (age {age}, {country}): {auth} — {result['reason']}")

    print("\n=== Deletion Scope Calculation ===")
    scope = calculate_deletion_scope("full_account", ["safeguarding_investigation"])
    print(f"  Delete: {scope['delete_count']} categories")
    for item in scope["to_delete"]:
        print(f"    - {item['category']}")
    print(f"  Retain: {scope['retain_count']} categories")
    for item in scope["to_retain"]:
        print(f"    - {item['category']} ({item['reason']})")

    print("\n=== Deletion Request Processing ===")
    request = DeletionRequest(
        reference="DEL-CHILD-2026-0284",
        child_identifier="child_bp_8f3a2d",
        requester_identifier="parent_bp_c7e4f1",
        requester_type="parent",
        verification_status="verified",
        verification_method="account_credentials",
        deletion_status="in_progress",
    )

    result = process_deletion_request(request)
    print(f"  Reference: {result['reference']}")
    print(f"  Deadline: {result['overall_deadline']}")
    for stage in result["stages"]:
        print(f"    {stage['stage']}: {stage['status']}")
