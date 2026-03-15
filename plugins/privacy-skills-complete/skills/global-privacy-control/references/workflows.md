# Workflows — Implementing Global Privacy Control

## Workflow 1: Client-Side GPC Detection and Response

```
START: User's browser loads CloudVault SaaS Inc. web application
  │
  ├─► Step 1: Privacy initialization script runs before any tracking code
  │     │
  │     ├─► Check navigator.globalPrivacyControl
  │     │     ├─ If true: Set window.__cloudvault_gpc = true
  │     │     └─ If false/undefined: Set window.__cloudvault_gpc = false
  │     │
  │     └─► If GPC detected:
  │           ├─ Block loading of third-party advertising scripts
  │           ├─ Block loading of cross-site tracking pixels
  │           ├─ Allow first-party analytics (not sale/sharing)
  │           └─ Set cookie: cv_gpc_detected=1; SameSite=Strict; Secure
  │
  ├─► Step 2: Cookie consent banner renders
  │     │
  │     ├─► If GPC detected:
  │     │     ├─ Pre-select "Opt Out of Sale/Sharing" toggle
  │     │     ├─ Display notice: "We detected your Global Privacy Control
  │     │     │   signal and have applied your opt-out preference."
  │     │     └─ User can still manually adjust other purposes
  │     │
  │     └─► If GPC not detected:
  │           └─ Display standard consent banner with all purposes unticked
  │
  └─► Step 3: Log GPC detection event to consent system
        ├─ Event type: gpc_signal_detected
        ├─ Timestamp: ISO 8601 UTC
        ├─ User agent: navigator.userAgent
        └─ Associated user ID (if authenticated)
```

## Workflow 2: Server-Side GPC Processing

```
START: HTTP request received by CloudVault SaaS Inc. server
  │
  ├─► Step 1: Middleware inspects request headers
  │     │
  │     ├─► Check for Sec-GPC header
  │     │     ├─ If Sec-GPC: 1 → Set request context: gpc_opt_out = true
  │     │     └─ If absent → Set request context: gpc_opt_out = false
  │     │
  │     └─► Add Sec-GPC echo in response headers (transparency)
  │
  ├─► Step 2: If gpc_opt_out = true AND request is authenticated
  │     │
  │     ├─► Query consent database for this user
  │     │
  │     ├─► Check if user has existing opt-in for sale/sharing purposes
  │     │     │
  │     │     ├─► If user opted in manually:
  │     │     │     ├─ GPC takes precedence (per AG Reg 11 CCR 7025)
  │     │     │     ├─ Update consent record: withdraw pur_benchmarking_003
  │     │     │     ├─ Update consent record: withdraw pur_advertising_004
  │     │     │     └─ Queue notification to user about conflict resolution
  │     │     │
  │     │     └─► If user has no prior opt-in:
  │     │           └─ Record GPC-based opt-out in consent database
  │     │
  │     └─► Trigger downstream propagation for affected purposes
  │
  ├─► Step 3: Apply opt-out to request processing
  │     ├─ Do not include user data in third-party data feeds
  │     ├─ Do not fire cross-site tracking events
  │     ├─ Suppress targeted advertising parameters
  │     └─ Allow first-party service functionality
  │
  └─► Step 4: Log GPC processing event
        ├─ Timestamp, user ID, IP address, user agent
        ├─ Purposes affected
        ├─ Actions taken (consent records updated, systems notified)
        └─ Conflict resolution (if applicable)
```

## Workflow 3: GPC Compliance Verification Testing

```
TRIGGER: Pre-deployment QA or quarterly compliance check
  │
  ├─► Step 1: Prepare test environment
  │     ├─ Configure browser with GPC enabled (Brave, DuckDuckGo, or OptMeowt extension)
  │     ├─ Configure browser without GPC for control comparison
  │     └─ Set up network traffic monitoring (browser DevTools or proxy)
  │
  ├─► Step 2: Test client-side detection
  │     ├─ Load application with GPC-enabled browser
  │     ├─ Verify Sec-GPC: 1 header in outgoing requests
  │     ├─ Verify navigator.globalPrivacyControl === true in console
  │     ├─ Verify third-party tracking scripts NOT loaded
  │     ├─ Verify consent banner reflects GPC opt-out
  │     └─ Compare network requests against non-GPC browser (control)
  │
  ├─► Step 3: Test server-side processing
  │     ├─ Send authenticated request with Sec-GPC: 1 header
  │     ├─ Verify consent database updated with GPC opt-out
  │     ├─ Verify downstream systems notified
  │     ├─ Verify response includes Sec-GPC echo header
  │     └─ Verify server logs capture GPC event
  │
  ├─► Step 4: Test conflict resolution
  │     ├─ Create test user with manual opt-in for sharing
  │     ├─ Send request with Sec-GPC: 1 header for that user
  │     ├─ Verify GPC overrides manual opt-in
  │     └─ Verify user notification queued about conflict
  │
  └─► Step 5: Generate compliance verification report
        ├─ Test results for each verification step
        ├─ Screenshots of consent banner with GPC detected
        ├─ Network traffic logs showing blocked/allowed requests
        └─ Submit to DPO for review
```
