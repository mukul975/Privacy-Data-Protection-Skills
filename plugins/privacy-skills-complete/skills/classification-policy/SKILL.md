---
name: classification-policy
description: >-
  Develops data classification policies with tiered handling (public, internal,
  confidential, restricted), labeling requirements, enforcement mechanisms, and
  procedures per tier. Covers policy governance, exception handling, and
  compliance monitoring. Keywords: classification policy, data tiers, handling
  procedures, labeling, enforcement, data governance, information security.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-classification
  tags: "classification-policy, data-tiers, handling-procedures, labeling, enforcement, governance"
---

# Data Classification Policy Development

## Overview

A data classification policy establishes the enterprise-wide framework for categorising data by sensitivity level and prescribing handling requirements per tier. The policy translates GDPR classification obligations (personal, special category, criminal) and information security requirements (confidentiality, integrity, availability) into practical, enforceable rules that govern how data is stored, transmitted, accessed, and disposed of throughout its lifecycle. This skill covers the design, implementation, and enforcement of a four-tier classification scheme aligned with GDPR requirements and ISO 27001 Annex A controls.

## Classification Tier Structure

### Four-Tier Model for Vanguard Financial Services

| Tier | Label | Description | GDPR Mapping | ISO 27001 Mapping |
|------|-------|-------------|-------------|------------------|
| **Tier 1: Public** | PUBLIC | Information approved for public release. Disclosure carries no risk to the organisation or individuals. | Anonymised data (Recital 26), published reports, public filings | A.8.2 — Unclassified/Public |
| **Tier 2: Internal** | INTERNAL | Information for internal use only. Disclosure would cause minor inconvenience but no significant harm. | Pseudonymised aggregate data, internal procedures, organisational charts | A.8.2 — Internal |
| **Tier 3: Confidential** | CONFIDENTIAL | Information whose disclosure would cause significant harm to individuals or the organisation. | Personal data (Art. 4(1)), financial data, customer records, employee records | A.8.2 — Confidential |
| **Tier 4: Restricted** | RESTRICTED | Information whose disclosure would cause severe harm, regulatory sanction, or irreversible damage. | Art. 9 special category data, Art. 10 criminal data, trade secrets, regulatory investigation data | A.8.2 — Restricted/Secret |

### Classification Decision Matrix

| Data Type | Tier | Rationale |
|-----------|------|-----------|
| Published annual report | PUBLIC | Approved for public disclosure |
| Internal org chart | INTERNAL | No individual harm from disclosure, but not intended for external distribution |
| Customer name and email | CONFIDENTIAL | Personal data — disclosure would breach GDPR obligations |
| Customer account number and transactions | CONFIDENTIAL | Personal data with financial sensitivity |
| Employee National Insurance Number | CONFIDENTIAL (borderline RESTRICTED) | High-sensitivity direct identifier |
| Employee health records | RESTRICTED | Art. 9 special category data |
| Biometric access templates | RESTRICTED | Art. 9 biometric data |
| Criminal background check results | RESTRICTED | Art. 10 criminal data |
| AML investigation files | RESTRICTED | Criminal data + legal privilege |
| Board strategic plans | RESTRICTED | Commercial sensitivity |
| Encryption keys and credentials | RESTRICTED | Security-critical |

## Handling Procedures Per Tier

### Tier 1: PUBLIC

| Control | Requirement |
|---------|-------------|
| **Storage** | No restrictions; any approved platform |
| **Transmission** | No restrictions; may be sent via any channel |
| **Access control** | No restrictions; accessible to all |
| **Encryption** | Not required (but recommended for integrity) |
| **Retention** | Per document retention schedule |
| **Disposal** | Standard deletion |
| **Labelling** | Label: "Public" or no label required |

### Tier 2: INTERNAL

| Control | Requirement |
|---------|-------------|
| **Storage** | Vanguard-managed systems only (no personal devices, no personal cloud) |
| **Transmission** | Vanguard email or approved collaboration tools; not via personal email |
| **Access control** | All Vanguard employees and approved contractors with valid account |
| **Encryption** | Required in transit (TLS 1.2+); recommended at rest |
| **Retention** | Per document retention schedule |
| **Disposal** | Standard secure deletion (file system delete) |
| **Labelling** | Label: "Internal" applied via header/footer or metadata |

### Tier 3: CONFIDENTIAL

| Control | Requirement |
|---------|-------------|
| **Storage** | Vanguard-managed systems with access controls; encrypted at rest (AES-256) |
| **Transmission** | Encrypted email (TLS 1.3 or S/MIME); approved SFTP; no unencrypted channels |
| **Access control** | Role-based access control (RBAC); business need-to-know; MFA required |
| **Encryption** | Required at rest (AES-256) and in transit (TLS 1.3); field-level encryption for high-sensitivity fields |
| **Printing** | Permitted with secure print release; printed copies secured in locked cabinets |
| **External sharing** | Permitted only with approved third parties under DPA/NDA; DPO approval for new recipients |
| **Retention** | Per data-specific retention schedule; automated enforcement |
| **Disposal** | Secure overwrite (NIST 800-88 Clear); shredding for physical media |
| **Labelling** | Label: "Confidential" in document header/footer, email subject tag, and metadata |
| **Audit** | Access logged; quarterly review of access permissions |
| **DLP** | DLP policies active: warn on external sharing, block sharing to personal email |

### Tier 4: RESTRICTED

| Control | Requirement |
|---------|-------------|
| **Storage** | Designated restricted-access systems only; encrypted at rest with customer-managed keys; separate network segment or HSM where applicable |
| **Transmission** | End-to-end encrypted channels only; no email without encryption; approved secure file transfer only |
| **Access control** | Named individual access lists (not role-based); dual-person authorisation for bulk access; MFA required; privileged access management (PAM) |
| **Encryption** | AES-256 at rest with customer-managed keys; TLS 1.3 in transit; field-level encryption mandatory |
| **Printing** | Prohibited unless specifically authorised by DPO; watermarked with user identity |
| **External sharing** | Prohibited unless DPO and Chief Privacy Officer jointly approve; encrypted transfer only |
| **Retention** | Strict retention with automated deletion; no extensions without DPO approval |
| **Disposal** | NIST 800-88 Purge (cryptographic erasure or physical destruction); disposal certificate required |
| **Labelling** | Label: "Restricted" in document header/footer (red), email banner, and metadata; visual marking on screens |
| **Audit** | All access logged with user identity, timestamp, and purpose; monthly audit review by DPO |
| **DLP** | DLP policies active: block all external sharing, block USB copy, block print, block screenshot; alert DPO on policy trigger |
| **Incident response** | Any unauthorised access or disclosure treated as data breach; immediate DPO notification |

## Policy Governance

### Policy Document Structure

| Section | Content |
|---------|---------|
| 1. Purpose and Scope | Defines why classification is required and what data is covered |
| 2. Classification Tiers | Four-tier definitions with examples |
| 3. Roles and Responsibilities | Data owner, data steward, DPO, IT Security, all employees |
| 4. Classification Procedures | How to classify new data, reclassification triggers |
| 5. Handling Requirements | Per-tier controls matrix |
| 6. Labelling Requirements | How to apply labels (manual and automated) |
| 7. Exception Process | How to request exceptions with risk acceptance |
| 8. Enforcement | Monitoring, audit, and consequences for violations |
| 9. Training | Classification awareness training requirements |
| 10. Review Schedule | Annual review; interim reviews on regulatory change |

### Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Data Owner** (business unit head) | Classify data for their business function; approve access requests; review classifications annually |
| **Data Steward** (departmental) | Maintain classification labels; ensure handling compliance in their area; report classification issues |
| **DPO** | Oversee policy compliance; approve Restricted tier exceptions; conduct classification audits |
| **IT Security** | Implement technical controls per tier; manage DLP policies; configure encryption; monitor audit logs |
| **All Employees** | Apply classification labels to data they create; handle data per tier requirements; report suspected misclassification |
| **Privacy Engineering** | Configure automated classification tools; manage discovery platforms; tune detection accuracy |

### Exception Process

```
Exception Request
  │
  ├─► Step 1: Requestor documents the exception
  │     - What data? What tier? What control cannot be met?
  │     - Why is the exception needed?
  │     - What alternative controls are proposed?
  │     - Duration of exception requested
  │
  ├─► Step 2: Risk Assessment
  │     - Data Steward assesses the risk of the exception
  │     - For Confidential tier: Data Owner approves
  │     - For Restricted tier: DPO and CISO jointly approve
  │
  ├─► Step 3: Approval and Documentation
  │     - Exception recorded in exception register
  │     - Alternative controls documented and implemented
  │     - Expiry date set (maximum 12 months, renewable)
  │
  └─► Step 4: Review
        - Exception reviewed at expiry
        - Renewed only if original justification remains valid
        - Chronic exceptions trigger process improvement
```

## Enforcement Mechanisms

| Mechanism | Implementation |
|-----------|---------------|
| **Automated labelling** | Microsoft Purview auto-labelling applies Confidential/Restricted labels based on detected PII |
| **DLP policies** | Microsoft Purview DLP blocks or warns on policy violations (external sharing, USB copy) |
| **Access reviews** | Quarterly certification of access permissions for Confidential; monthly for Restricted |
| **Audit logging** | All access to Confidential and Restricted data logged and retained for 2 years |
| **Classification audits** | DPO conducts semi-annual audits sampling 100 items per tier for classification accuracy |
| **Training compliance** | Annual classification training required for all employees; completion tracked in LMS |
| **Disciplinary policy** | Violations escalated per employee handbook: warning → formal warning → disciplinary action |

## Enforcement Precedents

- **ICO v Interserve Group (2022)**: GBP 4.4 million fine for inadequate security measures — the ICO noted that failure to classify data by sensitivity contributed to the inability to apply proportionate security controls, leading to a breach affecting 113,000 employees.
- **CNIL v Sergic (2019)**: EUR 400,000 fine for failing to implement adequate access controls on tenant personal data — absence of data classification meant all data was treated with the same (insufficient) controls.
- **AEPD v CaixaBank (2021)**: EUR 6 million fine — the DPA noted that inadequate data classification contributed to excessive data collection and retention, violating data minimisation and storage limitation principles.

## Integration Points

- **personal-data-test**: Classification policy tiers are assigned based on personal data classification results
- **special-category-data**: Art. 9 data automatically assigned Restricted tier
- **criminal-data-handling**: Art. 10 data automatically assigned Restricted tier
- **data-labeling-system**: Labelling system implements the policy's labelling requirements
- **auto-data-discovery**: Discovery tools validate that classification labels match detected data sensitivity
