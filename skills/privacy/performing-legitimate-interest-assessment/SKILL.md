---
name: performing-legitimate-interest-assessment
description: >-
  Guides the three-part Legitimate Interest Assessment (LIA) required under GDPR
  Article 6(1)(f): purpose test, necessity test, and balancing test. Activate when
  evaluating legitimate interest as a lawful basis, conducting LIA reviews, or
  documenting proportionality analysis. Keywords: LIA, legitimate interest,
  balancing test, necessity test, purpose test, Article 6(1)(f).
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: gdpr-compliance
  tags: "gdpr, legitimate-interest, lia, balancing-test, article-6, proportionality"
---

# Performing Legitimate Interest Assessment

## Overview

When a controller relies on Art. 6(1)(f) as the lawful basis for processing, a Legitimate Interest Assessment (LIA) must be conducted and documented before processing begins. The LIA consists of three sequential tests derived from the wording of Art. 6(1)(f) and elaborated in WP29 Opinion 06/2014. If any test fails, legitimate interest cannot be relied upon, and an alternative lawful basis must be found or processing must not proceed.

## Part 1: Purpose Test

The purpose test establishes whether the controller (or a third party) has a legitimate interest that is real, lawful, and clearly articulated.

### Assessment Criteria

1. **Identify the interest**: What specific interest does the controller or third party pursue? The interest must be concrete and articulated, not vague or hypothetical.

2. **Verify legitimacy**: The interest must be:
   - Lawful (not prohibited by any law)
   - Sufficiently specific to be assessed
   - Real and present (not speculative or future)
   - Consistent with what data subjects would reasonably expect

3. **Common legitimate interests recognised by the GDPR**:
   - Fraud prevention (Recital 47)
   - Direct marketing to existing customers (Recital 47)
   - Network and information security (Recital 49)
   - Intra-group transfers for internal administrative purposes (Recital 48)
   - Reporting possible criminal acts or threats to public security (Recital 50)

4. **Document the interest**: State the interest in a single clear sentence that could be understood by a non-expert.

### Purpose Test Outcome

- **PASS**: A legitimate interest has been clearly identified and is lawful.
- **FAIL**: No legitimate interest can be articulated, or the interest is prohibited by law. Stop the assessment — Art. 6(1)(f) cannot be relied upon.

## Part 2: Necessity Test

The necessity test determines whether the specific processing is necessary to achieve the identified legitimate interest. This is not a test of whether the interest itself is necessary, but whether the processing is necessary for the interest.

### Assessment Criteria

1. **Could the interest be achieved without processing personal data?** If the same outcome can be reached without personal data, the processing fails the necessity test.

2. **Could the interest be achieved with less personal data?** Apply data minimisation — only the minimum data necessary should be processed.

3. **Could the interest be achieved with a less intrusive method?** Consider alternatives:
   - Anonymisation or aggregation instead of identifiable data
   - Pseudonymisation to reduce impact
   - Shorter retention periods
   - More limited sharing
   - Technical restrictions on access

4. **Is the processing proportionate to the interest?** The scope and intensity of processing should be proportionate to the significance of the interest.

### Necessity Test Outcome

- **PASS**: The processing is necessary for the legitimate interest, no less intrusive alternative achieves the same result, and the scope is proportionate.
- **FAIL**: A less intrusive alternative exists, or the processing scope exceeds what is necessary. Modify the processing to meet the necessity test, or stop — Art. 6(1)(f) cannot be relied upon.

## Part 3: Balancing Test

The balancing test weighs the controller's legitimate interest against the interests, fundamental rights, and freedoms of data subjects. This is the most complex and contextual part of the LIA.

### Factors Favouring the Controller

- The interest is strong and compelling (e.g., fraud prevention, security)
- Processing has minimal impact on data subjects
- Data subjects would reasonably expect the processing
- There is an existing relationship between controller and data subject
- Robust safeguards are in place (pseudonymisation, encryption, access controls)
- Data subjects have an easy and effective opt-out mechanism
- Processing uses non-sensitive data
- Data is not shared with third parties
- The controller is transparent about the processing

### Factors Favouring the Data Subject

- Special category or sensitive data is involved (even if not Art. 9 data, sensitivity matters)
- Data subjects are vulnerable (children, employees, patients, elderly)
- Processing has significant impact on data subjects (profiling, automated decisions, financial consequences)
- Data subjects would not reasonably expect the processing
- There is no direct relationship between controller and data subject
- Data is shared widely or with third parties
- Processing involves large-scale monitoring or tracking
- No opt-out mechanism is provided
- Data is combined from multiple sources to create profiles

### Balancing Methodology

1. **Assess the nature of the interest**: How important is the controller's interest? Rate from routine (low) to essential (high).

2. **Assess the impact on data subjects**: What is the likely effect? Consider:
   - Physical, material, or financial harm
   - Social disadvantage or discrimination
   - Loss of control over personal data
   - Reputational effects
   - Psychological impact

3. **Consider reasonable expectations**: Would data subjects expect their data to be used this way? The closer the processing is to the original context and the existing relationship, the more likely it meets expectations.

4. **Evaluate additional safeguards**: Do safeguards sufficiently mitigate the impact? Effective safeguards can tip the balance in the controller's favour.

5. **Consider the possibility of objection**: Is there a mechanism for data subjects to object under Art. 21? The right to object is a mandatory counterbalance when relying on Art. 6(1)(f).

### Balancing Test Outcome

- **PASS**: The controller's legitimate interest is not overridden by the data subject's interests, rights, and freedoms, taking into account all relevant factors and safeguards.
- **FAIL**: The data subject's rights outweigh the controller's interest. Consider additional safeguards that could tip the balance, or use a different lawful basis (typically consent), or do not process.

## Documentation Requirements

The completed LIA must document:

1. **Assessment metadata**: Date, assessor, processing activity, RoPA reference.
2. **Purpose test**: The identified interest, evidence of legitimacy, outcome.
3. **Necessity test**: Analysis of alternatives, proportionality, outcome.
4. **Balancing test**: Factors considered, weighting rationale, safeguards, outcome.
5. **Overall conclusion**: Whether Art. 6(1)(f) can be relied upon.
6. **Safeguards committed**: Specific measures to mitigate data subject impact.
7. **Right to object**: How the Art. 21 right to object is facilitated.
8. **Review schedule**: When the LIA will be reassessed.

## Reassessment Triggers

- Material change in processing scope, purpose, or data categories
- Change in the relationship with data subjects
- New technology or methodology introduced
- Supervisory authority guidance or enforcement action relevant to the processing
- Data subject complaints challenging the legitimate interest basis
- Periodic review (minimum annual)
