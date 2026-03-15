"""
Retention Exception Management Process
Manages exception requests, approvals, monitoring, and auto-expiry.
"""

import json
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional


class ExceptionCategory(Enum):
    LEGAL_HOLD = "legal_hold"
    REGULATORY_REQUIREMENT = "regulatory_requirement"
    CONTRACTUAL_OBLIGATION = "contractual_obligation"
    ONGOING_DISPUTE = "ongoing_dispute"
    BUSINESS_CONTINUITY = "business_continuity"
    RESEARCH_STATISTICAL = "research_statistical"
    PUBLIC_INTEREST_ARCHIVING = "public_interest_archiving"


class ExceptionStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    APPROVED_WITH_CONDITIONS = "approved_with_conditions"
    REJECTED = "rejected"
    ACTIVE = "active"
    EXPIRED = "expired"
    RENEWED = "renewed"


# Maximum durations per exception category
MAX_DURATIONS = {
    ExceptionCategory.LEGAL_HOLD: None,  # Duration of proceedings + 6 months
    ExceptionCategory.REGULATORY_REQUIREMENT: 180,  # 6 months
    ExceptionCategory.CONTRACTUAL_OBLIGATION: None,  # Duration of obligation + limitation
    ExceptionCategory.ONGOING_DISPUTE: 365,  # 12 months, renewable
    ExceptionCategory.BUSINESS_CONTINUITY: 180,  # 6 months, non-renewable without reapplication
    ExceptionCategory.RESEARCH_STATISTICAL: None,  # Duration of project + 6 months
    ExceptionCategory.PUBLIC_INTEREST_ARCHIVING: None,  # Indefinite with annual review
}

# Approval authorities per exception category
APPROVAL_AUTHORITIES = {
    ExceptionCategory.LEGAL_HOLD: ["Legal Counsel"],
    ExceptionCategory.REGULATORY_REQUIREMENT: ["DPO", "Legal Counsel"],
    ExceptionCategory.CONTRACTUAL_OBLIGATION: ["Business Owner", "DPO"],
    ExceptionCategory.ONGOING_DISPUTE: ["DPO"],
    ExceptionCategory.BUSINESS_CONTINUITY: ["IT Director", "DPO"],
    ExceptionCategory.RESEARCH_STATISTICAL: ["DPO", "Research Lead"],
    ExceptionCategory.PUBLIC_INTEREST_ARCHIVING: ["DPO", "Board"],
}


class RetentionException:
    """Represents a retention exception with lifecycle management."""

    def __init__(
        self,
        reference: str,
        data_category: str,
        records_affected: int,
        original_deletion_date: str,
        requested_extension_days: int,
        category: ExceptionCategory,
        justification: str,
        requestor_name: str,
        requestor_department: str,
    ):
        self.reference = reference
        self.data_category = data_category
        self.records_affected = records_affected
        self.original_deletion_date = original_deletion_date
        self.requested_extension_days = requested_extension_days
        self.category = category
        self.justification = justification
        self.requestor_name = requestor_name
        self.requestor_department = requestor_department
        self.status = ExceptionStatus.PENDING
        self.created_at = datetime.utcnow()
        self.approved_at: Optional[datetime] = None
        self.extended_deletion_date: Optional[str] = None
        self.review_date: Optional[str] = None
        self.dpo_assessment: Optional[dict] = None
        self.approval_chain: list[dict] = []
        self.review_history: list[dict] = []
        self.conditions: list[str] = []

    def validate_duration(self) -> dict:
        """Validate the requested duration against maximum allowed."""
        max_days = MAX_DURATIONS.get(self.category)
        if max_days is None:
            return {"valid": True, "message": "No maximum duration for this category"}
        if self.requested_extension_days > max_days:
            return {
                "valid": False,
                "message": f"Requested {self.requested_extension_days} days exceeds maximum {max_days} days for {self.category.value}",
                "maximum_days": max_days,
            }
        return {"valid": True, "message": "Within maximum duration"}

    def assess(
        self,
        dpo_name: str,
        necessity: bool,
        proportionality: bool,
        legal_basis_valid: bool,
        risk_level: str,
        recommendation: str,
        notes: str,
    ) -> None:
        """Record DPO assessment."""
        self.dpo_assessment = {
            "dpo_name": dpo_name,
            "assessment_date": datetime.utcnow().isoformat(),
            "necessity_test": "PASS" if necessity else "FAIL",
            "proportionality_test": "PASS" if proportionality else "FAIL",
            "legal_basis_check": "PASS" if legal_basis_valid else "FAIL",
            "risk_to_data_subjects": risk_level,
            "recommendation": recommendation,
            "notes": notes,
        }

    def approve(
        self, approver_name: str, approver_role: str, conditions: Optional[list[str]] = None
    ) -> None:
        """Approve the exception."""
        self.approval_chain.append({
            "approver": approver_name,
            "role": approver_role,
            "date": datetime.utcnow().isoformat(),
            "decision": "approved",
        })
        self.conditions = conditions or []
        self.status = ExceptionStatus.APPROVED_WITH_CONDITIONS if conditions else ExceptionStatus.APPROVED
        self.approved_at = datetime.utcnow()

        orig = datetime.fromisoformat(self.original_deletion_date)
        extended = orig + timedelta(days=self.requested_extension_days)
        self.extended_deletion_date = extended.strftime("%Y-%m-%d")

        review = self.approved_at + timedelta(days=min(self.requested_extension_days // 2, 180))
        self.review_date = review.strftime("%Y-%m-%d")
        self.status = ExceptionStatus.ACTIVE

    def reject(self, approver_name: str, approver_role: str, reason: str) -> None:
        """Reject the exception."""
        self.approval_chain.append({
            "approver": approver_name,
            "role": approver_role,
            "date": datetime.utcnow().isoformat(),
            "decision": "rejected",
            "reason": reason,
        })
        self.status = ExceptionStatus.REJECTED

    def review(self, reviewer: str, still_necessary: bool, scope_reducible: bool, notes: str) -> str:
        """Conduct periodic review. Returns the review outcome."""
        outcome = "renewed"
        if not still_necessary:
            outcome = "expired"
            self.status = ExceptionStatus.EXPIRED
        elif scope_reducible:
            outcome = "scope_reduced"

        self.review_history.append({
            "review_date": datetime.utcnow().isoformat(),
            "reviewer": reviewer,
            "still_necessary": still_necessary,
            "scope_reducible": scope_reducible,
            "outcome": outcome,
            "notes": notes,
        })

        if outcome != "expired":
            self.review_date = (datetime.utcnow() + timedelta(days=180)).strftime("%Y-%m-%d")

        return outcome

    def is_expired(self) -> bool:
        """Check if the exception has expired."""
        if self.extended_deletion_date:
            return datetime.utcnow() >= datetime.fromisoformat(self.extended_deletion_date)
        return False

    def to_dict(self) -> dict:
        return {
            "reference": self.reference,
            "data_category": self.data_category,
            "records_affected": self.records_affected,
            "original_deletion_date": self.original_deletion_date,
            "extended_deletion_date": self.extended_deletion_date,
            "requested_extension_days": self.requested_extension_days,
            "category": self.category.value,
            "justification": self.justification,
            "requestor": f"{self.requestor_name} ({self.requestor_department})",
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "review_date": self.review_date,
            "dpo_assessment": self.dpo_assessment,
            "approval_chain": self.approval_chain,
            "conditions": self.conditions,
            "review_history": self.review_history,
        }


def generate_quarterly_report(exceptions: list[RetentionException]) -> dict:
    """Generate quarterly exception report for Board."""
    active = [e for e in exceptions if e.status == ExceptionStatus.ACTIVE]
    total_records = sum(e.records_affected for e in active)

    category_breakdown = {}
    for e in active:
        cat = e.category.value
        category_breakdown[cat] = category_breakdown.get(cat, 0) + 1

    return {
        "report_date": datetime.utcnow().isoformat(),
        "organization": "Orion Data Vault Corp",
        "total_active_exceptions": len(active),
        "total_records_affected": total_records,
        "new_this_quarter": sum(1 for e in exceptions if e.status == ExceptionStatus.ACTIVE and e.created_at > datetime.utcnow() - timedelta(days=90)),
        "expired_this_quarter": sum(1 for e in exceptions if e.status == ExceptionStatus.EXPIRED),
        "rejected_this_quarter": sum(1 for e in exceptions if e.status == ExceptionStatus.REJECTED),
        "category_breakdown": category_breakdown,
        "approaching_max_duration": [e.reference for e in active if e.is_expired()],
    }


if __name__ == "__main__":
    exc = RetentionException(
        reference="RET-EXC-2026-0014",
        data_category="CAT-002",
        records_affected=85200,
        original_deletion_date="2026-03-01",
        requested_extension_days=180,
        category=ExceptionCategory.BUSINESS_CONTINUITY,
        justification="Data migration to new CRM system in progress. Migration estimated to complete by August 2026. Deletion before migration would result in data loss for active customer accounts.",
        requestor_name="IT Director",
        requestor_department="IT",
    )
    exc.assess("DPO", True, True, True, "Medium", "APPROVE", "Migration schedule confirmed with vendor.")
    exc.approve("IT Director", "IT Director")
    print(json.dumps(exc.to_dict(), indent=2))
