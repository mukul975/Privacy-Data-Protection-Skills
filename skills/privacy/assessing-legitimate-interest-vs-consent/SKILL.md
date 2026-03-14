---
name: assessing-legitimate-interest-vs-consent
description: >-
  Decision framework for choosing between consent and legitimate interest as the
  lawful basis for processing. Covers power imbalance indicators, conditionality
  prohibition under Article 7(4), granularity requirements, the three-part LIA test
  (purpose, necessity, balancing), and practical decision trees for common scenarios.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: consent-management
  tags: "legitimate-interest, consent-vs-lia, lawful-basis, power-imbalance, article-6"
---

# Assessing Legitimate Interest vs Consent

## Overview

GDPR Article 6(1) provides six lawful bases for processing. Consent (Article 6(1)(a)) and legitimate interest (Article 6(1)(f)) are the two most commonly used bases for commercial data processing. Choosing the wrong basis creates compliance risk: relying on consent when it cannot be freely given undermines validity, while relying on legitimate interest when consent is required (e.g., for electronic marketing under the ePrivacy Directive) violates sectoral law.

## Decision Framework: When to Use Each Basis

### Use Consent When:

1. **Regulatory requirement**: Specific legislation mandates consent (e.g., ePrivacy Directive Article 5(3) for non-essential cookies, Article 13 for unsolicited electronic marketing)
2. **Special category data**: Processing sensitive data under Article 9(2)(a) requires explicit consent
3. **Automated decision-making**: Processing under Article 22(2)(c) requires explicit consent
4. **International transfers**: Article 49(1)(a) explicit consent for transfers without adequacy/safeguards
5. **User control priority**: The processing is entirely optional and the data subject should have full control

### Use Legitimate Interest When:

1. **Power imbalance exists**: Consent cannot be freely given (employer-employee, public authority-citizen)
2. **Processing is necessary**: The processing is necessary for the controller's or third party's legitimate interest and is proportionate
3. **Reasonable expectation**: The data subject would reasonably expect the processing (Recital 47)
4. **Withdrawal would be problematic**: If consent withdrawal would cause operational issues (e.g., fraud prevention)
5. **No specific consent requirement**: No ePrivacy or sectoral law mandates consent

## Power Imbalance Indicators

Per EDPB Guidelines 05/2020 (paragraphs 13-25) and Recital 43, consent is presumed not to be freely given when a clear imbalance exists:

| Indicator | Example | Implication |
|-----------|---------|-------------|
| Employment relationship | Employer asks employee to consent to monitoring | Use LI or legal obligation, not consent |
| Public authority | Tax authority processes taxpayer data | Use legal obligation or public task |
| Service dependency | Only provider in market; user has no alternative | Consent may not be freely given |
| Contractual bundling | Consent required as condition of contract (Art. 7(4)) | Consent likely invalid |
| Vulnerable data subjects | Children, elderly, patients | Extra scrutiny; consent may not be free |
| Significant consequence | Refusing consent leads to job loss or service termination | Consent not freely given |

## The Three-Part Legitimate Interest Assessment (LIA)

Per CJEU case law (C-13/16 Rigas, C-40/17 Fashion ID) and Article 29 Working Party Opinion 06/2014:

### Part 1: Purpose Test

Is the interest legitimate?

- The interest must be lawful (not in itself illegal)
- The interest must be real and present (not speculative)
- The interest must be sufficiently clearly articulated

**CloudVault SaaS Inc. examples of legitimate interests:**
- Network and information security (Recital 49)
- Fraud prevention and detection
- Direct marketing to existing customers (Recital 47)
- Internal administrative purposes within a group (Recital 48)
- Service improvement based on aggregated usage analytics

### Part 2: Necessity Test

Is the processing necessary for the legitimate interest?

- Could the same interest be achieved with less data?
- Could the same interest be achieved without processing personal data?
- Is the processing proportionate to the interest pursued?

### Part 3: Balancing Test

Do the data subject's rights and freedoms override the legitimate interest?

| Factor | Weighs Toward LI | Weighs Toward Data Subject |
|--------|------------------|---------------------------|
| Data sensitivity | Non-sensitive data | Special category data |
| Reasonable expectation | Processing expected by data subject | Surprising or unexpected processing |
| Relationship | Existing customer/user relationship | No prior relationship |
| Impact | Minimal impact on individual | Significant consequences |
| Safeguards | Robust safeguards in place | No safeguards |
| Data subject control | Easy opt-out available | No opt-out mechanism |
| Vulnerable groups | No vulnerable individuals | Children or vulnerable adults |
| Data volume | Minimal data used | Extensive profiling |

## Decision Tree

```
START: Need to establish lawful basis for processing activity
  │
  ├─► Q1: Does specific legislation require consent?
  │     (ePrivacy Art. 5(3) for cookies, Art. 13 for e-marketing,
  │      GDPR Art. 9(2)(a) for special categories, Art. 22(2)(c) for automated decisions)
  │     │
  │     ├─ YES → Use CONSENT (mandatory)
  │     │
  │     └─ NO → Continue to Q2
  │
  ├─► Q2: Is there a power imbalance between controller and data subject?
  │     (employer-employee, public authority, service dependency)
  │     │
  │     ├─ YES → Consent likely INVALID; consider LEGITIMATE INTEREST
  │     │         (or legal obligation/public task if applicable)
  │     │
  │     └─ NO → Continue to Q3
  │
  ├─► Q3: Is consent conditioned on the service?
  │     (Would refusing consent result in service denial or degradation?)
  │     │
  │     ├─ YES → Violates Art. 7(4); consent likely INVALID
  │     │         Consider LEGITIMATE INTEREST or restructure the service
  │     │
  │     └─ NO → Continue to Q4
  │
  ├─► Q4: Is consent withdrawal operationally feasible?
  │     (Can you stop processing immediately if consent is withdrawn?)
  │     │
  │     ├─ NO → LEGITIMATE INTEREST may be more appropriate
  │     │        (e.g., fraud prevention cannot stop mid-transaction)
  │     │
  │     └─ YES → Continue to Q5
  │
  ├─► Q5: Does the data subject reasonably expect this processing?
  │     │
  │     ├─ YES → Either CONSENT or LEGITIMATE INTEREST may work
  │     │         Choose based on control preference and overhead
  │     │
  │     └─ NO → CONSENT is more appropriate
  │               (unexpected processing needs explicit agreement)
  │
  └─► Q6: Final determination
        ├─ If consent: Implement full Art. 7 requirements (freely given, specific,
        │   informed, unambiguous, withdrawal as easy as giving)
        └─ If LI: Document three-part LIA, implement opt-out mechanism,
            include in privacy notice per Art. 13(1)(d)/14(2)(b)
```

## Common Scenarios at CloudVault SaaS Inc.

| Scenario | Recommended Basis | Reasoning |
|----------|------------------|-----------|
| Essential cookies for session management | Not consent; exempt under ePrivacy Art. 5(3) | Strictly necessary; no consent required |
| Analytics cookies (non-essential) | Consent | ePrivacy Art. 5(3) requires consent for non-essential cookies |
| Email marketing to existing customers | Legitimate interest (soft opt-in) | ePrivacy Art. 13(2) allows soft opt-in for existing customers with opt-out |
| Email marketing to new contacts | Consent | ePrivacy Art. 13(1) requires prior consent for unsolicited e-marketing |
| Fraud detection on transactions | Legitimate interest | Cannot withdraw; Recital 47 recognizes fraud prevention |
| Sharing data with Datalytics Partners Ltd. | Consent | Third-party sharing not reasonably expected; user control appropriate |
| Network security monitoring | Legitimate interest | Recital 49 explicitly recognizes network security as LI |
| Employee performance monitoring | Legitimate interest | Power imbalance makes employee consent invalid (WP29 Opinion 2/2017) |

## Key Regulatory References

- GDPR Article 6(1)(a) — Consent as lawful basis
- GDPR Article 6(1)(f) — Legitimate interest as lawful basis
- GDPR Article 7(4) — Conditionality prohibition
- GDPR Recitals 47, 48, 49 — Guidance on legitimate interest scenarios
- Article 29 WP Opinion 06/2014 on Legitimate Interest (WP217)
- EDPB Guidelines 05/2020 on Consent — Power imbalance analysis
- CJEU C-13/16 (Rigas) — Legitimate interest balancing test
- CJEU C-40/17 (Fashion ID) — Joint controller LI responsibility
- ePrivacy Directive Articles 5(3) and 13 — Sector-specific consent requirements
- WP29 Opinion 2/2017 on Data Processing at Work — Employee consent limitations
