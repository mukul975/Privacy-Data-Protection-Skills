# AI Training Data Lawfulness Assessment Template

## Organisation: Cerebrum AI Labs

---

## SECTION 1: ASSESSMENT OVERVIEW

| Field | Value |
|-------|-------|
| Assessment Reference | AITL-2026-___ |
| AI System / Model Name | |
| Assessment Lead | |
| Legal Counsel Reviewer | |
| DPO Reviewer | |
| Date | |
| Version | 1.0 |

---

## SECTION 2: TRAINING DATA SOURCE INVENTORY

### Source 1: _________________

| Element | Value |
|---------|-------|
| Source Name | |
| Source Type | First-party / Third-party / Public / Open-source / Web-scraped / User-contributed |
| Description | |
| Data Categories | |
| Record Count | |
| Contains PII? | Yes / No |
| Contains Art. 9 Special Category Data? | Yes / No — Types: |
| Original Collection Purpose | |
| AI Training Disclosed at Collection? | Yes / No |
| Geographic Scope | |
| Data Provider (if third-party) | |

(Repeat for each source)

---

## SECTION 3: LAWFUL BASIS ASSESSMENT PER SOURCE

### Source: _________________

#### 3.1 Selected Lawful Basis

| | |
|---|---|
| Lawful Basis | Art. 6(1)(a) Consent / (b) Contract / (c) Legal Obligation / (e) Public Interest / (f) Legitimate Interest |
| Justification | |

#### 3.2 Consent Assessment (if Art. 6(1)(a))

| Requirement | Met? | Evidence |
|-------------|------|----------|
| Consent specifically covers AI training | Yes / No | |
| Consent is freely given (not bundled) | Yes / No | |
| Consent is informed (AI training explained) | Yes / No | |
| Consent is specific (not generic) | Yes / No | |
| Consent is unambiguous (affirmative opt-in) | Yes / No | |
| Withdrawal mechanism available | Yes / No | |
| Withdrawal process for trained models documented | Yes / No | |

#### 3.3 Contract Necessity Assessment (if Art. 6(1)(b))

| Question | Response |
|----------|----------|
| Is AI training necessary for the contracted service? | Yes / No |
| Is the training for a personalised model serving this data subject? | Yes / No |
| Could the service be delivered without AI training? | Yes / No |
| EDPB position: general model improvement is not contract necessity | Acknowledged |

#### 3.4 Legitimate Interest Balancing Test (if Art. 6(1)(f))

**Part 1: Interest Identification**

| Element | Assessment |
|---------|------------|
| Specific interest pursued | |
| Is the interest lawful? | Yes / No |
| Is the interest real and present? | Yes / No |
| Is the interest sufficiently specific? | Yes / No |
| Beneficiaries | Controller / Third parties / Data subjects / Society |

**Part 2: Necessity**

| Question | Response | Evidence |
|----------|----------|----------|
| Is personal data required for the interest? | Yes / No | |
| Has anonymised data been tested? | Yes / No | Performance result: |
| Has synthetic data been evaluated? | Yes / No | |
| Has federated learning been assessed? | Yes / No | |
| Has minimum dataset been determined? | Yes / No | Minimum: ___ records |
| Are all data categories necessary? | Yes / No | |

**Part 3: Balancing**

| Factor | Assessment | Weight |
|--------|------------|--------|
| Data subject impact | Low / Medium / High | |
| Reasonable expectations met? | Met / Partially / Not met | |
| Special category data involved? | Yes / No | |
| Vulnerable data subjects? | Yes / No | |
| Safeguards level | Comprehensive / Adequate / Insufficient | |
| Opt-out mechanism available? | Yes / No | |
| Transparency provided? | Yes / No | |
| Web-scraped data? (heightened scrutiny) | Yes / No | |

**Balancing Outcome**: Controller overrides / Data subject overrides / Marginal

**Justification**: _______________

#### 3.5 Art. 9 Special Category Assessment (if applicable)

| Element | Assessment |
|---------|------------|
| Special category types present | |
| Art. 9(2) condition relied upon | (a) Explicit consent / (g) Substantial public interest / (j) Research / Other: |
| Condition documented? | Yes / No |
| Suitable safeguards in place? | Yes / No |

#### 3.6 Purpose Compatibility Assessment (Art. 6(4))

| Factor | Assessment |
|--------|------------|
| Link between original purpose and AI training | Strong / Moderate / Weak |
| Context of original collection | |
| Nature of the data | |
| Consequences of AI training for data subjects | |
| Safeguards in place | |
| Compatible? | Yes / No |

---

## SECTION 4: WEB SCRAPING SPECIFIC ASSESSMENT

Complete only for web-scraped data sources.

| Factor | Assessment |
|--------|------------|
| Personal data present in scraped data? | Yes / No |
| PII detection and removal applied? | Yes / No |
| Robots.txt respected? | Yes / No |
| Website ToS prohibits scraping? | Yes / No |
| Data subjects aware of scraping? | Yes / No |
| Privacy settings respected? | Yes / No |
| Children's data likely present? | Yes / No |
| Opt-out mechanism available? | Yes / No |
| Differential privacy applied? | Yes / No |
| EDPB heightened scrutiny documented? | Yes / No |

---

## SECTION 5: THIRD-PARTY DATA CHAIN VERIFICATION

Complete for each third-party data source.

| Element | Assessment |
|---------|------------|
| Data provider name | |
| Provider's documented lawful basis | |
| Due diligence conducted on provider? | Yes / No |
| Contractual warranties obtained? | Yes / No |
| Licence explicitly permits AI training? | Yes / No |
| Provider consent scope covers AI training? | Yes / No / Unknown |
| Provider audit right included in agreement? | Yes / No |

---

## SECTION 6: SAFEGUARDS INVENTORY

| Safeguard | Applied? | Details |
|-----------|----------|---------|
| PII detection and removal pre-training | Yes / No | Tool: |
| Pseudonymisation of training data | Yes / No | Method: |
| Differential privacy during training | Yes / No | Epsilon: |
| Training data access controls | Yes / No | |
| Training data encryption (rest/transit) | Yes / No | |
| Opt-out mechanism for data subjects | Yes / No | URL/contact: |
| Privacy notice updated for AI training | Yes / No | |
| Training data audit trail | Yes / No | |
| Regular lawful basis review scheduled | Yes / No | Frequency: |

---

## SECTION 7: OVERALL ASSESSMENT

| Element | Value |
|---------|-------|
| Total data sources assessed | |
| Sources with valid lawful basis | |
| Sources requiring remediation | |
| Sources to exclude from training | |
| Overall compliance status | Compliant / Conditionally Compliant / Non-Compliant |

### Action Items

| # | Action | Owner | Deadline | Status |
|---|--------|-------|----------|--------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

## SECTION 8: APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Assessment Lead | | | |
| Legal Counsel | | | |
| Data Protection Officer | | | |

### Review Schedule

Next review: [12 months from approval or when training purpose/scope changes]
