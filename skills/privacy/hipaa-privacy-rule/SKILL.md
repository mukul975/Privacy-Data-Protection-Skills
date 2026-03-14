---
name: hipaa-privacy-rule
description: >-
  Implements HIPAA Privacy Rule requirements under 45 CFR §164.500-534 for
  covered entities and business associates. Covers minimum necessary standard,
  treatment-payment-operations exceptions, directory opt-out, personal
  representative rules, and authorization requirements. Keywords: HIPAA Privacy
  Rule, PHI, minimum necessary, TPO, authorization, covered entity.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: healthcare-privacy
  tags: "hipaa, privacy-rule, phi, minimum-necessary, tpo, authorization, covered-entity, healthcare"
---

# HIPAA Privacy Rule — 45 CFR §164.500-534

## Overview

The HIPAA Privacy Rule establishes national standards for the protection of individually identifiable health information — Protected Health Information (PHI) — held by covered entities and their business associates. Enacted under the Health Insurance Portability and Accountability Act of 1996 and finalized in the Privacy Rule of 2000 (with major modifications in 2002 and 2013 under HITECH/Omnibus), the rule balances patient privacy rights with the practical needs of healthcare delivery. The Privacy Rule applies to health plans, healthcare clearinghouses, and healthcare providers who transmit any health information electronically in connection with a HIPAA-covered transaction.

## Covered Entities and Business Associates

### Who Is a Covered Entity

Under 45 CFR §160.103, covered entities include:

| Entity Type | Definition | Examples |
|-------------|-----------|----------|
| Healthcare Provider | Any provider who transmits health information electronically in connection with a covered transaction | Hospitals, physician practices, pharmacies, laboratories, dentists, chiropractors |
| Health Plan | Individual or group plan that provides or pays for medical care | Health insurers, HMOs, employer-sponsored health plans, government programs (Medicare, Medicaid, TRICARE) |
| Healthcare Clearinghouse | Entity that processes nonstandard health information into standard format | Billing services, repricing companies, community health management information systems |

### Asclepius Health Network Example

Asclepius Health Network operates as a covered entity comprising 12 hospitals, 85 outpatient clinics, and an affiliated health plan. Every workforce member — from attending physicians to front desk staff — must comply with the Privacy Rule. Asclepius designates its Chief Privacy Officer to manage rule implementation across all facilities.

## Protected Health Information (PHI)

### Definition

PHI is individually identifiable health information that is transmitted or maintained in any form or medium by a covered entity or business associate. Under 45 CFR §160.103, individually identifiable health information is information that:

1. Is created or received by a healthcare provider, health plan, employer, or healthcare clearinghouse
2. Relates to the past, present, or future physical or mental health or condition of an individual, the provision of healthcare to an individual, or payment for healthcare
3. Identifies the individual or provides a reasonable basis to believe the individual can be identified

### What PHI Includes

PHI encompasses information in any form — electronic (ePHI), paper, or oral. The 18 identifiers defined in §164.514(b)(2) include:

1. Names
2. Geographic data smaller than state (street address, city, county, ZIP code — first 3 digits allowed if population > 20,000)
3. Dates related to the individual (birth, admission, discharge, death — year alone is permitted)
4. Telephone numbers
5. Fax numbers
6. Email addresses
7. Social Security numbers
8. Medical record numbers
9. Health plan beneficiary numbers
10. Account numbers
11. Certificate/license numbers
12. Vehicle identifiers and serial numbers including license plates
13. Device identifiers and serial numbers
14. Web URLs
15. IP addresses
16. Biometric identifiers (fingerprints, voiceprints)
17. Full-face photographs and comparable images
18. Any other unique identifying number, characteristic, or code

### Exclusions

PHI does not include:

- Education records covered by FERPA
- Employment records held by a covered entity in its role as employer
- De-identified data meeting §164.514(a)-(b) standards

## Uses and Disclosures of PHI

### Permitted Uses Without Authorization

The Privacy Rule permits uses and disclosures of PHI without individual authorization in the following circumstances:

#### Treatment, Payment, and Healthcare Operations (TPO) — §164.506

TPO is the primary exception enabling routine healthcare delivery:

**Treatment (§164.501)**: The provision, coordination, or management of healthcare and related services by one or more healthcare providers. Includes consultation between providers, referrals, and provider-to-provider communication about a patient.

At Asclepius Health Network, a cardiologist may share a patient's echocardiogram results with the referring primary care physician without patient authorization because this constitutes treatment.

**Payment (§164.501)**: Activities by a covered entity or its business associate to obtain or provide reimbursement for healthcare. Includes eligibility determinations, billing, claims management, utilization review, and collection activities.

Asclepius Health Network's billing department may submit a patient's diagnosis codes and procedure codes to the patient's health insurer for claim adjudication without patient authorization.

**Healthcare Operations (§164.501)**: Activities including quality assessment, competency assurance, conducting or arranging medical review, legal services, auditing, business planning, customer service, resolution of internal grievances, compliance activities, and limited de-identified data analysis.

#### Public Interest and Benefit Activities — §164.512

| Activity | CFR Section | Requirements |
|----------|-------------|--------------|
| Required by law | §164.512(a) | Disclosure compelled by statute, regulation, or court order |
| Public health | §164.512(b) | To public health authorities for disease prevention, FDA reporting, workplace safety |
| Victims of abuse/neglect | §164.512(c) | To government authority authorized to receive reports |
| Health oversight | §164.512(d) | To health oversight agencies for audits, investigations, inspections |
| Judicial proceedings | §164.512(e) | In response to court order or qualified protective order with subpoena |
| Law enforcement | §164.512(f) | Pursuant to process, limited circumstances (identification, crime on premises, emergency) |
| Decedents | §164.512(g) | To coroners, medical examiners, funeral directors |
| Organ donation | §164.512(h) | To organ procurement organizations |
| Research | §164.512(i) | With IRB/Privacy Board waiver of authorization, preparatory to research, or decedent research |
| Serious threat | §164.512(j) | To prevent or lessen serious and imminent threat to health or safety |
| Essential government functions | §164.512(k) | Military, veterans, national security, intelligence, protective services |
| Workers' compensation | §164.512(l) | As authorized by workers' compensation laws |

### Uses and Disclosures Requiring Authorization — §164.508

An authorization is required for:

- Uses and disclosures of psychotherapy notes (§164.508(a)(2))
- Uses and disclosures for marketing purposes (§164.508(a)(3))
- Sale of PHI (§164.508(a)(4))
- Any use or disclosure not otherwise permitted or required by the Privacy Rule

#### Valid Authorization Requirements

A valid authorization under §164.508(c) must contain:

1. A specific and meaningful description of the information to be used or disclosed
2. The name or specific identification of the person(s) authorized to make the use or disclosure
3. The name or specific identification of the person(s) to whom the disclosure may be made
4. A description of each purpose of the use or disclosure ("at the request of the individual" is sufficient)
5. An expiration date or event
6. The individual's signature and date
7. If signed by a personal representative, a description of the representative's authority

Required statements on the authorization form:

- Right to revoke the authorization in writing
- Ability or inability to condition treatment, payment, enrollment, or eligibility on the authorization
- Potential for re-disclosure by the recipient (no longer protected by HIPAA)

## Minimum Necessary Standard — §164.502(b)

### General Requirement

Covered entities must make reasonable efforts to limit PHI to the minimum necessary to accomplish the intended purpose of the use, disclosure, or request. This is one of the most frequently cited and enforced provisions.

### Exceptions to Minimum Necessary

The minimum necessary standard does NOT apply to:

1. Disclosures to or requests by a healthcare provider for treatment purposes
2. Disclosures to the individual who is the subject of the PHI
3. Uses or disclosures made pursuant to a valid authorization
4. Disclosures to HHS for compliance investigation or enforcement
5. Uses or disclosures required by law
6. Uses or disclosures required for HIPAA Administrative Simplification compliance

### Implementation at Asclepius Health Network

Asclepius Health Network implements the minimum necessary standard through:

**Workforce Access**: Role-based access controls defining the categories of PHI each workforce member role needs. Emergency department nurses access current visit records, vital signs, allergies, and medication lists. Billing staff access demographic information, insurance details, diagnosis codes, and procedure codes — not clinical notes.

**Routine Disclosures**: For routine, recurring disclosures, Asclepius maintains standard protocols limiting information provided. For insurance eligibility verification, only the patient name, date of birth, insurance ID, and requested service dates are transmitted.

**Non-Routine Disclosures**: For non-routine disclosures, each request is reviewed on a case-by-case basis by the Privacy Office. The reviewer applies the minimum necessary principle and documents the rationale for the scope of disclosure.

## Individual Rights

### Right of Access — §164.524

Individuals have the right to inspect and obtain a copy of PHI maintained in a designated record set, with limited exceptions:

- **Timeframe**: Covered entity must act on a request within 30 days (one 30-day extension permitted with written explanation)
- **Format**: If requested, PHI must be provided in electronic form if readily producible
- **Fees**: Limited to reasonable, cost-based fees for labor for copying, supplies, and postage (not retrieval or search)
- **Denial grounds**: Psychotherapy notes, information compiled for legal proceedings, lab results subject to CLIA, inmates if access would jeopardize health/safety, research participant during study if agreed upon enrollment

Asclepius Health Network provides patient portal access to electronic health records. Patients who request additional records receive them within 15 business days. Asclepius charges $6.50 per electronic copy (flat fee covering labor and transmission).

### Right to Amend — §164.526

Individuals may request amendment of PHI in a designated record set. The covered entity may deny if the information:

- Was not created by the covered entity (unless the originator is no longer available)
- Is not part of the designated record set
- Would not be available for access under §164.524
- Is accurate and complete

If denied, the individual may submit a statement of disagreement appended to the record.

### Right to an Accounting of Disclosures — §164.528

Individuals have the right to receive an accounting of disclosures made by the covered entity in the six years prior to the request. Exceptions include disclosures:

- For treatment, payment, or healthcare operations
- To the individual
- Pursuant to an authorization
- For the facility's directory or to persons involved in care
- For national security or intelligence purposes
- To correctional institutions or law enforcement in custody situations
- Part of a limited data set
- That occurred before the Privacy Rule compliance date

### Right to Request Restrictions — §164.522(a)

Individuals may request restrictions on uses and disclosures for TPO. The covered entity is NOT required to agree to the restriction, except:

- **Mandatory restriction**: If the individual pays out of pocket in full for a healthcare item or service, the covered entity MUST agree to restrict disclosure to a health plan for payment or healthcare operations purposes (added by HITECH §13405(a))

### Right to Request Confidential Communications — §164.522(b)

Individuals may request that communications be sent by alternative means or to alternative locations. Healthcare providers must accommodate reasonable requests. Health plans must accommodate when the individual states that disclosure could endanger them.

### Right to Receive Notice of Privacy Practices — §164.520

Covered entities must provide a Notice of Privacy Practices (NPP) that describes:

- How PHI may be used and disclosed
- The individual's rights regarding PHI
- The covered entity's legal duties
- Whom to contact for further information
- How to file complaints

**Distribution**: Healthcare providers with a direct treatment relationship must provide the NPP at first service delivery and make a good faith effort to obtain written acknowledgment. Health plans must provide at enrollment and within 60 days of material revision.

## Directory Opt-Out — §164.510(a)

Covered entities that maintain a facility directory may include limited PHI (patient name, location in facility, general condition, religious affiliation) for directory purposes. The individual must be:

1. Informed in advance of the PHI to be included
2. Given the opportunity to restrict or prohibit some or all uses
3. Allowed to opt out entirely

If the individual is incapacitated or unavailable, the covered entity may include directory information if consistent with any prior expressed preference and if disclosure is in the individual's best interest as determined by professional judgment.

At Asclepius Health Network, patients are asked at registration whether they wish to be listed in the facility directory. Those who opt out are flagged in the admissions system, and all staff are instructed that no information may be provided to callers or visitors.

## Personal Representatives — §164.502(g)

A personal representative must be treated as the individual for purposes of the Privacy Rule if the representative has authority under applicable law to act on behalf of the individual in making healthcare decisions:

| Individual | Personal Representative | Authority Basis |
|-----------|----------------------|-----------------|
| Adult | Person with healthcare power of attorney | State healthcare POA statute |
| Minor (general) | Parent, guardian, or person acting in loco parentis | State law on parental authority |
| Minor (exceptions) | Minor acts as own representative | State law permitting minor consent (STI treatment, substance abuse, reproductive health) |
| Deceased individual | Executor, administrator, or person with legal authority over estate | State probate law |
| Adult lacking capacity | Court-appointed guardian or person authorized under state law | State guardianship statute |

**Abuse/neglect exception**: A covered entity may decline to treat a person as a personal representative if the covered entity reasonably believes the individual has been or may be subject to domestic violence, abuse, or neglect by the representative, and treating them as representative is not in the individual's best interest.

## Enforcement and Penalties

### OCR Enforcement

The HHS Office for Civil Rights (OCR) enforces the Privacy Rule through:

- Complaint investigations
- Compliance reviews
- Technical assistance and guidance

### Civil Monetary Penalties (as amended by HITECH)

| Tier | Culpability Level | Per Violation | Annual Maximum |
|------|------------------|---------------|----------------|
| 1 | Did not know (and would not have known with reasonable diligence) | $137–$68,928 | $2,067,813 |
| 2 | Reasonable cause, not willful neglect | $1,379–$68,928 | $2,067,813 |
| 3 | Willful neglect, corrected within 30 days | $13,785–$68,928 | $2,067,813 |
| 4 | Willful neglect, not corrected | $68,928–$2,067,813 | $2,067,813 |

Penalty amounts are adjusted annually for inflation per 45 CFR §160.404.

### Notable Enforcement Actions

- **Anthem Inc. (2018)**: $16 million settlement — largest HIPAA settlement — for breach affecting 78.8 million individuals. Findings included insufficient access controls and failure to conduct enterprise-wide risk analysis.
- **Premera Blue Cross (2020)**: $6.85 million settlement for breach of 10.4 million records due to failure to conduct risk analysis and implement adequate security controls.
- **Banner Health (2023)**: $1.25 million settlement for breach affecting over 2.81 million individuals. OCR found failure to conduct accurate risk analysis and implement audit controls.

## Integration Points

- **hipaa-security-rule**: Technical safeguards implementing the Privacy Rule's ePHI protections
- **hipaa-minimum-necessary**: Detailed implementation of the minimum necessary standard
- **hipaa-breach-notify**: Breach notification obligations when Privacy Rule violations result in unauthorized disclosure
- **hipaa-baa-management**: Business associate obligations under the Privacy Rule
- **hipaa-deidentification**: Methods for de-identifying PHI to remove it from Privacy Rule scope
