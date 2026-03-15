---
name: gpc-cookie-integration
description: >-
  Integrating Global Privacy Control (GPC) signals with cookie consent platforms.
  Covers GPC signal detection in browsers, automatic opt-out triggering, mapping
  GPC to US state privacy laws, and CMP integration for CCPA, CPA, and CTDPA compliance.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cookie-consent-compliance
  tags: "gpc, global-privacy-control, opt-out, ccpa-opt-out, universal-opt-out"
---

# Global Privacy Control Integration with Cookie Consent

## Overview

Global Privacy Control (GPC) is a browser-level signal that communicates a user's privacy preferences to websites. Specified by the GPC community group and recognized as a legally binding opt-out mechanism under California's CCPA/CPRA (effective January 1, 2023), Colorado's CPA (effective July 1, 2024), Connecticut's CTDPA (effective July 1, 2023), and other US state privacy laws, GPC transmits a `Sec-GPC: 1` HTTP header and a `navigator.globalPrivacyControl` JavaScript property with each request. Websites must detect this signal and automatically trigger opt-out of sale, sharing, and targeted advertising without requiring additional user action. Integration with cookie consent management platforms (CMPs) is essential to ensure the GPC signal correctly suppresses advertising cookies and data sharing.

## GPC Signal Specification

### How GPC Works

**HTTP Header:**
```
Sec-GPC: 1
```
Present on every HTTP request when the user has enabled GPC in their browser or browser extension.

**JavaScript API:**
```javascript
navigator.globalPrivacyControl  // Returns true if GPC is enabled
```

**GPC-Enabled Browsers and Extensions:**

| Browser/Extension | GPC Support | How to Enable |
|-------------------|-------------|---------------|
| Firefox | Built-in (v120+) | Settings > Privacy & Security > "Tell websites not to sell or share my data" |
| Brave | Built-in (default ON) | Enabled by default; disable in Settings > Shields |
| DuckDuckGo Browser | Built-in (default ON) | Enabled by default on mobile and desktop |
| DuckDuckGo Extension | Extension | Install extension; GPC enabled by default |
| Privacy Badger (EFF) | Extension | Install extension; GPC enabled by default |
| OptMeowt | Extension | Chrome/Firefox extension specifically for GPC |
| Safari | Not natively supported | Requires third-party extension |
| Chrome | Not natively supported | Requires extension (DuckDuckGo, Privacy Badger) |

### GPC vs. Do Not Track (DNT)

| Feature | GPC | DNT |
|---------|-----|-----|
| HTTP header | `Sec-GPC: 1` | `DNT: 1` |
| JavaScript API | `navigator.globalPrivacyControl` | `navigator.doNotTrack` |
| Legal recognition | Yes — CCPA/CPRA, CPA, CTDPA, other state laws | No legal enforcement mechanism |
| Scope | Opt-out of sale, sharing, targeted advertising | General tracking preference |
| Browser adoption | Growing (Firefox, Brave, DuckDuckGo) | Deprecated by most browsers |
| Industry compliance | Legally required in applicable jurisdictions | Largely ignored |

## US State Law Mapping

### GPC Legal Requirements by State

| State | Law | GPC Status | Effective Date | Requirement |
|-------|-----|------------|----------------|-------------|
| California | CCPA/CPRA | Legally binding opt-out | Jan 1, 2023 | Must treat GPC as valid opt-out of sale and sharing (Cal. Civ. Code §1798.135(e); 11 CCR §7025(b)) |
| Colorado | CPA | Legally binding opt-out | Jul 1, 2024 | Must honor "universal opt-out mechanism" including GPC (C.R.S. §6-1-1313(1)(a); 4 CCR 904-3 Rule 5.11) |
| Connecticut | CTDPA | Legally binding opt-out | Jul 1, 2023 (UOM: Jan 1, 2025) | Must honor "opt-out preference signal" (P.A. 22-15, §6(a)(6)) |
| Montana | MCDPA | Legally binding opt-out | Oct 1, 2024 | Must honor universal opt-out mechanism |
| Texas | TDPSA | Legally binding opt-out | Jul 1, 2024 (UOM: Jan 1, 2025) | Must honor universal opt-out mechanism |
| Oregon | OCPA | Legally binding opt-out | Jul 1, 2024 (UOM: Jan 1, 2026) | Must honor universal opt-out mechanism |
| Delaware | DPDPA | Legally binding opt-out | Jan 1, 2025 (UOM: Jan 1, 2026) | Must honor universal opt-out mechanism |
| New Hampshire | NHPA | Legally binding opt-out | Jan 1, 2025 | Must honor universal opt-out mechanism |
| New Jersey | NJDPA | Legally binding opt-out | Jan 15, 2025 (UOM: Jul 15, 2025) | Must honor universal opt-out mechanism |
| Virginia | VCDPA | Voluntary (no UOM mandate) | Jan 1, 2023 | No explicit UOM requirement, but opt-out of targeted advertising required |
| Utah | UCPA | Voluntary (no UOM mandate) | Dec 31, 2023 | No UOM requirement |

### What GPC Triggers

When GPC is detected for a user in an applicable jurisdiction:

| Processing Activity | GPC Impact | Action Required |
|--------------------|-----------|--------------------|
| Sale of personal information | Opt-out triggered | Stop selling PI for this user |
| Sharing for cross-context behavioral advertising | Opt-out triggered | Stop sharing PI with ad partners |
| Targeted advertising | Opt-out triggered (CPA, CTDPA, TDPSA) | Disable behavioral targeting |
| Profiling for automated decisions | Opt-out triggered (some states) | Disable profiling |
| Analytics (first-party) | Not triggered | GPC does not opt out of first-party analytics |
| Essential cookies | Not triggered | Strictly necessary cookies unaffected |

## CMP Integration

### Detection and Response Flow

```
Page Load
    │
    ├── Check for GPC signal
    │   ├── navigator.globalPrivacyControl === true
    │   │   OR
    │   └── Server detects Sec-GPC: 1 header
    │
    ├── Determine user jurisdiction
    │   ├── IP geolocation → US state mapping
    │   └── Check if state has GPC legal requirement
    │
    ├── If GPC detected AND applicable jurisdiction:
    │   ├── Automatically set consent state:
    │   │   ├── ad_storage: denied
    │   │   ├── ad_user_data: denied
    │   │   ├── ad_personalization: denied
    │   │   ├── analytics_storage: [per CMP default — GPC does not cover]
    │   │   └── sale_of_data: opted_out
    │   │
    │   ├── Block advertising cookies and tags
    │   ├── Do NOT fire: Meta Pixel, Google Ads remarketing, third-party ad tags
    │   ├── DO fire: GA4 (if analytics consent separate from GPC)
    │   │
    │   ├── Display modified banner (optional):
    │   │   "We detected your Global Privacy Control preference.
    │   │    We will not sell or share your personal information.
    │   │    [Manage Other Preferences]"
    │   │
    │   └── Record GPC opt-out in consent log
    │
    └── If GPC detected but NON-applicable jurisdiction (e.g., EU):
        └── Treat as privacy signal but apply jurisdiction's own rules
            (EU still requires opt-in consent regardless of GPC)
```

### Implementation for Pinnacle E-Commerce Ltd

**Server-Side GPC Detection (Node.js middleware):**

```javascript
function detectGPC(req, res, next) {
  const gpcHeader = req.headers['sec-gpc'];
  const gpcEnabled = gpcHeader === '1';

  req.gpcSignal = gpcEnabled;

  if (gpcEnabled) {
    // Determine jurisdiction from IP
    const userState = geolocateToState(req.ip);

    // States where GPC is legally binding
    const gpcMandatoryStates = ['CA', 'CO', 'CT', 'MT', 'TX', 'OR', 'DE', 'NH', 'NJ'];

    req.gpcLegallyBinding = gpcMandatoryStates.includes(userState);
    req.gpcOptOut = {
      sale: gpcEnabled && req.gpcLegallyBinding,
      sharing: gpcEnabled && req.gpcLegallyBinding,
      targetedAdvertising: gpcEnabled && req.gpcLegallyBinding,
    };
  }

  next();
}
```

**Client-Side GPC Detection and CMP Update:**

```javascript
function handleGPCSignal() {
  const gpcEnabled = navigator.globalPrivacyControl === true;

  if (!gpcEnabled) return;

  // Get user's jurisdiction (from server or geolocation)
  const userJurisdiction = getUserJurisdiction();
  const gpcBindingStates = ['CA', 'CO', 'CT', 'MT', 'TX', 'OR', 'DE', 'NH', 'NJ'];

  if (gpcBindingStates.includes(userJurisdiction)) {
    // Update Google Consent Mode
    gtag('consent', 'update', {
      'ad_storage': 'denied',
      'ad_user_data': 'denied',
      'ad_personalization': 'denied',
      // analytics_storage not affected by GPC
    });

    // Update CMP state
    updateCMPState({
      sale_optout: true,
      sharing_optout: true,
      targeted_advertising_optout: true,
      source: 'gpc_signal',
    });

    // Remove any existing advertising cookies
    removeAdvertisingCookies();

    // Log GPC opt-out
    logConsentEvent({
      type: 'gpc_auto_optout',
      jurisdiction: userJurisdiction,
      timestamp: new Date().toISOString(),
      gpc_header_present: true,
    });
  }
}

function removeAdvertisingCookies() {
  const adCookies = ['_fbp', '_fbc', '_gcl_au', 'IDE', 'fr', 'NID'];
  adCookies.forEach(name => {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; domain=.pinnacle-ecommerce.com`;
  });
}

// Run on page load
handleGPCSignal();
```

### CMP Platform Integration

**OneTrust GPC Configuration:**

| Setting | Value |
|---------|-------|
| Honor GPC Signal | Enabled |
| GPC Treatment | Apply to "Sale of Personal Data" and "Targeted Advertising" categories |
| GPC Applicable Regions | US-CA, US-CO, US-CT, US-MT, US-TX, US-OR, US-DE, US-NH, US-NJ |
| GPC Banner Behavior | Suppress opt-out banner (already opted out); show confirmation notice |
| GPC Consent Record | Log GPC signal as opt-out source |

**Cookiebot GPC Configuration:**

| Setting | Value |
|---------|-------|
| Respect GPC | Enabled |
| GPC → Category Mapping | GPC = reject "Marketing" category |
| GPC Regions | California, Colorado, Connecticut, Montana, Texas, Oregon, Delaware, New Hampshire, New Jersey |

## GPC Verification and Compliance

### Testing GPC Integration

| Test | Expected Behavior | Verification Method |
|------|-------------------|-------------------|
| GPC header sent | Browser sends `Sec-GPC: 1` | Network inspector |
| Server detects GPC | Middleware sets `req.gpcSignal = true` | Server logs |
| Ad cookies blocked | No _fbp, _gcl_au, IDE cookies set | Cookie inspector |
| Ad tags blocked | No Meta Pixel, Google Ads remarketing requests | Network inspector |
| Analytics unaffected | GA4 still fires (GPC does not cover analytics) | GA4 real-time reports |
| Consent log records GPC | GPC opt-out logged with timestamp and jurisdiction | Database query |
| CCPA opt-out link reflects GPC | "Do Not Sell" page shows GPC-detected opt-out status | UI inspection |
| Modified banner displayed | Banner acknowledges GPC preference | Visual verification |

### CCPA/CPRA Specific Requirements

Under California Attorney General regulations (11 CCR §7025):

1. **No degradation of service**: A business must not interpret GPC as consent to financial incentive opt-in
2. **Conflict resolution**: If a user has previously opted in to sale/sharing, GPC on a subsequent visit should be treated as a revocation of that opt-in
3. **No re-prompting**: Do not ask a GPC user to reconsider their opt-out choice
4. **Record keeping**: Maintain records of GPC-triggered opt-outs for 24 months
5. **Privacy policy disclosure**: State in the privacy policy that the business honors GPC

**Pinnacle E-Commerce Ltd Privacy Policy Language:**

> "We recognize the Global Privacy Control (GPC) signal sent by your browser. When we detect a GPC signal from a user in California, we treat it as a request to opt out of the sale and sharing of personal information as defined under the California Consumer Privacy Act (CCPA) and California Privacy Rights Act (CPRA). We apply this opt-out automatically without requiring any additional action from you."

## Edge Cases

| Scenario | Resolution |
|----------|-----------|
| User has GPC enabled but previously opted IN to sharing | GPC overrides — treat as opt-out (most recent signal governs) |
| User has GPC enabled and is in non-applicable state (e.g., Utah) | Respect GPC as privacy preference but not legally required |
| User has GPC enabled and is in EU | GPC does not substitute for opt-in consent; apply EU rules |
| GPC detected on API request (no browser) | Honor if Sec-GPC header present (may be from privacy-aware app) |
| GPC enabled for some pages, disabled for others | Per-request evaluation; this should not normally occur |
| Multiple opt-out signals (GPC + cookie banner reject) | Apply most restrictive — both result in opt-out |

## Key Legal and Technical References

- **GPC Specification (globalprivacycontrol.org)** — Technical specification for the GPC signal
- **CCPA/CPRA Cal. Civ. Code §1798.135(e)** — Business must treat GPC as valid opt-out request
- **11 CCR §7025(b)-(c) (California AG Regulations)** — GPC implementation requirements
- **Colorado CPA Rules, 4 CCR 904-3, Rule 5.11** — Universal opt-out mechanism requirements including GPC
- **Connecticut CTDPA P.A. 22-15, §6(a)(6)** — Opt-out preference signal requirement
- **California AG Enforcement Action: Sephora (August 2022)** — First CCPA enforcement for failure to honor GPC; $1.2 million settlement
- **EDPB Statement on GPC (2023)** — European perspective on GPC as an expression of Article 21 objection right
- **W3C Privacy Community Group** — GPC specification development
- **IAB CCPA Compliance Framework** — US Privacy String and GPC interoperability
