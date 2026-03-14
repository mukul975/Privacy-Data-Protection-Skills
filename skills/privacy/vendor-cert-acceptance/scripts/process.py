#!/usr/bin/env python3
"""
Vendor Certification Acceptance — Evaluation and Equivalence Engine

Implements certification verification, scope alignment checking,
GDPR gap analysis, equivalence mapping, and acceptance decision
management for vendor privacy certifications.
"""

import json
import uuid
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class CertificationTier(Enum):
    TIER_A = "tier_a_strong_privacy"
    TIER_B = "tier_b_security_with_privacy"
    TIER_C = "tier_c_domain_specific"
    TIER_D = "tier_d_self_assessment"


class AcceptanceDecision(Enum):
    FULL_COVERAGE = "accepted_full_coverage"
    WITH_SUPPLEMENTATION = "accepted_with_supplementation"
    INSUFFICIENT = "insufficient"


class VerificationStatus(Enum):
    VERIFIED = "verified"
    UNVERIFIED = "unverified"
    EXPIRED = "expired"
    SCOPE_MISMATCH = "scope_mismatch"
    INVALID = "invalid"


GDPR_REQUIREMENTS = [
    {"id": "28_3_a", "description": "Documented instructions", "article": "28(3)(a)"},
    {"id": "28_3_b", "description": "Confidentiality", "article": "28(3)(b)"},
    {"id": "28_3_c", "description": "Security measures (Art. 32)", "article": "28(3)(c)"},
    {"id": "28_3_d", "description": "Sub-processor management", "article": "28(3)(d)"},
    {"id": "28_3_e", "description": "DSR assistance", "article": "28(3)(e)"},
    {"id": "28_3_f", "description": "Compliance assistance (Art. 32-36)", "article": "28(3)(f)"},
    {"id": "28_3_g", "description": "Deletion/return at termination", "article": "28(3)(g)"},
    {"id": "28_3_h", "description": "Audit rights", "article": "28(3)(h)"},
    {"id": "33_2", "description": "Breach notification to controller", "article": "33(2)"},
    {"id": "ch_v", "description": "International transfer controls", "article": "Ch. V"},
]

# Coverage mapping: certification -> GDPR requirement -> coverage level
COVERAGE_MATRIX = {
    "iso_27701": {
        "28_3_a": "full", "28_3_b": "full", "28_3_c": "full",
        "28_3_d": "full", "28_3_e": "full", "28_3_f": "full",
        "28_3_g": "full", "28_3_h": "full", "33_2": "full", "ch_v": "partial",
    },
    "soc2_privacy": {
        "28_3_a": "partial", "28_3_b": "full", "28_3_c": "full",
        "28_3_d": "partial", "28_3_e": "partial", "28_3_f": "partial",
        "28_3_g": "full", "28_3_h": "partial", "33_2": "full", "ch_v": "none",
    },
    "soc2_security": {
        "28_3_a": "none", "28_3_b": "partial", "28_3_c": "full",
        "28_3_d": "none", "28_3_e": "none", "28_3_f": "none",
        "28_3_g": "none", "28_3_h": "none", "33_2": "partial", "ch_v": "none",
    },
    "iso_27001": {
        "28_3_a": "none", "28_3_b": "full", "28_3_c": "full",
        "28_3_d": "partial", "28_3_e": "none", "28_3_f": "none",
        "28_3_g": "partial", "28_3_h": "partial", "33_2": "partial", "ch_v": "none",
    },
    "iso_27018": {
        "28_3_a": "full", "28_3_b": "full", "28_3_c": "full",
        "28_3_d": "full", "28_3_e": "partial", "28_3_f": "none",
        "28_3_g": "full", "28_3_h": "full", "33_2": "partial", "ch_v": "none",
    },
    "gdpr_art42": {
        "28_3_a": "full", "28_3_b": "full", "28_3_c": "full",
        "28_3_d": "full", "28_3_e": "full", "28_3_f": "full",
        "28_3_g": "full", "28_3_h": "full", "33_2": "full", "ch_v": "full",
    },
}

CERTIFICATION_TIERS = {
    "iso_27701": CertificationTier.TIER_A,
    "gdpr_art42": CertificationTier.TIER_A,
    "soc2_privacy": CertificationTier.TIER_B,
    "soc2_security": CertificationTier.TIER_B,
    "iso_27001": CertificationTier.TIER_B,
    "iso_27018": CertificationTier.TIER_C,
    "csa_star_l2": CertificationTier.TIER_C,
    "apec_cbpr": CertificationTier.TIER_C,
    "eu_cloud_coc": CertificationTier.TIER_C,
    "csa_star_l1": CertificationTier.TIER_D,
    "cyber_essentials": CertificationTier.TIER_D,
}


@dataclass
class VendorCertification:
    """A certification held by a vendor."""
    cert_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_id: str = ""
    certification_type: str = ""
    certification_name: str = ""
    certification_body: str = ""
    certificate_number: str = ""
    scope_description: str = ""
    valid_from: str = ""
    valid_until: str = ""
    tier: str = ""
    verification_status: str = VerificationStatus.UNVERIFIED.value
    verification_date: Optional[str] = None
    verification_notes: str = ""
    scope_covers_services: bool = False


@dataclass
class GapAnalysisResult:
    """Result of GDPR gap analysis for a vendor's certifications."""
    analysis_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    vendor_id: str = ""
    vendor_name: str = ""
    certifications_evaluated: list[str] = field(default_factory=list)
    combined_coverage: dict = field(default_factory=dict)
    gaps: list[dict] = field(default_factory=list)
    supplementation_needed: list[dict] = field(default_factory=list)
    coverage_score: float = 0.0
    decision: str = ""
    analysis_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


SUPPLEMENTATION_METHODS = {
    "28_3_a": "Vendor provides documented instructions register and processing boundary documentation",
    "28_3_d": "Vendor provides sub-processor list, notification mechanism, and sample flow-down DPA",
    "28_3_e": "Vendor provides DSR handling procedure documentation with SLA commitments",
    "28_3_f": "Vendor provides DPIA contribution process and Art. 32-36 assistance capability",
    "28_3_g": "Vendor demonstrates deletion procedure and provides sample deletion certificate",
    "28_3_h": "DPA audit rights clause verified; vendor confirms practical audit access",
    "33_2": "Vendor provides incident response plan with controller notification timeframes",
    "ch_v": "Transfer Impact Assessment and supplementary measures documentation",
}


class CertificationAcceptanceEngine:
    """
    Evaluates vendor certifications, performs GDPR gap analysis,
    and determines acceptance decisions with supplementation requirements.
    """

    def __init__(self):
        self.certifications: dict[str, list[VendorCertification]] = {}
        self.gap_analyses: dict[str, GapAnalysisResult] = {}

    def register_certification(self, cert: VendorCertification) -> str:
        """Register a vendor certification."""
        cert.tier = CERTIFICATION_TIERS.get(
            cert.certification_type, CertificationTier.TIER_D
        ).value

        if cert.vendor_id not in self.certifications:
            self.certifications[cert.vendor_id] = []
        self.certifications[cert.vendor_id].append(cert)
        return cert.cert_id

    def verify_certification(
        self, cert_id: str, vendor_id: str,
        verified: bool, scope_covers: bool, notes: str = ""
    ) -> str:
        """Record verification result for a certification."""
        certs = self.certifications.get(vendor_id, [])
        for cert in certs:
            if cert.cert_id == cert_id:
                now = datetime.now(timezone.utc)
                expiry = datetime.fromisoformat(cert.valid_until.replace("Z", "+00:00")) if cert.valid_until else now

                if not verified:
                    cert.verification_status = VerificationStatus.INVALID.value
                elif expiry < now:
                    cert.verification_status = VerificationStatus.EXPIRED.value
                elif not scope_covers:
                    cert.verification_status = VerificationStatus.SCOPE_MISMATCH.value
                else:
                    cert.verification_status = VerificationStatus.VERIFIED.value

                cert.verification_date = now.isoformat()
                cert.verification_notes = notes
                cert.scope_covers_services = scope_covers
                return cert.verification_status

        raise ValueError(f"Certification {cert_id} not found for vendor {vendor_id}")

    def perform_gap_analysis(self, vendor_id: str, vendor_name: str) -> GapAnalysisResult:
        """Perform GDPR gap analysis against vendor's combined certifications."""
        certs = self.certifications.get(vendor_id, [])
        verified_certs = [
            c for c in certs
            if c.verification_status == VerificationStatus.VERIFIED.value
        ]

        # Calculate combined coverage (best coverage across all certifications)
        combined = {}
        for req in GDPR_REQUIREMENTS:
            req_id = req["id"]
            best_coverage = "none"
            for cert in verified_certs:
                cert_coverage = COVERAGE_MATRIX.get(cert.certification_type, {})
                coverage = cert_coverage.get(req_id, "none")
                if coverage == "full":
                    best_coverage = "full"
                    break
                elif coverage == "partial" and best_coverage == "none":
                    best_coverage = "partial"
            combined[req_id] = best_coverage

        # Identify gaps
        gaps = []
        supplementation = []
        for req in GDPR_REQUIREMENTS:
            req_id = req["id"]
            coverage = combined.get(req_id, "none")
            if coverage != "full":
                gap = {
                    "requirement_id": req_id,
                    "description": req["description"],
                    "article": req["article"],
                    "coverage_level": coverage,
                }
                gaps.append(gap)
                if req_id in SUPPLEMENTATION_METHODS:
                    supplementation.append({
                        "requirement_id": req_id,
                        "description": req["description"],
                        "method": SUPPLEMENTATION_METHODS[req_id],
                    })

        # Calculate coverage score
        coverage_points = {"full": 1.0, "partial": 0.5, "none": 0.0}
        total = sum(coverage_points.get(combined.get(r["id"], "none"), 0) for r in GDPR_REQUIREMENTS)
        coverage_score = round(total / len(GDPR_REQUIREMENTS) * 100, 1)

        # Determine acceptance decision
        none_count = sum(1 for v in combined.values() if v == "none")
        if coverage_score >= 90 and none_count == 0:
            decision = AcceptanceDecision.FULL_COVERAGE.value
        elif coverage_score >= 50:
            decision = AcceptanceDecision.WITH_SUPPLEMENTATION.value
        else:
            decision = AcceptanceDecision.INSUFFICIENT.value

        result = GapAnalysisResult(
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            certifications_evaluated=[c.certification_name for c in verified_certs],
            combined_coverage=combined,
            gaps=gaps,
            supplementation_needed=supplementation,
            coverage_score=coverage_score,
            decision=decision,
        )

        self.gap_analyses[vendor_id] = result
        return result

    def get_analysis_summary(self, vendor_id: str) -> dict:
        """Generate a summary of the gap analysis."""
        result = self.gap_analyses.get(vendor_id)
        if not result:
            raise ValueError(f"No gap analysis for vendor {vendor_id}")

        return {
            "vendor_name": result.vendor_name,
            "certifications_evaluated": result.certifications_evaluated,
            "coverage_score": f"{result.coverage_score}%",
            "decision": result.decision,
            "total_gaps": len(result.gaps),
            "gaps_none": len([g for g in result.gaps if g["coverage_level"] == "none"]),
            "gaps_partial": len([g for g in result.gaps if g["coverage_level"] == "partial"]),
            "supplementation_items": len(result.supplementation_needed),
            "analysis_date": result.analysis_date,
        }


if __name__ == "__main__":
    engine = CertificationAcceptanceEngine()

    # Register certifications for NimbusAnalytics
    certs = [
        VendorCertification(
            vendor_id="nimbus-001",
            certification_type="iso_27001",
            certification_name="ISO/IEC 27001:2022",
            certification_body="TUV Rheinland",
            certificate_number="01 150 2204567",
            scope_description="Cloud analytics platform and supporting infrastructure",
            valid_from="2024-06-15",
            valid_until="2027-06-15",
        ),
        VendorCertification(
            vendor_id="nimbus-001",
            certification_type="soc2_security",
            certification_name="SOC 2 Type II (Security, Availability, Confidentiality)",
            certification_body="Deloitte GmbH",
            certificate_number="SOC2-2025-NA-001",
            scope_description="NimbusAnalytics cloud platform",
            valid_from="2025-01-01",
            valid_until="2025-12-31",
        ),
    ]

    for cert in certs:
        engine.register_certification(cert)

    # Verify certifications
    engine.verify_certification(
        certs[0].cert_id, "nimbus-001", True, True,
        "Verified on TUV Rheinland registry. Scope covers analytics platform."
    )
    engine.verify_certification(
        certs[1].cert_id, "nimbus-001", True, True,
        "SOC 2 report reviewed. No qualified opinions. Scope covers platform."
    )

    # Perform gap analysis
    analysis = engine.perform_gap_analysis("nimbus-001", "NimbusAnalytics GmbH")
    print(f"Coverage Score: {analysis.coverage_score}%")
    print(f"Decision: {analysis.decision}")

    print(f"\nGaps identified ({len(analysis.gaps)}):")
    for gap in analysis.gaps:
        print(f"  {gap['article']}: {gap['description']} — {gap['coverage_level']}")

    print(f"\nSupplementation needed ({len(analysis.supplementation_needed)}):")
    for s in analysis.supplementation_needed:
        print(f"  {s['requirement_id']}: {s['method']}")

    # Summary
    summary = engine.get_analysis_summary("nimbus-001")
    print(f"\n=== Certification Acceptance Summary ===")
    print(json.dumps(summary, indent=2))
