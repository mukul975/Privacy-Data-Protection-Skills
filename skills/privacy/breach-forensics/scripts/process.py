#!/usr/bin/env python3
"""
Breach Investigation Forensics — Evidence Tracking and Timeline Reconstruction

Manages forensic evidence chain of custody, generates investigation timelines,
and maps attack techniques to the MITRE ATT&CK framework.
"""

import json
import hashlib
from datetime import datetime, timezone, timedelta
from enum import Enum
from typing import Optional


class EvidenceType(Enum):
    MEMORY_DUMP = "memory_dump"
    DISK_IMAGE = "disk_image"
    LOG_EXPORT = "log_export"
    NETWORK_CAPTURE = "network_capture"
    CLOUD_LOG = "cloud_log"
    MALWARE_SAMPLE = "malware_sample"


class EvidenceStatus(Enum):
    COLLECTED = "collected"
    IN_ANALYSIS = "in_analysis"
    ANALYZED = "analyzed"
    ARCHIVED = "archived"
    DISPOSED = "disposed"


MITRE_ATTACK_TECHNIQUES = {
    "T1566.001": {"name": "Spearphishing Attachment", "tactic": "Initial Access"},
    "T1566.002": {"name": "Spearphishing Link", "tactic": "Initial Access"},
    "T1078": {"name": "Valid Accounts", "tactic": "Persistence"},
    "T1078.001": {"name": "Default Accounts", "tactic": "Persistence"},
    "T1078.002": {"name": "Domain Accounts", "tactic": "Persistence"},
    "T1078.004": {"name": "Cloud Accounts", "tactic": "Persistence"},
    "T1021.001": {"name": "Remote Desktop Protocol", "tactic": "Lateral Movement"},
    "T1021.004": {"name": "SSH", "tactic": "Lateral Movement"},
    "T1021.006": {"name": "Windows Remote Management", "tactic": "Lateral Movement"},
    "T1003.001": {"name": "LSASS Memory", "tactic": "Credential Access"},
    "T1003.003": {"name": "NTDS", "tactic": "Credential Access"},
    "T1056.001": {"name": "Keylogging", "tactic": "Credential Access"},
    "T1486": {"name": "Data Encrypted for Impact", "tactic": "Impact"},
    "T1048.001": {"name": "Exfiltration Over Symmetric Encrypted Non-C2 Protocol", "tactic": "Exfiltration"},
    "T1048.002": {"name": "Exfiltration Over Asymmetric Encrypted Non-C2 Protocol", "tactic": "Exfiltration"},
    "T1071.001": {"name": "Web Protocols", "tactic": "Command and Control"},
    "T1059.001": {"name": "PowerShell", "tactic": "Execution"},
    "T1059.003": {"name": "Windows Command Shell", "tactic": "Execution"},
    "T1070.001": {"name": "Clear Windows Event Logs", "tactic": "Defense Evasion"},
    "T1070.004": {"name": "File Deletion", "tactic": "Defense Evasion"},
    "T1547.001": {"name": "Registry Run Keys", "tactic": "Persistence"},
}


class EvidenceItem:
    """Represents a single piece of forensic evidence."""

    def __init__(
        self,
        evidence_id: str,
        evidence_type: str,
        description: str,
        source_system: str,
        collected_by: str,
        collection_tool: str,
        file_path: str,
        file_size_bytes: int,
    ):
        self.evidence_id = evidence_id
        self.evidence_type = EvidenceType(evidence_type)
        self.description = description
        self.source_system = source_system
        self.collected_by = collected_by
        self.collection_tool = collection_tool
        self.collection_timestamp = datetime.now(timezone.utc)
        self.file_path = file_path
        self.file_size_bytes = file_size_bytes
        self.sha256_hash = self._generate_hash()
        self.status = EvidenceStatus.COLLECTED
        self.chain_of_custody = [
            {
                "action": "collected",
                "timestamp": self.collection_timestamp.isoformat(),
                "person": collected_by,
                "location": "Forensic workstation, Building A, Room 104",
                "hash_verified": True,
            }
        ]

    def _generate_hash(self) -> str:
        """Generate a simulated SHA-256 hash for the evidence file."""
        hash_input = f"{self.evidence_id}:{self.file_path}:{self.file_size_bytes}"
        return hashlib.sha256(hash_input.encode()).hexdigest()

    def transfer(self, released_by: str, received_by: str, purpose: str, location: str) -> None:
        """Record a chain of custody transfer."""
        self.chain_of_custody.append({
            "action": "transferred",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "released_by": released_by,
            "received_by": received_by,
            "purpose": purpose,
            "location": location,
            "hash_verified": True,
        })

    def to_dict(self) -> dict:
        return {
            "evidence_id": self.evidence_id,
            "type": self.evidence_type.value,
            "description": self.description,
            "source_system": self.source_system,
            "collected_by": self.collected_by,
            "collection_tool": self.collection_tool,
            "collection_timestamp": self.collection_timestamp.isoformat(),
            "file_path": self.file_path,
            "file_size_bytes": self.file_size_bytes,
            "file_size_human": f"{self.file_size_bytes / (1024**3):.2f} GB" if self.file_size_bytes > 1024**3 else f"{self.file_size_bytes / (1024**2):.1f} MB",
            "sha256_hash": self.sha256_hash,
            "status": self.status.value,
            "chain_of_custody": self.chain_of_custody,
        }


class InvestigationTimeline:
    """Reconstructs and manages the breach investigation timeline."""

    def __init__(self, breach_reference: str):
        self.breach_reference = breach_reference
        self.events = []

    def add_event(
        self,
        timestamp: str,
        event_type: str,
        description: str,
        source_system: str,
        evidence_reference: str,
        mitre_technique: Optional[str] = None,
        personal_data_impact: bool = False,
    ) -> None:
        event = {
            "timestamp": timestamp,
            "event_type": event_type,
            "description": description,
            "source_system": source_system,
            "evidence_reference": evidence_reference,
            "personal_data_impact": personal_data_impact,
        }
        if mitre_technique and mitre_technique in MITRE_ATTACK_TECHNIQUES:
            technique = MITRE_ATTACK_TECHNIQUES[mitre_technique]
            event["mitre_attack"] = {
                "technique_id": mitre_technique,
                "technique_name": technique["name"],
                "tactic": technique["tactic"],
            }
        self.events.append(event)
        self.events.sort(key=lambda e: e["timestamp"])

    def get_timeline(self) -> dict:
        earliest = self.events[0]["timestamp"] if self.events else None
        latest = self.events[-1]["timestamp"] if self.events else None

        if earliest and latest:
            start = datetime.fromisoformat(earliest)
            end = datetime.fromisoformat(latest)
            dwell_time = end - start
            dwell_hours = dwell_time.total_seconds() / 3600
        else:
            dwell_hours = 0

        techniques_used = []
        for event in self.events:
            if "mitre_attack" in event:
                tech = event["mitre_attack"]
                if tech["technique_id"] not in [t["technique_id"] for t in techniques_used]:
                    techniques_used.append(tech)

        data_impact_events = [e for e in self.events if e["personal_data_impact"]]

        return {
            "breach_reference": self.breach_reference,
            "timeline_summary": {
                "earliest_event": earliest,
                "latest_event": latest,
                "total_events": len(self.events),
                "dwell_time_hours": round(dwell_hours, 1),
                "personal_data_impact_events": len(data_impact_events),
            },
            "mitre_attack_techniques": techniques_used,
            "events": self.events,
        }


def generate_scope_assessment(
    compromised_systems: list,
    data_impact: dict,
    exfiltration_status: str,
) -> dict:
    """
    Generate a scope assessment summarizing what personal data was affected.

    Args:
        compromised_systems: List of dicts with system details.
        data_impact: Dict mapping data categories to affected counts.
        exfiltration_status: One of 'confirmed', 'not_confirmed', 'cannot_be_ruled_out'.

    Returns:
        Scope assessment report.
    """
    total_subjects = sum(
        sys.get("data_subject_count", 0) for sys in compromised_systems
    )

    personal_data_systems = [
        sys for sys in compromised_systems if sys.get("contains_personal_data", False)
    ]

    return {
        "scope_assessment": {
            "total_compromised_systems": len(compromised_systems),
            "systems_containing_personal_data": len(personal_data_systems),
            "total_data_subjects_affected": total_subjects,
            "data_categories_compromised": data_impact,
            "exfiltration_determination": exfiltration_status,
            "confidence_level": "medium" if exfiltration_status == "cannot_be_ruled_out" else "high",
        },
        "compromised_systems": compromised_systems,
        "recommendation": (
            "Based on the scope assessment, Art. 33 supervisory authority notification is "
            f"required. {'Art. 34 data subject notification is also required due to confirmed exfiltration.' if exfiltration_status == 'confirmed' else 'Art. 34 notification should be assessed based on the risk scoring methodology.'}"
        ),
    }


def main():
    print("=" * 70)
    print("FORENSIC EVIDENCE INVENTORY")
    print("=" * 70)

    evidence_items = [
        EvidenceItem(
            evidence_id="SPG-BREACH-2026-003-EV-001",
            evidence_type="memory_dump",
            description="Full RAM dump of db-prod-eu-west-01 (PostgreSQL primary server, 128 GB RAM)",
            source_system="db-prod-eu-west-01",
            collected_by="Thomas Brenner (CISO)",
            collection_tool="WinPmem 4.0",
            file_path="/forensic/spg-2026-003/ev-001-db01-memory.raw",
            file_size_bytes=137438953472,
        ),
        EvidenceItem(
            evidence_id="SPG-BREACH-2026-003-EV-002",
            evidence_type="disk_image",
            description="Forensic disk image of db-prod-eu-west-01 system volume (2 TB NVMe)",
            source_system="db-prod-eu-west-01",
            collected_by="Sarah Mitchell (Mandiant)",
            collection_tool="FTK Imager 4.7",
            file_path="/forensic/spg-2026-003/ev-002-db01-disk.e01",
            file_size_bytes=2199023255552,
        ),
        EvidenceItem(
            evidence_id="SPG-BREACH-2026-003-EV-003",
            evidence_type="log_export",
            description="Splunk export: all authentication and database audit events, 10 Feb - 14 Mar 2026",
            source_system="Splunk Enterprise Security",
            collected_by="SOC Lead (Marcus Weber)",
            collection_tool="Splunk CLI export (splunk search)",
            file_path="/forensic/spg-2026-003/ev-003-splunk-export.json",
            file_size_bytes=47244640256,
        ),
        EvidenceItem(
            evidence_id="SPG-BREACH-2026-003-EV-004",
            evidence_type="network_capture",
            description="Full packet capture from network tap on db-prod VLAN, 12-14 Mar 2026",
            source_system="Network TAP (db-prod VLAN)",
            collected_by="Network Security (Petra Hoffmann)",
            collection_tool="tcpdump via dedicated capture server",
            file_path="/forensic/spg-2026-003/ev-004-pcap-dbvlan.pcapng",
            file_size_bytes=85899345920,
        ),
    ]

    evidence_items[1].transfer(
        released_by="Thomas Brenner (CISO)",
        received_by="Sarah Mitchell (Mandiant)",
        purpose="Forensic disk analysis",
        location="Mandiant Berlin Office, Potsdamer Platz 10",
    )

    for item in evidence_items:
        print(json.dumps(item.to_dict(), indent=2))
        print()

    print("=" * 70)
    print("INVESTIGATION TIMELINE — SPG-BREACH-2026-003")
    print("=" * 70)

    timeline = InvestigationTimeline("SPG-BREACH-2026-003")

    timeline.add_event(
        timestamp="2026-03-10T09:23:00+00:00",
        event_type="initial_access",
        description="Spear-phishing email received by IT operations engineer j.richter@stellarpayments.eu from spoofed sender support@stellarpayrnents.eu (note: 'rn' instead of 'm'). Email contained link to credential harvesting page.",
        source_system="Microsoft 365 Unified Audit Log",
        evidence_reference="SPG-BREACH-2026-003-EV-003",
        mitre_technique="T1566.002",
    )

    timeline.add_event(
        timestamp="2026-03-10T09:24:15+00:00",
        event_type="credential_harvest",
        description="Engineer clicked phishing link and entered credentials on fake Okta login page. Keylogger payload also downloaded to workstation.",
        source_system="CrowdStrike Falcon (retroactive analysis)",
        evidence_reference="SPG-BREACH-2026-003-EV-001",
        mitre_technique="T1056.001",
    )

    timeline.add_event(
        timestamp="2026-03-10T14:07:00+00:00",
        event_type="valid_account_use",
        description="Attacker authenticated to Okta using harvested credentials from IP 185.220.101.45 (Tor exit node). MFA bypassed using push fatigue (repeated MFA prompts until engineer accepted).",
        source_system="Okta System Log",
        evidence_reference="SPG-BREACH-2026-003-EV-003",
        mitre_technique="T1078.002",
    )

    timeline.add_event(
        timestamp="2026-03-11T02:15:00+00:00",
        event_type="lateral_movement",
        description="Attacker used compromised credentials to SSH into db-admin-jumpbox from the engineer's VPN session. From jumpbox, pivoted to db-prod-eu-west-01 using stale service account svc-migration-2024.",
        source_system="SSH authentication logs + Okta",
        evidence_reference="SPG-BREACH-2026-003-EV-003",
        mitre_technique="T1021.004",
    )

    timeline.add_event(
        timestamp="2026-03-13T11:15:00+00:00",
        event_type="impact",
        description="LockBit 3.0 ransomware deployed on db-prod-eu-west-01 through db-prod-eu-west-04. Rapid encryption of PostgreSQL data files (48,720 records across customers, transactions, accounts tables).",
        source_system="CrowdStrike Falcon",
        evidence_reference="SPG-BREACH-2026-003-EV-001",
        mitre_technique="T1486",
        personal_data_impact=True,
    )

    timeline.add_event(
        timestamp="2026-03-13T12:45:00+00:00",
        event_type="containment",
        description="SOC team isolated db-prod cluster from network. All connections severed. Forensic preservation initiated.",
        source_system="Palo Alto Firewall + Manual action",
        evidence_reference="SPG-BREACH-2026-003-EV-003",
    )

    timeline.add_event(
        timestamp="2026-03-13T14:30:00+00:00",
        event_type="awareness",
        description="Controller (Stellar Payments Group) officially became aware of the personal data breach. 72-hour Art. 33 notification clock activated.",
        source_system="Incident management system (ServiceNow)",
        evidence_reference="SPG-BREACH-2026-003-EV-003",
    )

    print(json.dumps(timeline.get_timeline(), indent=2))

    print("\n" + "=" * 70)
    print("SCOPE ASSESSMENT")
    print("=" * 70)

    scope = generate_scope_assessment(
        compromised_systems=[
            {
                "hostname": "db-prod-eu-west-01",
                "function": "PostgreSQL primary — customer database",
                "contains_personal_data": True,
                "data_subject_count": 15230,
                "data_categories": ["names", "addresses", "emails", "payment card last-4", "transactions", "balances"],
            },
            {
                "hostname": "db-prod-eu-west-02",
                "function": "PostgreSQL replica — customer database (read replica)",
                "contains_personal_data": True,
                "data_subject_count": 15230,
                "data_categories": ["names", "addresses", "emails", "payment card last-4", "transactions", "balances"],
            },
            {
                "hostname": "db-admin-jumpbox",
                "function": "SSH jump server for database administration",
                "contains_personal_data": False,
                "data_subject_count": 0,
                "data_categories": [],
            },
            {
                "hostname": "ws-jrichter-01",
                "function": "IT operations engineer workstation",
                "contains_personal_data": False,
                "data_subject_count": 0,
                "data_categories": [],
            },
        ],
        data_impact={
            "full_names": 15230,
            "postal_addresses": 15230,
            "email_addresses": 14870,
            "payment_card_last_4": 12650,
            "transaction_histories": 48720,
            "account_balances": 15230,
        },
        exfiltration_status="cannot_be_ruled_out",
    )

    print(json.dumps(scope, indent=2))


if __name__ == "__main__":
    main()
