"""
Automated PII Discovery and Classification Framework
Orchestrates scanning across data sources and consolidates findings.
"""

import re
import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from datetime import datetime, date


class DiscoveryPlatform(Enum):
    PURVIEW = "Microsoft Purview"
    BIGID = "BigID"
    ONETRUST = "OneTrust DataDiscovery"
    MACIE = "AWS Macie"
    CUSTOM = "Custom Scanner"


class DataSourceType(Enum):
    RELATIONAL_DB = "relational_database"
    NOSQL_DB = "nosql_database"
    FILE_SHARE = "file_share"
    CLOUD_STORAGE = "cloud_storage"
    SAAS_APP = "saas_application"
    EMAIL = "email_system"
    COLLABORATION = "collaboration_platform"


class ScanType(Enum):
    FULL = "full_scan"
    INCREMENTAL = "incremental_scan"
    ON_DEMAND = "on_demand_scan"
    TARGETED = "targeted_scan"


class ConfidenceLevel(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class PIICategory(Enum):
    DIRECT_IDENTIFIER = "direct_identifier"
    INDIRECT_IDENTIFIER = "indirect_identifier"
    SPECIAL_CATEGORY = "special_category_art9"
    CRIMINAL_DATA = "criminal_data_art10"
    FINANCIAL = "financial_data"
    LOCATION = "location_data"
    ONLINE_IDENTIFIER = "online_identifier"
    PSEUDONYMISED = "pseudonymised"


@dataclass
class SensitiveInfoType:
    """A pattern-based classifier for detecting PII in data."""
    name: str
    category: PIICategory
    pattern: str
    keywords: list[str] = field(default_factory=list)
    negative_keywords: list[str] = field(default_factory=list)
    confidence_boost_keywords: list[str] = field(default_factory=list)
    base_confidence: float = 0.75
    checksum_validator: Optional[str] = None


@dataclass
class DiscoveryFinding:
    """A single PII discovery finding."""
    finding_id: str
    data_source: str
    source_type: DataSourceType
    location: str
    field_or_path: str
    sit_name: str
    category: PIICategory
    confidence: ConfidenceLevel
    confidence_score: float
    sample_count: int
    first_detected: str
    scan_type: ScanType
    platform: DiscoveryPlatform
    auto_label_applied: str = ""
    reviewed: bool = False
    false_positive: bool = False


@dataclass
class ScanJob:
    """A scanning job configuration and result summary."""
    job_id: str
    platform: DiscoveryPlatform
    scan_type: ScanType
    sources_scanned: int
    records_scanned: int
    findings_count: int
    start_time: str
    end_time: str
    status: str
    errors: list[str] = field(default_factory=list)


@dataclass
class AccuracyMetrics:
    """Accuracy measurement for a scan cycle."""
    measurement_date: str
    sample_size: int
    true_positives: int
    false_positives: int
    true_negatives: int
    false_negatives: int

    @property
    def precision(self) -> float:
        denom = self.true_positives + self.false_positives
        return self.true_positives / denom if denom > 0 else 0.0

    @property
    def recall(self) -> float:
        denom = self.true_positives + self.false_negatives
        return self.true_positives / denom if denom > 0 else 0.0

    @property
    def f1_score(self) -> float:
        p, r = self.precision, self.recall
        return 2 * p * r / (p + r) if (p + r) > 0 else 0.0

    @property
    def false_positive_rate(self) -> float:
        denom = self.false_positives + self.true_negatives
        return self.false_positives / denom if denom > 0 else 0.0


VANGUARD_SIT_LIBRARY: list[SensitiveInfoType] = [
    SensitiveInfoType(
        name="UK National Insurance Number",
        category=PIICategory.DIRECT_IDENTIFIER,
        pattern=r"[A-CEGHJ-PR-TW-Z]{2}\d{6}[A-D]",
        keywords=["national insurance", "ni number", "nino"],
        negative_keywords=["phone", "tel", "fax", "mobile", "reference"],
        base_confidence=0.85,
    ),
    SensitiveInfoType(
        name="IBAN",
        category=PIICategory.FINANCIAL,
        pattern=r"[A-Z]{2}\d{2}[A-Z0-9]{4}\d{7}([A-Z0-9]?){0,16}",
        keywords=["iban", "bank account", "account number"],
        base_confidence=0.80,
    ),
    SensitiveInfoType(
        name="Email Address",
        category=PIICategory.DIRECT_IDENTIFIER,
        pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        keywords=["email", "e-mail", "contact"],
        base_confidence=0.90,
    ),
    SensitiveInfoType(
        name="UK Passport Number",
        category=PIICategory.DIRECT_IDENTIFIER,
        pattern=r"\d{9}",
        keywords=["passport", "travel document"],
        confidence_boost_keywords=["passport number", "passport no"],
        base_confidence=0.60,
    ),
    SensitiveInfoType(
        name="Vanguard Customer Account",
        category=PIICategory.INDIRECT_IDENTIFIER,
        pattern=r"VFS-\d{10}",
        keywords=["customer", "account", "client"],
        base_confidence=0.95,
    ),
    SensitiveInfoType(
        name="Vanguard Employee ID",
        category=PIICategory.INDIRECT_IDENTIFIER,
        pattern=r"EMP-[A-Z]{2}\d{6}",
        keywords=["employee", "staff", "worker"],
        base_confidence=0.95,
    ),
    SensitiveInfoType(
        name="ICD-10 Diagnosis Code",
        category=PIICategory.SPECIAL_CATEGORY,
        pattern=r"[A-Z]\d{2}\.\d{1,4}",
        keywords=["diagnosis", "icd", "medical", "health"],
        base_confidence=0.80,
    ),
    SensitiveInfoType(
        name="IP Address",
        category=PIICategory.ONLINE_IDENTIFIER,
        pattern=r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        keywords=["ip", "address", "network", "connection"],
        negative_keywords=["version", "subnet", "mask", "gateway"],
        base_confidence=0.65,
    ),
    SensitiveInfoType(
        name="Credit Card Number",
        category=PIICategory.FINANCIAL,
        pattern=r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
        keywords=["card", "credit", "debit", "payment", "visa", "mastercard"],
        base_confidence=0.85,
        checksum_validator="luhn",
    ),
    SensitiveInfoType(
        name="Genetic Marker (rs-number)",
        category=PIICategory.SPECIAL_CATEGORY,
        pattern=r"\brs\d{4,12}\b",
        keywords=["genetic", "snp", "variant", "genome"],
        base_confidence=0.90,
    ),
]


class PIIScanner:
    """
    Pattern-based PII scanner implementing the discovery engine logic.
    Simulates the scanning approach used by enterprise discovery platforms.
    """

    def __init__(self, sit_library: list[SensitiveInfoType] | None = None):
        self.sit_library = sit_library or VANGUARD_SIT_LIBRARY
        self._compiled_patterns = {
            sit.name: re.compile(sit.pattern) for sit in self.sit_library
        }

    def scan_text(self, text: str, source_context: str = "") -> list[dict]:
        """
        Scan a text block for PII matches using the SIT library.

        Args:
            text: The text content to scan
            source_context: Additional context (field name, file path) for confidence adjustment

        Returns:
            List of match dicts with sit_name, category, confidence, match_count
        """
        findings = []
        combined = f"{source_context} {text}".lower()

        for sit in self.sit_library:
            pattern = self._compiled_patterns[sit.name]
            matches = pattern.findall(text)

            if not matches:
                continue

            confidence = sit.base_confidence

            keyword_found = any(kw in combined for kw in sit.keywords)
            if keyword_found:
                confidence = min(confidence + 0.10, 1.0)

            boost_found = any(kw in combined for kw in sit.confidence_boost_keywords)
            if boost_found:
                confidence = min(confidence + 0.15, 1.0)

            negative_found = any(kw in combined for kw in sit.negative_keywords)
            if negative_found:
                confidence = max(confidence - 0.25, 0.1)

            if sit.checksum_validator == "luhn":
                validated = [m for m in matches if self._luhn_check(m)]
                matches = validated
                if validated:
                    confidence = min(confidence + 0.10, 1.0)

            if matches:
                if confidence >= 0.85:
                    level = ConfidenceLevel.HIGH
                elif confidence >= 0.70:
                    level = ConfidenceLevel.MEDIUM
                else:
                    level = ConfidenceLevel.LOW

                findings.append({
                    "sit_name": sit.name,
                    "category": sit.category.value,
                    "confidence_score": round(confidence, 2),
                    "confidence_level": level.value,
                    "match_count": len(matches),
                })

        return findings

    @staticmethod
    def _luhn_check(card_number: str) -> bool:
        """Validate a number using the Luhn algorithm."""
        digits = [int(d) for d in card_number if d.isdigit()]
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

    def scan_structured_record(
        self, record: dict, source_name: str
    ) -> list[dict]:
        """
        Scan a structured data record (dict of field_name: value).

        Args:
            record: Dictionary of field names to values
            source_name: Name of the data source

        Returns:
            List of findings with field context
        """
        all_findings = []
        for field_name, value in record.items():
            if value is None:
                continue
            text = str(value)
            findings = self.scan_text(text, source_context=field_name)
            for f in findings:
                f["field_name"] = field_name
                f["source"] = source_name
            all_findings.extend(findings)
        return all_findings


class DiscoveryOrchestrator:
    """
    Orchestrates scanning across multiple data sources and consolidates results.
    """

    def __init__(self):
        self.scanner = PIIScanner()
        self.findings: list[DiscoveryFinding] = []
        self.scan_jobs: list[ScanJob] = []

    def create_scan_job(
        self,
        platform: DiscoveryPlatform,
        scan_type: ScanType,
        sources: list[str],
    ) -> ScanJob:
        """Create and track a scan job."""
        job = ScanJob(
            job_id=f"SCAN-{date.today().strftime('%Y%m%d')}-{len(self.scan_jobs)+1:03d}",
            platform=platform,
            scan_type=scan_type,
            sources_scanned=len(sources),
            records_scanned=0,
            findings_count=0,
            start_time=datetime.now().isoformat(),
            end_time="",
            status="running",
        )
        self.scan_jobs.append(job)
        return job

    def measure_accuracy(
        self,
        verified_findings: list[dict],
    ) -> AccuracyMetrics:
        """
        Measure scan accuracy based on manually verified findings.

        Args:
            verified_findings: List of dicts with keys:
                - classified_as_pii (bool): scanner classified as PII
                - actually_pii (bool): manual verification result
        """
        tp = sum(1 for f in verified_findings if f["classified_as_pii"] and f["actually_pii"])
        fp = sum(1 for f in verified_findings if f["classified_as_pii"] and not f["actually_pii"])
        tn = sum(1 for f in verified_findings if not f["classified_as_pii"] and not f["actually_pii"])
        fn = sum(1 for f in verified_findings if not f["classified_as_pii"] and f["actually_pii"])

        return AccuracyMetrics(
            measurement_date=date.today().isoformat(),
            sample_size=len(verified_findings),
            true_positives=tp,
            false_positives=fp,
            true_negatives=tn,
            false_negatives=fn,
        )

    def generate_discovery_report(self) -> dict:
        """Generate consolidated discovery report."""
        categories = {}
        sources = {}
        high_conf = 0
        medium_conf = 0

        for f in self.findings:
            cat = f.category.value
            categories[cat] = categories.get(cat, 0) + 1
            sources[f.data_source] = sources.get(f.data_source, 0) + 1
            if f.confidence == ConfidenceLevel.HIGH:
                high_conf += 1
            elif f.confidence == ConfidenceLevel.MEDIUM:
                medium_conf += 1

        return {
            "report_date": date.today().isoformat(),
            "total_findings": len(self.findings),
            "high_confidence": high_conf,
            "medium_confidence": medium_conf,
            "findings_by_category": categories,
            "findings_by_source": sources,
            "scan_jobs_completed": len(self.scan_jobs),
        }


def run_vanguard_example():
    """Demonstrate PII scanning for Vanguard Financial Services."""
    scanner = PIIScanner()

    sample_records = [
        {
            "customer_name": "Elizabeth Thornton",
            "email": "e.thornton@personal-mail.co.uk",
            "account_number": "VFS-2847593012",
            "national_insurance": "AB123456C",
            "iban": "GB29NWBK60161331926819",
            "notes": "Customer requested portfolio review. IP: 192.168.1.105",
        },
        {
            "employee_id": "EMP-LN004821",
            "department": "Trading Floor",
            "health_record": "Diagnosis code J06.9 — Upper respiratory infection",
            "card_on_file": "4532-0151-2847-3920",
        },
        {
            "data_field": "Average daily temperature readings for London office",
            "sensor_id": "HVAC-BLDG3-FL7",
            "value": "21.5C",
        },
    ]

    print("=" * 70)
    print("VANGUARD FINANCIAL SERVICES — PII DISCOVERY SCAN")
    print("=" * 70)

    for i, record in enumerate(sample_records, 1):
        print(f"\n--- Record {i} ---")
        findings = scanner.scan_structured_record(record, f"CRM_Record_{i}")
        if findings:
            for f in findings:
                print(f"  [{f['confidence_level'].upper()}] {f['sit_name']} "
                      f"in field '{f['field_name']}' "
                      f"(confidence: {f['confidence_score']:.0%}, "
                      f"matches: {f['match_count']})")
        else:
            print("  No PII detected")

    print(f"\n{'='*70}")
    print("ACCURACY MEASUREMENT")
    print("=" * 70)

    orchestrator = DiscoveryOrchestrator()
    verified = [
        {"classified_as_pii": True, "actually_pii": True},
        {"classified_as_pii": True, "actually_pii": True},
        {"classified_as_pii": True, "actually_pii": False},
        {"classified_as_pii": True, "actually_pii": True},
        {"classified_as_pii": False, "actually_pii": False},
        {"classified_as_pii": False, "actually_pii": True},
        {"classified_as_pii": True, "actually_pii": True},
        {"classified_as_pii": True, "actually_pii": True},
        {"classified_as_pii": False, "actually_pii": False},
        {"classified_as_pii": True, "actually_pii": True},
    ]
    metrics = orchestrator.measure_accuracy(verified)
    print(f"  Precision: {metrics.precision:.0%}")
    print(f"  Recall: {metrics.recall:.0%}")
    print(f"  F1 Score: {metrics.f1_score:.2f}")
    print(f"  False Positive Rate: {metrics.false_positive_rate:.0%}")


if __name__ == "__main__":
    run_vanguard_example()
