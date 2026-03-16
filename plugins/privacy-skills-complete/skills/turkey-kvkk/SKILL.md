---
name: turkey-kvkk
description: >-
  Implements compliance with Turkey's Personal Data Protection Law (Kisisel
  Verilerin Korunmasi Kanunu, KVKK, Law No. 6698). Covers data controller
  obligations, data subject rights, VERBIS registration, cross-border transfer
  restrictions, Board decisions, and administrative fines. Keywords: KVKK,
  Turkey, VERBIS, data controller registry, Board decision, cross-border.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: jurisdiction-compliance
  tags: "kvkk, turkey, verbis, cross-border-transfer, data-controller-registry"
---

# Turkey KVKK Compliance

## Overview

The Kisisel Verilerin Korunmasi Kanunu (KVKK), Law No. 6698, is Turkey's comprehensive personal data protection law. It was published in the Official Gazette on 7 April 2016 and entered into force on the same date. The KVKK is modelled on the EU Data Protection Directive 95/46/EC and shares structural similarities with the GDPR, though there are significant differences in cross-border transfer mechanisms, consent requirements, and the role of the Personal Data Protection Authority (Kisisel Verileri Koruma Kurumu, KVKK Authority) and its decision-making body, the Personal Data Protection Board (Kurul).

Turkey applied for EU membership in 1987, and the KVKK was enacted partly to align with EU data protection standards. However, Turkey has not received an adequacy decision from the European Commission under GDPR Article 45, which creates complexity for EU-Turkey data flows.

## Key Definitions

| Turkish Term | English | GDPR Equivalent |
|-------------|---------|----------------|
| Kisisel veri | Personal data | Personal data (Art. 4(1)) |
| Ozel nitelikli kisisel veri | Special category personal data | Special category data (Art. 9) |
| Veri sorumlusu | Data controller | Controller (Art. 4(7)) |
| Veri isleyen | Data processor | Processor (Art. 4(8)) |
| Ilgili kisi | Data subject / Relevant person | Data subject |
| Acik riza | Explicit consent | Consent |
| VERBIS | Data Controllers Registry | No direct equivalent (registration system) |

## Lawful Bases for Processing (Article 5)

Processing of personal data is prohibited without the explicit consent of the data subject, except where:

1. **Expressly provided by law** — processing is clearly laid down in legislation
2. **Necessary for protection of life or physical integrity** — where the data subject or another person is physically or legally incapable of giving consent
3. **Necessary for performance of a contract** — directly related to establishing or performing a contract
4. **Necessary for the controller to fulfil a legal obligation**
5. **Data made public by the data subject** — manifestly made public
6. **Necessary for establishment, exercise, or defence of a right**
7. **Necessary for legitimate interests of the controller** — provided this does not violate fundamental rights and freedoms of the data subject

## Special Category Data (Article 6)

Special category data includes: race, ethnic origin, political opinion, philosophical belief, religion, sect or other belief, appearance and dressing, association/foundation/union membership, health, sexual life, criminal conviction and security measures, and biometric and genetic data.

Processing requires either:
- Explicit consent of the data subject, OR
- Express authorisation by law (for categories other than health and sexual life)
- For health and sexual life data: processing by persons or authorised institutions under secrecy obligations for purposes of public health, preventive medicine, medical diagnosis, treatment, care, or health service management

## VERBIS — Data Controllers Registry

All data controllers meeting the registration threshold must register with VERBIS (Veri Sorumlulari Sicil Bilgi Sistemi). Registration requires disclosure of:
- Identity and contact information of the data controller and representative
- Purpose of data processing
- Categories of data subjects and personal data
- Recipients or categories of recipients
- Personal data transferred abroad and transfer safeguards
- Maximum retention periods
- Security measures taken

**Exemptions from VERBIS**: The Board has exempted certain categories including data controllers processing data as required by law, data controllers with fewer than 50 employees and less than TRY 100 million annual turnover (provided core activity is not special category data processing), and notaries.

## Cross-Border Transfers (Article 9)

Transfer of personal data abroad requires:
1. **Explicit consent** of the data subject, OR
2. One of the Article 5(2) or Article 6(3) conditions is met, AND one of:
   - Transfer is to a country with **adequate protection** (as determined by the Board — as of 2026 the Board has not yet published a list of adequate countries)
   - Data controllers in Turkey and abroad provide **adequate protection in writing** and the Board grants permission
   - **Binding corporate rules** approved by the Board

**2024 Amendment**: The KVKK was amended in March 2024 to introduce new cross-border transfer mechanisms including standard contractual clauses and adequacy decisions aligned more closely with GDPR Chapter V, with transitional provisions extending to 1 September 2024.

## Data Subject Rights (Article 11)

Data subjects have the right to:
1. Learn whether their personal data is being processed
2. Request information about processing if data has been processed
3. Learn the purpose of processing and whether data is used in accordance with its purpose
4. Know the third parties to whom personal data is transferred domestically or abroad
5. Request rectification of incomplete or inaccurate data
6. Request erasure or destruction of personal data under Article 7
7. Request notification of rectification/erasure to third parties
8. Object to a result that is against them produced by analysis of processed data exclusively through automated systems
9. Claim compensation for damages arising from unlawful processing

## Enforcement and Penalties

The Personal Data Protection Board may impose administrative fines:
- **TRY 5,000 to 1,000,000** for failure to comply with the obligation to inform (Article 10)
- **TRY 15,000 to 1,000,000** for failure to comply with data security obligations (Article 12)
- **TRY 25,000 to 1,000,000** for failure to comply with Board decisions (Article 15)
- **TRY 20,000 to 1,000,000** for failure to register with VERBIS (Article 16)

Fine amounts are adjusted annually based on the revaluation rate.

## Key Board Decisions

- **Decision 2019/78**: Guidelines on explicit consent — consent must be freely given, informed, specific, and an unambiguous indication of will
- **Decision 2019/10**: Data controller and data processor distinction — clarified responsibilities and contractual requirements
- **Decision 2020/915**: Cookie consent requirements — prior consent required for non-essential cookies
- **Decision 2022/1**: Cross-border transfer assessment criteria prior to the 2024 amendments

## Integration Points

- **cross-border transfers**: KVKK Article 9 transfer mechanisms interact with GDPR Chapter V for EU-Turkey flows
- **vendor-privacy-due-diligence**: Data processor agreements must include Article 12 security obligations
- **breach-72h-notification**: KVKK Article 12(5) requires notification to the Board "as soon as possible" (Board guideline suggests 72 hours)
- **data-inventory-mapping**: VERBIS registration requires comprehensive processing inventory
