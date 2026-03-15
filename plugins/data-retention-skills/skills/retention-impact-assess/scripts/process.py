"""
Retention Impact Assessment Process
Structured evaluation for determining appropriate retention periods for new processing activities.
"""

import json
from datetime import datetime
from typing import Optional


class RetentionImpactAssessment:
    """Manages a Retention Impact Assessment for a processing activity."""

    def __init__(
        self,
        reference: str,
        processing_activity: str,
        business_owner: str,
        assessor: str,
    ):
        self.reference = reference
        self.processing_activity = processing_activity
        self.business_owner = business_owner
        self.assessor = assessor
        self.created_at = datetime.utcnow()
        self.scope: Optional[dict] = None
        self.regulatory_scan: list[dict] = []
        self.purpose_analysis: list[dict] = []
        self.proportionality: Optional[dict] = None
        self.recommendation: Optional[dict] = None
        self.approvals: list[dict] = []
        self.status = "in_progress"

    def set_scope(
        self,
        purposes: list[str],
        legal_basis: str,
        data_subjects: list[str],
        data_categories: list[str],
        special_category: bool,
        estimated_volume: str,
        data_sources: list[str],
        recipients: list[str],
        international_transfers: bool,
    ) -> None:
        """Set the scope and context of the assessment."""
        self.scope = {
            "processing_activity": self.processing_activity,
            "purposes": purposes,
            "legal_basis": legal_basis,
            "data_subjects": data_subjects,
            "data_categories": data_categories,
            "special_category_data": special_category,
            "estimated_volume": estimated_volume,
            "data_sources": data_sources,
            "recipients": recipients,
            "international_transfers": international_transfers,
        }

    def add_regulatory_requirement(
        self,
        domain: str,
        applicable: bool,
        statute: Optional[str] = None,
        minimum_period: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> None:
        """Add a regulatory requirement to the scan."""
        self.regulatory_scan.append({
            "domain": domain,
            "applicable": applicable,
            "statute": statute,
            "minimum_period": minimum_period,
            "notes": notes,
        })

    def add_purpose_analysis(
        self,
        purpose: str,
        legal_basis: str,
        data_categories_needed: list[str],
        duration: str,
        retention_period: str,
        justification: str,
    ) -> None:
        """Add a purpose-based retention analysis."""
        self.purpose_analysis.append({
            "purpose": purpose,
            "legal_basis": legal_basis,
            "data_categories_needed": data_categories_needed,
            "duration_of_purpose": duration,
            "retention_period": retention_period,
            "justification": justification,
        })

    def assess_proportionality(
        self,
        is_minimum_necessary: bool,
        shorter_period_possible: bool,
        anonymization_possible: bool,
        staged_deletion_possible: bool,
        access_restriction_plan: str,
        risk_level: str,
        risk_justification: str,
        alternatives_considered: list[str],
        conclusion: str,
    ) -> None:
        """Conduct the proportionality assessment."""
        self.proportionality = {
            "necessity": {
                "is_minimum_necessary": is_minimum_necessary,
                "shorter_period_possible": shorter_period_possible,
                "anonymization_possible": anonymization_possible,
            },
            "data_minimization_over_time": {
                "staged_deletion_possible": staged_deletion_possible,
            },
            "access_restriction": access_restriction_plan,
            "risk_to_data_subjects": {
                "level": risk_level,
                "justification": risk_justification,
            },
            "alternatives_considered": alternatives_considered,
            "conclusion": conclusion,
        }

    def make_recommendation(
        self,
        phases: list[dict],
        total_identifiable_days: int,
        retention_trigger: str,
        deletion_method: str,
        justification_summary: str,
    ) -> None:
        """Make the retention period recommendation."""
        self.recommendation = {
            "phases": phases,
            "total_identifiable_retention_days": total_identifiable_days,
            "retention_trigger": retention_trigger,
            "deletion_method": deletion_method,
            "justification_summary": justification_summary,
        }

    def approve(self, approver_name: str, approver_role: str) -> None:
        """Record an approval."""
        self.approvals.append({
            "approver": approver_name,
            "role": approver_role,
            "date": datetime.utcnow().isoformat(),
        })

    def finalize(self) -> None:
        """Finalize the assessment."""
        self.status = "completed"

    def generate_report(self) -> dict:
        """Generate the full RIA report."""
        return {
            "reference": self.reference,
            "organization": "Orion Data Vault Corp",
            "processing_activity": self.processing_activity,
            "business_owner": self.business_owner,
            "assessor": self.assessor,
            "created_at": self.created_at.isoformat(),
            "status": self.status,
            "scope": self.scope,
            "regulatory_scan": self.regulatory_scan,
            "purpose_analysis": self.purpose_analysis,
            "proportionality_assessment": self.proportionality,
            "recommendation": self.recommendation,
            "approvals": self.approvals,
            "implementation_checklist": [
                "Add data category to retention schedule",
                "Configure automated deletion rules",
                "Update ROPA with retention period",
                "Update privacy notice",
                "Configure access restrictions",
                "Update processor agreements if applicable",
                "Schedule first review (12 months)",
                "Brief data owners and staff",
            ],
        }


def generate_implementation_checklist(ria_reference: str, retention_period: str) -> list[dict]:
    """Generate the post-RIA implementation checklist."""
    return [
        {"step": 1, "action": "Add data category to retention schedule", "responsible": "DPO", "deadline": "14 days"},
        {"step": 2, "action": "Configure automated deletion rules", "responsible": "IT", "deadline": "Before processing starts"},
        {"step": 3, "action": "Update ROPA with retention period", "responsible": "DPO", "deadline": "14 days"},
        {"step": 4, "action": "Update privacy notice", "responsible": "DPO/Marketing", "deadline": "Before processing starts"},
        {"step": 5, "action": "Configure access restrictions", "responsible": "IT/Security", "deadline": "Before processing starts"},
        {"step": 6, "action": "Update processor agreements", "responsible": "Legal/Procurement", "deadline": "Before processing starts"},
        {"step": 7, "action": "Schedule first review", "responsible": "DPO", "deadline": "Set for 12 months after start"},
        {"step": 8, "action": "Brief data owners and staff", "responsible": "DPO/Training", "deadline": "Before processing starts"},
    ]


if __name__ == "__main__":
    ria = RetentionImpactAssessment(
        reference="RIA-2026-0019",
        processing_activity="Customer loyalty program",
        business_owner="Marketing Director",
        assessor="Privacy Analyst",
    )
    ria.set_scope(
        purposes=["Loyalty point management", "Personalized offers", "Programme analytics"],
        legal_basis="Art. 6(1)(b) Contract",
        data_subjects=["Loyalty programme members"],
        data_categories=["Name", "email", "purchase history", "loyalty points", "preferences"],
        special_category=False,
        estimated_volume="50,000 members, growing 10% annually",
        data_sources=["Collected directly from data subject"],
        recipients=["Marketing team", "CRM processor", "Email service provider"],
        international_transfers=False,
    )
    ria.add_regulatory_requirement("Tax and fiscal", False)
    ria.add_regulatory_requirement("Company law", False)
    ria.add_regulatory_requirement("Limitation periods", True, "Limitation Act 1980 s.5", "6 years", "Contract claims limitation")
    ria.add_purpose_analysis(
        purpose="Loyalty point management",
        legal_basis="Art. 6(1)(b) Contract",
        data_categories_needed=["Name", "email", "purchase history", "loyalty points"],
        duration="Duration of membership",
        retention_period="Duration of membership + 2 years",
        justification="Contractual obligation plus limitation period buffer for any membership-related disputes",
    )
    ria.assess_proportionality(
        is_minimum_necessary=True,
        shorter_period_possible=False,
        anonymization_possible=True,
        staged_deletion_possible=True,
        access_restriction_plan="Active access during membership; restricted to compliance team post-membership",
        risk_level="Low",
        risk_justification="Standard personal data; no special categories; limited to programme context",
        alternatives_considered=["Anonymization at membership end", "Aggregated analytics only"],
        conclusion="Retention of membership + 2 years is proportionate given limitation period considerations.",
    )
    ria.make_recommendation(
        phases=[
            {"phase": "Active processing", "duration": "Duration of membership", "data_state": "Full data, full access"},
            {"phase": "Post-membership retention", "duration": "2 years", "data_state": "Full data, restricted access"},
            {"phase": "Anonymized retention", "duration": "Indefinite", "data_state": "Anonymized aggregates only"},
        ],
        total_identifiable_days=730,
        retention_trigger="Membership termination date",
        deletion_method="Automated deletion + anonymization pipeline",
        justification_summary="Membership data retained for 2 years post-termination to cover limitation period for contractual disputes. Anonymized aggregates retained indefinitely for programme analytics.",
    )
    ria.approve("Marketing Director", "Business Owner")
    ria.approve("DPO", "DPO")
    ria.finalize()

    print(json.dumps(ria.generate_report(), indent=2))
