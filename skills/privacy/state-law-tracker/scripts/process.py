#!/usr/bin/env python3
"""
US State Privacy Law Tracker — Legislation Monitoring and Compliance Engine

Tracks enacted and pending US state comprehensive privacy laws,
calculates applicability, identifies compliance gaps across states,
and monitors effective dates and cure period expirations.
"""

import json
from datetime import datetime, timezone, date
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


class LawStatus(Enum):
    INTRODUCED = "introduced"
    COMMITTEE = "in_committee"
    PASSED_ONE_CHAMBER = "passed_one_chamber"
    PASSED_BOTH = "passed_both_chambers"
    SIGNED = "signed_by_governor"
    EFFECTIVE = "effective"
    AMENDED = "amended"


class ComplianceReadiness(Enum):
    COMPLIANT = "compliant"
    IN_PROGRESS = "in_progress"
    GAP_IDENTIFIED = "gap_identified"
    NOT_STARTED = "not_started"
    NOT_APPLICABLE = "not_applicable"


class EnforcementModel(Enum):
    AG_ONLY = "ag_only"
    AG_AND_AGENCY = "ag_and_agency"
    PRIVATE_RIGHT = "private_right_of_action"


@dataclass
class StatePrivacyLaw:
    """Representation of a state comprehensive privacy law."""
    state: str = ""
    abbreviation: str = ""
    law_name: str = ""
    statute_citation: str = ""
    enacted_date: str = ""
    effective_date: str = ""
    status: str = LawStatus.EFFECTIVE.value
    enforcement: str = EnforcementModel.AG_ONLY.value
    consumer_threshold: int = 100000
    revenue_threshold: Optional[int] = None
    data_sales_threshold_pct: int = 25
    data_sales_consumer_threshold: int = 25000
    rights_access: bool = True
    rights_delete: bool = True
    rights_correct: bool = True
    rights_portability: bool = True
    rights_opt_out_sale: bool = True
    rights_opt_out_targeted_ads: bool = True
    rights_opt_out_profiling: bool = False
    rights_appeal: bool = False
    private_right_of_action: bool = False
    cure_period_days: Optional[int] = None
    cure_period_sunset: Optional[str] = None
    universal_opt_out_required: bool = False
    universal_opt_out_date: Optional[str] = None
    sensitive_data_opt_in: bool = True
    nonprofit_exempt: bool = True
    employee_data_exempt: bool = True


ENACTED_LAWS = [
    StatePrivacyLaw(
        state="California", abbreviation="CA", law_name="CCPA/CPRA",
        statute_citation="Cal. Civ. Code 1798.100-1798.199.100",
        enacted_date="2018-06-28", effective_date="2023-01-01",
        enforcement=EnforcementModel.AG_AND_AGENCY.value,
        consumer_threshold=0, revenue_threshold=25000000,
        private_right_of_action=True, cure_period_days=None,
        universal_opt_out_required=True, universal_opt_out_date="2024-03-29",
        rights_opt_out_profiling=False, rights_appeal=False,
        nonprofit_exempt=True, employee_data_exempt=False,
    ),
    StatePrivacyLaw(
        state="Virginia", abbreviation="VA", law_name="VCDPA",
        statute_citation="Va. Code Ann. 59.1-575 through 59.1-585",
        enacted_date="2021-03-02", effective_date="2023-01-01",
        cure_period_days=30, rights_opt_out_profiling=True, rights_appeal=True,
        universal_opt_out_required=False,
    ),
    StatePrivacyLaw(
        state="Colorado", abbreviation="CO", law_name="CPA",
        statute_citation="C.R.S. 6-1-1301 through 6-1-1313",
        enacted_date="2021-07-07", effective_date="2023-07-01",
        cure_period_days=60, cure_period_sunset="2025-01-01",
        rights_opt_out_profiling=True, rights_appeal=True,
        universal_opt_out_required=True, universal_opt_out_date="2024-07-01",
    ),
    StatePrivacyLaw(
        state="Connecticut", abbreviation="CT", law_name="CTDPA",
        statute_citation="Conn. Gen. Stat. 42-515 through 42-525",
        enacted_date="2022-05-10", effective_date="2023-07-01",
        cure_period_days=60, cure_period_sunset="2025-01-01",
        rights_opt_out_profiling=True, rights_appeal=True,
        universal_opt_out_required=True, universal_opt_out_date="2025-01-01",
    ),
    StatePrivacyLaw(
        state="Texas", abbreviation="TX", law_name="TDPSA",
        statute_citation="Tex. Bus. & Com. Code Chapter 541",
        enacted_date="2023-06-18", effective_date="2024-07-01",
        cure_period_days=None, rights_opt_out_profiling=True, rights_appeal=True,
        universal_opt_out_required=True, universal_opt_out_date="2025-01-01",
        consumer_threshold=50000,
    ),
    StatePrivacyLaw(
        state="Oregon", abbreviation="OR", law_name="OCPA",
        statute_citation="ORS 757A.005 through 757A.100",
        enacted_date="2023-07-18", effective_date="2024-07-01",
        cure_period_days=None, rights_opt_out_profiling=True, rights_appeal=True,
        universal_opt_out_required=True, universal_opt_out_date="2025-01-01",
        nonprofit_exempt=False,
    ),
    StatePrivacyLaw(
        state="New Jersey", abbreviation="NJ", law_name="NJDPA",
        statute_citation="N.J.S.A. 56:12C-1 through 56:12C-20",
        enacted_date="2024-01-16", effective_date="2025-01-15",
        cure_period_days=None, rights_opt_out_profiling=True, rights_appeal=True,
        universal_opt_out_required=True,
    ),
    StatePrivacyLaw(
        state="Maryland", abbreviation="MD", law_name="MODPA",
        statute_citation="Md. Code Ann., Com. Law 14-4801 through 14-4824",
        enacted_date="2024-05-09", effective_date="2025-10-01",
        cure_period_days=None, rights_opt_out_profiling=True, rights_appeal=True,
        universal_opt_out_required=True,
    ),
]


@dataclass
class ApplicabilityResult:
    """Result of applicability analysis for a state law."""
    state: str = ""
    law_name: str = ""
    applicable: bool = False
    basis: list[str] = field(default_factory=list)
    exemptions_applied: list[str] = field(default_factory=list)
    effective_date: str = ""
    days_until_effective: int = 0


@dataclass
class ComplianceGap:
    """Gap between current programme and state law requirement."""
    state: str = ""
    requirement: str = ""
    current_status: str = ""
    gap_description: str = ""
    priority: str = "medium"


class StatePrivacyLawTracker:
    """
    Tracks US state privacy legislation, assesses applicability,
    identifies compliance gaps, and monitors deadlines.
    """

    def __init__(self):
        self.laws: list[StatePrivacyLaw] = list(ENACTED_LAWS)
        self.custom_laws: list[StatePrivacyLaw] = []

    def get_all_effective_laws(self) -> list[dict]:
        """Return all currently effective state privacy laws."""
        today = date.today().isoformat()
        effective = [
            asdict(law) for law in self.laws
            if law.effective_date <= today and law.status == LawStatus.EFFECTIVE.value
        ]
        return effective

    def get_upcoming_effective_dates(self, within_days: int = 365) -> list[dict]:
        """Return laws becoming effective within the specified period."""
        today = date.today()
        upcoming = []
        for law in self.laws:
            eff = date.fromisoformat(law.effective_date)
            delta = (eff - today).days
            if 0 < delta <= within_days:
                upcoming.append({
                    "state": law.state,
                    "law_name": law.law_name,
                    "effective_date": law.effective_date,
                    "days_until_effective": delta,
                })
        return sorted(upcoming, key=lambda x: x["days_until_effective"])

    def assess_applicability(
        self,
        conducts_business_in: list[str],
        consumers_per_state: dict[str, int],
        annual_revenue: int,
        pct_revenue_from_data_sales: float,
        is_nonprofit: bool = False,
    ) -> list[ApplicabilityResult]:
        """Assess which state laws apply to the organisation."""
        results = []

        for law in self.laws:
            result = ApplicabilityResult(
                state=law.state,
                law_name=law.law_name,
                effective_date=law.effective_date,
            )

            state_consumers = consumers_per_state.get(law.abbreviation, 0)

            if law.abbreviation not in conducts_business_in:
                result.applicable = False
                result.basis.append("Does not conduct business in state")
                results.append(result)
                continue

            if is_nonprofit and law.nonprofit_exempt:
                result.applicable = False
                result.exemptions_applied.append("Non-profit exemption")
                results.append(result)
                continue

            meets_consumer_threshold = state_consumers >= law.consumer_threshold
            meets_revenue = (
                law.revenue_threshold is not None
                and annual_revenue >= law.revenue_threshold
            )
            meets_data_sales = (
                state_consumers >= law.data_sales_consumer_threshold
                and pct_revenue_from_data_sales >= law.data_sales_threshold_pct
            )

            if meets_consumer_threshold:
                result.applicable = True
                result.basis.append(
                    f"Processes {state_consumers:,} consumers (threshold: {law.consumer_threshold:,})"
                )
            if meets_revenue:
                result.applicable = True
                result.basis.append(
                    f"Annual revenue ${annual_revenue:,} meets ${law.revenue_threshold:,} threshold"
                )
            if meets_data_sales:
                result.applicable = True
                result.basis.append(
                    f"Data sales revenue ({pct_revenue_from_data_sales}%) meets threshold"
                )

            if not result.applicable:
                result.basis.append("Does not meet any applicability threshold")

            today = date.today()
            eff = date.fromisoformat(law.effective_date)
            result.days_until_effective = max(0, (eff - today).days)

            results.append(result)

        return results

    def identify_compliance_gaps(
        self,
        applicable_states: list[str],
        supports_access: bool = True,
        supports_delete: bool = True,
        supports_correct: bool = True,
        supports_portability: bool = True,
        supports_opt_out_sale: bool = True,
        supports_opt_out_ads: bool = True,
        supports_opt_out_profiling: bool = False,
        supports_appeal: bool = False,
        supports_universal_opt_out: bool = False,
    ) -> list[ComplianceGap]:
        """Identify compliance gaps across applicable state laws."""
        gaps = []

        for law in self.laws:
            if law.abbreviation not in applicable_states:
                continue

            if law.rights_opt_out_profiling and not supports_opt_out_profiling:
                gaps.append(ComplianceGap(
                    state=law.state,
                    requirement="Opt-out of profiling",
                    current_status="Not supported",
                    gap_description=f"{law.law_name} requires opt-out of profiling right",
                    priority="high",
                ))

            if law.rights_appeal and not supports_appeal:
                gaps.append(ComplianceGap(
                    state=law.state,
                    requirement="Appeal right",
                    current_status="Not supported",
                    gap_description=f"{law.law_name} requires consumer appeal mechanism",
                    priority="high",
                ))

            if law.universal_opt_out_required and not supports_universal_opt_out:
                gaps.append(ComplianceGap(
                    state=law.state,
                    requirement="Universal opt-out mechanism",
                    current_status="Not implemented",
                    gap_description=f"{law.law_name} requires recognition of universal opt-out signals (e.g., GPC)",
                    priority="critical",
                ))

            if not law.nonprofit_exempt:
                gaps.append(ComplianceGap(
                    state=law.state,
                    requirement="Non-profit coverage",
                    current_status="Review needed",
                    gap_description=f"{law.law_name} applies to non-profits — verify compliance if applicable",
                    priority="medium",
                ))

        return gaps

    def get_cure_period_status(self) -> list[dict]:
        """Report cure period availability across states."""
        results = []
        today = date.today()
        for law in self.laws:
            entry = {
                "state": law.state,
                "law_name": law.law_name,
                "cure_period_days": law.cure_period_days,
            }
            if law.cure_period_sunset:
                sunset = date.fromisoformat(law.cure_period_sunset)
                entry["cure_period_sunset"] = law.cure_period_sunset
                entry["cure_period_expired"] = today >= sunset
            else:
                entry["cure_period_sunset"] = None
                entry["cure_period_expired"] = law.cure_period_days is None
            results.append(entry)
        return results

    def generate_summary_report(self) -> dict:
        """Generate a summary of the state privacy law landscape."""
        today = date.today()
        effective = [l for l in self.laws if l.effective_date <= today.isoformat()]
        upcoming = [l for l in self.laws if l.effective_date > today.isoformat()]
        uoo_required = [l for l in self.laws if l.universal_opt_out_required]
        no_cure = [l for l in self.laws if l.cure_period_days is None]
        pra = [l for l in self.laws if l.private_right_of_action]

        return {
            "report_date": today.isoformat(),
            "total_enacted_laws": len(self.laws),
            "currently_effective": len(effective),
            "upcoming": len(upcoming),
            "states_requiring_universal_opt_out": [l.state for l in uoo_required],
            "states_with_no_cure_period": [l.state for l in no_cure],
            "states_with_private_right_of_action": [l.state for l in pra],
            "effective_laws": [
                {"state": l.state, "law": l.law_name, "effective": l.effective_date}
                for l in effective
            ],
        }


if __name__ == "__main__":
    tracker = StatePrivacyLawTracker()

    # Summary report
    summary = tracker.generate_summary_report()
    print("=== US State Privacy Law Landscape ===")
    print(json.dumps(summary, indent=2))

    # Applicability assessment for a mid-size SaaS company
    applicability = tracker.assess_applicability(
        conducts_business_in=["CA", "VA", "CO", "CT", "TX", "OR", "NJ", "MD"],
        consumers_per_state={
            "CA": 450000, "VA": 120000, "CO": 85000, "CT": 60000,
            "TX": 200000, "OR": 55000, "NJ": 95000, "MD": 40000,
        },
        annual_revenue=35000000,
        pct_revenue_from_data_sales=0,
    )

    print("\n=== Applicability Assessment ===")
    for r in applicability:
        print(f"{r.state}: {'APPLICABLE' if r.applicable else 'Not applicable'} — {', '.join(r.basis)}")

    # Identify gaps
    applicable_states = [r.state[:2].upper() for r in applicability if r.applicable]
    gaps = tracker.identify_compliance_gaps(
        applicable_states=["CA", "VA", "CO", "CT", "TX", "OR", "NJ", "MD"],
        supports_access=True,
        supports_delete=True,
        supports_correct=True,
        supports_portability=True,
        supports_opt_out_sale=True,
        supports_opt_out_ads=True,
        supports_opt_out_profiling=False,
        supports_appeal=False,
        supports_universal_opt_out=False,
    )

    print(f"\n=== Compliance Gaps ({len(gaps)} found) ===")
    for gap in gaps:
        print(f"  [{gap.priority.upper()}] {gap.state}: {gap.requirement} — {gap.gap_description}")

    # Cure period status
    print("\n=== Cure Period Status ===")
    for cp in tracker.get_cure_period_status():
        print(json.dumps(cp))
