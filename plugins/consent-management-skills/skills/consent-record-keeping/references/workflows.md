# Workflows — Building Consent Record-Keeping

## Workflow 1: Recording a Consent Decision

```
TRIGGER: User makes a consent decision (grant or withdraw)
  │
  ├─► Step 1: Capture consent context
  │     ├─ subject_id: authenticated user UUID
  │     ├─ purpose_id: identifier of the processing purpose
  │     ├─ decision: "granted" or "not_granted" or "withdrawn"
  │     ├─ mechanism: "checkbox_tick", "toggle_switch", etc.
  │     ├─ source: "signup_flow", "preference_center", "cookie_banner"
  │     ├─ timestamp: server-generated UTC timestamp (not client-supplied)
  │     ├─ ip_address: request IP address
  │     ├─ user_agent: browser user agent string
  │     └─ session_id: current session identifier
  │
  ├─► Step 2: Retrieve current consent text version
  │     ├─ Query consent_text_versions for current version of this purpose
  │     ├─ Record the text_hash (SHA-256) of the consent text displayed
  │     └─ Store the full consent text in the version table (if not already present)
  │
  ├─► Step 3: Compute record integrity hash
  │     ├─ Concatenate: subject_id + purpose_id + decision + timestamp + text_hash
  │     ├─ Retrieve previous record hash for this subject (chain hashing)
  │     ├─ Compute SHA-256 of (concatenated fields + previous hash)
  │     └─ This creates a tamper-evident chain
  │
  ├─► Step 4: Insert consent record (append-only)
  │     ├─ INSERT INTO consent_records (all fields)
  │     ├─ Record is IMMUTABLE — no UPDATE or DELETE permitted
  │     └─ Return consent_id for receipt generation
  │
  └─► Step 5: Generate consent receipt
        ├─ Format as Kantara Consent Receipt JSON
        ├─ Store receipt in consent_receipts table
        ├─ Make available for download via user's preference center
        └─ Include in audit trail
```

## Workflow 2: Consent Record Audit

```
TRIGGER: Quarterly audit schedule, DPA inquiry, or data subject access request
  │
  ├─► Step 1: Define audit scope
  │     ├─ Time period: e.g., 2026-Q1 (January 1 to March 31)
  │     ├─ Purposes: all or specific
  │     └─ Subjects: all or specific (for DSAR)
  │
  ├─► Step 2: Record completeness check
  │     ├─ Query total consent decisions in period
  │     ├─ Verify all mandatory fields populated
  │     ├─ Flag records with missing fields:
  │     │   ├─ Missing consent_text_version → CRITICAL (cannot prove what was shown)
  │     │   ├─ Missing timestamp → CRITICAL (cannot prove when consent given)
  │     │   ├─ Missing mechanism → HIGH (cannot prove affirmative action)
  │     │   └─ Missing ip_address → LOW (supplementary evidence)
  │     └─ Calculate completeness percentage
  │
  ├─► Step 3: Chain integrity verification
  │     ├─ For each subject, traverse the consent record chain
  │     ├─ Recompute each record's hash from its fields + previous hash
  │     ├─ Compare computed hash against stored record_hash
  │     ├─ Flag any chain breaks (hash mismatch = potential tampering)
  │     └─ Report integrity status: intact / broken (with break point)
  │
  ├─► Step 4: Version consistency check
  │     ├─ For each consent record, verify the consent_text_version exists
  │     │   in the consent_text_versions table
  │     ├─ Verify the version was effective at the timestamp of the consent
  │     ├─ Flag orphaned records (version reference doesn't exist)
  │     └─ Flag anachronistic records (version wasn't effective at the timestamp)
  │
  ├─► Step 5: Statistical analysis
  │     ├─ Consent grant rate per purpose
  │     ├─ Withdrawal rate per purpose
  │     ├─ Average time between grant and withdrawal
  │     ├─ Consent source distribution (signup vs preference center vs banner)
  │     └─ Mechanism distribution (checkbox vs toggle vs API)
  │
  └─► Step 6: Generate audit report
        ├─ Executive summary with compliance metrics
        ├─ Completeness scores per field
        ├─ Chain integrity results
        ├─ Version consistency findings
        ├─ Statistical overview
        └─ Recommendations for any deficiencies found
```

## Workflow 3: Responding to Supervisory Authority Inquiry

```
TRIGGER: Supervisory authority (e.g., Irish DPC) requests evidence of valid consent
  │
  ├─► Step 1: Identify scope of inquiry
  │     ├─ Which data subjects?
  │     ├─ Which processing purposes?
  │     ├─ Which time period?
  │     └─ What format does the authority require?
  │
  ├─► Step 2: Extract consent records
  │     ├─ Query consent_records for matching criteria
  │     ├─ Include full consent text versions
  │     ├─ Include chain integrity verification results
  │     └─ Generate consent receipts in Kantara format
  │
  ├─► Step 3: Prepare evidence package
  │     ├─ Consent records (JSON export)
  │     ├─ Consent text versions with effective dates
  │     ├─ Screenshots/recordings of consent UI at relevant times
  │     ├─ Chain integrity verification report
  │     ├─ System architecture documentation
  │     └─ Data flow diagrams showing how consent decisions propagate
  │
  └─► Step 4: Submit to DPO for review and submission
        ├─ DPO reviews evidence package for completeness
        ├─ Legal counsel reviews for privilege concerns
        └─ Submit to supervisory authority within response deadline
```
