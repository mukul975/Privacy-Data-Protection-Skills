#!/usr/bin/env python3
"""
US Federal Privacy Landscape — Applicability Assessment Engine

Maps the US federal privacy landscape including sectoral laws (HIPAA, GLBA,
FERPA, COPPA, FCRA, ECPA, VPPA), FTC Section 5 enforcement authority,
and preemption analysis for federal-state interaction.
"""

import json
import uuid
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class FederalLaw(Enum):
    HIPAA = "hipaa"
    CFR_PART_2 = "42_cfr_part_2"
    FTC_HEALTH_BREACH = "ftc_health_breach_rule"
    GLBA = "glba"
    FCRA = "fcra"
    COPPA = "coppa"
    FERPA = "ferpa"
    ECPA_WIRETAP = "ecpa_wiretap"
    SCA = "stored_communications_act"
    VPPA = "vppa"
    FTC_SECTION_5 = "ftc_section_5"


class HIPAAEntityType(Enum):
    HEALTH_PLAN = "health_plan"
    CLEARINGHOUSE = "clearinghouse"
    PROVIDER = "health_care_provider"
    BUSINESS_ASSOCIATE = "business_associate"
    NOT_APPLICABLE = "not_applicable"


class GLBAEntityType(Enum):
    BANK = "bank"
    CREDIT_UNION = "credit_union"
    INSURANCE = "insurance"
    SECURITIES = "securities"
    OTHER_FINANCIAL = "other_financial"
    NOT_APPLICABLE = "not_applicable"


class FCRARoleType(Enum):
    CRA = "consumer_reporting_agency"
    USER = "user_of_reports"
    FURNISHER = "furnisher"
    NOT_APPLICABLE = "not_applicable"


class ComplianceStatus(Enum):
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PARTIAL = "partially_compliant"
    NOT_ASSESSED = "not_assessed"
    NOT_APPLICABLE = "not_applicable"


FEDERAL_LAWS = {
    FederalLaw.HIPAA: {
        "name": "Health Insurance Portability and Accountability Act",
        "citation": "Pub. L. 104-191; 45 CFR Parts 160, 164",
        "regulator": "HHS Office for Civil Rights",
        "max_penalty": "USD 2,067,813 per violation per year",
        "private_right_of_action": False,
    },
    FederalLaw.GLBA: {
        "name": "Gramm-Leach-Bliley Act",
        "citation": "Pub. L. 106-102; 16 CFR Part 314",
        "regulator": "FTC / Prudential regulators",
        "max_penalty": "USD 100,000 per violation",
        "private_right_of_action": False,
    },
    FederalLaw.FCRA: {
        "name": "Fair Credit Reporting Act",
        "citation": "15 U.S.C. 1681 et seq.",
        "regulator": "CFPB / FTC",
        "max_penalty": "Statutory damages USD 100-1,000 per violation",
        "private_right_of_action": True,
    },
    FederalLaw.COPPA: {
        "name": "Children's Online Privacy Protection Act",
        "citation": "15 U.S.C. 6501-6506; 16 CFR Part 312",
        "regulator": "FTC",
        "max_penalty": "USD 50,120 per violation (2024)",
        "private_right_of_action": False,
    },
    FederalLaw.FERPA: {
        "name": "Family Educational Rights and Privacy Act",
        "citation": "20 U.S.C. 1232g; 34 CFR Part 99",
        "regulator": "US Department of Education",
        "max_penalty": "Withdrawal of federal funding",
        "private_right_of_action": False,
    },
    FederalLaw.VPPA: {
        "name": "Video Privacy Protection Act",
        "citation": "18 U.S.C. 2710",
        "regulator": "N/A (private enforcement)",
        "max_penalty": "Actual + punitive damages + attorney fees",
        "private_right_of_action": True,
    },
    FederalLaw.FTC_SECTION_5: {
        "name": "FTC Act Section 5",
        "citation": "15 U.S.C. 45(a)",
        "regulator": "FTC",
        "max_penalty": "USD 50,120 per violation (2024)",
        "private_right_of_action": False,
    },
}


@dataclass
class LawApplicability:
    """Applicability determination for a single federal law."""
    law: str = ""
    law_name: str = ""
    applicable: bool = False
    basis: str = ""
    entity_type: str = ""
    primary_regulator: str = ""
    private_right_of_action: bool = False
    preemption_notes: str = ""
    compliance_status: str = ComplianceStatus.NOT_ASSESSED.value


@dataclass
class PreemptionAnalysis:
    """Analysis of federal-state preemption for a specific state law."""
    state: str = ""
    state_law: str = ""
    federal_law: str = ""
    preempted: str = ""  # yes / no / partial
    explanation: str = ""
    exempt_data_categories: list[str] = field(default_factory=list)


@dataclass
class FederalPrivacyAssessment:
    """Complete federal privacy applicability assessment."""
    assessment_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    organisation_name: str = ""
    industry: str = ""
    states_of_operation: list[str] = field(default_factory=list)
    law_applicability: list[dict] = field(default_factory=list)
    preemption_analyses: list[dict] = field(default_factory=list)
    assessment_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    assessor: str = ""


class FederalPrivacyEngine:
    """
    Assesses applicability of US federal privacy laws, identifies
    compliance obligations, and analyses federal-state preemption.
    """

    def __init__(self):
        self.assessments: dict[str, FederalPrivacyAssessment] = {}

    def create_assessment(
        self, organisation_name: str, industry: str,
        states: list[str], assessor: str
    ) -> FederalPrivacyAssessment:
        """Create a new federal privacy applicability assessment."""
        assessment = FederalPrivacyAssessment(
            organisation_name=organisation_name,
            industry=industry,
            states_of_operation=states,
            assessor=assessor,
        )
        self.assessments[assessment.assessment_id] = assessment
        return assessment

    def assess_hipaa(
        self, assessment_id: str, entity_type: HIPAAEntityType,
        conducts_standard_transactions: bool = False
    ) -> LawApplicability:
        """Assess HIPAA applicability."""
        assessment = self.assessments.get(assessment_id)
        if not assessment:
            raise ValueError(f"Assessment {assessment_id} not found")

        info = FEDERAL_LAWS[FederalLaw.HIPAA]
        applicable = entity_type != HIPAAEntityType.NOT_APPLICABLE

        if entity_type == HIPAAEntityType.PROVIDER and not conducts_standard_transactions:
            applicable = False

        result = LawApplicability(
            law=FederalLaw.HIPAA.value,
            law_name=info["name"],
            applicable=applicable,
            basis=f"Entity type: {entity_type.value}" if applicable else "Not a covered entity or business associate",
            entity_type=entity_type.value,
            primary_regulator=info["regulator"],
            private_right_of_action=info["private_right_of_action"],
            preemption_notes="Preempts contrary state laws; state laws providing greater protection survive (45 CFR 160.203)",
        )
        assessment.law_applicability.append(asdict(result))
        return result

    def assess_glba(
        self, assessment_id: str, entity_type: GLBAEntityType
    ) -> LawApplicability:
        """Assess GLBA applicability."""
        assessment = self.assessments.get(assessment_id)
        if not assessment:
            raise ValueError(f"Assessment {assessment_id} not found")

        info = FEDERAL_LAWS[FederalLaw.GLBA]
        applicable = entity_type != GLBAEntityType.NOT_APPLICABLE

        regulator_map = {
            GLBAEntityType.BANK: "OCC / Fed / FDIC",
            GLBAEntityType.CREDIT_UNION: "NCUA",
            GLBAEntityType.INSURANCE: "State insurance regulators",
            GLBAEntityType.SECURITIES: "SEC / CFTC",
            GLBAEntityType.OTHER_FINANCIAL: "FTC",
        }

        result = LawApplicability(
            law=FederalLaw.GLBA.value,
            law_name=info["name"],
            applicable=applicable,
            basis=f"Financial institution type: {entity_type.value}" if applicable else "Not a financial institution",
            entity_type=entity_type.value,
            primary_regulator=regulator_map.get(entity_type, info["regulator"]),
            private_right_of_action=info["private_right_of_action"],
            preemption_notes="Financial Privacy Rule preempts inconsistent state laws; Safeguards Rule does not preempt stricter state requirements",
        )
        assessment.law_applicability.append(asdict(result))
        return result

    def assess_coppa(
        self, assessment_id: str, directed_to_children: bool,
        actual_knowledge_children: bool
    ) -> LawApplicability:
        """Assess COPPA applicability."""
        assessment = self.assessments.get(assessment_id)
        if not assessment:
            raise ValueError(f"Assessment {assessment_id} not found")

        info = FEDERAL_LAWS[FederalLaw.COPPA]
        applicable = directed_to_children or actual_knowledge_children

        basis_parts = []
        if directed_to_children:
            basis_parts.append("Website/service directed to children under 13")
        if actual_knowledge_children:
            basis_parts.append("Actual knowledge of collecting from children under 13")

        result = LawApplicability(
            law=FederalLaw.COPPA.value,
            law_name=info["name"],
            applicable=applicable,
            basis="; ".join(basis_parts) if applicable else "Not directed to children; no actual knowledge",
            primary_regulator=info["regulator"],
            private_right_of_action=info["private_right_of_action"],
            preemption_notes="Does not preempt consistent state laws",
        )
        assessment.law_applicability.append(asdict(result))
        return result

    def assess_ftc_section_5(
        self, assessment_id: str, is_common_carrier: bool = False,
        is_nonprofit: bool = False, is_bank: bool = False
    ) -> LawApplicability:
        """Assess FTC Section 5 jurisdiction."""
        assessment = self.assessments.get(assessment_id)
        if not assessment:
            raise ValueError(f"Assessment {assessment_id} not found")

        info = FEDERAL_LAWS[FederalLaw.FTC_SECTION_5]

        exempt = is_common_carrier or is_nonprofit or is_bank
        exemption_reasons = []
        if is_common_carrier:
            exemption_reasons.append("Common carrier exemption")
        if is_nonprofit:
            exemption_reasons.append("Non-profit exemption")
        if is_bank:
            exemption_reasons.append("Bank exemption (prudential regulator jurisdiction)")

        result = LawApplicability(
            law=FederalLaw.FTC_SECTION_5.value,
            law_name=info["name"],
            applicable=not exempt,
            basis="FTC jurisdiction confirmed" if not exempt else f"Exempt: {'; '.join(exemption_reasons)}",
            primary_regulator=info["regulator"],
            private_right_of_action=info["private_right_of_action"],
        )
        assessment.law_applicability.append(asdict(result))
        return result

    def analyse_preemption(
        self, assessment_id: str, state: str, state_law: str,
        federal_law: FederalLaw
    ) -> PreemptionAnalysis:
        """Analyse federal-state preemption for a specific combination."""
        assessment = self.assessments.get(assessment_id)
        if not assessment:
            raise ValueError(f"Assessment {assessment_id} not found")

        preemption_rules = {
            FederalLaw.HIPAA: {
                "preempted": "partial",
                "explanation": "HIPAA preempts contrary state laws but state laws providing greater protection to individuals survive (45 CFR 160.203)",
                "exempt_data": ["PHI as defined under HIPAA"],
            },
            FederalLaw.GLBA: {
                "preempted": "partial",
                "explanation": "Financial Privacy Rule preempts inconsistent state laws; Safeguards Rule does not preempt stricter state security requirements",
                "exempt_data": ["NPI under GLBA"],
            },
            FederalLaw.FCRA: {
                "preempted": "partial",
                "explanation": "FCRA broadly preempts state laws in areas addressed by FCRA Section 1681t, including prescreening, credit score disclosure, and identity theft provisions",
                "exempt_data": ["Consumer report data under FCRA"],
            },
            FederalLaw.COPPA: {
                "preempted": "no",
                "explanation": "COPPA does not preempt consistent state laws; state children's privacy laws may impose additional requirements",
                "exempt_data": [],
            },
        }

        rules = preemption_rules.get(federal_law, {
            "preempted": "no",
            "explanation": "No preemption provision",
            "exempt_data": [],
        })

        analysis = PreemptionAnalysis(
            state=state,
            state_law=state_law,
            federal_law=federal_law.value,
            preempted=rules["preempted"],
            explanation=rules["explanation"],
            exempt_data_categories=rules["exempt_data"],
        )
        assessment.preemption_analyses.append(asdict(analysis))
        return analysis

    def generate_summary(self, assessment_id: str) -> dict:
        """Generate assessment summary."""
        assessment = self.assessments.get(assessment_id)
        if not assessment:
            raise ValueError(f"Assessment {assessment_id} not found")

        applicable_laws = [
            la for la in assessment.law_applicability if la.get("applicable")
        ]
        pra_laws = [
            la for la in applicable_laws if la.get("private_right_of_action")
        ]

        return {
            "assessment_id": assessment_id,
            "organisation": assessment.organisation_name,
            "industry": assessment.industry,
            "states": assessment.states_of_operation,
            "total_laws_assessed": len(assessment.law_applicability),
            "applicable_laws": len(applicable_laws),
            "laws_with_private_right_of_action": len(pra_laws),
            "applicable_law_names": [la["law_name"] for la in applicable_laws],
            "preemption_analyses": len(assessment.preemption_analyses),
            "assessment_date": assessment.assessment_date,
        }


if __name__ == "__main__":
    engine = FederalPrivacyEngine()

    # Assess a health-tech startup that offers a telehealth platform
    assessment = engine.create_assessment(
        organisation_name="MedConnect Health Technologies Inc.",
        industry="Health Technology",
        states=["CA", "NY", "TX", "FL", "IL"],
        assessor="Jennifer Walsh, Chief Privacy Officer",
    )
    print(f"Assessment ID: {assessment.assessment_id}")

    # HIPAA assessment
    hipaa = engine.assess_hipaa(
        assessment.assessment_id,
        entity_type=HIPAAEntityType.BUSINESS_ASSOCIATE,
        conducts_standard_transactions=True,
    )
    print(f"\nHIPAA: {'Applicable' if hipaa.applicable else 'Not applicable'} — {hipaa.basis}")

    # GLBA assessment
    glba = engine.assess_glba(
        assessment.assessment_id,
        entity_type=GLBAEntityType.NOT_APPLICABLE,
    )
    print(f"GLBA: {'Applicable' if glba.applicable else 'Not applicable'} — {glba.basis}")

    # COPPA assessment
    coppa = engine.assess_coppa(
        assessment.assessment_id,
        directed_to_children=False,
        actual_knowledge_children=False,
    )
    print(f"COPPA: {'Applicable' if coppa.applicable else 'Not applicable'} — {coppa.basis}")

    # FTC Section 5
    ftc = engine.assess_ftc_section_5(
        assessment.assessment_id,
        is_common_carrier=False,
        is_nonprofit=False,
        is_bank=False,
    )
    print(f"FTC Section 5: {'Applicable' if ftc.applicable else 'Not applicable'} — {ftc.basis}")

    # Preemption analysis
    preemption = engine.analyse_preemption(
        assessment.assessment_id,
        state="California",
        state_law="CCPA/CPRA",
        federal_law=FederalLaw.HIPAA,
    )
    print(f"\nPreemption (HIPAA vs CA CCPA): {preemption.preempted} — {preemption.explanation}")

    # Summary
    summary = engine.generate_summary(assessment.assessment_id)
    print(f"\n=== Federal Privacy Assessment Summary ===")
    print(json.dumps(summary, indent=2))
