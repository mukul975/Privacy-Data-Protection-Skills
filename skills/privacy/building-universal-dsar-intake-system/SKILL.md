---
name: building-universal-dsar-intake-system
description: >-
  Builds a multi-channel DSAR intake system supporting web form, email, phone,
  and in-person requests with identity verification tiers, automated routing
  logic, SLA tracking, and response generation. Activate for DSAR intake,
  rights request portal, multi-channel intake, SLA tracking, request management queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-subject-rights
  tags: "dsar-intake, multi-channel, identity-verification, sla-tracking, request-management"
---

# Building a Universal DSAR Intake System

## Overview

A universal DSAR intake system centralises the receipt, verification, routing, and tracking of all data subject rights requests across multiple channels. This skill provides the architectural design, identity verification framework, routing logic, SLA management, and response generation capabilities needed to operate a compliant and efficient rights request management programme.

## System Architecture

### Multi-Channel Intake

The intake system must accept requests from all channels through which data subjects may contact the organisation:

| Channel | Intake Method | Processing |
|---------|--------------|------------|
| Web form | Dedicated privacy rights portal at meridiananalytics.co.uk/privacy/rights | Automated capture, structured data, immediate acknowledgement |
| Email | dsar@meridiananalytics.co.uk (dedicated monitored inbox) | Semi-automated: email parser extracts key fields, manual triage |
| Telephone | Privacy hotline: +44 20 7946 0958 (staffed Mon-Fri 09:00-17:00 GMT) | Agent-assisted: agent completes intake form during call |
| Postal mail | Data Protection Office, 47 Canary Wharf Tower, London E14 5AB | Manual: scanned, digitised, entered into system within 2 business days |
| In-person | Reception desk at registered office | Agent-assisted: staff member completes intake form |
| Social media | Direct messages on official channels | Redirect to formal channel; do not process rights requests via social media |

### Central Request Register

All requests from all channels feed into a single central register with the following record structure:

| Field | Description |
|-------|-------------|
| Reference | Auto-generated: [TYPE]-YYYY-NNNN (e.g., DSAR-2026-0142) |
| Receipt date | UTC timestamp of initial receipt |
| Channel | Source channel |
| Request type | Access (Art. 15), Erasure (Art. 17), Portability (Art. 20), Restriction (Art. 18), Rectification (Art. 16), Object (Art. 21), Marketing opt-out (Art. 21(2)), Automated decision (Art. 22), CCPA know, CCPA delete, CCPA opt-out |
| Data subject name | As provided by requester |
| Data subject identifiers | Email, account number, other identifiers provided |
| Verification status | Pending / Verified / Failed |
| Verification tier | Low / Medium / High |
| Assignee | Privacy team member responsible |
| Priority | Standard / Complex / Urgent |
| Status | Received / Acknowledged / Verifying / Processing / QA Review / Delivered / Closed |
| Deadline | Calculated response deadline |
| Extension | Whether extension has been applied |
| Notes | Free text for processing notes |

## Identity Verification Framework

### Tiered Verification

| Tier | When Applied | Requirements | Clock Behaviour |
|------|-------------|--------------|-----------------|
| **Tier 1 — Low Risk** | Request from authenticated account (logged-in portal, verified email) | Confirm account ownership via existing authentication | Clock starts immediately |
| **Tier 2 — Medium Risk** | Request from known email address (matches records) but not authenticated | Provide 2 of: date of birth, account number, postal code, last 4 digits of payment method | Clock starts on verification |
| **Tier 3 — High Risk** | Request from unknown channel, or request on behalf of another person | Government-issued photo ID + one additional identifier. Third-party requests: signed authorisation from data subject + ID for both | Clock starts on verification |

### Verification Workflow

```
[Request Received]
         │
         ▼
[Determine Verification Tier]
   │
   ├── Authenticated channel? ──► Tier 1 (auto-verified)
   ├── Known identifier matches? ──► Tier 2 (request 2 data points)
   └── Unknown channel / third party? ──► Tier 3 (request ID + authorisation)
         │
         ▼
[Verification Request Sent (within 3 business days)]
         │
         ▼
[Verification Response Received?]
   ├── Yes ──► [Data Points Match?]
   │             ├── Yes ──► Mark Verified, start clock
   │             └── No ──► Request additional info (one retry)
   │                          ├── Second attempt matches ──► Verified
   │                          └── Second attempt fails ──► Close as Unverified
   │
   └── No response (30 days) ──► Close as Abandoned
```

## Routing Logic

### Automated Request Classification

Upon intake, the system classifies and routes requests based on:

1. **Request type** (extracted from web form selection or email keywords):
   - Access/DSAR → DSAR team
   - Erasure/Deletion → Erasure team
   - Portability/Export → Portability team
   - Marketing opt-out → Marketing Operations (immediate processing)
   - CCPA requests → US Privacy team
   - Regulatory complaint → DPO + Legal

2. **Complexity assessment**:
   - Standard: single request type, single jurisdiction, < 5 data systems
   - Complex: multiple request types, cross-border, > 5 data systems, or involving exemptions
   - Urgent: regulatory enquiry, legal deadline, or data subject facing imminent harm

3. **Jurisdiction detection**:
   - UK/EU data subject → GDPR workflow (30-day deadline)
   - California resident → CCPA workflow (45-day deadline)
   - Other US state → Applicable state privacy law workflow
   - Other jurisdiction → Assess applicable law, default to GDPR standard

### Routing Matrix

| Request Type | Assignee | Priority | SLA |
|-------------|----------|----------|-----|
| DSAR (Art. 15) — Standard | Privacy Analyst | Standard | 30 days |
| DSAR (Art. 15) — Complex | Senior Privacy Analyst | Complex | 30 days (extendable to 90) |
| Erasure (Art. 17) | Privacy Analyst | Standard | 30 days |
| Portability (Art. 20) | Data Engineer + Privacy Analyst | Standard | 30 days |
| Rectification (Art. 16) | Privacy Analyst | Standard | 30 days |
| Restriction (Art. 18) | Senior Privacy Analyst | Standard | 30 days + 72h implementation |
| Object (Art. 21) | DPO | Complex | 30 days + immediate cessation |
| Marketing opt-out (Art. 21(2)) | Marketing Operations | Urgent | 24 hours |
| Automated decision (Art. 22) | DPO + Technical Lead | Complex | 30 days |
| CCPA Know | Privacy Analyst | Standard | 45 days |
| CCPA Delete | Privacy Analyst | Standard | 45 days |
| CCPA Opt-Out | Marketing Operations | Urgent | 15 business days |
| Regulatory complaint | DPO + General Counsel | Urgent | Per DPA deadline |

## SLA Tracking

### Dashboard Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Acknowledgement within 3 business days | 100% | (Acknowledged requests / Total requests) within 3 business days |
| Response within statutory deadline | 100% | (On-time responses / Total responses) |
| Average response time | < 20 calendar days | Sum of response days / Number of completed requests |
| Verification completion rate | > 95% | (Verified requests / Total requests requiring verification) |
| Extension rate | < 15% | (Extended requests / Total requests) |
| First-contact resolution (marketing opt-out) | 100% within 24h | (Resolved within 24h / Total marketing opt-outs) |

### Escalation Rules

| Condition | Escalation |
|-----------|-----------|
| 20 days elapsed, response not delivered | Alert to assignee and team lead |
| 25 days elapsed, response not delivered | Alert to DPO |
| 28 days elapsed, response not delivered | Alert to DPO + General Counsel (emergency priority) |
| Extension notification not sent by day 28 | Alert to DPO (compliance risk) |
| Verification pending > 14 days | Alert to assignee (follow up with data subject) |

## Response Generation

### Automated Response Components

The system generates responses by assembling modular components:

1. **Cover letter**: Standard header, addressee, reference number, opening paragraph.
2. **Right-specific content**: Template paragraph for each right type.
3. **Data compilation**: System-generated data extract (for access requests).
4. **Supplementary information**: Art. 15(1)(a)-(h) information block (for access requests).
5. **Redaction log**: Automatically generated from redaction flags (for access requests with exemptions).
6. **Third-party notification log**: Recipients notified under Art. 19 (for erasure/rectification/restriction).
7. **Rights information**: Standard block listing the data subject's other rights and complaint mechanisms.
8. **Sign-off**: DPO name and contact details.

### Quality Assurance Checklist

Before any response is sent, the QA reviewer verifies:

- [ ] Response addresses all elements of the relevant GDPR article
- [ ] Data extract is complete (all identified systems queried)
- [ ] Redactions are legally justified and documented
- [ ] Response deadline has been met (or extension properly communicated)
- [ ] Response is in clear, plain language per Art. 12
- [ ] Delivery method is secure (encryption, secure portal, or registered post)
- [ ] DPO sign-off obtained
