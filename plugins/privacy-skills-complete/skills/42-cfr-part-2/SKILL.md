---
name: 42-cfr-part-2
description: >-
  Implements 42 CFR Part 2 protections for substance use disorder patient
  records. Covers written consent requirements stricter than HIPAA,
  re-disclosure prohibition, court order procedures, qualified service
  organization agreements, and 2024 amendments aligning Part 2 with HIPAA.
  Keywords: 42 CFR Part 2, substance use disorder, SUD records,
  re-disclosure, consent, Part 2 amendments.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: healthcare-privacy
  tags: "42-cfr-part-2, substance-use-disorder, sud-records, re-disclosure, consent, court-order"
---

# 42 CFR Part 2 — Substance Use Disorder Records

## Overview

42 CFR Part 2 establishes federal confidentiality protections for patient records created by federally assisted programs treating substance use disorders (SUDs). Originally enacted under the Comprehensive Alcohol Abuse and Alcoholism Prevention, Treatment, and Rehabilitation Act of 1970 and the Drug Abuse Prevention, Treatment, and Rehabilitation Act of 1972, Part 2 was designed to remove barriers to treatment by ensuring that SUD records could not be used to criminally prosecute or otherwise discriminate against patients. Part 2 is intentionally stricter than HIPAA — it requires specific written consent for most disclosures and prohibits re-disclosure by recipients. The CARES Act §3221 (enacted March 2020) and the subsequent 2024 Final Rule (89 FR 12472, effective February 16, 2024) significantly amended Part 2 to align certain provisions with HIPAA while preserving core patient protections.

## Applicability — Who Must Comply

### Part 2 Programs

Part 2 applies to any "program" that is federally assisted and holds itself out as providing, and provides, substance use disorder diagnosis, treatment, or referral for treatment. A program is federally assisted if it:

1. Is conducted by any department or agency of the United States (VA, IHS, military)
2. Is carried out under a license, certification, registration, or authorization from the federal government (DEA registration for opioid treatment programs)
3. Is supported by funds from any federal department or agency (Medicare/Medicaid participation qualifies)
4. Is assisted by the IRS through tax-exempt status under 26 USC §501(c)(3)
5. Is conducted by a state or local government receiving federal funds that could be used for SUD programs (even if not directly used for SUD)

**Asclepius Health Network Applicability**: Asclepius operates 3 dedicated SUD treatment facilities and provides SUD treatment services in all 12 hospitals. Because Asclepius participates in Medicare and Medicaid, all SUD treatment records are Part 2 records. Asclepius maintains a separate consent workflow for Part 2 records in its EHR.

### General Medical Facilities

A general medical facility (like a hospital ED) is a Part 2 program only with respect to an identified unit that holds itself out as providing SUD diagnosis, treatment, or referral. However, the 2024 amendments clarify that incidental SUD information in a general medical record (e.g., a note that a patient has a history of alcohol use disorder documented during a cardiac admission) is subject to Part 2 only if the information was obtained from a Part 2 program.

## What Records Are Protected — §2.12

Part 2 protects records that:

1. Would identify a patient as having or having had a substance use disorder
2. Are created by a Part 2 program (or received from a Part 2 program)
3. Contain SUD diagnosis, treatment, or referral information

The protections apply to **any information** that would identify an individual as a SUD patient, including the fact that the person is or was a patient in a Part 2 program.

## Consent Requirements — §2.31

### Written Consent Required

Unlike HIPAA, which permits disclosures for TPO without consent, Part 2 historically required specific written consent for virtually all disclosures. The 2024 amendments introduced a HIPAA-aligned consent-once model for TPO, but with important safeguards.

### Pre-2024 Consent Requirements (Still Applicable for Non-TPO Disclosures)

A valid Part 2 consent must include all of the following:

| Element | Requirement |
|---------|-------------|
| **Name of patient** | Full legal name of the patient |
| **Name of Part 2 program** | Specific program making the disclosure |
| **Recipient name** | Name or general designation of the person(s) or entity to whom disclosure is made |
| **Purpose** | The purpose of the disclosure must be specified |
| **Information to be disclosed** | How much and what kind of information is to be disclosed |
| **Patient signature** | Patient (or authorized representative) signature |
| **Date signed** | Date the consent was signed |
| **Revocability statement** | Statement that consent is subject to revocation at any time, except to the extent the program has already acted in reliance on it |
| **Expiration** | Date, event, or condition upon which consent will expire (if none, the consent must state it expires when the purpose is fulfilled) |
| **Re-disclosure prohibition notice** | Statement that information disclosed pursuant to consent may not be further disclosed unless permitted by Part 2 |

### 2024 Amendments — HIPAA-Aligned Consent for TPO

The 2024 Final Rule (89 FR 12472) introduced §2.33, allowing a single prior written consent for all future uses and disclosures for treatment, payment, and healthcare operations:

**Key Features of §2.33 Consent**:

- Patient may provide a single written consent covering all future TPO disclosures
- Consent covers disclosures to treating providers, payers, and entities performing healthcare operations
- Consent need not name each specific recipient — a general designation of recipient categories is sufficient (e.g., "my treating providers" or "my health plan")
- Consent does not expire unless the patient revokes it
- Patient retains the right to revoke at any time (revocation effective prospectively)
- Recipients remain bound by Part 2's anti-discrimination and limited use/disclosure restrictions

**Asclepius Health Network Implementation**: Asclepius offers patients a §2.33 TPO consent form at SUD program intake. Patients who sign the TPO consent have their Part 2 records flagged in the EHR for permitted sharing with treating providers and the patient's health plan. Patients who decline the TPO consent retain the traditional per-disclosure consent process. All consent decisions are documented in the EHR.

## Re-Disclosure Prohibition — §2.32

### The Core Part 2 Protection

Each disclosure of Part 2 records must be accompanied by the following notice:

> "This record which has been disclosed to you is protected by federal confidentiality rules (42 CFR Part 2). The federal rules prohibit you from making any further disclosure of information in this record that identifies a patient as having or having had a substance use disorder either directly, by reference to publicly available information, or through verification of such identification by another person unless further disclosure is expressly permitted by the written consent of the individual whose information is being disclosed or as otherwise permitted by 42 CFR Part 2. A general authorization for the release of medical or other information is NOT sufficient for this purpose (see §2.31). The federal rules restrict any use of the information to investigate or prosecute with regard to a crime any patient with a substance use disorder, except as provided at §§2.12(c)(5) and 2.65."

### 2024 Amendment Impact on Re-Disclosure

Under the 2024 amendments, when Part 2 records are disclosed pursuant to a §2.33 TPO consent:

- Recipients who are HIPAA covered entities or business associates may further use and disclose the records under HIPAA rules (effectively treating them as HIPAA-protected PHI for TPO purposes)
- The re-disclosure prohibition is relaxed for HIPAA-covered recipients to permit standard HIPAA-authorized TPO activities
- However, Part 2's prohibition on use in civil, criminal, administrative, or legislative proceedings against the patient is preserved (§2.12(d))
- Non-HIPAA-covered recipients remain bound by the traditional re-disclosure prohibition

## Court Order Requirements — §2.64, §2.65

### Authorizing Disclosures by Court Order

When consent is unavailable or not applicable, a court may issue an order authorizing disclosure only after the court finds "good cause" — meaning that:

1. Other ways of obtaining the information are not available or would not be effective
2. The public interest and need for disclosure outweigh the potential injury to the patient, the physician-patient relationship, and the treatment services

### Application Process

An application for a court order must use a fictitious name for the patient and may not disclose patient-identifying information to the court unless the patient is the applicant. The application must be filed under seal.

### Criminal Investigations — §2.65

Part 2 records may not be used to investigate or prosecute a patient with respect to a substance use disorder-related crime, with very limited exceptions:

- A court order under §2.65 requires an additional finding that the crime is extremely serious (causing or threatening to cause death or serious bodily injury)
- The order must limit disclosure to the information essential to fulfill the purpose and limit access to those who need the information

## Qualified Service Organization Agreements — §2.11(a)

Part 2 uses QSOAs (analogous to HIPAA BAAs) for entities that provide services to Part 2 programs:

| QSOA Requirement | Description |
|------------------|-------------|
| Written agreement | Must be in writing, signed by both parties |
| Acknowledge Part 2 obligations | QSO acknowledges it is bound by Part 2 |
| Permitted activities | Data processing, laboratory analyses, legal/medical/accounting/other professional services |
| No re-disclosure | QSO agrees not to re-disclose except as permitted by Part 2 |
| Resistibility to compulsory process | QSO agrees to resist judicial process seeking patient records unless permitted by Part 2 |

**2024 Amendment**: Existing QSOAs may be maintained, but programs may now transition to using HIPAA-style BAAs for Part 2 records, provided the BAA includes Part 2's specific protections (anti-discrimination, use restriction for investigations/prosecutions).

## Comparison: Part 2 vs HIPAA (Post-2024 Amendments)

| Aspect | HIPAA | 42 CFR Part 2 (Post-2024) |
|--------|-------|--------------------------|
| Consent for TPO | Not required | Written consent required (§2.33 single consent available) |
| Consent specificity | N/A (no consent needed for TPO) | Must include specified elements; may use general recipient designation for TPO |
| Re-disclosure | HIPAA allows under permitted uses/disclosures | Restricted — recipients who are HIPAA CEs may use under HIPAA for TPO; anti-discrimination protections preserved |
| Use in legal proceedings against patient | No prohibition | Prohibited except under specific court order (§2.12(d)) |
| Breach notification | Required under §164.400-414 | Now aligned with HIPAA breach notification requirements (2024 amendment) |
| Penalties | HIPAA civil and criminal penalties | Part 2 criminal penalties (§2.4) PLUS HIPAA penalties for covered entities (2024 amendment) |
| Enforcement | OCR | SAMHSA (Part 2-specific) AND OCR (aligned enforcement, 2024 amendment) |
| Patient right of access | Yes, §164.524 | Now aligned with HIPAA (2024 amendment) |

## Special Populations and Situations

### Minors — §2.14

- State law governs whether a minor may consent to SUD treatment
- If the minor can lawfully consent to SUD treatment, the minor controls the Part 2 consent for disclosure
- A parent/guardian may consent for a minor who cannot lawfully consent to treatment, but the Part 2 program may deny parental access to protect the minor

### Medical Emergencies — §2.51

Disclosure without consent is permitted in a bona fide medical emergency to medical personnel to the extent necessary to meet the emergency. The program must document: the name and affiliation of the recipient, the name of the individual authorizing disclosure, the date and time of disclosure, the nature of the emergency, and the information disclosed.

### Audit and Evaluation — §2.53

Federal, state, and local government agencies and third-party payers may access Part 2 records for audit and evaluation purposes without consent, subject to restrictions on re-disclosure and a prohibition on use in criminal investigation or prosecution.

## Asclepius Health Network Part 2 Compliance Program

1. **EHR Segmentation**: Part 2 records are flagged with a sensitivity code; access controls prevent viewing by users without Part 2 authorization
2. **Consent Management**: Dedicated consent forms tracked in the EHR with consent status (granted/revoked/never requested) visible to clinical staff
3. **Staff Training**: Annual Part 2-specific training for all clinical, billing, and HIM staff; quarterly refresher for SUD program staff
4. **HIE Participation**: Part 2 records are excluded from automated HIE feeds unless patient has signed §2.33 TPO consent
5. **Breach Response**: Part 2 breach response follows HIPAA breach notification procedures (aligned under 2024 amendments) with additional SAMHSA reporting

## Enforcement

### Criminal Penalties — §2.4

Any person who violates Part 2 is subject to:
- First offense: Fine of not more than $500
- Subsequent offenses: Fine of not more than $5,000

### 2024 Amendment Penalty Alignment

The 2024 Final Rule aligned Part 2 enforcement with HIPAA's penalty tiers for covered entities and business associates, enabling OCR to impose HIPAA-level civil monetary penalties for Part 2 violations.

## Integration Points

- **hipaa-privacy-rule**: Part 2 records held by HIPAA CEs are subject to both Part 2 and HIPAA; Part 2 is the more restrictive standard
- **hipaa-breach-notify**: Part 2 breach notification now aligned with HIPAA breach notification requirements
- **hipaa-minimum-necessary**: Part 2 consent specifies the scope of disclosure; minimum necessary applies separately under HIPAA
- **hipaa-baa-management**: QSOAs serve Part 2's function analogous to BAAs; 2024 amendments permit BAA use with Part 2 additions
