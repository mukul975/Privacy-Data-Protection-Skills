# Workflows — Implementing CNIL-Compliant Cookies

## Workflow 1: Cookie Consent Banner Display and Response

```
START: User visits cloudvault-saas.eu
  │
  ├─► Step 1: Check for existing consent cookie
  │     ├─ Read cv_consent_version cookie
  │     ├─ If present and not expired (< 6 months):
  │     │   ├─ Apply stored consent choices
  │     │   ├─ Load consented cookies/scripts only
  │     │   └─ Do NOT show banner
  │     └─ If absent or expired:
  │           ├─ Block ALL non-essential cookies/scripts
  │           └─ Display consent banner
  │
  ├─► Step 2: Display CNIL-compliant banner (first layer)
  │     ├─ Information: "CloudVault uses cookies to improve your experience."
  │     ├─ Link: "Learn more in our Cookie Policy"
  │     ├─ Three buttons with EQUAL prominence:
  │     │   ├─ [Accept All] — 160x44px, #2563EB, 16px Inter Bold
  │     │   ├─ [Reject All] — 160x44px, #2563EB, 16px Inter Bold
  │     │   └─ [Customize]  — 160x44px, #2563EB, 16px Inter Bold
  │     └─ Content remains accessible behind banner (no cookie wall)
  │
  ├─► Step 3: Handle user choice
  │     │
  │     ├─► [Accept All]:
  │     │     ├─ Set all cookie purposes to "granted"
  │     │     ├─ Load all cookie scripts
  │     │     ├─ Set cv_consent_version cookie (Max-Age: 15778800 = ~6 months)
  │     │     └─ Record consent in audit trail
  │     │
  │     ├─► [Reject All]:
  │     │     ├─ Set all non-essential purposes to "not_granted"
  │     │     ├─ Keep essential cookies only
  │     │     ├─ Set cv_consent_version cookie (same 6-month expiry)
  │     │     └─ Record refusal in audit trail
  │     │
  │     └─► [Customize]:
  │           ├─ Display second layer with per-purpose toggles:
  │           │   ├─ Essential Cookies [Always On, cannot toggle off]
  │           │   │   Listed: cv_session_id, cv_csrf_token, cv_consent_version, etc.
  │           │   ├─ Analytics Cookies [Toggle: OFF by default]
  │           │   │   Listed: Google Analytics (_ga, _gid)
  │           │   ├─ Advertising Cookies [Toggle: OFF by default]
  │           │   │   Listed: Facebook Pixel (_fbp), AppsFlyer (_af_*)
  │           │   └─ Functionality Cookies [Toggle: OFF by default]
  │           │       Listed: A/B testing (cv_ab_test)
  │           │
  │           ├─ Two buttons with equal prominence:
  │           │   ├─ [Save Preferences] — saves current toggle states
  │           │   └─ [Reject All] — sets all non-essential to off
  │           │
  │           └─ Record per-purpose decisions in audit trail
  │
  └─► Step 4: Apply consent decisions
        ├─ For each granted purpose: load corresponding scripts/cookies
        ├─ For each refused purpose: ensure no scripts load, no cookies set
        └─ Banner disappears after choice is made
```

## Workflow 2: Consent Renewal (6-Month Interval)

```
TRIGGER: cv_consent_version cookie expires (after ~6 months)
  │
  ├─► Step 1: On next page load, detect missing/expired consent cookie
  │
  ├─► Step 2: Block all non-essential cookies (same as first visit)
  │
  ├─► Step 3: Display consent banner (identical to first-visit banner)
  │     └─ Previous choices are NOT pre-selected (fresh consent)
  │
  ├─► Step 4: User makes new choice
  │     └─ Standard accept/reject/customize flow
  │
  └─► Step 5: Record new consent with new timestamp
```

## Workflow 3: Cookie Consent Withdrawal

```
TRIGGER: User clicks "Privacy Choices" link in footer or navigates to Settings > Privacy
  │
  ├─► Display current cookie consent state (per-purpose toggles)
  │     ├─ Analytics: ON/OFF
  │     ├─ Advertising: ON/OFF
  │     └─ Functionality: ON/OFF
  │
  ├─► User changes a toggle → processed immediately:
  │     ├─ If disabling: stop script, delete associated cookies
  │     ├─ If enabling: load script, set cookies
  │     └─ Update cv_consent_version cookie
  │
  └─► Record change in consent audit trail
```
