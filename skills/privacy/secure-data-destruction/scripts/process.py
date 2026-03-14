#!/usr/bin/env python3
"""
Secure Data Destruction Process
Manages destruction workflow, certificate generation, and vendor audit tracking
per NIST SP 800-88 Rev. 1 for Orion Data Vault Corp.
"""

import json
import hashlib
from datetime import datetime, timedelta
from enum import Enum


class SanitizationLevel(Enum):
    CLEAR = "Clear"
    PURGE = "Purge"
    DESTROY = "Destroy"


class MediaType(Enum):
    HDD = "HDD (Magnetic)"
    SSD = "SSD / Flash"
    TAPE = "Magnetic Tape"
    OPTICAL = "Optical Media"
    USB = "USB Flash Drive"
    MOBILE = "Mobile Device"
    PAPER = "Paper Documents"
    VM = "Virtual Machine"


class DataClassification(Enum):
    STANDARD = "Standard Personal Data"
    SPECIAL_CATEGORY = "Special Category Data (Art. 9)"
    HIGHLY_SENSITIVE = "Highly Sensitive (financial, security, legal)"


DIN_66399_LEVELS = {
    "P-1": {"particle_size": "12mm strips", "use_case": "General non-personal"},
    "P-2": {"particle_size": "6mm strips", "use_case": "Internal, low sensitivity"},
    "P-3": {"particle_size": "2mm strips or 320mm² particles", "use_case": "Personal data (standard)"},
    "P-4": {"particle_size": "160mm² (max 6mm width)", "use_case": "GDPR personal data minimum"},
    "P-5": {"particle_size": "30mm² (max 2mm width)", "use_case": "Special category, financial"},
    "P-6": {"particle_size": "10mm² (max 1mm width)", "use_case": "Classified, intelligence"},
    "P-7": {"particle_size": "5mm² (max 1mm width)", "use_case": "Top secret, maximum security"},
}


def determine_sanitization_level(
    classification: DataClassification, disposition: str
) -> SanitizationLevel:
    """Determine the appropriate NIST SP 800-88 sanitization level."""
    matrix = {
        DataClassification.STANDARD: {
            "reuse_internal": SanitizationLevel.CLEAR,
            "reuse_external": SanitizationLevel.PURGE,
            "disposal": SanitizationLevel.DESTROY,
        },
        DataClassification.SPECIAL_CATEGORY: {
            "reuse_internal": SanitizationLevel.PURGE,
            "reuse_external": SanitizationLevel.DESTROY,
            "disposal": SanitizationLevel.DESTROY,
        },
        DataClassification.HIGHLY_SENSITIVE: {
            "reuse_internal": SanitizationLevel.DESTROY,
            "reuse_external": SanitizationLevel.DESTROY,
            "disposal": SanitizationLevel.DESTROY,
        },
    }
    return matrix.get(classification, {}).get(disposition, SanitizationLevel.DESTROY)


def determine_din_level(classification: DataClassification) -> str:
    """Determine the minimum DIN 66399 shredding level for paper documents."""
    levels = {
        DataClassification.STANDARD: "P-4",
        DataClassification.SPECIAL_CATEGORY: "P-5",
        DataClassification.HIGHLY_SENSITIVE: "P-6",
    }
    return levels.get(classification, "P-4")


def generate_destruction_reference() -> str:
    """Generate a unique certificate of destruction reference."""
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    year = datetime.utcnow().strftime("%Y")
    seq = hashlib.md5(timestamp.encode()).hexdigest()[:4].upper()
    return f"COD-{year}-{seq}"


def generate_certificate_of_destruction(
    assets: list[dict],
    destruction_method: str,
    particle_size: str,
    location: str,
    destruction_operator: str,
    verification_officer: str,
    org_name: str = "Orion Data Vault Corp",
) -> dict:
    """Generate a Certificate of Destruction."""
    reference = generate_destruction_reference()

    certificate = {
        "certificate_number": reference,
        "organization": org_name,
        "date_of_destruction": datetime.utcnow().strftime("%Y-%m-%d"),
        "location": location,
        "assets": [],
        "sanitization_details": {
            "method": destruction_method,
            "particle_size": particle_size,
            "standard": "NIST SP 800-88 Rev. 1",
        },
        "verification": {
            "officer": verification_officer,
            "result": "PASS",
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
        "destruction_operator": destruction_operator,
        "chain_of_custody": [],
        "waste_disposal": {
            "recycler": "Licensed WEEE Recycler",
            "transfer_note_ref": f"WTN-{datetime.utcnow().strftime('%Y')}-{reference[-4:]}",
        },
        "retention_of_certificate": {
            "period": "7 years",
            "expiry_date": (datetime.utcnow() + timedelta(days=2555)).strftime("%Y-%m-%d"),
        },
    }

    for asset in assets:
        level = determine_sanitization_level(
            DataClassification(asset.get("classification", "Standard Personal Data")),
            asset.get("disposition", "disposal"),
        )
        certificate["assets"].append({
            "asset_tag": asset.get("asset_tag", "N/A"),
            "serial_number": asset.get("serial_number", "N/A"),
            "media_type": asset.get("media_type", "Unknown"),
            "capacity": asset.get("capacity", "N/A"),
            "classification": asset.get("classification", "Standard Personal Data"),
            "sanitization_level": level.value,
        })

    cert_json = json.dumps(certificate, sort_keys=True)
    certificate["integrity_hash"] = hashlib.sha256(cert_json.encode()).hexdigest()

    return certificate


def vendor_compliance_checklist() -> dict:
    """Generate the vendor qualification compliance checklist."""
    return {
        "checklist_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "requirements": [
            {"requirement": "ISO/IEC 27001:2022 certification", "category": "Information Security", "status": "pending"},
            {"requirement": "EN 15713:2009 certification", "category": "Secure Destruction", "status": "pending"},
            {"requirement": "ADISA certification", "category": "Asset Disposal", "status": "pending"},
            {"requirement": "GDPR Art. 28 DPA signed", "category": "Data Protection", "status": "pending"},
            {"requirement": "DBS checks on all personnel", "category": "Personnel Security", "status": "pending"},
            {"requirement": "Professional indemnity insurance (min 5M GBP)", "category": "Insurance", "status": "pending"},
            {"requirement": "WEEE compliance / waste carrier license", "category": "Environmental", "status": "pending"},
            {"requirement": "Business continuity plan", "category": "Resilience", "status": "pending"},
            {"requirement": "Incident response procedure (24h notification)", "category": "Incident Management", "status": "pending"},
            {"requirement": "GPS-tracked, locked vehicles", "category": "Transport Security", "status": "pending"},
        ],
    }


def generate_vendor_audit_report(
    vendor_name: str, audit_date: str, findings: list[dict]
) -> dict:
    """Generate a vendor annual audit report."""
    critical = sum(1 for f in findings if f.get("severity") == "critical")
    major = sum(1 for f in findings if f.get("severity") == "major")
    minor = sum(1 for f in findings if f.get("severity") == "minor")

    if critical > 0:
        recommendation = "SUSPEND engagement"
    elif major > 0:
        recommendation = "REMEDIATE within 14 days; increased monitoring"
    elif minor > 0:
        recommendation = "REMEDIATE within 30 days"
    else:
        recommendation = "CONTINUE engagement — no findings"

    return {
        "vendor": vendor_name,
        "audit_date": audit_date,
        "findings_summary": {
            "critical": critical,
            "major": major,
            "minor": minor,
            "total": len(findings),
        },
        "findings": findings,
        "recommendation": recommendation,
        "next_audit_date": (
            datetime.strptime(audit_date, "%Y-%m-%d") + timedelta(days=365)
        ).strftime("%Y-%m-%d"),
    }


if __name__ == "__main__":
    level = determine_sanitization_level(DataClassification.SPECIAL_CATEGORY, "disposal")
    print(f"Special Category + Disposal → {level.value}")

    din = determine_din_level(DataClassification.SPECIAL_CATEGORY)
    print(f"DIN 66399 Level: {din} ({DIN_66399_LEVELS[din]['particle_size']})")

    sample_assets = [
        {
            "asset_tag": "OD-SRV-441",
            "serial_number": "WD-2TB-A8F21",
            "media_type": "HDD 3.5\"",
            "capacity": "2 TB",
            "classification": "Special Category Data (Art. 9)",
            "disposition": "disposal",
        },
        {
            "asset_tag": "OD-LAP-219",
            "serial_number": "SM-512-C3E01",
            "media_type": "SSD M.2",
            "capacity": "512 GB",
            "classification": "Standard Personal Data",
            "disposition": "disposal",
        },
    ]

    cert = generate_certificate_of_destruction(
        assets=sample_assets,
        destruction_method="Industrial shredder (HSM Powerline FA 500.3)",
        particle_size="2mm (DIN 66399 E-4 / H-5)",
        location="Orion Data Vault Corp — Secure Destruction Room B2",
        destruction_operator="IT Security Technician",
        verification_officer="Security Officer",
    )
    print(f"\nCertificate: {cert['certificate_number']}")
    print(f"Assets Destroyed: {len(cert['assets'])}")
    print(f"Integrity Hash: {cert['integrity_hash'][:32]}...")

    vendor_audit = generate_vendor_audit_report(
        vendor_name="SecureShred Ltd",
        audit_date="2026-03-14",
        findings=[],
    )
    print(f"\nVendor Audit: {vendor_audit['recommendation']}")
