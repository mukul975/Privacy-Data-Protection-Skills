---
name: cpra-opt-out-signals
description: >-
  Implements CPRA Section 1798.135 opt-out preference signal handling, covering
  Global Privacy Control (GPC) technical detection, automated signal honoring,
  cross-device consistency, and the relationship between browser signals and
  explicit consumer choices. Activate for GPC, opt-out preference signal,
  CPRA 1798.135, browser privacy signal, Do Not Sell queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-subject-rights
  tags: "opt-out-preference-signal, gpc, cpra, global-privacy-control, do-not-sell"
---

# Implementing CPRA Opt-Out Preference Signals

## Overview

CPRA Section 1798.135 requires businesses to treat opt-out preference signals (such as Global Privacy Control / GPC) as valid consumer requests to opt out of the sale and sharing of personal information. This skill covers the technical detection of GPC signals, automated honoring workflows, cross-device consistency requirements, and the interaction between browser-level signals and explicit consumer choices.

## Legal Foundation

### CPRA Section 1798.135 — Methods of Limiting Sale, Sharing, and Use

1. **Section 1798.135(a)** — A business that sells or shares consumers' personal information shall provide a clear and conspicuous link on its homepage titled "Do Not Sell or Share My Personal Information."

2. **Section 1798.135(b)(1)** — A business that sells or shares personal information shall treat the consumer's use of an opt-out preference signal as a valid request to opt out under Section 1798.120.

3. **Section 1798.135(b)(3)** — A business that complies with subsection (b)(1) is not required to post the "Do Not Sell or Share My Personal Information" link on its homepage, provided it instead posts a link to a page describing the consumer's opt-out rights.

4. **Section 1798.135(e)** — A business may not interpret the absence of an opt-out preference signal as consent to sell or share personal information.

### CCPA Regulations (11 CCR Section 7025)

- **Section 7025(a)** — A business shall process an opt-out preference signal as a valid request to opt out of sale/sharing for that browser or device, and, if known, the consumer.
- **Section 7025(b)** — If the business is unable to identify the consumer, the opt-out shall apply to the browser or device from which the signal was sent.
- **Section 7025(c)** — The business shall not require the consumer to provide additional information to opt out via a preference signal, unless necessary to verify the consumer's identity.
- **Section 7025(d)** — If a conflict exists between the opt-out preference signal and a consumer's business-specific privacy setting, the business shall process the opt-out preference signal but may notify the consumer of the conflict and provide the consumer the opportunity to confirm their intention.

### Global Privacy Control (GPC) Specification

GPC is an HTTP header and JavaScript API signal that communicates a user's privacy preferences:
- **HTTP header**: `Sec-GPC: 1`
- **JavaScript API**: `navigator.globalPrivacyControl === true`
- **DNT header**: GPC is distinct from the deprecated Do Not Track (DNT) header. GPC has legal effect under CPRA and Colorado Privacy Act; DNT does not.

## Technical Implementation

### Step 1: Detect the GPC Signal

#### Server-Side Detection

Check for the GPC HTTP header on every incoming request:

```
HTTP Header: Sec-GPC: 1
```

If the header is present and its value is `1`, the user has activated GPC.

#### Client-Side Detection (JavaScript)

For single-page applications or client-side consent management:

```javascript
if (navigator.globalPrivacyControl === true) {
    // GPC signal detected — treat as opt-out of sale/sharing
}
```

### Step 2: Map GPC Signal to Consumer

| Scenario | Action |
|----------|--------|
| Consumer is logged in (authenticated) | Apply opt-out to the consumer's account across all devices |
| Consumer is not logged in but has cookies | Apply opt-out to the browser/device |
| Consumer is anonymous (no identification) | Apply opt-out to the current browsing session and device |

### Step 3: Automated Honoring

When a GPC signal is detected, the following actions must be executed automatically:

1. **Suppress third-party tracking scripts**: Do not load advertising pixels, third-party analytics trackers, or cross-site tracking scripts.
2. **Disable advertising cookies**: Do not set or read cookies used for targeted advertising or cross-context behavioral advertising.
3. **Exclude from data sharing**: Do not include the user's data in any data-sharing arrangements with third parties for advertising or monetisation purposes.
4. **Exclude from sale**: Do not sell the user's personal information to any third party.
5. **Update consent management platform**: Set the user's sale/sharing preference to "opted-out" in the CMP.

### Step 4: Consent Management Platform (CMP) Integration

The CMP must be configured to:

1. **Detect GPC on page load**: Before any third-party scripts are loaded.
2. **Suppress consent banner sale/sharing options**: If GPC is detected, automatically set the sale/sharing toggle to "opted-out" and suppress any request for consent to sell/share.
3. **Allow explicit re-consent**: If the consumer explicitly chooses to opt back in through the business's privacy settings, this explicit choice overrides the GPC signal for that business only.
4. **Log the signal**: Record the GPC signal detection for compliance audit purposes.

### Step 5: Cross-Device Consistency

| Consumer Status | Cross-Device Behaviour |
|----------------|----------------------|
| Authenticated (logged-in account) | GPC signal from one device triggers account-level opt-out across all devices |
| Unauthenticated | GPC signal applies only to the device/browser from which it was sent |
| Consumer later logs in from GPC-enabled device | Account-level opt-out is applied retroactively |

### Step 6: Conflict Resolution

When a conflict exists between the GPC signal and the consumer's explicit business-specific setting:

```
[GPC Signal Detected: Opt-Out]
         │
         ▼
[Does consumer have an explicit business-specific setting?]
   │
   ├── No explicit setting ──► Honor GPC signal (opt-out)
   │
   ├── Explicit opt-in to sale/sharing ──► [Conflict]
   │     └── Honor GPC signal (opt-out applies)
   │         Optionally: display notification
   │         "Your browser is sending a Global Privacy Control signal.
   │          We have applied this as an opt-out of sale/sharing.
   │          You previously opted in to sale/sharing on this site.
   │          If you wish to maintain your opt-in, please confirm
   │          in your privacy settings."
   │
   └── Explicit opt-out ──► No conflict (both agree on opt-out)
```

### Step 7: Documentation and Audit

1. Log every GPC signal detection with timestamp, IP hash, device identifier, and authenticated status.
2. Log every opt-out action taken in response to a GPC signal.
3. Maintain records for 24 months per CCPA regulation requirements.
4. Include GPC signal handling in quarterly privacy compliance audits.
5. Test GPC detection quarterly using browsers with GPC enabled (Firefox, Brave, DuckDuckGo).

## Monitoring and Testing

### Monthly Verification Checklist

- [ ] GPC header detection confirmed operational (test with Sec-GPC: 1)
- [ ] JavaScript API detection confirmed operational (test with navigator.globalPrivacyControl)
- [ ] Third-party tracking scripts are suppressed when GPC is detected
- [ ] Advertising cookies are not set when GPC is detected
- [ ] CMP correctly reflects GPC opt-out status
- [ ] Cross-device consistency confirmed for authenticated users
- [ ] Conflict resolution functioning as designed
- [ ] Audit logs recording GPC detections
