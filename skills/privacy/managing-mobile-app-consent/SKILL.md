---
name: managing-mobile-app-consent
description: >-
  Guide for mobile-specific consent management covering Apple ATT framework for iOS,
  Android permission model, in-app consent flows, SDK consent propagation to third-party
  libraries, and IDFA/GAID handling. Addresses platform-specific requirements alongside
  GDPR and ePrivacy compliance for mobile applications.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: consent-management
  tags: "mobile-consent, att-framework, android-permissions, idfa, sdk-consent"
---

# Managing Mobile App Consent

## Overview

Mobile applications present unique consent challenges: platform-level permission systems (Apple ATT, Android runtime permissions), advertising identifiers (IDFA/GAID), SDK-level data collection by third-party libraries, and limited screen real estate for consent interfaces. Compliance requires coordination between GDPR/ePrivacy requirements and platform-specific privacy frameworks.

## Apple App Tracking Transparency (ATT) Framework

### Requirements (iOS 14.5+, enforced April 2021)

Apple's ATT framework requires apps to request user permission before tracking across apps and websites owned by other companies. Key aspects:

- **NSUserTrackingUsageDescription**: Apps must include a purpose string in Info.plist explaining why tracking is needed.
- **ATTrackingManager.requestTrackingAuthorization()**: Must be called before accessing IDFA or performing tracking.
- **IDFA Access**: The Identifier for Advertisers (IDFA) returns all zeros unless the user grants ATT permission.
- **Tracking Definition**: Apple defines "tracking" as linking user/device data from your app with data from other companies' apps/websites for advertising or sharing with data brokers.

### CloudVault SaaS Inc. ATT Implementation

**Purpose String (NSUserTrackingUsageDescription):**
"CloudVault uses this identifier to measure the effectiveness of our advertising campaigns and provide relevant ads. You can change this in Settings at any time."

**Pre-Permission Prompt (shown before ATT dialog):**
CloudVault SaaS Inc. displays a custom pre-permission screen explaining the value exchange before triggering the system ATT dialog:

"Help us improve CloudVault by allowing measurement of our advertising. This helps us understand which ads brought you here and improve our marketing spend. Your data is never sold. You can change this choice in iOS Settings at any time."

[Continue] → triggers ATTrackingManager.requestTrackingAuthorization()

### ATT States and Handling

| ATT Status | Meaning | CloudVault Action |
|-----------|---------|------------------|
| .notDetermined | User hasn't been asked yet | Show pre-permission screen, then request |
| .authorized | User allowed tracking | Enable IDFA access, attribution SDKs |
| .denied | User denied tracking | Disable IDFA, use SKAdNetwork for attribution |
| .restricted | Tracking restricted by parental controls/MDM | Do not request, use SKAdNetwork |

## Android Permission Model and Privacy Changes

### Android 13+ (API 33) Ad ID Changes

- **AD_ID Permission**: Apps must declare `com.google.android.gms.permission.AD_ID` in AndroidManifest.xml to access Google Advertising ID (GAID).
- **Google Play Requirements**: Apps targeting children must not access GAID.
- **User Reset**: Users can reset or delete their GAID in Android Settings.

### Android Privacy Sandbox (In Development)

Google's Privacy Sandbox for Android introduces:
- **Topics API**: Returns coarse-grained interest topics (replaces FLoC for mobile)
- **Attribution Reporting API**: Privacy-preserving ad attribution (similar to SKAdNetwork)
- **FLEDGE**: On-device ad auctions without cross-app tracking

### CloudVault SaaS Inc. Android Implementation

```xml
<!-- AndroidManifest.xml -->
<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>
```

GAID is only accessed if the user has granted consent for advertising purposes through the in-app consent flow. If consent is not granted, GAID is not read.

## In-App Consent Flow Design

### First Launch Consent

```
App First Launch
  │
  ├─► Step 1: Welcome screen with privacy summary
  │     "Welcome to CloudVault. Before you get started,
  │      let's set up your privacy preferences."
  │     [Set Up Privacy]
  │
  ├─► Step 2: Layered consent screen
  │     ├─ Purpose 1: Analytics [Toggle, OFF by default]
  │     │   "Help us improve CloudVault by sharing anonymous usage data"
  │     │   [Learn More] → detailed Art. 13 information
  │     │
  │     ├─ Purpose 2: Advertising Measurement [Toggle, OFF by default]
  │     │   "Measure which ads brought you to CloudVault"
  │     │   [Learn More] → detailed information + ATT context
  │     │
  │     ├─ Purpose 3: Crash Reporting [Toggle, OFF by default]
  │     │   "Share crash reports to help us fix bugs faster"
  │     │   [Learn More] → data types, retention
  │     │
  │     └─ "You can change these at any time in Settings > Privacy"
  │
  ├─► Step 3: Record consent decisions
  │     ├─ Per-purpose consent records (standard fields)
  │     ├─ Platform: iOS/Android
  │     ├─ OS version, app version, device model
  │     └─ SDK consent propagation (see below)
  │
  ├─► Step 4: Platform-specific follow-up
  │     ├─ iOS: If advertising consent granted → trigger ATT dialog
  │     └─ Android: If advertising consent granted → access GAID
  │
  └─► Step 5: Proceed to app
        └─ SDKs initialized based on consent state
```

## SDK Consent Propagation

Third-party SDKs in the CloudVault mobile app must respect user consent:

| SDK | Purpose | Data Collected | Consent Required | Propagation Method |
|-----|---------|---------------|-----------------|-------------------|
| Firebase Analytics | Usage analytics | Events, screen views, device info | pur_analytics_001 | `FirebaseAnalytics.setAnalyticsCollectionEnabled(granted)` |
| Crashlytics | Crash reporting | Stack traces, device state | pur_crash_003 | `FirebaseCrashlytics.setCrashlyticsCollectionEnabled(granted)` |
| AppsFlyer | Attribution | IDFA/GAID, install referrer | pur_advertising_002 | `AppsFlyerLib.start()` only if consented |
| Google AdMob | Advertising | IDFA/GAID, device info | pur_advertising_002 | `MobileAds.setRequestConfiguration()` with consent |

### SDK Initialization Pattern

SDKs must not be initialized before consent is obtained. CloudVault SaaS Inc. implements a "consent gate":

1. App launches → load only essential SDKs (no tracking)
2. Consent flow completes → read consent state
3. For each SDK: initialize only if corresponding purpose is consented
4. If consent is later withdrawn: disable SDK data collection (where SDK API supports it) or defer to next app restart

## IDFA and GAID Handling

| Identifier | Platform | When to Access | When NOT to Access |
|-----------|----------|---------------|-------------------|
| IDFA | iOS | ATT status = .authorized AND pur_advertising_002 consented | ATT denied/restricted OR advertising consent not granted |
| GAID | Android | pur_advertising_002 consented AND AD_ID permission declared | Advertising consent not granted OR app targets children |

## Key Regulatory References

- GDPR Article 5(3) via ePrivacy Directive — Consent for device storage access
- GDPR Article 7 — Conditions for consent (apply to in-app consent)
- Apple ATT Framework Documentation — App Tracking Transparency requirements
- Apple App Store Review Guideline 5.1.2 — Data Use and Sharing
- Google Play Developer Policy — Advertising ID and User Data
- CNIL Mobile Privacy Guidelines (2023) — Mobile-specific consent requirements
- EDPB Guidelines 05/2020 — Consent in mobile context
