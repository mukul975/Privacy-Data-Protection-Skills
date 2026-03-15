"""
NIST Privacy Framework COMMUNICATE Function — Transparency Assessor

Evaluates organizational transparency mechanisms, privacy notice
compliance, and stakeholder communication effectiveness aligned
with CM.AW and CM.PO subcategories.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import json


class NoticeType(Enum):
    SHORT = "short_notice"
    FULL = "full_privacy_notice"
    SUPPLEMENTARY = "supplementary_notice"
    JUST_IN_TIME = "just_in_time"
    BREACH = "breach_notification"


class Jurisdiction(Enum):
    EU_GDPR = "EU_GDPR"
    US_CCPA = "US_CCPA"
    US_CPRA = "US_CPRA"
    UK_DPA = "UK_DPA"
    BR_LGPD = "BR_LGPD"
    CA_PIPEDA = "CA_PIPEDA"


REQUIRED_ELEMENTS = {
    Jurisdiction.EU_GDPR: [
        "controller_identity",
        "dpo_contact",
        "processing_purposes",
        "legal_basis",
        "data_categories",
        "recipients",
        "international_transfers",
        "retention_periods",
        "data_subject_rights",
        "right_to_complain",
        "automated_decision_making",
    ],
    Jurisdiction.US_CCPA: [
        "business_identity",
        "data_categories_collected",
        "processing_purposes",
        "sale_sharing_disclosure",
        "opt_out_right",
        "data_subject_rights",
        "non_discrimination",
        "contact_information",
    ],
    Jurisdiction.UK_DPA: [
        "controller_identity",
        "dpo_contact",
        "processing_purposes",
        "legal_basis",
        "data_categories",
        "recipients",
        "international_transfers",
        "retention_periods",
        "data_subject_rights",
        "right_to_complain_ico",
    ],
}


@dataclass
class PrivacyNotice:
    notice_id: str
    notice_type: NoticeType
    jurisdictions: list[Jurisdiction]
    url: str
    language: str
    last_updated: datetime
    version: str
    elements_present: list[str]
    readability_grade: float
    accessibility_wcag: str


@dataclass
class ComplianceResult:
    jurisdiction: Jurisdiction
    required_elements: list[str]
    present_elements: list[str]
    missing_elements: list[str]
    compliance_rate: float


class TransparencyAssessor:
    """
    Assess privacy notice compliance and transparency effectiveness.
    """

    def assess_notice_compliance(
        self, notice: PrivacyNotice
    ) -> list[ComplianceResult]:
        """Check a privacy notice against jurisdictional requirements."""
        results = []

        for jurisdiction in notice.jurisdictions:
            required = REQUIRED_ELEMENTS.get(jurisdiction, [])
            present = [e for e in required if e in notice.elements_present]
            missing = [e for e in required if e not in notice.elements_present]

            results.append(ComplianceResult(
                jurisdiction=jurisdiction,
                required_elements=required,
                present_elements=present,
                missing_elements=missing,
                compliance_rate=len(present) / len(required) if required else 1.0,
            ))

        return results

    def assess_readability(self, notice: PrivacyNotice) -> dict:
        """Assess notice readability against best practice targets."""
        target_grade = 8.0  # Grade 8 reading level target

        return {
            "current_grade": notice.readability_grade,
            "target_grade": target_grade,
            "meets_target": notice.readability_grade <= target_grade,
            "recommendation": (
                "Notice meets readability target"
                if notice.readability_grade <= target_grade
                else f"Simplify language to reduce from grade {notice.readability_grade} to grade {target_grade}"
            ),
        }

    def generate_transparency_report(
        self, notices: list[PrivacyNotice]
    ) -> dict:
        """Generate a comprehensive transparency assessment report."""
        all_results = []
        for notice in notices:
            results = self.assess_notice_compliance(notice)
            readability = self.assess_readability(notice)
            all_results.append({
                "notice_id": notice.notice_id,
                "type": notice.notice_type.value,
                "url": notice.url,
                "last_updated": notice.last_updated.isoformat(),
                "compliance_by_jurisdiction": [
                    {
                        "jurisdiction": r.jurisdiction.value,
                        "compliance_rate": f"{r.compliance_rate*100:.1f}%",
                        "missing_elements": r.missing_elements,
                    }
                    for r in results
                ],
                "readability": readability,
                "accessibility": notice.accessibility_wcag,
            })

        overall_compliance = sum(
            r["compliance_rate"]
            for notice_result in all_results
            for r in [
                {
                    "compliance_rate": float(jr["compliance_rate"].rstrip("%")) / 100
                }
                for jr in notice_result["compliance_by_jurisdiction"]
            ]
        )
        total_checks = sum(
            len(nr["compliance_by_jurisdiction"]) for nr in all_results
        )

        return {
            "assessment_date": datetime.now(timezone.utc).isoformat(),
            "total_notices_assessed": len(notices),
            "overall_compliance_rate": f"{(overall_compliance / total_checks * 100) if total_checks > 0 else 0:.1f}%",
            "notice_assessments": all_results,
        }


if __name__ == "__main__":
    assessor = TransparencyAssessor()

    notice = PrivacyNotice(
        notice_id="PN-001",
        notice_type=NoticeType.FULL,
        jurisdictions=[Jurisdiction.EU_GDPR, Jurisdiction.US_CCPA],
        url="https://www.cipherengineeringlabs.com/privacy",
        language="en",
        last_updated=datetime(2025, 11, 1, tzinfo=timezone.utc),
        version="3.2",
        elements_present=[
            "controller_identity", "dpo_contact", "processing_purposes",
            "legal_basis", "data_categories", "recipients",
            "retention_periods", "data_subject_rights", "right_to_complain",
            "business_identity", "data_categories_collected",
            "sale_sharing_disclosure", "opt_out_right",
            "non_discrimination", "contact_information",
        ],
        readability_grade=9.2,
        accessibility_wcag="AA",
    )

    report = assessor.generate_transparency_report([notice])
    print(json.dumps(report, indent=2))
