---
name: cnil-compliant-cookies
description: >-
  Implementation guide for CNIL cookie guidelines compliance. References the EUR 150M
  Google fine and EUR 60M Meta fine. Covers equal prominence accept/reject buttons,
  cookie wall prohibition, 6-month reconsent intervals, essential cookies exemption,
  and detailed CNIL Deliberation No. 2020-091 requirements.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: consent-management
  tags: "cnil-cookies, cookie-compliance, french-cookie-law, accept-reject-equal, cookie-wall"
---

# Implementing CNIL-Compliant Cookies

## Overview

The French Commission Nationale de l'Informatique et des Libertés (CNIL) has been the most aggressive European enforcer of cookie consent rules. In January 2022, CNIL issued a EUR 150 million fine to Google LLC and a EUR 60 million fine to Meta Platforms Ireland Ltd. for cookie consent violations. These enforcement actions, combined with CNIL Deliberation No. 2020-091 (September 17, 2020), establish the most detailed cookie consent standards in Europe.

## CNIL Cookie Consent Requirements

### 1. Equal Prominence of Accept and Reject (CNIL Deliberation 2020-091, Section 2.1)

**Requirement:** Users must be able to refuse cookies as easily as accepting them. The "Refuse All" option must be presented with the same visual prominence as the "Accept All" option.

**Specific CNIL Requirements:**
- "Accept All" and "Refuse All" buttons must be on the same hierarchical level (same layer of the interface)
- Both buttons must have comparable visual treatment (size, color, font, position)
- Neither button may be visually promoted or demoted relative to the other
- A "Manage Preferences" option may be offered as a third option but must not replace "Refuse All"

**CloudVault SaaS Inc. Implementation:**
```
┌─────────────────────────────────────────────────────────────┐
│  CloudVault uses cookies to improve your experience.        │
│  [Learn more about our cookie use]                          │
│                                                             │
│  ┌──────────────────┐  ┌──────────────────┐                │
│  │  Accept All       │  │  Refuse All       │               │
│  └──────────────────┘  └──────────────────┘                │
│                                                             │
│  [Manage Preferences]                                       │
└─────────────────────────────────────────────────────────────┘

Button specifications:
- Both: 200x44px, #2563EB blue background, white text, 16px bold
- Position: side by side, same vertical level
- "Manage Preferences": text link below, #6B7280 grey, 14px regular
```

### 2. No Cookie Walls (CNIL Deliberation 2020-091, Section 2.2)

**Requirement:** Access to the website or service must not be conditioned on accepting cookies. Users who refuse all cookies must be able to access the same content and functionality.

**Exceptions:**
- The CNIL acknowledges that some functionality (e.g., personalized recommendations) may require cookies. In that case, a degraded but functional experience must be available.
- Paywall vs cookie wall: CNIL has indicated (Deliberation No. 2022-003) that offering a paid cookie-free alternative alongside a free cookie-funded option may be permissible under certain conditions (the "pay or consent" model), though this remains contested.

### 3. Six-Month Reconsent Interval (CNIL Deliberation 2020-091, Section 2.3)

**Requirement:** Consent must be renewed at appropriate intervals. CNIL recommends a maximum of 6 months between consent requests.

**Implementation:**
- Set a first-party cookie `cv_consent_timestamp` with the consent date
- After 180 days, re-display the consent banner
- If the user has previously refused, re-ask (they may have changed their mind)
- If the user has previously accepted, re-ask (they should confirm continued consent)

### 4. Essential Cookies Exemption (CNIL Deliberation 2020-091, Section 3)

The following categories do not require consent per CNIL guidance:

| Category | Examples | Justification |
|----------|----------|---------------|
| Authentication | Session cookies, CSRF tokens | Strictly necessary for security |
| Load balancing | Server routing cookies | Strictly necessary for service |
| User preferences | Language, display settings | Strictly necessary for requested functionality |
| Shopping cart | Cart session cookies | Strictly necessary for requested service |
| First-party analytics (limited) | Audience measurement with limited scope | CNIL exemption for first-party, aggregate-only analytics (strict conditions) |

**CNIL conditions for first-party analytics exemption:**
- Data used only for aggregate statistical analysis
- Data not cross-referenced with other processing
- Cookies limited to single site
- IP addresses anonymized or truncated
- Cookie lifetime limited to 13 months, data retention limited to 25 months
- User informed of the use and right to object
- Must not enable individual tracking across sites

### 5. Comprehensive Information (CNIL Deliberation 2020-091, Section 2.4)

Before consenting, the user must be informed of:
- The identity of all organizations using cookies (controllers and third parties)
- The specific purposes of each category of cookies
- The consequences of accepting or refusing
- How to withdraw consent
- Cookie retention periods

## CNIL Enforcement Reference

| Entity | Fine | Date | Deliberation | Key Violations |
|--------|------|------|-------------|----------------|
| Google LLC | EUR 150,000,000 | Jan 6, 2022 | 2022-013 | No "Refuse All" on first layer; multiple clicks to refuse |
| Meta Platforms | EUR 60,000,000 | Jan 6, 2022 | 2022-014 | "Accept" on first layer, "Refuse" buried in secondary page |
| Microsoft Ireland | EUR 60,000,000 | Dec 22, 2022 | 2022-023 | bing.com: "Accept" without equally prominent "Refuse" |
| TikTok | EUR 5,000,000 | Dec 29, 2022 | 2022-025 | Rejecting more complex than accepting; info inadequate |
| Voodoo (mobile games) | EUR 3,000,000 | Jan 2023 | 2023-004 | Used Apple IDFA for advertising without consent |
| Apple Distribution | EUR 8,000,000 | Jan 4, 2023 | 2023-001 | Targeted advertising on App Store without valid consent |

## Implementation Checklist

| # | Requirement | CNIL Reference | CloudVault Status |
|---|-----------|---------------|------------------|
| 1 | "Refuse All" button on first layer | Deliberation 2020-091 Section 2.1 | Implemented |
| 2 | Equal visual prominence accept/refuse | Deliberation 2020-091 Section 2.1 | Both 200x44px, same color |
| 3 | No cookie wall | Deliberation 2020-091 Section 2.2 | Full access without cookies |
| 4 | Reconsent every 6 months maximum | Deliberation 2020-091 Section 2.3 | 180-day reconsent cycle |
| 5 | Essential cookies documented and exempted | Deliberation 2020-091 Section 3 | 4 essential cookies listed |
| 6 | Third parties identified by name | Deliberation 2020-091 Section 2.4 | All third parties named |
| 7 | Cookie purposes described | Deliberation 2020-091 Section 2.4 | Per-category descriptions |
| 8 | Cookie retention periods stated | Deliberation 2020-091 Section 2.4 | Max 13 months per CNIL |
| 9 | Withdrawal as easy as giving consent | GDPR Art. 7(3) | Footer link on every page |
| 10 | Consent records maintained | GDPR Art. 7(1) | Full audit trail |

## Key Regulatory References

- CNIL Deliberation No. 2020-091 (September 17, 2020) — Cookie guidelines
- CNIL Deliberation No. 2022-013 — Google fine (EUR 150M)
- CNIL Deliberation No. 2022-014 — Meta fine (EUR 60M)
- CNIL Deliberation No. 2022-023 — Microsoft fine (EUR 60M)
- ePrivacy Directive Article 5(3) — Consent for device storage
- GDPR Article 7 — Conditions for consent
- EDPB Guidelines 05/2020 — Consent under Regulation 2016/679
