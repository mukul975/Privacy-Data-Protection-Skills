---
name: preparing-iso-31700-certification
description: >-
  Preparation guide for ISO 31700 privacy by design for consumer goods certification.
  Covers the 30 requirements across design, production, and disposal phases. Includes
  gap assessment methodology, remediation planning, and mapping to GDPR Article 25
  data protection by design obligations for consumer-facing products and services.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-by-design
  tags: "iso-31700, privacy-by-design, certification, consumer-goods, gap-assessment"
---

# Preparing ISO 31700 Certification

## Overview

ISO 31700:2023 "Consumer protection — Privacy by design for consumer goods and services" is the first international standard specifically dedicated to privacy by design. Published in February 2023, it provides 30 requirements organized across three lifecycle phases: design, production/deployment, and end-of-life/disposal.

ISO 31700 operationalizes the privacy by design concept originally proposed by Ann Cavoukian and codified in GDPR Article 25(1). While Article 25 establishes the legal obligation, ISO 31700 provides a certifiable framework for demonstrating compliance through structured requirements across the entire product lifecycle.

## ISO 31700 Structure

### Part 1: High-Level Requirements (ISO 31700-1:2023)

30 requirements organized into three lifecycle phases.

### Part 2: Use Cases (ISO 31700-2:2023)

Practical use cases illustrating application of Part 1 requirements across industries including e-commerce, IoT devices, mobile applications, and cloud services.

## The 30 Requirements

### Phase 1: Design (Requirements 1-16)

| Req # | Title | Summary | GDPR Mapping |
|-------|-------|---------|-------------|
| 1 | Designing privacy controls | Consumer goods shall include privacy controls that enable consumers to manage collection, use, and disclosure of their PII | Art. 25(1), Art. 25(2) |
| 2 | Privacy notice and consent | Privacy information shall be communicated to consumers in a clear and understandable manner | Art. 12-14 |
| 3 | Consumer PII collection | PII collection shall be limited to what is necessary and proportionate | Art. 5(1)(c) |
| 4 | Creating and managing consumer PII | Processes shall be established for the creation, maintenance, and deletion of PII | Art. 5(1)(d), Art. 5(1)(e) |
| 5 | Consumer PII use limitation | PII shall be processed only for specified, explicit, and legitimate purposes | Art. 5(1)(b) |
| 6 | Consumer PII disclosure to third parties | PII disclosure to third parties shall be limited and controlled | Art. 28, Art. 44-49 |
| 7 | Consumer PII quality | Measures shall ensure accuracy and currency of PII | Art. 5(1)(d) |
| 8 | Consumer PII security | Appropriate security measures shall protect PII | Art. 32 |
| 9 | Consumer PII retention | PII shall not be retained longer than necessary | Art. 5(1)(e) |
| 10 | Organizational commitment | Management shall commit resources and oversight for privacy | Art. 24 |
| 11 | Privacy risk assessment | Privacy risks shall be identified, assessed, and treated | Art. 35 |
| 12 | Designing PII processing rights | Consumer rights to access, correct, delete, and port their PII shall be built into the design | Art. 15-20 |
| 13 | Designing ergonomic privacy controls | Privacy controls shall be usable and accessible to consumers | Art. 25(2) |
| 14 | Designing privacy for vulnerable consumers | Design shall consider the needs of children, elderly, and other vulnerable populations | Art. 8, Recital 38 |
| 15 | Supply chain management | Privacy requirements shall be imposed on suppliers and sub-processors | Art. 28 |
| 16 | Designing for disposal | Design shall include mechanisms for PII deletion at end of product life | Art. 17 |

### Phase 2: Production and Deployment (Requirements 17-24)

| Req # | Title | Summary | GDPR Mapping |
|-------|-------|---------|-------------|
| 17 | Privacy awareness and training | Personnel shall receive privacy training appropriate to their role | Art. 39(1)(b) |
| 18 | Privacy operations | Operational procedures shall implement designed privacy controls | Art. 24, Art. 25(1) |
| 19 | Privacy breach management | Incident response procedures for privacy breaches shall be established | Art. 33, Art. 34 |
| 20 | Communication with consumers | Channels for consumer privacy inquiries and complaints shall be maintained | Art. 12(2) |
| 21 | Third-party management | Third parties processing PII shall be managed and monitored | Art. 28 |
| 22 | Consumer PII use | PII processing in production shall align with designed purposes and controls | Art. 5(1)(b) |
| 23 | Managing privacy inquiries and complaints | Consumer inquiries and complaints shall be handled within specified timeframes | Art. 12(3) |
| 24 | Privacy performance monitoring | Privacy controls shall be monitored for effectiveness | Art. 24(1) |

### Phase 3: End-of-Life and Disposal (Requirements 25-30)

| Req # | Title | Summary | GDPR Mapping |
|-------|-------|---------|-------------|
| 25 | End-of-life PII management | PII shall be managed when a product reaches end of life | Art. 17 |
| 26 | Consumer notification of disposal | Consumers shall be informed about PII handling during disposal | Art. 13 |
| 27 | PII disposal | PII shall be securely deleted or anonymized at end of life | Art. 5(1)(e), Art. 17 |
| 28 | Data portability at end of life | Consumers shall be able to retrieve their data before disposal | Art. 20 |
| 29 | Supply chain disposal | Suppliers and sub-processors shall delete PII upon product disposal | Art. 28(3)(g) |
| 30 | Disposal documentation | Disposal activities shall be documented and verifiable | Art. 5(2) |

## Gap Assessment Methodology

### Assessment Scoring

For each of the 30 requirements, assess the current state:

| Score | Level | Description |
|-------|-------|-------------|
| 0 | Non-existent | No awareness of the requirement |
| 1 | Initial | Awareness exists but no formal implementation |
| 2 | Developing | Partial implementation, ad hoc processes |
| 3 | Defined | Formal processes documented and communicated |
| 4 | Managed | Processes monitored, measured, and consistently applied |
| 5 | Optimizing | Continuous improvement based on metrics and feedback |

**Certification readiness:** All requirements must be at Level 3 or above. Level 4 or above is recommended for high-risk processing.

### Gap Assessment Process

1. **Document current state** — For each requirement, document what controls, processes, and evidence currently exist.
2. **Score maturity** — Apply the 0-5 scoring scale based on documented evidence.
3. **Identify gaps** — Requirements scoring below 3 are certification gaps.
4. **Prioritize remediation** — Rank gaps by: risk impact (high-risk processing first), dependency (foundational requirements first), and effort.
5. **Create remediation plan** — Define specific actions, responsible parties, and target dates for each gap.
6. **Execute and verify** — Implement remediations and verify through evidence collection.
7. **Pre-certification audit** — Conduct internal audit using ISO 31700 checklist before engaging certification body.

## Prism Data Systems AG Gap Assessment Summary

| Phase | Requirements | Avg Score | Gaps (< 3) | Critical Gaps (< 2) |
|-------|-------------|-----------|------------|---------------------|
| Design (1-16) | 16 | 3.8 | 2 | 0 |
| Production (17-24) | 8 | 3.5 | 1 | 0 |
| Disposal (25-30) | 6 | 2.7 | 3 | 1 |
| **Total** | **30** | **3.4** | **6** | **1** |

**Critical gap:** Requirement 27 (PII disposal) scored 1 — while Prism Data Systems AG has automated deletion for database records, physical media disposal procedures for decommissioned hardware lack documented verification.

## Remediation Roadmap

| Priority | Req # | Gap Description | Remediation Action | Owner | Target |
|----------|-------|----------------|-------------------|-------|--------|
| 1 | 27 | Physical media disposal lacks verification | Implement NIST SP 800-88 media sanitization with certificate of destruction | IT Operations | 2026-05-01 |
| 2 | 25 | End-of-life PII management incomplete | Define end-of-life procedures for each product line; assign lifecycle owners | Product Management | 2026-05-15 |
| 3 | 29 | Supplier disposal obligations not enforced | Add disposal audit clause to supplier contracts; annual verification | Procurement | 2026-06-01 |
| 4 | 14 | Vulnerable consumer design considerations informal | Document accessibility and child safety review as design stage gate | UX Engineering | 2026-06-15 |
| 5 | 16 | Disposal design mechanisms incomplete | Add data wipe functionality to all IoT device firmware | Firmware Engineering | 2026-07-01 |
| 6 | 24 | Privacy monitoring metrics not formalized | Define KPIs for each privacy control; implement dashboard | Privacy Engineering | 2026-06-01 |

## Implementation Workflow

1. **Executive sponsorship** — Secure management commitment (Requirement 10) with budget allocation and executive sponsor assignment.

2. **Gap assessment** — Conduct full assessment of all 30 requirements using the scoring methodology above.

3. **Remediation planning** — Create prioritized remediation roadmap addressing all gaps below Level 3.

4. **Implementation** — Execute remediations in priority order, documenting evidence of implementation for each requirement.

5. **Internal audit** — Conduct pre-certification internal audit using the ISO 31700 checklist to verify all requirements are at Level 3+.

6. **Certification body engagement** — Select an accredited certification body and schedule the Stage 1 (documentation review) and Stage 2 (implementation audit) assessments.

7. **Continuous improvement** — After certification, maintain a continuous improvement cycle with annual surveillance audits and periodic internal reviews.

## Key Regulatory References

- ISO 31700-1:2023 — Consumer protection — Privacy by design for consumer goods and services — Part 1: High-level requirements
- ISO 31700-2:2023 — Part 2: Use cases
- GDPR Article 25 — Data protection by design and by default
- GDPR Article 42 — Certification
- GDPR Article 43 — Certification bodies
- EDPB Guidelines 4/2019 on Article 25 Data Protection by Design and by Default
- NIST SP 800-88 Rev. 1 — Guidelines for Media Sanitization
