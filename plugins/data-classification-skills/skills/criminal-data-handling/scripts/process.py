"""
Criminal Conviction and Offence Data Handler
GDPR Art. 10 compliance engine for criminal data classification and processing validation.
"""

import re
import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from datetime import date, datetime


class CriminalDataType(Enum):
    CONVICTION = "criminal_conviction"
    OFFENCE = "criminal_offence"
    SECURITY_MEASURE = "related_security_measure"
    PROCEEDING = "criminal_proceeding"
    ACQUITTAL = "acquittal_or_dismissal"
    CAUTION = "caution_or_warning"
    SPENT_CONVICTION = "spent_conviction"
    NOT_CRIMINAL = "not_criminal_data"


class Art10Basis(Enum):
    OFFICIAL_AUTHORITY = "Under control of official authority"
    DPA_SCH1_P1_EMPLOYMENT = "DPA 2018 Sch.1 Part 1 para 1 — Employment"
    DPA_SCH1_P2_REGULATORY = "DPA 2018 Sch.1 Part 2 para 6 — Regulatory requirements"
    DPA_SCH1_P2_UNLAWFUL_ACTS = "DPA 2018 Sch.1 Part 2 para 10 — Preventing/detecting unlawful acts"
    DPA_SCH1_P2_FRAUD = "DPA 2018 Sch.1 Part 2 para 14 — Preventing fraud"
    POCA_SAR = "Proceeds of Crime Act 2002 s.330-332 — SAR obligation"
    FSMA_FIT_PROPER = "FSMA 2000 s.61 — Fitness and propriety"
    MLR_CDD = "Money Laundering Regulations 2017 reg.28 — Customer due diligence"
    NO_BASIS = "No legal basis identified — PROCESSING MUST CEASE"


CRIMINAL_FIELD_PATTERNS = [
    (r"(?i)criminal", CriminalDataType.CONVICTION, 0.9),
    (r"(?i)conviction", CriminalDataType.CONVICTION, 0.9),
    (r"(?i)offence|offense", CriminalDataType.OFFENCE, 0.85),
    (r"(?i)dbs_", CriminalDataType.CONVICTION, 0.95),
    (r"(?i)police_record", CriminalDataType.CONVICTION, 0.9),
    (r"(?i)arrest", CriminalDataType.PROCEEDING, 0.8),
    (r"(?i)charge[d_]", CriminalDataType.PROCEEDING, 0.7),
    (r"(?i)sentence|sentencing", CriminalDataType.CONVICTION, 0.85),
    (r"(?i)probation", CriminalDataType.SECURITY_MEASURE, 0.75),
    (r"(?i)restraining_order", CriminalDataType.SECURITY_MEASURE, 0.8),
    (r"(?i)caution", CriminalDataType.CAUTION, 0.6),
    (r"(?i)acquit", CriminalDataType.ACQUITTAL, 0.85),
    (r"(?i)sar_|suspicious_activity", CriminalDataType.OFFENCE, 0.7),
    (r"(?i)fraud_case|fraud_investigation", CriminalDataType.OFFENCE, 0.75),
    (r"(?i)background_check.*criminal", CriminalDataType.CONVICTION, 0.85),
]


@dataclass
class CriminalDataClassification:
    field_name: str
    system_name: str
    data_type: CriminalDataType
    confidence: float
    matched_pattern: str
    art10_basis: Art10Basis = Art10Basis.NO_BASIS
    is_spent_conviction: bool = False
    exceptions_order_applicable: bool = False
    comprehensive_register_risk: bool = False
    retention_period: str = ""
    safeguards: list[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class SpentConvictionAssessment:
    """Assessment under Rehabilitation of Offenders Act 1974."""
    conviction_date: str
    sentence_type: str
    sentence_length: str
    rehabilitation_period_years: int
    is_spent: bool
    exceptions_order_exempt_role: bool
    can_disclose: bool
    reasoning: str


class CriminalDataClassifier:
    """
    Classifies data fields under GDPR Art. 10 and validates processing legality.
    """

    REHABILITATION_PERIODS = {
        "absolute_discharge": 0,
        "conditional_discharge": 1,
        "fine": 1,
        "community_order": 1,
        "suspended_sentence_up_to_6_months": 2,
        "custody_up_to_6_months": 2,
        "custody_6_to_30_months": 4,
        "custody_30_to_48_months": 7,
        "custody_over_48_months": -1,  # Never spent
    }

    EXCEPTIONS_ORDER_ROLES = {
        "fca_controlled_function",
        "fca_senior_manager",
        "fca_certification_function",
        "healthcare_professional",
        "legal_professional",
        "accountant",
        "childcare_worker",
        "education_professional",
        "social_worker",
        "security_industry",
    }

    def classify_field(
        self,
        field_name: str,
        system_name: str,
        field_description: str = "",
    ) -> CriminalDataClassification:
        """Classify a data field under Art. 10."""
        text = f"{field_name} {field_description}".lower()
        best_type = CriminalDataType.NOT_CRIMINAL
        best_confidence = 0.0
        best_pattern = ""

        for pattern, data_type, confidence in CRIMINAL_FIELD_PATTERNS:
            if re.search(pattern, text):
                if confidence > best_confidence:
                    best_type = data_type
                    best_confidence = confidence
                    best_pattern = pattern

        return CriminalDataClassification(
            field_name=field_name,
            system_name=system_name,
            data_type=best_type,
            confidence=best_confidence,
            matched_pattern=best_pattern,
        )

    def assign_legal_basis(
        self,
        classification: CriminalDataClassification,
        processing_context: str,
    ) -> CriminalDataClassification:
        """Assign Art. 10 legal basis based on processing context."""
        basis_map = {
            "employment_screening": Art10Basis.DPA_SCH1_P1_EMPLOYMENT,
            "regulatory_compliance": Art10Basis.DPA_SCH1_P2_REGULATORY,
            "aml_sar": Art10Basis.POCA_SAR,
            "fraud_prevention": Art10Basis.DPA_SCH1_P2_FRAUD,
            "fitness_propriety": Art10Basis.FSMA_FIT_PROPER,
            "customer_due_diligence": Art10Basis.MLR_CDD,
            "unlawful_act_prevention": Art10Basis.DPA_SCH1_P2_UNLAWFUL_ACTS,
            "official_authority": Art10Basis.OFFICIAL_AUTHORITY,
        }
        classification.art10_basis = basis_map.get(
            processing_context, Art10Basis.NO_BASIS
        )
        return classification

    def assess_spent_conviction(
        self,
        conviction_date: str,
        sentence_type: str,
        role_type: str = "",
    ) -> SpentConvictionAssessment:
        """
        Assess whether a conviction is spent under the Rehabilitation of Offenders Act 1974.
        """
        rehab_years = self.REHABILITATION_PERIODS.get(sentence_type, -1)

        if rehab_years == -1:
            is_spent = False
            reasoning = (
                f"Sentence type '{sentence_type}' has no rehabilitation period "
                "— conviction is never spent under the Rehabilitation of Offenders Act 1974"
            )
        else:
            try:
                conv_date = datetime.strptime(conviction_date, "%Y-%m-%d").date()
                today = date.today()
                years_elapsed = (today - conv_date).days / 365.25
                is_spent = years_elapsed >= rehab_years
                reasoning = (
                    f"Rehabilitation period: {rehab_years} years. "
                    f"Time elapsed: {years_elapsed:.1f} years. "
                    f"Conviction is {'SPENT' if is_spent else 'NOT YET SPENT'}."
                )
            except ValueError:
                is_spent = False
                reasoning = f"Unable to parse conviction date: {conviction_date}"

        exceptions_exempt = role_type.lower() in self.EXCEPTIONS_ORDER_ROLES
        can_disclose = not is_spent or exceptions_exempt

        if is_spent and exceptions_exempt:
            reasoning += (
                f" However, role '{role_type}' is exempt under the "
                "Rehabilitation of Offenders Act 1974 (Exceptions) Order 1975 — "
                "spent conviction may still be disclosed."
            )

        return SpentConvictionAssessment(
            conviction_date=conviction_date,
            sentence_type=sentence_type,
            sentence_length="",
            rehabilitation_period_years=rehab_years,
            is_spent=is_spent,
            exceptions_order_exempt_role=exceptions_exempt,
            can_disclose=can_disclose,
            reasoning=reasoning,
        )

    def assess_comprehensive_register_risk(
        self,
        system_name: str,
        record_count: int,
        covers_defined_population: bool,
        enables_search_across_individuals: bool,
    ) -> dict:
        """
        Assess whether a system constitutes a 'comprehensive register of criminal
        convictions' prohibited under Art. 10 for non-official-authority entities.
        """
        risk_factors = []
        if record_count > 100:
            risk_factors.append(f"Contains {record_count} criminal records")
        if covers_defined_population:
            risk_factors.append("Covers a defined population comprehensively")
        if enables_search_across_individuals:
            risk_factors.append("Enables searching criminal history across individuals")

        is_comprehensive = len(risk_factors) >= 2

        return {
            "system": system_name,
            "comprehensive_register_risk": is_comprehensive,
            "risk_level": "HIGH" if is_comprehensive else "LOW",
            "risk_factors": risk_factors,
            "recommendation": (
                "System may constitute a comprehensive register of criminal convictions. "
                "Art. 10 prohibits this unless under control of official authority. "
                "Immediate legal review required."
                if is_comprehensive
                else "System does not appear to constitute a comprehensive register."
            ),
        }

    def generate_appropriate_policy_document(
        self,
        organisation: str,
        processing_activities: list[dict],
    ) -> dict:
        """
        Generate the structure for an Appropriate Policy Document as required
        by DPA 2018 s.11 when processing criminal data under Schedule 1 conditions.
        """
        return {
            "document_title": f"{organisation} — Appropriate Policy Document for Criminal Data Processing",
            "version": "1.0",
            "date": date.today().isoformat(),
            "review_date": date.today().replace(year=date.today().year + 1).isoformat(),
            "sections": {
                "1_schedule_1_conditions": [
                    {
                        "activity": pa.get("activity", ""),
                        "condition": pa.get("condition", ""),
                        "lawful_basis_art6": pa.get("art6_basis", ""),
                    }
                    for pa in processing_activities
                ],
                "2_compliance_with_principles": {
                    "lawfulness": "Criminal data processed only with established Art. 10 legal basis",
                    "purpose_limitation": "Criminal data used only for the specific authorised purpose",
                    "data_minimisation": "Only outcome recorded, not full criminal record",
                    "accuracy": "Criminal data verified against official sources (DBS, NCA)",
                    "storage_limitation": "Defined retention periods per processing activity",
                    "integrity_confidentiality": "Encrypted storage, RBAC access, audit logging",
                },
                "3_retention_and_erasure": "Retention periods defined per processing activity. "
                "Automated deletion triggers configured. Secure overwrite on disposal.",
            },
        }


def run_vanguard_example():
    """Demonstrate criminal data classification for Vanguard Financial Services."""
    classifier = CriminalDataClassifier()

    fields_to_scan = [
        {"name": "dbs_check_result", "description": "DBS certificate outcome for new hire"},
        {"name": "criminal_conviction_flag", "description": "Whether candidate has criminal convictions"},
        {"name": "sar_reference_number", "description": "Suspicious activity report reference"},
        {"name": "fraud_investigation_status", "description": "Internal fraud investigation case status"},
        {"name": "employee_salary", "description": "Monthly gross salary amount"},
        {"name": "civil_litigation_status", "description": "Status of civil court proceedings"},
        {"name": "fca_fitness_criminal_history", "description": "Criminal history for FCA fitness and propriety"},
    ]

    print("=" * 70)
    print("VANGUARD FINANCIAL SERVICES — CRIMINAL DATA CLASSIFICATION SCAN")
    print("=" * 70)

    for f in fields_to_scan:
        result = classifier.classify_field(f["name"], "HR_Compliance", f.get("description", ""))
        if result.data_type != CriminalDataType.NOT_CRIMINAL:
            print(f"\n  Field: {result.field_name}")
            print(f"  Type: {result.data_type.value}")
            print(f"  Confidence: {result.confidence:.0%}")

    print("\n" + "=" * 70)
    print("SPENT CONVICTION ASSESSMENT")
    print("=" * 70)

    assessment = classifier.assess_spent_conviction(
        conviction_date="2018-06-15",
        sentence_type="fine",
        role_type="fca_senior_manager",
    )
    print(f"\n  Conviction Date: {assessment.conviction_date}")
    print(f"  Sentence Type: {assessment.sentence_type}")
    print(f"  Is Spent: {assessment.is_spent}")
    print(f"  Can Disclose: {assessment.can_disclose}")
    print(f"  Reasoning: {assessment.reasoning}")

    print("\n" + "=" * 70)
    print("COMPREHENSIVE REGISTER RISK ASSESSMENT")
    print("=" * 70)

    register_risk = classifier.assess_comprehensive_register_risk(
        system_name="Compliance_Case_Management",
        record_count=350,
        covers_defined_population=True,
        enables_search_across_individuals=True,
    )
    print(f"\n  System: {register_risk['system']}")
    print(f"  Risk Level: {register_risk['risk_level']}")
    print(f"  Recommendation: {register_risk['recommendation']}")


if __name__ == "__main__":
    run_vanguard_example()
