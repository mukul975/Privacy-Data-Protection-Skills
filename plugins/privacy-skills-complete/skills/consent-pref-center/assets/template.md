# Consent Preference Center — Requirements Specification

## Project Information

| Field | Value |
|-------|-------|
| **Organization** | CloudVault SaaS Inc. |
| **Project** | Consent Preference Center v2.0 |
| **Document Version** | 1.0 |
| **Author** | James Park, Lead Frontend Engineer |
| **Reviewed By** | Marta Kowalski, DPO |
| **Date** | 2026-03-14 |

## Functional Requirements

### FR-01: Per-Purpose Consent Management

Users must be able to grant or withdraw consent for each processing purpose independently. The preference center must display:

- Purpose name and short description (1 sentence)
- Current consent state (granted / not granted)
- Toggle control to change state
- "Learn More" expandable section with full Article 13 information
- "View History" link to consent decision history for this purpose

**Active Purposes at CloudVault SaaS Inc.:**

| Purpose ID | Name | Data Categories | Recipients |
|-----------|------|-----------------|------------|
| pur_analytics_001 | Service Improvement Analytics | File metadata, access frequency, storage patterns | None (internal only) |
| pur_marketing_002 | Product Update Emails | Email address, name, product usage tier | None (internal only) |
| pur_benchmarking_003 | Industry Benchmarking | Anonymized usage metrics, storage tier, region | Datalytics Partners Ltd. |

### FR-02: Equal Ease Withdrawal (Art. 7(3))

Withdrawal must require no more steps than granting consent. Specifically:
- Sign-up consent: 1 click (checkbox tick)
- Preference center withdrawal: 1 click (toggle) + 1 confirmation dialog = 2 interactions maximum
- Preference center must be reachable in 2 clicks from any page

### FR-03: Consent History and Receipts

For each purpose, users can view:
- Complete decision history (date, action, consent text version)
- Download consent receipt in JSON format (Kantara Consent Receipt v1.1)
- Consent text that was displayed at the time of each decision

### FR-04: Version-Controlled Consent Text

- Every consent text change creates a new immutable version record
- Version identified by SHA-256 hash of the text content
- Historical versions preserved for audit trail
- Material changes trigger re-consent workflow

### FR-05: Downstream Propagation

When consent is withdrawn:
- Propagation events dispatched to all affected downstream systems within 1 hour
- Downstream systems must acknowledge receipt within 24 hours
- Processing must cease within 24 hours of withdrawal
- Propagation status logged for audit purposes

## Non-Functional Requirements

### NFR-01: Accessibility
- WCAG 2.1 Level AA compliance
- Screen reader compatible toggle controls
- Keyboard navigation support
- Minimum contrast ratio 4.5:1 for all text

### NFR-02: Performance
- Preference center page load: under 2 seconds
- Consent state change API response: under 500ms
- Consent history retrieval: under 1 second for up to 1000 records

### NFR-03: Data Integrity
- All consent records immutable (append-only)
- SHA-256 hashes verified on read
- Database-level constraints on required fields
- Automated integrity checks in quarterly audit

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/v1/consent/preferences/{subject_id} | Get current consent state |
| PUT | /api/v1/consent/preferences/{subject_id} | Update consent decisions |
| GET | /api/v1/consent/history/{subject_id} | Get consent history |
| GET | /api/v1/consent/receipt/{decision_id} | Get consent receipt |
| GET | /api/v1/consent/purposes | List all active purposes |

## Database Schema Summary

Four tables: consent_purposes, consent_text_versions, consent_decisions, consent_propagation_log. Full schema in SKILL.md architecture section.
