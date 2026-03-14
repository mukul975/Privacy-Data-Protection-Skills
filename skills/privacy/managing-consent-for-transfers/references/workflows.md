# Workflows — Managing Consent for Transfers

## Workflow 1: Transfer Consent Collection

```
START: User encounters transfer consent in CloudVault SaaS Inc. settings
  │
  ├─► Step 1: Display transfer information
  │     ├─ Destination: India (CloudVault India Pvt. Ltd., Bengaluru)
  │     ├─ Purpose: 24/7 customer support
  │     ├─ Data: name, email, account metadata, support ticket content
  │     ├─ Adequacy status: No EU adequacy decision for India
  │     ├─ Safeguards: Not covered by SCCs or BCRs for this transfer
  │     └─ Specific risks: detailed risk disclosure
  │
  ├─► Step 2: Require explicit consent action
  │     ├─ User must read full disclosure (scroll tracking or read time check)
  │     ├─ User must type: "I consent to the transfer" in text input field
  │     └─ Typed declaration satisfies "explicit consent" under Art. 49(1)(a)
  │
  ├─► Step 3: Record transfer consent
  │     ├─ Standard consent record fields
  │     ├─ Transfer-specific fields:
  │     │   ├─ destination_country: "IN" (India)
  │     │   ├─ recipient: "CloudVault India Pvt. Ltd."
  │     │   ├─ adequacy_decision: false
  │     │   ├─ appropriate_safeguards: false
  │     │   ├─ risk_disclosure_version: SHA-256 hash
  │     │   └─ consent_type: "explicit_typed_declaration"
  │     └─ Mechanism: typed statement
  │
  └─► Step 4: Confirm
        "Transfer consent recorded. Your support tickets may now be
         handled by our Bengaluru team outside EU business hours."
```

## Workflow 2: Transfer Consent Withdrawal

```
TRIGGER: User withdraws transfer consent in Settings > Privacy > Data Transfers
  │
  ├─► Step 1: Process withdrawal
  │     ├─ Record withdrawal in consent system
  │     └─ Update transfer consent status to "withdrawn"
  │
  ├─► Step 2: Operational impact
  │     ├─ Route future support tickets to EU-only queue
  │     ├─ Notify Bengaluru team: do not access this user's tickets
  │     └─ Apply routing rule within 24 hours
  │
  ├─► Step 3: Confirm to user
  │     "Transfer consent withdrawn. Your support requests will be
  │      handled during EU business hours (Mon-Fri, 08:00-18:00 CET)."
  │
  └─► Step 4: Audit trail
        ├─ Log withdrawal event
        ├─ Log routing rule change
        └─ Verify no data transferred after withdrawal
```
