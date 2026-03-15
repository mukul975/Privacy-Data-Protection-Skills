#!/usr/bin/env python3
"""
Vendor Privacy Risk Scoring — Risk Calculation and Tiering Engine

Implements multi-dimensional vendor risk scoring, weighted risk calculation,
tier assignment, and risk trend tracking per GDPR risk-based approach.
"""

import json
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class RiskTier(Enum):
    TIER_1_HIGH = "tier_1_high"
    TIER_2_STANDARD = "tier_2_standard"
    TIER_3_LOW = "tier_3_low"


class EscalationTrigger(Enum):
    BREACH = "personal_data_breach"
    ENFORCEMENT = "regulatory_enforcement"
    CERT_LAPSE = "certification_lapse"
    SERVICE_CHANGE = "material_service_change"
    CRITICAL_FINDING = "critical_audit_finding"


DIMENSION_WEIGHTS = {
    "data_volume": 0.15,
    "data_sensitivity": 0.25,
    "transfer_locations": 0.15,
    "certifications": 0.15,
    "breach_history": 0.10,
    "control_maturity": 0.10,
    "processing_autonomy": 0.10,
}

TIER_THRESHOLDS = {
    RiskTier.TIER_1_HIGH: 3.5,
    RiskTier.TIER_2_STANDARD: 2.5,
}

OVERSIGHT_REQUIREMENTS = {
    RiskTier.TIER_1_HIGH: {
        "due_diligence_refresh": "annual",
        "audit_type": "remote_technical_or_on_site",
        "audit_frequency": "annual",
        "sub_processor_review": "quarterly",
        "dpa_review": "annual",
        "risk_recalculation": "semi_annual",
        "monitoring": "continuous_active",
    },
    RiskTier.TIER_2_STANDARD: {
        "due_diligence_refresh": "biennial",
        "audit_type": "documentation_review",
        "audit_frequency": "annual",
        "sub_processor_review": "semi_annual",
        "dpa_review": "biennial",
        "risk_recalculation": "annual",
        "monitoring": "periodic",
    },
    RiskTier.TIER_3_LOW: {
        "due_diligence_refresh": "triennial",
        "audit_type": "documentation_review",
        "audit_frequency": "biennial",
        "sub_processor_review": "annual",
        "dpa_review": "triennial",
        "risk_recalculation": "biennial",
        "monitoring": "annual_check",
    },
}


@dataclass
class DimensionScore:
    """Score for a single risk dimension."""
    dimension: str = ""
    score: int = 1  # 1-5
    justification: str = ""
    scored_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class VendorRiskScore:
    """Complete risk scoring record for a vendor."""
    score_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_id: str = ""
    vendor_name: str = ""
    dimension_scores: dict = field(default_factory=dict)
    weighted_score: float = 0.0
    risk_tier: str = RiskTier.TIER_2_STANDARD.value
    override_applied: bool = False
    override_reason: str = ""
    scored_by: str = ""
    approved_by: str = ""
    scored_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    next_recalculation: Optional[str] = None
    escalation_active: bool = False
    escalation_trigger: Optional[str] = None
    escalation_date: Optional[str] = None


@dataclass
class RiskHistory:
    """Historical record of vendor risk score changes."""
    vendor_id: str = ""
    score_date: str = ""
    weighted_score: float = 0.0
    risk_tier: str = ""
    change_reason: str = ""


class VendorRiskScoringEngine:
    """
    Calculates and manages vendor privacy risk scores, tier assignments,
    and risk trend monitoring.
    """

    def __init__(self):
        self.risk_scores: dict[str, VendorRiskScore] = {}
        self.risk_history: list[RiskHistory] = []

    def score_data_volume(self, subject_count: int) -> int:
        """Score data volume dimension based on data subject count."""
        if subject_count > 100000:
            return 5
        elif subject_count > 10000:
            return 4
        elif subject_count > 1000:
            return 3
        elif subject_count > 100:
            return 2
        return 1

    def score_data_sensitivity(
        self, has_special_category: bool, has_government_ids: bool,
        has_behavioral: bool, has_basic_pii: bool
    ) -> int:
        """Score data sensitivity dimension."""
        if has_special_category:
            return 5
        elif has_government_ids:
            return 4
        elif has_behavioral:
            return 3
        elif has_basic_pii:
            return 2
        return 1

    def score_transfer_locations(
        self, eea_only: bool, adequacy_only: bool,
        has_sccs: bool, surveillance_jurisdiction: bool
    ) -> int:
        """Score transfer location dimension."""
        if surveillance_jurisdiction:
            return 4
        elif has_sccs and not eea_only and not adequacy_only:
            return 3
        elif adequacy_only and not eea_only:
            return 2
        elif eea_only:
            return 1
        return 5

    def score_certifications(self, certifications: list[str]) -> int:
        """Score certifications dimension (inverse — more certs = lower risk)."""
        cert_set = {c.lower() for c in certifications}

        has_27001 = any("27001" in c for c in cert_set)
        has_27701 = any("27701" in c for c in cert_set)
        has_soc2 = any("soc 2" in c or "soc2" in c for c in cert_set)
        has_sector = any(
            term in c for c in cert_set
            for term in ["27018", "27017", "csa star level 2", "hitrust"]
        )

        if has_27001 and has_27701 and has_soc2:
            return 1
        elif has_27001 and has_soc2:
            return 2
        elif has_27001 or has_soc2:
            return 3
        elif any("star" in c or "self-assessment" in c for c in cert_set):
            return 4
        return 5

    def score_breach_history(
        self, breach_count_5yr: int, enforcement_actions: int,
        adequate_response: bool
    ) -> int:
        """Score breach and enforcement history dimension."""
        if enforcement_actions > 0 or breach_count_5yr > 2:
            return 5
        elif breach_count_5yr == 2 or (breach_count_5yr == 1 and not adequate_response):
            return 4
        elif breach_count_5yr == 1 and adequate_response:
            return 3
        elif breach_count_5yr == 0 and enforcement_actions == 0:
            return 1
        return 2

    def calculate_weighted_score(self, dimensions: dict[str, int]) -> float:
        """Calculate the weighted risk score from dimension scores."""
        weighted = sum(
            dimensions.get(dim, 3) * weight
            for dim, weight in DIMENSION_WEIGHTS.items()
        )
        return round(weighted, 2)

    def assign_tier(self, weighted_score: float) -> RiskTier:
        """Assign risk tier based on weighted score."""
        if weighted_score >= TIER_THRESHOLDS[RiskTier.TIER_1_HIGH]:
            return RiskTier.TIER_1_HIGH
        elif weighted_score >= TIER_THRESHOLDS[RiskTier.TIER_2_STANDARD]:
            return RiskTier.TIER_2_STANDARD
        return RiskTier.TIER_3_LOW

    def score_vendor(
        self,
        vendor_id: str,
        vendor_name: str,
        dimensions: dict[str, DimensionScore],
        scored_by: str,
    ) -> VendorRiskScore:
        """Calculate and record complete risk score for a vendor."""
        dim_values = {dim: ds.score for dim, ds in dimensions.items()}
        weighted = self.calculate_weighted_score(dim_values)
        tier = self.assign_tier(weighted)

        recalc_months = 6 if tier == RiskTier.TIER_1_HIGH else (12 if tier == RiskTier.TIER_2_STANDARD else 24)

        risk_score = VendorRiskScore(
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            dimension_scores={dim: asdict(ds) for dim, ds in dimensions.items()},
            weighted_score=weighted,
            risk_tier=tier.value,
            scored_by=scored_by,
            next_recalculation=(
                datetime.now(timezone.utc) + timedelta(days=recalc_months * 30)
            ).isoformat(),
        )

        self.risk_scores[vendor_id] = risk_score
        self.risk_history.append(RiskHistory(
            vendor_id=vendor_id,
            score_date=risk_score.scored_date,
            weighted_score=weighted,
            risk_tier=tier.value,
            change_reason="Initial scoring" if not any(
                h.vendor_id == vendor_id for h in self.risk_history
            ) else "Periodic recalculation",
        ))

        return risk_score

    def escalate_vendor(
        self, vendor_id: str, trigger: EscalationTrigger
    ) -> VendorRiskScore:
        """Temporarily escalate vendor risk tier by one level."""
        risk_score = self.risk_scores.get(vendor_id)
        if not risk_score:
            raise ValueError(f"No risk score found for vendor {vendor_id}")

        current_tier = RiskTier(risk_score.risk_tier)
        if current_tier == RiskTier.TIER_3_LOW:
            new_tier = RiskTier.TIER_2_STANDARD
        elif current_tier == RiskTier.TIER_2_STANDARD:
            new_tier = RiskTier.TIER_1_HIGH
        else:
            new_tier = RiskTier.TIER_1_HIGH

        risk_score.risk_tier = new_tier.value
        risk_score.escalation_active = True
        risk_score.escalation_trigger = trigger.value
        risk_score.escalation_date = datetime.now(timezone.utc).isoformat()

        self.risk_history.append(RiskHistory(
            vendor_id=vendor_id,
            score_date=datetime.now(timezone.utc).isoformat(),
            weighted_score=risk_score.weighted_score,
            risk_tier=new_tier.value,
            change_reason=f"Escalation: {trigger.value}",
        ))

        return risk_score

    def get_oversight_requirements(self, vendor_id: str) -> dict:
        """Get tier-based oversight requirements for a vendor."""
        risk_score = self.risk_scores.get(vendor_id)
        if not risk_score:
            raise ValueError(f"No risk score found for vendor {vendor_id}")

        tier = RiskTier(risk_score.risk_tier)
        requirements = OVERSIGHT_REQUIREMENTS[tier].copy()
        requirements["vendor_name"] = risk_score.vendor_name
        requirements["risk_tier"] = tier.value
        requirements["weighted_score"] = risk_score.weighted_score
        requirements["escalation_active"] = risk_score.escalation_active
        return requirements

    def get_risk_dashboard(self) -> dict:
        """Generate aggregated risk dashboard."""
        total = len(self.risk_scores)
        if total == 0:
            return {"total_vendors": 0}

        scores = list(self.risk_scores.values())
        tier_counts = {tier.value: 0 for tier in RiskTier}
        for s in scores:
            tier_counts[s.risk_tier] += 1

        avg_score = round(sum(s.weighted_score for s in scores) / total, 2)

        now = datetime.now(timezone.utc).isoformat()
        overdue = [
            s.vendor_name for s in scores
            if s.next_recalculation and s.next_recalculation < now
        ]

        return {
            "total_vendors": total,
            "tier_distribution": tier_counts,
            "average_risk_score": avg_score,
            "escalations_active": len([s for s in scores if s.escalation_active]),
            "overdue_recalculations": overdue,
            "as_of": now,
        }


if __name__ == "__main__":
    engine = VendorRiskScoringEngine()

    # Score NimbusAnalytics GmbH
    nimbus_dimensions = {
        "data_volume": DimensionScore(
            dimension="data_volume", score=4,
            justification="~70,000 data subjects (Summit enterprise + trial + API users)",
        ),
        "data_sensitivity": DimensionScore(
            dimension="data_sensitivity", score=3,
            justification="Behavioral data (usage patterns, session data) + IP-derived location",
        ),
        "transfer_locations": DimensionScore(
            dimension="transfer_locations", score=1,
            justification="Processing exclusively within EEA (Germany + Ireland)",
        ),
        "certifications": DimensionScore(
            dimension="certifications", score=2,
            justification="ISO 27001:2022 + SOC 2 Type II — strong but no ISO 27701",
        ),
        "breach_history": DimensionScore(
            dimension="breach_history", score=1,
            justification="No breaches or enforcement actions in past 5 years",
        ),
        "control_maturity": DimensionScore(
            dimension="control_maturity", score=2,
            justification="Managed controls with regular testing, documented procedures",
        ),
        "processing_autonomy": DimensionScore(
            dimension="processing_autonomy", score=3,
            justification="Processor selects technical means for analytics processing",
        ),
    }

    nimbus_score = engine.score_vendor(
        vendor_id="nimbus-001",
        vendor_name="NimbusAnalytics GmbH",
        dimensions=nimbus_dimensions,
        scored_by="Sarah Chen, Privacy Analyst",
    )
    print(f"NimbusAnalytics — Score: {nimbus_score.weighted_score}, Tier: {nimbus_score.risk_tier}")

    # Score a higher-risk vendor: CloudMetrics US Inc.
    cloudmetrics_dimensions = {
        "data_volume": DimensionScore(
            dimension="data_volume", score=5,
            justification="~200,000 data subjects across global customer base",
        ),
        "data_sensitivity": DimensionScore(
            dimension="data_sensitivity", score=4,
            justification="Processes government IDs for identity verification",
        ),
        "transfer_locations": DimensionScore(
            dimension="transfer_locations", score=4,
            justification="US processing with SCCs but US surveillance risk per Schrems II",
        ),
        "certifications": DimensionScore(
            dimension="certifications", score=3,
            justification="SOC 2 Type II only — no ISO 27001",
        ),
        "breach_history": DimensionScore(
            dimension="breach_history", score=3,
            justification="One breach in 2024, adequately responded with prompt notification",
        ),
        "control_maturity": DimensionScore(
            dimension="control_maturity", score=3,
            justification="Defined procedures and periodic testing, some documentation gaps",
        ),
        "processing_autonomy": DimensionScore(
            dimension="processing_autonomy", score=4,
            justification="Significant discretion in identity verification processing logic",
        ),
    }

    cm_score = engine.score_vendor(
        vendor_id="cloudmetrics-001",
        vendor_name="CloudMetrics US Inc.",
        dimensions=cloudmetrics_dimensions,
        scored_by="Sarah Chen, Privacy Analyst",
    )
    print(f"CloudMetrics — Score: {cm_score.weighted_score}, Tier: {cm_score.risk_tier}")

    # Get oversight requirements
    nimbus_oversight = engine.get_oversight_requirements("nimbus-001")
    print(f"\nNimbusAnalytics Oversight: {json.dumps(nimbus_oversight, indent=2)}")

    cm_oversight = engine.get_oversight_requirements("cloudmetrics-001")
    print(f"\nCloudMetrics Oversight: {json.dumps(cm_oversight, indent=2)}")

    # Simulate breach escalation for CloudMetrics
    engine.escalate_vendor("cloudmetrics-001", EscalationTrigger.BREACH)
    print(f"\nCloudMetrics post-escalation tier: {engine.risk_scores['cloudmetrics-001'].risk_tier}")

    # Dashboard
    dashboard = engine.get_risk_dashboard()
    print(f"\n=== Vendor Risk Dashboard ===")
    print(json.dumps(dashboard, indent=2))
