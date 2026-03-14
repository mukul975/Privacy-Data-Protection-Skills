# Workflows — Implementing GDPR-Valid Consent

## Workflow 1: Consent Collection Flow

```
START: User visits CloudVault SaaS Inc. sign-up page
  │
  ├─► Display registration form with mandatory fields (name, email, password)
  │
  ├─► Display separate consent section with heading "Your Privacy Choices"
  │     │
  │     ├─► Purpose 1: "Service Improvement Analytics" [Unticked checkbox]
  │     │     └─ Expandable: Full Art. 13 notice for this purpose
  │     │
  │     ├─► Purpose 2: "Product Update Emails" [Unticked checkbox]
  │     │     └─ Expandable: Full Art. 13 notice for this purpose
  │     │
  │     └─► Purpose 3: "Third-Party Benchmarking with Datalytics Partners Ltd." [Unticked checkbox]
  │           └─ Expandable: Full Art. 13 notice for this purpose
  │
  ├─► "Create Account" button is ALWAYS active regardless of consent choices
  │
  ├─► On submit:
  │     ├─► Create user account (independent of consent)
  │     ├─► Record consent receipt for each purpose:
  │     │     ├─ Subject ID: user UUID
  │     │     ├─ Timestamp: ISO 8601 UTC
  │     │     ├─ Consent version: SHA-256 hash of consent text
  │     │     ├─ Purpose ID: enumerated purpose code
  │     │     ├─ Decision: granted / not-granted
  │     │     ├─ Mechanism: checkbox-tick
  │     │     ├─ IP address (for fraud prevention)
  │     │     └─ User agent string
  │     │
  │     └─► Route to downstream systems:
  │           ├─ If Purpose 1 granted → enable analytics SDK
  │           ├─ If Purpose 2 granted → add to email marketing list
  │           └─ If Purpose 3 granted → enable data sharing pipeline
  │
  └─► Redirect to dashboard with consent summary visible in account settings
```

## Workflow 2: Consent Audit Process

```
TRIGGER: Quarterly audit schedule OR consent UI change deployed
  │
  ├─► Step 1: Retrieve current consent form from production environment
  │
  ├─► Step 2: Run 15-point audit checklist (see SKILL.md)
  │     ├─► For each item, record: Pass / Fail / Not Applicable
  │     └─► For each Fail, document the specific deficiency
  │
  ├─► Step 3: Cross-reference consent text versions in database
  │     ├─► Verify all historical versions are preserved
  │     └─► Verify current production version matches latest approved version
  │
  ├─► Step 4: Sample consent records (minimum 100 records)
  │     ├─► Verify all required fields are populated
  │     ├─► Verify timestamps are in UTC ISO 8601 format
  │     └─► Verify consent version hashes match known versions
  │
  ├─► Step 5: Test withdrawal flow
  │     ├─► Measure steps required to withdraw consent
  │     ├─► Compare with steps required to give consent
  │     ├─► Verify downstream processing stops within SLA (24 hours)
  │     └─► Verify confirmation notification sent to data subject
  │
  ├─► Step 6: Generate audit report
  │     ├─► Summary of findings
  │     ├─► List of deficiencies with severity rating
  │     └─► Remediation actions with assigned owners and deadlines
  │
  └─► Step 7: Submit report to DPO for review and sign-off
```

## Workflow 3: Consent Re-Collection (Purpose Change)

```
TRIGGER: New processing purpose added or existing purpose modified
  │
  ├─► Step 1: DPO reviews the new/modified purpose
  │     ├─► Confirm consent is the appropriate lawful basis
  │     └─► Draft new consent text meeting Art. 13 requirements
  │
  ├─► Step 2: Legal team reviews and approves consent text
  │
  ├─► Step 3: Engineering implements new consent request in UI
  │     ├─► New purpose appears as additional unticked checkbox
  │     └─► Existing consents remain unchanged
  │
  ├─► Step 4: Deploy to production with new consent version hash
  │
  ├─► Step 5: Notify affected users via in-app banner and email
  │     ├─► "We've added a new optional data use. Review your privacy choices."
  │     └─► Direct link to consent preference center
  │
  ├─► Step 6: Record new consent decisions as they come in
  │     └─► Do NOT assume prior consent covers new purpose
  │
  └─► Step 7: After 30 days, generate report on re-consent rates
```
