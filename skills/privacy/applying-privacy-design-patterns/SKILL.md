---
name: applying-privacy-design-patterns
description: >-
  Systematic application of the eight privacy design patterns per Hoepman: minimize,
  hide, separate, abstract, inform, control, enforce, and demonstrate. Covers pattern
  selection methodology per processing activity, mapping to GDPR principles, and
  practical implementation guidance for privacy-by-design system architecture.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-by-design
  tags: "privacy-design-patterns, hoepman, minimize-hide-separate, privacy-architecture, by-design"
---

# Applying Privacy Design Patterns

## Overview

Privacy design patterns provide reusable architectural solutions for implementing data protection principles in system design. Jaap-Henk Hoepman's framework (2014, expanded in "Privacy Design Strategies: The Eight Strategies for GDPR Compliance") defines eight privacy design strategies organized into two categories: data-oriented strategies (minimize, hide, separate, abstract) that focus on the processing of personal data itself, and process-oriented strategies (inform, control, enforce, demonstrate) that focus on the organizational processes surrounding data processing.

These patterns directly implement GDPR Article 25(1) data protection by design and map to specific GDPR principles under Article 5.

## The Eight Privacy Design Patterns

### Data-Oriented Strategies

#### 1. MINIMIZE

**Principle:** Limit the processing of personal data as much as possible.

**GDPR mapping:** Article 5(1)(c) data minimization, Article 25(2) by default.

**Sub-patterns:**

| Sub-pattern | Description | Implementation |
|------------|-------------|----------------|
| Select before collect | Determine which data is necessary before designing collection interfaces | API allowlists, form field audits |
| Exclude | Remove unnecessary data elements from collection | Schema validation rejecting non-required fields |
| Strip | Remove identifying information as soon as possible after collection | Pseudonymization at ingestion boundary |
| Destroy | Delete data as soon as the purpose is fulfilled | TTL-based automated deletion |

**Prism Data Systems AG Implementation:**
The customer onboarding API at Prism Data Systems AG validates incoming requests against a strict allowlist. The `/api/v2/register` endpoint accepts only `email`, `display_name`, and `country_code`. The `date_of_birth` field is collected only during age verification and is converted to a boolean `is_age_verified` within 24 hours, with the raw date destroyed.

#### 2. HIDE

**Principle:** Protect personal data, or make it unlinkable or unobservable.

**GDPR mapping:** Article 5(1)(f) integrity and confidentiality, Article 32(1)(a) encryption and pseudonymisation.

**Sub-patterns:**

| Sub-pattern | Description | Implementation |
|------------|-------------|----------------|
| Encrypt | Apply cryptographic protection to data at rest and in transit | AES-256-GCM field-level encryption, TLS 1.3 |
| Hash | Replace identifiers with irreversible digests | SHA-256 for log anonymization |
| Mix | Combine data from multiple subjects to prevent singling out | k-anonymity, differential privacy noise |
| Obfuscate | Add noise or perturbation to prevent precise inference | Differential privacy, data masking |
| Dissociate | Break the link between data and identity | Pseudonymization with separated key storage |

**Prism Data Systems AG Implementation:**
All personally identifiable fields are encrypted with per-field AES-256-GCM Data Encryption Keys (DEKs) managed in AWS KMS. Customer identifiers entering the analytics pipeline are pseudonymized via HMAC-SHA256 with keys stored in a Hardware Security Module physically separated from analytics infrastructure.

#### 3. SEPARATE

**Principle:** Process personal data in a distributed fashion, preventing correlation.

**GDPR mapping:** Article 5(1)(b) purpose limitation, Article 25(1) by design.

**Sub-patterns:**

| Sub-pattern | Description | Implementation |
|------------|-------------|----------------|
| Isolate | Process different categories of data in separate systems | Purpose-partitioned databases, microservice isolation |
| Distribute | Spread data across multiple locations to prevent single-point access | Federated learning, SMPC, sharding |

**Prism Data Systems AG Implementation:**
Prism Data Systems AG maintains purpose-partitioned PostgreSQL databases: the authentication database stores only credential-related data, the billing database stores only financial data, and the analytics warehouse stores only pseudonymized event data. No single database contains a complete profile of any customer. Cross-purpose joins require explicit compatibility assessment per Article 6(4).

#### 4. ABSTRACT

**Principle:** Limit the detail of personal data as much as possible.

**GDPR mapping:** Article 5(1)(c) data minimization, Recital 26 anonymization.

**Sub-patterns:**

| Sub-pattern | Description | Implementation |
|------------|-------------|----------------|
| Summarize | Replace detailed data with aggregated summaries | Aggregate reporting with minimum group size 11 |
| Group | Generalize values to broader categories | Age ranges instead of exact ages, region instead of postal code |
| Perturb | Add randomness to exact values | Differential privacy, random rounding |

**Prism Data Systems AG Implementation:**
Customer age is stored as a 5-year bracket (e.g., "25-29") rather than exact date of birth. Geographic data is generalized from full postal code to canton-level. Analytics dashboards enforce a minimum group size of 11 records per cell, with smaller groups suppressed and displayed as "< 11."

### Process-Oriented Strategies

#### 5. INFORM

**Principle:** Inform data subjects about the processing of their personal data.

**GDPR mapping:** Articles 12-14 transparency obligations.

**Sub-patterns:**

| Sub-pattern | Description | Implementation |
|------------|-------------|----------------|
| Supply | Proactively provide privacy information | Layered privacy notices, just-in-time notifications |
| Notify | Alert data subjects about processing events | Email notifications for new data access, breach notifications |
| Explain | Provide meaningful explanations of processing logic | Explainable AI outputs, processing purpose descriptions |

**Prism Data Systems AG Implementation:**
A layered privacy notice is presented at every data collection point. The first layer is a plain-language summary (Flesch-Kincaid grade 8). The second layer provides full Article 13 information. Just-in-time notifications appear when a new feature requires additional data: "To activate bulk export, Prism Data Systems AG needs to process your API usage history."

#### 6. CONTROL

**Principle:** Provide data subjects with control over the processing of their personal data.

**GDPR mapping:** Articles 15-22 data subject rights, Article 7(3) consent withdrawal.

**Sub-patterns:**

| Sub-pattern | Description | Implementation |
|------------|-------------|----------------|
| Consent | Obtain and manage consent for each processing purpose | Granular consent UI with unticked defaults |
| Choose | Allow data subjects to select processing options | Privacy preference center |
| Update | Enable data subjects to correct their data | Self-service profile editing |
| Retract | Enable data subjects to withdraw consent or request erasure | One-click consent withdrawal, erasure request workflow |

**Prism Data Systems AG Implementation:**
The Privacy Preference Center at `account.prism-data.ch/privacy` provides data subjects with granular controls: per-purpose consent toggles, data download (portability), correction interface, and one-click erasure request. Consent withdrawal takes effect within 24 hours and triggers downstream processing cessation.

#### 7. ENFORCE

**Principle:** Commit to processing personal data in a privacy-friendly way, and enforce this.

**GDPR mapping:** Article 24 controller responsibility, Article 25(1) by design, Article 28 processor contracts.

**Sub-patterns:**

| Sub-pattern | Description | Implementation |
|------------|-------------|----------------|
| Create | Define and publish privacy policies and standards | GDPR policy framework, data classification standard |
| Maintain | Regularly update and enforce privacy policies | Quarterly policy reviews, automated compliance checks |
| Uphold | Implement technical enforcement of privacy rules | Purpose-based access control (OPA), automated retention |

**Prism Data Systems AG Implementation:**
Privacy policies are enforced technically through Open Policy Agent (OPA) rules that evaluate every data access request against the purpose registry. The CI/CD pipeline includes a privacy gate that blocks deployment of services failing the data minimization assessment. Processor contracts include standard contractual clauses reviewed semi-annually.

#### 8. DEMONSTRATE

**Principle:** Demonstrate compliance with privacy policies and applicable regulations.

**GDPR mapping:** Article 5(2) accountability, Article 30 records of processing, Article 35 DPIA.

**Sub-patterns:**

| Sub-pattern | Description | Implementation |
|------------|-------------|----------------|
| Record | Maintain comprehensive records of processing activities | Article 30 register, consent logs, DPIA repository |
| Audit | Conduct regular privacy audits | Quarterly internal audits, annual external audit |
| Report | Generate compliance reports for regulators and management | DPO quarterly report, board privacy report |

**Prism Data Systems AG Implementation:**
All data access events are logged in an immutable audit trail with: timestamp, requester identity, purpose declaration, data categories accessed, and authorization decision. The Article 30 register is maintained as a living document updated within 5 business days of any processing change. DPIAs are conducted for all high-risk processing and reviewed annually.

## Pattern Selection Methodology

### Step 1: Map Processing to GDPR Principles

For each processing activity, identify which GDPR principles are most relevant:

| GDPR Principle | Primary Pattern | Supporting Patterns |
|---------------|----------------|-------------------|
| Data minimization (Art. 5(1)(c)) | MINIMIZE | ABSTRACT, HIDE |
| Purpose limitation (Art. 5(1)(b)) | SEPARATE | ENFORCE |
| Storage limitation (Art. 5(1)(e)) | MINIMIZE (Destroy) | ENFORCE |
| Integrity & confidentiality (Art. 5(1)(f)) | HIDE | ENFORCE |
| Transparency (Art. 5(1)(a)) | INFORM | DEMONSTRATE |
| Lawfulness (Art. 5(1)(a)) | CONTROL | ENFORCE |
| Accuracy (Art. 5(1)(d)) | CONTROL (Update) | INFORM |
| Accountability (Art. 5(2)) | DEMONSTRATE | ENFORCE |

### Step 2: Assess Pattern Applicability

Score each pattern's applicability (1-5) for the specific processing activity.

### Step 3: Select and Combine

Select the highest-scoring patterns. Most processing activities require a combination of 3-5 patterns applied at different architectural layers.

## Key Regulatory References

- GDPR Article 5 — Principles relating to processing of personal data
- GDPR Article 25(1) — Data protection by design
- GDPR Article 25(2) — Data protection by default
- EDPB Guidelines 4/2019 on Article 25 Data Protection by Design and by Default
- Hoepman, J.-H. (2014). "Privacy Design Strategies." IFIP SEC. Extended in "Privacy Design Strategies: The Eight Strategies for GDPR Compliance" (2022).
