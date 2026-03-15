---
name: multi-jurisdiction-matrix
description: >-
  Guides building a multi-jurisdiction privacy compliance matrix for organisations
  operating across multiple countries. Covers common requirements identification,
  jurisdiction-specific deltas, gap analysis, and harmonised control frameworks.
  Keywords: multi-jurisdiction, compliance matrix, harmonised controls, gap analysis,
  jurisdiction mapping.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: global-privacy-regulations
  tags: "multi-jurisdiction, compliance-matrix, harmonised-controls, gap-analysis, jurisdiction-mapping"
---

# Multi-Jurisdiction Privacy Compliance Matrix

## Overview

Organisations operating across multiple jurisdictions face the challenge of complying with overlapping, divergent, and sometimes conflicting privacy requirements. A multi-jurisdiction compliance matrix provides a structured approach to identifying common requirements across all applicable privacy laws, mapping jurisdiction-specific variations (deltas), identifying gaps between current compliance posture and legal requirements, and designing harmonised controls that satisfy the most stringent requirements across all jurisdictions.

## Compliance Matrix Structure

### Dimension 1: Requirement Categories

| Category | Sub-Categories |
|----------|---------------|
| Lawful basis for processing | Consent, legitimate interest, contract, legal obligation, vital interests, public interest |
| Individual rights | Access, correction, deletion/erasure, portability, restriction, objection, automated decision review |
| Consent management | Form, withdrawal, children, sensitive data, separate consent |
| Data collection and notice | Notice content, timing, language, format |
| Cross-border transfers | Mechanisms, adequacy, contractual safeguards, data localisation |
| Data protection officer | Appointment criteria, qualifications, independence, functions |
| Breach notification | Authority notification, individual notification, timelines, content |
| Impact assessment | When required, contents, review cycle |
| Security safeguards | Technical measures, organisational measures, encryption, access control |
| Retention and deletion | Limitation periods, destruction methods, legal holds |
| Enforcement and penalties | Administrative fines, criminal penalties, civil liability |
| Record-keeping | Processing records, consent records, transfer records, breach records |

### Dimension 2: Jurisdictions

For Zenith Global Enterprises, the compliance matrix covers:

| Jurisdiction | Primary Law | Regulator |
|-------------|-------------|-----------|
| European Union | GDPR | National DPAs / EDPB |
| United Kingdom | UK GDPR + DPA 2018 | ICO |
| Brazil | LGPD (Lei 13.709/2018) | ANPD |
| China | PIPL | CAC |
| South Korea | PIPA | PIPC |
| India | DPDP Act 2023 | DPBI |
| Thailand | PDPA B.E. 2562 | PDPC |
| Singapore | PDPA 2012 | PDPC |
| Japan | APPI | PPC |
| Australia | Privacy Act 1988 | OAIC |
| United States | State laws (CCPA/CPRA, etc.) | State AGs / CPPA (California) |

## Cross-Jurisdiction Requirement Comparison

### Lawful Bases Comparison

| Jurisdiction | Consent | Contract | Legitimate Interest | Legal Obligation | Vital Interests | Other Unique Bases |
|-------------|---------|----------|-------------------|-----------------|-----------------|-------------------|
| EU (GDPR) | Art. 6(1)(a) | Art. 6(1)(b) | Art. 6(1)(f) | Art. 6(1)(c) | Art. 6(1)(d) | Public interest (Art. 6(1)(e)) |
| Brazil (LGPD) | Art. 7, I | Art. 7, V | Art. 7, IX | Art. 7, II | Art. 7, VII | Credit protection (Art. 7, X); Research (Art. 7, IV); Public policy (Art. 7, III); Health (Art. 7, VIII); Exercise of rights (Art. 7, VI) |
| China (PIPL) | Art. 13(1) | Art. 13(2) | None | Art. 13(3) | Art. 13(4) | Publicly disclosed (Art. 13(6)); Other statutory (Art. 13(7)) |
| Korea (PIPA) | Art. 15(1)(1) | Art. 15(1)(4) | Art. 15(1)(6) (2023) | Art. 15(1)(2) | Art. 15(1)(5) | Public institution duty (Art. 15(1)(3)) |
| India (DPDP) | Section 6 | N/A (under legitimate uses) | N/A | Section 7(c) | Section 7(d) | Employment (Section 7(f)); State functions (Section 7(b)) |
| Japan (APPI) | Implied consent | Permitted purpose | None (use limitation approach) | Statutory basis | Life protection | Pseudonymous processing (relaxed rules) |

### Breach Notification Timeline Comparison

| Jurisdiction | Authority Timeline | Individual Timeline | Threshold |
|-------------|-------------------|--------------------|-----------|
| EU (GDPR) | 72 hours from awareness | Without undue delay | Risk to rights and freedoms |
| UK GDPR | 72 hours from awareness | Without undue delay | Risk to rights and freedoms |
| Brazil (LGPD) | 3 business days | 3 business days | Relevant risk or damage |
| China (PIPL) | Promptly (no fixed deadline) | Promptly | Any PI security incident |
| Korea (PIPA) | 72 hours (1,000+ individuals) | Without delay | Any breach |
| India (DPDP) | 72 hours (draft rules) | 72 hours (draft rules) | Likely harm to data principal |
| Thailand (PDPA) | 72 hours | Without delay if high risk | Affects rights and freedoms |
| Singapore (PDPA) | 3 calendar days after assessment | As soon as practicable | Significant harm OR 500+ individuals |
| Japan (APPI) | 3-5 business days (preliminary) | Promptly | PPC-defined thresholds |
| Australia (Privacy Act) | As soon as practicable (30-day assessment) | As soon as practicable | Likely serious harm |

### Children's Age Thresholds

| Jurisdiction | Age Threshold | Parental Consent Mechanism |
|-------------|--------------|---------------------------|
| EU (GDPR) | 16 (Member States may lower to 13) | Art. 8: Parental consent for ISS |
| Brazil (LGPD) | Best interest standard | At least one parent's consent |
| China (PIPL) | Under 14 = minor PI | Parent/guardian consent |
| Korea (PIPA) | Under 14 | Legal representative consent |
| India (DPDP) | Under 18 | Verifiable parental consent |
| Thailand (PDPA) | Under 10 for parental consent | Parent/guardian consent |
| Singapore (PDPA) | No specific age (reasonable expectations) | Not specified |
| Japan (APPI) | No specific threshold | General consent rules apply |
| Australia | Under 18 (reform amendments) | Best interests standard; children's code |

## Harmonised Control Framework

### Principle: Highest Common Denominator

The harmonised control framework applies the most stringent requirement from any jurisdiction as the baseline control, ensuring compliance across all operating jurisdictions.

### Harmonised Controls for Zenith Global Enterprises

| Control Area | Harmonised Standard | Driven By |
|-------------|-------------------|-----------|
| Consent | Free, specific, informed, unambiguous, separate per purpose, with easy withdrawal | EU GDPR + China PIPL separate consent |
| Breach notification | 72 hours to authority + individuals simultaneously | EU GDPR / Korea PIPA / India DPDP |
| Children's consent | Parental consent for all processing of under-18 data | India DPDP (18 threshold) |
| DPO appointment | Appoint in all jurisdictions with >500 employees or significant processing | EU GDPR / Thailand PDPA / Brazil LGPD |
| Impact assessment | Conduct for all high-risk processing, cross-border transfers, automated decisions | EU GDPR + China PIPL + Australia (2024) |
| Retention | Delete within 5 days of purpose fulfilment | Korea PIPA (most stringent) |
| Security | AES-256 encryption at rest and TLS 1.3 in transit | Cross-jurisdiction best practice |
| Cross-border transfer | Contractual safeguards + TIA + consent where required | EU GDPR SCCs + China PIPL mechanisms |
| Record-keeping | 7-year retention for consent records, processing records, transfer records | India DPDP (7-year consent manager), extended by statutory requirements |
| Automated decisions | Transparency notice + human review + impact assessment | EU GDPR Art. 22 + Australia 2024 |

## Jurisdiction-Specific Deltas

### Requirements Unique to Specific Jurisdictions

| Delta | Jurisdiction | Requirement | Harmonised Approach |
|-------|-------------|-------------|-------------------|
| Credit protection basis | Brazil | Art. 7, X — lawful basis for credit protection | Document where Brazil-specific basis is relied upon |
| Separate consent (单独同意) | China | Five specific separate consent triggers | Implement separate consent globally where any trigger is met |
| Pre-transfer information | Japan | Provide destination country PI protection system info before consent | Include in all cross-border consent forms globally |
| DNC Registry check | Singapore | Mandatory check before telephone/SMS marketing | Implement DNC checking in Singapore; voluntary in other jurisdictions |
| Data localisation | China (CIIO) | CIIO must store data in PRC | Local storage for PRC data; process copies abroad |
| Resident registration number encryption | Korea | Mandatory encryption for RRN | Encrypt all government identifiers in all jurisdictions |
| Consent Manager | India | Registered intermediary for consent management | Integrate with consent manager in India; optional elsewhere |
| Pseudonymisation framework | Korea / Japan | Statutory pseudonymisation frameworks | Implement pseudonymisation programme meeting both PIPA and APPI standards |

## Gap Identification Process

### Step 1: Map Current Controls
1. Document existing privacy controls, policies, and procedures.
2. Map each control to the requirements of each applicable jurisdiction.
3. Identify controls that satisfy requirements in multiple jurisdictions.

### Step 2: Identify Gaps
1. For each jurisdiction, identify requirements not met by existing controls.
2. Classify gaps as: critical (legal non-compliance), significant (enforcement risk), or minor (best practice deficit).
3. Prioritise gaps based on: regulatory activity in the jurisdiction, potential penalty exposure, data subject volume.

### Step 3: Design Remediation
1. Where possible, design a single harmonised control that addresses the gap across all jurisdictions.
2. Where harmonisation is not possible (conflicting requirements), design jurisdiction-specific controls.
3. Estimate remediation effort and timeline.
4. Assign ownership and track implementation.

## Compliance Matrix Governance

| Element | Detail |
|---------|--------|
| Matrix owner | Chief Privacy Officer, Zenith Global Enterprises |
| Update frequency | Quarterly for law changes; annual comprehensive review |
| Change trigger | New jurisdiction entry, significant law amendment, enforcement action |
| Review committee | Privacy Steering Committee (CPO, regional DPOs, Legal, IT Security) |
| Tool | Compliance matrix maintained in GRC platform with automated law change alerts |
