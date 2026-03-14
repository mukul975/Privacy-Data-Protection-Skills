"""
PII Detection Pipeline — Detection and Redaction Engine

Pattern-based PII detection for common entity types.
Designed to complement Microsoft Presidio and spaCy NER
in production pipelines.
"""

import re
from dataclasses import dataclass
from typing import Optional
import json


@dataclass
class Detection:
    entity_type: str
    text: str
    start: int
    end: int
    score: float
    source: str


class PatternDetector:
    """
    Rule-based PII detection using regex patterns.
    Used as a baseline and as custom recognizers in Presidio.
    """

    PATTERNS = {
        "EMAIL_ADDRESS": {
            "regex": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "score": 0.95,
        },
        "PHONE_US": {
            "regex": r"\b(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}\b",
            "score": 0.75,
        },
        "SSN_US": {
            "regex": r"\b(?!000|666|9\d{2})\d{3}[-\s]?(?!00)\d{2}[-\s]?(?!0000)\d{4}\b",
            "score": 0.90,
        },
        "CREDIT_CARD": {
            "regex": r"\b(?:4\d{3}|5[1-5]\d{2}|3[47]\d{2}|6(?:011|5\d{2}))[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",
            "score": 0.90,
        },
        "IP_ADDRESS_V4": {
            "regex": r"\b(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b",
            "score": 0.85,
        },
        "IBAN": {
            "regex": r"\b[A-Z]{2}\d{2}[A-Z0-9]{4}\d{7}(?:[A-Z0-9]?){0,16}\b",
            "score": 0.85,
        },
        "UK_NINO": {
            "regex": r"\b[A-CEGHJ-PR-TW-Z]{2}\s?\d{2}\s?\d{2}\s?\d{2}\s?[A-D]\b",
            "score": 0.85,
        },
        "DATE_OF_BIRTH": {
            "regex": r"\b(?:DOB|Date of Birth|born|birthday)[\s:]*\d{1,2}[/\-\.]\d{1,2}[/\-\.]\d{2,4}\b",
            "score": 0.80,
        },
        "EMPLOYEE_ID_CEL": {
            "regex": r"\bCEL-\d{5}\b",
            "score": 0.95,
        },
    }

    def detect(self, text: str, entities: list[str] = None) -> list[Detection]:
        """
        Detect PII entities in text using regex patterns.

        Args:
            text: Input text to scan
            entities: Entity types to detect (all if None)
        """
        detections = []
        patterns_to_use = self.PATTERNS

        if entities:
            patterns_to_use = {k: v for k, v in self.PATTERNS.items() if k in entities}

        for entity_type, config in patterns_to_use.items():
            for match in re.finditer(config["regex"], text, re.IGNORECASE):
                detections.append(Detection(
                    entity_type=entity_type,
                    text=match.group(),
                    start=match.start(),
                    end=match.end(),
                    score=config["score"],
                    source="pattern_detector",
                ))

        return sorted(detections, key=lambda d: d.start)


class TextRedactor:
    """Redact detected PII from text."""

    STRATEGIES = {
        "replace": lambda entity_type, text: f"<{entity_type}>",
        "mask": lambda entity_type, text: "*" * len(text),
        "hash": lambda entity_type, text: f"[HASH:{hash(text) % 10**8:08d}]",
        "redact": lambda entity_type, text: "[REDACTED]",
    }

    def __init__(self, strategy: str = "replace"):
        self.strategy_fn = self.STRATEGIES.get(strategy, self.STRATEGIES["replace"])

    def redact(self, text: str, detections: list[Detection], min_score: float = 0.5) -> str:
        """Apply redaction to detected PII entities."""
        filtered = [d for d in detections if d.score >= min_score]
        filtered.sort(key=lambda d: d.start, reverse=True)

        result = text
        for det in filtered:
            replacement = self.strategy_fn(det.entity_type, det.text)
            result = result[:det.start] + replacement + result[det.end:]

        return result


class PIIScanner:
    """High-level PII scanning interface combining detection and redaction."""

    def __init__(self, strategy: str = "replace", min_score: float = 0.5):
        self.detector = PatternDetector()
        self.redactor = TextRedactor(strategy)
        self.min_score = min_score

    def scan(self, text: str) -> dict:
        """Scan text for PII and return detection summary."""
        detections = self.detector.detect(text)
        filtered = [d for d in detections if d.score >= self.min_score]

        entity_counts = {}
        for d in filtered:
            entity_counts[d.entity_type] = entity_counts.get(d.entity_type, 0) + 1

        return {
            "total_detections": len(filtered),
            "entity_counts": entity_counts,
            "detections": [
                {
                    "type": d.entity_type,
                    "text": d.text[:4] + "..." if len(d.text) > 4 else d.text,
                    "position": [d.start, d.end],
                    "score": d.score,
                }
                for d in filtered
            ],
            "risk_level": (
                "critical" if any(d.entity_type in ("SSN_US", "CREDIT_CARD") for d in filtered)
                else "high" if len(filtered) > 5
                else "medium" if len(filtered) > 0
                else "low"
            ),
        }

    def scan_and_redact(self, text: str) -> tuple[str, dict]:
        """Scan and redact PII, return redacted text and summary."""
        detections = self.detector.detect(text)
        redacted = self.redactor.redact(text, detections, self.min_score)
        summary = self.scan(text)
        return redacted, summary


if __name__ == "__main__":
    scanner = PIIScanner(strategy="replace", min_score=0.5)

    sample_text = """
    Customer: John Smith (CEL-00142)
    Email: john.smith@cipherengineeringlabs.com
    Phone: +1 (555) 012-3456
    SSN: 123-45-6789
    Card: 4111-1111-1111-1111
    IP: 192.168.1.100
    DOB: 01/15/1990
    """

    redacted, summary = scanner.scan_and_redact(sample_text)
    print("=== Detection Summary ===")
    print(json.dumps(summary, indent=2))
    print("\n=== Redacted Text ===")
    print(redacted)
