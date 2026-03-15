#!/usr/bin/env python3
"""
AI Training Data Lawfulness Assessment Engine

Evaluates lawful basis for AI training data processing per EDPB Guidelines
04/2025, conducting balancing tests and generating compliance reports.
"""

import json
import datetime
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class LawfulBasis(Enum):
    CONSENT = "Art. 6(1)(a) - Consent"
    CONTRACT = "Art. 6(1)(b) - Contract Necessity"
    LEGAL_OBLIGATION = "Art. 6(1)(c) - Legal Obligation"
    VITAL_INTEREST = "Art. 6(1)(d) - Vital Interest"
    PUBLIC_INTEREST = "Art. 6(1)(e) - Public Interest"
    LEGITIMATE_INTEREST = "Art. 6(1)(f) - Legitimate Interest"
    NONE = "No lawful basis identified"


class SourceType(Enum):
    FIRST_PARTY = "first_party"
    THIRD_PARTY = "third_party"
    PUBLIC_DATASET = "public_dataset"
    OPEN_SOURCE = "open_source"
    WEB_SCRAPED = "web_scraped"
    USER_CONTRIBUTED = "user_contributed"


class BalancingOutcome(Enum):
    CONTROLLER_OVERRIDES = "Controller interest overrides data subject rights"
    DATA_SUBJECT_OVERRIDES = "Data subject rights override controller interest"
    MARGINAL = "Marginal — maximum safeguards required"


class ComplianceStatus(Enum):
    COMPLIANT = "Compliant"
    NON_COMPLIANT = "Non-Compliant"
    CONDITIONALLY_COMPLIANT = "Conditionally Compliant"
    REQUIRES_REMEDIATION = "Requires Remediation"


@dataclass
class LegitimateInterestTest:
    interest_description: str
    interest_is_lawful: bool = True
    interest_is_real: bool = True
    interest_is_specific: bool = True
    necessity_personal_data_required: bool = True
    necessity_anonymised_tested: bool = False
    necessity_synthetic_tested: bool = False
    necessity_federated_assessed: bool = False
    necessity_minimum_dataset_determined: bool = False
    balance_data_subject_impact: str = "medium"  # low, medium, high
    balance_expectations_met: str = "not_met"  # met, partially_met, not_met
    balance_special_category_involved: bool = False
    balance_vulnerable_subjects: bool = False
    balance_safeguards_level: str = "adequate"  # comprehensive, adequate, insufficient
    balance_opt_out_available: bool = False
    balance_transparency_provided: bool = False
    outcome: Optional[BalancingOutcome] = None


@dataclass
class DataSource:
    name: str
    source_type: SourceType
    description: str
    data_categories: list[str]
    record_count: int
    contains_pii: bool = True
    contains_special_category: bool = False
    special_category_types: list[str] = field(default_factory=list)
    original_collection_purpose: str = ""
    ai_training_disclosed: bool = False
    lawful_basis: LawfulBasis = LawfulBasis.NONE
    art9_condition: Optional[str] = None
    consent_covers_ai_training: Optional[bool] = None
    consent_is_specific: Optional[bool] = None
    consent_is_withdrawable: Optional[bool] = None
    upstream_basis_verified: Optional[bool] = None
    licence_permits_ai_training: Optional[bool] = None
    pii_filtering_applied: bool = False
    pseudonymisation_applied: bool = False
    differential_privacy_applied: bool = False
    compatibility_assessed: bool = False
    notes: str = ""


@dataclass
class SourceAssessment:
    source: DataSource
    status: ComplianceStatus
    lawful_basis_valid: bool
    issues: list[str] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)
    risk_factors: list[str] = field(default_factory=list)
    balancing_test: Optional[LegitimateInterestTest] = None


def assess_consent_validity(source: DataSource) -> tuple[bool, list[str], list[str]]:
    issues = []
    recommendations = []
    valid = True

    if source.consent_covers_ai_training is False:
        valid = False
        issues.append(
            "Consent does not specifically cover AI/ML model training as a processing purpose"
        )
        recommendations.append(
            "Obtain fresh consent specifying AI training purpose, or switch to alternative lawful basis"
        )

    if source.consent_covers_ai_training is None:
        valid = False
        issues.append("Consent scope for AI training has not been verified")
        recommendations.append(
            "Review original consent language to confirm AI training is an explicit purpose"
        )

    if source.consent_is_specific is False:
        valid = False
        issues.append(
            "Consent is not specific to AI training — bundled with other processing purposes"
        )
        recommendations.append(
            "Separate AI training consent from other processing consents per Art. 7(2)"
        )

    if source.consent_is_withdrawable is False:
        valid = False
        issues.append(
            "No mechanism for consent withdrawal — violates Art. 7(3)"
        )
        recommendations.append(
            "Implement consent withdrawal mechanism with clear process for removing data from training pipeline"
        )

    if source.contains_special_category and not source.art9_condition:
        valid = False
        issues.append(
            "Special category data processed under consent basis but no Art. 9(2)(a) explicit consent documented"
        )
        recommendations.append(
            "Obtain explicit consent per Art. 9(2)(a) for special category data, or remove from training set"
        )

    return valid, issues, recommendations


def assess_contract_validity(source: DataSource) -> tuple[bool, list[str], list[str]]:
    issues = []
    recommendations = []
    valid = False

    issues.append(
        "EDPB position: general AI model training is not necessary for contract performance with individual data subjects"
    )
    recommendations.append(
        "Assess whether the specific AI training produces a personalised model necessary for the contracted service"
    )
    recommendations.append(
        "If general model improvement: switch to legitimate interest (Art. 6(1)(f)) with balancing test"
    )

    return valid, issues, recommendations


def assess_legitimate_interest(
    source: DataSource, li_test: LegitimateInterestTest
) -> tuple[bool, list[str], list[str], BalancingOutcome]:
    issues = []
    recommendations = []
    score = 0
    max_score = 10

    if not li_test.interest_is_specific:
        issues.append(
            "Legitimate interest not articulated with sufficient specificity"
        )
        recommendations.append(
            "Articulate the specific interest — not 'AI improvement' but the precise capability being developed"
        )
        score -= 2

    if li_test.necessity_anonymised_tested:
        score += 1
    else:
        recommendations.append(
            "Test model performance with anonymised data and document results"
        )

    if li_test.necessity_synthetic_tested:
        score += 1
    else:
        recommendations.append(
            "Evaluate synthetic data as alternative or supplement to personal data"
        )

    if li_test.necessity_minimum_dataset_determined:
        score += 1
    else:
        issues.append("Minimum effective dataset not determined")
        recommendations.append(
            "Conduct ablation study to determine minimum training data requirement"
        )

    impact_scores = {"low": 2, "medium": 0, "high": -2}
    score += impact_scores.get(li_test.balance_data_subject_impact, 0)

    expectation_scores = {"met": 2, "partially_met": 0, "not_met": -2}
    score += expectation_scores.get(li_test.balance_expectations_met, 0)

    if li_test.balance_special_category_involved:
        score -= 3
        issues.append(
            "Special category data involved — significantly tips balance toward data subject"
        )

    if li_test.balance_vulnerable_subjects:
        score -= 2
        issues.append(
            "Vulnerable data subjects involved — heightened protection required"
        )

    safeguard_scores = {"comprehensive": 3, "adequate": 1, "insufficient": -2}
    score += safeguard_scores.get(li_test.balance_safeguards_level, 0)

    if li_test.balance_opt_out_available:
        score += 1
    else:
        issues.append("No opt-out mechanism available for data subjects")
        recommendations.append(
            "Implement accessible opt-out mechanism per EDPB recommendation"
        )

    if li_test.balance_transparency_provided:
        score += 1
    else:
        issues.append("Transparency about AI training use not provided to data subjects")
        recommendations.append(
            "Update privacy notices to disclose AI training processing"
        )

    if source.source_type == SourceType.WEB_SCRAPED:
        score -= 3
        issues.append(
            "EDPB Guidelines 04/2025: Web-scraped data faces heightened scrutiny — high bar for legitimate interest"
        )
        recommendations.append(
            "Document comprehensive justification for web scraping necessity"
        )
        recommendations.append(
            "Implement maximum safeguards: PII removal, differential privacy, opt-out, transparency"
        )

    if score >= 3:
        outcome = BalancingOutcome.CONTROLLER_OVERRIDES
    elif score <= -2:
        outcome = BalancingOutcome.DATA_SUBJECT_OVERRIDES
    else:
        outcome = BalancingOutcome.MARGINAL

    li_test.outcome = outcome
    valid = outcome != BalancingOutcome.DATA_SUBJECT_OVERRIDES

    return valid, issues, recommendations, outcome


def assess_web_scraped_source(source: DataSource) -> tuple[list[str], list[str]]:
    issues = []
    recommendations = []

    issues.append(
        "Web-scraped data: consent not feasible at scale per EDPB guidance"
    )
    issues.append(
        "Data subjects typically do not expect web-scraped data to be used for AI training"
    )

    if not source.pii_filtering_applied:
        issues.append("PII detection and removal not applied before training")
        recommendations.append(
            "Apply PII detection and removal to web-scraped data before including in training pipeline"
        )

    if not source.differential_privacy_applied:
        recommendations.append(
            "Apply differential privacy during training to mitigate individual data leakage risk"
        )

    recommendations.append(
        "Implement web-accessible opt-out mechanism for data subjects"
    )
    recommendations.append(
        "Publish transparency information about web scraping practices and AI training use"
    )
    recommendations.append(
        "Respect robots.txt directives and website-specific scraping restrictions"
    )
    recommendations.append(
        "Assess whether children's data is likely present and implement age filtering"
    )

    return issues, recommendations


def assess_third_party_source(source: DataSource) -> tuple[list[str], list[str]]:
    issues = []
    recommendations = []

    if source.upstream_basis_verified is False:
        issues.append(
            "Upstream lawful basis not verified — provider's collection practices not assessed"
        )
        recommendations.append(
            "Conduct due diligence on provider's data collection and obtain lawful basis warranties"
        )

    if source.upstream_basis_verified is None:
        issues.append("Upstream lawful basis verification not yet completed")
        recommendations.append(
            "Request documentation of provider's lawful basis and consent scope from data provider"
        )

    if source.licence_permits_ai_training is False:
        issues.append(
            "Data licence does not explicitly permit AI training use"
        )
        recommendations.append(
            "Negotiate licence amendment to cover AI training, or exclude this source"
        )

    if source.licence_permits_ai_training is None:
        recommendations.append(
            "Review data licence terms to confirm AI training is a permitted use"
        )

    if not source.compatibility_assessed:
        issues.append(
            "Art. 6(4) compatibility assessment not completed for third-party data repurposed for AI training"
        )
        recommendations.append(
            "Conduct Art. 6(4) compatibility assessment documenting link between original and training purposes"
        )

    return issues, recommendations


def assess_source(
    source: DataSource,
    li_test: Optional[LegitimateInterestTest] = None,
) -> SourceAssessment:
    issues = []
    recommendations = []
    risk_factors = []
    lawful_basis_valid = False

    if source.lawful_basis == LawfulBasis.NONE:
        issues.append("No lawful basis identified for AI training processing")
        recommendations.append(
            "Select and document a lawful basis under Art. 6(1) before using this data for training"
        )
        status = ComplianceStatus.NON_COMPLIANT
        return SourceAssessment(
            source=source,
            status=status,
            lawful_basis_valid=False,
            issues=issues,
            recommendations=recommendations,
        )

    if source.lawful_basis == LawfulBasis.CONSENT:
        lawful_basis_valid, consent_issues, consent_recs = assess_consent_validity(source)
        issues.extend(consent_issues)
        recommendations.extend(consent_recs)

    elif source.lawful_basis == LawfulBasis.CONTRACT:
        lawful_basis_valid, contract_issues, contract_recs = assess_contract_validity(source)
        issues.extend(contract_issues)
        recommendations.extend(contract_recs)

    elif source.lawful_basis == LawfulBasis.LEGITIMATE_INTEREST:
        if li_test:
            lawful_basis_valid, li_issues, li_recs, outcome = assess_legitimate_interest(
                source, li_test
            )
            issues.extend(li_issues)
            recommendations.extend(li_recs)
        else:
            issues.append(
                "Legitimate interest claimed but no balancing test documented"
            )
            recommendations.append(
                "Complete three-part legitimate interest balancing test per EDPB Guidelines 04/2025"
            )
            lawful_basis_valid = False

    elif source.lawful_basis == LawfulBasis.PUBLIC_INTEREST:
        lawful_basis_valid = True
        recommendations.append(
            "Document the specific Union or Member State law authorising AI training in the public interest"
        )

    if source.source_type == SourceType.WEB_SCRAPED:
        ws_issues, ws_recs = assess_web_scraped_source(source)
        issues.extend(ws_issues)
        recommendations.extend(ws_recs)
        risk_factors.append("Web-scraped data — heightened EDPB scrutiny")

    if source.source_type == SourceType.THIRD_PARTY:
        tp_issues, tp_recs = assess_third_party_source(source)
        issues.extend(tp_issues)
        recommendations.extend(tp_recs)

    if source.contains_special_category:
        risk_factors.append(
            f"Special category data present: {', '.join(source.special_category_types)}"
        )
        if not source.art9_condition:
            issues.append(
                "Special category data present without Art. 9(2) condition identified"
            )
            lawful_basis_valid = False

    if not source.ai_training_disclosed:
        issues.append(
            "AI training not disclosed as a processing purpose in privacy notice"
        )
        recommendations.append(
            "Update privacy notice to include AI training as a specified processing purpose per Arts. 13-14"
        )

    if not source.compatibility_assessed and not source.ai_training_disclosed:
        issues.append(
            "Art. 6(4) purpose compatibility not assessed for data not collected for AI training"
        )
        recommendations.append(
            "Conduct Art. 6(4) compatibility assessment for repurposed data"
        )

    if source.record_count > 1_000_000:
        risk_factors.append(f"Large-scale processing: {source.record_count:,} records")

    if not lawful_basis_valid:
        status = ComplianceStatus.NON_COMPLIANT
    elif issues:
        status = ComplianceStatus.CONDITIONALLY_COMPLIANT
    else:
        status = ComplianceStatus.COMPLIANT

    return SourceAssessment(
        source=source,
        status=status,
        lawful_basis_valid=lawful_basis_valid,
        issues=issues,
        recommendations=recommendations,
        risk_factors=risk_factors,
        balancing_test=li_test,
    )


def format_assessment_report(assessments: list[SourceAssessment], org_name: str) -> str:
    lines = []
    today = datetime.date.today().isoformat()

    lines.append(f"{'='*80}")
    lines.append(f"AI TRAINING DATA LAWFULNESS ASSESSMENT REPORT")
    lines.append(f"Organisation: {org_name}")
    lines.append(f"Date: {today}")
    lines.append(f"{'='*80}")

    compliant = sum(1 for a in assessments if a.status == ComplianceStatus.COMPLIANT)
    conditional = sum(1 for a in assessments if a.status == ComplianceStatus.CONDITIONALLY_COMPLIANT)
    non_compliant = sum(1 for a in assessments if a.status == ComplianceStatus.NON_COMPLIANT)

    lines.append(f"\n## EXECUTIVE SUMMARY")
    lines.append(f"Total sources assessed: {len(assessments)}")
    lines.append(f"Compliant: {compliant}")
    lines.append(f"Conditionally compliant: {conditional}")
    lines.append(f"Non-compliant: {non_compliant}")

    for idx, assessment in enumerate(assessments, 1):
        lines.append(f"\n{'─'*60}")
        lines.append(f"## SOURCE {idx}: {assessment.source.name}")
        lines.append(f"Type: {assessment.source.source_type.value}")
        lines.append(f"Records: {assessment.source.record_count:,}")
        lines.append(f"Lawful Basis: {assessment.source.lawful_basis.value}")
        lines.append(f"Status: {assessment.status.value}")
        lines.append(f"Lawful Basis Valid: {'YES' if assessment.lawful_basis_valid else 'NO'}")

        if assessment.risk_factors:
            lines.append("\nRisk Factors:")
            for rf in assessment.risk_factors:
                lines.append(f"  - {rf}")

        if assessment.issues:
            lines.append("\nIssues:")
            for issue in assessment.issues:
                lines.append(f"  - {issue}")

        if assessment.recommendations:
            lines.append("\nRecommendations:")
            for rec in assessment.recommendations:
                lines.append(f"  - {rec}")

        if assessment.balancing_test and assessment.balancing_test.outcome:
            lines.append(f"\nBalancing Test Outcome: {assessment.balancing_test.outcome.value}")

    lines.append(f"\n{'='*80}")
    lines.append("OVERALL RECOMMENDATIONS:")
    if non_compliant > 0:
        lines.append(
            f"  - {non_compliant} source(s) non-compliant: remediate or exclude from training pipeline before model training"
        )
    if conditional > 0:
        lines.append(
            f"  - {conditional} source(s) conditionally compliant: address identified issues to achieve full compliance"
        )
    lines.append("  - Maintain training data catalogue with lawful basis documentation per source")
    lines.append("  - Review assessments when EDPB or national DPA guidance is updated")
    lines.append("  - Reassess lawful basis when training purpose or scope changes")

    return "\n".join(lines)


def demo_cerebrum_ai_labs():
    source1 = DataSource(
        name="Customer Service Transcripts",
        source_type=SourceType.FIRST_PARTY,
        description="Customer support chat transcripts from Cerebrum AI Labs platform",
        data_categories=["names", "email_addresses", "support_queries", "account_details"],
        record_count=850_000,
        contains_special_category=False,
        original_collection_purpose="Customer support service delivery",
        ai_training_disclosed=False,
        lawful_basis=LawfulBasis.LEGITIMATE_INTEREST,
    )

    li_test1 = LegitimateInterestTest(
        interest_description="Training customer support AI to improve response quality and reduce resolution time",
        interest_is_specific=True,
        necessity_anonymised_tested=True,
        necessity_synthetic_tested=False,
        necessity_minimum_dataset_determined=True,
        balance_data_subject_impact="low",
        balance_expectations_met="partially_met",
        balance_safeguards_level="adequate",
        balance_opt_out_available=True,
        balance_transparency_provided=False,
    )

    source2 = DataSource(
        name="Common Crawl Web Extract",
        source_type=SourceType.WEB_SCRAPED,
        description="Web-scraped text data from Common Crawl for language model training",
        data_categories=["names", "email_addresses", "social_profiles", "published_content"],
        record_count=50_000_000,
        contains_special_category=True,
        special_category_types=["health_data", "political_opinions", "religious_beliefs"],
        original_collection_purpose="N/A - web scraping",
        ai_training_disclosed=False,
        lawful_basis=LawfulBasis.LEGITIMATE_INTEREST,
        pii_filtering_applied=False,
        differential_privacy_applied=False,
    )

    li_test2 = LegitimateInterestTest(
        interest_description="Training foundation language model for general-purpose text generation",
        interest_is_specific=False,
        necessity_anonymised_tested=False,
        necessity_synthetic_tested=False,
        necessity_minimum_dataset_determined=False,
        balance_data_subject_impact="medium",
        balance_expectations_met="not_met",
        balance_special_category_involved=True,
        balance_safeguards_level="insufficient",
        balance_opt_out_available=False,
        balance_transparency_provided=False,
    )

    source3 = DataSource(
        name="Licensed Medical Records Dataset",
        source_type=SourceType.THIRD_PARTY,
        description="De-identified medical records from healthcare data provider",
        data_categories=["diagnosis_codes", "treatment_records", "demographics", "lab_results"],
        record_count=2_000_000,
        contains_special_category=True,
        special_category_types=["health_data"],
        original_collection_purpose="Healthcare delivery and clinical research",
        ai_training_disclosed=False,
        lawful_basis=LawfulBasis.CONSENT,
        art9_condition="Art. 9(2)(a) - Explicit consent",
        consent_covers_ai_training=False,
        consent_is_specific=False,
        upstream_basis_verified=True,
        licence_permits_ai_training=True,
        compatibility_assessed=False,
    )

    source4 = DataSource(
        name="User Feedback Submissions",
        source_type=SourceType.USER_CONTRIBUTED,
        description="Voluntary feedback and ratings submitted by platform users",
        data_categories=["user_ids", "feedback_text", "ratings", "timestamps"],
        record_count=200_000,
        contains_special_category=False,
        original_collection_purpose="Product improvement and user experience research",
        ai_training_disclosed=True,
        lawful_basis=LawfulBasis.CONSENT,
        consent_covers_ai_training=True,
        consent_is_specific=True,
        consent_is_withdrawable=True,
    )

    assessments = [
        assess_source(source1, li_test1),
        assess_source(source2, li_test2),
        assess_source(source3),
        assess_source(source4),
    ]

    report = format_assessment_report(assessments, "Cerebrum AI Labs")
    print(report)


if __name__ == "__main__":
    demo_cerebrum_ai_labs()
