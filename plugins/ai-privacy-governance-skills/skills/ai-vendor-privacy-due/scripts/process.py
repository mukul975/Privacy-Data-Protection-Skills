#!/usr/bin/env python3
"""
AI Vendor Privacy Due Diligence Assessment Engine

Determines controller-processor roles and conducts privacy risk
assessment for AI service vendors.
"""

import json
import datetime
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class VendorRole(Enum):
    PROCESSOR = "Processor (Art. 28)"
    JOINT_CONTROLLER = "Joint Controller (Art. 26)"
    INDEPENDENT_CONTROLLER = "Independent Controller"
    REQUIRES_ASSESSMENT = "Requires Further Assessment"


class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class AIServiceModel(Enum):
    SAAS_INFERENCE = "SaaS AI — Inference Only"
    SAAS_TRAINING = "SaaS AI — With Model Training"
    API_INFERENCE = "API-based Inference"
    EMBEDDED = "Embedded AI (On-Premise)"
    PLATFORM = "AI Development Platform"


@dataclass
class AIVendorProfile:
    vendor_name: str
    service_model: AIServiceModel
    description: str
    data_categories_processed: list[str]
    contains_special_category: bool = False
    vendor_trains_on_customer_data: bool = False
    training_opt_out_available: bool = False
    data_retention_beyond_service: bool = False
    retention_purpose: str = ""
    vendor_independent_decisions: bool = False
    sub_processors: list[str] = field(default_factory=list)
    processing_jurisdictions: list[str] = field(default_factory=list)
    iso27001_certified: bool = False
    soc2_certified: bool = False
    prior_incidents: int = 0
    dpa_in_place: bool = False
    audit_rights: bool = False


@dataclass
class VendorAssessment:
    vendor: AIVendorProfile
    determined_role: VendorRole
    risk_level: RiskLevel
    required_agreement: str
    issues: list[str]
    recommendations: list[str]
    date: str


def determine_role(vendor: AIVendorProfile) -> tuple[VendorRole, list[str]]:
    reasons = []

    if vendor.vendor_trains_on_customer_data:
        reasons.append("Vendor trains models on customer data — determines own processing purpose")
        if vendor.vendor_independent_decisions:
            return VendorRole.INDEPENDENT_CONTROLLER, reasons
        return VendorRole.JOINT_CONTROLLER, reasons

    if vendor.data_retention_beyond_service and vendor.retention_purpose:
        reasons.append(f"Vendor retains data beyond service for: {vendor.retention_purpose}")
        return VendorRole.JOINT_CONTROLLER, reasons

    if vendor.vendor_independent_decisions:
        reasons.append("Vendor makes independent processing decisions")
        return VendorRole.JOINT_CONTROLLER, reasons

    reasons.append("Vendor processes data solely on customer instructions")
    return VendorRole.PROCESSOR, reasons


def assess_risk(vendor: AIVendorProfile) -> tuple[RiskLevel, list[str]]:
    issues = []
    risk_score = 0

    if vendor.contains_special_category:
        risk_score += 3
        issues.append("Special category data processed by vendor")

    if vendor.vendor_trains_on_customer_data and not vendor.training_opt_out_available:
        risk_score += 3
        issues.append("Vendor trains on customer data without opt-out mechanism")

    if any(j not in ["EU", "EEA", "adequacy_country"] for j in vendor.processing_jurisdictions):
        risk_score += 2
        issues.append(f"Processing in non-EU jurisdictions: {', '.join(vendor.processing_jurisdictions)}")

    if not vendor.iso27001_certified and not vendor.soc2_certified:
        risk_score += 2
        issues.append("Vendor lacks ISO 27001 or SOC 2 certification")

    if vendor.prior_incidents > 0:
        risk_score += vendor.prior_incidents
        issues.append(f"Vendor has {vendor.prior_incidents} prior security incident(s)")

    if len(vendor.sub_processors) > 5:
        risk_score += 1
        issues.append(f"Complex sub-processor chain: {len(vendor.sub_processors)} sub-processors")

    if not vendor.dpa_in_place:
        risk_score += 3
        issues.append("No Data Processing Agreement in place")

    if not vendor.audit_rights:
        risk_score += 1
        issues.append("No audit rights established")

    if risk_score >= 8:
        return RiskLevel.CRITICAL, issues
    elif risk_score >= 5:
        return RiskLevel.HIGH, issues
    elif risk_score >= 3:
        return RiskLevel.MEDIUM, issues
    return RiskLevel.LOW, issues


def run_assessment(vendor: AIVendorProfile) -> VendorAssessment:
    today = datetime.date.today().isoformat()
    role, role_reasons = determine_role(vendor)
    risk, issues = assess_risk(vendor)

    recommendations = []

    if role == VendorRole.PROCESSOR:
        agreement = "Art. 28 Data Processing Agreement"
        if not vendor.dpa_in_place:
            recommendations.append("Execute Art. 28 DPA with AI-specific clauses")
    elif role == VendorRole.JOINT_CONTROLLER:
        agreement = "Art. 26 Joint Controller Agreement"
        recommendations.append("Execute Art. 26 JCA defining respective responsibilities")
        if vendor.vendor_trains_on_customer_data:
            recommendations.append("Negotiate model training restrictions or obtain opt-out")
    else:
        agreement = "Separate controller notification and legal basis"
        recommendations.append("Ensure data subjects are informed about vendor's independent processing")

    if vendor.vendor_trains_on_customer_data:
        recommendations.append("Include contractual clause prohibiting model training without consent")

    if not vendor.audit_rights:
        recommendations.append("Negotiate audit rights for AI processing activities")

    if risk in [RiskLevel.HIGH, RiskLevel.CRITICAL]:
        recommendations.append("Conduct enhanced due diligence with annual vendor review")

    for reason in role_reasons:
        issues.append(f"Role determination: {reason}")

    return VendorAssessment(
        vendor=vendor,
        determined_role=role,
        risk_level=risk,
        required_agreement=agreement,
        issues=issues,
        recommendations=recommendations,
        date=today,
    )


def format_report(assessment: VendorAssessment) -> str:
    lines = []
    lines.append(f"{'='*80}")
    lines.append("AI VENDOR PRIVACY DUE DILIGENCE ASSESSMENT")
    lines.append(f"Vendor: {assessment.vendor.vendor_name}")
    lines.append(f"Date: {assessment.date}")
    lines.append(f"{'='*80}")
    lines.append(f"\nService Model: {assessment.vendor.service_model.value}")
    lines.append(f"Determined Role: {assessment.determined_role.value}")
    lines.append(f"Risk Level: {assessment.risk_level.value}")
    lines.append(f"Required Agreement: {assessment.required_agreement}")

    if assessment.issues:
        lines.append(f"\n## FINDINGS ({len(assessment.issues)})")
        for issue in assessment.issues:
            lines.append(f"  - {issue}")

    if assessment.recommendations:
        lines.append(f"\n## RECOMMENDATIONS")
        for rec in assessment.recommendations:
            lines.append(f"  - {rec}")

    return "\n".join(lines)


def demo_cerebrum_ai_labs():
    vendor = AIVendorProfile(
        vendor_name="CloudAI Solutions — NLP Service",
        service_model=AIServiceModel.SAAS_TRAINING,
        description="NLP inference API with model improvement using aggregated customer data",
        data_categories_processed=["customer_names", "support_transcripts", "email_addresses"],
        contains_special_category=False,
        vendor_trains_on_customer_data=True,
        training_opt_out_available=True,
        data_retention_beyond_service=True,
        retention_purpose="Model improvement and benchmark dataset creation",
        vendor_independent_decisions=False,
        sub_processors=["AWS", "MongoDB Atlas"],
        processing_jurisdictions=["EU", "US"],
        iso27001_certified=True,
        soc2_certified=True,
        prior_incidents=0,
        dpa_in_place=True,
        audit_rights=False,
    )

    assessment = run_assessment(vendor)
    print(format_report(assessment))


if __name__ == "__main__":
    demo_cerebrum_ai_labs()
