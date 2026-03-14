---
name: personal-data-test
description: >-
  Classifies personal vs non-personal data per GDPR Art. 4(1) definition test
  with decision tree for borderline cases. References Breyer v Germany CJEU
  C-582/14 dynamic IP ruling and WP29 Opinion 4/2007. Keywords: personal data,
  GDPR Art 4, data classification, Breyer ruling, identifiability test, PII.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-classification
  tags: "personal-data, gdpr-art-4, classification, breyer-ruling, identifiability, pii"
---

# Personal Data Classification Test — GDPR Art. 4(1)

## Overview

Article 4(1) of the GDPR defines personal data as "any information relating to an identified or identifiable natural person ('data subject')." This definition is deliberately broad and technology-neutral. The European Court of Justice in Breyer v Bundesrepublik Deutschland (C-582/14, 19 October 2016) confirmed that even dynamic IP addresses can constitute personal data when the controller has legal means to obtain additional information enabling identification. This skill provides a systematic decision framework for classifying data elements as personal, non-personal, or borderline requiring contextual assessment.

## Legal Foundation

### Art. 4(1) — Four Constituent Elements

Personal data exists when ALL four elements are satisfied:

| Element | Definition | Assessment Criteria |
|---------|-----------|-------------------|
| **Any information** | No restriction on nature, content, or format of information | Includes objective facts (age, blood type) and subjective assessments (credit rating, performance review). Covers all formats: text, image, audio, biometric, metadata, behavioural |
| **Relating to** | Information must have a content, purpose, or result link to the individual | Content link: information is about the person. Purpose link: information is used to evaluate or influence the person. Result link: processing has an impact on the person's rights or interests |
| **Identified or identifiable** | The person is or can be distinguished from all other persons | Identified: directly singled out. Identifiable: can be singled out by using additional data, taking into account all means reasonably likely to be used |
| **Natural person** | Living human being, not legal entities or deceased persons | Excludes companies, government bodies, associations. Member State law may extend protections to deceased persons (e.g., Italy extends to 20 years post-mortem) |

### Recital 26 — "Reasonably Likely" Test for Identifiability

To determine whether a natural person is identifiable, account should be taken of all the means reasonably likely to be used, such as singling out, either by the controller or by another person to identify the natural person directly or indirectly. The assessment must consider:

- **All objective factors**: cost of identification, time required, available technology at the time of processing, and technological developments anticipated during the retention period
- **All means reasonably likely**: not limited to means the controller currently possesses — includes means any third party might reasonably employ
- **Dynamic assessment**: what is not identifiable today may become identifiable as technology evolves or datasets are linked

## The Breyer Ruling — CJEU C-582/14

### Facts

Patrick Breyer challenged the German Federal Government's practice of storing dynamic IP addresses of visitors to government websites. Germany argued that dynamic IP addresses were not personal data because the website operator could not identify visitors without additional data held by the internet service provider (ISP).

### Holding

The CJEU ruled that dynamic IP addresses constitute personal data for the website operator when:

1. The operator has **legal means** available to obtain additional identifying information from a third party (the ISP)
2. Identification does not require **disproportionate effort** in terms of time, cost, or labour
3. The means are **reasonably likely** to be used — not merely theoretical

### Key Legal Principles Established

- **Relative approach to identifiability**: Personal data status is assessed relative to each controller's circumstances, not in the abstract
- **Legal means suffice**: The controller need not currently possess the identifying data; having legal channels to obtain it is sufficient
- **Third-party knowledge counts**: Information held by third parties must be considered if the controller has lawful means of access
- **Broad interpretation**: The CJEU confirmed the GDPR's (then Directive 95/46/EC's) intent to apply broadly to protect fundamental rights

### Practical Impact

After Breyer, the following are presumptively personal data for most controllers:

- Dynamic and static IP addresses
- Device fingerprints and browser fingerprints
- Cookie identifiers and advertising IDs
- MAC addresses when combined with network access logs
- Pseudonymised datasets where re-identification keys exist or are obtainable

## Decision Tree for Personal Data Classification

### Stage 1: Is the Data About a Natural Person?

```
Data Element
    │
    ├── About a living natural person? ──► YES → Go to Stage 2
    │
    ├── About a deceased person? ──► Check Member State law (may still be protected)
    │
    ├── About a legal entity only? ──► NOT personal data under GDPR
    │       (but may contain personal data of individuals within,
    │        e.g., sole trader name = personal data)
    │
    └── About an anonymous aggregate? ──► Go to Stage 3 (verify truly anonymous)
```

### Stage 2: Can the Person Be Identified or Is the Person Identifiable?

```
Data relates to a natural person
    │
    ├── Person is DIRECTLY identified?
    │   (name, photograph, unique ID number)
    │   ──► PERSONAL DATA
    │
    ├── Person is INDIRECTLY identifiable?
    │   (combination of data points enables singling out)
    │   ──► Apply Recital 26 "reasonably likely" test → Stage 2a
    │
    └── Person cannot be identified by any means reasonably likely?
        ──► NOT personal data (but document the assessment)
```

### Stage 2a: Recital 26 Reasonably Likely Assessment

```
Indirect identifiers present
    │
    ├── Does the controller hold additional data enabling identification?
    │   ──► YES → PERSONAL DATA
    │
    ├── Does a third party hold such data, and does the controller
    │   have legal means to access it? (Breyer test)
    │   ──► YES → PERSONAL DATA
    │
    ├── Could publicly available data be combined to identify?
    │   (social media, public registers, news articles)
    │   ──► YES → PERSONAL DATA
    │
    ├── Is re-identification feasible considering:
    │   - Cost vs. value of identification
    │   - Time required vs. retention period
    │   - Current and foreseeable technology
    │   ──► YES → PERSONAL DATA
    │
    └── Identification requires disproportionate effort with no
        reasonable motivation?
        ──► NOT personal data (document reasoning)
```

### Stage 3: Anonymisation Verification

```
Data claimed to be anonymous/aggregated
    │
    ├── Can any individual be singled out from the dataset?
    │   ──► YES → PERSONAL DATA (pseudonymised, not anonymised)
    │
    ├── Can records be linked to form a profile of an individual?
    │   ──► YES → PERSONAL DATA
    │
    ├── Can information be inferred about a specific individual?
    │   ──► YES → PERSONAL DATA
    │
    └── Passes all three tests (singling out, linkability, inference)?
        ──► Anonymised data — NOT personal data
        (Apply WP29 Opinion 05/2014 framework)
```

## Classification Categories with Examples

### Category A: Clear Personal Data (Always Personal)

| Data Element | Reason |
|-------------|--------|
| Full name | Direct identifier |
| National ID number (SSN, Aadhaar, BSN) | Unique direct identifier |
| Email address (personal) | Directly identifies in most contexts |
| Photograph of a face | Direct visual identifier (also biometric if processed for identification) |
| Biometric data (fingerprint, iris scan) | Unique to individual, Art. 9 special category when used for identification |
| Genetic data | Unique biological identifier, Art. 9 special category |
| Health records with patient name | Direct identifier plus Art. 9 special category |
| Home address with name | Direct identifier with location |

### Category B: Contextually Personal Data (Requires Assessment)

| Data Element | When Personal | When Not Personal |
|-------------|--------------|------------------|
| Dynamic IP address | When controller has legal means to obtain subscriber info from ISP (Breyer) | When controller has no means and no motivation to identify (rare) |
| Cookie identifier | When linked to browsing profile that enables singling out | When session-only cookie with no profile building |
| Device fingerprint | When used to track across sites/sessions | When used only for aggregate device statistics with k-anonymity |
| Employee ID number | When linked to HR records by same controller | When used in anonymised survey with no re-identification key |
| Location data (GPS coordinates) | When tracking individual movement patterns | When aggregated to postcode-level with >1000 individuals per cell |
| Purchase history | When linked to customer account | When stripped of all identifiers and aggregated by product category |
| Vehicle registration number | When plate-to-owner lookup is legally available | Not applicable — plate lookup is available in most jurisdictions, so nearly always personal |

### Category C: Typically Not Personal Data

| Data Element | Condition for Non-Personal Status |
|-------------|----------------------------------|
| Weather data | General environmental data not relating to individuals |
| Stock prices | Corporate financial data |
| Machine sensor readings | Equipment telemetry with no operator identification |
| Aggregated census statistics | Published statistical tables with adequate anonymisation |
| Chemical compound properties | Scientific data about substances |
| Company financial statements | Legal entity data (but may contain director names) |

## Borderline Cases — Detailed Analysis

### Case 1: Pseudonymised Data

Pseudonymised data remains personal data under GDPR (Recital 26, Art. 4(5)). The existence of a re-identification key — even if held by a separate entity — means the data relates to an identifiable person. Pseudonymisation is a security measure, not an anonymisation technique.

**Vanguard Financial Services Application**: Customer transaction records where account numbers are replaced with random tokens. The mapping table is held by a separate internal department with access controls. These remain personal data because:
- Vanguard holds the re-identification key internally
- Re-identification requires minimal effort (database lookup)
- The data was processed for purposes relating to specific customers

### Case 2: Behavioural Profiles Without Direct Identifiers

A profile built from browsing behaviour, purchase patterns, and location data — even without a name or email — constitutes personal data when the profile enables singling out the individual. The Article 29 Working Party in Opinion 4/2007 on the concept of personal data confirmed that "a profile can in itself be sufficient to identify a specific user."

### Case 3: Encrypted Data

Encrypted personal data remains personal data for the controller who holds the decryption key. For a third party without the key and no reasonable means to obtain it, the encrypted data may not constitute personal data (applying the Breyer relative approach). However, this assessment must account for future cryptanalytic capabilities.

## WP29 Opinion 4/2007 — Key Principles

The Article 29 Working Party Opinion 4/2007 on the concept of personal data established foundational interpretive guidance:

1. **Content element**: Information "about" a person exists when the content concerns that individual, regardless of purpose or result
2. **Purpose element**: Data is "about" a person when it is used or likely to be used to evaluate, treat, or influence that person
3. **Result element**: Data is "about" a person when processing is likely to have an impact on that person's rights or interests
4. **Any one element suffices**: Data need only satisfy the content, purpose, OR result element to "relate to" a person

## Implementation Procedure for Vanguard Financial Services

### Step 1: Data Element Inventory

For each system, catalogue every data element collected, stored, or processed. Record:
- Field name and data type
- Source of data (collected from data subject, derived, inferred, received from third party)
- Sample values (redacted as needed)
- Current classification if any

### Step 2: Apply the Four-Element Test

For each data element, document the assessment against Art. 4(1):
- Is this any information? (Almost always yes)
- Does it relate to a natural person? (Content, purpose, or result link)
- Is the person identified or identifiable? (Direct or indirect, applying Breyer)
- Is the person a living natural person?

### Step 3: Borderline Assessment

For elements not clearly personal or non-personal:
- Apply the Recital 26 reasonably likely test
- Consider the Breyer third-party knowledge doctrine
- Document the reasoning and conclusion
- Assign to a review schedule (reassess annually or when technology/data partnerships change)

### Step 4: Classification Tagging

Apply classification labels:
- `PERSONAL_DIRECT`: Directly identifies a natural person
- `PERSONAL_INDIRECT`: Indirectly identifies through combination or third-party data
- `SPECIAL_CATEGORY`: Art. 9 special category personal data
- `PSEUDONYMISED`: Personal data with re-identification key separated
- `ANONYMISED`: Verified anonymous data (not personal data)
- `NON_PERSONAL`: Not personal data under any reasonable assessment
- `BORDERLINE_REVIEW`: Requires periodic reassessment

### Step 5: Documentation and Governance

- Record all classification decisions in the data inventory
- Link each personal data element to its Art. 6 lawful basis
- Link Art. 9 special category data to its Art. 9(2) processing condition
- Schedule annual review of borderline classifications
- Trigger reclassification when new data partnerships, technologies, or regulatory guidance emerge

## Enforcement Precedents

- **Breyer v Bundesrepublik Deutschland (CJEU C-582/14, 2016)**: Dynamic IP addresses are personal data when legal means to identify exist — established the relative identifiability standard
- **Nowak v Data Protection Commissioner (CJEU C-434/16, 2017)**: Examination answers and examiner's corrections are personal data of the candidate — applied the broad "relating to" test
- **YS v Minister voor Immigratie (CJEU C-141/12, 2014)**: Legal analysis in an immigration decision document is personal data of the applicant — the "result" element of the relating-to test
- **Scarlet Extended SA v SABAM (CJEU C-70/10, 2011)**: IP addresses collected in the context of monitoring internet traffic constitute personal data

## Integration Points

- **Art. 9 Special Categories**: Personal data classified as special category requires additional processing conditions — see `special-category-data` skill
- **Art. 30 Records of Processing**: Classification feeds directly into the categories of personal data field in RoPA
- **Art. 35 DPIA**: High-risk personal data classifications trigger DPIA requirements
- **Art. 25 Data Protection by Design**: Classification determines the level of technical protection required
