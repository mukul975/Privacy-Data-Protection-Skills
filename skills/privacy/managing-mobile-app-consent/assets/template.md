# Mobile App SDK Privacy Audit Report

## App Information

| Field | Value |
|-------|-------|
| **App Name** | CloudVault |
| **Bundle ID (iOS)** | eu.cloudvault-saas.app |
| **Package Name (Android)** | eu.cloudvault_saas.app |
| **App Version** | 4.2.1 |
| **Audit Date** | 2026-03-14 |
| **Auditor** | Marta Kowalski, DPO |

## SDK Inventory

| SDK | Version | Vendor | Purpose | Consent Purpose | ATT Required |
|-----|---------|--------|---------|-----------------|--------------|
| Firebase Analytics | 10.21.0 | Google LLC | Usage analytics | pur_analytics_001 | No |
| Crashlytics | 10.21.0 | Google LLC | Crash reporting | pur_crash_003 | No |
| AppsFlyer | 6.14.0 | AppsFlyer Ltd. | Attribution | pur_advertising_002 | Yes (iOS) |

## Consent Gating Verification

| SDK | Consent Gate | Pre-Consent Network Traffic | Post-Denial Network Traffic | Status |
|-----|-------------|---------------------------|----------------------------|--------|
| Firebase Analytics | Yes — `setAnalyticsCollectionEnabled(false)` until consent | None detected | None detected | PASS |
| Crashlytics | Yes — `setCrashlyticsCollectionEnabled(false)` until consent | None detected | None detected | PASS |
| AppsFlyer | Yes — `start()` not called until consent + ATT | None detected | None detected | PASS |

## Platform-Specific Compliance

### iOS

| Requirement | Status |
|------------|--------|
| ATT dialog displayed before IDFA access | PASS |
| NSUserTrackingUsageDescription in Info.plist | PASS |
| IDFA returns zeros when ATT denied | PASS |
| SKAdNetwork used as fallback for attribution | PASS |
| Privacy Nutrition Label accurate | PASS |

### Android

| Requirement | Status |
|------------|--------|
| AD_ID permission declared in manifest | PASS |
| GAID not accessed without consent | PASS |
| Data Safety section accurate | PASS |
| No GAID collection for child accounts | PASS |

## Sign-Off

| Role | Name | Date |
|------|------|------|
| DPO | Marta Kowalski | 2026-03-14 |
| Mobile Lead | Aoife Brennan | 2026-03-14 |
