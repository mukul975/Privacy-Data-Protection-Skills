---
name: ccpa-cpra-compliance
description: >-
  Complete CCPA/CPRA compliance implementation covering California Civil Code
  §1798.100-199. Includes consumer rights framework, business obligations,
  service provider and contractor requirements, enforcement mechanisms, and
  CPPA rulemaking. Triggers on CCPA, CPRA, California privacy, consumer rights.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "ccpa, cpra, california-privacy, consumer-rights, business-obligations"
---

# CCPA/CPRA Compliance

## Overview

The California Consumer Privacy Act (CCPA), as amended by the California Privacy Rights Act (CPRA), establishes comprehensive consumer privacy rights under California Civil Code §1798.100-199. The CPRA, approved by voters on November 3, 2020 (Proposition 24), substantially amended the CCPA effective January 1, 2023, with a lookback period to January 1, 2022. The California Privacy Protection Agency (CPPA) was established as the first dedicated state privacy enforcement agency in the United States.

The CPRA replaced the California Attorney General as the primary enforcement body with the CPPA, added the category of sensitive personal information, created new consumer rights (correction and limit use of sensitive PI), expanded the definition of "sharing" for cross-context behavioral advertising, and introduced requirements for data processing agreements.

## Applicability (§1798.140(d))

A business is subject to CCPA/CPRA if it:

1. Has annual gross revenues exceeding $25,000,000 in the preceding calendar year (adjusted by the CPPA for inflation starting January 1, 2024)
2. Annually buys, sells, or shares the personal information of 100,000 or more consumers or households (CPRA increased from 50,000)
3. Derives 50% or more of its annual revenues from selling or sharing consumers' personal information

**Liberty Commerce Inc. Assessment:**
Liberty Commerce Inc., with annual revenues of $48 million and processing personal information of approximately 320,000 California consumers through its e-commerce platform, meets threshold (1) and threshold (2). Liberty Commerce Inc. is classified as a "business" under §1798.140(d).

## Key Definitions

### Personal Information (§1798.140(v))

Information that identifies, relates to, describes, is reasonably capable of being associated with, or could reasonably be linked, directly or indirectly, with a particular consumer or household. Categories include:

| Category | Examples |
|----------|----------|
| Identifiers | Real name, alias, postal address, unique personal identifier, online identifier, IP address, email, account name, SSN, driver's license, passport number |
| Commercial Information | Records of personal property, products or services purchased, obtaining, or considered |
| Biometric Information | Physiological, biological, or behavioral characteristics used to establish individual identity (fingerprint, face, voice, iris, keystroke patterns) |
| Internet/Network Activity | Browsing history, search history, information regarding interaction with website, application, or advertisement |
| Geolocation Data | Physical location or movements |
| Sensory Data | Audio, electronic, visual, thermal, olfactory, or similar information |
| Professional/Employment | Current or past job-related information |
| Education Information | Non-publicly available education records per FERPA (20 U.S.C. §1232g) |
| Inferences | Profiles reflecting preferences, characteristics, psychological trends, predispositions, behavior, attitudes, intelligence, abilities, aptitudes |
| Sensitive PI (CPRA) | SSN/driver's license/passport, account log-in with password, precise geolocation, racial/ethnic origin, religious/philosophical beliefs, union membership, contents of mail/email/text, genetic data, biometric data for identification, health information, sex life/sexual orientation data |

### Sale (§1798.140(ad))

Selling, renting, releasing, disclosing, disseminating, making available, transferring, or otherwise communicating orally, in writing, or by electronic or other means, a consumer's personal information by the business to a third party for monetary or other valuable consideration.

### Sharing (§1798.140(ah)) — Added by CPRA

Sharing, renting, releasing, disclosing, disseminating, making available, transferring, or otherwise communicating a consumer's personal information by the business to a third party for cross-context behavioral advertising, whether or not for monetary or other valuable consideration, including situations where no money is exchanged.

### Service Provider vs. Contractor (§1798.140(ag), §1798.140(j))

| Aspect | Service Provider | Contractor |
|--------|-----------------|------------|
| Definition | Processes PI on behalf of business per written contract | Processes PI made available by business per written contract |
| Contract Requirements | Written agreement prohibiting selling/sharing, limiting use to specified purposes | Written agreement with same prohibitions plus certification of understanding, grant of compliance audit rights |
| Subcontracting | May engage subcontractors with written contract | May engage subcontractors with written contract and business notification |
| Compliance Audits | Not expressly required in statute | Business has right to audit contractor compliance |

## Consumer Rights

### 1. Right to Know (§1798.100, §1798.110, §1798.115)

Consumers may request that a business disclose:
- Categories of PI collected
- Categories of sources
- Business or commercial purpose for collecting, selling, or sharing
- Categories of third parties to whom PI is disclosed
- Specific pieces of PI collected about the consumer

**Lookback period:** 12 months preceding the request (business may voluntarily go beyond).

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. provides a "Know My Data" portal at privacy.libertycommerce.com/know where verified consumers can request all five categories of disclosure. The system generates a structured report in machine-readable format (JSON) and human-readable format (PDF) within 10 business days.

### 2. Right to Delete (§1798.105)

Consumers may request deletion of personal information collected from them. Upon receiving a verified request, the business must delete the PI and direct service providers and contractors to delete the consumer's PI.

**Exceptions (§1798.105(d)):** Transaction completion, security, error repair, free speech (Cal. Civ. Code §1798.105(d)(4)), internal uses reasonably aligned with consumer expectations, compliance with legal obligation, internal uses compatible with the context of collection.

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. processes deletion requests through a cascading deletion workflow that propagates to all service providers (payment processor, shipping partner, analytics provider) within 45 calendar days. Retained data for legal compliance (tax records per 26 U.S.C. §6001) is documented with the specific legal basis.

### 3. Right to Correct (§1798.106) — Added by CPRA

Consumers may request correction of inaccurate personal information. The business must use commercially reasonable efforts to correct the information.

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. allows consumers to self-correct profile data (name, address, email, phone) directly in their account. For data in backend systems (purchase history corrections, loyalty points), verified requests are processed through the privacy team with documentation of the correction.

### 4. Right to Opt-Out of Sale/Sharing (§1798.120)

Consumers have the right to direct a business that sells or shares their personal information to stop selling or sharing that information. The business must respect this direction.

**Key requirements:**
- "Do Not Sell or Share My Personal Information" link on homepage
- Must honor Global Privacy Control (GPC) signals as valid opt-out requests (CPPA Regulations §7025)
- No re-solicitation for 12 months after opt-out
- Must not discriminate against consumers who opt out (§1798.125)

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. displays a persistent "Do Not Sell or Share My Personal Information" link in the footer of every page. The system detects GPC signals via the `Sec-GPC: 1` HTTP header and `navigator.globalPrivacyControl` JavaScript API, automatically applying opt-out status to the browsing session and associating it with the consumer's account if authenticated.

### 5. Right to Limit Use of Sensitive PI (§1798.121) — Added by CPRA

Consumers may direct a business to limit its use of sensitive personal information to specified purposes (performing services/providing goods, preventing security incidents, resisting malicious/deceptive actions, ensuring safety, short-term transient use, performing services on behalf of the business, verifying/maintaining quality, upgrading/enhancing services).

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. displays a "Limit the Use of My Sensitive Personal Information" link adjacent to the opt-out link. When activated, the system restricts processing of sensitive PI categories (precise geolocation, racial/ethnic origin data from surveys, payment card details beyond transaction processing) to the enumerated permitted purposes.

### 6. Right to Non-Discrimination (§1798.125)

A business may not discriminate against a consumer for exercising their CCPA rights, including by:
- Denying goods or services
- Charging different prices or rates
- Providing a different level or quality of goods or services
- Suggesting that the consumer will receive a different price or quality

**Financial incentive programs** are permitted if the consumer is notified and opts in, the incentive is reasonably related to the value of the consumer's data, and the business can explain the valuation methodology.

## Business Obligations

### Privacy Notice (§1798.100(a), §1798.130(a)(5))

The privacy notice must be updated at least once every 12 months and include:
- Categories of PI collected in the preceding 12 months
- Categories of sensitive PI collected
- Purposes for which each category is used and whether it is sold or shared
- Length of time each category is retained (or criteria for determining retention) — added by CPRA
- Categories of sources
- Categories of third parties to which PI is disclosed
- Instructions for submitting consumer requests
- Whether the business sells or shares PI, and categories involved
- Categories of PI disclosed for a business purpose

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. publishes its California Privacy Notice at privacy.libertycommerce.com/california, updated annually in January. The notice uses a layered format with a summary table followed by detailed sections. Retention periods are specified per data category (e.g., transaction records: 7 years per tax requirements; browsing data: 13 months; account data: duration of account plus 30 days).

### Data Processing Agreements (§1798.100(d)) — Added by CPRA

Businesses must enter into agreements with service providers, contractors, and third parties that:
- Specify the business purpose for which PI is made available
- Require the recipient to comply with CCPA/CPRA obligations
- Grant the business rights to take reasonable steps to ensure compliance
- Require notification if the recipient determines it can no longer meet its obligations
- Grant the business the right to stop and remediate unauthorized use of PI

### Data Minimization (§1798.100(c)) — Added by CPRA

A business's collection, use, retention, and sharing of PI must be:
- Reasonably necessary and proportionate to the purposes for which the PI was collected or processed
- Not further processed in a manner incompatible with those purposes

### Consumer Request Processing (§1798.130)

| Requirement | Detail |
|-------------|--------|
| Response deadline | 45 calendar days from receipt of verifiable request |
| Extension | Up to 45 additional days (90 total) with notice to consumer |
| Verification | Reasonable methods to verify identity; match at least two data points for access; three data points for specific pieces |
| Authorized agents | Must accept requests from authorized agents with signed permission or power of attorney |
| Free requests | At least two free requests per 12-month period |
| Format | Delivered in readily usable, machine-readable format (for portability requests) |
| Toll-free number | Required for businesses that operate exclusively online only if they have a direct relationship with the consumer |

### Record Keeping (CPPA Regulations §7101)

Businesses that buy, receive, or sell the PI of 10,000,000 or more consumers must compile metrics for the prior calendar year and disclose:
- Number of requests to know, delete, correct, and opt-out received
- Number of requests complied with in whole or in part
- Number of requests denied
- Median number of days to respond

## Enforcement

### CPPA Enforcement (§1798.199.40-199.100)

- Administrative enforcement actions by the CPPA
- Administrative fines up to $2,500 per violation; $7,500 per intentional violation or violations involving minors under 16
- CPPA has authority to issue regulations, conduct investigations, and bring enforcement actions
- 30-day cure period was eliminated by CPRA effective January 1, 2023

### Private Right of Action (§1798.150)

Limited to data breach claims where nonencrypted and nonredacted PI (as defined in Cal. Civ. Code §1798.81.5(d)(1)(A)) is subject to unauthorized access due to the business's failure to implement reasonable security measures.

- Statutory damages: $100-$750 per consumer per incident, or actual damages (whichever is greater)
- Injunctive or declaratory relief
- Any other relief the court deems proper
- 30-day notice and cure period before filing suit

## Implementation Roadmap for Liberty Commerce Inc.

### Phase 1: Assessment (Weeks 1-4)
1. Data inventory and mapping of all PI and sensitive PI categories
2. Identify all data flows: collection, use, sale, sharing, disclosure
3. Map service providers, contractors, and third parties
4. Assess current privacy notice against CPRA requirements
5. Evaluate consumer request processing workflows

### Phase 2: Legal Framework (Weeks 5-8)
6. Update privacy notice with retention periods, sensitive PI categories, sale/sharing disclosures
7. Draft/update data processing agreements for all service providers and contractors
8. Develop consumer request verification procedures
9. Establish authorized agent acceptance procedures
10. Create financial incentive program valuation methodology (if applicable)

### Phase 3: Technical Implementation (Weeks 9-16)
11. Deploy "Do Not Sell or Share My Personal Information" link
12. Deploy "Limit the Use of My Sensitive Personal Information" link
13. Implement GPC signal detection and honoring
14. Build consumer request intake portal with identity verification
15. Implement cascading deletion workflow
16. Build right-to-know report generation (JSON and PDF)
17. Implement data minimization controls and retention enforcement

### Phase 4: Operations (Weeks 17-20)
18. Train customer service team on CCPA/CPRA consumer rights
19. Establish 45-day SLA monitoring for consumer requests
20. Implement metrics tracking per CPPA Regulations §7101
21. Schedule annual privacy notice review
22. Conduct tabletop exercise for consumer request processing

## Key Regulatory References

- California Civil Code §1798.100-199 (CCPA as amended by CPRA)
- California Privacy Rights Act (Proposition 24, approved November 3, 2020)
- CPPA Final Regulations (effective March 29, 2023; updated regulations effective March 29, 2024)
- CPPA Regulations §7001-7102 (Title 11, Division 6, California Code of Regulations)
- Cal. Civ. Code §1798.81.5 — Data breach notification
- AG Enforcement Actions: Sephora Inc. ($1.2 million settlement, August 2022) — first public CCPA enforcement action for failure to honor GPC opt-out signals
- CPPA Enforcement Advisory No. 2024-01 — Dark patterns in consent interfaces
