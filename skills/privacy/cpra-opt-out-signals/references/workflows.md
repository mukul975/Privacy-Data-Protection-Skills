# CPRA Opt-Out Preference Signal Workflows

## Workflow 1: GPC Signal Detection and Processing

```
[HTTP Request Received]
         │
         ▼
[Check for Sec-GPC Header]
   │
   ├── Sec-GPC: 1 ──► [GPC Signal Detected]
   │                         │
   │                         ▼
   │                   [Consumer Authenticated?]
   │                     ├── Yes ──► Apply account-level opt-out
   │                     │            across all devices
   │                     └── No ──► Apply device/browser-level opt-out
   │                         │
   │                         ▼
   │                   [Execute Automated Honoring]
   │                     - Suppress third-party tracking
   │                     - Block advertising cookies
   │                     - Exclude from data sharing
   │                     - Update CMP status
   │                     - Log detection
   │
   └── No GPC Header ──► [Check navigator.globalPrivacyControl (client-side)]
         │
         ├── true ──► Same as above
         └── false/undefined ──► Process normally
                                  (absence ≠ consent)
```

## Workflow 2: CMP Integration

```
[Page Load]
         │
         ▼
[Detect GPC Signal (before loading any third-party scripts)]
   │
   ├── GPC Detected
   │     └── Set CMP sale_sharing_consent = OPTED_OUT
   │         Suppress consent banner sale/sharing options
   │         Load only essential scripts
   │         Display opt-out confirmation (optional)
   │
   └── No GPC Signal
         └── Display standard consent banner
             Process according to consumer's explicit choice
```

## Workflow 3: Conflict Resolution

```
[GPC Signal: OPT-OUT]
   +
[Business-Specific Setting: OPT-IN]
         │
         ▼
[CONFLICT DETECTED]
         │
         ▼
[Apply GPC Signal (opt-out takes precedence)]
         │
         ▼
[Optionally Notify Consumer]
   "Your browser is sending a privacy signal.
    We have applied this as an opt-out.
    You may confirm your preference in your privacy settings."
         │
         ▼
[Consumer Explicitly Confirms Opt-In?]
   ├── Yes ──► Override GPC for this business only
   │            Log explicit confirmation
   └── No ──► Maintain opt-out (GPC honored)
```

## Workflow 4: Quarterly Testing Protocol

```
[Quarterly GPC Compliance Test]
         │
         ▼
[Test 1: Server-Side Detection]
   - Send request with Sec-GPC: 1 header
   - Verify tracking scripts not loaded in response
   - Verify no advertising cookies set
         │
         ▼
[Test 2: Client-Side Detection]
   - Open site in GPC-enabled browser (Brave/Firefox)
   - Verify navigator.globalPrivacyControl = true detected
   - Verify CMP shows opt-out status
         │
         ▼
[Test 3: Cross-Device Consistency]
   - Log in from GPC-enabled browser
   - Verify account-level opt-out applied
   - Log in from non-GPC browser on different device
   - Verify account opt-out status persists
         │
         ▼
[Test 4: Audit Log Verification]
   - Verify GPC detections are logged
   - Verify opt-out actions are recorded
   - Verify logs include timestamp, device, auth status
         │
         ▼
[Generate Test Report + Remediation Actions]
```
