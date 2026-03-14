---
name: conducting-linddun-threat-modeling
description: >-
  Comprehensive guide to LINDDUN privacy threat modeling methodology covering all
  seven threat categories: Linking, Identifying, Non-repudiation, Detecting, Data
  Disclosure, Unawareness, and Non-compliance. Includes DFD-based analysis, threat
  tree catalogs, mitigation mapping, and integration with GDPR Article 25 and 35.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-by-design
  tags: "linddun, privacy-threat-modeling, dfd-analysis, threat-trees, privacy-threats"
---

# Conducting LINDDUN Threat Modeling

## Overview

LINDDUN is a systematic privacy threat modeling methodology developed by the DistriNet research group at KU Leuven (Deng et al., 2011; Wuyts et al., 2015). It provides a structured approach to identifying privacy threats in system architectures by analyzing Data Flow Diagrams (DFDs) against seven privacy threat categories. The methodology maps directly to privacy design strategies and GDPR principles, making it essential for Article 25(1) data protection by design and Article 35 DPIA risk assessment.

LINDDUN stands for:
- **L**inking
- **I**dentifying
- **N**on-repudiation
- **D**etecting
- **D**ata Disclosure
- **U**nawareness
- **N**on-compliance

## The Seven LINDDUN Threat Categories

### L — Linking

**Definition:** The ability to sufficiently distinguish whether two or more items of interest (data records, messages, actions, identities) are related or not within the system.

**Privacy property violated:** Unlinkability

**GDPR relevance:** Article 5(1)(b) purpose limitation (linking enables purpose creep), Article 5(1)(c) data minimization (linked data reveals more than necessary).

**Threat examples:**
- Correlating pseudonymized analytics records with customer accounts using quasi-identifiers
- Linking browser sessions across different services via shared tracking identifiers
- Matching records across databases using common attributes (date of birth + postal code)

**DFD elements affected:** Data stores, data flows, external entities

### I — Identifying

**Definition:** The ability to identify a data subject from a set of data items, within a system or across systems.

**Privacy property violated:** Anonymity, pseudonymity

**GDPR relevance:** Article 4(5) pseudonymisation, Recital 26 anonymous information, Article 5(1)(c).

**Threat examples:**
- Re-identifying pseudonymized records through linkage attacks
- Identifying individuals from aggregated statistics (small group inference)
- Facial recognition from uploaded images in a profile system

### N — Non-repudiation

**Definition:** The inability of a data subject to deny having performed an action, when this denial should be possible.

**Privacy property violated:** Plausible deniability

**GDPR relevance:** Article 5(1)(a) fairness (unnecessary non-repudiation may unfairly burden data subjects).

**Threat examples:**
- System logs irrefutably linking every action to a named individual
- Digital signatures on documents that cannot be repudiated even after the purpose is fulfilled
- Immutable audit trails recording every click and interaction

### D — Detecting

**Definition:** The ability to sufficiently distinguish whether an item of interest (data subject, message, action) exists or not within the system.

**Privacy property violated:** Undetectability, unobservability

**GDPR relevance:** Article 5(1)(c) data minimization (detecting existence reveals information).

**Threat examples:**
- Traffic analysis revealing that a patient communicated with a specific medical specialist
- Detecting the existence of a record in a database through timing side-channels
- Observing that encrypted data is being transmitted even without reading the content

### D — Data Disclosure

**Definition:** Unauthorized access to or exposure of personal data.

**Privacy property violated:** Confidentiality

**GDPR relevance:** Article 5(1)(f) integrity and confidentiality, Article 32(1) security measures, Article 33-34 breach notification.

**Threat examples:**
- SQL injection exposing database contents
- Misconfigured cloud storage bucket making personal data publicly accessible
- Insider access to personal data beyond authorized purpose

### U — Unawareness

**Definition:** Data subjects being insufficiently aware of the processing of their personal data, their rights, or the consequences of sharing their data.

**Privacy property violated:** Transparency, intervenability

**GDPR relevance:** Articles 12-14 transparency obligations, Article 22 automated decision-making rights.

**Threat examples:**
- Collecting data without informing the data subject (violation of Article 13/14)
- Obscure or inaccessible privacy policies
- Automated decisions affecting individuals without explanation
- No mechanism for data subjects to exercise their rights

### N — Non-compliance

**Definition:** Failure to comply with applicable data protection legislation, policies, or standards.

**Privacy property violated:** Compliance

**GDPR relevance:** All articles; specifically Article 5 principles, Article 6 lawful basis, Article 25 by design, Article 30 records.

**Threat examples:**
- Processing without a valid lawful basis
- Retaining data beyond the documented retention period
- Failing to conduct a DPIA for high-risk processing
- Inadequate data processing agreements with processors

## DFD-Based Analysis Process

### Step 1: Create the Data Flow Diagram

Model the system using standard DFD notation:

| Element | Symbol | Description | LINDDUN Threats |
|---------|--------|-------------|----------------|
| External Entity | Rectangle | Actors outside the system boundary (users, third parties) | L, I, U, N(compliance) |
| Process | Circle | Operations on data within the system | L, I, N(repudiation), D(etecting), D(isclosure), U, N(compliance) |
| Data Store | Parallel lines | Persistent storage of data | L, I, D(isclosure), N(compliance) |
| Data Flow | Arrow | Movement of data between elements | L, I, D(etecting), D(isclosure) |
| Trust Boundary | Dashed line | Boundary between different trust levels | D(isclosure) |

### Step 2: Map Threats to DFD Elements

For each DFD element, systematically evaluate each LINDDUN threat category:

| DFD Element | L | I | N-rep | D-det | D-disc | U | N-comp |
|-------------|---|---|-------|-------|--------|---|--------|
| External Entity (Customer) | X | X | | | | X | X |
| Process (Analytics Engine) | X | X | X | X | X | X | X |
| Data Store (Customer DB) | X | X | | | X | | X |
| Data Flow (API Request) | X | X | | X | X | | |
| Data Flow (Analytics Export) | X | X | | X | X | | X |

### Step 3: Threat Tree Analysis

For each identified threat, use the LINDDUN threat tree catalog to enumerate specific attack scenarios.

**Example: Linking threat tree for Analytics Engine (Process)**

```
Linking (Analytics Engine)
├── Cross-session linking
│   ├── Persistent user identifiers in analytics events
│   ├── Browser fingerprinting across sessions
│   └── IP address correlation across time periods
├── Cross-purpose linking
│   ├── Shared identifiers between transactional and analytics stores
│   ├── Common quasi-identifiers enabling join attacks
│   └── Insufficient pseudonymization (reversible mapping)
└── Cross-system linking
    ├── Third-party tracking pixels in the application
    ├── Shared analytics SDK sending data to external services
    └── API responses containing cross-system correlation identifiers
```

### Step 4: Risk Assessment

For each threat, assess likelihood and impact:

| Threat | Likelihood (1-5) | Impact (1-5) | Risk Score | Priority |
|--------|-----------------|-------------|------------|----------|
| Cross-session linking via persistent user ID | 4 | 3 | 12 | High |
| Re-identification of pseudonymized analytics records | 3 | 4 | 12 | High |
| SQL injection exposing customer database | 2 | 5 | 10 | High |
| Insufficient privacy notice for analytics | 3 | 3 | 9 | Medium |
| Data retained beyond documented retention period | 3 | 3 | 9 | Medium |

### Step 5: Mitigation Mapping

Map threats to privacy design patterns (Hoepman) and GDPR controls:

| Threat Category | Primary Mitigation Pattern | Specific Controls |
|----------------|--------------------------|-------------------|
| Linking | SEPARATE, HIDE (Dissociate) | Purpose-partitioned stores, pseudonymization with separated keys |
| Identifying | HIDE (Encrypt, Hash), ABSTRACT | Field-level encryption, k-anonymity, differential privacy |
| Non-repudiation | HIDE, MINIMIZE | Retention limits on audit logs, aggregated logging |
| Detecting | HIDE (Encrypt), ABSTRACT | Encrypted communications, padding, dummy traffic |
| Data Disclosure | HIDE (Encrypt), ENFORCE | AES-256-GCM encryption, RBAC, security testing |
| Unawareness | INFORM, CONTROL | Layered privacy notices, consent management, DSR portal |
| Non-compliance | ENFORCE, DEMONSTRATE | OPA policies, automated retention, audit trail, DPIA |

## Prism Data Systems AG LINDDUN Assessment Example

**System:** Customer analytics pipeline

**DFD Summary:**
- External Entity: Customer (web/mobile app user)
- Process: API Gateway → Analytics Ingestion Service → Analytics Engine
- Data Store: Transactional DB, Pseudonymized Analytics Warehouse
- Data Flow: Customer actions → API Gateway → Ingestion → Warehouse → Dashboards

**Top 5 Identified Threats:**

| # | Threat | Category | Risk | Mitigation Status |
|---|--------|----------|------|-------------------|
| 1 | Analytics records linked to customer accounts via session correlation | Linking | High | Mitigated: HMAC pseudonymization at ingestion boundary |
| 2 | Re-identification from quasi-identifiers (age, region, device type) | Identifying | High | Mitigated: k-anonymity (k=5) + differential privacy (ε=0.3) |
| 3 | Customer unaware that feature usage is analyzed | Unawareness | Medium | Mitigated: Privacy notice updated, just-in-time notification added |
| 4 | Analytics data retained beyond 13-month policy | Non-compliance | Medium | Mitigated: TTL-based automated deletion deployed |
| 5 | Analytics export to business intelligence tool without access control | Data Disclosure | Medium | Mitigated: OPA purpose-based access control enforced |

## Key Regulatory References

- GDPR Article 25(1) — Data protection by design (LINDDUN as a design-phase assessment)
- GDPR Article 35 — DPIA (LINDDUN provides structured risk identification)
- GDPR Article 32(1) — Security of processing (Data Disclosure threats)
- GDPR Articles 12-14 — Transparency (Unawareness threats)
- GDPR Article 5 — Processing principles (Non-compliance threats)
- Deng, M., Wuyts, K., Scandariato, R., Preneel, B., & Joosen, W. (2011). "A privacy threat analysis framework." Requirements Engineering.
- LINDDUN.org — Official methodology documentation and threat tree catalogs
