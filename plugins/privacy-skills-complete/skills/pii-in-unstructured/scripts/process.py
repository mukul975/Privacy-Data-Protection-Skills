"""
PII Detection in Unstructured Data
NER-based and pattern-based PII detection engine using spaCy and regex patterns.
"""

import re
import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from datetime import date


class PIIType(Enum):
    PERSON_NAME = "person_name"
    EMAIL = "email_address"
    PHONE = "phone_number"
    NINO = "uk_national_insurance_number"
    IBAN = "iban"
    CREDIT_CARD = "credit_card_number"
    IP_ADDRESS = "ip_address"
    DATE_OF_BIRTH = "date_of_birth"
    ADDRESS = "postal_address"
    ACCOUNT_NUMBER = "account_number"
    EMPLOYEE_ID = "employee_id"
    PASSPORT = "passport_number"
    HEALTH_CODE = "health_icd10_code"
    GENERIC_PII = "generic_pii"


class ConfidenceLevel(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    BELOW_THRESHOLD = "below_threshold"


@dataclass
class PIIDetection:
    """A single PII detection result."""
    pii_type: PIIType
    value_masked: str
    start_position: int
    end_position: int
    confidence_score: float
    confidence_level: ConfidenceLevel
    detection_method: str
    context_snippet: str
    source_document: str = ""
    notes: str = ""


@dataclass
class DocumentScanResult:
    """Complete scan result for a single document."""
    document_id: str
    document_name: str
    document_type: str
    source_system: str
    text_length: int
    scan_date: str
    detections: list[PIIDetection] = field(default_factory=list)
    pii_types_found: list[str] = field(default_factory=list)
    highest_sensitivity: str = ""
    ocr_applied: bool = False
    ocr_confidence: float = 0.0


class PatternRecogniser:
    """Regex-based pattern recogniser for PII types."""

    PATTERNS: dict[PIIType, dict] = {
        PIIType.EMAIL: {
            "pattern": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            "base_confidence": 0.90,
            "boost_keywords": ["email", "e-mail", "contact", "address"],
            "negative_keywords": ["example.com", "test.com", "placeholder"],
        },
        PIIType.NINO: {
            "pattern": r"\b[A-CEGHJ-PR-TW-Z]{2}\d{6}[A-D]\b",
            "base_confidence": 0.85,
            "boost_keywords": ["national insurance", "ni number", "nino", "ni no"],
            "negative_keywords": ["phone", "tel", "ref", "order"],
        },
        PIIType.PHONE: {
            "pattern": r"\b(?:0|\+44)\s?\d{4}\s?\d{6}\b",
            "base_confidence": 0.75,
            "boost_keywords": ["phone", "tel", "mobile", "call", "contact"],
            "negative_keywords": ["fax", "switchboard"],
        },
        PIIType.IBAN: {
            "pattern": r"\b[A-Z]{2}\d{2}[A-Z0-9]{4}\d{7}([A-Z0-9]{0,16})\b",
            "base_confidence": 0.80,
            "boost_keywords": ["iban", "bank", "account", "transfer"],
            "negative_keywords": [],
        },
        PIIType.CREDIT_CARD: {
            "pattern": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
            "base_confidence": 0.70,
            "boost_keywords": ["card", "credit", "debit", "visa", "mastercard", "payment"],
            "negative_keywords": ["reference", "tracking", "order number"],
            "validator": "luhn",
        },
        PIIType.IP_ADDRESS: {
            "pattern": r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b",
            "base_confidence": 0.65,
            "boost_keywords": ["ip", "address", "connection", "logged in from"],
            "negative_keywords": ["version", "subnet", "mask", "gateway", "dns"],
        },
        PIIType.DATE_OF_BIRTH: {
            "pattern": r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",
            "base_confidence": 0.50,
            "boost_keywords": ["born", "dob", "date of birth", "birthday", "age"],
            "negative_keywords": ["created", "modified", "expires", "effective", "invoice"],
        },
        PIIType.ACCOUNT_NUMBER: {
            "pattern": r"\bVFS-\d{10}\b",
            "base_confidence": 0.95,
            "boost_keywords": ["account", "customer", "client"],
            "negative_keywords": [],
        },
        PIIType.EMPLOYEE_ID: {
            "pattern": r"\bEMP-[A-Z]{2}\d{6}\b",
            "base_confidence": 0.95,
            "boost_keywords": ["employee", "staff", "worker"],
            "negative_keywords": [],
        },
        PIIType.HEALTH_CODE: {
            "pattern": r"\b[A-Z]\d{2}\.\d{1,4}\b",
            "base_confidence": 0.75,
            "boost_keywords": ["diagnosis", "icd", "medical", "health", "condition"],
            "negative_keywords": ["version", "section", "clause", "article"],
        },
    }

    @staticmethod
    def _luhn_check(number: str) -> bool:
        digits = [int(d) for d in number if d.isdigit()]
        if len(digits) < 13 or len(digits) > 19:
            return False
        checksum = 0
        for i, d in enumerate(reversed(digits)):
            if i % 2 == 1:
                d *= 2
                if d > 9:
                    d -= 9
            checksum += d
        return checksum % 10 == 0

    def detect(self, text: str, context: str = "") -> list[PIIDetection]:
        """Run all pattern recognisers against text."""
        detections = []
        combined_lower = f"{context} {text}".lower()

        for pii_type, config in self.PATTERNS.items():
            pattern = re.compile(config["pattern"])
            for match in pattern.finditer(text):
                confidence = config["base_confidence"]

                # Boost for keyword proximity
                match_start = max(0, match.start() - 100)
                match_end = min(len(text), match.end() + 100)
                nearby_text = text[match_start:match_end].lower()

                if any(kw in nearby_text for kw in config.get("boost_keywords", [])):
                    confidence = min(confidence + 0.12, 1.0)

                if any(kw in nearby_text for kw in config.get("negative_keywords", [])):
                    confidence = max(confidence - 0.25, 0.1)

                # Luhn validation for credit cards
                if config.get("validator") == "luhn":
                    if not self._luhn_check(match.group()):
                        continue
                    confidence = min(confidence + 0.10, 1.0)

                # Determine confidence level
                if confidence >= 0.85:
                    level = ConfidenceLevel.HIGH
                elif confidence >= 0.70:
                    level = ConfidenceLevel.MEDIUM
                elif confidence >= 0.50:
                    level = ConfidenceLevel.LOW
                else:
                    level = ConfidenceLevel.BELOW_THRESHOLD

                # Mask the detected value
                raw_value = match.group()
                if len(raw_value) > 4:
                    masked = raw_value[:2] + "*" * (len(raw_value) - 4) + raw_value[-2:]
                else:
                    masked = "*" * len(raw_value)

                # Extract context snippet
                snippet_start = max(0, match.start() - 30)
                snippet_end = min(len(text), match.end() + 30)
                snippet = text[snippet_start:snippet_end].replace("\n", " ")

                detections.append(PIIDetection(
                    pii_type=pii_type,
                    value_masked=masked,
                    start_position=match.start(),
                    end_position=match.end(),
                    confidence_score=round(confidence, 2),
                    confidence_level=level,
                    detection_method="pattern_regex",
                    context_snippet=f"...{snippet}...",
                ))

        return detections


class NameRecogniser:
    """
    Simple name detection using common name patterns.
    In production, use spaCy NER model (en_core_web_trf) for PERSON entities.
    """

    NAME_INDICATORS = [
        r"\b(?:Mr|Mrs|Ms|Miss|Dr|Prof)\.\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+",
        r"\bDear\s+[A-Z][a-z]+",
        r"\bName:\s*[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+",
        r"\bPatient:\s*[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+",
        r"\bCustomer:\s*[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+",
        r"\bEmployee:\s*[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+",
    ]

    def detect(self, text: str) -> list[PIIDetection]:
        detections = []
        for pattern_str in self.NAME_INDICATORS:
            pattern = re.compile(pattern_str)
            for match in pattern.finditer(text):
                raw = match.group()
                masked = raw[:3] + "*" * max(0, len(raw) - 5) + raw[-2:] if len(raw) > 5 else "***"

                snippet_start = max(0, match.start() - 20)
                snippet_end = min(len(text), match.end() + 20)
                snippet = text[snippet_start:snippet_end].replace("\n", " ")

                detections.append(PIIDetection(
                    pii_type=PIIType.PERSON_NAME,
                    value_masked=masked,
                    start_position=match.start(),
                    end_position=match.end(),
                    confidence_score=0.80,
                    confidence_level=ConfidenceLevel.MEDIUM,
                    detection_method="name_pattern",
                    context_snippet=f"...{snippet}...",
                ))
        return detections


class UnstructuredPIIScanner:
    """
    Orchestrates PII detection across unstructured text using multiple recognisers.
    """

    def __init__(self):
        self.pattern_recogniser = PatternRecogniser()
        self.name_recogniser = NameRecogniser()

    def scan_document(
        self,
        text: str,
        document_id: str,
        document_name: str,
        document_type: str,
        source_system: str,
        context: str = "",
        ocr_applied: bool = False,
        ocr_confidence: float = 1.0,
    ) -> DocumentScanResult:
        """Scan a document for PII."""
        all_detections = []

        pattern_detections = self.pattern_recogniser.detect(text, context)
        all_detections.extend(pattern_detections)

        name_detections = self.name_recogniser.detect(text)
        all_detections.extend(name_detections)

        # Adjust confidence for OCR quality
        if ocr_applied and ocr_confidence < 0.80:
            for d in all_detections:
                d.confidence_score = max(d.confidence_score - 0.20, 0.1)
                if d.confidence_score < 0.50:
                    d.confidence_level = ConfidenceLevel.BELOW_THRESHOLD
                elif d.confidence_score < 0.70:
                    d.confidence_level = ConfidenceLevel.LOW
                elif d.confidence_score < 0.85:
                    d.confidence_level = ConfidenceLevel.MEDIUM

        # Set source document
        for d in all_detections:
            d.source_document = document_name

        # Filter below-threshold detections
        filtered = [d for d in all_detections if d.confidence_level != ConfidenceLevel.BELOW_THRESHOLD]

        pii_types = list(set(d.pii_type.value for d in filtered))
        special_cat_types = {PIIType.HEALTH_CODE.value}
        has_special = any(t in special_cat_types for t in pii_types)
        sensitivity = "Restricted" if has_special else ("Confidential" if pii_types else "Internal")

        return DocumentScanResult(
            document_id=document_id,
            document_name=document_name,
            document_type=document_type,
            source_system=source_system,
            text_length=len(text),
            scan_date=date.today().isoformat(),
            detections=filtered,
            pii_types_found=pii_types,
            highest_sensitivity=sensitivity,
            ocr_applied=ocr_applied,
            ocr_confidence=ocr_confidence,
        )


def run_vanguard_example():
    """Demonstrate PII detection on sample unstructured documents."""
    scanner = UnstructuredPIIScanner()

    email_text = """
    From: sarah.jones@vanguardfs.co.uk
    To: customer.service@vanguardfs.co.uk
    Subject: Re: Account Query - VFS-2847593012

    Dear Mr. Thompson,

    Thank you for contacting Vanguard Financial Services regarding your account
    VFS-2847593012. I can confirm that the recent transaction of GBP 15,420.00
    was processed on 12/03/2026.

    For your records, your National Insurance number AB123456C has been verified
    against HMRC records. Please contact us on +44 7700 900123 if you need
    further assistance.

    Your IBAN GB29NWBK60161331926819 has been updated in our system.

    Best regards,
    Sarah Jones
    Customer Service Team
    """

    log_text = """
    2026-03-14 10:23:45 INFO [AuthService] User login: IP=192.168.1.105, UserAgent=Mozilla/5.0
    2026-03-14 10:23:46 INFO [AuthService] Session created for employee EMP-LN004821
    2026-03-14 10:24:12 ERROR [PaymentService] Transaction failed for customer t.wilson@email.co.uk
    2026-03-14 10:24:15 WARN [AMLService] Suspicious pattern detected for VFS-9182736450
    """

    medical_text = """
    Occupational Health Assessment
    Employee: Dr. Rebecca Foster
    Date: 14/03/2026

    Diagnosis: J06.9 - Acute upper respiratory infection, unspecified
    Secondary: M54.5 - Low back pain

    Recommendation: Fit for work with adjustments. Ergonomic assessment required.
    Review date: 14/04/2026
    """

    print("=" * 70)
    print("VANGUARD FINANCIAL SERVICES — UNSTRUCTURED PII SCAN")
    print("=" * 70)

    documents = [
        ("DOC-001", "customer_email_thompson.eml", "email", "Exchange Online", email_text, False),
        ("DOC-002", "auth_service.log", "log_file", "Application Logs", log_text, False),
        ("DOC-003", "occ_health_foster.pdf", "medical_document", "Cority OH System", medical_text, True),
    ]

    for doc_id, doc_name, doc_type, source, text, ocr in documents:
        result = scanner.scan_document(
            text=text,
            document_id=doc_id,
            document_name=doc_name,
            document_type=doc_type,
            source_system=source,
            ocr_applied=ocr,
            ocr_confidence=0.95 if ocr else 1.0,
        )

        print(f"\n--- {result.document_name} ({result.source_system}) ---")
        print(f"    Sensitivity: {result.highest_sensitivity}")
        print(f"    PII types found: {', '.join(result.pii_types_found)}")
        print(f"    Detections: {len(result.detections)}")
        for d in result.detections:
            print(f"      [{d.confidence_level.value.upper():6s}] {d.pii_type.value}: "
                  f"{d.value_masked} (conf: {d.confidence_score:.0%})")


if __name__ == "__main__":
    run_vanguard_example()
