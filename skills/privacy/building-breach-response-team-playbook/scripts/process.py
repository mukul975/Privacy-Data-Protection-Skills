#!/usr/bin/env python3
"""
Breach Response Team Playbook Generator

Generates playbook components including team rosters, escalation matrices,
communication templates, and regulatory contact directories.
"""

import json
from datetime import datetime, timezone
from enum import Enum


class Severity(Enum):
    SEV1_CRITICAL = "SEV-1"
    SEV2_HIGH = "SEV-2"
    SEV3_MEDIUM = "SEV-3"
    SEV4_LOW = "SEV-4"


CORE_TEAM = [
    {
        "role": "Incident Commander",
        "primary": {"name": "Thomas Brenner", "title": "CISO", "phone": "+49 30 7742 8100", "email": "ic@stellarpayments.eu"},
        "backup": {"name": "Marcus Weber", "title": "SOC Lead", "phone": "+49 30 7742 8101", "email": "soc-lead@stellarpayments.eu"},
        "activation_severity": ["SEV-1", "SEV-2", "SEV-3"],
    },
    {
        "role": "Data Protection Officer",
        "primary": {"name": "Dr. Elena Vasquez", "title": "DPO", "phone": "+49 30 7742 8001", "email": "dpo@stellarpayments.eu"},
        "backup": {"name": "Anna Schmidt", "title": "Deputy DPO", "phone": "+49 30 7742 8002", "email": "deputy-dpo@stellarpayments.eu"},
        "activation_severity": ["SEV-1", "SEV-2", "SEV-3", "SEV-4"],
    },
    {
        "role": "Legal Counsel",
        "primary": {"name": "Sarah Chen", "title": "General Counsel", "phone": "+49 30 7742 8200", "email": "legal@stellarpayments.eu"},
        "backup": {"name": "Dr. Klaus Fischer", "title": "Partner, Freshfields", "phone": "+49 30 2028 39000", "email": "kfischer@freshfields.com"},
        "activation_severity": ["SEV-1", "SEV-2"],
    },
    {
        "role": "IT Forensics Lead",
        "primary": {"name": "Petra Hoffmann", "title": "IT Director", "phone": "+49 30 7742 8300", "email": "it-forensics@stellarpayments.eu"},
        "backup": {"name": "Sarah Mitchell", "title": "Mandiant IR Lead", "phone": "+1 703 935 1700", "email": "smitchell@mandiant.com"},
        "activation_severity": ["SEV-1", "SEV-2", "SEV-3"],
    },
    {
        "role": "Communications Lead",
        "primary": {"name": "Martin Keller", "title": "Communications Director", "phone": "+49 30 7742 8400", "email": "comms@stellarpayments.eu"},
        "backup": {"name": "Lisa Braun", "title": "Senior Comms Manager", "phone": "+49 30 7742 8401", "email": "l.braun@stellarpayments.eu"},
        "activation_severity": ["SEV-1", "SEV-2"],
    },
    {
        "role": "Executive Sponsor",
        "primary": {"name": "Marcus Lindqvist", "title": "CEO", "phone": "+49 30 7742 8000", "email": "ceo@stellarpayments.eu"},
        "backup": {"name": "Dr. Andrea Hoffmann", "title": "CFO", "phone": "+49 30 7742 8010", "email": "cfo@stellarpayments.eu"},
        "activation_severity": ["SEV-1"],
    },
    {
        "role": "Customer Relations",
        "primary": {"name": "James Park", "title": "VP Customer Success", "phone": "+49 30 7742 5000", "email": "customers@stellarpayments.eu"},
        "backup": {"name": "Maria Santos", "title": "CS Director", "phone": "+49 30 7742 5001", "email": "m.santos@stellarpayments.eu"},
        "activation_severity": ["SEV-1", "SEV-2"],
    },
    {
        "role": "HR Lead",
        "primary": {"name": "Claudia Richter", "title": "CHRO", "phone": "+49 30 7742 7500", "email": "hr-confidential@stellarpayments.eu"},
        "backup": {"name": "Stefan Müller", "title": "HR Director", "phone": "+49 30 7742 7501", "email": "s.mueller@stellarpayments.eu"},
        "activation_severity": ["SEV-1", "SEV-2"],
    },
]

SEVERITY_CRITERIA = {
    "SEV-1": {
        "label": "Critical",
        "criteria": [
            "10,000+ data subjects affected",
            "Special category data (Art. 9) compromised",
            "Active/ongoing data exfiltration",
            "Ransomware with encryption of production systems",
            "Breach involving imminent physical harm risk",
        ],
        "response_time_minutes": 15,
        "required_roles": ["Incident Commander", "Data Protection Officer", "Executive Sponsor", "Legal Counsel", "IT Forensics Lead", "Communications Lead"],
    },
    "SEV-2": {
        "label": "High",
        "criteria": [
            "1,000-10,000 data subjects affected",
            "Financial data or authentication credentials compromised",
            "Media coverage of the breach",
            "Breach at a critical processor",
        ],
        "response_time_minutes": 30,
        "required_roles": ["Incident Commander", "Data Protection Officer", "Legal Counsel", "IT Forensics Lead"],
    },
    "SEV-3": {
        "label": "Medium",
        "criteria": [
            "100-1,000 data subjects affected",
            "Non-sensitive personal data compromised",
            "Breach is fully contained",
        ],
        "response_time_minutes": 120,
        "required_roles": ["Incident Commander", "Data Protection Officer"],
    },
    "SEV-4": {
        "label": "Low",
        "criteria": [
            "Under 100 data subjects affected",
            "Low-sensitivity data only",
            "Breach contained with no evidence of exfiltration",
        ],
        "response_time_minutes": 240,
        "required_roles": ["Data Protection Officer"],
    },
}


def generate_activation_roster(severity: str) -> dict:
    """Generate the activation roster for a given severity level."""
    criteria = SEVERITY_CRITERIA.get(severity)
    if not criteria:
        raise ValueError(f"Unknown severity: {severity}")

    activated_team = [
        member for member in CORE_TEAM
        if severity in member["activation_severity"]
    ]

    return {
        "severity": severity,
        "label": criteria["label"],
        "response_time_minutes": criteria["response_time_minutes"],
        "activation_criteria": criteria["criteria"],
        "activated_roles": [
            {
                "role": member["role"],
                "primary": member["primary"],
                "backup": member["backup"],
            }
            for member in activated_team
        ],
        "total_team_size": len(activated_team),
    }


def generate_playbook_summary() -> dict:
    """Generate a complete playbook summary for distribution."""
    return {
        "playbook_metadata": {
            "organization": "Stellar Payments Group GmbH",
            "version": "3.1",
            "last_updated": "2026-03-01",
            "next_review": "2026-09-01",
            "approved_by": "Marcus Lindqvist (CEO), Board Audit Committee",
            "classification": "CONFIDENTIAL — Restricted to Core Response Team",
        },
        "team_roster": {
            "core_team_size": len(CORE_TEAM),
            "roles": [{"role": m["role"], "primary": m["primary"]["name"], "backup": m["backup"]["name"]} for m in CORE_TEAM],
        },
        "severity_levels": {
            sev: {
                "label": info["label"],
                "response_time_minutes": info["response_time_minutes"],
                "criteria_count": len(info["criteria"]),
                "required_roles": info["required_roles"],
            }
            for sev, info in SEVERITY_CRITERIA.items()
        },
        "communication_templates": [
            "Internal breach alert (Core Response Team)",
            "Media holding statement",
            "Customer service talking points",
            "Board notification",
            "Employee all-staff communication",
        ],
        "pre_negotiated_vendors": [
            {"service": "Incident Response", "vendor": "Mandiant", "retainer": "SPG-IR-2025-007"},
            {"service": "External Legal (EU)", "vendor": "Freshfields", "retainer": "SPG-LEG-2025-012"},
            {"service": "External Legal (US)", "vendor": "Covington & Burling", "retainer": "SPG-LEG-2025-013"},
            {"service": "Credit Monitoring", "vendor": "Experian IdentityWorks", "retainer": "SPG-EXP-2025-003"},
            {"service": "Crisis Communications", "vendor": "Brunswick Group", "retainer": "SPG-COM-2025-001"},
            {"service": "Cyber Insurance", "vendor": "Allianz", "retainer": "SPG-CYB-2025-001"},
        ],
        "regulatory_contacts": {
            "eu_lead_sa": "Berliner BfDI — datenschutz-berlin.de — +49 30 13889 0",
            "uk": "ICO — ico.org.uk — +44 303 123 1113",
            "us_hhs": "HHS/OCR — ocrportal.hhs.gov — +1 800 368 1019",
            "us_ca_ag": "California AG — oag.ca.gov — +1 916 210 6276",
        },
        "maintenance_schedule": {
            "contact_verification": "Quarterly",
            "tabletop_exercise": "Semi-annually",
            "full_revision": "Annually",
            "post_incident_revision": "After every SEV-1 or SEV-2 incident",
        },
    }


def main():
    print("=" * 70)
    print("BREACH RESPONSE PLAYBOOK SUMMARY")
    print("=" * 70)
    summary = generate_playbook_summary()
    print(json.dumps(summary, indent=2))

    print("\n" + "=" * 70)
    print("SEV-1 ACTIVATION ROSTER")
    print("=" * 70)
    sev1 = generate_activation_roster("SEV-1")
    print(json.dumps(sev1, indent=2))

    print("\n" + "=" * 70)
    print("SEV-3 ACTIVATION ROSTER")
    print("=" * 70)
    sev3 = generate_activation_roster("SEV-3")
    print(json.dumps(sev3, indent=2))


if __name__ == "__main__":
    main()
