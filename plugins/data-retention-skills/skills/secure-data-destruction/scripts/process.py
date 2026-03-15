"""
Secure Data Destruction Process
Manages destruction workflows, certificate generation, and vendor tracking per NIST SP 800-88.
"""

import json
from datetime import datetime
from enum import Enum
from typing import Optional


class SanitizationLevel(Enum):
    CLEAR = "Clear"
    PURGE = "Purge"
    DESTROY = "Destroy"


class MediaType(Enum):
    HDD = "HDD (magnetic)"
    SSD = "SSD / Flash"
    TAPE = "Magnetic tape"
    OPTICAL = "Optical media (CD/DVD/Blu-ray)"
    USB = "USB flash drive"
    MOBILE = "Mobile device"
    PAPER = "Paper documents"
    VIRTUAL = "Virtual machine / cloud instance"


class DataClassification(Enum):
    STANDARD_PD = "Standard personal data"
    SPECIAL_CATEGORY = "Special category data (Art. 9)"
    HIGHLY_SENSITIVE = "Highly sensitive (financial, security, legal)"
    NON_PERSONAL = "Non-personal data"


class MediaDisposition(Enum):
    REUSE_INTERNAL = "Reuse within organization"
    REUSE_EXTERNAL = "Reuse external (sale, donation)"
    DISPOSAL = "Disposal / recycling"


# NIST SP 800-88 sanitization method recommendations
SANITIZATION_METHODS = {
    (MediaType.HDD, SanitizationLevel.CLEAR): "ATA Secure Erase (single pass overwrite with fixed pattern)",
    (MediaType.HDD, SanitizationLevel.PURGE): "ATA Secure Erase Enhanced (multiple pass) or degaussing with NSA-approved degausser",
    (MediaType.HDD, SanitizationLevel.DESTROY): "Physical destruction: shredding (particle size <= 2mm), disintegration, or incineration",
    (MediaType.SSD, SanitizationLevel.CLEAR): "ATA Secure Erase (vendor implementation)",
    (MediaType.SSD, SanitizationLevel.PURGE): "ATA Sanitize Block Erase or Crypto Erase (if SED)",
    (MediaType.SSD, SanitizationLevel.DESTROY): "Physical destruction: shredding (particle size <= 2mm), disintegration",
    (MediaType.TAPE, SanitizationLevel.CLEAR): "Overwrite entire tape with fixed pattern (single pass)",
    (MediaType.TAPE, SanitizationLevel.PURGE): "Degaussing with NSA-approved degausser rated for tape coercivity",
    (MediaType.TAPE, SanitizationLevel.DESTROY): "Physical destruction: shredding or incineration",
    (MediaType.OPTICAL, SanitizationLevel.DESTROY): "Physical destruction: shredding (particle size <= 0.5mm) or incineration",
    (MediaType.USB, SanitizationLevel.CLEAR): "ATA Secure Erase (if supported)",
    (MediaType.USB, SanitizationLevel.PURGE): "Crypto Erase (if SED); vendor sanitize command",
    (MediaType.USB, SanitizationLevel.DESTROY): "Physical destruction: shredding or disintegration",
    (MediaType.MOBILE, SanitizationLevel.CLEAR): "Factory reset + encryption verification",
    (MediaType.MOBILE, SanitizationLevel.PURGE): "Crypto Erase (full-device encryption key destruction)",
    (MediaType.MOBILE, SanitizationLevel.DESTROY): "Physical destruction: shredding",
    (MediaType.PAPER, SanitizationLevel.DESTROY): "Cross-cut shredding (DIN 66399 P-4 minimum; P-5 for special category)",
}

# DIN 66399 paper shredding security levels
DIN_66399_LEVELS = {
    "P-1": {"max_particle": "12mm strips", "use_case": "General, non-personal"},
    "P-2": {"max_particle": "6mm strips", "use_case": "Internal, low sensitivity"},
    "P-3": {"max_particle": "2mm strips or 320mm2 particles", "use_case": "Personal data (standard)"},
    "P-4": {"max_particle": "160mm2 particles (max 6mm width)", "use_case": "GDPR personal data minimum"},
    "P-5": {"max_particle": "30mm2 particles (max 2mm width)", "use_case": "Special category, financial"},
    "P-6": {"max_particle": "10mm2 particles (max 1mm width)", "use_case": "Classified, intelligence-grade"},
    "P-7": {"max_particle": "5mm2 particles (max 1mm width)", "use_case": "Top secret, maximum security"},
}


def determine_sanitization_level(
    classification: DataClassification,
    disposition: MediaDisposition,
) -> SanitizationLevel:
    """Determine the appropriate sanitization level based on data classification and media disposition."""
    if classification == DataClassification.NON_PERSONAL:
        return SanitizationLevel.CLEAR

    if classification == DataClassification.HIGHLY_SENSITIVE:
        return SanitizationLevel.DESTROY

    if classification == DataClassification.SPECIAL_CATEGORY:
        if disposition == MediaDisposition.REUSE_INTERNAL:
            return SanitizationLevel.PURGE
        return SanitizationLevel.DESTROY

    # Standard personal data
    if disposition == MediaDisposition.REUSE_INTERNAL:
        return SanitizationLevel.CLEAR
    if disposition == MediaDisposition.REUSE_EXTERNAL:
        return SanitizationLevel.PURGE
    return SanitizationLevel.DESTROY


def get_sanitization_method(
    media_type: MediaType,
    level: SanitizationLevel,
) -> str:
    """Get the recommended sanitization method for a given media type and level."""
    key = (media_type, level)
    return SANITIZATION_METHODS.get(key, "No standard method — consult NIST SP 800-88 directly")


def get_din_paper_level(classification: DataClassification) -> str:
    """Get the minimum DIN 66399 paper shredding level for a data classification."""
    if classification == DataClassification.STANDARD_PD:
        return "P-4"
    if classification == DataClassification.SPECIAL_CATEGORY:
        return "P-5"
    if classification == DataClassification.HIGHLY_SENSITIVE:
        return "P-5"
    return "P-1"


class DestructionCertificate:
    """Generates a Certificate of Destruction."""

    def __init__(
        self,
        certificate_number: str,
        destruction_date: str,
        location: str,
        requesting_department: str,
        authorized_by: str,
        dpo_name: str,
    ):
        self.certificate_number = certificate_number
        self.destruction_date = destruction_date
        self.location = location
        self.requesting_department = requesting_department
        self.authorized_by = authorized_by
        self.dpo_name = dpo_name
        self.assets: list[dict] = []
        self.sanitization_details: Optional[dict] = None
        self.verification: Optional[dict] = None
        self.waste_disposal: Optional[dict] = None

    def add_asset(
        self,
        asset_tag: str,
        serial_number: str,
        media_type: str,
        capacity: str,
        classification: str,
        method: str,
    ) -> None:
        self.assets.append({
            "asset_tag": asset_tag,
            "serial_number": serial_number,
            "media_type": media_type,
            "capacity": capacity,
            "data_classification": classification,
            "destruction_method": method,
        })

    def set_sanitization_details(
        self,
        method: str,
        equipment_model: str,
        particle_size: Optional[str] = None,
        degausser_model: Optional[str] = None,
        field_strength: Optional[str] = None,
    ) -> None:
        self.sanitization_details = {
            "method": method,
            "equipment_model": equipment_model,
            "particle_size": particle_size,
            "degausser_model": degausser_model,
            "field_strength": field_strength,
        }

    def set_verification(
        self, result: str, verified_by: str, evidence_file: Optional[str] = None
    ) -> None:
        self.verification = {
            "result": result,
            "verified_by": verified_by,
            "evidence_file": evidence_file,
            "timestamp": datetime.utcnow().isoformat(),
        }

    def generate(self) -> dict:
        return {
            "certificate_number": self.certificate_number,
            "organization": "Orion Data Vault Corp",
            "destruction_date": self.destruction_date,
            "location": self.location,
            "requesting_department": self.requesting_department,
            "authorized_by": self.authorized_by,
            "dpo_approval": self.dpo_name,
            "assets_destroyed": self.assets,
            "sanitization_details": self.sanitization_details,
            "verification": self.verification,
            "waste_disposal": self.waste_disposal,
            "retention_period": "7 years from destruction date",
            "generated_at": datetime.utcnow().isoformat(),
        }


if __name__ == "__main__":
    level = determine_sanitization_level(
        DataClassification.SPECIAL_CATEGORY,
        MediaDisposition.DISPOSAL,
    )
    method = get_sanitization_method(MediaType.HDD, level)
    print(f"Level: {level.value}, Method: {method}")

    cert = DestructionCertificate(
        certificate_number="COD-2026-0087",
        destruction_date="2026-03-14",
        location="Orion Data Vault Corp — Secure Destruction Room B2",
        requesting_department="IT Operations",
        authorized_by="Information Security Manager",
        dpo_name="DPO",
    )
    cert.add_asset("OD-SRV-441", "WD-2TB-A8F21", "HDD 3.5\"", "2 TB", "Special Category", "DESTROY")
    cert.set_sanitization_details(
        "Physical destruction via industrial shredder",
        "HSM Powerline FA 500.3",
        particle_size="2mm",
    )
    cert.set_verification("PASS", "Security Officer")
    print(json.dumps(cert.generate(), indent=2))
