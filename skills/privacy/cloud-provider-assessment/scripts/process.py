#!/usr/bin/env python3
"""
Cloud Provider Privacy Assessment — Assessment and Scoring Engine

Implements cloud-specific privacy assessment covering data residency,
multi-tenancy isolation, ISO 27018 compliance, CSA STAR evaluation,
SOC 2 Privacy criterion, and shared responsibility mapping.
"""

import json
import uuid
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class CloudServiceModel(Enum):
    IAAS = "iaas"
    PAAS = "paas"
    SAAS = "saas"


class CSAStarLevel(Enum):
    NONE = "none"
    LEVEL_1 = "level_1_self_assessment"
    LEVEL_2 = "level_2_third_party_audit"
    LEVEL_3 = "level_3_continuous_monitoring"


class AssessmentDecision(Enum):
    APPROVED = "approved"
    CONDITIONAL = "conditional"
    REJECTED = "rejected"


DOMAIN_WEIGHTS = {
    "data_residency": 0.20,
    "multi_tenancy": 0.20,
    "iso_27018": 0.15,
    "csa_star": 0.15,
    "soc2_privacy": 0.15,
    "shared_responsibility": 0.15,
}


@dataclass
class CloudProviderProfile:
    """Cloud service provider profile."""
    provider_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = ""
    service_name: str = ""
    service_model: str = CloudServiceModel.SAAS.value
    headquarters: str = ""
    available_regions: list[str] = field(default_factory=list)
    certifications: list[str] = field(default_factory=list)
    csa_star_level: str = CSAStarLevel.NONE.value
    soc2_includes_privacy: bool = False
    iso_27018_certified: bool = False
    customer_managed_keys: bool = False
    region_lock_capability: bool = False
    government_access_notification: bool = False
    sub_processors: list[dict] = field(default_factory=list)


@dataclass
class DataResidencyAssessment:
    """Assessment of data residency and sovereignty controls."""
    data_at_rest_regions: list[str] = field(default_factory=list)
    data_processing_regions: list[str] = field(default_factory=list)
    backup_dr_regions: list[str] = field(default_factory=list)
    metadata_telemetry_regions: list[str] = field(default_factory=list)
    support_access_countries: list[str] = field(default_factory=list)
    region_lock_enabled: bool = False
    third_country_transfers: bool = False
    transfer_mechanisms: list[str] = field(default_factory=list)
    score: int = 0
    notes: str = ""


@dataclass
class SharedResponsibilityMapping:
    """Maps control responsibilities between controller and provider."""
    control_domain: str = ""
    controller_responsibility: str = ""
    provider_responsibility: str = ""
    gap_identified: bool = False
    gap_description: str = ""
    supplementary_measure: str = ""


@dataclass
class CloudAssessment:
    """Complete cloud provider privacy assessment."""
    assessment_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    provider_id: str = ""
    provider_name: str = ""
    service_model: str = ""
    assessment_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    assessor: str = ""
    data_residency: Optional[dict] = None
    multi_tenancy_score: int = 0
    multi_tenancy_notes: str = ""
    iso_27018_score: int = 0
    iso_27018_notes: str = ""
    csa_star_score: int = 0
    csa_star_notes: str = ""
    soc2_privacy_score: int = 0
    soc2_privacy_notes: str = ""
    shared_responsibility_score: int = 0
    shared_responsibility_mappings: list[dict] = field(default_factory=list)
    domain_scores: dict = field(default_factory=dict)
    weighted_score: float = 0.0
    decision: str = ""
    conditions: list[str] = field(default_factory=list)
    supplementary_measures: list[str] = field(default_factory=list)


class CloudProviderAssessmentEngine:
    """
    Manages cloud provider privacy assessments including data residency,
    multi-tenancy, certification evaluation, and shared responsibility mapping.
    """

    def __init__(self):
        self.providers: dict[str, CloudProviderProfile] = {}
        self.assessments: dict[str, CloudAssessment] = {}

    def register_provider(self, provider: CloudProviderProfile) -> str:
        self.providers[provider.provider_id] = provider
        return provider.provider_id

    def score_csa_star(self, level: CSAStarLevel) -> int:
        """Score CSA STAR certification level."""
        scores = {
            CSAStarLevel.NONE: 1,
            CSAStarLevel.LEVEL_1: 2,
            CSAStarLevel.LEVEL_2: 4,
            CSAStarLevel.LEVEL_3: 5,
        }
        return scores.get(level, 1)

    def score_iso_27018(self, certified: bool, scope_covers_service: bool) -> int:
        """Score ISO 27018 certification status."""
        if certified and scope_covers_service:
            return 5
        elif certified:
            return 3
        return 1

    def assess_data_residency(
        self, data_regions: list[str], support_countries: list[str],
        region_locked: bool
    ) -> int:
        """Score data residency based on processing locations."""
        eea_plus = {
            "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
            "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
            "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta",
            "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia",
            "Spain", "Sweden", "Iceland", "Liechtenstein", "Norway", "Switzerland",
        }

        all_locations = set(data_regions + support_countries)
        non_eea = all_locations - eea_plus

        if not non_eea and region_locked:
            return 5
        elif not non_eea:
            return 4
        elif len(non_eea) <= 2:
            return 3
        elif len(non_eea) <= 5:
            return 2
        return 1

    def create_assessment(
        self, provider_id: str, assessor: str,
        domain_scores: dict, shared_responsibility: list[SharedResponsibilityMapping],
        conditions: list[str] = None, supplementary_measures: list[str] = None,
    ) -> CloudAssessment:
        """Create and score a complete cloud provider assessment."""
        provider = self.providers.get(provider_id)
        if not provider:
            raise ValueError(f"Provider {provider_id} not found")

        assessment = CloudAssessment(
            provider_id=provider_id,
            provider_name=provider.provider_name,
            service_model=provider.service_model,
            assessor=assessor,
            domain_scores=domain_scores,
            shared_responsibility_mappings=[asdict(m) for m in shared_responsibility],
            conditions=conditions or [],
            supplementary_measures=supplementary_measures or [],
        )

        weighted = sum(
            domain_scores.get(domain, 3) * weight
            for domain, weight in DOMAIN_WEIGHTS.items()
        )
        assessment.weighted_score = round(weighted, 2)

        if assessment.weighted_score >= 4.0:
            assessment.decision = AssessmentDecision.APPROVED.value
        elif assessment.weighted_score >= 3.0:
            assessment.decision = AssessmentDecision.CONDITIONAL.value
        else:
            assessment.decision = AssessmentDecision.REJECTED.value

        self.assessments[assessment.assessment_id] = assessment
        return assessment

    def get_assessment_summary(self, assessment_id: str) -> dict:
        """Generate assessment summary."""
        a = self.assessments.get(assessment_id)
        if not a:
            raise ValueError(f"Assessment {assessment_id} not found")

        gaps = [
            m for m in a.shared_responsibility_mappings
            if m.get("gap_identified")
        ]

        return {
            "assessment_id": a.assessment_id,
            "provider": a.provider_name,
            "service_model": a.service_model,
            "assessment_date": a.assessment_date,
            "domain_scores": a.domain_scores,
            "weighted_score": a.weighted_score,
            "decision": a.decision,
            "conditions": a.conditions,
            "supplementary_measures": a.supplementary_measures,
            "shared_responsibility_gaps": len(gaps),
            "assessor": a.assessor,
        }


if __name__ == "__main__":
    engine = CloudProviderAssessmentEngine()

    # Register AWS as cloud provider
    aws = CloudProviderProfile(
        provider_name="Amazon Web Services EMEA SARL",
        service_name="AWS EU (Frankfurt + Ireland)",
        service_model=CloudServiceModel.IAAS.value,
        headquarters="Luxembourg",
        available_regions=["eu-central-1 (Frankfurt)", "eu-west-1 (Ireland)", "eu-west-2 (London)"],
        certifications=["ISO 27001", "ISO 27017", "ISO 27018", "SOC 2 Type II", "CSA STAR Level 2"],
        csa_star_level=CSAStarLevel.LEVEL_2.value,
        soc2_includes_privacy=True,
        iso_27018_certified=True,
        customer_managed_keys=True,
        region_lock_capability=True,
        government_access_notification=True,
        sub_processors=[
            {"name": "Amazon.com, Inc.", "location": "USA", "function": "Parent company engineering support"},
        ],
    )
    engine.register_provider(aws)

    # Perform assessment
    shared_resp = [
        SharedResponsibilityMapping(
            control_domain="Data encryption at rest",
            controller_responsibility="Configure KMS keys, select encryption policy",
            provider_responsibility="Provide KMS infrastructure, implement AES-256",
            gap_identified=False,
        ),
        SharedResponsibilityMapping(
            control_domain="Access management (application)",
            controller_responsibility="Define IAM policies, manage user access",
            provider_responsibility="Provide IAM platform, enforce policies",
            gap_identified=False,
        ),
        SharedResponsibilityMapping(
            control_domain="Incident detection (application layer)",
            controller_responsibility="Configure CloudTrail, GuardDuty, application monitoring",
            provider_responsibility="Provide monitoring infrastructure, detect infrastructure threats",
            gap_identified=True,
            gap_description="Summit must configure application-level monitoring; AWS only monitors infrastructure",
            supplementary_measure="Deploy Summit SIEM integration with CloudTrail and GuardDuty",
        ),
        SharedResponsibilityMapping(
            control_domain="Data deletion at termination",
            controller_responsibility="Initiate deletion process, verify completion",
            provider_responsibility="Execute deletion on underlying storage",
            gap_identified=True,
            gap_description="AWS does not provide automated deletion certification",
            supplementary_measure="Implement script-based deletion verification and manual certification process",
        ),
    ]

    domain_scores = {
        "data_residency": 5,    # EEA-only with region lock
        "multi_tenancy": 4,     # Strong isolation with per-tenant KMS keys
        "iso_27018": 5,         # Certified with full scope coverage
        "csa_star": 4,          # Level 2 third-party audit
        "soc2_privacy": 4,      # SOC 2 Type II with Privacy criterion
        "shared_responsibility": 3,  # Gaps identified requiring supplementary measures
    }

    assessment = engine.create_assessment(
        provider_id=aws.provider_id,
        assessor="Sarah Chen, Privacy Analyst — Summit Cloud Partners",
        domain_scores=domain_scores,
        shared_responsibility=shared_resp,
        conditions=[
            "Summit must implement application-layer monitoring via SIEM integration",
            "Summit must implement script-based deletion verification process",
        ],
        supplementary_measures=[
            "Deploy CloudTrail-to-SIEM integration within 30 days of deployment",
            "Implement automated deletion verification script with certification logging",
            "Enable AWS Config rules for compliance monitoring of region restrictions",
        ],
    )

    summary = engine.get_assessment_summary(assessment.assessment_id)
    print("=== Cloud Provider Assessment Summary ===")
    print(json.dumps(summary, indent=2))
