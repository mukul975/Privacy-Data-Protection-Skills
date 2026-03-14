#!/usr/bin/env python3
"""
Litigation Hold Management Process
Manages the lifecycle of legal holds including issuance, custodian tracking,
system hold implementation, and release procedures for Orion Data Vault Corp.
"""

import json
from datetime import datetime, timedelta
from enum import Enum


class HoldStatus(Enum):
    ACTIVE = "active"
    RELEASED = "released"
    UNDER_REVIEW = "under_review"


class HoldTrigger(Enum):
    LITIGATION_FILED = "litigation_filed"
    LITIGATION_ANTICIPATED = "litigation_anticipated"
    REGULATORY_INVESTIGATION = "regulatory_investigation"
    INTERNAL_INVESTIGATION = "internal_investigation"
    DPA_INQUIRY = "dpa_inquiry"
    TAX_AUDIT = "tax_audit"
    EMPLOYMENT_DISPUTE = "employment_dispute"


SYSTEM_HOLD_METHODS = {
    "Exchange Online": "Litigation Hold via Compliance Center",
    "Google Workspace": "Google Vault — Matter and Hold",
    "SharePoint / OneDrive": "Preservation Hold via Microsoft Purview",
    "AWS S3": "S3 Object Lock Legal Hold (PutObjectLegalHold)",
    "Azure Blob": "Legal Hold tags via immutability policy",
    "GCP GCS": "Temporary hold (gcloud storage objects update --temporary-hold)",
    "Databases": "Disable auto-deletion jobs; flag records with hold reference",
    "Backup Systems": "Tag for indefinite retention; exclude from rotation",
    "Deletion Orchestrator": "Add hold reference to exclusion list",
    "Teams / Slack": "Microsoft Purview retention / Slack Enterprise Legal Hold",
}


def generate_hold_reference() -> str:
    """Generate a unique litigation hold reference."""
    year = datetime.utcnow().strftime("%Y")
    seq = datetime.utcnow().strftime("%m%d")
    return f"LH-{year}-{seq}"


def create_litigation_hold(
    matter_description: str,
    trigger: HoldTrigger,
    legal_counsel: str,
    date_range_start: str,
    date_range_end: str,
    data_categories: list[str],
    systems_in_scope: list[str],
    custodians: list[dict],
) -> dict:
    """Create a new litigation hold record."""
    reference = generate_hold_reference()
    return {
        "hold_reference": reference,
        "status": HoldStatus.ACTIVE.value,
        "matter_description": matter_description,
        "trigger": trigger.value,
        "legal_counsel": legal_counsel,
        "date_issued": datetime.utcnow().strftime("%Y-%m-%d"),
        "scope": {
            "date_range": {"start": date_range_start, "end": date_range_end},
            "data_categories": data_categories,
            "systems_in_scope": systems_in_scope,
            "custodians": custodians,
        },
        "retention_interaction": {
            "normal_schedule": "SUSPENDED for all in-scope data",
            "automated_deletion": "PAUSED for in-scope data categories",
            "art17_requests": "Exception applies under Art. 17(3)(e)",
        },
        "review_schedule": {
            "frequency": "quarterly",
            "next_review": (datetime.utcnow() + timedelta(days=90)).strftime("%Y-%m-%d"),
        },
        "custodian_acknowledgements": {
            custodian["name"]: {
                "notified": datetime.utcnow().strftime("%Y-%m-%d"),
                "acknowledged": None,
                "deadline": (datetime.utcnow() + timedelta(days=2)).strftime("%Y-%m-%d"),
            }
            for custodian in custodians
        },
        "technical_holds": {
            system: {
                "method": SYSTEM_HOLD_METHODS.get(system, "Manual hold procedure"),
                "applied": False,
                "applied_date": None,
                "verified": False,
            }
            for system in systems_in_scope
        },
    }


def record_custodian_acknowledgement(hold: dict, custodian_name: str) -> dict:
    """Record a custodian's acknowledgement of a litigation hold."""
    if custodian_name in hold["custodian_acknowledgements"]:
        hold["custodian_acknowledgements"][custodian_name]["acknowledged"] = (
            datetime.utcnow().strftime("%Y-%m-%d")
        )
    return hold


def record_technical_hold(hold: dict, system_name: str) -> dict:
    """Record the application of a technical hold on a system."""
    if system_name in hold["technical_holds"]:
        hold["technical_holds"][system_name]["applied"] = True
        hold["technical_holds"][system_name]["applied_date"] = (
            datetime.utcnow().strftime("%Y-%m-%d")
        )
    return hold


def verify_technical_hold(hold: dict, system_name: str) -> dict:
    """Record verification of a technical hold on a system."""
    if system_name in hold["technical_holds"]:
        hold["technical_holds"][system_name]["verified"] = True
    return hold


def quarterly_review(hold: dict) -> dict:
    """Perform quarterly review of an active litigation hold."""
    review = {
        "hold_reference": hold["hold_reference"],
        "review_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "matter_still_active": None,
        "custodians_current": True,
        "new_custodians_identified": [],
        "technical_holds_verified": all(
            h["verified"] for h in hold["technical_holds"].values()
        ),
        "pending_art17_requests": [],
        "unacknowledged_custodians": [
            name
            for name, ack in hold["custodian_acknowledgements"].items()
            if ack["acknowledged"] is None
        ],
        "recommendation": None,
    }
    return review


def release_hold(hold: dict, authorizing_counsel: str, matter_outcome: str) -> dict:
    """Release a litigation hold and generate post-release actions."""
    hold["status"] = HoldStatus.RELEASED.value
    release_record = {
        "hold_reference": hold["hold_reference"],
        "release_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "authorizing_counsel": authorizing_counsel,
        "matter_outcome": matter_outcome,
        "post_release_actions": {
            "custodian_release_notices": "Issue to all custodians",
            "technical_hold_removal": {
                system: "Remove hold"
                for system in hold["technical_holds"]
            },
            "retention_catchup": {
                "expired_during_hold": "Schedule immediate deletion (within 30 days)",
                "queued_art17_requests": "Process immediately",
                "active_retention": "Resume normal countdown",
            },
        },
        "archive": {
            "documentation_retained_until": (
                datetime.utcnow() + timedelta(days=2190)
            ).strftime("%Y-%m-%d"),
        },
    }
    return release_record


def assess_art17_during_hold(
    hold: dict, data_subject_ref: str, data_categories_requested: list[str]
) -> dict:
    """Assess an Art. 17 erasure request against an active litigation hold."""
    overlapping = [
        cat
        for cat in data_categories_requested
        if cat in hold["scope"]["data_categories"]
    ]
    return {
        "hold_reference": hold["hold_reference"],
        "data_subject_ref": data_subject_ref,
        "assessment_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "categories_requested": data_categories_requested,
        "categories_under_hold": overlapping,
        "categories_not_held": [
            cat for cat in data_categories_requested if cat not in overlapping
        ],
        "exception_applies": len(overlapping) > 0,
        "exception_basis": "Art. 17(3)(e) — establishment, exercise, or defence of legal claims"
        if overlapping
        else "No exception — proceed with erasure",
        "action": {
            "held_categories": "Queue for processing upon hold release"
            if overlapping
            else "N/A",
            "non_held_categories": "Process erasure normally"
            if [c for c in data_categories_requested if c not in overlapping]
            else "N/A",
        },
    }


if __name__ == "__main__":
    hold = create_litigation_hold(
        matter_description="Commercial dispute — contract breach claim by Supplier X",
        trigger=HoldTrigger.LITIGATION_FILED,
        legal_counsel="External Counsel — Smith & Partners LLP",
        date_range_start="2024-01-01",
        date_range_end="2026-03-14",
        data_categories=["Email", "CRM records", "Financial records", "Contracts"],
        systems_in_scope=["Exchange Online", "AWS S3", "Databases"],
        custodians=[
            {"name": "Jane Smith", "title": "Procurement Director"},
            {"name": "John Doe", "title": "CFO"},
            {"name": "Sarah Brown", "title": "Legal Counsel"},
        ],
    )
    print(f"Hold Created: {hold['hold_reference']}")
    print(f"Status: {hold['status']}")
    print(f"Custodians: {len(hold['scope']['custodians'])}")
    print(f"Systems: {len(hold['technical_holds'])}")

    art17 = assess_art17_during_hold(
        hold,
        data_subject_ref="DS-HASH-abc123",
        data_categories_requested=["Email", "Marketing data"],
    )
    print(f"\nArt. 17 Assessment:")
    print(f"  Exception applies: {art17['exception_applies']}")
    print(f"  Held categories: {art17['categories_under_hold']}")
    print(f"  Non-held (process normally): {art17['categories_not_held']}")
