#!/usr/bin/env python3
"""
CMP Evaluation Scoring Engine

Implements weighted scoring methodology for evaluating and comparing
Consent Management Platforms against regulatory and technical requirements.
"""

import json
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional


EVALUATION_CATEGORIES = {
    "regulatory_compliance": {"weight": 0.30, "label": "Regulatory Compliance"},
    "technical_capabilities": {"weight": 0.25, "label": "Technical Capabilities"},
    "consent_record_management": {"weight": 0.20, "label": "Consent Record Management"},
    "reporting_analytics": {"weight": 0.15, "label": "Reporting and Analytics"},
    "vendor_support": {"weight": 0.10, "label": "Vendor and Support"},
}

EVALUATION_CRITERIA = {
    "regulatory_compliance": [
        {"id": "tcf_v2_2", "name": "TCF v2.2 Certified", "mandatory": True},
        {"id": "gdpr", "name": "GDPR Compliance", "mandatory": True},
        {"id": "ccpa_cpra", "name": "CCPA/CPRA Support", "mandatory": True},
        {"id": "gpc_support", "name": "GPC Signal Detection", "mandatory": True},
        {"id": "lgpd", "name": "LGPD Support", "mandatory": False},
        {"id": "cnil", "name": "CNIL Compliance", "mandatory": True},
        {"id": "multi_jurisdiction", "name": "Multi-Jurisdiction Support", "mandatory": True},
        {"id": "cookie_scanner", "name": "Automated Cookie Scanner", "mandatory": False},
    ],
    "technical_capabilities": [
        {"id": "api", "name": "REST API", "mandatory": True},
        {"id": "tag_manager", "name": "Tag Manager Integration", "mandatory": False},
        {"id": "mobile_sdks", "name": "Mobile SDKs (iOS + Android)", "mandatory": True},
        {"id": "performance", "name": "Page Load Impact (<100ms)", "mandatory": True},
        {"id": "customization", "name": "UI Customization", "mandatory": False},
        {"id": "ab_testing", "name": "Built-in A/B Testing", "mandatory": False},
        {"id": "geolocation", "name": "Geolocation Detection", "mandatory": True},
        {"id": "tc_string", "name": "TC String Generation", "mandatory": True},
    ],
    "consent_record_management": [
        {"id": "consent_receipts", "name": "Audit-Ready Consent Receipts", "mandatory": True},
        {"id": "version_control", "name": "Consent Text Version Control", "mandatory": True},
        {"id": "consent_history", "name": "Full Consent History per User", "mandatory": True},
        {"id": "data_export", "name": "Data Export (JSON/CSV)", "mandatory": True},
        {"id": "retention_controls", "name": "Configurable Retention", "mandatory": False},
        {"id": "search_query", "name": "Search and Query Capability", "mandatory": False},
    ],
    "reporting_analytics": [
        {"id": "dashboard", "name": "Consent Rate Dashboard", "mandatory": False},
        {"id": "trends", "name": "Historical Trend Analysis", "mandatory": False},
        {"id": "compliance_reports", "name": "Pre-Built Compliance Reports", "mandatory": False},
        {"id": "alerting", "name": "Anomaly Alerting", "mandatory": False},
        {"id": "gpc_reporting", "name": "GPC Detection Reporting", "mandatory": False},
    ],
    "vendor_support": [
        {"id": "dpa", "name": "GDPR DPA Available", "mandatory": True},
        {"id": "eu_hosting", "name": "EU Data Hosting", "mandatory": True},
        {"id": "sla", "name": "99.9%+ Uptime SLA", "mandatory": True},
        {"id": "support_quality", "name": "Dedicated Support", "mandatory": False},
        {"id": "pricing", "name": "Transparent Pricing", "mandatory": False},
    ],
}


@dataclass
class VendorScore:
    """Score for a single CMP vendor."""
    vendor_name: str = ""
    category_scores: dict = field(default_factory=dict)
    criterion_scores: dict = field(default_factory=dict)
    weighted_total: float = 0.0
    mandatory_met: bool = True
    mandatory_failures: list = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


def score_vendor(vendor_name: str, scores: dict[str, float]) -> VendorScore:
    """
    Score a CMP vendor against evaluation criteria.

    Args:
        vendor_name: Name of the CMP vendor.
        scores: Dict of criterion_id -> score (0.0 to 10.0).

    Returns:
        VendorScore with category and weighted totals.
    """
    result = VendorScore(vendor_name=vendor_name)
    result.criterion_scores = scores.copy()

    for cat_id, cat_info in EVALUATION_CATEGORIES.items():
        criteria = EVALUATION_CRITERIA.get(cat_id, [])
        if not criteria:
            continue

        cat_total = 0.0
        cat_count = 0

        for criterion in criteria:
            cid = criterion["id"]
            score = scores.get(cid, 0.0)
            cat_total += score
            cat_count += 1

            # Check mandatory requirements
            if criterion["mandatory"] and score < 5.0:
                result.mandatory_met = False
                result.mandatory_failures.append({
                    "criterion": criterion["name"],
                    "score": score,
                    "category": cat_info["label"],
                })

        cat_avg = cat_total / cat_count if cat_count > 0 else 0.0
        result.category_scores[cat_id] = {
            "label": cat_info["label"],
            "average": round(cat_avg, 2),
            "weight": cat_info["weight"],
            "weighted": round(cat_avg * cat_info["weight"], 2),
        }

    result.weighted_total = round(
        sum(cs["weighted"] for cs in result.category_scores.values()), 2
    )

    return result


def compare_vendors(vendor_scores: list[VendorScore]) -> dict:
    """
    Compare multiple CMP vendors and produce a ranking.

    Returns:
        Comparison report with rankings.
    """
    # Filter to those meeting mandatory requirements
    qualified = [v for v in vendor_scores if v.mandatory_met]
    disqualified = [v for v in vendor_scores if not v.mandatory_met]

    # Sort by weighted total (descending)
    qualified.sort(key=lambda v: v.weighted_total, reverse=True)

    ranking = []
    for i, vendor in enumerate(qualified, 1):
        ranking.append({
            "rank": i,
            "vendor": vendor.vendor_name,
            "weighted_total": vendor.weighted_total,
            "category_breakdown": {
                cat_id: cs["weighted"]
                for cat_id, cs in vendor.category_scores.items()
            },
        })

    return {
        "evaluation_date": datetime.now(timezone.utc).isoformat(),
        "total_vendors_evaluated": len(vendor_scores),
        "qualified_vendors": len(qualified),
        "disqualified_vendors": len(disqualified),
        "ranking": ranking,
        "disqualified": [
            {"vendor": v.vendor_name, "failures": v.mandatory_failures}
            for v in disqualified
        ],
        "recommended": qualified[0].vendor_name if qualified else "No vendor meets all mandatory requirements",
    }


if __name__ == "__main__":
    # Score vendors based on CloudVault SaaS Inc. evaluation
    vendors_data = {
        "OneTrust": {
            "tcf_v2_2": 10, "gdpr": 10, "ccpa_cpra": 10, "gpc_support": 9,
            "lgpd": 9, "cnil": 10, "multi_jurisdiction": 10, "cookie_scanner": 9,
            "api": 10, "tag_manager": 9, "mobile_sdks": 9, "performance": 7,
            "customization": 9, "ab_testing": 8, "geolocation": 9, "tc_string": 10,
            "consent_receipts": 9, "version_control": 9, "consent_history": 9,
            "data_export": 9, "retention_controls": 8, "search_query": 9,
            "dashboard": 9, "trends": 8, "compliance_reports": 9,
            "alerting": 8, "gpc_reporting": 8,
            "dpa": 10, "eu_hosting": 10, "sla": 10, "support_quality": 9, "pricing": 6,
        },
        "Usercentrics": {
            "tcf_v2_2": 10, "gdpr": 10, "ccpa_cpra": 9, "gpc_support": 9,
            "lgpd": 8, "cnil": 10, "multi_jurisdiction": 8, "cookie_scanner": 9,
            "api": 9, "tag_manager": 9, "mobile_sdks": 10, "performance": 8,
            "customization": 9, "ab_testing": 9, "geolocation": 8, "tc_string": 10,
            "consent_receipts": 9, "version_control": 9, "consent_history": 9,
            "data_export": 9, "retention_controls": 8, "search_query": 8,
            "dashboard": 9, "trends": 8, "compliance_reports": 8,
            "alerting": 7, "gpc_reporting": 8,
            "dpa": 10, "eu_hosting": 10, "sla": 9, "support_quality": 8, "pricing": 8,
        },
        "Cookiebot": {
            "tcf_v2_2": 10, "gdpr": 10, "ccpa_cpra": 8, "gpc_support": 8,
            "lgpd": 6, "cnil": 9, "multi_jurisdiction": 7, "cookie_scanner": 10,
            "api": 7, "tag_manager": 9, "mobile_sdks": 4, "performance": 9,
            "customization": 7, "ab_testing": 4, "geolocation": 8, "tc_string": 10,
            "consent_receipts": 7, "version_control": 8, "consent_history": 7,
            "data_export": 7, "retention_controls": 6, "search_query": 6,
            "dashboard": 6, "trends": 5, "compliance_reports": 6,
            "alerting": 4, "gpc_reporting": 5,
            "dpa": 10, "eu_hosting": 10, "sla": 9, "support_quality": 6, "pricing": 10,
        },
    }

    vendor_results = []
    for name, scores in vendors_data.items():
        result = score_vendor(name, scores)
        vendor_results.append(result)

    # Compare vendors
    comparison = compare_vendors(vendor_results)

    print("=== CMP Vendor Comparison ===")
    print(f"Vendors evaluated: {comparison['total_vendors_evaluated']}")
    print(f"Qualified: {comparison['qualified_vendors']}")
    print(f"Recommended: {comparison['recommended']}")

    print("\n=== Rankings ===")
    for entry in comparison["ranking"]:
        print(f"  #{entry['rank']}: {entry['vendor']} (Score: {entry['weighted_total']:.2f}/10)")
        for cat, score in entry["category_breakdown"].items():
            label = EVALUATION_CATEGORIES[cat]["label"]
            print(f"       {label}: {score:.2f}")

    if comparison["disqualified"]:
        print("\n=== Disqualified ===")
        for dq in comparison["disqualified"]:
            print(f"  {dq['vendor']}:")
            for f in dq["failures"]:
                print(f"    FAIL: {f['criterion']} (score: {f['score']})")
