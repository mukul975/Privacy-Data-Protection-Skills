#!/usr/bin/env python3
"""PIA Threshold Screening Tool.

Evaluates whether a processing activity requires a full DPIA based on
GDPR Art. 35 mandatory triggers, national SA blacklists, and the EDPB
WP248rev.01 nine-criteria test.
"""

import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class ScreeningOutcome(Enum):
    DPIA_MANDATORY = "DPIA Mandatory"
    DPIA_REQUIRED = "DPIA Required"
    DPIA_RECOMMENDED = "DPIA Recommended"
    DPIA_NOT_REQUIRED = "DPIA Not Required"


class CriterionStatus(Enum):
    MET = "Met"
    NOT_MET = "Not Met"
    BORDERLINE = "Borderline"


@dataclass
class MandatoryTrigger:
    article: str
    description: str
    met: bool
    rationale: str


@dataclass
class WP248Criterion:
    number: int
    name: str
    status: CriterionStatus
    rationale: str


@dataclass
class BlacklistCheck:
    supervisory_authority: str
    list_consulted: str
    match_found: bool
    matched_entry: Optional[str] = None


@dataclass
class ScreeningResult:
    processing_activity: str
    controller: str
    screening_date: str
    screened_by: str
    mandatory_triggers: list = field(default_factory=list)
    blacklist_checks: list = field(default_factory=list)
    wp248_criteria: list = field(default_factory=list)
    outcome: Optional[ScreeningOutcome] = None
    rationale: str = ""
    dpo_review_required: bool = True


WP248_CRITERIA_NAMES = [
    "Evaluation or scoring",
    "Automated decision-making with legal/similar effect",
    "Systematic monitoring",
    "Sensitive data or highly personal data",
    "Data processed on a large scale",
    "Matching or combining datasets",
    "Data concerning vulnerable data subjects",
    "Innovative use or new technological solutions",
    "Processing preventing exercise of a right or use of a service/contract",
]


def evaluate_mandatory_triggers(triggers_input: dict) -> list:
    """Evaluate Art. 35(3)(a)-(c) mandatory triggers."""
    triggers = []

    # Art. 35(3)(a): Systematic profiling with legal effects
    profiling = triggers_input.get("profiling", {})
    art35_3a = MandatoryTrigger(
        article="Art. 35(3)(a)",
        description="Systematic and extensive profiling-based evaluation with legal/significant effects",
        met=(
            profiling.get("systematic_extensive_evaluation", False)
            and profiling.get("automated_processing", False)
            and profiling.get("legal_or_significant_effects", False)
        ),
        rationale=profiling.get("rationale", "Not assessed"),
    )
    triggers.append(art35_3a)

    # Art. 35(3)(b): Large-scale special category processing
    special = triggers_input.get("special_category", {})
    art35_3b = MandatoryTrigger(
        article="Art. 35(3)(b)",
        description="Large-scale processing of special category or criminal conviction data",
        met=(
            special.get("special_category_or_criminal", False)
            and special.get("large_scale", False)
        ),
        rationale=special.get("rationale", "Not assessed"),
    )
    triggers.append(art35_3b)

    # Art. 35(3)(c): Large-scale public area monitoring
    monitoring = triggers_input.get("public_monitoring", {})
    art35_3c = MandatoryTrigger(
        article="Art. 35(3)(c)",
        description="Large-scale systematic monitoring of publicly accessible area",
        met=(
            monitoring.get("systematic_monitoring", False)
            and monitoring.get("publicly_accessible", False)
            and monitoring.get("large_scale", False)
        ),
        rationale=monitoring.get("rationale", "Not assessed"),
    )
    triggers.append(art35_3c)

    return triggers


def evaluate_wp248_criteria(criteria_input: list) -> list:
    """Evaluate the nine WP248rev.01 criteria."""
    criteria = []
    for i, name in enumerate(WP248_CRITERIA_NAMES):
        entry = criteria_input[i] if i < len(criteria_input) else {}
        status_str = entry.get("status", "Not Met")
        try:
            status = CriterionStatus(status_str)
        except ValueError:
            status = CriterionStatus.NOT_MET

        criteria.append(
            WP248Criterion(
                number=i + 1,
                name=name,
                status=status,
                rationale=entry.get("rationale", "Not assessed"),
            )
        )
    return criteria


def determine_outcome(result: ScreeningResult) -> ScreeningResult:
    """Apply decision logic to determine screening outcome."""
    # Check mandatory triggers first
    for trigger in result.mandatory_triggers:
        if trigger.met:
            result.outcome = ScreeningOutcome.DPIA_MANDATORY
            result.rationale = (
                f"Mandatory DPIA trigger met: {trigger.article} -- "
                f"{trigger.description}"
            )
            return result

    # Check national blacklist
    for check in result.blacklist_checks:
        if check.match_found:
            result.outcome = ScreeningOutcome.DPIA_REQUIRED
            result.rationale = (
                f"Processing matches {check.supervisory_authority} "
                f"Art. 35(4) blacklist entry: {check.matched_entry}"
            )
            return result

    # Count WP248 criteria met
    met_count = sum(
        1 for c in result.wp248_criteria if c.status == CriterionStatus.MET
    )
    borderline_count = sum(
        1 for c in result.wp248_criteria if c.status == CriterionStatus.BORDERLINE
    )

    if met_count >= 2:
        met_names = [c.name for c in result.wp248_criteria if c.status == CriterionStatus.MET]
        result.outcome = ScreeningOutcome.DPIA_REQUIRED
        result.rationale = (
            f"{met_count} WP248 criteria met ({', '.join(met_names)}). "
            f"EDPB guidance: 2+ criteria triggers DPIA requirement."
        )
    elif met_count == 1 or borderline_count > 0:
        result.outcome = ScreeningOutcome.DPIA_RECOMMENDED
        result.rationale = (
            f"{met_count} criterion met, {borderline_count} borderline. "
            f"Risk-based decision required -- DPO review recommended."
        )
    else:
        result.outcome = ScreeningOutcome.DPIA_NOT_REQUIRED
        result.rationale = (
            "No mandatory triggers, no blacklist matches, and no WP248 "
            "criteria met. Document exemption and link to RoPA entry."
        )
        result.dpo_review_required = False

    return result


def generate_report(result: ScreeningResult) -> str:
    """Generate a formatted screening report."""
    lines = [
        "=" * 70,
        "PIA THRESHOLD SCREENING REPORT",
        "=" * 70,
        f"Processing Activity: {result.processing_activity}",
        f"Controller:          {result.controller}",
        f"Screening Date:      {result.screening_date}",
        f"Screened By:         {result.screened_by}",
        "",
        "-" * 70,
        "PHASE 1: MANDATORY TRIGGERS (Art. 35(3))",
        "-" * 70,
    ]

    for trigger in result.mandatory_triggers:
        status = "MET" if trigger.met else "NOT MET"
        lines.append(f"  [{status:>7}] {trigger.article}: {trigger.description}")
        lines.append(f"           Rationale: {trigger.rationale}")
        lines.append("")

    lines.extend([
        "-" * 70,
        "PHASE 2: NATIONAL BLACKLIST CHECK",
        "-" * 70,
    ])

    for check in result.blacklist_checks:
        match = "MATCH" if check.match_found else "NO MATCH"
        lines.append(f"  [{match:>8}] {check.supervisory_authority}: {check.list_consulted}")
        if check.match_found and check.matched_entry:
            lines.append(f"             Matched entry: {check.matched_entry}")
        lines.append("")

    lines.extend([
        "-" * 70,
        "PHASE 3: WP248rev.01 NINE-CRITERIA TEST",
        "-" * 70,
    ])

    for criterion in result.wp248_criteria:
        lines.append(
            f"  [{criterion.status.value:>10}] {criterion.number}. {criterion.name}"
        )
        lines.append(f"              Rationale: {criterion.rationale}")
        lines.append("")

    met = sum(1 for c in result.wp248_criteria if c.status == CriterionStatus.MET)
    borderline = sum(
        1 for c in result.wp248_criteria if c.status == CriterionStatus.BORDERLINE
    )
    lines.append(f"  Criteria Met: {met} | Borderline: {borderline} | Threshold: 2")
    lines.append("")

    lines.extend([
        "=" * 70,
        "SCREENING OUTCOME",
        "=" * 70,
        f"  Decision:    {result.outcome.value}",
        f"  Rationale:   {result.rationale}",
        f"  DPO Review:  {'Required' if result.dpo_review_required else 'Not Required'}",
        "=" * 70,
    ])

    return "\n".join(lines)


def run_screening(config: dict) -> str:
    """Execute the full threshold screening process."""
    result = ScreeningResult(
        processing_activity=config.get("processing_activity", "Unknown"),
        controller=config.get("controller", "Unknown"),
        screening_date=config.get(
            "screening_date",
            datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        ),
        screened_by=config.get("screened_by", "DPO"),
    )

    # Phase 1: Mandatory triggers
    result.mandatory_triggers = evaluate_mandatory_triggers(
        config.get("mandatory_triggers", {})
    )

    # Phase 2: Blacklist checks
    for bl in config.get("blacklist_checks", []):
        result.blacklist_checks.append(
            BlacklistCheck(
                supervisory_authority=bl.get("supervisory_authority", ""),
                list_consulted=bl.get("list_consulted", ""),
                match_found=bl.get("match_found", False),
                matched_entry=bl.get("matched_entry"),
            )
        )

    # Phase 3: WP248 criteria
    result.wp248_criteria = evaluate_wp248_criteria(
        config.get("wp248_criteria", [])
    )

    # Determine outcome
    result = determine_outcome(result)

    return generate_report(result)


if __name__ == "__main__":
    sample_config = {
        "processing_activity": "Patient Genomic Profiling Platform",
        "controller": "QuantumLeap Health Technologies",
        "screening_date": "2026-03-14",
        "screened_by": "Dr. Elena Vasquez, DPO",
        "mandatory_triggers": {
            "profiling": {
                "systematic_extensive_evaluation": True,
                "automated_processing": True,
                "legal_or_significant_effects": True,
                "rationale": "Genomic analysis produces health risk scores that directly influence treatment pathways and insurance eligibility recommendations",
            },
            "special_category": {
                "special_category_or_criminal": True,
                "large_scale": True,
                "rationale": "Genetic data (Art. 9(1)) processed for 450,000+ patients across 12 hospital networks",
            },
            "public_monitoring": {
                "systematic_monitoring": False,
                "publicly_accessible": False,
                "large_scale": False,
                "rationale": "Processing occurs within clinical settings, not public areas",
            },
        },
        "blacklist_checks": [
            {
                "supervisory_authority": "BfDI (Germany)",
                "list_consulted": "DSK Muss-Liste (2018, updated 2023)",
                "match_found": True,
                "matched_entry": "Category 8: Processing of genetic or biometric data for unique identification",
            }
        ],
        "wp248_criteria": [
            {"status": "Met", "rationale": "Genomic risk scoring evaluates patient predispositions"},
            {"status": "Met", "rationale": "Automated treatment pathway recommendations based on genomic profile"},
            {"status": "Not Met", "rationale": "No monitoring of public areas"},
            {"status": "Met", "rationale": "Genetic data is special category under Art. 9(1)"},
            {"status": "Met", "rationale": "450,000+ patients across multiple hospital networks"},
            {"status": "Met", "rationale": "Combines genomic data with EHR, lifestyle, and environmental datasets"},
            {"status": "Met", "rationale": "Patients in clinical care are vulnerable data subjects"},
            {"status": "Met", "rationale": "Novel ML-based genomic analysis represents innovative technology"},
            {"status": "Not Met", "rationale": "Patients can opt out without losing access to standard care"},
        ],
    }

    report = run_screening(sample_config)
    print(report)
