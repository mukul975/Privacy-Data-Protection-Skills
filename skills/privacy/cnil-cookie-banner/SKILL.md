---
name: cnil-cookie-banner
description: >-
  Designing and implementing CNIL-compliant cookie consent banners for French and
  EU audiences. References the EUR 100M Google LLC fine and EUR 150M Meta Platforms
  fine for non-compliant cookie practices. Covers equal prominence, reject-all buttons,
  cookie walls prohibition, and 6-month reconsent cycles.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cookie-consent-compliance
  tags: "cnil, cookie-banner, french-privacy, google-fine, meta-fine, cookie-wall"
---

# CNIL-Compliant Cookie Banner Implementation

## Overview

The Commission Nationale de l'Informatique et des Libertés (CNIL) enforces some of the strictest cookie consent requirements in the EU. Following its updated guidelines (Deliberation No. 2020-091 of 17 September 2020) and landmark enforcement actions — including the EUR 100 million fine against Google LLC and EUR 50 million against Google Ireland Limited (31 December 2021), and the EUR 60 million fine against Meta Platforms Ireland Limited (31 December 2022, later increased in subsequent actions totaling EUR 150 million across multiple decisions) — organizations serving French users must implement cookie banners meeting specific design and functional requirements.

## CNIL Cookie Banner Requirements

### 1. Equal Prominence for Accept and Reject

The CNIL requires that the mechanism to refuse cookies must be as easy to use as the mechanism to accept them. This was the central issue in the Google and Meta enforcement actions — both companies provided a prominent "Accept All" button but required multiple clicks to reject cookies.

**Compliant Design for Pinnacle E-Commerce Ltd:**

```
+------------------------------------------------------------------+
|  Pinnacle E-Commerce uses cookies                                |
|                                                                  |
|  We use cookies to improve your shopping experience, analyse     |
|  site traffic, and personalise content. You can accept all       |
|  cookies, reject non-essential cookies, or customise your        |
|  choices.                                                        |
|                                                                  |
|  [Accept All]    [Reject All]    [Customise]                     |
|                                                                  |
|  Privacy Policy  |  Cookie Policy                                |
+------------------------------------------------------------------+
```

**Design Rules:**
- "Accept All" and "Reject All" buttons must have identical visual weight: same size, same font, same color scheme, same position hierarchy
- Neither button may use dark patterns (e.g., bright color for accept, grey for reject)
- A "Customise" or "Manage Preferences" option must also be available at the same level
- The banner must not use manipulative language ("Accept for the best experience" vs. neutral "Reject All")

### 2. No Cookie Walls

Under CNIL guidelines, access to the website must not be conditioned on accepting cookies. Cookie walls — where content is blocked until the user accepts all cookies — are prohibited.

**Prohibited Implementation:**
```
+------------------------------------------------------------------+
|  To access Pinnacle E-Commerce, please accept our cookies.       |
|                                                                  |
|  [Accept All Cookies]                                            |
+------------------------------------------------------------------+
```

**Compliant Alternative:**
The site must be fully functional (at minimum, browsable) when the user clicks "Reject All." Essential cookies for cart functionality, authentication, and security may still be set under the strictly necessary exemption.

### 3. Granular Purpose-Level Consent

The customisation layer must allow users to consent to each purpose individually:

**Layer 2 — Customise Preferences:**

```
+------------------------------------------------------------------+
|  Manage your cookie preferences                                  |
|                                                                  |
|  Strictly Necessary          [Always Active]                     |
|  Required for the site to function (cart, security, login).      |
|  These cannot be disabled.                                       |
|                                                                  |
|  Analytics                   [Toggle OFF]                        |
|  Help us understand how visitors use the site to improve our     |
|  services. Data is aggregated and anonymised.                    |
|  Partners: Google Analytics                                      |
|                                                                  |
|  Advertising                 [Toggle OFF]                        |
|  Used to show you relevant advertisements on other websites.     |
|  Partners: Meta, Google Ads                                      |
|                                                                  |
|  Functionality               [Toggle OFF]                        |
|  Remember your preferences such as language and currency.        |
|                                                                  |
|  [Confirm My Choices]    [Accept All]    [Reject All]            |
+------------------------------------------------------------------+
```

**Rules for Layer 2:**
- All non-essential toggles default to OFF (no pre-ticked consent)
- Each category lists specific third-party partners by name
- "Confirm My Choices" saves the current toggle state
- "Accept All" and "Reject All" remain available at this level too

### 4. Consent Validity and Reconsent

CNIL recommends that consent be renewed at regular intervals:

| Parameter | CNIL Requirement |
|-----------|-----------------|
| Maximum consent validity | 6 months (CNIL recommendation) |
| Refusal retention | 6 months before re-prompting |
| Consent proof retention | Duration of consent + applicable statute of limitations |
| Re-prompt after consent expiry | Banner must reappear automatically |
| Re-prompt after cookie policy change | Mandatory — new consent required |

**Implementation for Pinnacle E-Commerce Ltd:**

Store the consent timestamp in a first-party cookie:
```
cookie_consent_timestamp=2026-01-15T10:30:00Z
cookie_consent_version=v2.3
cookie_consent_state=accepted_analytics|rejected_advertising|accepted_functionality
```

On each page load, check:
1. Does `cookie_consent_timestamp` exist?
2. Is it less than 6 months old?
3. Does `cookie_consent_version` match the current cookie policy version?

If any check fails, redisplay the banner.

### 5. No Deceptive Design Patterns

CNIL specifically prohibits the following dark patterns:

| Dark Pattern | Description | Why Prohibited |
|-------------|-------------|----------------|
| Asymmetric buttons | Accept is large/colorful, reject is small/grey | Unequal prominence violates equal ease requirement |
| Hidden reject | Reject option buried in settings layers | Must be at same level as accept |
| Confusing toggles | Toggle visually suggests ON when it is OFF | Undermines informed consent |
| Guilt-tripping | "By rejecting, you'll miss personalised offers" | Manipulative language |
| Pre-selected purposes | Analytics or functionality toggles pre-enabled | Violates active consent requirement (Planet49) |
| Repeated prompting | Re-showing banner on every page after rejection | Coercion; must respect refusal for 6 months |

## Technical Implementation

### Banner Loading Behavior

1. **No cookies before consent**: Non-essential cookies must not be set before the user interacts with the banner. Tags must be blocked at the container level.
2. **Synchronous banner load**: The consent banner must load before any tag management scripts execute.
3. **Server-side enforcement**: Consent state should be validated server-side for requests that trigger cookie setting.

### Tag Blocking Architecture

```
Page Load
    │
    ├── Load consent banner script (synchronous)
    │
    ├── Check consent state cookie
    │   ├── No consent recorded → Show banner, block all non-essential tags
    │   ├── Consent expired (>6 months) → Show banner, block all non-essential tags
    │   ├── Consent recorded → Parse consent state
    │       ├── Analytics accepted → Fire GA4 tags
    │       ├── Advertising accepted → Fire Meta Pixel, Google Ads tags
    │       └── Functionality accepted → Fire preference cookies
    │
    └── User interacts with banner
        ├── Accept All → Set all tags, store consent
        ├── Reject All → Block all non-essential tags, store refusal
        └── Customise → Show Layer 2, await per-purpose selection
```

### Consent Storage

Store consent proof with the following minimum fields:

| Field | Value |
|-------|-------|
| Consent ID | UUID per consent event |
| User identifier | Pseudonymised user ID or cookie ID |
| Timestamp | ISO 8601 UTC |
| Banner version | Hash of banner text/design |
| Cookie policy version | Version identifier (e.g., v2.3) |
| Decisions | Per-purpose accept/reject |
| Collection mechanism | "cookie_banner_layer_1" or "cookie_banner_layer_2" |
| IP address | For geolocation verification (retained separately, access-restricted) |

### Accessibility Requirements

The cookie banner must meet WCAG 2.1 Level AA:
- Keyboard navigable (Tab, Enter, Escape)
- Screen reader compatible (ARIA roles, labels)
- Sufficient color contrast (4.5:1 ratio minimum)
- Focus trap within banner until interaction (preventing interaction with page behind)
- Banner text at minimum 14px font size

## CNIL Enforcement Precedents

| Date | Organization | Fine | Key Violation |
|------|-------------|------|--------------|
| 31 Dec 2021 | Google LLC | EUR 100,000,000 | No equivalent reject mechanism; cookies set before consent |
| 31 Dec 2021 | Google Ireland | EUR 50,000,000 | Same violations as Google LLC |
| 29 Dec 2022 | TikTok | EUR 5,000,000 | No equivalent reject mechanism |
| 31 Dec 2022 | Meta Platforms Ireland | EUR 60,000,000 | No equivalent reject mechanism |
| 15 Jun 2023 | Criteo | EUR 40,000,000 | Consent not freely given; insufficient information |
| 28 Dec 2023 | Amazon France | EUR 32,000,000 | Cookie deposits without consent |

## Key Legal References

- **CNIL Deliberation No. 2020-091 (17 September 2020)** — Guidelines on cookies and other trackers
- **CNIL Recommendation on cookies (1 October 2020)** — Practical modalities for consent collection
- **ePrivacy Directive 2002/58/EC, Article 5(3)** — Consent for storing/accessing information on devices
- **CJEU Case C-673/17 (Planet49)** — Active consent, no pre-ticked boxes
- **GDPR Article 7** — Conditions for consent, including withdrawal
- **CNIL Decision SAN-2021-023 (Google)** — EUR 150M total fine for cookie consent violations
- **CNIL Decision SAN-2022-021 (Meta)** — EUR 60M fine for cookie consent violations
