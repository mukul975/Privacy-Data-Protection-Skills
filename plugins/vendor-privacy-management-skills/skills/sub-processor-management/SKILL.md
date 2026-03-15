---
name: sub-processor-management
description: >-
  GDPR Article 28(2) sub-processor approval workflow management. Covers prior
  specific and general authorization mechanisms, change notification procedures,
  objection windows, flow-down obligation enforcement, and sub-processor chain
  risk monitoring.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: vendor-privacy-management
  tags: "sub-processor, article-28, flow-down-obligations, vendor-chain, processor-management"
---

# Sub-Processor Management

## Overview

GDPR Article 28(2) establishes that a processor shall not engage another processor (sub-processor) without prior specific or general written authorisation of the controller. Where general authorisation is granted, the processor must inform the controller of any intended changes concerning the addition or replacement of sub-processors, giving the controller the opportunity to object. This creates an ongoing management obligation that extends through the entire processing chain.

The EDPB Guidelines 07/2020 (paragraph 93) emphasize that the controller's Article 28(1) due diligence obligation extends to oversight of sub-processor arrangements, and that the processor remains fully liable for the sub-processor's compliance.

At Summit Cloud Partners, the Sub-Processor Management Program ensures visibility and control over the entire processing chain for all vendor relationships involving personal data.

## Authorization Models

### Model A: Prior Specific Authorization

Under this model, the controller individually approves each sub-processor before engagement.

**When to Use:**
- High-risk processing (special category data, large-scale processing, cross-border transfers)
- Processing involving sensitive industries (healthcare, financial services)
- When the controller requires direct assessment of each sub-processor

**Process:**

| Step | Action | Timeline |
|------|--------|----------|
| 1 | Processor identifies need for new sub-processor | — |
| 2 | Processor submits sub-processor details to controller | Pre-engagement |
| 3 | Controller conducts due diligence on proposed sub-processor | 15 business days |
| 4 | Controller issues written approval or rejection | 5 business days |
| 5 | If approved, processor executes sub-processor DPA | Before processing begins |
| 6 | Processor provides controller with confirmation of sub-processor DPA execution | 5 business days |

### Model B: General Written Authorization with Notification

Under this model, the controller grants blanket authorization for sub-processing, subject to a notification and objection mechanism.

**When to Use:**
- Standard-risk processing
- SaaS vendors with dynamic infrastructure providers
- When specific authorization would be operationally impractical

**Process:**

| Step | Action | Timeline |
|------|--------|----------|
| 1 | Processor notifies controller of intended sub-processor change | 30 days before engagement |
| 2 | Notification includes: name, location, function, data access scope | With notification |
| 3 | Controller evaluates notification and exercises objection right if needed | Within 14 days |
| 4 | If no objection, processor may engage sub-processor | After objection period expires |
| 5 | If objection raised, parties negotiate resolution | Within 30 days |
| 6 | If unresolved, either party may terminate affected services | Per DPA terms |

## Notification Requirements

The EDPB has clarified that the notification mechanism must be genuine and effective — a mere listing on a website that the controller must monitor does not satisfy Article 28(2) without an active notification mechanism.

**Required Notification Content:**

| Field | Description | Example |
|-------|-------------|---------|
| Sub-processor legal name | Full legal entity name | "Datastream Analytics Inc." |
| Jurisdiction | Country of establishment | "United States (Delaware)" |
| Processing location | Where personal data will be processed | "AWS us-east-1, Virginia, USA" |
| Processing function | What the sub-processor will do | "Real-time event processing and aggregation" |
| Data access scope | What personal data the sub-processor accesses | "Pseudonymized usage events, IP addresses" |
| Engagement date | Proposed start date | "2026-05-01" |
| Transfer mechanism | If outside EEA, the legal transfer basis | "EU-US Data Privacy Framework certification" |
| Security certifications | Relevant certifications held | "SOC 2 Type II, ISO 27001" |

**Notification Channels:**
- Email notification to designated controller privacy contact
- Supplement with web-based sub-processor register (not a replacement for active notification)
- Calendar integration for objection deadline tracking

## Objection Mechanism

The controller's right to object must be genuine per EDPB Guidelines 07/2020 (paragraph 115). The DPA must specify:

1. **Objection grounds**: Reasonable data protection concerns (not arbitrary)
2. **Objection period**: Minimum 14 calendar days from notification receipt (Summit Cloud Partners standard: 30 days)
3. **Objection format**: Written notice to processor's designated privacy contact
4. **Resolution process**: Good-faith negotiation within defined timeframe
5. **Escalation**: If unresolved, termination right for affected services without penalty

**Objection Decision Matrix:**

| Concern | Action | Escalation |
|---------|--------|------------|
| Sub-processor in jurisdiction with inadequate protection and no valid transfer mechanism | Object — require alternative sub-processor or supplementary measures | DPO review |
| Sub-processor lacks adequate security certifications | Object — request vendor provide evidence of equivalent controls | Privacy Team review |
| Sub-processor has history of data breaches | Object — require enhanced contractual safeguards or alternative | DPO review |
| Sub-processor change is administrative (name change, corporate restructure) | No objection — acknowledge notification | Privacy Team acknowledgment |
| Sub-processor adds processing location within EEA | Evaluate — generally no objection if controls equivalent | Privacy Team review |

## Flow-Down Obligations

Article 28(4) requires the processor to impose on each sub-processor, by contract, the same data protection obligations as in the controller-processor DPA. The CJEU has not yet directly interpreted the meaning of "same" obligations, but the EDPB position is that they must be materially equivalent.

**Flow-Down Checklist:**

| Obligation | Controller → Processor DPA | Processor → Sub-Processor DPA |
|-----------|--------------------------|-------------------------------|
| Process only on documented instructions | Article 28(3)(a) | Must mirror |
| Confidentiality obligations | Article 28(3)(b) | Must mirror |
| Security measures (Art. 32) | Article 28(3)(c) | Must mirror or exceed |
| Further sub-processing restrictions | Article 28(3)(d) | Must cascade |
| DSR assistance | Article 28(3)(e) | Must mirror |
| Compliance assistance (Art. 32-36) | Article 28(3)(f) | Must mirror |
| Deletion/return on termination | Article 28(3)(g) | Must mirror |
| Audit rights | Article 28(3)(h) | Must provide controller with audit path |
| Breach notification | Article 33(2) | Must cascade with equivalent or shorter timeframe |

**Key Consideration — Audit Rights Chain:**

The controller must ultimately be able to audit the sub-processor. This can be achieved through:
1. Direct audit rights over sub-processor (contractually passed through)
2. Processor audits sub-processor on controller's behalf and shares results
3. Sub-processor provides independent third-party audit reports (SOC 2, ISO 27001)

## Sub-Processor Register

Summit Cloud Partners maintains a centralized sub-processor register for all vendor relationships.

**Register Fields:**

| Field | Description |
|-------|-------------|
| Primary processor | Vendor with direct DPA |
| Sub-processor name | Legal entity name |
| Sub-processor location | Country and specific processing location |
| Processing function | What the sub-processor does |
| Data access scope | Categories of personal data accessed |
| Authorization type | Specific or general authorization |
| Authorization date | Date of approval |
| DPA status | Sub-processor DPA executed / pending |
| Transfer mechanism | If applicable — SCC, adequacy, DPF |
| Certifications | Current certifications |
| Last review date | Most recent assessment |
| Risk classification | High / Standard / Low |

## Monitoring and Compliance

### Ongoing Monitoring Activities

1. **Quarterly sub-processor list reconciliation**: Compare processor-provided lists against register
2. **Certification tracking**: Monitor sub-processor certification expiry dates
3. **Change notification tracking**: Verify all sub-processor changes were properly notified
4. **Annual flow-down verification**: Sample sub-processor DPAs to verify equivalent terms

### Key Performance Indicators

| KPI | Target | Measurement |
|-----|--------|-------------|
| Sub-processor notification compliance | 100% of changes notified before engagement | Quarterly audit |
| Objection response time | 100% within 14 calendar days | Continuous |
| Flow-down DPA coverage | 100% of sub-processors have executed DPAs | Quarterly audit |
| Sub-processor register accuracy | 100% match with processor-provided lists | Quarterly reconciliation |

## Key Regulatory References

- GDPR Article 28(2) — Sub-processor authorization requirements
- GDPR Article 28(3)(d) — Sub-processor conditions in DPA
- GDPR Article 28(4) — Flow-down obligations to sub-processors
- EDPB Guidelines 07/2020 — Controller and processor concepts (paragraphs 93, 115)
- Commission Implementing Decision (EU) 2021/915 — SCC Clause 7.7 on sub-processing
- CJEU C-311/18 (Schrems II) — Transfer assessment obligations extending to sub-processor chain
