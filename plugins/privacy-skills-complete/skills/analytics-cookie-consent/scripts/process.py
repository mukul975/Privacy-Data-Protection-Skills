"""
Analytics Consent Impact Analyzer

Estimates the impact of cookie consent rates on analytics data quality
and generates recommendations for privacy-preserving measurement.

Requirements:
    No external dependencies (uses standard library only)
"""

import json
import os
from datetime import datetime, timezone


class AnalyticsConsentAnalyzer:
    """Analyzes the impact of consent rates on analytics data quality."""

    # Industry benchmark consent rates
    CONSENT_RATE_BENCHMARKS = {
        "accept_prominent_reject_buried": {
            "description": "Accept All prominent, Reject buried in settings",
            "consent_rate": 0.85,
            "cnil_compliant": False,
        },
        "equal_prominence": {
            "description": "Equal prominence Accept/Reject (CNIL-compliant)",
            "consent_rate": 0.50,
            "cnil_compliant": True,
        },
        "reject_default": {
            "description": "Reject All as default/prominent action",
            "consent_rate": 0.28,
            "cnil_compliant": True,
        },
        "cookie_wall": {
            "description": "Cookie wall (must accept to access)",
            "consent_rate": 0.92,
            "cnil_compliant": False,
        },
    }

    # GA4 behavioral modeling recovery rates
    CONSENT_MODE_RECOVERY = {
        "user_count": 0.25,  # Recovers ~25% of lost user data
        "session_count": 0.20,
        "pageview_count": 0.15,
        "conversion_count": 0.30,  # Conversion modeling is more effective
    }

    def __init__(self, org_name: str, daily_users: int, daily_sessions: int,
                 daily_pageviews: int, daily_conversions: int):
        self.org_name = org_name
        self.daily_users = daily_users
        self.daily_sessions = daily_sessions
        self.daily_pageviews = daily_pageviews
        self.daily_conversions = daily_conversions

    def analyze_consent_impact(self, banner_type: str = "equal_prominence") -> dict:
        """Analyze impact of a given banner type on analytics data."""
        benchmark = self.CONSENT_RATE_BENCHMARKS.get(banner_type)
        if not benchmark:
            raise ValueError(f"Unknown banner type: {banner_type}")

        consent_rate = benchmark["consent_rate"]
        decline_rate = 1 - consent_rate

        # Direct measurement (consenting users)
        direct_users = int(self.daily_users * consent_rate)
        direct_sessions = int(self.daily_sessions * consent_rate)
        direct_pageviews = int(self.daily_pageviews * consent_rate)
        direct_conversions = int(self.daily_conversions * consent_rate)

        # Consent Mode behavioral modeling recovery
        recovered_users = int(
            self.daily_users * decline_rate * self.CONSENT_MODE_RECOVERY["user_count"]
        )
        recovered_sessions = int(
            self.daily_sessions * decline_rate * self.CONSENT_MODE_RECOVERY["session_count"]
        )
        recovered_conversions = int(
            self.daily_conversions * decline_rate * self.CONSENT_MODE_RECOVERY["conversion_count"]
        )

        # GA4 modeling eligibility
        modeling_eligible = direct_users >= 1000

        # Conversion modeling eligibility (per conversion action)
        conversion_modeling_eligible = direct_conversions >= 70

        total_coverage = {
            "users": min(100, round((direct_users + recovered_users) / self.daily_users * 100, 1)),
            "sessions": min(100, round((direct_sessions + recovered_sessions) / self.daily_sessions * 100, 1)),
            "conversions": min(100, round((direct_conversions + recovered_conversions) / self.daily_conversions * 100, 1)) if self.daily_conversions > 0 else 0,
        }

        return {
            "banner_type": banner_type,
            "banner_description": benchmark["description"],
            "cnil_compliant": benchmark["cnil_compliant"],
            "consent_rate": consent_rate,
            "actual_traffic": {
                "daily_users": self.daily_users,
                "daily_sessions": self.daily_sessions,
                "daily_pageviews": self.daily_pageviews,
                "daily_conversions": self.daily_conversions,
            },
            "direct_measurement": {
                "users": direct_users,
                "sessions": direct_sessions,
                "pageviews": direct_pageviews,
                "conversions": direct_conversions,
            },
            "consent_mode_modeling": {
                "recovered_users": recovered_users,
                "recovered_sessions": recovered_sessions,
                "recovered_conversions": recovered_conversions,
                "modeling_eligible": modeling_eligible,
                "conversion_modeling_eligible": conversion_modeling_eligible,
            },
            "total_coverage": total_coverage,
            "data_gap": {
                "users_missing": max(0, round(100 - total_coverage["users"], 1)),
                "sessions_missing": max(0, round(100 - total_coverage["sessions"], 1)),
                "conversions_missing": max(0, round(100 - total_coverage["conversions"], 1)),
            },
        }

    def compare_all_banner_types(self) -> dict:
        """Compare analytics impact across all banner types."""
        comparisons = {}
        for banner_type in self.CONSENT_RATE_BENCHMARKS:
            comparisons[banner_type] = self.analyze_consent_impact(banner_type)

        return {
            "organization": self.org_name,
            "analysis_date": datetime.now(timezone.utc).isoformat(),
            "baseline_traffic": {
                "daily_users": self.daily_users,
                "daily_sessions": self.daily_sessions,
                "daily_pageviews": self.daily_pageviews,
                "daily_conversions": self.daily_conversions,
            },
            "comparisons": comparisons,
            "recommendation": self._generate_recommendation(comparisons),
        }

    def _generate_recommendation(self, comparisons: dict) -> dict:
        """Generate recommendation based on analysis."""
        compliant_options = {
            k: v for k, v in comparisons.items() if v["cnil_compliant"]
        }

        best_compliant = max(
            compliant_options.items(),
            key=lambda x: x[1]["total_coverage"]["users"],
        )

        return {
            "recommended_banner_type": best_compliant[0],
            "reason": "Best data coverage among CNIL-compliant options",
            "expected_consent_rate": best_compliant[1]["consent_rate"],
            "expected_user_coverage": best_compliant[1]["total_coverage"]["users"],
            "supplementary_analytics": [
                {
                    "tool": "Matomo (self-hosted, CNIL-exempt)",
                    "coverage": "100% of users",
                    "data_granularity": "Per-session",
                    "consent_required": "No (under CNIL exemption with correct configuration)",
                },
                {
                    "tool": "Server-side log analysis",
                    "coverage": "100% of requests",
                    "data_granularity": "Aggregate",
                    "consent_required": "No (operational necessity)",
                },
            ],
        }


def main():
    """Run analytics consent impact analysis for Pinnacle E-Commerce Ltd."""
    analyzer = AnalyticsConsentAnalyzer(
        org_name="Pinnacle E-Commerce Ltd",
        daily_users=15000,
        daily_sessions=22000,
        daily_pageviews=85000,
        daily_conversions=450,
    )

    report = analyzer.compare_all_banner_types()

    output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "reports")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "consent_impact_analysis.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("=== Analytics Consent Impact Analysis ===")
    print(f"Organization: {report['organization']}")
    print(f"\nBaseline: {report['baseline_traffic']['daily_users']} daily users")

    for banner_type, data in report["comparisons"].items():
        compliant_tag = " (CNIL-compliant)" if data["cnil_compliant"] else " (NON-COMPLIANT)"
        print(f"\n{data['banner_description']}{compliant_tag}:")
        print(f"  Consent rate: {data['consent_rate'] * 100:.0f}%")
        print(f"  Direct users: {data['direct_measurement']['users']}")
        print(f"  Total coverage: {data['total_coverage']['users']}%")

    rec = report["recommendation"]
    print(f"\nRecommendation: {rec['recommended_banner_type']}")
    print(f"  Expected coverage: {rec['expected_user_coverage']}%")
    print(f"  Supplement with: {', '.join(s['tool'] for s in rec['supplementary_analytics'])}")
    print(f"\nReport saved to {output_path}")


if __name__ == "__main__":
    main()
