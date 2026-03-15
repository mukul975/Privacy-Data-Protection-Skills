"""
NIST Privacy Framework PROTECT Function — Security Controls Assessor

Evaluates data protection controls across PR.AC (Access Control),
PR.DS (Data Security), and PR.PO (Protective Policies).
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import json


class ControlStatus(Enum):
    NOT_IMPLEMENTED = "not_implemented"
    PARTIALLY_IMPLEMENTED = "partially_implemented"
    FULLY_IMPLEMENTED = "fully_implemented"
    NOT_APPLICABLE = "not_applicable"


class RiskRating(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class SecurityControl:
    subcategory: str
    control_name: str
    status: ControlStatus
    evidence: str
    risk_if_missing: RiskRating
    remediation: str = ""
    deadline: str = ""
    owner: str = ""


@dataclass
class EncryptionInventory:
    system_name: str
    data_at_rest: str  # AES-128, AES-256, None
    data_in_transit: str  # TLS 1.2, TLS 1.3, None
    key_management: str  # HSM, Software, None
    key_rotation: str  # Annual, Quarterly, None
    compliant: bool = False

    def __post_init__(self):
        self.compliant = (
            self.data_at_rest in ("AES-256", "AES-128")
            and self.data_in_transit in ("TLS 1.3", "TLS 1.2")
            and self.key_management in ("HSM", "Software")
        )


class ProtectFunctionAssessor:
    """
    Assess NIST PF PROTECT function control implementation.
    """

    def __init__(self, organization: str):
        self.organization = organization
        self.controls: list[SecurityControl] = []
        self.encryption_inventory: list[EncryptionInventory] = []

    def assess_access_controls(self, findings: list[dict]) -> list[SecurityControl]:
        """Assess PR.AC subcategories from audit findings."""
        controls = []

        ac_mappings = {
            "PR.AC-P1": ("Identity and credential management", RiskRating.HIGH),
            "PR.AC-P2": ("Physical access management", RiskRating.MEDIUM),
            "PR.AC-P3": ("Remote access management", RiskRating.HIGH),
            "PR.AC-P4": ("Least privilege and separation of duties", RiskRating.CRITICAL),
            "PR.AC-P5": ("Network integrity", RiskRating.HIGH),
            "PR.AC-P6": ("Identity proofing and binding", RiskRating.MEDIUM),
        }

        for subcategory, (name, risk) in ac_mappings.items():
            finding = next((f for f in findings if f.get("subcategory") == subcategory), None)
            if finding:
                controls.append(SecurityControl(
                    subcategory=subcategory,
                    control_name=name,
                    status=ControlStatus(finding["status"]),
                    evidence=finding.get("evidence", ""),
                    risk_if_missing=risk,
                    remediation=finding.get("remediation", ""),
                    owner=finding.get("owner", ""),
                ))
            else:
                controls.append(SecurityControl(
                    subcategory=subcategory,
                    control_name=name,
                    status=ControlStatus.NOT_IMPLEMENTED,
                    evidence="Not assessed",
                    risk_if_missing=risk,
                ))

        self.controls.extend(controls)
        return controls

    def assess_encryption(
        self, inventory: list[EncryptionInventory]
    ) -> dict:
        """Assess PR.DS-P1 and PR.DS-P2 encryption compliance."""
        self.encryption_inventory = inventory

        total = len(inventory)
        compliant = sum(1 for e in inventory if e.compliant)
        non_compliant = [e for e in inventory if not e.compliant]

        return {
            "total_systems": total,
            "compliant_systems": compliant,
            "compliance_rate": f"{compliant / total * 100:.1f}%" if total > 0 else "N/A",
            "non_compliant_systems": [
                {
                    "system": e.system_name,
                    "at_rest": e.data_at_rest,
                    "in_transit": e.data_in_transit,
                    "key_mgmt": e.key_management,
                    "issues": self._identify_encryption_issues(e),
                }
                for e in non_compliant
            ],
        }

    def _identify_encryption_issues(self, entry: EncryptionInventory) -> list[str]:
        """Identify specific encryption gaps."""
        issues = []
        if entry.data_at_rest == "None":
            issues.append("No encryption at rest")
        if entry.data_in_transit == "None":
            issues.append("No encryption in transit")
        elif entry.data_in_transit == "TLS 1.0" or entry.data_in_transit == "TLS 1.1":
            issues.append(f"Deprecated TLS version: {entry.data_in_transit}")
        if entry.key_management == "None":
            issues.append("No key management system")
        if entry.key_rotation == "None":
            issues.append("No key rotation policy")
        return issues

    def generate_protect_report(self) -> dict:
        """Generate PROTECT function assessment report."""
        total = len(self.controls)
        implemented = sum(1 for c in self.controls if c.status == ControlStatus.FULLY_IMPLEMENTED)
        partial = sum(1 for c in self.controls if c.status == ControlStatus.PARTIALLY_IMPLEMENTED)
        missing = sum(1 for c in self.controls if c.status == ControlStatus.NOT_IMPLEMENTED)

        critical_gaps = [
            c for c in self.controls
            if c.status != ControlStatus.FULLY_IMPLEMENTED
            and c.risk_if_missing in (RiskRating.CRITICAL, RiskRating.HIGH)
        ]

        return {
            "organization": self.organization,
            "date": datetime.now(timezone.utc).isoformat(),
            "summary": {
                "total_controls": total,
                "fully_implemented": implemented,
                "partially_implemented": partial,
                "not_implemented": missing,
                "implementation_rate": f"{implemented / total * 100:.1f}%" if total > 0 else "N/A",
            },
            "critical_gaps": [
                {
                    "subcategory": c.subcategory,
                    "control": c.control_name,
                    "status": c.status.value,
                    "risk": c.risk_if_missing.value,
                    "remediation": c.remediation,
                    "owner": c.owner,
                }
                for c in critical_gaps
            ],
        }


if __name__ == "__main__":
    assessor = ProtectFunctionAssessor("Cipher Engineering Labs")

    findings = [
        {"subcategory": "PR.AC-P1", "status": "fully_implemented", "evidence": "Okta IdP with MFA enforced", "owner": "IT Security"},
        {"subcategory": "PR.AC-P3", "status": "fully_implemented", "evidence": "Zero-trust VPN deployed", "owner": "IT Security"},
        {"subcategory": "PR.AC-P4", "status": "partially_implemented", "evidence": "RBAC in place but quarterly reviews not automated", "remediation": "Implement automated access review tool", "owner": "IT Security"},
    ]
    assessor.assess_access_controls(findings)

    encryption_inv = [
        EncryptionInventory("Customer DB", "AES-256", "TLS 1.3", "HSM", "Annual"),
        EncryptionInventory("Analytics DB", "AES-256", "TLS 1.2", "Software", "Annual"),
        EncryptionInventory("Legacy CRM", "None", "TLS 1.0", "None", "None"),
    ]
    enc_report = assessor.assess_encryption(encryption_inv)

    report = assessor.generate_protect_report()
    print(json.dumps(report, indent=2))
    print(json.dumps(enc_report, indent=2))
