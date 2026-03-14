---
name: restriction-of-processing
description: >-
  Handles GDPR Article 18 right to restriction of processing requests, covering
  the four grounds for restriction (accuracy contest, unlawful processing,
  erasure opposition, legitimate interest pending), technical flagging mechanisms,
  and lifting procedures. Activate for restriction request, Art. 18, processing freeze queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-subject-rights
  tags: "right-to-restriction, gdpr-article-18, processing-freeze, data-flagging, restriction-of-processing"
---

# Handling Right to Restriction Requests

## Overview

The right to restriction of processing under GDPR Article 18 allows data subjects to request that a controller limits the processing of their personal data in specific circumstances. When restriction is applied, data may be stored but not otherwise processed without the data subject's consent or for limited specified purposes. This skill provides the complete workflow for assessing, implementing, and managing restriction requests.

## Legal Foundation

### GDPR Article 18 — Right to Restriction of Processing

#### Four Grounds for Restriction Under Art. 18(1)

1. **Art. 18(1)(a) — Accuracy contested**: The data subject contests the accuracy of the personal data, for a period enabling the controller to verify the accuracy of the personal data.
2. **Art. 18(1)(b) — Unlawful processing, erasure opposed**: The processing is unlawful and the data subject opposes the erasure of the personal data and requests the restriction of their use instead.
3. **Art. 18(1)(c) — Erasure opposition for legal claims**: The controller no longer needs the personal data for the purposes of the processing, but they are required by the data subject for the establishment, exercise, or defence of legal claims.
4. **Art. 18(1)(d) — Objection pending verification**: The data subject has objected to processing under Art. 21(1) pending the verification whether the legitimate grounds of the controller override those of the data subject.

### Processing Permitted During Restriction (Art. 18(2))

When processing has been restricted, the personal data may only be processed:
- With the data subject's **consent**, OR
- For the **establishment, exercise, or defence of legal claims**, OR
- For the **protection of the rights of another natural or legal person**, OR
- For reasons of **important public interest** of the Union or a Member State.

### GDPR Article 19 — Notification Obligation

The controller must notify each recipient to whom the personal data have been disclosed of the restriction, unless this proves impossible or involves disproportionate effort.

### Lifting the Restriction (Art. 18(3))

A data subject who has obtained restriction of processing shall be informed by the controller before the restriction of processing is lifted.

## Restriction Processing Workflow

### Step 1: Receive and Log the Request

1. Log the request with reference RST-YYYY-NNNN.
2. Record the channel, timestamp (UTC), and identity of the requester.
3. Send acknowledgement within 3 business days.
4. Verify identity using tiered verification.

### Step 2: Identify the Ground for Restriction

Determine which of the four grounds applies:

| Ground | Trigger | Duration | Resolution |
|--------|---------|----------|------------|
| Art. 18(1)(a) — Accuracy contested | Data subject disputes data accuracy | Until accuracy verified | Verified accurate: lift restriction. Verified inaccurate: rectify under Art. 16 and lift. |
| Art. 18(1)(b) — Unlawful processing, erasure opposed | Processing found unlawful but subject prefers restriction over deletion | Indefinite until subject consents to erasure or processing becomes lawful | Subject requests erasure or lawful basis established. |
| Art. 18(1)(c) — Needed for legal claims | Controller no longer needs data but subject requires it for legal proceedings | Duration of legal proceedings | Legal proceedings concluded or subject no longer requires data. |
| Art. 18(1)(d) — Objection pending | Subject objects under Art. 21(1), assessment pending | Until Art. 21 assessment complete | Legitimate grounds assessment: controller overrides = lift restriction + inform subject. Subject's grounds prevail = erase under Art. 17(1)(c). |

### Step 3: Implement Technical Restriction

Apply a technical flagging mechanism to prevent processing of the restricted data:

#### Database-Level Flags

1. Set a `restriction_flag` field to `TRUE` on all records associated with the data subject.
2. Set a `restriction_date` timestamp.
3. Set a `restriction_ground` value (one of: `accuracy_contested`, `unlawful_opposed`, `legal_claims`, `objection_pending`).
4. Set a `restriction_reference` value linking to the request (RST-YYYY-NNNN).

#### Application-Level Controls

1. **Query filters**: Modify application queries to exclude records where `restriction_flag = TRUE` from all standard processing operations.
2. **API access controls**: Return HTTP 423 (Locked) or filtered results when restricted data is requested through APIs used for standard processing.
3. **Batch processing exclusions**: Add restriction checks to all ETL, reporting, and analytics pipelines.
4. **User interface masking**: Display restricted records with a visual indicator (e.g., "RESTRICTED — Processing Limited") in internal tools. Prevent editing or use of restricted data.

#### Storage Isolation (Recommended for High-Risk Data)

1. Move restricted records to a separate restricted data store or partition.
2. Apply access controls limiting access to the DPO and Legal team only.
3. Log all access to restricted data with justification.

### Step 4: Permitted Processing Assessment

When any team needs to process restricted data, they must complete a permitted processing assessment:

1. **Consent**: Has the data subject provided specific consent for this particular processing activity during the restriction period? Document the consent.
2. **Legal claims**: Is the processing necessary for the establishment, exercise, or defence of legal claims by the controller or a third party? Identify the specific claim.
3. **Protection of rights**: Is the processing necessary to protect the rights of another natural or legal person? Identify the person and right.
4. **Public interest**: Is the processing required for reasons of important public interest? Identify the specific public interest basis.

Any processing of restricted data outside these four purposes is a compliance violation.

### Step 5: Notify Third-Party Recipients (Art. 19)

1. Identify all recipients to whom the restricted data was previously disclosed.
2. Send restriction notification to each recipient:
   - Data subject reference (pseudonymised)
   - Data categories subject to restriction
   - Restriction ground (without disclosing details that would identify the subject's reason)
   - Instruction to cease processing except for permitted purposes
   - Request confirmation within 14 calendar days
3. Log all notifications and confirmations.

### Step 6: Monitor and Resolve

1. Set a review date based on the restriction ground:
   - **Accuracy contested**: Review within 15 business days (or as long as accuracy verification requires).
   - **Unlawful processing**: Review quarterly or upon data subject request.
   - **Legal claims**: Review upon conclusion of legal proceedings (liaise with Legal team quarterly).
   - **Objection pending**: Complete Art. 21 assessment within 20 business days.
2. When the restriction is to be lifted:
   - **Notify the data subject before lifting** (Art. 18(3)) with at least 7 calendar days' notice.
   - State the reason the restriction is being lifted.
   - Inform the data subject of their rights (including the right to object or request erasure).
3. Remove technical flags and restore normal processing access.
4. Notify third-party recipients that the restriction has been lifted.

### Step 7: Document and Close

1. Update the restriction register with:
   - Restriction applied date
   - Ground
   - Technical measures implemented
   - Third parties notified
   - Resolution date and outcome
   - Pre-lifting notification date
2. Retain the record for 3 years following resolution.

## Response Timeline

- **Standard deadline**: 30 calendar days from receipt of the request.
- **Extension**: Up to 60 additional days for complex cases (Art. 12(3)).
- **Technical implementation**: Restriction flags must be applied within 72 hours of the decision to restrict, regardless of the response deadline.
