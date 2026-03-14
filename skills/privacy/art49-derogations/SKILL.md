---
name: art49-derogations
description: >-
  Guides assessment and application of GDPR Article 49 derogation conditions for
  international data transfers in the absence of adequacy decisions or appropriate
  safeguards. Covers explicit consent, contract necessity, public interest, vital
  interests, public register, and compelling legitimate interests with restrictive
  interpretation per EDPB Guidelines 2/2018. Keywords: Art. 49, derogations,
  transfer exceptions, explicit consent, compelling legitimate interests.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cross-border-transfers
  tags: "article-49, derogations, transfer-exceptions, explicit-consent, legitimate-interests"
---

# Assessing Article 49 Derogations

## Overview

Article 49 GDPR provides a limited set of derogations permitting international data transfers in the absence of an adequacy decision (Art. 45) or appropriate safeguards (Art. 46). The EDPB has consistently emphasised in Guidelines 2/2018 on derogations under Article 49 (adopted 25 May 2018, last updated 6 February 2018) that these derogations must be interpreted restrictively and are intended as exceptions rather than the rule. They cannot serve as a basis for systematic, large-scale, or regular transfers.

## Derogation Conditions

### Art. 49(1)(a) — Explicit Consent

**Condition**: The data subject has explicitly consented to the proposed transfer, after having been informed of the possible risks of such transfers for the data subject due to the absence of an adequacy decision and appropriate safeguards.

**Requirements**:
1. **Specific**: Consent must specifically cover the transfer to the identified third country, not merely the processing activity itself.
2. **Informed**: The data subject must be told:
   - The specific third country or countries to which data will be transferred
   - The absence of an adequacy decision for that country
   - The absence of appropriate safeguards (SCCs, BCRs)
   - The specific risks arising from this (e.g., government access without EU-equivalent protections)
3. **Explicit**: Must be an unambiguous affirmative statement; implied consent or pre-ticked boxes are insufficient.
4. **Freely given**: No detriment to the data subject for withholding consent; must be a genuine choice.
5. **Withdrawable**: Data subject can withdraw consent at any time; withdrawal does not affect lawfulness of prior transfers.

**Athena Global Logistics example use case**: A European customer requests that their consignment tracking data be shared with their own broker in a non-adequate country. The customer is informed of the risks and explicitly consents via a signed transfer consent form.

**Limitations (EDPB Guidelines 2/2018)**:
- Cannot be used for systematic, repetitive, or large-scale transfers
- Not appropriate in employer-employee relationships due to the power imbalance (consent is unlikely to be freely given)
- Not a substitute for establishing systematic transfer mechanisms

### Art. 49(1)(b) — Necessary for Contract Performance

**Condition**: The transfer is necessary for the performance of a contract between the data subject and the controller, or the implementation of pre-contractual measures taken at the data subject's request.

**Requirements**:
1. **Direct contractual relationship**: A contract exists between the data subject and the controller (not between two controllers or a controller and a third party).
2. **Necessity**: The transfer must be objectively necessary for performing the contract — not merely useful or commercially convenient.
3. **Close and substantial connection**: There must be a close link between the transfer and the performance of the specific contractual obligation.
4. **Occasional**: This derogation is appropriate for occasional transfers; systematic reliance is not permitted.

**Athena Global Logistics example use case**: A European individual customer contracts Athena to ship personal effects to a non-adequate country. Transfer of the customer's address and contact details to the destination country delivery partner is necessary to perform the shipping contract.

**EDPB restrictive interpretation**:
- The contract must be with the data subject themselves, not with a corporate customer transferring employee data
- The fact that a transfer is commercially necessary is not sufficient; it must be contractually necessary
- If alternative means of contract performance exist that do not require the transfer, this derogation may not apply

### Art. 49(1)(c) — Necessary for Contract in the Interest of the Data Subject

**Condition**: The transfer is necessary for the conclusion or performance of a contract concluded in the interest of the data subject between the controller and another natural or legal person.

**Requirements**:
1. **Contract between controller and a third party**: Unlike Art. 49(1)(b), this covers contracts where the data subject is not a party.
2. **In the interest of the data subject**: The contract must serve the data subject's interests (e.g., insurance taken out on their behalf, travel arrangements made for them).
3. **Necessity**: The transfer must be objectively necessary for the contract, not merely convenient.
4. **Occasional**: Not a basis for systematic transfers.

**Athena Global Logistics example use case**: Athena arranges cargo insurance with a non-EU insurer on behalf of a customer. The transfer of the customer's details to the insurer is in the customer's interest to ensure coverage.

### Art. 49(1)(d) — Important Reasons of Public Interest

**Condition**: The transfer is necessary for important reasons of public interest.

**Requirements**:
1. **Recognised in EU or Member State law**: The public interest must be recognised in Union law or in the law of the Member State to which the controller is subject.
2. **Important**: Not any public interest qualifies; it must be of significant importance (e.g., international cooperation for tax enforcement, anti-money laundering, cross-border criminal investigations).
3. **Necessary**: The transfer must be necessary to serve that public interest.
4. **Cannot be used by private entities for commercial purposes**: Private companies cannot invoke public interest to justify commercial data transfers.

**Athena Global Logistics example use case**: Transfer of customer identity and shipment data to a third-country customs authority pursuant to a bilateral customs cooperation agreement between Germany and the third country, as required by EU Regulation 952/2013 (Union Customs Code).

### Art. 49(1)(e) — Legal Claims

**Condition**: The transfer is necessary for the establishment, exercise, or defence of legal claims.

**Requirements**:
1. **Actual or contemplated proceedings**: There must be actual legal proceedings or a concrete and identifiable prospect of proceedings (not merely a theoretical possibility).
2. **Necessity**: Only the data necessary for the legal claim may be transferred.
3. **Broad scope**: Covers judicial proceedings, administrative proceedings, and out-of-court procedures including regulatory investigations.
4. **Occasional**: Transfers must be linked to specific proceedings, not used as a routine transfer basis.

**Athena Global Logistics example use case**: Transfer of employment records to a non-EU jurisdiction where a former employee has filed a labour dispute claim, and the records are necessary for the company's defence.

### Art. 49(1)(f) — Vital Interests

**Condition**: The transfer is necessary in order to protect the vital interests of the data subject or of other persons, where the data subject is physically or legally incapable of giving consent.

**Requirements**:
1. **Life or death**: Vital interests typically relate to life-threatening situations (medical emergencies, natural disasters).
2. **Incapacity**: The data subject must be unable to consent (unconscious, incapacitated, or legally incapable).
3. **Strict necessity**: Only data strictly necessary to protect the vital interest.
4. **Rare application**: This derogation is very narrow and applies to genuine emergency situations.

**Athena Global Logistics example use case**: Transfer of a crew member's medical records to a third-country hospital following a medical emergency during international transport operations.

### Art. 49(1)(g) — Public Register

**Condition**: The transfer is made from a register which according to Union or Member State law is intended to provide information to the public and which is open to consultation either by the public in general or by any person who can demonstrate a legitimate interest.

**Requirements**:
1. **Legally established public register**: The register must be established by law with the explicit purpose of public access.
2. **Not the entire register**: Only specific entries may be transferred, not bulk copies of the entire register.
3. **Conditions for consultation met**: The conditions for access specified in the law establishing the register must be fulfilled.

**Athena Global Logistics example use case**: Transfer of company registration data from the German Handelsregister to a non-EU business partner for due diligence purposes, where the Handelsregister is a public register under German law.

### Art. 49(1) second subparagraph — Compelling Legitimate Interests

**Condition**: Where none of the other derogations applies, a transfer may take place if: (a) the transfer is not repetitive; (b) concerns only a limited number of data subjects; (c) is necessary for the purposes of compelling legitimate interests pursued by the controller; (d) these interests are not overridden by the interests or rights and freedoms of the data subject; and (e) the controller has assessed all the circumstances surrounding the transfer and has provided suitable safeguards.

**Requirements**:
1. **Last resort**: This is the derogation of last resort, applicable only when no other Art. 49 condition is met and no Art. 45/46 mechanism is available.
2. **Not repetitive**: One-time or very occasional transfers only.
3. **Limited data subjects**: Small number of individuals affected.
4. **Compelling legitimate interest**: Higher threshold than ordinary Art. 6(1)(f) legitimate interest; must be compelling.
5. **Balancing test**: Controller must document the balancing of its interests against the data subjects' rights and freedoms.
6. **Suitable safeguards**: Controller must provide suitable safeguards regarding the protection of personal data.
7. **SA notification**: The controller must inform the supervisory authority of the transfer.
8. **Data subject information**: The controller must inform the data subject of the transfer and the compelling legitimate interests pursued.

**Athena Global Logistics example use case**: A one-time transfer of a former employee's contact details to a non-EU regulatory authority investigating a historical compliance matter, where no other derogation applies and the transfer concerns a single individual.

## Decision Tree for Art. 49 Derogation Selection

```
Is there an adequacy decision for the destination country? (Art. 45)
  ├── YES → Transfer under adequacy; Art. 49 not needed
  └── NO → Can appropriate safeguards be established? (Art. 46)
        ├── YES → Use SCCs/BCRs/etc.; Art. 49 not needed
        └── NO → Is the transfer systematic, repetitive, or large-scale?
              ├── YES → Art. 49 derogations generally NOT available
              │         (establish Art. 46 safeguards instead)
              └── NO → Apply Art. 49 derogation assessment:
                    ├── Has the data subject explicitly consented? → Art. 49(1)(a)
                    ├── Is transfer necessary for DS contract? → Art. 49(1)(b)
                    ├── Is transfer for a contract in DS interest? → Art. 49(1)(c)
                    ├── Is transfer for important public interest? → Art. 49(1)(d)
                    ├── Is transfer for legal claims? → Art. 49(1)(e)
                    ├── Is transfer for vital interests? → Art. 49(1)(f)
                    ├── Is transfer from a public register? → Art. 49(1)(g)
                    └── None of the above? → Art. 49(1) compelling legitimate interests
                          (last resort, with SA notification)
```

## Documentation Requirements

For every transfer relying on an Art. 49 derogation, the following must be documented:

1. **Derogation relied upon**: Specific Art. 49 sub-paragraph
2. **Justification**: Why the derogation applies to this specific transfer
3. **Why Art. 45/46 mechanisms are not available**: Explanation of why adequacy or appropriate safeguards cannot be used
4. **Necessity analysis**: Why the transfer is necessary (not merely useful or convenient)
5. **Data minimisation**: Confirmation that only the minimum necessary data is transferred
6. **Occasional nature**: Confirmation that the transfer is not systematic or repetitive
7. **Risk to data subjects**: Assessment of the risks arising from the transfer
8. **Safeguards applied**: Any safeguards implemented to mitigate risks
9. **For Art. 49(1)(a)**: Copy of the consent form and evidence of information provided
10. **For Art. 49(1) compelling legitimate interests**: SA notification record, balancing test documentation, and suitable safeguards description
