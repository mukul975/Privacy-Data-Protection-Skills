"""
Litigation Hold Management Process
Manages legal hold lifecycle: issuance, tracking, monitoring, and release.
"""

import json
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional


class HoldStatus(Enum):
    ACTIVE = "active"
    RELEASED = "released"
    EXPIRED = "expired"


class TriggerCategory(Enum):
    LITIGATION_FILED = "litigation_filed"
    LITIGATION_ANTICIPATED = "litigation_anticipated"
    REGULATORY_INVESTIGATION = "regulatory_investigation"
    INTERNAL_INVESTIGATION = "internal_investigation"
    DPA_INQUIRY = "dpa_inquiry"
    TAX_AUDIT = "tax_audit"
    EMPLOYMENT_DISPUTE = "employment_dispute"


class CustodianAcknowledgement(Enum):
    PENDING = "pending"
    ACKNOWLEDGED = "acknowledged"
    OVERDUE = "overdue"


class LitigationHold:
    """Represents a litigation hold with full lifecycle management."""

    def __init__(
        self,
        hold_reference: str,
        matter_description: str,
        legal_counsel: str,
        trigger_category: TriggerCategory,
        date_range_start: str,
        date_range_end: Optional[str] = None,
        data_categories: Optional[list[str]] = None,
        systems_in_scope: Optional[list[str]] = None,
    ):
        self.hold_reference = hold_reference
        self.matter_description = matter_description
        self.legal_counsel = legal_counsel
        self.trigger_category = trigger_category
        self.date_range_start = date_range_start
        self.date_range_end = date_range_end or "ongoing"
        self.data_categories = data_categories or []
        self.systems_in_scope = systems_in_scope or []
        self.status = HoldStatus.ACTIVE
        self.issued_date = datetime.utcnow()
        self.released_date: Optional[datetime] = None
        self.next_review_date = self.issued_date + timedelta(days=90)
        self.custodians: list[dict] = []
        self.queued_erasure_requests: list[str] = []
        self.review_history: list[dict] = []

    def add_custodian(self, name: str, title: str, department: str) -> None:
        """Add a custodian to the hold."""
        self.custodians.append({
            "name": name,
            "title": title,
            "department": department,
            "notified_date": datetime.utcnow().isoformat(),
            "acknowledgement": CustodianAcknowledgement.PENDING.value,
            "acknowledged_date": None,
        })

    def acknowledge_custodian(self, name: str) -> None:
        """Record custodian acknowledgement."""
        for custodian in self.custodians:
            if custodian["name"] == name:
                custodian["acknowledgement"] = CustodianAcknowledgement.ACKNOWLEDGED.value
                custodian["acknowledged_date"] = datetime.utcnow().isoformat()
                return
        raise ValueError(f"Custodian not found: {name}")

    def check_overdue_acknowledgements(self, deadline_hours: int = 48) -> list[dict]:
        """Check for custodians who have not acknowledged within the deadline."""
        overdue = []
        deadline = timedelta(hours=deadline_hours)
        for custodian in self.custodians:
            if custodian["acknowledgement"] == CustodianAcknowledgement.PENDING.value:
                notified = datetime.fromisoformat(custodian["notified_date"])
                if datetime.utcnow() - notified > deadline:
                    custodian["acknowledgement"] = CustodianAcknowledgement.OVERDUE.value
                    overdue.append(custodian)
        return overdue

    def queue_erasure_request(self, request_reference: str) -> None:
        """Queue an Art. 17 erasure request for processing after hold release."""
        self.queued_erasure_requests.append(request_reference)

    def record_review(self, reviewer: str, outcome: str, notes: str) -> None:
        """Record a periodic review of the hold."""
        self.review_history.append({
            "review_date": datetime.utcnow().isoformat(),
            "reviewer": reviewer,
            "outcome": outcome,
            "notes": notes,
        })
        self.next_review_date = datetime.utcnow() + timedelta(days=90)

    def release(self, authorized_by: str, reason: str) -> dict:
        """Release the litigation hold."""
        self.status = HoldStatus.RELEASED
        self.released_date = datetime.utcnow()

        release_record = {
            "hold_reference": self.hold_reference,
            "released_date": self.released_date.isoformat(),
            "authorized_by": authorized_by,
            "reason": reason,
            "queued_erasure_requests": self.queued_erasure_requests,
            "actions_required": [
                "Remove technical holds from all in-scope systems",
                "Re-enable automated deletion for affected data categories",
                "Process queued erasure requests",
                "Assess whether retained data has exceeded retention period",
                "Notify DPO to resume normal retention schedule",
            ],
        }
        return release_record

    def is_review_due(self) -> bool:
        """Check if the hold is due for review."""
        return datetime.utcnow() >= self.next_review_date

    def to_dict(self) -> dict:
        return {
            "hold_reference": self.hold_reference,
            "matter_description": self.matter_description,
            "legal_counsel": self.legal_counsel,
            "trigger_category": self.trigger_category.value,
            "status": self.status.value,
            "issued_date": self.issued_date.isoformat(),
            "released_date": self.released_date.isoformat() if self.released_date else None,
            "date_range": f"{self.date_range_start} to {self.date_range_end}",
            "data_categories": self.data_categories,
            "systems_in_scope": self.systems_in_scope,
            "custodians": self.custodians,
            "next_review_date": self.next_review_date.isoformat(),
            "queued_erasure_requests": self.queued_erasure_requests,
            "review_history": self.review_history,
        }


class LitigationHoldRegister:
    """Central register of all litigation holds."""

    def __init__(self):
        self.holds: list[LitigationHold] = []

    def add_hold(self, hold: LitigationHold) -> None:
        self.holds.append(hold)

    def get_active_holds(self) -> list[LitigationHold]:
        return [h for h in self.holds if h.status == HoldStatus.ACTIVE]

    def get_holds_due_review(self) -> list[LitigationHold]:
        return [h for h in self.get_active_holds() if h.is_review_due()]

    def is_data_subject_held(self, data_subject_ref: str) -> list[str]:
        """Check if a data subject's data is under any active hold."""
        active_hold_refs = []
        for hold in self.get_active_holds():
            active_hold_refs.append(hold.hold_reference)
        return active_hold_refs

    def generate_register_report(self) -> dict:
        return {
            "report_date": datetime.utcnow().isoformat(),
            "organization": "Orion Data Vault Corp",
            "total_holds": len(self.holds),
            "active_holds": len(self.get_active_holds()),
            "holds_due_review": len(self.get_holds_due_review()),
            "holds": [h.to_dict() for h in self.holds],
        }


if __name__ == "__main__":
    register = LitigationHoldRegister()

    hold = LitigationHold(
        hold_reference="LH-2026-0023",
        matter_description="Commercial dispute — contract breach claim",
        legal_counsel="External Counsel — Smith & Partners LLP",
        trigger_category=TriggerCategory.LITIGATION_FILED,
        date_range_start="2024-01-01",
        data_categories=["Email", "CRM records", "Financial records"],
        systems_in_scope=["Exchange", "Salesforce", "SAP", "Finance system"],
    )
    hold.add_custodian("Jane Smith", "Sales Director", "Sales")
    hold.add_custodian("John Doe", "Finance Manager", "Finance")
    hold.add_custodian("Alice Johnson", "Account Manager", "Sales")
    hold.acknowledge_custodian("Jane Smith")

    register.add_hold(hold)
    print(json.dumps(register.generate_register_report(), indent=2))
