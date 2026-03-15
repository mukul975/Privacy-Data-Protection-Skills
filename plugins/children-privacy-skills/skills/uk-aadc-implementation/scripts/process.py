#!/usr/bin/env python3
"""
UK AADC Conformance Assessment Tool

Evaluates conformance with the UK Age Appropriate Design Code (Children's Code)
15 standards for information society services likely to be accessed by children.
"""

import json
from datetime import datetime, timezone

AADC_STANDARDS = [
    {"id": 1, "name": "Best interests of the child", "section": "Standard 1"},
    {"id": 2, "name": "Data protection impact assessments", "section": "Standard 2"},
    {"id": 3, "name": "Age-appropriate application", "section": "Standard 3"},
    {"id": 4, "name": "Transparency", "section": "Standard 4"},
    {"id": 5, "name": "Detrimental use of data", "section": "Standard 5"},
    {"id": 6, "name": "Policies and community standards", "section": "Standard 6"},
    {"id": 7, "name": "Default settings", "section": "Standard 7"},
    {"id": 8, "name": "Data minimisation", "section": "Standard 8"},
    {"id": 9, "name": "Data sharing", "section": "Standard 9"},
    {"id": 10, "name": "Geolocation", "section": "Standard 10"},
    {"id": 11, "name": "Parental controls", "section": "Standard 11"},
    {"id": 12, "name": "Profiling", "section": "Standard 12"},
    {"id": 13, "name": "Nudge techniques", "section": "Standard 13"},
    {"id": 14, "name": "Connected toys and devices", "section": "Standard 14"},
    {"id": 15, "name": "Online tools", "section": "Standard 15"},
]

ASSESSMENT_CRITERIA = {
    1: [
        "Best Interests Assessment (BIA) completed for all features",
        "BIA references UNCRC Articles 3, 12, 16, 31",
        "Children's interests weighed against commercial interests",
        "BIA reviewed when features change",
    ],
    2: [
        "Child-specific DPIA conducted",
        "DPIA segmented by developmental age group",
        "Child-specific harms assessed (grooming, bullying, commercial pressure)",
        "DPIA reviewed annually",
    ],
    3: [
        "Age assurance mechanism implemented",
        "Assurance level proportionate to risk",
        "Different design standards for different age groups",
        "Age data used only for age assurance purposes",
    ],
    4: [
        "Child-friendly privacy notice provided",
        "Notice tested with children for comprehension",
        "Just-in-time notices at collection points",
        "Language appropriate to target age group",
    ],
    5: [
        "Detrimental use register maintained",
        "No behavioural advertising to children",
        "No dark patterns in child experience",
        "Regular review against research on children's wellbeing",
    ],
    6: [
        "Published policies consistently enforced",
        "Child-accessible reporting mechanisms available",
        "Transparency report published",
    ],
    7: [
        "Profile visibility defaults to private",
        "Location sharing defaults to off",
        "Personalised advertising defaults to off",
        "Data sharing defaults to off",
        "Non-high-privacy defaults documented with compelling reason",
    ],
    8: [
        "Data limited to active, knowing engagement features",
        "Background data collection disabled unless feature-triggered",
        "Separate choices for optional data-intensive features",
    ],
    9: [
        "Children's data not shared unless compelling reason documented",
        "Third parties contractually bound to equivalent protections",
        "Transparent notice about any data sharing",
    ],
    10: [
        "Geolocation defaults to off",
        "Visible indicator when location tracking active",
        "Location visibility to others defaults to off",
        "Lowest necessary precision used",
    ],
    11: [
        "Child informed about parental controls in age-appropriate language",
        "Visible indicator when monitoring is active",
        "Child's evolving autonomy respected for older teens",
    ],
    12: [
        "Profiling defaults to off",
        "Content diversity safeguards for recommendations",
        "Time-limitation mechanisms implemented",
        "Mental health circuit-breakers active",
        "Annual algorithmic impact assessment conducted",
    ],
    13: [
        "Accept/reject options equally prominent",
        "No rewards for data or weakened privacy",
        "No confirmshaming or asymmetric choice architecture",
        "Privacy-first defaults presented",
    ],
    14: [
        "Connected device complies with all 15 standards",
        "Clear setup instructions for parents",
        "Recording/transmission indicator active",
        "Data deletion mechanism for device and cloud",
    ],
    15: [
        "Child-accessible privacy centre provided",
        "One-click data download and deletion available",
        "Reporting tools require no additional data",
        "Responses within one-month timeline",
    ],
}


def run_aadc_assessment(responses: dict[int, str], notes: dict[int, str] | None = None) -> dict:
    """
    Run AADC conformance assessment.

    Args:
        responses: Dict mapping standard ID to "conforming", "partially_conforming",
                   "non_conforming", or "na".
        notes: Optional dict mapping standard ID to assessment notes.

    Returns:
        Assessment report.
    """
    if notes is None:
        notes = {}

    results = []
    conforming = 0
    partial = 0
    non_conforming = 0
    na_count = 0

    for standard in AADC_STANDARDS:
        sid = standard["id"]
        status = responses.get(sid, "not_assessed")

        if status == "conforming":
            conforming += 1
        elif status == "partially_conforming":
            partial += 1
        elif status == "non_conforming":
            non_conforming += 1
        elif status == "na":
            na_count += 1

        results.append({
            "id": sid,
            "standard": standard["name"],
            "section": standard["section"],
            "criteria": ASSESSMENT_CRITERIA.get(sid, []),
            "status": status,
            "notes": notes.get(sid, ""),
        })

    applicable = conforming + partial + non_conforming
    conformance_rate = (conforming / applicable * 100) if applicable > 0 else 0.0

    return {
        "assessment_date": datetime.now(timezone.utc).isoformat(),
        "controller": "BrightPath Learning Inc.",
        "framework": "UK Age Appropriate Design Code (Children's Code)",
        "results": results,
        "summary": {
            "total_standards": 15,
            "conforming": conforming,
            "partially_conforming": partial,
            "non_conforming": non_conforming,
            "not_applicable": na_count,
            "not_assessed": 15 - conforming - partial - non_conforming - na_count,
            "conformance_rate_percent": round(conformance_rate, 1),
        },
        "overall_assessment": (
            "CONFORMING" if non_conforming == 0 and partial == 0
            else "PARTIALLY CONFORMING" if non_conforming == 0
            else "NON-CONFORMING"
        ),
    }


def check_default_settings(settings: list[dict]) -> dict:
    """
    Audit default settings against AADC Standard 7 requirements.

    Args:
        settings: List of dicts with keys: name, default_value, is_high_privacy,
                  compelling_reason (optional).

    Returns:
        Audit result.
    """
    conforming = []
    non_conforming = []
    exceptions = []

    for setting in settings:
        name = setting["name"]
        is_high_privacy = setting.get("is_high_privacy", False)
        compelling = setting.get("compelling_reason", "")

        if is_high_privacy:
            conforming.append({"name": name, "status": "conforming"})
        elif compelling:
            exceptions.append({
                "name": name,
                "status": "exception",
                "compelling_reason": compelling,
            })
        else:
            non_conforming.append({
                "name": name,
                "status": "non_conforming",
                "current_default": setting.get("default_value", "unknown"),
                "required_default": "high_privacy",
            })

    return {
        "audit_date": datetime.now(timezone.utc).isoformat(),
        "total_settings": len(settings),
        "conforming": len(conforming),
        "exceptions_with_reason": len(exceptions),
        "non_conforming": len(non_conforming),
        "details": {
            "conforming": conforming,
            "exceptions": exceptions,
            "non_conforming": non_conforming,
        },
        "overall": "PASS" if len(non_conforming) == 0 else "FAIL",
    }


if __name__ == "__main__":
    print("=== AADC Conformance Assessment ===")
    sample_responses = {
        1: "conforming", 2: "conforming", 3: "conforming",
        4: "conforming", 5: "conforming", 6: "conforming",
        7: "conforming", 8: "conforming", 9: "conforming",
        10: "conforming", 11: "conforming", 12: "conforming",
        13: "conforming", 14: "na", 15: "conforming",
    }

    report = run_aadc_assessment(sample_responses)
    print(f"Overall: {report['overall_assessment']}")
    print(f"Conformance Rate: {report['summary']['conformance_rate_percent']}%")
    print(f"Conforming: {report['summary']['conforming']}, "
          f"Partial: {report['summary']['partially_conforming']}, "
          f"Non-conforming: {report['summary']['non_conforming']}, "
          f"N/A: {report['summary']['not_applicable']}")

    print("\n=== Default Settings Audit ===")
    sample_settings = [
        {"name": "Profile visibility", "default_value": "private", "is_high_privacy": True},
        {"name": "Location sharing", "default_value": "off", "is_high_privacy": True},
        {"name": "Personalised advertising", "default_value": "off", "is_high_privacy": True},
        {"name": "Push notifications", "default_value": "on",
         "is_high_privacy": False,
         "compelling_reason": "Educational reminders support learning outcomes"},
        {"name": "Data sharing", "default_value": "off", "is_high_privacy": True},
    ]

    audit = check_default_settings(sample_settings)
    print(f"Overall: {audit['overall']}")
    print(f"Conforming: {audit['conforming']}, Exceptions: {audit['exceptions_with_reason']}, "
          f"Non-conforming: {audit['non_conforming']}")
