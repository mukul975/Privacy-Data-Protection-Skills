# Workflows — Implementing Consent Withdrawal

## Workflow 1: Standard Preference Center Withdrawal

```
START: User navigates to Settings > Privacy > Manage Consent
  │
  ├─► Display current consent state for all purposes
  │
  ├─► User clicks toggle for "Product Update Emails" (ON → OFF)
  │
  ├─► Confirmation dialog:
  │     "Withdraw consent for Product Update Emails?"
  │     "You will stop receiving emails about new CloudVault features."
  │     "You can re-enable this at any time."
  │     [Cancel] [Withdraw]
  │
  ├─► User clicks [Withdraw]
  │
  ├─► API: PUT /api/v1/consent/preferences/usr_7f3a9b2e
  │     Body: { decisions: [{ purpose_id: "pur_marketing_002", decision: "withdrawn" }] }
  │
  ├─► Backend processes withdrawal:
  │     ├─ Create ConsentDecision record
  │     ├─ Update consent cache
  │     ├─ Dispatch to email service: remove from marketing lists
  │     ├─ Dispatch to email service: add to suppression list
  │     ├─ Cancel scheduled campaigns for this user
  │     └─ Log propagation events
  │
  ├─► UI updates:
  │     ├─ Toggle shows OFF state
  │     └─ Message: "Done. You'll stop receiving product emails within 24 hours."
  │
  └─► Confirmation email sent:
        Subject: "CloudVault SaaS Inc. — Consent Withdrawal Confirmed"
        Body: "You've withdrawn consent for Product Update Emails.
               Processing will stop within 24 hours.
               You can re-enable this in Settings > Privacy at any time."
```

## Workflow 2: Email One-Click Unsubscribe (RFC 8058)

```
START: User receives marketing email from CloudVault SaaS Inc.
  │
  ├─► Email headers include:
  │     List-Unsubscribe: <https://app.cloudvault-saas.eu/unsubscribe?id=enc_abc123>
  │     List-Unsubscribe-Post: List-Unsubscribe=One-Click
  │
  ├─► Option A: User clicks "Unsubscribe" in email client UI
  │     ├─ Email client sends POST to List-Unsubscribe URL
  │     ├─ Server processes as consent withdrawal for pur_marketing_002
  │     └─ No further user interaction needed (true one-click per RFC 8058)
  │
  ├─► Option B: User clicks unsubscribe link in email footer
  │     ├─ Browser opens unsubscribe confirmation page
  │     ├─ Page shows: "Unsubscribe from CloudVault product emails?"
  │     │   [Unsubscribe] [Keep Receiving]
  │     ├─ User clicks [Unsubscribe]
  │     └─ Server processes as consent withdrawal for pur_marketing_002
  │
  ├─► Backend processing (same as preference center withdrawal):
  │     ├─ Create ConsentDecision record
  │     ├─ Remove from marketing lists
  │     ├─ Add to suppression list
  │     └─ Cancel scheduled campaigns
  │
  └─► Confirmation page:
        "You've been unsubscribed from CloudVault product emails.
         You can re-subscribe in Settings > Privacy."
```

## Workflow 3: Cascading Third-Party Notification

```
TRIGGER: User withdraws consent for pur_benchmarking_003 (third-party sharing)
  │
  ├─► Step 1: Internal systems processing (immediate)
  │     ├─ Stop data export pipeline for this user
  │     ├─ Flag user data in export staging table as "withdrawn"
  │     └─ Update consent cache
  │
  ├─► Step 2: Third-party notification (within 1 hour)
  │     ├─ Send API notification to Datalytics Partners Ltd.:
  │     │   POST https://api.datalytics-partners.nl/v2/consent/withdrawal
  │     │   {
  │     │     "notification_type": "consent_withdrawal",
  │     │     "subject_reference": "sha256_hashed_subject_id",
  │     │     "purpose_id": "pur_benchmarking_003",
  │     │     "withdrawal_timestamp": "2026-03-14T10:30:00Z",
  │     │     "required_action": "cease_processing",
  │     │     "action_deadline": "2026-03-15T10:30:00Z",
  │     │     "acknowledgment_required": true
  │     │   }
  │     │
  │     └─ Log notification dispatch in propagation table
  │
  ├─► Step 3: Monitor acknowledgment
  │     ├─ Expected response within 4 hours (per DPA Section 8.3)
  │     ├─ T+1 hour: No response → automated retry
  │     ├─ T+4 hours: No response → alert engineering team
  │     ├─ T+12 hours: No response → alert DPO
  │     └─ T+24 hours: No response → DPO initiates DPA breach process
  │
  ├─► Step 4: Acknowledgment received
  │     ├─ Update propagation log: status = "acknowledged"
  │     ├─ Record estimated processing cessation time
  │     └─ Schedule verification check at estimated completion time
  │
  └─► Step 5: Verification (at estimated completion time)
        ├─ Query Datalytics Partners Ltd. API to confirm processing stopped
        ├─ If confirmed: update propagation log: status = "completed"
        └─ If not confirmed: escalate to DPO for manual follow-up
```

## Workflow 4: Equal Ease Audit

```
TRIGGER: Quarterly compliance audit or consent UI deployment
  │
  ├─► Step 1: Measure consent-giving complexity
  │     ├─ Record click count for each consent-giving path
  │     ├─ Record page navigations
  │     ├─ Record form fields
  │     └─ Record estimated time to complete
  │
  ├─► Step 2: Measure withdrawal complexity
  │     ├─ Same metrics for each withdrawal path:
  │     │   ├─ Preference center path
  │     │   ├─ Footer link path
  │     │   ├─ Email unsubscribe path
  │     │   ├─ Dashboard widget path
  │     │   └─ API path
  │     └─ Record for each purpose
  │
  ├─► Step 3: Compare metrics
  │     ├─ For each purpose and each path:
  │     │   ├─ withdrawal_clicks <= consent_clicks ? PASS : FAIL
  │     │   ├─ withdrawal_pages <= consent_pages ? PASS : FAIL
  │     │   └─ withdrawal_fields <= consent_fields ? PASS : FAIL
  │     └─ Overall compliance determination
  │
  ├─► Step 4: Document findings
  │     ├─ Screenshot evidence for each path
  │     ├─ Metric comparison table
  │     └─ Remediation recommendations for any failures
  │
  └─► Step 5: Submit to DPO for sign-off
```
