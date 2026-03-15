"""
NIST Privacy Framework CONTROL Function — Data Management Processor

Implements data lifecycle controls, retention enforcement, and
de-identification assessment aligned with CT.DM, CT.DP, and CT.PO.
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Optional
import json
import uuid


class LifecycleStage(Enum):
    COLLECTION = "collection"
    STORAGE = "storage"
    PROCESSING = "processing"
    SHARING = "sharing"
    RETENTION = "retention"
    DELETION = "deletion"


class DeidentificationTechnique(Enum):
    PSEUDONYMIZATION = "pseudonymization"
    K_ANONYMITY = "k_anonymity"
    L_DIVERSITY = "l_diversity"
    T_CLOSENESS = "t_closeness"
    DIFFERENTIAL_PRIVACY = "differential_privacy"
    DATA_MASKING = "data_masking"
    GENERALIZATION = "generalization"
    SUPPRESSION = "suppression"
    SYNTHETIC_DATA = "synthetic_data"


class RetentionStatus(Enum):
    WITHIN_PERIOD = "within_period"
    APPROACHING_EXPIRY = "approaching_expiry"
    EXPIRED = "expired"
    LEGAL_HOLD = "legal_hold"


@dataclass
class RetentionRule:
    data_category: str
    retention_days: int
    legal_basis: str
    deletion_method: str
    verification_method: str
    exceptions: list[str] = field(default_factory=list)


@dataclass
class DataRecord:
    record_id: str
    data_category: str
    created_date: datetime
    last_accessed: datetime
    retention_rule: RetentionRule
    legal_hold: bool = False
    hold_reason: Optional[str] = None


@dataclass
class RetentionAuditResult:
    total_records: int
    within_period: int
    approaching_expiry: int
    expired: int
    legal_hold: int
    expired_records: list[dict]


class RetentionEnforcer:
    """
    Enforce data retention schedules and identify records
    that have exceeded their retention period.
    """

    def __init__(self, rules: list[RetentionRule]):
        self.rules = {r.data_category: r for r in rules}

    def check_record_status(self, record: DataRecord) -> RetentionStatus:
        """Check the retention status of a single record."""
        if record.legal_hold:
            return RetentionStatus.LEGAL_HOLD

        rule = self.rules.get(record.data_category)
        if not rule:
            return RetentionStatus.WITHIN_PERIOD

        expiry_date = record.created_date + timedelta(days=rule.retention_days)
        now = datetime.now(timezone.utc)
        warning_date = expiry_date - timedelta(days=30)

        if now >= expiry_date:
            return RetentionStatus.EXPIRED
        elif now >= warning_date:
            return RetentionStatus.APPROACHING_EXPIRY
        else:
            return RetentionStatus.WITHIN_PERIOD

    def audit_retention(self, records: list[DataRecord]) -> RetentionAuditResult:
        """Audit all records against retention schedules."""
        within = approaching = expired = hold = 0
        expired_records = []

        for record in records:
            status = self.check_record_status(record)
            if status == RetentionStatus.WITHIN_PERIOD:
                within += 1
            elif status == RetentionStatus.APPROACHING_EXPIRY:
                approaching += 1
            elif status == RetentionStatus.EXPIRED:
                expired += 1
                rule = self.rules.get(record.data_category)
                expired_records.append({
                    "record_id": record.record_id,
                    "data_category": record.data_category,
                    "created_date": record.created_date.isoformat(),
                    "retention_days": rule.retention_days if rule else "unknown",
                    "days_overdue": (
                        datetime.now(timezone.utc) - (record.created_date + timedelta(days=rule.retention_days))
                    ).days if rule else 0,
                })
            elif status == RetentionStatus.LEGAL_HOLD:
                hold += 1

        return RetentionAuditResult(
            total_records=len(records),
            within_period=within,
            approaching_expiry=approaching,
            expired=expired,
            legal_hold=hold,
            expired_records=expired_records,
        )


class DeidentificationAssessor:
    """
    Assess and recommend de-identification techniques based on use case.
    """

    TECHNIQUE_PROFILES = {
        DeidentificationTechnique.PSEUDONYMIZATION: {
            "identifiability_reduction": "medium",
            "data_utility": "high",
            "computational_cost": "low",
            "reversible": True,
            "best_for": ["internal analytics", "testing environments"],
        },
        DeidentificationTechnique.K_ANONYMITY: {
            "identifiability_reduction": "medium-high",
            "data_utility": "medium",
            "computational_cost": "medium",
            "reversible": False,
            "best_for": ["data sharing", "public datasets"],
        },
        DeidentificationTechnique.DIFFERENTIAL_PRIVACY: {
            "identifiability_reduction": "very_high",
            "data_utility": "medium",
            "computational_cost": "medium",
            "reversible": False,
            "best_for": ["aggregate queries", "statistical publishing", "census"],
        },
        DeidentificationTechnique.SYNTHETIC_DATA: {
            "identifiability_reduction": "very_high",
            "data_utility": "variable",
            "computational_cost": "high",
            "reversible": False,
            "best_for": ["ML training", "testing", "third-party sharing"],
        },
    }

    def recommend_technique(
        self,
        external_sharing: bool,
        utility_requirement: str,
        reversibility_needed: bool,
    ) -> list[dict]:
        """Recommend de-identification techniques based on requirements."""
        recommendations = []

        for technique, profile in self.TECHNIQUE_PROFILES.items():
            score = 0

            if external_sharing and profile["identifiability_reduction"] in ("very_high", "high"):
                score += 3
            elif not external_sharing:
                score += 1

            if utility_requirement == "high" and profile["data_utility"] in ("high", "very_high"):
                score += 3
            elif utility_requirement == "medium" and profile["data_utility"] in ("medium", "high"):
                score += 2

            if reversibility_needed and profile["reversible"]:
                score += 2
            elif not reversibility_needed and not profile["reversible"]:
                score += 1

            recommendations.append({
                "technique": technique.value,
                "score": score,
                "profile": profile,
            })

        return sorted(recommendations, key=lambda r: r["score"], reverse=True)


if __name__ == "__main__":
    rules = [
        RetentionRule("customer_transactions", 2555, "Tax regulations (7 years)", "secure_overwrite", "automated_audit"),
        RetentionRule("marketing_consent", 1095, "Legitimate interest (3 years)", "logical_deletion", "annual_review"),
        RetentionRule("website_analytics", 790, "Consent (26 months)", "automated_purge", "monthly_check"),
        RetentionRule("support_tickets", 1095, "Contract performance (3 years)", "secure_overwrite", "quarterly_audit"),
    ]

    enforcer = RetentionEnforcer(rules)

    sample_records = [
        DataRecord("rec-001", "website_analytics", datetime(2023, 6, 1, tzinfo=timezone.utc), datetime(2025, 1, 1, tzinfo=timezone.utc), rules[2]),
        DataRecord("rec-002", "customer_transactions", datetime(2025, 1, 15, tzinfo=timezone.utc), datetime(2025, 12, 1, tzinfo=timezone.utc), rules[0]),
        DataRecord("rec-003", "support_tickets", datetime(2022, 3, 1, tzinfo=timezone.utc), datetime(2022, 4, 1, tzinfo=timezone.utc), rules[3]),
    ]

    result = enforcer.audit_retention(sample_records)
    print(f"Retention Audit: {result.total_records} records, {result.expired} expired")

    assessor = DeidentificationAssessor()
    recs = assessor.recommend_technique(external_sharing=True, utility_requirement="medium", reversibility_needed=False)
    print(f"\nTop recommendation: {recs[0]['technique']} (score: {recs[0]['score']})")
