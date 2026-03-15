---
name: vendor-privacy-audit
description: >-
  On-site and remote vendor audit procedures per GDPR Article 28(3)(h). Covers
  audit planning, evidence collection methodologies, finding classification,
  remediation tracking, and audit report generation for processor compliance
  verification.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: vendor-privacy-management
  tags: "vendor-audit, article-28-audit, processor-compliance, audit-rights, remediation-tracking"
---

# Vendor Privacy Audit

## Overview

GDPR Article 28(3)(h) requires that the processor "make available to the controller all information necessary to demonstrate compliance with the obligations laid down in Article 28, and allow for and contribute to audits, including inspections, conducted by the controller or another auditor mandated by the controller." This audit right is a cornerstone of the controller's accountability obligations and must be exercisable in practice.

The EDPB Guidelines 07/2020 (paragraph 110) emphasize that audit rights must be practical and exercisable, not merely theoretical. Controllers must develop structured audit programs proportionate to the risk of the processing.

At Summit Cloud Partners, the Vendor Privacy Audit Program provides a systematic approach to verifying processor compliance through on-site inspections, remote audits, and documentation reviews.

## Audit Types

### Type 1: Documentation-Based Audit (Remote)

Suitable for standard-risk vendors with current third-party certifications.

| Aspect | Detail |
|--------|--------|
| **Scope** | Review of processor-provided documentation and certifications |
| **Duration** | 3-5 business days |
| **Frequency** | Annual |
| **Deliverable** | Documentation Audit Report |
| **Cost allocation** | Controller bears own costs |

**Evidence Reviewed:**
- Current ISO 27001/27701 certificates and audit reports
- SOC 2 Type II report (including management assertions and exceptions)
- DPA compliance self-assessment questionnaire
- Sub-processor register and DPA coverage confirmation
- Incident log summary for audit period
- Training records and confidentiality agreement coverage
- Data subject request handling metrics

### Type 2: Remote Technical Audit

Suitable for standard-to-high-risk vendors where on-site access is not practical.

| Aspect | Detail |
|--------|--------|
| **Scope** | Remote assessment including technical verification |
| **Duration** | 5-10 business days |
| **Frequency** | Annual for high-risk; biennial for standard-risk |
| **Deliverable** | Remote Audit Report |
| **Cost allocation** | Per DPA terms (typically split) |

**Activities:**
- All documentation review activities from Type 1
- Video-conference interviews with vendor privacy and security teams
- Screen-sharing walkthrough of access control configurations
- Review of logging and monitoring dashboards
- Live demonstration of data subject request handling process
- Review of encryption key management procedures
- Penetration test report review (vendor-provided under NDA)

### Type 3: On-Site Inspection

Required for high-risk vendors and when triggered by compliance concerns.

| Aspect | Detail |
|--------|--------|
| **Scope** | Physical inspection of processing facilities and controls |
| **Duration** | 1-3 days on-site, plus pre/post work |
| **Frequency** | As needed; minimum biennial for highest-risk vendors |
| **Deliverable** | On-Site Inspection Report |
| **Cost allocation** | Per DPA terms |

**Activities:**
- All remote audit activities
- Physical security inspection of data processing facilities
- Server room and network infrastructure walkthrough
- Badge access system review and testing
- Clean desk policy verification
- Environmental controls inspection (fire suppression, climate, power)
- Personnel interviews (privacy officer, security team, operations staff)
- Observation of operational procedures (incident response, change management)

## Audit Planning

### Pre-Audit Activities

**60 Days Before Audit:**

| Activity | Responsible |
|----------|-------------|
| Select vendors for audit based on risk tier and schedule | Privacy Team |
| Determine audit type (Documentation / Remote / On-Site) | Privacy Team Lead |
| Assign audit team lead and members | Privacy Team Lead |
| Notify vendor of audit intent per DPA notification requirements | Audit Team Lead |

**30 Days Before Audit:**

| Activity | Responsible |
|----------|-------------|
| Issue formal audit notification letter to vendor | Audit Team Lead |
| Submit document request list to vendor | Audit Team |
| Schedule interview slots (for Type 2 and 3) | Audit Team |
| Book travel and facilities (for Type 3) | Operations |
| Prepare audit checklist customized for vendor's processing | Audit Team |

**7 Days Before Audit:**

| Activity | Responsible |
|----------|-------------|
| Review vendor-provided documentation | Audit Team |
| Prepare interview question sets | Audit Team |
| Finalize on-site agenda (Type 3) | Audit Team Lead |
| Conduct team briefing | Audit Team Lead |

### Audit Checklist

**A. DPA Compliance Verification**

| # | Check Item | Article | Evidence Required |
|---|-----------|---------|-------------------|
| A1 | Processing limited to documented controller instructions | 28(3)(a) | Processing logs, instruction register |
| A2 | All authorized personnel bound by confidentiality | 28(3)(b) | Signed confidentiality agreements, HR records |
| A3 | Article 32 security measures implemented per DPA Annex II | 28(3)(c) | Security configuration evidence |
| A4 | Sub-processors authorized and DPAs in place | 28(3)(d) | Sub-processor register, executed DPAs |
| A5 | DSR assistance capability demonstrated | 28(3)(e) | DSR handling procedures, response metrics |
| A6 | Compliance assistance provided for Art. 32-36 | 28(3)(f) | DPIA contributions, breach investigation support |
| A7 | Deletion/return capabilities verified | 28(3)(g) | Deletion procedures, test results |
| A8 | Audit information and access provided | 28(3)(h) | Audit cooperation evidence |

**B. Technical Controls Verification**

| # | Check Item | Evidence Required |
|---|-----------|-------------------|
| B1 | Encryption at rest implemented per DPA specifications | Key management documentation, configuration screenshots |
| B2 | Encryption in transit per DPA specifications | TLS configuration, certificate management |
| B3 | Access controls configured per principle of least privilege | RBAC configuration, access review records |
| B4 | MFA enabled for all administrative access | MFA enrollment records, policy configuration |
| B5 | Logging enabled and retained per DPA retention period | Log storage configuration, sample logs |
| B6 | Vulnerability scanning performed per schedule | Scan reports, remediation records |
| B7 | Penetration testing performed per schedule | Pen test reports, finding remediation |
| B8 | Backup and recovery procedures tested | DR test results, RPO/RTO metrics |

**C. Organizational Controls Verification**

| # | Check Item | Evidence Required |
|---|-----------|-------------------|
| C1 | Privacy training delivered to all relevant staff | Training records with completion dates |
| C2 | Incident response plan documented and tested | IRP document, tabletop exercise records |
| C3 | Change management process followed | Change log, approval records |
| C4 | Physical security controls in place (Type 3 only) | Badge access logs, CCTV coverage, visitor log |
| C5 | Data retention and deletion procedures operational | Retention schedule, deletion logs |
| C6 | Records of processing maintained per Art. 30(2) | ROPA documentation |

**D. Breach Notification Readiness**

| # | Check Item | Evidence Required |
|---|-----------|-------------------|
| D1 | Breach detection capabilities operational | SIEM configuration, alert rules |
| D2 | Breach notification procedure documented with DPA-compliant timeframe | IRP with notification section, contact matrix |
| D3 | Breach notification contact details current | Verified contact information |
| D4 | Breach register maintained | Breach log (redacted if necessary) |

## Finding Classification

| Severity | Definition | Remediation Timeline | Follow-Up |
|----------|-----------|---------------------|-----------|
| **Critical** | Immediate risk to personal data or fundamental DPA violation | Immediate (within 7 days) | Verification audit within 30 days |
| **Major** | Significant gap in controls or DPA non-compliance | 30 calendar days | Written evidence of remediation |
| **Minor** | Control weakness not immediately impacting data protection | 90 calendar days | Verified at next scheduled audit |
| **Observation** | Area for improvement, not a compliance gap | Noted for next assessment | Tracked in audit records |

**Examples by Severity:**

| Severity | Example |
|----------|---------|
| Critical | Personal data accessible to unauthorized personnel; no encryption at rest despite DPA requirement |
| Major | Sub-processor engaged without notification; MFA not enforced for administrative access |
| Minor | Privacy training completion at 85% (target 100%); access review 2 weeks overdue |
| Observation | Incident response plan would benefit from more specific processor notification procedures |

## Remediation Tracking

All findings above Observation severity enter the remediation tracking system:

| Field | Description |
|-------|-------------|
| Finding ID | Unique identifier |
| Vendor | Processor name |
| Audit date | When finding was identified |
| Severity | Critical / Major / Minor |
| Description | Detailed description of the finding |
| Root cause | Why the gap exists |
| Remediation plan | Vendor's proposed corrective action |
| Deadline | Date by which remediation must be complete |
| Evidence required | What the vendor must provide to close the finding |
| Status | Open / In Progress / Remediated / Verified / Overdue |
| Verification method | How Summit Cloud Partners will verify remediation |

## Key Regulatory References

- GDPR Article 28(3)(h) — Audit rights and compliance information
- GDPR Article 5(2) — Accountability principle
- GDPR Article 24 — Responsibility of the controller
- GDPR Article 32 — Security of processing
- EDPB Guidelines 07/2020 — Controller and processor concepts (paragraph 110 on practical audit rights)
- Bavarian DPA (BayLDA) — Processor Audit Guidelines (2022)
- ISO 19011:2018 — Guidelines for auditing management systems
