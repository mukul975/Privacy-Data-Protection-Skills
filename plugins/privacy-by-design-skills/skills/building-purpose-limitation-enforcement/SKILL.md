---
name: building-purpose-limitation-enforcement
description: >-
  Technical enforcement of GDPR Article 5(1)(b) purpose limitation principle.
  Covers purpose-tagged data stores, access control per purpose, Article 6(4)
  compatibility assessment factors, and system design for preventing purpose creep.
  Includes purpose binding architecture and compatibility test implementation.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-by-design
  tags: "purpose-limitation, article-5, compatibility-test, purpose-binding, access-control"
---

# Building Purpose Limitation Enforcement

## Overview

Article 5(1)(b) of the GDPR requires that personal data be "collected for specified, explicit and legitimate purposes and not further processed in a manner that is incompatible with those purposes." This is the purpose limitation principle, one of the foundational data protection principles.

The controller must specify the purpose at or before the time of collection (Article 13(1)(c) for direct collection, Article 14(1)(c) for indirect collection). Any subsequent processing for a different purpose requires either a new lawful basis or must pass the compatibility assessment under Article 6(4).

The Article 29 Working Party Opinion 03/2013 on purpose limitation (WP203) provides detailed guidance on assessing compatibility, identifying five key factors codified in Article 6(4).

## Article 6(4) Compatibility Assessment Factors

When a controller wishes to process personal data for a purpose other than that for which it was collected, Article 6(4) requires an assessment of compatibility considering:

| Factor | Article 6(4) Reference | Assessment Question |
|--------|----------------------|---------------------|
| Link between purposes | Article 6(4)(a) | Is there a connection between the original and new purpose? |
| Context of collection | Article 6(4)(b) | What is the relationship between controller and data subject? What are the reasonable expectations? |
| Nature of data | Article 6(4)(c) | Does the data include special categories (Article 9) or criminal convictions (Article 10)? |
| Consequences | Article 6(4)(d) | What are the possible consequences of the further processing for data subjects? |
| Safeguards | Article 6(4)(e) | Are appropriate safeguards in place, including encryption or pseudonymisation? |

**Compatibility is not required when:**
- Processing is based on consent (Article 6(1)(a)) — new consent can be obtained for the new purpose
- Processing is based on Union or Member State law that constitutes a necessary and proportionate measure (Article 6(4) final paragraph)
- Processing is for archiving in the public interest, scientific/historical research, or statistics per Article 89(1)

## Purpose-Tagged Data Architecture

### Design Principles

1. **Purpose binding at ingestion** — Every data record is tagged with its collection purpose at the point of entry into the system
2. **Purpose-based access control** — Access policies are defined per purpose, not per data field alone
3. **Purpose audit trail** — Every access is logged with the purpose under which it was authorized
4. **Purpose expiry** — When a purpose is fulfilled, the associated data enters a retention countdown

### Architecture Diagram

```
┌────────────────────────────────────────────────────────────┐
│                   Data Collection Points                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ Web Form │  │ API Call │  │ IoT Feed │  │ Partner  │  │
│  │ P:ONBRD  │  │ P:ANALYT │  │ P:MAINT  │  │ P:MARKET │  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  │
│       └──────────────┼──────────────┼──────────────┘       │
└──────────────────────┼──────────────┼──────────────────────┘
                       │              │
┌──────────────────────▼──────────────▼──────────────────────┐
│              Purpose Tagging Gateway                        │
│  ┌─────────────────┐  ┌─────────────────────────────────┐  │
│  │ Purpose Registry │  │ Tag Injection Middleware        │  │
│  │ (canonical IDs)  │  │ (attaches purpose + timestamp)  │  │
│  └─────────────────┘  └─────────────────────────────────┘  │
└──────────────────────────────┬─────────────────────────────┘
                               │
┌──────────────────────────────▼─────────────────────────────┐
│              Purpose-Partitioned Data Store                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ ONBRD    │  │ ANALYT   │  │ MAINT    │  │ MARKET   │  │
│  │ Partition│  │ Partition│  │ Partition│  │ Partition│  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
└──────────────────────────────┬─────────────────────────────┘
                               │
┌──────────────────────────────▼─────────────────────────────┐
│              Purpose Enforcement Layer                       │
│  ┌─────────────────┐  ┌────────────────┐  ┌────────────┐  │
│  │ Policy Engine   │  │ Compatibility  │  │ Audit      │  │
│  │ (OPA / Cedar)   │  │ Assessor       │  │ Logger     │  │
│  └─────────────────┘  └────────────────┘  └────────────┘  │
└────────────────────────────────────────────────────────────┘
```

### Purpose Registry Schema

Each processing purpose is registered with canonical metadata:

```json
{
  "purpose_id": "PRP-ONBRD-001",
  "purpose_name": "Customer Account Onboarding",
  "description": "Collection and processing of personal data necessary to create and activate a customer account, verify identity, and establish the contractual relationship.",
  "lawful_basis": "Article 6(1)(b)",
  "data_categories": ["email", "display_name", "country_code", "identity_verification_result"],
  "controller": "Prism Data Systems AG",
  "retention_period_days": 2555,
  "retention_trigger": "account_closure",
  "compatible_purposes": ["PRP-SUPRT-001", "PRP-SECUR-001"],
  "incompatible_purposes": ["PRP-MARKET-001", "PRP-RESRCH-001"],
  "special_categories": false,
  "created_date": "2025-06-01",
  "last_reviewed": "2026-01-15",
  "review_cadence_days": 180,
  "owner": "product_team",
  "dpo_approved": true
}
```

## Access Control Per Purpose

### Policy-as-Code with Open Policy Agent (OPA)

Purpose-based access control is implemented using OPA policies that evaluate access requests against the purpose registry:

```
# Prism Data Systems AG — Purpose-Based Access Policy

# Rule: Access is granted only if the requesting service's declared purpose
# matches a purpose tag on the requested data record.

allow {
    input.action == "read"
    input.resource.purpose_tags[_] == input.requester.declared_purpose
    purpose_is_active(input.requester.declared_purpose)
    role_authorized_for_purpose(input.requester.role, input.requester.declared_purpose)
}

# Rule: Cross-purpose access requires a completed compatibility assessment
allow {
    input.action == "read"
    not input.resource.purpose_tags[_] == input.requester.declared_purpose
    compatibility_assessment_approved(input.resource.purpose_tags, input.requester.declared_purpose)
    purpose_is_active(input.requester.declared_purpose)
}

# Rule: Write operations must include a valid purpose tag
allow {
    input.action == "write"
    valid_purpose(input.resource.purpose_tag)
    input.requester.declared_purpose == input.resource.purpose_tag
}
```

### Role-Purpose Authorization Matrix

| Role | ONBRD | ANALYT | SUPRT | MARKET | SECUR | BILLING |
|------|-------|--------|-------|--------|-------|---------|
| Onboarding Service | Read/Write | — | — | — | — | — |
| Analytics Pipeline | — | Read | — | — | — | — |
| Support Agent | Read | — | Read/Write | — | — | Read |
| Marketing Automation | — | — | — | Read | — | — |
| Security Operations | Read | Read | Read | Read | Read/Write | Read |
| Billing Service | Read | — | — | — | — | Read/Write |

## Purpose Compatibility Assessment Workflow

1. **Request submission** — Service owner submits a request to process data collected under purpose A for new purpose B, documenting the business justification.

2. **Factor analysis** — The Data Protection Office evaluates the five Article 6(4) factors:
   - Link between purposes (scored 1-5: 1 = no link, 5 = closely linked)
   - Context and expectations (scored 1-5: 1 = unexpected, 5 = fully expected)
   - Nature of data (scored 1-5: 1 = special category, 5 = non-sensitive)
   - Consequences (scored 1-5: 1 = severe, 5 = minimal impact)
   - Safeguards (scored 1-5: 1 = no safeguards, 5 = comprehensive safeguards)

3. **Scoring** — Total score calculated (range 5-25):
   - 20-25: Compatible. Approve with standard documentation.
   - 15-19: Potentially compatible. Approve with additional safeguards (pseudonymization, access restriction).
   - 10-14: Likely incompatible. Requires DPO escalation and DPIA consideration.
   - 5-9: Incompatible. Denied. New lawful basis or separate consent required.

4. **Decision recording** — Assessment result recorded in the purpose registry with the assessor identity, date, score breakdown, conditions, and review date.

5. **Policy update** — If approved, OPA policies are updated to allow cross-purpose access under documented conditions.

## Prism Data Systems AG Implementation

### Purpose Registry

Prism Data Systems AG maintains 14 registered purposes in their purpose registry:

| Purpose ID | Name | Lawful Basis | Data Categories |
|-----------|------|-------------|-----------------|
| PRP-ONBRD-001 | Customer onboarding | Art. 6(1)(b) | email, display_name, country_code |
| PRP-AUTH-001 | Authentication | Art. 6(1)(b) | email, password_hash, mfa_token |
| PRP-BILLING-001 | Billing and invoicing | Art. 6(1)(b) | billing_address, payment_method, vat_id |
| PRP-SUPRT-001 | Customer support | Art. 6(1)(b) | email, display_name, support_ticket_history |
| PRP-ANALYT-001 | Product analytics | Art. 6(1)(f) | pseudonymized_user_id, feature_events, session_duration |
| PRP-MARKET-001 | Direct marketing | Art. 6(1)(a) | email, display_name, marketing_preferences |
| PRP-SECUR-001 | Security monitoring | Art. 6(1)(f) | ip_address, user_agent, login_events |
| PRP-LEGAL-001 | Legal compliance | Art. 6(1)(c) | transaction_records, consent_records |

### Enforcement Metrics

Prism Data Systems AG tracks the following purpose limitation enforcement metrics:

| Metric | Target | Measurement |
|--------|--------|-------------|
| Purpose tag coverage | 100% of records | Percentage of data records with valid purpose tags |
| Cross-purpose access attempts blocked | > 95% without assessment | Policy engine denial count vs. total cross-purpose requests |
| Compatibility assessments completed | 100% within 5 business days | Time from request to DPO decision |
| Purpose registry review currency | 100% reviewed within cadence | Percentage of purposes reviewed within their review cadence |

## Key Regulatory References

- GDPR Article 5(1)(b) — Purpose limitation principle
- GDPR Article 6(4) — Compatibility assessment factors
- GDPR Article 13(1)(c) — Information about purpose at collection
- GDPR Article 14(1)(c) — Information about purpose for indirect collection
- GDPR Article 89(1) — Exception for archiving, research, statistics
- GDPR Recital 50 — Further processing compatibility
- Article 29 Working Party Opinion 03/2013 on purpose limitation (WP203)
- EDPB Guidelines 4/2019 on Article 25 Data Protection by Design and by Default
