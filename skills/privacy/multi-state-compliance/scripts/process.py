#!/usr/bin/env python3
"""
Multi-State Privacy Compliance Assessment Engine

Evaluates applicability across all US state privacy laws, generates
common requirements matrix, identifies state-specific deltas, and
produces a unified compliance status report.
"""

import json
from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class State(Enum):
    CALIFORNIA = "california"
    VIRGINIA = "virginia"
    COLORADO = "colorado"
    CONNECTICUT = "connecticut"
    TEXAS = "texas"
    OREGON = "oregon"
    MONTANA = "montana"
    KENTUCKY = "kentucky"


STATE_LAWS = {
    State.CALIFORNIA: {
        "law": "CCPA/CPRA",
        "citation": "Cal. Civ. Code §1798.100-199",
        "effective": "2020-01-01",
        "threshold_1_consumers": 100_000,
        "threshold_2_consumers": None,
        "threshold_2_revenue_pct": 50,
        "revenue_threshold": 25_000_000,
        "cure_period_days": 0,
        "universal_opt_out": True,
        "private_right_of_action": True,
        "nonprofit_covered": False,
        "sensitive_data_model": "limit_right",
        "max_penalty": 7_500,
    },
    State.VIRGINIA: {
        "law": "VCDPA",
        "citation": "Va. Code §59.1-575-585",
        "effective": "2023-01-01",
        "threshold_1_consumers": 100_000,
        "threshold_2_consumers": 25_000,
        "threshold_2_revenue_pct": 50,
        "revenue_threshold": None,
        "cure_period_days": 30,
        "universal_opt_out": False,
        "private_right_of_action": False,
        "nonprofit_covered": False,
        "sensitive_data_model": "opt_in_consent",
        "max_penalty": 7_500,
    },
    State.COLORADO: {
        "law": "CPA",
        "citation": "C.R.S. §6-1-1301-1313",
        "effective": "2023-07-01",
        "threshold_1_consumers": 100_000,
        "threshold_2_consumers": 25_000,
        "threshold_2_revenue_pct": 0,
        "revenue_threshold": None,
        "cure_period_days": 0,
        "universal_opt_out": True,
        "private_right_of_action": False,
        "nonprofit_covered": False,
        "sensitive_data_model": "opt_in_consent",
        "max_penalty": 20_000,
    },
    State.CONNECTICUT: {
        "law": "CTDPA",
        "citation": "Conn. Gen. Stat. §42-515-525",
        "effective": "2023-07-01",
        "threshold_1_consumers": 100_000,
        "threshold_2_consumers": 25_000,
        "threshold_2_revenue_pct": 25,
        "revenue_threshold": None,
        "cure_period_days": 0,
        "universal_opt_out": True,
        "private_right_of_action": False,
        "nonprofit_covered": False,
        "sensitive_data_model": "opt_in_consent",
        "max_penalty": 5_000,
    },
    State.TEXAS: {
        "law": "TDPSA",
        "citation": "Tex. Bus. & Com. Code §541.001-203",
        "effective": "2024-07-01",
        "threshold_1_consumers": 0,
        "threshold_2_consumers": None,
        "threshold_2_revenue_pct": None,
        "revenue_threshold": None,
        "cure_period_days": 30,
        "universal_opt_out": False,
        "private_right_of_action": False,
        "nonprofit_covered": False,
        "sensitive_data_model": "opt_in_consent",
        "max_penalty": 7_500,
    },
    State.OREGON: {
        "law": "OCPA",
        "citation": "ORS §646A.570-604",
        "effective": "2024-07-01",
        "threshold_1_consumers": 100_000,
        "threshold_2_consumers": 25_000,
        "threshold_2_revenue_pct": 25,
        "revenue_threshold": None,
        "cure_period_days": 14,
        "universal_opt_out": False,
        "private_right_of_action": False,
        "nonprofit_covered": True,
        "sensitive_data_model": "opt_in_consent",
        "max_penalty": 25_000,
    },
    State.MONTANA: {
        "law": "MTDPA",
        "citation": "MCA §30-14-2801-2817",
        "effective": "2024-10-01",
        "threshold_1_consumers": 50_000,
        "threshold_2_consumers": 25_000,
        "threshold_2_revenue_pct": 25,
        "revenue_threshold": None,
        "cure_period_days": 60,
        "universal_opt_out": True,
        "private_right_of_action": False,
        "nonprofit_covered": False,
        "sensitive_data_model": "opt_in_consent",
        "max_penalty": None,
    },
    State.KENTUCKY: {
        "law": "KPPA",
        "citation": "KRS §367.401-445",
        "effective": "2026-01-01",
        "threshold_1_consumers": 100_000,
        "threshold_2_consumers": 25_000,
        "threshold_2_revenue_pct": 50,
        "revenue_threshold": None,
        "cure_period_days": 30,
        "universal_opt_out": False,
        "private_right_of_action": False,
        "nonprofit_covered": False,
        "sensitive_data_model": "opt_in_consent",
        "max_penalty": 7_500,
    },
}


@dataclass
class StateConsumerData:
    """Consumer data count and revenue for a specific state."""
    state: State
    consumer_count: int
    revenue_from_sale_pct: float


@dataclass
class MultiStateAssessment:
    """Assess applicability across all state privacy laws."""
    organization_name: str
    annual_revenue: float
    is_nonprofit: bool
    is_sba_small_business: bool
    state_data: list[StateConsumerData] = field(default_factory=list)

    def assess_all(self) -> dict:
        results = []
        applicable_states = []
        non_applicable_states = []

        for sd in self.state_data:
            law_info = STATE_LAWS[sd.state]
            applicable = False
            reasons = []

            # Texas special: no threshold for non-small businesses
            if sd.state == State.TEXAS:
                if not self.is_sba_small_business:
                    applicable = True
                    reasons.append("Non-SBA small business — no threshold")
                else:
                    reasons.append("SBA small business — most provisions exempt")

            # Oregon special: nonprofits covered
            elif sd.state == State.OREGON and self.is_nonprofit and not law_info["nonprofit_covered"]:
                pass  # Oregon covers nonprofits, this is handled below

            else:
                # California has revenue alternative
                if sd.state == State.CALIFORNIA and self.annual_revenue > 25_000_000:
                    applicable = True
                    reasons.append(f"Revenue ${self.annual_revenue:,.0f} > $25M")

                # Threshold 1
                if law_info["threshold_1_consumers"] and sd.consumer_count >= law_info["threshold_1_consumers"]:
                    applicable = True
                    reasons.append(f"{sd.consumer_count:,} consumers >= {law_info['threshold_1_consumers']:,}")

                # Threshold 2
                if (law_info["threshold_2_consumers"] and
                    sd.consumer_count >= law_info["threshold_2_consumers"] and
                    law_info["threshold_2_revenue_pct"] is not None and
                    sd.revenue_from_sale_pct > law_info["threshold_2_revenue_pct"]):
                    applicable = True
                    reasons.append(f"{sd.consumer_count:,} consumers + {sd.revenue_from_sale_pct}% revenue")

            # Nonprofit check
            if self.is_nonprofit and not law_info.get("nonprofit_covered", False) and sd.state != State.CALIFORNIA:
                applicable = False
                reasons = ["Nonprofit exemption applies"]

            result = {
                "state": sd.state.value,
                "law": law_info["law"],
                "applicable": applicable,
                "reasons": reasons,
                "consumer_count": sd.consumer_count,
                "cure_period_days": law_info["cure_period_days"],
                "universal_opt_out_required": law_info["universal_opt_out"],
                "max_penalty": law_info["max_penalty"],
            }
            results.append(result)

            if applicable:
                applicable_states.append(sd.state.value)
            else:
                non_applicable_states.append(sd.state.value)

        return {
            "organization": self.organization_name,
            "assessment_date": datetime.now(timezone.utc).isoformat(),
            "total_states_assessed": len(self.state_data),
            "applicable_states": applicable_states,
            "non_applicable_states": non_applicable_states,
            "state_results": results,
        }


def generate_delta_report() -> list[dict]:
    """Generate state-specific delta report showing unique requirements."""
    deltas = [
        {"state": "California", "delta": "Sensitive PI limit right (not opt-in consent)", "impact": "Different consent UX"},
        {"state": "California", "delta": "CPPA dedicated enforcement agency", "impact": "Higher enforcement activity"},
        {"state": "California", "delta": "Private right of action for data breaches", "impact": "Litigation exposure"},
        {"state": "California", "delta": "No cure period", "impact": "Immediate enforcement risk"},
        {"state": "California", "delta": "Retention period disclosure required", "impact": "Privacy notice content"},
        {"state": "Colorado", "delta": "Broadest profiling opt-out scope (7+ categories)", "impact": "Wider opt-out coverage"},
        {"state": "Colorado", "delta": "AG rulemaking (4 CCR 904-3)", "impact": "Detailed implementation requirements"},
        {"state": "Connecticut", "delta": "Dark pattern statutory definition and prohibition", "impact": "Consent UI audit required"},
        {"state": "Connecticut", "delta": "Loyalty program exemption", "impact": "Exemption assessment needed"},
        {"state": "Texas", "delta": "No revenue/consumer threshold", "impact": "Broadest applicability"},
        {"state": "Texas", "delta": "Data broker registration", "impact": "Registration if applicable"},
        {"state": "Oregon", "delta": "Nonprofit applicability", "impact": "Nonprofit organizations must comply"},
        {"state": "Oregon", "delta": "Specific third-party list right", "impact": "More detailed data sharing records needed"},
        {"state": "Oregon", "delta": "Most detailed de-identified data requirements", "impact": "De-identification compliance program"},
        {"state": "Oregon", "delta": "Transgender/nonbinary as sensitive data", "impact": "Additional consent category"},
        {"state": "Oregon", "delta": "14-day cure period (shortest)", "impact": "Faster remediation required"},
        {"state": "Montana", "delta": "50,000 consumer threshold (lowest)", "impact": "Catches smaller operations"},
        {"state": "Montana", "delta": "15-day extension only (60 total)", "impact": "Tighter response timeline"},
    ]
    return deltas


if __name__ == "__main__":
    # Multi-state assessment for Liberty Commerce Inc.
    print("=== Multi-State Applicability Assessment ===")
    assessment = MultiStateAssessment(
        organization_name="Liberty Commerce Inc.",
        annual_revenue=48_000_000,
        is_nonprofit=False,
        is_sba_small_business=False,
        state_data=[
            StateConsumerData(State.CALIFORNIA, 320_000, 12.0),
            StateConsumerData(State.VIRGINIA, 145_000, 12.0),
            StateConsumerData(State.COLORADO, 98_000, 12.0),
            StateConsumerData(State.CONNECTICUT, 87_000, 12.0),
            StateConsumerData(State.TEXAS, 410_000, 12.0),
            StateConsumerData(State.OREGON, 72_000, 12.0),
            StateConsumerData(State.MONTANA, 28_000, 12.0),
            StateConsumerData(State.KENTUCKY, 68_000, 12.0),
        ],
    )
    result = assessment.assess_all()
    print(f"Applicable states: {', '.join(result['applicable_states'])}")
    print(f"Non-applicable states: {', '.join(result['non_applicable_states'])}")

    # State-specific deltas
    print("\n=== State-Specific Deltas ===")
    for delta in generate_delta_report():
        print(f"  [{delta['state']}] {delta['delta']}")
