# Workflows — Managing Mobile App Consent

## Workflow 1: iOS First Launch Consent + ATT

```
START: User opens CloudVault iOS app for the first time
  │
  ├─► Step 1: Display privacy setup screen
  │     ├─ Brief, clear summary of data practices
  │     └─ [Set Up Privacy Preferences] button
  │
  ├─► Step 2: In-app consent flow (per-purpose toggles)
  │     ├─ Analytics: OFF by default
  │     ├─ Advertising Measurement: OFF by default
  │     ├─ Crash Reporting: OFF by default
  │     └─ [Save Preferences] button
  │
  ├─► Step 3: Record consent decisions
  │     ├─ Standard consent record per purpose
  │     └─ Platform metadata: iOS version, app version, device model
  │
  ├─► Step 4: If advertising consent granted
  │     ├─ Display pre-permission explanation screen
  │     ├─ [Continue] → trigger ATTrackingManager.requestTrackingAuthorization()
  │     ├─ System ATT dialog appears
  │     │   "CloudVault would like permission to track your activity
  │     │    across other companies' apps and websites"
  │     │   [Ask App Not to Track] [Allow]
  │     │
  │     ├─ If .authorized: enable IDFA, initialize attribution SDK
  │     └─ If .denied: use SKAdNetwork for attribution, no IDFA
  │
  ├─► Step 5: Initialize consented SDKs only
  │     ├─ Analytics consented? → FirebaseAnalytics.setAnalyticsCollectionEnabled(true)
  │     ├─ Crash consented? → Crashlytics.setCrashlyticsCollectionEnabled(true)
  │     └─ Advertising consented + ATT authorized? → AppsFlyer.start()
  │
  └─► Step 6: Proceed to main app
```

## Workflow 2: In-App Privacy Settings (Withdrawal)

```
TRIGGER: User navigates to Settings > Privacy within the app
  │
  ├─► Display current consent state per purpose (toggles)
  │
  ├─► User changes a toggle (e.g., Analytics ON → OFF)
  │     ├─ Record withdrawal in consent system
  │     ├─ Disable SDK: FirebaseAnalytics.setAnalyticsCollectionEnabled(false)
  │     ├─ Confirmation: "Analytics disabled. Changes take effect immediately."
  │     └─ Note: some SDKs may require app restart to fully stop collection
  │
  ├─► For advertising toggle:
  │     ├─ If turning OFF: disable attribution SDK, stop IDFA access
  │     ├─ Note to user: "To also reset your advertising identifier,
  │     │   go to iOS Settings > Privacy & Security > Tracking"
  │     └─ Record withdrawal in consent system
  │
  └─► "View Consent History" link → shows all consent decisions with timestamps
```

## Workflow 3: SDK Consent Audit

```
TRIGGER: App update release or quarterly privacy audit
  │
  ├─► Step 1: Inventory all SDKs in the app
  │     ├─ List each SDK, version, and declared purpose
  │     ├─ Cross-reference with App Store Privacy Nutrition Label
  │     └─ Cross-reference with Google Play Data Safety section
  │
  ├─► Step 2: Verify consent gating
  │     ├─ For each non-essential SDK:
  │     │   ├─ Is it initialized before consent? → FAIL
  │     │   ├─ Does it respect consent withdrawal? → PASS/FAIL
  │     │   └─ Does it collect data beyond declared purpose? → PASS/FAIL
  │     └─ Network traffic analysis: verify no tracking requests before consent
  │
  ├─► Step 3: Verify privacy labels accuracy
  │     ├─ App Store Privacy Nutrition Label matches actual collection
  │     └─ Google Play Data Safety section matches actual collection
  │
  └─► Step 4: Report and remediate
```
