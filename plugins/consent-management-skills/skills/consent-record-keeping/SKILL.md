---
name: consent-record-keeping
description: >-
  Guide for building a consent record-keeping system to demonstrate valid consent
  per GDPR Article 7(1). Covers required fields including timestamp, version, purpose,
  mechanism, and identity. Implements audit-ready consent receipts per the Kantara
  Initiative Consent Receipt Specification and supervisory authority expectations.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: consent-management
  tags: "consent-records, article-7-1, kantara-consent-receipt, audit-trail, consent-proof"
---

# Building Consent Record-Keeping

## Overview

GDPR Article 7(1) states: "Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to the processing of personal data." This obligation to demonstrate consent requires comprehensive record-keeping that captures not only the consent decision but the context in which it was made.

The Kantara Initiative Consent Receipt Specification (v1.1) provides a standardized machine-readable format for consent receipts that satisfies regulatory expectations and enables interoperability.

## Required Record Fields

Per EDPB Guidelines 05/2020 (paragraphs 89-107), demonstrating consent requires preserving evidence of:

### Core Fields (Mandatory)

| Field | Description | GDPR Reference | Format |
|-------|-------------|----------------|--------|
| consent_id | Unique identifier for this consent decision | Art. 7(1) | UUID v4 |
| subject_id | Identifier of the data subject | Art. 7(1) | UUID v4 |
| purpose_id | Identifier of the processing purpose | Art. 6(1)(a) | Purpose code |
| purpose_description | Plain-language description of the purpose | Art. 13(1)(c) | Text |
| decision | Consent granted or not granted | Art. 7(1) | Enum: granted, not_granted |
| timestamp | When the decision was made | Art. 7(1) | ISO 8601 UTC |
| mechanism | How consent was expressed | Art. 4(11) | Enum: checkbox_tick, toggle_switch, typed_statement, signature |
| consent_text_version | Hash of the exact consent text shown | Art. 7(1) | SHA-256 hex |
| consent_text | The exact text presented to the data subject | Art. 7(2) | Full text |
| controller_name | Legal name of the data controller | Art. 13(1)(a) | Text |
| controller_contact | Controller contact information | Art. 13(1)(a) | Text |

### Contextual Fields (Recommended)

| Field | Description | GDPR Reference | Format |
|-------|-------------|----------------|--------|
| ip_address | IP address at time of consent | Art. 7(1) proof | IPv4/IPv6 |
| user_agent | Browser/device user agent string | Art. 7(1) proof | Text |
| session_id | Session identifier | Art. 7(1) proof | UUID |
| source | Where consent was collected | Art. 7(1) proof | Enum: signup, preference_center, cookie_banner |
| data_categories | Categories of personal data for this purpose | Art. 13(1)(d) | JSON array |
| recipients | Named third-party recipients | Art. 13(1)(e) | JSON array |
| retention_period | How long data is retained for this purpose | Art. 13(2)(a) | Text |
| withdrawal_info | Instructions for withdrawing consent | Art. 7(3) | Text |
| dpo_contact | DPO contact information | Art. 13(1)(b) | Text |

### Immutability Requirements

Consent records must be immutable. Once a consent decision is recorded, it cannot be altered. This requires:

1. **Append-Only Storage**: Use an append-only database table or immutable log store. Never UPDATE or DELETE consent records.
2. **Integrity Hashing**: Each record includes a SHA-256 hash of its contents. Any tampering is detectable.
3. **Chain Hashing**: Each record's hash includes the previous record's hash, creating a verifiable chain (similar to blockchain concepts but without the distributed ledger overhead).
4. **Timestamp Integrity**: Timestamps are generated server-side (not client-supplied) to prevent manipulation.

## Kantara Initiative Consent Receipt Format

The Kantara Initiative Consent Receipt Specification v1.1 defines a JSON format:

```json
{
    "version": "KI-CR-v1.1.0",
    "jurisdiction": "EU/GDPR",
    "consentTimestamp": "2026-03-14T10:30:00Z",
    "collectionMethod": "web form with unticked checkboxes",
    "consentReceiptID": "cr_7f3a9b2e-41d8-4c76-b5e3-9a8d1c2f4e60",
    "publicKey": "cloudvault-saas-public-key-fingerprint",
    "language": "en",
    "piiPrincipalId": "usr_7f3a9b2e-41d8-4c76-b5e3-9a8d1c2f4e60",
    "piiControllers": [
        {
            "piiController": "CloudVault SaaS Inc.",
            "onBehalf": false,
            "contact": "42 Innovation Drive, Dublin, D02 YX88, Ireland",
            "phone": "+353-1-555-0142",
            "email": "privacy@cloudvault-saas.eu",
            "piiControllerUrl": "https://cloudvault-saas.eu"
        }
    ],
    "policyUrl": "https://cloudvault-saas.eu/privacy-policy",
    "services": [
        {
            "service": "CloudVault Cloud Storage",
            "purposes": [
                {
                    "purpose": "Service Improvement Analytics",
                    "purposeCategory": ["core function"],
                    "consentType": "explicit",
                    "piiCategory": ["file_metadata", "access_frequency", "storage_patterns"],
                    "primaryPurpose": true,
                    "termination": "https://app.cloudvault-saas.eu/settings/privacy",
                    "thirdPartyDisclosure": false
                }
            ]
        }
    ],
    "sensitive": false,
    "spiCat": []
}
```

## Database Schema

```sql
-- Consent records table (append-only, never UPDATE or DELETE)
CREATE TABLE consent_records (
    consent_id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    subject_id          UUID NOT NULL,
    purpose_id          VARCHAR(128) NOT NULL,
    purpose_description TEXT NOT NULL,
    decision            VARCHAR(16) NOT NULL CHECK (decision IN ('granted', 'not_granted', 'withdrawn')),
    mechanism           VARCHAR(64) NOT NULL,
    consent_text_version CHAR(64) NOT NULL,
    timestamp_utc       TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    ip_address          INET,
    user_agent          TEXT,
    session_id          UUID,
    source              VARCHAR(64) NOT NULL,
    controller_name     VARCHAR(256) NOT NULL DEFAULT 'CloudVault SaaS Inc.',
    record_hash         CHAR(64) NOT NULL,
    previous_hash       CHAR(64),
    created_at          TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
);

-- Index for efficient lookups per subject
CREATE INDEX idx_consent_records_subject ON consent_records(subject_id, purpose_id, timestamp_utc DESC);

-- Consent text versions (immutable)
CREATE TABLE consent_text_versions (
    version_id   UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    purpose_id   VARCHAR(128) NOT NULL,
    consent_text TEXT NOT NULL,
    text_hash    CHAR(64) NOT NULL UNIQUE,
    approved_by  VARCHAR(256) NOT NULL,
    effective_from TIMESTAMP WITH TIME ZONE NOT NULL,
    effective_until TIMESTAMP WITH TIME ZONE,
    created_at   TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
);

-- Prevent modifications to consent records
REVOKE UPDATE, DELETE ON consent_records FROM app_user;
REVOKE UPDATE, DELETE ON consent_text_versions FROM app_user;
```

## Audit Query Examples

**Reconstruct consent state for a subject at a point in time:**
```sql
SELECT DISTINCT ON (purpose_id)
    purpose_id, decision, timestamp_utc, consent_text_version, mechanism, source
FROM consent_records
WHERE subject_id = 'usr_7f3a9b2e-41d8-4c76-b5e3-9a8d1c2f4e60'
  AND timestamp_utc <= '2026-02-15T00:00:00Z'
ORDER BY purpose_id, timestamp_utc DESC;
```

**Verify record chain integrity:**
```sql
SELECT consent_id, record_hash, previous_hash,
    CASE WHEN LAG(record_hash) OVER (ORDER BY created_at) = previous_hash
         THEN 'VALID' ELSE 'BROKEN'
    END AS chain_status
FROM consent_records
WHERE subject_id = 'usr_7f3a9b2e-41d8-4c76-b5e3-9a8d1c2f4e60'
ORDER BY created_at;
```

## Key Regulatory References

- GDPR Article 7(1) — Controller must demonstrate consent
- GDPR Article 7(2) — Consent text requirements (clear, plain language, distinguishable)
- GDPR Article 5(2) — Accountability principle
- GDPR Article 30 — Records of processing activities (consent records support this)
- EDPB Guidelines 05/2020 — Paragraphs 89-107 on demonstrating consent
- Kantara Initiative Consent Receipt Specification v1.1 — Machine-readable receipt format
- ISO/IEC 29184:2020 — Online privacy notices and consent
