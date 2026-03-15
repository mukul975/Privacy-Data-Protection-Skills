---
name: cookie-lifetime-audit
description: >-
  Auditing cookie lifetimes against regulatory recommendations and browser policies.
  Covers CNIL 13-month maximum recommendation, session vs persistent classification,
  third-party cookie phase-out impact, and Safari ITP duration caps.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cookie-consent-compliance
  tags: "cookie-lifetime, cookie-duration, cnil-13-month, itp, cookie-phase-out"
---

# Auditing Cookie Lifetimes

## Overview

Cookie lifetime is a critical compliance factor often overlooked in consent implementations. The CNIL recommends a maximum cookie lifetime of 13 months from the point of collection, after which consent must be renewed. The CJEU in Planet49 (Case C-673/17) established that cookie duration must be disclosed to users before consent is obtained. Additionally, browser-enforced restrictions — Safari's Intelligent Tracking Prevention (ITP), Firefox's Enhanced Tracking Protection (ETP), and Chrome's third-party cookie deprecation — impose technical limits on cookie lifetimes that may conflict with server-set durations. A cookie lifetime audit identifies cookies exceeding regulatory or technical limits and ensures accurate duration disclosure.

## Cookie Duration Classification

### Session vs. Persistent Cookies

| Type | Duration | Behavior | Consent Implications |
|------|----------|----------|---------------------|
| Session cookie | No `Expires` or `Max-Age` attribute | Deleted when browser closes | Still requires consent if non-essential under ePrivacy Art. 5(3) |
| Persistent cookie | Has `Expires` or `Max-Age` | Survives browser restart | Requires consent; duration must be disclosed (Planet49) |
| Server-refreshed | Reset on each visit via Set-Cookie | Effectively indefinite if user visits regularly | Duration is from last visit, not first set — must disclose rolling nature |

### Duration Categories

| Category | Duration Range | Examples | Regulatory Concern |
|----------|---------------|----------|-------------------|
| Short-lived | < 24 hours | Session IDs, CSRF tokens | Low — typically strictly necessary |
| Medium-lived | 24 hours - 30 days | A/B test assignments, session replay | Medium — review necessity |
| Long-lived | 30 days - 13 months | Analytics IDs, preference cookies | High — must justify duration |
| Excessive | > 13 months | Legacy tracking cookies, _ga (2 years) | Very high — CNIL non-compliant duration |

## CNIL 13-Month Recommendation

### Regulatory Basis

CNIL's Recommendation on Cookies (1 October 2020, following Deliberation 2020-091 of 17 September 2020) states:

> "The duration of validity of the consent of the user to the deposit of trackers should not exceed thirteen months. At the end of this period, the consent of the user should be collected again."

This 13-month maximum applies to:
- The consent cookie itself (the cookie that records the user's consent choice)
- Non-essential tracking cookies (the cookies enabled by consent)

### Impact on Common Cookies

**Cookies Exceeding CNIL 13-Month Limit:**

| Cookie | Default Duration | Set By | CNIL Compliant | Remediation |
|--------|-----------------|--------|----------------|-------------|
| _ga | 2 years (730 days) | Google Analytics | No — exceeds 13 months | Set `cookie_expires` to 34128000 (395 days / ~13 months) |
| _ga_XXXXXXX | 2 years | GA4 | No — exceeds 13 months | Set `cookie_expires` to 34128000 |
| IDE | 13 months | DoubleClick | Borderline compliant | Monitor — at the limit |
| fr | 90 days | Meta/Facebook | Yes | No action needed |
| _gcl_au | 90 days | Google Ads | Yes | No action needed |
| _hjSessionUser_* | 1 year | Hotjar | Yes — under 13 months | No action needed |
| NID | 6 months | Google Search | Yes | No action needed |

### GA4 Cookie Lifetime Configuration for Pinnacle E-Commerce Ltd

Override default GA4 cookie duration to comply with CNIL:

**gtag.js implementation:**
```javascript
gtag('config', 'G-PINNACLE123', {
  'cookie_expires': 34128000,     // 395 days (~13 months) in seconds
  'cookie_update': true,           // Refresh cookie on each visit
  'cookie_domain': '.pinnacle-ecommerce.com',
  'cookie_flags': 'SameSite=Lax;Secure'
});
```

**GTM implementation:**
In the GA4 Configuration tag, set the field:
- Field name: `cookie_expires`
- Value: `34128000`

## Browser-Enforced Lifetime Restrictions

### Safari Intelligent Tracking Prevention (ITP)

Safari imposes strict cookie lifetime caps:

| Cookie Type | ITP Rule | Effective Lifetime |
|-------------|----------|-------------------|
| Client-side JavaScript cookie (document.cookie) | Capped at 7 days | 7 days maximum |
| Client-side JS cookie with link decoration (e.g., ?gclid=) | Capped at 24 hours | 24 hours |
| Server-set cookie (Set-Cookie header), first-party | No cap | As set by server |
| Server-set cookie, classified as tracking | Capped at 7 days | 7 days |
| Third-party cookie | Blocked entirely | 0 (cannot be set) |
| LocalStorage | Capped at 7 days | 7 days |

**Impact on Pinnacle E-Commerce Ltd:**
- GA4 `_ga` cookie set via JavaScript: Effective lifetime is 7 days on Safari, not 2 years
- Server-side tagging (via data.pinnacle-ecommerce.com) sets `_ga` via Set-Cookie header: Full configured lifetime applies
- Google Ads click IDs in URL parameters: `_gcl_au` cookie capped at 24 hours on Safari

### Firefox Enhanced Tracking Protection (ETP)

| Setting | Default (Standard) | Strict |
|---------|-------------------|--------|
| Third-party tracking cookies | Blocked | Blocked |
| Cross-site tracking cookies | Blocked | Blocked |
| First-party tracking cookies | Allowed | Limited to 7 days (if tracker classified) |
| Fingerprinting scripts | Blocked | Blocked |
| Cryptomining scripts | Blocked | Blocked |

### Chrome Third-Party Cookie Changes

As of 2025, Chrome has moved toward a user-choice model for third-party cookies rather than full deprecation:

| Phase | Status | Impact |
|-------|--------|--------|
| Privacy Sandbox APIs available | Active | Topics API, Attribution Reporting API available |
| Third-party cookie user controls | Active | Users can block third-party cookies in settings |
| IP Protection (Gnatcatcher) | In development | May affect IP-based tracking |

## Cookie Lifetime Audit Process

### Step 1: Extract Current Cookie Lifetimes

For each cookie on pinnacle-ecommerce.com, record:

| Cookie Name | Domain | Set By | Declared Duration | Actual Max-Age/Expires | Refreshed on Visit | Category |
|-------------|--------|--------|-------------------|----------------------|--------------------| ---------|
| _ga | .pinnacle-ecommerce.com | JavaScript | 2 years | Max-Age=63072000 | Yes | Analytics |
| _ga_PINNACLE | .pinnacle-ecommerce.com | JavaScript | 2 years | Max-Age=63072000 | Yes | Analytics |
| _gid | .pinnacle-ecommerce.com | JavaScript | 24 hours | Max-Age=86400 | Yes | Analytics |
| _fbp | .pinnacle-ecommerce.com | JavaScript | 90 days | Max-Age=7776000 | No | Advertising |
| _fbc | .pinnacle-ecommerce.com | JavaScript | 90 days | Max-Age=7776000 | No | Advertising |
| _gcl_au | .pinnacle-ecommerce.com | JavaScript | 90 days | Max-Age=7776000 | No | Advertising |
| session_id | .pinnacle-ecommerce.com | Server | Session | No Max-Age | N/A | Necessary |
| csrf_token | .pinnacle-ecommerce.com | Server | Session | No Max-Age | N/A | Necessary |
| locale | .pinnacle-ecommerce.com | Server | 1 year | Max-Age=31536000 | No | Functionality |
| consent_state | .pinnacle-ecommerce.com | JavaScript | 6 months | Max-Age=15768000 | No | Necessary |

### Step 2: Compare Against Limits

| Cookie | Server-Set Duration | CNIL 13-Month Limit | Safari ITP Limit | Compliant | Action Required |
|--------|--------------------|--------------------|-----------------|-----------|-----------------|
| _ga | 2 years | Exceeds | 7 days (JS) | No | Reduce to 13 months; move to server-side |
| _ga_PINNACLE | 2 years | Exceeds | 7 days (JS) | No | Reduce to 13 months; move to server-side |
| _gid | 24 hours | Within | 7 days (JS) | Yes | None |
| _fbp | 90 days | Within | 7 days (JS) | Partial | Move to server-side for Safari |
| locale | 1 year | Within | No cap (server) | Yes | None |
| consent_state | 6 months | Within | 7 days (JS) | Partial | Move to server-side; aligns with CNIL 6-month reconsent |

### Step 3: Verify Disclosure Accuracy

Compare actual cookie lifetimes with durations stated in the cookie policy:

| Cookie | Policy States | Actual Duration | Accurate |
|--------|--------------|-----------------|----------|
| _ga | "up to 2 years" | 2 years | Yes — but update to reflect 13-month override |
| _fbp | "3 months" | 90 days | Yes |
| locale | "12 months" | 1 year | Yes |
| _gid | "24 hours" | 24 hours | Yes |

### Step 4: Generate Remediation Plan

For Pinnacle E-Commerce Ltd:

1. **Immediate**: Override GA4 cookie duration to 13 months (`cookie_expires: 34128000`)
2. **Short-term**: Implement server-side tagging for `_ga`, `_fbp` cookies to bypass Safari ITP 7-day cap
3. **Medium-term**: Implement automatic consent recollection at 6 months (CNIL reconsent cycle)
4. **Ongoing**: Add cookie lifetime checks to CI/CD pipeline — flag any new cookie with duration > 13 months

## Key Legal and Technical References

- **CNIL Deliberation No. 2020-091 (17 September 2020)** — 13-month maximum cookie lifetime recommendation
- **CNIL Recommendation on Cookies (1 October 2020)** — Practical implementation of lifetime limits
- **CJEU Case C-673/17 (Planet49), para. 81** — Cookie duration must be disclosed before consent
- **ePrivacy Directive 2002/58/EC, Article 5(3)** — Consent required for non-essential cookie storage
- **Apple WebKit ITP Documentation** — Safari cookie lifetime restrictions
- **Mozilla ETP Documentation** — Firefox tracking protection policies
- **Google Privacy Sandbox Timeline** — Chrome third-party cookie deprecation status
- **GDPR Article 5(1)(e)** — Storage limitation principle applicable to cookie-stored personal data
