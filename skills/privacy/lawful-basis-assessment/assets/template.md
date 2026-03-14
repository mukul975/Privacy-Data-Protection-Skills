# Lawful Basis Assessment Record

**Organisation**: Nexus Technologies GmbH
**Assessment Date**: 2026-01-10
**Assessor**: Dr. Katharina Weiss, Data Protection Officer
**Review Date**: 2027-01-10

---

## Processing Activity Details

| Field | Detail |
|-------|--------|
| Processing Activity | Customer relationship management and order fulfilment |
| RoPA Reference | RPA-005 |
| Business Unit | Sales Operations |
| Processing Owner | Thomas Braun, Sales Operations Manager |
| Data Subjects | Customers (B2B and B2C) |
| Personal Data Categories | Name, business email, phone number, company name, order history, billing address, payment reference |
| Special Category Data | None |
| Processing Description | Collection and processing of customer contact and order data to fulfil purchase orders, manage delivery logistics, handle returns, and maintain customer account records in Salesforce CRM |

---

## Decision Tree Analysis

### Step 1: Legal Obligation (Art. 6(1)(c))

**Is the processing required by a specific EU or Member State law?**

Partially. Retention of invoicing and transaction records is required under Section 147 of the German Fiscal Code (Abgabenordnung, AO) for 10 years and Section 257 of the German Commercial Code (Handelsgesetzbuch, HGB) for 6 years. However, the broader CRM processing (maintaining customer profiles, contact management) is not mandated by law.

**Conclusion**: Art. 6(1)(c) applies to the tax/accounting record retention component only. A separate lawful basis is needed for the broader CRM processing.

### Step 2: Contract Performance (Art. 6(1)(b))

**Is the processing necessary for the performance of a contract with the data subject?**

Yes. The processing of customer name, delivery address, billing address, payment reference, and order details is objectively necessary to fulfil purchase orders placed by customers. Without this data, the company cannot deliver goods, process payment, or handle returns.

**Necessity test**: Each data element has been evaluated:
- Name and address: Required for delivery and invoicing — **necessary**
- Payment reference: Required for payment processing — **necessary**
- Order history: Required for returns handling and warranty claims — **necessary**
- Phone number: Required for delivery coordination and order queries — **necessary**
- Business email: Required for order confirmation and shipping notifications — **necessary**

**Conclusion**: Art. 6(1)(b) is the appropriate lawful basis for order fulfilment processing.

### Step 3-6: Not required

Contract performance has been confirmed as the appropriate basis. Steps 3-6 are not required for this processing activity.

---

## Lawful Basis Determination

| Component | Lawful Basis | Rationale |
|-----------|-------------|-----------|
| Order fulfilment, delivery, returns | Art. 6(1)(b) — Contract Performance | Processing is objectively necessary to fulfil the purchase contract with the customer |
| Tax and accounting record retention | Art. 6(1)(c) — Legal Obligation | Section 147 AO and Section 257 HGB require retention of transaction records for 10 and 6 years respectively |

---

## Rejected Alternatives

| Basis | Reason for Rejection |
|-------|---------------------|
| Art. 6(1)(a) Consent | Consent is not appropriate because: (1) it would create unnecessary withdrawal risk for essential business operations, (2) per ICO guidance, consent should not be relied upon when another basis is more appropriate, (3) order fulfilment cannot practically accommodate withdrawal |
| Art. 6(1)(d) Vital Interests | Not applicable — no life-threatening scenario |
| Art. 6(1)(e) Public Task | Not applicable — Nexus Technologies GmbH is a private company, not a public authority |
| Art. 6(1)(f) Legitimate Interests | While legitimate interest could apply, contract performance is more specific and appropriate for direct contractual processing. Legitimate interest would introduce unnecessary balancing test obligations for processing that is straightforwardly necessary for contract fulfilment |

---

## Data Subject Rights Implications

Under Art. 6(1)(b) Contract Performance, the following rights are available:

| Right | Available | Notes |
|-------|-----------|-------|
| Access (Art. 15) | Yes | Full access to all personal data processed |
| Rectification (Art. 16) | Yes | Customer can request correction of inaccurate data |
| Erasure (Art. 17) | Yes | After contract completion and expiry of legal retention periods |
| Restriction (Art. 18) | Yes | Where accuracy is contested or processing is unlawful |
| Data Portability (Art. 20) | Yes | Art. 6(1)(b) processing qualifies for portability |
| Object (Art. 21) | No | Right to object does not apply to Art. 6(1)(b) processing |

---

## Privacy Notice Update Required

The privacy notice at nexus-tech.eu/privacy must state:
- Lawful basis: Art. 6(1)(b) for order fulfilment, Art. 6(1)(c) for accounting records
- Specific purposes: as documented above
- Retention periods: active contract duration plus 10 years for accounting records per Section 147 AO

**Status**: Privacy notice verified as current on 2026-01-10 — no update required.

---

## Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Processing Owner | Thomas Braun | 2026-01-10 | T. Braun |
| Data Protection Officer | Dr. Katharina Weiss | 2026-01-10 | K. Weiss |

---

**Next Review**: 2027-01-10 or upon material change to processing activity, whichever is earlier.
