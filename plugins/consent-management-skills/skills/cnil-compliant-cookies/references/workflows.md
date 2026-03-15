# Workflows — Implementing CNIL-Compliant Cookies

## Workflow 1: Cookie Banner Display and Interaction

```
START: User visits CloudVault SaaS Inc. website (cloudvault-saas.eu)
  │
  ├─► Step 1: Check for existing consent
  │     ├─ Look for cv_consent cookie
  │     ├─ If exists and < 180 days old: respect stored preferences, no banner
  │     ├─ If exists and >= 180 days old: re-display banner (6-month reconsent)
  │     └─ If not exists: display consent banner
  │
  ├─► Step 2: Display CNIL-compliant consent banner
  │     ├─ Banner appears as overlay (not blocking content per no-cookie-wall rule)
  │     ├─ Layer 1:
  │     │   ├─ Brief description of cookie use
  │     │   ├─ [Accept All] button — 200x44px, blue, bold
  │     │   ├─ [Refuse All] button — 200x44px, blue, bold (same treatment)
  │     │   └─ [Manage Preferences] text link
  │     │
  │     └─ Layer 2 (if "Manage Preferences" clicked):
  │           ├─ Per-purpose toggles (all OFF by default):
  │           │   ├─ Audience Measurement (analytics)
  │           │   ├─ Advertising and Targeting
  │           │   └─ Social Media Sharing
  │           ├─ Essential Cookies section (always on, not toggleable):
  │           │   ├─ Session Management
  │           │   ├─ Security (CSRF)
  │           │   ├─ Load Balancing
  │           │   └─ Language Preference
  │           ├─ Third parties listed by name per purpose
  │           └─ [Accept Selected] [Refuse All] buttons
  │
  ├─► Step 3: Process user choice
  │     │
  │     ├─► "Accept All" clicked:
  │     │     ├─ Set cv_consent cookie: {accepted: all, timestamp: ISO8601, version: hash}
  │     │     ├─ Initialize all cookie categories
  │     │     ├─ Record consent in backend
  │     │     └─ Close banner
  │     │
  │     ├─► "Refuse All" clicked:
  │     │     ├─ Set cv_consent cookie: {accepted: none, timestamp: ISO8601, version: hash}
  │     │     ├─ Load only essential cookies
  │     │     ├─ Record refusal in backend
  │     │     └─ Close banner
  │     │
  │     └─► "Accept Selected" (from manage):
  │           ├─ Set cv_consent cookie with per-purpose selections
  │           ├─ Initialize selected categories only
  │           ├─ Record per-purpose decisions in backend
  │           └─ Close banner
  │
  └─► Step 4: Ongoing behavior
        ├─ No tracking scripts loaded before consent choice
        ├─ Essential cookies only until user makes a choice
        ├─ Banner does not reappear until 180 days
        └─ Preferences accessible via footer "Cookie Settings" link
```

## Workflow 2: Six-Month Reconsent Cycle

```
TRIGGER: User returns to site after 180+ days since last consent
  │
  ├─► Step 1: Detect expired consent
  │     ├─ Read cv_consent cookie
  │     ├─ Parse timestamp
  │     └─ If (current_date - consent_date) > 180 days: reconsent needed
  │
  ├─► Step 2: Re-display consent banner
  │     ├─ Same format as initial consent
  │     ├─ Pre-fill with previous choices as reference (but do NOT pre-select)
  │     └─ User makes fresh decision
  │
  ├─► Step 3: Process new consent
  │     ├─ Replace old consent cookie with new one
  │     ├─ Update consent records in backend
  │     └─ Apply new preferences immediately
  │
  └─► Step 4: If user previously accepted and now refuses
        ├─ Stop non-essential cookie processing immediately
        ├─ Delete non-essential cookies from browser
        └─ Record the change for audit trail
```

## Workflow 3: Essential Cookie Documentation

```
TRIGGER: Annual review of essential cookies list
  │
  ├─► Step 1: Inventory all cookies set by cloudvault-saas.eu
  │     ├─ First-party cookies (set by our domain)
  │     ├─ Third-party cookies (set by external domains)
  │     └─ For each: name, domain, purpose, expiry, data stored
  │
  ├─► Step 2: Classify each cookie
  │     ├─ Essential (exempt from consent per CNIL Section 3):
  │     │   ├─ cv_session: session management
  │     │   ├─ cv_csrf: CSRF protection
  │     │   ├─ cv_lb: load balancer affinity
  │     │   └─ cv_lang: language preference
  │     │
  │     └─ Non-essential (consent required):
  │           ├─ _ga, _gid: Google Analytics
  │           ├─ _fbp: Facebook Pixel
  │           └─ All advertising/tracking cookies
  │
  ├─► Step 3: Verify essential classification
  │     ├─ Each "essential" cookie must be strictly necessary
  │     ├─ Review against CNIL criteria:
  │     │   ├─ Would the site break without it? (session, CSRF)
  │     │   ├─ Did the user explicitly request the functionality? (language)
  │     │   └─ Is it purely for communication transmission? (load balancing)
  │     └─ DPO sign-off on essential classification
  │
  └─► Step 4: Update cookie policy page
        ├─ List all cookies by category
        ├─ Specify purpose, duration, and first/third party
        └─ Publish at cloudvault-saas.eu/cookie-policy
```
