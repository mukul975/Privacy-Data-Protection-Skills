---
name: implementing-lawful-basis-assessment
description: >-
  Guides determination of the correct lawful basis under GDPR Article 6(1)(a)-(f)
  for each processing activity. Includes decision tree logic for consent vs
  legitimate interest vs contract necessity. Activate when evaluating legal grounds
  for processing or reviewing lawful basis selections. Keywords: lawful basis,
  Article 6, consent, legitimate interest, legal obligation, contract.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: gdpr-compliance
  tags: "gdpr, lawful-basis, article-6, consent, legitimate-interest, processing-grounds"
---

# Implementing Lawful Basis Assessment

## Overview

Every processing activity under GDPR must have a valid lawful basis established before processing begins. Article 6(1) provides six mutually non-exclusive bases. Selecting the wrong basis creates compliance risk, may invalidate the processing entirely, and can result in enforcement action. This skill provides a systematic methodology for evaluating and documenting the appropriate lawful basis.

## The Six Lawful Bases — Art. 6(1)

### (a) Consent
The data subject has given consent to the processing of their personal data for one or more specific purposes.

**Requirements per Art. 7 and Recital 32:**
- Freely given: genuine choice, no imbalance of power, no conditionality (Art. 7(4))
- Specific: granular consent for distinct processing purposes
- Informed: clear plain language about identity, purpose, data types, rights
- Unambiguous: clear affirmative action (no pre-ticked boxes, no silence)
- Withdrawable: as easy to withdraw as to give (Art. 7(3))

**Best suited for:** Marketing communications, cookies/tracking, research participation, sharing data with third parties for their own purposes.

**Not appropriate when:** There is a power imbalance (employer-employee, public authority-citizen), processing is necessary for another basis, or withdrawal would be impractical.

### (b) Contract Performance
Processing is necessary for the performance of a contract to which the data subject is party, or to take steps at the data subject's request prior to entering into a contract.

**Key test:** Would the contract be impossible to perform without this specific processing? The processing must be objectively necessary, not merely useful or standard practice.

**Best suited for:** Delivering purchased goods, processing payments, providing contracted services, pre-contractual enquiries at the data subject's request.

**Not appropriate when:** Processing is useful but not necessary for the contract (e.g., profiling customers is not necessary to deliver their order).

### (c) Legal Obligation
Processing is necessary for compliance with a legal obligation to which the controller is subject.

**Requirements:**
- The obligation must be laid down by EU or Member State law (not contractual obligations)
- The law must be sufficiently clear about the processing required
- The processing must be limited to what is necessary to comply

**Best suited for:** Tax reporting, employment law obligations, anti-money laundering checks, regulatory reporting, court orders.

### (d) Vital Interests
Processing is necessary to protect the vital interests of the data subject or of another natural person.

**Requirements:**
- Relates to life-or-death situations or serious medical emergencies
- Cannot be used if another lawful basis is available (Recital 46)
- Very narrow scope in practice

**Best suited for:** Emergency medical treatment for unconscious patients, disaster response, humanitarian crises.

### (e) Public Task
Processing is necessary for the performance of a task carried out in the public interest or in the exercise of official authority vested in the controller.

**Requirements:**
- Must have a basis in EU or Member State law
- The specific task or function must be defined in law
- Primarily applies to public authorities and bodies

**Best suited for:** Public administration, law enforcement, statutory functions of public bodies, public health monitoring.

### (f) Legitimate Interests
Processing is necessary for the purposes of the legitimate interests pursued by the controller or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject.

**Requirements (three-part test):**
1. Purpose test: Is there a legitimate interest? (commercial, societal, or individual)
2. Necessity test: Is the processing necessary for that interest? (no less intrusive alternative)
3. Balancing test: Do the data subject's interests override the controller's?

**Best suited for:** Fraud prevention, network security, direct marketing to existing customers, intra-group administrative transfers, internal analytics.

**Not available to:** Public authorities in the performance of their tasks (Art. 6(1) final paragraph).

## Decision Tree for Lawful Basis Selection

### Step 1: Is the processing required by law?
- **YES** → Art. 6(1)(c) Legal Obligation. Identify the specific law and provision.
- **NO** → Proceed to Step 2.

### Step 2: Is the processing necessary to perform a contract with the data subject?
- **YES** → Art. 6(1)(b) Contract Performance. Verify objective necessity (not just convenience).
- **NO** → Proceed to Step 3.

### Step 3: Is this a life-threatening or medical emergency?
- **YES** → Art. 6(1)(d) Vital Interests. Document why no other basis applies.
- **NO** → Proceed to Step 4.

### Step 4: Is the controller a public authority performing a statutory function?
- **YES** → Art. 6(1)(e) Public Task. Identify the legal basis for the task.
- **NO** → Proceed to Step 5.

### Step 5: Does the controller have a legitimate interest that requires this processing?
- **YES** → Conduct a Legitimate Interest Assessment (three-part test).
  - If the LIA concludes the controller's interest is not overridden → Art. 6(1)(f).
  - If the LIA concludes the data subject's rights prevail → Consider consent or do not process.
- **NO** → Proceed to Step 6.

### Step 6: Can the data subject provide valid consent?
- Verify: no power imbalance, genuine choice, specific purpose, can withdraw without detriment.
- **YES** → Art. 6(1)(a) Consent. Implement compliant consent mechanism.
- **NO** → Processing may not have a valid lawful basis. Do not proceed. Consult the DPO.

## Documentation Requirements

For each processing activity, document:

1. **Processing activity name and RoPA reference**: Link to the Art. 30 record.
2. **Selected lawful basis**: Cite the specific Art. 6(1) paragraph.
3. **Rationale**: Explain why this basis was selected and why alternatives were rejected.
4. **Necessity analysis**: Demonstrate why the processing is necessary for the stated basis (not merely useful).
5. **Supporting evidence**: Reference the specific law (for legal obligation), contract (for contract performance), LIA (for legitimate interest), or consent mechanism (for consent).
6. **Special category data**: If Art. 9 data is involved, identify the additional Art. 9(2) condition.
7. **Criminal offence data**: If Art. 10 data is involved, confirm the specific authorisation in EU/Member State law.
8. **Review date**: Set the next review date (recommended: annually or upon material change).

## Common Assessment Errors

1. **Defaulting to consent**: Using consent when another basis is more appropriate, creating unnecessary withdrawal risk.
2. **Stretching contract performance**: Claiming processing is necessary for a contract when it is merely beneficial (e.g., profiling for cross-selling is not necessary to fulfil a purchase order).
3. **Citing non-existent legal obligations**: Referencing industry standards or contractual requirements as "legal obligations" when they do not constitute EU or Member State law.
4. **Ignoring the necessity test**: Selecting a basis without demonstrating that the specific processing is necessary (not just the purpose).
5. **Switching bases post-hoc**: Changing the lawful basis after processing has begun when the original basis fails, without valid justification.
6. **Overlooking power imbalances**: Relying on employee consent for workplace processing where genuine free choice is absent.

## Integration with Other GDPR Requirements

- **Transparency (Art. 13/14)**: The lawful basis must be communicated to data subjects in the privacy notice.
- **Data subject rights**: The lawful basis determines which rights are available (e.g., right to erasure is limited where legal obligation applies; right to data portability only applies to consent and contract).
- **RoPA (Art. 30)**: The lawful basis should be recorded alongside each processing activity.
- **DPIA (Art. 35)**: High-risk processing may require a DPIA regardless of which lawful basis is selected.
