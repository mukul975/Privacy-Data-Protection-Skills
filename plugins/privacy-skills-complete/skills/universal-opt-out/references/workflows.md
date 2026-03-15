# Workflows — Universal Opt-Out Mechanism

## Workflow 1: End-to-End GPC Signal Processing

```
START: HTTP request arrives at Liberty Commerce Inc. servers
  │
  ├─► Step 1: Edge Proxy Detection
  │     ├─ Parse HTTP headers for Sec-GPC: 1
  │     ├─ Add internal metadata: X-GPC-Detected: true
  │     └─ Forward to application server
  │
  ├─► Step 2: Application Server Processing
  │     ├─ Read X-GPC-Detected header
  │     ├─ Check consumer authentication status
  │     ├─ Determine applicable state(s) based on:
  │     │     ├─ Account address (if authenticated)
  │     │     ├─ IP geolocation (supplementary)
  │     │     └─ Default: apply to all (high-water mark)
  │     └─ Set request context: suppress_sale = true, suppress_targeted_ads = true
  │
  ├─► Step 3: Tag Management Decision
  │     ├─ IF GPC detected:
  │     │     ├─ BLOCK: AdReach Network pixel
  │     │     ├─ BLOCK: Cross-context behavioral ad tags
  │     │     ├─ BLOCK: Retargeting pixels (TargetAds, BidStream)
  │     │     ├─ BLOCK: Social tracking widgets
  │     │     ├─ ALLOW: First-party analytics (under SP agreement)
  │     │     ├─ ALLOW: Essential cookies (session, cart, CSRF)
  │     │     └─ ALLOW: Contextual ads (non-behavioral)
  │     └─ IF GPC not detected:
  │           └─ Normal tag execution per CMP consent state
  │
  ├─► Step 4: Consumer Account Update
  │     ├─ IF authenticated:
  │     │     ├─ Set account flag: gpc_opt_out = true
  │     │     ├─ Set: sale_opt_out = true
  │     │     ├─ Set: targeted_advertising_opt_out = true
  │     │     └─ Override any prior opt-in (most recent preference)
  │     └─ IF unauthenticated:
  │           ├─ Apply to current session
  │           └─ Set session cookie: gpc_session_opt_out=1
  │
  ├─► Step 5: Server-Side Data Pipeline
  │     ├─ Suppress outbound data feeds to third-party ad partners
  │     ├─ Update real-time bidding (RTB) exclusion list
  │     └─ Exclude consumer from cross-context behavioral ad audiences
  │
  └─► Step 6: Compliance Logging
        ├─ Log: timestamp, session_id, consumer_id (if auth)
        ├─ Log: GPC signal value, source (header/JS)
        ├─ Log: tags blocked, flags set, account updated
        └─ Retain for 24 months
```

## Workflow 2: GPC Testing Protocol

```
TRIGGER: Pre-deployment or quarterly validation
  │
  ├─► Test 1: Signal Detection
  │     ├─ Browser: Use Brave or Firefox with GPC enabled
  │     ├─ Verify: Server logs show Sec-GPC: 1 header
  │     ├─ Verify: Client-side navigator.globalPrivacyControl === true
  │     └─ Result: PASS / FAIL
  │
  ├─► Test 2: Tag Suppression
  │     ├─ With GPC: Open browser dev tools Network tab
  │     ├─ Verify: No requests to ad network domains
  │     ├─ Without GPC: Verify ad network requests fire
  │     └─ Result: PASS / FAIL
  │
  ├─► Test 3: No Pop-Up
  │     ├─ Visit with GPC enabled
  │     ├─ Verify: No modal, pop-up, or interstitial appears
  │     ├─ Verify: Consent banner does not override GPC
  │     └─ Result: PASS / FAIL
  │
  ├─► Test 4: Authenticated Persistence
  │     ├─ Enable GPC, log in, browse
  │     ├─ Disable GPC, revisit while logged in
  │     ├─ Verify: Account-level opt-out persists
  │     └─ Result: PASS / FAIL
  │
  ├─► Test 5: Unauthenticated Session
  │     ├─ Enable GPC, browse without logging in
  │     ├─ Verify: Session-level opt-out applied
  │     ├─ Close browser, reopen without GPC
  │     ├─ Verify: No residual opt-out (session cleared)
  │     └─ Result: PASS / FAIL
  │
  ├─► Test 6: Conflict Resolution
  │     ├─ Log in, opt in to targeted ads in settings
  │     ├─ Enable GPC, visit website
  │     ├─ Verify: GPC overrides prior opt-in
  │     └─ Result: PASS / FAIL
  │
  └─► Generate Test Report
        ├─ Document all test results
        ├─ Screenshot evidence for each test
        └─ File remediation tickets for failures
```
