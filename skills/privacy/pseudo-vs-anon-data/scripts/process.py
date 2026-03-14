"""
Pseudonymisation vs Anonymisation Classification Engine
Implements WP29 Opinion 05/2014 three-criteria test and motivated intruder assessment.
"""

import math
import json
from collections import Counter
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from datetime import date


class DeIdentificationStatus(Enum):
    ANONYMISED = "anonymised"
    PSEUDONYMISED = "pseudonymised"
    IDENTIFIED = "identified"
    ASSESSMENT_REQUIRED = "assessment_required"


class AnonymisationTechnique(Enum):
    TOKENISATION = "tokenisation"
    HASHING_UNSALTED = "hashing_unsalted"
    HASHING_SALTED = "hashing_salted"
    ENCRYPTION = "encryption"
    K_ANONYMITY = "k_anonymity"
    L_DIVERSITY = "l_diversity"
    T_CLOSENESS = "t_closeness"
    DIFFERENTIAL_PRIVACY = "differential_privacy"
    AGGREGATION = "aggregation"
    SUPPRESSION = "suppression"
    NOISE_ADDITION = "noise_addition"
    PERMUTATION = "permutation"


@dataclass
class SinglingOutResult:
    """Result of the singling out criterion test."""
    test_passed: bool
    k_anonymity_value: int
    unique_records: int
    total_records: int
    quasi_identifiers_tested: list[str]
    reasoning: str


@dataclass
class LinkabilityResult:
    """Result of the linkability criterion test."""
    test_passed: bool
    linkable_identifiers: list[str]
    external_datasets_considered: list[str]
    reasoning: str


@dataclass
class InferenceResult:
    """Result of the inference criterion test."""
    test_passed: bool
    l_diversity_value: int
    homogeneous_groups: int
    reasoning: str


@dataclass
class MotivatedIntruderResult:
    """Result of the ICO motivated intruder test."""
    test_passed: bool
    public_resources_considered: list[str]
    estimated_effort: str
    reasoning: str


@dataclass
class AnonymisationAssessment:
    """Complete anonymisation adequacy assessment."""
    dataset_name: str
    assessment_date: str
    assessor: str
    technique_applied: AnonymisationTechnique
    re_identification_key_exists: bool
    singling_out: Optional[SinglingOutResult] = None
    linkability: Optional[LinkabilityResult] = None
    inference: Optional[InferenceResult] = None
    motivated_intruder: Optional[MotivatedIntruderResult] = None
    technology_horizon_years: int = 0
    technology_risk: str = ""
    classification: DeIdentificationStatus = DeIdentificationStatus.ASSESSMENT_REQUIRED
    dpo_approved: bool = False
    review_date: str = ""

    def determine_classification(self) -> DeIdentificationStatus:
        if self.re_identification_key_exists:
            self.classification = DeIdentificationStatus.PSEUDONYMISED
            return self.classification

        three_criteria_pass = (
            self.singling_out and self.singling_out.test_passed
            and self.linkability and self.linkability.test_passed
            and self.inference and self.inference.test_passed
        )

        motivated_intruder_pass = (
            self.motivated_intruder and self.motivated_intruder.test_passed
        )

        if three_criteria_pass and motivated_intruder_pass:
            self.classification = DeIdentificationStatus.ANONYMISED
        else:
            self.classification = DeIdentificationStatus.PSEUDONYMISED

        return self.classification


class AnonymisationAssessor:
    """
    Implements the WP29 Opinion 05/2014 three-criteria test for anonymisation
    assessment and the ICO motivated intruder test.
    """

    def assess_singling_out(
        self,
        records: list[dict],
        quasi_identifiers: list[str],
        k_threshold: int = 5,
    ) -> SinglingOutResult:
        """
        Test whether individuals can be singled out using quasi-identifier combinations.

        Args:
            records: List of data records (dicts)
            quasi_identifiers: List of field names that are quasi-identifiers
            k_threshold: Minimum k-anonymity value (WP29 recommends k >= 5)

        Returns:
            SinglingOutResult with k-anonymity measurement
        """
        qi_tuples = []
        for record in records:
            qi_values = tuple(str(record.get(qi, "")) for qi in quasi_identifiers)
            qi_tuples.append(qi_values)

        group_counts = Counter(qi_tuples)
        min_k = min(group_counts.values()) if group_counts else 0
        unique_count = sum(1 for count in group_counts.values() if count == 1)

        test_passed = min_k >= k_threshold

        reasoning = (
            f"k-anonymity analysis on quasi-identifiers {quasi_identifiers}: "
            f"minimum group size = {min_k}, threshold = {k_threshold}. "
            f"{unique_count} unique records (groups of size 1) out of {len(records)} total. "
        )

        if test_passed:
            reasoning += (
                f"PASS: All quasi-identifier groups have at least {k_threshold} members. "
                "Singling out is not feasible via these quasi-identifiers."
            )
        else:
            reasoning += (
                f"FAIL: {unique_count} records can be singled out. "
                "Additional generalisation or suppression required."
            )

        return SinglingOutResult(
            test_passed=test_passed,
            k_anonymity_value=min_k,
            unique_records=unique_count,
            total_records=len(records),
            quasi_identifiers_tested=quasi_identifiers,
            reasoning=reasoning,
        )

    def assess_linkability(
        self,
        has_consistent_identifiers: bool,
        consistent_identifier_types: list[str],
        external_datasets: list[str],
        linkage_feasible: bool,
    ) -> LinkabilityResult:
        """
        Assess whether records can be linked to external data to identify individuals.

        Args:
            has_consistent_identifiers: Whether consistent identifiers exist across datasets
            consistent_identifier_types: Types of identifiers (hashed email, timestamps, etc.)
            external_datasets: External datasets considered for linkage
            linkage_feasible: Expert assessment of whether linkage is practically feasible
        """
        test_passed = not linkage_feasible

        if test_passed:
            reasoning = (
                f"Linkability assessment considered {len(external_datasets)} external datasets. "
                "No consistent identifiers enable practical cross-dataset linkage. "
                "PASS: Linkability criterion satisfied."
            )
        else:
            reasoning = (
                f"Linkability assessment found consistent identifiers "
                f"({', '.join(consistent_identifier_types)}) that could enable linkage "
                f"with external datasets ({', '.join(external_datasets)}). "
                "FAIL: Records can be linked to identify individuals."
            )

        return LinkabilityResult(
            test_passed=test_passed,
            linkable_identifiers=consistent_identifier_types if not test_passed else [],
            external_datasets_considered=external_datasets,
            reasoning=reasoning,
        )

    def assess_inference(
        self,
        records: list[dict],
        quasi_identifiers: list[str],
        sensitive_attribute: str,
        l_threshold: int = 3,
    ) -> InferenceResult:
        """
        Assess whether sensitive attribute values can be inferred (l-diversity test).

        Args:
            records: List of data records
            quasi_identifiers: Quasi-identifier field names
            sensitive_attribute: The sensitive attribute to test
            l_threshold: Minimum l-diversity value
        """
        groups: dict[tuple, list] = {}
        for record in records:
            qi_key = tuple(str(record.get(qi, "")) for qi in quasi_identifiers)
            sensitive_val = record.get(sensitive_attribute, "")
            if qi_key not in groups:
                groups[qi_key] = []
            groups[qi_key].append(sensitive_val)

        min_l = float("inf")
        homogeneous = 0
        for qi_key, values in groups.items():
            distinct_values = len(set(values))
            if distinct_values < min_l:
                min_l = distinct_values
            if distinct_values == 1:
                homogeneous += 1

        min_l = int(min_l) if min_l != float("inf") else 0
        test_passed = min_l >= l_threshold

        reasoning = (
            f"l-diversity analysis on sensitive attribute '{sensitive_attribute}': "
            f"minimum distinct values per group = {min_l}, threshold = {l_threshold}. "
            f"{homogeneous} homogeneous groups (all same sensitive value). "
        )

        if test_passed:
            reasoning += "PASS: Sufficient diversity prevents attribute inference."
        else:
            reasoning += (
                f"FAIL: {homogeneous} groups have homogeneous sensitive attributes, "
                "enabling inference of individual values."
            )

        return InferenceResult(
            test_passed=test_passed,
            l_diversity_value=min_l,
            homogeneous_groups=homogeneous,
            reasoning=reasoning,
        )

    def assess_motivated_intruder(
        self,
        dataset_description: str,
        public_resources: list[str],
        estimated_effort_days: int,
        intruder_could_identify: bool,
    ) -> MotivatedIntruderResult:
        """
        Apply the ICO motivated intruder test.
        """
        test_passed = not intruder_could_identify

        if test_passed:
            reasoning = (
                f"Motivated intruder assessment for '{dataset_description}': "
                f"Considered {len(public_resources)} public resources. "
                f"Estimated effort: {estimated_effort_days} days. "
                "A motivated intruder with general skills and public resources "
                "could NOT identify any individual. PASS."
            )
        else:
            reasoning = (
                f"Motivated intruder assessment for '{dataset_description}': "
                f"Considered {len(public_resources)} public resources. "
                f"Estimated effort: {estimated_effort_days} days. "
                "A motivated intruder COULD identify individuals using "
                f"available resources ({', '.join(public_resources[:3])}). FAIL."
            )

        return MotivatedIntruderResult(
            test_passed=test_passed,
            public_resources_considered=public_resources,
            estimated_effort=f"{estimated_effort_days} days",
            reasoning=reasoning,
        )


def run_vanguard_example():
    """Demonstrate anonymisation assessment for Vanguard Financial Services."""
    assessor = AnonymisationAssessor()

    sample_records = [
        {"age_band": "30-39", "region": "London", "salary_band": "50k-60k", "department": "Trading"},
        {"age_band": "30-39", "region": "London", "salary_band": "60k-70k", "department": "Trading"},
        {"age_band": "30-39", "region": "London", "salary_band": "50k-60k", "department": "IT"},
        {"age_band": "30-39", "region": "London", "salary_band": "70k-80k", "department": "Trading"},
        {"age_band": "30-39", "region": "London", "salary_band": "50k-60k", "department": "Trading"},
        {"age_band": "40-49", "region": "Edinburgh", "salary_band": "80k-90k", "department": "Compliance"},
        {"age_band": "40-49", "region": "Edinburgh", "salary_band": "60k-70k", "department": "Compliance"},
        {"age_band": "40-49", "region": "Edinburgh", "salary_band": "80k-90k", "department": "Legal"},
        {"age_band": "50-59", "region": "Edinburgh", "salary_band": "100k+", "department": "Executive"},
        {"age_band": "30-39", "region": "London", "salary_band": "60k-70k", "department": "IT"},
    ]

    print("=" * 70)
    print("VANGUARD FINANCIAL SERVICES — ANONYMISATION ASSESSMENT")
    print("Dataset: Employee Salary Survey (generalised)")
    print("=" * 70)

    singling = assessor.assess_singling_out(
        records=sample_records,
        quasi_identifiers=["age_band", "region", "department"],
        k_threshold=3,
    )
    print(f"\n1. SINGLING OUT TEST")
    print(f"   Result: {'PASS' if singling.test_passed else 'FAIL'}")
    print(f"   k-anonymity: {singling.k_anonymity_value}")
    print(f"   Unique records: {singling.unique_records}/{singling.total_records}")

    linkability = assessor.assess_linkability(
        has_consistent_identifiers=False,
        consistent_identifier_types=[],
        external_datasets=["LinkedIn profiles", "Companies House directors register", "Electoral roll"],
        linkage_feasible=True,
    )
    print(f"\n2. LINKABILITY TEST")
    print(f"   Result: {'PASS' if linkability.test_passed else 'FAIL'}")
    print(f"   {linkability.reasoning}")

    inference = assessor.assess_inference(
        records=sample_records,
        quasi_identifiers=["age_band", "region"],
        sensitive_attribute="salary_band",
        l_threshold=3,
    )
    print(f"\n3. INFERENCE TEST")
    print(f"   Result: {'PASS' if inference.test_passed else 'FAIL'}")
    print(f"   l-diversity: {inference.l_diversity_value}")
    print(f"   Homogeneous groups: {inference.homogeneous_groups}")

    intruder = assessor.assess_motivated_intruder(
        dataset_description="Generalised employee salary survey",
        public_resources=["LinkedIn", "Companies House", "Glassdoor salary data"],
        estimated_effort_days=3,
        intruder_could_identify=True,
    )
    print(f"\n4. MOTIVATED INTRUDER TEST")
    print(f"   Result: {'PASS' if intruder.test_passed else 'FAIL'}")

    assessment = AnonymisationAssessment(
        dataset_name="Employee Salary Survey (generalised)",
        assessment_date=date.today().isoformat(),
        assessor="Sarah Mitchell, Senior Privacy Analyst",
        technique_applied=AnonymisationTechnique.K_ANONYMITY,
        re_identification_key_exists=False,
        singling_out=singling,
        linkability=linkability,
        inference=inference,
        motivated_intruder=intruder,
        technology_horizon_years=5,
    )

    classification = assessment.determine_classification()
    print(f"\n{'='*70}")
    print(f"FINAL CLASSIFICATION: {classification.value.upper()}")
    print(f"{'='*70}")
    if classification == DeIdentificationStatus.PSEUDONYMISED:
        print("This dataset remains PERSONAL DATA under GDPR.")
        print("Full GDPR obligations apply, including lawful basis, data subject rights,")
        print("and security measures. Additional generalisation or differential privacy")
        print("noise is recommended to achieve true anonymisation.")


if __name__ == "__main__":
    run_vanguard_example()
