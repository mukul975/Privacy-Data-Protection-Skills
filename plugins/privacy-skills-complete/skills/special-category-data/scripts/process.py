"""
Special Category Data Classifier
Identifies Art. 9 GDPR special category data and maps processing conditions.
"""

import re
import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from datetime import date


class SpecialCategory(Enum):
    RACIAL_ETHNIC_ORIGIN = "racial_or_ethnic_origin"
    POLITICAL_OPINIONS = "political_opinions"
    RELIGIOUS_PHILOSOPHICAL = "religious_or_philosophical_beliefs"
    TRADE_UNION = "trade_union_membership"
    GENETIC = "genetic_data"
    BIOMETRIC = "biometric_data"
    HEALTH = "health_data"
    SEX_LIFE_ORIENTATION = "sex_life_or_sexual_orientation"
    NOT_SPECIAL = "not_special_category"


class ProcessingCondition(Enum):
    EXPLICIT_CONSENT = "Art. 9(2)(a) — Explicit consent"
    EMPLOYMENT_LAW = "Art. 9(2)(b) — Employment, social security, social protection law"
    VITAL_INTERESTS = "Art. 9(2)(c) — Vital interests"
    NONPROFIT_LEGITIMATE = "Art. 9(2)(d) — Legitimate activities of non-profit body"
    MANIFESTLY_PUBLIC = "Art. 9(2)(e) — Data manifestly made public"
    LEGAL_CLAIMS = "Art. 9(2)(f) — Legal claims"
    SUBSTANTIAL_PUBLIC_INTEREST = "Art. 9(2)(g) — Substantial public interest"
    HEALTHCARE = "Art. 9(2)(h) — Healthcare and occupational medicine"
    PUBLIC_HEALTH = "Art. 9(2)(i) — Public health"
    ARCHIVING_RESEARCH = "Art. 9(2)(j) — Archiving, research, statistics"
    NONE_IDENTIFIED = "No processing condition identified — PROCESSING PROHIBITED"


CATEGORY_FIELD_PATTERNS: dict[SpecialCategory, list[str]] = {
    SpecialCategory.RACIAL_ETHNIC_ORIGIN: [
        r"(?i)ethnicit", r"(?i)race\b", r"(?i)racial", r"(?i)ethnic",
        r"(?i)national_origin", r"(?i)nationality.*divers",
    ],
    SpecialCategory.POLITICAL_OPINIONS: [
        r"(?i)politic", r"(?i)party_affil", r"(?i)voting",
        r"(?i)political_donat", r"(?i)pac_contrib",
    ],
    SpecialCategory.RELIGIOUS_PHILOSOPHICAL: [
        r"(?i)religio", r"(?i)faith\b", r"(?i)church", r"(?i)mosque",
        r"(?i)synagogue", r"(?i)belief", r"(?i)philosophical",
        r"(?i)halal", r"(?i)kosher", r"(?i)dietary.*relig",
    ],
    SpecialCategory.TRADE_UNION: [
        r"(?i)trade.?union", r"(?i)union_member", r"(?i)union_dues",
        r"(?i)collective.?bargain", r"(?i)labor_union", r"(?i)labour_union",
    ],
    SpecialCategory.GENETIC: [
        r"(?i)genetic", r"(?i)dna\b", r"(?i)genome", r"(?i)genotype",
        r"(?i)allele", r"(?i)snp_", r"(?i)hereditar",
    ],
    SpecialCategory.BIOMETRIC: [
        r"(?i)biometric", r"(?i)fingerprint", r"(?i)iris_scan",
        r"(?i)facial_recogn", r"(?i)voice_print", r"(?i)retina_scan",
        r"(?i)palm_print", r"(?i)faceprint",
    ],
    SpecialCategory.HEALTH: [
        r"(?i)health", r"(?i)medic", r"(?i)diagnos", r"(?i)symptom",
        r"(?i)prescription", r"(?i)allerg", r"(?i)disabilit",
        r"(?i)illness", r"(?i)treatment", r"(?i)vaccine", r"(?i)icd.?10",
        r"(?i)patient", r"(?i)blood_type", r"(?i)sick_leave",
        r"(?i)mental_health", r"(?i)therapy",
    ],
    SpecialCategory.SEX_LIFE_ORIENTATION: [
        r"(?i)sexual_orient", r"(?i)sex_life", r"(?i)gender_identity",
        r"(?i)lgbtq", r"(?i)same.?sex", r"(?i)partner_gender",
    ],
}

ICD10_PATTERN = re.compile(r"^[A-Z]\d{2}(\.\d{1,4})?$")
GENETIC_MARKER_PATTERN = re.compile(r"^rs\d{4,}$")


@dataclass
class FieldClassification:
    field_name: str
    system_name: str
    detected_category: SpecialCategory
    confidence: float
    matched_pattern: str
    processing_condition: ProcessingCondition = ProcessingCondition.NONE_IDENTIFIED
    dpia_required: bool = False
    notes: str = ""


@dataclass
class SpecialCategoryReport:
    organisation: str
    assessment_date: str
    total_fields_scanned: int
    special_category_fields: list[FieldClassification]
    categories_found: dict[str, int]
    dpia_required_count: int
    fields_without_condition: list[str]


class SpecialCategoryClassifier:
    """
    Classifies data fields against GDPR Art. 9 special categories.
    Implements pattern-based detection with manual review flagging.
    """

    def classify_field(
        self,
        field_name: str,
        system_name: str,
        field_description: str = "",
        sample_values: list[str] | None = None,
        purpose_is_unique_identification: bool = False,
    ) -> FieldClassification:
        """
        Classify a single data field against Art. 9 special categories.

        Args:
            field_name: Name of the database field or column
            system_name: System containing the field
            field_description: Human-readable description
            sample_values: Example values for content-based detection
            purpose_is_unique_identification: For biometric data, whether the
                purpose is uniquely identifying a person (Art. 9(1) qualifier)
        """
        text_to_scan = f"{field_name} {field_description}".lower()
        best_match = SpecialCategory.NOT_SPECIAL
        best_confidence = 0.0
        best_pattern = ""

        for category, patterns in CATEGORY_FIELD_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, text_to_scan):
                    confidence = 0.85
                    if category == SpecialCategory.BIOMETRIC and not purpose_is_unique_identification:
                        confidence = 0.4
                    if confidence > best_confidence:
                        best_match = category
                        best_confidence = confidence
                        best_pattern = pattern

        if sample_values and best_match == SpecialCategory.NOT_SPECIAL:
            for value in sample_values:
                if ICD10_PATTERN.match(value.strip()):
                    best_match = SpecialCategory.HEALTH
                    best_confidence = 0.9
                    best_pattern = "ICD-10 code format detected"
                    break
                if GENETIC_MARKER_PATTERN.match(value.strip()):
                    best_match = SpecialCategory.GENETIC
                    best_confidence = 0.9
                    best_pattern = "Genetic marker (rs-number) detected"
                    break

        notes = ""
        if best_match == SpecialCategory.BIOMETRIC and not purpose_is_unique_identification:
            notes = (
                "Biometric data detected but purpose is not unique identification. "
                "Art. 9(1) applies only when processed 'for the purpose of uniquely "
                "identifying a natural person'. Manual review required."
            )

        return FieldClassification(
            field_name=field_name,
            system_name=system_name,
            detected_category=best_match,
            confidence=best_confidence,
            matched_pattern=best_pattern,
            notes=notes,
        )

    def assign_processing_condition(
        self,
        classification: FieldClassification,
        context: str,
    ) -> FieldClassification:
        """
        Assign an Art. 9(2) processing condition based on the processing context.

        Args:
            classification: The field classification result
            context: Processing context keyword (employment, consent, healthcare,
                     legal_claim, public_interest, research, vital_interest)
        """
        condition_map = {
            "consent": ProcessingCondition.EXPLICIT_CONSENT,
            "employment": ProcessingCondition.EMPLOYMENT_LAW,
            "vital_interest": ProcessingCondition.VITAL_INTERESTS,
            "nonprofit": ProcessingCondition.NONPROFIT_LEGITIMATE,
            "public_data": ProcessingCondition.MANIFESTLY_PUBLIC,
            "legal_claim": ProcessingCondition.LEGAL_CLAIMS,
            "public_interest": ProcessingCondition.SUBSTANTIAL_PUBLIC_INTEREST,
            "healthcare": ProcessingCondition.HEALTHCARE,
            "public_health": ProcessingCondition.PUBLIC_HEALTH,
            "research": ProcessingCondition.ARCHIVING_RESEARCH,
        }

        classification.processing_condition = condition_map.get(
            context, ProcessingCondition.NONE_IDENTIFIED
        )
        return classification

    def assess_dpia_requirement(
        self,
        classification: FieldClassification,
        record_count: int,
        geographic_scope: str = "national",
    ) -> FieldClassification:
        """
        Assess whether DPIA is required under Art. 35(3)(b) for large-scale
        special category processing.
        """
        if classification.detected_category == SpecialCategory.NOT_SPECIAL:
            classification.dpia_required = False
            return classification

        large_scale_thresholds = {
            "local": 5000,
            "regional": 2000,
            "national": 1000,
            "international": 500,
        }
        threshold = large_scale_thresholds.get(geographic_scope, 1000)
        classification.dpia_required = record_count >= threshold
        return classification

    def scan_system(
        self,
        system_name: str,
        fields: list[dict],
        processing_context: str = "",
        record_count: int = 0,
    ) -> list[FieldClassification]:
        """
        Scan all fields in a system for special category data.

        Args:
            system_name: Name of the system being scanned
            fields: List of dicts with keys: name, description, sample_values,
                    purpose_is_unique_identification
            processing_context: Context for Art. 9(2) condition assignment
            record_count: Number of records for DPIA scale assessment
        """
        results = []
        for f in fields:
            classification = self.classify_field(
                field_name=f.get("name", ""),
                system_name=system_name,
                field_description=f.get("description", ""),
                sample_values=f.get("sample_values"),
                purpose_is_unique_identification=f.get("purpose_is_unique_identification", False),
            )

            if classification.detected_category != SpecialCategory.NOT_SPECIAL:
                if processing_context:
                    self.assign_processing_condition(classification, processing_context)
                if record_count > 0:
                    self.assess_dpia_requirement(classification, record_count)
                results.append(classification)

        return results

    def generate_report(
        self,
        organisation: str,
        all_classifications: list[FieldClassification],
        total_fields_scanned: int,
    ) -> SpecialCategoryReport:
        """Generate a summary report of special category data findings."""
        categories_found: dict[str, int] = {}
        fields_without_condition = []
        dpia_count = 0

        for c in all_classifications:
            cat = c.detected_category.value
            categories_found[cat] = categories_found.get(cat, 0) + 1
            if c.processing_condition == ProcessingCondition.NONE_IDENTIFIED:
                fields_without_condition.append(f"{c.system_name}.{c.field_name}")
            if c.dpia_required:
                dpia_count += 1

        return SpecialCategoryReport(
            organisation=organisation,
            assessment_date=date.today().isoformat(),
            total_fields_scanned=total_fields_scanned,
            special_category_fields=all_classifications,
            categories_found=categories_found,
            dpia_required_count=dpia_count,
            fields_without_condition=fields_without_condition,
        )


def run_vanguard_example():
    """Demonstrate special category classification for Vanguard Financial Services."""
    classifier = SpecialCategoryClassifier()

    hr_fields = [
        {"name": "employee_ethnicity", "description": "Self-reported ethnicity for diversity monitoring"},
        {"name": "trade_union_dues", "description": "Monthly union dues payroll deduction amount"},
        {"name": "sick_leave_reason", "description": "Reason for sick leave absence"},
        {"name": "disability_accommodation", "description": "Workplace disability accommodation details"},
        {"name": "religious_holiday_request", "description": "Employee request for religious holiday leave"},
        {"name": "sexual_orientation", "description": "Self-reported sexual orientation for diversity survey"},
        {"name": "emergency_contact_name", "description": "Name of emergency contact person"},
        {"name": "salary_amount", "description": "Gross monthly salary"},
    ]

    access_fields = [
        {
            "name": "fingerprint_template",
            "description": "Biometric fingerprint template for building access",
            "purpose_is_unique_identification": True,
        },
        {
            "name": "access_card_id",
            "description": "RFID access card identifier",
        },
        {
            "name": "facial_recognition_embedding",
            "description": "Facial recognition vector for secure area access",
            "purpose_is_unique_identification": True,
        },
    ]

    health_fields = [
        {"name": "diagnosis_code", "description": "ICD-10 diagnosis code", "sample_values": ["J06.9", "M54.5"]},
        {"name": "prescription_medication", "description": "Current prescribed medications"},
        {"name": "genetic_test_result", "description": "Genetic predisposition test outcome from wellness program"},
    ]

    print("=" * 70)
    print("VANGUARD FINANCIAL SERVICES — SPECIAL CATEGORY DATA SCAN")
    print("=" * 70)

    all_results = []

    hr_results = classifier.scan_system("HR_System", hr_fields, "employment", record_count=12000)
    all_results.extend(hr_results)
    print(f"\nHR System: {len(hr_results)} special category fields detected")
    for r in hr_results:
        print(f"  - {r.field_name}: {r.detected_category.value} (confidence: {r.confidence:.0%})")

    access_results = classifier.scan_system("AccessControl", access_fields, "consent", record_count=8500)
    all_results.extend(access_results)
    print(f"\nAccess Control: {len(access_results)} special category fields detected")
    for r in access_results:
        print(f"  - {r.field_name}: {r.detected_category.value} (confidence: {r.confidence:.0%})")
        if r.notes:
            print(f"    Note: {r.notes}")

    health_results = classifier.scan_system("OccHealth", health_fields, "healthcare", record_count=12000)
    all_results.extend(health_results)
    print(f"\nOccupational Health: {len(health_results)} special category fields detected")
    for r in health_results:
        print(f"  - {r.field_name}: {r.detected_category.value} (confidence: {r.confidence:.0%})")

    total_scanned = len(hr_fields) + len(access_fields) + len(health_fields)
    report = classifier.generate_report("Vanguard Financial Services", all_results, total_scanned)

    print(f"\n{'='*70}")
    print("SUMMARY REPORT")
    print(f"{'='*70}")
    print(f"Total fields scanned: {report.total_fields_scanned}")
    print(f"Special category fields found: {len(report.special_category_fields)}")
    print(f"DPIA required for: {report.dpia_required_count} processing activities")
    print(f"\nCategories found:")
    for cat, count in report.categories_found.items():
        print(f"  {cat}: {count}")
    if report.fields_without_condition:
        print(f"\nFIELDS WITHOUT ART. 9(2) CONDITION (action required):")
        for f in report.fields_without_condition:
            print(f"  - {f}")


if __name__ == "__main__":
    run_vanguard_example()
