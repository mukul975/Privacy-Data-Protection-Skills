---
name: implementing-data-minimization-architecture
description: >-
  Architecture patterns for GDPR Article 5(1)(c) data minimization and Article 25(1)
  data protection by design. Covers field-level encryption, data masking, aggregation,
  pseudonymization per Article 4(5), and anonymization per Recital 26. Includes ENISA
  pseudonymization techniques and a data minimization assessment matrix.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-by-design
  tags: "data-minimization, article-25, pseudonymization, anonymization, field-level-encryption"
---

# Implementing Data Minimization Architecture

## Overview

Data minimization is a core principle of the GDPR under Article 5(1)(c), requiring that personal data be "adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed." Article 25(1) mandates that controllers implement appropriate technical and organisational measures, such as pseudonymisation, designed to implement data-protection principles effectively and to integrate necessary safeguards into the processing.

The European Data Protection Board (EDPB) Guidelines 4/2019 on Article 25 Data Protection by Design and by Default clarify that data minimization applies across four dimensions: the amount of data collected, the extent of processing, the period of storage, and the accessibility of data. ENISA's 2019 report on pseudonymisation techniques provides the technical foundation for implementing these requirements at scale.

## Data Minimization Architecture Layers

### Layer 1: Collection Minimization

Reduce data at the point of ingestion before it enters backend systems.

**Techniques:**

| Technique | Description | GDPR Basis | Implementation Complexity |
|-----------|-------------|------------|--------------------------|
| Schema enforcement | Reject fields not explicitly required for the declared purpose | Art. 5(1)(c), Art. 25(1) | Low |
| Client-side filtering | Strip unnecessary fields in the client SDK before transmission | Art. 5(1)(c) | Medium |
| Progressive collection | Request additional fields only when a specific feature is activated | Art. 5(1)(c), Recital 39 | Medium |
| Purpose-gated forms | Display only form fields relevant to the selected service tier | Art. 5(1)(b), Art. 25(2) | Low |

**Prism Data Systems AG Implementation:**
Prism Data Systems AG deploys an API gateway validation layer that enforces a strict allowlist of fields per endpoint. The customer onboarding endpoint `/api/v2/customers` accepts only: `email`, `display_name`, `country_code`, and `consent_references[]`. Fields like `date_of_birth`, `phone_number`, and `billing_address` are collected only when the customer activates the billing module, implementing progressive collection tied to purpose activation.

### Layer 2: Processing Minimization

Reduce the identifiability of data during computation.

#### Pseudonymization (Article 4(5))

Article 4(5) defines pseudonymisation as "the processing of personal data in such a manner that the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to technical and organisational measures."

**ENISA Pseudonymization Techniques (2019 Report):**

| Technique | Reversibility | Collision Risk | Suitable For |
|-----------|--------------|----------------|-------------|
| Counter-based mapping | Reversible with lookup table | None | Customer IDs, transaction references |
| HMAC-SHA256 with secret key | Reversible with key | Negligible (256-bit) | Cross-system linkage where re-identification is needed |
| Format-preserving encryption (FF1/FF3-1) | Reversible with key | None | Structured data (credit card numbers, SSNs) preserving format constraints |
| Tokenization with vault | Reversible with vault access | None | Payment card data (PCI DSS alignment) |
| Keyed hash with salt rotation | Computationally irreversible after rotation | Low | Session-level analytics where longitudinal tracking is unnecessary |

**Prism Data Systems AG Implementation:**
Prism Data Systems AG uses HMAC-SHA256 pseudonymization for all analytics pipelines. Customer identifiers are pseudonymized at the boundary between the transactional database and the analytics data warehouse. The HMAC key is stored in a Hardware Security Module (HSM) managed by the security operations team, physically and logically separated from the analytics infrastructure per ENISA recommended controls.

#### Anonymization (Recital 26)

Recital 26 states that the principles of data protection should not apply to anonymous information, namely "information which does not relate to an identified or identifiable natural person or to personal data rendered anonymous in such a manner that the data subject is not or no longer identifiable." The Article 29 Working Party Opinion 05/2014 on Anonymisation Techniques (WP216) established three risk criteria:

1. **Singling out** — the ability to isolate a record identifying an individual
2. **Linkability** — the ability to link two records relating to the same individual
3. **Inference** — the ability to deduce the value of an attribute from other attributes

**Anonymization Techniques:**

| Technique | Singling Out | Linkability | Inference | Data Utility |
|-----------|-------------|-------------|-----------|-------------|
| k-Anonymity (k=5) | Mitigated | Partially mitigated | Not mitigated | High |
| l-Diversity (l=3) | Mitigated | Mitigated | Partially mitigated | Medium-High |
| t-Closeness (t=0.15) | Mitigated | Mitigated | Mitigated | Medium |
| Differential privacy (epsilon=1.0) | Mitigated | Mitigated | Mitigated | Configurable |
| Data aggregation (min group=11) | Mitigated | Mitigated | Partially mitigated | Low-Medium |

### Layer 3: Storage Minimization

Limit how much identifiable data persists at rest.

**Field-Level Encryption Architecture:**

```
                    ┌────────────────────────┐
                    │   Application Layer    │
                    │  (plaintext in memory) │
                    └──────────┬─────────────┘
                               │
                    ┌──────────▼─────────────┐
                    │  Encryption Service    │
                    │  AES-256-GCM per field │
                    │  Key: KMS / HSM        │
                    └──────────┬─────────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
 ┌────────▼───────┐  ┌────────▼───────┐  ┌────────▼───────┐
 │  email (enc)   │  │  name (enc)    │  │  country (clr) │
 │  DEK-email-v3  │  │  DEK-name-v3   │  │  (not PII)     │
 └────────────────┘  └────────────────┘  └────────────────┘
```

Each personally identifiable field is encrypted with a dedicated Data Encryption Key (DEK) wrapped by a Key Encryption Key (KEK) in AWS KMS or Azure Key Vault. This enables selective decryption: analytics queries on `country` never require decrypting `email` or `name`.

**Prism Data Systems AG Implementation:**
Prism Data Systems AG classifies all database columns into four sensitivity tiers:

| Tier | Classification | Encryption | Access Control | Example Fields |
|------|---------------|------------|----------------|----------------|
| T1 | Direct identifier | AES-256-GCM, field-level | Named individuals with business justification | email, full_name, national_id |
| T2 | Quasi-identifier | AES-256-GCM, field-level | Role-based, logged | date_of_birth, postal_code, job_title |
| T3 | Sensitive attribute | AES-256-GCM, field-level | Purpose-restricted, dual approval | health_data, financial_score |
| T4 | Non-identifying | Transport encryption (TLS 1.3) | Standard RBAC | country_code, language_preference |

### Layer 4: Access Minimization

Restrict who and what systems can access identifiable data.

**Data Masking Patterns:**

| Pattern | Description | Use Case |
|---------|-------------|----------|
| Static masking | Irreversibly replace PII in non-production databases | Development and QA environments |
| Dynamic masking | Apply masking rules at query time based on the requester's role | Customer support dashboards |
| On-the-fly masking | Mask data in transit between microservices | Inter-service API calls where full PII is unnecessary |
| Tokenized views | Database views that return tokens instead of raw values | Reporting layers, third-party integrations |

**Prism Data Systems AG Implementation:**
Customer support agents at Prism Data Systems AG see dynamically masked data by default: `m***l@example.com` for email, `***-***-4892` for phone numbers. Only escalation-tier agents can request unmasked access, which requires a ticket reference, is logged in the audit trail, and auto-expires after 30 minutes.

## Data Minimization Assessment Matrix

Use this matrix to evaluate each data field against minimization requirements before approving a new processing activity or system design.

| Assessment Criterion | Question | Scoring |
|---------------------|----------|---------|
| Necessity | Is this field required to fulfill the stated purpose? | 0 = No, 1 = Partially, 2 = Yes |
| Proportionality | Could a less identifying alternative achieve the same result? | 0 = Yes (use alternative), 1 = Partially, 2 = No alternative exists |
| Aggregation potential | Can this field be aggregated or generalized without losing required utility? | 0 = Fully aggregable, 1 = Partially, 2 = Must remain granular |
| Pseudonymization feasibility | Can this field be pseudonymized for this processing purpose? | 0 = Easily pseudonymized, 1 = With effort, 2 = Not feasible |
| Temporal scope | Is this field needed beyond the immediate transaction? | 0 = No (delete after use), 1 = Short retention, 2 = Long retention required |
| Access scope | How many roles need access to the raw value? | 0 = None (mask/encrypt), 1 = Limited roles, 2 = Broad access required |

**Scoring interpretation:**
- 0-4: Strong candidate for elimination, aggregation, or pseudonymization
- 5-8: Apply masking, field-level encryption, and access controls
- 9-12: Justified retention with full technical safeguards and documentation

**Prism Data Systems AG Implementation:**
Before any new microservice is deployed, the data architecture review board at Prism Data Systems AG requires a completed minimization assessment for every personal data field. Fields scoring below 5 must be eliminated or pseudonymized before the service passes the privacy gate in the CI/CD pipeline.

## Key Regulatory References

- GDPR Article 4(5) — Definition of pseudonymisation
- GDPR Article 5(1)(c) — Data minimization principle
- GDPR Article 25(1) — Data protection by design
- GDPR Article 25(2) — Data protection by default
- GDPR Article 32(1)(a) — Pseudonymisation and encryption as security measures
- GDPR Recital 26 — Scope of anonymous information
- GDPR Recital 78 — Appropriate technical and organisational measures
- EDPB Guidelines 4/2019 on Article 25 Data Protection by Design and by Default
- ENISA Report: Pseudonymisation techniques and best practices (November 2019)
- Article 29 Working Party Opinion 05/2014 on Anonymisation Techniques (WP216)
