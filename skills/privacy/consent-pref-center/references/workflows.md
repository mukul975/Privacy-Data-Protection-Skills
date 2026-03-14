# Workflows — Building Consent Preference Center

## Workflow 1: User Manages Consent via Preference Center

```
START: User navigates to Settings > Privacy > Manage Consent
  │
  ├─► System loads current consent state via GET /api/v1/consent/preferences/{subject_id}
  │
  ├─► Display preference center UI:
  │     ├─► Purpose 1: "Service Improvement Analytics" [Toggle: ON]
  │     │     └─ "Learn More" expander → full Art. 13 details
  │     ├─► Purpose 2: "Product Update Emails" [Toggle: OFF]
  │     │     └─ "Learn More" expander → full Art. 13 details
  │     └─► Purpose 3: "Third-Party Benchmarking" [Toggle: ON]
  │           └─ "Learn More" expander → full Art. 13 details
  │
  ├─► User clicks toggle for Purpose 3 (ON → OFF)
  │     │
  │     ├─► Confirmation dialog:
  │     │     "Withdraw consent for sharing data with Datalytics Partners Ltd.?
  │     │      This will stop anonymized usage sharing. You can re-enable anytime."
  │     │     [Cancel] [Withdraw]
  │     │
  │     ├─► User clicks [Withdraw]
  │     │
  │     ├─► PUT /api/v1/consent/preferences/{subject_id}
  │     │     Body: { decisions: [{ purpose_id: "pur_benchmarking_003", decision: "withdrawn" }] }
  │     │
  │     ├─► Backend:
  │     │     ├─ Insert new ConsentDecision record (decision: "withdrawn")
  │     │     ├─ Insert ConsentPropagationLog entries for:
  │     │     │     ├─ Datalytics Partners Ltd. data sharing pipeline
  │     │     │     ├─ Internal analytics aggregation service
  │     │     │     └─ Data warehouse ETL pipeline
  │     │     ├─ Dispatch async notifications to downstream systems
  │     │     └─ Return updated preferences
  │     │
  │     └─► UI shows: "Consent withdrawn. Processing stops within 24 hours."
  │           Toggle now shows OFF state
  │
  └─► User can view "Consent History" per purpose:
        └─ Table: Date | Action | Consent Text Version | Download Receipt
```

## Workflow 2: Consent Text Version Update

```
TRIGGER: Legal team approves updated consent text for a processing purpose
  │
  ├─► Step 1: DPO submits new consent text via admin interface
  │     ├─ Purpose: "Service Improvement Analytics"
  │     ├─ New text: [updated plain-language description]
  │     └─ Reason: "Added clarification about file metadata types per DPC feedback"
  │
  ├─► Step 2: System generates SHA-256 hash of new text
  │     └─ Creates new ConsentTextVersion record
  │         ├─ version_id: auto-generated UUID
  │         ├─ text_hash: SHA-256 of new text
  │         ├─ effective_from: scheduled deployment date
  │         └─ approved_by: "Marta Kowalski, DPO"
  │
  ├─► Step 3: Set effective_until on previous version record
  │
  ├─► Step 4: Determine re-consent requirement
  │     ├─ If change is material (new data categories, new recipients, expanded purpose):
  │     │     ├─ Flag all existing consents for this purpose as "pending_reconsent"
  │     │     ├─ Trigger in-app notification to affected users
  │     │     └─ Send email: "We've updated how we use your data for [purpose]. Please review."
  │     │
  │     └─ If change is non-material (clarification, readability improvement):
  │           └─ Update displayed text; no re-consent required
  │
  └─► Step 5: Log version transition in audit trail
```

## Workflow 3: TCF v2.2 Consent Signal Integration

```
TRIGGER: User interacts with cookie consent banner (advertising purposes)
  │
  ├─► Step 1: CMP loads Global Vendor List (GVL) from vendorlist.consensu.org
  │     └─ Cache GVL locally; refresh weekly per IAB requirements
  │
  ├─► Step 2: Display TCF-compliant consent interface
  │     ├─► Layer 1: Banner with "Accept All" / "Manage Preferences" / "Reject All"
  │     └─► Layer 2 (if Manage): Per-purpose toggles mapped to TCF purposes 1-11
  │           └─ Per-vendor toggles within each purpose
  │
  ├─► Step 3: User makes selections and clicks "Save Preferences"
  │
  ├─► Step 4: Generate TC String
  │     ├─ Encode: CMP ID, consent screen number, purpose consents bitmap,
  │     │          vendor consents bitmap, publisher restrictions
  │     └─ Output: base64url-encoded TC String
  │
  ├─► Step 5: Store TC String
  │     ├─ Set __tcfapi cookie (first-party)
  │     ├─ Store in consent database linked to subject_id
  │     └─ Make available via CMP API (__tcfapi JavaScript function)
  │
  ├─► Step 6: Propagate consent signals
  │     ├─ Advertising SDKs query __tcfapi for consent status
  │     ├─ Analytics tags check purpose consent before firing
  │     └─ Server-side systems query consent API before processing
  │
  └─► Step 7: Log all decisions in ConsentDecision table
        └─ Map TCF purpose IDs to internal purpose IDs
```

## Workflow 4: Consent Audit Report Generation

```
TRIGGER: Quarterly audit schedule or regulatory inquiry
  │
  ├─► Step 1: Query consent database for audit period
  │     ├─ Total consent decisions recorded
  │     ├─ Breakdown by purpose, decision type, source
  │     └─ Consent/withdrawal ratio per purpose
  │
  ├─► Step 2: Validate record completeness
  │     ├─ Check all required fields populated per Art. 7(1)
  │     ├─ Verify version hashes match known consent text versions
  │     └─ Flag any orphaned records or data integrity issues
  │
  ├─► Step 3: Verify propagation completeness
  │     ├─ Check all withdrawals resulted in propagation events
  │     ├─ Verify downstream acknowledgments received
  │     └─ Flag any propagation failures or delays beyond SLA
  │
  ├─► Step 4: Generate audit report
  │     ├─ Executive summary with compliance metrics
  │     ├─ Detailed findings with severity ratings
  │     └─ Remediation recommendations
  │
  └─► Step 5: Submit to DPO for review
```
