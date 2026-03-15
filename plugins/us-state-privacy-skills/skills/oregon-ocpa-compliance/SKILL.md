---
name: oregon-ocpa-compliance
description: >-
  Oregon Consumer Privacy Act (OCPA) compliance. Unique provisions for
  de-identified data requirements, employee data partial exemption,
  nonprofit applicability, 14-day cure period, and consumer rights.
  Effective July 1, 2024. AG enforcement only.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "oregon-ocpa, deidentified-data, employee-exemption, nonprofit, cure-period"
---

# Oregon Consumer Privacy Act (OCPA)

## Overview

The Oregon Consumer Privacy Act (OCPA), codified as ORS §646A.570 through §646A.604, was signed into law on July 18, 2023 (SB 619), and became effective July 1, 2024. Oregon is notable for several unique provisions: it applies to nonprofit organizations (unlike most state privacy laws), has specific de-identified data compliance requirements, includes a partial exemption for employee data, and provides a 14-day cure period (the shortest of any state law with a cure period).

## Applicability (§646A.572)

The OCPA applies to a person that conducts business in Oregon or provides products or services to Oregon residents AND during a calendar year:

1. Controls or processes personal data of 100,000 or more Oregon consumers (excluding data processed solely for payment transactions); OR
2. Controls or processes personal data of 25,000 or more Oregon consumers AND derives 25% or more of annual gross revenue from selling personal data.

**Key unique features:**
- **Nonprofit applicability**: Unlike Virginia, Colorado, Connecticut, and Texas, the OCPA applies to nonprofit organizations
- **No revenue threshold alternative**: Like Virginia and Colorado, there is no standalone revenue threshold

**Exemptions (§646A.572(2)):**
- State and local government bodies
- GLBA-covered financial institutions (entity-level)
- HIPAA covered entities and business associates (entity-level)
- Data governed by GLBA, HIPAA, FERPA, FCRA, DPPA, COPPA, Farm Credit Act
- **Not exempt**: Nonprofit organizations (unique among state privacy laws)

**Liberty Commerce Inc. Assessment:**
Liberty Commerce Inc. processes personal data of approximately 72,000 Oregon consumers and derives 12% of revenue from data sale activities. It does not meet either threshold. However, Liberty Commerce Inc. implements OCPA compliance as part of its multi-state program for operational consistency.

## Consumer Rights (§646A.578)

### Six Consumer Rights

1. **Right to Access** (§646A.578(1)(a)): Confirm processing and access personal data
2. **Right to Correct** (§646A.578(1)(b)): Correct inaccuracies
3. **Right to Delete** (§646A.578(1)(c)): Delete personal data
4. **Right to Portability** (§646A.578(1)(d)): Obtain data in portable format
5. **Right to Opt Out** (§646A.578(1)(e)):
   - Targeted advertising
   - Sale of personal data
   - Profiling in furtherance of decisions producing legal or similarly significant effects
6. **Right to Know Third Parties** (§646A.578(1)(f)): Obtain a list of specific third parties to whom the controller has disclosed the consumer's personal data

**Note:** The Right to Know Third Parties is unique to Oregon — most other state laws only require disclosure of categories of third parties, not specific names.

### Response Requirements (§646A.580)
- Respond within 45 days
- Extension: up to 45 additional days with notice
- Appeal: controller must respond within 45 days (not 60 like other states)

## De-Identified Data Requirements (§646A.574)

Oregon has the most detailed de-identified data requirements of any state privacy law:

### Controller Obligations for De-Identified Data
1. Take reasonable measures to ensure data cannot be associated with a natural person
2. Publicly commit to maintain and use data only in de-identified form
3. Contractually obligate recipients to comply with de-identification requirements
4. Exercise reasonable oversight to monitor compliance with contractual obligations
5. Take appropriate steps to address any breach of the contractual obligations

### Technical Standards
- Must use technical safeguards to prevent re-identification
- Must implement organizational safeguards including access controls
- Must conduct regular assessments of re-identification risk
- Must delete or destroy data if de-identification can no longer be maintained

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. applies k-anonymity (k=5 minimum) and differential privacy techniques to de-identified datasets. A public commitment statement is posted at privacy.libertycommerce.com/deidentification. All recipients of de-identified data sign agreements prohibiting re-identification attempts. Quarterly re-identification risk assessments are conducted by the data science team.

## Employee Data Partial Exemption (§646A.572(4))

### Exemption Scope
The OCPA provides a **partial** exemption for employee data. Personal data processed in the context of employment is exempt from:
- Consumer rights provisions (§646A.578) — access, correct, delete, portability, opt-out
- Consumer request processing requirements (§646A.580)

### Not Exempt
Employee data is NOT exempt from:
- Controller obligations (§646A.576) — privacy notice, data minimization, security
- Processor requirements (§646A.582)
- De-identified data requirements (§646A.574)
- Data protection assessment requirements (§646A.584)
- Sensitive data consent requirements (§646A.576(8))

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. provides a privacy notice to Oregon employees covering all data processing activities. Sensitive employee data (health information for benefits, racial/ethnic data for diversity reporting) is processed only with consent. DPIAs are conducted for employee profiling activities (performance scoring, promotion algorithms).

## Nonprofit Applicability

Oregon is unique in applying its privacy law to nonprofit organizations. This has significant implications:

| Organization Type | OCPA | VCDPA | CPA | CTDPA | TDPSA | CCPA/CPRA |
|------------------|------|-------|-----|-------|-------|-----------|
| For-profit | Yes | Yes | Yes | Yes | Yes | Yes |
| Nonprofit | Yes | No | No | No | No | No |

**Implications for nonprofits:**
- Must assess applicability against 100,000/25,000 consumer thresholds
- Must provide consumer rights if applicable
- Must comply with controller obligations (privacy notice, minimization, security)
- Must obtain consent for sensitive data processing
- Must conduct DPIAs for targeted advertising, sale, profiling, and sensitive data

## Sensitive Data (§646A.574(14))

### Categories
1. Racial or ethnic origin
2. Religious beliefs
3. Mental or physical health diagnosis
4. Sexual orientation
5. Citizenship or immigration status
6. Genetic or biometric data for identification
7. Personal data of a known child
8. Precise geolocation data
9. **Transgender or nonbinary status** (unique to Oregon)

**Note:** Oregon is the first state to explicitly include transgender or nonbinary status as a sensitive data category.

### Consent Requirement
Processing requires opt-in consent. Consent must be freely given, specific, informed, and unambiguous.

## 14-Day Cure Period (§646A.600)

Oregon provides a 14-day cure period — the shortest among state privacy laws with cure provisions:

| State | Cure Period | Duration |
|-------|------------|----------|
| Oregon | 14 days | Permanent |
| Virginia | 30 days | Permanent |
| Texas | 30 days | Permanent |
| Colorado | 60 days | Expired January 1, 2025 |
| Connecticut | 60 days | Expired January 1, 2025 |
| California | None | Eliminated by CPRA |

### Cure Process
1. AG provides written notice of alleged violation
2. Controller has 14 days to cure
3. If cured and written statement provided: AG may not bring action
4. If not cured: AG may proceed under Oregon Unlawful Trade Practices Act (ORS §646.607)

## Key Regulatory References

- ORS §646A.570 through §646A.604 (OCPA)
- ORS §646.607 et seq. (Oregon Unlawful Trade Practices Act — enforcement)
- NIST Special Publication 800-188 — De-Identification of Personal Information (reference standard)
- Oregon AG Consumer Privacy Division guidance (as published)
