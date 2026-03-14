#!/usr/bin/env python3
"""New Technology Privacy Impact Assessment Engine.

Implements PIA methodology for emerging technologies including IoT,
blockchain, AR/VR, quantum computing, and digital twins.
"""

import json
from datetime import datetime, timedelta
from typing import Any

TECHNOLOGY_RISK_PROFILES = {
    "iot": {
        "name": "Internet of Things",
        "inherent_risks": [
            {
                "id": "IOT-R1",
                "name": "Pervasive data collection",
                "description": "Continuous sensor data collection without visible indicators",
                "wp248_criteria": ["C3", "C5"],
                "default_likelihood": "likely",
                "default_severity": "significant",
            },
            {
                "id": "IOT-R2",
                "name": "Insecure device communications",
                "description": "Unencrypted or weakly encrypted device-to-cloud communications",
                "wp248_criteria": ["C8"],
                "default_likelihood": "possible",
                "default_severity": "significant",
            },
            {
                "id": "IOT-R3",
                "name": "Third-party data collection",
                "description": "Incidental collection of data about bystanders and non-users",
                "wp248_criteria": ["C3", "C7"],
                "default_likelihood": "likely",
                "default_severity": "limited",
            },
            {
                "id": "IOT-R4",
                "name": "Cross-device profiling",
                "description": "Combination of data from multiple IoT devices creating comprehensive behavioural profiles",
                "wp248_criteria": ["C1", "C6"],
                "default_likelihood": "possible",
                "default_severity": "significant",
            },
        ],
        "recommended_mitigations": [
            "Local processing where possible — minimise cloud data transmission",
            "End-to-end encryption for all device communications (TLS 1.3 minimum)",
            "Privacy-preserving defaults: minimal data collection enabled by default",
            "Visual/audio indicators when data collection is active",
            "Automated data retention with short default periods",
            "Firmware update mechanism with integrity verification",
        ],
    },
    "blockchain": {
        "name": "Blockchain/Distributed Ledger Technology",
        "inherent_risks": [
            {
                "id": "BC-R1",
                "name": "Immutability vs right to erasure",
                "description": "Append-only ledger prevents deletion of personal data",
                "wp248_criteria": ["C8", "C9"],
                "default_likelihood": "almost_certain",
                "default_severity": "significant",
            },
            {
                "id": "BC-R2",
                "name": "Transaction transparency",
                "description": "Public ledger exposes transaction patterns revealing personal information",
                "wp248_criteria": ["C3", "C8"],
                "default_likelihood": "likely",
                "default_severity": "limited",
            },
            {
                "id": "BC-R3",
                "name": "Re-identification of pseudonymous addresses",
                "description": "Blockchain address analysis can link pseudonymous transactions to real identities",
                "wp248_criteria": ["C6", "C8"],
                "default_likelihood": "possible",
                "default_severity": "significant",
            },
        ],
        "recommended_mitigations": [
            "Store personal data off-chain; use only hashes or commitments on-chain",
            "Use permissioned blockchain with access controls where possible",
            "Implement zero-knowledge proofs for transaction privacy",
            "Use rotating addresses and mixing protocols to reduce linkability",
            "Designate clear data controller responsibilities among participants",
        ],
    },
    "ar_vr": {
        "name": "Augmented and Virtual Reality",
        "inherent_risks": [
            {
                "id": "ARVR-R1",
                "name": "Biometric data collection",
                "description": "Eye tracking, facial expressions, body movement patterns constitute biometric data",
                "wp248_criteria": ["C4", "C8"],
                "default_likelihood": "almost_certain",
                "default_severity": "significant",
            },
            {
                "id": "ARVR-R2",
                "name": "Environmental scanning of third parties",
                "description": "Spatial mapping captures data about people in the physical environment",
                "wp248_criteria": ["C3", "C7"],
                "default_likelihood": "likely",
                "default_severity": "limited",
            },
            {
                "id": "ARVR-R3",
                "name": "Behavioural profiling through gaze tracking",
                "description": "Eye movement data reveals interests, cognitive state, and emotional responses",
                "wp248_criteria": ["C1", "C4"],
                "default_likelihood": "likely",
                "default_severity": "significant",
            },
        ],
        "recommended_mitigations": [
            "Process biometric data locally on device; do not transmit raw biometric data to cloud",
            "Implement on-device anonymisation of spatial mapping data",
            "Granular consent for each biometric data type (eye tracking, face tracking, body tracking)",
            "Blurring or masking of bystander faces in spatial maps",
            "Age verification and enhanced protections for child users",
        ],
    },
    "quantum_computing": {
        "name": "Quantum Computing",
        "inherent_risks": [
            {
                "id": "QC-R1",
                "name": "Cryptographic vulnerability",
                "description": "Quantum computers can break RSA and ECC encryption protecting personal data",
                "wp248_criteria": ["C8"],
                "default_likelihood": "remote",
                "default_severity": "maximum",
            },
            {
                "id": "QC-R2",
                "name": "Harvest now, decrypt later",
                "description": "Encrypted data intercepted today can be decrypted when quantum computers mature",
                "wp248_criteria": ["C8"],
                "default_likelihood": "possible",
                "default_severity": "maximum",
            },
            {
                "id": "QC-R3",
                "name": "Enhanced analytical capabilities",
                "description": "Quantum ML enables analysis at scales impossible for classical computers",
                "wp248_criteria": ["C1", "C5", "C8"],
                "default_likelihood": "remote",
                "default_severity": "significant",
            },
        ],
        "recommended_mitigations": [
            "Inventory all cryptographic assets and classify by quantum vulnerability",
            "Begin migration to NIST post-quantum cryptography standards (ML-KEM, ML-DSA, SLH-DSA)",
            "Implement crypto-agility: design systems to swap cryptographic algorithms without redesign",
            "Apply post-quantum encryption to data with long-term confidentiality requirements immediately",
            "Monitor quantum computing developments and adjust migration timeline accordingly",
        ],
    },
    "digital_twins": {
        "name": "Digital Twins",
        "inherent_risks": [
            {
                "id": "DT-R1",
                "name": "Comprehensive data aggregation",
                "description": "Digital twin aggregates data from multiple sources creating a detailed virtual replica",
                "wp248_criteria": ["C1", "C5", "C6"],
                "default_likelihood": "almost_certain",
                "default_severity": "significant",
            },
            {
                "id": "DT-R2",
                "name": "Predictive modelling of individuals",
                "description": "Digital twin predicts future states and behaviours of the individual it represents",
                "wp248_criteria": ["C1", "C2"],
                "default_likelihood": "likely",
                "default_severity": "significant",
            },
            {
                "id": "DT-R3",
                "name": "Re-identification risk",
                "description": "Sufficiently detailed digital twin can be re-identified even without direct identifiers",
                "wp248_criteria": ["C6", "C8"],
                "default_likelihood": "possible",
                "default_severity": "significant",
            },
        ],
        "recommended_mitigations": [
            "Apply purpose limitation: digital twin used only for documented purposes",
            "Implement differential privacy for predictive model outputs",
            "Restrict access to individual-level digital twins to authorised personnel only",
            "Anonymise or aggregate digital twin data for any purpose beyond individual care/service",
            "Regular audit of digital twin data sources and access patterns",
        ],
    },
}

LIKELIHOOD_SCORES = {"remote": 1, "possible": 2, "likely": 3, "almost_certain": 4}
SEVERITY_SCORES = {"negligible": 1, "limited": 2, "significant": 3, "maximum": 4}
RISK_MATRIX = {
    (1, 1): "Low", (1, 2): "Low", (1, 3): "Medium", (1, 4): "Medium",
    (2, 1): "Low", (2, 2): "Medium", (2, 3): "High", (2, 4): "High",
    (3, 1): "Medium", (3, 2): "High", (3, 3): "High", (3, 4): "Very High",
    (4, 1): "Medium", (4, 2): "High", (4, 3): "Very High", (4, 4): "Very High",
}


def get_technology_risk_profile(technology_type: str) -> dict[str, Any] | None:
    """Retrieve the risk profile for a specific technology type."""
    return TECHNOLOGY_RISK_PROFILES.get(technology_type)


def assess_technology_risks(
    technology_type: str,
    risk_overrides: dict[str, dict[str, str]] | None = None,
) -> dict[str, Any]:
    """Assess risks for a specific emerging technology.

    Args:
        technology_type: Technology type key (iot, blockchain, ar_vr, quantum_computing, digital_twins)
        risk_overrides: Optional overrides for default likelihood/severity per risk ID

    Returns:
        Technology risk assessment
    """
    profile = TECHNOLOGY_RISK_PROFILES.get(technology_type)
    if not profile:
        return {"error": f"Unknown technology type: {technology_type}"}

    overrides = risk_overrides or {}
    assessed_risks = []

    for risk in profile["inherent_risks"]:
        rid = risk["id"]
        likelihood = overrides.get(rid, {}).get("likelihood", risk["default_likelihood"])
        severity = overrides.get(rid, {}).get("severity", risk["default_severity"])

        l_score = LIKELIHOOD_SCORES[likelihood]
        s_score = SEVERITY_SCORES[severity]
        level = RISK_MATRIX[(l_score, s_score)]

        assessed_risks.append({
            "risk_id": rid,
            "name": risk["name"],
            "description": risk["description"],
            "wp248_criteria": risk["wp248_criteria"],
            "likelihood": likelihood,
            "severity": severity,
            "risk_level": level,
            "requires_mitigation": level in ("High", "Very High"),
        })

    high_risks = [r for r in assessed_risks if r["requires_mitigation"]]

    return {
        "technology": profile["name"],
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "risks": assessed_risks,
        "total_risks": len(assessed_risks),
        "high_or_very_high_risks": len(high_risks),
        "recommended_mitigations": profile["recommended_mitigations"],
        "dpia_required": len(high_risks) > 0 or len(assessed_risks) >= 2,
        "review_interval_months": 6,
    }


def generate_technology_pia_report(
    reference: str,
    org_name: str,
    technology_name: str,
    technology_type: str,
    deployment_description: str,
    risk_assessment: dict[str, Any],
    proportionality_assessment: dict[str, str],
) -> dict[str, Any]:
    """Generate a complete PIA report for an emerging technology deployment."""
    return {
        "metadata": {
            "reference": reference,
            "organisation": org_name,
            "technology": technology_name,
            "version": "1.0",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "next_review": (
                datetime.now() + timedelta(days=180)
            ).strftime("%Y-%m-%d"),
        },
        "technology_description": deployment_description,
        "risk_assessment": risk_assessment,
        "proportionality_assessment": proportionality_assessment,
        "conclusion": {
            "dpia_required": risk_assessment["dpia_required"],
            "high_risks_count": risk_assessment["high_or_very_high_risks"],
            "deployment_recommendation": (
                "Deployment may proceed with implementation of all recommended "
                "mitigation measures and 6-month review cycle."
                if risk_assessment["high_or_very_high_risks"] <= 2
                else "Deployment should be paused pending resolution of multiple "
                "high-risk findings. Consider alternative technology or architecture."
            ),
        },
    }


def run_example_pia() -> dict[str, Any]:
    """Run an example PIA for QuantumLeap Health Technologies IoT deployment."""

    risk_assessment = assess_technology_risks(
        technology_type="iot",
        risk_overrides={
            "IOT-R1": {"likelihood": "likely", "severity": "significant"},
            "IOT-R2": {"likelihood": "possible", "severity": "significant"},
            "IOT-R3": {"likelihood": "possible", "severity": "limited"},
            "IOT-R4": {"likelihood": "possible", "severity": "significant"},
        },
    )

    return generate_technology_pia_report(
        reference="PIA-QLH-2026-0005",
        org_name="QuantumLeap Health Technologies",
        technology_name="Smart Building Environmental Monitoring System",
        technology_type="iot",
        deployment_description=(
            "QuantumLeap Health Technologies is deploying an IoT-based smart building "
            "system across its three office locations (London, Berlin, Dublin) to "
            "monitor environmental conditions (temperature, humidity, CO2 levels, "
            "occupancy) and optimise HVAC and lighting systems for energy efficiency "
            "and employee comfort. The system uses 450 environmental sensors, 85 "
            "occupancy sensors (passive infrared and ultrasonic), and 12 indoor air "
            "quality monitors. Occupancy data is aggregated to room level and does "
            "not identify individual employees. Environmental data is transmitted "
            "to a cloud platform (Siemens Navigator, hosted in AWS eu-central-1) "
            "for analytics and building management system integration."
        ),
        risk_assessment=risk_assessment,
        proportionality_assessment={
            "necessity": (
                "Environmental monitoring is necessary for building management, "
                "energy optimisation (EU Energy Efficiency Directive 2023/1791 "
                "compliance), and employee health and safety (Workplace Regulations "
                "1992, ArbStattV Germany)."
            ),
            "data_minimisation": (
                "Occupancy sensors detect presence only (not identity). Data is "
                "aggregated to room level. No individual tracking capability. "
                "Environmental data does not contain personal identifiers."
            ),
            "less_invasive_alternative": (
                "Alternative considered: manual environmental monitoring by facilities "
                "team. Rejected: insufficient granularity for regulatory compliance "
                "and significantly higher resource cost. The IoT approach with "
                "room-level aggregation is the least invasive automated option."
            ),
            "proportionality_conclusion": (
                "Processing is proportionate: occupancy data is aggregated to room "
                "level (not individual), environmental data serves legitimate health "
                "and safety purposes, and data minimisation is enforced by design."
            ),
        },
    )


if __name__ == "__main__":
    result = run_example_pia()
    print(json.dumps(result, indent=2, default=str))
