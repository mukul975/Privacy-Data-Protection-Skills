---
name: consent-for-transfers
description: >-
  Guide for obtaining explicit consent for international data transfers under GDPR
  Article 49(1)(a). Covers informed consent requirements including risks of transfers
  without adequacy decisions or appropriate safeguards, specific destination country
  disclosure, and the narrow scope of derogation-based transfers.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: consent-management
  tags: "transfer-consent, article-49, international-transfers, explicit-consent, data-transfers"
---

# Managing Consent for Transfers

## Overview

GDPR Article 49(1)(a) provides that in the absence of an adequacy decision (Article 45) or appropriate safeguards (Article 46), a transfer of personal data to a third country may take place if "the data subject has explicitly consented to the proposed transfer, after having been informed of the possible risks of such transfers for the data subject due to the absence of an adequacy decision and appropriate safeguards."

This is a derogation — a last resort — not a primary transfer mechanism. The EDPB Guidelines 2/2018 on derogations under Article 49 emphasize that derogations must be interpreted restrictively and should not become the rule.

## Explicit Consent Requirements for Transfers

### What Makes Transfer Consent "Explicit"

Explicit consent under Article 49(1)(a) requires a higher standard than standard consent under Article 6(1)(a):

1. **Express statement**: The data subject must make an express statement of consent specifically for the transfer. An unticked checkbox is sufficient for standard consent but may not be sufficient for explicit consent — a written or typed declaration is preferred.
2. **Specific to the transfer**: Consent must specifically mention the international transfer, not be buried in general terms.
3. **Informed of risks**: The data subject must be told about the specific risks of the transfer, not just generic warnings.
4. **Specific destination**: The third country or countries must be named.
5. **Absence disclosed**: The data subject must be told that there is no adequacy decision and no appropriate safeguards in place for the destination.

### Information That Must Be Provided Before Consent

Per Article 49(1)(a) and EDPB Guidelines 2/2018:

| Information Element | Description | Example for CloudVault SaaS Inc. |
|-------------------|-------------|----------------------------------|
| Destination country | Specific country name | India |
| Recipient identity | Who will receive the data | CloudVault India Pvt. Ltd. (subsidiary) |
| Purpose of transfer | Why the data is being transferred | Customer support during EU night hours |
| Data categories | What personal data will be transferred | Name, email, account metadata, support ticket content |
| Absence of adequacy decision | India does not have an EU adequacy decision | "India has not been recognized by the European Commission as providing an adequate level of data protection" |
| Absence of safeguards | No SCCs or BCRs in place for this transfer | "This transfer is not covered by Standard Contractual Clauses or Binding Corporate Rules" |
| Specific risks | What could go wrong | "Indian data protection law (DPDP Act 2023) may not provide equivalent protections. Government access requests may not be subject to the same limitations as under EU law." |
| Withdrawal right | How to withdraw consent | "You can withdraw consent for this transfer at any time in Settings > Privacy" |

## CloudVault SaaS Inc. Transfer Consent Implementation

### Scenario: Customer Support Data Transfer to India

CloudVault SaaS Inc. operates a customer support center in Bengaluru, India (CloudVault India Pvt. Ltd.). When EU users submit support tickets outside EU business hours, ticket data may be accessed from India.

**Consent Statement (displayed to users):**

"To provide you with 24/7 customer support, CloudVault SaaS Inc. may transfer your support ticket data (your name, email address, account details, and the content of your support request) to CloudVault India Pvt. Ltd. in Bengaluru, India.

India does not have an adequacy decision from the European Commission, and this specific transfer is not covered by Standard Contractual Clauses or Binding Corporate Rules.

This means your data may not receive the same level of protection as under EU law. In particular:
- The Indian Digital Personal Data Protection Act 2023 is still in early implementation and its enforcement mechanisms are not yet fully established
- Indian government authorities may have legal powers to access personal data that differ from those available to EU authorities
- Judicial remedies available to you in India may differ from those available under EU law

You are not required to consent to this transfer. If you do not consent, your support requests will be handled during EU business hours only (Monday-Friday, 08:00-18:00 CET) by our Dublin-based support team.

You can withdraw this consent at any time in Settings > Privacy > Data Transfers. Withdrawal will take effect within 24 hours."

### Consent Mechanism

- Two-step process: (1) user reads the full risk disclosure, (2) user types "I consent to the transfer" in a text field
- This typed declaration satisfies the "explicit" requirement
- Consent is recorded with all standard consent record fields plus transfer-specific fields

## Limitations of Consent as Transfer Basis

Per EDPB Guidelines 2/2018:

1. **Not for systematic/repetitive transfers**: Consent under Article 49(1)(a) should not be used as the basis for systematic, large-scale, or repetitive transfers. For those, use SCCs (Article 46(2)(c)) or BCRs (Article 47).
2. **Not a blank check**: Each transfer must be specifically consented to, or consent must cover a clearly defined and limited set of transfers.
3. **Power imbalance applies**: The same freely-given requirement applies — consent for transfers in an employment context is generally not valid.
4. **Withdrawal must be feasible**: If the controller cannot operationally stop transfers upon withdrawal, consent may not be the appropriate basis.

## Key Regulatory References

- GDPR Article 44 — General principle for transfers
- GDPR Article 45 — Transfers based on adequacy decisions
- GDPR Article 46 — Transfers subject to appropriate safeguards
- GDPR Article 49(1)(a) — Derogation: explicit consent for transfers
- EDPB Guidelines 2/2018 on Derogations under Article 49 (adopted May 25, 2018)
- CJEU C-311/18 (Schrems II, July 16, 2020) — Invalidated Privacy Shield; heightened transfer scrutiny
- EDPB Recommendations 01/2020 — Supplementary measures for transfers
