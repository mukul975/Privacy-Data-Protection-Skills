---
name: implementing-cnil-compliant-cookies
description: >-
  Implementation guide for CNIL-compliant cookie consent per French guidelines.
  References the EUR 150M Google fine and EUR 60M Meta fine as enforcement precedents.
  Covers equal prominence accept/reject requirements, cookie wall prohibition,
  6-month reconsent intervals, essential cookies exemption, and technical implementation.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: consent-management
  tags: "cnil-cookies, cookie-consent, french-privacy, cookie-wall, essential-cookies"
---

# Implementing CNIL-Compliant Cookies

## Overview

The CNIL (Commission Nationale de l'Informatique et des Libertes) has established the most detailed and strictly enforced cookie consent requirements in the EU through Deliberation No. 2020-091 (September 17, 2020) and subsequent enforcement actions. The EUR 150 million fine against Google LLC and the EUR 60 million fine against Meta Platforms Ireland (both January 6, 2022) established clear precedents for what constitutes non-compliant cookie consent.

## CNIL Cookie Consent Requirements

### 1. Equal Prominence of Accept and Reject

**Rule:** The mechanism for refusing cookies must be as easy to use as the mechanism for accepting them.

**CNIL interpretation (confirmed by enforcement):**
- A "Reject All" button must be available on the first layer of the consent banner
- The "Reject All" button must have the same visual weight as the "Accept All" button (same size, same color treatment, same font, same prominence)
- Having only an "Accept All" button and a "Manage Preferences" link is NOT compliant — this was the exact pattern that led to the Google EUR 150M fine

**CloudVault SaaS Inc. implementation:**
```
┌──────────────────────────────────────────────────────────┐
│  CloudVault uses cookies to improve your experience.     │
│  Learn more in our Cookie Policy.                        │
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │ Accept All   │  │ Reject All  │  │  Customize  │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
│                                                          │
│  All three buttons: same size (160x44px), same font      │
│  (16px Inter Bold), same color scheme (#2563EB blue      │
│  on white background)                                    │
└──────────────────────────────────────────────────────────┘
```

### 2. No Cookie Walls

**Rule:** Access to a website or service must not be conditioned on the user accepting cookies.

**CNIL Deliberation 2020-091, paragraph 17:** A "cookie wall" (making access to a site conditional on acceptance of cookies) generally deprives the user of genuine choice, thereby invalidating consent.

**Exception:** The CNIL has acknowledged (2022 guidance update) that a cookie wall may be acceptable in limited circumstances if the user has a genuine alternative means of accessing the content, but this exception is narrow and context-dependent.

### 3. Six-Month Reconsent Interval

**Rule:** Consent must be renewed at appropriate intervals.

**CNIL recommendation:** Maximum 6 months between consent requests. After 6 months, the consent choice expires and the user must be asked again.

**CloudVault SaaS Inc. implementation:**
- Cookie consent cookie (`cv_consent_version`) has a `Max-Age` of 15,778,800 seconds (approximately 6 months)
- When the cookie expires, the consent banner reappears
- If the consent text changes (new purposes, new vendors), reconsent is triggered immediately regardless of the 6-month interval

### 4. Essential Cookies Only Exemption

**Rule:** Cookies that are strictly necessary for the provision of the service explicitly requested by the user are exempt from the consent requirement.

**CNIL interpretation (aligned with ePrivacy Article 5(3) exemption):**

Exempt cookies at CloudVault SaaS Inc.:
| Cookie | Purpose | Exemption Basis |
|--------|---------|----------------|
| `cv_session_id` | User authentication session | Strictly necessary for authenticated service |
| `cv_csrf_token` | Cross-site request forgery protection | Strictly necessary for security |
| `cv_consent_version` | Storing consent choice | Strictly necessary for consent management |
| `cv_language` | User language preference | Strictly necessary for service delivery |
| `cv_load_balancer` | Server load distribution | Strictly necessary for service operation |

Non-exempt cookies requiring consent:
| Cookie | Purpose | Consent Required |
|--------|---------|-----------------|
| `_ga`, `_gid` | Google Analytics | Yes — analytics cookies |
| `_fbp` | Facebook Pixel | Yes — advertising/tracking |
| `_af_*` | AppsFlyer attribution | Yes — advertising measurement |
| `cv_ab_test` | A/B testing assignment | Yes — non-essential personalization |

### 5. No Scrolling or Browsing as Consent

**Rule:** Continuing to browse or scroll on a website does not constitute valid consent.

**CNIL Deliberation 2020-091, paragraph 16:** Consent must be manifested by a clear positive act. Continuing to browse a website is not such an act.

### 6. Complete Information Before Consent

**Rule:** Before consenting, the user must be informed of:
- The identity of all entities placing cookies (controllers and third parties, by name)
- The purposes of each cookie category
- How to withdraw consent
- The consequences of accepting or refusing

## Implementation Checklist

| # | Requirement | CNIL Reference | CloudVault Status |
|---|------------|----------------|-------------------|
| 1 | "Reject All" on first layer, same prominence as "Accept All" | Deliberation 2020-091; Google/Meta fines | Implemented |
| 2 | No cookie wall blocking content | Deliberation 2020-091, para 17 | Implemented |
| 3 | Consent expires and reconsent after maximum 6 months | Deliberation 2020-091, para 24 | 6-month cookie expiry |
| 4 | Essential cookies identified and exempt | ePrivacy Art. 5(3) exemption | 5 cookies exempt |
| 5 | No pre-selected cookie categories | GDPR Art. 4(11), CJEU C-673/17 | All toggles default OFF |
| 6 | Scrolling/browsing does not equal consent | Deliberation 2020-091, para 16 | No implicit consent |
| 7 | No cookies placed before consent (except essential) | ePrivacy Art. 5(3) | Consent gate blocks non-essential |
| 8 | Third parties identified by name | GDPR Art. 13(1)(e) | Named in "Customize" layer |
| 9 | Withdrawal accessible and equally easy | GDPR Art. 7(3) | Footer link + Settings > Privacy |
| 10 | Consent records maintained | GDPR Art. 7(1) | Full audit trail per consent |

## Enforcement Precedents

### CNIL v. Google LLC — EUR 150,000,000 (January 6, 2022)

**Violation:** On google.fr, the cookie consent interface offered a "J'accepte" (I accept) button on the first layer but no equivalent reject button. Users who wanted to refuse had to click "Personnaliser" (Customize) and then make selections before clicking "Confirmer" (Confirm). Accepting required 1 click; refusing required 2+ clicks.

**CNIL analysis:** The absence of a "Refuse All" button on the first layer, comparable to the "Accept All" button, impeded users' ability to refuse cookies as easily as they could accept them.

### CNIL v. Meta Platforms Ireland — EUR 60,000,000 (January 6, 2022)

**Violation:** On facebook.com, similar asymmetry: "Autoriser les cookies essentiels et optionnels" (Allow essential and optional cookies) was prominently displayed, while refusing required navigating to secondary pages.

### CNIL v. Microsoft Ireland — EUR 60,000,000 (December 22, 2022)

**Violation:** On bing.com, the "Accepter" (Accept) button was displayed without an equally visible "Refuser" (Refuse) button on the first layer.

### CNIL v. TikTok — EUR 5,000,000 (December 29, 2022)

**Violation:** On tiktok.com, refusing cookies was more complex than accepting; insufficient information provided about cookie purposes.

## Key Regulatory References

- CNIL Deliberation No. 2020-091 (September 17, 2020) — Guidelines on cookies and trackers
- CNIL Deliberation No. 2022-013 — Google LLC fine
- CNIL Deliberation No. 2022-014 — Meta fine
- CNIL Deliberation No. 2022-174 — Microsoft fine
- CNIL Deliberation No. 2022-177 — TikTok fine
- ePrivacy Directive Article 5(3) — Consent for device storage access
- GDPR Article 7 — Conditions for consent
- CJEU C-673/17 (Planet49) — Pre-ticked boxes prohibition
- EDPB Guidelines 05/2020 — Consent under Regulation 2016/679
