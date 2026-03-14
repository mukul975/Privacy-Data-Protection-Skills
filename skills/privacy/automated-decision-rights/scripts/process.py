#!/usr/bin/env python3
"""
Automated Decision-Making and Profiling Rights Manager

Assesses whether processing activities trigger GDPR Article 22,
manages contestation requests, and generates logic explanations.
"""

import argparse
import json
from datetime import datetime, timedelta
from typing import Optional


def assess_art22_applicability(
    processing_name: str,
    solely_automated: bool,
    human_intervention_quality: str,
    legal_effect: bool,
    significant_effect: bool,
    exception_basis: Optional[str] = None,
) -> dict:
    """
    Assess whether a processing activity triggers Art. 22.

    Args:
        processing_name: Name of the processing activity.
        solely_automated: Whether the decision is made without human intervention.
        human_intervention_quality: One of 'none', 'rubber_stamp', 'genuine'.
        legal_effect: Whether the decision produces legal effects.
        significant_effect: Whether the decision similarly significantly affects the subject.
        exception_basis: If Art. 22(2) exception applies: 'contract', 'law', or 'consent'.
    """
    assessment = {
        "processing_activity": processing_name,
        "assessment_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "solely_automated": False,
        "legal_or_significant_effect": False,
        "art_22_applies": False,
        "exception_applies": False,
        "safeguards_required": False,
        "reasoning": [],
    }

    # Step 1: Is the decision solely automated?
    if solely_automated or human_intervention_quality in ("none", "rubber_stamp"):
        assessment["solely_automated"] = True
        if human_intervention_quality == "rubber_stamp":
            assessment["reasoning"].append(
                "Human involvement classified as rubber-stamping per WP251 rev.01 "
                "paragraph 21 — reviewer lacks authority, competence, or does not "
                "genuinely consider the automated output."
            )
        else:
            assessment["reasoning"].append(
                "No human intervention in the decision process."
            )
    else:
        assessment["solely_automated"] = False
        assessment["reasoning"].append(
            "Genuine human intervention exists — reviewer has authority, competence, "
            "and genuinely considers the automated output before deciding."
        )
        assessment["art_22_applies"] = False
        assessment["recommendation"] = (
            "Art. 22 does not apply as the decision is not solely automated. "
            "General GDPR principles (Art. 5, 6) still apply to the processing."
        )
        return assessment

    # Step 2: Legal or significant effect?
    if legal_effect:
        assessment["legal_or_significant_effect"] = True
        assessment["effect_type"] = "legal"
        assessment["reasoning"].append(
            "Decision produces legal effects concerning the data subject."
        )
    elif significant_effect:
        assessment["legal_or_significant_effect"] = True
        assessment["effect_type"] = "similarly_significant"
        assessment["reasoning"].append(
            "Decision similarly significantly affects the data subject "
            "(material impact on circumstances, behaviour, or choices)."
        )
    else:
        assessment["legal_or_significant_effect"] = False
        assessment["reasoning"].append(
            "Decision does not produce legal effects or similarly significant effects."
        )
        assessment["art_22_applies"] = False
        assessment["recommendation"] = (
            "Art. 22 does not apply as the decision does not produce legal or "
            "similarly significant effects. Consider whether Art. 5(1)(a) fairness "
            "and transparency obligations still require safeguards."
        )
        return assessment

    # Step 3: Art. 22 applies
    assessment["art_22_applies"] = True

    # Step 4: Check for exceptions
    if exception_basis == "contract":
        assessment["exception_applies"] = True
        assessment["exception"] = {
            "article": "Art. 22(2)(a)",
            "basis": "Necessary for entering into or performance of a contract",
        }
    elif exception_basis == "law":
        assessment["exception_applies"] = True
        assessment["exception"] = {
            "article": "Art. 22(2)(b)",
            "basis": "Authorised by Union or Member State law with suitable safeguards",
        }
    elif exception_basis == "consent":
        assessment["exception_applies"] = True
        assessment["exception"] = {
            "article": "Art. 22(2)(c)",
            "basis": "Based on the data subject's explicit consent",
        }

    if assessment["exception_applies"]:
        assessment["safeguards_required"] = True
        assessment["required_safeguards"] = [
            "Right to obtain human intervention (Art. 22(3))",
            "Right to express their point of view (Art. 22(3))",
            "Right to contest the decision (Art. 22(3))",
            "Meaningful information about the logic involved (Art. 15(1)(h))",
            "Information about significance and envisaged consequences (Art. 15(1)(h))",
        ]
        assessment["recommendation"] = (
            f"Art. 22 applies but exception under {assessment['exception']['article']} is available. "
            f"Implement all required safeguards under Art. 22(3)."
        )
    else:
        assessment["safeguards_required"] = True
        assessment["recommendation"] = (
            "Art. 22(1) prohibition applies. The decision CANNOT be made solely by "
            "automated means. Implement meaningful human intervention in the "
            "decision process, or obtain explicit consent, or establish that the "
            "decision is necessary for a contract."
        )

    return assessment


def generate_logic_explanation(
    decision_name: str,
    input_factors: list,
    thresholds: dict,
    accuracy_rate: float,
    false_positive_rate: float,
    false_negative_rate: float,
    last_validation_date: str,
    possible_outcomes: list,
) -> dict:
    """Generate a plain-language Art. 15(1)(h) logic explanation."""
    explanation = {
        "decision_name": decision_name,
        "generated_date": datetime.utcnow().strftime("%Y-%m-%d"),
        "existence_confirmation": (
            f"Meridian Analytics Ltd uses an automated system to make decisions "
            f"regarding {decision_name}."
        ),
        "input_factors": [],
        "decision_logic": {},
        "accuracy_information": {},
        "significance_and_consequences": [],
    }

    for factor in input_factors:
        explanation["input_factors"].append({
            "name": factor["name"],
            "description": factor["description"],
            "approximate_weight": factor.get("weight", "not disclosed"),
        })

    explanation["decision_logic"] = {
        "method": "The system combines the input factors listed above using a weighted scoring model.",
        "thresholds": thresholds,
        "note": (
            "This is a functional description of the decision logic. "
            "The exact algorithm weights and source code are proprietary, "
            "but the above provides meaningful information about how the "
            "decision is reached, as required by Art. 15(1)(h)."
        ),
    }

    explanation["accuracy_information"] = {
        "overall_accuracy": f"{accuracy_rate:.1f}%",
        "false_positive_rate": f"{false_positive_rate:.1f}%",
        "false_negative_rate": f"{false_negative_rate:.1f}%",
        "last_validation": last_validation_date,
    }

    explanation["significance_and_consequences"] = possible_outcomes

    explanation["data_subject_rights"] = [
        "You have the right to request human intervention in this decision.",
        "You have the right to express your point of view regarding this decision.",
        "You have the right to contest this decision.",
        "To exercise these rights, contact dpo@meridiananalytics.co.uk referencing your decision.",
    ]

    return explanation


def process_contestation(
    decision_reference: str,
    data_subject_id: str,
    contestation_date: str,
    grounds: str,
    original_decision: str,
) -> dict:
    """Create a contestation record for an automated decision."""
    cont_date = datetime.strptime(contestation_date, "%Y-%m-%d")
    response_deadline = cont_date + timedelta(days=30)

    reference = f"ADM-{cont_date.strftime('%Y')}-{cont_date.strftime('%m%d')}"

    return {
        "contestation_reference": reference,
        "decision_reference": decision_reference,
        "data_subject_id": data_subject_id,
        "contestation_date": contestation_date,
        "response_deadline": response_deadline.strftime("%Y-%m-%d"),
        "original_decision": original_decision,
        "data_subject_grounds": grounds,
        "status": "pending_review",
        "reviewer_requirements": {
            "independence": "Must not have been involved in original automated decision",
            "authority": "Must have authority to override the decision",
            "competence": "Must have relevant domain expertise and understanding of the model",
        },
        "review_steps": [
            "1. Review the automated decision, its inputs, and its output",
            "2. Review the data subject's contestation grounds and any supporting evidence",
            "3. Consider the data subject's specific circumstances",
            "4. Analyse model behaviour for this specific case (input sensitivity, edge cases)",
            "5. Reach an independent decision: uphold, modify, or overturn",
            "6. Document reasoning in full",
            "7. Notify data subject of outcome within response deadline",
        ],
        "possible_outcomes": ["UPHOLD", "MODIFY", "OVERTURN"],
    }


def main():
    parser = argparse.ArgumentParser(
        description="Manage GDPR Art. 22 automated decision-making rights"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Assess command
    assess_p = subparsers.add_parser("assess", help="Assess Art. 22 applicability")
    assess_p.add_argument("--name", required=True, help="Processing activity name")
    assess_p.add_argument("--solely-automated", action="store_true")
    assess_p.add_argument(
        "--human-quality",
        choices=["none", "rubber_stamp", "genuine"],
        default="none",
    )
    assess_p.add_argument("--legal-effect", action="store_true")
    assess_p.add_argument("--significant-effect", action="store_true")
    assess_p.add_argument(
        "--exception", choices=["contract", "law", "consent"], default=None
    )

    # Contestation command
    contest_p = subparsers.add_parser("contest", help="Process a contestation")
    contest_p.add_argument("--decision-ref", required=True)
    contest_p.add_argument("--subject-id", required=True)
    contest_p.add_argument("--date", required=True)
    contest_p.add_argument("--grounds", required=True)
    contest_p.add_argument("--original-decision", required=True)

    args = parser.parse_args()

    if args.command == "assess":
        result = assess_art22_applicability(
            processing_name=args.name,
            solely_automated=args.solely_automated,
            human_intervention_quality=args.human_quality,
            legal_effect=args.legal_effect,
            significant_effect=args.significant_effect,
            exception_basis=args.exception,
        )
    elif args.command == "contest":
        result = process_contestation(
            decision_reference=args.decision_ref,
            data_subject_id=args.subject_id,
            contestation_date=args.date,
            grounds=args.grounds,
            original_decision=args.original_decision,
        )
    else:
        parser.print_help()
        return

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
