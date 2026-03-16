---
name: hipaa-research-privacy
description: >-
  Implements HIPAA Privacy Rule requirements for research uses of protected
  health information under 45 CFR §164.512(i). Covers IRB and Privacy Board
  waivers of authorization, individual authorization for research, limited
  data set and data use agreements, preparatory to research provisions, and
  decedent research provisions. Keywords: HIPAA research, IRB waiver,
  Privacy Board, authorization, limited data set, preparatory research,
  de-identification, Common Rule.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: healthcare-privacy
  tags: "hipaa, research-privacy, irb, privacy-board, authorization, limited-data-set, common-rule, phi-research"
---

# HIPAA Research Privacy — 45 CFR §164.512(i)

## Overview

The HIPAA Privacy Rule permits covered entities to use and disclose PHI for research purposes through several pathways. The primary mechanisms are: (1) individual authorization under §164.508, (2) waiver or alteration of authorization by an IRB or Privacy Board under §164.512(i), (3) use of a limited data set with a data use agreement under §164.514(e), (4) use of de-identified data under §164.514(a)-(b), (5) preparatory to research reviews under §164.512(i)(1)(ii), and (6) research on decedent information under §164.512(i)(1)(iii). Researchers and covered entities must understand the interplay between HIPAA and the Common Rule (45 CFR Part 46) which governs human subjects research independently.

## Regulatory Framework

### Authorization for Research — §164.508

- **§164.508(a)**: A covered entity may not use or disclose PHI without an authorization that satisfies §164.508 requirements, except as otherwise permitted
- **§164.508(b)(3)**: Research-specific authorization elements:
  - May describe the PHI to be used or disclosed in a specific or general manner if adequate to allow the individual to understand the PHI to be used/disclosed
  - May be for use/disclosure of PHI for a specific research study, or for future unspecified research if the authorization adequately describes the purposes
  - No expiration date required if the authorization states "end of the research study" or "none" or similar language

### Waiver of Authorization — §164.512(i)(1)(i)

A covered entity may use or disclose PHI for research without authorization if the covered entity obtains documentation that an IRB or Privacy Board has approved a waiver (or alteration) of authorization meeting ALL of the following criteria:

1. The use or disclosure involves no more than a **minimal risk** to the privacy of individuals based on:
   - An adequate plan to protect the identifiers from improper use and disclosure
   - An adequate plan to destroy the identifiers at the earliest opportunity consistent with the research (unless there is a health or research justification for retaining them, or retention is required by law)
   - Adequate written assurances that the PHI will not be reused or disclosed to any other person or entity except as required by law, for authorized oversight of the research, or for other research for which the use or disclosure would be permitted

2. The research **could not practicably be conducted** without the waiver or alteration

3. The research **could not practicably be conducted** without access to and use of the PHI

### Limited Data Set — §164.514(e)

A limited data set excludes the 16 direct identifiers listed in §164.514(e)(2) but may include:
- Dates (admission, discharge, birth, death, service)
- City, state, five-digit ZIP code
- Ages (including ages over 89 if not aggregated into a 90+ category)

A data use agreement (DUA) is required specifying:
- Permitted uses and disclosures
- Who may use or receive the limited data set
- Prohibition on re-identification or contacting individuals
- Adequate safeguards commitments
- Reporting of violations

### Preparatory to Research — §164.512(i)(1)(ii)

A covered entity may use or disclose PHI for reviews preparatory to research if the covered entity obtains representations that:
1. Use or disclosure is sought solely to review PHI as necessary to prepare a research protocol or for similar purposes preparatory to research
2. No PHI will be removed from the covered entity during the review
3. The PHI is necessary for the research purposes

### Decedent Research — §164.512(i)(1)(iii)

A covered entity may use or disclose PHI of a decedent for research if:
1. The covered entity obtains representation that use/disclosure is solely for research on the PHI of decedents
2. The PHI sought is necessary for the research
3. Documentation of the death (upon request) is provided

## HIPAA vs. Common Rule

| Requirement | HIPAA Privacy Rule | Common Rule (45 CFR Part 46) |
|------------|-------------------|------------------------------|
| Governs | Uses/disclosures of PHI by covered entities and BAs | Protection of human research subjects |
| Enforced by | OCR (HHS) | OHRP (HHS) and institutional IRBs |
| Authorization/Consent | HIPAA authorization (§164.508) | Informed consent (§46.116) |
| Waiver | IRB/Privacy Board waiver of authorization (§164.512(i)) | IRB waiver of informed consent (§46.116(f)) |
| De-identification | 18-identifier Safe Harbor or Expert Determination | Not a substitute for IRB review |
| Applies to | PHI held by covered entities and BAs | All human subjects research at institutions receiving federal funding |
| Overlap | Both may apply to same study — dual compliance required | Both may apply to same study — dual compliance required |

## Enforcement Examples

- **Lurie Children's Hospital (2024, $3.45M)**: Although primarily a cybersecurity settlement, OCR noted that research data containing PHI was among the compromised records, underscoring the obligation to secure research PHI
- **Memorial Sloan Kettering (NYS AG, 2023)**: State enforcement for insufficient research consent practices related to genetic data sharing with third parties
- **University of Mississippi Medical Center (2016, $2.75M)**: OCR found systemic failure in risk analysis and access controls affecting research data repositories

## Integration Points

- **hipaa-privacy-rule**: Research uses and disclosures are governed by the Privacy Rule
- **hipaa-deidentification**: De-identification eliminates HIPAA restrictions on research use
- **hipaa-minimum-necessary**: Minimum necessary applies to research disclosures under waiver (not to individual access or authorized disclosures)
- **hipaa-baa-management**: Research collaborators may be BAs if they create, receive, maintain, or transmit PHI
- **hipaa-breach-notification**: Research data breaches trigger the same notification obligations
