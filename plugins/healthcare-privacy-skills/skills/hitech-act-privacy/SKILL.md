---
name: hitech-act-privacy
description: >-
  Implements HITECH Act privacy and security requirements including breach
  notification expansion, four-tier penalty structure, state attorney general
  enforcement authority, EHR meaningful use privacy conditions, and business
  associate direct liability. Keywords: HITECH Act, breach notification,
  penalty tiers, state AG enforcement, meaningful use, EHR privacy.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: healthcare-privacy
  tags: "hitech-act, breach-notification, penalty-tiers, state-ag-enforcement, meaningful-use, ehr-privacy"
---

# HITECH Act Privacy and Security Requirements

## Overview

The Health Information Technology for Economic and Clinical Health (HITECH) Act was enacted as Title XIII of the American Recovery and Reinvestment Act of 2009 (Pub. L. 111-5). HITECH fundamentally transformed HIPAA enforcement by establishing breach notification requirements, creating a four-tier penalty structure with significantly increased penalties, granting enforcement authority to state attorneys general, extending HIPAA Security Rule requirements directly to business associates, and tying privacy and security compliance to the Electronic Health Record (EHR) meaningful use incentive program. The 2013 Omnibus Rule (78 FR 5566) implemented most HITECH provisions into the HIPAA regulatory framework.

## Breach Notification — HITECH §13402

### Establishment of Federal Healthcare Breach Notification

Prior to HITECH, HIPAA had no breach notification requirement. HITECH §13402 created the obligation for covered entities and business associates to notify individuals, HHS, and in some cases the media, following a breach of unsecured PHI.

**Key provisions enacted by HITECH**:

| Provision | HITECH Section | Implementation |
|-----------|---------------|----------------|
| Individual notification within 60 days | §13402(a) | Codified at 45 CFR §164.404 |
| HHS notification for breaches of 500+ immediately; under 500 annually | §13402(e)(1)-(3) | Codified at 45 CFR §164.408 |
| Media notification for 500+ in a state/jurisdiction | §13402(e)(2) | Codified at 45 CFR §164.406 |
| State AG notification for 500+ in a state | §13402(e)(3) | 45 CFR §164.408(c) |
| BA obligation to notify CE | §13402(b) | Codified at 45 CFR §164.410 |
| Unsecured PHI definition and safe harbor for encryption/destruction | §13402(h) | HHS guidance at 74 FR 19006 |

### Evolution of the Breach Standard

HITECH originally used a "harm standard" — notification was required only if there was a significant risk of financial, reputational, or other harm. The 2013 Omnibus Rule replaced this with the "low probability of compromise" standard under the four-factor risk assessment (§164.402(2)), which is more protective of individuals. Under this standard, an impermissible use or disclosure is presumed to be a breach unless the entity demonstrates low probability of compromise.

## Penalty Structure — HITECH §13410

### Four-Tier Civil Monetary Penalty Framework

HITECH §13410(d) replaced the single-tier HIPAA penalty structure with a graduated system based on culpability:

| Tier | Culpability Level | Per Violation (2024 adjusted) | Annual Cap (2024 adjusted) | Correction Possible |
|------|------------------|-------------------------------|---------------------------|-------------------|
| A | Did not know and would not have known by exercising reasonable diligence | $137 – $68,928 | $2,067,813 | Must correct within 30 days |
| B | Reasonable cause (not willful neglect) | $1,379 – $68,928 | $2,067,813 | Must correct within 30 days |
| C | Willful neglect — timely corrected | $13,785 – $68,928 | $2,067,813 | Corrected within 30 days of knowledge |
| D | Willful neglect — not timely corrected | $68,928 – $2,067,813 | $2,067,813 | Investigation/penalty mandatory |

Penalty amounts are adjusted annually for inflation under the Federal Civil Penalties Inflation Adjustment Act Improvements Act of 2015.

### Criminal Penalties

HITECH preserved and enhanced criminal penalties under 42 USC §1320d-6:

| Tier | Conduct | Maximum Penalty |
|------|---------|----------------|
| 1 | Knowingly obtaining or disclosing PHI | Up to $50,000 fine and 1 year imprisonment |
| 2 | Offenses committed under false pretenses | Up to $100,000 fine and 5 years imprisonment |
| 3 | Offenses with intent to sell, transfer, or use for commercial advantage, personal gain, or malicious harm | Up to $250,000 fine and 10 years imprisonment |

### Percentage of CMPs and Settlements to Affected Individuals — §13410(c)(2)

HITECH §13410(c)(2) directed HHS to establish methods for distributing a percentage of CMPs and settlement amounts to individuals harmed by HIPAA violations. HHS has not yet issued final regulations implementing this provision, but OCR has included equitable relief provisions in certain settlement agreements.

## State Attorney General Enforcement — HITECH §13410(e)

### Authority Granted

HITECH §13410(e) authorized state attorneys general to bring civil actions in federal district court on behalf of state residents who may have been affected by HIPAA violations. This was a significant expansion — previously only HHS/OCR could enforce HIPAA.

### Requirements for State AG Actions

| Requirement | Detail |
|-------------|--------|
| Prior notice to HHS | State AG must provide notice to the Secretary of HHS before filing suit |
| HHS intervention right | HHS may intervene and assume primary responsibility for the action |
| No action during pending HHS action | State AG may not bring action during a pending HHS action against the same entity for the same violation |
| Remedies available | Injunctive relief, damages (up to $100 per violation, $25,000 per calendar year per identical violation), attorneys' fees |

### State AG Enforcement Precedents

| State | Year | Entity | Outcome |
|-------|------|--------|---------|
| Connecticut | 2010 | Health Net of Connecticut | $250,000 settlement — first state AG action under HITECH; loss of unencrypted hard drive with PHI of 1.5 million individuals |
| Minnesota | 2011 | Accretive Health | $2.5 million settlement — unauthorized access to PHI; failure to have BAA |
| Indiana | 2014 | WellPoint (Anthem) | $1.9 million penalty — application vulnerability exposing ePHI of 612,402 individuals; state AG used HITECH authority alongside state law |
| New York | 2021 | EyeMed Vision Care | $600,000 settlement — email phishing breach exposing PHI of 2.1 million; state AG cited HITECH and state consumer protection |
| New Jersey | 2019 | Virtua Medical Group | $418,000 settlement — disclosure of PHI to vendor without BAA |

## Business Associate Direct Liability — HITECH §13401

### Pre-HITECH vs Post-HITECH

| Aspect | Pre-HITECH | Post-HITECH (§13401) |
|--------|-----------|---------------------|
| Security Rule compliance | Contractual obligation through BAA only; no direct regulatory liability | BAs directly subject to Security Rule; enforceable by OCR and state AGs |
| Privacy Rule | BAs bound only by BAA terms | BAs directly liable for impermissible uses/disclosures; subject to minimum necessary |
| Penalties | Only covered entities subject to HIPAA penalties; BAs subject only to breach of contract | BAs subject to same civil and criminal penalties as covered entities |
| Subcontractors | No regulatory requirements | Subcontractors treated as BAs; must have BAAs in place |

### Impact on Asclepius Health Network

Asclepius Health Network manages 47 business associate relationships. Post-HITECH, each BA must:
- Independently comply with all Security Rule administrative, physical, and technical safeguards
- Report breaches to Asclepius within 5 business days per the BAA
- Demonstrate compliance through annual security assessments
- Flow down BAA requirements to their subcontractors

## EHR Meaningful Use Privacy Conditions — HITECH §13401(b)

### Privacy and Security as Prerequisites for Incentive Payments

HITECH created the Medicare and Medicaid EHR Incentive Programs (now known as Promoting Interoperability) with total payments exceeding $38 billion. Privacy and security compliance is a prerequisite for receiving incentive payments:

| Meaningful Use Stage | Privacy/Security Requirements |
|---------------------|------------------------------|
| Stage 1 (2011-2013) | Conduct or review a security risk analysis; implement security updates; correct identified security deficiencies |
| Stage 2 (2014-2016) | All Stage 1 requirements plus: address encryption/security of data at rest; enable patient electronic access to health information |
| Stage 3 / Promoting Interoperability (2017+) | Security risk analysis; patient electronic access; secure messaging; API access; ONC Health IT Certification privacy and security criteria |

### Privacy Requirements in Health IT Certification

ONC Health IT Certification Criteria (45 CFR Part 170) require certified EHR technology to support:

- Authentication, access control, and authorization
- Auditable events and tamper-resistance
- Automatic access time-out
- Emergency access
- End-user device encryption
- Integrity verification
- Accounting of disclosures
- Amendments to health information
- Consent management (including segmentation for Part 2 and state-specific restrictions)

**Asclepius Health Network** uses ONC-certified Epic EHR and verifies that each software version maintains certification for privacy and security criteria. The Promoting Interoperability dashboard tracks privacy measure compliance for CMS attestation.

## Accounting of Disclosures Expansion — HITECH §13405(c)

### HITECH Expansion

HITECH §13405(c) expanded the right to an accounting of disclosures to include disclosures through an electronic health record for treatment, payment, and healthcare operations (previously excluded under HIPAA §164.528). The accounting period was set at 3 years (rather than HIPAA's 6 years) for EHR disclosures.

**Status**: HHS published a Notice of Proposed Rulemaking in 2011 (76 FR 31426) proposing an "access report" approach but withdrew the NPRM and has not issued a final rule. The HITECH provision is self-executing in the statute but implementation guidance remains pending.

## Restrictions on Sale of PHI — HITECH §13405(d)

HITECH §13405(d) prohibits a covered entity or business associate from receiving direct or indirect remuneration in exchange for PHI without a valid authorization from the individual that states whether the PHI can be further exchanged for remuneration.

### Exceptions

| Exception | Description |
|-----------|-------------|
| Public health | Disclosures for public health activities under §164.512(b) |
| Research | Reasonable cost-based fee for preparing and transmitting PHI for research |
| Treatment and payment | Normal treatment and payment activities |
| Transfer of business | Sale, transfer, merger of covered entity |
| BA services | Remuneration is for services BA provides on behalf of CE |
| Individual request | Individual requests own PHI |
| HHS-determined exceptions | Other purposes determined by HHS through regulation |

## Minimum Necessary Enhancement — HITECH §13405(b)

HITECH directed HHS to issue guidance making the minimum necessary standard more specific:

- Until HHS issues guidance, the limited dataset standard (§164.514(e)) is the floor for minimum necessary when PHI is in electronic form and a limited dataset would accomplish the purpose
- HHS has not issued the final rule, but the provision is self-executing to the extent described

## Enforcement Milestones Under HITECH

| Year | Action | Significance |
|------|--------|-------------|
| 2009 | HITECH enacted | Four-tier penalties, breach notification, BA liability, state AG enforcement |
| 2010 | Interim Final Breach Notification Rule | Initial implementation of breach notification with harm standard |
| 2011 | First resolution agreement post-HITECH (Cignet Health, $4.3M) | Demonstrated willingness to impose significant penalties |
| 2013 | Omnibus Rule | Comprehensive implementation of HITECH provisions into HIPAA regulations |
| 2016 | Advocate Medical Group ($5.55M) | Largest fine at the time; multiple breaches involving unencrypted devices |
| 2018 | Anthem ($16M) | Largest HIPAA settlement; demonstrated HITECH penalty levels for major breaches |
| 2020-2024 | Annual penalty adjustments | Inflation-adjusted penalties increasing annually |

## Integration Points

- **hipaa-breach-notify**: HITECH created the breach notification framework implemented in the Breach Notification Rule
- **hipaa-privacy-rule**: HITECH strengthened Privacy Rule provisions including restrictions on sale of PHI and minimum necessary
- **hipaa-security-rule**: HITECH extended Security Rule directly to business associates
- **hipaa-baa-management**: HITECH created BA direct liability and subcontractor requirements
- **hipaa-risk-analysis**: Risk analysis is a prerequisite for EHR meaningful use/Promoting Interoperability attestation
