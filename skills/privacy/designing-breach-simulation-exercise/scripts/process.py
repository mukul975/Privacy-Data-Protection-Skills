#!/usr/bin/env python3
"""
Breach Simulation Exercise Designer

Generates exercise scenarios with timed injects, participant role assignments,
evaluation scorecards, and after-action report frameworks.
"""

import json
from datetime import datetime, timezone, timedelta
from typing import Optional


SCENARIOS = {
    "ransomware_customer_db": {
        "title": "Ransomware Attack on Customer Database",
        "difficulty": "high",
        "duration_hours": 3.5,
        "participants_min": 8,
        "participants_max": 15,
        "gdpr_relevant": True,
        "hipaa_relevant": False,
        "narrative": (
            "A sophisticated threat actor deploys LockBit 3.0 ransomware targeting "
            "the production customer database cluster. The attack begins with a "
            "spear-phishing email to an IT administrator on the preceding Monday. "
            "The attacker harvests credentials, moves laterally, and deploys "
            "ransomware on Friday morning, encrypting 48,720 customer records."
        ),
    },
    "insider_employee_data": {
        "title": "Insider Threat — Departing Employee Data Theft",
        "difficulty": "medium",
        "duration_hours": 2.5,
        "participants_min": 6,
        "participants_max": 12,
        "gdpr_relevant": True,
        "hipaa_relevant": False,
        "narrative": (
            "A senior data analyst who has submitted resignation downloads 3,400 "
            "employee records including names, salaries, performance ratings, and "
            "health screening results to a personal cloud storage account."
        ),
    },
    "processor_breach": {
        "title": "Third-Party Processor Breach",
        "difficulty": "high",
        "duration_hours": 3.0,
        "participants_min": 8,
        "participants_max": 15,
        "gdpr_relevant": True,
        "hipaa_relevant": False,
        "narrative": (
            "The cloud analytics processor notifies Stellar Payments 5 days "
            "after discovering a breach affecting 42,000 customer records. "
            "The processor provides minimal details and disputes GDPR applicability."
        ),
    },
    "health_data_breach": {
        "title": "Healthcare PHI Exposure via Misconfigured Cloud Storage",
        "difficulty": "high",
        "duration_hours": 3.0,
        "participants_min": 8,
        "participants_max": 15,
        "gdpr_relevant": True,
        "hipaa_relevant": True,
        "narrative": (
            "The employee health plan's claims processing system is found to have "
            "an S3 bucket containing 8,420 employee PHI records publicly accessible "
            "for an estimated 14 days. The misconfiguration was introduced during "
            "a routine deployment update."
        ),
    },
}


def generate_inject_timeline(
    scenario_key: str,
    exercise_start_time: str,
) -> dict:
    """Generate a timed inject schedule for a simulation exercise."""
    scenario = SCENARIOS.get(scenario_key)
    if not scenario:
        return {"error": f"Unknown scenario: {scenario_key}"}

    start = datetime.fromisoformat(exercise_start_time)
    if start.tzinfo is None:
        start = start.replace(tzinfo=timezone.utc)

    inject_templates = {
        "ransomware_customer_db": [
            {"offset_min": 0, "title": "Opening Brief", "type": "brief", "description": "Exercise objectives, ground rules, scenario introduction", "decision_point": None},
            {"offset_min": 15, "title": "SOC Alert — Anomalous Encryption Activity", "type": "inject", "description": "CrowdStrike Falcon detects rapid file encryption on db-prod-eu-west-01. Over 500 file rename operations per second.", "decision_point": "Classify: potential breach or standard security incident?"},
            {"offset_min": 30, "title": "Breach Confirmed — Customer Data Encrypted", "type": "inject", "description": "Investigation confirms ransomware (LockBit 3.0). 48,720 customer records encrypted. Backup availability confirmed.", "decision_point": "Confirm personal data breach. Start 72-hour clock. Who to notify?"},
            {"offset_min": 50, "title": "Ransom Note Discovered", "type": "inject", "description": "Ransom note on encrypted systems demands 15 BTC within 72 hours. Threatens to publish data if not paid.", "decision_point": "Ransom payment decision. Law enforcement engagement?"},
            {"offset_min": 70, "title": "Initial Compromise Was 3 Days Ago", "type": "inject", "description": "Forensics reveals attacker presence since Monday. Multiple systems accessed including the DB admin jumpbox.", "decision_point": "Re-assess scope. Expand evidence preservation. Update risk assessment."},
            {"offset_min": 90, "title": "BREAK", "type": "break", "description": "15-minute break", "decision_point": None},
            {"offset_min": 105, "title": "Media Inquiry Received", "type": "inject", "description": "Technology journalist from Handelsblatt calls the press office asking about a cyberattack at Stellar Payments.", "decision_point": "Media response strategy. Who speaks? What is disclosed?"},
            {"offset_min": 120, "title": "Exfiltration Uncertain", "type": "inject", "description": "Mandiant forensic team reports: no evidence of exfiltration found, but 48-hour gap in network capture means exfiltration cannot be ruled out.", "decision_point": "Notification approach given uncertainty. Apply precautionary principle?"},
            {"offset_min": 140, "title": "72-Hour Deadline Falls on Holiday", "type": "inject", "description": "The 72-hour notification deadline is 14:30 UTC on Monday, which is a national holiday. SA portal availability uncertain.", "decision_point": "Submit before deadline? Identify backup notification channels."},
            {"offset_min": 160, "title": "SA Acknowledges and Requests Report", "type": "inject", "description": "Berliner BfDI acknowledges notification and requests detailed forensic report within 30 days.", "decision_point": "Commit to report timeline. Assign report preparation to investigation team."},
            {"offset_min": 180, "title": "Board Chair Calls for Briefing", "type": "inject", "description": "Board chair (dialed in from vacation) demands a full briefing within the hour.", "decision_point": "CEO prepares structured board briefing. What level of detail?"},
            {"offset_min": 195, "title": "Debrief and Hot Wash", "type": "debrief", "description": "Immediate debrief: what went well, what needs improvement", "decision_point": None},
            {"offset_min": 210, "title": "Exercise Concludes", "type": "end", "description": "Exercise end", "decision_point": None},
        ],
    }

    injects = inject_templates.get(scenario_key, inject_templates["ransomware_customer_db"])

    timeline = []
    for inject in injects:
        inject_time = start + timedelta(minutes=inject["offset_min"])
        timeline.append({
            "simulated_time": inject_time.strftime("%H:%M"),
            "offset_minutes": inject["offset_min"],
            "title": inject["title"],
            "type": inject["type"],
            "description": inject["description"],
            "decision_point": inject["decision_point"],
        })

    return {
        "scenario": scenario,
        "exercise_start": start.isoformat(),
        "exercise_end": (start + timedelta(hours=scenario["duration_hours"])).isoformat(),
        "total_injects": len([i for i in timeline if i["type"] == "inject"]),
        "timeline": timeline,
    }


def generate_evaluation_scorecard(participant_count: int) -> dict:
    """Generate an evaluation scorecard for exercise assessment."""
    categories = {
        "communication_effectiveness": {
            "weight": 25,
            "criteria": [
                "Right people notified at each stage",
                "Internal communication clear and timely",
                "Media response appropriate and pre-approved",
                "Data subject impact considered throughout",
            ],
        },
        "decision_quality": {
            "weight": 30,
            "criteria": [
                "Decisions were evidence-based",
                "GDPR notification thresholds correctly applied",
                "Precautionary principle applied under uncertainty",
                "Legal and regulatory obligations correctly identified",
            ],
        },
        "process_adherence": {
            "weight": 25,
            "criteria": [
                "Documented breach response procedure followed",
                "Escalation matrix and timelines followed",
                "Evidence preservation initiated before remediation",
                "Actions documented in incident management system",
            ],
        },
        "timeliness": {
            "weight": 20,
            "criteria": [
                "72-hour GDPR notification deadline would be met",
                "Escalation targets reached within required timeframes",
                "Risk assessment completed within expected timeline",
                "Media response prepared within 2 hours of inquiry",
            ],
        },
    }

    return {
        "exercise_evaluation_scorecard": {
            "participant_count": participant_count,
            "scoring_scale": "1 (Not Demonstrated) to 5 (Excellent)",
            "categories": categories,
            "total_weight": sum(c["weight"] for c in categories.values()),
            "pass_threshold": "Weighted average of 3.0 or above across all categories",
        },
    }


def main():
    print("=" * 70)
    print("BREACH SIMULATION EXERCISE — INJECT TIMELINE")
    print("=" * 70)

    timeline = generate_inject_timeline(
        scenario_key="ransomware_customer_db",
        exercise_start_time="2026-04-15T09:00:00+02:00",
    )
    print(json.dumps(timeline, indent=2))

    print("\n" + "=" * 70)
    print("EVALUATION SCORECARD")
    print("=" * 70)

    scorecard = generate_evaluation_scorecard(participant_count=12)
    print(json.dumps(scorecard, indent=2))

    print("\n" + "=" * 70)
    print("AVAILABLE SCENARIOS")
    print("=" * 70)

    for key, scenario in SCENARIOS.items():
        print(f"  {key}:")
        print(f"    Title: {scenario['title']}")
        print(f"    Difficulty: {scenario['difficulty']}")
        print(f"    Duration: {scenario['duration_hours']}h")
        print(f"    GDPR: {scenario['gdpr_relevant']} | HIPAA: {scenario['hipaa_relevant']}")
        print()


if __name__ == "__main__":
    main()
