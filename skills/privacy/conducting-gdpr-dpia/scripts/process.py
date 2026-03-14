#!/usr/bin/env python3
"""GDPR DPIA Screening, Risk Assessment, and Report Generation Engine.

Implements the WP248rev.01 nine-criteria screening methodology and
Art. 35(7) risk assessment framework for Data Protection Impact Assessments.
"""

import json
import hashlib
from datetime import datetime, timedelta
from typing import Any

# ---------------------------------------------------------------------------
# WP248rev.01 DPIA Screening Criteria
# ---------------------------------------------------------------------------

EDPB_CRITERIA = [
    {
        "id": "C1",
        "name": "Evaluation or Scoring",
        "description": (
            "Profiling and predicting aspects concerning data subject performance "
            "at work, economic situation, health, personal preferences, interests, "
            "reliability, behaviour, location, or movements."
        ),
        "examples": [
            "Credit scoring",
            "Behavioural advertising profiles",
            "Employee performance scoring",
            "Insurance risk profiling",
        ],
    },
    {
        "id": "C2",
        "name": "Automated Decision-Making with Legal or Significant Effect",
        "description": (
            "Processing intended to make decisions about data subjects producing "
            "legal effects or similarly significantly affecting them."
        ),
        "examples": [
            "Automated loan approval or rejection",
            "Algorithmic hiring decisions",
            "Automated insurance claim processing",
            "E-government benefit eligibility determination",
        ],
    },
    {
        "id": "C3",
        "name": "Systematic Monitoring",
        "description": (
            "Processing used to observe, monitor, or control data subjects, "
            "including data collected through networks or systematic monitoring "
            "of a publicly accessible area."
        ),
        "examples": [
            "CCTV surveillance systems",
            "Employee email and internet monitoring",
            "GPS tracking of vehicles or personnel",
            "Wi-Fi or Bluetooth tracking in public spaces",
        ],
    },
    {
        "id": "C4",
        "name": "Sensitive Data or Highly Personal Data",
        "description": (
            "Special categories of data under Art. 9, criminal conviction data "
            "under Art. 10, or other data considered highly personal such as "
            "financial data, location data, or communications content."
        ),
        "examples": [
            "Health records processing",
            "Biometric identification data",
            "Genetic data analysis",
            "Financial transaction monitoring",
        ],
    },
    {
        "id": "C5",
        "name": "Large-Scale Processing",
        "description": (
            "Processing involving a large number of data subjects, large volume "
            "of data items, wide geographic scope, or long duration."
        ),
        "examples": [
            "National patient records system",
            "Telecom metadata retention",
            "Social media platform user data",
            "Nationwide loyalty card programme",
        ],
    },
    {
        "id": "C6",
        "name": "Matching or Combining Datasets",
        "description": (
            "Combining, comparing, or matching personal data from multiple "
            "sources in a way that exceeds the reasonable expectation of the "
            "data subject."
        ),
        "examples": [
            "Cross-device tracking and profile merging",
            "Data broker aggregation from public and private sources",
            "Merging HR data with health insurer data",
            "Combining online and offline purchase data",
        ],
    },
    {
        "id": "C7",
        "name": "Vulnerable Data Subjects",
        "description": (
            "Processing data of vulnerable individuals where the power imbalance "
            "between data subject and controller is significant."
        ),
        "examples": [
            "Children's data in educational platforms",
            "Patient data in clinical settings",
            "Employee monitoring and surveillance",
            "Asylum seeker case management systems",
        ],
    },
    {
        "id": "C8",
        "name": "Innovative Technology",
        "description": (
            "Use of new or innovative technological or organisational solutions "
            "where the personal data protection impact is not yet fully understood."
        ),
        "examples": [
            "AI/ML-based decision systems",
            "Facial recognition technology",
            "IoT sensor networks collecting personal data",
            "Blockchain-based identity management",
        ],
    },
    {
        "id": "C9",
        "name": "Processing Preventing Exercise of Rights or Use of Service",
        "description": (
            "Processing that blocks or restricts data subjects from exercising "
            "a right or using a service or a contract."
        ),
        "examples": [
            "Credit reference checks blocking account opening",
            "Background checks preventing employment",
            "Fraud screening denying transaction processing",
            "Age verification systems blocking service access",
        ],
    },
]

ART_35_3_TRIGGERS = [
    {
        "id": "T1",
        "reference": "Art. 35(3)(a)",
        "name": "Systematic Extensive Profiling with Significant Effects",
        "description": (
            "Systematic and extensive evaluation of personal aspects of natural "
            "persons based on automated processing, including profiling, on which "
            "decisions are based that produce legal effects or similarly significantly "
            "affect the natural person."
        ),
    },
    {
        "id": "T2",
        "reference": "Art. 35(3)(b)",
        "name": "Large-Scale Special Category or Criminal Data",
        "description": (
            "Processing on a large scale of special categories of data referred "
            "to in Art. 9(1), or of personal data relating to criminal convictions "
            "and offences referred to in Art. 10."
        ),
    },
    {
        "id": "T3",
        "reference": "Art. 35(3)(c)",
        "name": "Systematic Large-Scale Public Area Monitoring",
        "description": (
            "Systematic monitoring of a publicly accessible area on a large scale."
        ),
    },
]

LIKELIHOOD_SCALE = {
    "remote": {"label": "Remote", "range": "< 10%", "score": 1},
    "possible": {"label": "Possible", "range": "10-50%", "score": 2},
    "likely": {"label": "Likely", "range": "50-90%", "score": 3},
    "almost_certain": {"label": "Almost Certain", "range": "> 90%", "score": 4},
}

SEVERITY_SCALE = {
    "negligible": {
        "label": "Negligible",
        "description": "Minor inconvenience, easily recoverable",
        "score": 1,
    },
    "limited": {
        "label": "Limited",
        "description": "Significant difficulties but recoverable with effort",
        "score": 2,
    },
    "significant": {
        "label": "Significant",
        "description": "Serious consequences, difficult to recover from",
        "score": 3,
    },
    "maximum": {
        "label": "Maximum",
        "description": "Irreversible consequences, inability to recover",
        "score": 4,
    },
}

RISK_MATRIX = {
    (1, 1): "Low",
    (1, 2): "Low",
    (1, 3): "Medium",
    (1, 4): "Medium",
    (2, 1): "Low",
    (2, 2): "Medium",
    (2, 3): "High",
    (2, 4): "High",
    (3, 1): "Medium",
    (3, 2): "High",
    (3, 3): "High",
    (3, 4): "Very High",
    (4, 1): "Medium",
    (4, 2): "High",
    (4, 3): "Very High",
    (4, 4): "Very High",
}


def generate_dpia_reference(org_name: str, year: int, sequence: int) -> str:
    """Generate a unique DPIA reference number."""
    prefix = org_name[:3].upper()
    return f"DPIA-{prefix}-{year}-{sequence:04d}"


def screen_art35_3_triggers(trigger_responses: dict[str, bool]) -> dict[str, Any]:
    """Screen processing against Art. 35(3)(a)-(c) mandatory triggers.

    Args:
        trigger_responses: dict mapping trigger IDs (T1, T2, T3) to True/False

    Returns:
        Screening result with mandatory flag and matched triggers
    """
    matched = []
    for trigger in ART_35_3_TRIGGERS:
        tid = trigger["id"]
        if trigger_responses.get(tid, False):
            matched.append(
                {
                    "id": tid,
                    "reference": trigger["reference"],
                    "name": trigger["name"],
                }
            )

    return {
        "mandatory_dpia": len(matched) > 0,
        "matched_triggers": matched,
        "trigger_count": len(matched),
        "assessment": (
            "DPIA is mandatory under Art. 35(3) — one or more automatic triggers met."
            if matched
            else "No Art. 35(3) automatic triggers met. Proceed to EDPB criteria screening."
        ),
    }


def screen_edpb_criteria(criteria_responses: dict[str, bool]) -> dict[str, Any]:
    """Screen processing against EDPB WP248rev.01 nine criteria.

    Args:
        criteria_responses: dict mapping criteria IDs (C1-C9) to True/False

    Returns:
        Screening result with recommendation level and matched criteria
    """
    matched = []
    for criterion in EDPB_CRITERIA:
        cid = criterion["id"]
        if criteria_responses.get(cid, False):
            matched.append(
                {"id": cid, "name": criterion["name"]}
            )

    count = len(matched)
    if count >= 2:
        recommendation = "DPIA is strongly recommended (presumptively required per WP248rev.01)."
        dpia_required = True
    elif count == 1:
        recommendation = (
            "DPIA is recommended. Consult DPO for final determination. "
            "One EDPB criterion met — risk may still be high depending on context."
        )
        dpia_required = False
    else:
        recommendation = (
            "DPIA is not required based on EDPB criteria. "
            "Document screening outcome and rationale."
        )
        dpia_required = False

    return {
        "dpia_recommended": dpia_required,
        "criteria_met_count": count,
        "matched_criteria": matched,
        "recommendation": recommendation,
    }


def full_screening(
    trigger_responses: dict[str, bool],
    criteria_responses: dict[str, bool],
    national_list_match: bool = False,
) -> dict[str, Any]:
    """Complete DPIA screening combining all trigger sources.

    Args:
        trigger_responses: Art. 35(3) trigger responses
        criteria_responses: EDPB criteria responses
        national_list_match: Whether processing appears on national SA Art. 35(4) list

    Returns:
        Complete screening result with final determination
    """
    art35_result = screen_art35_3_triggers(trigger_responses)
    edpb_result = screen_edpb_criteria(criteria_responses)

    dpia_mandatory = (
        national_list_match
        or art35_result["mandatory_dpia"]
        or edpb_result["dpia_recommended"]
    )

    reasons = []
    if national_list_match:
        reasons.append("Processing appears on the national supervisory authority Art. 35(4) list.")
    reasons.extend(
        f"Art. 35(3) trigger: {t['reference']} — {t['name']}"
        for t in art35_result["matched_triggers"]
    )
    if edpb_result["dpia_recommended"]:
        reasons.append(
            f"EDPB WP248rev.01: {edpb_result['criteria_met_count']} criteria met "
            f"(threshold is 2)."
        )

    return {
        "screening_date": datetime.now().strftime("%Y-%m-%d"),
        "dpia_required": dpia_mandatory,
        "determination_reasons": reasons,
        "art35_3_result": art35_result,
        "edpb_criteria_result": edpb_result,
        "national_list_match": national_list_match,
        "next_step": (
            "Proceed to full DPIA execution under Art. 35(7)."
            if dpia_mandatory
            else "Document screening outcome. No DPIA required at this time."
        ),
    }


def assess_risk(
    risk_id: str,
    description: str,
    threat_source: str,
    harm_type: str,
    likelihood: str,
    severity: str,
) -> dict[str, Any]:
    """Assess a single risk using the DPIA risk matrix.

    Args:
        risk_id: Unique risk identifier (e.g., DPIA-QLH-2026-0001-R01)
        description: Risk scenario description
        threat_source: Source of the threat (internal, external, processor, system)
        harm_type: Type of harm (physical, material, non-material, social)
        likelihood: Likelihood level (remote, possible, likely, almost_certain)
        severity: Severity level (negligible, limited, significant, maximum)

    Returns:
        Risk assessment with calculated risk level
    """
    l_score = LIKELIHOOD_SCALE[likelihood]["score"]
    s_score = SEVERITY_SCALE[severity]["score"]
    risk_level = RISK_MATRIX[(l_score, s_score)]

    return {
        "risk_id": risk_id,
        "description": description,
        "threat_source": threat_source,
        "harm_type": harm_type,
        "likelihood": {
            "level": LIKELIHOOD_SCALE[likelihood]["label"],
            "range": LIKELIHOOD_SCALE[likelihood]["range"],
            "score": l_score,
        },
        "severity": {
            "level": SEVERITY_SCALE[severity]["label"],
            "description": SEVERITY_SCALE[severity]["description"],
            "score": s_score,
        },
        "inherent_risk_level": risk_level,
        "requires_mitigation": risk_level in ("High", "Very High"),
        "requires_prior_consultation": risk_level == "Very High",
    }


def assess_residual_risk(
    inherent_assessment: dict[str, Any],
    mitigation_measures: list[dict[str, str]],
    residual_likelihood: str,
    residual_severity: str,
) -> dict[str, Any]:
    """Calculate residual risk after mitigation measures.

    Args:
        inherent_assessment: Original risk assessment from assess_risk()
        mitigation_measures: List of measures with 'type', 'description', 'owner', 'deadline'
        residual_likelihood: Post-mitigation likelihood level
        residual_severity: Post-mitigation severity level

    Returns:
        Residual risk assessment with comparison to inherent risk
    """
    l_score = LIKELIHOOD_SCALE[residual_likelihood]["score"]
    s_score = SEVERITY_SCALE[residual_severity]["score"]
    residual_level = RISK_MATRIX[(l_score, s_score)]

    return {
        "risk_id": inherent_assessment["risk_id"],
        "inherent_risk_level": inherent_assessment["inherent_risk_level"],
        "mitigation_measures": mitigation_measures,
        "residual_likelihood": {
            "level": LIKELIHOOD_SCALE[residual_likelihood]["label"],
            "score": l_score,
        },
        "residual_severity": {
            "level": SEVERITY_SCALE[residual_severity]["label"],
            "score": s_score,
        },
        "residual_risk_level": residual_level,
        "risk_reduced": residual_level != inherent_assessment["inherent_risk_level"],
        "requires_prior_consultation": residual_level in ("High", "Very High"),
        "recommendation": (
            "Residual risk remains high. Art. 36 prior consultation with the "
            "supervisory authority is required before processing may begin."
            if residual_level in ("High", "Very High")
            else "Residual risk is acceptable. Processing may proceed with "
            "implementation of documented mitigation measures."
        ),
    }


def generate_dpia_report(
    reference: str,
    org_name: str,
    processing_name: str,
    processing_description: str,
    lawful_basis: str,
    data_categories: list[str],
    data_subjects: list[str],
    recipients: list[str],
    retention_period: str,
    screening_result: dict[str, Any],
    risk_assessments: list[dict[str, Any]],
    dpo_name: str,
    dpo_advice: str,
    data_subject_views_sought: bool,
    data_subject_views_justification: str,
) -> dict[str, Any]:
    """Generate a complete DPIA report structure per Art. 35(7).

    Returns:
        Complete DPIA report as structured data
    """
    high_risks = [r for r in risk_assessments if r.get("requires_mitigation", False)]
    very_high_residual = [
        r for r in risk_assessments if r.get("requires_prior_consultation", False)
    ]

    report = {
        "metadata": {
            "dpia_reference": reference,
            "organisation": org_name,
            "processing_name": processing_name,
            "version": "1.0",
            "status": "Draft",
            "created_date": datetime.now().strftime("%Y-%m-%d"),
            "next_review_date": (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d"),
            "dpo": dpo_name,
        },
        "art_35_7_a_systematic_description": {
            "processing_name": processing_name,
            "processing_description": processing_description,
            "lawful_basis": lawful_basis,
            "data_categories": data_categories,
            "data_subjects": data_subjects,
            "recipients": recipients,
            "retention_period": retention_period,
        },
        "art_35_7_b_necessity_proportionality": {
            "lawful_basis_justification": lawful_basis,
            "data_minimisation_assessment": (
                "Each data category has been assessed for necessity. "
                "No data category can be removed without undermining the processing purpose."
            ),
            "retention_justification": retention_period,
        },
        "art_35_7_c_risk_assessment": {
            "total_risks_identified": len(risk_assessments),
            "high_or_very_high_risks": len(high_risks),
            "risk_register": risk_assessments,
        },
        "art_35_7_d_mitigation_measures": {
            "measures_count": sum(
                len(r.get("mitigation_measures", []))
                for r in risk_assessments
            ),
            "prior_consultation_required": len(very_high_residual) > 0,
        },
        "art_35_2_dpo_advice": {
            "dpo_name": dpo_name,
            "advice": dpo_advice,
            "advice_followed": True,
        },
        "art_35_9_data_subject_views": {
            "views_sought": data_subject_views_sought,
            "justification": data_subject_views_justification,
        },
        "screening_result": screening_result,
        "conclusion": {
            "prior_consultation_required": len(very_high_residual) > 0,
            "processing_approved": len(very_high_residual) == 0,
            "approval_conditions": (
                "Processing may proceed subject to implementation of all documented "
                "mitigation measures and scheduled periodic review."
                if len(very_high_residual) == 0
                else "Processing must not proceed until Art. 36 prior consultation "
                "is completed and supervisory authority response is received."
            ),
        },
    }

    report_json = json.dumps(report, sort_keys=True)
    report["metadata"]["integrity_hash"] = hashlib.sha256(
        report_json.encode()
    ).hexdigest()[:16]

    return report


# ---------------------------------------------------------------------------
# Example: QuantumLeap Health Technologies — Employee Monitoring System DPIA
# ---------------------------------------------------------------------------

def run_example_dpia() -> dict[str, Any]:
    """Execute a complete DPIA for QuantumLeap Health Technologies employee monitoring system."""

    org_name = "QuantumLeap Health Technologies"
    reference = generate_dpia_reference(org_name, 2026, 1)

    # Step 1: Screening
    screening = full_screening(
        trigger_responses={"T1": False, "T2": False, "T3": False},
        criteria_responses={
            "C1": True,   # Evaluation/scoring — employee performance scoring
            "C2": False,
            "C3": True,   # Systematic monitoring — email, internet, badge access
            "C4": False,
            "C5": False,
            "C6": True,   # Matching datasets — HR + badge + email + productivity
            "C7": True,   # Vulnerable data subjects — employees (power imbalance)
            "C8": False,
            "C9": False,
        },
        national_list_match=False,
    )

    # Step 2: Risk Assessment
    risk_1 = assess_risk(
        risk_id=f"{reference}-R01",
        description=(
            "Unauthorised access to employee monitoring data by line managers "
            "for purposes beyond legitimate performance management, leading to "
            "discriminatory treatment based on monitoring patterns."
        ),
        threat_source="Internal — line managers",
        harm_type="Non-material (discrimination, chilling effect on workplace behaviour)",
        likelihood="possible",
        severity="significant",
    )

    risk_2 = assess_risk(
        risk_id=f"{reference}-R02",
        description=(
            "Aggregation of email monitoring, internet usage, badge access, and "
            "productivity metrics creates a comprehensive behavioural profile "
            "that exceeds employee expectations and proportionality requirements."
        ),
        threat_source="System design — excessive data combination",
        harm_type="Non-material (loss of autonomy, chilling effect)",
        likelihood="likely",
        severity="significant",
    )

    risk_3 = assess_risk(
        risk_id=f"{reference}-R03",
        description=(
            "Data breach exposing employee monitoring records to external attackers, "
            "revealing detailed behavioural patterns, health-related absence data, "
            "and disciplinary information."
        ),
        threat_source="External — cyber attack",
        harm_type="Material (identity theft, reputational damage) and non-material (distress)",
        likelihood="possible",
        severity="significant",
    )

    # Step 3: Mitigation and Residual Risk
    risk_1_residual = assess_residual_risk(
        inherent_assessment=risk_1,
        mitigation_measures=[
            {
                "type": "Organisational",
                "description": (
                    "Role-based access controls restricting monitoring data access to "
                    "HR department only; line managers receive aggregated reports without "
                    "individual-level detail."
                ),
                "owner": "Head of HR, QuantumLeap Health Technologies",
                "deadline": "2026-05-01",
            },
            {
                "type": "Technical",
                "description": (
                    "Audit logging of all access to monitoring data with automated "
                    "alerts for unusual access patterns or bulk data retrieval."
                ),
                "owner": "Chief Information Security Officer",
                "deadline": "2026-04-15",
            },
        ],
        residual_likelihood="remote",
        residual_severity="limited",
    )

    risk_2_residual = assess_residual_risk(
        inherent_assessment=risk_2,
        mitigation_measures=[
            {
                "type": "Technical",
                "description": (
                    "Data minimisation controls: email monitoring limited to "
                    "metadata (sender, recipient, timestamp) without content access; "
                    "internet monitoring limited to category-level classification "
                    "without URL-level logging; productivity metrics aggregated to "
                    "daily summaries without keystroke-level data."
                ),
                "owner": "Data Protection Officer",
                "deadline": "2026-04-01",
            },
            {
                "type": "Organisational",
                "description": (
                    "Proportionality policy: no cross-referencing of monitoring "
                    "datasets for individual employees without documented justification "
                    "approved by DPO and HR director."
                ),
                "owner": "Data Protection Officer",
                "deadline": "2026-04-01",
            },
        ],
        residual_likelihood="possible",
        residual_severity="limited",
    )

    risk_3_residual = assess_residual_risk(
        inherent_assessment=risk_3,
        mitigation_measures=[
            {
                "type": "Technical",
                "description": (
                    "AES-256 encryption at rest for all monitoring databases; "
                    "TLS 1.3 encryption in transit; network segmentation isolating "
                    "monitoring infrastructure from general corporate network."
                ),
                "owner": "Chief Information Security Officer",
                "deadline": "2026-04-15",
            },
            {
                "type": "Technical",
                "description": (
                    "90-day automated retention with cryptographic erasure for "
                    "monitoring data; 30-day retention for email metadata; "
                    "annual retention for aggregated performance reports only."
                ),
                "owner": "IT Operations Manager",
                "deadline": "2026-05-01",
            },
        ],
        residual_likelihood="remote",
        residual_severity="limited",
    )

    # Step 4: Generate report
    report = generate_dpia_report(
        reference=reference,
        org_name=org_name,
        processing_name="Employee Workplace Monitoring System",
        processing_description=(
            "QuantumLeap Health Technologies operates an employee workplace monitoring "
            "system that collects and processes email metadata (sender, recipient, "
            "timestamp, subject line), internet usage categories, physical badge "
            "access logs, and daily productivity metrics for 2,847 employees across "
            "three office locations (London, Berlin, Dublin). The system aggregates "
            "data into weekly departmental reports used by HR for performance "
            "management, security incident investigation, and regulatory compliance "
            "with financial services record-keeping obligations."
        ),
        lawful_basis=(
            "Art. 6(1)(f) legitimate interest — the controller's legitimate interest "
            "in maintaining workplace security, ensuring regulatory compliance with "
            "FCA record-keeping requirements (SYSC 10A.1), and managing employee "
            "performance. Balancing test documented in separate LIA reference "
            "LIA-QLH-2026-0003."
        ),
        data_categories=[
            "Email metadata (sender, recipient, timestamp, subject line)",
            "Internet usage categories (not URLs)",
            "Physical badge access timestamps and locations",
            "Daily productivity metric summaries",
            "Employee identifiers (name, employee ID, department, role)",
        ],
        data_subjects=[
            "QuantumLeap Health Technologies employees (2,847 across UK, Germany, Ireland)",
            "Contractors with corporate email accounts (approximately 340)",
        ],
        recipients=[
            "HR Department — performance management and disciplinary proceedings",
            "IT Security Team — security incident investigation (access-restricted)",
            "CloudSecure Ltd (processor) — hosting infrastructure under Art. 28 DPA",
            "FCA — regulatory disclosure upon lawful request",
        ],
        retention_period=(
            "Email metadata: 30 days rolling deletion. Internet usage categories: "
            "90 days rolling deletion. Badge access logs: 12 months then automated "
            "erasure. Productivity summaries: 12 months at individual level, then "
            "aggregated to department level and retained for 3 years. All retention "
            "periods enforced by automated deletion scripts with cryptographic erasure."
        ),
        screening_result=screening,
        risk_assessments=[risk_1_residual, risk_2_residual, risk_3_residual],
        dpo_name="Dr. Elena Vasquez, CIPP/E, CIPM",
        dpo_advice=(
            "The processing as initially proposed included keystroke logging and "
            "full URL capture, which I advised were disproportionate to the stated "
            "purposes. Following my advice, these elements were removed and replaced "
            "with aggregated productivity metrics and category-level internet "
            "monitoring respectively. I am satisfied that the revised processing, "
            "with the documented mitigation measures implemented, represents a "
            "proportionate approach. I recommend the DPIA be reviewed in 6 months "
            "rather than 12 given the sensitivity of employee monitoring."
        ),
        data_subject_views_sought=True,
        data_subject_views_justification=(
            "Employee works council representatives were consulted on 2026-01-15. "
            "Consultation covered the scope of monitoring, data access controls, "
            "and retention periods. Works council feedback resulted in: (1) removal "
            "of keystroke logging, (2) restriction of line manager access to "
            "aggregated data only, (3) commitment to 6-month DPIA review cycle. "
            "Union representatives confirmed these changes addressed their primary "
            "concerns regarding proportionality."
        ),
    )

    return report


if __name__ == "__main__":
    result = run_example_dpia()
    print(json.dumps(result, indent=2, default=str))
