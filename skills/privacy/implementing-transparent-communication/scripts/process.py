#!/usr/bin/env python3
"""
Transparent Communication Compliance Checker

Evaluates privacy notices and data subject communications against
GDPR Article 12 transparency requirements, including readability
analysis and completeness checks.
"""

import argparse
import json
import re
import math
from datetime import datetime
from typing import Optional


# Art. 13 required elements (direct collection)
ART_13_REQUIRED_ELEMENTS = [
    {"id": "13_1_a", "article": "Art. 13(1)(a)", "element": "Identity and contact details of the controller"},
    {"id": "13_1_b", "article": "Art. 13(1)(b)", "element": "Contact details of the DPO"},
    {"id": "13_1_c", "article": "Art. 13(1)(c)", "element": "Purposes and legal basis for processing"},
    {"id": "13_1_d", "article": "Art. 13(1)(d)", "element": "Legitimate interests pursued (if Art. 6(1)(f) relied upon)"},
    {"id": "13_1_e", "article": "Art. 13(1)(e)", "element": "Recipients or categories of recipients"},
    {"id": "13_1_f", "article": "Art. 13(1)(f)", "element": "International transfers and safeguards"},
    {"id": "13_2_a", "article": "Art. 13(2)(a)", "element": "Retention period or criteria for determining retention"},
    {"id": "13_2_b", "article": "Art. 13(2)(b)", "element": "Right of access, rectification, erasure, restriction, objection, portability"},
    {"id": "13_2_c", "article": "Art. 13(2)(c)", "element": "Right to withdraw consent (if consent is the legal basis)"},
    {"id": "13_2_d", "article": "Art. 13(2)(d)", "element": "Right to lodge a complaint with a supervisory authority"},
    {"id": "13_2_e", "article": "Art. 13(2)(e)", "element": "Whether provision of data is statutory/contractual requirement and consequences of non-provision"},
    {"id": "13_2_f", "article": "Art. 13(2)(f)", "element": "Automated decision-making including profiling (existence, logic, significance, consequences)"},
    {"id": "13_2_g", "article": "Art. 13(2)(g)", "element": "Further processing for a different purpose (information before further processing)"},
]

# Art. 14 required elements (indirect collection)
ART_14_REQUIRED_ELEMENTS = ART_13_REQUIRED_ELEMENTS + [
    {"id": "14_2_f", "article": "Art. 14(2)(f)", "element": "Source of the personal data and whether it came from publicly accessible sources"},
]


def count_syllables(word: str) -> int:
    """Estimate syllable count for a word."""
    word = word.lower().strip()
    if len(word) <= 3:
        return 1

    # Remove trailing 'e'
    if word.endswith("e"):
        word = word[:-1]

    # Count vowel groups
    vowels = "aeiouy"
    count = 0
    prev_vowel = False
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel

    return max(count, 1)


def calculate_readability(text: str) -> dict:
    """
    Calculate Flesch-Kincaid readability metrics for a text.

    Returns Flesch Reading Ease and Flesch-Kincaid Grade Level.
    """
    # Clean text
    text = re.sub(r"[#*|_\-=\[\]\(\)]", " ", text)  # Remove markdown
    text = re.sub(r"\s+", " ", text).strip()

    # Split into sentences
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
    num_sentences = max(len(sentences), 1)

    # Split into words
    words = text.split()
    words = [w for w in words if len(w) > 0 and w[0].isalpha()]
    num_words = max(len(words), 1)

    # Count syllables
    total_syllables = sum(count_syllables(w) for w in words)

    # Flesch Reading Ease
    fre = 206.835 - 1.015 * (num_words / num_sentences) - 84.6 * (total_syllables / num_words)
    fre = max(0, min(100, fre))

    # Flesch-Kincaid Grade Level
    fkgl = 0.39 * (num_words / num_sentences) + 11.8 * (total_syllables / num_words) - 15.59
    fkgl = max(0, fkgl)

    # Interpretation
    if fre >= 60:
        readability = "PASS — Accessible to general public"
    elif fre >= 50:
        readability = "MARGINAL — May be difficult for some readers"
    else:
        readability = "FAIL — Too complex for general public"

    if fkgl <= 8:
        grade_assessment = "PASS — At or below 8th grade level"
    elif fkgl <= 10:
        grade_assessment = "MARGINAL — Consider simplifying"
    else:
        grade_assessment = "FAIL — Exceeds recommended reading level"

    return {
        "word_count": num_words,
        "sentence_count": num_sentences,
        "syllable_count": total_syllables,
        "avg_words_per_sentence": round(num_words / num_sentences, 1),
        "avg_syllables_per_word": round(total_syllables / num_words, 2),
        "flesch_reading_ease": round(fre, 1),
        "flesch_reading_ease_assessment": readability,
        "flesch_kincaid_grade_level": round(fkgl, 1),
        "grade_level_assessment": grade_assessment,
    }


def check_completeness(
    notice_text: str,
    collection_type: str = "direct",
) -> dict:
    """
    Check a privacy notice for completeness against Art. 13 or Art. 14 requirements.

    Args:
        notice_text: The text of the privacy notice.
        collection_type: 'direct' for Art. 13 or 'indirect' for Art. 14.
    """
    elements = ART_13_REQUIRED_ELEMENTS if collection_type == "direct" else ART_14_REQUIRED_ELEMENTS
    text_lower = notice_text.lower()

    results = []
    found_count = 0

    # Keyword-based detection (simplified — production would use NLP)
    element_keywords = {
        "13_1_a": ["controller", "data controller", "company name", "registered"],
        "13_1_b": ["data protection officer", "dpo", "dpo@"],
        "13_1_c": ["purpose", "legal basis", "lawful basis", "we process"],
        "13_1_d": ["legitimate interest", "art. 6(1)(f)", "article 6"],
        "13_1_e": ["recipient", "share", "disclose", "third part"],
        "13_1_f": ["transfer", "international", "outside", "third countr", "adequacy", "standard contractual"],
        "13_2_a": ["retention", "retain", "keep", "storage period", "delete"],
        "13_2_b": ["right to access", "right to rectif", "right to erasure", "right to restrict", "right to object", "right to portab", "your rights"],
        "13_2_c": ["withdraw consent", "withdraw your consent"],
        "13_2_d": ["supervisory authority", "complaint", "ico", "information commissioner"],
        "13_2_e": ["statutory", "contractual", "obligat", "required to provide", "consequence"],
        "13_2_f": ["automated", "profiling", "automated decision"],
        "13_2_g": ["further processing", "different purpose", "new purpose"],
        "14_2_f": ["source", "obtained from", "publicly accessible"],
    }

    for element in elements:
        keywords = element_keywords.get(element["id"], [])
        found = any(kw in text_lower for kw in keywords)
        if found:
            found_count += 1
        results.append({
            "article": element["article"],
            "element": element["element"],
            "detected": found,
            "status": "FOUND" if found else "MISSING",
        })

    total = len(elements)
    completeness = (found_count / total * 100) if total > 0 else 0

    return {
        "collection_type": collection_type,
        "article": "Art. 13" if collection_type == "direct" else "Art. 14",
        "total_elements": total,
        "elements_found": found_count,
        "elements_missing": total - found_count,
        "completeness_percentage": round(completeness, 1),
        "overall_status": "PASS" if completeness >= 90 else "NEEDS_REVIEW" if completeness >= 70 else "FAIL",
        "elements": results,
    }


def assess_response_timeline(
    request_date: str,
    response_date: str,
    extension_notified: bool = False,
    extension_date: Optional[str] = None,
) -> dict:
    """Assess whether a response was delivered within Art. 12(3) timelines."""
    req = datetime.strptime(request_date, "%Y-%m-%d")
    resp = datetime.strptime(response_date, "%Y-%m-%d")
    days_taken = (resp - req).days
    standard_deadline = 30

    assessment = {
        "request_date": request_date,
        "response_date": response_date,
        "days_taken": days_taken,
        "standard_deadline_days": standard_deadline,
    }

    if days_taken <= standard_deadline:
        assessment["status"] = "COMPLIANT"
        assessment["note"] = f"Response delivered in {days_taken} days (within 30-day deadline)"
    elif extension_notified and days_taken <= 90:
        assessment["status"] = "COMPLIANT_WITH_EXTENSION"
        assessment["note"] = f"Response delivered in {days_taken} days with valid extension"
    elif days_taken <= 90 and not extension_notified:
        assessment["status"] = "NON_COMPLIANT"
        assessment["note"] = f"Response took {days_taken} days — extension was not notified within 30 days as required by Art. 12(3)"
    else:
        assessment["status"] = "NON_COMPLIANT"
        assessment["note"] = f"Response took {days_taken} days — exceeds maximum 90-day extended deadline"

    return assessment


def main():
    parser = argparse.ArgumentParser(
        description="GDPR Art. 12 transparent communication compliance tools"
    )
    subparsers = parser.add_subparsers(dest="command")

    read_p = subparsers.add_parser("readability", help="Check readability of text")
    read_p.add_argument("--file", required=True, help="Path to text file to analyse")

    comp_p = subparsers.add_parser("completeness", help="Check privacy notice completeness")
    comp_p.add_argument("--file", required=True, help="Path to privacy notice file")
    comp_p.add_argument("--type", choices=["direct", "indirect"], default="direct", help="Collection type")

    time_p = subparsers.add_parser("timeline", help="Assess response timeline compliance")
    time_p.add_argument("--request-date", required=True, help="YYYY-MM-DD")
    time_p.add_argument("--response-date", required=True, help="YYYY-MM-DD")
    time_p.add_argument("--extension-notified", action="store_true")

    args = parser.parse_args()

    if args.command == "readability":
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
        result = calculate_readability(text)
    elif args.command == "completeness":
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
        result = check_completeness(text, args.type)
    elif args.command == "timeline":
        result = assess_response_timeline(
            request_date=args.request_date,
            response_date=args.response_date,
            extension_notified=args.extension_notified,
        )
    else:
        parser.print_help()
        return

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
