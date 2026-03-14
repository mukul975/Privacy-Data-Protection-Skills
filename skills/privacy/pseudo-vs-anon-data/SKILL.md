---
name: pseudo-vs-anon-data
description: >-
  Classifies data as pseudonymised or anonymised using Recital 26 reasonably
  likely test, Breyer ruling C-582/14, motivated intruder test, and WP29
  Opinion 05/2014 on anonymisation techniques. Covers singling out, linkability,
  and inference tests. Keywords: pseudonymisation, anonymisation, Recital 26,
  re-identification, k-anonymity, differential privacy, WP29 Opinion 05/2014.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-classification
  tags: "pseudonymisation, anonymisation, recital-26, re-identification, k-anonymity, wp29"
---

# Pseudonymised vs Anonymised Data Classification

## Overview

The distinction between pseudonymised and anonymised data is one of the most consequential classifications in data protection law. Pseudonymised data remains personal data subject to the full GDPR (Art. 4(5), Recital 26). Anonymised data falls outside the GDPR entirely (Recital 26). The boundary between them determines whether processing requires a lawful basis, whether data subjects can exercise rights, and whether the data can be freely shared. This skill provides the analytical framework for making this determination, drawing on the CJEU Breyer ruling (C-582/14), the Article 29 Working Party Opinion 05/2014 on Anonymisation Techniques (WP216), and the ICO motivated intruder test.

## Legal Definitions

### Pseudonymisation — Art. 4(5)

"The processing of personal data in such a manner that the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to technical and organisational measures to ensure that the personal data are not attributed to an identified or identifiable natural person."

**Key characteristics**:
- Data has undergone a transformation (tokenisation, hashing, encryption)
- A re-identification key or method exists
- The key is kept separately from the data
- Technical and organisational controls protect the key
- The data REMAINS personal data under GDPR

### Anonymisation — Recital 26

"The principles of data protection should therefore not apply to anonymous information, namely information which does not relate to an identified or identifiable natural person or to personal data rendered anonymous in such a manner that the data subject is not or no longer identifiable."

**Key characteristics**:
- No means exist that are reasonably likely to be used for identification
- Assessment considers ALL means reasonably likely, including third-party means
- Assessment accounts for cost, time, and available technology
- Assessment considers technological developments over the data retention period
- Truly anonymised data is NOT personal data — GDPR does not apply

## The Three-Criteria Test — WP29 Opinion 05/2014 (WP216)

The Article 29 Working Party established three criteria for evaluating whether anonymisation is effective. Data is NOT anonymised if ANY of the three attacks can succeed:

### Criterion 1: Singling Out

**Definition**: The possibility of isolating some or all records that identify an individual in the dataset.

**Test**: Can a specific individual be distinguished from all other individuals in the dataset?

**Examples of failure**:
- A dataset with unique combinations of age, postcode, and gender that correspond to only one person in the population
- A dataset with unique transaction patterns that correspond to a single customer
- Removing a name but retaining a rare medical condition in a small geographic area

**Mitigation techniques**: k-anonymity (ensure at least k individuals share each combination of quasi-identifiers), aggregation to sufficiently large groups

### Criterion 2: Linkability

**Definition**: The ability to link at least two records concerning the same data subject or a group of data subjects, either within the same dataset or between two separate datasets.

**Test**: Can records be combined across datasets to build a profile of an individual?

**Examples of failure**:
- A hashed email address that can be matched across two datasets released by the same controller
- A dataset with date of birth, postcode, and hospital visit date that can be linked to public voter registration records
- Transaction patterns that can be matched with social media activity timestamps

**Mitigation techniques**: l-diversity, t-closeness, differential privacy noise addition, removing linkable quasi-identifiers

### Criterion 3: Inference

**Definition**: The possibility of deducing, with significant probability, the value of an attribute from the values of a set of other attributes.

**Test**: Can sensitive information about an individual be inferred from the released data?

**Examples of failure**:
- A dataset shows that all patients in a particular age-postcode group have the same diagnosis
- Salary data for a small department where only one person holds a particular role
- Aggregate statistics with small cell sizes that reveal individual values

**Mitigation techniques**: t-closeness (ensure attribute value distribution in each equivalence class is close to the overall distribution), differential privacy, cell suppression for small groups

### Assessment Matrix

| Criterion | Passes? | Overall Anonymisation Status |
|-----------|---------|----------------------------|
| Singling out: NOT possible | Linkability: NOT possible | Inference: NOT possible → **ANONYMISED** |
| Singling out: possible | Any | Any → **NOT anonymised (personal data)** |
| Any | Linkability: possible | Any → **NOT anonymised (personal data)** |
| Any | Any | Inference: possible → **NOT anonymised (personal data)** |

All three criteria must be satisfied for data to qualify as anonymised.

## The Motivated Intruder Test (ICO)

The ICO supplements the WP29 framework with the "motivated intruder" test:

**The motivated intruder is**:
- A person who starts without any prior knowledge of the data subject
- Has access to the dataset and to publicly available resources (internet, public registers, social media, published statistics)
- Has reasonable competence and motivation to re-identify (not a specialist)
- Does NOT have access to specialist equipment, techniques, or insider knowledge
- Would invest reasonable time and effort (days, not months)

**If the motivated intruder could re-identify any individual**: the data is NOT anonymised.

This test provides a practical complement to the WP29 criteria by establishing a baseline attacker model for the "reasonably likely means" assessment under Recital 26.

## Anonymisation Techniques — Effectiveness Assessment

### Technique 1: Randomisation (Noise Addition)

| Approach | Description | Singling Out | Linkability | Inference |
|----------|-------------|-------------|-------------|-----------|
| Noise addition | Add random values to numerical attributes | Reduced | Reduced | Reduced |
| Permutation | Shuffle values across records within groups | Mitigated (within group) | Reduced | Reduced |
| Differential privacy | Add calibrated noise to query results | Provably mitigated (with epsilon budget) | Provably mitigated | Provably mitigated |

### Technique 2: Generalisation

| Approach | Description | Singling Out | Linkability | Inference |
|----------|-------------|-------------|-------------|-----------|
| k-anonymity | Ensure each combination of quasi-identifiers applies to at least k records | Mitigated (k ≥ 5 recommended) | Not addressed | Not addressed |
| l-diversity | Within each k-anonymous group, ensure at least l distinct values for sensitive attributes | Mitigated | Partially mitigated | Reduced |
| t-closeness | Ensure distribution of sensitive attribute in each group is within distance t of overall distribution | Mitigated | Reduced | Mitigated |
| Aggregation | Replace individual records with group statistics | Mitigated (if groups large enough) | Mitigated | Residual risk with small groups |

### Technique 3: Suppression

| Approach | Description | Singling Out | Linkability | Inference |
|----------|-------------|-------------|-------------|-----------|
| Record suppression | Remove outlier records | Reduces unique records | No effect on remaining | No effect on remaining |
| Cell suppression | Replace small cell values with null/range | Reduces singling out for small groups | No direct effect | Reduces inference from small cells |
| Attribute suppression | Remove entire columns (direct identifiers, high-risk quasi-identifiers) | Reduces identifiability | Reduces cross-dataset linkage | No direct effect |

### WP29 Effectiveness Summary (from Opinion 05/2014, Section 4)

| Technique | Singling Out | Linkability | Inference | Recommended Use |
|-----------|-------------|-------------|-----------|----------------|
| Pseudonymisation (tokenisation, hashing) | Still possible | Still possible | Still possible | **NOT anonymisation** — remains personal data |
| k-anonymity alone | Partially mitigated | NOT mitigated | NOT mitigated | Insufficient alone |
| l-diversity | Mitigated | Partially mitigated | Partially mitigated | Stronger than k-anonymity |
| Differential privacy | Provably mitigated | Provably mitigated | Provably mitigated | Strongest formal guarantee |
| Aggregation + suppression | Mitigated | Mitigated | Residual | Suitable for statistical outputs |

## Decision Framework for Classification

```
Data has undergone a de-identification process
  │
  ├─► Step 1: Does a re-identification key exist?
  │     YES → PSEUDONYMISED (personal data, GDPR applies)
  │     NO  → Continue to Step 2
  │
  ├─► Step 2: Apply WP29 Three-Criteria Test
  │     2a. Singling out test — can any individual be isolated?
  │     2b. Linkability test — can records be linked to an individual?
  │     2c. Inference test — can attributes be inferred for an individual?
  │
  │     ANY test fails → NOT anonymised (personal data, GDPR applies)
  │     ALL tests pass → Continue to Step 3
  │
  ├─► Step 3: Apply Motivated Intruder Test (ICO)
  │     Could a motivated person with public resources re-identify anyone?
  │     YES → NOT anonymised
  │     NO  → Continue to Step 4
  │
  ├─► Step 4: Breyer Relative Assessment
  │     Does the specific data controller have legal means to obtain
  │     complementary data enabling identification? (per C-582/14)
  │     YES → NOT anonymised FOR THIS CONTROLLER
  │     NO  → Continue to Step 5
  │
  └─► Step 5: Technology Projection
        Over the intended retention period, are technological developments
        reasonably anticipated that would enable re-identification?
        YES → NOT anonymised (or must be re-assessed before technology matures)
        NO  → ANONYMISED — GDPR does not apply

        CLASSIFICATION: ANONYMISED
        Document: technique used, assessment reasoning, review date,
        assessor, technology projection horizon
```

## CJEU Case C-413/23 — European Data Protection Supervisor v Single Resolution Board (Pending)

In 2023, the CJEU was asked to rule on whether pseudonymised data transmitted to a recipient who does not have the re-identification key constitutes personal data for that recipient. Advocate General Szpunar's opinion (September 2024) suggested a relative approach — if the recipient cannot reasonably re-identify, the data may not be personal data for them. This case, when decided, may significantly impact the pseudonymisation vs anonymisation boundary by establishing that the same dataset can be pseudonymised (personal data) for the data holder and effectively anonymous for a recipient without the key.

## Implementation at Vanguard Financial Services

### Common Pseudonymisation Scenarios

| Scenario | Technique | Classification | Reasoning |
|----------|-----------|---------------|-----------|
| Customer analytics dataset with account IDs replaced by random tokens | Tokenisation | PSEUDONYMISED | Vanguard holds the token-to-account mapping table |
| Employee survey responses with employee IDs removed but department and role retained | Attribute suppression + quasi-identifiers remain | PSEUDONYMISED (likely) | Unique department-role combinations may enable singling out for small departments |
| Aggregated website traffic statistics: page views by week, no user identifiers | Aggregation | ANONYMISED (if cell sizes adequate) | No individual can be singled out from aggregate page view counts with >1000 visitors per cell |
| Hashed customer emails for analytics | Hashing (SHA-256) | PSEUDONYMISED | Hash can be reversed via dictionary attack or rainbow table; same email always produces same hash, enabling linkage |

### Anonymisation Validation Process

Before classifying data as anonymised, Vanguard requires:
1. Written anonymisation assessment documenting technique applied and WP29 three-criteria evaluation
2. Motivated intruder test conducted by Privacy Engineering team
3. DPO review and sign-off
4. Annual reassessment (technology evolution check)
5. If data is shared externally: assessment from recipient's perspective (Breyer relative approach)

## Enforcement Precedents

- **Breyer v Bundesrepublik Deutschland (CJEU C-582/14, 2016)**: Established relative approach to identifiability — central to distinguishing pseudonymised (identifiable) from anonymised (not identifiable) for a specific controller
- **CNIL — Practical Guide on Anonymisation (2019)**: CNIL rejected k-anonymity alone as sufficient for anonymisation, requiring assessment against all three WP29 criteria
- **Austrian DPA — 1&1 Telecom case (2019)**: EUR 9.55 million fine partly related to inadequate pseudonymisation measures — telephone customer service could identify callers with minimal verification, demonstrating pseudonymisation was ineffective

## Integration Points

- **personal-data-test**: Pseudonymised data is personal data; anonymised data is not — classification feeds the Art. 4(1) test
- **classification-policy**: Pseudonymised data classified as Internal or Confidential; anonymised data classified as Public or Internal
- **ai-training-data-class**: AI training datasets frequently use pseudonymisation; this skill validates whether the technique achieves true anonymisation
- **data-lineage-tracking**: Lineage must track the anonymisation transformation and preserve the assessment record
