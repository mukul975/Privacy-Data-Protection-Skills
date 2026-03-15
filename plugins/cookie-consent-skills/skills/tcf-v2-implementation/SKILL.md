---
name: tcf-v2-implementation
description: >-
  Implementing the IAB Transparency and Consent Framework v2.2 for programmatic
  advertising consent management. Covers CMP registration, Global Vendor List
  integration, TC String encoding, publisher restrictions, and compliance validation.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: cookie-consent-compliance
  tags: "tcf, iab, consent-management-platform, tc-string, global-vendor-list"
---

# IAB TCF v2.2 Implementation

## Overview

The IAB Europe Transparency and Consent Framework (TCF) v2.2, released in May 2023 as an update to v2.0, provides a standardized mechanism for collecting, encoding, and distributing user consent signals across the programmatic advertising supply chain. Publishers, advertisers, and ad technology vendors use TCF to communicate consent status through the TC String — a compact, base64url-encoded data structure. TCF v2.2 introduced key changes including the removal of legitimate interest as a legal basis for cross-device targeting (Purpose 2 in part) and restrictions on certain vendor practices.

## TCF v2.2 Architecture

### Core Components

1. **Consent Management Platform (CMP)**: The user-facing interface that collects consent. Must be registered with IAB Europe and assigned a CMP ID.
2. **Global Vendor List (GVL)**: A centralized registry of ad technology vendors, maintained by IAB Europe, listing each vendor's declared purposes and legal bases.
3. **TC String**: The encoded consent signal transmitted through the ad supply chain.
4. **CMP API (__tcfapi)**: A JavaScript API that vendors call to read the current consent state.

### Implementation for Pinnacle E-Commerce Ltd

#### Step 1: CMP Registration

Register Pinnacle E-Commerce Ltd's CMP with IAB Europe:

| Registration Field | Value |
|-------------------|-------|
| CMP Name | Pinnacle Consent Manager |
| Publisher | Pinnacle E-Commerce Ltd |
| CMP ID | Assigned by IAB Europe upon registration (e.g., 432) |
| Supported TCF version | 2.2 |
| GVL version | Latest (auto-updated weekly) |
| CMP JavaScript URL | https://cmp.pinnacle-ecommerce.com/tcf-v2.js |

Registration requirements:
- Demonstrate CMP compliance with IAB TCF Policies
- Pass IAB Europe CMP validation testing
- Agree to the CMP Terms and Conditions
- Implement the `__tcfapi` stub before the full CMP loads

#### Step 2: Global Vendor List Integration

The GVL is published at `https://vendor-list.consensu.org/v3/vendor-list.json` and contains:

```json
{
  "gvlSpecificationVersion": 3,
  "vendorListVersion": 287,
  "tcfPolicyVersion": 4,
  "lastUpdated": "2026-03-01T12:00:00Z",
  "purposes": {
    "1": {
      "id": 1,
      "name": "Store and/or access information on a device",
      "description": "Cookies, device or similar online identifiers...",
      "illustrations": ["..."]
    }
  },
  "vendors": {
    "755": {
      "id": 755,
      "name": "Google Advertising Products",
      "purposes": [1, 3, 4],
      "legIntPurposes": [2, 7, 9, 10],
      "flexiblePurposes": [2, 7, 9, 10],
      "specialPurposes": [1, 2],
      "features": [1, 2],
      "specialFeatures": [],
      "policyUrl": "https://policies.google.com/privacy",
      "cookieMaxAgeSeconds": 63072000,
      "usesCookies": true,
      "usesNonCookieAccess": true
    }
  }
}
```

**GVL Management for Pinnacle E-Commerce Ltd:**

1. Cache the GVL locally with a maximum staleness of 24 hours
2. Display only vendors that Pinnacle E-Commerce Ltd actually uses (vendor subset)
3. Show vendor count in the consent banner: "We work with 47 advertising partners"
4. Provide a searchable vendor list in the detailed consent layer

**Pinnacle E-Commerce Ltd Vendor Subset:**

| Vendor ID | Vendor Name | Purposes | Legal Basis |
|-----------|------------|----------|-------------|
| 755 | Google Advertising Products | 1, 3, 4 | Consent |
| 91 | Criteo SA | 1, 2, 3, 4, 7 | Consent |
| 42 | Taboola Inc. | 1, 2, 3, 4, 5, 7 | Consent |
| 69 | OpenX Technologies | 1, 2, 3, 4, 7 | Consent |
| 253 | Meta Platforms, Inc. | 1, 2, 3, 4, 7, 10 | Consent |

#### Step 3: TCF v2.2 Purposes

The 11 TCF purposes and their mapping for Pinnacle E-Commerce Ltd:

| TCF Purpose | Name | Legal Basis at Pinnacle |
|-------------|------|------------------------|
| 1 | Store and/or access information on a device | Consent only |
| 2 | Select basic ads | Consent only |
| 3 | Create profiles for personalised advertising | Consent only |
| 4 | Use profiles to select personalised ads | Consent only |
| 5 | Create profiles to personalise content | Consent only |
| 6 | Use profiles to select personalised content | Consent only |
| 7 | Measure ad performance | Consent only |
| 8 | Measure content performance | Consent only |
| 9 | Understand audiences through statistics or combinations of data from different sources | Consent only |
| 10 | Develop and improve services | Consent only |
| 11 | Use limited data to select content | Consent only |

**Special Purposes** (always allowed, no consent required):
- SP1: Ensure security, prevent and detect fraud, and fix errors
- SP2: Deliver and present advertising and content

**Features** (declared, not consented to individually):
- F1: Match and combine data from other data sources
- F2: Link different devices
- F3: Receive and use automatically-sent device characteristics for identification

**Special Features** (require explicit consent):
- SF1: Use precise geolocation data
- SF2: Actively scan device characteristics for identification

#### Step 4: TC String Structure

The TC String is a base64url-encoded binary string containing:

**Core String Segments:**

| Field | Bits | Description |
|-------|------|-------------|
| Version | 6 | TCF version (value: 2) |
| Created | 36 | Deciseconds since 01/01/2020 00:00:00 UTC |
| LastUpdated | 36 | Deciseconds since 01/01/2020 00:00:00 UTC |
| CmpId | 12 | CMP ID (Pinnacle: 432) |
| CmpVersion | 12 | CMP version number |
| ConsentScreen | 6 | Screen number in CMP where consent was given |
| ConsentLanguage | 12 | ISO 639-1 language code |
| VendorListVersion | 12 | GVL version used |
| TcfPolicyVersion | 6 | TCF Policy version (value: 4) |
| IsServiceSpecific | 1 | 1 = publisher-specific TC String |
| UseNonStandardStacks | 1 | Whether non-IAB standard stacks are used |
| PurposeConsents | 24 | Bitfield for purpose consent (purposes 1-24) |
| PurposeLegitimateInterests | 24 | Bitfield for purpose LI |
| PurposeOneTreatment | 1 | 0 = purpose 1 was disclosed; 1 = not |
| PublisherCC | 12 | ISO 3166-1 alpha-2 publisher country code |

**Vendor Consent Section:**
Variable-length encoding of per-vendor consent using either a bitfield or range encoding, depending on which is more compact.

**Publisher Restrictions Section:**
Overrides vendor-declared legal bases at the publisher level.

#### Step 5: Publisher Restrictions

Pinnacle E-Commerce Ltd applies publisher restrictions to enforce consent-only for all purposes:

```json
{
  "publisherRestrictions": [
    {
      "purposeId": 2,
      "restrictionType": 1,
      "vendorIds": [91, 42, 69]
    },
    {
      "purposeId": 7,
      "restrictionType": 1,
      "vendorIds": [91, 42, 69, 253]
    },
    {
      "purposeId": 9,
      "restrictionType": 1,
      "vendorIds": [91, 42, 69]
    },
    {
      "purposeId": 10,
      "restrictionType": 1,
      "vendorIds": [91, 42, 69, 253]
    }
  ]
}
```

Restriction types:
- 0 = Purpose flatly not allowed by publisher
- 1 = Require consent (override legitimate interest)
- 2 = Require legitimate interest (override consent)
- 3 = Vendor requires both consent and LI to process

#### Step 6: CMP API Implementation

The `__tcfapi` must be available before any vendor scripts load:

**Stub Implementation (loads first):**
```javascript
(function() {
  var queue = [];
  var tcfapi = function(command, version, callback, parameter) {
    if (command === 'addEventListener') {
      queue.push({ command: command, callback: callback });
    } else {
      queue.push({ command: command, version: version, callback: callback, parameter: parameter });
    }
  };
  tcfapi.queue = queue;
  window.__tcfapi = tcfapi;
})();
```

**Supported Commands:**

| Command | Description |
|---------|-------------|
| getTCData | Returns the TC String and parsed consent data |
| ping | Returns CMP status and loading state |
| addEventListener | Registers a callback for consent changes |
| removeEventListener | Removes a registered callback |
| getInAppTCData | Returns TC data for in-app (mobile) contexts |

**getTCData Response:**
```json
{
  "tcString": "CPyXXYAPyXXYAAGABCENB4CgAP_AAH_AAAAAHfoBpDxkBSFCAGJoYtkgAAAGxwAAICACABAAoAAAABoAIAQAAAAQAAAgBAAAABIAIAIAAABAGEAAAAAAQAAAAQAAAEAAAAAAIQIAAAAAAiBAAAAAAAAAAAAAAABAAAAAAAAAAgAAAAAAAQAA",
  "tcfPolicyVersion": 4,
  "cmpId": 432,
  "cmpVersion": 1,
  "gdprApplies": true,
  "eventStatus": "useractioncomplete",
  "purpose": {
    "consents": { "1": true, "2": false, "3": false, "4": false, "7": true },
    "legitimateInterests": {}
  },
  "vendor": {
    "consents": { "755": true, "91": false, "42": false },
    "legitimateInterests": {}
  },
  "publisher": {
    "restrictions": { "2": { "91": 1, "42": 1, "69": 1 } }
  }
}
```

## TCF v2.2 Compliance Validation

### Validation Checklist

| Requirement | Verification Method |
|-------------|-------------------|
| CMP registered with IAB Europe | Check CMP ID in IAB registry |
| GVL version current (within 7 days) | Parse TC String VendorListVersion field |
| TC String decodes correctly | Use IAB reference decoder |
| Purpose 1 consent collected before device storage | Verify no cookies set pre-consent |
| Publisher restrictions encoded | Decode TC String restrictions segment |
| `__tcfapi` responds to ping | Call `__tcfapi('ping', 2, callback)` |
| Consent UI shows all declared purposes | Compare UI with GVL purposes |
| Vendor list matches GVL subset | Compare displayed vendors with GVL |
| TC String transmitted in bid requests | Inspect OpenRTB `consent` field |

## Key Legal and Technical References

- **IAB Europe TCF v2.2 Technical Specification (May 2023)** — TC String format, CMP API, GVL structure
- **IAB Europe TCF Policies v4** — Rules governing CMPs and vendors
- **IAB Europe CMP Validator Tool** — Automated TC String validation
- **ePrivacy Directive 2002/58/EC, Article 5(3)** — Legal basis for TCF Purpose 1
- **CJEU Case C-673/17 (Planet49)** — Active consent requirements
- **Belgian DPA Decision 21/2022 (IAB Europe)** — Found IAB Europe a data controller for TC String; TCF must ensure valid GDPR consent
- **GDPR Article 4(11)** — Consent definition applicable to TCF consent signals
