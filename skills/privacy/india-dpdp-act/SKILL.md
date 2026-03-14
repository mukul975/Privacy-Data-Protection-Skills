---
name: india-dpdp-act
description: >-
  Guides compliance with India's Digital Personal Data Protection Act 2023. Covers
  consent manager registration, data fiduciary obligations under Sections 4-7,
  significant data fiduciary requirements under Section 10, data principal rights,
  and Board enforcement framework. Keywords: DPDP Act, India data protection,
  consent manager, data fiduciary, significant data fiduciary, data principal rights.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: global-privacy-regulations
  tags: "dpdp-act, india-data-protection, consent-manager, data-fiduciary, data-principal"
---

# India DPDP Act 2023 Compliance

## Overview

The Digital Personal Data Protection Act, 2023 (DPDP Act) received Presidential assent on 11 August 2023 and was notified in the Gazette of India as Act No. 22 of 2023. The DPDP Act establishes India's first comprehensive personal data protection framework, replacing the data protection provisions of the Information Technology Act, 2000 (Section 43A and the Sensitive Personal Data or Information Rules, 2011). The Act applies to digital personal data processing within India and to processing outside India if it involves offering goods or services to data principals in India (Section 3).

The Data Protection Board of India (DPBI) is established under Section 18 as the adjudicatory body for enforcement. The Central Government retains rule-making authority under Section 40 to prescribe detailed implementing rules.

**Status as of March 2026**: The Central Government has published draft DPDP Rules for public consultation. Several provisions await final notification of the rules for full operationalisation.

## Key Definitions

| Term | Definition | DPDP Act Section |
|------|-----------|-----------------|
| Data Principal | The individual to whom the personal data relates; for children (under 18), the parent/lawful guardian | Section 2(j) |
| Data Fiduciary | Any person who alone or in conjunction with others determines the purpose and means of processing personal data | Section 2(i) |
| Data Processor | Any person who processes personal data on behalf of a data fiduciary | Section 2(k) |
| Consent Manager | A person registered with the Board who acts as a single point of contact for the data principal to manage consent | Section 2(g) |
| Significant Data Fiduciary | A data fiduciary designated as such by the Central Government based on prescribed criteria | Section 10 |
| Personal Data | Any data about an individual who is identifiable by or in relation to such data | Section 2(t) |

## Data Fiduciary Obligations (Sections 4-7)

### Section 4: Grounds for Processing

Personal data may be processed only for a lawful purpose and only with the consent of the data principal or for certain legitimate uses.

| Ground | Section | Detail |
|--------|---------|--------|
| Consent | Section 6 | Free, specific, informed, unconditional, unambiguous consent with clear affirmative action |
| Legitimate uses | Section 7 | Seven specified legitimate use categories (see below) |

### Section 5: Notice Before Consent Collection

Before collecting consent, the data fiduciary must provide notice to the data principal containing:
1. Description of personal data to be processed and the purpose of processing
2. How the data principal may exercise rights (complaint to Board, grievance redressal)
3. How the data principal may make a complaint to the Board

The notice must be in English or any of the 22 languages listed in the Eighth Schedule to the Constitution of India.

### Section 6: Consent Requirements

| Requirement | Detail |
|-------------|--------|
| Nature | Free, specific, informed, unconditional, and unambiguous |
| Form | Clear affirmative action signifying agreement; no bundled consent for multiple purposes |
| Scope limitation | Limited to the specified purpose; fresh consent required for new purposes |
| Withdrawal | Data principal may withdraw consent at any time; withdrawal must be as easy as giving consent |
| Effect of withdrawal | Data fiduciary must cease processing (and cause processors to cease) within a reasonable period; does not affect lawfulness of prior processing |
| Deemed consent for existing data | Section 6(4): For personal data processed before the Act's commencement, processing may continue if consent would have been required; the data fiduciary must provide notice as soon as reasonably practicable |

### Section 7: Legitimate Uses (Without Consent)

| Legitimate Use | Section 7 Clause | Scope |
|---------------|------------------|-------|
| Specified purpose for which data was provided voluntarily | Section 7(a) | Data principal voluntarily provides data for a specified purpose (e.g., applying for a government benefit) |
| State functions | Section 7(b) | Processing by the State or its instrumentalities for subsidies, benefits, services, licences, permits |
| Legal obligation | Section 7(c) | Processing under any law for compliance with any judgement or order |
| Medical emergency | Section 7(d) | Responding to a medical emergency involving a threat to life or health |
| Epidemic/disaster response | Section 7(e) | Processing during an epidemic, outbreak, or threat to public health; disaster or public order breakdown |
| Employment purposes | Section 7(f) | Processing by employer for employment purposes (prevention of espionage, maintaining confidentiality, recruitment, attendance verification, assessment) |
| Public interest | Section 7(g) | Processing for purposes as may be prescribed by the Central Government |

## Consent Manager Framework (Section 6(7))

### Registration Requirements
A Consent Manager must be registered with the Data Protection Board and must:
- Be accountable to the data principal
- Act as a single point of contact to enable the data principal to give, manage, review, and withdraw consent
- Interoperable, accessible, and transparent

### Consent Manager Obligations (Draft DPDP Rules)

| Obligation | Detail |
|-----------|--------|
| Registration | Must register with the Board; registration valid for 3 years (renewable) |
| Capital requirement | Minimum net worth of INR 2 crore (approximately USD 240,000) |
| Interoperability | Must be interoperable with other consent managers and data fiduciaries |
| Data principal interface | User-friendly dashboard showing all active consents, purposes, and withdrawal options |
| Record-keeping | Maintain auditable records of all consent transactions for 7 years |
| Independence | Must not have any conflict of interest with data fiduciaries it serves |

### Zenith Global Enterprises Consent Manager Integration

| Element | Detail |
|---------|--------|
| Registered consent managers engaged | DigiConsent India Pvt Ltd (Reg. No. CM-2025-001) |
| Integration method | API integration with Zenith's customer portal and employee HRMS |
| Data principal dashboard | Accessible at zenithglobal.in/privacy-dashboard in English and Hindi |
| Consent transaction volume | Approximately 50,000 consent records per month |

## Significant Data Fiduciary (Section 10)

### Designation Criteria

The Central Government may designate a data fiduciary as a Significant Data Fiduciary (SDF) based on:
- Volume and sensitivity of personal data processed
- Risk to the rights of data principals
- Potential impact on the sovereignty and integrity of India
- Risk to electoral democracy
- Security of the State
- Public order

### Additional SDF Obligations (Section 10)

| Obligation | Detail |
|-----------|--------|
| Data Protection Officer (DPO) | Appoint a DPO based in India who represents the SDF and is the point of contact for the data principal and Board (Section 10(2)(a)) |
| Independent data auditor | Appoint an independent data auditor to evaluate compliance; audit report submitted to the Board (Section 10(2)(b)) |
| Data Protection Impact Assessment (DPIA) | Conduct periodic DPIAs as prescribed (Section 10(2)(c)) |
| Periodic audits | Regular compliance audits by the independent auditor |
| Algorithmic transparency | If using algorithmic processing likely to affect data principals, ensure fairness and transparency |

### Zenith Global Enterprises SDF Assessment

| Criterion | Assessment | Designation Risk |
|-----------|-----------|-----------------|
| Volume of personal data | 500,000+ data principals in India | Medium-High |
| Sensitivity of data | Financial data, identity documents for customs | Medium |
| Impact on data principals | Moderate (business logistics, not consumer profiling) | Medium |
| Sovereignty/security risk | Low (commercial logistics, no government data processing) | Low |
| Overall SDF likelihood | Medium — monitoring Central Government notifications | — |

## Data Principal Rights (Sections 11-14)

| Right | Section | Detail | Implementation |
|-------|---------|--------|----------------|
| Right to access information about processing | Section 11(1)(a) | Summary of personal data processed and processing activities | Privacy portal in English and Hindi |
| Right to access identities of data fiduciaries and processors | Section 11(1)(b) | Identity of all data fiduciaries and processors who have been shared data | Data sharing register accessible to data principals |
| Right to correction and erasure | Section 12 | Right to correction of inaccurate or misleading data; right to erasure of data no longer necessary for the purpose | Self-service correction in portal; erasure request workflow |
| Right to grievance redressal | Section 13 | Right to nominate a person to exercise rights in case of death or incapacity; right to have grievances addressed within prescribed period | Grievance officer designated; 30-day response target |
| Right to nominate | Section 14 | Right to nominate another person to exercise rights in case of death or incapacity | Nomination form available in privacy portal |

### Data Principal Duties (Section 15)

The DPDP Act uniquely imposes duties on data principals:
- Not to register a false or frivolous complaint with the Board
- Not to furnish false or misleading information when exercising rights
- Not to suppress material information when exercising rights
- Not to impersonate another person while interacting with data fiduciary

Breach of data principal duties can result in a penalty of up to INR 10,000.

## Children's Data Protection (Section 9)

| Requirement | Detail |
|-------------|--------|
| Age of consent | 18 years (no differentiation; all individuals under 18 are children) |
| Verifiable parental consent | Consent of parent or lawful guardian required before processing child's data |
| Prohibition on harmful processing | No tracking, behavioural monitoring, or targeted advertising directed at children |
| Prohibition on detrimental processing | No processing likely to cause detrimental effect on the well-being of a child |
| Exemptions | Central Government may exempt certain data fiduciaries or classes of data fiduciaries from some child protection requirements (e.g., for educational or health purposes) |

## Cross-Border Data Transfer (Section 16)

### Transfer Framework
The Central Government may, by notification, restrict the transfer of personal data to countries or territories specified in the notification (blacklist approach). Transfer is permitted to all destinations not appearing on the restricted list.

| Element | Detail |
|---------|--------|
| Default position | Transfer permitted unless the destination is specifically restricted by Central Government notification |
| Restricted destinations | To be notified by the Central Government (none notified as of March 2026) |
| Sector-specific restrictions | Certain sectoral regulations (e.g., RBI data localisation circular for payment data) continue to apply |
| Contractual safeguards | While not legally mandated under DPDP Act, contractual safeguards recommended as best practice |

### Zenith Global Enterprises Transfer Register

| Transfer Flow | Destination | Sectoral Restriction | Status |
|---------------|-------------|---------------------|--------|
| Customer data → EU HQ | Germany | None | Active |
| Employee data → Regional HR | Singapore | None | Active |
| Payment data → Global Treasury | United Kingdom | RBI localisation applies to payment system data (stored in India, processed copy abroad) | Active with localisation |
| Logistics data → APAC operations | Japan | None | Active |

## Enforcement Framework

### Data Protection Board of India (Section 18)

| Function | Detail |
|---------|--------|
| Adjudicatory body | Determines whether data fiduciaries have breached the Act |
| Complaint handling | Receives complaints from data principals; investigates and adjudicates |
| Penalty imposition | Imposes financial penalties per the Schedule to the Act |
| Appeals | Appeals from Board decisions lie to the Telecom Disputes Settlement and Appellate Tribunal (TDSAT) |

### Penalty Schedule

| Violation | Maximum Penalty (INR) | Maximum Penalty (USD approx.) |
|-----------|----------------------|------------------------------|
| Failure to take reasonable security safeguards (leading to breach) | INR 250 crore (2.5 billion) | USD 30 million |
| Failure to notify the Board and data principals of a breach | INR 200 crore (2 billion) | USD 24 million |
| Non-fulfilment of obligations related to children | INR 200 crore (2 billion) | USD 24 million |
| Non-fulfilment of additional SDF obligations | INR 150 crore (1.5 billion) | USD 18 million |
| Other breaches by data fiduciary or processor | INR 50 crore (500 million) | USD 6 million |
| Breach of data principal duties | INR 10,000 | USD 120 |

### Breach Notification (Section 8(6))

| Element | Requirement |
|---------|-------------|
| Obligation | Data fiduciary must notify the Board and each affected data principal of a personal data breach |
| Content | Form and manner as may be prescribed by the Board |
| Timeline | As prescribed in the rules (expected to be within 72 hours based on draft rules) |
| Scope | Breaches that are likely to cause harm to the data principal |

## Compliance Programme

| Component | Detail |
|-----------|--------|
| Grievance Officer (India) | Rajesh Sharma, Head of Compliance — Mumbai office |
| Privacy notice | Published at zenithglobal.in/privacy in English and Hindi |
| Consent manager integration | DigiConsent India API integration for customer consent management |
| Employee processing | Section 7(f) legitimate use for employment purposes; consent for non-employment processing |
| Security safeguards | Reasonable security safeguards per Section 8(4): encryption, access control, incident response |
| Breach notification | Procedure for notification to Board and data principals per Section 8(6) |
| Data processor contracts | Written contracts with all processors per Section 8(2): process only per instructions, implement safeguards |
| Retention limitation | Data deleted upon purpose fulfilment or consent withdrawal, unless retention required by law (Section 8(7)) |
| Annual training | DPDP Act compliance training for all India employees |
