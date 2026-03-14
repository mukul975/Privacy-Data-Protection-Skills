---
name: global-privacy-control
description: >-
  Implementation guide for Global Privacy Control (GPC) automated opt-out signal
  per CPRA Section 1798.135(e). Covers Sec-GPC HTTP header detection, JavaScript
  navigator.globalPrivacyControl API, and state-specific requirements for CA, CO,
  CT, MT, TX, and OR. Includes server-side detection code and compliance mapping.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: consent-management
  tags: "global-privacy-control, gpc, cpra, opt-out-signal, browser-privacy"
---

# Implementing Global Privacy Control (GPC)

## Overview

Global Privacy Control (GPC) is a browser-level signal that communicates a user's privacy preference to opt out of the sale or sharing of their personal information. The GPC specification defines both an HTTP header (`Sec-GPC: 1`) and a JavaScript API (`navigator.globalPrivacyControl`) for transmitting this signal.

Under California Privacy Rights Act (CPRA) Section 1798.135(e), businesses must treat GPC signals as valid opt-out requests. The California Attorney General confirmed this enforcement position in the Sephora settlement (August 2022, $1.2 million fine), which was the first enforcement action involving GPC signals.

## Legal Requirements by State

### California — CPRA (effective January 1, 2023)

- **Section 1798.135(e)**: A business that collects consumers' personal information shall treat the consumer's use of an opt-out preference signal as a valid request to opt out of sale/sharing under Section 1798.120.
- **AG Regulation 11 CCR 7025(b)**: If a business collects personal information from consumers online, the business shall treat an opt-out preference signal as a valid request to opt-out of sale/sharing for that browser or device and any consumer profile associated with that browser or device.
- **Sephora Settlement (August 2022)**: California AG fined Sephora $1.2 million for failing to honor GPC signals, among other violations.

### Colorado — Colorado Privacy Act (CPA, effective July 1, 2024)

- **Section 6-1-1306(1)(a)(IV)(A)**: Consumers may exercise the right to opt out through an opt-out preference signal sent by a platform, technology, or mechanism on behalf of the consumer, to the extent technically feasible.
- **CPA Rules 4.6**: Controllers must recognize universal opt-out mechanisms by July 1, 2024.

### Connecticut — Connecticut Data Privacy Act (CTDPA, effective July 1, 2023)

- **Section 42-520(b)(5)**: Beginning January 1, 2025, controllers must recognize universal opt-out mechanisms for the sale of personal data and targeted advertising.

### Montana — Montana Consumer Data Privacy Act (effective October 1, 2024)

- **Section 30-14-2807**: Controllers must recognize opt-out preference signals as valid opt-out requests for the sale of personal data and targeted advertising.

### Texas — Texas Data Privacy and Security Act (TDPSA, effective July 1, 2024)

- **Section 541.055**: Controllers must allow consumers to opt out of the sale of personal data and targeted advertising. Universal opt-out mechanisms must be honored beginning January 1, 2025.

### Oregon — Oregon Consumer Privacy Act (effective July 1, 2024)

- **Section 646A.578**: Controllers shall provide a method by which consumers can opt out that includes recognition of opt-out preference signals.

## GPC Technical Specification

### HTTP Header Detection

The GPC signal is transmitted as an HTTP request header:

```
Sec-GPC: 1
```

This header is set by the browser (or browser extension) on every HTTP request when the user has enabled GPC. The header is absent (not set to 0) when GPC is not enabled.

### JavaScript API Detection

The GPC signal is also available via the JavaScript DOM API:

```javascript
// Check if GPC is supported and enabled
if (navigator.globalPrivacyControl === true) {
    // User has opted out — do not sell/share personal information
    // Do not load non-essential tracking scripts
    // Set internal opt-out flag for this user
}
```

Key considerations:
- `navigator.globalPrivacyControl` returns `true` when GPC is enabled
- `navigator.globalPrivacyControl` returns `false` or `undefined` when GPC is not enabled or not supported
- Check should occur before loading any tracking or advertising scripts

### Server-Side Detection (HTTP Header)

On the server side, check for the `Sec-GPC` header in incoming requests:

```
If Sec-GPC header is present AND equals "1":
    → Set opt-out flag for this session/user
    → Do not initiate sale or sharing of personal information
    → Do not load third-party tracking pixels
    → Log GPC signal receipt for compliance records
```

## Implementation Architecture at CloudVault SaaS Inc.

### Client-Side Detection

CloudVault SaaS Inc. checks GPC at two points:

1. **Page Load**: Before initializing any analytics or advertising SDKs, check `navigator.globalPrivacyControl`. If `true`, suppress non-essential tracking.

2. **Consent Banner Interaction**: If GPC is detected, pre-select the "Opt Out of Sale/Sharing" option in the cookie consent banner and display a notice: "We detected your Global Privacy Control signal. Your opt-out preference has been applied."

### Server-Side Processing

The CloudVault SaaS Inc. backend middleware:

1. Inspects every incoming HTTP request for the `Sec-GPC: 1` header.
2. If detected, sets a session-level flag `gpc_opt_out = true`.
3. If the request is associated with an authenticated user, propagates the opt-out to the user's consent record for applicable purposes (sale/sharing).
4. Returns a `Sec-GPC` response header echoing the signal (transparency).
5. Logs the GPC signal receipt with timestamp, user agent, and associated user ID (if authenticated).

### Mapping GPC to Internal Consent System

GPC is a binary signal (opt out of sale/sharing). CloudVault SaaS Inc. maps it to specific consent purposes:

| GPC Signal | Internal Purpose | Action |
|-----------|-----------------|--------|
| Sec-GPC: 1 | pur_benchmarking_003 (Third-party data sharing) | Withdraw consent / opt out |
| Sec-GPC: 1 | pur_advertising_004 (Targeted advertising) | Withdraw consent / opt out |
| Sec-GPC: 1 | pur_analytics_001 (Service improvement) | No change (internal use, not sale/sharing) |
| Sec-GPC: 1 | pur_marketing_002 (Product emails) | No change (direct marketing, not sale/sharing) |

### Conflict Resolution

When a user has manually opted in via the preference center but their browser sends GPC:

- **CPRA approach**: GPC takes precedence. Per AG regulation 11 CCR 7025(c), if a conflict exists between the opt-out preference signal and the consumer's participation in a financial incentive program, the business shall respect the opt-out preference signal but may notify the consumer of the conflict and give the consumer the choice to confirm their participation.
- **CloudVault SaaS Inc. policy**: Display a notification: "Your browser is sending a Global Privacy Control signal to opt out of data sharing. This overrides your previous opt-in. To continue sharing data for industry benchmarking, you can confirm your preference in Settings > Privacy."

## Compliance Verification

To verify GPC implementation:

1. Install a GPC-enabled browser or extension (Firefox with Enhanced Tracking Protection, DuckDuckGo browser, Brave browser, or the OptMeowt extension for Chrome)
2. Navigate to CloudVault SaaS Inc. application
3. Verify that `Sec-GPC: 1` header is sent in network requests
4. Confirm that tracking scripts are not loaded
5. Confirm that the consent banner reflects the opt-out preference
6. Verify server-side logs record the GPC signal
7. Confirm that authenticated users have their consent record updated

## Key Regulatory References

- CPRA Section 1798.135(e) — Opt-out preference signal requirement
- California AG Regulation 11 CCR 7025 — GPC implementation details
- GPC Specification (globalprivacycontrol.org) — Technical standard
- Colorado Privacy Act Section 6-1-1306(1)(a)(IV)(A) — Universal opt-out
- Connecticut CTDPA Section 42-520(b)(5) — Universal opt-out mechanism
- Montana MCDPA Section 30-14-2807 — Opt-out preference signals
- Texas TDPSA Section 541.055 — Opt-out methods
- Oregon OCPA Section 646A.578 — Opt-out preference signals
- Sephora Settlement (California AG, August 2022) — First GPC enforcement
