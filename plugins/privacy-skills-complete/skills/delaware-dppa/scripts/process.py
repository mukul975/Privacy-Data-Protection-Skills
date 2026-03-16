#!/usr/bin/env python3
"""
Delaware DPPA Compliance Tool

Assesses DPPA applicability under 6 Del. C. §12D-103, processes consumer
rights requests per §12D-106, manages sensitive data consent per §12D-105,
and conducts data protection assessments per §12D-105(b).
"""

import json
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class RightType(Enum):
    ACCESS = "access"
    CORRECTION = "correction"
    DELETION = "deletion"
    PORTABILITY = "portability"
    OPT_OUT_TARGETED_ADS = "opt_out_targeted_advertising"
    OPT_OUT_SALE = "opt_out_sale"
    OPT_OUT_PROFILING = "opt_out_profiling"
    APPEAL = "appeal"


class RequestStatus(Enum):
    RECEIVED = "received"
    VERIFYING = "identity_verification"
    PROCESSING = "processing"
    EXTENDED = "extended"
    COMPLETED = "completed"
    DENIED = "denied"
    APPEALED = "appealed"
    APPEAL_UPHELD = "appeal_upheld"
    APPEAL_DENIED = "appeal_denied"


class SensitiveCategory(Enum):
    RACIAL_ETHNIC = "racial_or_ethnic_origin"
    RELIGIOUS = "religious_beliefs"
    HEALTH = "health_diagnosis"
    SEXUAL_ORIENTATION = "sexual_orientation"
    CITIZENSHIP_IMMIGRATION = "citizenship_or_immigration_status"
    GENETIC = "genetic_data"
    BIOMETRIC = "biometric_data"
    CHILD_DATA = "known_child_under_13"
    PRECISE_GEOLOCATION = "precise_geolocation"


ENTITY_EXEMPTIONS = [
    "state_local_government",
    "glba_financial_institution",
    "hipaa_covered_entity",
    "hipaa_business_associate",
    "nonprofit_organization",
    "higher_education_institution",
    "national_securities_exchange",
]

DATA_EXEMPTIONS = [
    "hipaa_health_data",
    "glba_financial_data",
    "fcra_credit_data",
    "ferpa_education_records",
    "federal_dppa_driver_data",
    "farm_credit_act_data",
    "clinical_trial_data",
    "employment_context_data",
    "b2b_contact_data",
]

RESPONSE_DEADLINE_DAYS = 45
EXTENSION_DAYS = 45
APPEAL_DEADLINE_DAYS = 60
CONSUMER_THRESHOLD_A = 35_000
CONSUMER_THRESHOLD_B_COUNT = 10_000
CONSUMER_THRESHOLD_B_REVENUE_PCT = 20.0
CIVIL_PENALTY_PER_VIOLATION = 10_000
UNIVERSAL_OPT_OUT_EFFECTIVE = datetime(2026, 1, 1, tzinfo=timezone.utc)


@dataclass
class ApplicabilityResult:
    """Result of DPPA applicability assessment under §12D-103."""
    entity_name: str
    assessment_date: str
    entity_exempt: bool
    exemption_type: Optional[str]
    de_consumer_count: int
    payment_only_excluded: int
    net_consumer_count: int
    revenue_from_sale_pct: float
    threshold_a_met: bool
    threshold_b_met: bool
    dppa_applies: bool
    data_exemptions: list
    notes: str

    def to_dict(self) -> dict:
        return asdict(self)


def assess_applicability(
    entity_name: str,
    entity_type: str,
    de_consumer_count: int,
    payment_only_count: int,
    revenue_from_sale_pct: float,
    data_categories_exempt: Optional[list] = None,
) -> ApplicabilityResult:
    """
    Determine whether the DPPA applies to the entity under §12D-103.

    Args:
        entity_name: Name of the organization
        entity_type: Entity classification for exemption check
        de_consumer_count: Total Delaware consumers whose data is processed
        payment_only_count: Consumers whose data is processed solely for payments
        revenue_from_sale_pct: Percentage of gross revenue derived from data sale
        data_categories_exempt: List of data-level exemption categories
    """
    entity_exempt = entity_type in ENTITY_EXEMPTIONS
    net_count = de_consumer_count - payment_only_count
    threshold_a = net_count >= CONSUMER_THRESHOLD_A
    threshold_b = (
        net_count >= CONSUMER_THRESHOLD_B_COUNT
        and revenue_from_sale_pct > CONSUMER_THRESHOLD_B_REVENUE_PCT
    )
    applies = not entity_exempt and (threshold_a or threshold_b)

    notes_parts = []
    if entity_exempt:
        notes_parts.append(f"Entity exempt as {entity_type}")
    if threshold_a:
        notes_parts.append(
            f"Threshold A met: {net_count:,} >= {CONSUMER_THRESHOLD_A:,} consumers"
        )
    if threshold_b:
        notes_parts.append(
            f"Threshold B met: {net_count:,} consumers + "
            f"{revenue_from_sale_pct}% revenue from sale"
        )
    if not threshold_a and not threshold_b and not entity_exempt:
        notes_parts.append("Neither threshold met; DPPA does not apply")

    return ApplicabilityResult(
        entity_name=entity_name,
        assessment_date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        entity_exempt=entity_exempt,
        exemption_type=entity_type if entity_exempt else None,
        de_consumer_count=de_consumer_count,
        payment_only_excluded=payment_only_count,
        net_consumer_count=net_count,
        revenue_from_sale_pct=revenue_from_sale_pct,
        threshold_a_met=threshold_a,
        threshold_b_met=threshold_b,
        dppa_applies=applies,
        data_exemptions=data_categories_exempt or [],
        notes="; ".join(notes_parts),
    )


@dataclass
class ConsumerRequest:
    """Tracks a consumer rights request under §12D-106."""
    request_id: str
    consumer_id: str
    right_type: str
    status: str = RequestStatus.RECEIVED.value
    received_date: str = field(
        default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    )
    verification_method: Optional[str] = None
    verified: bool = False
    response_deadline: str = ""
    extended: bool = False
    extension_reason: Optional[str] = None
    response_date: Optional[str] = None
    denial_reason: Optional[str] = None
    appeal_filed: bool = False
    appeal_deadline: Optional[str] = None
    appeal_outcome: Optional[str] = None
    notes: str = ""

    def __post_init__(self):
        if not self.response_deadline:
            received = datetime.fromisoformat(
                self.received_date.replace("Z", "+00:00")
            )
            deadline = received + timedelta(days=RESPONSE_DEADLINE_DAYS)
            self.response_deadline = deadline.strftime("%Y-%m-%dT%H:%M:%SZ")

    def to_dict(self) -> dict:
        return asdict(self)


def create_request(
    request_id: str,
    consumer_id: str,
    right_type: RightType,
) -> ConsumerRequest:
    """Create a new consumer rights request."""
    return ConsumerRequest(
        request_id=request_id,
        consumer_id=consumer_id,
        right_type=right_type.value,
    )


def verify_identity(
    request: ConsumerRequest,
    method: str,
    data_points_matched: int,
) -> ConsumerRequest:
    """
    Verify consumer identity for the request.
    Access/portability (specific pieces) requires 3 data points + declaration.
    Other requests require 2 data points.
    Opt-out requests do not require verification.
    """
    request.verification_method = method
    request.status = RequestStatus.VERIFYING.value

    if request.right_type in (
        RightType.OPT_OUT_TARGETED_ADS.value,
        RightType.OPT_OUT_SALE.value,
        RightType.OPT_OUT_PROFILING.value,
    ):
        request.verified = True
        request.status = RequestStatus.PROCESSING.value
        request.notes = "Opt-out: no identity verification required"
        return request

    required_points = 2
    if request.right_type in (RightType.ACCESS.value, RightType.PORTABILITY.value):
        required_points = 3

    if data_points_matched >= required_points:
        request.verified = True
        request.status = RequestStatus.PROCESSING.value
    else:
        request.verified = False
        request.status = RequestStatus.DENIED.value
        request.denial_reason = (
            f"Identity verification failed: {data_points_matched} of "
            f"{required_points} required data points matched"
        )
    return request


def extend_deadline(
    request: ConsumerRequest,
    reason: str,
) -> ConsumerRequest:
    """Extend the response deadline by up to 45 additional days (§12D-106)."""
    if request.extended:
        request.notes += " Extension already applied; cannot extend again."
        return request

    current_deadline = datetime.fromisoformat(
        request.response_deadline.replace("Z", "+00:00")
    )
    new_deadline = current_deadline + timedelta(days=EXTENSION_DAYS)
    request.response_deadline = new_deadline.strftime("%Y-%m-%dT%H:%M:%SZ")
    request.extended = True
    request.extension_reason = reason
    request.status = RequestStatus.EXTENDED.value
    return request


def complete_request(
    request: ConsumerRequest,
) -> ConsumerRequest:
    """Mark a request as completed."""
    request.status = RequestStatus.COMPLETED.value
    request.response_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return request


def deny_request(
    request: ConsumerRequest,
    reason: str,
) -> ConsumerRequest:
    """Deny a request and inform of appeal right."""
    request.status = RequestStatus.DENIED.value
    request.denial_reason = reason
    request.response_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    request.notes += (
        " Consumer informed of right to appeal under §12D-106(f)."
    )
    return request


def file_appeal(
    request: ConsumerRequest,
) -> ConsumerRequest:
    """File an appeal on a denied request (§12D-106(f))."""
    if request.status != RequestStatus.DENIED.value:
        request.notes += " Cannot appeal: request was not denied."
        return request

    request.appeal_filed = True
    request.status = RequestStatus.APPEALED.value
    appeal_start = datetime.now(timezone.utc)
    deadline = appeal_start + timedelta(days=APPEAL_DEADLINE_DAYS)
    request.appeal_deadline = deadline.strftime("%Y-%m-%dT%H:%M:%SZ")
    return request


def resolve_appeal(
    request: ConsumerRequest,
    upheld: bool,
    reason: str,
) -> ConsumerRequest:
    """Resolve an appeal. If denied, inform consumer of right to contact AG."""
    if not request.appeal_filed:
        request.notes += " No appeal filed."
        return request

    if upheld:
        request.status = RequestStatus.APPEAL_UPHELD.value
        request.appeal_outcome = f"Upheld: {reason}"
    else:
        request.status = RequestStatus.APPEAL_DENIED.value
        request.appeal_outcome = f"Denied: {reason}"
        request.notes += (
            " Consumer informed of right to contact Delaware AG "
            "(Department of Justice, Consumer Protection Unit)."
        )
    return request


@dataclass
class SensitiveDataConsent:
    """Records consent for sensitive data processing under §12D-105(a)(4)."""
    consent_id: str
    consumer_id: str
    sensitive_category: str
    purpose: str
    consent_text_shown: str
    consent_method: str
    granted: bool
    granted_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    )
    withdrawn: bool = False
    withdrawn_at: Optional[str] = None
    consumer_age_bracket: str = "adult"
    parental_consent: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


def record_sensitive_consent(
    consent_id: str,
    consumer_id: str,
    category: SensitiveCategory,
    purpose: str,
    consent_text: str,
    method: str,
    age_bracket: str = "adult",
) -> SensitiveDataConsent:
    """
    Record consent for sensitive data processing.
    For children under 13, parental consent is required.
    """
    parental = age_bracket == "under_13"
    return SensitiveDataConsent(
        consent_id=consent_id,
        consumer_id=consumer_id,
        sensitive_category=category.value,
        purpose=purpose,
        consent_text_shown=consent_text,
        consent_method=method,
        granted=True,
        consumer_age_bracket=age_bracket,
        parental_consent=parental,
    )


def withdraw_consent(consent: SensitiveDataConsent) -> SensitiveDataConsent:
    """Withdraw previously granted sensitive data consent."""
    consent.withdrawn = True
    consent.withdrawn_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return consent


@dataclass
class GpcSignalResult:
    """Result of processing a GPC universal opt-out signal."""
    consumer_id: Optional[str]
    signal_detected: bool
    authenticated: bool
    opt_out_applied_scope: str
    categories_opted_out: list
    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    )

    def to_dict(self) -> dict:
        return asdict(self)


def process_gpc_signal(
    gpc_header_value: str,
    consumer_id: Optional[str] = None,
    authenticated: bool = False,
) -> GpcSignalResult:
    """
    Process a Global Privacy Control signal per §12D-106(a)(5)(c).
    Effective January 1, 2026.
    """
    signal_detected = gpc_header_value == "1"

    if not signal_detected:
        return GpcSignalResult(
            consumer_id=consumer_id,
            signal_detected=False,
            authenticated=authenticated,
            opt_out_applied_scope="none",
            categories_opted_out=[],
        )

    scope = "account" if authenticated and consumer_id else "device_browser"
    categories = [
        RightType.OPT_OUT_SALE.value,
        RightType.OPT_OUT_TARGETED_ADS.value,
    ]

    return GpcSignalResult(
        consumer_id=consumer_id,
        signal_detected=True,
        authenticated=authenticated,
        opt_out_applied_scope=scope,
        categories_opted_out=categories,
    )


@dataclass
class DpiaRecord:
    """Data Protection Assessment record under §12D-105(b)."""
    dpia_id: str
    processing_activity: str
    trigger_reason: str
    data_categories: list
    consumer_categories: list
    benefits_controller: str
    benefits_consumer: str
    benefits_public: str
    risks_identified: list
    mitigations_applied: list
    benefits_outweigh_risks: bool
    assessor: str
    assessment_date: str = field(
        default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%d")
    )
    approved: bool = False
    next_review_date: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)


DPIA_TRIGGERS = [
    "targeted_advertising",
    "sale_of_personal_data",
    "profiling_with_harm_risk",
    "sensitive_data_processing",
    "minor_data_non_service",
]


def requires_dpia(processing_purposes: list) -> bool:
    """Check if a DPIA is required based on processing purposes."""
    return any(purpose in DPIA_TRIGGERS for purpose in processing_purposes)


def create_dpia(
    dpia_id: str,
    processing_activity: str,
    trigger_reason: str,
    data_categories: list,
    consumer_categories: list,
    benefits_controller: str,
    benefits_consumer: str,
    benefits_public: str,
    risks: list,
    mitigations: list,
    assessor: str,
) -> DpiaRecord:
    """Create a data protection assessment record."""
    benefits_outweigh = len(mitigations) >= len(risks) and len(risks) > 0
    review_date = (
        datetime.now(timezone.utc) + timedelta(days=365)
    ).strftime("%Y-%m-%d")

    return DpiaRecord(
        dpia_id=dpia_id,
        processing_activity=processing_activity,
        trigger_reason=trigger_reason,
        data_categories=data_categories,
        consumer_categories=consumer_categories,
        benefits_controller=benefits_controller,
        benefits_consumer=benefits_consumer,
        benefits_public=benefits_public,
        risks_identified=risks,
        mitigations_applied=mitigations,
        benefits_outweigh_risks=benefits_outweigh,
        assessor=assessor,
        approved=benefits_outweigh,
        next_review_date=review_date,
    )


def generate_compliance_report(
    applicability: ApplicabilityResult,
    requests: list,
    consents: list,
    dpias: list,
) -> dict:
    """Generate a DPPA compliance summary report."""
    completed = [r for r in requests if r.status == RequestStatus.COMPLETED.value]
    denied = [r for r in requests if r.status == RequestStatus.DENIED.value]
    pending = [
        r for r in requests
        if r.status not in (
            RequestStatus.COMPLETED.value,
            RequestStatus.DENIED.value,
            RequestStatus.APPEAL_UPHELD.value,
            RequestStatus.APPEAL_DENIED.value,
        )
    ]
    active_consents = [c for c in consents if c.granted and not c.withdrawn]
    withdrawn_consents = [c for c in consents if c.withdrawn]

    return {
        "report_title": "Delaware DPPA Compliance Report",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "applicability": applicability.to_dict(),
        "consumer_requests": {
            "total": len(requests),
            "completed": len(completed),
            "denied": len(denied),
            "pending": len(pending),
            "by_type": _count_by_type(requests),
        },
        "sensitive_data_consent": {
            "total_records": len(consents),
            "active": len(active_consents),
            "withdrawn": len(withdrawn_consents),
            "by_category": _count_consent_by_category(consents),
        },
        "data_protection_assessments": {
            "total": len(dpias),
            "approved": sum(1 for d in dpias if d.approved),
            "pending_review": sum(1 for d in dpias if not d.approved),
        },
        "universal_opt_out": {
            "effective_date": "2026-01-01",
            "gpc_detection_implemented": True,
        },
    }


def _count_by_type(requests: list) -> dict:
    counts = {}
    for r in requests:
        counts[r.right_type] = counts.get(r.right_type, 0) + 1
    return counts


def _count_consent_by_category(consents: list) -> dict:
    counts = {}
    for c in consents:
        counts[c.sensitive_category] = counts.get(c.sensitive_category, 0) + 1
    return counts


if __name__ == "__main__":
    result = assess_applicability(
        entity_name="Liberty Commerce Inc.",
        entity_type="commercial_entity",
        de_consumer_count=52_000,
        payment_only_count=3_000,
        revenue_from_sale_pct=12.0,
    )
    print(json.dumps(result.to_dict(), indent=2))

    req = create_request("REQ-DE-001", "CONSUMER-4421", RightType.ACCESS)
    req = verify_identity(req, "account_match", 3)
    req = complete_request(req)

    consent = record_sensitive_consent(
        consent_id="SC-DE-001",
        consumer_id="CONSUMER-4421",
        category=SensitiveCategory.PRECISE_GEOLOCATION,
        purpose="Provide location-based store recommendations",
        consent_text="I consent to Liberty Commerce Inc. using my precise location to show nearby stores.",
        method="in_app_toggle",
    )

    gpc = process_gpc_signal("1", consumer_id="CONSUMER-4421", authenticated=True)

    dpia = create_dpia(
        dpia_id="DPIA-DE-001",
        processing_activity="Targeted advertising based on browsing behavior",
        trigger_reason="targeted_advertising",
        data_categories=["browsing_history", "purchase_history", "device_info"],
        consumer_categories=["registered_customers", "website_visitors"],
        benefits_controller="Revenue from personalized advertising",
        benefits_consumer="More relevant product recommendations",
        benefits_public="None directly",
        risks=["Profiling without awareness", "Data sharing with ad networks"],
        mitigations=["Opt-out mechanism", "GPC signal honor", "Data minimization"],
        assessor="Privacy Team Lead",
    )

    report = generate_compliance_report(result, [req], [consent], [dpia])
    print(json.dumps(report, indent=2))
