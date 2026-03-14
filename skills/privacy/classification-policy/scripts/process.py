"""
Data Classification Policy Engine
Assigns classification tiers and generates handling requirement specifications.
"""

import json
from dataclasses import dataclass, field
from enum import Enum
from datetime import date


class ClassificationTier(Enum):
    PUBLIC = "Public"
    INTERNAL = "Internal"
    CONFIDENTIAL = "Confidential"
    RESTRICTED = "Restricted"


class GDPRCategory(Enum):
    NON_PERSONAL = "non_personal"
    ANONYMISED = "anonymised"
    PSEUDONYMISED = "pseudonymised"
    PERSONAL_DIRECT = "personal_direct"
    PERSONAL_INDIRECT = "personal_indirect"
    SPECIAL_CATEGORY = "special_category"
    CRIMINAL_DATA = "criminal_data"


TIER_MAPPING: dict[GDPRCategory, ClassificationTier] = {
    GDPRCategory.NON_PERSONAL: ClassificationTier.PUBLIC,
    GDPRCategory.ANONYMISED: ClassificationTier.PUBLIC,
    GDPRCategory.PSEUDONYMISED: ClassificationTier.INTERNAL,
    GDPRCategory.PERSONAL_INDIRECT: ClassificationTier.CONFIDENTIAL,
    GDPRCategory.PERSONAL_DIRECT: ClassificationTier.CONFIDENTIAL,
    GDPRCategory.SPECIAL_CATEGORY: ClassificationTier.RESTRICTED,
    GDPRCategory.CRIMINAL_DATA: ClassificationTier.RESTRICTED,
}


@dataclass
class HandlingRequirements:
    """Per-tier handling requirements specification."""
    tier: ClassificationTier
    storage: str
    transmission: str
    access_control: str
    encryption_at_rest: str
    encryption_in_transit: str
    printing: str
    external_sharing: str
    retention: str
    disposal: str
    labelling: str
    audit: str
    dlp: str
    incident_response: str


HANDLING_SPECS: dict[ClassificationTier, HandlingRequirements] = {
    ClassificationTier.PUBLIC: HandlingRequirements(
        tier=ClassificationTier.PUBLIC,
        storage="No restrictions; any approved platform",
        transmission="No restrictions",
        access_control="No restrictions",
        encryption_at_rest="Not required",
        encryption_in_transit="Not required",
        printing="No restrictions",
        external_sharing="No restrictions",
        retention="Per document retention schedule",
        disposal="Standard deletion",
        labelling="'Public' label or no label",
        audit="Not required",
        dlp="Not required",
        incident_response="Standard incident process",
    ),
    ClassificationTier.INTERNAL: HandlingRequirements(
        tier=ClassificationTier.INTERNAL,
        storage="Vanguard-managed systems only",
        transmission="Vanguard email or approved collaboration tools",
        access_control="All employees and approved contractors",
        encryption_at_rest="Recommended",
        encryption_in_transit="Required (TLS 1.2+)",
        printing="Permitted; collect from printer promptly",
        external_sharing="Not permitted without Data Owner approval",
        retention="Per document retention schedule",
        disposal="Standard secure deletion",
        labelling="'Internal' in header/footer and metadata",
        audit="Annual access review",
        dlp="Warn on external sharing",
        incident_response="Standard incident process",
    ),
    ClassificationTier.CONFIDENTIAL: HandlingRequirements(
        tier=ClassificationTier.CONFIDENTIAL,
        storage="Encrypted at rest (AES-256); Vanguard-managed systems",
        transmission="Encrypted email (TLS 1.3); approved SFTP",
        access_control="RBAC; business need-to-know; MFA required",
        encryption_at_rest="Required (AES-256)",
        encryption_in_transit="Required (TLS 1.3)",
        printing="Secure print release; locked cabinet storage",
        external_sharing="Approved third parties under DPA/NDA; DPO approval for new recipients",
        retention="Data-specific schedule; automated enforcement",
        disposal="NIST 800-88 Clear; shredding for physical",
        labelling="'Confidential' in header/footer, email tag, metadata",
        audit="Access logged; quarterly permission review",
        dlp="Warn on external sharing; block personal email",
        incident_response="DPO notification within 4 hours; Art. 33 assessment",
    ),
    ClassificationTier.RESTRICTED: HandlingRequirements(
        tier=ClassificationTier.RESTRICTED,
        storage="Designated restricted systems; customer-managed encryption keys; separate network segment",
        transmission="End-to-end encryption only; no email without encryption",
        access_control="Named individual lists; dual-person authorisation for bulk access; MFA; PAM",
        encryption_at_rest="Required (AES-256 with customer-managed keys)",
        encryption_in_transit="Required (TLS 1.3; end-to-end where possible)",
        printing="Prohibited unless DPO authorises; watermarked with user identity",
        external_sharing="Prohibited unless DPO and CPO jointly approve; encrypted transfer only",
        retention="Strict; automated deletion; no extensions without DPO approval",
        disposal="NIST 800-88 Purge; disposal certificate required",
        labelling="'Restricted' (red) in header/footer, email banner, metadata, screen marking",
        audit="All access logged; monthly DPO review",
        dlp="Block all external sharing, USB, print, screenshot; alert DPO",
        incident_response="Immediate DPO notification; treat as breach; Art. 33 within 72 hours",
    ),
}


@dataclass
class ClassificationDecision:
    """A classification decision for a data element or dataset."""
    element_name: str
    gdpr_category: GDPRCategory
    assigned_tier: ClassificationTier
    commercial_sensitivity_override: bool
    final_tier: ClassificationTier
    handling: HandlingRequirements
    classified_by: str
    classification_date: str
    review_date: str
    notes: str = ""


class ClassificationPolicyEngine:
    """Applies classification policy to data elements."""

    def classify(
        self,
        element_name: str,
        gdpr_category: GDPRCategory,
        commercial_sensitivity: str = "normal",
        classified_by: str = "",
    ) -> ClassificationDecision:
        """
        Classify a data element per policy.

        Args:
            element_name: Name of the data element
            gdpr_category: GDPR data category
            commercial_sensitivity: 'normal', 'high', or 'critical'
            classified_by: Name of the person classifying
        """
        base_tier = TIER_MAPPING.get(gdpr_category, ClassificationTier.INTERNAL)

        override = False
        final_tier = base_tier
        if commercial_sensitivity == "high" and base_tier.value in ("Public", "Internal"):
            final_tier = ClassificationTier.CONFIDENTIAL
            override = True
        elif commercial_sensitivity == "critical":
            final_tier = ClassificationTier.RESTRICTED
            override = True

        handling = HANDLING_SPECS[final_tier]
        today = date.today()
        review_months = 6 if final_tier == ClassificationTier.RESTRICTED else 12

        return ClassificationDecision(
            element_name=element_name,
            gdpr_category=gdpr_category,
            assigned_tier=base_tier,
            commercial_sensitivity_override=override,
            final_tier=final_tier,
            handling=handling,
            classified_by=classified_by,
            classification_date=today.isoformat(),
            review_date=today.replace(
                month=today.month + review_months if today.month + review_months <= 12
                else (today.month + review_months) - 12,
                year=today.year if today.month + review_months <= 12
                else today.year + 1,
            ).isoformat(),
        )

    def generate_policy_compliance_report(
        self, decisions: list[ClassificationDecision]
    ) -> dict:
        """Generate a compliance report for classification decisions."""
        tier_counts: dict[str, int] = {}
        override_count = 0
        for d in decisions:
            tier = d.final_tier.value
            tier_counts[tier] = tier_counts.get(tier, 0) + 1
            if d.commercial_sensitivity_override:
                override_count += 1

        return {
            "report_date": date.today().isoformat(),
            "total_classified": len(decisions),
            "by_tier": tier_counts,
            "commercial_overrides": override_count,
        }


def run_vanguard_example():
    """Demonstrate classification policy application."""
    engine = ClassificationPolicyEngine()

    elements = [
        ("annual_report_2025", GDPRCategory.NON_PERSONAL, "normal"),
        ("internal_org_chart", GDPRCategory.NON_PERSONAL, "normal"),
        ("customer_email_address", GDPRCategory.PERSONAL_DIRECT, "normal"),
        ("employee_health_record", GDPRCategory.SPECIAL_CATEGORY, "normal"),
        ("dbs_check_result", GDPRCategory.CRIMINAL_DATA, "normal"),
        ("board_strategy_document", GDPRCategory.NON_PERSONAL, "critical"),
        ("pseudonymised_analytics", GDPRCategory.PSEUDONYMISED, "normal"),
        ("customer_transaction_history", GDPRCategory.PERSONAL_INDIRECT, "high"),
    ]

    decisions = []
    print("=" * 70)
    print("VANGUARD FINANCIAL SERVICES — CLASSIFICATION POLICY APPLICATION")
    print("=" * 70)

    for name, category, sensitivity in elements:
        decision = engine.classify(name, category, sensitivity, "Sarah Mitchell")
        decisions.append(decision)
        override_note = " [COMMERCIAL OVERRIDE]" if decision.commercial_sensitivity_override else ""
        print(f"\n  {decision.element_name}:")
        print(f"    GDPR Category: {decision.gdpr_category.value}")
        print(f"    Assigned Tier: {decision.final_tier.value}{override_note}")
        print(f"    Storage: {decision.handling.storage}")
        print(f"    Encryption: {decision.handling.encryption_at_rest}")
        print(f"    DLP: {decision.handling.dlp}")

    report = engine.generate_policy_compliance_report(decisions)
    print(f"\n{'='*70}")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    run_vanguard_example()
