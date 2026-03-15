---
name: hipaa-deidentification
description: >-
  Implements HIPAA de-identification methods under 45 CFR §164.514(a)-(b).
  Covers expert determination method and safe harbor method with 18
  identifiers removal, re-identification risk assessment, limited dataset
  requirements, and data use agreements. Keywords: HIPAA de-identification,
  safe harbor, expert determination, 18 identifiers, limited dataset, PHI.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: healthcare-privacy
  tags: "hipaa, de-identification, safe-harbor, expert-determination, 18-identifiers, limited-dataset, phi"
---

# HIPAA De-Identification Methods — 45 CFR §164.514(a)-(b)

## Overview

De-identification is the process by which protected health information (PHI) is stripped of identifying elements such that it no longer identifies an individual and there is no reasonable basis to believe it can be used to identify an individual. Under 45 CFR §164.514(a), health information that has been de-identified is no longer PHI and is not subject to the HIPAA Privacy Rule. HIPAA provides two permissible methods for de-identification: expert determination (§164.514(b)(1)) and safe harbor (§164.514(b)(2)). The choice of method depends on the nature of the data, the intended use, and the organization's risk tolerance and resources. OCR published detailed guidance on de-identification methods in November 2012 (updated September 2023), providing extensive clarification on both methods.

## Legal Framework

### Definition of De-Identified Information — §164.514(a)

Health information is de-identified if it does not identify an individual and if the covered entity has no reasonable basis to believe it can be used to identify an individual. The standard is met by applying either the expert determination or safe harbor method.

### Key Distinction: De-Identification vs Anonymization

HIPAA uses the term "de-identification" rather than "anonymization." De-identified data under HIPAA may still carry some theoretical re-identification risk — the standard is "no reasonable basis" to believe identification is possible, not absolute impossibility. This contrasts with GDPR's concept of anonymization, which requires irreversibility.

## Method 1: Expert Determination — §164.514(b)(1)

### Requirements

A person with appropriate knowledge of and experience with generally accepted statistical and scientific principles and methods for rendering information not individually identifiable must:

1. Apply such principles and methods to determine that the risk is very small that the information could be used, alone or in combination with other reasonably available information, to identify an individual who is a subject of the information
2. Document the methods and results of the analysis that justify the determination

### Qualified Expert

OCR guidance does not specify required credentials but indicates the expert should have knowledge in:

- Statistical methods for assessing disclosure risk (k-anonymity, l-diversity, t-closeness)
- Re-identification attack methodologies (linkage attacks, inference attacks)
- Publicly available data sources and their linkage potential
- Health data characteristics and population uniqueness

Typical qualifications include PhD-level training in statistics, biostatistics, data science, or computer science with specialization in privacy or disclosure limitation.

### Expert Determination Process

#### Step 1: Threat Modeling

The expert identifies plausible re-identification scenarios:

| Attack Type | Description | Example |
|------------|-------------|---------|
| Prosecutor attack | Adversary knows the target is in the dataset and attempts to match records | Researcher knows a specific person visited the hospital and tries to find their record in a published dataset |
| Journalist attack | Adversary attempts to re-identify any individual in the dataset | Reporter uses voter registration data to link de-identified hospital discharge records to named individuals |
| Marketer attack | Adversary attempts to re-identify as many individuals as possible | Data broker combines de-identified health data with consumer databases |

#### Step 2: Risk Quantification

The expert applies statistical methods to quantify re-identification risk:

**Population Uniqueness Analysis**: Assess how unique combinations of quasi-identifiers are in the relevant population.

**Commonly used metrics**:

| Metric | Definition | Threshold |
|--------|-----------|-----------|
| k-anonymity | Every record in the dataset is identical to at least k-1 other records with respect to quasi-identifiers | k ≥ 5 is commonly accepted; k ≥ 10 for higher sensitivity |
| l-diversity | Within each equivalence class (k-anonymous group), there are at least l distinct values for sensitive attributes | l ≥ 3 to protect against homogeneity attacks |
| t-closeness | Distribution of sensitive attributes within each equivalence class is within distance t of the overall distribution | t ≤ 0.15 (application-dependent) |
| Maximum re-identification probability | Probability that any single record can be matched to a specific individual | ≤ 0.04 (4%) — commonly cited by experts; some use 0.05 or 0.09 |

#### Step 3: Transformation Application

The expert specifies transformations to reduce risk to an acceptable level:

| Transformation | Application |
|---------------|-------------|
| Generalization | Replace specific values with ranges (age 47 → age 45-49; ZIP 02139 → 021**) |
| Suppression | Remove records or values that are too unique (suppress records with rare diseases in small populations) |
| Perturbation | Add controlled noise to numerical values (date of birth shifted by random offset within ±7 days) |
| Aggregation | Replace individual-level data with group-level statistics |
| Top/bottom coding | Cap extreme values (age >89 → 90+; weight >300 → 300+) |

#### Step 4: Documentation

The expert must document:
- Qualifications and experience
- Methodology applied
- Data analyzed (original and transformed)
- Risk metrics computed
- Justification for risk thresholds selected
- Residual risk assessment
- Any conditions on data use that affect the risk determination

**Asclepius Health Network** engages an external expert (PhD biostatistician with healthcare disclosure risk expertise) for expert determination on research datasets. The expert's report is retained as required documentation.

## Method 2: Safe Harbor — §164.514(b)(2)

### Requirements

Remove the following 18 categories of identifiers of the individual or of relatives, employers, or household members:

| # | Identifier | Removal Specification |
|---|-----------|----------------------|
| 1 | Names | All names |
| 2 | Geographic data | All geographic subdivisions smaller than a state. Exception: first 3 digits of ZIP code may be retained if the geographic unit formed by combining all ZIP codes with the same first 3 digits contains more than 20,000 persons (per Census Bureau data). ZIP codes where the 3-digit prefix has ≤20,000 persons must be replaced with 000 |
| 3 | Dates | All elements of dates (except year) directly related to an individual, including birth date, admission date, discharge date, death date. All ages over 89 and all elements of dates (including year) indicative of such age must be aggregated into a single category of 90+ |
| 4 | Telephone numbers | All telephone numbers |
| 5 | Fax numbers | All fax numbers |
| 6 | Email addresses | All email addresses |
| 7 | Social Security numbers | All SSNs |
| 8 | Medical record numbers | All MRNs |
| 9 | Health plan beneficiary numbers | All plan IDs |
| 10 | Account numbers | All account numbers |
| 11 | Certificate/license numbers | All certificate and license numbers |
| 12 | Vehicle identifiers | All vehicle identifiers and serial numbers including license plate numbers |
| 13 | Device identifiers | All device identifiers and serial numbers |
| 14 | Web URLs | All web Universal Resource Locators |
| 15 | IP addresses | All Internet Protocol address numbers |
| 16 | Biometric identifiers | Including finger and voice prints |
| 17 | Full-face photographs | And any comparable images |
| 18 | Any other unique identifying number, characteristic, or code | Except as permitted by re-identification under §164.514(c) |

### Additional Safe Harbor Requirement

The covered entity must have no actual knowledge that the remaining information could be used alone or in combination with other information to identify an individual.

### Asclepius Health Network Safe Harbor Implementation

Asclepius Health Network uses an automated de-identification pipeline for data released under the safe harbor method:

1. **Structured data**: EHR extraction scripts strip all 18 identifier categories from structured fields. Date fields are transformed to retain year only (or year and quarter if research protocol requires and dates are not directly related to the individual). Ages over 89 are mapped to 90+. ZIP codes are truncated to 3 digits and validated against the Census Bureau threshold table.

2. **Unstructured data (clinical notes)**: NLP-based named entity recognition (NER) system identifies and redacts names, locations, dates, phone numbers, SSNs, MRNs, email addresses, URLs, and other identifiers in free-text clinical notes. Redacted text is replaced with category-specific tags (e.g., `[DATE]`, `[NAME]`, `[LOCATION]`). Human review sample (10% of documents) validates NER accuracy.

3. **Imaging data**: DICOM header scrubbing removes patient name, ID, dates, institution name, and all private tags. Burned-in annotations on images are reviewed and redacted for identifiers (facial photographs require defacing algorithms).

4. **Quality assurance**: Post-de-identification audit scans output datasets for residual identifiers using regular expressions, dictionaries of patient names, and cross-reference against the source dataset. Any residual identifiers trigger re-processing and root cause analysis.

## Re-Identification — §164.514(c)

### Code-Based Re-Identification

A covered entity may assign a code or other record identification mechanism to de-identified information, enabling re-identification under the following conditions:

1. The code is not derived from or related to information about the individual (cannot be a hash of SSN or MRN)
2. The code is not otherwise capable of being translated to identify the individual
3. The covered entity does not use or disclose the code for any other purpose
4. The covered entity does not disclose the mechanism for re-identification

The re-identification key must be maintained securely and separately from the de-identified dataset.

**Asclepius Health Network**: Research datasets are assigned a study-specific random identifier. The crosswalk (random ID ↔ MRN) is encrypted and stored separately from the de-identified dataset in a restricted-access key management system accessible only to the IRB-approved honest broker.

## Limited Data Set — §164.514(e)

### Definition

A limited data set is PHI that excludes the following direct identifiers of the individual or of relatives, employers, or household members:

- Names
- Street addresses (city, state, ZIP code may be retained)
- Telephone numbers, fax numbers, email addresses
- Social Security numbers
- Medical record numbers, health plan beneficiary numbers, account numbers
- Certificate/license numbers
- Vehicle identifiers, device identifiers
- Web URLs, IP addresses
- Biometric identifiers
- Full-face photographs

A limited data set **retains** dates (birth, admission, discharge, death), city, state, ZIP code, and ages (including over 89).

### Data Use Agreement (DUA) — §164.514(e)(4)

A limited data set may be used or disclosed only if the covered entity enters into a data use agreement with the recipient. The DUA must:

1. Establish the permitted uses and purposes of the limited data set (limited to research, public health, or healthcare operations)
2. Establish who is permitted to use or receive the limited data set
3. Provide that the recipient will not use or further disclose the information other than as permitted by the DUA or as required by law
4. Provide that the recipient will use appropriate safeguards to prevent unauthorized use or disclosure
5. Provide that the recipient will report any unauthorized use or disclosure to the covered entity
6. Provide that the recipient will ensure that any agents to whom it provides the limited data set agree to the same restrictions and conditions
7. Provide that the recipient will not attempt to identify the individuals or contact the individuals

### Limited Data Set vs De-Identified Data

| Feature | De-Identified (Safe Harbor) | Limited Data Set |
|---------|---------------------------|-----------------|
| HIPAA status | Not PHI; not subject to Privacy Rule | Still PHI; subject to Privacy Rule |
| Dates permitted | Year only | Full dates |
| Geographic data | First 3 digits of ZIP (if population threshold met) | City, state, full ZIP code |
| Ages over 89 | Must be aggregated to 90+ | Retained |
| Agreement required | None | Data Use Agreement |
| Permitted uses | Any (not PHI) | Research, public health, healthcare operations only |
| Breach notification | Not applicable (not PHI) | Required if unsecured |

## Re-Identification Risk Considerations

### Publicly Available Data Sources

The expert determination method requires assessment of "reasonably available" data that could be combined with de-identified health data:

| Data Source | Re-Identification Risk | Availability |
|------------|----------------------|-------------|
| Voter registration records | Name, address, DOB, gender | Publicly available in most states |
| Property records | Name, address, purchase date | County recorder offices; commercial aggregators |
| News/media reports | Specific incident details (accident, shooting, notable illness) | Internet search |
| Social media | Self-disclosed health information, location, activities | Publicly posted profiles |
| Death records | Name, DOB, date of death, cause | State vital statistics; SSDI |
| Court records | Name, address, case details | PACER; state court systems |
| Commercial data brokers | Demographics, purchasing behavior, inferred attributes | Commercially available |

### OCR Guidance on Re-Identification Risk

OCR has noted that:
- Small geographic areas (census tracts, block groups) combined with birth dates and gender can uniquely identify a high percentage of the US population
- Rare diseases and unusual procedures increase uniqueness even after safe harbor de-identification
- Temporal specificity (exact dates of admission/discharge) combined with institution identity can enable re-identification via news reports
- The "no actual knowledge" requirement under safe harbor is a substantive obligation, not merely a formality

## Enforcement

- **Aetna (2017)**: Settled with multiple state AGs and OCR for $1.15 million (state AG settlement) plus separate OCR resolution — mailing envelopes with visible window revealed HIV medication status of approximately 12,000 members. While not a de-identification case per se, it demonstrated the risk of identifiable health information exposure through seemingly innocuous channels.

OCR has not imposed penalties specifically for de-identification methodology failures, but has included de-identification review in corrective action plans and emphasized the importance of proper de-identification in guidance documents.

## Integration Points

- **hipaa-privacy-rule**: De-identification removes data from Privacy Rule scope; failure to properly de-identify means all Privacy Rule requirements apply
- **hipaa-minimum-necessary**: De-identification and limited datasets serve minimum necessary purposes for research and analytics
- **healthcare-ai-privacy**: AI training data often requires de-identification; model memorization risk can undermine de-identification
- **hipaa-risk-analysis**: Re-identification risk assessment parallels security risk analysis methodology
