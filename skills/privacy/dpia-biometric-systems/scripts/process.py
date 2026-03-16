#!/usr/bin/env python3
"""DPIA Assessment Tool for Biometric Systems.

Conducts structured Data Protection Impact Assessments for biometric
identification and authentication systems under GDPR Article 35 and
Article 9 special category rules. Evaluates necessity, proportionality,
risks, and mitigation measures with biometric-specific criteria.
"""

import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class BiometricModality(Enum):
    FINGERPRINT = "Fingerprint Recognition"
    FACIAL = "Facial Recognition"
    IRIS = "Iris Scanning"
    VOICE = "Voice Recognition"
    BEHAVIOURAL = "Behavioural Biometrics"
    MULTIMODAL = "Multimodal (Multiple Modalities)"


class MatchingMode(Enum):
    VERIFICATION = "1:1 Verification"
    IDENTIFICATION = "1:N Identification"


class TemplateStorage(Enum):
    ON_DEVICE = "On-device (badge/token held by data subject)"
    LOCAL_DB = "Local server database"
    CENTRALISED_DB = "Centralised database"
    CLOUD = "Cloud-hosted database"


class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    VERY_HIGH = "Very High"


class LawfulBasis(Enum):
    CONSENT = "Art. 6(1)(a) Consent + Art. 9(2)(a) Explicit Consent"
    LEGAL_OBLIGATION = "Art. 6(1)(c) Legal Obligation + Art. 9(2)(b) Employment Law"
    LEGITIMATE_INTEREST = "Art. 6(1)(f) Legitimate Interest (Art. 9(2) exception required)"
    PUBLIC_INTEREST = "Art. 6(1)(e) Public Interest + Art. 9(2)(g) Substantial Public Interest"
    EMPLOYMENT_LAW = "Art. 6(1)(b)/(c) Employment + Art. 9(2)(b) Employment Obligations"


def score_to_level(score: int) -> RiskLevel:
    if score <= 3:
        return RiskLevel.LOW
    elif score <= 6:
        return RiskLevel.MEDIUM
    elif score <= 9:
        return RiskLevel.HIGH
    return RiskLevel.VERY_HIGH


@dataclass
class BiometricSystem:
    name: str
    modality: BiometricModality
    matching_mode: MatchingMode
    template_storage: TemplateStorage
    vendor: str
    enrolled_subjects: int
    daily_transactions: int
    subject_categories: list  # e.g., ["employees", "contractors", "visitors"]
    deployment_locations: list  # e.g., ["HQ Building A", "R&D Lab"]
    liveness_detection: bool
    iso_24745_compliant: bool
    alternative_method_available: bool
    has_encryption_at_rest: bool
    has_encryption_in_transit: bool


@dataclass
class NecessityAssessment:
    specific_purpose: str
    lawful_basis: LawfulBasis
    alternatives_evaluated: list  # list of dicts with name, reason_insufficient
    necessity_conclusion: str  # "Necessary" or "Not necessary"
    proportionality_conclusion: str  # "Proportionate" or "Disproportionate"
    dpo_advice: str


@dataclass
class BiometricRisk:
    risk_id: str
    category: str
    description: str
    likelihood: int  # 1-4
    severity: int  # 1-4
    mitigation_measures: list = field(default_factory=list)
    residual_likelihood: Optional[int] = None
    residual_severity: Optional[int] = None

    @property
    def inherent_score(self) -> int:
        return self.likelihood * self.severity

    @property
    def inherent_level(self) -> RiskLevel:
        return score_to_level(self.inherent_score)

    @property
    def residual_score(self) -> int:
        rl = self.residual_likelihood if self.residual_likelihood else self.likelihood
        rs = self.residual_severity if self.residual_severity else self.severity
        return rl * rs

    @property
    def residual_level(self) -> RiskLevel:
        return score_to_level(self.residual_score)


@dataclass
class MitigationMeasure:
    measure_id: str
    description: str
    standard_reference: str
    reduces_likelihood_by: int
    reduces_severity_by: int
    status: str  # Planned, Implemented, Verified
    addresses_risks: list  # Risk IDs


@dataclass
class BiometricDPIA:
    reference: str
    assessment_date: str
    controller: str
    dpo: str
    system: BiometricSystem
    necessity: NecessityAssessment
    risks: list = field(default_factory=list)
    measures: list = field(default_factory=list)
    prior_consultation_required: bool = False


def check_dpia_obligation(system: BiometricSystem) -> dict:
    """Determine whether DPIA is mandatory under EDPB criteria."""
    criteria_met = []

    # Criterion 4: Special category data -- biometric for identification
    criteria_met.append({
        "criterion": "Special category data (EDPB Criterion 4)",
        "met": True,
        "reason": f"Biometric data ({system.modality.value}) processed for unique identification under Art. 9(1)",
    })

    # Criterion 5: Large-scale processing
    large_scale = system.enrolled_subjects >= 1000 or system.daily_transactions >= 5000
    criteria_met.append({
        "criterion": "Large-scale processing (EDPB Criterion 5)",
        "met": large_scale,
        "reason": f"{system.enrolled_subjects} enrolled subjects, {system.daily_transactions} daily transactions",
    })

    # Criterion 3: Systematic monitoring
    systematic = system.modality in (BiometricModality.FACIAL, BiometricModality.BEHAVIOURAL)
    criteria_met.append({
        "criterion": "Systematic monitoring (EDPB Criterion 3)",
        "met": systematic,
        "reason": f"{system.modality.value} may involve continuous or passive monitoring",
    })

    # Criterion 8: Innovative technology
    innovative = system.modality in (BiometricModality.BEHAVIOURAL, BiometricModality.MULTIMODAL)
    criteria_met.append({
        "criterion": "Innovative technology (EDPB Criterion 8)",
        "met": innovative,
        "reason": f"{system.modality.value} represents innovative biometric technology",
    })

    # Criterion 7: Vulnerable data subjects
    vulnerable = "employees" in system.subject_categories or "children" in system.subject_categories
    criteria_met.append({
        "criterion": "Vulnerable data subjects (EDPB Criterion 7)",
        "met": vulnerable,
        "reason": f"Subject categories include: {', '.join(system.subject_categories)}",
    })

    # Criterion 2: Automated decision-making
    criteria_met.append({
        "criterion": "Automated decision-making (EDPB Criterion 2)",
        "met": True,
        "reason": "Biometric matching produces automated access/deny decisions",
    })

    met_count = sum(1 for c in criteria_met if c["met"])
    dpia_mandatory = met_count >= 2  # EDPB: two or more criteria triggers mandatory DPIA

    return {
        "dpia_mandatory": dpia_mandatory,
        "criteria_met": met_count,
        "criteria_details": criteria_met,
        "conclusion": f"DPIA is {'MANDATORY' if dpia_mandatory else 'recommended'} -- {met_count} of 6 EDPB criteria met",
    }


def assess_template_storage_risk(system: BiometricSystem) -> dict:
    """Assess risk level based on template storage method per CNIL hierarchy."""
    storage_risk = {
        TemplateStorage.ON_DEVICE: {
            "tier": 1,
            "risk": "Lowest",
            "justification_required": "Standard",
            "recommendation": "Preferred storage method per CNIL Reglement Type Biometrie",
        },
        TemplateStorage.LOCAL_DB: {
            "tier": 2,
            "risk": "Medium",
            "justification_required": "Enhanced -- document why on-device storage is infeasible",
            "recommendation": "Implement employee-controlled access key",
        },
        TemplateStorage.CENTRALISED_DB: {
            "tier": 3,
            "risk": "High",
            "justification_required": "Strongest -- specific documented security requirement",
            "recommendation": "Justify why Tier 1 and Tier 2 are technically infeasible",
        },
        TemplateStorage.CLOUD: {
            "tier": 3,
            "risk": "Highest",
            "justification_required": "Strongest + international transfer assessment",
            "recommendation": "Avoid unless operationally essential; assess Chapter V transfer mechanism",
        },
    }
    return storage_risk[system.template_storage]


def calculate_residual_risks(dpia: BiometricDPIA) -> BiometricDPIA:
    """Calculate residual risk after applying mitigation measures."""
    for risk in dpia.risks:
        applicable = [m for m in dpia.measures if risk.risk_id in m.addresses_risks]
        total_l_reduction = sum(m.reduces_likelihood_by for m in applicable)
        total_s_reduction = sum(m.reduces_severity_by for m in applicable)
        risk.residual_likelihood = max(1, risk.likelihood - total_l_reduction)
        risk.residual_severity = max(1, risk.severity - total_s_reduction)
    return dpia


def assess_prior_consultation(dpia: BiometricDPIA) -> dict:
    """Determine whether Art. 36 prior consultation is required."""
    high_residual = [
        r for r in dpia.risks
        if r.residual_level in (RiskLevel.HIGH, RiskLevel.VERY_HIGH)
    ]

    triggers = []
    if high_residual:
        triggers.append(f"{len(high_residual)} risk(s) with residual level High or Very High")

    if dpia.system.matching_mode == MatchingMode.IDENTIFICATION and dpia.system.enrolled_subjects > 10000:
        triggers.append("1:N identification mode with >10,000 enrolled subjects")

    if dpia.system.modality == BiometricModality.FACIAL and not dpia.system.alternative_method_available:
        triggers.append("Facial recognition without alternative non-biometric method")

    required = len(triggers) > 0
    dpia.prior_consultation_required = required

    return {
        "prior_consultation_required": required,
        "triggers": triggers,
        "action": "Submit DPIA to lead supervisory authority under Art. 36(1) before commencing processing"
        if required else "Prior consultation not required; proceed with implementation",
    }


def generate_compliance_checklist(system: BiometricSystem) -> list:
    """Generate biometric-specific compliance checklist."""
    checks = [
        {"item": "Art. 9(2) exception identified and documented", "status": "Required", "reference": "GDPR Art. 9(2)"},
        {"item": "DPIA completed before processing commences", "status": "Required", "reference": "GDPR Art. 35(1)"},
        {"item": "DPO consulted during DPIA", "status": "Required", "reference": "GDPR Art. 35(2)"},
        {"item": "Necessity test: specific purpose documented", "status": "Required", "reference": "EDPB WP248rev.01"},
        {"item": "Less intrusive alternatives evaluated", "status": "Required", "reference": "EDPB WP248rev.01"},
        {
            "item": "Alternative non-biometric method available",
            "status": "PASS" if system.alternative_method_available else "FAIL",
            "reference": "CNIL Reglement Type Biometrie",
        },
        {
            "item": "Liveness detection (anti-spoofing) implemented",
            "status": "PASS" if system.liveness_detection else "FAIL",
            "reference": "ISO/IEC 30107",
        },
        {
            "item": "Biometric template protection per ISO 24745",
            "status": "PASS" if system.iso_24745_compliant else "FAIL",
            "reference": "ISO/IEC 24745:2022",
        },
        {
            "item": "Encryption at rest for biometric templates",
            "status": "PASS" if system.has_encryption_at_rest else "FAIL",
            "reference": "GDPR Art. 32(1)(a)",
        },
        {
            "item": "Encryption in transit for biometric data",
            "status": "PASS" if system.has_encryption_in_transit else "FAIL",
            "reference": "GDPR Art. 32(1)(a)",
        },
        {"item": "Data subjects informed of biometric processing", "status": "Required", "reference": "GDPR Art. 13/14"},
        {"item": "Template deletion upon purpose cessation", "status": "Required", "reference": "GDPR Art. 5(1)(e)"},
        {"item": "Biometric vendor Art. 28 DPA in place", "status": "Required", "reference": "GDPR Art. 28"},
        {"item": "Annual DPIA review scheduled", "status": "Required", "reference": "GDPR Art. 35(11)"},
        {"item": "Biometric-specific breach response procedure", "status": "Required", "reference": "GDPR Art. 33-34"},
    ]

    passed = sum(1 for c in checks if c["status"] == "PASS")
    failed = sum(1 for c in checks if c["status"] == "FAIL")
    required = sum(1 for c in checks if c["status"] == "Required")

    return {
        "checklist": checks,
        "passed": passed,
        "failed": failed,
        "requires_verification": required,
        "compliance_score": f"{passed}/{passed + failed}" if (passed + failed) > 0 else "N/A",
    }


def generate_report(dpia: BiometricDPIA) -> str:
    """Generate the complete DPIA report for the biometric system."""
    lines = [
        "=" * 78,
        "DATA PROTECTION IMPACT ASSESSMENT -- BIOMETRIC SYSTEM",
        "=" * 78,
        f"Reference:           {dpia.reference}",
        f"Assessment Date:     {dpia.assessment_date}",
        f"Controller:          {dpia.controller}",
        f"DPO:                 {dpia.dpo}",
        "",
    ]

    # System description
    s = dpia.system
    lines.extend([
        "-" * 78,
        "SECTION 1: BIOMETRIC SYSTEM DESCRIPTION",
        "-" * 78,
        f"  System Name:         {s.name}",
        f"  Modality:            {s.modality.value}",
        f"  Matching Mode:       {s.matching_mode.value}",
        f"  Template Storage:    {s.template_storage.value}",
        f"  Vendor:              {s.vendor}",
        f"  Enrolled Subjects:   {s.enrolled_subjects:,}",
        f"  Daily Transactions:  {s.daily_transactions:,}",
        f"  Subject Categories:  {', '.join(s.subject_categories)}",
        f"  Deployment Sites:    {', '.join(s.deployment_locations)}",
        f"  Liveness Detection:  {'Yes' if s.liveness_detection else 'No'}",
        f"  ISO 24745 Compliant: {'Yes' if s.iso_24745_compliant else 'No'}",
        f"  Non-biometric Alt:   {'Available' if s.alternative_method_available else 'NOT AVAILABLE'}",
        "",
    ])

    # DPIA obligation check
    obligation = check_dpia_obligation(s)
    lines.extend([
        "-" * 78,
        "SECTION 2: DPIA OBLIGATION ASSESSMENT",
        "-" * 78,
        f"  Conclusion: {obligation['conclusion']}",
        "",
    ])
    for c in obligation["criteria_details"]:
        status = "MET" if c["met"] else "NOT MET"
        lines.append(f"  [{status:>7}] {c['criterion']}")
        lines.append(f"           {c['reason']}")

    # Template storage risk
    storage = assess_template_storage_risk(s)
    lines.extend([
        "",
        "-" * 78,
        "SECTION 3: TEMPLATE STORAGE RISK ASSESSMENT (CNIL HIERARCHY)",
        "-" * 78,
        f"  Storage Method:          {s.template_storage.value}",
        f"  CNIL Tier:               {storage['tier']}",
        f"  Risk Level:              {storage['risk']}",
        f"  Justification Required:  {storage['justification_required']}",
        f"  Recommendation:          {storage['recommendation']}",
        "",
    ])

    # Necessity and proportionality
    n = dpia.necessity
    lines.extend([
        "-" * 78,
        "SECTION 4: NECESSITY AND PROPORTIONALITY",
        "-" * 78,
        f"  Purpose:          {n.specific_purpose}",
        f"  Lawful Basis:     {n.lawful_basis.value}",
        f"  Necessity:        {n.necessity_conclusion}",
        f"  Proportionality:  {n.proportionality_conclusion}",
        f"  DPO Advice:       {n.dpo_advice}",
        "",
        "  Alternatives Evaluated:",
    ])
    for alt in n.alternatives_evaluated:
        lines.append(f"    - {alt['name']}: {alt['reason_insufficient']}")

    # Risk assessment
    lines.extend(["", "-" * 78, "SECTION 5: RISK ASSESSMENT", "-" * 78])
    for r in dpia.risks:
        lines.append(f"\n  {r.risk_id}: {r.category}")
        lines.append(f"    Description:  {r.description}")
        lines.append(f"    Inherent:     L={r.likelihood} x S={r.severity} = {r.inherent_score} ({r.inherent_level.value})")
        if r.residual_likelihood is not None:
            lines.append(f"    Residual:     L={r.residual_likelihood} x S={r.residual_severity} = {r.residual_score} ({r.residual_level.value})")
        if r.mitigation_measures:
            lines.append(f"    Measures:     {', '.join(r.mitigation_measures)}")

    # Mitigation measures
    lines.extend(["", "-" * 78, "SECTION 6: MITIGATION MEASURES", "-" * 78])
    for m in dpia.measures:
        lines.append(f"\n  {m.measure_id}: {m.description}")
        lines.append(f"    Standard:     {m.standard_reference}")
        lines.append(f"    Addresses:    {', '.join(m.addresses_risks)}")
        lines.append(f"    Status:       {m.status}")

    # Prior consultation
    consultation = assess_prior_consultation(dpia)
    lines.extend([
        "",
        "-" * 78,
        "SECTION 7: ART. 36 PRIOR CONSULTATION",
        "-" * 78,
        f"  Required: {'YES' if consultation['prior_consultation_required'] else 'No'}",
    ])
    if consultation["triggers"]:
        lines.append("  Triggers:")
        for t in consultation["triggers"]:
            lines.append(f"    - {t}")
    lines.append(f"  Action: {consultation['action']}")

    # Compliance checklist
    checklist = generate_compliance_checklist(dpia.system)
    lines.extend([
        "",
        "-" * 78,
        "SECTION 8: COMPLIANCE CHECKLIST",
        "-" * 78,
        f"  Score: {checklist['compliance_score']} technical controls passed",
        f"  Requires Verification: {checklist['requires_verification']} items",
        "",
    ])
    for c in checklist["checklist"]:
        icon = "PASS" if c["status"] == "PASS" else ("FAIL" if c["status"] == "FAIL" else " -- ")
        lines.append(f"  [{icon:>4}] {c['item']} ({c['reference']})")

    lines.extend(["", "=" * 78])
    return "\n".join(lines)


if __name__ == "__main__":
    system = BiometricSystem(
        name="SecureEntry Fingerprint Access Control",
        modality=BiometricModality.FINGERPRINT,
        matching_mode=MatchingMode.VERIFICATION,
        template_storage=TemplateStorage.ON_DEVICE,
        vendor="Suprema BioStar 2",
        enrolled_subjects=2400,
        daily_transactions=9600,
        subject_categories=["employees", "contractors"],
        deployment_locations=["HQ Building A", "R&D Laboratory", "Data Centre"],
        liveness_detection=True,
        iso_24745_compliant=True,
        alternative_method_available=True,
        has_encryption_at_rest=True,
        has_encryption_in_transit=True,
    )

    necessity = NecessityAssessment(
        specific_purpose="Controlling physical access to R&D laboratory containing proprietary pharmaceutical formulations and data centre housing patient clinical trial data",
        lawful_basis=LawfulBasis.EMPLOYMENT_LAW,
        alternatives_evaluated=[
            {"name": "Proximity badge only", "reason_insufficient": "17 tailgating incidents in 12 months; badge sharing documented in 3 internal audit findings"},
            {"name": "Badge + PIN", "reason_insufficient": "PIN sharing observed in 8 cases; insufficient for pharmaceutical GMP compliance requirement"},
            {"name": "Smart card + password", "reason_insufficient": "Impractical for cleanroom access where gloving prevents keyboard use"},
        ],
        necessity_conclusion="Necessary -- biometric verification required for pharmaceutical cleanroom and data centre access where less intrusive alternatives have documented failure rates",
        proportionality_conclusion="Proportionate -- targeted deployment limited to 3 high-security locations (not organisation-wide); on-device template storage; alternative PIN+badge method available",
        dpo_advice="DPO concurs with necessity finding for R&D and data centre; recommends annual review and demographic accuracy audit across employee population",
    )

    risks = [
        BiometricRisk("BIO-R1", "Template Breach", "Unauthorised access to fingerprint templates enabling identity fraud; templates cannot be reset like passwords", 2, 4, ["M1", "M2"]),
        BiometricRisk("BIO-R2", "Function Creep", "Fingerprint data collected for access control repurposed for time and attendance monitoring without separate lawful basis", 2, 3, ["M3"]),
        BiometricRisk("BIO-R3", "Discrimination", "Fingerprint scanner failure rates vary by skin type, age, and manual labour exposure; higher false rejection rates for certain employee groups", 3, 3, ["M4", "M5"]),
        BiometricRisk("BIO-R4", "Spoofing", "Artificial fingerprint (gummy finger) used to bypass access control", 2, 3, ["M6"]),
        BiometricRisk("BIO-R5", "Vendor Data Access", "Biometric vendor support staff access templates during maintenance", 2, 4, ["M7"]),
        BiometricRisk("BIO-R6", "Irrevocability", "Compromised fingerprint data has lifetime impact on data subject", 2, 4, ["M1", "M8"]),
    ]

    measures = [
        MitigationMeasure("M1", "On-device template storage on employee ID badges (CNIL Tier 1); no centralised fingerprint database", "CNIL Reglement Type Biometrie / ISO 24745", 1, 1, "Verified", ["BIO-R1", "BIO-R6"]),
        MitigationMeasure("M2", "AES-256 encryption of templates on badge chip; TLS 1.3 for scanner-to-controller communication", "GDPR Art. 32(1)(a)", 1, 0, "Verified", ["BIO-R1"]),
        MitigationMeasure("M3", "Technical access control policy restricting fingerprint use to physical access only; system architecture prevents data export to HR/payroll", "GDPR Art. 5(1)(b)", 1, 0, "Implemented", ["BIO-R2"]),
        MitigationMeasure("M4", "Alternative PIN+badge access for employees with skin conditions, injuries, or objections; no adverse consequences policy signed by HR Director", "CNIL Reglement Type Biometrie", 1, 1, "Verified", ["BIO-R3"]),
        MitigationMeasure("M5", "Quarterly demographic accuracy audit across employee population groups; scanner recalibration when FRR exceeds 2% for any group", "ISO/IEC 19795", 1, 0, "Implemented", ["BIO-R3"]),
        MitigationMeasure("M6", "Suprema BioStar 2 liveness detection (capacitive + temperature sensing); ISO 30107 Level 2 certified", "ISO/IEC 30107", 1, 0, "Verified", ["BIO-R4"]),
        MitigationMeasure("M7", "Art. 28 DPA with Suprema prohibiting template access; maintenance conducted on-site with DPO observer; no remote template access", "GDPR Art. 28(3)", 1, 0, "Verified", ["BIO-R5"]),
        MitigationMeasure("M8", "Cancelable biometric scheme: system-specific irreversible template transformation; templates from this system cannot be matched against other biometric systems", "ISO/IEC 24745 Section 6", 0, 1, "Verified", ["BIO-R6"]),
    ]

    dpia = BiometricDPIA(
        reference="DPIA-BIO-2026-003",
        assessment_date="2026-03-15",
        controller="NovaPharma GmbH",
        dpo="Dr. Sabine Kessler, Group DPO",
        system=system,
        necessity=necessity,
        risks=risks,
        measures=measures,
    )

    dpia = calculate_residual_risks(dpia)
    report = generate_report(dpia)
    print(report)
