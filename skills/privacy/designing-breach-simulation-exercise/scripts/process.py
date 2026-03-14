#!/usr/bin/env python3
"""
Breach Simulation Exercise Generator

Generates structured tabletop exercise scenarios with inject timelines,
participant assignments, decision points, and after-action report templates.
"""

import json
from datetime import datetime, timezone, timedelta
from typing import Optional


SCENARIO_TEMPLATES = {
    "ransomware": {
        "title": "Ransomware Attack on Production Database",
        "complexity": "high",
        "duration_hours": 3,
        "participants_min": 8,
        "participants_max": 15,
        "objectives": [
            "Test Art. 33 72-hour notification decision-making",
            "Validate executive escalation procedures",
            "Assess media and stakeholder communication readiness",
            "Evaluate backup restoration and service recovery coordination",
        ],
    },
    "insider_threat": {
        "title": "Employee Data Exfiltration by Departing Staff",
        "complexity": "medium",
        "duration_hours": 2.5,
        "participants_min": 8,
        "participants_max": 12,
        "objectives": [
            "Test HR-legal-privacy coordination for insider incidents",
            "Assess Works Council consultation procedures",
            "Evaluate evidence preservation vs. confrontation timing",
            "Validate employee notification communication approach",
        ],
    },
    "processor_breach": {
        "title": "Third-Party Processor Data Breach",
        "complexity": "medium",
        "duration_hours": 2,
        "participants_min": 6,
        "participants_max": 10,
        "objectives": [
            "Test processor notification obligations under Art. 28/33(2)",
            "Assess controller awareness determination when processor delays",
            "Evaluate vendor management and contract enforcement",
            "Validate parallel investigation capabilities",
        ],
    },
    "phishing_credential": {
        "title": "Mass Credential Compromise via Phishing Campaign",
        "complexity": "medium",
        "duration_hours": 2.5,
        "participants_min": 8,
        "participants_max": 12,
        "objectives": [
            "Test mass password reset and account recovery procedures",
            "Evaluate customer communication at scale",
            "Assess credential monitoring and dark web surveillance response",
            "Validate multi-channel notification execution",
        ],
    },
}

STANDARD_PARTICIPANTS = [
    {"role": "Incident Commander", "function": "IT Security", "name": "Thomas Brenner", "title": "CISO"},
    {"role": "Privacy Lead", "function": "Data Protection", "name": "Dr. Elena Vasquez", "title": "DPO"},
    {"role": "Legal Counsel", "function": "Legal", "name": "Sarah Chen", "title": "General Counsel"},
    {"role": "Communications Lead", "function": "Communications", "name": "Martin Keller", "title": "Communications Director"},
    {"role": "IT Operations", "function": "IT", "name": "Petra Hoffmann", "title": "IT Director"},
    {"role": "Executive Sponsor", "function": "Executive", "name": "Marcus Lindqvist", "title": "CEO"},
    {"role": "Customer Relations", "function": "Customer Success", "name": "James Park", "title": "VP Customer Success"},
    {"role": "HR Lead", "function": "Human Resources", "name": "Claudia Richter", "title": "CHRO"},
]


def generate_exercise(
    scenario_type: str,
    exercise_date: str,
    custom_injects: Optional[list] = None,
) -> dict:
    """
    Generate a complete breach simulation exercise plan.

    Args:
        scenario_type: One of 'ransomware', 'insider_threat', 'processor_breach', 'phishing_credential'.
        exercise_date: ISO date for the exercise.
        custom_injects: Optional list of custom inject descriptions.

    Returns:
        Complete exercise plan with scenario, injects, participants, and evaluation criteria.
    """
    template = SCENARIO_TEMPLATES.get(scenario_type)
    if not template:
        raise ValueError(f"Unknown scenario type: {scenario_type}. Available: {list(SCENARIO_TEMPLATES.keys())}")

    default_injects = {
        "ransomware": [
            {"time_offset_min": 0, "inject": "SOC alert: CrowdStrike detects rapid file encryption on db-prod-eu-west-01. 500+ file operations per second. LockBit 3.0 indicators.", "decision_point": "Initiate incident response. Activate Incident Commander."},
            {"time_offset_min": 15, "inject": "Encryption spreading to db-prod-eu-west-02 and 03. Customer portal returning errors. 12 customer complaints received.", "decision_point": "Network isolation decision. Service disruption acceptance."},
            {"time_offset_min": 30, "inject": "Forensic finding: compromised service account (svc-migration-2024) authenticated from Tor exit node 3 days prior.", "decision_point": "Scope assessment. Additional credential revocation needed?"},
            {"time_offset_min": 60, "inject": "Database confirmed encrypted: 48,720 records, 15,230 data subjects. Clean backup available from 12 hours ago.", "decision_point": "Art. 33 clock determination. Backup restoration authorization."},
            {"time_offset_min": 90, "inject": "Ransom note: 50 BTC. Threat to publish data within 48 hours. Handelsblatt reporter calls for comment.", "decision_point": "Ransom payment policy. Law enforcement engagement. Media response."},
            {"time_offset_min": 120, "inject": "Mandiant: no exfiltration evidence but cannot rule out. Restoration 60% complete. SA office opens in 2 hours.", "decision_point": "Art. 33 notification: submit now or wait? Art. 34 preparation."},
            {"time_offset_min": 150, "inject": "Bloomberg publishes story. Social media trending. 50+ customer calls. Three enterprise clients demand assurance.", "decision_point": "Crisis communication execution. B2B stakeholder management."},
        ],
        "insider_threat": [
            {"time_offset_min": 0, "inject": "DLP alert: HR database export (3,400 records) copied to personal OneDrive by employee on notice period.", "decision_point": "Alert validation. Personal data involvement determination."},
            {"time_offset_min": 20, "inject": "Records include names, addresses, salaries, bank details, national IDs. Employee's last day is Friday.", "decision_point": "Preservation vs. confrontation. Legal/HR involvement."},
            {"time_offset_min": 45, "inject": "File synced to personal laptop. Employee is currently in the office.", "decision_point": "Device seizure considerations. Works Council notification."},
            {"time_offset_min": 75, "inject": "Works Council representative requests consultation before any employee confrontation.", "decision_point": "Balance urgency with labor law obligations."},
            {"time_offset_min": 105, "inject": "Employee interviewed, claims 'reference purposes', refuses laptop access.", "decision_point": "Law enforcement referral. Court order for device. Art. 33 assessment."},
            {"time_offset_min": 135, "inject": "Risk assessment: 3,400 employees, government IDs + financial data = high risk.", "decision_point": "Art. 33/34 notification. Employee breach communication."},
        ],
        "processor_breach": [
            {"time_offset_min": 0, "inject": "Email from PayrollCloud GmbH: security incident affecting customer data. No details.", "decision_point": "Contact processor. Review Art. 28 DPA notification clauses."},
            {"time_offset_min": 20, "inject": "Processor: SQL injection. Unclear which clients affected. Impact assessment in 5-7 days.", "decision_point": "72-hour clock assessment. Can we wait for processor details?"},
            {"time_offset_min": 45, "inject": "Processor: 'Your data was on the affected server but access not confirmed.' 3,400 employee records potentially exposed.", "decision_point": "Controller awareness determination. Parallel risk assessment."},
            {"time_offset_min": 75, "inject": "Media reports the processor breach. Other clients acknowledging impact publicly.", "decision_point": "Proactive disclosure vs. wait for confirmation."},
            {"time_offset_min": 105, "inject": "Processor confirms: Stellar data accessed. 3,400 employees — names, salaries, bank accounts, tax IDs.", "decision_point": "Art. 33 notification. Processor accountability. Employee communication."},
        ],
        "phishing_credential": [
            {"time_offset_min": 0, "inject": "Security team detects sophisticated phishing campaign targeting customer accounts. 8,200 credential pairs harvested via fake login page.", "decision_point": "Incident response initiation. Phishing page takedown."},
            {"time_offset_min": 20, "inject": "Credential testing detected: 2,100 accounts show successful unauthorized login from foreign IPs.", "decision_point": "Mass account lockout decision. Customer impact assessment."},
            {"time_offset_min": 45, "inject": "Unauthorized logins accessed account dashboards showing names, addresses, transaction history, and partial payment data.", "decision_point": "Data exposure scope determination. Art. 33 assessment."},
            {"time_offset_min": 75, "inject": "Dark web forum post offering 'Stellar Payments credential dump' for sale.", "decision_point": "Law enforcement notification. Dark web monitoring escalation."},
            {"time_offset_min": 105, "inject": "Customer reports unauthorized transaction on linked bank account. First confirmed financial fraud.", "decision_point": "Art. 34 high risk confirmation. Credit monitoring activation."},
            {"time_offset_min": 135, "inject": "News coverage begins. Customer support overwhelmed with 200+ calls per hour.", "decision_point": "Crisis communication. Support scaling. Substitute notice consideration."},
        ],
    }

    injects = custom_injects or default_injects.get(scenario_type, [])

    decision_points = [
        {
            "id": i + 1,
            "time_offset_min": inject["time_offset_min"],
            "decision_required": inject["decision_point"],
            "evaluation_criteria": "Was the decision made promptly, correctly, and with appropriate consultation?",
        }
        for i, inject in enumerate(injects)
    ]

    return {
        "exercise_metadata": {
            "title": template["title"],
            "date": exercise_date,
            "scenario_type": scenario_type,
            "complexity": template["complexity"],
            "duration_hours": template["duration_hours"],
            "generated_at": datetime.now(timezone.utc).isoformat(),
        },
        "objectives": template["objectives"],
        "participants": STANDARD_PARTICIPANTS[:template["participants_max"]],
        "schedule": {
            "opening_briefing": "15 minutes",
            "scenario_execution": f"{template['duration_hours'] - 0.75} hours",
            "debrief_discussion": "30-45 minutes",
        },
        "injects": injects,
        "decision_points": decision_points,
        "evaluation_framework": {
            "categories": [
                "Detection and initial response",
                "Escalation and communication",
                "Risk assessment and notification decision",
                "Stakeholder management",
                "Documentation and accountability",
            ],
            "scoring": {
                "1_inadequate": "Critical gap — response would likely result in regulatory non-compliance",
                "2_needs_improvement": "Significant delays or errors — response would be suboptimal",
                "3_adequate": "Acceptable response — meets minimum requirements with some room for improvement",
                "4_effective": "Strong response — well-coordinated and timely",
                "5_exemplary": "Best-practice response — proactive, well-documented, and efficiently executed",
            },
        },
        "after_action_report_template": {
            "sections": [
                "Exercise summary and objectives assessment",
                "Timeline analysis (actual vs. expected)",
                "Findings (Critical / Major / Minor / Observation)",
                "Recommendations with owners and deadlines",
                "Metrics (detection time, escalation time, decision quality)",
            ],
        },
    }


def main():
    print("=" * 70)
    print("BREACH SIMULATION EXERCISE PLAN — RANSOMWARE SCENARIO")
    print("=" * 70)

    exercise = generate_exercise(
        scenario_type="ransomware",
        exercise_date="2026-04-15",
    )
    print(json.dumps(exercise, indent=2))

    print("\n" + "=" * 70)
    print("AVAILABLE SCENARIO TYPES")
    print("=" * 70)
    for key, template in SCENARIO_TEMPLATES.items():
        print(f"\n{key}:")
        print(f"  Title: {template['title']}")
        print(f"  Complexity: {template['complexity']}")
        print(f"  Duration: {template['duration_hours']} hours")
        print(f"  Participants: {template['participants_min']}-{template['participants_max']}")


if __name__ == "__main__":
    main()
