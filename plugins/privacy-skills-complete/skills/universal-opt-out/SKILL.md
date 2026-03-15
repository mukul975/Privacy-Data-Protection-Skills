---
name: universal-opt-out
description: >-
  Universal opt-out mechanism implementation across US state privacy laws.
  Covers Global Privacy Control (GPC) signal technical implementation,
  state-by-state recognition requirements, browser detection methods,
  authenticated vs unauthenticated handling, and compliance testing.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "universal-opt-out, gpc, global-privacy-control, opt-out-signal, browser-signal"
---

# Universal Opt-Out Mechanism Implementation

## Overview

A universal opt-out mechanism is a browser or device-level signal that communicates a consumer's privacy preferences to websites and online services. The Global Privacy Control (GPC) is the leading universal opt-out mechanism, supported by major browsers (Firefox, Brave, DuckDuckGo) and browser extensions (Privacy Badger, Disconnect). Multiple US state privacy laws now require businesses to recognize and honor these signals.

GPC is defined in the Global Privacy Control specification (published by the GPC project), transmitted via the `Sec-GPC: 1` HTTP header and the `navigator.globalPrivacyControl` JavaScript API.

## State-by-State Requirements

| State | Law | Signal Required | Effective Date | Scope |
|-------|-----|-----------------|---------------|-------|
| California | CCPA/CPRA | Yes | Jan 1, 2023 | Sale + Sharing |
| Colorado | CPA | Yes | Jul 1, 2024 | Targeted ads + Sale |
| Connecticut | CTDPA | Yes | Jan 1, 2025 | Targeted ads + Sale |
| Montana | MTDPA | Yes | Oct 1, 2025 | Targeted ads + Sale |
| Texas | TDPSA | Not required | N/A | N/A |
| Virginia | VCDPA | Not required | N/A | N/A |
| Oregon | OCPA | Not required | N/A | N/A |
| Kentucky | KPPA | Not required | N/A | N/A |

## GPC Technical Specification

### HTTP Header

```
Sec-GPC: 1
```

The `Sec-GPC` header is a structured header with a bare item value of `1` (true) or absent (no preference expressed). The `Sec-` prefix indicates it is a fetch metadata header set by the browser, not by JavaScript.

### JavaScript API

```javascript
navigator.globalPrivacyControl  // boolean: true or undefined
```

The `navigator.globalPrivacyControl` property returns `true` if the user has enabled GPC in their browser or extension, or `undefined` if GPC is not active.

### Detection Code

```javascript
function detectGPC() {
    // Check JavaScript API
    const jsGPC = navigator.globalPrivacyControl === true;

    // The HTTP header is checked server-side
    // This function covers client-side detection only

    return {
        gpcEnabled: jsGPC,
        timestamp: new Date().toISOString(),
        userAgent: navigator.userAgent,
    };
}
```

### Server-Side Detection (Node.js/Express example)

```javascript
function checkGPCHeader(req) {
    const gpcHeader = req.headers['sec-gpc'];
    return gpcHeader === '1';
}

app.use((req, res, next) => {
    if (checkGPCHeader(req)) {
        req.gpcOptOut = true;
        // Apply opt-out before rendering page
        res.locals.suppressThirdPartyTags = true;
        res.locals.suppressCrossSiteBehavioralAds = true;
    }
    next();
});
```

## Implementation Architecture

### Layer 1: Signal Detection

```
HTTP Request Arrives
  │
  ├─► Server-Side Check
  │     └─ Parse Sec-GPC header from request
  │
  ├─► Client-Side Check (for SPAs)
  │     └─ Read navigator.globalPrivacyControl
  │
  └─► Combined Result
        ├─ GPC detected = true → Apply opt-out
        └─ GPC not detected → Normal processing
```

### Layer 2: Scope Determination

| State | Sale Opt-Out | Sharing Opt-Out | Targeted Ads Opt-Out | Profiling Opt-Out |
|-------|-------------|-----------------|---------------------|-------------------|
| California | Yes | Yes | Implied (sharing = cross-context behavioral ads) | No (separate) |
| Colorado | Yes | N/A | Yes | No (separate) |
| Connecticut | Yes | N/A | Yes | No (separate) |
| Montana | Yes | N/A | Yes | No (separate) |

### Layer 3: Consumer Identity Resolution

**Authenticated Consumer (logged in):**
- Associate GPC opt-out with consumer account
- Set persistent flag: `sale_opt_out = true`, `targeted_ads_opt_out = true`
- Override any prior opt-in (most recent preference per CO Rule 5.13)
- Persist across sessions and devices (account-level)

**Unauthenticated Consumer (not logged in):**
- Apply opt-out to current browsing session
- Set first-party session cookie to maintain state during session
- Apply on each new session when GPC signal is present
- Do not require identity verification

### Layer 4: Enforcement

Upon detecting GPC signal, the system must:

1. **Suppress third-party advertising tags** before page render:
   - AdReach Network pixel — BLOCKED
   - Cross-context behavioral advertising tags — BLOCKED
   - Retargeting/remarketing pixels — BLOCKED
   - Social media tracking widgets — BLOCKED

2. **Allow first-party processing**:
   - First-party analytics (where data stays with controller or service provider under contract)
   - Essential functionality cookies (session, cart, security)
   - Contextual advertising (based on current page content, not behavioral profile)

3. **Update server-side systems**:
   - Data sharing pipeline: suppress outbound feeds to third-party ad partners
   - CMP state: update consent management platform to reflect opt-out
   - Consumer profile: flag account (if authenticated) for persistent opt-out

## Compliance Rules by State

### California (CPPA Regulations §7025)

- §7025(a): Must process opt-out preference signals as valid opt-out requests
- §7025(b): Two-step opt-out process prohibited
- §7025(c): Must not require consumer to verify identity
- §7025(d): Must not display pop-up or notification questioning the signal
- §7025(e): If consumer not identifiable, apply to browser/device
- §7025(f): If authenticated user has different prior setting, GPC takes precedence as most recent expression
- Scope: Sale AND sharing (cross-context behavioral advertising)

### Colorado (4 CCR 904-3, Rule 5.11)

- Rule 5.10: Must recognize universal opt-out mechanisms
- Rule 5.11: Must not display pop-up, interstitial, or other mechanism questioning signal
- Rule 5.12: Authenticated = account-level; unauthenticated = session-level
- Rule 5.13: Most recently expressed preference prevails on conflict
- Rule 5.14: AG biennial review of recognized mechanisms
- Scope: Targeted advertising AND sale
- Requirement: Mechanism must be affirmatively selected by consumer (not default)

### Connecticut (§42-520(a)(6))

- Must recognize universal opt-out mechanisms starting January 1, 2025
- Same principles as Colorado: no verification, no pop-ups
- Scope: Targeted advertising AND sale

### Montana (§30-14-2808(3))

- Must recognize universal opt-out mechanisms starting October 1, 2025
- Same principles as Colorado and Connecticut
- Scope: Targeted advertising AND sale

## Testing Protocol

### Test 1: GPC Signal Detection
- Install GPC-enabled browser (Brave, Firefox with GPC extension)
- Visit website
- Verify server logs show `Sec-GPC: 1` header detected
- Verify client-side `navigator.globalPrivacyControl === true`

### Test 2: Tag Suppression
- With GPC enabled: verify third-party advertising tags do NOT fire
- Without GPC: verify third-party advertising tags fire normally
- Inspect network requests to confirm suppression

### Test 3: Authenticated vs. Unauthenticated
- Visit with GPC while logged out: verify session-level opt-out
- Log in with GPC: verify account-level opt-out persists
- Log in without GPC after prior GPC opt-out: verify prior opt-out persists (account-level)

### Test 4: No Pop-Up or Interstitial
- Visit with GPC: verify no pop-up asks to confirm or modify signal
- Verify consent banner does not override or question GPC signal

### Test 5: Conflict Resolution
- Set account preference to opt-in to sale/targeted ads
- Visit with GPC enabled
- Verify GPC takes precedence (opt-out applied)

## Liberty Commerce Inc. Implementation

**Technology stack:** Consent management platform (CMP) with GPC signal handler, tag management system (TMS) with server-side control, privacy operations dashboard.

**Architecture:**
1. Edge proxy detects `Sec-GPC: 1` header on incoming requests
2. Request metadata includes `gpc_opt_out: true` flag
3. TMS evaluates flag before injecting any tags
4. CMP state updated for session/account
5. Server-side data sharing pipeline checks flag before transmitting to third parties
6. Compliance dashboard reports GPC detection rates and opt-out volume

## Key Regulatory References

- CPPA Regulations §7025 — Opt-out preference signals
- Colorado AG Regulations 4 CCR 904-3, Rule 5 — Universal opt-out mechanism
- Conn. Gen. Stat. §42-520(a)(6) — Universal opt-out recognition
- MCA §30-14-2808(3) — Universal opt-out recognition
- Global Privacy Control Specification v1.0 (globalprivacycontrol.org)
- W3C Community Group: GPC specification
- In re Sephora Inc. (2022) — $1.2M settlement for failure to honor GPC
