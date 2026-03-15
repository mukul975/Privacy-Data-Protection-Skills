---
name: right-to-object
description: >-
  Handles GDPR Article 21 right to object to processing, including compelling
  legitimate grounds assessment, ceasing processing obligations, documentation
  requirements, and the relationship with erasure under Article 17(1)(c).
  Activate for right to object, Art. 21, objection to processing, legitimate interest queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-subject-rights
  tags: "right-to-object, gdpr-article-21, legitimate-interest, objection-processing, cease-processing"
---

# Handling Right to Object to Processing

## Overview

The right to object under GDPR Article 21(1) allows data subjects to object to processing based on legitimate interests (Art. 6(1)(f)) or public interest/official authority (Art. 6(1)(e)), including profiling based on those provisions. Upon objection, the controller must cease processing unless it demonstrates compelling legitimate grounds that override the interests, rights, and freedoms of the data subject, or processing is necessary for legal claims.

## Legal Foundation

### GDPR Article 21 — Right to Object

1. **Art. 21(1)** — The data subject has the right to object, on grounds relating to their particular situation, to processing based on Art. 6(1)(e) (public interest) or Art. 6(1)(f) (legitimate interests), including profiling based on those provisions. The controller shall no longer process the personal data unless it demonstrates compelling legitimate grounds for the processing which override the interests, rights, and freedoms of the data subject, or for the establishment, exercise, or defence of legal claims.

2. **Art. 21(2)-(3)** — [Covered separately in managing-direct-marketing-objection skill]

3. **Art. 21(4)** — At the latest at the time of the first communication with the data subject, the right to object shall be explicitly brought to the attention of the data subject and shall be presented clearly and separately from any other information.

4. **Art. 21(5)** — In the context of the use of information society services, the data subject may exercise their right to object by automated means using technical specifications.

5. **Art. 21(6)** — Where personal data are processed for scientific or historical research purposes or statistical purposes under Art. 89(1), the data subject has the right to object unless the processing is necessary for the performance of a task carried out for reasons of public interest.

### Relationship with Art. 17(1)(c) — Erasure Following Objection

Where the data subject successfully objects and there are no overriding legitimate grounds, the data subject also has the right to erasure under Art. 17(1)(c).

## Objection Processing Workflow

### Step 1: Receive and Log the Objection

1. Log with reference OBJ-YYYY-NNNN.
2. Record the specific processing activities objected to.
3. Record the data subject's particular situation and grounds.
4. Acknowledge receipt within 3 business days.
5. Verify identity.
6. **Immediately cease the objected-to processing** pending the compelling grounds assessment (apply restriction under Art. 18(1)(d)).

### Step 2: Identify the Processing and Its Legal Basis

1. Identify all processing activities covered by the objection.
2. Confirm that the legal basis for each activity is either:
   - Art. 6(1)(e) — Public interest / official authority, or
   - Art. 6(1)(f) — Legitimate interests
3. If the processing is based on a different legal basis (consent, contract, legal obligation), the right to object under Art. 21(1) does not apply. Inform the data subject of the applicable basis and suggest the appropriate right (e.g., withdrawal of consent under Art. 7(3)).

### Step 3: Compelling Legitimate Grounds Assessment

The controller must demonstrate that its legitimate grounds for processing are **compelling** and **override** the data subject's interests, rights, and freedoms. This is a higher bar than the standard legitimate interest assessment under Art. 6(1)(f).

#### Assessment Framework

| Factor | Controller's Position | Data Subject's Position |
|--------|----------------------|------------------------|
| Nature of the data | What categories? How sensitive? | Privacy impact of continued processing |
| Processing purpose | How critical is this processing to the controller's operations? | Alternative means available to the controller? |
| Impact on data subject | Minimal, moderate, or significant? | What specific harm or distress does the subject describe? |
| Number of affected individuals | Does cessation affect only this subject or others? | Individual circumstances cited by the subject |
| Safeguards in place | What measures mitigate the impact on the subject? | Are safeguards sufficient from the subject's perspective? |
| Vulnerability | N/A | Is the data subject in a vulnerable situation (child, employee, patient)? |
| Legal claims | Is the data needed for establishment, exercise, or defence of legal claims? | Is the subject's objection related to a legal dispute? |

#### Decision Criteria

- **Compelling grounds established**: The controller can continue processing, but must document the assessment in full and inform the data subject of the outcome and their right to complain.
- **Compelling grounds NOT established**: The controller must cease processing and inform the data subject. The data subject may also request erasure under Art. 17(1)(c).
- **Legal claims exception**: Processing may continue if necessary for legal claims, even without compelling grounds for the main processing purpose.

### Step 4: Implement the Decision

#### If Objection Upheld (No Compelling Grounds)

1. Cease all objected-to processing activities immediately.
2. Remove data from processing pipelines, analytics, and any automated systems.
3. Retain data only in restricted storage (if needed for legal compliance or other valid legal bases).
4. Notify third-party recipients under Art. 19.
5. Inform the data subject of their right to request erasure under Art. 17(1)(c).
6. Update privacy notices and records of processing to reflect the change.

#### If Objection Overridden (Compelling Grounds)

1. Resume the objected-to processing (or confirm it was never ceased, if the assessment was completed within the initial processing cycle).
2. Document the compelling legitimate grounds assessment in full.
3. Notify the data subject:
   - The specific compelling grounds identified
   - Why those grounds override the data subject's interests
   - The data subject's right to lodge a complaint with the supervisory authority (Art. 77)
   - The data subject's right to a judicial remedy (Art. 79)

### Step 5: Document and Close

1. Record the full assessment in the objection register.
2. Retain the record for 3 years.
3. If the objection is upheld, ensure all downstream systems reflect the cessation of processing.
4. Feed findings into the legitimate interest assessment register to inform future Art. 6(1)(f) reliance.

## Response Timeline

- **Standard deadline**: 30 calendar days from receipt.
- **Extension**: Up to 60 additional days for complex cases.
- **Processing cessation**: Must be implemented immediately upon receipt of the objection, pending the compelling grounds assessment. Processing may only resume if compelling grounds are demonstrated.
