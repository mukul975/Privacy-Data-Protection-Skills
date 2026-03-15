---
name: cookie-audit
description: >-
  Comprehensive methodology for auditing website cookies and tracking technologies.
  Covers automated scanning, cookie categorization, lifecycle documentation, and
  compliance gap analysis referencing the Planet49 CJEU ruling (C-673/17).
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cookie-consent-compliance
  tags: "cookie-audit, cookie-scanning, tracker-detection, planet49, cookie-categorization"
---

# Auditing Website Cookies and Trackers

## Overview

A cookie audit is the foundational step in achieving cookie consent compliance. It involves systematically identifying, categorizing, and documenting every cookie and tracking technology deployed on a website. The Court of Justice of the European Union in Planet49 GmbH v. Bundesverband der Verbraucherzentralen (Case C-673/17, 1 October 2019) established that pre-ticked checkboxes do not constitute valid consent under the ePrivacy Directive, and that users must be informed about cookie duration and third-party access before consenting. A thorough audit reveals what consent must be obtained and what disclosures must be made.

## Audit Methodology

### Phase 1: Preparation

Before scanning, document the audit scope for Pinnacle E-Commerce Ltd:

| Parameter | Value |
|-----------|-------|
| Primary domain | www.pinnacle-ecommerce.com |
| Subdomains in scope | shop.pinnacle-ecommerce.com, account.pinnacle-ecommerce.com, blog.pinnacle-ecommerce.com |
| Authenticated pages | Yes — customer account, checkout flow |
| Mobile-specific pages | m.pinnacle-ecommerce.com |
| Third-party integrations | Google Analytics 4, Meta Pixel, Hotjar, Stripe, Intercom |
| Scan frequency | Quarterly (next: Q2 2026) |

### Phase 2: Automated Scanning

Deploy scanning tools to capture all cookies and tracking technologies:

**Browser-Based Scanning**

Use a headless Chromium instance to crawl the site and capture:
- First-party cookies set via `Set-Cookie` headers
- First-party cookies set via `document.cookie` JavaScript API
- Third-party cookies from embedded resources
- LocalStorage and SessionStorage entries
- IndexedDB databases
- Pixels and beacons (1x1 image requests, `navigator.sendBeacon()` calls)
- Browser fingerprinting scripts (canvas, WebGL, AudioContext)

**Network-Level Capture**

Monitor HTTP/HTTPS traffic to identify:
- Tracking parameters in URL query strings (utm_*, fbclid, gclid)
- Redirect chains through tracking domains
- Cookie syncing between third parties
- Server-to-server data sharing endpoints

### Phase 3: Cookie Categorization

Classify each cookie using the ICC UK Cookie Guide categories, aligned with the ePrivacy Directive Article 5(3):

**Category 1: Strictly Necessary**
Cookies essential for the website to function. No consent required under Article 5(3) exemption.

Examples for Pinnacle E-Commerce Ltd:
| Cookie Name | Domain | Duration | Purpose |
|-------------|--------|----------|---------|
| session_id | .pinnacle-ecommerce.com | Session | Maintains user session state |
| csrf_token | .pinnacle-ecommerce.com | Session | Cross-site request forgery protection |
| cart_items | shop.pinnacle-ecommerce.com | 24 hours | Shopping cart contents |
| auth_token | account.pinnacle-ecommerce.com | 30 minutes | Authentication state |
| load_balancer | .pinnacle-ecommerce.com | Session | Server load distribution |

**Category 2: Performance/Analytics**
Cookies that collect aggregate usage data. Consent required.

| Cookie Name | Domain | Duration | Purpose |
|-------------|--------|----------|---------|
| _ga | .pinnacle-ecommerce.com | 2 years | Google Analytics client ID |
| _ga_XXXXXXX | .pinnacle-ecommerce.com | 2 years | GA4 session persistence |
| _gid | .pinnacle-ecommerce.com | 24 hours | GA4 session distinction |
| _hjSessionUser_* | .pinnacle-ecommerce.com | 1 year | Hotjar user identification |
| _hjSession_* | .pinnacle-ecommerce.com | 30 minutes | Hotjar session data |

**Category 3: Functionality**
Cookies that remember user preferences. Consent required unless strictly necessary.

| Cookie Name | Domain | Duration | Purpose |
|-------------|--------|----------|---------|
| locale | .pinnacle-ecommerce.com | 1 year | Language preference |
| currency | shop.pinnacle-ecommerce.com | 1 year | Currency selection |
| recently_viewed | shop.pinnacle-ecommerce.com | 30 days | Recently viewed products |

**Category 4: Targeting/Advertising**
Cookies used for ad targeting and cross-site tracking. Consent always required.

| Cookie Name | Domain | Duration | Purpose |
|-------------|--------|----------|---------|
| _fbp | .pinnacle-ecommerce.com | 90 days | Meta Pixel browser ID |
| _fbc | .pinnacle-ecommerce.com | 90 days | Meta click identifier |
| _gcl_au | .pinnacle-ecommerce.com | 90 days | Google Ads conversion linker |
| IDE | .doubleclick.net | 13 months | Google ad serving |
| fr | .facebook.com | 90 days | Meta ad delivery and measurement |

### Phase 4: Gap Analysis

For each cookie identified, verify against Planet49 requirements:

**Planet49 Compliance Checklist:**

1. **Active consent mechanism**: Is consent collected via affirmative action (click, toggle), not pre-ticked boxes? (Planet49, para. 62)
2. **Pre-consent information**: Before consent is given, is the user informed of:
   - Cookie duration? (Planet49, para. 81)
   - Whether third parties have access? (Planet49, para. 81)
   - The specific purpose of each cookie category?
3. **Granularity**: Can users consent to cookie categories individually, not just accept all?
4. **No cookie walls**: Is site access available without consenting to non-essential cookies?
5. **Withdrawal mechanism**: Can users withdraw consent as easily as they gave it?

**Gap Analysis Template:**

| Cookie | Category | Consent Collected | Duration Disclosed | Third-Party Disclosed | Gap |
|--------|----------|-------------------|--------------------|-----------------------|-----|
| _ga | Analytics | Yes | No — listed as "persistent" not "2 years" | No — Google not named | Duration + third-party disclosure |
| _fbp | Targeting | Yes | Yes | Yes | None |
| locale | Functionality | No | No | N/A | Assess if strictly necessary |

### Phase 5: Reporting

The audit report for Pinnacle E-Commerce Ltd must include:

1. **Executive summary**: Total cookies found, breakdown by category, critical gaps
2. **Complete cookie inventory**: Full table with name, domain, duration, purpose, category, legal basis
3. **Third-party tracker inventory**: All third-party domains receiving data, with data types shared
4. **Compliance gap register**: Each gap, severity (high/medium/low), remediation recommendation
5. **Cookie policy update recommendations**: Specific text changes needed
6. **Consent mechanism assessment**: Whether current banner meets Planet49 requirements
7. **Recommended scan schedule**: Quarterly for production, on-demand for new feature deployments

## Ongoing Monitoring

Schedule automated scans to detect new cookies introduced by:
- Developer deployments (new analytics or marketing tags)
- Third-party script updates (vendor SDK updates adding new cookies)
- A/B testing platforms adding experiment cookies
- CDN or infrastructure changes

Integrate cookie scanning into the CI/CD pipeline: any new cookie detected in staging must be categorized and documented before deployment to production.

## Key Legal References

- **CJEU Case C-673/17 (Planet49)** — Active consent required; pre-ticked boxes invalid; cookie duration and third-party access must be disclosed before consent
- **ePrivacy Directive 2002/58/EC, Article 5(3)** — Consent required for storing/accessing information on user devices, with strictly necessary exemption
- **GDPR Article 4(11)** — Definition of consent: freely given, specific, informed, unambiguous indication
- **EDPB Guidelines 05/2020 on Consent** — Detailed guidance on valid consent mechanisms
- **ICC UK Cookie Guide (2012)** — Cookie categorization framework (strictly necessary, performance, functionality, targeting)
- **CNIL Deliberation No. 2020-091 (17 September 2020)** — Guidelines on cookies and other trackers
