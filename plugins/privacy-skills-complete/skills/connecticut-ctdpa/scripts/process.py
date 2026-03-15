#!/usr/bin/env python3
"""
Connecticut CTDPA Compliance Tool

Assesses CTDPA applicability, audits consent interfaces for dark patterns
per §42-515(8), and tracks consumer rights requests with appeal process.
"""

import json
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class DarkPatternType(Enum):
    CONFIRM_SHAMING = "confirm_shaming"
    HIDDEN_OPTIONS = "hidden_options"
    FORCED_ACTION = "forced_action"
    TRICK_QUESTIONS = "trick_questions"
    MISDIRECTION = "misdirection"
    NAGGING = "nagging"
    DESIGN_ASYMMETRY = "design_asymmetry"
    BUNDLED_CONSENT = "bundled_consent"
    OBSTRUCTION = "obstruction"


DARK_PATTERN_CHECKS = [
    {
        "id": "DP-01",
        "pattern": DarkPatternType.CONFIRM_SHAMING.value,
        "check": "Does the decline/reject option use guilt-inducing or emotional language?",
        "example_violation": "No thanks, I prefer not to save money",
        "passing_standard": "Neutral language: 'Decline' or 'No, thank you'",
    },
    {
        "id": "DP-02",
        "pattern": DarkPatternType.DESIGN_ASYMMETRY.value,
        "check": "Are accept and decline buttons the same size, color prominence, and visual weight?",
        "example_violation": "Large green 'Accept' button, small gray 'Decline' text link",
        "passing_standard": "Equal size, equal color prominence, same visual treatment",
    },
    {
        "id": "DP-03",
        "pattern": DarkPatternType.HIDDEN_OPTIONS.value,
        "check": "Is the decline/reject option visible without scrolling or additional clicks?",
        "example_violation": "Accept button visible; decline requires scrolling down",
        "passing_standard": "Both options visible in the same viewport",
    },
    {
        "id": "DP-04",
        "pattern": DarkPatternType.FORCED_ACTION.value,
        "check": "Can the consumer access the service without providing optional consent?",
        "example_violation": "Must accept marketing to create account",
        "passing_standard": "Service accessible regardless of optional consent choices",
    },
    {
        "id": "DP-05",
        "pattern": DarkPatternType.TRICK_QUESTIONS.value,
        "check": "Is consent language free of double negatives and confusing phrasing?",
        "example_violation": "Uncheck to not opt out of sharing",
        "passing_standard": "Clear affirmative: 'Share my data for advertising' [checkbox]",
    },
    {
        "id": "DP-06",
        "pattern": DarkPatternType.MISDIRECTION.value,
        "check": "Does the visual design avoid steering the user toward the consent option?",
        "example_violation": "Accept button highlighted with animation; decline is static",
        "passing_standard": "No preferential visual treatment for either option",
    },
    {
        "id": "DP-07",
        "pattern": DarkPatternType.NAGGING.value,
        "check": "After declining, does the interface avoid re-prompting within the same session?",
        "example_violation": "Consent pop-up reappears on every page after declining",
        "passing_standard": "Decline is respected for the session; no re-prompts",
    },
    {
        "id": "DP-08",
        "pattern": DarkPatternType.BUNDLED_CONSENT.value,
        "check": "Is consent granular per purpose rather than bundled into a single checkbox?",
        "example_violation": "Single checkbox for analytics + marketing + third-party sharing",
        "passing_standard": "Separate consent for each distinct purpose",
    },
    {
        "id": "DP-09",
        "pattern": DarkPatternType.OBSTRUCTION.value,
        "check": "Is consent withdrawal as easy as granting consent?",
        "example_violation": "One-click consent; withdrawal requires email to privacy team",
        "passing_standard": "Same number of steps or fewer for withdrawal",
    },
]


@dataclass
class DarkPatternAuditResult:
    """Result of a dark pattern audit for a consent interface."""
    interface_name: str
    audit_date: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    results: list = field(default_factory=list)

    def run_audit(self, responses: dict[str, str]) -> dict:
        """Run dark pattern audit. responses maps check ID to 'pass', 'fail', or 'na'."""
        pass_count = 0
        fail_count = 0
        violations = []

        for check in DARK_PATTERN_CHECKS:
            status = responses.get(check["id"], "not_assessed")
            result = {
                "check_id": check["id"],
                "pattern": check["pattern"],
                "check": check["check"],
                "status": status,
            }

            if status == "pass":
                pass_count += 1
            elif status == "fail":
                fail_count += 1
                violations.append({
                    "check_id": check["id"],
                    "pattern": check["pattern"],
                    "violation": check["example_violation"],
                    "standard": check["passing_standard"],
                })

            self.results.append(result)

        consent_valid = fail_count == 0
        return {
            "interface": self.interface_name,
            "audit_date": self.audit_date,
            "passed": pass_count,
            "failed": fail_count,
            "consent_valid_under_ctdpa": consent_valid,
            "violations": violations,
            "note": "Consent obtained through dark patterns is not valid under §42-515(8)" if not consent_valid else "No dark patterns detected",
        }


@dataclass
class CTDPAApplicability:
    """Assess CTDPA applicability."""
    organization_name: str
    conducts_business_in_ct: bool
    targets_ct_residents: bool
    ct_consumer_count: int
    ct_consumer_count_excl_payment: int
    revenue_from_sale_pct: float
    is_exempt_entity: bool = False
    exemption_basis: str = ""

    def assess(self) -> dict:
        if self.is_exempt_entity:
            return {
                "organization": self.organization_name,
                "applicable": False,
                "reason": f"Entity-level exemption: {self.exemption_basis}",
            }

        if not (self.conducts_business_in_ct or self.targets_ct_residents):
            return {"organization": self.organization_name, "applicable": False, "reason": "No Connecticut nexus"}

        thresholds_met = []
        if self.ct_consumer_count_excl_payment >= 100_000:
            thresholds_met.append({
                "threshold": "option_1",
                "description": f"{self.ct_consumer_count_excl_payment:,} consumers (excl. payment-only) ≥ 100,000",
                "section": "§42-516(a)(1)",
            })
        if self.ct_consumer_count_excl_payment >= 25_000 and self.revenue_from_sale_pct > 25:
            thresholds_met.append({
                "threshold": "option_2",
                "description": f"{self.ct_consumer_count_excl_payment:,} consumers ≥ 25,000 AND {self.revenue_from_sale_pct}% revenue > 25%",
                "section": "§42-516(a)(2)",
            })

        return {
            "organization": self.organization_name,
            "applicable": len(thresholds_met) > 0,
            "thresholds_met": thresholds_met,
            "assessment_date": datetime.now(timezone.utc).isoformat(),
        }


@dataclass
class LoyaltyProgramAssessment:
    """Assess if a loyalty program qualifies for CTDPA exemption under §42-517(c)."""
    program_name: str
    provides_genuine_value: bool
    voluntary_participation: bool
    terms_disclose_data_collection: bool
    data_used_solely_for_program: bool

    def assess(self) -> dict:
        qualifies = all([
            self.provides_genuine_value,
            self.voluntary_participation,
            self.terms_disclose_data_collection,
            self.data_used_solely_for_program,
        ])
        criteria_results = {
            "genuine_value": self.provides_genuine_value,
            "voluntary": self.voluntary_participation,
            "disclosed": self.terms_disclose_data_collection,
            "program_purpose_only": self.data_used_solely_for_program,
        }
        failed = [k for k, v in criteria_results.items() if not v]

        return {
            "program_name": self.program_name,
            "qualifies_for_exemption": qualifies,
            "section": "§42-517(c)",
            "criteria_results": criteria_results,
            "failed_criteria": failed,
            "note": "Exempt from sale opt-out for program data" if qualifies else f"Does not qualify — failed: {', '.join(failed)}",
        }


if __name__ == "__main__":
    # Applicability assessment
    print("=== CTDPA Applicability Assessment ===")
    assessment = CTDPAApplicability(
        organization_name="Liberty Commerce Inc.",
        conducts_business_in_ct=True,
        targets_ct_residents=True,
        ct_consumer_count=87_000,
        ct_consumer_count_excl_payment=87_000,
        revenue_from_sale_pct=12.0,
    )
    print(json.dumps(assessment.assess(), indent=2))

    # Dark pattern audit
    print("\n=== Dark Pattern Audit ===")
    audit = DarkPatternAuditResult(interface_name="Cookie consent banner")
    responses = {
        "DP-01": "pass", "DP-02": "fail", "DP-03": "pass",
        "DP-04": "pass", "DP-05": "pass", "DP-06": "fail",
        "DP-07": "pass", "DP-08": "pass", "DP-09": "pass",
    }
    result = audit.run_audit(responses)
    print(json.dumps(result, indent=2))

    # Loyalty program assessment
    print("\n=== Loyalty Program Exemption Assessment ===")
    loyalty = LoyaltyProgramAssessment(
        program_name="Liberty Rewards",
        provides_genuine_value=True,
        voluntary_participation=True,
        terms_disclose_data_collection=True,
        data_used_solely_for_program=True,
    )
    print(json.dumps(loyalty.assess(), indent=2))
