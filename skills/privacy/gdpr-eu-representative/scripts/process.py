#!/usr/bin/env python3
"""
EU Representative Requirement Assessment

Determines whether a non-EU controller/processor must appoint an
EU representative under Art. 27, and validates appointment documentation.
"""

import json
import sys
from datetime import datetime


def assess_requirement(input_data: dict) -> dict:
    result = {
        "assessment_date": datetime.now().strftime("%Y-%m-%d"),
        "entity_name": input_data.get("entity_name", ""),
        "established_in_eu": input_data.get("established_in_eu", False),
        "representative_required": False,
        "rationale": "",
        "exemption_applies": False,
    }

    if input_data.get("established_in_eu", False):
        result["rationale"] = "Entity is established in the EU. Art. 27 does not apply."
        return result

    art_3_2_applies = input_data.get("art_3_2_applies", False)
    if not art_3_2_applies:
        result["rationale"] = "GDPR does not apply to this entity under Art. 3(2). No representative required."
        return result

    is_public_authority = input_data.get("is_public_authority", False)
    if is_public_authority:
        result["exemption_applies"] = True
        result["rationale"] = "Entity is a public authority. Exempt under Art. 27(2)(b)."
        return result

    processing_occasional = input_data.get("processing_occasional", False)
    no_large_scale_special = input_data.get("no_large_scale_special_category", True)
    unlikely_risk = input_data.get("unlikely_to_result_in_risk", True)

    if processing_occasional and no_large_scale_special and unlikely_risk:
        result["exemption_applies"] = True
        result["rationale"] = (
            "Processing is occasional, does not include large-scale special category data, "
            "and is unlikely to result in risk. Exempt under Art. 27(2)(a)."
        )
        return result

    result["representative_required"] = True
    result["rationale"] = (
        "Entity is not established in the EU, GDPR applies under Art. 3(2), "
        "and no Art. 27(2) exemption applies. An EU representative MUST be appointed."
    )

    member_states = input_data.get("affected_member_states", [])
    if member_states:
        result["recommended_location"] = member_states[0]
        result["note"] = f"Representative should be established in {member_states[0]} where affected data subjects are located."

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python process.py <entity_data.json>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        input_data = json.load(f)

    result = assess_requirement(input_data)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
