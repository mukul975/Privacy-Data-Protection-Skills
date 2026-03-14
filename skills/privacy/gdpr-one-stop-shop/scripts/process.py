#!/usr/bin/env python3
"""
Lead Supervisory Authority Determination Tool

Determines the lead supervisory authority under Art. 56 based on
the controller/processor establishment locations and processing activities.
"""

import json
import sys
from datetime import datetime


def determine_lead_authority(input_data: dict) -> dict:
    entity_type = input_data.get("entity_type", "controller")
    establishments = input_data.get("establishments", [])
    central_admin = input_data.get("central_administration", "")
    decision_making_location = input_data.get("decision_making_location", "")

    result = {
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "entity_type": entity_type,
        "establishments": establishments,
        "lead_authority": None,
        "main_establishment": None,
        "rationale": "",
        "concerned_authorities": [],
    }

    if not establishments:
        result["rationale"] = "No EU establishments identified. One-stop-shop does not apply."
        return result

    if len(establishments) == 1:
        est = establishments[0]
        result["main_establishment"] = est["country"]
        result["lead_authority"] = est.get("supervisory_authority", f"DPA of {est['country']}")
        result["rationale"] = f"Single establishment in {est['country']}. Lead authority is the DPA of that Member State."
        return result

    if entity_type == "controller":
        if decision_making_location and decision_making_location != central_admin:
            main_est = decision_making_location
            result["rationale"] = (
                f"Decisions on purposes and means of processing are taken at "
                f"{decision_making_location}, which differs from central administration "
                f"({central_admin}). Per Art. 4(16)(a), the decision-making location "
                f"is the main establishment."
            )
        elif central_admin:
            main_est = central_admin
            result["rationale"] = (
                f"Central administration is at {central_admin} and processing decisions "
                f"are taken there. This is the main establishment per Art. 4(16)(a)."
            )
        else:
            main_est = establishments[0]["country"]
            result["rationale"] = "Could not determine main establishment. Defaulting to first listed establishment."
    else:
        if central_admin:
            main_est = central_admin
            result["rationale"] = f"Processor central administration at {central_admin} is the main establishment per Art. 4(16)(b)."
        else:
            main_est = establishments[0]["country"]
            result["rationale"] = "Processor has no central administration in the EU. Main establishment is where main processing activities occur."

    result["main_establishment"] = main_est

    for est in establishments:
        if est["country"] == main_est:
            result["lead_authority"] = est.get("supervisory_authority", f"DPA of {main_est}")
        else:
            result["concerned_authorities"].append(est.get("supervisory_authority", f"DPA of {est['country']}"))

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <establishment_data.json>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        input_data = json.load(f)

    result = determine_lead_authority(input_data)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
