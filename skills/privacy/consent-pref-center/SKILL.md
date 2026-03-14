---
name: building-consent-preference-center
description: >-
  Technical architecture guide for building a multi-purpose consent preference center.
  Covers per-purpose granularity, easy withdrawal under Article 7(3), version history,
  audit trails, and IAB Transparency and Consent Framework v2.2 integration.
  Includes database schema, API design, and UI component specifications.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: consent-management
  tags: "consent-preference-center, tcf-v2, consent-management, audit-trail, consent-ui"
---

# Building a Consent Preference Center

## Overview

A consent preference center is the centralized interface through which data subjects manage their consent choices across all processing purposes. Under GDPR Article 7(3), withdrawal of consent must be as easy as giving it, making a well-designed preference center critical for compliance. The IAB Europe Transparency and Consent Framework (TCF) v2.2 provides a standardized approach for advertising-related consent that integrates with this architecture.

## Architecture Components

### 1. Data Model

The consent preference center requires four core data entities:

**Consent Purpose Registry**
Stores all processing purposes for which consent is the lawful basis.

| Field | Type | Description |
|-------|------|-------------|
| purpose_id | UUID | Unique identifier for the processing purpose |
| purpose_name | VARCHAR(256) | Human-readable purpose name |
| purpose_description | TEXT | Plain-language description (Flesch-Kincaid grade 8 or below) |
| legal_basis | ENUM | "consent" or "explicit_consent" |
| data_categories | JSONB | Array of personal data categories processed |
| recipients | JSONB | Array of named third-party recipients |
| retention_period | VARCHAR(128) | Data retention period for this purpose |
| tcf_purpose_id | INTEGER | Mapped IAB TCF v2.2 purpose ID (1-11) if applicable |
| is_active | BOOLEAN | Whether this purpose is currently offered |
| created_at | TIMESTAMP | When the purpose was registered |
| updated_at | TIMESTAMP | Last modification timestamp |

**Consent Text Version**
Immutable records of consent text presented to users.

| Field | Type | Description |
|-------|------|-------------|
| version_id | UUID | Unique version identifier |
| purpose_id | UUID | FK to purpose registry |
| consent_text | TEXT | Exact text displayed to the user |
| text_hash | CHAR(64) | SHA-256 hash of consent_text |
| effective_from | TIMESTAMP | When this version went live |
| effective_until | TIMESTAMP | When this version was superseded (NULL if current) |
| approved_by | VARCHAR(256) | Name of DPO or legal reviewer who approved |

**Consent Decision**
Records each consent decision made by a data subject.

| Field | Type | Description |
|-------|------|-------------|
| decision_id | UUID | Unique decision identifier |
| subject_id | UUID | Data subject identifier |
| purpose_id | UUID | FK to purpose registry |
| version_id | UUID | FK to consent text version shown |
| decision | ENUM | "granted" or "withdrawn" |
| mechanism | VARCHAR(64) | "checkbox_tick", "toggle_switch", "api_call" |
| timestamp | TIMESTAMP | ISO 8601 UTC timestamp |
| ip_address | INET | IP address at time of decision |
| user_agent | TEXT | Browser user agent string |
| source | VARCHAR(64) | "signup_flow", "preference_center", "cookie_banner", "api" |

**Consent Propagation Log**
Tracks downstream system notifications after consent changes.

| Field | Type | Description |
|-------|------|-------------|
| propagation_id | UUID | Unique propagation event ID |
| decision_id | UUID | FK to consent decision that triggered this |
| target_system | VARCHAR(256) | Name of downstream system notified |
| status | ENUM | "pending", "delivered", "acknowledged", "failed" |
| sent_at | TIMESTAMP | When notification was dispatched |
| acknowledged_at | TIMESTAMP | When downstream system confirmed receipt |

### 2. API Design

**GET /api/v1/consent/preferences/{subject_id}**
Returns current consent state for all purposes for a given data subject.

Response:
```json
{
  "subject_id": "usr_7f3a9b2e-41d8-4c76-b5e3-9a8d1c2f4e60",
  "preferences": [
    {
      "purpose_id": "pur_analytics_001",
      "purpose_name": "Service Improvement Analytics",
      "decision": "granted",
      "granted_at": "2026-01-15T10:30:00Z",
      "version_id": "ver_a1b2c3d4"
    },
    {
      "purpose_id": "pur_marketing_002",
      "purpose_name": "Product Update Emails",
      "decision": "withdrawn",
      "withdrawn_at": "2026-02-20T14:45:00Z",
      "version_id": "ver_e5f6g7h8"
    }
  ],
  "last_updated": "2026-02-20T14:45:00Z"
}
```

**PUT /api/v1/consent/preferences/{subject_id}**
Updates consent for one or more purposes. Triggers downstream propagation.

Request:
```json
{
  "decisions": [
    {
      "purpose_id": "pur_marketing_002",
      "decision": "granted",
      "mechanism": "toggle_switch"
    }
  ]
}
```

**GET /api/v1/consent/history/{subject_id}**
Returns full consent history for audit purposes per Article 7(1).

**GET /api/v1/consent/receipt/{decision_id}**
Returns a single consent receipt in Kantara Initiative Consent Receipt format.

### 3. TCF v2.2 Integration

The IAB Transparency and Consent Framework v2.2 (released September 2023) requires:

- **TC String Generation**: Encode consent signals into the IAB TC String format. The TC String is a base64url-encoded bitfield that captures consent for TCF-defined purposes (1-11) and legitimate interest assertions.
- **CMP Registration**: Register with the IAB Europe as a Consent Management Platform. Each registered CMP receives a unique CMP ID used in TC String generation.
- **Vendor List Integration**: Consume the IAB Global Vendor List (GVL) to display vendor-level consent options. The GVL is published at vendorlist.consensu.org and updated weekly.
- **Purpose Mapping**: Map internal CloudVault SaaS Inc. purposes to TCF v2.2 purposes:
  - TCF Purpose 1 (Store and/or access information on a device) → Cookie consent
  - TCF Purpose 3 (Create profiles for personalised advertising) → If applicable
  - TCF Purpose 7 (Measure ad performance) → Analytics consent
- **Publisher Restrictions**: Configure publisher-level restrictions to limit vendors to consent-only legal basis where CloudVault SaaS Inc. policy requires it.

### 4. UI Component Specification

The preference center interface at CloudVault SaaS Inc. follows these design principles:

**Layout:**
- Accessible at Settings > Privacy > Manage Consent (maximum 2 clicks from any page)
- Also accessible via direct URL: app.cloudvault-saas.eu/settings/privacy
- Persistent "Privacy Choices" link in the page footer on every page

**Per-Purpose Toggle:**
- Each purpose displays: purpose name, 1-sentence description, current state (on/off toggle)
- "Learn More" expandable section with: full description, data categories, recipients, retention period
- Toggle change triggers immediate API call and visual confirmation

**Consent History:**
- "View History" link per purpose showing: date, action (granted/withdrawn), consent text version
- Downloadable consent receipt in JSON format (Kantara Consent Receipt specification v1.1)

**Withdrawal Flow:**
- Single toggle click to withdraw (matching the single click to grant during sign-up)
- Confirmation dialog: "Are you sure you want to withdraw consent for [purpose]? This will stop [specific processing]. You can re-enable this at any time."
- Post-withdrawal confirmation: "Consent withdrawn. Processing will stop within 24 hours."

## Version History and Audit Trail

Every consent text change creates a new version record. The preference center always displays the current version but retains all historical versions. Audit queries can reconstruct:

- What text was shown to a specific user at a specific time
- When consent was given and withdrawn for each purpose
- Whether downstream systems were notified of consent changes
- The propagation status and timing for each consent change

## Key Regulatory References

- GDPR Article 7(1) — Demonstrating consent
- GDPR Article 7(3) — Right to withdraw consent, equal ease requirement
- GDPR Article 12(1) — Transparent, intelligible, easily accessible information
- IAB TCF v2.2 Specification (September 2023) — TC String encoding, CMP requirements
- Kantara Initiative Consent Receipt Specification v1.1 — Standard consent receipt format
- EDPB Guidelines 05/2020 — Consent under Regulation 2016/679
