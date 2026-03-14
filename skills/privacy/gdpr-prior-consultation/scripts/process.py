#!/usr/bin/env python3
"""
Prior Consultation Readiness Assessment

Evaluates whether prior consultation under Art. 36 is required based on
DPIA findings and residual risk levels, and validates submission completeness.
"""

import json
import sys
from datetime import datetime, timedelta


ART_36_3_REQUIREMENTS = [
    "responsibilities_documented",
    "purposes_and_means_described",
    "safeguards_documented",
    "dpo_contact_provided",
    "dpia_completed",
]


def assess_prior_consultation_need(dpia_summary: dict) -> dict:
    result = {
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "prior_consultation_required": False,
        "rationale": "",
        "steps": [],
    }

    dpia_conducted = dpia_summary.get("dpia_conducted", False)
    if not dpia_conducted:
        result["rationale"] = "No DPIA conducted. Prior consultation not triggered."
        result["steps"].append({"step": "DPIA conducted?", "answer": "No", "outcome": "Not required"})
        return result

    result["steps"].append({"step": "DPIA conducted?", "answer": "Yes", "outcome": "Continue"})

    high_risk_identified = dpia_summary.get("high_risk_identified", False)
    if not high_risk_identified:
        result["rationale"] = "DPIA did not identify high risks. Prior consultation not required."
        result["steps"].append({"step": "High risks identified?", "answer": "No", "outcome": "Not required"})
        return result

    result["steps"].append({"step": "High risks identified?", "answer": "Yes", "outcome": "Continue"})

    all_measures_applied = dpia_summary.get("all_mitigation_measures_applied", False)
    if not all_measures_applied:
        result["rationale"] = "Not all available mitigation measures have been applied. Apply measures before considering prior consultation."
        result["steps"].append({"step": "All measures applied?", "answer": "No", "outcome": "Apply measures first"})
        return result

    result["steps"].append({"step": "All measures applied?", "answer": "Yes", "outcome": "Continue"})

    residual_risk_high = dpia_summary.get("residual_risk_remains_high", False)
    if not residual_risk_high:
        result["rationale"] = "Residual risk has been reduced to acceptable level. Prior consultation not required. Proceed with processing."
        result["steps"].append({"step": "Residual risk still high?", "answer": "No", "outcome": "Not required"})
        return result

    result["prior_consultation_required"] = True
    result["rationale"] = "DPIA identifies high residual risk despite all available mitigation. Prior consultation with the supervisory authority is REQUIRED under Art. 36(1)."
    result["steps"].append({"step": "Residual risk still high?", "answer": "Yes", "outcome": "REQUIRED"})

    return result


def validate_submission(submission: dict) -> dict:
    findings = []
    for req in ART_36_3_REQUIREMENTS:
        if not submission.get(req, False):
            findings.append({
                "requirement": req,
                "article": "Art. 36(3)",
                "status": "Missing",
            })

    submission_date = submission.get("submission_date")
    timeline = {}
    if submission_date:
        sub_dt = datetime.strptime(submission_date, "%Y-%m-%d")
        timeline = {
            "submission_date": submission_date,
            "initial_deadline": (sub_dt + timedelta(weeks=8)).strftime("%Y-%m-%d"),
            "extended_deadline": (sub_dt + timedelta(weeks=14)).strftime("%Y-%m-%d"),
        }

    return {
        "submission_complete": len(findings) == 0,
        "missing_requirements": findings,
        "timeline": timeline,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <dpia_summary.json>")
        example = {
            "processing_activity": "Biometric access control system",
            "dpia_conducted": True,
            "high_risk_identified": True,
            "all_mitigation_measures_applied": True,
            "residual_risk_remains_high": True,
            "submission": {
                "responsibilities_documented": True,
                "purposes_and_means_described": True,
                "safeguards_documented": True,
                "dpo_contact_provided": True,
                "dpia_completed": True,
                "submission_date": "2026-02-15",
            },
        }
        print(json.dumps(example, indent=2))
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = json.load(f)

    need_assessment = assess_prior_consultation_need(data)
    result = {"need_assessment": need_assessment}

    if need_assessment["prior_consultation_required"]:
        submission = data.get("submission", {})
        result["submission_validation"] = validate_submission(submission)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
