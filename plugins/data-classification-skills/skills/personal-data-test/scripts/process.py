"""
Personal Data Classification Test Engine
Implements GDPR Art. 4(1) four-element test with Breyer ruling assessment.
"""

import json
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Optional
from datetime import datetime, date


class ClassificationResult(Enum):
    PERSONAL_DIRECT = "PERSONAL_DIRECT"
    PERSONAL_INDIRECT = "PERSONAL_INDIRECT"
    SPECIAL_CATEGORY = "SPECIAL_CATEGORY"
    PSEUDONYMISED = "PSEUDONYMISED"
    ANONYMISED = "ANONYMISED"
    NON_PERSONAL = "NON_PERSONAL"
    BORDERLINE_REVIEW = "BORDERLINE_REVIEW"


class IdentifiabilityLevel(Enum):
    DIRECTLY_IDENTIFIED = "directly_identified"
    INDIRECTLY_IDENTIFIABLE = "indirectly_identifiable"
    NOT_IDENTIFIABLE = "not_identifiable"
    UNCERTAIN = "uncertain"


class RelatingToElement(Enum):
    CONTENT_LINK = "content_link"
    PURPOSE_LINK = "purpose_link"
    RESULT_LINK = "result_link"
    NO_LINK = "no_link"


@dataclass
class BreyerAssessment:
    """Assessment under CJEU C-582/14 Breyer ruling for indirect identifiers."""
    complementary_data_holders: list[str] = field(default_factory=list)
    legal_means_available: bool = False
    legal_means_description: str = ""
    identification_cost: str = ""
    identification_time: str = ""
    technology_required: str = ""
    proportionate_effort: bool = True
    motivation_exists: bool = False
    conclusion: str = ""

    def is_personal_data(self) -> bool:
        return self.legal_means_available and self.proportionate_effort


@dataclass
class FourElementTest:
    """GDPR Art. 4(1) four-element test for personal data classification."""
    data_element_name: str
    data_element_description: str
    system_name: str

    # Element 1: Any information
    is_information: bool = True
    information_format: str = ""

    # Element 2: Relating to a natural person
    relating_to: RelatingToElement = RelatingToElement.NO_LINK
    relating_to_reasoning: str = ""

    # Element 3: Identified or identifiable
    identifiability: IdentifiabilityLevel = IdentifiabilityLevel.UNCERTAIN
    identifiability_reasoning: str = ""
    breyer_assessment: Optional[BreyerAssessment] = None

    # Element 4: Natural person
    is_natural_person: bool = False
    natural_person_notes: str = ""

    def all_elements_satisfied(self) -> bool:
        return (
            self.is_information
            and self.relating_to != RelatingToElement.NO_LINK
            and self.identifiability in (
                IdentifiabilityLevel.DIRECTLY_IDENTIFIED,
                IdentifiabilityLevel.INDIRECTLY_IDENTIFIABLE,
            )
            and self.is_natural_person
        )

    def classify(self) -> ClassificationResult:
        if not self.is_information:
            return ClassificationResult.NON_PERSONAL
        if not self.is_natural_person:
            return ClassificationResult.NON_PERSONAL
        if self.relating_to == RelatingToElement.NO_LINK:
            return ClassificationResult.NON_PERSONAL
        if self.identifiability == IdentifiabilityLevel.DIRECTLY_IDENTIFIED:
            return ClassificationResult.PERSONAL_DIRECT
        if self.identifiability == IdentifiabilityLevel.INDIRECTLY_IDENTIFIABLE:
            return ClassificationResult.PERSONAL_INDIRECT
        if self.identifiability == IdentifiabilityLevel.UNCERTAIN:
            return ClassificationResult.BORDERLINE_REVIEW
        return ClassificationResult.NON_PERSONAL


@dataclass
class DataElementClassification:
    """Complete classification record for a data element."""
    element_id: str
    element_name: str
    system_name: str
    data_source: str
    four_element_test: FourElementTest
    classification: ClassificationResult
    lawful_basis_article_6: str = ""
    article_9_condition: str = ""
    assessor: str = ""
    assessment_date: str = ""
    review_date: str = ""
    reasoning_summary: str = ""


class PersonalDataClassifier:
    """
    Implements the GDPR Art. 4(1) personal data classification decision tree.
    Incorporates Breyer v Germany (C-582/14) relative identifiability standard.
    """

    DIRECT_IDENTIFIERS = {
        "full_name", "first_name_last_name", "national_id",
        "social_security_number", "passport_number", "drivers_license",
        "email_personal", "photograph_face", "biometric_fingerprint",
        "biometric_iris", "biometric_voice", "genetic_data",
        "bank_account_with_name", "tax_identification_number",
    }

    INDIRECT_IDENTIFIERS = {
        "ip_address_dynamic", "ip_address_static", "cookie_identifier",
        "device_fingerprint", "advertising_id", "mac_address",
        "employee_id", "customer_id", "pseudonymised_token",
        "location_data_gps", "browsing_history", "purchase_history",
        "vehicle_registration", "telephone_number",
    }

    SPECIAL_CATEGORY_INDICATORS = {
        "racial_ethnic_origin", "political_opinion", "religious_belief",
        "philosophical_belief", "trade_union_membership", "genetic_data",
        "biometric_for_identification", "health_data", "sex_life",
        "sexual_orientation",
    }

    NON_PERSONAL_TYPES = {
        "weather_data", "stock_price", "machine_sensor",
        "aggregated_census", "chemical_property", "company_financials",
        "product_specification", "software_version",
    }

    def classify_element(
        self,
        element_name: str,
        element_type: str,
        system_name: str,
        data_source: str,
        relates_to_person: bool,
        is_living_person: bool,
        controller_holds_complementary_data: bool = False,
        third_party_legal_means: bool = False,
        publicly_combinable: bool = False,
        identification_cost_proportionate: bool = True,
    ) -> DataElementClassification:
        """
        Classify a data element using the Art. 4(1) four-element test.

        Args:
            element_name: Human-readable name of the data element
            element_type: Category key matching internal identifier sets
            system_name: Name of the system where the data resides
            data_source: How the data was obtained
            relates_to_person: Whether the data has content/purpose/result link to a person
            is_living_person: Whether the data subject is a living natural person
            controller_holds_complementary_data: Whether the controller holds linking data
            third_party_legal_means: Whether legal means to access third-party data exist (Breyer)
            publicly_combinable: Whether public data can be combined for identification
            identification_cost_proportionate: Whether identification effort is proportionate

        Returns:
            DataElementClassification with full assessment record
        """
        four_element = FourElementTest(
            data_element_name=element_name,
            data_element_description=f"Data element '{element_name}' of type '{element_type}' in system '{system_name}'",
            system_name=system_name,
            is_information=True,
            information_format=element_type,
        )

        # Element 2: Relating to
        if relates_to_person:
            four_element.relating_to = RelatingToElement.CONTENT_LINK
            four_element.relating_to_reasoning = (
                f"Data element '{element_name}' has a content link to a natural person"
            )
        else:
            four_element.relating_to = RelatingToElement.NO_LINK
            four_element.relating_to_reasoning = (
                f"Data element '{element_name}' does not relate to any identifiable natural person"
            )

        # Element 4: Natural person
        four_element.is_natural_person = is_living_person

        # Element 3: Identifiability assessment
        if element_type in self.DIRECT_IDENTIFIERS:
            four_element.identifiability = IdentifiabilityLevel.DIRECTLY_IDENTIFIED
            four_element.identifiability_reasoning = (
                f"'{element_type}' is a direct identifier under Art. 4(1)"
            )
        elif element_type in self.INDIRECT_IDENTIFIERS:
            breyer = BreyerAssessment()
            if controller_holds_complementary_data:
                breyer.legal_means_available = True
                breyer.legal_means_description = "Controller holds complementary identification data internally"
                breyer.proportionate_effort = True
                breyer.conclusion = "Personal data — controller can identify via internal data linkage"
            elif third_party_legal_means:
                breyer.legal_means_available = True
                breyer.legal_means_description = (
                    "Legal means available to obtain identification data from third party (per Breyer C-582/14)"
                )
                breyer.proportionate_effort = identification_cost_proportionate
                breyer.conclusion = (
                    "Personal data per Breyer ruling — legal means to third-party identification data exist"
                    if identification_cost_proportionate
                    else "Not personal data — identification requires disproportionate effort despite legal means"
                )
            elif publicly_combinable:
                breyer.legal_means_available = True
                breyer.legal_means_description = "Identification possible via combination with publicly available data"
                breyer.proportionate_effort = identification_cost_proportionate
                breyer.conclusion = (
                    "Personal data — publicly available data enables identification"
                    if identification_cost_proportionate
                    else "Not personal data — combination with public data is disproportionate"
                )
            else:
                breyer.legal_means_available = False
                breyer.conclusion = "Not personal data for this controller — no legal means to identify"

            four_element.breyer_assessment = breyer

            if breyer.is_personal_data():
                four_element.identifiability = IdentifiabilityLevel.INDIRECTLY_IDENTIFIABLE
            else:
                four_element.identifiability = IdentifiabilityLevel.NOT_IDENTIFIABLE

            four_element.identifiability_reasoning = breyer.conclusion

        elif element_type in self.NON_PERSONAL_TYPES:
            four_element.identifiability = IdentifiabilityLevel.NOT_IDENTIFIABLE
            four_element.identifiability_reasoning = (
                f"'{element_type}' does not relate to any identifiable natural person"
            )
        else:
            four_element.identifiability = IdentifiabilityLevel.UNCERTAIN
            four_element.identifiability_reasoning = (
                f"'{element_type}' requires manual borderline assessment"
            )

        # Determine classification
        classification = four_element.classify()

        # Check for special category
        if element_type in self.SPECIAL_CATEGORY_INDICATORS and classification in (
            ClassificationResult.PERSONAL_DIRECT,
            ClassificationResult.PERSONAL_INDIRECT,
        ):
            classification = ClassificationResult.SPECIAL_CATEGORY

        today = date.today()
        review_months = 12 if classification == ClassificationResult.BORDERLINE_REVIEW else 24
        review_date = today.replace(year=today.year + (review_months // 12))

        return DataElementClassification(
            element_id=f"DC-{system_name.upper()[:3]}-{element_name.upper()[:5]}-{today.strftime('%Y%m%d')}",
            element_name=element_name,
            system_name=system_name,
            data_source=data_source,
            four_element_test=four_element,
            classification=classification,
            assessment_date=today.isoformat(),
            review_date=review_date.isoformat(),
        )

    def generate_classification_report(
        self, classifications: list[DataElementClassification]
    ) -> dict:
        """Generate a summary report of data element classifications."""
        summary = {
            "report_date": date.today().isoformat(),
            "total_elements": len(classifications),
            "classification_counts": {},
            "elements_requiring_review": [],
            "special_category_elements": [],
            "elements_by_system": {},
        }

        for c in classifications:
            label = c.classification.value
            summary["classification_counts"][label] = (
                summary["classification_counts"].get(label, 0) + 1
            )

            if c.classification == ClassificationResult.BORDERLINE_REVIEW:
                summary["elements_requiring_review"].append({
                    "element_id": c.element_id,
                    "element_name": c.element_name,
                    "system": c.system_name,
                    "review_date": c.review_date,
                })

            if c.classification == ClassificationResult.SPECIAL_CATEGORY:
                summary["special_category_elements"].append({
                    "element_id": c.element_id,
                    "element_name": c.element_name,
                    "system": c.system_name,
                })

            sys_name = c.system_name
            if sys_name not in summary["elements_by_system"]:
                summary["elements_by_system"][sys_name] = []
            summary["elements_by_system"][sys_name].append({
                "element_id": c.element_id,
                "element_name": c.element_name,
                "classification": label,
            })

        return summary


def run_vanguard_example():
    """Demonstrate classification for Vanguard Financial Services data elements."""
    classifier = PersonalDataClassifier()

    elements_to_classify = [
        {
            "element_name": "customer_full_name",
            "element_type": "full_name",
            "system_name": "CRM",
            "data_source": "collected_from_data_subject",
            "relates_to_person": True,
            "is_living_person": True,
        },
        {
            "element_name": "visitor_ip_address",
            "element_type": "ip_address_dynamic",
            "system_name": "WebAnalytics",
            "data_source": "automatically_collected",
            "relates_to_person": True,
            "is_living_person": True,
            "third_party_legal_means": True,
            "identification_cost_proportionate": True,
        },
        {
            "element_name": "health_insurance_claim",
            "element_type": "health_data",
            "system_name": "BenefitsPortal",
            "data_source": "collected_from_data_subject",
            "relates_to_person": True,
            "is_living_person": True,
        },
        {
            "element_name": "daily_stock_price",
            "element_type": "stock_price",
            "system_name": "MarketData",
            "data_source": "third_party_feed",
            "relates_to_person": False,
            "is_living_person": False,
        },
        {
            "element_name": "tracking_cookie_id",
            "element_type": "cookie_identifier",
            "system_name": "WebAnalytics",
            "data_source": "automatically_collected",
            "relates_to_person": True,
            "is_living_person": True,
            "controller_holds_complementary_data": True,
        },
        {
            "element_name": "pseudonymised_transaction_token",
            "element_type": "pseudonymised_token",
            "system_name": "DataWarehouse",
            "data_source": "derived",
            "relates_to_person": True,
            "is_living_person": True,
            "controller_holds_complementary_data": True,
        },
    ]

    classifications = []
    for elem in elements_to_classify:
        result = classifier.classify_element(**elem)
        classifications.append(result)
        print(f"\n{'='*60}")
        print(f"Element: {result.element_name}")
        print(f"System: {result.system_name}")
        print(f"Classification: {result.classification.value}")
        print(f"Identifiability: {result.four_element_test.identifiability.value}")
        print(f"Reasoning: {result.four_element_test.identifiability_reasoning}")
        if result.four_element_test.breyer_assessment:
            print(f"Breyer Assessment: {result.four_element_test.breyer_assessment.conclusion}")
        print(f"Review Date: {result.review_date}")

    report = classifier.generate_classification_report(classifications)
    print(f"\n{'='*60}")
    print("CLASSIFICATION SUMMARY REPORT")
    print(f"{'='*60}")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    run_vanguard_example()
