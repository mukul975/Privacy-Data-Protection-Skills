---
name: vendor-cert-acceptance
description: >-
  Vendor certification acceptance criteria and equivalence mapping. Covers ISO
  27701, SOC 2 Privacy, APEC CBPR, EU Code of Conduct evaluation, certification
  scope analysis, gap supplementation requirements, and cross-framework
  equivalence assessment.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: vendor-privacy-management
  tags: "vendor-certification, iso-27701, soc-2-privacy, apec-cbpr, certification-equivalence"
---

# Vendor Certification Acceptance Criteria

## Overview

GDPR Article 42 establishes a framework for data protection certification mechanisms, and Article 28(5) notes that a processor's adherence to an approved certification mechanism may be used as an element to demonstrate sufficient guarantees. The EDPB Guidelines 07/2020 (paragraph 86) confirm that certifications may serve as indicators of processor reliability, though they do not discharge the controller's obligation to conduct its own assessment.

Vendor certifications and attestations provide structured evidence of control implementation, but their value depends on scope coverage, certification body credibility, recency, and relevance to the specific processing relationship. Summit Cloud Partners maintains a Certification Acceptance Framework that defines which certifications are recognized, how they are evaluated, and what supplementary measures are needed when certification coverage has gaps.

## Recognized Certification Frameworks

### Tier A: Strong Privacy Certifications

Certifications specifically designed for privacy/data protection management, independently audited.

**ISO/IEC 27701:2019 — Privacy Information Management System (PIMS)**

| Aspect | Detail |
|--------|--------|
| **Standard** | Extension to ISO 27001/27002 for PII management |
| **Scope** | PII controller (Annex A) and PII processor (Annex B) controls |
| **Certification body** | Accredited ISO certification bodies |
| **Audit type** | Third-party certification audit (Stage 1 + Stage 2) |
| **Validity** | 3-year cycle with annual surveillance audits |
| **GDPR relevance** | High — maps directly to GDPR requirements per Annex D |
| **Acceptance criteria** | Certificate scope must cover processing services provided to Summit |
| **Verification** | Check accreditation body registry; verify scope statement |
| **Supplementation needed** | Verify that Annex B (processor) controls are in scope; if only Annex A (controller), supplementary processor assessment required |

**GDPR Certification per Article 42**

| Aspect | Detail |
|--------|--------|
| **Standard** | Certification per criteria approved by supervisory authority or EDPB |
| **Certification body** | Accredited per Article 43 by national accreditation body and supervisory authority |
| **GDPR relevance** | Maximum — specifically designed for GDPR compliance demonstration |
| **Acceptance criteria** | Certificate issued by Article 43 accredited body; scope covers processing |
| **Current status** | Very few Article 42 certifications currently available (as of March 2026) |
| **Supplementation needed** | Minimal if scope covers all processing activities |

### Tier B: Strong Security Certifications with Privacy Elements

Certifications primarily security-focused but including privacy-relevant controls.

**SOC 2 Type II with Privacy Trust Services Criterion**

| Aspect | Detail |
|--------|--------|
| **Standard** | AICPA Trust Services Criteria — Privacy criterion |
| **Scope** | Notice, choice, collection, use/retention/disposal, access, disclosure, security, quality, monitoring |
| **Audit type** | Independent CPA examination over minimum 6-month period |
| **GDPR relevance** | Moderate-High — covers many Article 28/32 requirements but US-centric |
| **Acceptance criteria** | Type II (not Type I); Privacy criterion included; no qualified opinions; scope covers relevant services |
| **Verification** | Request full report under NDA; review scope, findings, exceptions |
| **Supplementation needed** | GDPR-specific gap assessment required: cross-border transfer controls, DPA-specific obligations, sub-processor cascade |

**SOC 2 Type II (Security Criterion Only)**

| Aspect | Detail |
|--------|--------|
| **Acceptance criteria** | Type II; no qualified opinions; scope covers relevant services |
| **GDPR relevance** | Moderate — covers Article 32 security measures |
| **Supplementation needed** | Full privacy assessment required for non-security GDPR obligations |

**ISO/IEC 27001:2022 — Information Security Management System**

| Aspect | Detail |
|--------|--------|
| **Acceptance criteria** | Current version (2022 preferred); scope covers processing services; accredited certification body |
| **GDPR relevance** | Moderate — strong for Article 32 security; does not address privacy-specific requirements |
| **Supplementation needed** | Privacy gap assessment covering Art. 28(3) obligations, DSR assistance, breach notification, data handling |

### Tier C: Domain-Specific Certifications

**ISO/IEC 27018:2019 — Cloud Privacy**

| Aspect | Detail |
|--------|--------|
| **Scope** | Cloud-specific PII protection controls |
| **Acceptance** | Relevant only for cloud service providers; supplements ISO 27001 |
| **Supplementation** | Must be combined with ISO 27001; does not stand alone |

**CSA STAR Level 2 — Cloud Security**

| Aspect | Detail |
|--------|--------|
| **Scope** | Cloud Controls Matrix (CCM) third-party audit |
| **Acceptance** | Level 2 (third-party audit) required; Level 1 (self-assessment) insufficient as standalone |
| **Supplementation** | Cloud security focus; privacy gap assessment required |

**APEC Cross-Border Privacy Rules (CBPR) System**

| Aspect | Detail |
|--------|--------|
| **Scope** | Asia-Pacific cross-border data transfer framework |
| **Acceptance** | Recognized for APEC economy vendors; does not substitute for GDPR compliance |
| **GDPR relevance** | Limited — different legal framework; may indicate privacy program maturity |
| **Supplementation** | Full GDPR compliance assessment still required |

**EU Cloud Code of Conduct (SCOPE Europe)**

| Aspect | Detail |
|--------|--------|
| **Standard** | GDPR Article 40 approved code of conduct for cloud services |
| **Scope** | Cloud service provider GDPR compliance |
| **Acceptance** | Approved by Belgian DPA as monitoring body (2021) |
| **GDPR relevance** | High — specifically mapped to GDPR obligations |
| **Supplementation** | Minimal for in-scope cloud processing; verify monitoring body oversight |

### Tier D: Self-Assessments and Basic Certifications

| Certification | Acceptance Level |
|--------------|-----------------|
| CSA STAR Level 1 (self-assessment) | Accepted as supplementary evidence only; not standalone |
| Vendor privacy policy / self-declaration | Not accepted as certification; supplementary only |
| HITRUST CSF | Accepted for healthcare contexts; GDPR gap assessment required |
| Cyber Essentials (UK) | Basic security only; full assessment required |

## Certification Equivalence Matrix

Maps certification coverage against GDPR Article 28 requirements:

| GDPR Requirement | ISO 27701 | SOC 2 Privacy | SOC 2 Security | ISO 27001 | ISO 27018 | Art. 42 Cert |
|------------------|:---------:|:-------------:|:--------------:|:---------:|:---------:|:------------:|
| Art. 28(3)(a) Documented instructions | Full | Partial | None | None | Full | Full |
| Art. 28(3)(b) Confidentiality | Full | Full | Partial | Full | Full | Full |
| Art. 28(3)(c) Security (Art. 32) | Full | Full | Full | Full | Full | Full |
| Art. 28(3)(d) Sub-processor mgmt | Full | Partial | None | Partial | Full | Full |
| Art. 28(3)(e) DSR assistance | Full | Partial | None | None | Partial | Full |
| Art. 28(3)(f) Compliance assistance | Full | Partial | None | None | None | Full |
| Art. 28(3)(g) Deletion/return | Full | Full | None | Partial | Full | Full |
| Art. 28(3)(h) Audit rights | Full | Partial | None | Partial | Full | Full |
| Art. 33(2) Breach notification | Full | Full | Partial | Partial | Partial | Full |
| Ch. V International transfers | Partial | None | None | None | None | Full |

**Legend:** Full = requirement addressed, Partial = partially addressed, None = not addressed

## Gap Supplementation Requirements

When a vendor holds certifications that do not fully cover GDPR requirements, Summit Cloud Partners requires supplementary evidence for uncovered obligations:

| Gap | Supplementation Method |
|-----|----------------------|
| DSR assistance capability | Vendor provides DSR handling procedure documentation and SLA commitments |
| Sub-processor management | Vendor provides sub-processor list, notification mechanism, and flow-down DPA sample |
| Breach notification process | Vendor provides incident response plan with notification timeframes |
| International transfer controls | Vendor provides Transfer Impact Assessment and supplementary measures documentation |
| Deletion/return capabilities | Vendor demonstrates deletion procedure and provides sample deletion certificate |
| Audit facilitation | DPA audit rights clause verified; vendor confirms practical audit access |

## Certification Verification Process

| Step | Activity | Evidence |
|------|----------|---------|
| 1 | Obtain copy of certificate and audit report | PDF certificate; SOC 2 report under NDA |
| 2 | Verify certification body accreditation | Check national accreditation body registry |
| 3 | Verify certificate validity (not expired) | Certificate dates; annual surveillance confirmation |
| 4 | Verify scope covers relevant services | Scope statement includes services provided to Summit |
| 5 | Review exceptions or qualified opinions (SOC 2) | No material exceptions affecting Summit data |
| 6 | Identify gaps per equivalence matrix | Document uncovered requirements |
| 7 | Request supplementary evidence for gaps | Per gap supplementation table |
| 8 | Document acceptance decision | Record in vendor assessment file |

## Key Regulatory References

- GDPR Article 42 — Data protection certification mechanisms
- GDPR Article 43 — Certification bodies
- GDPR Article 40 — Codes of conduct
- GDPR Article 28(5) — Adherence to certifications as element of sufficient guarantees
- EDPB Guidelines 07/2020 — Paragraph 86 on certifications as sufficiency indicators
- EDPB Guidelines 1/2018 — Certification and identifying certification criteria per Article 42
- ISO/IEC 27701:2019 — Privacy information management system
- AICPA Trust Services Criteria — Privacy criterion (2017 revision with 2022 updates)
- APEC Cross-Border Privacy Rules System — Policies, Rules, and Guidelines
- EU Cloud Code of Conduct — SCOPE Europe (approved 2021)
