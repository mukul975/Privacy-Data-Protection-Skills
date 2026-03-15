# RoPA Change Request Form — Helix Biotech Solutions GmbH

**Change Request ID**: CR-ROPA-2025-017
**Date Submitted**: 2025-02-28
**Submitted By**: Anna Bergmann, Procurement Manager
**Department**: Procurement

---

## Change Type

- [ ] New processing activity (new RoPA entry)
- [ ] Processing activity discontinued (entry archival)
- [ ] Field update — purpose change
- [x] Field update — new/changed recipients or processors
- [ ] Field update — international transfer change
- [ ] Field update — retention period change
- [ ] Field update — security measures change
- [ ] Field update — data subject or data category change
- [ ] Administrative correction (contact details, formatting)
- [ ] Post-audit remediation (finding reference: ___)
- [ ] Post-breach remediation (incident reference: ___)

---

## Trigger Event

**What triggered this change?**

- [ ] IT change request (ref: ___)
- [x] New vendor/processor onboarding
- [ ] Vendor/processor termination
- [ ] Regulatory or legislative change
- [ ] DPIA outcome
- [ ] Annual review
- [ ] Audit finding
- [ ] Data breach remediation
- [ ] Organisational restructuring
- [ ] Data subject complaint

**Description of trigger**: Procurement has selected a new laboratory reagent supplier, BioReagents France S.A.S., to replace ChemSupply GmbH effective 2025-04-01. The new supplier will receive purchase order data including supplier contact personal data. A new DPA is required and the Supplier Management RoPA entry must reflect the new recipient.

---

## Affected RoPA Entry/Entries

| Record ID | Processing Activity | Current Owner |
|-----------|---------------------|---------------|
| RPA-2024-SUP-004 | Supplier and Vendor Management | Anna Bergmann, Procurement Manager |

---

## Change Description

### Current State (Old Values)

| Field | Current Value |
|-------|---------------|
| Recipient (Supplier #3) | ChemSupply GmbH, Industriestrasse 15, 60329 Frankfurt, Germany |
| DPA Reference (Supplier #3) | DPA-2022-CSG-003 (expiry: 2025-03-31) |

### Proposed State (New Values)

| Field | Proposed Value |
|-------|----------------|
| Recipient (Supplier #3) | BioReagents France S.A.S., 28 Rue Pasteur, 69007 Lyon, France |
| DPA Reference (Supplier #3) | DPA-2025-BRF-008 (effective: 2025-04-01, expiry: 2028-03-31) |

### Justification

ChemSupply GmbH contract expires 2025-03-31 and will not be renewed due to quality issues identified in QA audit QA-2024-089. BioReagents France S.A.S. was selected after competitive tender (Procurement ref: TENDER-2025-LAB-003). The new supplier processes identical categories of personal data (supplier contact name, email, phone, bank account for payment) and is established in the EEA. No new international transfer is introduced. DPA-2025-BRF-008 has been reviewed and approved by the DPO office on 2025-02-20.

---

## Supporting Evidence

| Document | Reference | Attached |
|----------|-----------|----------|
| IT change request | N/A (no IT system change) | N/A |
| Art. 28 DPA | DPA-2025-BRF-008 | [x] |
| DPIA | N/A (no DPIA triggered — standard supplier processing unchanged) | N/A |
| Transfer Impact Assessment | N/A (intra-EEA transfer only) | N/A |
| Audit finding | N/A | N/A |
| Regulatory reference | N/A | N/A |
| Supplier termination notice | TERM-2025-CSG-001 (sent to ChemSupply GmbH 2025-01-31) | [x] |

---

## Impact Assessment

**Does this change affect other RoPA entries?** [ ] Yes [x] No

**Does this change require a privacy notice update?** [ ] Yes [x] No

(Supplier privacy notice PN-SUP-2024-001 already covers the category "laboratory reagent suppliers" generically, so no update needed.)

**Does this change require a DPIA or DPIA update?** [ ] Yes [x] No

(Supplier management processing is unchanged in nature, scope, and risk profile.)

---

## Version Impact

**Current RoPA version**: 4.2.0
**Proposed version after change**: 4.3.0

- [ ] Major version increment (new/removed processing activity)
- [x] Minor version increment (field content update)
- [ ] Patch version increment (administrative correction)

---

## Review and Approval

| Step | Reviewer | Decision | Date | Comments |
|------|----------|----------|------|----------|
| Privacy analyst review | Sophie Krause | [x] Approve [ ] Revise | 2025-03-03 | DPA-2025-BRF-008 reviewed, compliant with Art. 28 requirements |
| DPO review | Dr. Elena Voss | [x] Approve [ ] Revise [ ] Reject | 2025-03-05 | Approved. No additional risk introduced. ChemSupply data deletion confirmed for DPA-2022-CSG-003 wind-down. |
| Processing owner sign-off | Anna Bergmann | [x] Confirm accuracy | 2025-03-05 | Values confirmed against signed DPA and supplier master data |

---

## Post-Implementation Verification

| Check | Completed | Date | Verified By |
|-------|-----------|------|-------------|
| RoPA system updated | [x] | 2025-03-06 | Sophie Krause |
| Version number incremented | [x] | 2025-03-06 | Sophie Krause |
| Change log updated | [x] | 2025-03-06 | Sophie Krause |
| Processing owner notified | [x] | 2025-03-06 | Sophie Krause |
| Automated validation passed | [x] | 2025-03-06 | Automated (RoPA validation script v2.1) |
| Privacy notice update triggered (if applicable) | N/A | N/A | N/A |
| ChemSupply GmbH data deletion confirmation requested | [x] | 2025-03-06 | Anna Bergmann |

---

*Submit this form to the DPO office at dpo@helix-biotech.eu for processing.*
