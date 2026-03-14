#!/usr/bin/env python3
"""
Children's Privacy Notice Readability Analyzer

Analyzes privacy notice text for readability metrics and compliance with
age-appropriate communication requirements under GDPR Art. 12, UK AADC
Standard 4, and COPPA Section 312.4.
"""

import re
import json
from datetime import datetime, timezone

READABILITY_TARGETS = {
    "under_8": {"fk_grade": 1.0, "fre": 90, "fog": 3, "avg_sentence": 6},
    "8_11": {"fk_grade": 4.0, "fre": 80, "fog": 6, "avg_sentence": 10},
    "12_15": {"fk_grade": 8.0, "fre": 60, "fog": 10, "avg_sentence": 15},
    "16_17": {"fk_grade": 10.0, "fre": 50, "fog": 12, "avg_sentence": 18},
    "parent": {"fk_grade": 12.0, "fre": 40, "fog": 14, "avg_sentence": 22},
}

ART_13_ELEMENTS = [
    {"id": "13_1_a", "element": "Controller identity and contact details", "required": True},
    {"id": "13_1_b", "element": "DPO contact details", "required": True},
    {"id": "13_1_c", "element": "Purposes and lawful basis", "required": True},
    {"id": "13_1_d", "element": "Legitimate interests (if applicable)", "required": False},
    {"id": "13_1_e", "element": "Recipients or categories of recipients", "required": True},
    {"id": "13_1_f", "element": "International transfers and safeguards", "required": True},
    {"id": "13_2_a", "element": "Retention period or criteria", "required": True},
    {"id": "13_2_b", "element": "Data subject rights", "required": True},
    {"id": "13_2_c", "element": "Right to withdraw consent", "required": True},
    {"id": "13_2_d", "element": "Right to lodge complaint with SA", "required": True},
    {"id": "13_2_e", "element": "Statutory/contractual requirement", "required": True},
    {"id": "13_2_f", "element": "Automated decision-making/profiling", "required": True},
]


def count_syllables(word: str) -> int:
    """Estimate syllable count for an English word."""
    word = word.lower().strip()
    if len(word) <= 3:
        return 1
    word = re.sub(r"(?:es|ed|e)$", "", word) or word
    vowel_groups = re.findall(r"[aeiouy]+", word)
    count = len(vowel_groups)
    return max(count, 1)


def analyze_readability(text: str) -> dict:
    """
    Analyze text readability using Flesch-Kincaid and related metrics.

    Returns readability metrics and compliance assessment for each age tier.
    """
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    words = re.findall(r"\b[a-zA-Z]+\b", text)

    if not sentences or not words:
        return {"error": "Insufficient text for analysis"}

    num_sentences = len(sentences)
    num_words = len(words)
    num_syllables = sum(count_syllables(w) for w in words)
    complex_words = [w for w in words if count_syllables(w) >= 3]
    num_complex = len(complex_words)

    avg_sentence_length = num_words / num_sentences
    avg_syllables_per_word = num_syllables / num_words

    # Flesch-Kincaid Grade Level
    fk_grade = 0.39 * avg_sentence_length + 11.8 * avg_syllables_per_word - 15.59

    # Flesch Reading Ease
    fre = 206.835 - 1.015 * avg_sentence_length - 84.6 * avg_syllables_per_word

    # Gunning Fog Index
    fog = 0.4 * (avg_sentence_length + 100 * (num_complex / num_words))

    # Passive voice estimation (simplified)
    passive_patterns = len(re.findall(
        r"\b(?:is|are|was|were|been|being)\s+\w+ed\b", text, re.IGNORECASE
    ))
    passive_pct = (passive_patterns / num_sentences * 100) if num_sentences > 0 else 0

    metrics = {
        "word_count": num_words,
        "sentence_count": num_sentences,
        "avg_sentence_length": round(avg_sentence_length, 1),
        "avg_syllables_per_word": round(avg_syllables_per_word, 2),
        "flesch_kincaid_grade": round(max(fk_grade, 0), 1),
        "flesch_reading_ease": round(min(max(fre, 0), 100), 1),
        "gunning_fog_index": round(fog, 1),
        "complex_word_count": num_complex,
        "complex_word_percentage": round(num_complex / num_words * 100, 1),
        "estimated_passive_voice_pct": round(passive_pct, 1),
    }

    tier_compliance = {}
    for tier, targets in READABILITY_TARGETS.items():
        passes = {
            "fk_grade": metrics["flesch_kincaid_grade"] <= targets["fk_grade"],
            "fre": metrics["flesch_reading_ease"] >= targets["fre"],
            "fog": metrics["gunning_fog_index"] <= targets["fog"],
            "avg_sentence": metrics["avg_sentence_length"] <= targets["avg_sentence"],
        }
        tier_compliance[tier] = {
            "targets": targets,
            "results": passes,
            "compliant": all(passes.values()),
        }

    return {
        "metrics": metrics,
        "tier_compliance": tier_compliance,
        "analysis_date": datetime.now(timezone.utc).isoformat(),
    }


def audit_art13_completeness(elements_present: dict[str, bool]) -> dict:
    """
    Audit whether all Art. 13 elements are present in the privacy notice.

    Args:
        elements_present: Dict mapping element ID to presence (True/False).

    Returns:
        Completeness audit result.
    """
    results = []
    missing_required = []
    missing_optional = []

    for element in ART_13_ELEMENTS:
        eid = element["id"]
        present = elements_present.get(eid, False)
        results.append({
            "id": eid,
            "element": element["element"],
            "required": element["required"],
            "present": present,
        })
        if not present:
            if element["required"]:
                missing_required.append(element["element"])
            else:
                missing_optional.append(element["element"])

    total = len(ART_13_ELEMENTS)
    present_count = sum(1 for r in results if r["present"])

    return {
        "total_elements": total,
        "present": present_count,
        "missing_required": missing_required,
        "missing_optional": missing_optional,
        "compliant": len(missing_required) == 0,
        "completeness_pct": round(present_count / total * 100, 1),
        "results": results,
    }


if __name__ == "__main__":
    print("=== Privacy Notice Readability Analysis ===")

    child_notice = (
        "When you play our games, we remember your name and which games you like. "
        "We use this to show you new games you might enjoy. "
        "Only you and your parent can see your game scores. "
        "If you want us to forget about you, your parent can ask us. "
        "We keep your information safe and do not share it with anyone else."
    )

    result = analyze_readability(child_notice)
    print(f"\nMetrics:")
    for key, value in result["metrics"].items():
        print(f"  {key}: {value}")

    print(f"\nTier Compliance:")
    for tier, data in result["tier_compliance"].items():
        status = "PASS" if data["compliant"] else "FAIL"
        print(f"  {tier}: {status}")

    print("\n=== Art. 13 Completeness Audit ===")
    elements = {
        "13_1_a": True, "13_1_b": True, "13_1_c": True,
        "13_1_d": False, "13_1_e": True, "13_1_f": True,
        "13_2_a": True, "13_2_b": True, "13_2_c": True,
        "13_2_d": True, "13_2_e": True, "13_2_f": True,
    }

    audit = audit_art13_completeness(elements)
    print(f"Completeness: {audit['completeness_pct']}%")
    print(f"Compliant: {audit['compliant']}")
    if audit["missing_required"]:
        print(f"Missing required: {', '.join(audit['missing_required'])}")
